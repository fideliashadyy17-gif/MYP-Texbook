import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {launchBrowser} from './browser.mjs';
import {withServer} from './util.mjs';

const __dirname=path.dirname(fileURLToPath(import.meta.url));
const qaDir=path.resolve(__dirname,'../../../qa/myp1');
fs.mkdirSync(qaDir,{recursive:true});
const chapter=Number(process.argv[2]||1);
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'.generated',`chapter-${String(chapter).padStart(2,'0')}.manifest.json`),'utf8'));
const report=await withServer(4174,async base=>{
  const browser=await launchBrowser();
  try{
    const page=await browser.newPage({viewport:{width:1200,height:900}});
    const errors=[];
    page.on('pageerror',e=>errors.push(String(e)));
    page.on('console',m=>{if(m.type()==='error') errors.push(m.text());});
    await page.goto(`${base}/chapter-${String(chapter).padStart(2,'0')}.html`,{waitUntil:'networkidle'});
    await page.waitForFunction(()=>document.querySelectorAll('.pagedjs_page').length>0,{timeout:30000});
    await page.evaluate(()=>document.fonts.ready);
    await page.waitForTimeout(500);
    const metrics=await page.evaluate((expectedPages)=>{
      const pages=[...document.querySelectorAll('.pagedjs_page')];
      const overflow=[];
      pages.forEach((p,i)=>{
        const content=p.querySelector('.pagedjs_page_content');
        if(content && content.scrollHeight>content.clientHeight+1) overflow.push({page:i+1,scrollHeight:content.scrollHeight,clientHeight:content.clientHeight});
      });
      const ids=[...document.querySelectorAll('.pagedjs_page [id^="page-"]')].map(e=>e.id);
      const seen=new Set(), duplicateIds=[];
      for(const id of ids){if(seen.has(id)) duplicateIds.push(id); seen.add(id);}
      const missingIds=Array.from({length:expectedPages},(_,i)=>`page-${i+1}`).filter(id=>!seen.has(id));
      const pagesWithMultipleIds=pages.map((p,i)=>({page:i+1,ids:[...p.querySelectorAll('[id^="page-"]')].map(e=>e.id)})).filter(x=>x.ids.length>1);
      const text=document.body.innerText;
      return {
        expectedPages,
        sourcePages:ids.length,
        renderedPages:pages.length,
        duplicateIds,
        missingIds,
        pagesWithMultipleIds,
        overflow,
        rawPlaceholders:(text.match(/\{\{[^}]+\}\}/g)||[]),
        rawLatex:(text.match(/\\(?:frac|times|div|sqrt|left|right)\b/g)||[]),
        katexErrors:document.querySelectorAll('.katex-error').length,
        pageSizes:pages.slice(0,3).map(p=>{const r=p.getBoundingClientRect();return {w:r.width,h:r.height};}),
        textLength:text.length,
      };
    },manifest.expectedPages);
    return {chapter,errors,...metrics};
  }finally{await browser.close();}
});
report.status=(report.errors.length===0&&report.overflow.length===0&&report.rawPlaceholders.length===0&&report.rawLatex.length===0&&report.katexErrors===0&&report.renderedPages===report.expectedPages&&report.duplicateIds.length===0&&report.missingIds.length===0&&report.pagesWithMultipleIds.length===0)?'PASS':'FAIL';
const out=path.join(qaDir,`chapter-${String(chapter).padStart(2,'0')}-layout-check.json`);
fs.writeFileSync(out,JSON.stringify(report,null,2));
console.log(JSON.stringify(report,null,2));
if(report.status!=='PASS') process.exitCode=1;
