from __future__ import annotations
from project_paths import project_path

import csv
import json
import re
from dataclasses import asdict
from collections import Counter
from pathlib import Path

from active_tex import compiled_keys, scan_manuscript


ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = project_path("references.bib")


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


def publication_venue(fields: dict[str, str]) -> str:
    return next((fields.get(name, "") for name in ("journal", "booktitle", "howpublished", "publisher") if fields.get(name)), "")


def citation_contexts(root: Path = ROOT, main: str = "manuscript.tex") -> dict[str, list[dict[str, object]]]:
    output: dict[str, list[dict[str, object]]] = {}
    for citation in scan_manuscript(root, main).citations:
        for key in citation.keys:
            output.setdefault(key, []).append(asdict(citation))
    return output


def main() -> None:
    text = BIB_PATH.read_text(encoding="utf-8", errors="replace")
    entries = balanced_entries(text)
    contexts = citation_contexts()
    scan = scan_manuscript(ROOT)
    compiled = compiled_keys(ROOT)
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
                "venue": publication_venue(fields),
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

    out_dir = project_path("audit_work")
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
        "scope": "literal active inclusion graph rooted at manuscript.tex; no root glob",
        "source_files": scan.files,
        "excluded_ranges": scan.excluded_ranges,
        "bib_entries": len(entries),
        "unique_bib_keys": len(bib_keys),
        "cited_keys": len(cited_keys),
        "citation_commands": len(scan.citations),
        "citation_key_occurrences": sum(len(c.keys) for c in scan.citations),
        "nocite_keys": scan.nocite_keys,
        "compiled_artifacts": compiled["artifacts"],
        "aux_cited_keys": len(compiled["aux_keys"]),
        "aux_citation_commands": len(compiled["aux_commands"]),
        "aux_key_occurrences": compiled["aux_key_occurrences"],
        "bbl_entries": len(compiled["bbl_keys"]),
        "source_aux_keys_match": cited_keys == set(compiled["aux_keys"]),
        "source_aux_commands_match": Counter(tuple(c.keys) for c in scan.citations) == Counter(tuple(c) for c in compiled["aux_commands"]),
        "source_bbl_keys_match": cited_keys == set(compiled["bbl_keys"]),
        "cited_keys_missing_from_bib": sorted(cited_keys - bib_keys),
        "uncited_bib_keys": sorted(bib_keys - cited_keys),
    }
    (out_dir / "active_citations.json").write_text(json.dumps([asdict(c) for c in scan.citations], ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "inventory_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
