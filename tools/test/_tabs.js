// grade tabs on the crit helmet: high / bal / ess / flowchart → shots/tabs-*.png
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(), p=await b.newPage({viewport:{width:1440,height:1000}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/recipes.html?lang=kr#r-diztoh-crit-helmet-v2'); await p.waitForFunction(()=>window.__rec && __rec.booted);
  console.log('board cards for helmet:', await p.$$eval('.card', els=>els.filter(e=>e.dataset.id.startsWith('diztoh-crit-helmet')).map(e=>e.dataset.id)));
  for(const t of ['diztoh-crit-helmet-v2','diztoh-crit-helmet-v2-bal','diztoh-crit-helmet-v2-ess','fc']){
    await p.click(`[data-rtab="${t}"]`); await p.waitForTimeout(500);
    if(t==='fc') await p.waitForSelector('.fcpane .fcn');
    const info=await p.evaluate(()=>({tabs:[...document.querySelectorAll('.rtab')].map(x=>(x.classList.contains('on')?'*':'')+x.textContent), nodes:document.querySelectorAll('#detail .node').length, fc:!!document.querySelector('.fcpane .fcn')}));
    console.log(t, JSON.stringify(info)); await p.screenshot({path:`shots/tabs-${t.replace('diztoh-crit-helmet-v2','h')||'h'}.png`}); }
  console.log('errors', errs); await b.close(); })();
