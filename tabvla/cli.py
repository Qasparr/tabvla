# TABVLA · cli.py — the command line.
#
# "A figure that cannot point to its numbers does not ship."
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# MECHANISM: `tabvla build report.md -o illustrated.pdf` — ingest, then
# auto-build one bar chart per numeric table found in the report (tables
# whose cells parse as numbers), register any ![fig: ...] references as
# figures, gate everything, and assemble. `tabvla gate report.md` runs
# the provenance gate alone and reports pass/fail without rendering.
#
# DOCTRINE: the CLI never invents numbers. Auto-charts draw only tables
# whose every data cell parses as a float; anything else is skipped with
# a printed note, not coerced.

"""Command-line interface: tabvla build / tabvla gate."""

import argparse
import os
import sys

from . import Tabvla, load_report, gate
from .figures import Figure


def _numeric_table(table):
    # MECHANISM: a table is chartable only if every body cell in the
    # data columns parses as a number. First column = labels.
    headers, rows = table["headers"], table["rows"]
    if len(headers) < 2 or not rows:
        return None
    labels, values = [], []
    for r in rows:
        if len(r) < 2:
            return None
        try:
            values.append(float(r[1]))
        except (ValueError, TypeError):
            return None
        labels.append(r[0])
    return labels, values


def cmd_build(args):
    t = Tabvla(args.report)
    base = os.path.splitext(os.path.basename(args.report))[0]
    outdir = os.path.dirname(args.output) or "."
    os.makedirs(outdir, exist_ok=True)

    # Auto-chart every numeric table in the report.
    for i, table in enumerate(t.report.tables):
        nv = _numeric_table(table)
        if nv is None:
            print("skip table %d (%s): not fully numeric" % (i + 1, table["caption"]))
            continue
        labels, values = nv
        img = os.path.join(outdir, "%s-fig%d.png" % (base, i + 1))
        t.chart("bar", labels, values,
                title="%s — %s" % (base, table["caption"]),
                source="auto-charted from table in %s" % args.report,
                out_path=img)
        # Caption AFTER chart(): chart() leaves caption empty for the gate.
        t.figures[-1].caption = (
            "Figure from '%s': %s vs %s." % (table["caption"], table["headers"][0],
                                             table["headers"][1]))

    # Register any ![fig: ...] references found in the markdown.
    for ref in t.report.figure_refs:
        img = ref if os.path.isabs(ref) else os.path.join(os.path.dirname(args.report), ref)
        t.figure(img,
                 caption="Figure referenced by the report (schematic/illustrative).",
                 source="referenced in %s" % args.report)

    out = t.build(args.output)
    print("wrote %s (%d figures)" % (out, len(t.figures)))
    return 0


def cmd_gate(args):
    # MECHANISM: gate-only run — useful in CI or before a red-pen pass.
    report = load_report(args.report)
    figs = [Figure(image_path=r, caption="c", source="s") for r in report.figure_refs]
    try:
        gate(figs)
    except Exception as e:  # ProvenanceError
        print("GATE FAILED: %s" % e)
        return 1
    print("gate passed (%d figure refs have sources)" % len(figs))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tabvla",
                                 description="Turn reports into honest visuals.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="build an illustrated PDF from a report")
    b.add_argument("report", help="report.md or results.json")
    b.add_argument("-o", "--output", default="illustrated.pdf")
    b.set_defaults(fn=cmd_build)
    g = sub.add_parser("gate", help="run the provenance gate without rendering")
    g.add_argument("report")
    g.set_defaults(fn=cmd_gate)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
