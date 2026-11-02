#!/usr/bin/env python3
"""Full-book PDF QA for the assembled MYP 1 second-edition coursebook.

Checks page count and size, embedded fonts, absence of replacement glyphs and
unresolved placeholders, printed page numbers, chapter start pages and
question/answer coverage. Writes book-qa.json next to this script.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, "/home/user/.cache/myp-review-tools")
import fitz  # PyMuPDF

PDF = HERE.parents[2] / "exports/myp1/MYP1-Student-Coursebook-Second-Edition.pdf"
manifest = json.loads((HERE / "book.manifest.json").read_text(encoding="utf-8"))
book_html = (HERE / "book.html").read_text(encoding="utf-8")
page_ids = re.findall(r'data-page-id="([^"]*)"', book_html)

doc = fitz.open(PDF)
report = {"file": str(PDF), "pages": doc.page_count, "expected_pages": manifest["pages"]}

# ---- geometry -------------------------------------------------------------
sizes = set()
for p in doc:
    r = p.rect
    sizes.add((round(r.width, 1), round(r.height, 1)))
report["page_sizes"] = sorted(sizes)
report["a4"] = all(abs(w - 595.3) < 1.5 and abs(h - 841.9) < 1.5 for w, h in sizes)

# ---- fonts ----------------------------------------------------------------
not_embedded, fonts = [], set()
for i, p in enumerate(doc):
    for f in p.get_fonts(full=True):
        xref, ext, ftype, basefont, name, encoding = f[0], f[1], f[2], f[3], f[4], f[5]
        fonts.add(basefont)
        if ext in ("n/a", "", None) and ftype not in ("Type3",):
            not_embedded.append({"page": i + 1, "font": basefont, "type": ftype})
report["fonts"] = sorted(fonts)
report["fonts_not_embedded"] = not_embedded[:20]
report["fonts_embedded"] = not not_embedded

# ---- text ----------------------------------------------------------------
texts = [p.get_text() for p in doc]
all_text = "\n".join(texts)
report["replacement_chars"] = all_text.count("\ufffd")
report["raw_placeholders"] = len(re.findall(r"\{\{[^}]*\}\}", all_text))
report["raw_math"] = len(re.findall(r"\[\[math:", all_text))
report["katex_errors"] = all_text.count("KaTeX parse error")

# ---- printed page numbers (covers carry no folio by design) ---------------
number_re = re.compile(r"^\s*(\d{1,3})\s*$", re.M)
cover_pages = {i for i, pid in enumerate(page_ids, start=1) if "cover" in pid}
bad_numbers = []
for i, t in enumerate(texts, start=1):
    if i in cover_pages:
        continue
    if str(i) not in number_re.findall(t):
        bad_numbers.append(i)
report["cover_pages"] = sorted(cover_pages)
report["missing_page_numbers"] = bad_numbers[:20]
report["page_numbers_ok"] = not bad_numbers

# ---- chapter starts -------------------------------------------------------
chapter_pages = {int(k): v for k, v in manifest["chapters"].items()}
titles = {}
for ch in chapter_pages:
    d = json.loads((ROOT / "data" / ("chapter-%02d.exercises.json" % ch)).read_text(encoding="utf-8"))
    titles[ch] = d["title"]
def norm(s):
    return re.sub(r"\s+", " ", s).lower()


bad_starts = []
for ch, start in chapter_pages.items():
    t = norm(texts[start - 1])
    if norm(titles[ch])[:24] not in t:
        bad_starts.append({"chapter": ch, "page": start})
report["chapter_start_mismatch"] = bad_starts
report["chapter_starts_ok"] = not bad_starts

# ---- contents accuracy ----------------------------------------------------
toc_text = norm(texts[6])
bad_toc = []
for ch, start in chapter_pages.items():
    if not re.search(r"%d\.\s+%s" % (ch, re.escape(norm(titles[ch])[:16])), toc_text):
        bad_toc.append(ch)
    elif not re.search(r"%d\.\s+%s.*?\b%d\b" % (ch, re.escape(norm(titles[ch])[:16]), start), toc_text):
        bad_toc.append(("number", ch, start))
report["contents_mismatch"] = bad_toc
report["contents_ok"] = not bad_toc

# ---- question / answer coverage -------------------------------------------
q_ids = re.findall(r'id="q-([^"]+)"', book_html)
a_ids = re.findall(r'data-answer-for="([^"]+)"', book_html)
proto_ids = re.findall(r'data-item-id="([^"]+)"', book_html)
report["html_questions"] = len(q_ids)
report["html_answers"] = len(a_ids)
report["prototype_item_ids"] = len(proto_ids)
missing_q = sorted(set(a_ids) - set(q_ids) - set(proto_ids))
all_practice = q_ids + proto_ids
dup_q = sorted({i for i in all_practice if all_practice.count(i) > 1})
# ids are unique within a chapter (1.1.1, 3.B1, 7.2.01 ...) and across the book
chapter_of = lambda i: i.split(".")[0]
dup_q = [i for i in dup_q
         if len([x for x in all_practice if x == i]) > 1]
report["questions_without_practice_item"] = missing_q[:20]
report["duplicate_item_ids"] = dup_q[:20]
not_in_pdf = [i for i in sorted(set(a_ids)) if all_text.count(i) < 2]
report["items_not_twice_in_pdf"] = not_in_pdf[:20]
report["items_total"] = len(a_ids)
report["coverage_ok"] = (not missing_q and not dup_q and not not_in_pdf
                         and len(a_ids) == manifest["items"])

# ---- back matter ----------------------------------------------------------
report["back_matter_starts"] = manifest["back_matter"]
for key, page in manifest["back_matter"].items():
    t = texts[page - 1].lower()
    report["back_matter_%s_ok" % key] = {
        "answers": "answers and reasoning" in t,
        "formula": "formula bank" in t,
        "glossary": "glossary" in t,
        "references": "references" in t,
    }[key]

checks = {
    "page_count": report["pages"] == report["expected_pages"],
    "a4": report["a4"],
    "fonts_embedded": report["fonts_embedded"],
    "no_replacement_chars": report["replacement_chars"] == 0,
    "no_placeholders": report["raw_placeholders"] == 0 and report["raw_math"] == 0,
    "page_numbers": report["page_numbers_ok"],
    "chapter_starts": report["chapter_starts_ok"],
    "contents": report["contents_ok"],
    "coverage": report["coverage_ok"],
    "back_matter": all(v for k, v in report.items() if k.startswith("back_matter_")),
}
report["checks"] = checks
report["status"] = "PASS" if all(checks.values()) else "FAIL"
(HERE / "book-qa.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in report.items()
                  if k not in ("fonts", "html_questions", "html_answers")}, indent=2)[:4000])
print("STATUS:", report["status"])
