import fs from 'node:fs';
import path from 'node:path';

const C = {ink:'#182c2a', green:'#0d2a28', rust:'#b24f32', gold:'#d7a55d', cream:'#fbf6ec', sand:'#e7ddca', blue:'#38566e', pale:'#eef3f4'};
const font = `font-family="Inter, Arial, sans-serif"`;
function svg(title, desc, body, w=680, h=150){
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" role="img" aria-labelledby="title desc"><title id="title">${title}</title><desc id="desc">${desc}</desc>${body}</svg>`;
}
function line(x1,y1,x2,y2,stroke=C.ink,width=2,extra=''){return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="${width}" ${extra}/>`;}
function text(x,y,s,size=16,fill=C.ink,anchor='middle',weight=500){return `<text x="${x}" y="${y}" font-size="${size}" fill="${fill}" text-anchor="${anchor}" font-weight="${weight}" ${font}>${s}</text>`;}
function numberLine(name, desc, min, max, marks, labels, y=78, ticks=null){
  const x0=45,x1=635, X=v=>x0+(v-min)/(max-min)*(x1-x0);
  let b=line(x0,y,x1,y,C.ink,2.5)+`<path d="M ${x1} ${y} l -10 -6 v 12 z" fill="${C.ink}"/>`;
  const tickValues=ticks||Array.from({length:Math.floor(max-min)+1},(_,i)=>min+i);
  for(const v of tickValues){b+=line(X(v),y-6,X(v),y+6,C.ink,1.5);b+=text(X(v),y+27,String(Number(v.toFixed(3))),12);}
  for(const m of marks){b+=`<circle cx="${X(m.v)}" cy="${y}" r="6" fill="${m.color||C.rust}"/>`;b+=text(X(m.v),y-18,m.label,15,m.color||C.rust,'middle',700);}
  return svg(name, desc, b, 680, 135);
}
export function generateDiagrams(outDir){
  fs.mkdirSync(outDir,{recursive:true});
  const figs={};
  figs['number-line-integers']=numberLine('Integer number line','A horizontal number line from minus five to five. Values increase from left to right. Points are marked at minus four, zero and two point five.',-5,5,[{v:-4,label:'−4'},{v:0,label:'0',color:C.green},{v:2.5,label:'2.5',color:C.blue}],'Integers and the rational number 2.5 on the same number line.');
  figs['decimal-zoom']=numberLine('Zoomed decimal number line','A number line zooms from 3.50 to 3.52 and is divided into thousandths. Points show 3.501 and 3.512, both of which lie between 3.5 and 3.6.',3.5,3.52,[{v:3.501,label:'3.501',color:C.blue},{v:3.512,label:'3.512',color:C.rust}],'A zoomed interval showing that many decimals lie between 3.5 and 3.6.',78,[3.5,3.502,3.504,3.506,3.508,3.51,3.512,3.514,3.516,3.518,3.52]);
  // Rounding line uses custom ticks at 39.9, 39.95, 40.0
  {
    const X=v=>70+(v-39.9)/0.1*540; let b=line(70,80,610,80,C.ink,2.5);
    for(const [v,l] of [[39.9,'39.9'],[39.95,'39.95'],[40.0,'40.0']]){b+=line(X(v),70,X(v),90,C.ink,2);b+=text(X(v),116,l,16);}
    b+=`<circle cx="${X(39.95)}" cy="80" r="7" fill="${C.rust}"/>`;b+=text(X(39.95),48,'halfway',15,C.rust,'middle',700);
    b+=`<path d="M ${X(39.95)+12} 62 Q ${X(40)-20} 34 ${X(40)-4} 66" fill="none" stroke="${C.rust}" stroke-width="2"/><path d="M ${X(40)-4} 66 l -10 -3 l 5 9 z" fill="${C.rust}"/>`;
    figs['rounding-carry']=svg('Rounding with a carry','39.95 is halfway between 39.9 and 40.0. Under the usual convention, a 5 in the next place rounds up to 40.0.',b,680,145);
  }
  // Place-value chart
  {
    const cols=[['Thousands','3'],['Hundreds','0'],['Tens','4'],['Ones','8'],['Tenths','3'],['Hundredths','0'],['Thousandths','7']];
    const w=88,h=72,x0=26,y0=24; let b='';
    cols.forEach((c,i)=>{const x=x0+i*w; const dec=i>=4; b+=`<rect x="${x}" y="${y0}" width="${w}" height="${h}" fill="${dec?'#eef3f4':'#f5eee2'}" stroke="${C.sand}"/>`;b+=text(x+w/2,y0+20,c[0],11,C.ink,'middle',600);b+=text(x+w/2,y0+55,c[1],28,i===2?C.rust:C.green,'middle',700);});
    b+=`<circle cx="${x0+3.5*w}" cy="${y0+h+14}" r="4" fill="${C.rust}"/>`;b+=text(x0+3.5*w,y0+h+38,'decimal point',12,C.rust);
    figs['place-value-chart']=svg('Place-value chart for 3048.307','Columns show thousands, hundreds, tens, ones, tenths, hundredths and thousandths. The digits are 3, 0, 4, 8, 3, 0, 7. The highlighted 4 is in the tens place.',b,680,160);
  }
  // Nested number families
  {
    let b=`<rect x="30" y="18" width="620" height="150" rx="16" fill="#eef3f4" stroke="${C.blue}"/>`;
    b+=text(52,44,'Rational numbers',16,C.blue,'start',700);
    b+=`<rect x="70" y="58" width="540" height="94" rx="14" fill="#f5eee2" stroke="${C.gold}"/>`+text(90,84,'Integers',15,C.ink,'start',700);
    b+=`<rect x="110" y="96" width="460" height="44" rx="12" fill="#fbf6ec" stroke="${C.sand}"/>`+text(130,124,'Whole numbers',14,C.ink,'start',700);
    b+=`<rect x="300" y="101" width="250" height="34" rx="10" fill="#ffffff" stroke="${C.rust}"/>`+text(320,124,'Natural numbers: 1, 2, 3, …',13,C.rust,'start',700);
    b+=text(40,124,'−3',15,C.ink,'start',700)+text(150,124,'0',15,C.ink,'start',700)+text(590,44,'2.5, 3/4',14,C.blue,'end',700);
    figs['number-families']=svg('Nested number families','Natural numbers sit inside whole numbers, which sit inside integers, which sit inside rational numbers. Zero is whole but not natural in this book. Negative integers are outside the whole numbers. Fractions such as three quarters and decimals such as 2.5 are rational.',b,680,190);
  }
  // Digit cards
  {
    let b=''; ['0','2','5','8'].forEach((d,i)=>{const x=110+i*120;b+=`<rect x="${x}" y="24" width="86" height="104" rx="10" fill="${i===0?'#f5eee2':'#fbf6ec'}" stroke="${i===0?C.gold:C.sand}" stroke-width="2"/>`;b+=text(x+43,94,d,44,C.green,'middle',700);});
    b+=text(340,154,'Use each card once. A four-digit number cannot begin with 0.',14,C.ink);
    figs['digit-cards']=svg('Digit cards','Four cards show 0, 2, 5 and 8. They are used to build four-digit numbers without repeating a digit.',b,680,175);
  }
  for(const [name,content] of Object.entries(figs)) fs.writeFileSync(path.join(outDir,name+'.svg'),content);
  return figs;
}
