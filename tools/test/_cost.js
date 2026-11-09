// Prices every recipe (and its draft) with the Recipes tab engine: guaranteed / with extras (div), expensive omens, settle forks
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const drafts=await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
  const o={}; for(const x of S.recSamples){ const it=await S.parse(x.text); const an=S.analyse(it); const d=S.makeDraft(it,an); if(d) o[x.id]=d; } return o; });
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const rows=await p.evaluate(async(drafts)=>{ const S=__rec, P=await fetch('data/prices.json').then(r=>r.json()), B=await fetch('data/budget.json').then(r=>r.json());
  const ex=id=>id==='Exalted_Orb'?1:P.p[id]; const dv=u=>{ let v=0, m=[]; for(const k in u){ const x=ex(k); if(x==null) m.push(k); else v+=u[k]*x; } return [v/P.divine, m]; };
  const om=a=>B.expensive.reduce((s,k)=>s+(a.tot[k]||0),0);
  const one=r=>{ r._an=null; const a=S.analyse(r); const [g,m]=dv(a.tot), [all]=dv(a.totAll); return {g:+g.toFixed(2), all:+all.toFixed(2), om:+om(a).toFixed(1), miss:m, comp:r.nodes.filter(n=>n.compromise&&!n.fallbackFor).length+r.nodes.filter(n=>n.optional&&n.fallbackFor).length, d:r.difficulty}; };
  return S.recipes.filter(r=>!r.draft).map(r=>({id:r.id, orig:one(r), draft:drafts[r.id]?one({...drafts[r.id], likes:0, success:0}):null})); }, drafts);
rows.forEach(x=>console.log([x.id, x.orig.d, x.orig.g, x.orig.all, x.orig.om, x.orig.miss.join('+'), '|', x.draft?[x.draft.d, x.draft.g, x.draft.all, x.draft.om, x.draft.comp].join(' '):'-'].join(' ')));
await b.close();})();
