const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('http://localhost:8779/recipes.html?lang=kr');await p.waitForFunction(()=>window.__rec&&__rec.booted);
console.log(await p.evaluate(id=>{const r=__rec.recipes.find(x=>x.id===id);const a=__rec.analyse(r);return a.nodes.map((o,i)=>(i+1)+' '+o.n.id+' p='+(o.p!=null?o.p.toFixed(3):'-')+' use='+JSON.stringify(Object.fromEntries(Object.entries(o.use||{}).map(([k,v])=>[k,+v.toFixed(2)])))).join('\n')},process.argv[2]));await b.close();})();
