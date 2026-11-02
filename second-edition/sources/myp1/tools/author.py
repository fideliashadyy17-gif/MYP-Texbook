#!/usr/bin/env python3
"""Generate editable chapter sources from verified content plans (Chapters 3–10)."""
import json, sys, importlib.util
from pathlib import Path
TOOLS=Path(__file__).resolve().parent
ROOT=TOOLS.parent
sys.path.insert(0,str(TOOLS/'content'))

def load(n):
    p=TOOLS/'content'/f'chapter_{n:02d}.py'
    spec=importlib.util.spec_from_file_location(f'chapter_{n:02d}',p)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.PLAN

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def table(t):
    if not t: return ''
    return '<table><thead><tr>'+''.join(f'<th>{esc(h)}</th>' for h in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{esc(c)}</td>' for c in row)+'</tr>' for row in t['rows'])+'</tbody></table>'

def page(kicker,title,body,cls=''):
    return f'<section class="page {cls}"><div class="kicker">{esc(kicker)}</div><h2>{esc(title)}</h2>{body}</section>'

def render(p):
    ch=p['chapter']; out=[]
    out.append(f'''<section class="page cover"><div><div class="kicker">MYP Mathematics 1 · Second edition</div><div class="numeral">{ch:02d}</div><h1>{esc(p['title'])}</h1><p class="subtitle">{esc(p['part'])}</p></div><div class="edition">Revision proof · Editable source · {esc(p['context'])}</div></section>''')
    obj=''.join(f'<li>{esc(x)}</li>' for x in p['objectives'])
    voc=' · '.join(esc(x) for x in p['vocabulary'].split(' · '))
    out.append(page(f'Chapter {ch} · Opener',p['title'],f'''
<p class="standfirst">{esc(p['soi'])}</p>
<div class="callout"><div class="label">Engagement</div><p>{esc(p['engage'])}</p></div>
<div class="grid-2"><div class="card sand"><h3>Learning goals</h3><ul>{obj}</ul></div><div class="card pale"><h3>MYP lens</h3><p><strong>Key concept:</strong> {esc(p['key'])}</p><p><strong>Related concepts:</strong> {esc(p['related'])}</p><p><strong>Global context:</strong> {esc(p['context'])}</p></div></div>
<div class="atl"><strong>ATL focus.</strong> {esc(p['atl'])}</div>
<p class="small"><strong>Language bank:</strong> {voc}</p>''','opener'))
    secmap=''.join(f'<li><strong>{esc(s["number"])} {esc(s["title"])}</strong> — {esc(s["intent"])}</li>' for s in p['sections'])
    out.append(page(f'Chapter {ch} · Start here','Ready check and chapter map',f'''
<p class="lede">Use the ready check to find the ideas you already control. Then follow the chapter map from concrete examples to explanations and decisions.</p>
{{{{exercise:ready}}}}
<div class="card sand"><h3>Chapter map</h3><ol>{secmap}</ol></div>
<div class="callout blue"><div class="label">Explain how you know</div><p>For every answer, be ready to give a method, a diagram or a reason. A correct result without a check is only half an explanation.</p></div>'''))
    for s in p['sections']:
        fig=f'{{{{figure:{s["diagram"]["kind"]}-{ch}|{s["diagram"]["caption"]}}}}}' if s.get('diagram') else ''
        ex=s['example']; steps=''.join(f'<li>{esc(x)}</li>' for x in ex['steps'])
        paras=''.join(f'<p>{esc(x)}</p>' for x in s['paras'])
        out.append(page(f'Chapter {ch} · Mathematical development',f'{s["number"]} {s["title"]}',f'''
<div class="callout"><div class="label">Big idea</div><p>{esc(s['intent'])}</p></div>{paras}{fig}
<div class="example"><div class="example-title">Worked example · {esc(ex['title'])}</div><p>{esc(ex['problem'])}</p><ol class="steps">{steps}</ol><div class="answer">{esc(ex['answer'])}</div></div>'''))
        ids=[q['id'] for q in s['practice']]
        g='p'+s['number'].replace('.','')
        out.append(page(f'Chapter {ch} · Practice',f'{s["number"]} Guided and independent practice',f'''
<div class="callout rust"><div class="label">Watch for this misconception</div><p>{esc(s['warning'])}</p></div>
{{{{exercise:{g}:{','.join(ids[:3])}:Guided practice · first steps}}}}
<div class="workspace"></div>
{{{{exercise:{g}:{','.join(ids[3:])}:Independent practice · explain and apply}}}}
<p class="small muted">Check one answer with a different representation or an inverse operation. Record the check in your working.</p>'''))
    e=p['explore']
    out.append(page(f'Chapter {ch} · Exploration',e['title'],f'''
<p class="lede">{esc(e['intro'])}</p><div class="callout blue"><div class="label">Investigation</div><p>{esc(e['instruction'])}</p></div>{table(e.get('table'))}
{{{{exercise:explore}}}}<div class="workspace tall"></div>'''))
    out.append(page(f'Chapter {ch} · Checkpoint','Checkpoint and reflection',f'''
{{{{exercise:check}}}}
<div class="card sand"><h3>Reflection</h3><ul><li>Which representation made the idea clearest: a diagram, a table, symbols or words?</li><li>Where did you check an answer instead of trusting it?</li><li>Write one question you would ask a partner to test understanding.</li></ul></div>
<div class="workspace tall"></div>'''))
    a=p['application']
    out.append(page(f'Chapter {ch} · Application',a['title'],f'''
<p class="lede">{esc(a['intro'])}</p><div class="callout"><div class="label">Real-life application</div><p>{esc(a['instruction'])}</p></div>{table(a.get('table'))}
{{{{exercise:application}}}}<div class="workspace"></div>'''))
    s=p['assessment']
    out.append(page(f'Chapter {ch} · Assessment practice',s['title'],f'''
<div class="assessment"><div class="criterion">MYP assessment practice</div><p>{esc(s['instruction'])}</p><p>{esc(s['intro'])}</p></div>
{{{{exercise:assessment}}}}
<div class="card pale"><h3>Success criteria</h3><ul><li>Use correct mathematical language and notation.</li><li>Show a method or representation that another student can follow.</li><li>Check the result and explain why it is reasonable.</li></ul></div><div class="workspace tall"></div>'''))
    out.append(page(f'Chapter {ch} · Mixed practice',f'Mixed practice {ch}',f'''
<p class="instructions">Connect ideas across the chapter. Give units and reasons where requested.</p>
{{{{exercise:mixed}}}}
<div class="callout blue"><div class="label">Final reflection</div><p>Choose one item you solved confidently and one that needed a revision. Explain the difference in your method.</p></div>'''))
    out.append('{{answers}}')
    return '\n'.join(out)

def main():
    chapters=[int(x) for x in sys.argv[1:]] or list(range(3,11))
    for n in chapters:
        p=load(n)
        data={k:v for k,v in p.items() if k not in ('layout',)}
        (ROOT/'data'/f'chapter-{n:02d}.exercises.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        (ROOT/'data'/f'chapter-{n:02d}.layout.json').write_text(json.dumps(p['layout'],ensure_ascii=False,indent=2)+'\n')
        (ROOT/'manuscript'/f'chapter-{n:02d}.source.html').write_text(render(p)+'\n')
        print(f'Author chapter {n}: {sum(len(g["items"]) for g in p["groups"])} items, {len(p["layout"]["answerPages"])} answer pages')
if __name__=='__main__': main()
