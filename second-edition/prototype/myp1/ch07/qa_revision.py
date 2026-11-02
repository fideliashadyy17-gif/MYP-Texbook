"""Revision 02 QA: counts, coverage, closed-answer checks, teaching order, PDF integrity.
Run: PYTHONPATH=/home/user/.cache/myp-review-tools python second-edition/prototype/myp1/ch07/qa_revision.py
"""
from pathlib import Path
from collections import Counter
import hashlib, json, re, sys
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
from exercises_data import ITEMS
from worked_examples import EXAMPLES
SOURCE_IDS = {i["source_id"] for i in ITEMS if i.get("source_id")}

checks = []
def check(name, ok, detail=""):
    checks.append({"check": name, "pass": bool(ok), "detail": detail})
    if not ok:
        print("FAIL", name, detail)

items = {i["id"]: i for i in ITEMS}
check("69 core items", len(ITEMS) == 69)
check("14 worked examples", len(EXAMPLES) == 14)
check("unique item IDs", len(items) == len(ITEMS))
check("every example has six components and a visual", all(all(e.get(k) for k in ("problem","visual","reasoning","steps","answer","interpretation")) for e in EXAMPLES))
check("35 First-Edition source IDs mapped", len(SOURCE_IDS) == 35)
visual = [i for i in ITEMS if i.get("visual")]
check("provided visual assets >= 40%", len(visual)/len(ITEMS) >= 0.4, f"{len(visual)}/{len(ITEMS)}")
check("concept counts 16/20/17/16", Counter(i["concept"] for i in ITEMS) == Counter({"7.1":16,"7.2":20,"7.3":17,"7.4":16}))
sub = Counter(i["subtopic"] for i in ITEMS)
check("subtopics >= 8 items", all(v >= 8 for v in sub.values()), dict(sub))
think = Counter(i["thinking"] for i in ITEMS)
check("A-F thinking types present", set(think) == {"Understand","Fluency","Application","Reasoning","Investigation","Challenge"}, dict(think))
check("open-ended answers flagged multiple", all(i.get("multiple") for i in ITEMS if "may vary" in i["answer"].lower() or "your own" in i["answer"].lower() or "student row" in i["answer"].lower()))

# Closed-answer checks (independent recomputation where possible)
expected = {
 "7.1.04": ["115"], "7.1.05": ["85"], "7.1.06": ["115", "65"], "7.1.07": ["35", "65", "70", "45"],
 "7.1.08": ["15", "75", "105"], "7.1.09": ["78"], "7.1.10": ["60"], "7.1.11": ["36", "72", "108", "144"],
 "7.1.12": ["360"], "7.1.14": ["80", "160", "120"], "7.1.15": ["50", "70", "100", "140"],
 "7.2.03": ["68", "112"], "7.2.04": ["52", "128"], "7.2.06": ["60"], "7.2.07": ["30", "90"],
 "7.2.08": ["70"], "7.2.09": ["67", "65"], "7.2.10": ["50", "115"], "7.2.11": ["114"],
 "7.2.12": ["70", "140"], "7.2.13": ["76", "104"], "7.2.17": ["50", "80"], "7.2.18": ["52", "78", "50"],
 "7.2.19": ["73", "107"], "7.2.20": ["25", "60", "120"], "7.3.03": ["360", "540", "720"],
 "7.3.04": ["900", "1260", "1440"], "7.3.05": ["80"], "7.3.06": ["8", "135"], "7.3.07": ["octagon"],
 "7.3.11": ["7+9>15", "No change"], "7.3.14": ["5", "17"], "7.3.15": ["5"], "7.3.17": ["12"], "7.4.05": ["12"],
 "7.4.09": ["3.6"], "7.4.10": ["32"], "7.4.15": ["12", "1.8"], "7.4.16": ["28"],
}
for iid, vals in expected.items():
    ans = items[iid]["answer"]
    check(f"answer {iid}", all(v in ans for v in vals), ans[:120])

# Arithmetic identities behind the closed items
identities = {
 "straight 47": 47+133 == 180,
 "full 95/120/85": 95+120+85+60 == 360,
 "vertical algebra": 3*20+10 == 20+50 == 70 and 70+110 == 180,
 "parallel 68": 68+112 == 180,
 "exterior 115": 115-48 == 67 and 48+67+65 == 180,
 "isosceles 40": (180-40)/2 == 70,
 "quad 85/95/110": 360-(85+95+110) == 70,
 "regular exterior 40": 360/40 == 9 and 180-40 == 140,
 "third side 7/11": 11-7 == 4 and 11+7 == 18 and list(range(5,18)) == list(range(5,18)),
 "triangle inequality 7/9/15": 7+9 > 15,
 "truss 8": 2*5 > 8 and 2*4 == 8,
 "interior=5 exterior": 180/6 == 30 and 360/30 == 12,
 "canopy 2.4/1.5": abs(__import__("math").degrees(__import__("math").acos(1.2/1.5))-36.86989765) < 1e-6,
}
for name, ok in identities.items():
    check("identity "+name, ok)

# Teaching-order and editorial checks
html = (HERE/"index.html").read_text()
figs = [int(x) for x in re.findall(r"Figure 7\.(\d+)", html)]
check("figure numbers sequential in reading order", figs == list(range(1,19)), figs)
check("7.1.09 uses right-angle split, not untaught triangle sum", "90° − 12°" in items["7.1.09"]["reasoning"] and "180° − 90°" not in items["7.1.09"]["reasoning"])
check("complementary defined before 7.1.11", "Complementary angles sum to 90°" in html.split('data-page-id="theory-7-1"')[1].split('data-page-id="practice-7.1-7.1.11"')[0])
check("7.1.15 obtuse definition complete", "between 90° and 180°" in items["7.1.15"]["answer"])
check("road loci restricted to interior of angle", "inside the angle" in items["7.4.01"]["prompt"].lower() and "inside the angle" in items["7.4.16"]["prompt"].lower())
check("7.2.12 avoids formal congruence terminology", all("congruent" not in items["7.2.12"][k].lower() and "congruence" not in items["7.2.12"][k].lower() for k in ("prompt","reasoning","visual")))

# Manifest / PDF integrity
manifest = json.loads((HERE/"manifest.json").read_text())
pdf = ROOT/"second-edition/exports/myp1/prototype/MYP1-Chapter-07-Prototype-Revision-02.pdf"
doc = pymupdf.open(pdf)
check("PDF page count 84", len(doc) == 84)
layout = json.loads((ROOT/"second-edition/qa/myp1/prototype/revision-02-layout.json").read_text())
check("print overflow gate empty", layout["overflow"] == [])
practice = [iid for p in manifest if p["kind"]=="practice" for iid in p["items"]]
answers = [iid for p in manifest if p["kind"]=="answers" for iid in p["items"]]
check("all 69 items in practice once", sorted(practice)==sorted(items))
check("all 69 items in answers once", sorted(answers)==sorted(items))
page_of_practice = {iid:p["page"] for p in manifest if p["kind"]=="practice" for iid in p["items"]}
page_of_answer = {iid:p["page"] for p in manifest if p["kind"]=="answers" for iid in p["items"]}
check("practice precedes answers", all(page_of_practice[i] < page_of_answer[i] for i in items))
# inequality practice must come after discovery page
disc = [p["page"] for p in manifest if p["id"]=="inquiry-discovery"][0]
ineq = [page_of_practice[i["id"]] for i in items.values() if i["subtopic"]=="Triangle inequality"]
check("inequality practice after discovery", all(p > disc for p in ineq))
text = "\n".join(p.get_text() for p in doc)
check("no replacement characters", "\ufffd" not in text)
check("no raw placeholders", "{{" not in text)
check("no raw HTML entities in PDF", "&lt;" not in text and "&gt;" not in text and "&amp;" not in text)

def norm(s):
    import html as _html
    s = _html.unescape(s)
    return re.sub(r"\s+", "", s).replace("\u00ad", "")
ntext = norm(text)
check("all item prompts rendered in PDF", all(norm(i["prompt"]) in ntext for i in ITEMS), [i["id"] for i in ITEMS if norm(i["prompt"]) not in ntext])
check("all item answers rendered in PDF", all(norm(i["answer"]) in ntext for i in ITEMS), [i["id"] for i in ITEMS if norm(i["answer"]) not in ntext])
check("all item reasonings rendered in PDF", all(norm(i["reasoning"]) in ntext for i in ITEMS), [i["id"] for i in ITEMS if norm(i["reasoning"]) not in ntext])
check("all worked-example components rendered in PDF", all(norm(e[k]) in ntext for e in EXAMPLES for k in ("problem","reasoning","answer","interpretation") ) and all(norm(s) in ntext for e in EXAMPLES for s in e["steps"]))
for e in EXAMPLES:
    check(f"example {e['id']} in PDF", e["id"] in text or e["title"] in text)

summary = {
 "pdf": str(pdf.relative_to(ROOT)), "pages": len(doc), "bytes": pdf.stat().st_size,
 "sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
 "items": len(ITEMS), "worked_examples": len(EXAMPLES), "provided_visual_items": len(visual),
 "visual_fraction": round(len(visual)/len(ITEMS),3), "thinking": dict(think), "subtopics": dict(sub),
 "checks": checks, "passed": sum(c["pass"] for c in checks), "total": len(checks),
}
out = ROOT/"second-edition/qa/myp1/prototype/revision-02/qa-summary.json"
out.write_text(json.dumps(summary, indent=2))
print(json.dumps({k:summary[k] for k in ("pages","bytes","sha256","items","worked_examples","provided_visual_items","visual_fraction","passed","total")}, indent=2))
if summary["passed"] != summary["total"]:
    sys.exit(1)
