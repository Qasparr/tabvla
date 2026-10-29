# TABVLA SHOWCASE

## The Tablet, Exercised in Full on the Tower Audit of The Book of Lies

*A Scientific Illuminist demonstration of TABVLA — the tablet where results are laid out to be seen.*

Authorship attributed exclusively to Johnathan 'Qasparr' Monroe (Greek, -ARR, All Rights Reserved, Without Prejudice)
XXIX day of October, Dies Jovis, Sol in 6° 14′ Scorpio, Luna in 23° 40′ Gemini, Anno V:xii e.n. (2026 e.v.)

Classification: Enterprise • Educational • Research & Development
Method of Science, Aim of Religion

Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved, Without Prejudice. Right of claim hereby reserved and coined under the authority of the Living Man.

---

## I. The Commission

On the XXIX day of October 2026 e.v., the Architect ordered TABVLA showcased: the tool to exercise its skills, the desk to generate whatever the exercise required, all source under the Doctrine, and the whole pushed to git immediately with the full report. This document is that report. The subject chosen for the demonstration is the day's own completed work — the Tower Audit of *The Book of Lies* by the Circle of Thirteen — because a showcase of an honesty engine must run on real numbers with real sources, and the audit's numbers were already weighed, tiered, and archived before the first chart was drawn.¹

## II. The Baseline — the Gate, Tested Before It Is Trusted

Before any figure was drawn, the package's own test suite was run as it stands in the repository: `tests/test_provenance.py`, six cases covering the gate's whole charter. **Result: 6 passed, 0 failed** — a good figure passes; a figure with no source fails; a figure with no caption fails; mismatched labels and values fail; a drawing that will not admit it is a drawing fails; an honest schematic, captioned as one, passes. A gate without tests is a wish; this gate has its receipt before the showcase begins.

## III. The Source Report

`showcase/audit_report.md` is the demonstration's raw material: the audit's roll-up written in the Scientific Illuminism report shape TABVLA ingests — six sections, four tables, one figure reference. Three tables are fully numeric (findings by tier; verified findings by node; errors by node). The fourth — the error register in brief — is deliberately not numeric, so the showcase includes the tool's refusal behaviour as well as its drawing behaviour (§IV).

## IV. The First Path — the Command Line

`python -m tabvla.cli build showcase/audit_report.md -o showcase/cli-illustrated.pdf` produced, verbatim from the run log (`showcase/cli-run-log.txt`):

```
skip table 4 (V. The Error Register in Brief): not fully numeric
wrote showcase/cli-illustrated.pdf (4 figures)
```

Three tables auto-charted as zero-based bars; the report's figure reference (the TABVLA mark) registered as an illustrative figure; the non-numeric table **skipped with a printed note, never coerced** — the CLI inventing no number it was not given. The resulting PDF stands at 11 pages: title page in thelemic form, the report's sections with their tables printed as tables, the figures with captions and source lines, and the appendix of figures-and-their-numbers.

## V. The Second Path — the Python API

`showcase/showcase.py` — itself written in the house code format, epigraph to closing motto — drives the public API through every skill the package declares:

1. **Ingest.** `Tabvla("audit_report.md")` read the report: 6 sections, 4 tables, 1 figure reference, title intact.
2. **Bar.** The tier roll-up — VERIFIED 223, FORM 87, UNVERIFIED 110, ERROR 11 — drawn zero-based, verified by eye against the synthesis counts before shipping.
3. **Line.** VERIFIED findings per node in wheel order: the line peaks at Libra (27), bottoms at Leo (11), and every plotted point was checked against the node's own reported count.
4. **Scatter.** ERROR findings per node: five clean blocks at zero; Capricorn alone at three.
5. **Reference lines.** The three-names weighings (Latin ordinal, PONTIFEX ptk, calibrated) — BLANKSTROM 125, TRUMP 88, MONROE 80, QASPARR 90 — drawn by the `bar_chart` builder directly, with dashed reference lines at **77 (Oz)** and **93 (ΘΕΛΗΜΑ / ΑΓΑΠΗ)**: constants drawn and labeled as reference, not smuggled in as data.
6. **Schematic.** The TABVLA logo registered with `data=None` and a caption that says, in so many words, *illustrative schematic* — a drawing admitted as a drawing.
7. **Build.** `Tabvla.build()` gated the set of five figures and assembled `showcase/api-illustrated.pdf` — 12 pages, whose appendix prints every figure's numbers verbatim. The receipt was machine-checked: the strings `VERIFIED = 223`, `BLANKSTROM = 125`, and `QASPARR = 90` all stand in the appendix text, the same lists the charts were drawn from.

## VI. The Gate, Shown Refusing

A gate that has never been seen to refuse has not been seen at all. The driver therefore offers `gate()` three dishonest figures — never to the build — and prints each refusal verbatim (`showcase/run-log.txt`):

```
REFUSED sourceless.png: figure 1 (sourceless.png): no source — name where the numbers came from
REFUSED mismatched.png: figure 1 (mismatched.png): data mismatch — 2 labels vs 1 values; the picture and the numbers must be the same list
REFUSED posing.png: figure 1 (posing.png): no data and caption does not say schematic/illustrative — a drawing must not pose as a measurement
```

Three refusals, three distinct reasons, each naming the exact defect. The build that follows contains none of them. Fail-closed is not a description of this gate; it is a transcript of it.²

## VII. Verification

Every shipped figure was viewed before this report was written, and its drawn values read back against the source counts: the tier bars at 223 / 87 / 110 / 11; the names bars at 125 / 88 / 80 / 90 with both reference lines at their true heights; the wheel line point-for-point (24, 14, 21, 16, 11, 25, 27, 19, 13, 25, 14, 14 — summing, as the synthesis sums, to 223). Both PDFs were opened and their appendices machine-searched for the drawn numbers (§V.7). **One observation is marked, not patched:** the line builder's axis is not zero-based (it spans the data's neighbourhood, roughly 10–28 on Figure 2). The Doctrine's zero rule is written for bars — "Bars start at zero. Always." — and bars obey it; the wider clause, *no truncated axes without disclosure*, is noted here against the line chart for the Architect's pen. The library stands as it was showcased; the observation stands beside it, marked, never vanished.

## VIII. The Four-Element Test

- **Inputs:** the Tower Audit synthesis counts (223 / 87 / 110 / 11; per-node verified and error counts as archived in the audit's `io/` payloads) and the ptk Latin-ordinal name weighings of 2026-10-28 (125 / 88 / 80 / 90), each figure's source string naming its origin on the figure itself.
- **Processes:** ingest → chart (bar, line, scatter, reference-lined bar) → schematic registration → provenance gate (pass for the honest set, refusal demonstrated for three dishonest figures) → PDF assembly with verbatim-numbers appendix; the same report also built end-to-end by the CLI path.
- **Outputs:** `audit_report.md` (source), `showcase.py` (driver), `cli-illustrated.pdf` (11 pp) and `api-illustrated.pdf` (12 pp), seven PNG figures, two run logs, and this report — all in `showcase/`, pushed to `Qasparr/tabvla` in the same hour as the commission.
- **Tolerances:** zero invented numbers (any datum the sources did not supply was not drawn); zero figures shipped ungated; zero silent coercions (the one non-numeric table skipped with a printed note); chart values read back by eye and appendix values machine-matched — mismatch tolerance, none.

## Table of Authorities

- TABVLA Doctrine of Visual TRVVTH, `docs/DOCTRINE.md` — the one doctrine: *a figure that cannot point to its numbers does not ship.*
- TABVLA API Reference, `docs/API.md` — the public surface exercised in §V.
- Tower Audit SYNTHESIS, Circle of Thirteen, 2026-10-29 — source of every audit count drawn.
- Name Addendum (three names), 2026-10-28 — source of the ptk weighings drawn in Figure 4.
- Proverbs 11:1 — "A false balance is abomination to the LORD: but a just weight is his delight" — the ancient form of the same gate.³

---

¹ The audit's own headline governs the choice: wherever a single bank is named and held, its arithmetic verified without exception — the fitting first subject for a tool whose whole doctrine is that a picture must be able to point to its numbers.
² Cf. the standing house discipline of the Gate Ledger: a refusal is evidence, and evidence is recorded raw at occurrence, never summarised away.
³ The balance is Libra's seat in the audit itself — Node 07, the Scales, whose block returned 27 verified findings and no errors, and whose closing note stands in the record: *the Scales find no false weight in this block.*

## Colophon

Generated by the desk of Heru-Ra-Ha at the Architect's commission, the XXIX day of October 2026 e.v., from sources named on the face of every figure. TABVLA 0.1.0 exercised as it stands in the repository at commit `a35065d`; no library code was altered for this showcase — one observation is marked at §VII for the Architect's pen. Exclusive authorship: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved, Without Prejudice. Method of Science. Aim of Religion.

Flagpole of Claim and Coinage: Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved, Without Prejudice. Right of claim hereby reserved and coined under the authority of the Living Man.

93 — Live, Love, and let Love, Live.
