# MYP 3 — final alignment review of the practice exercises

A focused review of the whole MYP 3 coursebook, checking that the mathematical
practice exercises under Criteria A, B, C and D genuinely reflect the MYP
unit-planning framework of each chapter.

This is **not** a restart, a redesign or a rewrite. The chapter sequence, the
page model, the investigations, the worked examples, the teaching sequence, the
Service as Action / Community Project / Personal Project connections and the
approved MYP 1 prototype are untouched.

## 1. What was reviewed

All **470 practice items** in the ten chapters (47 per chapter: 12 under
Criterion A, 11 under Criterion B, 12 under Criterion C, 12 under Criterion D),
together with their 470 answers and the reasons given in the answer section.

Each item was tested against the unit framework of its own chapter:

| Test | Question asked of every item |
| --- | --- |
| Key concept | Does the item exercise the chapter's key concept (form, relationships, logic)? |
| Related concepts | Does it require the related concepts named in the statement of inquiry (quantity, equivalence, representation, patterns, generalisation, change, systems, space, justification, measurement, models)? |
| Global context and exploration | Is the mathematical situation drawn from the chapter's official global context and exploration, rather than a generic drill? |
| Statement of inquiry | Does the item help build the understanding the statement of inquiry claims? |
| Factual / conceptual / debatable questions | Does the body of practice support the three question categories — recall and procedure, reasoning and understanding, justification and evaluation? |
| Criterion fit | Is the item assigned to the criterion it genuinely assesses? |

The review was mechanical as well as editorial: a MYP 3-adapted diagnostic
(`myp3_practice_audit.py`) flagged every item whose prompt and reasoning
contained no contextual or conceptual vocabulary of its chapter, and each flagged
item was then read and judged.

**Result: 449 of 470 items match their criterion on the mechanical test.**

| Criterion | Items | Match | Flagged |
| --- | --- | --- | --- |
| A · Knowing and understanding | 120 | **120** | 0 |
| B · Investigating patterns | 110 | **107** | 3 |
| C · Communicating | 120 | **117** | 3 |
| D · Applying mathematics in real-life contexts | 120 | **105** | 15 |
| **Total** | **470** | **449** | **21** |

Per chapter the split is exactly A = 12, B = 11, C = 12, D = 12 (47 items).

## 2. The 21 flagged items, read individually

The mechanical test over-flags Criterion D whenever the real-world keyword list
is narrower than the situations the chapter actually uses. Every flagged item
was read. All 21 are authentic tasks for the criterion they sit under; none is a
misassignment, and none was changed.

### Criterion B (3 flagged)

These are genuine investigations in which the pattern is described in words
rather than in the vocabulary the keyword list expected.

* **3.4.2, 3.4.6** — items that ask the student to find a rule from a table of
  paired values and then test it on a pair that was not given. This is
  formulating and testing a generalisation, which is what Criterion B at Year 3
  asks for; the word "generalisation" simply does not appear in the prompt.
* **7.2.5** — an item that asks whether a claimed scale factor holds for every
  corresponding length. The task is to justify a generalisation about a family
  of similar figures, not to compute one ratio.

### Criterion C (3 flagged)

These are communication tasks whose demand is structural rather than verbal.

* **4.3.3, 5.3.2** — items that ask the student to choose between a table, a
  graph and an algebraic rule and explain which answers a stated question best.
  Selecting and justifying a complete representation is Criterion C work even
  though no explanatory prose is requested in the prompt itself.
* **9.3.4** — an item that asks the student to label a scatter plot fully and
  state in one sentence what the plot does and does not show. Complete,
  correctly labelled representation plus a precise statement of scope.

### Criterion D (15 flagged)

These are real-context tasks in which the authentic situation is described in
the language of the situation rather than in generic "real life" wording.

* **8.4.2, 8.4.3, 8.4.8, 8.4.11** — packing, filling and canvas problems
  (cubes in a box, cups in a jug, grain silo, conical tent). Each requires the
  student to identify which measurement is relevant, convert units, decide what
  to round and comment on whether the answer is sensible — the four strands of
  Criterion D, in the context of the chapter's global context (*human impact on
  the environment*).
* **8.4.10** — explain whether a 1% error in a radius matters more or less than
  a 1% error in a height. This is commenting on the accuracy and sense of a
  result, which is the highest strand of Criterion D.
* **9.4.4, 9.4.8** — an income gap between two neighbourhoods, and a line of
  best fit extrapolated beyond the collected data. Both ask the student to say
  what the mathematics can and cannot support, in the chapter's global context
  (*inequality, difference and inclusion*).
* **10.4.5, 10.4.9** — a lottery ticket and a quality check on a sample. Both
  require the student to state the uncertainty attached to an estimate, which is
  the Criterion D demand in the chapter's global context (*beliefs and values*).
* The remaining flagged D items are of the same kind: a concrete situation
  (a hire charge, a fuel bill, a survey, a dosage, a ramp) in which the student
  must select the mathematics, carry it out and then judge the result.

## 3. Criterion fit by design

The criterion split is not a label applied after the fact; the four sets are
written to different demands.

* **Criterion A** items are knowledge and understanding applied to familiar and
  unfamiliar problems, with a check on the result. They are the only set in
  which a single correct answer is the whole task.
* **Criterion B** items are additional genuine pattern investigation. None of
  them repeats a worked example: each supplies a new pattern, asks for a
  conjecture, and then asks for the generalisation to be justified rather than
  illustrated. At Year 3 a justification is a logical argument, not a list of
  cases, and the items are written to that standard.
* **Criterion C** items require correct notation, a complete representation and
  reasoning organised so that a reader can follow it. Several explicitly ask for
  a structure ("set out your working so that another student can follow it").
* **Criterion D** items are authentic situations drawn from the chapter's global
  context and exploration. Each asks the student to identify the relevant
  information, apply the mathematics, and comment on the accuracy and sense of
  the result.

## 4. What was deliberately not done

* No practice item, answer or reasoning was copied from MYP 2.
* No item was moved between criteria to make the mechanical count look better.
  The 21 flagged items were read, judged and left where they are, because they
  belong where they are.
* The approved MYP 1 prototype pages are not touched.

## 5. Status

470 items, 470 answers with student-facing reasoning, 40 answer pages,
**449/470 mechanical match** with all 21 exceptions confirmed by reading.
The practice sets are aligned to their unit frameworks and to their criteria.
