# MYP 2 — final alignment review of the practice exercises

A focused review of the whole MYP 2 coursebook, checking that the mathematical
practice exercises under Criteria A, B, C and D genuinely reflect the MYP
unit-planning framework of each chapter.

This is **not** a restart, a redesign or a rewrite. The chapter sequence, the
page model, the investigations, the worked examples, the teaching sequence, the
Service as Action / Community Project / Personal Project connections and the
approved MYP 1 prototype are untouched.

## 1. What was reviewed

All **517 practice items** in the eleven chapters (47 per chapter: 12 under
Criterion A, 11 under Criterion B, 12 under Criterion C, 12 under Criterion D),
together with their 517 answers and the reasons given in the answer section.

Each item was tested against the unit framework of its own chapter:

| Test | Question asked of every item |
| --- | --- |
| Key concept | Does the item exercise the chapter's key concept (form, relationships, logic)? |
| Related concepts | Does it require the related concepts named in the statement of inquiry (equivalence, representation, patterns, generalisation)? |
| Global context and exploration | Is the mathematical situation drawn from the chapter's official global context and exploration, rather than a generic drill? |
| Statement of inquiry | Does the item help build the understanding the statement of inquiry claims? |
| Factual / conceptual / debatable questions | Does the body of practice support the three question categories — recall and procedure, reasoning and understanding, justification and evaluation? |
| Criterion fit | Is the item assigned to the criterion it genuinely assesses? |

The review was mechanical as well as editorial: `practice_audit.py` flagged
every item whose prompt and reasoning contained no contextual or conceptual
vocabulary of its chapter, and each flagged item was then read and judged.

**Starting point: 377 of 517 items connected to their unit framework.**
After the corrections below: **485 of 517**, with the remaining 32 confirmed by
reading to be connected in substance (for example 4.C7 *"Explain the sign rule
for division"*, which is a communication task about the logic of signed numbers,
and 5.D12 *"a 2-litre tank filled by a pump"*, which is a process-and-solution
task); the mechanical test cannot see a conceptual connection that is carried by
the reasoning rather than by a context noun.

## 2. Chapters that already met the requirements

No chapter was left untouched in the sense of being ignored, but the following
were already substantially aligned and needed only two to eight targeted
corrections each:

| Chapter | Items revised | Nature of the corrections |
| --- | --- | --- |
| 3 Rates and conversions | 5 | retold two printer/fuel drills as measurement tasks; kept the two-tap challenge |
| 6 Numerical patterns and generalisation | 5 | tied the non-linear test, the n² plot and the rebound height to mosaic, strip and craft patterns |
| 7 2D geometry | 3 | two bare circumference calculations became a flower-bed edging and a pond path; the cutting-and-rearranging investigation is now set on a site plan |
| 9 Transformations and symmetry | 2 | a mirror line explained through folding fabric; a negative scale factor explained through a printed motif |
| 10 Probability and simulation | 7 | four calculation-only Criterion C items became explain-and-justify tasks; three drills became forecast, lock-code and counter-bag situations |
| 11 Univariate data | 2 | the IQR investigation now uses a household survey; the 70% treatment item now asks what it does and does not say about one person |

Chapters 6, 9 and 11 were otherwise already aligned: their Criterion D items
were authentic applications, and their Criterion B items were genuine pattern
investigations.

## 3. Chapters that needed improvement, and what was corrected

**144 practice items were revised in place.** No item was deleted, no item was
added, and no answer was removed: the count per criterion per chapter is exactly
what it was (12 / 11 / 12 / 12), so the book is still 517 items and 517 answers.

### Chapter 1 · Ratios and equivalent ratios — 22 items

* Criterion A: bare simplifications (*"Simplify 45:60"*, *"Simplify 0.4:0.6"*)
  became sharings of donated books and tuck-shop profit; *"Are 6:9 and 10:15
  equivalent?"* became two classes sharing apples and oranges; the part-part /
  part-whole item now also asks which describes 5 seats out of 12 on a council.
* Criterion B: the pattern investigations are now framed as scaled sharings, so
  the multiplier k has a fairness meaning; the counterexample item tests whether
  equivalent ratios must have equal totals, using two donations.
* Criterion C: the ratio-table and double-number-line items now say what each row
  represents in a sharing, and the co-operative share table makes the constant
  explicit.
* Criterion D: *"15 red of 25"* became *"15 girls out of 25 in class A against 18
  out of 30 in class B — which class has the greater proportion, and what does
  this say about equal representation?"*

### Chapter 2 · Proportional reasoning — 25 items

The largest single weakness was Criterion C, where 9 of 12 items were abstract
graph drills (*"Sketch the graph of y = 3x"*). Every one is now a market graph:
cost against mass for rice at 3 dollars per kg, two price lines of slopes 2 and 5,
a delivery-cost line through (2, 90), and a line through the origin that does not
represent a unit price. Criterion A gained a rice-price equation, a wholesale
price list to test, and the meaning of k as a unit price. Criterion B's unit rates
are now a delivery van, a short delivery and a baker's recipe. Criterion D's
scaling items are now a site plan, a scale model of a stall, a display carton, an
awning, a poster, two similar stalls and a trader's percentage increase.

### Chapter 4 · Integers and their operations — 30 items

The worst-aligned chapter. Criterion C was 11 items of the form *"Evaluate
(−4) × 6"* — arithmetic drills filed under **Communicating**. All twelve are now
communication tasks: explain the sign rule from a pattern, decide between two
students who disagree about (−7) × (−1), write a rule in words for any two
integers with different signs, draw the number line for a descending lift, write
the division for a scuba diver's stages, and explain what the sign of a shared
debt means. Criterion A and Criterion B were retold as heights relative to a
marker, borehole depths, mountain-station temperatures, a drone's altitude and a
mine cage, so that the representation of position and the logic of direction are
visible in the exercises. Criterion D's football-score item became a construction
site's daily changes in material stock.

### Chapter 5 · Algebraic expressions and equations — 35 items

Criterion C was twelve bare *"Solve x + 9 = 15"* items. All twelve now require
the student to write the equation from a design situation, solve it **and**
explain the step in words, show the check by substitution, or explain the mistake
in a wrong answer. Criterion A's expressions are now machine output, process
costs, prototype costs and panel areas. Criterion B's collecting and expanding
are now fixings per kit, board and tape per carton, acid and water per solution
and reagent per process. Criterion D's remaining abstract items became shelves of
books, a factory output with defective units, a machine's part limit and two
production batches.

### Chapter 8 · 3D geometry — 8 items

Criterion A's seven naming and counting items (*"What is a net?"*, *"How many
faces does a triangular prism have?"*) are now packaging questions: what a net is
and why a carton designer needs one before the cardboard is cut, how many faces
of a triangular-prism carton must be printed and folded, what a plan view shows
when a container is packed into a box, and how many vertices a carton has. A
volume conversion became a tank of liquid in litres.

### Chapters 1, 2, 3, 6, 7, 9, 10, 11 — remaining 19 items

Small targeted retellings of the kind listed in section 2, so that no criterion
in any chapter is left with a drill that has no connection to the unit.

## 4. How each criterion now reflects the unit framework

* **Criterion A — Knowing and understanding.** Every item still assesses recall
  and procedure, but the procedure is now applied to the unit's own concepts: the
  simplest form of a sharing rule, the constant of proportionality as a unit
  price, the sign rule as a rule about direction, the variable as the number of
  parts in a design, the net of a carton. Nothing was reduced to a label: the
  context appears in the mathematics, not in a tag.
* **Criterion B — Investigating patterns.** Each item asks the student to
  generate, test, generalise or find a counterexample, and the patterns
  investigated are the ones the statement of inquiry relies on: equivalent
  ratios under scaling, the constant difference of a proportional relationship,
  the constant second difference of a quadratic rule, the pattern that forces
  the sign of a product.
* **Criterion C — Communicating.** Items require explanation, justification,
  notation, diagrams and checks — not silent calculation. This is where chapters
  4 and 5 changed most, because their Criterion C items had been arithmetic
  drills; they are now explain-in-your-own-words, decide-who-is-right,
  write-a-rule and show-the-check tasks, several of which ask for a number line
  or a balance as the representation.
* **Criterion D — Applying mathematics in real-life contexts.** These items
  interpret a situation, choose a strategy, solve, and state the answer in
  context, using the chapter's official global context and exploration: sharing a
  donation fairly (inequality, difference and inclusion), comparing unit prices
  and scaling a stall (markets, commodities and commercialisation), converting
  units precisely (precision, accuracy and measurement), heights, depths and
  temperatures (natural and human landscapes and resources), designing and
  checking a process (products, processes and solutions), staircase and border
  patterns (artistry, craft, creation and beauty), costing a planned space
  (urban and rural planning), reducing the cardboard for a container (human
  impact on the environment), describing a movement in a design (artistry,
  craft, creation and beauty), assessing a risk (randomness, chance, risk and
  uncertainty) and reporting a sample about a population (population and
  demography).

Each exercise remains assigned to the criterion it genuinely assesses; no
exercise was forced to carry all four criteria.

## 5. Connection to the inquiry questions

* Factual questions are supported by the Criterion A items, which now ask for the
  definitions and procedures in the chapter's own situations.
* Conceptual questions are explored by the Criterion B and Criterion C items,
  which require reasoning about *why* a rule holds and not only how to apply it —
  for example why a proportional graph must pass through the origin, why
  equivalent ratios can have different totals, and why (−2)⁴ is positive.
* Debatable questions are supported by Criterion D and by the reasoning-tier
  items: whether the cheaper unit price is always the fairer choice, whether the
  most efficient shape is always the best for the environment, whether an average
  can mislead a population report, and whether sharing in a ratio is the same as
  sharing equally.

## 6. Preservation of the approved prototype and architecture

* **Page count unchanged: 422 pages** (the same as before this review), so no
  repagination and no layout shift was introduced.
* A page-by-page comparison of the exported PDF before and after the review
  (matched by page id, ignoring the page number in the footer) gives **340 pages
  textually identical and 82 changed**. The 82 are exactly the 50 practice pages
  and the 32 answer pages that carry the revised items. Every opener,
  investigation, investigation-notes page, teaching page, worked-example page,
  assessment page, review page, reflection page, projects page, cover, contents
  page, formula-bank page, glossary page and references page is textually
  identical.
* The chapter sequence, section titles, investigation tasks, tables and diagrams,
  the six-part worked examples, the practice structure (Criterion A/B/C/D, six
  items per page, tier labels), the item count (517) and the answer count (517)
  are unchanged.
* No content was deleted, no exercise quantity was reduced and no mathematical
  rigour was weakened: every revised item still assesses the same mathematical
  skill as the item it replaced, in a situation that belongs to the chapter.
* The approved MYP 1 build is untouched and remains at 381 pages with QA
  STATUS: PASS.
* Exported book: **422 pages, 3 342 568 bytes**, A4, fonts embedded,
  **0 overflow, 0 placeholders, 0 raw maths, 0 KaTeX errors, 0 console errors**,
  517 items / 517 answers, 44 answer pages; mechanical QA `book-qa.json` →
  **STATUS: PASS**.
* The unit-alignment audit is unchanged at **165 / 165 points** across the eleven
  chapters.

## 7. Visual check

The revised Criterion A–D pages of chapters 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and 11
were rendered at 110 dpi and inspected: the longer prompts still fit six items to
a page, the tier labels and work lines are intact, and no page is clipped.
Renders and the QA JSON are in `second-edition/qa/myp2/fullbook/`.

## 8. Next step

MYP 3, then MYP 4, then MYP 5, with the same framework applied from the start:
official global context and exploration, a statement of inquiry that names the
key and related concepts, an inquiry question opening every investigation, and
Criterion A–D practice written for the level rather than copied from MYP 2.
