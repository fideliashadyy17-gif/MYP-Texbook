#!/usr/bin/env python3
"""Extract the shipped cover pages from the assembled MYP 5 coursebook as artwork.

Writes, next to the assembled PDF in ``second-edition/exports/myp5/covers/``:

* ``MYP5-Front-Cover-Second-Edition.pdf`` / ``.png``
* ``MYP5-Back-Cover-Second-Edition.pdf`` / ``.png``

The pages are taken from the compiled book, so the artwork can never drift from
what is printed inside the volume. PNG previews are rendered at 200 dpi.

    PYTHONPATH=/home/user/.cache/myp-review-tools python3 extract_covers.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, "/home/user/.cache/myp-review-tools")
import fitz  # PyMuPDF

PDF = HERE.parents[2] / "exports/myp5/MYP5-Student-Coursebook-Second-Edition.pdf"
OUT = PDF.parent / "covers"
DPI = 200


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    for index, name in ((0, "MYP5-Front-Cover-Second-Edition"),
                        (doc.page_count - 1, "MYP5-Back-Cover-Second-Edition")):
        single = fitz.open()
        single.insert_pdf(doc, from_page=index, to_page=index)
        pdf_path = OUT / (name + ".pdf")
        single.set_metadata({"title": name.replace("-", " "),
                             "creator": "MYP-Texbook fullbook assembler"})
        single.save(pdf_path, garbage=3, deflate=True)
        single.close()
        doc[index].get_pixmap(dpi=DPI).save(str(OUT / (name + ".png")))
        print("wrote", pdf_path.name, "and", name + ".png")
    doc.close()


if __name__ == "__main__":
    main()
