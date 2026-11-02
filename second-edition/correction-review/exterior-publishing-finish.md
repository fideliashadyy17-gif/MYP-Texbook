# MYP1 Second Edition — exterior publishing finish

**Scope:** exterior only. Front cover, author credit, back cover, five-volume collection
presentation. No academic content, chapter organisation, teaching structure, exercise,
investigation, MYP activity or interior layout was changed.

**Date:** 2 November 2026 · branch `arena/847a0a51-myp-texbook` · pipeline
`second-edition/sources/myp1/fullbook/`

## Deliverables

| file | what it is |
|---|---|
| `second-edition/exports/myp1/MYP1-Student-Coursebook-Second-Edition.pdf` | the complete coursebook, **381 A4 pages** (was 380) |
| `second-edition/exports/myp1/covers/MYP1-Front-Cover-Second-Edition.pdf` / `.png` | front cover as standalone artwork (extracted from page 1) |
| `second-edition/exports/myp1/covers/MYP1-Back-Cover-Second-Edition.pdf` / `.png` | back cover as standalone artwork (extracted from page 381) |
| `second-edition/exports/myp1/MYP-Collection-Cover-Concepts-Second-Edition.pdf` | 6 pages: MYP1 front, MYP1 back and one full-size cover concept each for MYP 2–5 |
| `second-edition/sources/myp1/fullbook/covers.py` | editable cover artwork source (inline SVG + CSS, fully vector) |
| `second-edition/sources/myp1/fullbook/make_css.py` | cover stylesheet source |
| `second-edition/sources/myp1/fullbook/framework.py` | cover/back-cover text, author constant, collection data |
| `second-edition/qa/myp1/fullbook/` | QA report, page map and renders of the new covers |

## 1. Front cover

Designed from the first-edition visual identity (deep green, cream, gold, rust; Fraunces /
Source Serif 4 / Inter) rather than adjusting the previous cover:

- **Composition** — full-bleed deep-green field with a soft radial gradient, a faint graph-paper
  grid that fades across the page, and a portrait illustration plate on the right.
- **Illustration** — one coherent MYP1 plate built from four mathematical elements: the nested
  golden-rectangle squares with the spiral of quarter circles (geometric construction), two
  overlapping sets with the intersection shaded (sets), a straight line through three marked
  points (coordinates and patterns) and a number line with a marked half (number
  representation). Three small concept labels — STRUCTURE, RELATIONSHIPS, QUANTITY — tie the
  elements together.
- **Hierarchy** — `MYP` eyebrow, `Mathematics` in Fraunces, a large gold `1` with
  `STUDENT COURSEBOOK` and `MYP 1 · YEAR 1 · TEN CHAPTERS IN FIVE PARTS`, italic standfirst,
  gold rule, the ten chapter topics, a "How this book works" note and the four MYP assessment
  criteria.
- **Required information** — `MYP MATHEMATICS · STUDENT COURSEBOOK`, `MYP 1`, `SECOND EDITION`
  and the author credit `SADIKOU MOUKODDIM` in the bottom band, with
  `MYP MATHEMATICS · VOLUME 1 OF 5`.

## 2. Author credit

`SADIKOU MOUKODDIM` appears, in the same uppercase letterspaced treatment, on:

1. the front cover (bottom band),
2. the imprint / title page (page 2), as an `AUTHOR` credit above "About this edition",
3. the back cover (bottom band),
4. every MYP 2–5 collection cover concept.

No qualifications, professional titles, biography, credentials, publisher, school branding, ISBN,
publication date or other bibliographic data are claimed anywhere.

## 3. Back cover

- Same palette, typography and grid language as the front cover, with the cover plate echoed
  faintly behind the text.
- A short description drawn only from the book's actual content: ten chapters that open with a
  task, the investigate → conclude → formal sequence, worked examples, 722 practice items
  separated into Criterion A–D practice, the Service as Action / Community Project / Personal
  Project (MYP 5) connections, and the answers, formula bank, glossary and references at the back.
- Small print restates what the file does not claim (no ISBN, publisher, print specification or
  commercial print-readiness claim).

## 4. Five-volume collection presentation

The back cover carries a strip of five miniature covers (30 × 45 mm each): **MYP 1 highlighted
with a gold border and the caption `VOLUME 1 · THIS VOLUME`**, and MYP 2–5 captioned
`VOLUME n · FORTHCOMING`. Each miniature uses the same construction — `MYP` label, level motif,
large level numeral, `MATHEMATICS` — with its own mathematical illustration:

| level | illustration |
|---|---|
| 1 | nested squares, spiral and number line (the MYP1 hero plate, reduced) |
| 2 | growth pattern with a line through the corners (ratio and proportion) |
| 3 | scatter of points with a line of best fit |
| 4 | quadratic with intercepts and axis of symmetry |
| 5 | exponential and logarithmic curves |

Volumes 2–5 do not exist yet. The back cover says so explicitly ("Volumes 2–5 are in
preparation; the covers shown here are coordinated collection designs, not published volumes"),
and the full-size concepts in `MYP-Collection-Cover-Concepts-Second-Edition.pdf` are each
labelled `COVER CONCEPT` / `COLLECTION COVER CONCEPT · VOLUME IN PREPARATION. NOT A PUBLISHED
VOLUME.` They are reusable artwork for when those volumes are produced.

**Future consistency:** when MYP 2–5 are built, each back cover should carry the same
five-cover strip with its own level highlighted. The artwork is parameterised by level in
`covers.py` (`collection_strip()`, `cover_concept_page()`), so the strip can be regenerated for
any volume without redrawing it.

## 5. Interior preservation — verified

- The back cover was appended **after** the references page, so no interior page moved.
- Page-by-page text comparison of the previous 380-page build against the new 381-page build:
  **pages 3–380 are identical** (378 pages compared, 0 differences). Vector and image counts were
  also compared on a 12-page random sample: no differences.
- Only page 1 (cover) and page 2 (imprint, author credit added) differ.
- Item count, answer pages, chapter start pages, contents and back-matter positions are unchanged
  (chapters 8/37/67/93/122/145/168/237/260/283; answers 306, formula 371, glossary 376,
  references 380).

## 6. QA

`second-edition/qa/myp1/fullbook/book-qa.json` → **STATUS: PASS**, including a new `exterior`
check group: front cover title/level/author/edition, author credit on front cover + imprint +
back cover, collection heading, all five volume captions, "this volume" on MYP1, exactly four
"forthcoming" captions, and the no-ISBN statement. Export gate: 381 pages, 0 overflow, 0 raw
placeholders, 0 raw math, 0 KaTeX errors, 0 console errors; fonts embedded.

Renders inspected: `qa/myp1/fullbook/renders/p001-front-cover.png`, `p002-imprint.png`,
`p381-back-cover.png`, `concept-1…6.png`.

## 7. Print specifications still required

The exterior is vector and resolution-independent, and the trim is the A4 page box used
throughout the book. Still unknown, and therefore not invented:

- **spine width** (depends on the printer's paper stock and the 381-page count),
- **trim size** if a non-A4 trim is wanted,
- **paper stock and weight**, which drives the spine and the cover board,
- **bleed** (this file has none: the artwork runs to the A4 page edge, not beyond it),
- **cover finish** (lamination, spot UV, foil) and whether the printer wants a separate
  spine panel or a full wrap.

Once those are confirmed, the covers can be re-exported at the exact trim and bleed, and a spine
panel can be added to `covers.py` without touching the interior.
