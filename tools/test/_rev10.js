const {chromium}=require('playwright');
const IDS=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
const r=await p.evaluate(async(IDS)=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
 if(!S.prices) S.prices=await fetch('data/prices.json').then(r=>r.json());
 const out=[]; for(const id of IDS){ const x=S.recSamples.find(s=>s.id===id); if(!x){out.push({id,miss:1});continue;}
  const it=await S.parse(x.text); const an=S.analyse(it);
  const rows=an.rows.map(r=>({t:(r.kr||r.txt||r.m?.kr||'').toString().slice(0,60), side:r.side||r.m?.side, tier:r.tierNo, cnt:r.tierCnt, fr:!!r.m?.fr, unrev:!!r.unrev}));
  const an2={...an, rows:an.rows.filter(r=>!r.unrev)};
  let d=null, err=null; try{ d=S.makeDraft(it,an2,{}); }catch(e){ err=e.message; }
  if(!d){ out.push({id, rows, blocked: err || (an.tr&&an.tr[0]&&an.tr[0].t.replace(/<[^>]+>/g,''))}); continue; }
  const c=S.verifyDraft(it,an2,d); let cost=null; try{ cost=S.draftCost(it,an2,d);}catch(e){cost='ERR '+e.message}
  out.push({id, title:x.title.kr, rows, diff:d.difficulty, start:d.start&&{rar:d.start.rar, n:(d.start.mods||[]).length}, nodes:d.nodes.map(n=>({id:n.id,do:n.do,cur:n.cur,om:n.omens,opt:!!n.optional,ph:n.phase,lbl:(n.label&&n.label.kr)||(n.note&&n.note.kr)||'',fail:n.fail&&(n.fail.goto||'')+(n.fail.lost?'/lost':''),comp:!!n.compromise})), check:c.filter(z=>z.lv!=='ok').map(z=>z.lv+' '+z.kr), cost, comps:d.compromises, price:d.priceTier}); }
 return out; }, IDS);
console.log(JSON.stringify(r)); await b.close();})();
