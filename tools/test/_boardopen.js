// 요약으로 그린 목록에서 레시피 열기·주소로 바로 열기 점검
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:900}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8779/recipes.html?lite&lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
 const ids=await p.evaluate(()=>[...document.querySelectorAll('#board .card')].map(c=>c.dataset.id)); let ok=0;
 for(const id of ids){ await p.evaluate(id=>document.querySelector(`#board .card[data-id="${id}"]`).click(), id);
   await p.waitForFunction(id=>__rec.open===id && !document.querySelector('#detail').hidden && document.querySelector('#detail').innerHTML.length>500, id, {timeout:15000}).then(()=>ok++).catch(()=>console.log('안 열림', id));
   await p.evaluate(()=>document.querySelector('[data-act="back"]')?.click()); await p.waitForFunction(()=>!__rec.open); }
 const q=await b.newPage(); q.on('pageerror',e=>errs.push(e.message)); await q.goto('http://localhost:8779/recipes.html?lite&lang=kr#r-'+ids[5]); await q.waitForFunction(()=>window.__rec&&__rec.booted);
 const d=await q.evaluate(()=>document.querySelector('#detail').innerHTML.length);
 console.log('열림', ok+'/'+ids.length, '| 주소로 열기 상세 길이', d, '| 오류', errs.length, errs.slice(0,3).join(' / ')); await b.close();})();
