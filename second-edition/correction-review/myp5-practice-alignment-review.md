# MYP 5 — final alignment review of the practice exercises

A focused review of the whole MYP 5 coursebook, checking that the mathematical
practice exercises under Criteria A, B, C and D genuinely reflect the MYP
unit-planning framework of each chapter.

This is **not** a restart, a redesign or a rewrite. The chapter sequence, the
page model, the investigations, the worked examples, the teaching sequence, the
Service as Action / Community Project / Personal Project connections and the
approved MYP 1 prototype are untouched.

## 1. What was reviewed

All **564 practice items** in the twelve chapters (47 per chapter: 12 under
Criterion A, 11 under Criterion B, 12 under Criterion C, 12 under Criterion D),
together with their 564 answers and the reasons given in the answer section.

Each item was tested against the unit framework of its own chapter:

| Test | Question asked of every item |
| --- | --- |
| Key concept | Does the item exercise the chapter's key concept (form, relationships, logic, change)? |
| Related concepts | Does it require the related concepts named in the statement of inquiry (equivalence, generalisation, simplification, representation, patterns, change, system, space, justification, measurement)? |
| Global context and exploration | Is the mathematical situation drawn from the chapter's official global context and exploration, rather than a generic drill? |
| Statement of inquiry | Does the item help build the understanding the statement of inquiry claims? |
| Factual / conceptual / debatable questions | Does the body of practice support the three question categories — recall and procedure, reasoning and understanding, justification and evaluation? |
| Criterion fit | Is the item assigned to the criterion it genuinely assesses? |

The review was mechanical as well as editorial: a MYP 5 diagnostic
(`practice_audit.py`, output `practice-audit.json`) flagged every item whose
prompt, answer and reasoning contained no contextual or conceptual vocabulary of
its chapter, and each flagged item was then read and judged.

**Result: 553 of 564 items match their criterion on the mechanical test.**

| Criterion | Items | Match | Flagged |
| --- | --- | --- | --- |
| A · Knowing and understanding | 144 | **136** | 8 |
| B · Investigating patterns | 132 | **132** | 0 |
| C · Communicating | 144 | **142** | 2 |
| D · Applying mathematics in real-life contexts | 144 | **143** | 1 |
| **Total** | **564** | **553** | **11** |

Per chapter the split is exactly A = 12, B = 11, C = 12, D = 12 (47 items), so
the volume is internally consistent with MYP 4 (14 × 47 = 658).

## 2. The 11 flagged items, read individually

Every flagged item is a short computation or a single-idea task, and every one of
them is an authentic fluency exercise: a bare calculation is precisely what
"knowing and understanding" asks for at the start of a criterion set, and a
complete written solution is precisely what "communicating" asks for. None is a
misassignment and none was changed.

### Chapter 2 · Functions

* **2.1.2** — *Given f(x) = 4x − 7, find f(3) and f(−2).* Direct substitution,
  the first procedure the section teaches. Correctly A.

### Chapter 3 · Exponential and Logarithmic Functions

* **3.1.3** — *Evaluate 27^(−2/3).* A negative fractional index evaluated
  directly; the answer 1/9 with "take the cube root, then square, then
  reciprocate" is the taught procedure. Correctly A.
* **3.1.6** — *Given log 5 ≈ 0.6990, find log 125 and log 0.2.* Log laws applied
  to a given value; 3(0.6990) ≈ 2.097 and −0.6990. Correctly A.

### Chapter 4 · Sequences and Series

* **4.1.7** — *Find the sum to infinity of 30 + 10 + 10/3 + …* The convergent
  geometric series formula with the |r| < 1 test first. Correctly A.
* **4.3.3** and **4.3.9** — *Write a complete solution to evaluating
  Σ(5 − 2r) and Σ(4r − 1) by splitting the sum.* Both require the linearity of
  summation and the sum of the first n positive integers; both are full written
  solutions. Correctly C.

### Chapter 8 · Vectors and Matrices

* **8.1.4** — *Given a = (2, 5) and b = (−3, 1), find a · b.* A scalar product,
  computed as −6 + 5 = −1. Correctly A.

### Chapter 10 · Probability: Conditional Probability and Counting

* **10.1.10** — *How many ways can 4 books be arranged on a shelf?* 4! = 24, the
  multiplication principle in its simplest form. Correctly A.
* **10.4.9** — *A password uses 3 letters followed by 2 digits, with repetition
  allowed.* 26³ × 10² = 1 757 600, the multiplication principle applied at each
  position in a real security context. Correctly D.

### Chapter 12 · Cumulative Revision

* **12.1.3** — *Given f(x) = 4x − 7, find f⁻¹(x).* (x + 7)/4, the inverse by
  rearrangement. Correctly A.
* **12.1.11** — *Find the determinant of [[3, 5], [7, 2]].* 6 − 35 = −29 using
  ad − bc. Correctly A.

## 3. One answer corrected during the review

* **10.1.5** — *P(A) = 0.3 and P(B) = 0.6, and P(A and B) = 0.15. Are A and B
  independent?* The answer read "Yes, because 0.3 × 0.6 = 0.18 ≠ 0.15, so they
  are not independent", which contradicts itself in the first word. It now reads
  "No, because 0.3 × 0.6 = 0.18, which is not 0.15, so the events are not
  independent." The prompt and the reasoning were already correct.

This was the only contradiction found in the 564 answers; every other answer was
checked for agreement between the prompt, the answer and the reasoning.

## 4. How the practice sets are built

Criterion A carries short fluency tasks drawn from the chapter's own sections.
Criterion B carries pattern investigations that ask the student to extend,
generalise and test a rule. Criterion C carries complete written solutions to
exam-style problems, which is the criterion the MYP names "communicating".
Criterion D carries applied problems set in the chapter's global context — a
packaging decision, a screening test, a savings plan, a navigation problem — so
that the applied work is genuinely applied rather than a drill with a story
attached.

The chapter review closes each chapter with a short cumulative set and a
reflection prompt that returns to the statement of inquiry, which is the same
closing shape used in MYP 3 and MYP 4.
