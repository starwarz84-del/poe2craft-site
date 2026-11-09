const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const drafts=await p.evaluate(async()=>{ const S=__rev; if(!S.index)[S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
  const out=[]; for(const x of S.recSamples){ const it=await S.parse(x.text); if(it.err) continue; const d=S.makeDraft(it,S.analyse(it)); if(!d) continue; d.id='draft-'+x.id.replace(/[^a-z0-9]/g,''); d.orig=x.id; out.push(d);} return out; });
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const res=await p.evaluate(async(ds)=>{ const R=__rec; const o=[];
  const nm=id=>(R.byId[id]?.kr||id||'');
  const sum=(r,a)=>a.nodes.map((x,i)=>{ const n=x.n,t=n.target||{}; const g=gi=>{ const G=R.cls[r.cls].groups[gi]; return G?G.t[0][4].split('\n')[0].slice(0,22):gi; };
    let tg = t.gi!=null?g(t.gi)+(t.tmax?'≤T'+t.tmax:''): t.anyOf?'['+t.anyOf.map(x=>g(x.gi)).join('/')+']': t.junk?'잡옵'+t.junk: t.unrev?'훼손'+t.unrev: t.reveal?'공개:'+(t.reveal.gi!=null?g(t.reveal.gi):JSON.stringify(t.reveal).slice(0,30)): t.quality?'Q'+t.quality: t.removeGi!=null?'제거'+g(t.removeGi): JSON.stringify(t).slice(0,40);
    return `  ${String(i+1).padStart(2)} ${n.do.padEnd(9)} ${nm(n.cur)}${(n.omens||[]).map(x=>'+'+nm(x).replace(/의 징조$/,'')).join('')} → ${tg} ${x.pUnknown?'[?]':x.p<0.995?'['+(x.p*100).toFixed(2)+'%]':''}${n.fail?' ↺'+(n.fail.via?nm(n.fail.via.cur)+(n.fail.via.omens||[]).map(x=>'+'+nm(x).replace(/의 징조$/,'')).join(''):''):''}`; }).join('\n');
  for(const d of ds){ d.likes=0; d.success=0; R.recipes.unshift(d); if(!R.cls[d.cls]) continue; }
  for(const d of ds){ const r0=R.recipes.find(x=>x.id===d.orig); if(!R.cls[d.cls]) continue;
    let A,B; try{ A=R.analyse(d); B=R.analyse(r0);}catch(e){ o.push(d.orig+' ERR '+e.message); continue; }
    o.push(`\n### ${d.orig}  [${r0.title.kr}]\n-- 원본 (start ${r0.start?JSON.stringify(r0.start.mods.map(m=>(m.fr?'분열:':'')+(m.gi!=null?R.cls[r0.cls].groups[m.gi].t[0][4].slice(0,15):'잡옵'))):'일반'})\n${sum(r0,B)}\n   tot ${JSON.stringify(B.tot).slice(0,200)}\n-- 초안\n${sum(d,A)}\n   tot ${JSON.stringify(A.tot).slice(0,200)}`); }
  return o.join('\n'); }, drafts);
fs.writeFileSync('cmp2.txt',res); console.log(res.length);
await b.close();})();
