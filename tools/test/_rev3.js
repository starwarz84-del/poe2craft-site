// 리버스 연습: 레시피 완성품 → 필수(레시피가 노리는 옵션)·유효(결과 그대로 옵션)·잡옵으로 나눠 초안 → 엔진 비용을 원본과 비교
// node _rev3.js <LV json> [id…]   (id 없으면 LV의 모든 레시피)
const {chromium}=require('playwright'); const fs=require('fs');
const LV=JSON.parse(fs.readFileSync(process.argv[2])); let IDS=process.argv.slice(3); if(!IDS.length) IDS=Object.keys(LV);
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
const drafts=await p.evaluate(async([IDS,LV,FLOOR,TM])=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
 const o=[]; for(const id of IDS){ const x=S.recSamples.find(s=>s.id===id); if(!x) continue; const it=await S.parse(x.text); if(it.err) continue; const an=S.analyse(it); if(an.putrid) continue; const lv=LV[id];
  S.need=new Set(); S.soft=new Set(); S.tsel={}; S.buy=new Set();
  const FL=FLOOR, process_TM=TM; an.rows.forEach((r,i)=>{ if(r.unrev||r.m.fr) return; if(FL) S.tsel[i]=Math.max(r.tierNo, Math.min(FL, r.tierCnt)); else if(process_TM && lv.tmax?.[r.m.gi]) S.tsel[i]=Math.max(r.tierNo, Math.min(lv.tmax[r.m.gi], r.tierCnt)); if(lv.must.includes(r.m.gi)) S.need.add(i); else if(lv.soft.includes(r.m.gi)) S.soft.add(i); });
  if(!S.need.size) an.rows.forEach((r,i)=>{ if(!r.unrev && !r.m.fr && !S.soft.has(i)) S.need.add(i); });
  for(const v of ['old','new']){ S.noSwap = v==='old'; const sv = v==='old' ? S.soft : null; if(v==='old'){ S._soft=S.soft; S.soft=new Set(); S._soft.forEach(i=>S.need.add(i)); }
   let a2=S.needAn(an,0,it); let d=null, err=null; try{ const bd=S.bestDraft(it,a2,{market:1e9}); d=bd.d; a2=bd.an; }catch(e){ err=e.message; }
   if(v==='old'){ S._soft.forEach(i=>S.need.delete(i)); S.soft=S._soft; }
   if(!d){ o.push({id,v,err:err||'blocked'}); continue; }
   const c=S.verifyDraft(it,a2,d); d.id='draft-'+v+'-'+id.replace(/[^a-z0-9]/g,''); d.src=id; d._v=v; d._err=c.filter(z=>z.lv==='err').map(z=>z.kr); d._swap=d.knowhow||null; d._soft=a2.rows.filter(r=>r.soft).length; d._must=a2.rows.filter(r=>!r.soft&&!r.m.fr).length; o.push(d); } }
 return o; },[IDS,LV,+(process.env.FLOOR||0),!!process.env.TM]);
await p.goto('http://localhost:8779/recipes.html?lang=kr&debug=1'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const res=await p.evaluate(async(ds)=>{ const R=__rec; for(const d of ds){ if(!d.nodes) continue; d.likes=0; d.success=0; R.recipes.unshift(d);} await new Promise(r=>setTimeout(r,300));
 const cost=r=>{ try{ const c=R.recipeCost(r); return c&&{v:+c.v.toFixed(1), all:+c.all.toFixed(1)}; }catch(e){ return {e:e.message}; } };
 return ds.map(d=>{ if(!d.nodes) return d; const orig=R.recipes.find(r=>r.id===d.src && !r.draft); const a=R.analyse(d);
  const top=a.nodes.map(o=>({id:o.n.id, k:o.n.do+' '+(o.n.cur||'')+' '+(o.n.omens||[]).join('+')+(o.n.optional?' (opt)':'')+(o.n.compromise?' (settle)':''), d:(R.divOf(o.use||{})?.v||0)+(R.divOf(o.settleUse||{})?.v||0), p:o.p, note:((o.n.note&&o.n.note.kr)||'').slice(0,80)})).sort((x,y)=>y.d-x.d).slice(0,3);
  return {id:d.src, v:d._v, top, draft:cost(d), orig:orig?cost(orig):null, unk:a.nodes.filter(n=>n.pUnknown).length, err:d._err, swap:d._swap, soft:d._soft, must:d._must, steps:d.nodes.length}; }); }, drafts);
console.log(JSON.stringify(res)); await b.close();})();
