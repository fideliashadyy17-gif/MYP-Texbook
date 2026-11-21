# Premium MYP Mathematics Series

**Author: SADIKOU MOUKODDIM**

**Status: editorial development.** The current teaching drafts span MYP1 Chapters 1–5 and MYP2 Chapter 1. No volume is ready for release. All mathematics is based on the root first-edition PDFs, not the rejected edition.

- [Audit, reference review and benchmark](docs/editorial-evidence.md)
- [Source inventory](docs/source-inventory.json)
- [First-edition curriculum coverage registers for all five levels](docs/curriculum/)
- [MYP1 chapter 2 source](myp1/chapter-02.typ) · [PDF](myp1/output/MYP1-Chapter-02-Proof.pdf) · [Internal review](docs/chapter-02-review.md)
- [MYP1 chapter 3 source](myp1/chapter-03.typ) · [PDF](myp1/output/MYP1-Chapter-03-Proof.pdf) · [Internal review](docs/chapter-03-review.md)
- [MYP1 chapter 4 source](myp1/chapter-04.typ) · [PDF](myp1/output/MYP1-Chapter-04-Proof.pdf)
- [MYP1 chapter 1 source](myp1/chapter-01.typ) · [Vector figure](myp1/assets/number-line.svg) · [PDF proof](myp1/output/MYP1-Chapter-01-Proof.pdf)

## Volume production

Chapters are internal production units, not approval milestones. Keep the personal pages as placeholders until the five volumes are academically and editorially complete. Do not issue chapter PDFs as final deliverables.

`tools/volumes.py` builds explicitly labelled local editorial assemblies for all five levels with cover, generated contents, personal-page layouts, available chapters and back cover. The assemblies list missing chapters and are excluded from Git. The source entry points are generated from the script and editable includes. `--check` reports missing chapter sources and four required volume-level QA records; its success would establish presence only, not certify review. Inspect signed-off reports and the complete rendered volumes before issuing final PDFs. Required reports under each `mypN/qa/`: `mathematical.md`, `visual-editorial.md`, `curriculum-alignment.md`, `print-layout.md`.

## Build and validation

From the repository root, with Python 3.11 or later:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r premium-series/tools/requirements.txt
.venv/bin/python premium-series/tools/build.py
.venv/bin/python premium-series/tools/inventory.py > premium-series/docs/source-inventory.json
.venv/bin/python premium-series/tools/curriculum_index.py
.venv/bin/python premium-series/tools/volumes.py
.venv/bin/python premium-series/tools/volumes.py --check  # nonzero until prerequisites exist
```

The build checks page count, A4 dimensions, author metadata, page text presence and text-block bounds. It independently checks selected rounding cases and the two stock decisions. These checks do not certify the entire chapter mathematically or replace visual review. Each `mypN/personal-pages.typ` invokes the shared [personal-page template](shared/personal-pages.typ). Dedication and Acknowledgements are separate pages, followed by an About the Author layout. Pass approved content as `dedication`, `acknowledgements`, and `biography` when it is supplied; until then the output is explicitly a proof with placeholders only.
