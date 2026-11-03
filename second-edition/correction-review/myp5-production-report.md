# MYP 5 Second Edition — assembled coursebook production report

**Deliverable:** `second-edition/exports/myp5/MYP5-Student-Coursebook-Second-Edition.pdf`
**Built:** 2026-11-03 · pipeline `second-edition/sources/myp5/fullbook/` · QA
`second-edition/qa/myp5/fullbook/`

## Scope

The twelve MYP 5 chapters (Polynomials, Factor Theorem and Algebraic Fractions ·
Functions: Transformations, Composites and Inverses · Exponential and Logarithmic
Functions · Sequences and Series · Quadratic Inequalities and Linear Programming
· Circle Geometry and Geometric Proof · Sine and Cosine Rules; Trigonometry in
Three Dimensions · Vectors and Matrices · Statistics: Dispersion, Correlation and
Regression · Probability: Conditional Probability and Counting · Capstone: A
Mathematical Modelling Project · Cumulative Revision and the Transition to DP
Mathematics) are assembled into **one continuous A4 document** with front matter,
contents, and end matter (answers, formula bank, glossary, references).

Chapter scope, key and related concepts, global contexts, explorations and
inquiry questions come from the pre-rewrite MYP 5 audit and registers
(`second-edition/audit/chapter-audits/myp5-audit.md`, restated in the compact
chapter and subtopic register `second-edition/audit/chapter-audits/myp5-register.md`).
The section ids and titles of all **82** register rows are reproduced exactly.
The teaching sequence, investigations, worked examples, practice sets,
assessment tasks, project connections, formula bank, glossary, references and
editorial framework are author-designed material written for this second
edition; they are not IB publications and carry no IB endorsement.

The volume closes the five-volume sequence MYP 1 → MYP 2 → MYP 3 → MYP 4 → MYP 5
and is built on the same architecture, page model and design system as the
approved MYP 1 prototype.

## Measured result

| measure | value |
| --- | --- |
| pages | **648** (A4, 595 × 842 pt) |
| file size | **5 515 691 bytes** |
| practice items | **564** (all with student-facing answers and reasoning) |
| answer pages | **48** |
| mathematics expressions | **318** (KaTeX) |
| embedded fonts | **11**, all embedded |
| overflow / placeholders / raw maths / KaTeX errors / console errors / missing glyphs | **0 / 0 / 0 / 0 / 0 / 0** |
| unit alignment | **180 / 180** points across 12 chapters |
| subtopic register | **82 / 82** rows matched (id + title) |
| practice/criterion diagnostic | **553 / 564** items match on the mechanical test |
| QA renders kept as evidence | **200** pages |

Chapter start pages: 1 → 13, 2 → 62, 3 → 111, 4 → 160, 5 → 209, 6 → 258,
7 → 307, 8 → 356, 9 → 405, 10 → 454, 11 → 503, 12 → 547; answers 591, formula
bank 639, glossary 644, references 647, back cover 648.

Every chapter carries the same seven-part sequence (`x.1` investigate … `x.6`
investigation, `x.7` mixed practice) except the two closing chapters, which
carry six sections each. Practice is uniform across the volume at **47 items per
chapter**: 12 under Criterion A, 11 under B, 12 under C and 12 under D.

## How it is built

```
second-edition/sources/myp5/fullbook/
    framework.py            content: 12 chapters, criteria, formulas, glossary,
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
cd second-edition/sources/myp5/fullbook
python3 make_css.py
python3 build_book.py
node render_math.mjs
node export_book.mjs
python3 qa_book.py
python3 unit_alignment_audit.py
python3 practice_audit.py
python3 render_qa.py
```

The chapter sources are authored in `/tmp/myp5` (`head.py` plus `ch01.py`–`ch12.py`)
and concatenated by `assemble.py` into `framework.py`; `check.py` is the
structural gate on the sources.

## Defects found and fixed

1. **52 missing glyphs, the largest single defect in the volume.** The dividing
   stroke in the conditional-probability notation `P(A ∣ B)` was set as a
   literal Unicode character that the text fonts cannot supply; it produced NULs
   on 17 pages (Chapters 10 and 12 and their answers). `U+2223` is now routed
   through KaTeX with the other symbols in `build_book.SYMBOL_MATH`. The
   formula-bank and glossary entry for total probability used a bare
   `[[math:_i]]` subscript with no base character, which also produced a NUL;
   it is now written in words. Chapter 1's algebraic-fraction proof used the
   modifier letters `ᵢ`, `ⱼ`, `ⁱ`, `ʲ`, `ₘ`, `ₙ`, `ᵐ`, `ⁿ`, and one answer used
   the minus-plus sign `∓`; both are now written out in words and with the two
   turning points given separately. Now **0** missing glyphs.
2. **A self-contradictory answer, 10.1.5.** The independence item began "Yes,
   because 0.3 × 0.6 = 0.18 ≠ 0.15, so they are not independent." It now reads
   "No, because 0.3 × 0.6 = 0.18, which is not 0.15, so the events are not
   independent."
3. **A formula bank that overflowed its page.** The single 26-entry "Vectors,
   matrices and data" group was too tall for one page and blocked the PDF
   export. It is split into "Vectors and matrices" (8 entries) and "Statistics
   and probability" (18 entries), which took the book to 648 pages with zero
   overflow.
4. **The cover topic list** no longer matched the built chapter titles; it was
   regenerated from the finished chapters.

## Editorial position

* No IB publication has been reproduced. All investigations, examples, practice
  items, assessments and reference material are original to this edition.
* The exterior carries the author credit on the front cover, the imprint and the
  back cover, the five-volume collection strip with the forthcoming volumes
  labelled, and no ISBN and no publisher, as approved.
* The MYP 1 prototype design system, the MYP 2 architecture and the approved
  interior are unchanged.
