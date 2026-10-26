# TABVLA — the tablet where results are laid out to be seen.
#
# "A figure that cannot point to its numbers does not ship."
# — the visual TRVVTH doctrine
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# METHOD (Scientific Illuminism): hypothesis → method → observation → result.
# This package is the method made executable: a report goes in, and figures
# that honestly show the results come out. Every figure carries its data
# provenance — the gate in provenance.py refuses any figure that cannot
# point to the numbers it displays.
#
# MECHANISM: the Tabvla class is the whole public API. It ingests a report
# (markdown or JSON), builds charts from real data, binds captioned figures
# to their sources, and assembles an illustrated PDF whose appendix maps
# every figure back to its numbers.
#
# DOCTRINE: visuals persuade; therefore visuals must be true. A chart is a
# claim drawn in ink. TRVVTH gates claims, so TRVVTH gates charts.

"""TABVLA — turn reports into visuals that accurately show the results."""

from .ingest import Report, load_report, load_results_json
from .figures import Figure, bar_chart, line_chart, scatter_chart
from .provenance import ProvenanceError, gate
from .assemble import build_pdf

__version__ = "0.1.0"
__all__ = [
    "Tabvla",
    "Tabula",  # backwards-compatible alias (see below)
    "Report",
    "Figure",
    "ProvenanceError",
    "load_report",
    "load_results_json",
    "bar_chart",
    "line_chart",
    "scatter_chart",
    "gate",
    "build_pdf",
    "__version__",
]


class Tabvla:
    """The tablet. One object, one report, honest figures.

    MECHANISM: holds the ingested Report and the list of Figures built
    from it. Nothing renders until build() runs the provenance gate —
    fail-closed, like everything else in the house.
    """

    def __init__(self, report_path):
        # DOCTRINE: ingest first, so every figure is born from the report's
        # own data, never from decoration invented after the fact.
        # MECHANISM: .json reports go through the JSON reader; everything
        # else through the markdown reader.
        if report_path.lower().endswith(".json"):
            self.report = load_results_json(report_path)
        else:
            self.report = load_report(report_path)
        self.figures = []

    def chart(self, kind, labels, values, title, source, out_path):
        """Build a chart from real data and register it as a Figure.

        MECHANISM: the numbers pass through untouched — labels[i] is drawn
        at values[i], full stop. The source string names where the numbers
        came from (e.g. 'PONTIFEX ptk 0.1.0, Latin ordinal weighings').
        """
        builders = {"bar": bar_chart, "line": line_chart, "scatter": scatter_chart}
        if kind not in builders:
            raise ValueError("unknown chart kind: %r (bar, line, scatter)" % kind)
        fig = builders[kind](labels, values, out_path, title=title)
        fig.source = source
        # DOCTRINE: the data rides with the figure — the caption and the
        # appendix both read from here, so the numbers can never drift.
        fig.data = {"labels": list(labels), "values": list(values), "title": title}
        self.figures.append(fig)
        return fig

    def figure(self, image_path, caption, source, data=None):
        """Register an existing image (micrograph, schematic, plate).

        MECHANISM: even a found image must declare its source and, where
        applicable, the data it shows. data=None is allowed only for
        illustrative schematics — and the caption must say so.
        """
        fig = Figure(image_path=image_path, caption=caption, source=source, data=data)
        self.figures.append(fig)
        return fig

    def build(self, out_path):
        """Gate, then assemble. Returns the output path.

        MECHANISM: gate() raises ProvenanceError on the first figure that
        cannot point to its numbers. No partial PDFs, no silent drops —
        fail-closed.
        """
        gate(self.figures)
        build_pdf(self.report, self.figures, out_path)
        return out_path


# Backwards-compatible alias: code written against the pre-rename name
# (Tabula, before the inscriptional-orthography rename of 2026-10-25)
# keeps working. New code uses Tabvla.
Tabula = Tabvla


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
