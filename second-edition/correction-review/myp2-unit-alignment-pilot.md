# MYP 2 — unit alignment pilot (Chapter 1) and diagnosis of the remaining chapters

Prepared for review before the alignment framework is applied to chapters 2–11.
Nothing in the approved MYP 1 prototype has been changed.

## 1. Status of the existing work

* The whole MYP 2 build is committed on branch `arena/c767ce09-myp-texbook`
  (commit `6adf119`, tree clean): `framework.py` (11 chapters), `diagrams2.py`,
  `build_book.py`, the CSS/KaTeX/PDF/QA toolchain and the exported A4 PDF.
* Exported book: **411 pages, 3 219 015 bytes**, A4, fonts embedded,
  **0 overflow, 0 placeholders, 0 raw maths, 0 console errors**, 517 practice
  items; mechanical QA `book-qa.json` → **STATUS: PASS**.
* Chapters 2–11 are byte-for-byte the same authored content as before this
  alignment pass; only Chapter 1 has been revised.

## 2. Diagnosis of the eleven MYP 2 chapters (mechanical audit)

Audit tool: `unit_alignment_audit.py` (15 alignment points per chapter).

| Requirement | Chapter 1 | Chapters 2–11 |
| --- | --- | --- |
| Key concept, related concepts, global context shown on the opener | yes | yes |
| Statement of inquiry present and chapter-specific | yes | yes |
| ATL, engagement hook, three question categories | yes | yes |
| **Global context *exploration* named** | **added** | **absent (0/10)** |
| **Statement of inquiry phrased as a statement that names the key and related concepts** | **yes** | **no — all ten are phrased as questions** |
| **Every investigation opens with a formulated inquiry question** | **yes (4/4)** | **no (0/41)** |
| Investigation → observation → mathematical conclusion → formal development | yes | yes |
| Worked examples with all six required parts | yes (8/8) | yes (66/66) |
| Criterion A/B/C/D practice, assessment, review, projects | yes | yes |
| Service as Action / Community Project / Personal Project (MYP 5) | yes | yes |
| **Final reflection returning to the statement of inquiry** | **added** | **absent (0/10)** |

Audit score before the pilot: **93/165 points** across the eleven chapters.
After the pilot: **108/165**, with Chapter 1 at **15/15**.

Three systematic gaps, all of which are additions inside the existing page
model rather than changes to it:

1. no explicit Global Context exploration;
2. no inquiry question opening each investigation;
3. no closing reflection that returns to the statement of inquiry;
4. the statements of inquiry are phrased as questions and do not name the key
   concept, the related concepts or the exploration, so the "central thread"
   could not be traced.

## 3. The pilot: Chapter 1 · Ratios and equivalent ratios

### Unit framework

| Element | Content |
| --- | --- |
| Key concept | Form |
| Related concepts | Equivalence · Representation |
| Global context | Fairness and development |
| Global context exploration | Inequality, difference and inclusion |
| Statement of inquiry | *The form of a ratio, and the equivalence of its different representations, allow a limited resource to be shared fairly and allow that fairness to be justified and checked.* |
| Factual question | What does the ratio 3:5 compare, what is its simplest form, and how do you generate ratios equivalent to it? |
| Conceptual question | Why can one ratio describe many different-sized situations, and how does representing it as a unit rate or a ratio table change what you are able to compare? |
| Debatable question | Is a ratio always the fairest way to share a limited resource, and how could you use mathematical evidence to defend your position? |

The statement of inquiry names the key concept (*form*), both related concepts
(*equivalence*, *representations*) and the global context with its exploration
(fair shares for a limited resource, inequality and inclusion). It is a claim
that can be investigated, and it is deepened by the chapter rather than
restated: the student begins by asking whether one comparison can describe many
situations and ends by asking whether a ratio is ever the *fairest* sharing
rule, which requires evidence and admits limitations.

### Inquiry questions opening the four investigations

| Section | Inquiry question | Mathematical conclusion that answers it |
| --- | --- | --- |
| 1.1 Understanding ratio language | How can one ratio describe a comparison between two quantities, and what does its simplest form tell us about that comparison? | a : b = (ak) : (bk) for any non-zero k, so one ratio describes the comparison in any size and its simplest form is the shortest honest description. |
| 1.2 Equivalent ratios and simplest form | What stays the same when both parts of a ratio change, and how can you tell whether two ratios describe the same comparison? | What stays the same is the comparison: equivalent ratios are exactly the ratios that reduce to the same simplest form. |
| 1.3 Ratio tables and double number lines | How can a ratio table or a double number line find a missing value in a comparison without guessing? | A missing value is found by locating the multiplier in one row and applying it to the other. |
| 1.4 Sharing and comparing with ratios | When is a sharing rule fair, and how can you check that a sharing really matches the rule that was agreed? | A sharing is fair when the rule is stated first and the result is checked: find the value of one part, then verify the total and the simplest form. |

Each investigation now follows the required sequence: **inquiry question →
purposeful tasks → exploration and discovery → mathematical conclusion →
formal development → worked examples → practice**. The formal development page
still comes after the investigation and its conclusion, and the investigation
still precedes the formal statement of the same idea.

### Global context made mathematically authentic

The exploration is carried by mathematics that genuinely belongs to the chapter,
not by decoration:

* investigation 1.1 shares a donation of coloured tiles between two classes, so
  the shaded : unshaded ratio *is* the sharing rule;
* investigation 1.4 shares 120 donated books between two year groups and asks
  which sharing actually matches the agreed ratio;
* worked example 1.4 and Criterion D items compare value per unit and split a
  prize in the ratio of hours contributed, which is a fairness claim that can be
  checked;
* the Service as Action opportunity shares donated supplies between two year
  groups in a ratio based on need, and the Community Project asks *what sharing
  rule gives the fairest distribution*.

### Final reflection

The chapter review page now carries **"Returning to the statement of
inquiry"** with seven prompts and a writing space: restate the statement of
inquiry in the student's own words; name the mathematical ideas used; explain
how the key concept and related concepts appeared; connect the learning to the
global context and its exploration; justify with evidence from an investigation
or worked example; say whether understanding has changed; and identify
limitations and further questions.

### What was *not* changed

Chapter sequence, section titles, investigation tasks, tables, diagrams,
worked examples (all six parts), the 47 Criterion A–D practice items and their
answers, the assessment tasks, the review vocabulary and mixed practice, the
Service as Action / Community Project / Personal Project connections, the page
model, the palette, the typography and the running heads. The additions occupy
space that was previously empty on the opener, the investigation page and the
review page, so the chapter is still 33 pages and the book is still 411 pages.

## 4. Alignment audit for the pilot

```
Chapter 1 · Ratios and equivalent ratios  ->  15/15 points
```

All fifteen points pass. The audit is reproducible with
`python3 unit_alignment_audit.py 1`.

## 5. How the MYP 1 prototype is preserved

* No MYP 1 source, export, cover or QA file has been touched; the MYP 1 build
  remains at 381 pages with QA STATUS: PASS.
* The MYP 2 pipeline copies the MYP 1 architecture: the same page model
  (`.page`, running heads, page numbering), the same CSS class vocabulary, the
  same palette and typography, the same investigation → teaching → worked
  example → criterion practice → assessment → review → projects order.
* The alignment additions reuse existing classes (`.callout`, `.label`,
  `.assessment-task`, `.construction-space`, `.review-grid`) and existing page
  types; no new page structure and no new visual language were introduced.
* Where the MYP 1 opener already showed key concept, related concepts and
  global context, MYP 2 now additionally names the exploration — the same
  information, one more line, in the same card.
* Renderer changes are conditional: a chapter without an exploration, an
  inquiry question or a reflection renders exactly as it did before, which is
  why chapters 2–11 are unchanged in this build.

## 6. Next step

Awaiting approval of this pilot. On approval the same framework will be applied
to chapters 2–11 — each with its own exploration, its own statement of inquiry,
its own inquiry questions and its own reflection, not copied from Chapter 1 —
followed by MYP 3, MYP 4 and MYP 5 with level-appropriate content.
