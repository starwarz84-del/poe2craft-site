// recipe tab detail screenshot: node _recshot.js <id> → shots/rec-<id>.png
const {chromium}=require('playwright');
(async()=>{const id=process.argv[2]; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1300,height:900}});
const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto(`http://localhost:8779/recipes.html?lang=kr#r-${id}`); await p.waitForFunction(()=>window.__rec&&__rec.booted); await p.waitForTimeout(1200);
await p.screenshot({path:`shots/rec-${id}.png`, fullPage:true}); console.log('errors',errs); await b.close();})();
