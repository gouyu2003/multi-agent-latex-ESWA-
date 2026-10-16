from __future__ import annotations
from project_paths import project_path

import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = project_path("audit_work")
USER_AGENT = "ESWA-reference-audit/1.0 (mailto:literature.audit@example.com)"


def clean_tex(value: str) -> str:
    value = re.sub(r"\\(?:textit|textbf|emph|url)\{([^{}]*)\}", r"\1", value)
    value = value.replace("{", "").replace("}", "")
    value = re.sub(r"\\['\"`^~=vcH]\s*([A-Za-z])", r"\1", value)
    value = value.replace("\\&", "&")
    return value


def normalise(value: str) -> str:
    value = unicodedata.normalize("NFKD", clean_tex(value)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def similarity(a: str, b: str) -> float:
    na, nb = normalise(a), normalise(b)
    if not na or not nb:
        return 0.0
    seq = SequenceMatcher(None, na, nb).ratio()
    ta, tb = set(na.split()), set(nb.split())
    jac = len(ta & tb) / max(1, len(ta | tb))
    containment = len(ta & tb) / max(1, min(len(ta), len(tb)))
    return round(max(seq, 0.55 * jac + 0.45 * containment), 4)


def get_json(url: str, retries: int = 3) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError("unreachable")


def crossref_candidates(item: dict) -> list[dict]:
    query = urllib.parse.urlencode(
        {
            "query.bibliographic": f"{clean_tex(item['title'])} {clean_tex(item['author']).split(' and ')[0]}",
            "rows": 5,
            "select": "DOI,title,author,published-print,published-online,issued,container-title,volume,issue,page,type,URL",
            "mailto": "literature.audit@example.com",
        }
    )
    data = get_json("https://api.crossref.org/works?" + query)
    return data.get("message", {}).get("items", [])


def openalex_candidates(item: dict) -> list[dict]:
    params = urllib.parse.urlencode({"search": clean_tex(item["title"]), "per-page": 5})
    data = get_json("https://api.openalex.org/works?" + params)
    return data.get("results", [])


def first_author_crossref(work: dict) -> str:
    authors = work.get("author") or []
    if not authors:
        return ""
    first = authors[0]
    return " ".join(x for x in (first.get("given", ""), first.get("family", "")) if x)


def first_author_openalex(work: dict) -> str:
    authorships = work.get("authorships") or []
    if not authorships:
        return ""
    return authorships[0].get("author", {}).get("display_name", "")


def issued_year(work: dict) -> str:
    for key in ("published-print", "published-online", "issued"):
        parts = (work.get(key) or {}).get("date-parts") or []
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def arxiv_id(item: dict) -> str:
    joined = " ".join((item.get("venue", ""), item.get("url", ""), item.get("note", "")))
    match = re.search(r"(?:arXiv:|arxiv\.org/(?:abs|pdf)/)(\d{4}\.\d{4,5})", joined, re.I)
    return match.group(1) if match else ""


def choose_best(item: dict, crossref: list[dict], openalex: list[dict]) -> dict:
    candidates = []
    for work in crossref:
        title = (work.get("title") or [""])[0]
        candidates.append(
            {
                "source": "Crossref",
                "title": title,
                "author": first_author_crossref(work),
                "year": issued_year(work),
                "venue": (work.get("container-title") or [""])[0],
                "volume": work.get("volume", ""),
                "number": work.get("issue", ""),
                "pages": work.get("page", ""),
                "doi": work.get("DOI", ""),
                "official_url": "https://doi.org/" + work.get("DOI", "") if work.get("DOI") else work.get("URL", ""),
                "title_similarity": similarity(item["title"], title),
            }
        )
    for work in openalex:
        title = work.get("display_name", "")
        primary = work.get("primary_location") or {}
        source = primary.get("source") or {}
        ids = work.get("ids") or {}
        doi = (work.get("doi") or "").replace("https://doi.org/", "")
        candidates.append(
            {
                "source": "OpenAlex",
                "title": title,
                "author": first_author_openalex(work),
                "year": str(work.get("publication_year") or ""),
                "venue": source.get("display_name", ""),
                "volume": work.get("biblio", {}).get("volume") or "",
                "number": work.get("biblio", {}).get("issue") or "",
                "pages": "--".join(
                    x for x in (
                        work.get("biblio", {}).get("first_page") or "",
                        work.get("biblio", {}).get("last_page") or "",
                    ) if x
                ),
                "doi": doi,
                "official_url": "https://doi.org/" + doi if doi else ids.get("openalex", ""),
                "title_similarity": similarity(item["title"], title),
            }
        )
    if not candidates:
        return {}
    return max(candidates, key=lambda value: (value["title_similarity"], value["source"] == "Crossref"))


def status_for(item: dict, best: dict, arxiv: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    score = best.get("title_similarity", 0.0)
    if score < 0.82:
        if arxiv:
            return "verified_preprint_id", ["No high-confidence bibliographic match; arXiv identifier is explicit in the source entry."]
        if item.get("url") or "http" in item.get("venue", ""):
            return "technical_source_url", ["Technical or software source; verify against the official URL rather than Crossref."]
        return "manual_needed", [f"Best title similarity is {score:.3f}."]
    local_year, source_year = item.get("year", ""), best.get("year", "")
    if local_year and source_year and local_year != source_year:
        notes.append(f"Year mismatch: local {local_year}; source {source_year}.")
    local_author = clean_tex(item.get("author", "")).split(" and ")[0]
    source_author = best.get("author", "")
    if local_author and source_author and similarity(local_author, source_author) < 0.55:
        notes.append(f"First-author mismatch: local '{local_author}'; source '{source_author}'.")
    if notes:
        return "mismatch", notes
    return "verified", notes


def main() -> None:
    items = json.loads((WORK / "reference_inventory.json").read_text(encoding="utf-8"))
    cache_path = WORK / "verification_cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    results = []
    for index, item in enumerate(items, start=1):
        key = item["key"]
        if key in cache:
            result = cache[key]
        else:
            arxiv = arxiv_id(item)
            crossref, openalex, errors = [], [], []
            try:
                crossref = crossref_candidates(item)
            except Exception as exc:  # Preserve partial-source verification.
                errors.append(f"Crossref: {type(exc).__name__}: {exc}")
            try:
                openalex = openalex_candidates(item)
            except Exception as exc:
                errors.append(f"OpenAlex: {type(exc).__name__}: {exc}")
            best = choose_best(item, crossref, openalex)
            status, notes = status_for(item, best, arxiv)
            official_url = best.get("official_url", "")
            if status == "verified_preprint_id" and arxiv:
                official_url = f"https://arxiv.org/abs/{arxiv}"
            elif status == "technical_source_url":
                official_url = item.get("url", "") or re.sub(r"^\\url\{(.+)\}$", r"\1", item.get("venue", ""))
            result = {
                "sequence": item["sequence"],
                "key": key,
                "status": status,
                "official_url": official_url,
                "arxiv_id": arxiv,
                "best_match": best,
                "notes": notes,
                "source_errors": errors,
            }
            cache[key] = result
            cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
            time.sleep(0.12)
        results.append(result)
        print(f"[{index:03}/{len(items)}] {key}: {result['status']}", flush=True)
    (WORK / "auto_verification.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
