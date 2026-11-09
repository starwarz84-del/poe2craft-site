const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const r=await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]);
 const R=await fetch('data/recipes.json').then(r=>r.json()); const L=Array.isArray(R)?R:R.recipes;
 const o=[]; for(const x of S.recSamples){ const it=await S.parse(x.text); if(it.err) continue; const an=S.analyse(it); const r0=L.find(y=>y.id===x.id); o.push([x.id, r0?.difficulty, S.estDiff(it,an)]); } return o; });
let e=0; r.forEach(x=>{ e+=Math.abs(x[1]-x[2]); console.log(x.join(' ')); }); console.log('MAE', e/r.length); await b.close();})();
