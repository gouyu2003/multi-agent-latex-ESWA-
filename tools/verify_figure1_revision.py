"""Check Figure 1 against source records, compiled output, and its saved baseline."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re

import pymupdf as fitz

from active_tex import scan_manuscript

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "figure1_audit"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def spans(page):
    return [span for block in page.get_text("dict")["blocks"]
            for line in block.get("lines", []) for span in line["spans"]]


def verify(baseline_directory: Path, figure_only: bool = False) -> dict:
    baseline = json.loads((baseline_directory / "baseline.json").read_text(encoding="utf-8"))
    data = json.loads((AUDIT / "source_summary.json").read_text(encoding="utf-8"))
    scan = scan_manuscript(ROOT)
    citations = [{"command": c.command, "keys": c.keys, "raw_command": c.raw_command}
                 for c in scan.citations]
    with (ROOT / "figure1_source_data.csv").open(encoding="utf-8", newline="") as handle:
        source_rows = list(csv.DictReader(handle))
    expected_rows = [{k: str(v) for k, v in row.items()} for row in data["records"]]
    changed = sorted(name for name, digest in baseline["files"].items()
                     if not (ROOT / name).exists() or sha(ROOT / name) != digest)
    allowed = {"manuscript.tex", "tools/generate_reference_figures.py",
               "fig_reference_corpus.pdf", "fig_reference_corpus.svg", "fig_reference_corpus.png"}
    protected_changes = [name for name in changed if name not in allowed]
    figure = fitz.open(ROOT / "fig_reference_corpus.pdf")
    figure_page = figure[0]
    figure_spans = spans(figure_page)
    figure_text = figure_page.get_text()
    normalized = re.sub(r"\s+", "", figure_text)
    required = ["Bibliographypool", "n=85", "Citedsources", "n=78", "Uncitedrecords", "n=7",
                "I:13", "S:15", "B:42", "T:8"]
    historical_labels = ["Historicalworkingrecords", "Candidates", "Retained",
                         "Additions", "Excluded(logged)", "Latersourceaudit", "n=84"]
    paper = None if figure_only else fitz.open(ROOT / "manuscript.pdf")
    figure_pages = [page for page in paper
                    if page.search_for("Bibliography pool") and page.search_for("I: 13")
                    and page.search_for("Uncited records")] if paper is not None else []
    final_spans = [span for page in figure_pages for span in spans(page)
                   if "Arial" in span["font"]]
    # This contract is about the figure's glyphs, not the document's caption font.
    final_sizes = [span["size"] for span in final_spans]
    current_log = "" if figure_only else (ROOT / "manuscript.log").read_text(encoding="utf-8", errors="replace")
    before_log = (baseline_directory / "before_manuscript.log").read_text(encoding="utf-8", errors="replace")
    overfull = lambda log: [line for line in log.splitlines() if line.startswith("Overfull")]
    undefined = [line for line in current_log.splitlines()
                 if re.search(r"(?:Citation|Reference).*undefined|There were undefined", line)]
    collision = json.loads((AUDIT / "collision.json").read_text(encoding="utf-8"))
    # Check the exported geometry, not only the plotting code's arithmetic.
    bar_segments = sorted([path["rect"] for path in figure_page.get_drawings()
                           if path.get("fill") is not None
                           and abs(path["rect"].height * 25.4 / 72 - 7.5) < 0.05
                           and abs(path["rect"].y0 * 25.4 / 72 - 21.5) < 0.05],
                          key=lambda rect: rect.x0)
    bar_total = sum(rect.width for rect in bar_segments)
    proportional_bar = len(bar_segments) == 4 and all(
        abs(rect.width / bar_total - count / 78) < 0.0001
        for rect, count in zip(bar_segments, (13, 15, 42, 8)))
    checks = {
        "source_inputs_match_recorded_hashes": all(sha(ROOT / name) == digest
                                                   for name, digest in data["input_sha256"].items()),
        "pool_partition_85_78_7": (data["pool_count"], data["cited_count"], data["uncited_count"]) == (85, 78, 7),
        "cited_roles_13_15_42_8": data["cited_roles"] == {"I": 13, "S": 15, "B": 42, "T": 8},
        "pool_roles_13_17_46_9": data["pool_roles"] == {"I": 13, "S": 17, "B": 46, "T": 9},
        "source_csv_matches_summary": source_rows == expected_rows,
        "active_citation_commands_and_keys_preserved": citations == baseline["citations"],
        "136_commands_180_key_occurrences": (data["citation_commands"], data["expanded_key_occurrences"]) == (136, 180),
        "protected_tracked_files_unchanged": not protected_changes,
        "historical_summary_not_used_as_figure_data": "historical_flow" not in data and "figure_source_data.csv" not in data["input_sha256"],
        "figure_pdf_has_all_expected_labels_and_counts": all(term in normalized for term in required),
        "historical_flow_absent_from_export": not any(term in normalized for term in historical_labels),
        "figure_pdf_is_vector": not figure_page.get_images(full=True),
        "figure_pdf_140_by_48_mm": abs(figure_page.rect.width * 25.4 / 72 - 140) < 0.1 and abs(figure_page.rect.height * 25.4 / 72 - 48) < 0.1,
        "figure_pdf_uses_Arial": bool(figure_spans) and all("Arial" in span["font"] for span in figure_spans),
        "figure_fonts_embedded": all(figure.extract_font(font[0])[3] for font in figure_page.get_fonts()),
        "collision_audit_pass": collision.get("verdict") == "PASS",
        "rendered_bar_widths_proportional_to_13_15_42_8": proportional_bar,
    }
    if not figure_only:
        compiled_figure_text = re.sub(r"\s+", "", "".join(span["text"] for span in final_spans))
        checks.update({
            "compiled_bibliography_identical_to_baseline": sha(ROOT / "manuscript.bbl") == sha(baseline_directory / "before_manuscript.bbl"),
            "figure_appears_once_in_manuscript": len(figure_pages) == 1,
            "compiled_figure_matches_latest_current_only_labels": all(term in compiled_figure_text for term in required)
                and not any(term in compiled_figure_text for term in historical_labels),
            "final_figure_glyph_sizes_6_8_to_8_pt": bool(final_sizes) and min(final_sizes) >= 6.8 and max(final_sizes) <= 8.0,
            "no_undefined_citations_or_cross_references": not undefined,
            "no_new_overfull_warnings": overfull(current_log) == overfull(before_log),
        })
    result = {
        "date": "2026-10-13", "baseline_head": baseline["head"],
        "validation_scope": "standalone figure and source preservation" if figure_only else "figure and compiled manuscript",
        "compilation_status": "PENDING_USER_VSCODE" if figure_only else "existing compiled output inspected",
        "checks": checks, "all_passed": all(checks.values()),
        "changed_preexisting_tracked_files": changed, "unexpected_protected_changes": protected_changes,
        "manuscript_pages": len(paper) if paper is not None else None, "figure_page": figure_pages[0].number + 1 if figure_pages else None,
        "figure_pdf_font_sizes_pt": sorted({round(span["size"], 3) for span in figure_spans}),
        "final_figure_font_sizes_pt": sorted({round(size, 3) for size in final_sizes}),
        "overfull_before": overfull(before_log), "overfull_after": None if figure_only else overfull(current_log),
        "underfull_before": before_log.count("Underfull"), "underfull_after": None if figure_only else current_log.count("Underfull"),
        "source_and_output_sha256": {name: sha(ROOT / name) for name in [
            "manuscript.tex", "references.bib", "literature_audit.csv", "figure_source_data.csv",
            "fig_reference_corpus.pdf", "fig_reference_corpus.svg", "fig_reference_corpus.png",
            "figure1_source_data.csv", "tools/generate_reference_figures.py"]
            + ([] if figure_only else ["manuscript.pdf", "manuscript.bbl"])},
        "visual_review": "pending; automated checks do not approve layout or scientific claims",
    }
    (AUDIT / "acceptance.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["all_passed", "checks", "manuscript_pages", "figure_page", "final_figure_font_sizes_pt"]}, indent=2))
    figure.close()
    if paper is not None:
        paper.close()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=ROOT / "tmp/figure1_revision")
    parser.add_argument("--figure-only", action="store_true", help="Check the standalone figure; leave manuscript compilation to the user")
    args = parser.parse_args()
    raise SystemExit(0 if verify(args.baseline, args.figure_only)["all_passed"] else 1)
