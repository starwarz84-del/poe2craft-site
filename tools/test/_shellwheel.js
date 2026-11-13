// 껍데기 바깥 휠 점검(2026-11-14 도과장): node _shellwheel.js (배포 폴더 서버 8790) — 로고·좌우 여백에서 휠을 굴려 안쪽 페이지가 내려가는지, 로고가 접혀 탭 줄이 맨 위에 붙는지
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1800,height:900}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.addInitScript(()=>{ try{ localStorage.setItem('poe2lang','kr'); }catch(e){} });
  for(const tab of ['recipes','emulator','main']){ await p.goto('http://localhost:8790/#'+tab); await p.waitForTimeout(5000);
    const st=()=>p.evaluate(()=>{ const f=[...document.querySelectorAll('main iframe')].find(x=>!x.hidden); const se=f.contentDocument.scrollingElement; return {y:Math.round(se.scrollTop), max:se.scrollHeight-se.clientHeight, compact:document.body.classList.contains('compact'), tabsTop:Math.round(document.querySelector('.tabs').getBoundingClientRect().top)}; });
    const s0=await st(); await p.mouse.move(900,120); for(let i=0;i<4;i++){ await p.mouse.wheel(0,300); await p.waitForTimeout(150); } await p.waitForTimeout(500); const s1=await st();
    await p.mouse.move(40,600); for(let i=0;i<3;i++){ await p.mouse.wheel(0,300); await p.waitForTimeout(150); } await p.waitForTimeout(500); const s2=await st();
    if(tab==='recipes') await p.screenshot({path:__dirname+'/shots/shellwheel-down.png'});
    for(let i=0;i<20;i++){ await p.mouse.wheel(0,-400); await p.waitForTimeout(60); } await p.waitForTimeout(600); const s3=await st();
    console.log(tab, '처음', JSON.stringify(s0), '\n  로고에서 휠↓', JSON.stringify(s1), '\n  여백에서 휠↓', JSON.stringify(s2), '\n  휠↑ 끝까지', JSON.stringify(s3)); }
  console.log('오류', errs.slice(0,3)); await b.close(); })();
