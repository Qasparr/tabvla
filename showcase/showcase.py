# TABVLA · showcase/showcase.py — the tablet, exercised in full.
#
# "A figure that cannot point to its numbers does not ship."
#
# XXIX day of October, Dies Jovis, Sol in 6° 14′ Scorpio,
# Luna in 23° 40′ Gemini, Anno V:xii e.n. (2026 e.v.) — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure, at the Architect's commission of the same
# day: "get TABVLA to showcase its skills … use the Doctrine for all source
# and push to git immediately with the full report."
#
# MECHANISM: this driver walks every public skill of the package, in the
# order a reader meets them —
#   1. INGEST   — Tabvla() reads audit_report.md (the Tower Audit roll-up).
#   2. BAR      — the tier roll-up, drawn from the synthesis counts.
#   3. LINE     — VERIFIED findings per node, in wheel order.
#   4. SCATTER  — ERROR findings per node, one point per node.
#   5. REFERENCE LINES — the three-names weighings against the two house
#      constants, 77 (Oz) and 93 (ΘΕΛΗΜΑ / ΑΓΑΠΗ), drawn dashed by the
#      figures.bar_chart builder directly, then registered by hand.
#   6. SCHEMATIC — the TABVLA logo registered as what it is: an
#      illustrative mark carrying no measured data (data=None), its
#      caption saying so, as the Doctrine requires.
#   7. THE GATE, FAIL-CLOSED — three dishonest figures are offered to
#      gate() alone (never to the build): no source; mismatched data;
#      a drawing posing as a measurement. Each refusal is caught and its
#      ProvenanceError printed verbatim — the refusals are part of the
#      showcase, because a gate that has never been seen to refuse has
#      not been seen at all.
#   8. BUILD    — Tabvla.build() gates the honest set and assembles the
#      illustrated PDF, appendix printing every figure's numbers verbatim.
#
# DOCTRINE: every number below is copied from a named source and the
# source string rides on the figure itself — audit counts from the Tower
# Audit SYNTHESIS (Circle of Thirteen, 2026-10-29); name weighings from
# PONTIFEX ptk, Latin ordinal bank, calibrated 2026-10-28. Nothing here
# is invented for the drawing; where the drawing needed a number the
# audit did not supply, the drawing was not made.

"""TABVLA showcase driver — every skill, exercised on real audit data."""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

from tabvla import Tabvla, Figure, ProvenanceError, gate
from tabvla.figures import bar_chart

AUDIT_SRC = ("Tower Audit of The Book of Lies — SYNTHESIS.md, Circle of "
             "Thirteen roll-up, 2026-10-29")
PTK_SRC = ("PONTIFEX ptk, Latin ordinal bank, calibrate True, weighed "
           "2026-10-28 (Name Addendum, three names)")

# The wheel, in order. Counts are the nodes' own reported counts, as the
# synthesis prints them — summed there, re-summed here by the appendix.
NODES = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
         "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
VERIFIED = [24, 14, 21, 16, 11, 25, 27, 19, 13, 25, 14, 14]   # sums to 223
ERRORS = [1, 1, 2, 2, 0, 0, 0, 1, 1, 3, 0, 0]                # sums to 11


def out(name):
    return os.path.join(HERE, name)


def main():
    t = Tabvla(os.path.join(HERE, "audit_report.md"))
    print("ingested: %r — %d sections, %d tables, %d figure refs"
          % (t.report.title, len(t.report.sections), len(t.report.tables),
             len(t.report.figure_refs)))

    # --- 2. BAR: the tier roll-up -------------------------------------
    fig = t.chart("bar", ["VERIFIED", "FORM", "UNVERIFIED", "ERROR"],
                  [223, 87, 110, 11],
                  title="Tower Audit — findings by tier",
                  source=AUDIT_SRC, out_path=out("fig1-tiers.png"))
    fig.caption = ("Findings by tier across the twelve zodiac nodes: "
                   "VERIFIED 223, FORM 87, UNVERIFIED 110, ERROR 11 "
                   "(+2 conditional, counted in the synthesis, not drawn).")

    # --- 3. LINE: verified findings across the wheel ------------------
    fig = t.chart("line", NODES, VERIFIED,
                  title="Verified findings per node, in wheel order",
                  source=AUDIT_SRC, out_path=out("fig2-verified-line.png"))
    fig.caption = ("VERIFIED findings per node, Aries through Pisces. "
                   "Libra's block weighs heaviest at 27; Leo's lightest "
                   "at 11, its weight sitting in FORM and UNVERIFIED.")

    # --- 4. SCATTER: errors per node ----------------------------------
    fig = t.chart("scatter", NODES, ERRORS,
                  title="Error findings per node",
                  source=AUDIT_SRC, out_path=out("fig3-errors-scatter.png"))
    fig.caption = ("ERROR findings per node. Five nodes returned clean "
                   "blocks (Leo, Virgo, Libra, Aquarius, Pisces); "
                   "Capricorn's block carries three.")

    # --- 5. REFERENCE LINES: the three names against 77 and 93 --------
    # MECHANISM: Tabvla.chart() does not take reference lines, so the
    # builder is called directly and the Figure registered by hand —
    # the same Figure record, the same gate, no side door.
    fig = bar_chart(["BLANKSTROM", "TRUMP", "MONROE", "QASPARR"],
                    [125, 88, 80, 90],
                    out("fig4-names.png"),
                    title="The three names, weighed — Latin ordinal",
                    reference_lines=[(77, "77 — Oz"),
                                     (93, "93 — Thelema / Agape")])
    fig.source = PTK_SRC
    fig.data = {"labels": ["BLANKSTROM", "TRUMP", "MONROE", "QASPARR"],
                "values": [125, 88, 80, 90],
                "title": "The three names, weighed — Latin ordinal"}
    fig.caption = ("Surname weighings, Latin ordinal: BLANKSTROM 125, "
                   "TRUMP 88, MONROE 80; the pen name QASPARR 90. Dashed "
                   "reference lines at 77 (Oz) and 93 (Thelema, Agape) — "
                   "drawn, labeled, and not part of the data.")
    t.figures.append(fig)

    # --- 6. SCHEMATIC: the mark, admitted as a mark -------------------
    t.figure(os.path.join(HERE, "..", "assets", "tabvla-logo.png"),
             caption=("The TABVLA mark — a thirteen-spoked data rose, "
                      "gold on indigo. Illustrative schematic: the logo "
                      "carries no measured data and claims none."),
             source="tabvla repository assets/tabvla-logo.png "
                    "(tools/build_logo.py)",
             data=None)

    # --- 7. THE GATE, FAIL-CLOSED: three refusals, verbatim -----------
    print("\n--- the gate, shown refusing (these never reach the build) ---")
    dishonest = [
        Figure(image_path="sourceless.png", caption="A chart.",
               source="",
               data={"labels": ["A"], "values": [1], "title": "t"}),
        Figure(image_path="mismatched.png", caption="A chart.",
               source="named, but the numbers do not match the drawing",
               data={"labels": ["A", "B"], "values": [1], "title": "t"}),
        Figure(image_path="posing.png",
               caption="The structure as measured in the field.",
               source="a drawing, offered as a measurement",
               data=None),
    ]
    for bad in dishonest:
        try:
            gate([bad])
            print("GATE PASSED %s — THIS MUST NOT HAPPEN" % bad.image_path)
            return 1
        except ProvenanceError as e:
            print("REFUSED %s: %s" % (bad.image_path, e))

    # --- 8. BUILD ------------------------------------------------------
    pdf = t.build(out("api-illustrated.pdf"))
    print("\nwrote %s (%d figures, gate passed)" % (pdf, len(t.figures)))
    return 0


if __name__ == "__main__":
    sys.exit(main())


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
