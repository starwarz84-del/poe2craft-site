// engine (recipes.html analyse) numbers for one recipe: main path, prep, costs in div — for comparing with the graph simulation
// usage: node tools/sim/engine.js <recipe id> > tools/sim/engine/<recipe id>.json   (test server running; tools/sim/run.js adds it to the sim data)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.setDefaultTimeout(180000);   /* 클래스 파일을 다 받는 테스트 서버라 30초를 넘길 때가 있음(2026-11-13 S2, G7 보고) */
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec && __rec.booted);
const out=await p.evaluate((id)=>{ const S=__rec, r0=S.recipes.find(x=>x.id===id);
  /* 플로우차트에서 읽은 레시피(fcRead)는 analyse가 확률·사용량을 시뮬 값으로 덮어써서, 그대로 계산하면 '엔진 값' = 지난번 시뮬 값이 됨(2026-11-13 S1: 시한 차유라 반지 엔진 197 = 옛 시뮬).
     엔진 비교값은 시뮬 값을 빼고(fcRead·fcs 없이) 엔진 계산으로, 막히면 예전처럼 */
  let r=r0, a, mode='engine';
  if(r0.fcRead){ try { r={...JSON.parse(JSON.stringify(r0)), id:r0.id+'~engine', fcRead:null, _an:null, _prep:null}; r.nodes.forEach(n=>{ delete n.fcs; if(!n.fail && (n.routes||[]).some(x=>x.to==='self' && x.cls==='no')) n.fail={goto:'self'}; });   /* 플로우차트 '빗나가면 다시' 선 → 엔진의 같은 단계 반복 */ a=S.analyse(r); } catch(e){ r=r0; a=null; mode='fcRead('+String(e.message||e).slice(0,80)+')'; } }
  if(!a){ r=r0; a=S.analyse(r); if(r0.fcRead && mode==='engine') mode='fcRead'; } const pr=S.prepRecipe(r); const pa=pr?S.analyse(pr):null;
  const ex=k=>k==='Exalted_Orb'?1:(S.prices.p[k]??null), dv=u=>{let v=0; for(const k in u){ const e=ex(k); if(e!=null) v+=u[k]*e; } return v/S.prices.divine; };
  const nodes=x=>x.nodes.map(o=>({id:o.n.id, do:o.n.do, p:o.p, tries:o.useTries, passes:o.passes, use:o.use, lose:o.lose}));
  const main={tot:a.tot, totAll:a.totAll, bases:a.bases, div:dv(a.tot), divAll:dv(a.totAll), nodes:nodes(a)}, prep=pa?{tot:pa.tot, bases:pa.bases, div:dv(pa.tot), nodes:nodes(pa)}:null;
  const base=(+r.basePrice||0)*(prep?prep.bases:a.bases);   // the whole item: main path + base preparation + bought bases
  return {mode, total:main.div+(prep?prep.div:0)+base, totalAll:main.divAll+(prep?prep.div:0)+base, main, prep, basePrice:r.basePrice}; }, process.argv[2]);
console.log(JSON.stringify(out,null,1)); await b.close();})();
