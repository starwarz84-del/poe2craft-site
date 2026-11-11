const {chromium}=require('playwright');
const IDS=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
const r=await p.evaluate(async(IDS)=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
 const o=[]; for(const id of IDS){ const x=S.recSamples.find(s=>s.id===id); const it=await S.parse(x.text); const an=S.analyse(it);
  const c=f=>{ const an2={...an,rows:an.rows.flatMap(r=>{ if(r.unrev) return []; if(r.m.fr) return [r]; const t=Math.max(r.tierNo, f?Math.min(f,r.tierCnt):0); return [t===r.tierNo?r:{...r,tierNo:t}]; })}; try{ const d=S.makeDraft(it,an2,{}), d2=S.makeDraft(it,an2,{market:1e9}); return d? S.draftCost(it,an2,d).toFixed(1)+'|'+S.draftCost(it,an2,d2).toFixed(1):null;}catch(e){return 'E';} };
  o.push([id,c(0),c(2),c(3)]); } return o;},IDS);
r.forEach(x=>console.log(x.join('\t'))); await b.close();})();
