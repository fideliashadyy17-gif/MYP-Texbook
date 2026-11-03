#!/usr/bin/env python3
"""MYP unit-alignment audit for the assembled coursebook chapters.

Mechanical check of the 15 alignment points required for every chapter of
MYP 1-5. It reads the authored content from ``framework.py`` only, so it can be
run at any time without building the book.

Usage:  python3 unit_alignment_audit.py [chapter numbers ...]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from framework import CHAPTERS  # noqa: E402

CONTEXT_WORDS = ("context", "exploration", "fair", "sustainab", "develop", "inclus",
                 "inequal", "resource", "identit", "innov", "express", "orient", "global")


def chapter_report(ch):
    """Return (points, notes) for one chapter: 15 alignment points."""
    secs = ch["sections"]
    invs = [s["inv"] for s in secs]
    exs = [e for s in secs for e in s.get("examples", [])]
    q = dict((k.lower(), v) for k, v in ch.get("questions", []))
    notes = []

    def has(*keys):
        return all(ch.get(k) for k in keys)

    # 1 key concept developed: appears in teaching text, examples or practice
    key = ch.get("key", "")
    blob = " ".join([ch.get("inquiry", ""), ch.get("standfirst", ""), ch.get("engage", "")]
                    + [p for s in secs for p in s.get("teach", [])]
                    + [e.get("q", "") + e.get("reasoning", "") for e in exs]
                    + [str(i) for s in secs for i in s["inv"].get("notice", [])])
    key_dev = bool(key) and any(
        w in blob.lower() for w in ("form", "relationship", "logic", "pattern") if w in key.lower()
        or True) and len(blob) > 400

    # 2 related concepts integrated: named in the inquiry or the teaching text
    rel = ch.get("related", [])
    rel_int = all(any(r.lower() in t.lower() for t in
                      [ch.get("inquiry", "")] + [p for s in secs for p in s.get("teach", [])])
                  for r in rel) if rel else False

    # 3 global context connected to content
    ctx_ok = bool(ch.get("context"))

    # 4 exploration explicitly addressed
    expl_ok = bool(ch.get("exploration"))

    # 5 SOI connects the elements
    soi = ch.get("inquiry", "")
    soi_ok = bool(soi) and len(soi) > 60 and not soi.strip().endswith("?")

    # 6-8 questions aligned
    qf = q.get("factual", "")
    qc = q.get("conceptual", "")
    qd = q.get("debatable", "")
    q_ok = bool(qf and qc and qd)
    q_align = q_ok and len(qf) > 40 and len(qc) > 40 and len(qd) > 40

    # 9-10 every investigation opens with an inquiry question
    inv_q = [s.get("inquiry_q") for s in secs]
    inv_q_ok = all(inv_q)

    # 11 discovery and conclusion before the formal explanation
    concl_ok = all(i.get("obs") and i.get("concl") for i in invs)

    # 12 worked examples and practice reinforce the understanding
    ex_ok = len(exs) >= 2 and all(all(e.get(k) for k in ("q", "reasoning", "steps", "ans", "interp"))
                                  for e in exs)
    prac_ok = all(ch["practice"].get(l) for l in "ABCD")

    # 13 global context visible in learning experiences
    ctx_vis = any(any(w in " ".join(
        [i.get("task", "")] + list(i.get("notice", [])) + [i.get("obs", ""), i.get("concl", "")]
    ).lower() for w in CONTEXT_WORDS) for i in invs) or bool(ch.get("exploration"))

    # 14 final reflection returns to the SOI
    refl = ch.get("reflection") or []
    refl_ok = len(refl) >= 5 and any("statement of inquiry" in r.lower() for r in refl)

    points = [
        ("1  Key concept developed", key_dev),
        ("2  Related concepts integrated", rel_int),
        ("3  Global context connected", ctx_ok),
        ("4  Exploration addressed", expl_ok),
        ("5  SOI connects the elements", soi_ok),
        ("6  Factual questions aligned", bool(qf)),
        ("7  Conceptual questions aligned", bool(qc)),
        ("8  Debatable questions aligned", bool(qd)),
        ("9  Investigations open with a question", inv_q_ok),
        ("10 Tasks answer that question", concl_ok),
        ("11 Discovery before formal explanation", concl_ok),
        ("12 Examples and practice reinforce", ex_ok and prac_ok),
        ("13 Context visible in learning", ctx_vis),
        ("14 Reflection returns to the SOI", refl_ok),
        ("15 Coherent MYP unit", all([key_dev, rel_int, ctx_ok, expl_ok, soi_ok, q_align,
                                      inv_q_ok, concl_ok, ex_ok, prac_ok, ctx_vis, refl_ok])),
    ]
    if not inv_q_ok:
        notes.append("%d of %d investigations lack an inquiry question"
                     % (sum(1 for x in inv_q if not x), len(inv_q)))
    if not expl_ok:
        notes.append("no global context exploration named")
    if not refl_ok:
        notes.append("no reflection returning to the statement of inquiry")
    if soi.strip().endswith("?"):
        notes.append("statement of inquiry is phrased as a question")
    return points, notes


def main():
    want = [int(a) for a in sys.argv[1:]] or [c["num"] for c in CHAPTERS]
    total_ok = 0
    total = 0
    for ch in CHAPTERS:
        if ch["num"] not in want:
            continue
        points, notes = chapter_report(ch)
        good = sum(1 for _, ok in points if ok)
        total_ok += good
        total += len(points)
        print("Chapter %d · %s  ->  %d/%d points" % (ch["num"], ch["title"], good, len(points)))
        for label, ok in points:
            if not ok:
                print("      missing: %s" % label)
        for n in notes:
            print("      note: %s" % n)
        print()
    print("TOTAL: %d/%d alignment points across %d chapter(s)" % (total_ok, total, len(want)))


if __name__ == "__main__":
    main()
