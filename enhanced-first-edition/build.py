#!/usr/bin/env python3
"""Render original added practice and interleave it into the verified first editions."""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re

import pymupdf as pdf
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph
from xml.sax.saxutils import escape

HOME = Path(__file__).resolve().parent
ROOT = HOME.parent
SOURCES = {
    1: ('MYP-Mathematics-1-Student-Coursebook.pdf', '131a3a99d14ae5a7613c7e9da24c540e29029d93a1a360abcc8516835798b3f0'),
    2: ('MYP-Mathematics-2-Student-Coursebook.pdf', '565ed7876b3cf2e16d0a7c9607fe9cf93a8edc40d599ce8772ad70ca76baa30e'),
    3: ('MYP-Mathematics-3-Student-Coursebook.pdf', '3cb3bb8071713cd453da62972451dada54c2a63f5266b00b7970bb8239c519ed'),
    4: ('MYP_Mathematics_4_Student_Coursebook.pdf', '4e0e8a32776f43f8565966edb54f9f30c6f45e7858259bd9799931e89197c393'),
    5: ('MYP_Mathematics_5_Student_Coursebook.pdf', '5f2e8001623ce1e26c72a94755127ee0828c4b0756fcc6c5bc0604e223d3274f'),
}
CRITERIA = {'A': 'Knowing and understanding', 'B': 'Investigating patterns',
            'C': 'Communicating', 'D': 'Applying mathematics in real-life contexts'}
REFERENCE_IDS = {'2A','2B','3A','3B','4A','4B','4C','5A','5C'}
TINT = HexColor('#e8eeeb')
GRID = HexColor('#c5ceca')
INK = HexColor('#172622')
MUTED = HexColor('#465750')
GOLD = HexColor('#8c6039')
PAPER = HexColor('#fbfaf5')
DARKS = {1:'#14342f', 2:'#152a3a', 3:'#19323d', 4:'#12433d', 5:'#133731'}
PALETTE = ('#17574f', '#a65533', '#324c79', '#775868')
M = 65  # generous, symmetric print margin for both recto and verso


def validate(condition, message):
    if not condition:
        raise ValueError(message)


def read_practice(year):
    source = HOME / 'source' / f'myp{year}.txt'
    sections = {}
    section = task = None
    for lineno, raw in enumerate(source.read_text().splitlines(), 1):
        text = raw.strip()
        if not text or text.startswith('#'):
            continue
        fields = [field.strip() for field in text.split('|')]
        token = fields[0]
        context = f'{source.name}:{lineno}'
        if re.fullmatch(r'(?:\d+|[CE])\.\d+', token):
            validate(len(fields)==2 and token not in sections and
                     set(fields[1].split(',')) <= REFERENCE_IDS, context)
            section = {'refs': fields[1].split(','), 'tasks': []}
            sections[token] = section
            task = None
        elif token in CRITERIA:
            validate(section is not None and len(fields)>=6 and all(fields) and
                     (task is None or task['answers']), context)
            task = dict(criterion=token, title=fields[1], stem=fields[2],
                        parts=fields[3:], visuals=[], answers=[])
            section['tasks'].append(task)
        elif text.startswith('@'):
            validate(task is not None and not task['answers'], context)
            cmd, _, value = text[1:].partition(' ')
            task['visuals'].append((cmd, value.strip()))
        elif text.startswith('= '):
            validate(task is not None and not task['answers'], context)
            task['answers'] = [s.strip() for s in text[2:].split('~')]
            validate(len(task['parts'])==len(task['answers']) and all(task['answers']), context)
        else:
            raise ValueError(context)
    for sid, section in sections.items():
        validate(section['tasks'] and all(t['answers'] for t in section['tasks']), f'Empty: {sid}')
    return sections


def register_fonts():
    directory = Path(os.environ.get('DEJAVU_DIR', '/usr/share/fonts/truetype/dejavu'))
    for name, filename in [('Body', 'DejaVuSerif'), ('Heading', 'DejaVuSerif-Bold'),
                           ('Label', 'DejaVuSans'), ('Bold', 'DejaVuSans-Bold')]:
        pdfmetrics.registerFont(TTFont(name, str(directory / (filename + '.ttf'))))


def para(c, text, x, y, w, size=11, leading=None, font='Body', color=INK):
    widths = pdfmetrics.getFont(font).face.charWidths
    fallback = pdfmetrics.getFont('Label').face.charWidths
    missing = {char for char in text if ord(char) not in widths}
    validate(all(ord(char) in fallback for char in missing), f'Missing glyphs {missing!r}: {text}')
    markup = ''.join(escape(ch) if ch not in missing else f'<font name="Label">{escape(ch)}</font>' for ch in text)
    style = ParagraphStyle('copy', fontName=font, fontSize=size, leading=leading or size*1.43,
                           textColor=color, alignment=TA_LEFT, splitLongWords=False)
    p = Paragraph(markup, style)
    _, h = p.wrap(w, 10_000)
    for line in p.blPara.lines:
        if isinstance(line, tuple):
            validate(line[0] >= -6, f'Unbreakable text: {line[0]:.2f} {line[1]}')
    p.drawOn(c, x, y-h)
    return y-h


def label(c, text, x, y, size=9, color=MUTED, align='left', font='Label'):
    for char in text:
        validate(ord(char) in pdfmetrics.getFont(font).face.charWidths, f'Missing label glyph: {char!r} in {text}')
    c.setFillColor(color)
    c.setFont(font, size)
    {'left':c.drawString,'mid':c.drawCentredString,'right':c.drawRightString}[align](x,y,text)


def line(c, x1,y1,x2,y2, color=INK, width=1):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1,y1,x2,y2)


def dot(c,x,y,r=2.8,color=INK):
    c.setFillColor(color)
    c.circle(x,y,r,0,1)


def number(n):
    return f'{n:g}'.replace('-', '−')


def ticks(lo, hi, target=8):
    validate(hi>lo, f'Invalid scale: {lo}, {hi}')
    a = 10**math.floor(math.log10((hi-lo)/target))
    step = next(m*a for m in (1,2,2.5,5,10) if m*a>=((hi-lo)/target)-1e-10)
    return [round(i*step, 10) for i in range(math.ceil(lo/step-1e-10),math.floor(hi/step+1e-10)+1)]


def path(c, points, stroke=INK, fill=None, width=1.25):
    p=c.beginPath()
    for i,(x,y) in enumerate(points):
        (p.moveTo if i==0 else p.lineTo)(x,y)
    if fill is not None:
        p.close()
        c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.drawPath(p,stroke=1,fill=fill is not None)


def points(text):
    output = [tuple(map(float, point.split(','))) for point in text.split()]
    validate(all(len(pair)==2 and all(map(math.isfinite, pair)) for pair in output), text)
    return output


def render_visual(c, cmd, value, x, y, w, compact=False):
    v = [s.strip() for s in value.split('|')]
    if cmd in ('table','stem'):
        table, *keys = v if cmd=='stem' else [value]
        cells=[row.split('~') for row in table.split(';')]
        n=len(cells[0]); validate(all(len(row)==n for row in cells), f'Ragged table: {value}')
        weights = [max(1.0,min(4.2, max(len(row[j]) for row in cells)/7)) for j in range(n)]
        ws=[w*a/sum(weights) for a in weights]
        for i, row in enumerate(cells):
            cell_style=ParagraphStyle('cell',fontName='Bold' if i==0 else 'Label', fontSize=9, leading=12, textColor=INK)
            paragraphs=[Paragraph(escape(cell.strip()),cell_style) for cell in row]
            for cell in row:
                validate(all(ord(char) in pdfmetrics.getFont(cell_style.fontName).face.charWidths for char in cell), value)
            heights=[p.wrap(cw-12,1000)[1] for p,cw in zip(paragraphs,ws)]
            rh=max(heights)+12
            xx=x
            for p,cw,h in zip(paragraphs,ws,heights):
                c.setFillColor(TINT if i==0 else (white if i%2 else PAPER)); c.setStrokeColor(GRID); c.setLineWidth(.45)
                c.rect(xx,y-rh,cw,rh,1,1); p.drawOn(c,xx+6,y-6-h); xx+=cw
            y-=rh
        if keys:
            y=para(c,keys[0],x,y-6,w,8.1,11,'Label',MUTED)
        return y-9

    if cmd in ('xy','hist','curve','cubic'):
        xmin,xmax,ymin,ymax=map(float,v[0].split()); xlabel,ylabel=v[1:3]; series=v[3] if len(v)>3 else ''
        validate(xmax>xmin and ymax>ymin, value)
        graphs = [(name, points(coords)) for name, coords in (s.split(':',1) for s in series.split(';'))] if cmd=='xy' and series else []
        def dashed(index,name):
            return name.startswith('~') or (not name.startswith('+') and index%2==1)
        legends=[(k,name) for k,(name,_) in enumerate(graphs) if name not in {'p','d'}]
        graph_h=82 if compact else (126 if not legends else 137)
        margin=44; avail=w-76
        gw,gh=avail,graph_h
        # Use physically equal unit lengths for Cartesian geometry and maps with the same units.
        if cmd=='xy' and (xlabel,ylabel) in [('x','y'),('m','m'),('East (m)','North (m)')]:
            scale=min(avail/(xmax-xmin),graph_h/(ymax-ymin)); gw=scale*(xmax-xmin); gh=scale*(ymax-ymin)
            if gw < 120 and not compact:  # coordinate plates still need an adequate area for reading
                gw=min(avail, 175); gh=gw*(ymax-ymin)/(xmax-xmin)
                if gh>176: gw,gh=scale*(xmax-xmin),scale*(ymax-ymin)
        x0=x+margin+(avail-gw)/2; y0=y-gh-22-(18 if legends else 0)
        X=lambda a: x0+(a-xmin)*gw/(xmax-xmin)
        Y=lambda b: y0+(b-ymin)*gh/(ymax-ymin)
        if legends:
            lx=x
            for k,name in legends:
                color=HexColor(PALETTE[k%len(PALETTE)])
                if dashed(k,name): c.setDash(5,2)
                line(c,lx,y-7,lx+17,y-7,color,1.8); c.setDash()
                legend=name.lstrip('~+')
                label(c,legend,lx+23,y-10,8,INK)
                lx+=33+pdfmetrics.stringWidth(legend,'Label',8)
            validate(lx<=x+w+12,value)
        for a in ticks(xmin,xmax):
            line(c,X(a),y0,X(a),y0+gh,GRID,.5); label(c,number(a),X(a),y0-13,7.3,align='mid')
        for b in ticks(ymin,ymax,6):
            line(c,x0,Y(b),x0+gw,Y(b),GRID,.5); label(c,number(b),x0-5,Y(b)-2.5,7.3,align='right')
        label(c,ylabel,x0,y0+gh+7,8,font='Bold')
        label(c,xlabel,x0+gw,y0-26,8,align='right',font='Bold')
        if xmin<=0<=xmax: line(c,X(0),y0,X(0),y0+gh,MUTED,.9)
        if ymin<=0<=ymax: line(c,x0,Y(0),x0+gw,Y(0),MUTED,.9)
        c.saveState(); box=c.beginPath(); box.rect(x0-.6,y0-.6,gw+1.2,gh+1.2); c.clipPath(box,0,0)
        if cmd=='hist':
            for a,b,h in (map(float,s.split(',')) for s in series.split(';')):
                validate(xmin<=a<b<=xmax and ymin<=h<=ymax,value)
                c.setFillColor(HexColor('#cdded7')); c.setStrokeColor(INK); c.setLineWidth(.8)
                c.rect(X(a),Y(ymin),X(b)-X(a),Y(h)-Y(ymin),1,1)
        elif cmd in ('curve','cubic'):
            coeffs=list(map(float,series.split(','))); validate(len(coeffs)==(3 if cmd=='curve' else 4),value)
            def polynomial(x):
                f=0
                for coeff in coeffs: f=f*x+coeff
                return f
            p=[(X(a),Y(polynomial(a))) for a in (xmin+(xmax-xmin)*i/240 for i in range(241))]
            path(c,p,HexColor(PALETTE[0]),width=1.65)
        else:
            for k,(name,p) in enumerate(graphs):
                color=HexColor(PALETTE[k%len(PALETTE)])
                validate(all(xmin-1e-6<=a<=xmax+1e-6 and ymin-1e-6<=b<=ymax+1e-6 for a,b in p), f'Off-grid: {value}')
                if name=='d':
                    for a,b in p: dot(c,X(a),Y(b),2.4,color)
                else:
                    if dashed(k,name): c.setDash(4.5,2)
                    path(c,[(X(a),Y(b)) for a,b in p],color,HexColor('#d9e7e1') if name=='p' else None,1.65)
                    c.setDash()
        c.restoreState()
        c.setStrokeColor(MUTED); c.setLineWidth(.6); c.rect(x0,y0,gw,gh,1,0)
        return y0-34

    if cmd in ('line','dots','box'):
        lo,hi=map(float,v[:2]); v+=['']*(4-len(v)); validate(hi>lo,value)
        x0=x+35; aw=w-63; X=lambda a: x0+(a-lo)*aw/(hi-lo)
        is_line=cmd=='line'
        stop=y-(50 if is_line else 81 if cmd=='dots' else 97)
        axis=stop+21
        line(c,x0,axis,x0+aw,axis,MUTED,.95)
        for a in ticks(lo,hi, min(13,int(hi-lo)) if is_line and lo.is_integer() and hi.is_integer() else 8):
            line(c,X(a),axis-3,X(a),axis+3,MUTED,.65); label(c,number(a),X(a),axis-13,8,align='mid')
        if not is_line: label(c,v[2],x0+aw,axis-25,8,align='right',font='Bold')
        if cmd=='box':
            for j, series in enumerate(v[3].split(';')):
                name,Data=series.split(':'); a,b,m,d,e=map(float,Data.split(',')); validate(lo<=a<=b<=m<=d<=e<=hi,value)
                cy=y-22-30*j
                label(c,name,x0-9,cy-3,9,align='right',font='Bold')
                line(c,X(a),cy,X(e),cy); line(c,X(a),cy-4,X(a),cy+4); line(c,X(e),cy-4,X(e),cy+4)
                c.setFillColor(TINT); c.setStrokeColor(INK); c.rect(X(b),cy-8,X(d)-X(b),16,1,1)
                line(c,X(m),cy-8,X(m),cy+8,INK,1.4)
        else:
            for item in filter(None,v[2 if is_line else 3].split(',')):
                a,t=item.split(':'); a=float(a); validate(lo<=a<=hi,value)
                if is_line:
                    dot(c,X(a),axis,2.5); label(c,t,X(a),axis+9,8,align='mid',font='Bold')
                else:
                    validate(1<=int(t)<=7,value)
                    for j in range(int(t)): dot(c,X(a),axis+8+6*j,2.3)
        return stop-9

    if cmd=='bar':
        lo,hi=map(float,v[0].split()); bars=[(name,float(h)) for name,h in (s.split(':') for s in v[2].split(','))]
        x0=x+34; aw=w-60; h=87; y0=y-104; Y=lambda a:y0+h*(a-lo)/(hi-lo)
        for t in ticks(lo,hi,5):
            line(c,x0,Y(t),x0+aw,Y(t),GRID,.6); label(c,number(t),x0-5,Y(t)-3,8,align='right')
        if lo not in ticks(lo,hi,5): label(c,number(lo),x0-5,y0-3,8,align='right')
        label(c,v[1],x0,y0+h+7,9,font='Bold'); gap=aw/len(bars)
        for i,(name,b) in enumerate(bars):
            validate(lo<=b<=hi,value); xx=x0+gap*(i+.5); bw=min(56,gap*.57)
            c.setFillColor(TINT); c.setStrokeColor(INK); c.setLineWidth(.75); c.rect(xx-bw/2,y0,bw,Y(b)-y0,1,1)
            label(c,name,xx,y0-14,8,align='mid')
        line(c,x0,y0,x0+aw,y0,MUTED,.8); line(c,x0,y0,x0,y0+h,MUTED,.8)
        return y0-22

    if cmd=='shape':
        # Paths separated by semicolons; vertices and optional point labels by pipes.
        paths=[]
        for seg in value.split(';'):
            p=[]
            for token in seg.split('|'):
                pair,_,text=token.strip().partition(' '); a,b=points(pair)[0]; p.append((a,b,text))
            paths.append(p)
        allp=[p for group in paths for p in group]; xx=[a for a,_,_ in allp]; yy=[b for _,b,_ in allp]
        a0,b0=min(xx),min(yy); dx=max(max(xx)-a0,.01); dy=max(max(yy)-b0,.01)
        scale=min((w-76)/dx,92/dy); left=x+(w-dx*scale)/2; bottom=y-26-dy*scale
        X=lambda a:left+(a-a0)*scale; Y=lambda b:bottom+(b-b0)*scale
        for group in paths:
            if len(group)==2 and group[0][:2]==group[1][:2]: dot(c,X(group[0][0]),Y(group[0][1]),2.1)
            elif len(group)>1: path(c,[(X(a),Y(b)) for a,b,_ in group],HexColor(PALETTE[0]))
        for group in paths:
            for a,b,name in group:
                if not name: continue
                if len(group)==1:
                    label(c,name,X(a),Y(b)-2,8,INK,'mid')
                elif a <= (a0+dx/2):
                    label(c,name,X(a)-4,Y(b)+3,8,INK,'right','Bold')
                else: label(c,name,X(a)+5,Y(b)+3,8,INK,font='Bold')
        label(c,'Schematic · labels give the measurements',x,bottom-16,7.6)
        return bottom-24

    if cmd=='venn':
        validate(len(v)==6,value)
        cx=x+w/2; cy=y-53
        c.setStrokeColor(MUTED); c.rect(cx-120,cy-42,240,84,1,0)
        c.setStrokeColor(HexColor(PALETTE[0])); c.circle(cx-24,cy,35,1,0); c.circle(cx+24,cy,35,1,0)
        for name,ax,ay in [(v[0],cx-35,cy+21),(v[1],cx+35,cy+21),(v[2],cx-41,cy-4),(v[3],cx,cy-4),(v[4],cx+41,cy-4),(v[5],cx+89,cy-21),('U',cx-104,cy+25)]:
            label(c,name,ax,ay,9,INK,'mid')
        return cy-52

    if cmd=='tree':
        validate(len(v) in (8,10),value)
        labels=v[:2]; outcomes=v[8:] or labels
        x0=x+16; x1=x+w*.38; x2=x+w*.76; yc=y-68
        a=(x0,yc); bs=[(x1,yc+31),(x1,yc-31)]; cs=[(x2,yc+d) for d in (53,19,-19,-53)]
        for j,b in enumerate(bs):
            line(c,*a,*b,MUTED,1); label(c,labels[j],b[0]+4,b[1]+5,9,font='Bold'); dot(c,*b,2)
            label(c,v[2+j],(a[0]+b[0])/2,(a[1]+b[1])/2+4,8,INK,'mid')
            for k in range(2):
                t=cs[j*2+k]; line(c,*b,*t,MUTED,1); dot(c,*t,2)
                label(c,outcomes[k],t[0]+7,t[1]-3,9)
                label(c,v[4+j*2+k],(b[0]+t[0])/2,(b[1]+t[1])/2+4,8,INK,'mid')
        dot(c,*a,2)
        return yc-67

    if cmd=='net':
        cells=[(points(s.split(':')[0])[0],s.split(':')[1]) for s in value.split()]; sq=22
        lx=min(a for (a,_),_ in cells); ly=min(b for (_,b),_ in cells)
        nx=max(a for (a,_),_ in cells)-lx+1; ny=max(b for (_,b),_ in cells)-ly+1
        x0=x+(w-nx*sq)/2; y0=y-ny*sq-8
        for (a,b),name in cells:
            xx=x0+(a-lx)*sq; yy=y0+(b-ly)*sq
            c.setFillColor(TINT); c.setStrokeColor(INK); c.rect(xx,yy,sq,sq,1,1)
            label(c,name,xx+sq/2,yy+sq/2-3,8,INK,'mid')
        return y0-9

    if cmd in ('strips','hundred'):
        if cmd=='strips':
            for trial in value.split(','):
                n,k=map(int,trial.split(':')); validate(0<=k<=n,value)
                size=min(245,w)/n
                for j in range(n):
                    c.setFillColor(TINT if j<k else white); c.setStrokeColor(MUTED); c.setLineWidth(.7)
                    c.rect(x+(w-size*n)/2+j*size,y-24,size,17,1,1)
                y-=32
            return y-2
        k=int(value); validate(0<=k<=100,value); size=8
        for j in range(100):
            c.setFillColor(HexColor('#90b3a5') if j<k else white); c.setStrokeColor(MUTED); c.setLineWidth(.4)
            c.rect(x+w/2-40+(j%10)*size,y-14-(j//10)*size,size,size,1,1)
        return y-96

    if cmd=='spinner':
        names=value.split(','); n=len(names); r=46; cx=x+w/2; cy=y-54
        for j,t in enumerate(names):
            theta=2*math.pi*j/n; phi=2*math.pi*(j+.5)/n
            line(c,cx,cy,cx+r*math.cos(theta),cy+r*math.sin(theta),MUTED,.75)
            label(c,t,cx+.7*r*math.cos(phi),cy+.7*r*math.sin(phi)-3,8,INK,'mid')
        c.setStrokeColor(MUTED); c.circle(cx,cy,r,1,0); dot(c,cx,cy,2.3)
        return cy-r-9

    if cmd=='circle':
        r=47; cx=x+w/2; cy=y-67
        pts={'O':(cx,cy)}
        c.setStrokeColor(MUTED); c.setLineWidth(1); c.circle(cx,cy,r,1,0)
        for item in v[0].split():
            a,name=item.split(':'); theta=math.radians(float(a)); u=math.cos(theta); s=math.sin(theta)
            pts[name]=(cx+r*u,cy+r*s); label(c,name,cx+(r+10)*u,cy+(r+10)*s-3,8,INK,'mid','Bold')
            dot(c,*pts[name],1.8)
        for a,b in v[1].split(): line(c,*pts[a],*pts[b],HexColor(PALETTE[0]))
        dot(c,cx,cy,1.8); label(c,'O',cx-6,cy-9,8,INK)
        if len(v)>2:
            ax,ay=pts[v[2]]; u=(ax-cx)/r; s=(ay-cy)/r
            line(c,ax-55*s,ay+55*u,ax+55*s,ay-55*u,MUTED,.9)
        return cy-r-18

    if cmd=='cuboid':
        start=x+w/2-84; base=y-118
        a=(start,base+13); b=(start+116,base+13); d=(start+48,base+38); e=(start+164,base+38)
        up=lambda p:(p[0],p[1]+51)
        for p,q in [(a,b),(b,e),(e,d),(d,a),(a,up(a)),(b,up(b)),(d,up(d)),(e,up(e)),(up(a),up(b)),(up(b),up(e)),(up(e),up(d)),(up(d),up(a))]:
            if d in (p,q): c.setDash(3,2)
            line(c,*p,*q,MUTED,.85); c.setDash()
        line(c,*a,*e,GOLD,1.25); c.setDash(4,2); line(c,*a,*up(e),HexColor(PALETTE[0]),1.4); c.setDash()
        label(c,v[0],start+58,base,9,INK,'mid'); label(c,v[1],start+148,base+20,9,INK); label(c,v[2],start+171,base+61,9,INK)
        label(c,'Schematic · base and space diagonals',x,base-15,7.6)
        return base-23

    if cmd in ('cap','capsule'):
        if cmd=='cap':
            a,b=map(float,v); s=12; x0=x+w/2-a*s/2; y0=y-(b+a/2)*s-6; w0=a*s; h=b*s
            path(c,[(x0,y0+h),(x0,y0),(x0+w0,y0),(x0+w0,y0+h)])
            c.setStrokeColor(INK); c.arc(x0,y0+h-w0/2,x0+w0,y0+h+w0/2,0,180)
            c.setDash(4,2); line(c,x0,y0+h,x0+w0,y0+h,MUTED,.8); c.setDash()
            label(c,f'{v[0]} cm',x0+w0/2,y0-13,8,INK,'mid'); label(c,f'{v[1]} cm',x0-8,y0+h/2,8,INK,'right')
        else:
            a,b=map(float,v); s=13; r=a*s; b*=s; x0=x+w/2-b/2; y0=y-2*r-17; h=2*r
            line(c,x0,y0,x0+b,y0); line(c,x0,y0+h,x0+b,y0+h)
            c.setStrokeColor(INK); c.arc(x0-r,y0,x0+r,y0+h,90,180); c.arc(x0+b-r,y0,x0+b+r,y0+h,-90,180)
            for xx in (x0,x0+b):
                c.setDash(4,2); line(c,xx,y0,xx,y0+h,MUTED,.8); c.setDash()
            dot(c,x0,y0+r,1.6); line(c,x0,y0+r,x0,y0+h,MUTED,.8)
            label(c,f'r = {v[0]} cm',x0-5,y0+r+4,8,INK,'right'); label(c,f'{v[1]} cm',x0+b/2,y0-13,8,INK,'mid')
        return y0-22
    raise ValueError(f'Unknown visual {cmd!r}')


def new_page(c,year,w,h,kicker,tag,footer):
    dark=HexColor(DARKS[year]); c.setFillColor(PAPER); c.rect(0,0,w,h,0,1)
    line(c,M,h-56,w-M,h-56,GOLD,.85)
    label(c, f'MYP MATHEMATICS {year}   /   {kicker}',M,h-47,8,dark,font='Bold')
    label(c,tag,w-M,h-47,8,GOLD,'right','Bold')
    line(c,M,54,w-M,54,GRID,.55)
    label(c,footer,M,38,7.5,MUTED)
    label(c,tag,w-M,38,8.5,GOLD,'right','Bold')
    return h-83


def practice_leaf(year,sid,section,work,size):
    buffer=io.BytesIO(); w,h=size; c=Canvas(buffer,pagesize=size,invariant=1)
    tag='P'+sid
    y=new_page(c,year,w,h,'SECTION PRACTICE',tag,'ENHANCED ORIGINAL FIRST EDITION  /  LINKED WORKED ANSWERS')
    dark=HexColor(DARKS[year]); aw=w-2*M
    y=para(c, section['title'],M,y,aw,24,27,'Heading',dark)
    y=para(c,f"Section {sid}  ·  After original page {section['printed_anchor']}",M,y-7,aw,9,13,'Label',MUTED)-20
    is_compact=sum(cmd in ('xy','hist','curve','cubic') for task in work['tasks'] for cmd,_ in task['visuals'])>=2
    for k,t in enumerate(work['tasks'],1):
        label(c,f'{sid}.{k:02d}   /   CRITERION {t["criterion"]}',M,y,8.4,GOLD,font='Bold')
        y=para(c,t['title'],M,y-7,aw,14,17,'Heading',dark)-5
        y=para(c,t['stem'],M,y,aw,11)-9
        for cmd,value in t['visuals']:
            y=render_visual(c,cmd,value,M+18,y,aw-36,is_compact)
        for j,part in enumerate(t['parts']):
            label(c,f'({chr(97+j)})',M+2,y-10,9,MUTED,font='Bold')
            y=para(c,part,M+26,y,aw-26,11)-4
        y-=16 if k < len(work["tasks"]) else 6
    validate(y>=83, f'Overflow in MYP{year} {sid}: cursor at {y:.1f} pt')
    if y>=183:
        label(c,'WORKING SPACE',M,y-9,8,MUTED,font='Bold')
        for yy in range(round(y-36),96,-23):
            line(c,M,yy,w-M,yy,GRID,.45)
    label(c,'Worked answers',M,66,8,GOLD,font='Bold')
    c.showPage(); c.save()
    return pdf.open(stream=buffer.getvalue(),filetype='pdf'), round(y,1)


def front_leaf(year,size,count):
    w,h=size; buf=io.BytesIO(); c=Canvas(buf,pagesize=size,invariant=1); aw=w-2*M
    y=new_page(c,year,w,h,'READER’S GUIDE','E','SADIKOU MOUKODDIM  /  STUDENT COURSEBOOK')
    y=para(c,'Enhanced original first edition',M,y-15,aw,31,37,'Heading',HexColor(DARKS[year]))-24
    y=para(c,f'This volume keeps the original MYP {year} lessons, worked examples, investigations, assessment and reference pages. {count} new practice pages are interleaved beside the matching sections.',M,y,aw,13,21)-26
    for name,body in [
        ('Read the original page numbers as printed','The original contents, index and cross-references still use the original printed numbers. The new pages have labels like P3.2 (practice for section 3.2). The file’s physical page count therefore differs from those printed numbers.'),
        ('Find practice and check your reasoning','Use the PDF bookmarks to jump to a chapter, its original sections or the added practice. On paper, each new page appears after the printed page named in its heading. Work in a notebook, then check the added Worked Answers after the original reference material. Digital copies link each practice page to its answers.'),
        ('Read the criterion as a focus, not a grade','A  Knowing and understanding  ·  B  Investigating patterns  ·  C  Communicating  ·  D  Applying mathematics in real-life contexts. These are practice emphases, not official IB tasks or grades.'),
    ]:
        y=para(c,name,M,y,aw,15,19,'Heading',HexColor(DARKS[year]))-7
        y=para(c,body,M,y,aw,11.5,17)-20
    validate(y>80,f'Front page overflow MYP{year}')
    c.showPage(); c.save(); return pdf.open(stream=buf.getvalue(),filetype='pdf')


def solution_leaves(year,sections,practice,size):
    buf=io.BytesIO(); w,h=size; aw=w-2*M
    c=Canvas(buf,pagesize=size,invariant=1)
    locations={}; sheet=0; y=0
    def open_leaf(chapter):
        nonlocal sheet,y
        sheet+=1
        y=new_page(c,year,w,h,'WORKED ANSWERS',f'S{sheet}','ADDED PRACTICE   /   CHECK REASONING, NOT JUST RESULTS')
        y=para(c,f'Chapter {chapter} · Worked answers',M,y,aw,21,27,'Heading',HexColor(DARKS[year]))-19
    last=None
    for sid, data in practice.items():
        chapter=sid.split('.')[0]
        tasks=data['tasks']
        # Conservative fit estimation; exact checks guard against unexpected wrapping.
        estimate=30+sum(22+sum(max(1,math.ceil(len(a)/80))*13+4 for a in t['answers']) for t in tasks)
        if chapter!=last or y-estimate<71:
            if sheet: c.showPage()
            open_leaf(chapter)
        last=chapter
        locations[sid]=(sheet-1,round(h-y,1))
        y=para(c,f'P{sid}  ·  {sections[sid]["title"]}',M,y,aw,11.5,16,'Heading',HexColor(DARKS[year]))-4
        for n,t in enumerate(tasks,1):
            label(c,f'{sid}.{n:02d}  /  {t["title"]}',M+2,y-8,8.8,GOLD,font='Bold')
            y-=15
            for j,a in enumerate(t['answers']):
                label(c,f'({chr(97+j)})',M+3,y-9,8,MUTED,font='Bold')
                y=para(c,a,M+23,y,aw-23,9.5,13)-3
        y-=11
        validate(y>=60, f'Solution page overflow MYP{year} {sid}: {y:.1f}')
    c.showPage(); c.save()
    return pdf.open(stream=buf.getvalue(),filetype='pdf'),locations


def roman(n):
    result=''
    for a,name in ((10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')):
        while n>=a: n-=a;result+=name
    return result


def original_label(i,offset):
    if not offset: return str(i+1)
    if i==0: return 'Cover'
    if i<offset: return roman(i)
    return str(i+1-offset)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def myp3_named_pages(spec):
    """Resolve anchors missing from the uploaded MYP3 PDF's catalog.

    All destinations are the one-based printed pages of the original contents.
    """
    pages = dict(how=7, framework=9, criteria=12, map=14, notation=16,
                 cumulative=231, answers=239, formulas=269, glossary=271,
                 index=273, references=274)
    pages.update((f'ch-{ch}', row['start']) for ch,row in spec['chapters'].items() if ch.isdigit())
    pages.update(('sec-'+row['id'].replace('.', '-'), row['start'])
                 for row in spec['sections'] if row['id'][0].isdigit())
    for ch, triple in enumerate([(32,32,34),(48,48,51),(65,65,68),(85,85,88),
                                 (104,104,107),(128,128,131),(149,150,152),
                                 (174,174,177),(199,200,202),(225,225,228)], 1):
        pages.update((f'sec-{ch}-{name}', page) for name,page in zip(('inv','app','summary'),triple))
    return {name: page-1 for name,page in pages.items()}


def original_dests(original, out, original_pages, named_pages):
    """PyMuPDF only copies intra-document links inside each consecutive inserted run.

    Restore original internal page links across runs, using the preserved page mapping.
    """
    for index,new in original_pages.items():
        for link in original[index].get_links():
            target = None
            if link['kind']==pdf.LINK_GOTO:
                target=link.get('page',-1)
            elif link['kind']==pdf.LINK_NAMED and named_pages:
                target=named_pages[link['nameddest']]
            if target in original_pages:
                dest=original_pages[target]
                if not any(l['kind']==pdf.LINK_GOTO and l.get('page')==dest and l['from']==link['from'] for l in out[new].get_links()):
                    out[new].insert_link({'kind':pdf.LINK_GOTO,'from':link['from'],
                                         'page':dest,'to':link.get('to',pdf.Point(0,0))})


def build(year,spec,export,verify_only=False):
    rel,expected=SOURCES[year]; src=ROOT/rel
    validate(sha(src.read_bytes())==expected, f'Source hash mismatch: {src}')
    original=pdf.open(src); size=tuple(original[0].rect)[2:]; width,height=size
    sections={row['id']:row for row in spec['sections']}; offset=spec['offset']
    practice=read_practice(year)
    validate(not set(practice)-set(sections), f'Unmapped MYP{year}: {set(practice)-set(sections)}')
    missing=[key for key,d in sections.items() if key not in practice and d['kind'] in ('concept','application')]
    validate(not missing, f'Missing MYP{year} section(s): {missing}')
    order=list(sections)
    validate(list(practice)==[sid for sid in order if sid in practice], f'Out of order MYP{year}')
    insertions=defaultdict(list); bottom_clearance={}
    for sid in practice:
        row=sections[sid]; after=row['after']
        validate(offset+row['start']<=after<len(original), f'Invalid anchor {year}/{sid}')
        insertions[after].append(sid)
    path_out=export/f'MYP{year}-Student-Coursebook-Enhanced-Original-First-Edition.pdf'
    if verify_only:
        with pdf.open(path_out) as finished:
            result=inspect_pdf(year,original,finished,spec,practice,insertions)
        original.close()
        return result
    out=pdf.open(); original_pages={}; practice_pages={}; labels=[]
    solution_after = len(original)-(1 if year in (1,2,3) else 0)
    boundaries=sorted({1,solution_after,len(original),*insertions})
    prev=0
    for after in boundaries:
        start=len(out)
        out.insert_pdf(original,from_page=prev,to_page=after-1,final=after==len(original))
        for idx in range(prev,after):
            dest=start+idx-prev;original_pages[idx]=dest
            labels.append(dict(startpage=dest,prefix=original_label(idx,offset),style=''))
        prev=after
        if after==1:
            labels.append(dict(startpage=len(out),prefix='E',style=''))
            guide=front_leaf(year,size,len(practice))
            out.insert_pdf(guide); guide.close()
        for sid in insertions[after]:
            inset,end=practice_leaf(year,sid,sections[sid],practice[sid],size)
            practice_pages[sid]=len(out); bottom_clearance[sid]=end
            labels.append(dict(startpage=len(out),prefix='P'+sid,style='')); out.insert_pdf(inset); inset.close()
        if after==solution_after:
            solution_start=len(out)
            solutions,places=solution_leaves(year,sections,practice,size)
            labels.append(dict(startpage=len(out),prefix='S',style='D',firstpagenum=1))
            out.insert_pdf(solutions); solutions.close()
    original_dests(original,out,original_pages,myp3_named_pages(spec) if year==3 else {})
    bookmarks=[[1,'Reader’s guide',2]]
    for ch,row in spec['chapters'].items():
        bookmarks.append([1,f'{ch} · {row["title"]}',original_pages[row['start']+offset-1]+1])
        for sid,d in sections.items():
            if not sid.startswith(ch+'.'): continue
            bookmarks.append([2,f'{sid} · {d["title"]}',original_pages[d['start']+offset-1]+1])
            if sid in practice:
                bookmarks.append([3,f'P{sid} · Added practice',practice_pages[sid]+1])
    original_reference={1:216,2:222,3:239,4:363,5:245}[year]
    bookmarks.append([1,'Original reference material',original_pages[original_reference+offset-1]+1])
    if year == 3:
        bookmarks.append([1,'Original MYP3 supplementary section',original_pages[274]+1])
    bookmarks.append([1,'Worked answers · Added practice',solution_start+1])
    last=None
    for sid,(index,y) in places.items():
        ch=sid.split('.')[0]
        if ch!=last:
            bookmarks.append([2,f'Chapter {ch} · Worked answers',solution_start+index+1]); last=ch
        page_out=solution_start+index
        out[practice_pages[sid]].insert_link(dict(kind=pdf.LINK_GOTO,**{'from':pdf.Rect(M,height-76,M+128,height-59)},page=page_out,to=pdf.Point(0,max(0,y-23))))
        out[page_out].insert_link({'kind':pdf.LINK_GOTO,'from':pdf.Rect(M,y-2,width-M,y+16),'page':practice_pages[sid],'to':pdf.Point(0,0)})
    if year in (1,2,3):
        bookmarks.append([1,'Original back cover',original_pages[len(original)-1]+1])
    out.set_toc(bookmarks,collapse=2); out.set_page_labels(labels)
    out.set_metadata({**{k:v for k,v in original.metadata.items() if k not in ('format','encryption')},'title':f'MYP{year} Mathematics Student Coursebook — Enhanced Original First Edition','author':'Sadikou Moukoddim','subject':'Original first-edition pages with integrated section practice and worked answers','creator':'Enhanced first edition interleaving workflow'})
    out.save(path_out,garbage=4,deflate=True,compression_effort=2,no_new_id=True)
    out.close()
    with pdf.open(path_out) as finished:
        result=inspect_pdf(year,original,finished,spec,practice,insertions)
    original.close()
    result['lowest_exercise_cursor_pt']=min(bottom_clearance.values())
    return result


def inspect_pdf(year,original,out,spec,practice,insertions):
    """Verify every copied page's streams and geometry, insertion and navigation."""
    expected_labels=['E',*('P'+sid for sid in practice)]; new_labels=set(expected_labels)
    copied=[]; leaves=[]; solutions=[]; blanks=[]; seen=[]; visual_counts=defaultdict(int)
    for p in out:
        tag=p.get_label()
        if tag.startswith('S') and tag[1:].isdigit():
            solutions.append(p.number)
            validate('Worked answers' in p.get_text(),f'Missing solution text: MYP{year} {tag}')
        elif tag in new_labels:
            leaves.append(p.number);seen.append(tag)
            t=p.get_text()
            validate('ENHANCED ORIGINAL FIRST EDITION' in t or tag=='E', f'Missing footer: MYP{year} {tag}')
            if tag!='E':
                sid=tag[1:]
                for k, task in enumerate(practice[sid]['tasks'],1):
                    validate(f'{sid}.{k:02d}' in t, f'Missing exercise MYP{year} {sid}.{k:02d}')
                    for name,_ in task['visuals']: visual_counts[name]+=1
                validate(len(p.get_links())==1, f'No unique answer link: {tag}')
            rendered=p.get_pixmap(matrix=pdf.Matrix(.18,.18),colorspace=pdf.csGRAY,alpha=False)
            validate(max(rendered.samples)-min(rendered.samples)>=40, f'Blank newly rendered page: MYP{year} {tag}')
            for rect in p.get_text('blocks'):
                validate(rect[0]>=42 and rect[2]<=p.rect.width-34 and rect[1]>=29 and rect[3]<=p.rect.height-28,
                         f'Text outside page margins MYP{year} {tag}: {rect[:4]}')
        else:
            idx=len(copied)
            validate(tag==original_label(idx,spec['offset']), f'Original page label {tag} not expected at {idx+1}')
            old=original[idx]
            validate(tuple(p.rect)==tuple(old.rect) and p.rotation==old.rotation and
                     tuple(p.mediabox)==tuple(old.mediabox) and tuple(p.cropbox)==tuple(old.cropbox) and
                     p.read_contents()==old.read_contents(), f'Original page altered: MYP{year}, {idx+1}')
            if not old.read_contents() and not old.get_text().strip(): blanks.append(idx+1)
            copied.append(p.number)
            wanted=insertions[idx+1]
            pnext=p.number+1+(idx==0)
            validate(all(out[pnext+j].get_label()=='P'+sid for j,sid in enumerate(wanted)), f'Wrong anchor after {idx+1}')
    validate(len(copied)==len(original) and seen==expected_labels, f'Page ordering error: MYP{year}')
    validate(bool(out.get_toc()), f'Missing bookmarks: MYP{year}')
    render_blank = []
    for k in spec['original_render_blank_pages']:
        screen = original[k-1].get_pixmap(matrix=pdf.Matrix(.09,.09),colorspace=pdf.csGRAY,alpha=False)
        validate(not original[k-1].get_text().strip() and max(screen.samples)-min(screen.samples)<4,
                 f'Original blank-page record has drifted: {year}/{k}')
        render_blank.append(k)
    # Render a deterministic sample spanning the original volume to check resources, not only commands.
    sample=sorted(set([0,1,len(original)-1]+list(range(6,len(original),13))))
    for k in sample:
        params={'matrix':pdf.Matrix(.30,.30),'alpha':False,'annots':False}
        validate(original[k].get_pixmap(**params).samples==out[copied[k]].get_pixmap(**params).samples,
                 f'Original page render changed: MYP{year}, {k+1}')
    for p in leaves[1:]:
        target=out[p].get_links()[0]['page']; ty=out[p].get_label()
        validate(target in solutions and ty in out[target].get_text() and
                 any(l.get('page')==p for l in out[target].get_links()), f'Broken reciprocal navigation: MYP{year} {ty}')
    restored_links=0
    if year==3:
        names=myp3_named_pages(spec)
        for idx,dest in enumerate(copied):
            actual=out[dest].get_links()
            for source in original[idx].get_links():
                if source['kind']!=pdf.LINK_NAMED:
                    continue
                page=copied[names[source['nameddest']]]
                validate(any(link['kind']==pdf.LINK_GOTO and link['from']==source['from'] and
                             link.get('page')==page for link in actual),
                         f'Missing restored MYP3 anchor: {source["nameddest"]} from page {idx+1}')
                restored_links+=1
    return dict(**({'restored_original_links':restored_links} if year==3 else {}),
                original_pages=len(original), output_pages=len(out), practice_pages=len(practice),
                worked_answer_pages=len(solutions), exercises=sum(len(s['tasks']) for s in practice.values()),
                exercise_parts=sum(len(t['parts']) for s in practice.values() for t in s['tasks']),
                visuals=dict(sorted(visual_counts.items())),original_render_samples=len(sample),
                source_empty_pdf_pages=blanks, original_render_blank_pages=render_blank, filename=Path(out.name).name)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--years',nargs='+',type=int,choices=range(1,6),default=list(range(1,6)))
    parser.add_argument('--out',type=Path,default=HOME/'books')
    parser.add_argument('--verify-only',action='store_true')
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=True)
    register_fonts()
    spec=json.loads((HOME/'source'/'inventory.json').read_text()); results={}
    for i in args.years:
        results[i]=build(i,spec[str(i)],args.out,args.verify_only)
        print(f'MYP{i}: {json.dumps(results[i],ensure_ascii=False)}',flush=True)
    if not args.verify_only and args.years==list(range(1,6)):
        (HOME/'build-report.json').write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__':
    main()
