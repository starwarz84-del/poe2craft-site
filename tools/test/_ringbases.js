// 반지 일반·특수 베이스 점검(2026-11-13 도과장): node _ringbases.js (테스트 서버 8779) → 에뮬레이터·속성부여 반지 목록, 스크린샷 shots/ringbases-*.png
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); for(const [pg,hook] of [['emulator','__emu'],['builder','__S']]){ const p=await b.newPage({viewport:{width:1400,height:950}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(`http://localhost:8779/${pg}.html?lang=kr&debug`); await p.waitForTimeout(2500);
  await p.selectOption('#cats', {label:'장신구'}).catch(()=>{}); await p.waitForTimeout(600); await p.selectOption('#clss', {label:'반지'}).catch(()=>{}); await p.waitForTimeout(1500);
  const read=async()=>p.evaluate(()=>[...document.querySelectorAll('#bases .bsec span, #bases [data-bi] .bn, #bases button .nm, #bases .bname, #bases [data-bi]')].map(e=>e.innerText.replace(/\s+/g,' ').trim()).filter(Boolean).slice(0,40));
  const n=await read(); await p.screenshot({path:__dirname+`/shots/ringbases-${pg}-normal.png`});
  const btn=await p.$('#bkind [data-k="special"], [data-k="special"]'); if(btn) await btn.click(); await p.waitForTimeout(800);
  const s=await read(); await p.screenshot({path:__dirname+`/shots/ringbases-${pg}-special.png`});
  console.log(pg,'\n 일반:',n.join(' / '),'\n 특수:',s.join(' / '),'\n 오류',errs); await p.close(); } await b.close(); })();
