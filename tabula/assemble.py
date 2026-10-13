# TABVLA · assemble.py — bind the report and its figures into one PDF.
#
# "A figure that cannot point to its numbers does not ship."
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# MECHANISM: build_pdf(report, figures, out_path) renders a title page in
# thelemic form, the report's sections as body text, each figure centered
# with its caption and source line, then an appendix — "Figures and their
# numbers" — where every figure's data table is printed verbatim. The
# appendix is the receipt: any reader can check any bar against its number.
#
# DOCTRINE: the illustrated report must carry the same standing as the
# plain one — same date, same authorship, same rights notice — or the
# pictures become a different document wearing the report's name.

"""Assemble an illustrated PDF: report + gated figures + numbers appendix."""

import os

from fpdf import FPDF


class _Doc(FPDF):
    # MECHANISM: footer carries the standing line on every page, so no
    # page can be quoted out of its rights context.
    def footer(self):
        self.set_y(-14)
        self.set_font("dejavu", "", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "TABVLA illustrated report — All Rights Reserved, Without Prejudice.",
                  align="C")


def build_pdf(report, figures, out_path):
    """Render the full illustrated report. Figures must already be gated.

    MECHANISM: title page (thelemic form) → sections → figures interleaved
    after the body → appendix of figures-and-numbers. Each figure gets a
    page-break check so captions never orphan from their image.
    """
    pdf = _Doc(format="Letter")
    pdf.set_auto_page_break(True, margin=22)
    # MECHANISM: DejaVu Sans is a Unicode TTF — em-dashes, Greek, and the
    # thelemic date all render. Core Helvetica would die on latin-1.
    pdf.add_font("dejavu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    pdf.add_font("dejavu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    pdf.add_font("dejavu", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    W = pdf.w - pdf.l_margin - pdf.r_margin

    def para(text, size=11, style="", color=(20, 20, 20), align="L", after=4):
        pdf.set_font("dejavu", style if style in ("", "B") else "", size)
        pdf.set_text_color(*color)
        pdf.multi_cell(W, size * 0.5, text, align=align,
                       new_x="LMARGIN", new_y="NEXT")
        pdf.ln(after)

    # ---- title page ----
    pdf.add_page()
    pdf.ln(30)
    para(report.title or "Illustrated Report", 22, "B", align="C", after=8)
    para("illustrated by TABVLA — every figure gated on its numbers",
         11, "I", (80, 80, 80), align="C", after=12)
    for line in (report.meta.get("topmatter") or [])[:6]:
        para(line, 10, "", (80, 80, 80), align="C", after=1)
    pdf.ln(10)
    para("Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' "
         "(%s) Monroe, Keeper of the Secret Treasure." % "Κασπάρρ",
         10, "I", (80, 80, 80), align="C", after=2)
    para("93. Live, Love, and let Love, Live.", 10, "I", (80, 80, 80), align="C")

    # ---- body ----
    for heading, body in report.sections:
        pdf.add_page()
        para(heading, 15, "B", after=6)
        for ln in body:
            s = ln.strip()
            if not s:
                pdf.ln(3)
            elif s.startswith("**") and s.endswith("**"):
                para(s.strip("*"), 11, "B", after=3)
            else:
                para(s, 10.5, after=2)
        # Tables belonging to this section print as real tables —
        # DOCTRINE: the numbers appear as a table AND as a chart, so the
        # reader can check the drawing against the list it was drawn from.
        for table in report.tables:
            if table.get("section") != heading:
                continue
            pdf.ln(4)
            pdf.set_font("dejavu", "", 10)
            with pdf.table(first_row_as_headings=True, width=W) as pdf_table:
                hdr = pdf_table.row()
                for h in table["headers"]:
                    hdr.cell(h)
                for r in table["rows"]:
                    row = pdf_table.row()
                    for cell in r:
                        row.cell(cell)
            pdf.ln(4)

    # ---- figures ----
    if figures:
        pdf.add_page()
        para("Figures", 16, "B", after=8)
        for n, fig in enumerate(figures, start=1):
            if pdf.get_y() > pdf.h - 90:
                pdf.add_page()
            para("Figure %d." % n, 11, "B", after=2)
            if fig.image_path and os.path.exists(fig.image_path):
                w = W * 0.94
                x = pdf.l_margin + (W - w) / 2
                if pdf.get_y() + 80 > pdf.h - 40:
                    pdf.add_page()
                pdf.image(fig.image_path, x=x, w=w)
                pdf.ln(3)
            else:
                para("[image not found: %s]" % fig.image_path, 9, "", (150, 0, 0))
            para(fig.caption, 10, "", after=1)
            para("Source: %s" % fig.source, 9, "I", (90, 90, 90), after=8)

    # ---- appendix: figures and their numbers ----
    pdf.add_page()
    para("Appendix — Figures and their numbers", 15, "B", after=4)
    para("Every figure above, with the exact numbers it was drawn from. "
         "Check any bar against its number; they are the same list.",
         10, "I", (80, 80, 80), after=8)
    for n, fig in enumerate(figures, start=1):
        para("Figure %d — %s" % (n, fig.image_path and os.path.basename(fig.image_path)),
             11, "B", after=2)
        para("Source: %s" % fig.source, 9, "I", (90, 90, 90), after=2)
        if fig.data:
            labels = fig.data.get("labels", [])
            values = fig.data.get("values", [])
            rows = ["%s = %s" % (l, v) for l, v in zip(labels, values)]
            # MECHANISM: the numbers printed verbatim — the receipt.
            para(", ".join(rows), 9, "", after=6)
        else:
            para("(illustrative schematic — no measured data; see caption.)",
                 9, "I", (90, 90, 90), after=6)

    pdf.output(out_path)


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
