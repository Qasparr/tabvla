# TABVLA — CLI entry for the deprecated pre-rename package name.
#
# A real file, deliberately: runpy will not execute a sys.modules alias
# under a second name, so `python -m tabula.cli` needs an actual module
# to run. It forwards to the canonical implementation, unchanged.
#
# DEPRECATED: use `python -m tabvla.cli`. See tabula/__init__.py.

"""Deprecated alias: forwards to tabvla.cli."""

import sys

from tabvla.cli import main

if __name__ == "__main__":
    sys.exit(main())
