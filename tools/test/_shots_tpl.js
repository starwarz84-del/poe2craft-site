// 리버스 등록 틀(W9) 화면: 등록 완성품을 붙여 넣고 필수 옵션을 고른 뒤 '초안 만들기' → 검산 위 '등록 레시피 …를 틀로 씀' 줄·플로우차트 검사·미리보기 → shots/tpl-<id>-<lang>.png
// node _shots_tpl.js <레시피 id> [kr|en]   (테스트 서버 :8779)
const {chromium}=require('playwright'); const fs=require('fs'); const {registered, ROOT}=require('./_regcard.js');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const id=process.argv[2], lang=process.argv[3]||'kr', r=R.find(x=>x.id===id), reg=registered(r,50);
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1280,height:900}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
await p.goto(`http://localhost:8779/discover.html?lang=${lang}`); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
const i=await p.evaluate(id=>__rev.recSamples.findIndex(s=>s.id===id), id); await p.selectOption('#recs', String(i)); await p.waitForTimeout(1500);
await p.evaluate(([card,per])=>{ const S=__rev, an=S.last.an; S.need=new Set(); const took=new Set(); card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const k=an.rows.findIndex((r,q)=>!r.unrev && !took.has(q) && l.opts.some(o=>o.gi===r.m.gi)); if(k<0) return; took.add(k); const rr=an.rows[k]; if(rr.m.fr) return; const o=l.opts.find(o=>o.gi===rr.m.gi); S.need.add(k); if(o.tmax) S.tsel[k]=Math.max(rr.tierNo, Math.min(o.tmax, rr.tierCnt)); }); S.okQR=true; S.unkOk=true; S.minDraftMs=0; },[reg.card,reg.per]);
await p.evaluate(()=>{ document.querySelector('#qrok') && (document.querySelector('#qrok').checked=true); }); 
await p.evaluate(()=>{ const S=__rev; const ev=new Event('input'); }); await p.click('#mk');
await p.waitForFunction(()=>__rev.flow && !__rev.flow.wait, null, {timeout:240000}); await p.waitForTimeout(2500);
const info=await p.evaluate(()=>({tpl:__rev.draft?.tpl||null, line:document.querySelector('.tplline')?.textContent||null, issues:(__rev.flow?.issues||[]).map(x=>x.kr), grades:(__rev.flow?.res||[]).map(x=>[x.id, x.cost])}));
const el=await p.$('#mkmsg'); fs.mkdirSync(__dirname+'/shots',{recursive:true}); await el.screenshot({path:`${__dirname}/shots/tpl-${id}-${lang}.png`});
await p.setViewportSize({width:390,height:900}); await p.waitForTimeout(500); await el.screenshot({path:`${__dirname}/shots/tpl-${id}-${lang}-m.png`});
console.log(JSON.stringify(info), errs.length?'ERR '+errs.join(' | '):'오류 0'); await b.close(); })();
