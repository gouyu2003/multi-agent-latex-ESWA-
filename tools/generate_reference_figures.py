"""Generate the reference-corpus and core-study summary figures."""
from project_paths import project_path

from pathlib import Path
import argparse
import csv
import hashlib
import json
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle


ROOT = Path(__file__).resolve().parents[1]

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 8,
    "axes.titlesize": 9,
    "axes.labelsize": 8,
    "xtick.labelsize": 7.5,
    "ytick.labelsize": 7.5,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.7,
})

NAVY = "#183B56"
BLUE = "#2A6F97"
TEAL = "#2A9D8F"
PALE_BLUE = "#E8F1F5"
PALE_TEAL = "#E4F3F0"
PALE_ORANGE = "#F8E9D5"
ORANGE = "#D77A28"
GREY = "#66737D"
LIGHT_GREY = "#EEF1F3"


def save_figure(fig: plt.Figure, stem: str) -> None:
    for suffix, kwargs in {
        ".pdf": {},
        ".svg": {},
        ".png": {"dpi": 400},
    }.items():
        fig.savefig(project_path(f"{stem}{suffix}"), bbox_inches="tight", facecolor="white", **kwargs)


def rounded_box(ax, xy, width, height, facecolor, edgecolor, title, subtitle=""):
    box = FancyBboxPatch(
        xy, width, height,
        boxstyle="round,pad=0.018,rounding_size=0.025",
        linewidth=1.05, edgecolor=edgecolor, facecolor=facecolor,
        transform=ax.transAxes,
    )
    ax.add_patch(box)
    x, y = xy
    ax.text(x + width / 2, y + height * 0.62, title, ha="center", va="center",
            fontsize=11, fontweight="bold", color=NAVY, transform=ax.transAxes)
    if subtitle:
        ax.text(x + width / 2, y + height * 0.29, subtitle, ha="center", va="center",
                fontsize=7.2, color=GREY, transform=ax.transAxes)


def current_corpus_data() -> dict:
    """Count the current pool and active citations; do not reconstruct searches."""
    from active_tex import scan_manuscript
    from build_reference_inventory import balanced_entries

    entries = list(balanced_entries((project_path("references.bib")).read_text(encoding="utf-8")))
    pool = {key for _, key, _ in entries}
    if len(entries) != len(pool):
        raise ValueError("Duplicate bibliography keys")
    scan = scan_manuscript(ROOT)
    cited = {key for citation in scan.citations for key in citation.keys}
    if cited - pool:
        raise ValueError(f"Cited keys missing from bibliography: {sorted(cited - pool)}")
    with (project_path("literature_audit.csv")).open(encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))
    roles = {row["key"]: row["evidence_role"] for row in records}
    if len(roles) != len(records):
        raise ValueError("Duplicate keys in the evidence-role table")
    if pool - roles.keys() or any(roles[key] not in "ISBT" for key in pool):
        raise ValueError("Every bibliography record must have a current I/S/B/T role")
    uncited = pool - cited
    counts = lambda keys: {role: sum(roles[key] == role for key in keys) for role in "ISBT"}
    data = {
        "scope": "Current bibliography pool and author-coded evidence roles of actively cited sources",
        "pool_count": len(pool), "cited_count": len(cited), "uncited_count": len(uncited),
        "pool_roles": counts(pool), "cited_roles": counts(cited), "uncited_roles": counts(uncited),
        "citation_commands": len(scan.citations),
        "expanded_key_occurrences": sum(len(citation.keys) for citation in scan.citations),
        "records": [{"key": key, "evidence_role": roles[key], "cited_in_active_manuscript": key in cited}
                    for key in sorted(pool)],
        "input_sha256": {name: hashlib.sha256((project_path(name)).read_bytes()).hexdigest()
                         for name in ("references.bib", "literature_audit.csv", "manuscript.tex")},
    }
    if data["pool_count"] != data["cited_count"] + data["uncited_count"]:
        raise ValueError("Pool partition does not balance")
    if sum(data["cited_roles"].values()) != data["cited_count"]:
        raise ValueError("Cited evidence roles do not balance")
    return data


def make_corpus_flow(qa_scripts: Path | None = None) -> None:
    """One connected, data-derived diagram at approximately its printed size."""
    data = current_corpus_data()
    audit = project_path("figure1_audit")
    audit.mkdir(exist_ok=True)
    (audit / "source_summary.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (project_path("figure1_source_data.csv")).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["key", "evidence_role", "cited_in_active_manuscript"])
        writer.writeheader()
        writer.writerows(data["records"])

    with mpl.rc_context({"font.family": "Arial", "font.size": 7.1,
                         "svg.fonttype": "none", "pdf.fonttype": 42}):
        fig = plt.figure(figsize=(140 / 25.4, 48 / 25.4), facecolor="white")
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set(xlim=(0, 140), ylim=(0, 48))
        ax.set_axis_off()

        def box(x, y, width, height, fill, edge):
            ax.add_patch(FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0,rounding_size=1.2", linewidth=0.7,
                         facecolor=fill, edgecolor=edge, zorder=2))

        def node(x, y, width, height, label, count, fill, edge):
            box(x, y, width, height, fill, edge)
            ax.text(x + width / 2, y + height / 2 + 1.9, label,
                    ha="center", va="center", fontsize=7.1, color=NAVY)
            ax.text(x + width / 2, y + height / 2 - 2.1, f"n = {count}",
                    ha="center", va="center", fontsize=7.8, fontweight="bold", color=NAVY)

        def line(xs, ys):
            ax.plot(xs, ys, color=GREY, linewidth=0.7, solid_capstyle="butt",
                    zorder=1)

        def arrow(start, end):
            ax.annotate("", xy=end, xytext=start, zorder=1,
                        arrowprops={"arrowstyle": "-|>", "color": GREY, "lw": 0.7,
                                    "mutation_scale": 6, "shrinkA": 0, "shrinkB": 1})

        node(4, 23, 32, 14, "Bibliography pool", data["pool_count"], PALE_BLUE, BLUE)
        node(78.5, 31, 32, 13, "Cited sources", data["cited_count"], PALE_TEAL, TEAL)
        node(53, 4, 32, 10, "Uncited records", data["uncited_count"], LIGHT_GREY, GREY)
        line([36, 44], [30, 30])
        line([44, 44], [9, 37.5])
        arrow((44, 37.5), (78.5, 37.5))
        arrow((44, 9), (53, 9))
        arrow((94.5, 31), (94.5, 26.5))

        # One quantitative bar: segment widths share the cited-source denominator.
        bar_x, bar_y, bar_width, bar_height = 53, 19, 83, 7.5
        segment_left = bar_x
        for role, fill in [("I", TEAL), ("S", BLUE), ("B", GREY), ("T", ORANGE)]:
            count = data["cited_roles"][role]
            width = bar_width * count / data["cited_count"]
            ax.add_patch(Rectangle((segment_left, bar_y), width, bar_height,
                                  facecolor=fill, edgecolor="white", linewidth=0.6, zorder=2))
            ax.text(segment_left + width / 2, bar_y + bar_height / 2,
                    f"{role}: {count}", ha="center", va="center",
                    fontsize=7.1, fontweight="bold", color="white", zorder=3)
            segment_left += width

        fig.canvas.draw()
        if qa_scripts:
            sys.path.insert(0, str(qa_scripts))
            from audit_panel_alignment import require_matplotlib_panel_alignment
            require_matplotlib_panel_alignment(fig, json_out=audit / "alignment.json", strict=True)
        else:
            (audit / "alignment.json").write_text(json.dumps({
                "verdict": "NOT APPLICABLE", "reason": "Single connected diagram on one axes; no comparable panels"
            }, indent=2) + "\n", encoding="utf-8")
        # Keep a fixed physical canvas: tight cropping would change the font scale in LaTeX.
        for suffix, options in (("pdf", {}), ("svg", {}), ("png", {"dpi": 400})):
            fig.savefig(project_path(f"fig_reference_corpus.{suffix}"), facecolor="white", **options)
        svg = project_path("fig_reference_corpus.svg")
        svg.write_text("\n".join(line.rstrip() for line in svg.read_text(encoding="utf-8").splitlines())
                       + "\n", encoding="utf-8")
        plt.close(fig)
    print(f"Figure 1: pool={data['pool_count']}, cited={data['cited_count']}, uncited={data['uncited_count']}; "
          f"cited roles={data['cited_roles']}")


def make_core_overview() -> None:
    # Core conclusion: the 14 directly included studies are concentrated in
    # 2024 and in ACL-family venues.
    venue_labels = ["ACL family", "NeurIPS", "ICML", "ICLR", "IEEE", "ACM"]
    venue_counts = [8, 2, 1, 1, 1, 1]
    years = [2023, 2024, 2025, 2026]
    year_counts = [1, 8, 3, 2]

    assert sum(venue_counts) == 14
    assert sum(year_counts) == 14

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 3.0),
                                   gridspec_kw={"width_ratios": [1.25, 1]})

    y_pos = list(range(len(venue_labels)))
    colors = [TEAL] + [BLUE] * (len(venue_labels) - 1)
    ax1.barh(y_pos, venue_counts, color=colors, height=0.62)
    ax1.set_yticks(y_pos, venue_labels)
    ax1.invert_yaxis()
    ax1.set_xlabel("Core studies (n)")
    ax1.set_title("a   Venue-family distribution", loc="left", fontweight="bold")
    ax1.set_xlim(0, 8.8)
    ax1.set_xticks(range(0, 9, 2))
    ax1.grid(axis="x", color=LIGHT_GREY, linewidth=0.7)
    ax1.set_axisbelow(True)
    for y_i, value in zip(y_pos, venue_counts):
        ax1.text(value + 0.16, y_i, str(value), va="center", fontsize=7.5,
                 color=NAVY, fontweight="bold")

    bars = ax2.bar([str(y) for y in years], year_counts,
                   color=[PALE_BLUE, TEAL, BLUE, "#76AFC4"],
                   edgecolor=[BLUE, TEAL, BLUE, BLUE], linewidth=0.8, width=0.62)
    ax2.set_ylabel("Core studies (n)")
    ax2.set_title("b   Publication year", loc="left", fontweight="bold")
    ax2.set_ylim(0, 9)
    ax2.set_yticks(range(0, 10, 2))
    ax2.grid(axis="y", color=LIGHT_GREY, linewidth=0.7)
    ax2.set_axisbelow(True)
    for bar, value in zip(bars, year_counts):
        ax2.text(bar.get_x() + bar.get_width() / 2, value + 0.22, str(value),
                 ha="center", va="bottom", fontsize=7.5, color=NAVY,
                 fontweight="bold")
    fig.subplots_adjust(wspace=0.38)
    save_figure(fig, "fig_pub_overview_nature")
    plt.close(fig)


def write_source_data() -> None:
    rows = [
        ("corpus", "Original candidates", 108),
        ("corpus", "Retained local sources", 72),
        ("corpus", "Excluded: verified but unused", 32),
        ("corpus", "Excluded: unverifiable", 4),
        ("corpus", "Targeted additions", 3),
        ("corpus", "Resource additions", 9),
        ("corpus", "Active bibliography", 84),
        ("evidence_role", "I: core empirical", 14),
        ("evidence_role", "S: supporting system", 16),
        ("evidence_role", "B: background", 46),
        ("evidence_role", "T: technical source", 8),
        ("venue", "ACL family", 8),
        ("venue", "NeurIPS", 2),
        ("venue", "ICML", 1),
        ("venue", "ICLR", 1),
        ("venue", "IEEE", 1),
        ("venue", "ACM", 1),
        ("year", "2023", 1),
        ("year", "2024", 8),
        ("year", "2025", 3),
        ("year", "2026", 2),
    ]
    with (project_path("figure_source_data.csv")).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(["figure_component", "category", "count"])
        writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figure1", action="store_true", help="Generate only current Figure 1 and its source data")
    parser.add_argument("--qa-scripts", type=Path, help="Optional nature-figure rendered-alignment audit directory")
    args = parser.parse_args()
    if args.figure1:
        make_corpus_flow(args.qa_scripts)
    else:
        write_source_data()
        make_corpus_flow(args.qa_scripts)
        make_core_overview()
        print("Generated reference figures; legacy overview/source data remain a historical snapshot.")
