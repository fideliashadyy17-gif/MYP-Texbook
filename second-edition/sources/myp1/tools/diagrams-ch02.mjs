import fs from 'node:fs';
import path from 'node:path';

const C={ink:'#182c2a',green:'#0d2a28',rust:'#b24f32',gold:'#d7a55d',cream:'#fbf6ec',sand:'#e7ddca',blue:'#38566e',pale:'#eef3f4'};
const font='font-family="Inter, Arial, sans-serif"';
const svg=(title,desc,body,w=680,h=180)=>`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${w} ${h}" role="img" aria-labelledby="title desc"><title id="title">${title}</title><desc id="desc">${desc}</desc>${body}</svg>`;
const text=(x,y,s,size=16,fill=C.ink,anchor='middle',weight=500)=>`<text x="${x}" y="${y}" font-size="${size}" fill="${fill}" text-anchor="${anchor}" font-weight="${weight}" ${font}>${s}</text>`;
const line=(x1,y1,x2,y2,stroke=C.ink,width=2)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${stroke}" stroke-width="${width}"/>`;
const rect=(x,y,w,h,fill,stroke='none',rx=0)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${fill}" stroke="${stroke}"/>`;

export function generateChapter02Diagrams(outDir){
  fs.mkdirSync(outDir,{recursive:true});
  const figs={};
  {
    let b=rect(20,18,640,150,'#ffffff',C.sand,12);
    b+=text(95,92,'3',54,C.green,'middle',700)+text(128,58,'4',28,C.rust,'middle',700);
    b+=line(122,64,170,44,C.rust,1.5)+text(235,40,'exponent: 4 factors',14,C.rust,'middle',600);
    b+=line(92,100,150,126,C.blue,1.5)+text(225,136,'base: repeated factor 3',14,C.blue,'middle',600);
    b+=text(390,88,'3 × 3 × 3 × 3',22,C.ink,'middle',600)+text(560,88,'= 81',22,C.green,'middle',700);
    b+=text(420,154,'The exponent counts factors; it is not a multiplier.',12.5,C.ink);
    figs['power-anatomy']=svg('Anatomy of a power','In 3 to the fourth power, 3 is the base and 4 is the exponent. The expanded product is 3 times 3 times 3 times 3, which equals 81.',b,680,186);
  }
  {
    const cols=[['Millions','10⁶','1,000,000'],['Hundred thousands','10⁵','100,000'],['Ten thousands','10⁴','10,000'],['Thousands','10³','1,000'],['Hundreds','10²','100'],['Tens','10¹','10'],['Ones','10⁰','1']];
    const w=92,x0=18,y0=24; let b='';
    cols.forEach((c,i)=>{const x=x0+i*w; b+=rect(x,y0,w,92,i%2?'#f5eee2':'#eef3f4',C.sand); b+=text(x+w/2,y0+20,c[0],10.5,C.ink,'middle',600); b+=text(x+w/2,y0+50,c[1],22,C.green,'middle',700); b+=text(x+w/2,y0+76,c[2],11,C.ink);});
    b+=text(340,146,'Each step left multiplies by 10; each step right divides by 10.',13,C.rust,'middle',600);
    figs['powers-of-ten-chart']=svg('Place values as powers of ten','Columns from millions to ones are labelled 10 to the sixth down to 10 to the zero, with values 1,000,000 down to 1.',b,680,164);
  }
  {
    let b=rect(18,16,644,224,'#ffffff',C.sand,12);
    // 4 by 4 square
    const sx=58,sy=52,cell=28;
    for(let r=0;r<4;r++)for(let c=0;c<4;c++)b+=rect(sx+c*cell,sy+r*cell,cell,cell,(r+c)%2?'#f5eee2':'#fbf6ec',C.gold);
    b+=text(sx+2*cell,sy+4*cell+26,'4 × 4 = 4² = 16',15,C.green,'middle',700);
    b+=text(sx+2*cell,38,'square: 16 unit squares',13,C.ink);
    // isometric cube, 4 units per edge
    const ox=386,oy=164,u=24,dx=12,dy=-12,n=4;
    const front=`${ox},${oy} ${ox+n*u},${oy} ${ox+n*u},${oy-n*u} ${ox},${oy-n*u}`;
    const top=`${ox},${oy-n*u} ${ox+n*u},${oy-n*u} ${ox+n*u+n*dx},${oy-n*u+n*dy} ${ox+n*dx},${oy-n*u+n*dy}`;
    const right=`${ox+n*u},${oy} ${ox+n*u+n*dx},${oy+n*dy} ${ox+n*u+n*dx},${oy-n*u+n*dy} ${ox+n*u},${oy-n*u}`;
    b+=`<polygon points="${top}" fill="#eef3f4" stroke="${C.blue}"/><polygon points="${right}" fill="#dfe8ec" stroke="${C.blue}"/><polygon points="${front}" fill="#f5eee2" stroke="${C.blue}"/>`;
    for(let i=1;i<n;i++){
      b+=line(ox+i*u,oy,ox+i*u,oy-n*u,C.blue,1);
      b+=line(ox,oy-i*u,ox+n*u,oy-i*u,C.blue,1);
      b+=line(ox+i*u,oy-n*u,ox+i*u+n*dx,oy-n*u+n*dy,C.blue,1);
      b+=line(ox+i*dx,oy-n*u+i*dy,ox+n*u+i*dx,oy-n*u+i*dy,C.blue,0.8);
      b+=line(ox+n*u+i*dx,oy-n*u+i*dy,ox+n*u+i*dx,oy+i*dy,C.blue,0.8);
      b+=line(ox+n*u,oy-i*u,ox+n*u+n*dx,oy-i*u+n*dy,C.blue,1);
    }
    b+=text(470,206,'4 × 4 × 4 = 4³ = 64',15,C.green,'middle',700);
    b+=text(470,228,'cube: 64 unit cubes',13,C.ink);
    figs['square-cube-models']=svg('Square and cube models','A 4 by 4 square contains 16 unit squares. A cube with edge 4 contains 4 layers of 16 unit cubes, so 4 cubed is 64.',b,680,252);
  }
  {
    let b=rect(18,16,644,164,'#ffffff',C.sand,12);
    b+=text(340,46,'7 + 2 × 3²',22,C.green,'middle',700);
    const boxes=[[110,'3² = 9','indices first'],[340,'2 × 9 = 18','then multiply'],[570,'7 + 18 = 25','then add']];
    boxes.forEach(([x,val,lab])=>{b+=rect(x-88,72,176,62,C.pale,C.blue,8);b+=text(x,98,val,17,C.ink,'middle',700);b+=text(x,121,lab,12,C.blue);});
    b+=line(198,103,252,103,C.rust,2)+`<path d="M252 103 l-9 -5 v10 z" fill="${C.rust}"/>`;
    b+=line(428,103,482,103,C.rust,2)+`<path d="M482 103 l-9 -5 v10 z" fill="${C.rust}"/>`;
    b+=text(340,161,'Brackets would change the order; without them, powers before multiplication before addition.',12.5,C.ink);
    figs['order-of-operations-flow']=svg('Order of operations flow','To evaluate 7 plus 2 times 3 squared, first square 3 to get 9, then multiply 2 by 9 to get 18, then add 7 to get 25.',b,680,190);
  }
  {
    let b=rect(18,16,644,180,'#ffffff',C.sand,12);
    const base=158,x0=120,step=140;
    for(let n=0;n<=3;n++){const layers=2**n,h=layers*8,x=x0+n*step; b+=rect(x-28,base-h,56,h,n%2?C.gold:C.blue,'none',3); b+=text(x,base+20,`n=${n}`,13,C.ink); b+=text(x,base-h-10,`${layers} layer${layers>1?'s':''}`,13,C.green,'middle',700); b+=text(x,base+40,`${(0.1*layers).toFixed(1)} mm`,12,C.ink);}
    b+=text(340,38,'Ideal model: each fold doubles the layers',14,C.rust,'middle',700);
    b+=text(340,212,'The first four stages are shown. Bar height represents layers, not paper width.',12,C.ink);
    figs['folding-stack']=svg('Doubling layers in an ideal folding model','Bars show 1, 2, 4 and 8 layers after 0, 1, 2 and 3 folds. For a sheet 0.1 millimetres thick, the modelled thicknesses are 0.1, 0.2, 0.4 and 0.8 millimetres. Later fold counts are left for the investigation.',b,680,228);
  }
  {
    let b=rect(18,16,644,150,'#ffffff',C.sand,12);
    b+=rect(42,42,270,96,C.sand,'none',8)+rect(368,42,270,96,C.pale,'none',8);
    b+=text(177,70,'3x² when x = 4',17,C.green,'middle',700)+text(177,100,'3 × 4² = 3 × 16 = 48',16,C.ink);
    b+=text(503,70,'(3x)² when x = 4',17,C.green,'middle',700)+text(503,100,'(3 × 4)² = 12² = 144',16,C.ink);
    b+=text(177,124,'Only x is squared.',12.5,C.rust);
    b+=text(503,124,'The whole product 3x is squared.',12.5,C.blue);
    figs['brackets-change-base']=svg('Brackets change the base of a power','When x is 4, 3 x squared is 48 because only x is squared. The quantity 3 x, all squared, is 144 because brackets include the factor 3 in the base.',b,680,178);
  }
  for(const [name,content] of Object.entries(figs)) fs.writeFileSync(path.join(outDir,name+'.svg'),content);
  return figs;
}
