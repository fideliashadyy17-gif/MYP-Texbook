import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import katex from '../tools/node_modules/katex/dist/katex.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const file = path.join(here, 'book.html');
let html = fs.readFileSync(file, 'utf8');
let n = 0;
html = html.replace(/\[\[math:([\s\S]*?)\]\]/g, (_, tex) => {
  n += 1;
  return katex.renderToString(tex.trim(), {throwOnError: true, output: 'htmlAndMathml'});
});
const left = (html.match(/\[\[math:/g) || []).length;
if (left) { console.error('Unresolved math placeholders:', left); process.exit(1); }
fs.writeFileSync(file, html);
console.log(`Rendered ${n} mathematics expressions with KaTeX.`);
