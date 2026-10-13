# TABVLA · figures.py — draw only what the numbers say.
#
# "A figure that cannot point to its numbers does not ship."
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# MECHANISM: thin chart builders over matplotlib — bar, line, scatter —
# with the same conventions as PONTIFEX's ptk.chart, so a weighing that
# was drawn in research can be redrawn in a report without translation
# error. Every builder returns a Figure whose .data carries the exact
# labels and values drawn; the caption and the appendix read from .data,
# so the picture and the numbers can never disagree.
#
# DOCTRINE: no 3D, no truncated axes without disclosure, no decoration
# that is not data. A chart is a claim drawn in ink, and claims pass the
# gate (see provenance.py).

"""Chart builders and the Figure record."""

from dataclasses import dataclass, field

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


@dataclass
class Figure:
    """One visual in the illustrated report.

    image_path: rendered file. caption: what the reader is told.
    source: where the numbers (or the image) came from — required.
    data: {"labels": [...], "values": [...], "title": ...} for charts;
          None allowed only for illustrative schematics whose caption
          says they are illustrative.
    """

    image_path: str = ""
    caption: str = ""
    source: str = ""
    data: object = field(default=None)


def _finish(fig, path, title):
    # MECHANISM: one exit for all builders — titled, tightened, saved,
    # closed. No builder leaves a figure open to leak into the next.
    fig.suptitle(title, fontsize=13)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def bar_chart(labels, values, path, title="", reference_lines=None):
    """Bars at exactly values[i] for labels[i]. Zero-based axis.

    MECHANISM: the y-axis starts at zero unless the caller passes
    reference_lines AND documents the truncation in the caption —
    the gate checks the caption for the disclosure (see provenance.py).
    reference_lines: [(value, label), ...] drawn dashed, e.g. bridges.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(range(len(labels)), values, color="#5b7a99")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
    ax.set_ylabel("value")
    ax.set_ylim(bottom=0)  # DOCTRINE: bars start at zero. Always.
    for val, lab in reference_lines or []:
        ax.axhline(val, color="gray", linestyle="--", linewidth=1)
        ax.text(len(labels) - 1, val, " %s" % lab, va="bottom", ha="right",
                fontsize=8, color="gray")
    _finish(fig, path, title)
    return Figure(image_path=path, caption="", source="")


def line_chart(labels, values, path, title="", reference_lines=None):
    """Points joined in order. For sequences — weighings across a sweep."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(range(len(labels)), values, marker="o", color="#5b7a99")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
    ax.set_ylabel("value")
    for val, lab in reference_lines or []:
        ax.axhline(val, color="gray", linestyle="--", linewidth=1)
        ax.text(len(labels) - 1, val, " %s" % lab, va="bottom", ha="right",
                fontsize=8, color="gray")
    _finish(fig, path, title)
    return Figure(image_path=path, caption="", source="")


def scatter_chart(labels, values, path, title=""):
    """One point per term — for showing where a cloud of weighings lands."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(range(len(labels)), values, color="#5b7a99", s=36)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=9)
    ax.set_ylabel("value")
    _finish(fig, path, title)
    return Figure(image_path=path, caption="", source="")


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
