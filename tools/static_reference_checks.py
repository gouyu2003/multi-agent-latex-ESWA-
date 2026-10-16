"""Check active-source/compiled-artifact consistency and audit-ledger coverage.

A structural pass does not mean unsupported claims or metadata are corrected.
No fixed corpus size is required, and unused bibliography records are allowed.
"""
from __future__ import annotations
from project_paths import project_path
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from active_tex import compiled_keys, scan_manuscript
from build_reference_inventory import balanced_entries, parse_fields

ROOT = Path(__file__).resolve().parents[1]
WORK = project_path("audit_work")
FIELDS = ("author", "title", "year", "venue", "volume", "number", "pages", "doi", "url", "type")


def main() -> None:
    entries = balanced_entries((project_path("references.bib")).read_text(encoding="utf-8"))
    keys = [key for _, key, _ in entries]
    fields = {key: parse_fields(raw) for _, key, raw in entries}
    scan = scan_manuscript(ROOT)
    compiled = compiled_keys(ROOT)
    cited = {key for c in scan.citations for key in c.keys}
    bib_keys = set(keys)
    expected_bbl = cited | (bib_keys if "*" in scan.nocite_keys else set(scan.nocite_keys))
    expected_aux = Counter(tuple(c.keys) for c in scan.citations)
    expected_aux.update((key,) for key in scan.nocite_keys)
    errors: dict[str, object] = {}
    warnings: dict[str, object] = {}

    def check(name: str, value: object) -> None:
        if value:
            errors[name] = value

    check("duplicate_bib_keys", [k for k, n in Counter(keys).items() if n > 1])
    check("duplicate_dois", [d for d, n in Counter(f.get("doi", "").strip().lower() for f in fields.values() if f.get("doi")).items() if n > 1])
    check("undefined_citations", sorted((cited | set(scan.nocite_keys)) - bib_keys - {"*"}))
    check("missing_core_fields", {k: [n for n in ("title", "author", "year") if not f.get(n)] for k, f in fields.items() if any(not f.get(n) for n in ("title", "author", "year"))})
    check("missing_doi_and_url", [k for k, f in fields.items() if not f.get("doi") and not f.get("url")])
    check("truncated_author_lists", [k for k, f in fields.items() if re.search(r"\band\s+others\b", f.get("author", ""), re.I)])
    check("source_aux_key_difference", sorted((cited | set(scan.nocite_keys)) ^ set(compiled["aux_keys"])))
    check("source_aux_command_multiset_differs", expected_aux != Counter(tuple(c) for c in compiled["aux_commands"]))
    check("source_bbl_key_difference", sorted(expected_bbl ^ set(compiled["bbl_keys"])))
    check("duplicate_bbl_keys", [k for k, n in Counter(compiled["bbl_keys"]).items() if n > 1])
    warnings["uncited_bibliography_pool_records"] = sorted(bib_keys - cited)
    reference_path = WORK / "reference_field_audit.json"
    citation_path = WORK / "citation_claim_audit.json"
    ledger_counts: dict[str, object] = {}
    for path in (reference_path, citation_path):
        check("missing_" + path.stem, not path.exists())
    if reference_path.exists() and citation_path.exists():
        refs = json.loads(reference_path.read_text(encoding="utf-8"))
        claims = json.loads(citation_path.read_text(encoding="utf-8"))
        ref_keys = [r["key"] for r in refs]
        check("reference_ledger_key_difference", sorted(set(ref_keys) ^ bib_keys))
        check("duplicate_reference_ledger_keys", [k for k, n in Counter(ref_keys).items() if n > 1])
        check("reference_ledger_missing_field_checks", {r["key"]: [f for f in FIELDS if f not in r["field_checks"]] for r in refs if any(f not in r["field_checks"] for f in FIELDS)})
        check("reference_ledger_missing_sources", [r["key"] for r in refs if not r.get("official_sources")])
        current_by_id = {c.command_id: c for c in scan.citations}
        ids = [c["command_id"] for c in claims]
        check("citation_ledger_id_difference", sorted(set(ids) ^ set(current_by_id)))
        check("duplicate_citation_ledger_ids", [i for i, n in Counter(ids).items() if n > 1])
        citation_errors = []
        for row in claims:
            current = current_by_id.get(row["command_id"])
            if not current:
                continue
            if (row["keys"] != current.keys or row["file"] != current.file or row["line"] != current.line
                or row["offset"] != current.offset or row["original_sentence"] != current.original_sentence):
                citation_errors.append(row["command_id"] + ": stale context")
            assessments = row.get("by_key_assessments", [])
            if Counter(a["key"] for a in assessments) != Counter(current.keys):
                citation_errors.append(row["command_id"] + ": key assessment coverage")
            if any(not a.get("source_evidence") or not a.get("evidence_url") or not a.get("locator") or not a.get("recommendation") for a in assessments):
                citation_errors.append(row["command_id"] + ": incomplete evidence record")
        check("citation_ledger_errors", citation_errors)
        ledger_counts = {"reference_rows": len(refs), "citation_command_rows": len(claims),
            "citation_key_assessments": sum(len(c["by_key_assessments"]) for c in claims),
            "support_degrees": dict(Counter(c["support_degree"] for c in claims)),
            "field_status_counts": dict(Counter(f["status"] for r in refs for f in r["field_checks"].values()))}
        warnings["citation_rows_requiring_attention"] = [c["command_id"] for c in claims if c["support_degree"] != "direct"]
        warnings["metadata_fields_requiring_attention"] = [{"key": r["key"], "fields": [k for k, f in r["field_checks"].items() if f["status"] not in {"verified", "not_applicable"}]} for r in refs if any(f["status"] not in {"verified", "not_applicable"} for f in r["field_checks"].values())]
        warnings["additional_fields_requiring_attention"] = [{"key": r["key"], "fields": [k for k, f in r.get("additional_field_checks", {}).items() if f["status"] not in {"verified", "not_applicable"}]} for r in refs if any(f["status"] not in {"verified", "not_applicable"} for f in r.get("additional_field_checks", {}).values())]
        manifest_path = WORK / "ledger_manifest.json"
        check("missing_ledger_manifest", not manifest_path.exists())
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            check("ledger_snapshot_stale", [p for p, h in manifest["input_sha256"].items() if not (project_path(p)).exists() or hashlib.sha256((project_path(p)).read_bytes()).hexdigest() != h])
            check("ledger_output_modified", [p for p, h in manifest["ledger_output_sha256"].items() if not (project_path(p)).exists() or hashlib.sha256((project_path(p)).read_bytes()).hexdigest() != h])
            if manifest.get("corrections_applied"):
                check("compilation_not_current", not manifest.get("compilation_current"))
                check("compilation_failed", not manifest.get("compilation_passed"))
                verification_path = WORK / "correction_verification.json"
                check("missing_correction_verification", not verification_path.exists())
                if verification_path.exists():
                    check("protected_material_changed", not json.loads(verification_path.read_text(encoding="utf-8"))["checks_passed"])
    legacy_path = project_path("literature_audit.csv")
    if legacy_path.exists():
        with legacy_path.open(encoding="utf-8-sig", newline="") as handle:
            legacy = list(csv.DictReader(handle))
        counts = Counter(key for c in scan.citations for key in c.keys)
        warnings["legacy_csv_stale_citation_flags"] = [r["key"] for r in legacy if r["key"] in bib_keys and (r["cited_in_manuscript"] == "yes") != (r["key"] in cited)]
        warnings["legacy_csv_stale_citation_counts"] = [r["key"] for r in legacy if r["key"] in bib_keys and int(r["citation_count"] or 0) != counts[r["key"]]]
    report = {"scope": "current active manuscript inclusion graph; historical CSV not authoritative",
        "source_files": scan.files, "compiled_artifacts": compiled["artifacts"],
        "bib_pool_entries": len(entries), "active_cited_keys": len(cited),
        "citation_commands": len(scan.citations), "citation_key_occurrences": sum(len(c.keys) for c in scan.citations),
        "aux_citation_commands": len(compiled["aux_commands"]), "bbl_entries": len(compiled["bbl_keys"]),
        "ledger_coverage": ledger_counts, "errors": errors, "warnings": warnings,
        "checks_passed": not errors,
        "meaning_of_pass": "Active-scope counting, fresh compiled-artifact consistency, ledger completeness and preserved source/figure boundaries. Corrections and unresolved evidence are recorded separately; pass is not blanket field verification."}
    WORK.mkdir(exist_ok=True)
    (WORK / "static_reference_checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("bib_pool_entries", "active_cited_keys", "citation_commands", "citation_key_occurrences", "ledger_coverage", "errors", "checks_passed")}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
