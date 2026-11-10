const {chromium}=require('playwright');
(async()=>{const id=process.argv[2]; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1300,height:900}});
p.on('pageerror',e=>console.log('ERR',e.message, e.stack)); 
await p.goto(`http://localhost:8779/recipes.html?lang=kr#r-${id}`); await p.waitForFunction(()=>window.__rec&&__rec.booted); await p.waitForTimeout(800);
await p.click('[data-rtab="fc"]'); await p.waitForTimeout(2500); console.log(await p.$eval('.fcpane',e=>e.innerText.slice(0,300)).catch(e=>'no pane')); await b.close();})();
