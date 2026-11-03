# MYP 4 Second Edition — assembled coursebook production report

**Deliverable:** `second-edition/exports/myp4/MYP4-Student-Coursebook-Second-Edition.pdf`
**Built:** 2026-11-03 · pipeline `second-edition/sources/myp4/fullbook/` · QA
`second-edition/qa/myp4/fullbook/`

## Scope

The fourteen MYP 4 chapters (Number Foundations: Exponents, Surds and Accuracy ·
Algebraic Expressions and Factorisation · Linear Equations, Inequalities and
Systems · Functions, Coordinates and Linear Models · Quadratic Expressions and
Equations · Quadratic Functions and Graphical Reasoning · Patterns, Sequences
and Generalisation · Growth and Financial Mathematics · Congruence, Similarity
and Transformations · Pythagoras, Trigonometry and Measurement · Surface Area
and Volume · Statistics: Distributions and Data · Probability: Combined Events ·
Capstone: Designing a Sustainable Space) are assembled into **one continuous A4
document** with front matter, contents, and end matter (answers, formula bank,
glossary, references).

Chapter scope, key and related concepts, global contexts, explorations and
inquiry questions come from the pre-rewrite MYP 4 audit and registers
(`second-edition/audit/evidence/chapter-register.csv`,
`second-edition/audit/evidence/subtopic-register.csv`). The section ids and
titles of all **82** register rows are reproduced exactly. The teaching
sequence, investigations, worked examples, practice sets, assessment tasks,
project connections, formula bank, glossary, references and editorial framework
are author-designed material written for this second edition; they are not IB
publications and carry no IB endorsement.

## Measured result

| measure | value |
| --- | --- |
| pages | **691** (A4, 595 × 842 pt) |
| file size | **5 834 068 bytes** |
| practice items | **658** (all with student-facing answers and reasoning) |
| answer pages | **56** |
| mathematics expressions | **148** (KaTeX) |
| embedded fonts | **10**, all embedded |
| overflow / placeholders / raw maths / KaTeX errors / console errors / missing glyphs | **0 / 0 / 0 / 0 / 0 / 0** |
| unit alignment | **210 / 210** points across 14 chapters |
| subtopic register | **82 / 82** rows matched (id + title) |
| practice/criterion diagnostic | **645 / 658** items match on the mechanical test |
| QA renders kept as evidence | **230** pages |

Chapter start pages: 1 → 13, 2 → 57, 3 → 101, 4 → 145, 5 → 189, 6 → 234,
7 → 278, 8 → 322, 9 → 366, 10 → 410, 11 → 456, 12 → 501, 13 → 544,
14 → 588; answers 626, formula bank 682, glossary 687, references 690,
back cover 691.

## How it is built

```
second-edition/sources/myp4/fullbook/
    framework.py            content: 14 chapters, criteria, formulas, glossary,
                            references, front and back matter
    diagrams2.py            SVG diagram library (25 figure types)
    covers.py               cover, imprint, back cover, collection strip
    make_css.py             assembles book.css from the approved prototype
                            stylesheet plus the legacy component styles
    build_book.py           paginates the whole book and writes book.html
    render_math.mjs         KaTeX-renders every [[math:…]] expression
    export_book.mjs         prints book.html to the A4 PDF and reports overflow
    qa_book.py              full-book PDF QA, writes book-qa.json
    unit_alignment_audit.py 15-point MYP unit alignment audit
    practice_audit.py       practice/criterion diagnostic, practice-audit.json
    render_qa.py            renders the inspected pages as PNG evidence
```

Rebuild with:

```
cd second-edition/sources/myp4/fullbook
python3 make_css.py
python3 build_book.py
node render_math.mjs
node export_book.mjs
python3 qa_book.py
python3 unit_alignment_audit.py
python3 practice_audit.py
python3 render_qa.py
```

## Defects found and fixed

1. **13 missing glyphs** — the modifier superscript `ˣ` and the arrow `→`
   inside an SVG table. `ˣ` is now routed through KaTeX with the other fragile
   superscripts; the transformation table in 9.4 says "maps to" inside the
   diagram. Now 0 missing glyphs.
2. **Running head said "MYP MATHEMATICS 3"** — `make_css.py` had not been
   level-patched. Now "MYP MATHEMATICS 4".
3. **Seven parabola grids drew a chord** between the two roots, reading as a
   straight line; each now plots five points on the curve. One also had its root
   markers corrected.
4. **A mislabelled solid** in 11.3 ("r = 6" for a radius of 3 cm).
5. **The cover said "a capstone in five parts"**; the capstone has four.
6. **The cover topic list** no longer matched the built chapter titles.

## Editorial position

* No IB publication has been reproduced. All investigations, examples, practice
  items, assessments and reference material are original to this edition.
* The exterior carries the author credit on the front cover, the imprint and the
  back cover, the five-volume collection strip with the forthcoming volumes
  labelled, and no ISBN and no publisher, as approved.
* The MYP 1 prototype design system, the MYP 2 architecture and the approved
  interior are unchanged.
