#!/usr/bin/env python3
"""Render the inspected pages of the MYP 4 coursebook PDF as PNG evidence.

The page numbers come from ``book.html`` (``data-page-id`` attributes), so the
renders always match the exported PDF page for page. The set rendered mirrors
the MYP 3 inspection set: the covers, the contents, and for every chapter the
opener, every investigation task page, the first two pages of each criterion
practice set, the reflection, and the whole of the back matter.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, "/home/user/.cache/myp-review-tools")
import fitz  # noqa: E402

PDF = ROOT / "exports/myp4/MYP4-Student-Coursebook-Second-Edition.pdf"
OUT = ROOT / "qa/myp4/fullbook/renders"
OUT.mkdir(parents=True, exist_ok=True)
ZOOM = 1.4


def wanted():
    """Return {page_id: filename} for the pages to render."""
    picks = {}
    picks["book-cover"] = "p001-front-cover.png"
    picks["imprint"] = "p002-imprint.png"
    picks["contents-1"] = "p007-contents.png"
    for n in range(1, 15):
        c = "ch%02d" % n
        picks["%s-cover" % c] = "OPENER"
        tag = "C" if n == 14 else str(n)
        for m in range(1, 7):
            picks["%s-inv-%s-%d-notes" % (c, tag, m)] = "INV"
        for tier in ("a", "b", "c", "d"):
            for k in (1, 2):
                picks["%s-crit-%s" % (c, tier) + ("-1" if k == 1 else "-2")] = "CRIT"
        picks["%s-review-reflection" % c] = "REFLECTION"
    picks["answers-1"] = "answers-start.png"
    picks["formula-1"] = "formula.png"
    picks["glossary-1"] = "glossary.png"
    picks["references"] = "references.png"
    picks["back-cover"] = "back-cover.png"
    return picks


def main():
    html = (HERE / "book.html").read_text(encoding="utf-8")
    order = re.findall(r'data-page-id="([^"]*)"', html)
    pos = {}
    for i, pid in enumerate(order, start=1):
        pos.setdefault(pid, i)
    picks = wanted()
    doc = fitz.open(PDF)
    made = []
    for pid, kind in picks.items():
        if pid not in pos:
            print("missing page id:", pid)
            continue
        page_no = pos[pid]
        m = re.match(r"^(ch\d+)-(.*)$", pid)
        if kind == "OPENER":
            name = "p%03d-%s-opener.png" % (page_no, m.group(1))
        elif kind == "INV":
            name = "p%03d-%s-%s.png" % (page_no, m.group(1), m.group(2))
        elif kind == "CRIT":
            name = "p%03d-%s-%s.png" % (page_no, m.group(1), m.group(2))
        elif kind == "REFLECTION":
            name = "p%03d-%s-reflection.png" % (page_no, m.group(1))
        else:
            name = kind
        pix = doc[page_no - 1].get_pixmap(matrix=fitz.Matrix(ZOOM, ZOOM))
        pix.save(OUT / name)
        made.append(name)
    print("rendered %d pages to %s" % (len(made), OUT))


if __name__ == "__main__":
    main()
