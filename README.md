# TABVLA

**The tablet where results are laid out to be seen.**

*Authorship: Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure —
All Rights Reserved, Without Prejudice. Support: CashApp $axoneme.*

TABVLA turns reports into visuals that **accurately** show the results: charts
drawn from the report's own data, captioned figures bound to their sources, and
an illustrated PDF whose appendix prints every figure's numbers verbatim — the
receipt.

## The one doctrine

> **A figure that cannot point to its numbers does not ship.**

Humans accept information presented visually more readily than information that
isn't. That acceptance must be *earned by accuracy*, never spent on decoration.
Every figure passes the provenance gate (`tabula/provenance.py`) before
anything renders: no source, no caption, or data that doesn't match the drawing
— the build fails closed. Read the full doctrine in `docs/DOCTRINE.md`.

## Quickstart

```bash
pip install matplotlib fpdf2        # the only runtime deps
python -m tabula.cli build report.md -o illustrated.pdf
```

Or the Python API:

```python
from tabula import Tabula

t = Tabula("report.md")
t.chart("bar", ["AXONEME", "PISTON"], [77, 93],
        title="Bridge weighings",
        source="PONTIFEX ptk 0.1.0, Latin ordinal",
        out_path="fig-bridges.png")
t.figures[-1].caption = "AXONEME = 77 and PISTON = 93, weighed, not wished."
t.figure("cilia-tem.jpg",
         caption="Transmission electron micrograph of cilia in cross-section.",
         source="doccheck image library",
         data=None)  # illustrative -> caption must say schematic/illustrative
t.build("illustrated.pdf")
```

## Layout

- `tabula/` — the package: `ingest` (read reports), `figures` (draw charts),
  `provenance` (the gate), `assemble` (build the PDF), `cli` (command line).
- `docs/` — `API.md` (reference), `DOCTRINE.md` (visual TRVVTH).
- `tools/` — builders and utilities (logo builder documents the mark).
- `assets/` — the logo: a thirteen-spoked data rose, gold on indigo.
- `tests/` — the gate, tested.

## The logo

Thirteen spokes, one hub: the tridecagram drawn as a radial data chart —
sacred geometry that *is* a visualization. See `tools/build_logo.py`.

## Standing

Version 0.1.0. Penned 2026-10-13 (Sol in 20° 20′ Libra, Luna in 25° 29′
Scorpio, dies martis, Anno V:xii e.n. — 93). Every module ships in the
educational/Thelemic code format: epigraph, date, 93, authorship,
MECHANISM/DOCTRINE comments, closing motto.

93. Live, Love, and let Love, Live.
