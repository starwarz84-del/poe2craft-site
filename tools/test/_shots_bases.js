// Special Bases tab screenshots → shots/bases-*.png (kr desktop full, en, mobile, rune section, recipe link opens Recipes)
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(), errs=[];
  for(const [name,lang,w] of [['kr','kr',1400],['en','en',1400],['mobile','kr',390]]){
    const p=await b.newPage({viewport:{width:w,height:900}}); p.on('pageerror',e=>errs.push(e.message));
    await p.goto(`http://localhost:8779/bases.html?lang=${lang}`); await p.waitForFunction(()=>window.__bases&&__bases.booted);
    await p.screenshot({path:`shots/bases-${name}.png`, fullPage:true}); await p.close(); }
  const p=await b.newPage({viewport:{width:1400,height:900}}); p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/app.html#bases'); await p.waitForTimeout(1500);
  const f=p.frames().find(x=>x.url().includes('bases.html')); await f.fill('#q','부재'); await f.waitForTimeout(200);
  await f.click('[data-rid]'); await p.waitForTimeout(1500); console.log('hash after link:', await p.evaluate(()=>location.hash));
  console.log('errors', errs); await b.close(); })();
