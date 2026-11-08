const {chromium}=require('playwright');(async()=>{const b=await chromium.launch(),p=await b.newPage();await p.goto('http://localhost:8779/recipes.html?debug=1&lang=kr');await p.waitForTimeout(2500);
console.log(await p.evaluate(()=>{const r=JSON.parse(JSON.stringify(__rec.recipes.find(x=>x.id=='sl-flamewave-ring')));let a=__rec.analyse(r);const o1=a.nodes.find(o=>o.n.id=='s2');
const n=r.nodes.find(x=>x.id=='s2');n.do='chaos';n.cur='Greater_Chaos_Orb';n.omens=['Omen_of_Dextral_Erasure'];delete n.withEach;a=__rec.analyse(r);const o2=a.nodes.find(o=>o.n.id=='s2');
return {annul:[o1.p,o1.warn], erase:[o2.p,o2.warn]}}));await b.close()})();
