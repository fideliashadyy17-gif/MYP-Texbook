# MYP 1 second edition — Chapters 3–10 QA summary

Date: 2026-11-02
Scope: MYP 1 only. First-edition archive PDFs were not modified.

## Verification status

All eight chapters passed the three automated gates and were visually inspected from exported PDF renders.

| Chapter | Title | PDF pages | Items | Layout | Math QA | PDF QA | SHA-256 |
|---:|---|---:|---:|---|---|---|---|
| 3 | Factors, multiples and primes | 25 | 61 | PASS | 61/61 | PASS | `c00ac41b6ba7cfad0571bc7ca87e7419e88fd252c39fe8d1b51233e90856c45d` |
| 4 | Fractions and decimals | 27 | 67 | PASS | 67/67 | PASS | `76bee47abe4cd5be935fa9e4a92e8a6d490f14a11a75d5abf737f6d2d38e8e23` |
| 5 | Percentages and applications | 22 | 55 | PASS | 55/55 | PASS | `a6eb613ab2c7f2e0c2be60f71b89c7f73f1028332b1535a422cc65e6573bf8e6` |
| 6 | Patterns, expressions and equations | 22 | 55 | PASS | 55/55 | PASS | `e07f1b6c60e989a8987850fdb9ef9dfb6d332f47a35a77c32fa5883ecba631a6` |
| 7 | Lines, angles, triangles and constructions | 22 | 55 | PASS | 55/55 | PASS | `3e23ef2b75b36fcf0ea6fdac6d9b2470ba7a9a512931c883883fedc23acd2980` |
| 8 | Sets and classification | 22 | 55 | PASS | 55/55 | PASS | `7658a05df77d72fcde647fa43893703f13e75524a0152c641e972882663e692a` |
| 9 | Perimeter, area, surface area and volume | 22 | 56 | PASS | 56/56 | PASS | `281beb8d3afa1d8e971b6fb351b06ae62e0b1900e3d2bba4c4a3deed07109952` |
| 10 | Data, tables and graphs | 22 | 55 | PASS | 55/55 | PASS | `ac46d516384d796c748e25f029030931c2ad985579629d380596defcabd5ef73` |

Total Chapters 3–10: **459 exercise items**, **184 PDF pages**.

Export directory: `second-edition/exports/myp1/`
Editable sources: `second-edition/sources/myp1/`
Authoring plans: `second-edition/sources/myp1/tools/content/chapter_03.py` … `chapter_10.py`
Machine reports: `chapter-NN-layout-check.json`, `chapter-NN-pdf-qa.json`, `chapter-NN-math-qa.json`, and `chapters-03-10-math-summary.json` in this directory.
Visual renders: `renders/chapter-NN/` and contact sheets `renders/chapter-NN-contact-*.png`.

## Scope and provenance

No standalone MYP 1 curriculum overview or unit planner documents were present in the repository. Scope was therefore verified from the first-edition MYP 1 PDF itself: embedded course map (p. 13), chapter unit planners, table of contents, section headings, investigations, applications and answer pages. Each exercise JSON records the first-edition source file, SHA-256 and physical page range.

First-edition MYP 1 archive hash re-verified unchanged:
`131a3a99d14ae5a7613c7e9da24c540e29029d93a1a360abcc8516835798b3f0`

New classroom contexts are labelled simulated. Currency and measurement contexts follow the verified first-edition tasks where retained; no real-world dataset is presented as measured data without provenance.

## Checks performed

1. **Authoring lint / mathematical QA:** `python qa_math_chapters.py 3 4 5 6 7 8 9 10` evaluates restricted verification expressions independently of answer prose. All 459 items pass.
2. **Layout QA:** `npm run check -- N` in headless Chromium/Paged.js. Expected page count, source page IDs, question/answer IDs, overflow, raw placeholders, raw LaTeX and KaTeX errors all pass.
3. **Export:** `npm run export -- N` writes A4 PDFs with embedded fonts.
4. **PDF QA:** `python qa_pdf.py N` checks page count, A4 geometry, embedded fonts, question/answer ID pairing and renders every page.
5. **Visual inspection:** contact sheets and selected full-page renders were opened. Diagrams, set notation, worked examples, practice pages and answer pages were reviewed.

## Issues found and corrected during QA

- Chapter 3 exploration: factor count of 36 corrected to 9.
- Chapter 5 investigation: successive-discount integer-pair answer corrected to include 4% and 25% as a valid pair distinct from 10% and 20%.
- Chapter 6 exploration: 20-square matchstick count corrected to 61.
- Chapter 9 investigation: surface area of 1×6×6 corrected to 96 cm².
- Chapter 10 grouped-mean estimate corrected to 168 minutes and distinguished from the raw mean 158 minutes.
- Chapter 8: set symbols and double-struck number-set symbols were moved to KaTeX after missing-glyph boxes appeared in the first export; the number-set diagram was redrawn with plain labels and clearer nesting.
- Chapter 9: cuboid net diagram was redrawn to prevent the surface-area formula overlapping a face.

## Remaining limitations

- These are chapter revision proofs, not a combined final coursebook with front matter and continuous pagination.
- Commercial print production may still require bleed/crop marks and printer-specific colour settings.
- The scope remains anchored to the first-edition embedded planning material because no separate school curriculum overview was available.
