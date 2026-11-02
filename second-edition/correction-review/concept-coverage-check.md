# Concept coverage check · MYP1 Chapter 7 prototype (Revision 02)

**Scope:** Chapter 7 only. The approved visual design is preserved; mathematical depth, practice volume, worked examples, assessment authenticity and answer accuracy were revised.  
**Reference PDF:** `second-edition/exports/myp1/prototype/MYP1-Chapter-07-Prototype-Revision-02.pdf`  
**Pages:** 84 · **Core practice items:** 69 · **Visual worked examples:** 14 · **Provided visual practice items:** 56/69 (81.2%)  
**QA:** `second-edition/qa/myp1/prototype/revision-02/qa-summary.json` — 95/95 checks pass; layout overflow `[]`.

## 1. Coverage by major concept

| Concept | Teaching pages | Worked examples | Practice items | Provided visuals | Thinking spread | MYP assessment link |
|---|---:|---:|---:|---:|---|---|
| 7.1 Lines, angles and angle facts | 5 | 3 (pp. 6–8) | 16 (pp. 9–14) | 11 | Understand 3 · Fluency 5 · Application 3 · Reasoning 3 · Challenge 2 | Criterion A1; Criterion C language/reasoning |
| 7.2 Parallel lines and triangles | 15–16 | 4 (pp. 17–20) | 20 (pp. 21–30) | 18 | Understand 3 · Fluency 5 · Reasoning 5 · Application 5 · Challenge 2 | Criterion A1/A2; Criterion C1/C2 |
| 7.3 Polygons and triangle inequality | 31, 38–40 | 3 (pp. 32–33, 41) | 17 (pp. 34–37, 42–44) | 13 | Understand 2 · Fluency 5 · Application 2 · Reasoning 2 · Investigation 2 · Challenge 4 | Criterion A3; Criterion B1 |
| 7.4 Ruler-and-compass constructions | 45–46 | 4 (pp. 47–50) | 16 (pp. 51–57) | 14 | Understand 2 · Fluency 7 · Application 2 · Reasoning 3 · Challenge 2 | Criterion D1; Criterion C communication |

## 2. Coverage by subtopic and teaching order

| Subtopic | Explanation | Examples | Basic practice | Application | Reasoning / investigation | Visual demand |
|---|---|---|---|---|---|---|
| Angle language and turn facts | p. 5: straight line, full turn, vertically opposite, right angle, complementary/supplementary | 7.1.1–7.1.3 | 7.1.01–7.1.08 | 7.1.09–7.1.11 | 7.1.12–7.1.16 | Angle sectors, crossing lines, right-angle split, fact table, student sketches |
| Parallel lines and transversals | p. 15: corresponding, alternate, co-interior; converse | 7.2.1 | 7.2.01–7.2.04 | 7.2.11, 7.2.19 | 7.2.05, 7.2.20 | Numbered transversal, angle chase, shelf/support table |
| Triangle and exterior-angle facts | p. 16: angle sum, exterior angle, isosceles and converse, classification | 7.2.2–7.2.4 | 7.2.06–7.2.09 | 7.2.10, 7.2.12, 7.2.13 | 7.2.14–7.2.18 | Exterior-angle diagrams, isosceles ticks, truss, kite, ramp, comparison triangles |
| Polygon angle sums | p. 31: triangulation, interior/exterior sums, regular polygons | 7.3.1–7.3.2 | 7.3.01–7.3.06 | 7.3.07 | 7.3.08 | Triangulated hexagon, quadrilateral, regular polygons, tables |
| Triangle inequality | pp. 38–40: predict → test → observe → discover → conclude | 7.3.3 | 7.3.09–7.3.11 | 7.3.12, 7.3.15 | 7.3.13, 7.3.14, 7.3.16 | Compass arcs, borderline case, number line, truss constraint |
| Bisectors and loci | p. 45: perpendicular bisector, angle bisector, equal-radius evidence | 7.4.1–7.4.2 | 7.4.01–7.4.05 | 7.4.06 | 7.4.07–7.4.08 | Construction arcs, radius comparison, gates, locus table |
| Constructing triangles | p. 46: SSS arcs and triangle inequality | 7.4.3–7.4.4 | 7.4.09–7.4.12 | 7.4.15 | 7.4.13, 7.4.14, 7.4.16 | SSS construction, isosceles locus, impossible arcs, scale model, roads |

## 3. Teaching-order guards

- The ready check (p. 3) now tests only prerequisite skills; it no longer sends students to untaught chapter items.
- Complementary angles are defined on p. 5 before 7.1.11 asks about complementary pairs.
- 7.1.09 uses a right-angle split (90° − 12°), not the triangle angle sum, because triangle sum is taught later in 7.2.
- The isosceles converse (“equal angles face equal sides”) is stated on p. 16 before 7.2.10 uses it.
- The triangle inequality is discovered on pp. 38–40 before inequality practice on pp. 42–44.
- Formal congruence terminology is avoided in 7.2.12; the kite uses “identical” triangles at MYP1 level.
- Road-locus questions specify the interior of the angle so the intended angle bisector is unique.

## 4. Answer and diagram accuracy review

- All 69 items have student-facing answers and reasoning; all 14 worked examples contain Problem, Visual Representation, Mathematical Reasoning, Step-by-Step Solution, Final Answer and Interpretation.
- Closed numeric answers were recomputed or checked against the governing identity (angle sums, parallel-line facts, polygon sums, triangle inequality, scale factor).
- Open-ended tasks are explicitly flagged where sketches, examples or explanations may vary; closed numeric items are not flagged as multiple-answer.
- Practice figures do not leak intended answers: unknowns use `x`, `?`, `x m`, `9 cm model`, or incomplete constructions.
- Diagram fixes verified in the exported PDF: parallel-line caption wording, perpendicular-bisector prose, SSS base centring/clipping, degenerate SSS labels, quadrilateral vertex order, kite wording, right-angle ramp model, and sequential figure numbering (7.1–7.18).
- Glyph fixes verified: no tofu boxes for angle, square, parallel or perpendicular symbols; mathematical prose uses words or KaTeX-safe notation.
- HTML less-than signs in inequalities are escaped and render correctly in the PDF (e.g. 4 < x < 18).

## 5. Visual inspection evidence

- All 84 pages were rendered at 130 dpi to `second-edition/qa/myp1/prototype/revision-02/page-01.png` … `page-84.png`.
- 21 four-up contact sheets were regenerated for layout scanning.
- Full-page reads covered the complete chapter; changed pages were re-read after each rebuild.
- Final inspected PDF: 84 pages, 805,410 bytes, SHA-256 `09b1963777ceee478c77103abf86881796fb273431e86b5199e40685451f905a`.

## 6. Status

This check supports a Stage 3 approval request for the Chapter 7 prototype only. It is not approval of the full MYP1 coursebook, other chapters, or MYP2. No commercial print-readiness claim is made.
