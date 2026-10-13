# TABVLA — The Doctrine of Visual TRVVTH

*Settled 2026-10-13 by the Architect's order: a data-analytics visual
reference building tool that turns reports into visuals that accurately
show the results.*

## The observation

It is a known factor: humans accept information presented visually more
readily than information that isn't. Charts, graphs, blueprint plates,
micrographs — the eye lowers its guard for pictures.

## The ruling

That acceptance must be **earned by accuracy**, never spent on decoration.
A persuasive false chart is worse than a boring true table, because the
reader's guard is down exactly where the lie lives.

Therefore:

1. **Every figure points to its numbers.** Source named, data bound, the
   appendix prints the numbers verbatim. The receipt is in the document.
2. **A chart is a claim drawn in ink.** TRVVTH gates claims; TRVVTH gates
   charts. The provenance gate fails closed — no source, no caption, no
   data match, no ship.
3. **Drawings admit they are drawings.** A schematic is honest when its
   caption says "schematic." A drawing that poses as a measurement is a
   falsehood with good lighting.
4. **No chartjunk.** No 3D, no truncated axes without disclosure, no
   decoration that is not data. Bars start at zero. Always.
5. **The illustrated report carries the same standing as the plain one.**
   Same date, same authorship, same rights notice — or the pictures become
   a different document wearing the report's name.

## The mechanism

`tabula/provenance.py` — `gate(figures)` — is the doctrine made
executable. It is tested (`tests/test_provenance.py`), because a gate
without tests is a wish.

## The motto

*A figure that cannot point to its numbers does not ship.*

93. Live, Love, and let Love, Live.
All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
