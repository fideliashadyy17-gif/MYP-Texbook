"""Accurate, editable SVG mathematics for Chapter 7. Angles are mathematical degrees (CCW)."""
from math import sin, cos, tan, radians, sqrt, hypot, atan2, degrees
from html import escape

G='#0d2a28'; GOLD='#d7a55d'; RUST='#b24f32'; INK='#1d2523'; MUT='#5c6663'; PALE='#eef3ef'; SAND='#f4ead8'

def pt(x,y,r,a):
    return x+r*cos(radians(a)), y-r*sin(radians(a))

def fmt(v): return f'{v:.2f}'.rstrip('0').rstrip('.')

def line(a,b,stroke=G,sw=2,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{fmt(a[0])}" y1="{fmt(a[1])}" x2="{fmt(b[0])}" y2="{fmt(b[1])}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def label(x,y,s,fill=INK,size=17,anchor='middle',italic=False):
    style=' font-style="italic"' if italic else ''
    return f'<text x="{fmt(x)}" y="{fmt(y)}" fill="{fill}" font-size="{size}" text-anchor="{anchor}"{style}>{escape(str(s))}</text>'

def dot(p,r=3.5,fill=G): return f'<circle cx="{fmt(p[0])}" cy="{fmt(p[1])}" r="{r}" fill="{fill}"/>'

def polygon(points,stroke=G,fill='none',sw=2):
    ps=' '.join(f'{fmt(x)},{fmt(y)}' for x,y in points)
    return f'<polygon points="{ps}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'

def arc(c,r,a0,a1,stroke=RUST,sw=1.8,fill='none',dash=None):
    p0=pt(*c,r,a0); p1=pt(*c,r,a1); large=int(abs(a1-a0)>180)
    sweep=0 if a1>a0 else 1
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<path d="M {fmt(p0[0])} {fmt(p0[1])} A {r} {r} 0 {large} {sweep} {fmt(p1[0])} {fmt(p1[1])}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def sector(c,r,a0,a1,fill=SAND):
    p0=pt(*c,r,a0); p1=pt(*c,r,a1); large=int(abs(a1-a0)>180)
    return f'<path d="M {fmt(c[0])} {fmt(c[1])} L {fmt(p0[0])} {fmt(p0[1])} A {r} {r} 0 {large} 0 {fmt(p1[0])} {fmt(p1[1])} Z" fill="{fill}" stroke="none"/>'

def angle_mark(c,a0,a1,r=32,text=None,color=RUST,lr=None):
    out=arc(c,r,a0,a1,color)
    if text is not None:
        lr=lr or r+24; x,y=pt(*c,lr,(a0+a1)/2)
        out+=label(x,y+5,text,color,16)
    return out

def tick(a,b,n=1,stroke=RUST):
    mx=(a[0]+b[0])/2; my=(a[1]+b[1])/2; dx=b[0]-a[0]; dy=b[1]-a[1]; L=hypot(dx,dy)
    ux,uy=dx/L,dy/L; px,py=-uy,ux; out=''
    for k in range(n):
        off=(k-(n-1)/2)*6; cx=mx+off*ux; cy=my+off*uy
        out+=line((cx-6*px,cy-6*py),(cx+6*px,cy+6*py),stroke,2)
    return out

def right_angle(c,a0,size=13):
    p1=pt(*c,size,a0); p2=pt(*c,size,a0+90); corner=(p1[0]+p2[0]-c[0],p1[1]+p2[1]-c[1])
    return line(p1,corner,MUT,1.5)+line(corner,p2,MUT,1.5)

def svg(w,h,body,title='Mathematical diagram'):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{body}</svg>'

def around(angles,labels,start=0,c=(250,125),r=95,title='Angles around a point',cross=False):
    assert abs(sum(angles)-360)<1e-8
    out=''; cum=start; rays=[]
    for i,a in enumerate(angles):
        rays.append(cum)
        out+=sector(c,42,cum,cum+a, SAND if i%2==0 else PALE)
        out+=angle_mark(c,cum,cum+a,42,labels[i],RUST if i%2==0 else G,68)
        cum+=a
    if cross:
        for a in rays[:2]: out+=line(pt(*c,r,a),pt(*c,r,a+180))
    else:
        for a in rays: out+=line(c,pt(*c,r,a))
    out+=dot(c)
    return svg(500,250,out,title)

def straight_pair(first,lab1,lab2='x',title='Adjacent angles on a straight line'):
    c=(250,165); r=185; out=''
    out+=sector(c,48,0,first,SAND)+sector(c,48,first,180,PALE)
    out+=line(pt(*c,r,180),pt(*c,r,0))+line(c,pt(*c,r,first))
    out+=angle_mark(c,0,first,48,lab1,RUST,88)+angle_mark(c,first,180,48,lab2,G,92)
    out+=dot(c)+label(c[0]-r,c[1]+25,'A',INK,15)+label(c[0]+r,c[1]+25,'B',INK,15)
    return svg(500,220,out,title)

def right_angle_split(first=12,lab1='12°',lab2='x',title='A right angle split by a ramp'):
    c=(150,200); out=''
    ground=(450,200); post=(150,35); ramp=pt(*c,300,first)
    out+=line(c,ground)+line(c,post)+line(c,ramp,G,2)
    out+=right_angle(c,0,18)
    out+=angle_mark(c,0,first,70,lab1,RUST,105)
    out+=angle_mark(c,first,90,52,lab2,G,88)
    out+=dot(c)
    out+=label(350,226,'level ground',MUT,14)+label(96,70,'vertical post',MUT,14)
    return svg(500,250,out,title)

def parallel_map(top_labels,bottom_labels,parallel=True,acute=65,title='Two lines cut by a transversal'):
    # At each intersection: sectors 1/5 top-left, 2/6 top-right, 3/7 bottom-left, 4/8 bottom-right.
    y1,y2=72,177; x1=235; x2=x1+(y2-y1)/tan(radians(acute))
    out=line((45,y1),(455,y1))+line((45,y2),(455,y2))
    out+=line(pt(x1,y1,145,180-acute),pt(x1,y1,145,-acute))
    if parallel:
        for y in (y1,y2):
            out+=line((390,y-5),(397,y),G,1.5)+line((397,y),(390,y+5),G,1.5)
        out+=label(468,y1+5,'l',INK,17,italic=True)+label(468,y2+5,'m',INK,17,italic=True)
    # sector boundaries in math angles: east 0, up-left 115, west 180, down-right 295
    bounds=[180-acute,180,360-acute,360]
    starts=[180-acute,0,180,360-acute]  # top-left, top-right, bottom-left, bottom-right
    spans=[acute,180-acute,180-acute,acute]
    for c,labels_ in [((x1,y1),top_labels),((x2,y2),bottom_labels)]:
        for i,(a0,span,lab) in enumerate(zip(starts,spans,labels_)):
            if lab is None: continue
            out+=angle_mark(c,a0,a0+span,27,lab,RUST if str(lab).endswith('°') else G,48)
    return svg(500,240,out,title)

def numbered_parallel():
    return parallel_map(['1','2','3','4'],['5','6','7','8'],title='Eight angles formed by a transversal; lines l and m are parallel')

def triangle(Aang,Bang,Cang=None,Alab=None,Blab=None,Clab=None,vertices=('A','B','C'),ticks=None,exterior=None,title='Triangle angle diagram'):
    Cang=Cang or 180-Aang-Bang
    assert abs(Aang+Bang+Cang-180)<1e-7 and min(Aang,Bang,Cang)>0
    base=300.0; ax,ay=0.0,0.0; bx,by=base,0.0
    cx=base*tan(radians(Bang))/(tan(radians(Aang))+tan(radians(Bang))); cy=cx*tan(radians(Aang))
    scale=min(350/base,175/cy); base*=scale; cx*=scale; cy*=scale
    ox=(500-base)/2; oy=210
    A=(ox,oy); B=(ox+base,oy); C=(ox+cx,oy-cy)
    out=polygon([A,B,C])
    # vertex labels outward from centroid
    cent=((A[0]+B[0]+C[0])/3,(A[1]+B[1]+C[1])/3)
    for P,lab in zip([A,B,C],vertices):
        dx=P[0]-cent[0]; dy=P[1]-cent[1]; L=hypot(dx,dy)
        out+=label(P[0]+22*dx/L,P[1]+22*dy/L+5,lab,INK,16)
    # interior angle marks using directions toward the other vertices
    def dirang(P,Q): return degrees(atan2(P[1]-Q[1],Q[0]-P[0]))%360
    for P,Q,R,lab in [(A,B,C,Alab),(B,C,A,Blab),(C,A,B,Clab)]:
        if lab is None: continue
        a0=dirang(P,Q); a1=dirang(P,R)
        while a1<a0: a1+=360
        if a1-a0>180: a0,a1=a1,a0+360
        out+=angle_mark(P,a0,a1,25,lab,RUST,52)
    if ticks:
        sides={0:(A,B),1:(B,C),2:(C,A)}
        for idx,n in ticks.items(): out+=tick(*sides[idx],n)
    if exterior is not None:
        ext_label,extend=exterior
        E=(B[0]+extend,B[1]); out+=line(B,E,G,2)
        a0=dirang(B,C)
        out+=angle_mark(B,0,a0,30,ext_label,RUST,62)
    return svg(500,255,out,title)

def quad_angles(Aang,Bang,Cang,Dang,labels=None,title='Quadrilateral divided into two triangles'):
    assert abs(Aang+Bang+Cang+Dang-360)<1e-7
    labels=labels or [str(Aang)+'°',str(Bang)+'°',str(Cang)+'°',str(Dang)+'°']
    a1=Aang*.45; a2=Aang-a1; c1=180-Bang-a1; c2=Cang-c1
    assert min(a1,a2,c1,c2)>0 and abs(180-a2-c2-Dang)<1e-7
    A=(0,0); C=(1,0)
    def intersect(a0,c0):
        # rays from A at a0 and C at 180-c0 (above) or negative equivalents
        t=tan(radians(a0)); u=tan(radians(c0))
        x=u/(t+u); y=t*x
        return x,y
    B=intersect(a1,c1); D=intersect(-a2,-c2)
    pts=[A,B,C,D]; xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    s=min(330/(max(xs)-min(xs)),140/(max(ys)-min(ys)))
    ox=250-s*(max(xs)+min(xs))/2; oy=125+s*(max(ys)+min(ys))/2
    P=[(ox+s*x,oy-s*y) for x,y in pts]
    out=polygon(P)+line(P[0],P[2],GOLD,1.8,'5 4')
    cent=(sum(p[0] for p in P)/4,sum(p[1] for p in P)/4)
    for p,lab,v in zip(P,labels,['A','B','C','D']):
        dx=p[0]-cent[0]; dy=p[1]-cent[1]; L=hypot(dx,dy)
        out+=label(p[0]+38*dx/L,p[1]+38*dy/L+5,lab,RUST if '?' in str(lab) or 'x' in str(lab) else G,16)
        out+=label(p[0]+18*dx/L,p[1]+18*dy/L+5,v,INK,13)
    return svg(500,250,out,title)

def regular_polygon(n,triangulate=False,angle_labels=False,interior_point=False,title=None):
    c=(250,122); r=96; start=90
    P=[pt(*c,r,start+360*k/n) for k in range(n)]
    out=polygon(P)
    if triangulate:
        for k in range(2,n-1): out+=line(P[0],P[k],GOLD,1.7)
        for k in range(1,n-1):
            tri=[P[0],P[k],P[k+1]]; cx=sum(p[0] for p in tri)/3; cy=sum(p[1] for p in tri)/3
            out+=label(cx,cy+5,str(k),G,16)
    if interior_point:
        for p in P: out+=line(c,p,GOLD,1.5)
        out+=dot(c,4,RUST)+label(c[0]+14,c[1]-8,'O',RUST,15)
    if angle_labels:
        for k,p in enumerate(P):
            dx=c[0]-p[0]; dy=c[1]-p[1]; L=hypot(dx,dy)
            out+=label(p[0]+30*dx/L,p[1]+30*dy/L+5,f'{(n-2)*180/n:g}°',G,13)
    for p in P: out+=dot(p,2.5)
    return svg(500,250,out,title or f'Regular {n}-gon')

def perp_bisector(length=8,radius=5,complete=True,title='Perpendicular bisector construction'):
    s=30; c=(250,130); A=(250-length*s/2,130); B=(250+length*s/2,130); r=radius*s
    out=line(A,B)+dot(A)+dot(B)+label(A[0]-8,A[1]+25,'A',INK,16)+label(B[0]+8,B[1]+25,'B',INK,16)
    out+=label(250,158,f'{length:g} cm',MUT,15)
    if r>length*s/2:
        h=sqrt(r*r-(length*s/2)**2); P=(250,130-h); Q=(250,130+h)
        for C in (A,B):
            a=degrees(atan2(C[1]-P[1],P[0]-C[0]))
            b=degrees(atan2(C[1]-Q[1],Q[0]-C[0]))
            out+=arc(C,r,a-16,a+16,GOLD,1.7,dash='5 4')
            if complete: out+=arc(C,r,b-16,b+16,GOLD,1.7,dash='5 4')
        if complete:
            out+=line((250,P[1]-18),(250,Q[1]+18),RUST,2)+dot(P)+dot(Q)+right_angle((250,130),0)
            out+=label(P[0]+15,P[1]-8,'P',RUST,16)+label(Q[0]+15,Q[1]+18,'Q',RUST,16)+label(264,151,'M',INK,14)
        else:
            out+=dot(P)+label(P[0]+15,P[1]-8,'P',RUST,16)
    return svg(500,270,out,title)

def angle_bisector(total=64,labels=None,complete=True,title='Angle bisector construction'):
    O=(115,150); half=total/2; r1=88; r2=74
    P=pt(*O,r1,half); Q=pt(*O,r1,-half)
    dx=sqrt(r2*r2-(r1*sin(radians(half)))**2)
    R=(O[0]+r1*cos(radians(half))+dx,O[1])
    out=line(O,pt(*O,285,half))+line(O,pt(*O,285,-half))+dot(O)+label(O[0]-18,O[1]+6,'O',INK,16)
    out+=arc(O,r1,-half-10,half+10,GOLD,1.7,dash='5 4')+dot(P)+dot(Q)
    out+=label(P[0]+8,P[1]-12,'P',INK,15)+label(Q[0]+8,Q[1]+22,'Q',INK,15)
    if complete:
        for C in (P,Q):
            a=degrees(atan2(C[1]-R[1],R[0]-C[0]))
            out+=arc(C,r2,a-20,a+20,GOLD,1.7,dash='5 4')
        out+=line(O,(R[0]+90,O[1]),RUST,2)+dot(R)+label(R[0]+8,R[1]-12,'R',RUST,16)
        labs=labels or [f'{half:g}°',f'{half:g}°']
        out+=angle_mark(O,0,half,58,labs[0],RUST,105)+angle_mark(O,-half,0,58,labs[1],G,105)
    else:
        labs=labels or [f'{total:g}°','']
        out+=angle_mark(O,-half,half,58,labs[0],RUST,100)
    return svg(500,280,out,title)

def sss(a,b,c,complete=True,title='Triangle constructed from three sides'):
    # base c=AB, AC=b, BC=a; all in cm
    s=min(30,360/c); A=((500-c*s)/2,210); B=(A[0]+c*s,210)
    x=(b*b+c*c-a*a)/(2*c); h2=b*b-x*x
    out=line(A,B)+dot(A)+dot(B)+label(A[0]-10,A[1]+24,'A',INK,16)+label(B[0]+10,B[1]+24,'B',INK,16)
    base_y=A[1]+24 if h2>1e-9 else A[1]-35
    out+=label((A[0]+B[0])/2,base_y,f'{c:g} cm',MUT,15)
    if h2>1e-9:
        h=sqrt(h2); C=(A[0]+x*s,A[1]-h*s)
        for O,r,other in [(A,b*s,B),(B,a*s,A)]:
            a0=degrees(atan2(O[1]-C[1],C[0]-O[0]))
            out+=arc(O,r,a0-14,a0+14,GOLD,1.7,dash='5 4')
        if complete:
            out+=line(A,C)+line(B,C)+dot(C)+label(C[0],C[1]-14,'C',INK,16)
            out+=label((A[0]+C[0])/2-24,(A[1]+C[1])/2,f'{b:g} cm',G,15)
            out+=label((B[0]+C[0])/2+24,(B[1]+C[1])/2,f'{a:g} cm',G,15)
        else:
            out+=label(C[0],C[1]-14,'apex?',RUST,15)
    elif abs(h2)<=1e-9:
        C=(A[0]+x*s,A[1]); out+=arc(A,b*s,-18,18,GOLD,1.7,dash='5 4')+arc(B,a*s,162,198,GOLD,1.7,dash='5 4')
        out+=dot(C,4,RUST)+label(C[0],C[1]-16,'arcs meet on the base',RUST,14)
        out+=label((A[0]+C[0])/2,A[1]+24,f'{b:g} cm',G,15)+label((B[0]+C[0])/2,B[1]+24,f'{a:g} cm',G,15)
        out+=label(B[0]+10,B[1]+24,'B',INK,16)
    else:
        out+=arc(A,b*s,35,85,GOLD,1.7,dash='5 4')+arc(B,a*s,95,145,GOLD,1.7,dash='5 4')
        out+=label(250,55,'arcs do not meet',RUST,15)
    return svg(500,260,out,title)

def number_line(lo=4,hi=18,integers=True,title='Possible third-side lengths'):
    x0,x1=55,455; y=110; s=(x1-x0)/20
    out=line((x0-12,y),(x1+12,y))
    for k in range(0,21,2):
        x=x0+k*s; out+=line((x,y-5),(x,y+5),G,1.5)+label(x,y+27,k,MUT,13)
    a=x0+lo*s; b=x0+hi*s
    out+=line((a,y),(b,y),GOLD,7)
    for x in (a,b): out+=f'<circle cx="{fmt(x)}" cy="{y}" r="7" fill="#fbf6ec" stroke="{RUST}" stroke-width="2.5"/>'
    if integers:
        for k in range(lo+1,hi): out+=dot((x0+k*s,y),3,G)
    out+=label(a,y-24,'4',RUST,16)+label(b,y-24,'18',RUST,16)
    out+=label(250,45,'4 < x < 18',G,20)+label(250,175,'open circles: endpoints are not allowed',MUT,14)
    return svg(500,205,out,title)

def truss(base=8,rafter=None,base_angle=None,apex_label='?',collar=False,rafter_label=None,title='Simplified roof-truss model'):
    if base_angle:
        h=(base/2)*tan(radians(base_angle)); s=min(340/base,150/h)
    else:
        h=sqrt(rafter*rafter-(base/2)**2); s=min(340/base,150/h)
    A=(250-base*s/2,200); B=(250+base*s/2,200); C=(250,200-h*s)
    out=polygon([A,B,C])+dot(A)+dot(B)+dot(C)
    if collar:
        y=(A[1]+C[1])/2; t=(A[1]-y)/(A[1]-C[1]); L=(A[0]+t*(C[0]-A[0]),y); R=(B[0]+t*(C[0]-B[0]),y)
        out+=line(L,R,GOLD,2)
    out+=label(250,228,f'{base:g} m base',MUT,15)
    if base_angle:
        out+=angle_mark(A,0,base_angle,32,f'{base_angle:g}°',RUST,62)+angle_mark(B,180-base_angle,180,32,f'{base_angle:g}°',RUST,62)
    if rafter:
        lab=rafter_label or f'{rafter:g} m'
        out+=label((A[0]+C[0])/2-28,(A[1]+C[1])/2,lab,G,15)+label((B[0]+C[0])/2+28,(B[1]+C[1])/2,lab,G,15)
    out+=label(C[0],C[1]+42,apex_label,RUST,17)
    return svg(500,255,out,title)

def gates(title='Equidistant path between two gates'):
    A=(110,140); B=(390,140); out=line(A,B,GOLD,1.5,'5 4')+line((250,35),(250,215),RUST,2)
    out+=dot(A,5)+dot(B,5)+label(A[0],A[1]+28,'Gate A',INK,15)+label(B[0],B[1]+28,'Gate B',INK,15)
    out+=right_angle((250,140),0)+label(270,55,'path',RUST,15,'start')
    return svg(500,250,out,title)

def compare_radius(title='Compass radius comparison for a 6 cm segment'):
    out=''
    for ox,r,lab,ok in [(20,60,'radius 2 cm',False),(270,120,'radius 4 cm',True)]:
        A=(ox+25,120); B=(ox+205,120); out+=line(A,B)+dot(A)+dot(B)
        out+=label(ox+115,35,lab,G,16)+label(ox+115,150,'6 cm',MUT,14)
        for C in (A,B): out+=arc(C,r,35,145,GOLD,1.6,dash='5 4')+arc(C,r,215,325,GOLD,1.6,dash='5 4')
        if ok:
            h=sqrt(r*r-90*90); out+=line((ox+115,120-h-10),(ox+115,120+h+10),RUST,2)
    return svg(520,220,out,title)

def straight_sectors(angles,labels,title='Three adjacent angles on a straight line'):
    assert abs(sum(angles)-180)<1e-8
    c=(250,170); r=185; out=line(pt(*c,r,180),pt(*c,r,0)); cum=0
    for i,(a,lab) in enumerate(zip(angles,labels)):
        out+=sector(c,48,cum,cum+a,SAND if i%2==0 else PALE)
        out+=line(c,pt(*c,r,cum))+angle_mark(c,cum,cum+a,48,lab,RUST if i%2==0 else G,92)
        cum+=a
    out+=line(c,pt(*c,r,180))+dot(c)
    return svg(500,225,out,title)

def kite(apex=40,title='Kite made from two identical isosceles triangles'):
    baseang=(180-apex)/2; base=150; h=(base/2)*tan(radians(baseang)); s=min(1,220/(2*h)); base*=s; h*=s
    L=(250-base/2,150); R=(250-base/2+base,150); T=(250,150-h); B=(250,150+h)
    out=polygon([T,R,B,L])+line(L,R,GOLD,1.6,'5 4')
    out+=angle_mark(T,270-baseang,270+baseang,24,f'{apex:g}°',RUST,48)
    out+=angle_mark(L,0,baseang,24,f'{baseang:g}°',G,48)
    out+=angle_mark(R,180-baseang,180,24,'?',RUST,48)
    out+=label(250,285,'upper and lower triangles are identical',MUT,14)
    return svg(500,300,out,title)

def two_triangles(title='Two triangles with the same angles but different sizes'):
    out=''
    for ox,scale in [(30,1.0),(285,.62)]:
        A=(ox,190); B=(ox+180*scale,190); C=(ox+70*scale,190-120*scale)
        out+=polygon([A,B,C])
        for P,lab in zip([A,B,C],['40°','60°','80°']): out+=label(P[0],P[1]-10 if P==C else P[1]+24,lab,G,14)
    return svg(500,240,out,title)

def roads(complete=True,title='Point equidistant from two roads'):
    O=(100,190); a=56
    out=line(O,pt(*O,330,0))+line(O,pt(*O,330,a))
    if complete:
        out+=line(O,pt(*O,300,a/2),RUST,2,'6 4')
        out+=angle_mark(O,0,a/2,55,f'{a/2:g}°',RUST,90)+angle_mark(O,a/2,a,55,f'{a/2:g}°',G,90)
        out+=label(365,105,'path',RUST,14)
    else:
        out+=angle_mark(O,0,a,55,f'{a:g}°',RUST,95)
    out+=label(420,212,'road 1',MUT,14)+label(300,35,'road 2',MUT,14)
    return svg(500,250,out,title)

def triangle_sum_model(Aang=55,Bang=65,title='Triangle angle sum from a parallel line'):
    Cang=180-Aang-Bang; base=300.0
    cx=base*tan(radians(Bang))/(tan(radians(Aang))+tan(radians(Bang))); cy=cx*tan(radians(Aang))
    s=min(300/base,150/cy); base*=s; cx*=s; cy*=s
    A=((500-base)/2,205); B=(A[0]+base,205); C=(A[0]+cx,205-cy)
    out=polygon([A,B,C])+line((C[0]-150,C[1]),(C[0]+150,C[1]),GOLD,2)
    out+=label(C[0]-158,C[1]+5,'l',GOLD,15)+label(C[0]+158,C[1]+5,'l',GOLD,15)
    out+=angle_mark(A,0,Aang,28,f'{Aang:g}°',RUST,55)
    out+=angle_mark(B,180-Bang,180,28,f'{Bang:g}°',RUST,55)
    # at C: left horizontal to CA is A, interior is C, CB to right horizontal is B
    aCA=degrees(atan2(C[1]-A[1],A[0]-C[0]))%360
    aCB=degrees(atan2(C[1]-B[1],B[0]-C[0]))%360
    out+=angle_mark(C,180,aCA,28,f'{Aang:g}°',G,55)
    out+=angle_mark(C,aCB,aCA,28,f'{Cang:g}°',RUST,55)
    out+=angle_mark(C,aCB,360,28,f'{Bang:g}°',G,55)
    out+=label(250,240,'line through C is parallel to AB',MUT,14)
    return svg(500,260,out,title)

def isosceles_bisector(equal=6,base=8,title='Isosceles triangle and the perpendicular bisector of its base'):
    s=28; A=(250-base*s/2,210); B=(250+base*s/2,210); h=sqrt(equal*equal-(base/2)**2)*s; C=(250,210-h)
    out=polygon([A,B,C])+line((250,C[1]-15),(250,225),RUST,1.8,'6 4')+right_angle((250,210),0)
    out+=tick(A,C,1)+tick(B,C,1)+dot(A)+dot(B)+dot(C)
    out+=label(A[0]-10,A[1]+24,'A',INK,16)+label(B[0]+10,B[1]+24,'B',INK,16)+label(C[0],C[1]-14,'C',INK,16)
    out+=label((A[0]+C[0])/2-26,(A[1]+C[1])/2,f'{equal:g} cm',G,15)+label((B[0]+C[0])/2+26,(B[1]+C[1])/2,f'{equal:g} cm',G,15)
    out+=label(250,240,f'{base:g} cm base',MUT,15)
    return svg(500,265,out,title)
