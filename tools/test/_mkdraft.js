// 초안 만들기 화면 흐름 점검: 등록 레시피 완성품 → 필수 지정 → 확인 체크 → '레시피 초안 만들기' → 진행 문구 → 10초 이상 뒤 초안·플로우차트 검사
// node _mkdraft.js [레시피 번호=0]   (테스트 서버 필요)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForSelector('#recs');
await p.selectOption('#recs', String(+(process.argv[2]||0))); await p.waitForSelector('[data-lv]', {timeout:20000});
for(let i=0;i<3;i++){ const xs=await p.$$('[data-lv$=":must"][aria-pressed="false"]'); if(!xs.length) break; await xs[0].click(); await p.waitForTimeout(120); }
await p.check('#qrok'); const t=Date.now(); await p.click('#mk'); await p.waitForTimeout(1500);
const mid=await p.$eval('#mkmsg', e=>e.textContent).catch(()=>'' );
await p.waitForFunction(()=>window.__rev.flow && !window.__rev.flow.wait, null, {timeout:180000}); const dt=(Date.now()-t)/1000;
const out=await p.evaluate(()=>({steps:__rev.draft?.nodes.length, tried:__rev.draft?.tried, pick:__rev.draft?.pick, issues:(__rev.flow.issues||[]).length, err:__rev.flow.err||null}));
console.log('진행 문구:', mid.trim()); console.log('걸린 시간', dt.toFixed(1)+'초', JSON.stringify(out), 'page errors', errs.length, errs[0]||''); await b.close();})();
