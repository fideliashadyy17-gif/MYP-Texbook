"""Authoring helpers. Verification expressions are evaluated independently of answer prose."""
from fractions import Fraction as F
from math import ceil, floor, sqrt, isqrt
def q(id, tier, prompt, answer, reasoning, checks):
    if isinstance(checks, dict): checks=[checks]
    return dict(id=id,tier=tier,prompt=prompt,answer=answer,reasoning=reasoning,verify=checks)
def v(expr, equals=None, contains=None, **kw):
    d={'expr':expr}
    if equals is not None: d['equals']=equals
    if contains: d['contains']=contains
    d.update(kw); return d
def section(n,title,short,intent,paras,example,warning,practice,diagram=None):
    return dict(number=n,title=title,short=short,intent=intent,paras=paras,example=example,warning=warning,practice=practice,diagram=diagram)
def ex(title,problem,steps,answer): return dict(title=title,problem=problem,steps=steps,answer=answer)
def group(id,title,instruction,items): return dict(id=id,title=title,instruction=instruction,items=items)
def plan(ch,title,part,hours,context,related,soi,engage,atl,sections,explore,application,assessment,mixed,ready,check,diagrams,objectives,vocabulary,key='Relationships',sourcepages='',answerpages='',notes=None):
    groups=[group('ready','Ready check','Try these without a calculator. They check the ideas this chapter builds on.',ready)]
    groups += [group('p'+s['number'].replace('.',''), 'Practice '+s['number']+' · '+s['short'], 'Show a method or explanation that someone else can check.',s['practice']) for s in sections]
    groups += [group('explore','Exploration · '+explore['title'],explore['instruction'],explore['items']),group('check','Checkpoint','Answer, then explain one result to a partner.',check),group('application','Application · '+application['title'],application['instruction'],application['items']),group('assessment','Assessment practice · '+assessment['title'],assessment['instruction'],assessment['items']),group('mixed','Mixed practice '+str(ch),'Connect ideas. Give units and reasons where requested.',mixed)]
    ids=[x['id'] for g in groups for x in g['items']]; assert len(ids)==len(set(ids)),(ch,'duplicate ids')
    layout=[]
    layout.append({'title':'Answers · Ready check and Checkpoint','groups':[['ready'],['check']]})
    for i in range(0,len(sections),2):
        ss=sections[i:i+2]; layout.append({'title':'Answers · '+' and '.join(s['number'] for s in ss),'groups':[['p'+s['number'].replace('.','')] for s in ss]})
    layout += [{'title':'Answers · Exploration','groups':[['explore']]},{'title':'Answers · Application and Assessment','groups':[['application'],['assessment']]},{'title':'Answers · Mixed practice','groups':[['mixed']]}]
    return dict(chapter=ch,title=title,part=part,hours=hours,key=key,related=related,context=context,soi=soi,engage=engage,atl=atl,objectives=objectives,vocabulary=vocabulary,sections=sections,explore=explore,application=application,assessment=assessment,diagrams=diagrams,notes=notes or [],groups=groups,layout={'chapter':ch,'answerPages':layout},source=dict(file='MYP-Mathematics-1-Student-Coursebook.pdf',sha256='131a3a99d14ae5a7613c7e9da24c540e29029d93a1a360abcc8516835798b3f0',pages=sourcepages,scope_note='Rewritten within the verified first-edition chapter scope and embedded planner. No standalone school curriculum overview was present. New classroom contexts are simulated and labelled.'))
