// 군주 징조 공개 단계 확률 점검: node _lord.js
const {chromium}=require('playwright');
const L=[['absent-amulet-video','a10'],['absent-amulet-video','a18'],['mazbro-caster-amulet','a17'],['belton-plus8-wand','b2'],['diztoh-budget-2h-mace','g8'],['diztoh-budget-crossbow','c8'],['diztoh-onehand-mace','m10'],['diztoh-talisman','t4'],['ragna-ashot-bow-v2-bal','w6'],['ragna-ashot-bow-v2-ess','w6'],['sane-resist-belt-v2-bal','b4'],['sane-resist-belt-v2-ess','b4'],['diztoh-budget-mace-v2-bal','d8'],['diztoh-budget-mace-v2-ess','d8']];
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const out=await p.evaluate(L=>L.map(([id,nid])=>{ const R=__rec, r=R.recipes.find(x=>x.id===id); if(!r) return id+' 없음';
  const a=R.analyse(r); const i=a.nodes.findIndex(o=>o.n.id===nid); const o=a.nodes[i];
  const rv=a.nodes.slice(i,i+3).find(x=>x.n.do==='reveal')||o;
  return `${id} ${nid}: 훼손 p=${(o.p*100).toFixed(1)}% · 공개(${rv.n.id}) p=${rv.pUnknown?'?':(rv.p*100).toFixed(1)}% tries=${(+rv.tries||0).toFixed(2)}`; }), L);
console.log(out.join('\n')); await b.close();})();
