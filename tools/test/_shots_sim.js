// Flowchart (simulation) view screenshots → shots/sim-<id>-*.png. usage: node _shots_sim.js [recipe id]   (test server running)
const {chromium}=require('playwright');
(async()=>{ const id=process.argv[2]||'diztoh-crit-helmet-v2', b=await chromium.launch(), p=await b.newPage({viewport:{width:1440,height:1000}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
  for(const lang of ['kr','en']){
    await p.goto(`http://localhost:8779/recipes.html?lang=${lang}#r-${id}`); await p.waitForFunction(()=>window.__rec && __rec.booted);
    await p.click('[data-act="sim"]'); await p.waitForSelector('[data-simbox] .fcn'); await p.waitForTimeout(300);
    const box=await p.$('[data-simbox]'); await box.screenshot({path:`shots/sim-${id}-${lang}.png`});
    if(lang==='kr'){ await p.$eval('[data-simbox] .fc', e=>e.style.maxHeight='none'); await (await p.$('[data-simbox]')).screenshot({path:`shots/sim-${id}-full.png`}); await p.$eval('[data-simbox] .fc', e=>e.style.maxHeight=''); }
    if(lang==='kr'){ await p.click('[data-simk="cMiss"][data-simv="erase"]'); await p.waitForTimeout(200); await (await p.$('[data-simbox]')).screenshot({path:`shots/sim-${id}-erase.png`});
      const sum=await p.$eval('[data-simbox] .simsum', e=>e.textContent); console.log('erase:', sum);
      await p.click('[data-simk="cMiss"][data-simv="settle"]'); await p.waitForTimeout(200); console.log('settle:', await p.$eval('[data-simbox] .simsum', e=>e.textContent));
      await p.setViewportSize({width:390,height:844}); await p.waitForTimeout(300); await p.screenshot({path:`shots/sim-${id}-mobile.png`});
      const ov=await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth); console.log('mobile horizontal overflow px:', ov);
      await p.setViewportSize({width:1440,height:1000}); }
  }
  console.log('errors:', errs.length, errs.slice(0,5)); await b.close(); })();
