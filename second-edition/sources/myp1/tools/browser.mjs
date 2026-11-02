export async function launchBrowser(){
  process.env.AWS_EXECUTION_ENV=process.env.AWS_EXECUTION_ENV||'nodejs22.x';
  const {default:chromium}=await import('@sparticuz/chromium');
  const {chromium:pw}=await import('playwright-core');
  const executablePath=await chromium.executablePath();
  return pw.launch({executablePath,args:chromium.args,headless:true});
}
