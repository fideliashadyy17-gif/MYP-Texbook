#!/usr/bin/env python3
"""Parametrised SVG teaching diagrams for the MYP 3 second-edition coursebook.

Every diagram is vector, labelled and sized for a 78 mm text column, so it stays
sharp in print. Diagrams are referenced from the content data by name, e.g.
``fig("number_line", 0, 3, 1, [1, 2])``.
"""
import re

GOLD = "#d7a55d"
GREEN = "#0d2a28"
RUST = "#b24f32"
INK = "#22302c"
LINE = "#9aa8a2"


def _open(vb, extra=""):
    return ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" '
            'role="img" %s fill="none">' % (vb[0], vb[1], extra))


def number_line(lo, hi, step, marks=(), label="", unit=""):
    """A horizontal number line with ticks and highlighted marks."""
    x0, x1, y = 30, 300, 40
    span = hi - lo
    def X(v):
        return x0 + (v - lo) * (x1 - x0) / span
    ticks = []
    v = lo
    while v <= hi + 1e-9:
        ticks.append(v)
        v += step
    out = [_open((330, 74)), '<g stroke="%s" stroke-width="1.2">' % INK,
           '<path d="M%d %d H%d"/>' % (x0, y, x1)]
    for t in ticks:
        out.append('<path d="M%.1f %dv6"/>' % (X(t), y - 3))
    out.append("</g>")
    for m in marks:
        out.append('<circle cx="%.1f" cy="%d" r="3.4" fill="%s"/>' % (X(m), y, RUST))
    for t in ticks:
        out.append('<text x="%.1f" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" text-anchor="middle">%s%s</text>'
                   % (X(t), y + 18, INK, _num(t), unit))
    if label:
        out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (x1 + 6, y + 4, LINE, label))
    out.append("</svg>")
    return "".join(out)


SUPERS = {
    "\u2070": "0", "\u00b9": "1", "\u00b2": "2", "\u00b3": "3",
    "\u2074": "4", "\u2075": "5", "\u2076": "6", "\u2077": "7",
    "\u2078": "8", "\u2079": "9", "\u207a": "+", "\u207b": "-",
    "\u207d": "(", "\u207e": ")", "\u1d50": "m", "\u207f": "n",
}
SUPER_RUN = re.compile("[" + "".join(SUPERS) + "]+")


def _superscripts(svg):
    """Raise superscript runs inside SVG text nodes, where KaTeX cannot be used."""
    def sub(m):
        body = "".join(SUPERS[c] for c in m.group(0))
        return '<tspan baseline-shift="super" font-size="72%">' + body + '</tspan>'
    parts = re.split(r"(<[^>]*>)", svg)
    for i, part in enumerate(parts):
        if part.startswith("<"):
            continue
        parts[i] = SUPER_RUN.sub(sub, part)
    return "".join(parts)


def _text_width(txt, fs):
    """Approximate rendered width of a string in Inter at font-size fs."""
    w = 0.0
    for ch in txt:
        if ch == " ":
            w += 0.26
        elif ch.isdigit() or ch.isupper():
            w += 0.62
        elif ch.islower():
            w += 0.52
        else:
            w += 0.42
    return w * fs


def _wrap(txt, fs, maxw):
    """Greedy word wrap to a maximum width, honouring explicit line breaks."""
    out = []
    for para in txt.split("|"):
        words = para.split(" ")
        cur = ""
        for wd in words:
            trial = (cur + " " + wd).strip()
            if not cur or _text_width(trial, fs) <= maxw:
                cur = trial
            else:
                out.append(cur)
                cur = wd
        out.append(cur)
    return [l for l in out if l != ""] or [""]


def _num(v):
    if abs(v - int(v)) < 1e-9:
        return str(int(v)).replace("-", "\u2212")
    return ("%g" % v).replace("-", "\u2212")


def double_number_line(top, bottom, title=""):
    """Two aligned number lines for ratio and proportion."""
    out = [_open((330, 96))]
    if title:
        out.append('<text x="30" y="14" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    for row, (labels, y) in enumerate(((top, 34), (bottom, 70))):
        n = len(labels)
        step = 260 / max(n - 1, 1)
        out.append('<path d="M30 %d H290" stroke="%s" stroke-width="1.2"/>' % (y, INK))
        for i, lab in enumerate(labels):
            x = 30 + i * step
            out.append('<path d="M%.1f %dv6" stroke="%s" stroke-width="1"/>' % (x, y - 3, INK))
            out.append('<text x="%.1f" y="%d" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="9" text-anchor="middle">%s</text>' % (x, y + 16, INK, lab))
    # join matching positions
    for i in range(min(len(top), len(bottom))):
        x = 30 + i * (260 / max(len(top) - 1, 1))
        out.append('<path d="M%.1f 40 V70" stroke="%s" stroke-width=".8" opacity=".55"/>' % (x, GOLD))
    out.append("</svg>")
    return "".join(out)


def table(rows, header=True, widths=None, caption="", fs=9.5):
    """A labelled table; rows is a list of lists of strings.

    Cell text wraps to the column width and the row height grows to fit, so long
    explanations stay inside their cell instead of running over the neighbours.
    """
    cols = max(len(r) for r in rows)
    cw = widths or [int(300 / cols)] * cols
    # A long table is set with tighter rows so that it still reads at the size
    # the page allows instead of being scaled down into illegibility.
    lead = fs + 2.4 if len(rows) <= 8 else fs + 1.3
    row_min = 20 if len(rows) <= 8 else 14.5
    # wrap every cell first so the row heights can be computed
    cells = []
    for row in rows:
        line_sets = []
        for c in range(cols):
            val = str(row[c]) if c < len(row) else ""
            avail = cw[c] - 8
            lines = _wrap(val, fs, avail) if val else [""]
            if len(lines) > 1 and fs > 8.4:
                # a wrapped cell is given a slightly smaller size so it still fits
                lines = _wrap(val, fs - 1.0, avail)
            line_sets.append(lines)
        cells.append(line_sets)
    heights = [max(row_min, max(len(lines) for lines in ls) * lead + 6) for ls in cells]
    h = sum(heights) + (18 if caption else 0) + 4
    out = [_open((306, h))]
    y = 4
    for r, line_sets in enumerate(cells):
        x = 3
        rh = heights[r]
        for c, lines in enumerate(line_sets):
            if header and r == 0:
                out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#f2ece0"/>'
                           % (x, y, cw[c], rh))
            out.append('<rect x="%d" y="%d" width="%d" height="%d" stroke="%s" stroke-width=".7"/>'
                       % (x, y, cw[c], rh, LINE))
            size = fs - 1.0 if len(lines) > 1 else fs
            top = y + (rh - len(lines) * lead) / 2 + size
            for li, line in enumerate(lines):
                out.append('<text x="%d" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                           'font-size="%.1f" text-anchor="middle">%s</text>'
                           % (x + cw[c] // 2, top + li * lead, INK, size, line))
            x += cw[c]
        y += rh
    if caption:
        out.append('<text x="3" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="8.5">%s</text>' % (y + 13, LINE, caption))
    out.append("</svg>")
    return "".join(out)


def bar_model(total, parts, labels=None, title=""):
    """A strip divided into parts, with the named parts shaded (fractions/ratios)."""
    w = 300
    out = [_open((312, 78))]
    if title:
        out.append('<text x="6" y="13" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    x = 6
    y = 24
    for i, p in enumerate(parts):
        pw = (w - 12) * p / total
        shade = i in (labels or [])
        out.append('<rect x="%.1f" y="%d" width="%.1f" height="26" fill="%s" stroke="%s" '
                   'stroke-width="1"/>' % (x, y, pw, RUST if shade else "#fbf6ec", INK))
        out.append('<text x="%.1f" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9.5" text-anchor="middle">%s</text>'
                   % (x + pw / 2, y + 42, INK, _num(p)))
        x += pw
    out.append("</svg>")
    return "".join(out)


def tiles(cols, rows, shade=(), title="", cell=22, gap=2.5, note=""):
    """A grid of unit tiles; shade is an iterable of (row, col) pairs, 0-based."""
    shade = set(shade)
    w = 12 + cols * (cell + gap)
    h = 26 + rows * (cell + gap) + (14 if note else 0)
    out = [_open((312, h))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    for r in range(rows):
        for c in range(cols):
            x = 6 + c * (cell + gap)
            y = 22 + r * (cell + gap)
            on = (r, c) in shade
            out.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="%s" '
                       'fill-opacity="%s" stroke="%s" stroke-width=".9"/>'
                       % (x, y, cell, cell, GOLD if on else "#fbf6ec",
                          ".8" if on else "1", INK))
    if note:
        out.append('<text x="6" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="8.5">%s</text>' % (h - 4, LINE, note))
    out.append("</svg>")
    return "".join(out)


def staircase(steps, title="", cell=20, gap=2.5):
    """A staircase of unit squares: 1, 2, 3 ... steps tiles."""
    w = 12 + steps * (cell + gap)
    h = 26 + steps * (cell + gap)
    out = [_open((312, h))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    for r in range(steps):
        for c in range(r + 1):
            x = 6 + c * (cell + gap)
            y = 22 + (steps - 1 - r) * (cell + gap)
            out.append('<rect x="%.1f" y="%.1f" width="%d" height="%d" fill="%s" '
                       'fill-opacity=".8" stroke="%s" stroke-width=".9"/>'
                       % (x, y, cell, cell, GOLD, INK))
    out.append("</svg>")
    return "".join(out)


def grid(points=(), labels=(), xmin=-5, xmax=5, ymin=-5, ymax=5, shape=(), title=""):
    """A coordinate grid with plotted points and an optional polygon.

    The plot is centred on the middle of the requested range, so an asymmetric
    window such as x from 0 to 10 still fills the frame instead of running off
    the top and the right. A title sits in its own band above the plot.
    """
    W, H = 300, 214
    top = 32 if title else 18
    bot = H + (30 if title else 6)
    out = [_open((312, bot))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    hmid, vmid = (xmin + xmax) / 2.0, (ymin + ymax) / 2.0
    ox, oy = W / 2, (top + bot) / 2.0
    sx, sy = (W - 40) / (xmax - xmin), (H - 40) / (ymax - ymin)

    def X(v):
        return ox + (v - hmid) * sx

    def Y(v):
        return oy - (v - vmid) * sy
    out.append('<g stroke="%s" stroke-width=".5" opacity=".5">' % LINE)
    v = xmin
    while v <= xmax:
        out.append('<path d="M%.1f %d V%.1f"/>' % (X(v), top, Y(ymin)))
        v += 1
    v = ymin
    while v <= ymax:
        out.append('<path d="M%d %.1f H%d"/>' % (X(xmin), Y(v), X(xmax)))
        v += 1
    out.append("</g>")
    out.append('<g stroke="%s" stroke-width="1.3">' % INK)
    out.append('<path d="M%d %.1f H%d"/>' % (X(xmin), Y(0), X(xmax)))
    out.append('<path d="M%.1f %.1f V%.1f"/>' % (X(0), Y(ymin), Y(ymax)))
    out.append("</g>")
    if shape:
        pts = " ".join("%.1f,%.1f" % (X(p[0]), Y(p[1])) for p in shape)
        out.append('<polygon points="%s" fill="rgba(215,165,93,.18)" stroke="%s" '
                   'stroke-width="1.4"/>' % (pts, GOLD))
    for i, p in enumerate(points):
        out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/>' % (X(p[0]), Y(p[1]), RUST))
        if i < len(labels):
            out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="9">%s</text>' % (X(p[0]) + 6, Y(p[1]) - 5, INK, labels[i]))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" font-size="9">x</text>'
               % (X(xmax) + 4, Y(0) + 12, INK))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" font-size="9">y</text>'
               % (X(0) + 6, Y(ymax) - 6, INK))
    out.append("</svg>")
    return "".join(out)


def venn(a_label="A", b_label="B", shared="", only_a="", only_b=""):
    """Two overlapping sets with room for elements."""
    out = [_open((312, 150))]
    out.append('<path d="M96 40 A58 58 0 0 1 96 132 A58 58 0 0 1 96 40 Z" fill="%s" '
               'fill-opacity=".16" stroke="none"/>' % GOLD)
    out.append('<circle cx="96" cy="86" r="58" stroke="%s" stroke-width="1.3"/>' % INK)
    out.append('<circle cx="176" cy="86" r="58" stroke="%s" stroke-width="1.3"/>' % INK)
    out.append('<text x="60" y="30" fill="%s" font-family="Inter, sans-serif" font-size="11">%s</text>'
               % (INK, a_label))
    out.append('<text x="206" y="30" fill="%s" font-family="Inter, sans-serif" font-size="11">%s</text>'
               % (INK, b_label))
    for txt, x in ((only_a, 66), (shared, 130), (only_b, 194)):
        if txt:
            out.append('<text x="%d" y="92" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="10" text-anchor="middle">%s</text>' % (x, INK, txt))
    out.append("</svg>")
    return "".join(out)


def triangle(pts, labels=(), right=(), angles=(), title=""):
    """A labelled triangle; pts is a list of (x, y) in a 300 x 180 box."""
    out = [_open((312, 196))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    poly = " ".join("%.1f,%.1f" % (p[0] + 6, p[1] + 20) for p in pts)
    out.append('<polygon points="%s" fill="rgba(215,165,93,.14)" stroke="%s" '
               'stroke-width="1.4"/>' % (poly, GOLD))
    for i, (x, y) in enumerate(pts):
        if i < len(labels):
            out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="11">%s</text>' % (x + 6, y + 20, INK, labels[i]))
    for (vx, vy, txt) in right:
        out.append('<path d="M%.1f %.1f h10 v10 h-10 Z" stroke="%s" stroke-width="1"/>'
                   % (vx + 6, vy + 20, INK))
    for (vx, vy, txt) in angles:
        out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="10">%s</text>' % (vx + 6, vy + 20, RUST, txt))
    out.append("</svg>")
    return "".join(out)


def prism(kind="cuboid", w=4, h=3, d=2, caption=""):
    """A simple labelled solid: cuboid or cylinder."""
    out = [_open((312, 190))]
    if kind == "cuboid":
        out.append('<g stroke="%s" stroke-width="1.3" fill="none">' % INK)
        out.append('<rect x="60" y="70" width="120" height="70" fill="rgba(215,165,93,.14)"/>')
        out.append('<path d="M60 70 L100 40 L220 40 L220 110 L180 140 L60 140"/>')
        out.append('<path d="M180 140 L180 70 L220 40"/>')
        out.append('<path d="M100 40 L100 110 L180 110"/>')
        out.append("</g>")
        out.append('<text x="120" y="132" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="10" text-anchor="middle">%s</text>' % (INK, _num(w)))
        out.append('<text x="46" y="108" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="10" text-anchor="middle">%s</text>' % (INK, _num(h)))
        out.append('<text x="150" y="58" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="10" text-anchor="middle">%s</text>' % (INK, _num(d)))
    else:
        out.append('<g stroke="%s" stroke-width="1.3" fill="none">' % INK)
        out.append('<ellipse cx="130" cy="60" rx="60" ry="18" fill="rgba(215,165,93,.16)"/>')
        out.append('<path d="M70 60 V130 M190 60 V130"/>')
        out.append('<path d="M70 130 A60 18 0 0 0 190 130" fill="rgba(215,165,93,.10)"/>')
        out.append("</g>")
        out.append('<path d="M130 60 V130" stroke="%s" stroke-width=".8" stroke-dasharray="4 3"/>'
                   % LINE)
        out.append('<text x="140" y="100" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="10">r = %s</text>' % (INK, _num(w)))
        out.append('<text x="196" y="100" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="10">h = %s</text>' % (INK, _num(h)))
    if caption:
        out.append('<text x="6" y="182" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="8.5">%s</text>' % (LINE, caption))
    out.append("</svg>")
    return "".join(out)


def transform(shape, image, mirror="x", title=""):
    """A shape and its image on a grid (translation, reflection, rotation)."""
    W, H = 300, 214
    out = [_open((312, H + (16 if title else 6)))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    ox, oy = W / 2, (H + 16) / 2
    sp = (W - 40) / 12.0

    def X(v):
        return ox + v * sp

    def Y(v):
        return oy - v * sp
    out.append('<g stroke="%s" stroke-width=".5" opacity=".5">' % LINE)
    v = -6
    while v <= 6:
        out.append('<path d="M%.1f %d V%.1f"/>' % (X(v), 18, Y(-6)))
        v += 1
    v = -6
    while v <= 6:
        out.append('<path d="M%d %.1f H%d"/>' % (X(-6), Y(v), X(6)))
        v += 1
    out.append("</g>")
    out.append('<g stroke="%s" stroke-width="1.3">' % INK)
    out.append('<path d="M%d %.1f H%d"/>' % (X(-6), Y(0), X(6)))
    out.append('<path d="M%.1f %.1f V%.1f"/>' % (X(0), Y(-6), Y(6)))
    out.append("</g>")
    if mirror in ("x", "y"):
        out.append('<path d="M%.1f %.1f V%.1f" stroke="%s" stroke-width=".8" '
                   'stroke-dasharray="3 3"/>' % (X(0), Y(-6), Y(6), RUST))
    for pts, fill, stroke in ((shape, "rgba(215,165,93,.16)", GOLD),
                              (image, "rgba(178,79,50,.14)", RUST)):
        poly = " ".join("%.1f,%.1f" % (X(p[0]), Y(p[1])) for p in pts)
        out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.5"/>' % (poly, fill, stroke))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" font-size="9">x</text>'
               % (X(6) + 4, Y(0) + 12, INK))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" font-size="9">y</text>'
               % (X(0) + 6, Y(6) - 6, INK))
    out.append("</svg>")
    return "".join(out)


def pie(slices, labels=(), title=""):
    """A pie chart; slices are values, labels matching names."""
    import math
    total = sum(slices)
    out = [_open((312, 200))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    cx, cy, r = 90, 105, 62
    ang = -90.0
    cols = [GOLD, RUST, "#4d7a72", "#8a6f3c", "#b9a06a", "#6f8a83"]
    for i, s in enumerate(slices):
        sweep = 360.0 * s / total
        a0, a1 = math.radians(ang), math.radians(ang + sweep)
        large = 1 if sweep > 180 else 0
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        out.append('<path d="M%.1f %.1f A%d %d 0 %d 1 %.1f %.1f L%.1f %.1f Z" fill="%s" '
                   'fill-opacity=".75" stroke="%s" stroke-width="1"/>'
                   % (x0, y0, r, r, large, x1, y1, cx, cy, cols[i % len(cols)], INK))
        ang += sweep
    for i, lab in enumerate(labels):
        out.append('<rect x="176" y="%d" width="10" height="10" fill="%s" stroke="%s" '
                   'stroke-width=".6"/>' % (66 + i * 20, cols[i % len(cols)], INK))
        out.append('<text x="192" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9.5">%s</text>' % (74 + i * 20, INK, lab))
    out.append("</svg>")
    return "".join(out)


def bar_chart(cats, values, title="", ymax=None):
    """A vertical bar chart with labelled axes."""
    ymax = ymax or max(values) * 1.2
    W, H = 300, 190
    out = [_open((312, H + 8))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    x0, y0, x1 = 34, 26, 292
    y1 = H - 26
    out.append('<g stroke="%s" stroke-width="1.1">' % INK)
    out.append('<path d="M%d %d V%d H%d"/>' % (x0, y0, y1, x1))
    out.append("</g>")
    bw = (x1 - x0) / len(cats)
    for i, (c, v) in enumerate(zip(cats, values)):
        h = (y1 - y0) * v / ymax
        x = x0 + i * bw + bw * 0.18
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
                   'fill-opacity=".8" stroke="%s" stroke-width=".8"/>'
                   % (x, y1 - h, bw * 0.64, h, GOLD, INK))
        out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" text-anchor="middle">%s</text>'
                   % (x + bw * 0.32, y1 - h - 4, INK, _num(v)))
        out.append('<text x="%.1f" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="8.5" text-anchor="middle">%s</text>'
                   % (x + bw * 0.32, y1 + 13, INK, c))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" '
               'font-size="8.5" text-anchor="end">0</text>' % (x0 - 4, y1 + 3, INK))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" '
               'font-size="8.5" text-anchor="end">%s</text>' % (x0 - 4, y0 + 3, INK, _num(ymax)))
    out.append("</svg>")
    return "".join(out)


def box_plot(lo, q1, med, q3, hi, title=""):
    """A box plot on a simple scale."""
    x0, x1, y = 30, 290, 60
    span = hi - lo + 2
    def X(v):
        return x0 + (v - lo + 1) * (x1 - x0) / span
    out = [_open((312, 110))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    out.append('<path d="M%d %d H%d" stroke="%s" stroke-width="1.2"/>' % (x0, y, x1, INK))
    for v, lab in ((lo, _num(lo)), (q1, _num(q1)), (med, _num(med)), (q3, _num(q3)), (hi, _num(hi))):
        out.append('<path d="M%.1f %dv6" stroke="%s" stroke-width="1"/>' % (X(v), y - 3, INK))
        out.append('<text x="%.1f" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" text-anchor="middle">%s</text>' % (X(v), y + 19, INK, lab))
    out.append('<rect x="%.1f" y="%d" width="%.1f" height="22" fill="%s" fill-opacity=".25" '
               'stroke="%s" stroke-width="1.3"/>' % (X(q1), y - 11, X(q3) - X(q1), GOLD, INK))
    out.append('<path d="M%.1f %dV22" stroke="%s" stroke-width="1.6"/>' % (X(med), y - 11, RUST))
    out.append('<path d="M%.1f %d H%.1f M%.1f %d H%.1f" stroke="%s" stroke-width="1.2"/>'
               % (X(lo), y, X(q1), X(q3), y, X(hi), INK))
    out.append("</svg>")
    return "".join(out)


def tree(levels, probs, title=""):
    """A probability tree; levels is a list of branch-label lists.

    A branch probability is written above its own branch, clear of the outcome
    labels of the level before it, so the two can never print on top of one
    another when an outcome label is long.
    """
    step = 90
    xs = [40 + i * step for i in range(len(levels))]
    out = [_open((xs[-1] + step + 66, 60 + 44 * len(levels)))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    out.append('<circle cx="%d" cy="%d" r="3" fill="%s"/>' % (xs[0], 40, INK))
    for li, labels in enumerate(levels):
        for bi, lab in enumerate(labels):
            y = 44 + (bi + 0.5) * (44 * len(levels)) / len(labels)
            x2 = xs[li] + step
            out.append('<path d="M%d %d L%d %.1f" stroke="%s" stroke-width="1"/>'
                       % (xs[li], 40, x2, y, INK))
            p = probs[li][bi] if li < len(probs) and bi < len(probs[li]) else ""
            out.append('<text x="%d" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="9">%s</text>'
                       % (xs[li] + int(0.72 * step), 40 + 0.72 * (y - 40) - 8, INK, p))
            out.append('<text x="%d" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="9">%s</text>' % (x2 + 8, y + 3, INK, lab))
    out.append("</svg>")
    return "".join(out)


def scale_drawing(real, scale, shape="rectangle", title=""):
    """A scale drawing frame with a stated scale."""
    out = [_open((312, 170))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    w, h = 200, 100
    out.append('<rect x="56" y="34" width="%d" height="%d" fill="rgba(215,165,93,.14)" '
               'stroke="%s" stroke-width="1.3"/>' % (w, h, INK))
    out.append('<path d="M56 34 L76 20 L%d 20 L%d 34" stroke="%s" stroke-width=".8" '
               'fill="none"/>' % (76 + w, 76 + w, LINE))
    out.append('<path d="M%d 34 L%d 20" stroke="%s" stroke-width=".8" fill="none"/>'
               % (56 + w, 76 + w, LINE))
    out.append('<text x="%d" y="150" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10" text-anchor="middle">%s</text>' % (56 + w / 2, INK, real[0]))
    out.append('<text x="40" y="%d" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10" text-anchor="middle" transform="rotate(-90 40 %d)">%s</text>'
               % (34 + h / 2, INK, 34 + h / 2, real[1]))
    out.append('<text x="200" y="26" fill="%s" font-family="Inter, sans-serif" '
               'font-size="9.5">Scale %s</text>' % (RUST, scale))
    out.append("</svg>")
    return "".join(out)


def angle_diagram(kind="triangle_sum", values=(), title=""):
    """Angle diagrams: triangle sum, parallel lines, or polygon."""
    out = [_open((312, 170))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    if kind == "triangle_sum":
        out.append('<polygon points="70,140 240,140 150,40" fill="rgba(215,165,93,.14)" '
                   'stroke="%s" stroke-width="1.4"/>' % GOLD)
        for (x, y, t) in ((96, 132, values[0] if len(values) > 0 else ""),
                          (206, 132, values[1] if len(values) > 1 else ""),
                          (150, 62, values[2] if len(values) > 2 else "")):
            out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="11">%s</text>' % (x, y, RUST, t))
    elif kind == "parallel":
        out.append('<g stroke="%s" stroke-width="1.3" fill="none">' % INK)
        out.append('<path d="M40 50 H272 M40 130 H272"/>')
        out.append('<path d="M120 20 L200 160"/>')
        out.append("</g>")
        for (x, y, t) in ((128, 44, values[0] if len(values) > 0 else ""),
                          (176, 44, values[1] if len(values) > 1 else ""),
                          (128, 124, values[2] if len(values) > 2 else "")):
            out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" '
                       'font-size="11">%s</text>' % (x, y, RUST, t))
    else:  # polygon
        n = values[0] if values else 5
        import math
        cx, cy, r = 156, 100, 62
        pts = [(cx + r * math.cos(-90 + i * 360 / n), cy + r * math.sin(-90 + i * 360 / n))
               for i in range(n)]
        out.append('<polygon points="%s" fill="rgba(215,165,93,.14)" stroke="%s" '
                   'stroke-width="1.4"/>' % (" ".join("%.1f,%.1f" % p for p in pts), GOLD))
        out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="11" text-anchor="middle">%s</text>' % (cx, cy + 5, INK, "%d sides" % n))
    out.append("</svg>")
    return "".join(out)


# ---------------------------------------------------------------- MYP 3 additions
def scatter(points=(), xlabel="x", ylabel="y", xmin=0, xmax=10, ymin=0, ymax=10,
            line=None, title=""):
    """A scatter plot for bivariate data, with an optional line of best fit."""
    W, H = 300, 210
    top = 34 if title else 20
    bot = H + (30 if title else 6)
    out = [_open((312, bot))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    ox, oy = 42, bot - 22
    sx, sy = (W - 62) / (xmax - xmin), (bot - top - 26) / (ymax - ymin)

    def X(v):
        return ox + (v - xmin) * sx

    def Y(v):
        return oy - (v - ymin) * sy
    out.append('<g stroke="%s" stroke-width=".5" opacity=".55">' % LINE)
    for i in range(int(xmin), int(xmax) + 1):
        out.append('<path d="M%.1f %d V%.1f"/>' % (X(i), top, Y(ymin)))
    for i in range(int(ymin), int(ymax) + 1):
        out.append('<path d="M%d %.1f H%d"/>' % (X(xmin), Y(i), X(xmax)))
    out.append("</g>")
    out.append('<g stroke="%s" stroke-width="1.3">' % INK)
    out.append('<path d="M%d %.1f H%d"/>' % (X(xmin), Y(0), X(xmax) + 8))
    out.append('<path d="M%.1f %.1f V%.1f"/>' % (X(0), Y(ymin), Y(ymax) - 8))
    out.append("</g>")
    if line:
        (x1, y1), (x2, y2) = line
        out.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1.2" '
                   'stroke-dasharray="5 3"/>' % (X(x1), Y(y1), X(x2), Y(y2), RUST))
    for p in points:
        out.append('<circle cx="%.1f" cy="%.1f" r="3.1" fill="%s"/>' % (X(p[0]), Y(p[1]), GOLD))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" font-size="9">%s</text>'
               % (X(xmax) + 4, Y(0) + 14, INK, xlabel))
    out.append('<text x="%d" y="%d" fill="%s" font-family="Inter, sans-serif" font-size="9">%s</text>'
               % (X(0) + 6, Y(ymax) - 12, INK, ylabel))
    out.append("</svg>")
    return "".join(out)


def function_machine(pairs, rule, title=""):
    """A function machine: inputs on the left, the rule in the box, outputs right."""
    out = [_open((312, 120))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    out.append('<rect x="104" y="34" width="104" height="46" rx="6" stroke="%s" '
               'stroke-width="1.3" fill="rgba(215,165,93,.14)"/>' % INK)
    out.append('<text x="156" y="62" fill="%s" font-family="Inter, sans-serif" font-size="13" '
               'text-anchor="middle">%s</text>' % (INK, rule))
    for i, (a, b) in enumerate(pairs):
        y = 40 + i * 26
        out.append('<text x="30" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="12" text-anchor="middle">%s</text>' % (y + 5, INK, _num(a)))
        out.append('<path d="M46 %d H100" stroke="%s" stroke-width="1"/>' % (y + 5, LINE))
        out.append('<path d="M212 %d H268" stroke="%s" stroke-width="1"/>' % (y + 5, LINE))
        out.append('<text x="284" y="%d" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="12" text-anchor="middle">%s</text>' % (y + 5, GREEN, _num(b)))
    out.append("</svg>")
    return "".join(out)


def surd_spiral(steps=6, title=""):
    """The spiral of right triangles built from unit legs and hypotenuse √n."""
    import math
    out = [_open((312, 250))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    cx, cy, u = 70, 200, 34.0
    x, y, ang = cx, cy, 0.0
    pts = [(x, y)]
    for n in range(1, steps + 1):
        ang += math.radians(90.0 / n) if n > 1 else math.radians(90)
        nx, ny = x + u * math.cos(ang), y - u * math.sin(ang)
        out.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1.2"/>'
                   % (x, y, nx, ny, INK))
        out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9">%s</text>' % ((x + nx) / 2 + 4, (y + ny) / 2 + 4, RUST,
                                                "\u221a%d" % n))
        x, y = nx, ny
        pts.append((x, y))
    out.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1" '
               'stroke-dasharray="4 3"/>' % (cx, cy, x, y, LINE))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="9">hypotenuse \u221a%d</text>' % (x + 6, y + 4, LINE, steps))
    out.append("</svg>")
    return "".join(out)


def pythagoras(a=3, b=4, title=""):
    """A right-angled triangle with squares on each side, for Pythagoras' theorem."""
    W, H = 312, 220
    out = [_open((W, H))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    u = 26.0
    ax, ay = 60.0, 190.0
    bx, by = ax + a * u, ay
    cx, cy = ax, ay - b * u
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(215,165,93,.16)" '
               'stroke="%s" stroke-width="1.1"/>' % (ax, cy - a * u, a * u, a * u, GOLD))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(180,79,50,.12)" '
               'stroke="%s" stroke-width="1.1"/>' % (bx, by - b * u, b * u, b * u, RUST))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(13,42,40,.10)" '
               'stroke="%s" stroke-width="1.1" transform="rotate(-%f %.1f %.1f)"/>'
               % (bx - 0, by - b * u, (a * a + b * b) ** .5 * u, (a * a + b * b) ** .5 * u,
                  GREEN, 90 - math_deg(a, b), bx, by))
    out.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="rgba(215,165,93,.30)" '
               'stroke="%s" stroke-width="1.4"/>' % (ax, ay, bx, by, cx, cy, GOLD))
    out.append('<path d="M%.1f %.1f h12 v12 h-12 Z" stroke="%s" stroke-width="1" fill="none"/>'
               % (bx - 12, by - 12, INK))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="11" text-anchor="middle">%s</text>' % ((ax + bx) / 2, ay + 16, INK, _num(a)))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="11" text-anchor="middle">%s</text>' % (ax - 14, (ay + cy) / 2, INK, _num(b)))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="11" text-anchor="middle">%s</text>'
               % ((bx + cx) / 2 + 22, (by + cy) / 2, GREEN, "\u221a%d" % (a * a + b * b)))
    out.append("</svg>")
    return "".join(out)


def math_deg(a, b):
    import math
    return math.degrees(math.atan2(b, a))


def elevation(angle=35, dist=6, title=""):
    """A right-angled triangle showing an angle of elevation from the horizontal."""
    W, H = 312, 180
    out = [_open((W, H))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    import math
    u = 30.0
    ax, ay = 40.0, 150.0
    bx = ax + dist * u
    h = dist * u * math.tan(math.radians(angle))
    cy = ay - h
    out.append('<path d="M%d %.1f H%d" stroke="%s" stroke-width="1" stroke-dasharray="5 3"/>'
               % (ax - 16, ay, bx + 40, LINE))
    out.append('<path d="M%.1f %.1f H%.1f" stroke="%s" stroke-width="1.2"/>' % (ax, ay, bx, INK))
    out.append('<path d="M%.1f %.1f V%.1f" stroke="%s" stroke-width="1.2"/>' % (bx, ay, cy, INK))
    out.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="1.4"/>'
               % (ax, ay, bx, cy, GOLD))
    out.append('<path d="M%.1f %.1f A34 34 0 0 0 %.1f %.1f" stroke="%s" stroke-width="1" '
               'fill="none"/>' % (ax + 34, ay, ax + 34 * math.cos(math.radians(angle)),
                                  ay - 34 * math.sin(math.radians(angle)), RUST))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="11">%d°</text>' % (ax + 40, ay - 8, RUST, angle))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10" text-anchor="middle">%s m</text>'
               % ((ax + bx) / 2, ay + 16, INK, _num(dist)))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10" text-anchor="middle">h</text>' % (bx + 12, (ay + cy) / 2, GREEN))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10">eye</text>' % (ax - 34, ay + 14, LINE))
    out.append("</svg>")
    return "".join(out)


def cone(r=3, h=5, title=""):
    """A cone with its radius, height and slant height marked."""
    out = [_open((312, 200))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    cx, cy, rx, ry = 150.0, 158.0, 58.0, 16.0
    out.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="rgba(215,165,93,.16)" '
               'stroke="%s" stroke-width="1.3"/>' % (cx, cy, rx, ry, INK))
    out.append('<path d="M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f" stroke="%s" '
               'stroke-width="1.3" fill="none"/>'
               % (cx - rx, cy, cx, cy - 96, cx + rx, cy, cx, cy - 96, INK))
    out.append('<path d="M%.1f %.1f A%.1f %.1f 0 0 0 %.1f %.1f" stroke="%s" stroke-width=".8" '
               'stroke-dasharray="4 3" fill="none"/>' % (cx - rx, cy, rx, ry, cx + rx, cy, LINE))
    out.append('<path d="M%.1f %.1f V%.1f" stroke="%s" stroke-width=".8" stroke-dasharray="4 3"/>'
               % (cx, cy, cy - 96, LINE))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10" text-anchor="middle">r = %s</text>' % (cx, cy + 26, INK, _num(r)))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10">h = %s</text>' % (cx + 8, cy - 48, GREEN, _num(h)))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10">l</text>' % (cx + 24, cy - 74, RUST))
    out.append("</svg>")
    return "".join(out)


def sphere(r=3, title=""):
    """A sphere with its radius marked."""
    out = [_open((312, 190))]
    if title:
        out.append('<text x="6" y="12" fill="%s" font-family="Inter, sans-serif" '
                   'font-size="9" letter-spacing=".6">%s</text>' % (LINE, title))
    cx, cy, rr = 150.0, 100.0, 58.0
    out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="rgba(215,165,93,.16)" stroke="%s" '
               'stroke-width="1.3"/>' % (cx, cy, rr, INK))
    out.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="18" stroke="%s" stroke-width=".8" '
               'stroke-dasharray="4 3" fill="none"/>' % (cx, cy, rr, LINE))
    out.append('<path d="M%.1f %.1f H%.1f" stroke="%s" stroke-width="1.2"/>'
               % (cx, cy, cx + rr, RUST))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-family="Inter, sans-serif" '
               'font-size="10">r = %s</text>' % (cx + 20, cy - 6, INK, _num(r)))
    out.append("</svg>")
    return "".join(out)


FIGS = {
    "number_line": number_line, "double_number_line": double_number_line,
    "tiles": tiles, "staircase": staircase,
    "table": table, "bar_model": bar_model, "grid": grid, "venn": venn,
    "triangle": triangle, "prism": prism, "transform": transform, "pie": pie,
    "bar_chart": bar_chart, "box_plot": box_plot, "tree": tree,
    "scale_drawing": scale_drawing, "angle_diagram": angle_diagram,
    "scatter": scatter, "function_machine": function_machine, "surd_spiral": surd_spiral,
    "pythagoras": pythagoras, "elevation": elevation, "cone": cone, "sphere": sphere,
}


def fig(name, *args, **kwargs):
    """Render a diagram by name, e.g. fig('number_line', 0, 3, 1, [1])."""
    return _superscripts(FIGS[name](*args, **kwargs))


