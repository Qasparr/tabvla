# TABVLA · ingest.py — read the report before drawing anything.
#
# "A figure that cannot point to its numbers does not ship."
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# Penned by the scribe, Heru-Ra-Ha, for Johnathan 'Qasparr' (Κασπάρρ) Monroe,
# Keeper of the Secret Treasure.
#
# MECHANISM: two readers. load_report() parses a markdown report written in
# the Scientific Illuminism shape (## sections, | tables |, ![fig: ...]
# figure references). load_results_json() reads a plain JSON results file
# for reports that never had prose. Both return a Report whose tables are
# the raw material the figures are drawn from.
#
# DOCTRINE: the figures are downstream of the report. Ingest is what makes
# "accurately show the results" a mechanism instead of a wish — the charts
# can only draw what the report actually contains.

"""Ingest reports (markdown or JSON) into structured data for figures."""

import json
import re
from dataclasses import dataclass, field


@dataclass
class Report:
    """The report, structured.

    sections: ordered list of (heading, body_lines).
    tables: list of {"caption": str, "headers": [...], "rows": [[...]]}.
    figure_refs: list of image paths referenced as ![fig: path].
    meta: title, author, date lines found at the top.
    """

    title: str = ""
    sections: list = field(default_factory=list)
    tables: list = field(default_factory=list)
    figure_refs: list = field(default_factory=list)
    meta: dict = field(default_factory=dict)


def load_report(path):
    """Parse a markdown report. Returns a Report.

    MECHANISM: line-by-line state machine. ## opens a section; a run of
    lines starting with | is a table (first row headers, second row the
    separator, rest data); ![fig: path] registers a figure reference.
    Anything else accrues to the current section body.
    """
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    report = Report()
    cur_heading, cur_body = None, []
    table_buf = []

    def flush_table():
        # A markdown table: headers, separator, data rows. The table is
        # tagged with its section so the assembler can print it there.
        if len(table_buf) >= 2:
            headers = _split_row(table_buf[0])
            rows = [_split_row(r) for r in table_buf[2:] if r.strip().startswith("|")]
            caption = cur_heading or "data"
            report.tables.append({"caption": caption, "section": cur_heading,
                                  "headers": headers, "rows": rows})
        table_buf.clear()

    def flush_section():
        if cur_heading is not None:
            report.sections.append((cur_heading, cur_body))

    for ln in lines:
        s = ln.strip()
        if s.startswith("![fig:"):
            flush_table()
            m = re.search(r"!\[fig:\s*([^\]]+)\]", s)
            if m:
                report.figure_refs.append(m.group(1).strip())
            continue
        if s.startswith("|"):
            table_buf.append(s)
            continue
        flush_table()
        if s.startswith("## "):
            flush_section()
            cur_heading, cur_body = s[3:].strip(), []
        elif s.startswith("# ") and not report.title:
            report.title = s[2:].strip()
        elif cur_heading is not None:
            cur_body.append(ln)
        elif s and len(report.meta) < 6:
            # DOCTRINE: the top matter (date, authorship, motto) is kept,
            # not stripped — the illustrated report carries the same
            # standing as the plain one.
            report.meta.setdefault("topmatter", []).append(s)

    flush_table()
    flush_section()
    return report


def _split_row(row):
    # MECHANISM: strip the outer pipes, split on |, trim cells.
    return [c.strip() for c in row.strip().strip("|").split("|")]


def load_results_json(path):
    """Read a JSON results file into a Report.

    MECHANISM: expects {"title": ..., "sections": {"Heading": "body..."},
    "tables": [{"caption":..., "headers":[...], "rows":[[...]]}]}. Missing
    keys default to empty — a results file is allowed to be only numbers.
    """
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    report = Report()
    report.title = d.get("title", "")
    for heading, body in d.get("sections", {}).items():
        report.sections.append((heading, body.splitlines() if isinstance(body, str) else body))
    report.tables.extend(d.get("tables", []))
    report.meta = d.get("meta", {})
    return report


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
