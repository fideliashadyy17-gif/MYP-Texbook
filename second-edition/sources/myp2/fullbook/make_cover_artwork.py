#!/usr/bin/env python3
"""Build the standalone exterior cover artwork for the MYP 2 coursebook.

Writes ``covers.html`` in this directory: the MYP 2 front cover, the MYP 2 back
cover and one full-size collection cover concept for each of the other levels
(MYP 1, 3, 4, 5). Those pages are coordinated designs only -- the volumes do not
exist yet, and every page says so.

    python3 make_cover_artwork.py
    rm -f /tmp/chromium
    node export_book.mjs covers.html MYP-Collection-Cover-Concepts-Second-Edition.pdf 6

The MYP 1 front and back covers that ship inside the coursebook are the same
artwork, so they are also extracted straight from the assembled PDF by
``extract_covers.py``.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import covers  # noqa: E402
from framework import COLLECTION, LEVEL  # noqa: E402


def main():
    pages = [covers.front_cover_page(), covers.back_cover_page()]
    for v in COLLECTION:
        if v["level"] == LEVEL:
            continue
        pages.append(covers.cover_concept_page(v["level"], v["theme"]))
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8"/>'
            '<title>MYP Mathematics cover artwork</title>'
            '<link rel="stylesheet" href="/styles/book.css"/>'
            '</head><body>%s</body></html>' % "".join(pages))
    (HERE / "covers.html").write_text(html, encoding="utf-8")
    print("covers.html written:", len(pages), "pages")


if __name__ == "__main__":
    main()
