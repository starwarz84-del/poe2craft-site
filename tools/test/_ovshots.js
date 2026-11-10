// 영문 화면 긴 스크린샷 (서랍 닫고) → shots/ovs-<탭>-<폭>.png
const {chromium}=require('playwright');
const B='http://localhost:8790', TABS=process.argv[2]?process.argv[2].split(','):['emulator','builder','discover','recipes','bases','about','r-xeno-phys-crossbow-v2'], W=(process.argv[3]||'1024,390').split(',').map(Number);
(async()=>{ const br=await chromium.launch();
  for(const w of W){ const p=await br.newPage({viewport:{width:w,height:2200}}); await p.addInitScript(()=>{ try{localStorage.setItem('poe2lang','en')}catch(e){} });
    for(const t of TABS){ await p.goto(`${B}/?lang=en&_=${t}${w}#${t}`); await p.waitForTimeout(t.startsWith('r-')?3500:2400);
      const f=p.frames().find(f=>f.url().includes('emulator.html')); if(t==='emulator'&&f){ await f.evaluate(()=>document.querySelector('#drawer-close')?.click()); await p.waitForTimeout(400); }
      await p.screenshot({path:`tools/test/shots/ovs-${t}-${w}.png`}); }
    await p.close(); }
  await br.close(); })();
