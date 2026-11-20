#!/usr/bin/env python3
"""Export the first-edition heading and enrichment audit as a readable CSV."""
import csv
import json
import re

import pymupdf as pdf

from build import HOME, ROOT, SOURCES, read_practice

FIELDS = ['year','chapter','chapter_title','section','original_heading','kind',
          'original_printed_start','original_printed_anchor','original_pdf_anchor',
          'original_worked_example_markers','original_practice_markers',
          'original_figure_markers','original_investigation_markers','original_application_markers',
          'decision','new_exercises','new_parts','criterion_focus','reference_lens','visuals','new_task_titles']
PATTERNS = {
    'original_worked_example_markers': r'(?:worked)?example\d+\.\d+',
    'original_practice_markers': r'guidedpractice|exercise(?:[0-9]+[a-z]|c\.[0-9]+)|practice\d+\.\d+',
    'original_figure_markers': r'figure(?:\d+|c)\.\d+',
    'original_investigation_markers': r'investigation',
    'original_application_markers': r'real-lifeapplication|modellingtask|modelling·criteriond|applicationandextension',
}


def main():
    inventory=json.loads((HOME/'source'/'inventory.json').read_text())
    with (HOME/'coverage.csv').open('w',encoding='utf-8',newline='') as csv_file:
        writer=csv.DictWriter(csv_file,fieldnames=FIELDS,lineterminator="\n")
        writer.writeheader()
        for y in range(1,6):
            spec=inventory[str(y)]; authored=read_practice(y)
            with pdf.open(ROOT/SOURCES[y][0]) as original:
                for row in spec['sections']:
                    sid=row['id']; ch=sid.split('.')[0]; page=row['start']
                    first=page+spec['offset']-1
                    # These text signatures are audit clues, not counts of unique tasks.
                    # A shared source page may also include a feature of the next section.
                    text=re.sub(r'\s+','', '\n'.join(original[i].get_text() for i in range(first,row['after']))).lower()
                    signals={k:len(re.findall(v,text)) for k,v in PATTERNS.items()}
                    tasks=authored.get(sid,{}).get('tasks',[])
                    if tasks:
                        why='Interleave new practice with original text retained'
                    elif row['kind']=='investigation':
                        why='Retain original open task or project brief; no near-duplicate'
                    else:
                        why='Retain original review or assessment and its existing tasks'
                    writer.writerow(dict(year=y,chapter=ch,chapter_title=spec['chapters'][ch]['title'],section=sid,
                        original_heading=row['title'],kind=row['kind'],original_printed_start=page,
                        original_printed_anchor=row['printed_anchor'],original_pdf_anchor=row['after'],
                        **signals, decision=why,new_exercises=len(tasks),new_parts=sum(len(t['parts']) for t in tasks),
                        criterion_focus='; '.join(t['criterion'] for t in tasks),
                        reference_lens='; '.join(authored.get(sid,{}).get('refs',[])),
                        visuals='; '.join(cmd for t in tasks for cmd,_ in t['visuals']),
                        new_task_titles='; '.join(t['title'] for t in tasks)))
    print('Wrote coverage.csv')


if __name__=='__main__':
    main()
