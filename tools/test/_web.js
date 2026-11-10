// deployed build (web/) end to end: every tab, a recipe + flowchart, KR/EN, mobile → errors + shots/web-*.png
const {chromium}=require('playwright'); const B=process.env.WEB||'http://localhost:8790';
(async()=>{ const b=await chromium.launch(); const errs=[]; const out=[];
  const page=async(vp)=>{ const p=await b.newPage({viewport:vp}); p.on('pageerror',e=>errs.push(`${p.url()} ${e.message}`)); p.on('console',m=>{ if(m.type()==='error' && !/ERR_TUNNEL|net::ERR_/.test(m.text())) errs.push(`console ${m.text()}`); }); p.on('requestfailed',r=>{ if(r.url().startsWith(B)) errs.push(`404? ${r.url()}`); }); p.on('response',r=>{ if(r.url().startsWith(B) && r.status()>=400) errs.push(`HTTP ${r.status()} ${r.url()}`); }); return p; };
  const p=await page({width:1500,height:950});
  for(const v of ['recipes','discover','emulator','builder','bases','about']){ await p.goto(`${B}/#${v}`); await p.waitForTimeout(2200);
    const f=p.frames().find(f=>f.url().includes(v==='recipes'?'recipes.html':`${v}.html`)); const txt=f? (await f.evaluate(()=>document.body.innerText.length)) : -1;
    out.push(`${v}: frame ${f?'ok':'MISSING'} text ${txt}`); await p.screenshot({path:`shots/web-${v}.png`}); }
  // a recipe + its flowchart
  await p.goto(`${B}/#r-xeno-phys-crossbow-v2`); await p.waitForTimeout(2500); const rf=p.frames().find(f=>f.url().includes('recipes.html'));
  out.push('recipe detail: '+(await rf.evaluate(()=>!!document.querySelector('[data-rtab="fc"]'))));
  await rf.click('[data-rtab="fc"]'); await rf.waitForSelector('.fcpane .fcn',{timeout:15000}); out.push('flowchart boxes: '+await rf.evaluate(()=>document.querySelectorAll('.fcpane .fcn').length));
  out.push('extreme banner: '+await p.evaluate(()=>document.body.classList.contains('extreme'))); await p.screenshot({path:'shots/web-recipe-fc.png'});
  // back to list
  await p.goBack(); await p.waitForTimeout(1500); out.push('after back: '+p.url());
  // English
  await p.goto(`${B}/?lang=en#recipes`); await p.waitForTimeout(2200); await p.screenshot({path:'shots/web-en.png'});
  // mobile
  const m=await page({width:390,height:844}); await m.goto(`${B}/#recipes`); await m.waitForTimeout(2500); await m.screenshot({path:'shots/web-mobile.png'});
  out.push('mobile horizontal scroll: '+await m.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1));
  console.log(out.join('\n')); console.log('ERRORS', errs.length); errs.slice(0,30).forEach(e=>console.log(' ',e)); await b.close(); })();
