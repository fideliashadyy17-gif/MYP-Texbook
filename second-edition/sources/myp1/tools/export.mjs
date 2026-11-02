import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {launchBrowser} from './browser.mjs';
import {withServer} from './util.mjs';

const __dirname=path.dirname(fileURLToPath(import.meta.url));
const exportsDir=path.resolve(__dirname,'../../../exports/myp1');
fs.mkdirSync(exportsDir,{recursive:true});
const chapter=Number(process.argv[2]||1);
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'.generated',`chapter-${String(chapter).padStart(2,'0')}.manifest.json`),'utf8'));
const outFile=path.join(exportsDir,`MYP1-Chapter-${String(chapter).padStart(2,'0')}-Revision-Proof.pdf`);
await withServer(4175,async base=>{
  const browser=await launchBrowser();
  try{
    const page=await browser.newPage({viewport:{width:1200,height:900}});
    await page.goto(`${base}/chapter-${String(chapter).padStart(2,'0')}.html`,{waitUntil:'networkidle'});
    await page.waitForFunction((n)=>document.querySelectorAll('.pagedjs_page').length>=n,manifest.expectedPages,{timeout:30000});
    await page.evaluate(()=>document.fonts.ready);
    await page.waitForFunction(()=>[...document.images].every(img=>img.complete),null,{timeout:30000});
    await page.waitForTimeout(750);
    await page.pdf({path:outFile,preferCSSPageSize:true,printBackground:true,displayHeaderFooter:false});
  }finally{await browser.close();}
});
console.log(`Exported ${outFile} (${fs.statSync(outFile).size} bytes)`);
