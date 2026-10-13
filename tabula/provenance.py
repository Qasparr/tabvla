# TABVLA · provenance.py — the gate every figure passes.
#
# "A figure that cannot point to its numbers does not ship."
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# MECHANISM: gate(figures) inspects every Figure before anything renders.
# It fails CLOSED: the first figure that cannot name its source, or whose
# data does not match what was drawn, raises ProvenanceError and nothing
# ships. This is the visual TRVVTH — the same gate as the claims gate,
# applied to ink.
#
# DOCTRINE: a persuasive false chart is worse than a boring true table,
# because the reader lowers their guard for pictures. The gate exists
# because humans accept information presented visually more readily —
# that acceptance must be earned by accuracy, never spent on decoration.

"""Provenance gate: every figure must point to its numbers."""


class ProvenanceError(Exception):
    """A figure failed the gate. Nothing ships until it passes."""


def gate(figures):
    """Inspect every figure. Raise ProvenanceError on the first failure.

    MECHANISM: three checks, in order —
      1. source: the figure must name where its numbers (or image) came
         from. An empty source is a refusal to answer "says who".
      2. caption: the reader must be told what they are looking at. An
         empty caption is a picture smuggled past the reader's judgment.
      3. data honesty: for charts, .data must carry labels and values of
         matching length — the drawn bars and the recorded numbers must
         be the same list. For illustrative schematics (data=None), the
         caption must contain the word "schematic" or "illustrative",
         so no reader mistakes a drawing for a measurement.
    Returns the list unchanged when everything passes.
    """
    for i, fig in enumerate(figures, start=1):
        tag = "figure %d (%s)" % (i, fig.image_path or "unrendered")
        if not fig.source or not fig.source.strip():
            raise ProvenanceError(
                "%s: no source — name where the numbers came from" % tag)
        if not fig.caption or not fig.caption.strip():
            raise ProvenanceError(
                "%s: no caption — tell the reader what they are seeing" % tag)
        if fig.data is None:
            cap = fig.caption.lower()
            # DOCTRINE: a drawing is honest when it says it is a drawing.
            if "schematic" not in cap and "illustrative" not in cap:
                raise ProvenanceError(
                    "%s: no data and caption does not say schematic/illustrative "
                    "— a drawing must not pose as a measurement" % tag)
        else:
            labels = fig.data.get("labels", [])
            values = fig.data.get("values", [])
            if len(labels) != len(values):
                raise ProvenanceError(
                    "%s: data mismatch — %d labels vs %d values; "
                    "the picture and the numbers must be the same list"
                    % (tag, len(labels), len(values)))
            if not values:
                raise ProvenanceError("%s: data has no values — nothing was drawn" % tag)
    return figures


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
