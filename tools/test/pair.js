// 원본 레시피와 그 완성템으로 만든 역산 초안을 같은 엔진으로 단계별 계산해 나란히 출력: node pair.js <레시피id>
const {chromium}=require('playwright'); const id=process.argv[2];
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const d=await p.evaluate(async(id)=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]);
  const x=S.recSamples.find(s=>s.id===id); const it=await S.parse(x.text); const d=S.makeDraft(it,S.analyse(it)); d.id='draft-x'; return d; }, id);
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const out=await p.evaluate(async([id,d])=>{ const R=__rec; d.likes=0; d.success=0; R.recipes.unshift(d); await new Promise(r=>setTimeout(r,300));
  const one=r=>{ const a=R.analyse(r); return a.nodes.map((o,i)=>({i:i+1, t:(o.title||o.n.do)+'', cur:o.n.cur||'', om:(o.n.omens||[]).join('+'), p:o.pUnknown?'?':(o.p*100).toFixed(2), tries:o.tries, cost:JSON.stringify(o.cost||o.expectCost||''), warn:o.warn||''})); };
  return {orig:one(R.recipes.find(r=>r.id===id)), draft:one(d), keys:Object.keys(R.analyse(d).nodes[1]||{})}; }, [id,d]);
console.log('keys', out.keys.join(','));
for(const k of ['orig','draft']){ console.log('\n== '+k); out[k].forEach(x=>console.log(`${x.i}. ${x.cur} ${x.om} p=${x.p}% ${x.warn?' ⚠ '+x.warn:''}`)); }
await b.close();})();
