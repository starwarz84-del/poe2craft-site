// 껍데기 미러 탭 점검(2026-11-13 도과장): 배포 폴더 서버 8790 → #mirror 탭, 카드 열기, 플로우차트, 다른 탭 오가기 → shots/mirrortab-*.png
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:950}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
  await p.addInitScript(()=>{ try{ localStorage.setItem('poe2lang','kr'); }catch(e){} });
  await p.goto('http://localhost:8790/#mirror'); await p.waitForTimeout(2000);
  const f=()=>p.frames().find(x=>/recipes\.html\?mirror/.test(x.url()));
  await p.waitForFunction(()=>true); for(let i=0;i<60 && !(f() && await f().$('#board .card'));i++) await p.waitForTimeout(1000);
  console.log('탭 표시', await p.evaluate(()=>document.querySelector('.tabs a[aria-current]')?.innerText), '카드', await f().evaluate(()=>document.querySelectorAll('#board .card').length));
  await p.screenshot({path:__dirname+'/shots/mirrortab-list.png'});
  await f().click('#board .card'); for(let i=0;i<30 && !(await f().$('#detail:not([hidden])'));i++) await p.waitForTimeout(1000); await p.waitForTimeout(3000);
  console.log('상세', await f().evaluate(()=>document.querySelector('#detail h1,#detail h2')?.innerText), '플로우차트', await f().evaluate(()=>!!document.querySelector('.simbox, .fc, [data-act="sim"]')), '주소', p.url(), '불꽃', await p.evaluate(()=>document.body.classList.contains('extreme')));
  await p.screenshot({path:__dirname+'/shots/mirrortab-detail.png'});
  await p.click('.tabs a[data-view="recipes"]'); await p.waitForTimeout(3000); console.log('크래프팅으로', p.url(), await p.evaluate(()=>document.querySelector('.tabs a[aria-current]')?.innerText));
  await p.click('.tabs a[data-view="mirror"]'); await p.waitForTimeout(1000); console.log('미러로', p.url());
  console.log('오류', errs.slice(0,5)); await b.close(); })();
