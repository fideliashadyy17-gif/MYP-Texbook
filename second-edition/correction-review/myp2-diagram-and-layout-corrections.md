# MYP 2 — diagram and layout corrections carried over from the MYP 3 pass

The MYP 3 assembly surfaced four defects in `diagrams2.py` and the shared
stylesheet that also affect the delivered MYP 2 book. They are fixed here in the
MYP 2 pipeline and the book is rebuilt. The chapter content, the page model, the
teaching sequence and the approved MYP 1 prototype are untouched.

**Deliverable:** `second-edition/exports/myp2/MYP2-Student-Coursebook-Second-Edition.pdf`
**Rebuilt:** 2026-11-02 · pipeline `second-edition/sources/myp2/fullbook/` · QA
`second-edition/qa/myp2/fullbook/`

## Measured result after the corrections

| measure | before | after |
| --- | --- | --- |
| pages | 422 | **422** (unchanged) |
| file size | 3 342 568 bytes | **3 352 025 bytes** |
| spans bleeding past a page margin | 20 | **0** |
| overlapping text spans | 7 | **0** |
| missing glyphs | 0 | **0** |
| overflow / placeholders / raw maths / KaTeX errors / console errors | 0 | **0** |
| mechanical QA | PASS | **PASS** |

Pagination is unchanged: every chapter starts on the page it started on before,
so the contents, the answer section and every cross-reference still hold.

## 1. Coordinate grids were drawn off-canvas

`diagrams2.grid` centred the plot on zero rather than on the middle of the
requested range. For any window that is not symmetric about the origin — which
is most of them — the top and the right of the grid fell outside the viewBox and
were silently clipped. **Eleven of the fourteen MYP 2 grid diagrams were
affected**, including *Squares on a grid*, *A linear sequence*, *Linear against
quadratic*, *A 12 cm by 7 cm rectangle*, *Outcomes with total 7* and *Even
numbers and numbers above 4*. Roughly a third of each of those grids was
missing from the printed page.

The plot is now centred on the midpoint of the requested range:

```python
hmid, vmid = (xmin + xmax) / 2.0, (ymin + ymax) / 2.0
ox, oy = W / 2, (top + bot) / 2.0

def X(v): return ox + (v - hmid) * sx
def Y(v): return oy - (v - vmid) * sy
```

## 2. Diagram titles collided with axis labels

`grid` drew the title at the top-left and the y-axis label at the top of the
y-axis in the same horizontal band, so a long title printed on top of the axis
label. The title now sits in its own band above the plot. The titled canvas is
no taller than it was before, so no page grew.

## 3. Tree branch probabilities collided with outcome labels

`tree` wrote a level-2 branch probability exactly where the level-1 outcome
label already was, so the two printed on top of one another. Probabilities now
sit above their own branch, clear of the previous level's labels.

## 4. SVG table cells did not wrap

`table` placed each cell as a single `<text>` element, so long cell text ran
over the neighbouring column. A right-edge scan of the PDF does not catch this,
because the SVG is centred in its column and the overflow happens inside the
drawing. Cells now wrap to the column width and the row height grows to fit,
with tighter rows above eight rows so that a long table still reads at the size
the page allows. One investigation table header (*"measured perimeter"* /
*"calculated perimeter"*) was shortened to *"measured"* / *"calculated"*, which
the task text already makes unambiguous.

## 5. Assessment footer notes printed at the page foot

`.footer-note` was absolutely positioned against the `.page` element, so the
criteria note of every assessment task was drawn at x = 0, below the page
footer, on top of the other notes on the page — an unreadable smear at the foot
of all eleven assessment pages. It is now static, inside its own task box, with
the rule above it.

## Renders

`second-edition/qa/myp2/fullbook/renders/` is refreshed: the original 95 pages
(chapter covers, every investigation, every Criterion A–D practice page, every
chapter reflection) re-rendered, plus the front cover, imprint, contents, the
eleven assessment pages the footer-note fix changed, the answers, formula bank,
glossary, references and back cover — **114 pages** at 110 dpi.
