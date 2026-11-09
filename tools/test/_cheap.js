// Which draft steps the price-based orb choice changed, with the engine's cost of each step (div) before / after
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const D=await p.evaluate(async(only)=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
  const o=[]; for(const x of S.recSamples){ if(only && x.id!==only) continue; const it=await S.parse(x.text); const an=S.analyse(it); S.noCheap=true; const a=S.makeDraft(it,an); S.noCheap=false; const c=S.makeDraft(it,an); if(a) o.push({id:x.id,a,c}); } return o; }, process.argv[2]||null);
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const out=await p.evaluate(async(D)=>{ const S=__rec, P=await fetch('data/prices.json').then(r=>r.json()); const ex=id=>id==='Exalted_Orb'?1:(P.p[id]??0);
  const cost=u=>Object.entries(u||{}).reduce((s,[k,v])=>s+v*ex(k),0)/P.divine;
  return D.map(({id,a,c})=>{ const A=S.analyse({...a,likes:0}), C=S.analyse({...c,likes:0}); const L=[];
    c.nodes.forEach((n,i)=>{ const m=a.nodes[i]; if(m && m.cur!==n.cur) L.push(`#${i+1} ${n.do} ${m.cur}(p ${A.nodes[i].p.toFixed(4)}, ${cost(A.nodes[i].use).toFixed(1)}) -> ${n.cur}(p ${C.nodes[i].p.toFixed(4)}, ${cost(C.nodes[i].use).toFixed(1)})`); });
    return L.length ? id+'\n  '+L.join('\n  ') : ''; }).filter(Boolean).join('\n'); }, D);
console.log(out); await b.close();})();
