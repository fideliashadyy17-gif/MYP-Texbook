#!/usr/bin/env python3
"""Assemble the complete MYP 2 second-edition coursebook into one HTML file.

The whole volume is authored from structured content in ``framework.py`` and
drawn with the diagram library ``diagrams2.py``; there are no legacy manuscripts
to parse, so every page is generated here and the printed page number equals the
position of the page in the document.

Page model (mirrors the approved MYP 1 volume):

    front matter            cover, imprint, how-to, introduction, contents
    per chapter             opener, investigation, teaching, criterion practice,
                            application/assessment, review, projects
    back matter             answers, formula bank, glossary, references, back cover
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent                       # sources/myp2
EDITION = HERE.parents[2]                # second-edition
sys.path.insert(0, str(HERE))
from framework import (AUTHOR, CHAPTERS, COLLECTION, CRITERIA, FORMULAS, FRONT,  # noqa: E402
                       GLOSSARY, PARTS, REFERENCES, SERIES)
import diagrams2  # noqa: E402
import covers  # noqa: E402

LEVEL = 2
RUNNING = "MYP Mathematics 2 · Student coursebook"
ANSWERS = []          # (chapter, qid, question, answer, reasoning, criterion)
TIER_LABEL = {"F": "Fluency", "A": "Application", "R": "Reasoning", "C": "Challenge"}


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def make_page(inner, page_id, cls="", running_left="", running_right=""):
    rh = ""
    if running_left or running_right:
        rh = ('<div class="running-head"><span>%s</span><span>%s</span></div>'
              % (esc(running_left), esc(running_right)))
    return ('<section class="page %s" data-page-id="%s">%s%s</section>'
            % (cls, esc(page_id), rh, inner))


def figure(svg, caption=""):
    if not svg:
        return ""
    cap = '<figcaption>%s</figcaption>' % esc(caption) if caption else ""
    return '<figure>%s%s</figure>' % (svg, cap)


def visual(svg, caption=""):
    """An inline visual inside a practice item or example."""
    if not svg:
        return ""
    cap = '<span class="cap">%s</span>' % esc(caption) if caption else ""
    return '<div class="visual">%s%s</div>' % (svg, cap)


def banner(letter):
    name, _ = CRITERIA[letter]
    return ('<div class="criterion-banner %s"><span class="k">Criterion %s</span>'
            '<span class="v">%s</span></div>' % (letter.lower(), letter, esc(name)))


def example(ex, index):
    """A worked example with the six required parts."""
    parts = ['<div class="example"><div class="example-title">Worked example %s</div>'
             '<p class="prompt"><strong>Problem.</strong> %s</p>' % (index, esc(ex["q"]))]
    if ex.get("vis"):
        parts.append(visual(ex["vis"], ex.get("vis_cap", "")))
    if ex.get("reasoning"):
        parts.append('<p><strong>Mathematical reasoning.</strong> %s</p>' % esc(ex["reasoning"]))
    parts.append('<ol class="steps">%s</ol>'
                 % "".join("<li>%s</li>" % esc(s) for s in ex["steps"]))
    parts.append('<p class="answer"><strong>Final answer.</strong> %s</p>' % esc(ex["ans"]))
    parts.append('<p class="interpretation"><strong>Interpretation.</strong> %s</p>'
                 % esc(ex["interp"]))
    parts.append("</div>")
    return "".join(parts)


# ------------------------------------------------------------------ chapter pages
def chapter_opener(ch):
    qs = "".join('<li><strong>%s:</strong> %s</li>' % (esc(k), esc(v)) for k, v in ch["questions"])
    related = " · ".join(ch["related"])
    expl = ('<br/><strong>Global context exploration:</strong> %s' % esc(ch["exploration"]) \
            if ch.get("exploration") else "")
    body = (
        '<div class="kicker">Chapter %d · %s</div>'
        '<div class="chapter-number">%02d</div>'
        '<h1>%s</h1>'
        '<p class="standfirst">%s</p>'
        '<div class="callout"><div class="label">Engage</div><p>%s</p></div>'
        '<div class="review-grid">'
        '<div class="card"><h3>Framing the inquiry</h3>'
        '<p><strong>Key concept:</strong> %s<br/><strong>Related concepts:</strong> %s<br/>'
        '<strong>Global context:</strong> %s%s</p>'
        '<p><strong>Statement of inquiry:</strong> %s</p></div>'
        '<div class="card"><h3>Questions to guide us</h3><ul>%s</ul></div>'
        '</div>'
        '<div class="atl"><strong>ATL · %s.</strong> %s</div>'
        % (ch["num"], esc(PARTS[ch["num"]]), ch["num"], esc(ch["title"]), esc(ch["standfirst"]),
           esc(ch["engage"]), esc(ch["key"]), esc(related), esc(ch["context"]), expl,
           esc(ch["inquiry"]), qs, esc(ch["atl"][0]), esc(ch["atl"][1])))
    return make_page(body, "ch%02d-cover" % ch["num"], cls="opener",
                     running_left=RUNNING, running_right="Chapter %d · %s" % (ch["num"], ch["title"]))


def investigation_pages(ch, sec):
    """Two pages: the investigation itself, then observation and conclusion."""
    inv = sec["inv"]
    visuals = ""
    if inv.get("fig"):
        visuals += figure(inv["fig"], inv.get("fig_cap", ""))
    if inv.get("table"):
        visuals += figure(diagrams2.table(inv["table"]), inv.get("table_cap", ""))
    qblock = ('<div class="callout"><div class="label">Inquiry question</div><p>%s</p></div>'
              % esc(sec["inquiry_q"])) if sec.get("inquiry_q") else ""
    task = ('<div class="kicker">Chapter %d · Investigation %s</div><h2>%s</h2>'
            '<div class="investigate">%s'
            '<div class="task"><div class="label">Your task</div><p>%s</p>%s</div>'
            '</div>'
            % (ch["num"], esc(sec["id"]), esc(sec["title"]), qblock,
               esc(inv["task"]), visuals))
    prompts = "".join("<li>%s</li>" % esc(p) for p in inv.get("notice", []))
    discovery = ('<div class="kicker">Chapter %d · Investigation %s</div><h2>%s</h2>'
                 '<div class="investigate">'
                 '<div class="prompts"><strong>What do you notice?</strong><ul>%s</ul></div>'
                 '<div class="discovery"><strong>Observation.</strong> %s</div>'
                 '<div class="conclusion"><div class="label">Mathematical conclusion</div>'
                 '<p>%s</p></div>'
                 '<div class="prompts"><strong>Your own words</strong>'
                 '<div class="construction-space"></div></div>'
                 '</div>'
                 % (ch["num"], esc(sec["id"]), esc(sec["title"]), prompts,
                    esc(inv["obs"]), esc(inv["concl"])))
    return [make_page(task, "ch%02d-inv-%s" % (ch["num"], sec["id"].replace(".", "-")),
                      running_left=RUNNING, running_right="Investigation %s" % sec["id"]),
            make_page(discovery, "ch%02d-inv-%s-notes" % (ch["num"], sec["id"].replace(".", "-")),
                      running_left=RUNNING, running_right="Investigation %s" % sec["id"])]


def teaching_page(ch, sec):
    """The formal development of a section: teaching text, no worked examples."""
    body = ('<div class="kicker">Chapter %d · %s</div><h2>%s</h2>%s'
            '<div class="callout"><div class="label">Formal development</div><p>%s</p></div>'
            '<div class="prompts"><strong>In your own words</strong>'
            '<div class="construction-space"></div></div>'
            % (ch["num"], esc(sec["id"]), esc(sec["title"]),
               "".join("<p>%s</p>" % esc(p) for p in sec["teach"]),
               esc("Work through the investigation above before reading this page: the statements "
                   "here are the formal version of what you discovered.")))
    return make_page(body, "ch%02d-theory-%s" % (ch["num"], sec["id"].replace(".", "-")),
                     running_left=RUNNING, running_right="%s · %s" % (sec["id"], sec["title"]))


def example_page(ch, sec, ex, index):
    """One worked example per page, with all six required parts."""
    body = ('<div class="kicker">Chapter %d · %s · Worked example %s</div><h2>%s</h2>%s'
            % (ch["num"], esc(sec["id"]), index, esc(sec["title"]),
               example(ex, "%s.%s" % (sec["id"], index))))
    return make_page(body, "ch%02d-example-%s-%s" % (ch["num"], sec["id"].replace(".", "-"), index),
                     running_left=RUNNING, running_right="%s · Worked example %s"
                     % (sec["id"], index))


def practice_pages(ch):
    """One page per criterion group of six items."""
    pages = []
    for letter in ("A", "B", "C", "D"):
        items = ch["practice"].get(letter, [])
        for start in range(0, len(items), 6):
            group = items[start:start + 6]
            rows = []
            for j, it in enumerate(group):
                qid = "%d.%s%d" % (ch["num"], letter, start + j + 1)
                q, ans, why, tier = it[1], it[2], it[3], it[4]
                vis = it[5] if len(it) > 5 else ""
                ANSWERS.append((ch["num"], qid, q, ans, why, letter))
                rows.append(
                    '<div class="item" id="q-%s"><div class="id">%s'
                    '<span class="tier">%s</span></div>'
                    '<div class="prompt">%s%s<div class="workline"></div>'
                    '<div class="workline"></div></div></div>'
                    % (esc(qid), esc(qid), esc(TIER_LABEL.get(tier, tier)), esc(q), visual(vis)))
            head = banner(letter)
            if start == 0:
                head += ('<h3>Criterion %s practice · %s</h3>'
                         % (letter, esc(CRITERIA[letter][0])))
            else:
                head += '<h3>Criterion %s practice · %s (continued)</h3>' % (
                    letter, esc(CRITERIA[letter][0]))
            pages.append(make_page(head + "".join(rows),
                                   "ch%02d-crit-%s-%d" % (ch["num"], letter.lower(), start // 6 + 1),
                                   running_left=RUNNING,
                                   running_right="Criterion %s practice" % letter))
    return pages


def assessment_page(ch):
    tasks = []
    for t in ch["assessment"]:
        tasks.append(
            '<div class="assessment-task"><h3>%s</h3>%s<p>%s</p>%s</div>'
            % (esc(t["title"]), figure(t.get("fig"), t.get("fig_cap", "")), esc(t["text"]),
               '<p class="footer-note">%s</p>' % esc(t["note"]) if t.get("note") else ""))
    body = ('<div class="kicker">Chapter %d · Application and assessment</div>'
            '<h2>Applying chapter %d</h2><p class="lede">%s</p>%s'
            % (ch["num"], ch["num"], esc(ch["application_lede"]), "".join(tasks)))
    return make_page(body, "ch%02d-assessment" % ch["num"], running_left=RUNNING,
                     running_right="Application and assessment")


def review_pages(ch):
    """Two review pages: key ideas and vocabulary, then mixed practice."""
    ideas = "".join("<li>%s</li>" % esc(i) for i in ch["review"]["ideas"])
    vocab = " · ".join(ch["review"]["vocab"])
    summary = ('<div class="kicker">Chapter %d · Review</div>'
               '<h2>What you should now be able to do</h2>'
               '<div class="review-grid"><div class="card"><h3>Key ideas</h3><ul>%s</ul></div>'
               '<div class="card"><h3>Vocabulary</h3><p>%s</p></div></div>'
               % (ch["num"], ideas, esc(vocab)))
    mixed = ch["review"].get("mixed", [])
    rows = "".join('<div class="item"><div class="id">%s</div><div class="prompt">%s'
                   '<div class="workline"></div><div class="workline"></div></div></div>'
                   % (esc(m[0]), esc(m[1])) for m in mixed)
    practice = ('<div class="kicker">Chapter %d · Review</div>'
                '<h2>Mixed practice · consolidate and extend</h2>'
                '<p class="small muted">%s</p>%s'
                % (ch["num"], esc(ch["review"].get("mixed_note",
                   "Do not use a calculator unless a question asks for one. "
                   "Show a method where one is requested.")), rows))
    refl = ch.get("reflection") or []
    refl_rows = "".join("<li>%s</li>" % esc(r) for r in refl)
    reflection = ('<div class="assessment-task"><h3>Returning to the statement of inquiry</h3>'
                  '<p class="small muted">%s</p><ul>%s</ul>'
                  '<div class="construction-space"></div></div>'
                  % (esc("Answer in your own words, using evidence from this chapter."),
                     refl_rows))
    return [make_page(summary + reflection, "ch%02d-review" % ch["num"], running_left=RUNNING,
                      running_right="Chapter review"),
            make_page(practice, "ch%02d-review-mixed" % ch["num"], running_left=RUNNING,
                      running_right="Chapter review")]


def projects_page(ch):
    def card(title, rows):
        dl = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), esc(v)) for k, v in rows)
        return ('<div class="project-card"><h3>%s</h3><dl>%s</dl></div>' % (esc(title), dl))

    body = ('<div class="kicker">Chapter %d · Projects, service and action</div>'
            '<h2>Acting on what you have learned</h2>'
            '<p class="lede">%s</p>%s'
            % (ch["num"], esc(ch["projects_lede"]),
               card("Service as Action", ch["projects"]["service"])
               + card("Community Project", ch["projects"]["community"])
               + card("Personal Project connection · MYP 5", ch["projects"]["personal"])))
    return make_page(body, "ch%02d-projects" % ch["num"], running_left=RUNNING,
                     running_right="Projects and service")


def build_chapter(ch):
    pages = [chapter_opener(ch)]
    for sec in ch["sections"]:
        pages.extend(investigation_pages(ch, sec))
        pages.append(teaching_page(ch, sec))
        for i, ex in enumerate(sec.get("examples", []), start=1):
            pages.append(example_page(ch, sec, ex, "%d" % i))
    pages.extend(practice_pages(ch))
    pages.append(assessment_page(ch))
    pages.extend(review_pages(ch))
    pages.append(projects_page(ch))
    return pages


# ------------------------------------------------------------------- back matter
def answers_pages():
    pages = []
    by_ch = {}
    for row in ANSWERS:
        by_ch.setdefault(row[0], []).append(row)
    chunk = []
    count = 0

    def flush():
        nonlocal chunk, count
        if not chunk:
            return
        rows = []
        for chnum, qid, q, ans, why, letter in chunk:
            if chnum is None:                      # a criterion group title row
                rows.append(qid)
                continue
            rows.append('<div class="answer-item" data-answer-for="%s"><span class="aid">%s</span>'
                        '<div><div class="answer-text">%s</div>'
                        '<div class="reasoning">%s</div></div></div>'
                        % (esc(qid), esc(qid), esc(ans), esc(why)))
        pages.append(make_page('<div class="answer-section">%s</div>' % "".join(rows),
                               "answers-%d" % (len(pages) + 1), cls="answer-section",
                               running_left=RUNNING, running_right="Answers and reasoning"))
        chunk, count = [], 0

    current = None
    for chnum in sorted(by_ch):
        for letter in ("A", "B", "C", "D"):
            group = [r for r in by_ch[chnum] if r[5] == letter]
            if not group:
                continue
            head = ('<div class="answer-group-title">Chapter %d · Criterion %s · %s</div>'
                    % (chnum, letter, esc(CRITERIA[letter][0])))
            if count + len(group) > 14:
                flush()
            chunk.append((None, head, None, None, None, None))
            chunk.extend(group)
            count += len(group) + 1
    flush()
    return pages


def formula_pages():
    groups = []
    for title, items in FORMULAS:
        dl = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), esc(v)) for k, v in items)
        groups.append('<div class="fb-group"><h3>%s</h3><dl>%s</dl></div>' % (esc(title), dl))
    pages = []
    for i, grp in enumerate(groups, start=1):
        pages.append(make_page('<div class="formula-bank"><h2>Formula bank (%d of %d)</h2>'
                               '<p class="small muted">Key facts and formulas, chapter by chapter. '
                               'Use them to check work, not to replace reasoning.</p>%s</div>'
                               % (i, len(groups), grp),
                               "formula-%d" % i, running_left=RUNNING,
                               running_right="Formula bank"))
    return pages


def glossary_pages():
    terms = sorted(GLOSSARY, key=lambda t: t[0].lower())
    pages = []
    per = 24
    for i in range(0, len(terms), per):
        chunk = terms[i:i + per]
        dl = "".join('<dt>%s <span class="ch">ch. %s</span></dt><dd>%s</dd>'
                     % (esc(t), esc(t[2]), esc(t[1])) for t in chunk)
        pages.append(make_page('<div class="glossary"><h2>Glossary (%d of %d)</h2><dl>%s</dl></div>'
                               % (i // per + 1, (len(terms) + per - 1) // per, dl),
                               "glossary-%d" % (i // per + 1), running_left=RUNNING,
                               running_right="Glossary"))
    return pages


def reference_pages():
    body = ['<div class="kicker">References</div><h2>References and acknowledgements</h2>']
    for title, items in REFERENCES:
        body.append("<h3>%s</h3><ul>" % esc(title))
        for it in items:
            it = re.sub(r"(https?://[^\s]+)", r'<span class="url">\1</span>', esc(it))
            body.append("<li>%s</li>" % it)
        body.append("</ul>")
    body.append('<p class="small muted">Access date for official IB pages: 2 November 2026. '
                'Official programme requirements are distinguished from author-designed material '
                'throughout this book. No commercial print-readiness claim is made.</p>')
    return [make_page("".join(body), "references", running_left=RUNNING,
                      running_right="References and acknowledgements")]


# -------------------------------------------------------------------- front matter
def front_matter():
    c = FRONT["cover"]
    cover = covers.front_cover_page()

    im = FRONT["imprint"]
    imprint = make_page(
        '<div class="kicker">MYP 2 · Student coursebook</div>'
        '<div class="credit"><div class="credit-label">%s</div>'
        '<div class="credit-name">%s</div></div><h2>%s</h2>%s'
        % (esc(im["credit"]), esc(im["author"]), esc(im["title"]),
           "".join("<p>%s</p>" % esc(p) for p in im["body"])),
        "imprint", running_left=RUNNING, running_right="About this edition")

    h = FRONT["howto"]
    steps = "".join("<li><strong>%s.</strong> %s</li>" % (esc(k), esc(v)) for k, v in h["steps"])
    crit = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (esc(k), esc(v))
                   for k, v in h["criteria"])
    howto1 = make_page(
        '<div class="kicker">MYP 2 · Student coursebook</div><h2>%s</h2><p class="lede">%s</p>'
        '<h3>The chapter sequence</h3><ol class="steps">%s</ol>'
        % (esc(h["title"]), esc(h["intro"]), steps),
        "howto-1", running_left=RUNNING, running_right="How to use this book")
    howto2 = make_page(
        '<div class="kicker">MYP 2 · Student coursebook</div><h2>%s</h2><h3>%s</h3>'
        '<div class="grid-2">%s</div><h3>Working with this book</h3><ul>%s</ul>'
        % (esc(h["title"]), esc(h["criteria_title"]), crit,
           "".join("<li>%s</li>" % esc(n) for n in h["notes"])),
        "howto-2", running_left=RUNNING, running_right="How to use this book")

    intro = FRONT["intro"]
    proj = "".join('<div class="card"><h3>%s</h3><p>%s</p></div>' % (esc(k), esc(v))
                   for k, v in intro["projects"])
    intro1 = make_page(
        '<div class="kicker">MYP 2 · Student coursebook</div><h2>%s</h2>%s'
        % (esc(intro["title"]), "".join("<p>%s</p>" % esc(p) for p in intro["paras"])),
        "intro-1", running_left=RUNNING, running_right="Introduction")
    intro2 = make_page(
        '<div class="kicker">MYP 2 · Student coursebook</div><h2>%s</h2><h3>%s</h3>'
        '<div class="grid-2">%s</div><h3>%s</h3><ul>%s</ul>'
        % (esc(intro["title"]), esc(intro["projects_title"]), proj,
           esc(intro["honesty_title"]), "".join("<li>%s</li>" % esc(x) for x in intro["honesty"])),
        "intro-2", running_left=RUNNING, running_right="Introduction")
    return [cover, imprint, howto1, howto2, intro1, intro2]


def contents_rows(chapter_start, marks):
    rows = []

    def li(label, page, num=""):
        return ('<li><span class="num">%s</span><span class="t">%s</span>'
                '<span class="dots"></span><span class="p">%d</span></li>'
                % (esc(num), esc(label), page))

    rows.append(li("How to use this book", 3))
    rows.append(li("MYP mathematics and this coursebook", 5))
    rows.append(li("Answers and reasoning", marks["answers"]))
    rows.append(li("Formula bank", marks["formula"]))
    rows.append(li("Glossary", marks["glossary"]))
    rows.append(li("References and acknowledgements", marks["references"]))
    current = None
    for ch in CHAPTERS:
        part = PARTS[ch["num"]]
        if part != current:
            rows.append('<li class="part-head">%s</li>' % esc(part))
            current = part
        rows.append(li("%d. %s" % (ch["num"], ch["title"]), chapter_start[ch["num"]],
                       num="%02d" % ch["num"]))
        for sec in ch["sections"]:
            rows.append('<li class="sub"><span class="num"></span><span class="t">%s %s</span>'
                        '<span class="dots"></span><span class="p"></span></li>'
                        % (esc(sec["id"]), esc(sec["title"])))
        rows.append('<li class="sub"><span class="num"></span><span class="t">'
                    'Application and assessment · Review · Projects and service</span>'
                    '<span class="dots"></span><span class="p"></span></li>')
    return rows


CONTENTS_PER_PAGE = 22


def contents_pages(rows):
    note = ('<p class="small muted" style="margin-top:4mm">Every chapter follows the same sequence: '
            'engagement, inquiry questions, investigation, observation, mathematical conclusion, '
            'formal development, worked examples, Criterion A\u2013D practice, application, '
            'assessment and reflection, and project connections.</p>')
    chunks = [rows[i:i + CONTENTS_PER_PAGE] for i in range(0, len(rows), CONTENTS_PER_PAGE)] or [[]]
    out = []
    for n, chunk in enumerate(chunks):
        last = (n == len(chunks) - 1)
        body = ('<div class="kicker">MYP 2 · Student coursebook</div><h2>Contents%s</h2>'
                '<div class="toc"><ol>%s</ol></div>%s'
                % (" (continued)" if n else "", "".join(chunk), note if last else ""))
        out.append(make_page(body, "contents-%d" % (n + 1), running_left=RUNNING,
                             running_right="Contents"))
    return out


# ------------------------------------------------------------------------- symbols
PROTECTED = re.compile(
    r"(<svg.*?</svg>|<span class=\"katex-mathml\">.*?</span>|\salt=\"[^\"]*\"|\stitle=\"[^\"]*\")",
    re.S)
SYMBOL_MATH = {
    "\u2282": "[[math:\\subset]]", "\u2286": "[[math:\\subseteq]]",
    "\u222a": "[[math:\\cup]]", "\u2229": "[[math:\\cap]]",
    "\u2208": "[[math:\\in]]", "\u2205": "[[math:\\emptyset]]",
    "\u2218": "[[math:\\circ]]", "\u2260": "[[math:\\neq]]",
    "\u2192": "[[math:\\rightarrow]]", "\u2032": "[[math:\\prime]]",
    "\u221b": "[[math:\\sqrt[3]{%s}]]",
}


def symbols_to_math(html):
    """Route symbols the text font lacks through KaTeX."""
    parts = PROTECTED.split(html)
    for i, part in enumerate(parts):
        if PROTECTED.fullmatch(part):
            continue
        for sym, repl in SYMBOL_MATH.items():
            if "%s" in repl:
                def sub(m, _r=repl):
                    return _r % m.group(1)
                part = re.sub(sym + r"([0-9A-Za-z]+)", sub, part)
            else:
                part = part.replace(sym, repl)
        parts[i] = part
    return "".join(parts)


def main():
    pages = front_matter()
    toc_index = len(pages)
    # the contents list is generated after pagination is known, so reserve the right
    # number of slots first: the row count does not depend on the page numbers
    n_toc = max(1, -(-len(contents_rows({ch["num"]: 0 for ch in CHAPTERS},
                                       {k: 0 for k in ("answers", "formula", "glossary",
                                                       "references")})) // CONTENTS_PER_PAGE))
    toc_index = len(pages)
    pages.extend([None] * n_toc)

    chapter_start = {}
    for ch in CHAPTERS:
        chapter_start[ch["num"]] = len(pages) + 1
        pages.extend(build_chapter(ch))

    marks = {"answers": len(pages) + 1}
    pages.extend(answers_pages())
    marks["formula"] = len(pages) + 1
    pages.extend(formula_pages())
    marks["glossary"] = len(pages) + 1
    pages.extend(glossary_pages())
    marks["references"] = len(pages) + 1
    pages.extend(reference_pages())
    marks["back_cover"] = len(pages) + 1
    pages.append(covers.back_cover_page())

    pages[toc_index:toc_index + n_toc] = contents_pages(
        contents_rows(chapter_start, marks))

    for i, pg in enumerate(pages, start=1):
        if 'data-page-id="' not in pg[:240]:
            pg = re.sub(r'(<section class="page[^"]*")>',
                        r'\1 data-page-id="book-p%03d">' % i, pg, count=1)
            pages[i - 1] = pg

    html = ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/>"
            "<title>MYP 2 Mathematics · Student coursebook · Second edition</title>"
            "<link rel=\"stylesheet\" href=\"/styles/book.css\"/>"
            "<link rel=\"stylesheet\" href=\"/vendor/katex/katex.css\"/>"
            "</head><body>%s</body></html>" % "".join(pages))
    html = symbols_to_math(html)
    (HERE / "book.html").write_text(html, encoding="utf-8")

    manifest = {
        "pages": len(pages),
        "level": LEVEL,
        "chapters": {str(k): v for k, v in chapter_start.items()},
        "back_matter": marks,
        "items": len(ANSWERS),
        "answer_pages": len([p for p in pages if "answer-section" in p]),
    }
    (HERE / "book.manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
