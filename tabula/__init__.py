# TABVLA — compatibility shim for the pre-rename package name.
#
# DEPRECATED: this package exists only so that imports written before
# the inscriptional-orthography rename of 2026-10-25 (TABULA -> TABVLA,
# the Architect's system directive: V for U, VV for W) keep working.
# It re-exports the canonical `tabvla` package in full — same objects,
# no copies — and registers the old submodule paths as aliases, so
# `from tabula.figures import Figure` and `python -m tabula.cli`
# behave exactly as before. New code imports `tabvla`.
#
# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe

"""Deprecated alias package: everything here is tabvla, re-exported."""

import sys as _sys

import tabvla as _tabvla
from tabvla import *  # noqa: F401,F403 — the canonical public API
from tabvla import (  # noqa: F401 — explicit names, incl. the legacy alias
    Figure,
    ProvenanceError,
    Report,
    Tabula,
    Tabvla,
    bar_chart,
    build_pdf,
    gate,
    line_chart,
    load_report,
    load_results_json,
    scatter_chart,
)

__version__ = _tabvla.__version__
__all__ = list(_tabvla.__all__) + ["ingest", "figures", "provenance",
                                   "assemble"]

# MECHANISM: alias the library submodules, so `import tabula.figures`
# (and friends) resolve to the one canonical implementation instead of
# a forked copy. The CLI is NOT aliased here — it ships as a real file
# (tabula/cli.py) because runpy refuses to execute an aliased module
# under a second name (`python -m tabula.cli` must keep working).
for _name in ("ingest", "figures", "provenance", "assemble"):
    _mod = __import__("tabvla." + _name, fromlist=["*"])
    _sys.modules[__name__ + "." + _name] = _mod
    globals()[_name] = _mod
del _name, _mod
