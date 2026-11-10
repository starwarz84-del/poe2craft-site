const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(), p=await b.newPage({viewport:{width:1700,height:1000}});
 for(const id of process.argv.slice(2)){ await p.goto(`http://localhost:8779/recipes.html?lang=kr&_=${id}#r-${id}`); await p.waitForFunction(()=>window.__rec && __rec.booted);
  const t0=Date.now(); await p.click('[data-rtab="fc"]'); await p.waitForSelector('.fcpane .fcn'); console.log(id, Date.now()-t0,'ms'); }
 await b.close(); })();
