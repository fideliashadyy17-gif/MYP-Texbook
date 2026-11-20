"""Record the fourteen tracked root PDFs without reading rejected-edition content."""
import hashlib
import json
from pathlib import Path
import subprocess

import pymupdf

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parent
files = subprocess.check_output(['git', 'ls-files', '-z', '--', '*.pdf'], cwd=REPO).decode().split('\0')
records = []
for name in sorted(p for p in files if p.endswith('.pdf') and '/' not in p):
    data = (REPO / name).read_bytes()
    with pymupdf.open(stream=data, filetype='pdf') as pdf:
        records.append(dict(path=name, role='first-edition' if 'Coursebook' in name else 'exercise-reference',
                            pages=len(pdf), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                            creator=pdf.metadata.get('creator'), outline_entries=len(pdf.get_toc())))
print(json.dumps(records, ensure_ascii=False, indent=2))
