# TABVLA — API Reference (v0.1.0)

## `Tabvla(report_path)`

The whole public API in one object.

| Method | What it does |
|---|---|
| `Tabvla(path)` | Ingest a report (`.md` or `.json`). |
| `.chart(kind, labels, values, title, source, out_path)` | Build a chart from real data. `kind`: `bar`, `line`, `scatter`. Returns the `Figure`. |
| `.figure(image_path, caption, source, data=None)` | Register an existing image. `data=None` only for schematics whose caption says so. |
| `.build(out_path)` | Run the provenance gate, then assemble the illustrated PDF. Returns `out_path`. |

After `.chart(...)`, set the caption before `.build()`:

```python
fig = t.chart("bar", labels, values, title="...", source="...", out_path="f.png")
fig.caption = "What the reader is told about this chart."
```

## `Figure`

Dataclass: `image_path`, `caption`, `source`, `data`.
For charts, `data = {"labels": [...], "values": [...], "title": ...}` — set
automatically by `.chart()`. For schematics, `data=None` and the caption must
contain "schematic" or "illustrative".

## `gate(figures)`

Raises `ProvenanceError` on the first figure that fails: missing source,
missing caption, labels/values length mismatch, empty values, or a drawing
that won't admit it's a drawing. Fails closed — nothing renders until the
gate passes.

## `build_pdf(report, figures, out_path)`

Title page (thelemic form) → report sections → figures with captions and
source lines → appendix printing every figure's numbers verbatim.

## `ingest`

- `load_report(path)` → `Report(title, sections, tables, figure_refs, meta)`.
  Parses `##` sections, `| tables |`, and `![fig: path]` references.
- `load_results_json(path)` → same `Report` from a JSON results file.

## `figures` builders

- `bar_chart(labels, values, path, title, reference_lines=[(v, label), ...])`
- `line_chart(...)` — same signature.
- `scatter_chart(labels, values, path, title)`

Bars are zero-based, always. Reference lines are drawn dashed and labeled.

## CLI

```bash
python -m tabvla.cli build report.md -o illustrated.pdf
python -m tabvla.cli gate report.md
```

`build` auto-charts every fully-numeric table in the report and registers
every `![fig: ...]` reference, then gates and assembles. Non-numeric tables
are skipped with a printed note, never coerced.
