# MYP1 Chapter 7 prototype · Revision 02

Targeted mathematical-depth revision of the approved Chapter 7 design. **Chapter 7 only.** Awaiting Stage 3 approval; do not roll out to other chapters or MYP levels.

## Deliverable

- PDF: `../../../exports/myp1/prototype/MYP1-Chapter-07-Prototype-Revision-02.pdf`
- Pages: 84
- Core practice items: 69
- Provided visual practice items: 56 (81.2%)
- Visual worked examples: 14
- QA: 95/95 checks pass; layout overflow `[]`
- SHA-256: `09b1963777ceee478c77103abf86881796fb273431e86b5199e40685451f905a`

## Build and export

```bash
python build_prototype.py
AWS_EXECUTION_ENV=nodejs22.x node export.mjs
```

`build_prototype.py` writes `index.html`, `exercises.json`, `worked-examples.json`, `manifest.json` and `coverage.json`. `export.mjs` checks every `.page` for overflow and writes the PDF. It exits non-zero if any page overflows.

## QA and inspection

```bash
PYTHONPATH=/home/user/.cache/myp-review-tools python qa_revision.py
```

QA writes `../../../qa/myp1/prototype/revision-02/qa-summary.json`. Rendered inspection pages and contact sheets are in `../../../qa/myp1/prototype/revision-02/`.

## Contents

- `styles.css` — approved A4 print design system plus revision layout blocks.
- `assets/fonts/` — Fraunces, Source Serif 4, Inter.
- `diagrams.py` — editable, geometry-accurate SVG figures.
- `exercises_data.py` — 69 core items, subtopics, thinking types, answers, reasoning, visual kinds, source IDs.
- `worked_examples.py` — 14 six-component visual worked examples.
- `build_prototype.py` — page composition, teaching order, inquiry, assessment, answers.
- `export.mjs` — Chromium PDF export with overflow gate.
- `qa_revision.py` — counts, coverage, closed answers, teaching order, rendering integrity.

## Related review documents

- `../../../correction-review/revision-report.md`
- `../../../correction-review/concept-coverage-check.md`
- `../../../correction-review/source-register.md`

## Status

Revision 02 is presented for Stage 3 approval. The pre-revision 28-page prototype is preserved in `../../../correction-review/evidence/pre-targeted-prototype/`. No commercial print-readiness claim is made.
