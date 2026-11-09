const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const drafts=await p.evaluate(async()=>{ const S=__rev; if(!S.index)[S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json());
  const out=[]; for(const x of S.recSamples){ const it=await S.parse(x.text); if(it.err) continue; const d=S.makeDraft(it,S.analyse(it)); if(!d) continue; d.id='draft-'+x.id.replace(/[^a-z0-9]/g,''); out.push(d);} return out; });
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const res=await p.evaluate(async(ds)=>{ const R=__rec; const o=[]; for(const d of ds){ d.likes=0; d.success=0; R.recipes.unshift(d); }
  await new Promise(r=>setTimeout(r,300));
  for(const d of ds){ try{ const a=R.analyse(d); o.push({id:d.id, w:a.nodes.filter(n=>n.warn).map(n=>n.n.id+':'+n.warn), p:a.nodes.map(n=>n.pUnknown?'?':(n.p<0.995?(n.p*100).toFixed(2):'·')).join(' ')}); }catch(e){ o.push({id:d.id, err:e.message}); } } return o; }, drafts);
res.forEach(r=>console.log(r.id, r.err||'', r.p||'', (r.w||[]).join(' | ')));
await b.close();})();
