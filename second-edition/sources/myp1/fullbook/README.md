# MYP1 assembled coursebook — build pipeline

Assembles the ten MYP1 chapters plus front matter, contents and end matter into
**one continuous A4 PDF**: `second-edition/exports/myp1/MYP1-Student-Coursebook-Second-Edition.pdf`.

The chapter sources are the ten `manuscript/chapter-NN.source.html` files in
`second-edition/sources/myp1/` (Chapters 7 and 8 are additionally cross-checked against the
prototype in `second-edition/prototype/myp1/ch07/`). The Chapter 7 theory, investigation,
assessment and project pages are copied verbatim from that approved prototype, so the approved
design is preserved exactly.

## Files

| file | role |
| --- | --- |
| `framework.py` | chapter metadata (titles, sections, item ids, answers), 94-term glossary, reference list, framework text |
| `make_css.py` | writes `book.css` — print stylesheet (A4 page box, embedded fonts, running heads, cards, KaTeX) |
| `build_book.py` | writes `book.html`, `book.manifest.json`, `book.layout.json` |
| `render_math.mjs` | replaces `[[math:…]]` placeholders with KaTeX HTML (243 expressions) |
| `export_book.mjs` | serves the book, measures every page with Chromium, exports the PDF |
| `covers.py` | exterior cover artwork: premium front cover, back cover, five-volume collection strip and the MYP 2–5 cover concepts (all inline SVG/CSS, fully vector) |
| `make_cover_artwork.py` | writes `covers.html` (MYP 1 front + back covers and the four collection concepts) |
| `extract_covers.py` | pulls the shipped cover pages out of the compiled PDF as standalone artwork |
| `qa_book.py` | structural QA of the exported PDF with PyMuPDF → `book-qa.json` |

## Build

```bash
cd second-edition/sources/myp1/fullbook
python3 make_css.py          # → book.css
python3 build_book.py        # → book.html + manifest/layout JSON
npm ci --ignore-scripts      # once, in ../tools  (KaTeX)
rm -f /tmp/chromium          # Chromium sometimes needs a cold start
node render_math.mjs         # 243 expressions
AWS_EXECUTION_ENV=nodejs22.x node export_book.mjs   # → exports/myp1/*.pdf
PYTHONPATH=/home/user/.cache/myp-review-tools python3 qa_book.py
```

### Cover artwork

```bash
python3 make_cover_artwork.py                                   # → covers.html
rm -f /tmp/chromium
AWS_EXECUTION_ENV=nodejs22.x node export_book.mjs covers.html \
    MYP-Collection-Cover-Concepts-Second-Edition.pdf 6          # → exports/myp1/
PYTHONPATH=/home/user/.cache/myp-review-tools python3 extract_covers.py
```

`extract_covers.py` writes `exports/myp1/covers/MYP1-Front-Cover-Second-Edition.pdf`
and `MYP1-Back-Cover-Second-Edition.pdf` (plus 200 dpi PNG previews) by taking pages 1
and 381 straight out of the compiled book, so the standalone artwork can never drift from
what is printed inside the volume.

`export_book.mjs` refuses to write the PDF if any page overflows its A4 box, if a `[[math:…]]`
placeholder survives, if raw LaTeX leaks into the text, or if KaTeX/Chromium logs an error.

## Conventions

- **Page ids** — front matter and back matter use readable ids (`imprint`, `howto-1`,
  `contents`, `answers-1`, `formula-1`, `glossary-1`, `references`); the 380 sequential body
  pages use `book-pNNN`. Every page is tagged in order so `book.layout.json` maps id → page number.
- **Running heads** — front matter, back matter and the assembled pages carry a running head.
  Legacy manuscript pages keep their own kickers and never receive an injected head, so no page
  is over-full.
- **Folios** — printed page numbers match the physical index; cover pages carry no folio.
- **Exterior** — the front cover (page 1) and back cover (page 381) are built by `covers.py`.
  The back cover is appended after the references, so the 380-page interior is untouched.
  Both covers carry the author credit `SADIKOU MOUKODDIM`, repeated on the imprint page;
  no publisher, ISBN, date, spine width or other bibliographic data is invented.
- **Item ids** — globally unique. Manuscript short ids are prefixed with the chapter number
  (`3.B1`, `2.G1`, `3.M1`, `3.CK1`); section ids keep their dotted form (`3.1.1`); Chapter 7
  keeps its approved `7.1.01` markup. Textual cross-references were rewritten to match.
- **Answers** — `answers-NN` pages group by chapter, then by practice group, with a reasoning
  line per item and three items per row (twelve per page).
- **Fonts** — Fraunces (display), Source Serif 4 (text), Inter (labels) and OpenSans (mathematics)
  are embedded as subsets. Symbols the text font lacks (`⊂ ⊆ ∪ ∩ ∈ ∅ ∘ ≠ → ′`, `∛`) are routed
  through KaTeX by `symbols_to_math()` in `build_book.py`, so no glyph is dropped or substituted.
- **Colour** — identity palette `#0d2a28 / #fbf6ec / #d7a55d / #b24f32`, printed with
  `print-color-adjust: exact`.

## QA

`qa_book.py` checks page count and size, embedded fonts, replacement characters, leftover
placeholders or raw math, printed folios, chapter start pages, the contents table, per-chapter
item coverage, duplicate ids, and the presence of every back-matter section. The last run is
stored in `second-edition/qa/myp1/fullbook/book-qa.json` (**STATUS: PASS**).
