#!/usr/bin/env python3
"""Mechanical practice/criterion alignment diagnostic for the MYP 5 coursebook.

For every practice item the diagnostic asks whether the item's prompt, answer
and given reasoning contain any of the contextual or conceptual vocabulary of
its own chapter: the key concept, the related concepts named in the statement of
inquiry, the official global context and its exploration, the section titles,
and the real-world situations the chapter actually uses.

An item with no such vocabulary is *flagged*. A flag is not a defect: it means
the item was read and judged by hand. Criterion fit is judged editorially; the
mechanical test only says which items deserve a look.

Writes practice-audit.json next to this script and prints a summary.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from framework import CHAPTERS  # noqa: E402

# Words that carry context or a concept wherever they appear. They are the
# vocabulary the MYP unit framework of each chapter is written in.
CONTEXT_WORDS = {
    "money", "cost", "price", "pay", "paid", "budget", "interest", "loan", "save",
    "savings", "profit", "earn", "wage", "tax", "discount", "value", "offer",
    "bill", "rent", "invest", "depreciate", "inflation", "percentage",
    "distance", "speed", "journey", "travel", "route", "map", "bearing",
    "height", "depth", "length", "width", "area", "volume", "capacity", "surface",
    "perimeter", "scale", "model", "shape", "angle", "triangle", "circle",
    "prism", "cylinder", "cone", "sphere", "pyramid", "packaging", "container",
    "tank", "roof", "rain", "water", "material", "density", "mass", "tolerance",
    "time", "rate", "growth", "population", "temperature", "measurement",
    "survey", "data", "sample", "frequency", "average", "median", "quartile",
    "spread", "distribution", "outlier", "histogram", "box plot", "graph",
    "probability", "chance", "risk", "game", "fair", "dice", "die", "card",
    "spinner", "counter", "event", "outcome", "experiment", "simulation",
    "pattern", "sequence", "term", "rule", "generalisation", "justify",
    "justification", "proof", "conjecture", "equivalent", "equivalence",
    "simplify", "simplification", "approximation", "estimate", "bound", "error",
    "accuracy", "standard form", "surd", "index", "exponent", "factorise",
    "expand", "solve", "equation", "inequality", "formula", "function",
    "gradient", "intercept", "vertex", "parabola", "quadratic", "linear",
    "exponential", "variable", "domain", "range", "transform", "translation",
    "reflection", "rotation", "enlargement", "congruent", "congruence",
    "similar", "similarity", "pythagoras", "trigonometric", "sine", "cosine",
    "tangent", "elevation", "depression", "system", "systems", "quantity",
    "representation", "space", "change", "logic", "statistics", "form",
    "relationships", "measurement", "design", "optimisation", "efficient",
    "innovation", "orientation", "fairness", "development", "sustainability",
    "identities", "globalisation", "access", "decision", "limitation",
    "assumption", "constraint", "brief", "review", "communicate", "criterion",
    "criteria", "rubric", "assessment",
}
GENERIC = {"the", "and", "for", "with", "from", "that", "this", "your", "own",
           "into", "each", "when", "what", "how", "why", "use", "using", "find",
           "write", "explain", "show", "state", "give", "work", "out", "about"}


def words(text):
    """Word set with naive singulars, so 'costs' matches 'cost'."""
    raw = set(w for w in re.findall(r"[a-z]+", text.lower()) if len(w) > 3)
    out = set(raw)
    for w in raw:
        if w.endswith("s") and len(w) > 4:
            out.add(w[:-1])
        if w.endswith("es") and len(w) > 5:
            out.add(w[:-2])
    return out


def chapter_vocab(ch):
    v = set()
    v |= words(ch["key"])
    for r in ch["related"]:
        v |= words(r)
    v |= words(ch["context"])
    v |= words(ch["exploration"])
    v |= words(ch.get("standfirst", ""))
    v |= words(ch["inquiry"])
    for s in ch["sections"]:
        v |= words(s["title"])
        v |= words(s["inquiry_q"])
    v |= set(w for w in CONTEXT_WORDS if len(w.split()) == 1)
    # multi-word context phrases are matched separately
    return v, set(w for w in CONTEXT_WORDS if " " in w)


def item_text(item):
    return " ".join(str(x) for x in item[:4])


def main():
    report = {"chapters": [], "flagged": []}
    totals = {"A": [0, 0], "B": [0, 0], "C": [0, 0], "D": [0, 0]}
    for ch in CHAPTERS:
        vocab, phrases = chapter_vocab(ch)
        entry = {"num": ch["num"], "title": ch["title"], "items": 0, "flagged": 0,
                 "by_criterion": {}}
        for tier in ("A", "B", "C", "D"):
            n = flag = 0
            for item in ch["practice"][tier]:
                n += 1
                text = item_text(item).lower()
                hit = bool(words(text) & vocab) or any(p in text for p in phrases)
                totals[tier][0] += 1
                if not hit:
                    flag += 1
                    totals[tier][1] += 1
                    entry["flagged"] += 1
                    report["flagged"].append(
                        {"chapter": ch["num"], "criterion": tier, "id": item[0],
                         "prompt": item[1], "answer": item[2], "reason": item[3]})
            entry["by_criterion"][tier] = {"items": n, "flagged": flag}
            entry["items"] += n
        report["chapters"].append(entry)
    report["totals"] = {k: {"items": v[0], "flagged": v[1]} for k, v in totals.items()}
    report["items_total"] = sum(v[0] for v in totals.values())
    report["flagged_total"] = sum(v[1] for v in totals.values())
    (HERE / "practice-audit.json").write_text(json.dumps(report, indent=1),
                                              encoding="utf-8")
    print("items: %d   flagged: %d" % (report["items_total"],
                                       report["flagged_total"]))
    for k in ("A", "B", "C", "D"):
        t = totals[k]
        print("  criterion %s: %d items, %d flagged" % (k, t[0], t[1]))
    for e in report["chapters"]:
        print("  ch %-2d %-46s %2d items, %d flagged" %
              (e["num"], e["title"][:46], e["items"], e["flagged"]))


if __name__ == "__main__":
    main()
