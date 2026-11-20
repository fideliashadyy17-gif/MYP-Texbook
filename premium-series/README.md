# Premium MYP Mathematics Series

**Author: SADIKOU MOUKODDIM**

**Status: editorial development.** This directory contains a seven-page MYP1 chapter proof, not a finished coursebook. MYP1’s remaining chapters and the MYP2–MYP5 books have not been produced. The proof uses the root first-edition PDF as its curricular source; no rejected-edition text, template, assets or QA records were used.

- [Audit, reference review and benchmark](docs/editorial-evidence.md)
- [Source inventory](docs/source-inventory.json)
- [Editable proof](myp1/chapter-01.typ) · [Vector figure](myp1/assets/number-line.svg) · [PDF proof](myp1/output/MYP1-Chapter-01-Proof.pdf)

## Build and validation

From the repository root, with Python 3.11 or later:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r premium-series/tools/requirements.txt
.venv/bin/python premium-series/tools/build.py
.venv/bin/python premium-series/tools/inventory.py > premium-series/docs/source-inventory.json
```

The build checks page count, A4 dimensions, author metadata, page text presence and text-block bounds. It independently checks selected rounding cases and the two stock decisions. These checks do not certify the entire chapter mathematically or replace visual review. The author’s dedication, acknowledgements and biography are reserved for front/back matter and have not been written.
