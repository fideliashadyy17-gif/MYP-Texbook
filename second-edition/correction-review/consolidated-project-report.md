# Consolidated Project Report — MYP Mathematics Student Coursebooks, Second Edition

**Date:** 2026-11-21 · **Branch:** `arena/c2611429-myp-texbook` (from `main` @ `445af0d`)
**Author credit (all volumes):** SADIKOU MOUKODDIM
**Status:** Five complete volumes built, QA-passed, visually reviewed and delivered as PDFs with editable sources.

---

## 1. Handover checkpoint vs. verified reality

The handover brief reported a Typst workflow, branch `arena/3a7b6106-myp-texbook`,
commits `b575f8c`/`3a1f2ba`/`cb699ae`/`ea07988`, MYP1 Chapters 1–4 proofs,
percentage/budget and MYP2 ratio drafts, and preserved dedication/acknowledgements/
about-author placeholders.

**None of those items exists in the repository.** The verified state on takeover was:

| Claimed | Actual |
|---|---|
| Branch `arena/3a7b6106-myp-texbook`, 4+ commits | Single commit `445af0d` ("Add files via upload"); branch `arena/c2611429-myp-texbook` |
| Typst production environment | No `.typ` files anywhere. The established pipeline is **HTML/CSS + Chromium (Pipedream/PagedJS-style paged media) + KaTeX**, under `second-edition/sources/myp{1..5}/fullbook/` |
| MYP1 Ch1–4 proofs, teaching drafts | Five **complete assembled books** already built (see §2), plus MYP1 chapter proofs and the Ch7 prototype |
| Dedication/Acknowledgements/About-author placeholders preserved | **Absent** from all five books (only imprint "About this edition" + author credit) |
| Rejected edition preserved | **Not found** anywhere in the tree or history |

Preserved as found: five first-edition PDFs at the repository root (MYP1 240pp, MYP2 260pp,
MYP3 281pp, MYP4 458pp, MYP5 340pp) and nine reference PDFs (summative assessments and
MYP2 examinations). No first-edition or reference file was modified.

**Decision:** the existing HTML/CSS pipeline was preserved and completed rather than
rebuilt in Typst. Rebuilding five books in a new typesetting system would have
discarded validated work (3,000+ practice items, QA gates, approved Ch7 prototype
design) with no academic benefit. The brief's Typst instruction could not be followed
because no Typst environment exists in this repository; this is recorded as a limitation,
not silently ignored.

---

## 2. Delivered volumes (all rebuilt and re-verified in this session)

| Volume | PDF | Pages | Practice items | Chapters | QA |
|---|---|---:|---:|---:|---|
| MYP1 | `second-edition/exports/myp1/MYP1-Student-Coursebook-Second-Edition.pdf` | 385 | 722 | 10 | PASS |
| MYP2 | `second-edition/exports/myp2/MYP2-Student-Coursebook-Second-Edition.pdf` | 425 | 517 | 11 | PASS |
| MYP3 | `second-edition/exports/myp3/MYP3-Student-Coursebook-Second-Edition.pdf` | 458 | 470 | 10 | PASS |
| MYP4 | `second-edition/exports/myp4/MYP4-Student-Coursebook-Second-Edition.pdf` | 694 | 658 | 14 | PASS |
| MYP5 | `second-edition/exports/myp5/MYP5-Student-Coursebook-Second-Edition.pdf` | 651 | 564 | 12 | PASS |

Total: **2,613 pages, 2,931 practice items** (all with student-facing answers and reasoning).

Each volume contains: front cover, imprint/title page with author credit, **dedication
placeholder (p.3), acknowledgements placeholder (p.4), about-the-author placeholder
(p.5)**, how-to-use guide, introduction, contents, all teaching chapters (inquiry
framing with key/related concepts, global context, statement of inquiry, factual/
conceptual/debatable questions, ATL, investigations, worked examples, Criterion A–D
practice, application/assessment/review, Service as Action / Community Project /
Personal Project connections), answers and reasoning, formula bank, glossary,
references, back cover. Standalone front/back cover PDFs and PNGs are in
`exports/myp{1..5}/covers/`.

Unit-alignment audits: MYP2 165/165, MYP3 150/150, MYP4 210/210, MYP5 180/180.
MYP1 chapter math QA: all chapters pass (e.g. Ch6–10: 55–56/55–56).

---

## 3. Defects found and fixed in this session

1. **Glossary tuple leak (MYP2–5, every glossary page).** `build_book.py` rendered
   `esc(t)` where `t` is the `(term, definition, chapter)` tuple, printing raw Python
   reprs such as `('Absolute value', 'The distance…', 4) ch. 4` in bold above each
   definition. Fixed to `esc(t[0])` in myp2–5. MYP1 was unaffected. Verified: no
   `('` sequences remain in any glossary.
2. **Missing personal pages (all five).** Added Dedication, Acknowledgements and
   About the Author placeholder pages after the imprint, with contents entries and
   correct page numbers. Placeholders name no one and invent no biography; the
   About-the-Author page carries only the approved credit SADIKOU MOUKODDIM.
3. **MYP1 contents overflow.** The single contents page overflowed by 54px with the
   three new rows. Split MYP1 contents into two pages (consistent with MYP2–5) and
   updated `qa_book.py` to read both contents pages.
4. **MYP4/MYP5 cover overlap.** Criterion D ("Applying mathematics in real-life
   contexts") wrapped onto the gold rule above the author band. Tightened cover
   spacing (topics line-height 1.85→1.6, inquiry/criteria margins 8/9mm→5mm) in
   myp4/myp5 `make_css.py`. Verified visually.
5. **MYP5 unit-circle stray line.** A short segment floated outside the circle
   (`M330 190 L344 258`). Replaced with a true tangent through the marked point,
   perpendicular to the radius (`M296 186 L328 246`). MYP4's tangent was verified
   correct and left unchanged.

All five books were fully rebuilt (`make_css → build_book → render_math →
export_book → qa_book`) with **0 overflow, 0 KaTeX errors, 0 console errors,
0 missing glyphs** at export, and `book-qa.json` STATUS: PASS for every volume
(A4, embedded fonts, folios match physical pages, chapter starts and contents
accurate, full question/answer coverage).

---

## 4. Verification performed

- **Structural:** `qa_book.py` PASS ×5 (page count/size, embedded fonts, no
  replacement chars/placeholders/raw math, folios, chapter starts, contents,
  item coverage, back matter).
- **Alignment:** unit-alignment audits PASS ×4 (MYP2–5); MYP1 chapter math QA PASS.
- **Mathematical (independent spot checks):** 13 recomputations across all levels
  (ordering, powers, decay, area, cylinder volume, profit, tiles, independence,
  doubling rate, ratios, surds, cell counts) — all PASS. Worked examples and
  answers were additionally read on rendered pages (e.g. MYP3 √3 irrationality
  proof, MYP5 polynomial degree proof, MYP4 answer key).
- **Visual (readable size, not contact sheets):** covers (all five), contents,
  dedication/about-author pages, chapter covers, theory/worked-example pages,
  practice pages, answers pages, glossaries, back covers — inspected as rendered
  PNGs at 90–110 dpi. No clipping, blank pages, or tofu found in the sampled pages.
- **Practice diagnostics:** `practice_audit.py` flags a small number of items on a
  mechanical keyword test (MYP5: 11/564). These are known diagnostics documented in
  the earlier production reports, not errors; the items were not rewritten in this
  session.

---

## 5. Honest limitations

- **No physical print test was performed.** The PDFs are A4 review copies with
  embedded fonts and continuous pagination. No bleed, crop marks, paper stock, or
  printer colour profile has been supplied or verified; no commercial
  print-readiness is claimed (the books state this themselves).
- **Personal pages are placeholders** awaiting the author's dedication,
  acknowledgements and biography, per the brief.
- **No ISBN, publisher, or school branding** is claimed anywhere, per the brief.
  Oak International School's name/logo does not appear on any cover.
- **No Typst sources exist**; the editable sources are the HTML/CSS/Python pipeline
  under `second-edition/sources/`. Reproduction requires Node 22 + `npm ci` in each
  `tools/` directory (see each `fullbook/README.md` / build scripts).
- **The "rejected edition"** referenced in the handover could not be located; if it
  exists outside this repository it was not preserved here.
- **Practice-audit mechanical flags** (above) remain as documented diagnostics.
- First-edition PDFs and reference assessment PDFs are preserved untouched at the
  repository root.

---

## 6. File inventory

**Created/changed in this session:**
- `second-edition/sources/myp{1..5}/fullbook/build_book.py` — glossary fix (2–5),
  placeholder pages + contents (1–5), MYP1 contents split.
- `second-edition/sources/myp1/fullbook/qa_book.py` — multi-page contents check.
- `second-edition/sources/myp4,5/fullbook/make_css.py` — cover spacing.
- `second-edition/sources/myp5/fullbook/covers.py` — tangent fix.
- Regenerated: `book.html`, `book.css`, `book.manifest.json`, `book-qa.json` per level.
- Rebuilt PDFs: `second-edition/exports/myp{1..5}/MYP*-Student-Coursebook-Second-Edition.pdf`.
- New: `second-edition/exports/myp{2..5}/covers/*` (MYP1 covers re-extracted).
- This report: `second-edition/correction-review/consolidated-project-report.md`.

**Compiled:** all five PDFs (export gates passed). **Mathematically verified:**
spot checks + existing chapter/alignment audits. **Visually reviewed:** sampled
pages listed in §4. **Delivered:** the five PDFs above plus full editable sources.
