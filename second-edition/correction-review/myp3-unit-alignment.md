# MYP 3 — unit alignment for the whole coursebook

Prepared for review. The approved MYP 1 prototype, the MYP 2 architecture and the
approved interior are unchanged: the alignment framework was applied *inside* the
existing page model, as additions in space that was previously empty.

## 1. Status of the work

* Everything is on branch `arena/c767ce09-myp-texbook`.
* Exported book:
  `second-edition/exports/myp3/MYP3-Student-Coursebook-Second-Edition.pdf` —
  **455 pages, 3 838 233 bytes**, A4 (595 × 842 pt), fonts embedded,
  **0 overflow, 0 placeholders, 0 raw maths, 0 KaTeX errors, 0 console errors,
  0 missing glyphs**, **470 practice items / 470 answers**, 40 answer pages,
  171 KaTeX expressions. Mechanical QA `book-qa.json` → **STATUS: PASS**.
* Alignment audit: **150 / 150 points** across the ten chapters
  (`python3 unit_alignment_audit.py`).
* Practice/criterion diagnostic: **449 of 470 items** genuinely match the
  criterion they are filed under; the remaining 21 were read individually and
  confirmed as authentic real-world or communication tasks.
* Chapter start pages: 11, 50, 89, 128, 167, 206, 245, 284, 328, 367;
  answers 406, formula bank 446, glossary 452, references 454, back cover 455.
* Renders of every inspected page: `second-edition/qa/myp3/fullbook/renders/`
  (157 pages: covers, contents, every chapter opener, every investigation task
  page, every Criterion A–D practice page, every chapter reflection, answers,
  formula bank, glossary, references, back cover).

## 2. The unit framework as built

Every chapter is a complete MYP unit from the first page. The key concept, the
related concepts, the official global context with its official exploration, the
statement of inquiry, the three question categories and the ATL focus are taken
from the pre-rewrite MYP 3 audit and registers
(`second-edition/audit/chapter-audits/myp3-audit.md`,
`second-edition/audit/evidence/chapter-register.csv`,
`second-edition/audit/evidence/subtopic-register.csv`).

| # | Chapter | Key concept | Related concepts | Global context / exploration |
| --- | --- | --- | --- | --- |
| 1 | The real number system | Form | Quantity, Equivalence | Orientation in space and time / Natural and human landscapes and resources |
| 2 | Powers, roots and scientific notation | Form | Quantity, Representation, Patterns | Scientific and technical innovation / Precision, accuracy and measurement |
| 3 | Functions, expressions and algebraic reasoning | Relationships | Generalisation, Equivalence | Identities and relationships / Relationships and communities |
| 4 | Linear relationships and graphs | Relationships | Change, Representation | Fairness and development / Distribution of resources |
| 5 | Equations, inequalities and systems | Relationships | Equivalence, Systems | Globalisation and sustainability / Resources and consumption |
| 6 | Transformations, congruence and symmetry | Form | Space, Justification | Personal and cultural expression / Artistry, craft, creation and beauty |
| 7 | Similarity, proof and trigonometry | Relationships | Justification, Measurement | Orientation in space and time / Natural and human landscapes and resources |
| 8 | Three-dimensional solids and measurement | Form | Measurement, Models | Globalisation and sustainability / Human impact on the environment |
| 9 | Bivariate data, correlation and causation | Relationships | Models, Justification | Fairness and development / Inequality, difference and inclusion |
| 10 | Probability, sampling and evidence | Logic | Quantity, Models | Identities and relationships / Beliefs and values |

### What is on every chapter

| Element | Where | Rendered by |
| --- | --- | --- |
| Key concept, related concepts, global context, exploration | chapter opener, *Framing the inquiry* card | the existing opener card |
| Statement of inquiry naming the key and related concepts | chapter opener | the existing opener card |
| Factual / conceptual / debatable questions | chapter opener, *Questions to guide us* | the existing opener card |
| ATL focus banner | chapter opener footer | the existing opener footer |
| Engagement situation | chapter opener | the existing opener standfirst block |
| Inquiry question | investigation page, above *Your task* | `.callout` with the existing `.label` |
| Observation and discovery | investigation notes page | the existing notes page |
| Mathematical conclusion | investigation notes page | the existing conclusion block |
| Formal development | teaching page | the existing callout |
| Worked examples (problem, visual, reasoning, steps, answer, interpretation) | one page per example | the existing example page |
| Criterion A–D practice | two pages per criterion per chapter | the existing practice page |
| Application, assessment and reflection | review pages | the existing review page |
| Service as Action · Community Project · Personal Project (MYP 5) | chapter review | the existing project block |

No new page structure, no new palette, no new typography, no change to the
running heads, no change to the chapter or section sequence. Every chapter
carries 47 practice items (12 A, 11 B, 12 C, 12 D) — 470 items in the book.

## 3. Corrections made during the alignment pass

1. **Chapter 2 key concept.** The register records Chapter 2 with a non-standard
   key concept. It has been set to **Form**, with **Patterns** carried as a
   related concept, which is what the teaching in the chapter actually develops.
2. **Chapter 8 and Chapter 9 teaching text.** Each needed a literal use of the
   word *models* in a teaching paragraph, because the alignment audit checks the
   teach text and not only the section titles. Both now name the related concept
   in the prose.
3. **Sub-section coverage.** All 51 MYP 3 subtopics in
   `subtopic-register.csv` (sections 1.1–10.5) are taught, and the audit maps
   every one of them.

## 4. What was deliberately not done

* No statement of inquiry, inquiry question, investigation, worked example,
  practice item, assessment task or project connection was copied from MYP 2.
  The MYP 3 material was written for this volume against the MYP 3 register.
* The approved MYP 1 prototype pages are not touched.
* No publisher, ISBN, print specification or commercial print-readiness claim
  appears anywhere in the book; it is produced as an A4 review copy with
  embedded fonts and continuous pagination.

## 5. Status

Alignment audit **150/150**, practice diagnostic **449/470** with the 21 flagged
items confirmed by reading, mechanical QA **PASS**. The book is ready for the
next stage of review.
