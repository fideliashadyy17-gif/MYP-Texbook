import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {generateDiagrams} from './diagrams.mjs';
import katex from 'katex';

const __dirname=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(__dirname,'..');
const chapter=Number(process.argv[2]||1);
const dataPath=path.join(root,'data',`chapter-${String(chapter).padStart(2,'0')}.exercises.json`);
const data=JSON.parse(fs.readFileSync(dataPath,'utf8'));
const outDir=path.join(__dirname,'.generated');
fs.mkdirSync(outDir,{recursive:true});
generateDiagrams(path.join(root,'diagrams'));

const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const safe=s=>esc(s).replace(/&lt;(\/?)(u|b|i|sup|sub)&gt;/g,'<$1$2>').replace(/□/g,'<span class="blank-box" aria-label="blank"></span>');
const tierLabel={ready:'Ready',fluency:'Fluency',reasoning:'Reasoning',application:'Application',challenge:'Challenge',investigation:'Investigation',check:'Check',assessment:'Assessment'};
function renderItems(items){
  return `<ol class="exercises">${items.map(q=>`<li id="q-${esc(q.id)}"><span class="qid">${esc(q.id)}</span><span class="prompt">${safe(q.prompt)}<span class="tier">${esc(tierLabel[q.tier]||q.tier)}</span></span></li>`).join('')}</ol>`;
}
function exerciseBlock(group, ids=null, opts={}){
  const items=ids?group.items.filter(q=>ids.includes(q.id)):group.items;
  if(!items.length) throw new Error(`No items found for ${group.id}`);
  const cls=opts.columns?'practice-columns':'';
  return `<div class="exercise-block ${opts.class||''}" data-group="${esc(group.id)}"><h3>${esc(group.title)}</h3><p class="instructions">${esc(group.instruction||'')}</p><div class="${cls}">${renderItems(items)}</div></div>`;
}
function figure(name,caption=''){
  return `<figure><img src="/diagrams/${esc(name)}.svg" alt="${esc(caption||name)}"/><figcaption>${esc(caption)}</figcaption></figure>`;
}
function answerItem(q){
  return `<div class="answer-item" data-answer-for="${esc(q.id)}"><span class="aid">${esc(q.id)}</span><div><div class="answer-text">${safe(q.answer)}</div><div class="reasoning">${safe(q.reasoning||'')}</div></div></div>`;
}
function answerGroup(group, ids=null){
  const items=ids?group.items.filter(q=>ids.includes(q.id)):group.items;
  return `<div class="answer-group"><h3>${esc(group.title)}</h3>${items.map(answerItem).join('')}</div>`;
}
const byId=Object.fromEntries(data.groups.map(g=>[g.id,g]));
const range=(prefix,a,b)=>Array.from({length:b-a+1},(_,i)=>`${prefix}${a+i}`);
const answerPages=[
  {title:'Answers · Ready check and Practice 1.1', groups:[['ready'],['p11']]},
  {title:'Answers · Practice 1.2 and Exploration', groups:[['p12'],['explore']]},
  {title:'Answers · Practices 1.3 and 1.4', groups:[['p13'],['p14']]},
  {title:'Answers · Practice 1.5 and Checkpoint', groups:[['p15'],['check']]},
  {title:'Answers · Application and Assessment practice', groups:[['application'],['assessment']]},
  {title:'Answers · Mixed practice 1 (M1–M9)', groups:[['mixed',range('M',1,9)]]},
  {title:'Answers · Mixed practice 1 (M10–M18)', groups:[['mixed',range('M',10,18)]]},
];
const answersHtml=answerPages.map(p=>`<section class="page answer-section"><div class="kicker">Chapter ${chapter} · Answers and reasoning</div><h2>${esc(p.title)}</h2>${p.groups.map(([id,ids])=>answerGroup(byId[id],ids)).join('')}</section>`).join('\n');

let html=fs.readFileSync(path.join(root,'manuscript',`chapter-${String(chapter).padStart(2,'0')}.source.html`),'utf8');
html=html.replace(/\{\{exercise:([^}:]+)(?::([^}]+))?\}\}/g,(_,id,ids)=>{
  const g=byId[id]; if(!g) throw new Error(`Unknown exercise group ${id}`);
  const list=ids?ids.split(',').map(s=>s.trim()):null;
  const columns=ids&&list.length>4?'columns':'';
  return exerciseBlock(g,list,{columns:!!columns});
});
html=html.replace(/\{\{figure:([^}|]+)(?:\|([^}]*))?\}\}/g,(_,name,caption)=>figure(name,caption||''));
html=html.replace(/\{\{answers\}\}/g,answersHtml);
html=html.replace(/\[\[math:([\s\S]+?)\]\]/g,(_,tex)=>katex.renderToString(tex.trim(),{throwOnError:true,output:'htmlAndMathml'}));
html=html.replace(/\{\{chapter\}\}/g,String(chapter)).replace(/\{\{title\}\}/g,esc(data.title));
if(/\{\{[^}]+\}\}/.test(html)) throw new Error('Unresolved placeholder: '+html.match(/\{\{[^}]+\}\}/g).join(', '));
if(/\[\[math:/.test(html)) throw new Error('Unresolved math placeholder');
let pageNo=0;
html=html.replace(/<section class="page/g,()=>`<section id="page-${++pageNo}" class="page`);
fs.writeFileSync(path.join(outDir,`chapter-${String(chapter).padStart(2,'0')}.manifest.json`),JSON.stringify({chapter,expectedPages:pageNo,exerciseItems:data.groups.reduce((n,g)=>n+g.items.length,0)},null,2));
const full=`<!doctype html><html lang="en"><head><meta charset="utf-8"/><title>MYP 1 · Chapter ${chapter} · ${esc(data.title)}</title><link rel="stylesheet" href="/styles/book.css"/><script>window.PagedConfig={auto:true};</script><script src="/vendor/pagedjs/paged.polyfill.min.js"></script></head><body>${html}</body></html>`;
fs.writeFileSync(path.join(outDir,`chapter-${String(chapter).padStart(2,'0')}.html`),full);
fs.writeFileSync(path.join(outDir,'index.html'),`<!doctype html><meta charset="utf-8"><title>MYP 1 second edition</title><h1>MYP 1 second edition</h1><ul><li><a href="/chapter-01.html">Chapter 1 · Number systems and place value</a></li></ul>`);
console.log(`Built chapter ${chapter}: ${data.groups.reduce((n,g)=>n+g.items.length,0)} exercise items, ${answerPages.length} answer pages.`);
