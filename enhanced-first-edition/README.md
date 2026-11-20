# MYP Mathematics — Enhanced Original First Edition

Five complete coursebooks with original, section-level practice interleaved into the 2026 first editions. The production inputs are **only** the validated first-edition page masters and the new sources in this folder. The original covers, body, worked examples, investigations, assessments, answers and indexes remain in their original order. The enhanced PDFs add an edition guide, integrated practice and a separately labelled worked-answer section, not a detachable exercise booklet.

| Year | Original first-edition page master | Original pages | Practice pages | New exercises / parts | Enhanced PDF |
|---|---|---:|---:|---:|---|
| 1 | [`MYP-Mathematics-1-Student-Coursebook.pdf`](../MYP-Mathematics-1-Student-Coursebook.pdf) | 240 | 45 | 90 / 270 | [MYP1 PDF](books/MYP1-Student-Coursebook-Enhanced-Original-First-Edition.pdf) |
| 2 | [`MYP-Mathematics-2-Student-Coursebook.pdf`](../MYP-Mathematics-2-Student-Coursebook.pdf) | 260 | 42 | 84 / 252 | [MYP2 PDF](books/MYP2-Student-Coursebook-Enhanced-Original-First-Edition.pdf) |
| 3 | [`MYP-Mathematics-3-Student-Coursebook.pdf`](../MYP-Mathematics-3-Student-Coursebook.pdf) | 281 | 52 | 61 / 189 | [MYP3 PDF](books/MYP3-Student-Coursebook-Enhanced-Original-First-Edition.pdf) |
| 4 | [`MYP_Mathematics_4_Student_Coursebook.pdf`](../MYP_Mathematics_4_Student_Coursebook.pdf) | 458 | 69 | 80 / 253 | [MYP4 PDF](books/MYP4-Student-Coursebook-Enhanced-Original-First-Edition.pdf) |
| 5 | [`MYP_Mathematics_5_Student_Coursebook.pdf`](../MYP_Mathematics_5_Student_Coursebook.pdf) | 340 | 59 | 69 / 215 | [MYP5 PDF](books/MYP5-Student-Coursebook-Enhanced-Original-First-Edition.pdf) |

The MYP3 build now uses the 281-page first edition uploaded in [`445af0d`](https://github.com/fideliashadyy17-gif/MYP-Texbook/commit/445af0da16192b3279fb357c5377409119764acc), Git blob `98da8a456377c3667df02e3f28d91cab9a0d8af5`. Its first 274 pages have the same decoded content streams and extractable text as the earlier first-edition upload from [`910ec1c`](https://github.com/fideliashadyy17-gif/MYP-Texbook/commit/910ec1cce82e7dbe4074def33bf7b1128cb7f4e9), so none of the lesson anchors changed. The new master also includes six supplementary pages and a back cover. Both are preserved; the added worked answers follow the supplement, before the back cover. The enhanced MYP3 PDF also restores 484 original contents and index links whose named destinations were absent from the uploaded PDF catalog. All five source hashes are in [`build.py`](build.py). No second-edition PDF or source is a dependency.

## Reading and printing

The printed numbers and original cross-references are not renumbered. Added leaves use labels such as `P7.4`; `S1`, `S2`, etc. label the added answer pages. By default, bookmarks show the chapter structure and each section expands to its new practice. “Worked answers” at the foot of a practice page opens the relevant entry; clicking its heading returns to practice. Some original pages finish one section and start the next on the same page. The new leaf follows that shared page so the previous exercise is complete and no original text or figures are split. Use the viewer’s physical page numbers when specifying a print range in viewers that do not expose page labels. Added pages have embedded fonts and vector graphics at the original A4 trim; the files are not PDF/X-certified and no printer-specific bleed/profile or physical proof was supplied.

## Scope by volume

| Year | Coverage and additions keyed to the first-edition sequence |
|---|---|
| 1 | All 10 chapters: number families, place value, estimation, powers and operations; factors/divisibility/prime decomposition; fractions and decimals; percentages and budgets; expressions and equations; angle relationships and ruler–compass construction; set operations and surveys; perimeter/area/nets/capacity; and truthful data displays. Added fraction strips, count grids, scale comparisons, construction diagrams, dot plots and Venn models alongside the original F/R/P/E practice. |
| 2 | All 11 chapters: ratios, proportionality and rates; signed operations; expressions, equations and competing costs; explicit sequence rules and graphs; angles, area and 3D geometry; transformations; chance and simulation; distributions. Added ratio tables, comparison graphs, construction/scale figures, coordinate plates, nets, spinners and same-scale box plots. |
| 3 | All 10 chapters and cumulative review: exact real numbers, indices and precision; functions and formulas; rate and equations, inequalities and systems; congruence, symmetry and transformations; similarity, Pythagoras and trigonometry; solids and measurement; scatter plots and claims; compound probability, simulation, sampling and risk. Added labelled proof figures, accuracy and model checks, transformations, paired scatter plots and tabular/Venn evidence. |
| 4 | All 13 chapters and the sustainable-space capstone: proof, bounds and surds; factorisation, formulas and systems; coordinate functions; quadratics, sequences and finance; similarity, trigonometry and solids; distributions and combined events. Added bounds decisions, quadratic plots, a space-diagonal model, unequal-bin density, cumulative frequency, keyed ordinary and back-to-back stem-and-leaf displays, box plots and probability trees. The capstone additions quantify shade, capture limits and budget trade-offs rather than repeating the original assessment. |
| 5 | All 12 chapters: polynomials and rational equations; transformations and inverses; logs; sequences and series including annuity timing; constrained optimisation; circle geometry, proof and trig; vectors and matrices; dispersion and regression; conditional probability; modelling and cumulative reasoning. Added feasible-region grids, constrained integer choices, exact circle layouts, model residuals, an annuity comparison and case-based probability trees. |

The original books already include distinct forms of guided practice, illustrations, investigations and assessment. The enrichment was targeted at changing the representation, checking claims, comparing methods or justifying decisions rather than replacing what already worked. Numbered investigations, summaries and assessment pages without a new leaf are retained, not skipped or replaced in the output. In particular the longer open investigations, cumulative assessments and the Year 5 project brief did not need near-duplicate versions. See [the exercise-reference analysis](REFERENCE-REVIEW.md), the per-section [coverage map](coverage.csv) (original feature markers are text signatures, not counts of distinct tasks, and may include an adjoining section on shared pages) and machine-readable [PDF inspection report](build-report.json).

## Rebuild and verify

No editable first-edition project or export scripts were tracked with the original PDFs. Instead of reflowing or editing the flattened originals, the workflow renders new pages from editable files and copies the existing PDF page masters through without changing their original page content streams. Python 3.10+ and the DejaVu Sans/Serif font families are required (`DEJAVU_DIR` may point to their TTF directory; default on Debian-like systems is `/usr/share/fonts/truetype/dejavu`). From the repository root:

```sh
python -m venv /tmp/myp-venv
/tmp/myp-venv/bin/pip install -r enhanced-first-edition/requirements.txt
/tmp/myp-venv/bin/python enhanced-first-edition/build.py
/tmp/myp-venv/bin/python enhanced-first-edition/build.py --verify-only
/tmp/myp-venv/bin/python enhanced-first-edition/verify_samples.py
/tmp/myp-venv/bin/python enhanced-first-edition/coverage.py
```

Use `--years 2 4` for selected volumes or `--out PATH` to write elsewhere. `source/mypN.txt` contains the authored content, with `section|reference IDs`, `criterion|title|stem|part a|part b|…`, optional `@visual` rows, and `= answer a~answer b~…`. `source/inventory.json` stores the original headings, printed numbers, and physical insertion anchors (PDF page indices are expressed as one-based `after` boundaries). Before editing an anchor, inspect the original pages that straddle it; content on a shared page can’t be split by this workflow.

### Verification boundaries

- The build checks alignment to the mapped instructional sections, question/answer counts, font coverage, diagram inputs, layout bounds, navigation and the page geometry and decoded content streams of **every** original page. It compares proof renders across every original book and verifies reciprocal practice/answer links. The sample checker independently recomputes selected values; open responses have suggested evidence rather than unique machine-testable answers.
- Visual proofing sampled new practice pages across all five years and the reference images on each paper. The enhancements are not an errata pass on original content. In particular, MYP4 retains six pre-existing visually blank original pages (original physical PDF pages 181, 203, 231, 291, 325, 373); MYP5 retains nine (55, 101, 121, 163, 185, 207, 229, 257, 331). No blank practice pages were added.
