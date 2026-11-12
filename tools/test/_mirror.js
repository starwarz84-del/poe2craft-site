// 미러 탭·한국 리그명 점검(2026-11-13 도과장): node _mirror.js  (테스트 서버 8779) → 카드 목록·리그 선택·배지, 스크린샷 shots/mirror-<언어>.png
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); for(const lang of ['kr','en']){ const p=await b.newPage({viewport:{width:1300,height:900}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(`http://localhost:8779/recipes.html?mirror&lang=${lang}`); await p.waitForSelector('#board .card',{timeout:120000}).catch(()=>{}); await p.waitForTimeout(2000);
  const x=await p.evaluate(()=>({head:document.querySelector('.mhead')?.innerText, count:document.querySelector('#count')?.innerText, lg:[...document.querySelectorAll('#flg option')].map(o=>o.textContent), patchHidden:document.querySelector('#w-patch')?.hidden,
    cards:[...document.querySelectorAll('#board .card')].map(c=>c.querySelector('h3,.ttl,.title')?.innerText+' | '+(c.querySelector('.lg')?.innerText||'')+' | '+[...c.querySelectorAll('.tag.bud')].map(t=>t.innerText).join(','))}));
  console.log(lang, JSON.stringify(x,null,1)); await p.screenshot({path:__dirname+`/shots/mirror-${lang}.png`});
  if(lang==='kr'){ await p.selectOption('#flg', {index:1}).catch(()=>{}); await p.waitForTimeout(500); console.log('리그 선택 뒤', await p.evaluate(()=>document.querySelectorAll('#board .card').length));
    await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForSelector('#board .card',{timeout:120000}); await p.waitForTimeout(1500);
    console.log('크래프팅 배지', await p.evaluate(()=>[...new Set([...document.querySelectorAll('#board .lg')].map(e=>e.innerText))].join(' / ')), await p.evaluate(()=>document.querySelector('#l-patch').innerText)); }
  console.log('오류', errs); await p.close(); } await b.close(); })();
