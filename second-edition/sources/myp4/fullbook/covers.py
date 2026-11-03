#!/usr/bin/env python3
"""Exterior cover artwork for the MYP 4 second-edition coursebook.

Everything here is vector: inline SVG plus CSS, so the covers stay sharp at any
print resolution and can be re-rendered without raster assets.

Contents
--------
* :func:`front_cover_page`   - the premium MYP 4 front cover.
* :func:`back_cover_page`    - the MYP 4 back cover with the five-volume
                               collection strip.
* :func:`collection_strip`   - the five miniature collection covers.
* :func:`cover_concept_page` - a full A4 collection cover concept for a level
                               whose volume has not been produced yet
                               (MYP 1, 3, 4, 5). These are reusable artwork,
                               clearly labelled as concepts.

Design language (shared with the interior and the first edition):
deep green ``#0d2a28``, cream ``#fbf6ec``, gold ``#d7a55d``, rust ``#b24f32``;
Fraunces for display, Source Serif 4 for text, Inter for labels.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from framework import AUTHOR, COLLECTION, FRONT, LEVEL, SERIES  # noqa: E402

GREEN = "#0d2a28"
CREAM = "#fbf6ec"
GOLD = "#d7a55d"
RUST = "#b24f32"

PLATE = (420, 900)          # viewBox of the large cover plate


# --------------------------------------------------------------------- helpers
def _grid():
    """Faint graph-paper grid shared by every cover plate."""
    w, h = PLATE
    out = ['<g stroke="%s" stroke-width=".7" opacity=".07">' % GOLD]
    for x in range(42, w, 42):
        out.append('<path d="M%d 0 V%d"/>' % (x, h))
    for y in range(90, h, 90):
        out.append('<path d="M0 %d H%d"/>' % (y, w))
    out.append("</g>")
    return "".join(out)


def _axis(x, y0, y1, opacity=".30"):
    return ('<g stroke="%s" stroke-width="1" opacity="%s">'
            '<path d="M%d %d V%d"/></g>' % (GOLD, opacity, x, y0, y1))


def _label(x, y, text, anchor="start", size=11, opacity=".60"):
    return ('<text x="%s" y="%s" fill="%s" font-family="Inter, sans-serif" font-size="%s" '
            'letter-spacing="3.2" opacity="%s" text-anchor="%s">%s</text>'
            % (x, y, GOLD, size, opacity, anchor, text))


# ------------------------------------------------------------- MYP 1 hero plate
def _plate_myp1(labels=True):
    """Number systems, set relationships, a line through points, a number line."""
    g = []
    a = g.append
    a(_grid())
    a(_axis(210, 40, 880, ".22"))

    # --- nested squares with the spiral of quarter circles ------------------
    a('<g stroke="%s" stroke-width="1.15" opacity=".9" fill="none">' % GOLD)
    a('<path d="M32 90 H388 V310 H32 Z"/>')                     # golden rectangle
    a('<path d="M252 90 H388 V226 H252 Z"/>')                   # square 2
    a('<path d="M304 226 H388 V310 H304 Z"/>')                  # square 3
    a('<path d="M252 258 H304 V310 H252 Z"/>')                  # square 4
    a('<path d="M272 226 H304 V258 H272 Z"/>')                  # square 5
    a('<path d="M252 238 H272 V258 H252 Z"/>')                  # square 6
    a("</g>")
    a('<g stroke="%s" stroke-width="1.5" opacity=".95" fill="none">' % GOLD)
    a('<path d="M252 310 A220 220 0 0 0 32 90"/>')
    a('<path d="M252 226 A136 136 0 0 1 388 90"/>')
    a('<path d="M388 310 A84 84 0 0 0 304 226"/>')
    a('<path d="M252 258 A52 52 0 0 0 304 310"/>')
    a('<path d="M304 226 A32 32 0 0 1 272 258"/>')
    a('<path d="M272 258 A20 20 0 0 0 252 238"/>')
    a("</g>")
    a('<circle cx="252" cy="310" r="3.2" fill="%s"/>' % GOLD)
    a('<circle cx="388" cy="90" r="3.2" fill="%s"/>' % GOLD)
    a('<circle cx="304" cy="310" r="3.2" fill="%s"/>' % GOLD)

    # --- two overlapping sets ----------------------------------------------
    a('<path d="M210 416.7 A95 95 0 0 1 210 563.3 A95 95 0 0 1 210 416.7 Z" '
      'fill="%s" fill-opacity=".12" stroke="none"/>' % GOLD)
    a('<g stroke="%s" stroke-width="1.15" opacity=".9" fill="none">' % GOLD)
    a('<circle cx="150" cy="490" r="95"/>')
    a('<circle cx="270" cy="490" r="95"/>')
    a("</g>")
    a('<g fill="%s" font-family="Source Serif 4, serif" font-style="italic" '
      'font-size="30" opacity=".9">' % GOLD)
    a('<text x="106" y="502">A</text><text x="300" y="502">B</text>')
    a("</g>")

    # --- a straight line through three marked points ------------------------
    a('<path d="M60 740 L360 660" stroke="%s" stroke-width="1.2" opacity=".85" fill="none"/>' % GOLD)
    a('<g fill="%s">' % GOLD)
    a('<circle cx="60" cy="740" r="3.4"/><circle cx="210" cy="700" r="3.4"/>'
      '<circle cx="360" cy="660" r="3.4"/>')
    a("</g>")

    # --- number line with a marked half ------------------------------------
    a('<g stroke="%s" stroke-width="1.15" opacity=".85" fill="none">' % GOLD)
    a('<path d="M60 820 H360"/>')
    a('<path d="%s"/>' % " ".join("M%d 815v10" % x for x in range(60, 361, 25)))
    a('<path d="M60 812v16 M210 812v16 M360 812v16"/>')
    a("</g>")
    a('<path d="M60 820 H85" stroke="%s" stroke-width="4.5" opacity=".6" fill="none"/>' % RUST)
    a('<g fill="%s">' % GOLD)
    a('<circle cx="85" cy="820" r="3.4"/><circle cx="210" cy="820" r="3.4"/>')
    a("</g>")
    a('<g fill="%s" font-family="Inter, sans-serif" font-size="14" opacity=".8" '
      'text-anchor="middle">' % GOLD)
    a('<text x="60" y="846">0</text><text x="210" y="846">1</text><text x="360" y="846">2</text>')
    a("</g>")

    if labels:
        a(_label(32, 72, "STRUCTURE"))
        a(_label(55, 388, "RELATIONSHIPS"))
        a(_label(32, 872, "QUANTITY"))
    return ('<svg class="plate" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'fill="none">%s</svg>' % (PLATE[0], PLATE[1], "".join(g)))


# ------------------------------------------------------- collection mini plates
def _mini_myp1():
    g = ['<g stroke="%s" stroke-width="2.4" fill="none" opacity=".92">' % GOLD,
         '<path d="M12 12 H88 V60 H12 Z"/>',
         '<path d="M52 12 H88 V38 H52 Z"/>',
         '<path d="M66 38 H88 V60 H66 Z"/>',
         "</g>",
         '<g stroke="%s" stroke-width="2.8" fill="none">' % GOLD,
         '<path d="M52 60 A36 36 0 0 0 12 24"/>',
         '<path d="M52 38 A26 26 0 0 1 88 12"/>',
         '<path d="M88 60 A22 22 0 0 0 66 38"/>',
         "</g>",
         '<path d="M12 74 H88" stroke="%s" stroke-width="2" opacity=".85" fill="none"/>' % GOLD,
         '<path d="%s" stroke="%s" stroke-width="2" opacity=".85" fill="none"/>'
         % (" ".join("M%d 71v6" % x for x in range(12, 89, 9)), GOLD),
         '<path d="M12 74 H26" stroke="%s" stroke-width="5" opacity=".55" fill="none"/>' % RUST]
    return "".join(g)


def _mini_myp3():
    """Growth pattern and similar triangles."""
    bars = []
    for i, h in enumerate([14, 26, 38, 50]):
        x = 16 + i * 20
        bars.append('<path d="M%d %d H%d V62 H%d Z"/>' % (x, 62 - h, x + 13, x))
    tops = " ".join("%d,%d" % (16 + i * 20, 62 - h) for i, h in enumerate([14, 26, 38, 50]))
    return "".join([
        '<g stroke="%s" stroke-width="2.2" fill="none" opacity=".9">' % GOLD,
        "".join(bars),
        "</g>",
        '<path d="M%s" stroke="%s" stroke-width="2.4" fill="none" opacity=".95"/>' % (tops, GOLD),
        '<g fill="%s">%s</g>' % (GOLD, "".join(
            '<circle cx="%d" cy="%d" r="2.6"/>' % (16 + i * 20, 62 - h)
            for i, h in enumerate([14, 26, 38, 50]))),
        '<g stroke="%s" stroke-width="2" fill="none" opacity=".8">' % GOLD,
        '<path d="M14 88 H74 V70 H14 Z"/>',
        '<path d="M14 88 H38 V79 H14 Z" stroke-dasharray="4 3"/>',
        "</g>",
    ])


def _mini_myp3():
    """A scatter of points with a line of best fit."""
    pts = [(22, 62), (33, 70), (44, 50), (55, 64), (66, 42), (78, 54)]
    return "".join([
        '<path d="M14 84 H86" stroke="%s" stroke-width="1.6" fill="none" opacity=".55"/>' % GOLD,
        '<path d="M14 84 V20" stroke="%s" stroke-width="1.6" fill="none" opacity=".55"/>' % GOLD,
        '<path d="M20 76 L82 40" stroke="%s" stroke-width="2.2" fill="none" opacity=".92"/>' % GOLD,
        '<g fill="%s">%s</g>' % (GOLD, "".join('<circle cx="%d" cy="%d" r="2.6"/>' % p for p in pts)),
    ])


def _mini_myp4():
    """A quadratic with its intercepts and axis of symmetry."""
    return "".join([
        '<path d="M14 88 H86" stroke="%s" stroke-width="1.6" fill="none" opacity=".55"/>' % GOLD,
        '<path d="M18 88 Q50 62 82 88" stroke="%s" stroke-width="2.4" fill="none"/>' % GOLD,
        '<path d="M50 66 V88" stroke="%s" stroke-width="1.4" stroke-dasharray="4 3" fill="none" '
        'opacity=".7"/>' % GOLD,
        '<g fill="%s"><circle cx="18" cy="88" r="2.6"/><circle cx="82" cy="88" r="2.6"/>'
        '<circle cx="50" cy="75" r="2.6"/></g>' % GOLD,
    ])


def _mini_myp5():
    """Exponential and logarithmic curves meeting."""
    return "".join([
        '<path d="M14 90 H86" stroke="%s" stroke-width="1.6" fill="none" opacity=".5"/>' % GOLD,
        '<path d="M14 90 V22" stroke="%s" stroke-width="1.6" fill="none" opacity=".5"/>' % GOLD,
        '<path d="M16 84 C40 82 58 62 86 34" stroke="%s" stroke-width="2.4" fill="none"/>' % GOLD,
        '<path d="M16 30 C42 48 62 74 86 88" stroke="%s" stroke-width="2" fill="none" '
        'opacity=".8"/>' % GOLD,
        '<circle cx="46" cy="60" r="2.8" fill="%s"/>' % GOLD,
    ])


MINI = {1: _mini_myp1, 2: _mini_myp3, 3: _mini_myp3, 4: _mini_myp4, 5: _mini_myp5}


def mini_art(level):
    """Small motif (viewBox 0 0 100 96) used inside a collection miniature."""
    return ('<svg viewBox="0 0 100 96" xmlns="http://www.w3.org/2000/svg" fill="none">%s</svg>'
            % MINI[level]())


# ------------------------------------------------------------- concept plates
def _plate_myp3():
    """Ratio and proportion: a growth pattern, then similar triangles."""
    g = []
    a = g.append
    a(_grid())
    a('<g stroke="%s" stroke-width="1.2" opacity=".9" fill="none">' % GOLD)
    for i, h in enumerate([70, 140, 210, 280]):
        x = 70 + i * 74
        a('<path d="M%d %d H%d V430 H%d Z"/>' % (x, 430 - h, x + 46, x))
    a("</g>")
    a('<path d="M70 360 L362 150" stroke="%s" stroke-width="1.4" opacity=".9" fill="none"/>' % GOLD)
    a('<g fill="%s">%s</g>' % (GOLD, "".join(
        '<circle cx="%d" cy="%d" r="3.4"/>' % (70 + i * 74, 430 - h)
        for i, h in enumerate([70, 140, 210, 280]))))
    a(_label(70, 92, "GROWTH"))
    a('<g stroke="%s" stroke-width="1.3" opacity=".92" fill="none">' % GOLD)
    a('<path d="M60 830 H340 V590 H60 Z"/>')
    a('<path d="M60 830 H170 V710 H60 Z" stroke-dasharray="7 5"/>')
    a('<path d="M170 710 L340 590" stroke-dasharray="7 5" opacity=".7"/>')
    a("</g>")
    a('<path d="M60 830 L340 590" stroke="%s" stroke-width="1.2" opacity=".45" fill="none"/>' % GOLD)
    a(_label(60, 862, "PROPORTION"))
    return ('<svg class="plate" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'fill="none">%s</svg>' % (PLATE[0], PLATE[1], "".join(g)))


def _plate_myp3():
    """A quadratic with its axis of symmetry, and a scatter with a line of best fit."""
    g = []
    a = g.append
    a(_grid())
    a(_axis(210, 60, 880, ".20"))
    a('<path d="M60 210 Q210 480 360 210" stroke="%s" stroke-width="1.5" fill="none"/>' % GOLD)
    a('<path d="M210 150 V330" stroke="%s" stroke-width="1.3" stroke-dasharray="7 5" fill="none" '
      'opacity=".7"/>' % GOLD)
    a('<circle cx="210" cy="345" r="3.6" fill="%s"/>' % GOLD)
    a('<path d="M60 210 H360" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % GOLD)
    a(_label(60, 132, "QUADRATIC"))
    a('<path d="M70 620 H360" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % GOLD)
    a('<path d="M70 620 V880" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % GOLD)
    a('<path d="M80 850 L350 700" stroke="%s" stroke-width="1.5" fill="none" opacity=".92"/>' % GOLD)
    pts = [(100, 838), (128, 866), (156, 792), (184, 830), (212, 748), (240, 782),
           (268, 722), (296, 758), (324, 706)]
    a('<g fill="%s">%s</g>' % (GOLD, "".join('<circle cx="%d" cy="%d" r="3.2"/>' % p for p in pts)))
    a(_label(70, 878, "CORRELATION"))
    return ('<svg class="plate" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'fill="none">%s</svg>' % (PLATE[0], PLATE[1], "".join(g)))


def _plate_myp4():
    """Circle with a tangent, a quadratic with intercepts, and a distribution."""
    g = []
    a = g.append
    a(_grid())
    a('<circle cx="210" cy="300" r="118" stroke="%s" stroke-width="1.4" fill="none" opacity=".92"/>'
      % GOLD)
    a('<path d="M210 300 L293 217" stroke="%s" stroke-width="1.3" fill="none" opacity=".85"/>' % GOLD)
    a('<path d="M255 179 L331 255" stroke="%s" stroke-width="1.5" fill="none"/>' % GOLD)
    a('<path d="M293 217 l-7 0 M293 217 l0 7" stroke="%s" stroke-width="1.2" fill="none" '
      'opacity=".8"/>' % GOLD)
    a('<circle cx="210" cy="300" r="3.2" fill="%s"/>' % GOLD)
    a(_label(60, 150, "CIRCLE GEOMETRY"))
    a('<path d="M70 620 H360" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % GOLD)
    a('<path d="M100 620 Q210 830 320 620" stroke="%s" stroke-width="1.5" fill="none"/>' % GOLD)
    a('<path d="M210 600 V760" stroke="%s" stroke-width="1.3" stroke-dasharray="7 5" fill="none" '
      'opacity=".7"/>' % GOLD)
    a('<g fill="%s"><circle cx="100" cy="620" r="3.2"/><circle cx="320" cy="620" r="3.2"/>'
      '<circle cx="210" cy="725" r="3.2"/></g>' % GOLD)
    a(_label(70, 862, "QUADRATIC FUNCTION"))
    a('<path d="M60 848 C120 848 160 776 210 776 C260 776 300 848 360 848" stroke="%s" '
      'stroke-width="1.4" fill="none" opacity=".8"/>' % GOLD)
    return ('<svg class="plate" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'fill="none">%s</svg>' % (PLATE[0], PLATE[1], "".join(g)))


def _plate_myp5():
    """Unit circle with a marked angle, then exponential and logarithmic curves."""
    g = []
    a = g.append
    a(_grid())
    a('<circle cx="210" cy="270" r="118" stroke="%s" stroke-width="1.4" fill="none" opacity=".92"/>'
      % GOLD)
    a('<path d="M92 270 H328" stroke="%s" stroke-width="1.2" stroke-dasharray="7 5" fill="none" '
      'opacity=".65"/>' % GOLD)
    a('<path d="M210 270 L312 216" stroke="%s" stroke-width="1.4" fill="none" opacity=".9"/>' % GOLD)
    a('<path d="M210 270 A118 118 0 0 0 312 216" stroke="%s" stroke-width="1.3" fill="none" '
      'opacity=".7"/>' % GOLD)
    a('<path d="M330 190 L344 258" stroke="%s" stroke-width="1.5" fill="none" opacity=".9"/>' % GOLD)
    a('<circle cx="210" cy="270" r="3.2" fill="%s"/>' % GOLD)
    a(_label(60, 120, "UNIT CIRCLE"))
    a('<path d="M60 700 H360" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % GOLD)
    a('<path d="M60 700 V880" stroke="%s" stroke-width="1.1" fill="none" opacity=".45"/>' % GOLD)
    a('<path d="M70 862 C150 856 230 780 350 620" stroke="%s" stroke-width="1.6" fill="none"/>'
      % GOLD)
    a('<path d="M70 640 C160 720 250 820 350 866" stroke="%s" stroke-width="1.5" fill="none" '
      'opacity=".8"/>' % GOLD)
    a('<circle cx="222" cy="752" r="3.4" fill="%s"/>' % GOLD)
    a(_label(60, 892, "EXPONENTIAL AND LOGARITHMIC"))
    return ('<svg class="plate" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'fill="none">%s</svg>' % (PLATE[0], PLATE[1], "".join(g)))


PLATES = {1: _plate_myp1, 2: _plate_myp3, 3: _plate_myp3, 4: _plate_myp4, 5: _plate_myp5}


# ------------------------------------------------------------------- page HTML
def _top_band(left, right):
    return ('<div class="pc-top"><span>%s</span><span class="r">%s</span></div>'
            % (left, right))


def _foot(left, right):
    return ('<div class="pc-foot"><span class="pc-author">%s</span><span>%s</span></div>'
            % (left, right))


def _shell(inner, page_id, cls):
    return ('<section class="page cover %s" data-page-id="%s">'
            '<div class="pc-bg"></div><div class="pc-grid"></div>%s</section>'
            % (cls, page_id, inner))


def front_cover_page():
    """Premium MYP 1 front cover."""
    c = FRONT["cover"]
    topics = " ".join('<span class="t">%s</span>' % t for t in c["topics"])
    body = (
        '<div class="pc-body">'
        '<div class="pc-eyebrow">MYP</div>'
        '<h1 class="pc-title">%s</h1>'
        '<div class="pc-level"><span class="pc-numeral">%s</span>'
        '<span class="pc-leveltext"><span class="pc-levelname">%s</span>'
        '<span class="pc-levelnote">%s</span></span></div>'
        '<p class="pc-standfirst">%s</p>'
        '<div class="pc-rule"></div>'
        '<div class="pc-topics">%s</div>'
        '<div class="pc-inquiry"><div class="pc-inquirylabel">%s</div><p>%s</p></div>'
        '<div class="pc-criteria"><div class="pc-criteriahead">MYP assessment criteria</div>'
        '<div class="pc-criteriagrid">%s</div></div>'
        "</div>" % (c["title"], c["level"], c["level_text"], c["level_note"],
                    c["standfirst"], topics, c["inquiry_label"], c["inquiry"],
                    "".join('<span class="k">Criterion %s</span><span class="v">%s</span>'
                            % (k, v) for k, v in c["criteria"])))
    art = '<div class="pc-art">%s</div>' % PLATES[LEVEL]()
    top = _top_band(c["kicker"], c["edition"])
    foot = _foot(c["author"], c["series"])
    return _shell(top + art + body + foot, "book-cover", "premium-cover")


def collection_strip():
    """The five miniature collection covers for the back cover."""
    vols = []
    for v in COLLECTION:
        now = v["status"] == "this volume"
        mini = (
            '<div class="mini%s">'
            '<div class="m-top">MYP</div>'
            '<div class="m-art">%s</div>'
            '<div class="m-foot"><div class="m-num">%d</div>'
            '<div class="m-lab">Mathematics</div></div>'
            "</div>" % (" now" if now else "", mini_art(v["level"]), v["level"]))
        cap = ('<div class="pc-cap%s">Volume %d · %s</div>'
               % (" now" if now else "", v["level"], v["status"]))
        vols.append('<div class="pc-vol">%s%s</div>' % (mini, cap))
    return '<div class="pc-strip">%s</div>' % "".join(vols)


def back_cover_page():
    """Premium MYP 1 back cover carrying the five-volume collection."""
    b = FRONT["backcover"]
    paras = "".join("<p>%s</p>" % p for p in b["paras"])
    body = (
        '<div class="pc-bbody">'
        '<div class="pc-bheading">%s</div>'
        '<div class="pc-btext">%s</div>'
        '<div class="pc-becho">%s</div>'
        "</div>"
        '<div class="pc-collection">'
        '<div class="pc-collectionhead">%s</div>'
        "%s"
        '<p class="pc-collectionnote">%s</p>'
        "</div>"
        '<p class="pc-smallprint">%s</p>'
        % (b["heading"], paras, _plate_myp1(labels=False), b["collection_heading"],
           collection_strip(), b["collection_note"], b["smallprint"]))
    top = _top_band(b["kicker"], b["edition"])
    foot = _foot(b["author"], b["foot_right"])
    return _shell(top + body + foot, "back-cover", "back-cover-page")


def cover_concept_page(level, theme, status="forthcoming"):
    """A full A4 collection cover concept for a volume that is not yet produced."""
    vol = dict(level=str(level), theme=theme)
    c = FRONT["cover"]
    body = (
        '<div class="pc-body">'
        '<div class="pc-eyebrow">MYP</div>'
        '<h1 class="pc-title">Mathematics</h1>'
        '<div class="pc-level"><span class="pc-numeral">%s</span>'
        '<span class="pc-leveltext"><span class="pc-levelname">Student coursebook</span>'
        '<span class="pc-levelnote">%s</span></span></div>'
        '<div class="pc-rule"></div>'
        '<div class="pc-concept">%s</div>'
        "</div>" % (vol["level"], vol["theme"],
                    "Collection cover concept · volume in preparation. Not a published volume."))
    art = '<div class="pc-art">%s</div>' % PLATES[level]()
    top = _top_band("MYP Mathematics · Student coursebook", "Cover concept")
    foot = _foot(AUTHOR, "MYP Mathematics · Volume %d of 5" % level)
    return _shell(top + art + body + foot, "concept-%d" % level, "premium-cover")
