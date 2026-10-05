"""Generate the reference-corpus and core-study summary figures."""

from pathlib import Path
import csv

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


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
        fig.savefig(ROOT / f"{stem}{suffix}", bbox_inches="tight", facecolor="white", **kwargs)


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


def make_corpus_flow() -> None:
    # Transparent verification reduced 108 local candidates to 72 retained
    # sources; targeted updates and the resource map add 12 active sources.
    fig, ax = plt.subplots(figsize=(7.2, 3.05))
    ax.set_axis_off()

    rounded_box(ax, (0.025, 0.57), 0.20, 0.25, PALE_BLUE, BLUE,
                "108 candidates", "pre-audit local bibliography")
    rounded_box(ax, (0.31, 0.57), 0.20, 0.25, PALE_TEAL, TEAL,
                "72 retained", "cited and source-verified")
    rounded_box(ax, (0.595, 0.57), 0.17, 0.25, PALE_BLUE, BLUE,
                "+12 additions", "targeted update and\nresource coverage")
    rounded_box(ax, (0.82, 0.57), 0.155, 0.25, "#DDEEF4", NAVY,
                "84 active", "final bibliography")

    arrow = dict(arrowstyle="-|>", color=NAVY, lw=1.3, mutation_scale=12)
    ax.annotate("", xy=(0.305, 0.695), xytext=(0.23, 0.695),
                xycoords=ax.transAxes, arrowprops=arrow)
    ax.annotate("", xy=(0.59, 0.695), xytext=(0.515, 0.695),
                xycoords=ax.transAxes, arrowprops=arrow)
    ax.annotate("", xy=(0.815, 0.695), xytext=(0.77, 0.695),
                xycoords=ax.transAxes, arrowprops=arrow)

    ax.annotate("", xy=(0.225, 0.39), xytext=(0.225, 0.57),
                xycoords=ax.transAxes,
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.0))
    ax.text(0.145, 0.46, "36 excluded", ha="center", va="center",
            fontsize=8, color=ORANGE, transform=ax.transAxes)
    ax.text(0.225, 0.27, "32 not used in the manuscript\n4 unverifiable records",
            ha="center", va="center", fontsize=7.2, color=GREY,
            transform=ax.transAxes)

    roles = [("I", 14, "core empirical studies", TEAL),
             ("S", 16, "supporting systems", BLUE),
             ("B", 46, "background methods", GREY),
             ("T", 8, "technical sources", ORANGE)]
    x0, total_width, y, height = 0.42, 0.555, 0.17, 0.13
    cursor = x0
    for code, count, label, color in roles:
        width = total_width * count / 84
        ax.add_patch(FancyBboxPatch(
            (cursor, y), width, height,
            boxstyle="round,pad=0.006,rounding_size=0.012",
            linewidth=0.8, edgecolor="white", facecolor=color,
            transform=ax.transAxes,
        ))
        ax.text(cursor + width / 2, y + height / 2, f"{code}: {count}",
                ha="center", va="center", color="white", fontsize=7.3,
                fontweight="bold", transform=ax.transAxes)
        cursor += width
    ax.text(x0, 0.08,
            "Evidence roles: I = included empirical study; S = supporting system; "
            "B = background; T = technical source",
            ha="left", va="center", fontsize=6.9, color=GREY,
            transform=ax.transAxes)

    save_figure(fig, "fig_reference_corpus")
    plt.close(fig)


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
    with (ROOT / "figure_source_data.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(["figure_component", "category", "count"])
        writer.writerows(rows)


if __name__ == "__main__":
    write_source_data()
    make_corpus_flow()
    make_core_overview()
    print("Generated reference figures and source data.")
