#!/usr/bin/env python3
"""Assemble the complete MYP 1 second-edition coursebook into one HTML file.

Sources
-------
* ``../data/chapter-NN.exercises.json`` and ``../manuscript/chapter-NN.source.html``
  for chapters 1-6 and 8-10 (verified chapter sources).
* ``../../../prototype/myp1/ch07/index.html`` for the approved Chapter 7 design.
* ``framework.py`` for the authored editorial framework: inquiry questions,
  investigation-first pages, criterion-separated practice, project connections,
  front matter, formula bank, glossary and references.

Output
-----
``book.html`` in this directory: front matter, chapters 1-10 with continuous
pagination, global answers, formula bank, glossary and references. Every page is
an explicit ``.page`` element, so the printed page number equals its position in
the document.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent                       # sources/myp1
EDITION = HERE.parents[2]                # second-edition
PROTO_DIR = EDITION / "prototype/myp1/ch07"
sys.path.insert(0, str(HERE))
from framework import FW, FRONT, GLOSSARY, REFERENCES  # noqa: E402

CHAPTERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PROTO_CH = 7
PART = {1: "Part I · The grammar of number", 2: "Part I · The grammar of number",
        3: "Part I · The grammar of number", 4: "Part I · The grammar of number",
        5: "Part II · Parts and proportions", 6: "Part III · Patterns and symbols",
        7: "Part IV · Shape, structure and measure", 8: "Part IV · Shape, structure and measure",
        9: "Part IV · Shape, structure and measure", 10: "Part V · Data and decisions"}
CRITERIA = {"A": ("Knowing and understanding", "a"), "B": ("Investigating patterns", "b"),
            "C": ("Communicating", "c"), "D": ("Applying mathematics in real-life contexts", "d")}
TIER_LABEL = {"ready": "Ready", "fluency": "Fluency", "reasoning": "Reasoning",
              "application": "Application", "challenge": "Challenge",
              "investigation": "Investigation", "guided": "Guided", "check": "Check",
              "assessment": "Assessment"}


# --------------------------------------------------------------------- helpers
def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def safe(s):
    """Escape text but keep a small set of inline markup used by the sources."""
    s = esc(s)
    s = re.sub(r"&lt;(/?)(u|b|i|sup|sub|strong|em)&gt;", r"<\1\2>", s)
    s = s.replace("□", '<span class="blank-box"></span>')
    return s


def tag_text(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def make_page(inner, page_id, cls="", running_left="", running_right=""):
    rh = ""
    if running_left or running_right:
        rh = ('<div class="running-head"><span>%s</span><span>%s</span></div>'
              % (esc(running_left), esc(running_right)))
    return ('<section class="page %s" data-page-id="%s">%s%s</section>'
            % (cls, esc(page_id), rh, inner))


def banner(letter, note=""):
    name, cls = CRITERIA[letter]
    extra = ' <span class="v">%s</span>' % esc(note) if note else ""
    return ('<div class="criterion-banner %s"><span class="k">Criterion %s</span>'
            '<span class="v">%s</span>%s</div>' % (cls, letter, esc(name), extra))


def render_items(items):
    out = ['<ol class="exercises">']
    for it in items:
        out.append('<li id="q-%s"><span class="qid">%s</span><span class="prompt">%s'
                   '<span class="tier">%s</span></span></li>'
                   % (esc(it["id"]), esc(it["id"]), safe(it["prompt"]),
                      esc(TIER_LABEL.get(it.get("tier", ""), it.get("tier", "")))))
    out.append("</ol>")
    return "".join(out)


def exercise_block(group, ids=None, title=None, letter=None, columns=False):
    items = group["items"] if not ids else [i for i in group["items"] if i["id"] in set(ids)]
    if not items:
        raise ValueError("no items for group %s (ids=%s)" % (group["id"], ids))
    title = title or group["title"]
    cls = "exercise-block" + (" practice-columns" if columns else "")
    parts = ['<div class="%s" data-group="%s">' % (cls, esc(group["id"]))]
    if letter:
        parts.append(banner(letter))
    parts.append("<h3>%s</h3>" % esc(title))
    if group.get("instruction") and not letter:
        parts.append('<p class="instructions">%s</p>' % esc(group["instruction"]))
    parts.append('<div>%s</div></div>' % render_items(items))
    return "".join(parts)


def figure(name, caption=""):
    return ('<figure><img src="/diagrams/%s.svg" alt="%s"/><figcaption>%s</figcaption></figure>'
            % (esc(name), esc(caption or name), esc(caption)))


# ------------------------------------------------------------------ data access
def load_chapter(ch):
    data = json.loads((ROOT / "data" / ("chapter-%02d.exercises.json" % ch)).read_text(encoding="utf-8"))
    return data


def prepare_chapter_data(ch):
    """Return (data, rename) with globally unique item ids for the assembled book.

    Short ids such as B1 or M1 are unique inside a chapter but not across the
    book, so they are prefixed with the chapter number (3.B1). Checkpoint ids
    are renamed C* -> CK* so that authored Criterion C items can use C*.
    """
    data = load_chapter(ch)
    for g in data["groups"]:
        for it in g["items"]:
            if g["id"] == "check" and re.match(r"^C\d+$", it["id"]):
                it["id"] = "CK" + it["id"][1:]
    rename = {}
    for g in data["groups"]:
        for it in g["items"]:
            if not it["id"].startswith("%d." % ch):
                new = "%d.%s" % (ch, it["id"])
                rename[it["id"]] = new
                it["id"] = new
    if rename:
        pat = re.compile(r"\b(%s)\b" % "|".join(sorted(map(re.escape, rename), key=len, reverse=True)))
        for g in data["groups"]:
            for it in g["items"]:
                for f in ("prompt", "answer", "reasoning"):
                    if it.get(f):
                        it[f] = pat.sub(lambda m: rename[m.group(1)], it[f])
    return data, rename


def max_id(data, ch, prefix):
    best = 0
    for g in data["groups"]:
        for it in g["items"]:
            m = re.match(r"^%d\.%s(\d+)$" % (ch, prefix), it["id"])
            if m:
                best = max(best, int(m.group(1)))
    return best


def manuscript_pages(ch):
    src = (ROOT / "manuscript" / ("chapter-%02d.source.html" % ch)).read_text(encoding="utf-8")
    return re.findall(r'<section class="page[^"]*"[^>]*>.*?</section>', src, re.S)


def section_titles(data):
    out = {}
    for i, s in enumerate(data.get("sections", []), start=1):
        out["%d.%d" % (data["chapter"], i)] = s["title"]
    return out


def classify(page_html):
    head = page_html[:200]
    if 'class="page cover"' in head:
        return "cover", None
    kick = tag_text(re.search(r'<div class="kicker">(.*?)</div>', page_html, re.S).group(1)) \
        if '<div class="kicker">' in page_html else ""
    h2m = re.search(r"<h2>(.*?)</h2>", page_html, re.S)
    h2 = tag_text(h2m.group(1)) if h2m else ""
    m = re.search(r"(\d+\.\d+)", kick) or re.match(r"^(\d+\.\d+)", h2)
    sec = m.group(1) if m else None
    if "Opener" in kick:
        return "opener", sec
    if kick.startswith("Getting ready") or kick.startswith("Start here"):
        return "start", sec
    if "Guided and independent practice" in h2:
        return "practice", sec
    if "Exploration" in kick:
        return "explore", sec
    if "Checkpoint" in kick:
        return "checkpoint", sec
    if "Application" in kick:
        return "application", sec
    if "Assessment practice" in kick:
        return "assessment", sec
    if "Mixed practice" in kick or "Chapter review" in kick:
        return "mixed", sec
    if sec:
        return "teach", sec
    return "other", sec


# ------------------------------------------------------------- page transforms
def rewrite_cover(page_html, ch, data, fw):
    """Chapter divider: approved palette, chapter numeral, part and inquiry block."""
    title = data["title"]
    context = data.get("context", "")
    inquiry = fw.get("inquiry", [])
    inq = ""
    if inquiry:
        lis = "".join("<li><strong>%s:</strong> %s</li>" % (esc(k), esc(v)) for k, v in inquiry)
        inq = ('<div class="inquiry"><div class="label">Inquiry questions</div><ul>%s</ul></div>'
               % lis)
    inner = (
        '<div><div class="part">%s · MYP Year 1 · Chapter %02d</div>'
        '<h1>%s</h1>'
        '<p class="standfirst">%s</p>'
        '%s</div>'
        '<div class="foot"><span>Second edition</span><span>%s</span></div>'
        % (esc(PART[ch]), ch, esc(title),
           esc(data.get("soi") or fw.get("standfirst", "")), inq, esc(context)))
    return make_page(inner, "ch%02d-cover" % ch, cls="cover")


def inject_running_head(page_html, left, right):
    if "running-head" in page_html:
        return page_html
    rh = ('<div class="running-head"><span>%s</span><span>%s</span></div>'
          % (esc(left), esc(right)))
    return re.sub(r'(<section class="page[^"]*"[^>]*>)', r"\1" + rh, page_html, count=1)


def normalise_kicker(page_html, ch):
    """Make every chapter page kicker name its chapter (chapters 1-2 lack it)."""
    def fix(m):
        kick = m.group(1)
        if re.match(r"^\d+\.\d+ · ", kick):
            kick = "Chapter %d · %s" % (ch, kick)
        return '<div class="kicker">%s</div>' % kick
    return re.sub(r'<div class="kicker">(.*?)</div>', fix, page_html, count=1, flags=re.S)


def relabel_practice(page_html, sec, titles):
    kick = "Chapter %d · Practice · Criterion A" % int(sec.split(".")[0])
    h2 = "Criterion A practice · %s %s" % (sec, titles.get(sec, ""))
    page_html = re.sub(r'<div class="kicker">.*?</div>',
                       '<div class="kicker">%s</div>' % esc(kick), page_html, count=1, flags=re.S)
    page_html = re.sub(r"<h2>.*?</h2>", "<h2>%s</h2>" % esc(h2), page_html, count=1, flags=re.S)
    return page_html


def fill_placeholders(page_html, data, by_id, rename=None):
    rename = rename or {}
    def ex_sub(m):
        gid, ids, title = m.group(1), m.group(2), m.group(3)
        g = by_id[gid]
        idlist = [rename.get(s.strip(), s.strip()) for s in ids.split(",") if s.strip()] if ids else None
        letter = "A" if gid.startswith("p") or gid == "guided" else None
        columns = gid == "mixed" and idlist and len(idlist) > 4
        return exercise_block(g, idlist, title or None, letter=letter, columns=columns)

    page_html = re.sub(r"\{\{exercise:([a-z0-9]+)(?::([^:}]*))?(?::([^}]*))?\}\}", ex_sub, page_html)
    page_html = re.sub(r"\{\{figure:([^}|]+)(?:\|([^}]*))?\}\}",
                       lambda m: figure(m.group(1), m.group(2) or ""), page_html)
    page_html = page_html.replace("{{answers}}", "")
    return page_html


def add_criterion_banners(page_html):
    """Add a Criterion A banner to every section-practice block that lacks one."""
    def fix(m):
        block = m.group(0)
        if "criterion-banner" in block:
            return block
        gid = re.search(r'data-group="([^"]*)"', block)
        if not gid or not (gid.group(1).startswith("p") or gid.group(1) == "guided"):
            return block
        h3 = re.search(r"<h3>(.*?)</h3>", block, re.S)
        if not h3:
            return block
        return block.replace(h3.group(0), banner("A") + h3.group(0), 1)
    return re.sub(r'<div class="exercise-block[^"]*" data-group="[^"]*">.*?</div>\s*</div>',
                  fix, page_html, flags=re.S)


# ------------------------------------------------------------ authored pages
def investigation_page(ch, fw, sec, titles, data):
    inv = next(i for i in fw["investigations"] if i["section"] == sec)
    rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % esc(c) for c in r) for r in inv["rows"])
    table = ('<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>'
             % ("".join("<th>%s</th>" % esc(h) for h in inv["headers"]), rows))
    prompts = "".join("<li>%s</li>" % esc(p) for p in inv["prompts"])
    inner = (
        '<div class="kicker">Chapter %d · Investigation · before %s</div>'
        '<h2>Investigate · %s</h2>'
        '<div class="task"><div class="label">Your task</div><p>%s</p></div>'
        '%s'
        '<div class="prompts"><h3>What do you notice?</h3><ul>%s</ul></div>'
        '<div class="discovery"><strong>Observation.</strong> %s</div>'
        '<div class="conclusion"><div class="label">Mathematical conclusion</div><p>%s</p></div>'
        % (ch, esc(sec), esc(inv["title"]), esc(inv["task"]), table, prompts,
           esc(inv["discovery"]), esc(inv["conclusion"])))
    return make_page(inner, "ch%02d-inv-%s" % (ch, sec.replace(".", "-")), cls="investigate",
                     running_left=PART[ch], running_right="Chapter %d · %s" % (ch, data["title"]))


def criterion_practice_page(ch, fw, letter, data, blocks, page_no, total, note=""):
    inner = ['<div class="kicker">Chapter %d · Practice · Criterion %s</div>'
             % (ch, letter),
             "<h2>%sCriterion %s practice%s</h2>" % ("" if total == 1 else "(%d of %d) " % (page_no, total),
                                                     letter, " · " + note if note else ""),
             banner(letter)]
    inner.extend(blocks)
    return make_page("".join(inner), "ch%02d-crit-%s-%d" % (ch, letter.lower(), page_no),
                     running_left=PART[ch], running_right="Chapter %d · %s" % (ch, data["title"]))


def authored_item_block(ch, items, id_prefix, start, title, letter, tier):
    """Render authored items as an exercise block (answers live in the back matter)."""
    block_items = []
    for n, it in enumerate(items):
        iid = "%d.%s%d" % (ch, id_prefix, start + n)
        block_items.append({"id": iid, "tier": tier, "prompt": it["prompt"]})
        ANSWERS.append((ch, iid, it["answer"], it["reasoning"], title))
    group = {"id": "authored-%s" % id_prefix.lower(), "title": title, "instruction": "", "items": block_items}
    return exercise_block(group, None, None, letter=letter)


def project_page(ch, fw, data):
    p = fw["project"]
    def card(title, pairs):
        dl = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), esc(v)) for k, v in pairs)
        return ('<div class="project-card"><h3>%s</h3><dl>%s</dl></div>' % (esc(title), dl))
    service = card("Service as Action", [
        ("Community need", p["service"]["need"]), ("Mathematical connection", p["service"]["maths"]),
        ("Proposed action", p["service"]["action"]), ("Expected impact", p["service"]["impact"]),
        ("Student reflection", p["service"]["reflection"])])
    community = card("Community Project connection", [
        ("Project idea", p["community"]["idea"]), ("Community need", p["community"]["need"]),
        ("Research question", p["community"]["question"]), ("Mathematics", p["community"]["maths"]),
        ("Action and outcome", p["community"]["outcome"]), ("Beneficiaries", p["community"]["beneficiaries"]),
        ("Evidence", p["community"]["evidence"])])
    personal = card("Personal Project connection · MYP 5", [
        ("Personal interest", p["personal"]["interest"]), ("Learning goal", p["personal"]["goal"]),
        ("Product or outcome", p["personal"]["product"]), ("Mathematics", p["personal"]["maths"]),
        ("Process", p["personal"]["process"]), ("Evidence", p["personal"]["evidence"])])
    inner = (
        '<div class="kicker">Chapter %d · Action and projects</div>'
        '<h2>Project connections</h2>'
        '<p class="lede">Mathematics becomes service and action when it answers a need that other people have. '
        'Each connection below is student-led: choose one, plan it with your teacher and follow your school\u2019s requirements and supervision.</p>'
        '%s%s%s'
        '<p class="project-note">Service as Action is not the same as completing an exercise: it requires action that benefits others and a reflection on that action. '
        'The Community Project connection suits the MYP community project completed by students finishing MYP in Year 3 or Year 4, and the Personal Project connection is an adaptable MYP 5-oriented extension. '
        'They are deliberately different from one another.</p>'
        % (ch, service, community, personal))
    return make_page(inner, "ch%02d-projects" % ch, running_left=PART[ch],
                     running_right="Chapter %d · %s" % (ch, data["title"]))


def review_page(ch, fw, data):
    r = fw["review"]
    checks = "".join("<li>%s</li>" % esc(c) for c in r["checklist"])
    refl = "".join("<li>%s</li>" % esc(c) for c in r["reflection"])
    inner = (
        '<div class="kicker">Chapter %d · Review</div>'
        '<h2>Check your progress</h2>'
        '<p class="lede">Work through the checklist without looking back. Anything you cannot do yet is a target for the mixed practice.</p>'
        '<div class="grid-2"><div class="card"><h3>I can now</h3><ul class="checklist">%s</ul></div>'
        '<div class="card pale"><h3>Reflect</h3><ul>%s</ul></div></div>'
        '<div class="atl"><strong>ATL focus.</strong> %s</div>'
        % (ch, checks, refl, esc(data.get("atl", ""))))
    return make_page(inner, "ch%02d-review" % ch, running_left=PART[ch],
                     running_right="Chapter %d · %s" % (ch, data["title"]))


ANSWERS = []   # (chapter, id, answer, reasoning)


def build_legacy_chapter(ch):
    data, rename = prepare_chapter_data(ch)
    fw = FW[ch]
    titles = section_titles(data)
    by_id = {g["id"]: g for g in data["groups"]}
    pages = []
    b_max = max_id(data, ch, "B")
    d_max = max_id(data, ch, "D")

    seen_sections = set()
    manuscript = manuscript_pages(ch)
    kept = []
    for raw in manuscript:
        kind, sec = classify(raw)
        if kind == "cover":
            pages.append(rewrite_cover(raw, ch, data, fw))
            continue
        if kind in ("explore", "application"):
            continue                      # re-rendered as criterion practice pages
        html = fill_placeholders(raw, data, by_id, rename)
        html = add_criterion_banners(html)
        if kind == "practice" and sec:
            html = relabel_practice(html, sec, titles)
        html = normalise_kicker(html, ch)
        if kind == "teach" and sec and sec not in seen_sections:
            seen_sections.add(sec)
            if any(i["section"] == sec for i in fw.get("investigations", [])):
                pages.append(investigation_page(ch, fw, sec, titles, data))
        pages.append(html)

    # ---- criterion B practice (existing exploration + authored investigation items)
    explore = by_id.get("explore")
    blocks = []
    if explore:
        blocks.append(exercise_block(explore, None, "Investigation practice · %s" % explore["title"],
                                     letter="B"))
    blocks.append(authored_item_block(ch, fw["crit_b"], "B", b_max + 1,
                                      "Investigate further", "B", "investigation"))
    pages.append(criterion_practice_page(ch, fw, "B", data, blocks, 1, 1,
                                         note="investigating patterns"))

    # ---- criterion C practice (authored communication items)
    blocks = [authored_item_block(ch, fw["crit_c"], "C", 1,
                                  "Explain, justify and correct", "C", "reasoning")]
    pages.append(criterion_practice_page(ch, fw, "C", data, blocks, 1, 1,
                                         note="communicating"))

    # ---- criterion D practice (existing application + authored real-context items)
    application = by_id.get("application")
    blocks = []
    if application:
        blocks.append(exercise_block(application, None,
                                     "Application practice · %s" % application["title"], letter="D"))
    blocks.append(authored_item_block(ch, fw["crit_d"], "D", d_max + 1,
                                      "Apply in a new context", "D", "application"))
    pages.append(criterion_practice_page(ch, fw, "D", data, blocks, 1, 1,
                                         note="applying mathematics in real-life contexts"))

    pages.append(review_page(ch, fw, data))
    pages.append(project_page(ch, fw, data))

    # ---- collect answers for the back matter
    for g in data["groups"]:
        for it in g["items"]:
            ANSWERS.append((ch, it["id"], it["answer"], it.get("reasoning", ""), g["title"]))
    return pages


def build_prototype_chapter():
    """Import the approved Chapter 7 prototype, dropping its inline answer pages."""
    src = (PROTO_DIR / "index.html").read_text(encoding="utf-8")
    pages = re.findall(r'<section class="page[^"]*"[^>]*>.*?</section>', src, re.S)
    data = load_chapter(PROTO_CH)
    out = []
    for p in pages:
        pid = re.search(r'data-page-id="([^"]*)"', p)
        pid = pid.group(1) if pid else ""
        if pid.startswith("answers-") or pid.startswith("assessment-answers"):
            continue
        out.append(p)
    # insert the project-connections page before the progress page
    proj = project_page(PROTO_CH, FW[PROTO_CH], data)
    for i, p in enumerate(out):
        pid = re.search(r'data-page-id="([^"]*)"', p)
        if pid and pid.group(1) == "progress":
            out.insert(i, proj)
            break
    # answers for the back matter
    ex = json.loads((PROTO_DIR / "exercises.json").read_text(encoding="utf-8"))
    for it in ex["items"]:
        ANSWERS.append((PROTO_CH, it["id"], it["answer"], it.get("reasoning", ""), it.get("subtopic", "")))
    return out


# ------------------------------------------------------------------ front matter
def front_matter():
    c = FRONT["cover"]
    chips = "".join('<span class="chip">%s</span>' % esc(x) for x in c["chips"])
    cover = make_page(
        '<div><div class="part">%s</div><h1>%s</h1>'
        '<p class="standfirst">%s</p>'
        '<div class="chips">%s</div></div>'
        '<div><div class="inquiry"><div class="label">How this book works</div><p>%s</p></div>'
        '<div class="foot"><span>%s</span><span>%s</span></div></div>'
        % (esc(c["kicker"]), esc(c["title"]), esc(c["subtitle"]), chips, esc(c["inquiry"]),
           esc(c["foot_left"]), esc(c["foot_right"])),
        "book-cover", cls="cover book-cover")

    im = FRONT["imprint"]
    imprint = make_page(
        '<div class="kicker">MYP 1 · Student coursebook</div><h2>%s</h2>%s'
        % (esc(im["title"]), "".join("<p>%s</p>" % esc(p) for p in im["body"])),
        "imprint", running_left="MYP Mathematics 1 · Student coursebook", running_right="About this edition")

    h = FRONT["howto"]
    steps = "".join("<li><strong>%s.</strong> %s</li>" % (esc(k), esc(v)) for k, v in h["steps"])
    crit = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (esc(k), esc(v))
                   for k, v in h["criteria"])
    howto1 = make_page(
        '<div class="kicker">MYP 1 · Student coursebook</div><h2>%s</h2><p class="lede">%s</p>'
        '<h3>The chapter sequence</h3><ol class="steps">%s</ol>' % (esc(h["title"]), esc(h["intro"]), steps),
        "howto-1", running_left="MYP Mathematics 1 · Student coursebook", running_right="How to use this book")
    howto2 = make_page(
        '<div class="kicker">MYP 1 · Student coursebook</div><h2>%s</h2><h3>%s</h3>'
        '<div class="grid-2">%s</div><h3>Working with this book</h3><ul>%s</ul>'
        % (esc(h["title"]), esc(h["criteria_title"]), crit,
           "".join("<li>%s</li>" % esc(n) for n in h["notes"])),
        "howto-2", running_left="MYP Mathematics 1 · Student coursebook", running_right="How to use this book")

    intro = FRONT["intro"]
    proj = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (esc(k), esc(v))
                   for k, v in intro["projects"])
    intro1 = make_page(
        '<div class="kicker">MYP 1 · Student coursebook</div><h2>%s</h2>%s'
        % (esc(intro["title"]), "".join("<p>%s</p>" % esc(p) for p in intro["paras"])),
        "intro-1", running_left="MYP Mathematics 1 · Student coursebook", running_right="Introduction")
    intro2 = make_page(
        '<div class="kicker">MYP 1 · Student coursebook</div><h2>%s</h2><h3>%s</h3>'
        '<div class="grid-2">%s</div><h3>%s</h3><ul>%s</ul>'
        % (esc(intro["title"]), esc(intro["projects_title"]), proj,
           esc(intro["honesty_title"]), "".join("<li>%s</li>" % esc(x) for x in intro["honesty"])),
        "intro-2", running_left="MYP Mathematics 1 · Student coursebook", running_right="Introduction")

    return [cover, imprint, howto1, howto2, intro1, intro2]


def contents_page(chapter_pages):
    """Build the contents page; chapter_pages maps chapter -> 1-based page number."""
    rows = []

    def li(label, page, sub=False, num=""):
        return ('<li class="%s"><span class="num">%s</span><span class="t">%s</span>'
                '<span class="dots"></span><span class="p">%d</span></li>'
                % ("sub" if sub else "", esc(num), esc(label), page))

    rows.append(li("How to use this book", 3, num="\u2014"))
    rows.append(li("MYP mathematics and this coursebook", 5, num="\u2014"))
    rows.append(li("Answers and reasoning", chapter_pages["answers"], num="\u2014"))
    rows.append(li("Formula bank", chapter_pages["formula"], num="\u2014"))
    rows.append(li("Glossary", chapter_pages["glossary"], num="\u2014"))
    rows.append(li("References and acknowledgements", chapter_pages["references"], num="\u2014"))
    current_part = None
    for ch in CHAPTERS:
        part = PART[ch]
        if part != current_part:
            rows.append('<li class="part-head">%s</li>' % esc(part))
            current_part = part
        data = load_chapter(ch)
        rows.append(li("%d. %s" % (ch, data["title"]), chapter_pages[ch], num="%02d" % ch))
    body = ('<div class="kicker">MYP 1 · Student coursebook</div><h2>Contents</h2>'
            '<div class="toc"><ol>%s</ol></div>'
            '<p class="small muted" style="margin-top:5mm">Every chapter follows the same sequence: '
            'engagement, inquiry questions, investigation, observation, mathematical conclusion, formal '
            'development, worked examples, Criterion A\u2013D practice, application, assessment and reflection, '
            'and project connections.</p>' % "".join(rows))
    return make_page(body, "contents", running_left="MYP Mathematics 1 · Student coursebook",
                     running_right="Contents")


# ------------------------------------------------------------------- back matter
def answers_pages(answers):
    """Global answers, grouped by chapter, with chapter and group headings."""
    per_page = 12
    pages = []
    chunks = []
    current_ch, current_group, used = None, None, 0
    for entry in answers:
        ch, iid, ans, why, group = entry
        if ch != current_ch or used >= per_page:
            chunks.append([])
            current_ch, current_group, used = ch, None, 0
        if group != current_group:
            current_group = group
        chunks[-1].append(entry)
        used += 1
    previous_ch = None
    for n, chunk in enumerate(chunks, start=1):
        items = []
        last_group = None
        for ch, iid, ans, why, group in chunk:
            if group != last_group:
                items.append('<h4 class="answer-group-title">%s</h4>' % esc(group))
                last_group = group
            items.append('<div class="answer-item" data-answer-for="%s"><span class="aid">%s</span>'
                         '<div><div class="answer-text">%s</div><div class="reasoning">%s</div></div></div>'
                         % (esc(iid), esc(iid), safe(ans), safe(why)))
        ch = chunk[0][0]
        title = load_chapter(ch)["title"]
        heading = "Chapter %d · %s" % (ch, title)
        if previous_ch == ch:
            heading += " (continued)"
        previous_ch = ch
        body = ('<div class="kicker">Answers and reasoning</div><h2>%s</h2>%s'
                % (esc(heading), "".join(items)))
        pages.append(make_page(body, "answers-%d" % n, cls="answer-section",
                               running_left="MYP Mathematics 1 · Student coursebook",
                               running_right="Answers and reasoning"))
    return pages


def formula_pages():
    pages = []
    groups = []
    for ch in CHAPTERS:
        facts = FW[ch].get("facts", [])
        if not facts:
            continue
        data = load_chapter(ch)
        dl = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), esc(v)) for k, v in facts)
        groups.append('<div class="fb-group"><h3>Chapter %d · %s</h3><dl>%s</dl></div>'
                      % (ch, esc(data["title"]), dl))
    per_page = 2
    chunks = [groups[i:i + per_page] for i in range(0, len(groups), per_page)]
    for n, chunk in enumerate(chunks, start=1):
        body = ('<div class="kicker">Formula bank</div><h2>Formula bank (%d of %d)</h2>'
                '<p class="small muted">Key facts and formulas, chapter by chapter. Use them to check work, '
                'not to replace reasoning.</p>%s' % (n, len(chunks), "".join(chunk)))
        pages.append(make_page(body, "formula-%d" % n, cls="formula-bank",
                               running_left="MYP Mathematics 1 · Student coursebook",
                               running_right="Formula bank"))
    return pages


def glossary_pages():
    entries = sorted(GLOSSARY, key=lambda e: e[0].lower())
    per_page = 26
    chunks = [entries[i:i + per_page] for i in range(0, len(entries), per_page)]
    pages = []
    for n, chunk in enumerate(chunks, start=1):
        dl = "".join('<dt>%s <span class="ch">(ch. %d)</span></dt><dd>%s</dd>'
                     % (esc(t), ch, esc(d)) for t, d, ch in chunk)
        body = ('<div class="kicker">Glossary</div><h2>Glossary (%d of %d)</h2>'
                '<div class="glossary"><dl>%s</dl></div>' % (n, len(chunks), dl))
        pages.append(make_page(body, "glossary-%d" % n, running_left="MYP Mathematics 1 · Student coursebook",
                               running_right="Glossary"))
    return pages


def reference_pages():
    body = ['<div class="kicker">References</div><h2>References and acknowledgements</h2>']
    for title, items in REFERENCES:
        body.append("<h3>%s</h3><ul>" % esc(title))
        for it in items:
            it = re.sub(r"(https?://[^\s]+)",
                        r'<span class="url">\1</span>', esc(it))
            body.append("<li>%s</li>" % it)
        body.append("</ul>")
    body.append('<p class="small muted">Access date for official IB pages: 2 November 2026. '
                'Official programme requirements are distinguished from author-designed material throughout '
                'this book. No commercial print-readiness claim is made.</p>')
    return [make_page("".join(body), "references",
                      running_left="MYP Mathematics 1 · Student coursebook",
                      running_right="References and acknowledgements")]


# ------------------------------------------------------- glyph-safe symbols
# Source Serif 4 and Inter lack several mathematical symbols, which would print
# as empty boxes. They are converted to KaTeX so that every symbol is drawn by a
# font that contains it. Diagrams (<svg>) and hidden KaTeX MathML are protected.
PROTECTED = re.compile(
    r"(<svg.*?</svg>|<span class=\"katex-mathml\">.*?</span>|\salt=\"[^\"]*\"|\stitle=\"[^\"]*\")",
    re.S)
SYMBOL_MATH = {
    "\u2282": "[[math:\\subset]]", "\u2286": "[[math:\\subseteq]]",
    "\u222a": "[[math:\\cup]]", "\u2229": "[[math:\\cap]]",
    "\u2208": "[[math:\\in]]", "\u2205": "[[math:\\emptyset]]",
    "\u2218": "[[math:\\circ]]", "\u2260": "[[math:\\neq]]",
    "\u2192": "[[math:\\rightarrow]]", "\u2032": "[[math:\\prime]]",
}


def symbols_to_math(html):
    parts = PROTECTED.split(html)
    for i in range(0, len(parts), 2):
        seg = parts[i]
        for old, new in SYMBOL_MATH.items():
            seg = seg.replace(old, new)
        seg = re.sub(r"\u221b(\{[^}]*\}|\S+)", r"[[math:\\sqrt[3]{\1}]]", seg)
        parts[i] = seg
    return "".join(parts)


# ------------------------------------------------------------------------ main
def main():
    pages = front_matter()
    toc_index = len(pages)
    pages.append(None)                       # placeholder for the contents page

    chapter_start = {}
    for ch in CHAPTERS:
        chapter_start[ch] = len(pages) + 1   # 1-based page number of the chapter cover
        if ch == PROTO_CH:
            pages.extend(build_prototype_chapter())
        else:
            pages.extend(build_legacy_chapter(ch))

    marks = {"answers": len(pages) + 1}
    ans = answers_pages(ANSWERS)
    pages.extend(ans)
    marks["formula"] = len(pages) + 1
    pages.extend(formula_pages())
    marks["glossary"] = len(pages) + 1
    pages.extend(glossary_pages())
    marks["references"] = len(pages) + 1
    pages.extend(reference_pages())

    pages[toc_index] = contents_page({**chapter_start, **marks})

    # give every page a stable data-page-id for QA
    for i, pg in enumerate(pages, start=1):
        if 'data-page-id="' not in pg[:220]:
            pg = re.sub(r'(<section class="page[^"]*")>',
                        r'\1 data-page-id="book-p%03d">' % i, pg, count=1)
            pages[i - 1] = pg

    html = ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/>"
            "<title>MYP 1 Mathematics · Student coursebook · Second edition</title>"
            "<link rel=\"stylesheet\" href=\"/styles/book.css\"/>"
            "<link rel=\"stylesheet\" href=\"/vendor/katex/katex.css\"/>"
            "</head><body>%s</body></html>" % "".join(pages))
    html = symbols_to_math(html)
    (HERE / "book.html").write_text(html, encoding="utf-8")

    manifest = {
        "pages": len(pages),
        "chapters": {str(ch): chapter_start[ch] for ch in CHAPTERS},
        "back_matter": marks,
        "items": len(ANSWERS),
        "answer_pages": len(ans),
    }
    (HERE / "book.manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
