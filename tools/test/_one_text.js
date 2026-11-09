const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev);
const txt=fs.readFileSync(process.argv[2],'utf8');
const r=await p.evaluate(async(txt)=>{ const S=__rev; if(!S.index)[S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
 const it=await S.parse(txt); if(it.err) return {err:it.err}; const an=S.analyse(it); const d=S.makeDraft(it,an); if(!d) return {blocked:an.tr[0].t, rows:an.rows.length}; const c=S.verifyDraft(it,an,d);
 return {it:{cls:it.cls, base:it.b?.en||it.b, ilvl:it.ilvl, qual:it.qual, corrupted:it.corrupted, cat:it.cat, mods:(it.mods||[]).map(m=>({t:m.t||m.text, tag:m.tag, side:m.side, gi:m.gi}))},
   rows:an.rows.map(r=>({side:r.m.side, how:r.how, s:r.g?.s, txt:(r.t?.[4]||r.g?.t?.[0]?.[4]||'').split('\n')[0], tier:r.tierNo, unrev:r.unrev, fr:r.m.fr})), cap:an.cap, warn:an.warn,
   title:d.title, diff:d.difficulty, start:d.start, nodes:d.nodes.map(n=>[n.id,n.do,n.cur,(n.omens||[]).join('+'),JSON.stringify(n.target||{}).slice(0,90),(n.note?.kr||'').slice(0,80), JSON.stringify(n.fail||null)].join(' | ')),
   ver:c.filter(z=>z.lv!=='ok').map(z=>z.lv+' '+z.kr)};
},txt); console.log(JSON.stringify(r,null,1)); await b.close();})();
