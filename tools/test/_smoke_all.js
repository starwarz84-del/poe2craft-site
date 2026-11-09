const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const ids=await p.evaluate(()=>__rec.recipes.map(r=>r.id)); let opt=0, prep=0;
for(const id of ids){ await p.goto('about:blank'); await p.goto('http://localhost:8779/recipes.html?lang=kr#r-'+id); await p.waitForFunction(()=>window.__rec&&__rec.booted); await p.waitForSelector('#detail .flow',{timeout:5000}).catch(()=>errs.push('noflow '+id));
  opt += await p.$$eval('#detail .optsum', x=>x.length); prep += await p.$$eval('#detail .prep', x=>x.length); }
console.log('recipes',ids.length,'optsum',opt,'prep',prep,'errors',errs.length, errs.slice(0,5)); await b.close();})();
