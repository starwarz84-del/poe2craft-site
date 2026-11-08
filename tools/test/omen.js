const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.route(/fonts\./,r=>r.abort());
await p.goto('http://localhost:8779/recipes.html?lang=kr');await p.waitForTimeout(2500);
const res=await p.evaluate(()=>{ const out=[]; for(const r of __rec.recipes){ const a=__rec.analyse(r); a.nodes.forEach((o,i)=>{ const om=(o.n.omens||[]).find(x=>/(Sinistral|Dextral)_(Exaltation|Necromancy)/.test(x)); if(!om) return; const other=/Sinistral/.test(om)?'s':'p'; const cnt=(o.pre||[]).filter(m=>m.side===other).length; if(cnt>=o.cap[other]) out.push(`${r.id} #${i+1} ${o.n.id} ${om} (반대쪽 ${cnt}/${o.cap[other]})`); }); } return out; });
console.log(res.join('\n')||'none'); await b.close();})();
