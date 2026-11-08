const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const out=await p.evaluate(()=>{const R=__rec; const r=R.recipes.find(x=>x.id==='ragna-spell4-amulet'); const a=R.analyse(r); const f=a.final[0]; return {keys:Object.keys(a), fk:Object.keys(f), f:JSON.stringify(a.final.slice(0,3),(k,v)=>k==='g'?undefined:v).slice(0,800), q:JSON.stringify(a.qual), imp:JSON.stringify(a.imp)}});
console.log(out); await b.close();})();
