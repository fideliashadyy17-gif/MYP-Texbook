# MYP 1 Chapter 2 — QA summary

**Deliverable:** `../../exports/myp1/MYP1-Chapter-02-Revision-Proof.pdf`  
**Status:** PASS — Chapter 2 revision proof only  
**Date:** 2026-11-01

## Export checked

| Item | Result |
|---|---|
| PDF | `MYP1-Chapter-02-Revision-Proof.pdf` |
| SHA-256 | `4e425a2e35be7787b6800e838eead731ae837a096e836c28e97183db62dfefd3` |
| Pages | 32 |
| Chapter pages | 23 |
| Answer pages | 9 |
| Page size | A4 (594.96 × 841.92 pt) |
| Fonts | 11 font resources; all embedded |
| Exercise items | 87 |
| Question/answer pairing | All 87 exercise IDs found in question pages and answer pages |

## Validation results

| Check | Result | Evidence |
|---|---:|---|
| Paged.js layout check | PASS | `chapter-02-layout-check.json` |
| Expected/rendered pages | 32 / 32 | No missing, duplicate or split source pages |
| Overflow / continuation pages | 0 / 0 | Layout check |
| Raw placeholders / raw LaTeX / KaTeX errors | 0 / 0 / 0 | Layout check |
| Post-export PDF QA | PASS | `chapter-02-pdf-qa.json` |
| Independent mathematical checks | 87 / 87 PASS | `chapter-02-math-qa.json` |
| Visual inspection | Completed | Contact sheets and selected full-page renders |

## Visual inspection notes

Inspected cover, opener, learning intentions, power notation, powers of ten, square/cube models, order-of-operations pages, substitution pages, exploration, application, assessment practice, mixed practice and answer pages. The final proof has:

- a single cover page with visible cream title on deep green;
- no accidental continuation pages;
- a two-page investigation that separates model construction from model limits;
- a square/cube diagram with corrected cube grid lines;
- a power-anatomy diagram with non-overlapping labels;
- an order-of-operations flow diagram placed on a page with enough space;
- visible blank boxes for missing-exponent questions;
- answer pages consolidated where they fit without overflow.

## Corrections and editorial decisions during QA

1. **Source answer correction:** the first-edition mixed-practice answer comparing \(2^5\) and \(5^2\) is not followed where it states the larger value incorrectly. The second edition states \(2^5=32>25=5^2\).
2. **Exploration pagination:** split the doubling-sheet investigation into two intentional pages so the table, rule, verification and model-limit discussion do not overflow.
3. **Order-of-operations pagination:** moved the flow diagram to the brackets/fraction-bar page to remove an accidental continuation page.
4. **Answer pagination:** Practices 2.1 and 2.2 needed separate answer pages; application and assessment answers were combined after confirming no overflow; mixed-practice answers remained split into two pages.
5. **Diagram repair:** corrected cube-grid projection lines and moved the power-anatomy explanatory label to avoid overlap.
6. **Zero exponent boundary:** explicitly restricted \(a^0=1\) to nonzero bases.
7. **Storage context:** labelled the school data-store figures as simulated; stated decimal units; kept binary-unit comparison as a calculator extension with unit conventions.

## Remaining issues / limits

- This is **Chapter 2 only**, not the complete MYP 1 coursebook.
- It is an A4 revision proof. Final commercial print production may require bleed/crop marks and printer-specific colour settings.
- No standalone MYP 1 curriculum overview/unit documents were present in the repository; scope is anchored to the first-edition embedded course map, planner and TOC.
- Application and assessment datasets are explicitly simulated classroom data.
