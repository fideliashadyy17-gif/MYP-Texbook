# MYP 4 — final alignment review of the practice exercises

A focused review of the whole MYP 4 coursebook, checking that the mathematical
practice exercises under Criteria A, B, C and D genuinely reflect the MYP
unit-planning framework of each chapter.

This is **not** a restart, a redesign or a rewrite. The chapter sequence, the
page model, the investigations, the worked examples, the teaching sequence, the
Service as Action / Community Project / Personal Project connections and the
approved MYP 1 prototype are untouched.

## 1. What was reviewed

All **658 practice items** in the fourteen chapters (47 per chapter: 12 under
Criterion A, 11 under Criterion B, 12 under Criterion C, 12 under Criterion D),
together with their 658 answers and the reasons given in the answer section.

Each item was tested against the unit framework of its own chapter:

| Test | Question asked of every item |
| --- | --- |
| Key concept | Does the item exercise the chapter's key concept (form, relationships, logic)? |
| Related concepts | Does it require the related concepts named in the statement of inquiry (quantity, equivalence, representation, pattern, generalisation, change, systems, space, justification, measurement, model, statistics, probability)? |
| Global context and exploration | Is the mathematical situation drawn from the chapter's official global context and exploration, rather than a generic drill? |
| Statement of inquiry | Does the item help build the understanding the statement of inquiry claims? |
| Factual / conceptual / debatable questions | Does the body of practice support the three question categories — recall and procedure, reasoning and understanding, justification and evaluation? |
| Criterion fit | Is the item assigned to the criterion it genuinely assesses? |

The review was mechanical as well as editorial: a MYP 4 diagnostic
(`practice_audit.py`, output `practice-audit.json`) flagged every item whose
prompt, answer and reasoning contained no contextual or conceptual vocabulary of
its chapter, and each flagged item was then read and judged.

**Result: 645 of 658 items match their criterion on the mechanical test.**

| Criterion | Items | Match | Flagged |
| --- | --- | --- | --- |
| A · Knowing and understanding | 168 | **155** | 13 |
| B · Investigating patterns | 154 | **154** | 0 |
| C · Communicating | 168 | **168** | 0 |
| D · Applying mathematics in real-life contexts | 168 | **168** | 0 |
| **Total** | **658** | **645** | **13** |

Per chapter the split is exactly A = 12, B = 11, C = 12, D = 12 (47 items).

## 2. The 13 flagged items, read individually

Every flagged item is a short computation under Criterion A, and every one of
them is an authentic fluency task: a bare calculation is precisely what
"knowing and understanding" asks for at the start of a criterion set. None is a
misassignment and none was changed.

### Chapter 1 · Number Foundations

* **1.1.4** — *Evaluate 27^(2/3).* A fractional index evaluated directly; the
  answer 9 with "take the cube root first, then square" is the procedure the
  section teaches.
* **1.1.9** — *Rationalise 5/√7.* A single surd manipulation. Correctly A.

### Chapter 2 · Algebraic Expressions and Factorisation

* **2.1.4** — *Make x the subject of y = 3x − 7.* A one-step rearrangement.
* **2.1.10** — *Make a the subject of v = u + at.* A formula from physics
  rearranged for the acceleration. The physical context is present in the
  formula's own variables.

### Chapter 4 · Functions, Coordinates and Linear Models

* **4.1.4** — *Find f(4) for f(x) = 2x − 5.* Function notation evaluated at a
  point; this is the definition of function notation, which is the whole of 4.1.

### Chapter 6 · Quadratic Functions and Graphical Reasoning

* **6.1.3** — *State whether y = −3x² + 6 opens up or down.* Reading the sign of
  the leading coefficient.
* **6.1.4** — *Find the axis of symmetry of y = x² + 8x + 3.* The vertex
  abscissa −b/(2a) applied directly.
* **6.1.5** — *Find the roots of y = x² − 9.* The difference of two squares.
* **6.1.10** — *Evaluate 5 × 0.8³.* A repeated multiplier evaluated once, which
  is the arithmetic behind 6.5.

### Chapter 8 · Growth and Financial Mathematics

* **8.1.1** — *Increase 80 by 15% and then decrease the result by 15%.* The
  QA-anchored reverse-percentage item: 78.20, not 80. It is the chapter's
  central counter-intuitive result and belongs in the fluency set.

### Chapter 9 · Congruence, Similarity and Transformations

* **9.1.1** — *Translate (3, 2) by the vector (−2, 5).* The definition of a
  translation as a vector addition.
* **9.1.10** — *Rotate (1, 0) through 90° anticlockwise about the origin.* The
  quarter-turn rule (x, y) → (−y, x) applied to one point.

### Chapter 11 · Surface Area and Volume

* **11.1.9** — *Convert 2.5 litres to cubic centimetres.* The capacity
  conversion 1 litre = 1000 cm³, which 11.1 needs for every volume question.

## 3. Criterion fit across the book

* **Criterion A** carries the procedural core of each chapter: index and surd
  manipulation, expansion and factorisation, solving, function evaluation,
  gradient and intercept, the quadratic formula, sequence rules, percentage
  multipliers, Pythagoras and trigonometry, surface area and volume, averages,
  and probability from a sample space. The 13 flagged items are the purest of
  these and are all correct.
* **Criterion B** carries the investigations: conjecturing a rule, building a
  difference table, testing a rule on a term that was not used to find it, and
  justifying a generalisation. Every B item in the book passed the mechanical
  test, and the capstone's B items ask for a model, a check and a limitation.
* **Criterion C** carries the communication tasks: writing a complete solution,
  explaining why a rule holds, choosing between two representations, and stating
  an assumption. Every C item passed.
* **Criterion D** carries the application tasks: a fare model, a loan, a
  package, a survey, a sampling frame, a game and the capstone's design brief.
  Every D item passed, and each names a real situation from its chapter's global
  context rather than a generic drill.

## 4. Conclusion

The 658 practice items reflect the MYP unit framework of their chapters, and
the 13 items the mechanical test flagged are authentic Criterion A fluency
tasks. No item was changed by this review; the section realignment described in
`myp4-unit-alignment.md` moved teaching material, not practice items, and the
practice ids still follow the tier-to-section convention (`x.1.n` … `x.4.n`,
`C.1.n` … `C.4.n` in the capstone).
