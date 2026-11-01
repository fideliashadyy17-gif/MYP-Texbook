# MYP 1 Chapter 1 — QA summary

**Deliverable:** `../../exports/myp1/MYP1-Chapter-01-Revision-Proof.pdf`  
**Status:** PASS — Chapter 1 revision proof only  
**Date:** 2026-11-01

## Export checked

| Item | Result |
|---|---|
| PDF | `MYP1-Chapter-01-Revision-Proof.pdf` |
| SHA-256 | `f7addc70c3a86a8a406233e9055df11672e3b24036c17404128c0ffb13c2ce1d` |
| Pages | 28 |
| Page size | A4 (594.96 × 841.92 pt) |
| Fonts | 11 font resources; all embedded |
| Exercise items | 82 |
| Answer pages | 7 |
| Question/answer pairing | All 82 exercise IDs found as question + answer pairs |

## Validation results

| Check | Result | Evidence |
|---|---:|---|
| Paged.js layout check | PASS | `chapter-01-layout-check.json` |
| Expected/rendered pages | 28 / 28 | No missing, duplicate or split source pages |
| Overflow | 0 | Layout check |
| Raw placeholders / raw LaTeX / KaTeX errors | 0 / 0 / 0 | Layout check |
| Post-export PDF QA | PASS | `chapter-01-pdf-qa.json` |
| Independent mathematical checks | 69 / 69 PASS | `chapter-01-math-qa.json` |
| Visual inspection | Completed | Contact sheets and selected full-page renders |

## Visual inspection notes

Inspected cover, opener, learning intentions, number-line and place-value pages, exploration, application, assessment practice, mixed practice and answer pages. The final proof has:

- a single full-bleed-style cover page with visible cream title on deep green;
- no split cover or blank continuation page;
- readable exercise labels and answer reasoning;
- visible blank boxes for comparison questions;
- corrected number-family nesting caption;
- an exploration table that leaves most counts for students to complete;
- enlarged workspace on application/assessment pages;
- consolidated answer pages without overflow.

## Corrections made during QA

1. **1.5.3:** exact product corrected to `9.8 × 4.2 = 41.16` (not 41.18).
2. **S4:** sample comparison changed to “fewer than one in seven”, which is supported by `6,509 × 7 < 48,672`.
3. **1.4.8:** answer now explicitly states that 1,948 rounds to 2,000 to the nearest thousand.
4. **Cover:** title colour corrected for contrast against the deep-green background.
5. **Comparison boxes:** replaced unsupported square glyphs with styled blank boxes.
6. **Number families:** caption corrected to natural ⊂ whole ⊂ integer ⊂ rational.
7. **Exploration table:** removed pre-filled counts that would have given away the pattern.
8. **Answer pagination:** consolidated to seven answer pages after confirming no overflow.

## Remaining issues / limits

- This is **Chapter 1 only**, not the complete MYP 1 coursebook.
- It is an A4 revision proof. Final commercial print production may require bleed/crop marks and printer-specific colour settings.
- No standalone MYP 1 curriculum overview/unit documents were present in the repository; scope is anchored to the first-edition embedded course map, planner and TOC.
- Application and assessment datasets are explicitly simulated classroom data.
