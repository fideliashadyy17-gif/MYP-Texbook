import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import {fileURLToPath} from 'node:url';
import {launchBrowser} from '../tools/browser.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');                       // sources/myp1
const tools = path.join(root, 'tools');
const exportsDir = path.resolve(here, '../../../exports/myp1');
fs.mkdirSync(exportsDir, {recursive: true});
const outFile = path.join(exportsDir, 'MYP1-Student-Coursebook-Second-Edition.pdf');
const manifest = JSON.parse(fs.readFileSync(path.join(here, 'book.manifest.json'), 'utf8'));

const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.svg':'image/svg+xml',
  '.woff2':'font/woff2','.woff':'font/woff','.ttf':'font/ttf','.json':'application/json'};
function resolve(url) {
  const p = decodeURIComponent(url.split('?')[0]);
  if (p === '/' || p === '/book.html') return path.join(here, 'book.html');
  if (p.startsWith('/styles/')) return path.join(here, p.slice(8));
  if (p.startsWith('/assets/')) return path.join(here, 'assets', p.slice(8));
  if (p.startsWith('/vendor/katex/')) return path.join(tools, 'node_modules/katex/dist', p.slice(14));
  if (p.startsWith('/diagrams/')) return path.join(root, 'diagrams', p.slice(10));
  return null;
}
const server = http.createServer((req, res) => {
  const file = resolve(req.url || '/');
  if (!file) { res.writeHead(404); res.end('Not found'); return; }
  fs.readFile(file, (err, buf) => {
    if (err) { res.writeHead(404); res.end('Not found'); return; }
    res.writeHead(200, {'Content-Type': mime[path.extname(file)] || 'application/octet-stream',
      'Cache-Control': 'no-store'});
    res.end(buf);
  });
});
await new Promise(r => server.listen(4188, '0.0.0.0', r));
const base = 'http://127.0.0.1:4188';

const browser = await launchBrowser();
try {
  const page = await browser.newPage({viewport: {width: 1200, height: 900}});
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await page.goto(`${base}/book.html`, {waitUntil: 'networkidle'});
  await page.waitForFunction(n => document.querySelectorAll('.page').length >= n,
    manifest.pages, {timeout: 180000});
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => [...document.images].every(img => img.complete), null, {timeout: 60000});
  await page.waitForTimeout(1500);
  await page.emulateMedia({media: 'print'});
  const report = await page.evaluate(expected => {
    const pages = [...document.querySelectorAll('.page')];
    const overflow = [];
    pages.forEach((p, i) => {
      if (p.scrollHeight > p.clientHeight + 2 || p.scrollWidth > p.clientWidth + 2) {
        overflow.push({page: i + 1, id: p.dataset.pageId, scrollHeight: p.scrollHeight,
          clientHeight: p.clientHeight, scrollWidth: p.scrollWidth, clientWidth: p.clientWidth});
      }
    });
    const text = document.body.innerText;
    return {
      expected, rendered: pages.length, overflow,
      rawPlaceholders: (text.match(/\{\{[^}]*\}\}/g) || []).slice(0, 5),
      rawMath: (text.match(/\[\[math:/g) || []).length,
      katexErrors: document.querySelectorAll('.katex-error').length,
      questionIds: document.querySelectorAll('[id^="q-"]').length,
      answerIds: document.querySelectorAll('[data-answer-for]').length,
    };
  }, manifest.pages);
  fs.writeFileSync(path.join(here, 'book.layout.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify({pages: report.rendered, overflow: report.overflow.length,
    rawPlaceholders: report.rawPlaceholders.length, rawMath: report.rawMath,
    katexErrors: report.katexErrors, questions: report.questionIds, answers: report.answerIds,
    consoleErrors: errors.length}, null, 2));
  if (report.overflow.length) {
    console.error('Overflow on pages:', JSON.stringify(report.overflow.slice(0, 20)));
  }
  if (report.rendered !== report.expected) { console.error('Page count mismatch'); }
  if (!report.overflow.length && report.rendered === report.expected &&
      !report.rawPlaceholders.length && !report.rawMath && !report.katexErrors && !errors.length) {
    await page.pdf({path: outFile, preferCSSPageSize: true, printBackground: true, displayHeaderFooter: false});
    console.log(`Exported ${outFile} (${fs.statSync(outFile).size} bytes)`);
  } else {
    console.error('PDF not exported: layout or rendering checks failed.');
    process.exitCode = 1;
  }
} finally {
  await browser.close();
  server.close();
}
