const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const r=await p.evaluate(async(id)=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json());
 const x=S.recSamples.find(s=>s.id===id); const it=await S.parse(x.text); const an=S.analyse(it); const d=S.makeDraft(it,an);
 const D=it.D; return {cap:an.cap, start:d.start, rows:an.rows.map(r=>[r.m.side,r.how,r.g?.s,r.g?.sub?.[0],r.m.gi]), nodes:d.nodes.map(n=>JSON.stringify({do:n.do,cur:n.cur,omens:n.omens,target:n.target,label:n.label?.kr})+'  // '+n.note.kr), runes:Object.keys(D.runesBy||{}).slice(0,5), runeNames:(D.runes||[]).slice(0,3).map(r=>JSON.stringify(r).slice(0,150))}; }, process.argv[2]);
console.log(JSON.stringify(r,null,1)); await b.close();})();
