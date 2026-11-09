// engine (recipes.html analyse) numbers for one recipe: main path, prep, costs in div — for comparing with the graph simulation
// usage: node tools/sim/engine.js <recipe id> > tools/sim/engine/<recipe id>.json   (test server running; tools/sim/run.js adds it to the sim data)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec && __rec.booted);
const out=await p.evaluate((id)=>{ const S=__rec, r=S.recipes.find(x=>x.id===id); const a=S.analyse(r); const pr=S.prepRecipe(r); const pa=pr?S.analyse(pr):null;
  const ex=k=>k==='Exalted_Orb'?1:(S.prices.p[k]??null), dv=u=>{let v=0; for(const k in u){ const e=ex(k); if(e!=null) v+=u[k]*e; } return v/S.prices.divine; };
  const nodes=x=>x.nodes.map(o=>({id:o.n.id, do:o.n.do, p:o.p, tries:o.useTries, passes:o.passes, use:o.use, lose:o.lose}));
  const main={tot:a.tot, totAll:a.totAll, bases:a.bases, div:dv(a.tot), divAll:dv(a.totAll), nodes:nodes(a)}, prep=pa?{tot:pa.tot, bases:pa.bases, div:dv(pa.tot), nodes:nodes(pa)}:null;
  const base=(+r.basePrice||0)*(prep?prep.bases:a.bases);   // the whole item: main path + base preparation + bought bases
  return {total:main.div+(prep?prep.div:0)+base, totalAll:main.divAll+(prep?prep.div:0)+base, main, prep, basePrice:r.basePrice}; }, process.argv[2]);
console.log(JSON.stringify(out,null,1)); await b.close();})();
