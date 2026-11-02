import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(__dirname,'..');
const exportsRoot=path.resolve(root,'../../exports/myp1');
const port=Number(process.env.PORT||4173);
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.mjs':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.woff':'font/woff','.woff2':'font/woff2','.ttf':'font/ttf','.pdf':'application/pdf','.map':'application/json'};
function resolve(urlPath){
  const p=decodeURIComponent(urlPath.split('?')[0]);
  if(p==='/'||p==='/index.html') return path.join(__dirname,'.generated','index.html');
  if(/^\/chapter-\d+\.html$/.test(p)) return path.join(__dirname,'.generated',p.slice(1));
  if(p.startsWith('/styles/')) return path.join(root,'styles',p.slice(8));
  if(p.startsWith('/diagrams/')) return path.join(root,'diagrams',p.slice(10));
  if(p.startsWith('/vendor/katex/')) return path.join(__dirname,'node_modules','katex','dist',p.slice(14));
  if(p.startsWith('/vendor/pagedjs/')) return path.join(__dirname,'node_modules','pagedjs','dist',p.slice(16));
  if(p.startsWith('/vendor/fontsource/')) return path.join(__dirname,'node_modules','@fontsource',p.slice(19));
  if(p.startsWith('/exports/')) return path.join(exportsRoot,p.slice(9));
  return null;
}
const server=http.createServer((req,res)=>{
  const file=resolve(req.url||'/');
  if(!file){res.writeHead(404);res.end('Not found');return;}
  const resolved=path.resolve(file);
  const allowed=[path.join(__dirname,'.generated'),path.join(root,'styles'),path.join(root,'diagrams'),path.join(__dirname,'node_modules'),exportsRoot];
  if(!allowed.some(a=>resolved===a||resolved.startsWith(a+path.sep))){res.writeHead(403);res.end('Forbidden');return;}
  fs.readFile(resolved,(err,buf)=>{
    if(err){res.writeHead(404);res.end('Not found');return;}
    res.writeHead(200,{'Content-Type':mime[path.extname(resolved)]||'application/octet-stream','Access-Control-Allow-Origin':'*','Cache-Control':'no-store'});
    res.end(buf);
  });
});
server.listen(port,'0.0.0.0',()=>console.log(`MYP 1 preview server listening on http://0.0.0.0:${port}`));
