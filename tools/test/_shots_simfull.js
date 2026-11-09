// Flowchart full-screen check → shots/sim-<id>-fs.png / -fs-mobile.png. usage: node _shots_simfull.js [id] (test server running)
const {chromium}=require('playwright');
(async()=>{ const id=process.argv[2]||'diztoh-crit-helmet-v2', b=await chromium.launch(), p=await b.newPage({viewport:{width:1440,height:900}});
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(`http://localhost:8779/recipes.html#r-${id}`); await p.waitForFunction(()=>window.__rec && __rec.booted);
  await p.click('[data-act="sim"]'); await p.waitForSelector('[data-simbox] .fcn');
  await p.click('[data-act="simfull"]'); await p.waitForSelector('.simbox.full'); await p.waitForTimeout(200);
  console.log('full rect', await p.$eval('.simbox.full', e=>JSON.stringify(e.getBoundingClientRect())), 'fc h', await p.$eval('.simbox.full .fc', e=>e.clientHeight));
  await p.screenshot({path:`shots/sim-${id}-fs.png`});
  await p.click('[data-simk="cMiss"][data-simv="erase"]'); await p.waitForTimeout(200); console.log('still full after toggle:', !!await p.$('.simbox.full'));
  await p.keyboard.press('Escape'); await p.waitForTimeout(200); console.log('after Esc full:', !!await p.$('.simbox.full'), 'body lock:', await p.evaluate(()=>document.body.classList.contains('simfull')));
  await p.setViewportSize({width:390,height:844}); await p.click('[data-act="simfull"]'); await p.waitForTimeout(200); await p.screenshot({path:`shots/sim-${id}-fs-mobile.png`});
  await p.click('[data-act="simfull"]'); console.log('closed by button:', !(await p.$('.simbox.full')));
  console.log('errors', errs); await b.close(); })();
