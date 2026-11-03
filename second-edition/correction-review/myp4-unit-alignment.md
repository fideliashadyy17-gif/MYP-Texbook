# MYP 4 — unit alignment for the whole coursebook

Prepared for review. The approved MYP 1 prototype, the MYP 2 architecture and
the approved interior are unchanged: the alignment framework was applied *inside*
the existing page model, as additions in space that was previously empty.

## 1. Status of the work

* Everything is on branch `arena/c767ce09-myp-texbook`.
* Exported book:
  `second-edition/exports/myp4/MYP4-Student-Coursebook-Second-Edition.pdf` —
  **691 pages, 5 834 068 bytes**, A4 (595 × 842 pt), 10 fonts embedded,
  **0 overflow, 0 placeholders, 0 raw maths, 0 KaTeX errors, 0 console errors,
  0 missing glyphs**, **658 practice items / 658 answers**, 56 answer pages,
  148 KaTeX expressions. Mechanical QA `book-qa.json` → **STATUS: PASS**.
* Alignment audit: **210 / 210 points** across the fourteen chapters
  (`python3 unit_alignment_audit.py`).
* Scope register: all **82 rows** of
  `second-edition/audit/evidence/subtopic-register.csv` for level 4 are matched
  exactly, section id and section title, chapter by chapter
  (13 × 6 sections + 4 capstone sections `C.1`–`C.4`).
* Practice/criterion diagnostic: **645 of 658 items** genuinely match the
  criterion they are filed under; the remaining **13** were read individually
  and confirmed as authentic fluency tasks.
* Chapter start pages: 13, 57, 101, 145, 189, 234, 278, 322, 366, 410, 456, 501,
  544, 588; answers 626, formula bank 682, glossary 687, references 690,
  back cover 691.
* Renders of every inspected page: `second-edition/qa/myp4/fullbook/renders/`
  (230 pages: covers, contents, every chapter opener, every investigation task
  page, the first two pages of each Criterion A–D practice set, every chapter
  reflection, answers, formula bank, glossary, references, back cover).

## 2. The unit framework as built

Every chapter is a complete MYP unit from the first page. The key concept, the
related concepts, the official global context with its official exploration, the
statement of inquiry, the three question categories and the ATL focus are taken
from the pre-rewrite MYP 4 audit and registers
(`second-edition/audit/chapter-audits/myp4-audit.md`,
`second-edition/audit/evidence/chapter-register.csv`,
`second-edition/audit/evidence/subtopic-register.csv`).

| # | Chapter | Key concept | Related concepts | Global context / exploration |
| --- | --- | --- | --- | --- |
| 1 | Number Foundations: Exponents, Surds and Accuracy | Form | Simplification, Equivalence, Approximation, Quantity | Scientific and technical innovation / precision, measurement and discovery |
| 2 | Algebraic Expressions and Factorisation | Form | Equivalence, Simplification, Pattern, Representation | Scientific and technical innovation / design, optimisation and efficient form |
| 3 | Linear Equations, Inequalities and Systems | Relationships | Equivalence, Change, System | Fairness and development / collective decisions under constraints |
| 4 | Functions, Coordinates and Linear Models | Form | Representation, Change, Pattern | Orientation in space and time / maps, routes and rates |
| 5 | Quadratic Expressions and Equations | Logic | Equivalence, Generalisation, Justification | Scientific and technical innovation / design, motion and optimisation |
| 6 | Quadratic Functions and Graphical Reasoning | Form | Representation, Change, Pattern | Orientation in space and time / arches, paths and trajectories |
| 7 | Patterns, Sequences and Generalisation | Relationships | Pattern, Generalisation, Representation | Orientation in space and time / cycles, growth and prediction |
| 8 | Growth and Financial Mathematics | Relationships | Change, Quantity, Model | Fairness and development / access, saving and long-term planning |
| 9 | Congruence, Similarity and Transformations | Form | Space, Equivalence, Representation | Scientific and technical innovation / scale models, design and measurement at a distance |
| 10 | Pythagoras, Trigonometry and Measurement | Relationships | Space, Measurement, Equivalence | Scientific and technical innovation / surveying, navigation and safe design |
| 11 | Surface Area and Volume | Form | Space, Measurement, Quantity | Globalisation and sustainability / packaging, water storage and material efficiency |
| 12 | Statistics: Distributions and Data | Relationships | Statistics, Representation, Quantity | Identities and relationships / how data about groups shape decisions about individuals |
| 13 | Probability: Combined Events | Logic | Probability, Equivalence, Systems | Fairness and development / how chance, risk and rules shape opportunities |
| 14 | Capstone: Designing a Sustainable Space | Form | Measurement, Space, Change | Globalisation and sustainability / designing places that meet present needs without exhausting future resources |

The register's chapter titles, key concepts, related concepts, global contexts
and explorations were compared field by field against the built framework and
agree in every case. British spelling is used for the global-context names, as
in the MYP 3 volume; the registers keep the official IB spelling.

## 3. The teaching sequence as built

Each chapter carries the same six-part sequence, and the section ids and titles
are exactly those of the subtopic register:

1. an investigation section (`x.6`) that closes the chapter with an open task;
2. a teaching section per register subtopic, each with an inquiry question, a
   teaching sequence, worked examples and a table of notices, observations and a
   mathematical conclusion;
3. criterion practice split A / B / C / D with the tiers labelled Fluency,
   Reasoning, Application and Challenge;
4. application and assessment pages;
5. review, mixed review and a reflection that returns to the statement of
   inquiry;
6. Service as Action, Community Project and Personal Project connections.

The capstone is numbered `C.1`–`C.4` (The brief and the modelling cycle · Data,
constraints and assumptions · Analysis, evaluation and communication ·
Assessment task and rubric), and its practice items are numbered `C.1.n` to
`C.4.n` so that the tier-to-section convention holds there too.

## 4. What the audit measures

`unit_alignment_audit.py` awards 15 points per chapter: key concept, related
concepts (each must appear in the statement of inquiry or in a teaching
paragraph, not merely in the chapter metadata), the official global context and
its exploration, the three question categories, the ATL focus, the statement of
inquiry, the investigation, the criterion practice, the application and
assessment, the review and reflection, and the project connections.

The related-concept test is deliberately strict: a concept listed in `related`
but absent from the teaching prose scores nothing. That is why the teaching
sequence was re-read after the section realignment described in section 5, and
why the words *equivalence*, *generalisation*, *justification*, *pattern*,
*representation*, *space*, *measurement*, *systems* and *quantity* are woven
into the teaching paragraphs of the chapters that name them.

## 5. Section realignment against the subtopic register

The first draft of MYP 4 was written with section titles that had drifted from
the register. The register was then treated as authoritative — as it had been
for MYP 3, where all 51 section ids and titles match — and every chapter was
realigned to it:

* **Chapters 1** already matched and was left untouched.
* **Chapters 2–8** were renamed in place; where the register asked for a section
  the draft did not have, the section was written (2.2 Common factors and
  grouping, 2.4 Special products and identities, 3.3 Systems of equations:
  graphs and substitution, 3.6 Investigation: break-even and beyond, 4.2 Distance
  and midpoint, 4.4 Parallel and perpendicular lines, 4.6 Investigation:
  modelling a fair fare, 5.1 From expressions to equations, 5.2 Solving by
  factorising, 6.3 Quadratic inequalities, 7.1 Describing and extending
  patterns, 7.4 Recursive rules and spreadsheets, 8.4 Comparing financial
  offers).
* **Chapters 9, 11, 12** gained the sixth section the register requires
  (9.4 Transformations on the coordinate plane, 11.3 Spheres and composite
  solids, 12.3 Cumulative frequency and box plots) and 11.4 Scaling surface area
  and volume was added with it.
* **Chapter 10** gained 10.2 Pythagoras in three dimensions and 10.4 Solving
  right-angled triangles, and 10.5 now carries angles of elevation, depression
  and bearings together.
* **Chapter 13** gained 13.2 Two-way tables and Venn diagrams and 13.4
  Independent and dependent events.
* **Chapter 14** was renumbered from `14.1`–`14.6` to `C.1`–`C.4` and
  consolidated, and its practice ids were renumbered to match.

The content of the sections that were folded together was not discarded: their
teaching paragraphs, worked examples and investigation tables were reused inside
the sections that absorbed them, and the QA anchors were preserved (for example
Ex 5.1 keeps `(2x − 3)(x + 4)` at x = 1, Ex 9.1 keeps the translation of
(2, 1), (5, 1), (2, 4) by (4, −3), and Ex C.1 keeps the 1 : 50 plan of
7.2 cm × 4.8 cm giving a real area of 8.64 m²).

## 6. Defects found and fixed during production

* **Missing glyphs (13).** The modifier-letter superscript `ˣ` in `y = 2ˣ` and
  the arrow `→` drawn inside an SVG table were not supplied by the embedded
  fonts. `build_book.py` now routes `ˣ` through KaTeX with the other fragile
  superscripts, and the transformation table in 9.4 uses the words "maps to"
  inside the diagram. QA now reports 0 missing glyphs.
* **Wrong running head.** `make_css.py` still substituted "MYP MATHEMATICS 3"
  into the prototype stylesheet; it now substitutes "MYP MATHEMATICS 4".
* **Chord instead of parabola.** Seven coordinate grids drew the segment joining
  the two roots, which reads as a straight line. Each now plots five points on
  the parabola, so the curve is visible. One of them (2x² + 7x + 4 = 0) also had
  its root markers corrected to −2.78 and −0.72.
* **Mislabelled solid.** The composite-solid figure labelled its radius 6 when
  the example uses 3 cm; it now reads "a cylinder of radius 3 cm and height
  10 cm".
* **Capstone part count.** The cover note said "a capstone in five parts"; the
  capstone has four, and the cover now says so.
* **Cover topic list.** The front cover listed shortened chapter names that no
  longer matched the built chapters; it now lists the fourteen chapter titles.

## 7. What has not changed

The approved MYP 1 prototype, the page model, the interior design system, the
author credit on the front cover, the imprint and the back cover, the "no ISBN,
no publisher" exterior finish, and the Service as Action / Community Project /
Personal Project connections are all as approved. No IB material has been copied:
the investigations, worked examples, practice sets, assessments, formula bank,
glossary and references are author-designed for this second edition and carry no
IB endorsement.
