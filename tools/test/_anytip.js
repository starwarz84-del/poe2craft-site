// 리버스 '아무거나' 팁 점검(2026-11-12 도과장): node _anytip.js <샘플 레시피id…>  (테스트 서버 필요) → 비슷한 등록 레시피 칸과 팁 글, 스크린샷 shots/anytip-<id>.png
const {chromium}=require('playwright'); const fs=require('fs');
const S=JSON.parse(fs.readFileSync('/home/claude/poe2data/site/data/samples.json')).samples;
(async()=>{ const b=await chromium.launch(); for(const id of process.argv.slice(2)){ for(const lang of ['kr','en']){ const p=await b.newPage({viewport:{width:1300,height:900}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/discover.html?lang='+lang); await p.waitForTimeout(1500);
  await p.locator('textarea').first().fill(S.find(s=>s.id===id).text); await p.evaluate(()=>{ const b=[...document.querySelectorAll('button')].find(b=>/^(Analyse|분석)$/.test(b.textContent.trim())); b&&b.click(); });
  await p.waitForSelector('.simrec', {timeout:20000}).catch(()=>{}); await p.waitForTimeout(3000);
  const t=await p.evaluate(()=>[...document.querySelectorAll('.simrec .st, .anytip')].map(e=>(e.className==='anytip'?'  ▶ ':'- ')+e.textContent.trim()).join('\n'));
  console.log(`[${id} ${lang}]\n${t||'(비슷한 레시피 없음)'}${errs.length?'\n오류 '+errs.join(' | '):''}`);
  const el=await p.$('.simrec'); if(el && lang==='kr') await el.screenshot({path:__dirname+`/shots/anytip-${id}.png`}); await p.close(); } }
  await b.close(); })();
