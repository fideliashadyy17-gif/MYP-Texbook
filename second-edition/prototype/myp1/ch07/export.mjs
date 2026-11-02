import { launchBrowser } from '../../../sources/myp1/tools/browser.mjs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.resolve(here, '../../../exports/myp1/prototype/MYP1-Chapter-07-Prototype-Revision-02.pdf');
const qa = path.resolve(here, '../../../qa/myp1/prototype');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.mkdirSync(qa, { recursive: true });
const browser = await launchBrowser();
try {
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 } });
  await page.goto('file://' + path.join(here, 'index.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  const check = await page.evaluate(() => {
    const pages = [...document.querySelectorAll('.page')];
    return pages.map((p, i) => ({ page: i + 1, id: p.dataset.pageId, clientHeight: p.clientHeight, scrollHeight: p.scrollHeight, overflow: p.scrollHeight > p.clientHeight + 2 }));
  });
  const bad = check.filter(x => x.overflow);
  fs.writeFileSync(path.join(qa, 'revision-02-layout.json'), JSON.stringify({ pages: check.length, overflow: bad, details: check }, null, 2));
  console.log(JSON.stringify({ pages: check.length, overflow: bad }, null, 2));
  if (bad.length) { console.error('Overflow detected; PDF not exported.'); process.exitCode = 1; }
  else { await page.pdf({ path: out, preferCSSPageSize: true, printBackground: true }); console.log('Exported', out); }
} finally { await browser.close(); }
