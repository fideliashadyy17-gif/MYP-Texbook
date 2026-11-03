# MYP 5 — unit alignment for the whole coursebook

Prepared for review. The approved MYP 1 prototype, the MYP 2 architecture and
the approved interior are unchanged: the alignment framework was applied *inside*
the existing page model, as additions in space that was previously empty.

## 1. Status of the work

* Everything is on branch `arena/c767ce09-myp-texbook`.
* Exported book:
  `second-edition/exports/myp5/MYP5-Student-Coursebook-Second-Edition.pdf` —
  **648 pages, 5 515 691 bytes**, A4 (595 × 842 pt), 11 fonts embedded,
  **0 overflow, 0 placeholders, 0 raw maths, 0 KaTeX errors, 0 console errors,
  0 missing glyphs**, **564 practice items / 564 answers**, 48 answer pages,
  318 KaTeX expressions. Mechanical QA `book-qa.json` → **STATUS: PASS**.
* Alignment audit: **180 / 180 points** across the twelve chapters
  (`python3 unit_alignment_audit.py`).
* Scope register: all **82 rows** of
  `second-edition/audit/chapter-audits/myp5-register.md` for level 5 are matched
  exactly, section id and section title, chapter by chapter (10 × 7 sections +
  4 capstone sections + 6 transition sections).
* Practice/criterion diagnostic: **553 of 564 items** genuinely match the
  criterion they are filed under; the remaining **11** were read individually
  and confirmed as authentic fluency tasks.
* Chapter start pages: 13, 62, 111, 160, 209, 258, 307, 356, 405, 454, 503, 547;
  answers 591, formula bank 639, glossary 644, references 647, back cover 648.
* Renders of every inspected page: `second-edition/qa/myp5/fullbook/renders/`
  (200 pages: covers, contents, every chapter opener, every investigation task
  page, the first two pages of each Criterion A–D practice set, every chapter
  reflection, answers, formula bank, glossary, references, back cover).

## 2. The unit framework as built

Every chapter is a complete MYP unit from the first page. The key concept, the
related concepts, the official global context with its official exploration, the
statement of inquiry, the three question categories and the ATL focus are taken
from the pre-rewrite MYP 5 audit and register
(`second-edition/audit/chapter-audits/myp5-audit.md`, restated in
`second-edition/audit/chapter-audits/myp5-register.md`).

| # | Chapter | Key concept | Related concepts | Global context / exploration |
| --- | --- | --- | --- | --- |
| 1 | Polynomials, Factor Theorem and Algebraic Fractions | Form | Equivalence, Generalisation, Simplification | Personal and cultural expression / the language of algebra as a way of making structure visible |
| 2 | Functions: Transformations, Composites and Inverses | Relationships | Change, Representation, Patterns | Scientific and technical innovation / models that translate a measurement into a prediction |
| 3 | Exponential and Logarithmic Functions | Change | Equivalence, Patterns, Representation | Scientific and technical innovation / populations, medicines, sound and seismic energy |
| 4 | Sequences and Series | Form | Patterns, Generalisation, Simplification | Fairness and development / saving, loans and the long-term decisions that shape opportunity |
| 5 | Quadratic Inequalities and Linear Programming | Relationships | Change, Equivalence, System | Globalization and sustainability / production planning under resource limits |
| 6 | Circle Geometry and Geometric Proof | Logic | Space, Generalisation, Justification | Personal and cultural expression / the geometry of architecture and ornament |
| 7 | Sine and Cosine Rules; Trigonometry in Three Dimensions | Relationships | Space, Change, Measurement | Orientation in space and time / navigation, surveying and the geometry of place |
| 8 | Vectors and Matrices | Form | Space, Representation, Systems | Scientific and technical innovation / computer graphics, navigation and engineering |
| 9 | Statistics: Dispersion, Correlation and Regression | Relationships | Patterns, Representation, Measurement | Identities and relationships / how groups differ, and how claims about them are made |
| 10 | Probability: Conditional Probability and Counting | Logic | Relationships, Representation, Patterns | Fairness and development / risk, screening and fair decisions |
| 11 | Capstone: A Mathematical Modelling Project | Relationships | Change, Representation, System | Globalization and sustainability / decisions about shared resources, access and long-term cost |
| 12 | Cumulative Revision and the Transition to DP Mathematics | Logic | Generalisation, Representation, Justification | Identities and relationships / how mathematical habits shape the way we reason elsewhere |

The register's chapter titles, key concepts, related concepts, global contexts
and explorations were compared field by field against the built framework and
agree in every case. British spelling is used for the global-context names, as
in the MYP 3 and MYP 4 volumes; the registers keep the official IB spelling.

## 3. The teaching sequence as built

Chapters 1–10 each carry the same seven-part sequence, and the section ids and
titles are exactly those of the subtopic register:

1. an opening section (`x.1`) that states the inquiry, the three question
   categories and the ATL focus, and opens the first idea;
2. four teaching sections (`x.2`–`x.5`) that develop the mathematics, each with
   its own worked examples and practice;
3. an investigation section (`x.6`) that closes the chapter with an open task
   and a structured record table;
4. a mixed-practice section (`x.7`) carrying the four criterion sets A–D plus a
   review and reflection.

Chapters 11 and 12 carry six sections each, in the register's shape for the
capstone and the transition chapter.

Every chapter carries 12 worked examples, 47 practice items, two assessment
tasks and seven reflection prompts, so that a teacher can run any chapter from
its first page without assembling material from elsewhere.

## 4. Where the register and the previous edition disagreed

The pre-rewrite MYP 5 audit recorded five places where the old edition's
mathematics was wrong or ambiguous. All five are repaired in the student text,
not only in the answer key:

1. **Chapter 7, the ambiguous case of the sine rule (SSA).** The old edition
   implied that two triangles are always possible when the given angle is not
   the included angle. The student text now states the full condition: two
   triangles when `b sin A < a < b`; exactly one right triangle when
   `b sin A = a`; no triangle at all when `a < b sin A`. Worked example 7.2 uses
   A = 30°, a = 5, b = 10, where `b sin A = a`, and concludes **one** right
   triangle. The distinction is tested at 7.1.6–7.1.8, 7.2.1, 7.3.1, 7.4.7,
   7.4.10 and 12.4.12, and is restated in the chapter review.
2. **Chapter 8 and Chapter 11, matrix order.** Matrix multiplication is
   non-commutative and the order matters; the capstone no longer contains any
   matrix work at all, so the mismatch cannot arise, and Chapter 8 teaches the
   order explicitly with worked example 8.1 (a = (3, −2), b = (−1, 5),
   3a − 2b = (11, −16)) and 8.1.4.
3. **Chapter 11, the capstone task.** The old capstone prompt was ambiguous
   about the day origin, gave a profit hint with the wrong sign and described an
   open-top tank without saying whether the top is included. The rebuilt
   capstone's two assessment tasks state every constraint explicitly and the
   raw LaTeX that appeared in the old text is gone: the whole volume contains
   zero backslash commands in the framework.
4. **Chapter 12, 12D Q6.** The old answer treated an annual doubling rate as
   2/8 = 0.25`. It is now `2^(1/8) − 1 ≈ 0.0905`, about **9.05 per cent** per
   year, derived in worked example 12.5 and tested at 12.4.6.
5. **Chapter 9, variance.** The old edition reserved population variance for DP
   mathematics while computing it descriptively in the same chapter, which
   contradicts itself. Chapter 9 teaches the population variance and standard
   deviation of a data set directly, and 9.1 states explicitly that the mean is
   the value about which the squared deviations sum to zero.

## 5. The 15 alignment points, chapter by chapter

`unit_alignment_audit.py` checks fifteen points in each of the twelve chapters —
the key concept, each related concept, the global context, the exploration, the
statement of inquiry, the factual / conceptual / debatable question trio, the
ATL focus, the Service as Action connection, the four criterion sets, the
investigation, the worked examples, the mixed practice, the review and the
reflection — and reports **180 / 180**.

Every chapter scores 15 / 15. The Service as Action, community-project and
personal-project connections are made in the student text of every chapter, as
in MYP 3 and MYP 4.
