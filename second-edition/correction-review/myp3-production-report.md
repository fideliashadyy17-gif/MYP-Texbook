# MYP 3 Second Edition — assembled coursebook production report

**Deliverable:** `second-edition/exports/myp3/MYP3-Student-Coursebook-Second-Edition.pdf`
**Built:** 2026-11-02 · pipeline `second-edition/sources/myp3/fullbook/` · QA
`second-edition/qa/myp3/fullbook/`

## Scope

The ten MYP 3 chapters (The real number system · Powers, roots and scientific
notation · Functions, expressions and algebraic reasoning · Linear relationships
and graphs · Equations, inequalities and systems · Transformations, congruence
and symmetry · Similarity, proof and trigonometry · Three-dimensional solids and
measurement · Bivariate data, correlation and causation · Probability, sampling
and evidence) are assembled into **one continuous A4 document** with front
matter, contents, and end matter (answers, formula bank, glossary, references).

Chapter scope, key and related concepts, global contexts, explorations and
inquiry questions come from the pre-rewrite MYP 3 audit and registers. The
teaching sequence, investigations, worked examples, practice sets, assessment
tasks, project connections, formula bank, glossary, references and editorial
framework are author-designed material written for this second edition; they are
not IB publications and carry no IB endorsement.

## Measured result

| measure | value |
| --- | --- |
| pages | **455** (A4, 595 × 842 pt) |
| file size | **3 838 233 bytes** |
| practice items | **470** (all with student-facing answers and reasoning) |
| items per chapter | 47 each (A 12 · B 11 · C 12 · D 12) |
| investigation pages | 20 task pages + 20 notes pages (two per section) |
| criterion-practice pages | 80 (A, B, C, D in every chapter, two pages each) |
| project pages | 10 (Service as Action · Community Project · Personal Project MYP 5) |
| chapter review pages | 10 + 10 reflection pages |
| answer pages | 40 |
| formula bank | 1 page · glossary | 2 pages · references | 1 page |
| page overflow | **0** |
| missing glyphs | **0** |
| KaTeX expressions | 171 (0 errors) |
| KaTeX errors / console errors | **0 / 0** |
| fonts | embedded subsets (Fraunces, Source Serif 4, Inter, OpenSans, KaTeX) |

## Chapter start pages

1: 11 · 2: 50 · 3: 89 · 4: 128 · 5: 167 · 6: 206 · 7: 245 · 8: 284 · 9: 328 ·
10: 367.
Back matter: answers 406 · formula bank 446 · glossary 452 · references 454 ·
back cover 455.

## QA result

`second-edition/qa/myp3/fullbook/book-qa.json` → **STATUS: PASS**. Checks
passed: page count, A4 page size, embedded fonts, no replacement characters,
**no missing glyphs**, no `[[math:…]]` placeholders, no raw LaTeX in the text,
printed folios matching the physical index (cover pages carry no folio), chapter
start pages, contents accuracy, item coverage (470 question ids, all 470 items
present with an answer), no duplicate or unresolved item ids, and all four
back-matter sections present.

Independent scans of the exported text layer confirm **0 spans bleeding past a
page margin** and **0 overlapping text spans** on all 455 pages.

Renders of the inspected pages are stored in
`second-edition/qa/myp3/fullbook/renders/` (157 pages).

## Defects found and fixed during assembly

1. **Running head still said MYP 2.** `build_book.py` hard-codes the running
   head separately from `LEVEL`, so a level substitution left
   `"MYP Mathematics 2 · Student coursebook"` in the header of every page.
   Corrected to `"… 3 …"`.
2. **QA encoded MYP 2's cover collection strip.** `qa_book.py` expected four
   forthcoming volumes; it now derives the count from a `LEVEL` constant
   (`5 - LEVEL`).
3. **Missing glyphs — 59 empty boxes.** U+207B `⁻` (superscript minus) was
   absent from the embedded text font, so every `10⁻⁵` printed as `10⁵`.
   U+1D50 `ᵐ` and U+207F `ⁿ` failed the same way in the index laws
   (`aᵐ ÷ aᵐ = a⁰` printed as `a ÷ a = a⁰`). U+2153 `⅓` and the other vulgar
   fractions failed too. Fixed by routing fragile superscript runs through KaTeX
   (`SUPERSCRIPTS` / `_superscript` in `symbols_to_math`), raising superscript
   runs inside SVG text with `baseline-shift` tspans
   (`SUPERS` / `_superscripts` in `diagrams2.fig`), and adding the fraction
   characters to `SYMBOL_MATH`. The reliable signal for this class of defect is
   `\u0000` in `page.get_text()`, never a character count in `book.html`.
4. **`→` and `∈` are absent from the embedded Inter subset.** They render blank
   and extract as NUL. Six diagram call sites were reworded to avoid arrows
   (function-machine titles and rules, two investigation table columns, one
   solution-set column). A local Chromium font test is not a valid check here:
   Inter is not installed in the sandbox, so the fallback font supplies the
   glyph and reports a false pass.
5. **Investigation tables bypassed the SVG post-processing.** `build_book.py`
   called `diagrams2.table()` directly, so superscripts inside table cells were
   never raised. The call now goes through `diagrams2.fig("table", …)`.
6. **Investigation pages overflowed (18 pages).** The seven new MYP 3 diagrams
   are taller than the MYP 2 page budget allows. Capped with
   `.page .investigate figure svg{max-height:78mm}` and
   `.page .investigate .table-wrap{max-height:78mm;overflow:hidden}`.
7. **Coordinate grids were drawn off-canvas.** `diagrams2.grid` centred the plot
   on zero rather than on the middle of the requested range, so every asymmetric
   window (for example x from 0 to 10) ran off the top and the right of the
   viewBox and was silently clipped — roughly a third of each grid was missing.
   The plot is now centred on the midpoint of the range. (The same defect exists
   in MYP 2 and is being carried as a separate correction.)
8. **Diagram titles collided with axis labels.** In `grid` and `scatter` the
   title and the y-axis label shared the same horizontal band, so a long title
   printed on top of the axis label on five pages. Titles now sit in their own
   band above the plot.
9. **Tree branch probabilities collided with outcome labels.** In
   `diagrams2.tree` the probability of a level-2 branch was written where the
   level-1 outcome label already was. Probabilities now sit above their own
   branch, clear of the previous level's labels.
10. **SVG table cells did not wrap.** Long cell text ran over the neighbouring
    column, and a right-edge scan of the PDF does not catch it because the SVG
    is centred in the column. `table()` now wraps cell text to the column width
    and grows the row height to fit, with tighter rows for tables of more than
    eight rows so that a long table still reads at the size the page allows.
11. **Assessment footer notes printed at the page foot.** `.footer-note` was
    absolutely positioned against the page, so the criteria note of every
    assessment task was drawn at x = 0, below the page footer, on top of the
    other notes on the page. It is now static, inside its own task box.
12. **A 27-digit number overflowed its column** in the Chapter 2, section 2.3
    investigation table. The cell now reads "a 25-digit number".

## Status

**455 pages, 3 838 233 bytes, QA STATUS: PASS**, 470 items / 470 answers, 0
overflow, 0 placeholders, 0 raw maths, 0 KaTeX errors, 0 console errors, 0
missing glyphs, alignment audit 150/150. Renders and QA artefacts are in
`second-edition/qa/myp3/fullbook/`. The alignment and practice reviews are
`myp3-unit-alignment.md` and `myp3-practice-alignment-review.md` in this
directory.
