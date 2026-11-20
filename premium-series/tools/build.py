"""Compile the chapter proof and verify basic PDF invariants."""
from pathlib import Path

import pymupdf
import typst

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'myp1' / 'chapter-01.typ'
output = source.parent / 'output' / 'MYP1-Chapter-01-Proof.pdf'
output.parent.mkdir(exist_ok=True)
typst.compile(str(source), output=str(output))
with pymupdf.open(output) as pdf:
    assert len(pdf) == 7, 'Review pagination after changing the source'
    assert pdf.metadata['author'] == 'SADIKOU MOUKODDIM'
    for page in pdf:
        assert abs(page.rect.width - 595.28) < 0.1
        assert abs(page.rect.height - 841.89) < 0.1
        assert len(page.get_text().strip()) > 200
        for x0, y0, x1, y1, *_ in page.get_text('blocks'):
            assert page.rect.contains(pymupdf.Rect(x0, y0, x1, y1)), page.number + 1

# Check boundaries independently using integer arithmetic.
def rounded(n, unit):
    return ((2 * n + unit) // (2 * unit)) * unit

assert [n for n in range(6700, 6900) if rounded(n, 100) == 6800] == list(range(6750, 6850))
assert [n for n in range(2300, 2700) if rounded(n, 100) == 2500 and rounded(n, 1000) == 2000] == list(range(2450, 2500))
stock = [a + b for a in range(840, 860) for b in range(640, 660)
         if rounded(a, 10) == 850 and rounded(b, 10) == 650]
assert (min(stock), max(stock)) == (1490, 1508)
assert set(n // 15 for n in stock) == {99, 100}
assert min(stock) < 1500 <= min(stock) + 12
assert 1247 - 103 * 12 == 11
print(f'Built and checked {output.relative_to(ROOT)}')
