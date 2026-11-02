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
    manifest_path = ROOT / 'tools' / '.generated' / f'chapter-{chapter:02d}.manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    answer_start = int(manifest.get('answerStartPage', len(doc) + 1))
    report = {'file': str(pdf_path), 'pages': len(doc), 'expected_pages': manifest.get('expectedPages'), 'answer_start_page': answer_start, 'page_sizes': [], 'fonts': {}, 'issues': [], 'text_lengths': []}
    if report['expected_pages'] is not None and len(doc) != report['expected_pages']:
        report['issues'].append(f'PDF page count {len(doc)} does not match expected {report["expected_pages"]}')
    all_text = ''
    question_text = ''
    answer_text = ''
    font_xrefs = set()
    for i, page in enumerate(doc):
        r = page.rect
        report['page_sizes'].append([round(r.width, 2), round(r.height, 2)])
        if abs(r.width - 595.28) > 1.5 or abs(r.height - 841.89) > 1.5:
            report['issues'].append(f'Page {i+1} is not A4: {r.width} x {r.height}')
        text = page.get_text()
        all_text += text + '\n'
        if i + 1 < answer_start:
            question_text += text + '\n'
        else:
            answer_text += text + '\n'
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
    # Every exercise id should appear in the question pages and in the answer pages.
    # Use boundaries so M1 is not counted inside M10, or 2.1.1 inside 2.1.10.
    missing_questions, missing_answers = [], []
    for g in data['groups']:
        for q in g['items']:
            pat = re.compile(r'(?<![A-Za-z0-9.])' + re.escape(q['id']) + r'(?![A-Za-z0-9])')
            if not pat.search(question_text):
                missing_questions.append(q['id'])
            if not pat.search(answer_text):
                missing_answers.append(q['id'])
    report['missing_question_ids'] = missing_questions
    report['missing_answer_ids'] = missing_answers
    report['exercise_ids_missing_or_unpaired'] = sorted(set(missing_questions) | set(missing_answers))
    if missing_questions:
        report['issues'].append(f'Exercise ids missing from question pages: {missing_questions}')
    if missing_answers:
        report['issues'].append(f'Exercise ids missing from answer pages: {missing_answers}')
    # Render pages for visual inspection.
    render_dir = QA / 'renders' / f'chapter-{chapter:02d}'
    render_dir.mkdir(parents=True, exist_ok=True)
    for old in render_dir.glob('page-*.png'):
        old.unlink()
    for old in (QA / 'renders').glob(f'chapter-{chapter:02d}-contact-*.png'):
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
