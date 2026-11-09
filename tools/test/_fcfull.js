// whole flowchart (full-screen mode, tall viewport) → shots/fc-<id>-<ver>.png
const {chromium}=require('playwright');
(async()=>{ const id=process.argv[2]||'diztoh-crit-helmet-v2', ver=process.argv[3]||'settle', lang=process.argv[4]||'kr', b=await chromium.launch(), p=await b.newPage({viewport:{width:1700,height:1000}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(`http://localhost:8779/recipes.html?lang=${lang}#r-${id}`); await p.waitForFunction(()=>window.__rec && __rec.booted);
  await p.click('[data-act="sim"]'); await p.waitForSelector('[data-simbox] .fcn');
  await p.click(`[data-simver="${ver}"]`); await p.click('[data-act="simfull"]'); await p.waitForTimeout(300);
  const h=await p.$eval('.fcin', e=>e.offsetHeight), w=await p.$eval('.fcin', e=>e.offsetWidth);
  await p.setViewportSize({width:Math.max(1200,w+40), height:h+200}); await p.waitForTimeout(300);
  await p.screenshot({path:`shots/fc-${id}-${ver}-${lang}.png`});
  console.log('canvas', w, h, 'errors', errs); await b.close(); })();
