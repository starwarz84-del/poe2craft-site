// 리버스 초안이 시뮬에서 끝나지 않을 때 원인 찾기(2026-11-12 도과장): node _revtrace.js <레시피id> [후보키]  (테스트 서버 필요)
// 화면과 같은 방식으로 초안을 만들고 그 플로우차트를 node 시뮬로 돌려, 끝나지 않는 회차의 마지막 단계와 아이템 상태를 출력
const {chromium}=require('playwright'); const fs=require('fs'); const {registered, ROOT}=require('./_regcard.js'); const SIM=require(ROOT+'/site/sim.js');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const craft=JSON.parse(fs.readFileSync(ROOT+'/site/data/crafting.json')), prices=JSON.parse(fs.readFileSync(ROOT+'/site/data/prices.json'));
const [id, want]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
const r=R.find(x=>x.id===id), reg=registered(r, 100), buy=((r.start||{}).mods||[]).filter(m=>m.gi!=null && !m.crafted).map(m=>m.gi);
const x=await p.evaluate(async([id,card,buy,per,want,rtags,rreq])=>{ const S=__rev; const x=S.recSamples.find(s=>s.id===id); const it=await S.parse(x.text); const an=S.analyse(it);
  S.need=new Set(); S.soft=new Set(); S.tsel={}; S.alt={}; S.buy=new Set(); const took=new Set();
  card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const i=an.rows.findIndex((r,k)=>!r.unrev && !took.has(k) && l.opts.some(o=>o.gi===r.m.gi)); if(i<0) return; const r=an.rows[i], o=l.opts.find(o=>o.gi===r.m.gi); took.add(i); if(r.m.fr) return;
    S.need.add(i); if(o.tmax) S.tsel[i]=Math.max(r.tierNo, Math.min(o.tmax, r.tierCnt)); if(buy.includes(r.m.gi) && r.how==='n') S.buy.add(i); if(l.opts.length>1 && !false) S.alt[i]=l.opts.filter(x=>x.gi!==r.m.gi).map(x=>({gi:x.gi, tmax:x.tmax||null})); });
  let a2=S.needAn(an,0,it); const bs=new Set([...S.buy].map(i=>an.rows[i]?.m).filter(Boolean)), o={market:1e9, ...(bs.size?{buy:bs}:{})};
  let d; if(want){ await S.bestDraftAsync(it,a2,o,null,0); const c=S.lastC.find(c=>((c.K.k.join(',')||'-')+'|'+(c.k||'-'))===want); d=S.makeDraft(it,c.K.a,{...o,...c.o}); } else d=(await S.bestDraftAsync(it,a2,o,null,0)).d;
  const g=POE2GRAPH.fromDraft(d, it.D, {craft:S.craft, grades:['high']}); Object.assign(g.tags, rtags); g.require=rreq||g.require; return {g, cls:it.cls}; },[id,reg.card,buy,reg.per,want,reg.rtags,reg.rreq]);
await b.close();
const D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${x.g.cls||x.cls}.json`)), G=D.groups, g={...x.g, maxSteps:20000};
const nm=m=>m.unrev?`[미공개 ${m.side}]`:(m.fr?'분열 ':'')+(m.mark?'징표 ':'')+(m.des?'훼손 ':'')+((G[m.gi]?.t?.[m.ti]?.[2])||G[m.gi]?.f?.join('+')||'?')+` ${m.side}`;
const st=g.strategies[0], run=SIM.make(g,D,craft,st.params), rn=SIM.rng(5); let hist=[];
const T={visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done(){}};
for(let i=0;i<400;i++){ hist=[]; try{ run(rn,{tally:T, enter:(id,it)=>{ hist.push(id+' : '+it.mods.map(nm).join(' | ')); if(hist.length>60) hist.shift(); }}); }
  catch(e){ console.log(`회차 ${i}: ${e.message}`); console.log(hist.slice(-25).join('\n')); process.exit(0); } }
console.log('400회 모두 끝남');
})();
