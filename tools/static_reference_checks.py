"""Run reproducible static checks over the final bibliography and citations."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

from build_reference_inventory import balanced_entries, citation_contexts, parse_fields


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    bib_text = (ROOT / "references.bib").read_text(encoding="utf-8")
    entries = balanced_entries(bib_text)
    keys = [key for _, key, _ in entries]
    fields_by_key = {key: parse_fields(raw) for _, key, raw in entries}
    contexts = citation_contexts()
    cited = set(contexts)
    bib_keys = set(keys)

    duplicate_keys = sorted(key for key, count in Counter(keys).items() if count > 1)
    duplicate_dois = sorted(
        doi for doi, count in Counter(
            fields.get("doi", "").strip().lower()
            for fields in fields_by_key.values()
            if fields.get("doi", "").strip()
        ).items() if count > 1
    )
    missing_core_fields = {
        key: [name for name in ("title", "author", "year") if not fields.get(name)]
        for key, fields in fields_by_key.items()
        if any(not fields.get(name) for name in ("title", "author", "year"))
    }
    missing_persistent_source = sorted(
        key for key, fields in fields_by_key.items()
        if not fields.get("doi") and not fields.get("url")
    )
    truncated_author_lists = sorted(
        key for key, fields in fields_by_key.items()
        if re.search(r"\band\s+others\b", fields.get("author", ""), flags=re.I)
    )

    with (ROOT / "literature_audit.csv").open(encoding="utf-8-sig", newline="") as handle:
        audit = list(csv.DictReader(handle))
    verified_without_url = sorted(
        row["key"] for row in audit
        if row["existence_status"] == "verified" and not row["official_source"].strip()
    )
    unresolved_active = sorted(
        row["key"] for row in audit
        if row["cited_in_manuscript"] == "yes" and row["existence_status"] != "verified"
    )
    active_metadata_mismatches = []
    for row in audit:
        key = row["key"]
        if row["cited_in_manuscript"] != "yes" or key not in fields_by_key:
            continue
        fields = fields_by_key[key]
        expected = {
            "matched_title": fields.get("title", ""),
            "matched_first_author": fields.get("author", "").split(" and ")[0],
            "matched_year": fields.get("year", ""),
        }
        if any(row[name].strip() != value.strip() for name, value in expected.items()):
            active_metadata_mismatches.append(key)

    stale_patterns = {
        "old_78_study_claim": r"\b78\s+(?:representative\s+)?studies\b",
        "old_72_source_claim": r"\b72\s+(?:verified\s+|active\s+)?sources\b",
        "old_70_percent_validation": r"70\\%|7/10",
        "unsupported_benchmark_section": r"survey benchmark datasets and evaluation protocols",
        "old_mast_percentages": r"79\\%|80\\%",
    }
    manuscript_text = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(ROOT.glob("*.tex"))
    )
    commented_citation_arguments = re.findall(
        r"\\cite[tp]?\{[^}]*%[^}]*\}", manuscript_text, flags=re.S
    )
    unescaped_texttt_underscores = re.findall(
        r"\\texttt\{[^}]*?(?<!\\)_[^}]*\}", manuscript_text
    )
    stale_hits = {
        name: re.findall(pattern, manuscript_text, flags=re.I)
        for name, pattern in stale_patterns.items()
        if re.search(pattern, manuscript_text, flags=re.I)
    }

    highlights = (ROOT / "Highlights.txt").read_text(encoding="utf-8").splitlines()
    overlong_highlights = [line for line in highlights if len(line) > 85]

    report = {
        "bib_entries": len(entries),
        "unique_bib_keys": len(bib_keys),
        "cited_keys": len(cited),
        "undefined_citations": sorted(cited - bib_keys),
        "uncited_bibliography_entries": sorted(bib_keys - cited),
        "duplicate_keys": duplicate_keys,
        "duplicate_dois": duplicate_dois,
        "entries_missing_title_author_or_year": missing_core_fields,
        "entries_missing_doi_and_url": missing_persistent_source,
        "truncated_author_lists": truncated_author_lists,
        "audit_rows": len(audit),
        "verified_audit_rows_without_source_url": verified_without_url,
        "active_audit_rows_not_verified": unresolved_active,
        "active_audit_metadata_mismatches": sorted(active_metadata_mismatches),
        "stale_claim_hits": stale_hits,
        "citation_arguments_containing_comments": commented_citation_arguments,
        "texttt_arguments_with_unescaped_underscores": unescaped_texttt_underscores,
        "highlight_count": len(highlights),
        "highlights_over_85_characters": overlong_highlights,
    }
    checks_passed = all([
        len(entries) == 75,
        len(bib_keys) == 75,
        len(cited) == 75,
        not report["undefined_citations"],
        not report["uncited_bibliography_entries"],
        not duplicate_keys,
        not duplicate_dois,
        not missing_core_fields,
        not missing_persistent_source,
        not truncated_author_lists,
        len(audit) == 111,
        not verified_without_url,
        not unresolved_active,
        not active_metadata_mismatches,
        not stale_hits,
        not commented_citation_arguments,
        not unescaped_texttt_underscores,
        3 <= len(highlights) <= 5,
        not overlong_highlights,
    ])
    report["checks_passed"] = checks_passed

    output = ROOT / "audit_work" / "static_reference_checks.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if checks_passed else 1)


if __name__ == "__main__":
    main()
