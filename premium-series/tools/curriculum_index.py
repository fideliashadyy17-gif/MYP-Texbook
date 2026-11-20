"""Extract first-edition contents anchors, not rejected-edition material."""
import json
from pathlib import Path
import re

import pymupdf

PROJECT = Path(__file__).resolve().parents[1]
SOURCES = sorted((r['path'] for r in json.loads((PROJECT / 'docs/source-inventory.json').read_text())
                  if r['role'] == 'first-edition'))
EXPECTED = [10, 11, 10, 13, 12]


def sections(pdf, level):
    contents_pages = {1: (4, 6), 2: (5, 8), 3: (4, 6), 4: (5, 7), 5: (5, 7)}
    first, last = contents_pages[level]
    pages = range(first - 1, last)
    for i in pages:
        lines = [s.strip() for s in pdf[i].get_text().splitlines() if s.strip()]
        if level < 4:
            for j, line in enumerate(lines[:-1]):
                match = re.fullmatch(r'(\d+\.\d+)\s+(.+)', line)
                if match and lines[j+1].isdigit():
                    yield match[1], match[2], int(lines[j+1]), i+1
        else:
            for j, line in enumerate(lines):
                if re.fullmatch(r'\d+\.\d+', line):
                    end = j + 1
                    while end < len(lines) and not lines[end].isdigit():
                        end += 1
                    if end < len(lines):
                        yield line, ' '.join(lines[j+1:end]), int(lines[end]), i+1


def main():
    for level, name in enumerate(SOURCES, 1):
        with pymupdf.open(PROJECT.parent / name) as pdf:
            rows = list(sections(pdf, level))
        ids = [r[0] for r in rows]
        assert len(ids) == len(set(ids)), (level, ids)
        assert set(int(i.split('.')[0]) for i in ids) == set(range(1, EXPECTED[level-1]+1)), (level, ids)
        out = PROJECT / 'docs' / 'curriculum' / f'myp{level}.md'
        out.parent.mkdir(exist_ok=True)
        text = [f'# MYP{level} curriculum coverage register', '', f'First-edition source: `{name}`.', '',
                'Printed page numbers are the anchors from the original contents; PDF page numbers in the last column locate the contents entry itself. These anchors document source scope, not completed teaching material or a full editorial blueprint.', '']
        current = 0
        for id_, title, page, toc in rows:
            chapter = int(id_.split('.')[0])
            if chapter != current:
                current = chapter
                text += ([''] if current > 1 else []) + [f'## Chapter {chapter}', '', '| Section | Source topic | Printed page | Contents PDF page | Reconstruction |', '|---|---|---:|---:|---|']
            status = 'Chapter proof' if level == 1 and chapter <= 2 else 'Not drafted'
            text.append(f'| {id_} | {title.replace("|", "&#124;")} | {page} | {toc} | {status} |')
        out.write_text('\n'.join(text) + '\n')


if __name__ == '__main__':
    main()
