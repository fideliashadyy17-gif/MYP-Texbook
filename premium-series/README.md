# Premium MYP Mathematics Series

**Author: SADIKOU MOUKODDIM**

**Status: editorial development.** This directory contains four MYP1 chapter proofs and personal-page layout proofs for all five levels, not finished coursebooks. MYP1 chapters 5–10 and the MYP2–MYP5 teaching chapters have not been produced. The chapter proofs use the root first-edition PDF as its curricular source; no rejected-edition text, template, assets or QA records were used.

- [Audit, reference review and benchmark](docs/editorial-evidence.md)
- [Source inventory](docs/source-inventory.json)
- [First-edition curriculum coverage registers for all five levels](docs/curriculum/)
- [MYP1 chapter 2 source](myp1/chapter-02.typ) · [PDF](myp1/output/MYP1-Chapter-02-Proof.pdf) · [Internal review](docs/chapter-02-review.md)
- [MYP1 chapter 3 source](myp1/chapter-03.typ) · [PDF](myp1/output/MYP1-Chapter-03-Proof.pdf) · [Internal review](docs/chapter-03-review.md)
- [MYP1 chapter 4 source](myp1/chapter-04.typ) · [PDF](myp1/output/MYP1-Chapter-04-Proof.pdf)
- [MYP1 chapter 1 source](myp1/chapter-01.typ) · [Vector figure](myp1/assets/number-line.svg) · [PDF proof](myp1/output/MYP1-Chapter-01-Proof.pdf)

## Build and validation

From the repository root, with Python 3.11 or later:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r premium-series/tools/requirements.txt
.venv/bin/python premium-series/tools/build.py
.venv/bin/python premium-series/tools/inventory.py > premium-series/docs/source-inventory.json
.venv/bin/python premium-series/tools/curriculum_index.py
```

The build checks page count, A4 dimensions, author metadata, page text presence and text-block bounds. It independently checks selected rounding cases and the two stock decisions. These checks do not certify the entire chapter mathematically or replace visual review. Each `mypN/personal-pages.typ` invokes the shared [personal-page template](shared/personal-pages.typ). Dedication and Acknowledgements are separate pages, followed by an About the Author layout. Pass approved content as `dedication`, `acknowledgements`, and `biography` when it is supplied; until then the output is explicitly a proof with placeholders only.
