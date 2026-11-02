# MYP1 Chapter 7 correction prototype

This is a separate prototype, not a replacement for the unapproved revision proofs.

## Build

```bash
python build_prototype.py
AWS_EXECUTION_ENV=nodejs22.x node export.mjs
```

`build_prototype.py` writes `index.html` and `exercises.json`. `export.mjs` checks page overflow and writes the PDF to `../../../exports/myp1/prototype/MYP1-Chapter-07-Prototype.pdf`.

## Contents

- `styles.css` — A4 print design system.
- `assets/fonts/` — Fraunces, Source Serif 4, Inter.
- `build_prototype.py` — editable page content, SVG diagrams and exercise data.
- `exercises.json` — 35 items, 12 visual.
- `export.mjs` — Chromium PDF export with overflow gate.

## Status

Awaiting Stage 3 approval. Do not roll out to other chapters until approved.
