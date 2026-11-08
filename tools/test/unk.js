const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(/fonts\./,r=>r.abort());
await p.goto('http://localhost:8779/recipes.html?lang=kr');await p.waitForTimeout(2500);
const res=await p.evaluate(()=>__rec.recipes.map(r=>{const a=__rec.analyse(r); return r.id+': '+a.nodes.map((o,i)=>o.pUnknown?`#${i+1}(${o.pWhy?'촉진':'미확인'})`:(/cast|시전/.test(JSON.stringify(o.n.target||''))?'':'')).filter(Boolean).join(' ')+ '  | r1b/cast p: '+a.nodes.filter(o=>['r1b','g6','a10','c1'].includes(o.n.id)).map(o=>o.n.id+'='+(o.pUnknown?'?':o.p.toExponential(2))).join(',');}));
console.log(res.join('\n'),errs);await b.close();})();
