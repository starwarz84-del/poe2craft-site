const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const rec=JSON.parse(fs.readFileSync('/home/claude/poe2data/site/data/recipes.json')).recipes;
const res=await p.evaluate(async()=>{ const S=__rev; if(!S.index)[S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]);
  const out=[]; for(const x of S.recSamples){ const it=await S.parse(x.text); if(it.err){ out.push({id:x.id, err:it.err}); continue; }
    const an=S.analyse(it); const d=S.makeDraft(it,an);
    out.push({id:x.id, n:x.n, got:it.mods.length, unk:it.other.filter(o=>o.k==='?').map(o=>o.l), how:an.rows.map(r=>(r.m.side||'')+':'+r.how+(r.tierNo?'T'+r.tierNo:'')).join(' '),
      draft:d.nodes.map(n=>n.do+(n.cur?'('+n.cur.replace(/_/g,' ').replace(/Orb of |Perfect |Omen of /g,'')+')':'')).join(' > ')}); }
  return out; });
for(const r of res){ const o=rec.find(x=>x.id===r.id); console.log('\n#',r.id, r.err||`${r.got}/${r.n}`, r.unk?.length?'UNK '+r.unk.join('|'):''); console.log('  mods ', r.how); console.log('  draft', r.draft); console.log('  orig ', o.nodes.map(n=>n.do+(n.cur?'('+n.cur.replace(/_/g,' ').replace(/Orb of |Perfect |Omen of /g,'')+')':'')).join(' > ')); }
await b.close();})();
