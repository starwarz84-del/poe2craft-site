const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:900}}); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForSelector('#recs');
const i=await p.evaluate(()=>__rev.recSamples.findIndex(x=>x.id==='mazbro-proj-gloves'));
await p.selectOption('#recs',String(i)); await p.waitForTimeout(1200); await p.click('#mk'); await p.waitForTimeout(500);
const el=await p.$('#mkmsg'); await el.screenshot({path:'chk.png'}); await b.close();})();
