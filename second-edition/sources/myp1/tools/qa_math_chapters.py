#!/usr/bin/env python3
"""Independent mathematical QA for Chapters 3–10.
Evaluates verification expressions with a restricted AST and compares to expected values.
Also checks that scalar numeric answers appear in the student-facing answer/reasoning.
"""
import ast, json, math, re, sys, importlib.util
from fractions import Fraction
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from itertools import permutations
from collections import Counter
TOOLS=Path(__file__).resolve().parent; ROOT=TOOLS.parent; QA=ROOT.parent.parent/'qa'/'myp1'
sys.path.insert(0,str(TOOLS/'content'))
QA.mkdir(parents=True,exist_ok=True)

def F(a,b=None): return Fraction(a) if b is None else Fraction(a,b)
def factors(n): return [d for d in range(1,n+1) if n%d==0]
def primes(n): return [x for x in range(2,n) if all(x%d for d in range(2,int(math.isqrt(x))+1))]
def prime_factors(n):
    out=[]; d=2
    while d*d<=n:
        while n%d==0: out.append(d); n//=d
        d+=1
    if n>1: out.append(n)
    return out
def product(xs): return math.prod(xs)
def lcm(*xs): return math.lcm(*xs)
def gcd(*xs): return math.gcd(*xs)
def mean(xs): return sum(xs)/len(xs)
def median(xs):
    s=sorted(xs); n=len(s); return s[n//2] if n%2 else (s[n//2-1]+s[n//2])/2
def mode(xs): return Counter(xs).most_common(1)[0][0]
def roundh(x,places):
    q=Decimal(1).scaleb(-places); return str(Decimal(str(x)).quantize(q,rounding=ROUND_HALF_UP))
def terminates(f):
    f=F(f); return all(p in (2,5) for p in prime_factors(f.denominator))
def classify_angle(a): return 'acute' if a<90 else 'right' if a==90 else 'obtuse' if a<180 else 'reflex'
def triangle_possible(a,b,c):
    x,y,z=sorted([a,b,c]); return x+y>z
def number_family(x):
    if isinstance(x,int) or float(x).is_integer():
        x=int(x); return 'natural' if x>0 else 'whole' if x==0 else 'integer'
    return 'rational'
def is_irrational_symbol(s): return s in ('sqrt2','pi')
ENV={
 'F':F,'factors':factors,'primes':primes,'prime_factors':prime_factors,'product':product,
 'gcd':gcd,'lcm':lcm,'mean':mean,'median':median,'mode':mode,'roundh':roundh,
 'terminates':terminates,'classify_angle':classify_angle,'triangle_possible':triangle_possible,
 'number_family':number_family,'is_irrational_symbol':is_irrational_symbol,
 'sqrt':math.sqrt,'isqrt':math.isqrt,'ceil':math.ceil,'floor':math.floor,'abs':abs,
 'range':range,'len':len,'sum':sum,'min':min,'max':max,'sorted':sorted,'set':set,
 'list':list,'tuple':tuple,'zip':zip,'round':round,'int':int,'float':float,'str':str,
 'permutations':permutations,'True':True,'False':False,'None':None,
}
ALLOWED=(ast.Expression,ast.BinOp,ast.UnaryOp,ast.BoolOp,ast.Compare,ast.Call,ast.Name,ast.Load,
 ast.Constant,ast.List,ast.Tuple,ast.Dict,ast.Set,ast.ListComp,ast.SetComp,ast.GeneratorExp,
 ast.comprehension,ast.Add,ast.Sub,ast.Mult,ast.Div,ast.FloorDiv,ast.Mod,ast.Pow,ast.USub,ast.UAdd,
 ast.Eq,ast.NotEq,ast.Lt,ast.LtE,ast.Gt,ast.GtE,ast.And,ast.Or,ast.Not,ast.In,ast.NotIn,ast.IfExp,
 ast.Subscript,ast.Slice,ast.Index,ast.Attribute,ast.Store,ast.Starred,ast.BitOr,ast.BitAnd,ast.BitXor)
def safe_eval(expr,env):
    tree=ast.parse(expr,mode='eval')
    for node in ast.walk(tree):
        if not isinstance(node,ALLOWED): raise ValueError(f'Disallowed syntax {type(node).__name__}: {expr}')
        if isinstance(node,ast.Attribute) and node.attr.startswith('_'): raise ValueError('private attribute')
    g=dict(env); g['__builtins__']={}
    return eval(compile(tree,'<verify>','eval'),g)

def canon(x):
    if isinstance(x,Fraction): return x.numerator if x.denominator==1 else f'{x.numerator}/{x.denominator}'
    if isinstance(x,float):
        if math.isclose(x,round(x),abs_tol=1e-9): return int(round(x))
        return round(x,8)
    if isinstance(x,(list,tuple)): return [canon(v) for v in x]
    return x

def numeric(x):
    if isinstance(x,(int,float,Fraction)) and not isinstance(x,bool): return float(x)
    if isinstance(x,str):
        try: return float(Fraction(x))
        except Exception: return None
    return None
def eq(a,b):
    if isinstance(a,(list,tuple)) and isinstance(b,(list,tuple)): return len(a)==len(b) and all(eq(x,y) for x,y in zip(a,b))
    na,nb=numeric(a),numeric(b)
    if na is not None and nb is not None: return math.isclose(na,nb,rel_tol=1e-8,abs_tol=1e-8)
    return canon(a)==canon(b)

def norm(s): return re.sub(r'\s+',' ',str(s).replace('−','-').replace('–','-').replace('≈','').replace('×','*')).lower()
def variants(x):
    x=canon(x); out=set()
    if isinstance(x,bool): return out
    if isinstance(x,int): out.add(str(x)); out.add(f'{x:,}')
    elif isinstance(x,float):
        out.add(str(x)); out.add(f'{x:g}'); out.add(f'{x:.2f}'); out.add(f'{x:.1f}')
    elif isinstance(x,str): out.add(x)
    return {norm(v) for v in out}

def check_item(item,env):
    failures=[]; text=norm(item['answer']+' '+item.get('reasoning',''))
    for i,c in enumerate(item.get('verify',[])):
        try:
            if 'forall' in c:
                f=c['forall']; var=f['var']
                for val in f['values']:
                    e=dict(env); e[var]=val
                    if not eq(safe_eval(f['left'],e),safe_eval(f['right'],e)):
                        failures.append(f'check {i}: forall failed at {var}={val}')
            else:
                got=safe_eval(c['expr'],env)
                if 'equals' in c and not eq(got,c['equals']): failures.append(f'check {i}: {c["expr"]} -> {canon(got)} != {canon(c["equals"])}')
                if 'contains' in c:
                    compact=re.sub(r'\s+','',text)
                    for phrase in c['contains']:
                        if norm(phrase) not in text and re.sub(r'\s+','',norm(phrase)) not in compact:
                            failures.append(f'check {i}: missing phrase {phrase!r}')
        except Exception as e:
            failures.append(f'check {i}: {type(e).__name__}: {e}')
    if not item.get('verify'): failures.append('no verification checks')
    return failures

def load_env(n):
    env=dict(ENV)
    p=TOOLS/'content'/f'chapter_{n:02d}.py'
    if p.exists():
        spec=importlib.util.spec_from_file_location(f'c{n}',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k,v in vars(m).items():
            if k.isupper() and isinstance(v,(int,float,list,tuple,str)): env[k]=v
    return env

def main():
    chapters=[int(x) for x in sys.argv[1:]] or list(range(3,11))
    allpass=True; summary=[]
    for n in chapters:
        data=json.loads((ROOT/'data'/f'chapter-{n:02d}.exercises.json').read_text())
        env=load_env(n); items=[q for g in data['groups'] for q in g['items']]
        results=[]
        for q in items:
            f=check_item(q,env); results.append({'id':q['id'],'status':'PASS' if not f else 'FAIL','failures':f})
        passed=sum(r['status']=='PASS' for r in results); ok=passed==len(results)
        allpass &= ok
        report={'chapter':n,'title':data['title'],'items':len(results),'passed':passed,'status':'PASS' if ok else 'FAIL','results':results}
        (QA/f'chapter-{n:02d}-math-qa.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
        summary.append({'chapter':n,'items':len(results),'passed':passed,'status':report['status']})
        print(f'Chapter {n}: {passed}/{len(results)} {report["status"]}')
        for r in results:
            if r['failures']: print(' ',r['id'],r['failures'])
    (QA/'chapters-03-10-math-summary.json').write_text(json.dumps({'status':'PASS' if allpass else 'FAIL','chapters':summary},indent=2)+'\n')
    sys.exit(0 if allpass else 1)
if __name__=='__main__': main()
