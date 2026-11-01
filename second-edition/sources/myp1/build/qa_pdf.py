#!/usr/bin/env python3
"""Post-export QA for MYP1 chapter PDFs. Requires PyMuPDF and Pillow."""
import json, re, sys
from pathlib import Path
import pymupdf
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT.parents[1] / 'exports' / 'myp1'
QA = ROOT.parents[1] / 'qa' / 'myp1'

def check(chapter=1):
    pdf_path = EXPORTS / f'MYP1-Chapter-{chapter:02d}-Revision-Proof.pdf'
    data = json.loads((ROOT / 'data' / f'chapter-{chapter:02d}.exercises.json').read_text())
    doc = pymupdf.open(pdf_path)
    report = {'file': str(pdf_path), 'pages': len(doc), 'page_sizes': [], 'fonts': {}, 'issues': [], 'text_lengths': []}
    all_text = ''
    font_xrefs = set()
    for i, page in enumerate(doc):
        r = page.rect
        report['page_sizes'].append([round(r.width, 2), round(r.height, 2)])
        text = page.get_text()
        all_text += text + '\n'
        report['text_lengths'].append(len(text))
        if len(text.strip()) < 20:
            report['issues'].append(f'Page {i+1} has very little text ({len(text.strip())} chars)')
        for f in page.get_fonts(full=True):
            font_xrefs.add(f[0])
    for xref in sorted(font_xrefs):
        try:
            name, ext, ftype, content = doc.extract_font(xref)
            report['fonts'][name] = {'type': ftype, 'ext': ext, 'embedded': bool(content), 'bytes': len(content or b'')}
            if not content:
                report['issues'].append(f'Font not embedded: {name}')
        except Exception as e:
            report['issues'].append(f'Font extraction failed for xref {xref}: {e}')
    if re.search(r'\{\{[^}]+\}\}', all_text):
        report['issues'].append('Raw placeholder found in PDF text')
    if re.search(r'\\(?:frac|times|div|sqrt|left|right)\b', all_text):
        report['issues'].append('Raw LaTeX command found in PDF text')
    # Every exercise id should appear at least twice: question and answer.
    missing = []
    for g in data['groups']:
        for q in g['items']:
            if all_text.count(q['id']) < 2:
                missing.append(q['id'])
    report['exercise_ids_missing_or_unpaired'] = missing
    if missing:
        report['issues'].append(f'Exercise ids not found as question+answer pairs: {missing}')
    # Render pages for visual inspection.
    render_dir = QA / 'renders' / f'chapter-{chapter:02d}'
    render_dir.mkdir(parents=True, exist_ok=True)
    for old in render_dir.glob('page-*.png'):
        old.unlink()
    for old in QA.glob(f'chapter-{chapter:02d}-contact-*.png'):
        old.unlink()
    thumbs = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=110)
        out = render_dir / f'page-{i+1:02d}.png'
        pix.save(out)
        im = Image.open(out).convert('RGB')
        im.thumbnail((240, 340))
        thumbs.append(im)
    # Contact sheets, 8 pages per sheet.
    for start in range(0, len(thumbs), 8):
        batch = thumbs[start:start+8]
        cols, rows = 4, 2
        sheet = Image.new('RGB', (cols*250, rows*360), 'white')
        draw = ImageDraw.Draw(sheet)
        for j, im in enumerate(batch):
            x, y = (j % cols)*250+5, (j//cols)*360+15
            sheet.paste(im, (x, y))
            draw.text((x, y-12), f'p.{start+j+1}', fill='black')
        sheet.save(QA / 'renders' / f'chapter-{chapter:02d}-contact-{start//8+1}.png')
    report['status'] = 'PASS' if not report['issues'] else 'FAIL'
    QA.mkdir(parents=True, exist_ok=True)
    out = QA / f'chapter-{chapter:02d}-pdf-qa.json'
    out.write_text(json.dumps(report, indent=2))
    print(json.dumps({k: report[k] for k in ['file','pages','status','issues','exercise_ids_missing_or_unpaired']}, indent=2))
    print(f'Fonts: {len(report["fonts"])}; renders: {render_dir}')
    return 0 if report['status'] == 'PASS' else 1

if __name__ == '__main__':
    sys.exit(check(int(sys.argv[1]) if len(sys.argv) > 1 else 1))
