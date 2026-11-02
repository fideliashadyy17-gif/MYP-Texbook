# MYP1 Second Edition — assembled coursebook production report

**Deliverable:** `second-edition/exports/myp1/MYP1-Student-Coursebook-Second-Edition.pdf`
**Built:** 2026-11-02 · pipeline `second-edition/sources/myp1/fullbook/` · QA `second-edition/qa/myp1/fullbook/`

## Scope

The ten MYP1 chapters (Number systems · Powers and order · Fractions and decimals · Algebraic
foundations · Percentages and applications · Patterns and equations · Lines, angles and
constructions · Sets and Venn diagrams · Mensuration and geometry · Data handling) are assembled
into **one continuous A4 document** with front matter, contents, and end matter
(answers, formula bank, glossary, references).

Chapter 7 theory, investigation, worked-example, assessment and project pages are copied from the
approved Chapter 7 prototype, so the design the user approved is unchanged in the assembled book.
Chapters 1–6 and 8–10 come from the approved second-edition chapter manuscripts, with the
framework (Criterion A–D practice structure, projects, Service as Action, ATL banners) injected
around them.

## Measured result

| measure | value |
| --- | --- |
| pages | **380** (A4, 210 × 297 mm) |
| file size | 4,824,286 bytes |
| practice items | **722** (all with student-facing answers and reasoning) |
| items per chapter | 1: 90 · 2: 96 · 3: 70 · 4: 76 · 5: 64 · 6: 64 · 7: 69 · 8: 64 · 9: 65 · 10: 64 |
| investigation pages | 41 (one per new concept) |
| criterion-practice pages | 27 (A, B, C, D in every chapter) |
| project pages | 10 (Service as Action · Community Project · Personal Project MYP5, one per chapter) |
| chapter review pages | 9 |
| answer pages | 65 |
| formula bank | 5 pages · glossary | 4 pages · references | 1 page |
| page overflow | **0** |
| KaTeX errors / console errors | **0 / 0** |
| fonts | embedded subsets (Fraunces, Source Serif 4, Inter, OpenSans, KaTeX) |

## Chapter start pages

1: 8 · 2: 37 · 3: 67 · 4: 93 · 5: 122 · 6: 145 · 7: 168 · 8: 237 · 9: 260 · 10: 283
Back matter: answers 306 · formula bank 371 · glossary 376 · references 380.

## QA result

`second-edition/qa/myp1/fullbook/book-qa.json` → **STATUS: PASS**. Checks passed: page count, A4
page size, embedded fonts, no replacement characters, no `[[math:…]]` placeholders, no raw LaTeX
in the text, printed folios matching the physical index (cover pages carry no folio), chapter
start pages, contents accuracy, item coverage (653 question ids, all 722 items present with an
answer; the 69 Chapter 7 prototype items verified separately), no duplicate or unresolved item
ids, and all four back-matter sections present.

Renders of the inspected pages are stored in `second-edition/qa/myp1/fullbook/renders/`.

## Defects found and fixed during assembly

1. **Stray page-id text (134 pages).** The sequential page-id attribute was injected *after* the
   opening `<section>` tag, so `data-page-id="book-pNNN"` printed as a text line at the top of
   134 pages. The attribute is now inserted inside the tag; the export was re-run.
2. **Missing glyphs (empty boxes).** `→ ⊂ ∛ ∩ ∪ ∈ ⊆ ∘ ≠ ′` were absent from the embedded text font
   and rendered as empty boxes or tofu. `symbols_to_math()` now converts these symbols to KaTeX
   mathematics (243 expressions rendered); the affected pages (formula bank, glossary, chapter
   maps, Chapter 8 set notation, Chapter 5 captions) were re-rendered and checked.
3. **Chapter 1–2 covers without a standfirst.** `standfirst` text was added for chapters 1 and 2
   in `framework.py` so every chapter cover carries a statement-of-inquiry standfirst.
4. Earlier assembly passes fixed 37 overflowing pages by repaginating and compacting rather than
   shrinking type (legacy pages keep their own kickers; the answer pages were regrouped to twelve
   items per page; the formula bank holds two groups per page; contents padding and figure heights
   were tuned).

## Status

Complete for internal review and school printing. This is a **review/print-review copy**: A4,
embedded fonts, continuous pagination, no overflow. It is **not** a commercial print
specification — no bleed, crop marks, paper stock or printer colour profile has been supplied or
verified, and no publisher, ISBN or author credentials are claimed in the book.

## Out of scope

MYP2 and the other levels remain unstarted; they are not authorised until MYP1 is reviewed.
