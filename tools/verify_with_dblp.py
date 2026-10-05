from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

from verify_reference_metadata import clean_tex, similarity


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "audit_work"


def as_list(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def main() -> None:
    items = json.loads((WORK / "reference_inventory.json").read_text(encoding="utf-8"))
    cache_path = WORK / "dblp_verification.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    for index, item in enumerate(items, start=1):
        if item["key"] in cache:
            continue
        query = urllib.parse.urlencode(
            {"q": clean_tex(item["title"]), "format": "json", "h": 5}
        )
        url = "https://dblp.org/search/publ/api?" + query
        request = urllib.request.Request(url, headers={"User-Agent": "ESWA-reference-audit/1.0"})
        result = {"key": item["key"], "matches": [], "error": ""}
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.load(response)
            hits = data.get("result", {}).get("hits", {}).get("hit", [])
            for hit in hits:
                info = hit.get("info", {})
                authors = info.get("authors", {}).get("author", [])
                names = []
                for author in as_list(authors):
                    names.append(author.get("text", "") if isinstance(author, dict) else str(author))
                title = str(info.get("title", "")).rstrip(".")
                result["matches"].append(
                    {
                        "title": title,
                        "title_similarity": similarity(item["title"], title),
                        "authors": names,
                        "year": str(info.get("year", "")),
                        "venue": str(info.get("venue", "")),
                        "pages": str(info.get("pages", "")),
                        "type": str(info.get("type", "")),
                        "url": str(info.get("url", "")),
                        "ee": str(info.get("ee", "")),
                    }
                )
        except Exception as exc:
            result["error"] = f"{type(exc).__name__}: {exc}"
        cache[item["key"]] = result
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[{index:03}/{len(items)}] {item['key']}", flush=True)
        time.sleep(0.12)


if __name__ == "__main__":
    main()
