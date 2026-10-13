# TABVLA · tests/test_provenance.py — the gate, tested.
#
# Sol in 20° 20′ Libra, Luna in 25° 29′ Scorpio, dies martis,
# Anno V:xii e.n. — 93.
#
# MECHANISM: four cases. A good figure passes. A figure with no source
# fails. A figure with no caption fails. A drawing that will not admit it
# is a drawing fails. Run: python3 -m pytest tests/  (or plain python3).
#
# DOCTRINE: the gate is load-bearing; the tests are the receipt that the
# gate holds. If a test fails, the gate is broken and nothing ships.

"""Tests for the provenance gate."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tabula.figures import Figure
from tabula.provenance import gate, ProvenanceError


def _fig(**kw):
    base = dict(image_path="x.png", caption="Weighings.", source="ptk 0.1.0",
                data={"labels": ["A"], "values": [1], "title": "t"})
    base.update(kw)
    return Figure(**base)


def test_good_figure_passes():
    assert gate([_fig()]) is not None


def test_missing_source_fails():
    try:
        gate([_fig(source="")])
    except ProvenanceError:
        return
    raise AssertionError("gate passed a figure with no source")


def test_missing_caption_fails():
    try:
        gate([_fig(caption="  ")])
    except ProvenanceError:
        return
    raise AssertionError("gate passed a figure with no caption")


def test_drawing_must_admit_it_is_a_drawing():
    try:
        gate([_fig(data=None, caption="The structure as seen.")])
    except ProvenanceError:
        return
    raise AssertionError("gate passed a drawing posing as measurement")


def test_honest_schematic_passes():
    f = _fig(data=None, caption="Blueprint schematic (illustrative) of the 9+2 ring.")
    assert gate([f]) is not None


def test_data_mismatch_fails():
    try:
        gate([_fig(data={"labels": ["A", "B"], "values": [1], "title": "t"})])
    except ProvenanceError:
        return
    raise AssertionError("gate passed mismatched labels/values")


if __name__ == "__main__":
    # Plain-python runner: no pytest required.
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print("PASS", fn.__name__)
    print("%d tests passed" % len(fns))


# 93. Live, Love, and let Love, Live.
# All Rights Reserved, Without Prejudice. — Johnathan 'Qasparr' (Κασπάρρ) Monroe
