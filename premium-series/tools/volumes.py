"""Assemble all five editorial volumes from editable Typst sources.

The release check is deliberately independent of PDF compilation. It reports
missing content and signed-off evidence; it never issues a final PDF itself.
"""
from pathlib import Path
import argparse
import re

import pymupdf
import typst

ROOT = Path(__file__).resolve().parents[1]
COUNTS = {1: 10, 2: 11, 3: 10, 4: 13, 5: 12}
REVIEW_NAMES = ('mathematical', 'visual-editorial', 'curriculum-alignment', 'print-layout')


def draft_source(level, chapters):
    sections = '\n#pagebreak()\n'.join(f'#include "chapter-{n:02d}.typ"' for n in chapters)
    missing = [str(n) for n in range(1, COUNTS[level]+1) if n not in chapters]
    return f'''#import "../shared/volume.typ": cover
#import "../shared/personal-pages.typ": author
#set document(title: "MYP{level} Mathematics Student Coursebook · Editorial assembly", author: author)
#cover({level})
#pagebreak()
= Editorial assembly — not for distribution
This working PDF shows only the mathematics chapters currently available.
Missing chapter numbers: {', '.join(missing) or 'none'}.
A successful build is not mathematical, curriculum or print sign-off.
#outline(title: [Contents], depth: 1)
#pagebreak()
#include "personal-pages.typ"
#pagebreak()
{sections + chr(10) + '#pagebreak()' if sections else ''}
#cover({level}, back: true)
'''


def check(level, directory, chapters):
    missing = [str(n) for n in range(1, COUNTS[level]+1) if n not in chapters]
    reports = [name for name in REVIEW_NAMES if not (directory / 'qa' / f'{name}.md').is_file()]
    print(f'MYP{level}: {len(chapters)}/{COUNTS[level]} chapter sources. '
          f'Missing chapters: {", ".join(missing) or "none"}. '
          f'Missing volume reports: {", ".join(reports) or "none"}.')
    return not missing and not reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='check all five release prerequisites without building')
    args = parser.parse_args()
    statuses = []
    for level in COUNTS:
        directory = ROOT / f'myp{level}'
        chapters = sorted(int(re.fullmatch(r'chapter-(\d\d)\.typ', path.name)[1])
                          for path in directory.glob('chapter-[0-9][0-9].typ'))
        if not set(chapters).issubset(range(1, COUNTS[level]+1)):
            raise ValueError(f'Unexpected chapter number in MYP{level}: {chapters}')
        statuses.append(check(level, directory, chapters))
        if args.check:
            continue
        source = directory / 'editorial-volume.typ'
        source.write_text(draft_source(level, chapters), encoding='utf8')
        output = directory / 'output' / f'MYP{level}-Editorial-Assembly.pdf'
        output.parent.mkdir(exist_ok=True)
        typst.compile(str(source), root=str(ROOT), output=str(output))
        with pymupdf.open(output) as pdf:
            assert pdf.metadata['author'] == 'SADIKOU MOUKODDIM'
            assert all(abs(p.rect.width-595.28) < .1 and abs(p.rect.height-841.89) < .1 for p in pdf)
            print(f'  Built {len(pdf)} A4 pages: {output.relative_to(ROOT)}')
    if args.check and not all(statuses):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
