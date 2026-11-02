import fs from 'node:fs';
import path from 'node:path';
const C={green:'#0d2a28',cream:'#fbf6ec',gold:'#d7a55d',rust:'#b24f32',sand:'#f5eee2',blue:'#38566e',pale:'#eef3f4',line:'#e7ddca',ink:'#182c2a'};
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const T=(x,y,s,o={})=>`<text x="${x}" y="${y}" font-family="Inter,Arial,sans-serif" font-size="${o.size||14}" fill="${o.fill||C.ink}" text-anchor="${o.anchor||'middle'}" font-weight="${o.weight||400}">${esc(s)}</text>`;
const L=(x1,y1,x2,y2,o={})=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${o.stroke||C.green}" stroke-width="${o.w||2}" ${o.dash?`stroke-dasharray="${o.dash}"`:''}/>`;
const R=(x,y,w,h,o={})=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${o.rx||0}" fill="${o.fill||'none'}" stroke="${o.stroke||C.green}" stroke-width="${o.sw||1.5}"/>`;
const Ci=(x,y,r,o={})=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${o.fill||'none'}" stroke="${o.stroke||C.green}" stroke-width="${o.sw||2}"/>`;
const P=(d,o={})=>`<path d="${d}" fill="${o.fill||'none'}" stroke="${o.stroke||C.green}" stroke-width="${o.w||2}" ${o.dash?`stroke-dasharray="${o.dash}"`:''}/>`;
const wrap=(w,h,body)=>`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" role="img">${body}</svg>`;
function factors(d){
  const n=d.n||36; const pairs=[]; for(let a=1;a*a<=n;a++) if(n%a===0) pairs.push([a,n/a]);
  const cols=3, cw=220, ch=54, x0=30,y0=40;
  let b=T(360,24,`Factor pairs of ${n}`,{size:18,weight:700,fill:C.green});
  pairs.forEach((p,i)=>{const x=x0+(i%cols)*cw,y=y0+Math.floor(i/cols)*ch; b+=R(x,y,190,40,{fill:i===pairs.length-1&&p[0]===p[1]?C.sand:'#fff',stroke:C.line,rx:6})+T(x+95,y+25,`${p[0]} × ${p[1]}`,{size:16,weight:600});});
  return wrap(720, y0+Math.ceil(pairs.length/cols)*ch+10,b);
}
function factorTree(d){
  const n=d.n||84; let b=T(360,24,`Prime factorisation of ${n}`,{size:18,weight:700,fill:C.green});
  const nodes=[[360,60,'84'],[220,130,'4'],[500,130,'21'],[150,210,'2'],[290,210,'2'],[430,210,'3'],[570,210,'7']];
  [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]].forEach(([a,c])=>b+=L(nodes[a][0],nodes[a][1]+18,nodes[c][0],nodes[c][1]-18,{stroke:C.line,w:2}));
  nodes.forEach(([x,y,s],i)=>{const prime=i>=3;b+=Ci(x,y,22,{fill:prime?C.sand:C.pale,stroke:prime?C.gold:C.blue})+T(x,y+5,s,{size:16,weight:700,fill:C.green});});
  b+=T(360,262,'84 = 2² × 3 × 7',{size:18,weight:700,fill:C.rust});
  return wrap(720,285,b);
}
function fractionBars(d){
  const fr=d.fractions||[[1,2],[2,4],[4,8]]; let b=''; const x0=150,w=480,h=34,gap=24;
  fr.forEach(([a,n],i)=>{const y=30+i*(h+gap); b+=T(70,y+22,`${a}/${n}`,{size:18,weight:700,anchor:'middle'}); for(let k=0;k<n;k++) b+=R(x0+k*w/n,y,w/n,h,{fill:k<a?C.gold:'#fff',stroke:C.green,sw:1});});
  b+=T(390,205,'Same whole, same shaded amount',{size:15,fill:C.blue});
  return wrap(720,225,b);
}
function fractionArea(d){
  const [a,bn]=d.a||[2,3], [c,dn]=d.b||[3,5]; const x0=180,y0=30,w=360,h=180; let b='';
  for(let i=0;i<bn;i++) for(let j=0;j<dn;j++){const shade=i<a&&j<c; b+=R(x0+j*w/dn,y0+i*h/bn,w/dn,h/bn,{fill:shade?C.gold:C.cream,stroke:C.green,sw:1});}
  b+=T(90,120,`${a}/${bn}`,{size:20,weight:700})+T(360,245,`${c}/${dn}`,{size:20,weight:700})+T(360,275,`overlap = ${a*c}/${bn*dn} = 2/5`,{size:16,fill:C.rust,weight:700});
  return wrap(720,295,b);
}
function numberLine(d){
  const x0=70,x1=650,y=120,start=d.start??0,end=d.end??1,ticks=d.ticks||10; let b=L(x0,y,x1,y,{w:2});
  for(let i=0;i<=ticks;i++){const x=x0+(x1-x0)*i/ticks; b+=L(x,y-6,x,y+6)+T(x,y+28,(start+(end-start)*i/ticks).toFixed(1),{size:12});}
  (d.points||[]).forEach(([v,label],i)=>{const x=x0+(x1-x0)*(v-start)/(end-start); b+=Ci(x,y,5,{fill:C.rust,stroke:C.rust})+L(x,y-8,x,y-45,{stroke:C.rust})+T(x,y-55,label,{size:15,weight:700,fill:C.rust});});
  return wrap(720,180,b);
}
function percentGrid(d){
  const sh=d.shaded??37; let b=T(360,24,`${sh} out of 100 squares`,{size:18,weight:700,fill:C.green}); const x0=210,y0=40,s=30;
  for(let i=0;i<100;i++){const r=Math.floor(i/10),c=i%10; b+=R(x0+c*s,y0+r*s,s-2,s-2,{fill:i<sh?C.gold:'#fff',stroke:C.line,sw:1});}
  b+=T(360,370,`${sh}% = ${sh}/100 = ${(sh/100).toFixed(2)}`,{size:18,weight:700,fill:C.rust});
  return wrap(720,390,b);
}
function multiplierFlow(d){
  const start=d.start??250, steps=d.steps||[[0.8,'20% off'],[0.9,'10% off']]; let b='',x=80,val=start;
  const box=(x,label,sub)=>R(x,70,150,70,{fill:C.pale,stroke:C.blue,rx:8})+T(x+75,100,label,{size:18,weight:700})+T(x+75,125,sub,{size:13,fill:C.blue});
  b+=box(x,`£${val}`,'start');
  steps.forEach(([m,lab],i)=>{const nx=x+(i+1)*210; val=Math.round(val*m*100)/100; b+=L(x+i*210+150,105,nx,105,{stroke:C.rust,w:2})+T((x+i*210+150+nx)/2,90,`× ${m}`,{size:14,fill:C.rust,weight:700})+T((x+i*210+150+nx)/2,125,lab,{size:12})+box(nx,`£${val}`,i===steps.length-1?'final':'after step');});
  b+=T(360,190,'Each percentage uses the current amount as its base.',{size:15,fill:C.green});
  return wrap(720,215,b);
}
function matchChain(d){
  const stages=d.stages||[1,2,3]; let b=''; const y=70,s=44;
  stages.forEach((n,i)=>{const x0=60+i*220; for(let k=0;k<n;k++){const x=x0+k*s; b+=L(x,y,x+s,y)+L(x,y+s,x+s,y+s)+L(x,y,x,y+s); if(k===n-1)b+=L(x+s,y,x+s,y+s);} b+=T(x0+n*s/2,y+80,`${n} square${n>1?'s':''}: ${3*n+1} matches`,{size:14,weight:600});});
  b+=T(360,205,'Each extra square shares one side and adds 3 matches.',{size:15,fill:C.blue});
  return wrap(720,225,b);
}
function balance(d){
  let b=T(360,24,'Keep both sides balanced',{size:18,weight:700,fill:C.green});
  b+=L(180,80,540,80,{w:3})+L(360,80,360,150,{w:3})+P('M300 150 L420 150 L390 180 L330 180 Z',{fill:C.sand,stroke:C.gold});
  b+=R(140,40,160,40,{fill:C.pale,stroke:C.blue,rx:6})+T(220,66,d.left||'3n + 5',{size:18,weight:700})+R(420,40,160,40,{fill:C.pale,stroke:C.blue,rx:6})+T(500,66,d.right||'20',{size:18,weight:700});
  b+=T(360,220,'Subtract 5 from both sides, then divide both sides by 3.',{size:15,fill:C.rust});
  return wrap(720,240,b);
}
function crossingLines(d){
  const a=d.angle??115, b=180-a; let s=L(120,140,600,140,{w:2})+L(250,40,470,240,{w:2});
  s+=T(420,120,`${a}°`,{size:18,weight:700,fill:C.rust})+T(300,120,`${b}°`,{size:18,weight:700,fill:C.blue})+T(300,190,`${a}°`,{size:18,weight:700,fill:C.rust})+T(420,190,`${b}°`,{size:18,weight:700,fill:C.blue});
  s+=T(360,270,'Vertically opposite angles are equal; adjacent angles sum to 180°.',{size:14,fill:C.green});
  return wrap(720,290,s);
}
function parallelLines(d){
  const a=d.angle??65; let s=L(100,70,620,70,{w:2})+L(100,190,620,190,{w:2})+L(250,30,470,230,{w:2,stroke:C.rust});
  s+=T(390,55,`${a}°`,{size:17,weight:700,fill:C.rust})+T(330,175,`${a}°`,{size:17,weight:700,fill:C.blue})+T(430,215,`${180-a}°`,{size:17,weight:700,fill:C.green});
  s+=T(360,265,'Corresponding and alternate angles are equal; co-interior angles sum to 180°.',{size:13,fill:C.green});
  return wrap(720,285,s);
}
function polygon(d){
  const n=d.n||6,cx=360,cy=130,r=90; let pts=[]; for(let i=0;i<n;i++){const ang=-Math.PI/2+2*Math.PI*i/n;pts.push([cx+r*Math.cos(ang),cy+r*Math.sin(ang)]);}
  let s=`<polygon points="${pts.map(p=>p.join(',')).join(' ')}" fill="${C.pale}" stroke="${C.green}" stroke-width="2"/>`;
  for(let i=1;i<n-1;i++) s+=L(pts[0][0],pts[0][1],pts[i][0],pts[i][1],{stroke:C.gold,w:1.5,dash:'4 3'});
  s+=T(360,255,`${n} sides → ${n-2} triangles → ${(n-2)*180}° interior sum`,{size:16,weight:700,fill:C.green});
  return wrap(720,280,s);
}
function compassBisector(d){
  const len=d.length||6, r=d.radius||4; const ax=210,bx=510,y=140; let s=L(ax,y,bx,y,{w:2})+Ci(ax,y,3,{fill:C.green})+Ci(bx,y,3,{fill:C.green});
  s+=P(`M ${ax+80} ${y-100} A ${r*50} ${r*50} 0 0 1 ${ax+80} ${y+100}`,{stroke:C.gold,w:1.5,dash:'5 4'})+P(`M ${bx-80} ${y-100} A ${r*50} ${r*50} 0 0 0 ${bx-80} ${y+100}`,{stroke:C.gold,w:1.5,dash:'5 4'});
  s+=L(360,40,360,240,{stroke:C.rust,w:2})+T(ax,y+25,'A',{size:16,weight:700})+T(bx,y+25,'B',{size:16,weight:700})+T(360,30,'P',{size:16,weight:700,fill:C.rust})+T(360,265,'Q',{size:16,weight:700,fill:C.rust})+T(360,290,`AB = ${len} cm; equal radii locate the perpendicular bisector.`,{size:14,fill:C.green});
  return wrap(720,310,s);
}
function subsetTree(d){
  const els=d.elements||['a','b','c']; let b=T(360,24,'Each element: in or out',{size:18,weight:700,fill:C.green});
  const levels=[[[360,60,'{}']],[[200,120,'out'],[520,120,'in']],[[120,180,'out'],[280,180,'in'],[440,180,'out'],[600,180,'in']]];
  // draw a compact binary decision diagram for three elements
  const nodes=[[360,55,'start'],[200,115,'a out'],[520,115,'a in'],[120,175,'b out'],[280,175,'b in'],[440,175,'b out'],[600,175,'b in']];
  [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]].forEach(([a,c])=>b+=L(nodes[a][0],nodes[a][1]+14,nodes[c][0],nodes[c][1]-14,{stroke:C.line}));
  nodes.forEach(([x,y,s])=>b+=R(x-55,y-14,110,28,{fill:C.pale,stroke:C.blue,rx:5})+T(x,y+5,s,{size:12}));
  const leaves=['{}','{c}','{b}','{b,c}','{a}','{a,c}','{a,b}','{a,b,c}'];
  leaves.forEach((s,i)=>{const x=60+i*86;b+=T(x,235,s,{size:12,weight:600,fill:C.green});});
  b+=T(360,270,'2 × 2 × 2 = 8 subsets',{size:16,weight:700,fill:C.rust});
  return wrap(720,290,b);
}
function venn(d){
  const [lo,both,ro,out]=d.regions||[11,6,8,5]; let b=R(40,30,640,220,{fill:C.cream,stroke:C.line,rx:8})+T(70,55,'U',{size:18,weight:700,anchor:'start'});
  b+=Ci(280,140,95,{fill:'rgba(215,165,93,0.25)',stroke:C.gold,sw:2})+Ci(440,140,95,{fill:'rgba(56,86,110,0.18)',stroke:C.blue,sw:2});
  b+=T(230,140,lo,{size:24,weight:700})+T(360,140,both,{size:24,weight:700,fill:C.rust})+T(490,140,ro,{size:24,weight:700})+T(620,210,out,{size:22,weight:700,fill:C.green});
  b+=T(230,55,d.left||'A',{size:16,weight:700})+T(490,55,d.right||'B',{size:16,weight:700})+T(360,280,`Total = ${lo} + ${both} + ${ro} + ${out} = ${d.universe||30}`,{size:15,fill:C.green});
  return wrap(720,300,b);
}
function numberSets(d){
  let b='';
  const boxes=[
    [40,30,640,240,'Real numbers (R)',C.cream,C.green],
    [70,65,440,185,'Rational numbers (Q)','#fff',C.line],
    [100,100,380,130,'Integers (Z)','#fff',C.line],
    [130,135,320,75,'Whole numbers','#fff',C.line],
    [160,165,260,35,'Natural numbers (N)','#fff',C.gold]
  ];
  boxes.forEach(([x,y,w,h,lab,fill,stroke])=>b+=R(x,y,w,h,{fill,stroke,rx:8})+T(x+12,y+20,lab,{size:13,anchor:'start',weight:600,fill:C.green}));
  b+=T(575,130,'Irrationals',{size:15,weight:700,fill:C.rust})+T(575,155,'√2, π',{size:14,fill:C.rust})+T(575,180,'(real, not rational)',{size:12,fill:C.rust});
  return wrap(720,290,b);
}
function rectangleArea(d){
  const l=d.length||7,w=d.width||4; const x0=180,y0=30,s=40; let b='';
  for(let i=0;i<w;i++)for(let j=0;j<l;j++)b+=R(x0+j*s,y0+i*s,s-2,s-2,{fill:C.pale,stroke:C.blue,sw:1});
  b+=T(x0+l*s/2,y0+w*s+30,`${l} cm`,{size:16,weight:700})+T(x0-35,y0+w*s/2,`${w} cm`,{size:16,weight:700})+T(360,250,`Area = ${l*w} cm² · Perimeter = ${2*(l+w)} cm`,{size:16,weight:700,fill:C.green});
  return wrap(720,275,b);
}
function circle(d){
  const r=d.radius||6; let b=Ci(360,130,90,{fill:C.pale,stroke:C.green,sw:2})+L(360,130,450,130,{stroke:C.rust,w:2})+L(270,130,450,130,{stroke:C.blue,w:1.5,dash:'5 4'});
  b+=T(405,120,`r = ${r}`,{size:15,weight:700,fill:C.rust})+T(360,155,`d = ${2*r}`,{size:15,weight:700,fill:C.blue})+T(360,260,'C = 2πr = πd   ·   A = πr²   ·   π ≈ 3.14',{size:16,weight:700,fill:C.green});
  return wrap(720,285,b);
}
function cuboidNet(d){
  const l=d.l||4,w=d.w||3,h=d.h||2; const s=24,rowY=95; let b='';
  const widths=[l,h,l,h]; let x=180;
  widths.forEach((ww,i)=>{b+=R(x,rowY,ww*s,w*s,{fill:i%2?C.sand:C.pale,stroke:C.green})+T(x+ww*s/2,rowY+w*s/2+5,`${ww}×${w}`,{size:12});x+=ww*s;});
  const attachX=180+l*s;
  b+=R(attachX,rowY-w*s,h*s,w*s,{fill:C.cream,stroke:C.gold})+T(attachX+h*s/2,rowY-w*s/2+5,`${h}×${w}`,{size:12});
  b+=R(attachX,rowY+w*s,h*s,w*s,{fill:C.cream,stroke:C.gold})+T(attachX+h*s/2,rowY+w*s+w*s/2+5,`${h}×${w}`,{size:12});
  b+=T(360,265,`Surface area = 2(${l}×${w} + ${l}×${h} + ${w}×${h}) = ${2*(l*w+l*h+w*h)} square units`,{size:15,weight:700,fill:C.green});
  return wrap(720,285,b);
}
function prism(d){
  const l=d.l||5,w=d.w||3,h=d.h||2; const x=220,y=70,dx=70,dy=-40; let b='';
  const front=[[x,y],[x+l*35,y],[x+l*35,y+h*35],[x,y+h*35]];
  const back=front.map(([a,c])=>[a+dx,c+dy]);
  b+=`<polygon points="${front.map(p=>p.join(',')).join(' ')}" fill="${C.pale}" stroke="${C.green}" stroke-width="2"/>`;
  b+=`<polygon points="${back.map(p=>p.join(',')).join(' ')}" fill="none" stroke="${C.green}" stroke-width="1.5" stroke-dasharray="4 3"/>`;
  front.forEach((p,i)=>b+=L(p[0],p[1],back[i][0],back[i][1],{stroke:C.green,w:1.5}));
  b+=T(x+l*35/2,y+h*35+25,`${l} cm`,{size:15,weight:700})+T(x-25,y+h*35/2,`${h} cm`,{size:15,weight:700})+T(x+l*35+45,y+dy/2,`${w} cm`,{size:15,weight:700});
  b+=T(360,235,`Volume = ${l} × ${w} × ${h} = ${l*w*h} cm³ = ${l*w*h} mL`,{size:16,weight:700,fill:C.green});
  return wrap(720,260,b);
}
function frequencyTable(d){
  const rows=d.rows||[], headers=d.headers||['Category','Frequency']; let b=T(360,24,'Frequency table',{size:18,weight:700,fill:C.green});
  const x=140,y=45,cw=[280,160],rh=36;
  b+=R(x,y,cw[0]+cw[1],rh,{fill:C.green,stroke:C.green}); headers.forEach((h,i)=>b+=T(x+(i?cw[0]+cw[1]/2:cw[0]/2),y+23,h,{size:14,weight:700,fill:C.cream}));
  rows.forEach((row,ri)=>{const yy=y+(ri+1)*rh; b+=R(x,yy,cw[0]+cw[1],rh,{fill:ri%2?C.cream:'#fff',stroke:C.line}); row.forEach((c,ci)=>b+=T(x+(ci?cw[0]+cw[1]/2:cw[0]/2),yy+23,c,{size:14,weight:ri===rows.length-1?700:400}));});
  return wrap(720,y+(rows.length+2)*rh+20,b);
}
function pieChart(d){
  const labels=d.labels||[], values=d.values||[], total=values.reduce((a,b)=>a+b,0); let ang=-Math.PI/2,b='',cx=250,cy=140,r=100; const cols=[C.gold,C.blue,C.rust,C.green];
  values.forEach((v,i)=>{const a2=ang+2*Math.PI*v/total; const x1=cx+r*Math.cos(ang),y1=cy+r*Math.sin(ang),x2=cx+r*Math.cos(a2),y2=cy+r*Math.sin(a2); const large=v/total>0.5?1:0; b+=`<path d="M ${cx} ${cy} L ${x1} ${y1} A ${r} ${r} 0 ${large} 1 ${x2} ${y2} Z" fill="${cols[i%4]}" stroke="#fff" stroke-width="2"/>`; ang=a2;});
  labels.forEach((lab,i)=>{const y=70+i*45;b+=R(430,y-15,18,18,{fill:cols[i%4],stroke:'none'})+T(460,y,`${lab}: ${values[i]} (${(values[i]/total*360).toFixed(1)}°)`,{size:14,anchor:'start'});});
  return wrap(720,280,b);
}
function histogram(d){
  const labels=d.labels||[], values=d.values||[], max=Math.max(...values,1); const x0=80,y0=200,w=560,h=150,bw=w/values.length; let b=L(x0,y0,x0+w,y0,{w:2})+L(x0,y0,x0,y0-h,{w:2});
  values.forEach((v,i)=>{const bh=v/max*h;b+=R(x0+i*bw+4,y0-bh,bw-8,bh,{fill:C.gold,stroke:C.green,sw:1})+T(x0+i*bw+bw/2,y0-bh-8,v,{size:13,weight:700})+T(x0+i*bw+bw/2,y0+22,labels[i],{size:11});});
  b+=T(360,255,'Equal interval widths; heights show frequency.',{size:14,fill:C.green});
  return wrap(720,275,b);
}
function trend(d){
  const labels=d.labels||[], values=d.values||[], max=Math.max(...values)*1.15; const x0=90,y0=200,w=540,h=150; let b=L(x0,y0,x0+w,y0,{w:2})+L(x0,y0,x0,y0-h,{w:2});
  const pts=values.map((v,i)=>[x0+i*w/(values.length-1),y0-v/max*h]);
  b+=`<polyline points="${pts.map(p=>p.join(',')).join(' ')}" fill="none" stroke="${C.rust}" stroke-width="3"/>`;
  pts.forEach(([x,y],i)=>b+=Ci(x,y,5,{fill:C.rust,stroke:C.rust})+T(x,y-12,values[i],{size:13,weight:700})+T(x,y0+24,labels[i],{size:13}));
  b+=T(360,255,'Zero-based axis; time order left to right.',{size:14,fill:C.green});
  return wrap(720,275,b);
}
const makers={factors,factor_tree:factorTree,fraction_bars:fractionBars,fraction_area:fractionArea,number_line:numberLine,percent_grid:percentGrid,multiplier_flow:multiplierFlow,match_chain:matchChain,balance, crossing_lines:crossingLines,parallel_lines:parallelLines,polygon,compass_bisector:compassBisector,subset_tree:subsetTree,venn,number_sets:numberSets,rectangle_area:rectangleArea,circle,cuboid_net:cuboidNet,prism,frequency_table:frequencyTable,pie_chart:pieChart,histogram,trend};
export function generateExtraDiagrams(dir,chapter,specs){
  fs.mkdirSync(dir,{recursive:true});
  for(const d of specs){const fn=makers[d.kind]; if(!fn) throw new Error(`Unknown diagram kind ${d.kind}`); const name=`${d.kind}-${chapter}`; fs.writeFileSync(path.join(dir,name+'.svg'),fn(d));}
}
