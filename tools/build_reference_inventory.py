from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "references.bib"
TEX_PATHS = sorted(ROOT.glob("*.tex"))


def balanced_entries(text: str) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    pos = 0
    marker = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.I)
    while match := marker.search(text, pos):
        depth = 1
        i = match.end()
        escaped = False
        while i < len(text) and depth:
            char = text[i]
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            i += 1
        if depth:
            raise ValueError(f"Unbalanced BibTeX entry beginning at {match.start()}")
        entries.append((match.group(1).lower(), match.group(2), text[match.start():i]))
        pos = i
    return entries


def parse_fields(raw: str) -> dict[str, str]:
    body = raw[raw.find(",") + 1 : raw.rfind("}")]
    fields: dict[str, str] = {}
    field_re = re.compile(r"(?ms)^\s*([A-Za-z][\w-]*)\s*=\s*")
    matches = list(field_re.finditer(body))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        value = body[match.end():end].strip().rstrip(",").strip()
        if len(value) >= 2 and ((value[0], value[-1]) in (("{", "}"), ('"', '"'))):
            value = value[1:-1].strip()
        fields[match.group(1).lower()] = re.sub(r"\s+", " ", value)
    return fields


def citation_contexts() -> dict[str, list[dict[str, object]]]:
    output: dict[str, list[dict[str, object]]] = {}
    cite_re = re.compile(r"\\cite(?:t|p|author|year|alp|alt|num)?\s*(?:\[[^\]]*\]\s*)*\{([^}]+)\}")
    for path in TEX_PATHS:
        lines = path.read_text(encoding="utf-8").splitlines()
        for line_no, line in enumerate(lines, start=1):
            for match in cite_re.finditer(line):
                for key in (part.strip() for part in match.group(1).split(",")):
                    if not key:
                        continue
                    lo = max(0, line_no - 2)
                    hi = min(len(lines), line_no + 1)
                    context = " ".join(x.strip() for x in lines[lo:hi] if x.strip())
                    output.setdefault(key, []).append(
                        {"file": path.name, "line": line_no, "context": context}
                    )
    return output


def main() -> None:
    text = BIB_PATH.read_text(encoding="utf-8", errors="replace")
    entries = balanced_entries(text)
    contexts = citation_contexts()
    inventory = []
    for index, (entry_type, key, raw) in enumerate(entries, start=1):
        fields = parse_fields(raw)
        inventory.append(
            {
                "sequence": index,
                "key": key,
                "entry_type": entry_type,
                "title": fields.get("title", ""),
                "author": fields.get("author", ""),
                "year": fields.get("year", ""),
                "venue": fields.get("journal", fields.get("booktitle", fields.get("howpublished", ""))),
                "journal": fields.get("journal", ""),
                "booktitle": fields.get("booktitle", ""),
                "volume": fields.get("volume", ""),
                "number": fields.get("number", ""),
                "pages": fields.get("pages", ""),
                "publisher": fields.get("publisher", ""),
                "note": fields.get("note", ""),
                "doi": fields.get("doi", ""),
                "url": fields.get("url", ""),
                "arxiv": fields.get("eprint", ""),
                "citation_count": len(contexts.get(key, [])),
                "citation_contexts": contexts.get(key, []),
                "raw": raw,
            }
        )

    out_dir = ROOT / "audit_work"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "reference_inventory.json").write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (out_dir / "reference_inventory.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "sequence", "key", "entry_type", "title", "author", "year",
                "venue", "doi", "url", "arxiv", "volume", "number", "pages",
                "citation_count",
            ],
        )
        writer.writeheader()
        for item in inventory:
            writer.writerow({name: item[name] for name in writer.fieldnames})

    cited_keys = set(contexts)
    bib_keys = {entry[1] for entry in entries}
    summary = {
        "bib_entries": len(entries),
        "unique_bib_keys": len(bib_keys),
        "cited_keys": len(cited_keys),
        "cited_keys_missing_from_bib": sorted(cited_keys - bib_keys),
        "uncited_bib_keys": sorted(bib_keys - cited_keys),
    }
    (out_dir / "inventory_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
