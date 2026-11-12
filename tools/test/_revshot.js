// 리버스 화면 확인(2026-11-12 도과장): node _revshot.js <샘플 레시피id> [폭]  — 배포 폴더 서버 8790, 샘플을 눌러 분석한 뒤 스크린샷 shots/revshot-<폭>.png
const {chromium}=require('playwright'); const [q, W]=[process.argv[2], +(process.argv[3]||1300)];
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:W, height:900}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); });
  await p.goto('http://localhost:8790/?lang=kr&_=rs'+W+'#discover'); await p.waitForTimeout(3000);
  const f=p.frames().find(f=>f.url().includes('discover.html'));
  const txt=JSON.parse(require('fs').readFileSync('/home/claude/poe2data/site/data/samples.json')).samples.find(s=>s.id===q).text;
  const ta=f.locator('textarea').first(); await ta.fill(txt); console.log('붙여넣기');
  await p.waitForTimeout(4000);
  console.log('버튼', await f.evaluate(()=>[...document.querySelectorAll('button')].map(b=>b.textContent.trim()).filter(t=>t&&t.length<20).slice(0,40).join(' / ')));
  const run=await f.evaluate(()=>{ const b=[...document.querySelectorAll('button')].find(b=>/^(Analyse|분석)$/.test(b.textContent) && !b.disabled); if(b){ b.click(); return b.textContent.trim(); } return null; }); console.log('실행', run);
  await p.waitForTimeout(40000);
  await p.screenshot({path:__dirname+`/shots/revshot-${W}.png`, fullPage:true});
  console.log('본문', (await f.evaluate(()=>document.body.innerText)).replace(/\s+/g,' ').slice(0,1500));
  console.log('오류', errs.length, errs.slice(0,3)); await b.close(); })();
