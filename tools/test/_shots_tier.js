// Tier odds: emulator odds pane (tier select + Add) and builder chosen-tier odds → shots/tier-*.png
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(), errs=[];
  let p=await b.newPage({viewport:{width:1400,height:1000}}); p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/emulator.html?lang=kr'); await p.waitForTimeout(2500); await p.click('.base'); await p.waitForTimeout(500);
  const sel=await p.$('[data-otier]'); if(sel){ const opts=await sel.$$eval('option',o=>o.map(x=>x.value)); await sel.selectOption(opts[0]); await p.waitForTimeout(300); }
  const pane=await p.$('#pane'); await pane.screenshot({path:'shots/tier-emu-odds.png'});
  const before=await p.evaluate(()=>document.querySelectorAll('.mods li, .modline, [data-mod]').length);
  await p.click('[data-oadd]'); await p.waitForTimeout(400);
  await p.screenshot({path:'shots/tier-emu-added.png'});
  p=await b.newPage({viewport:{width:1400,height:1000}}); p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/builder.html?lang=kr'); await p.waitForTimeout(2500);
  const chip=await p.$$('.row.p.ok .tier:not([disabled])'); if(chip[1]) await chip[1].click(); await p.waitForTimeout(400);
  await p.screenshot({path:'shots/tier-builder.png'});
  console.log('errors', errs); await b.close(); })();
