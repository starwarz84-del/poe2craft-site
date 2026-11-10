// 영문: 플로우차트 탭 + 리버스 크래프팅 분석 결과 스크린샷과 넘침 점검
const {chromium}=require('playwright');
const B='http://localhost:8790';
(async()=>{ const br=await chromium.launch();
 for(const w of [1280,390]){ const p=await br.newPage({viewport:{width:w,height:2000}}); await p.addInitScript(()=>{ try{localStorage.setItem('poe2lang','en')}catch(e){} });
  await p.goto(`${B}/?lang=en&_=fc${w}#r-diztoh-crit-helmet-v2`); await p.waitForTimeout(3500);
  const rf=p.frames().find(f=>f.url().includes('recipes.html'));
  await rf.evaluate(()=>{ const b=[...document.querySelectorAll('button,[role=tab]')].find(b=>/Flowchart/.test(b.textContent)); b&&b.click(); }); await p.waitForTimeout(3000);
  await p.screenshot({path:`tools/test/shots/ovx-fc-${w}.png`});
  await p.goto(`${B}/?lang=en&_=dc${w}#discover`); await p.waitForTimeout(2500);
  const df=p.frames().find(f=>f.url().includes('discover.html'));
  await df.evaluate(()=>{ const b=[...document.querySelectorAll('button')].find(b=>/Amulet/.test(b.textContent)); b&&b.click(); }); await p.waitForTimeout(2500);
  await p.screenshot({path:`tools/test/shots/ovx-dc-${w}.png`, fullPage:false});
  await p.close(); }
 await br.close(); })();
