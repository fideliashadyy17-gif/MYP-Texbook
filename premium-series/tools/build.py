"""Compile the chapter proof and verify basic PDF invariants."""
from itertools import permutations
from math import gcd, lcm
from pathlib import Path

import pymupdf
import typst

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = 'SADIKOU MOUKODDIM'


def build(level, slug, filename, expected_pages, minimum_text):
    volume = ROOT / f'myp{level}'
    source = volume / f'{slug}.typ'
    output = volume / 'output' / filename
    output.parent.mkdir(exist_ok=True)
    typst.compile(str(source), root=str(ROOT), output=str(output))
    with pymupdf.open(output) as pdf:
        assert len(pdf) == expected_pages, output
        assert pdf.metadata['author'] == AUTHOR
        for page in pdf:
            assert abs(page.rect.width - 595.28) < 0.1
            assert abs(page.rect.height - 841.89) < 0.1
            assert len(page.get_text().strip()) >= minimum_text
            for x0, y0, x1, y1, *_ in page.get_text('blocks'):
                assert page.rect.contains(pymupdf.Rect(x0, y0, x1, y1)), (output, page.number + 1)
        if slug == 'personal-pages':
            for page, title in zip(pdf, ('Dedication', 'Acknowledgements', 'About the Author'), strict=True):
                assert title in page.get_text()
            assert AUTHOR in pdf[2].get_text()
    print(f'Built and checked {output.relative_to(ROOT)}')


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
# Chapter 2 proof: verify the finite searches and the storage decision.

assert {(b, e) for b in range(2, 9) for e in range(2, 7) if b**e == 64} == {(2, 6), (4, 3), (8, 2)}
assert 2**6 < 3**4 < 2**7
numbers = [int(''.join(p)) for p in permutations('0246') if p[0] != '0']
assert (min(numbers), max(numbers), max(numbers)-min(numbers)) == (2046, 6420, 4374)
assert min(set(n*n for n in range(2, 9)) & set(n**3 for n in range(2, 5))) == 64
assert {(d, 18//d - 2) for d in range(2, 19) if 18 % d == 0 and 18//d-2 > 1 and d != 18//d-2} == {(2, 7), (3, 4)}
assert {2+3*4-1, (2+3)*4-1, 2+(3*4)-1, 2+3*(4-1), (2+3*4)-1, 2+(3*4-1)} == {11, 13, 19}
assert sum((n+1)**2-n**2 for n in range(1, 12, 2)) == 78
storage = [(60-k)*(400**2+200)+k*(600**2+200) for k in range(61)]
assert (storage[0], storage[-1], storage[51], storage[52]) == (9612000, 21612000, 19812000, 20012000)
assert max(k for k, size in enumerate(storage) if size <= 2*10**7) == 51

# Chapter 3 proof: independent bounded searches and timeline checks.
assert [d for d in range(10) if (470 + d) % 6 == 0] == [4]
assert (234 % 8, 432 % 8) == (2, 0)
assert min(int(''.join(p)) for p in permutations('1236') if int(''.join(p)) % 4 == 0) == 1236
assert [n for n in range(3500, 3600) if n % 45 == 0] == [3510, 3555]
assert [(a, b) for a in range(1, 73) for b in range(a, 73)
        if gcd(a, b) == 6 and lcm(a, b) == 72] == [(6, 72), (18, 24)]
assert gcd(96, 72, 60) == 12
assert lcm(8, 12) + 4 == 28
assert [k for k in range(8, 12) if lcm(8, k) + 4 <= 25] == [8]

if __name__ == '__main__':
    for n in (1, 2, 3):
        build(1, f'chapter-{n:02d}', f'MYP1-Chapter-{n:02d}-Proof.pdf', 7, 200)
    for n in range(1, 6):
        build(n, 'personal-pages', f'MYP{n}-Personal-Pages-Proof.pdf', 3, 80)
