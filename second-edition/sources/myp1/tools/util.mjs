import {spawn} from 'node:child_process';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const __dirname=path.dirname(fileURLToPath(import.meta.url));
export async function withServer(port, fn){
  const child=spawn(process.execPath,[path.join(__dirname,'server.mjs')],{env:{...process.env,PORT:String(port)},stdio:['ignore','pipe','pipe']});
  let logs='';
  child.stdout.on('data',d=>logs+=d); child.stderr.on('data',d=>logs+=d);
  await new Promise((resolve,reject)=>{
    const t=setTimeout(()=>reject(new Error('Server start timeout: '+logs)),10000);
    child.stdout.on('data',d=>{if(String(d).includes('listening')){clearTimeout(t);resolve();}});
    child.on('exit',code=>{clearTimeout(t);reject(new Error('Server exited '+code+': '+logs));});
  });
  try{return await fn(`http://127.0.0.1:${port}`);}finally{child.kill('SIGTERM');}
}
