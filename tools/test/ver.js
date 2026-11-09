const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const r=await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
 const o=[]; for(const x of S.recSamples){ const it=await S.parse(x.text); const an=S.analyse(it); const d=S.makeDraft(it,an); if(!d){ o.push("# "+x.id+"\n  blocked "+an.tr[0].t.replace(/<[^>]+>/g,"")); continue; } const c=S.verifyDraft(it,an,d); o.push('# '+x.id+'\n'+c.filter(z=>z.lv!=='ok').map(z=>'  '+z.lv+' '+z.kr).join('\n')); } return o.join('\n'); });
console.log(r); await b.close();})();
