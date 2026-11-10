const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); for(const [w,h,n] of [[1520,950,'wide'],[1920,1000,'fhd'],[1100,900,'mid'],[390,844,'mob']]){ const p=await b.newPage({viewport:{width:w,height:h}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8779/emulator.html?lang=kr'); await p.waitForTimeout(2200);
 if(w<1280){ const c=await p.$('#drawer-close'); if(c && await c.isVisible()) await c.click(); await p.waitForTimeout(300); }
 else { await p.click('#bases .base >> nth=3'); await p.waitForTimeout(800); }
 const hs=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
 await p.screenshot({path:`shots/emu-${n}.png`}); console.log(n, 'hscroll',hs, errs); }
 await b.close(); })();
