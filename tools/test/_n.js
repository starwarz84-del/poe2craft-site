const {chromium}=require('playwright');(async()=>{const b=await chromium.launch(),p=await b.newPage();await p.goto('http://localhost:8779/recipes.html?debug=1&lang=kr');await p.waitForTimeout(2000);
const ids=await p.evaluate(()=>__rec.recipes.map(r=>r.id));let out=[];
for(const id of ids){await p.goto('http://localhost:8779/recipes.html?debug=1&lang=kr#r-'+id);await p.reload();await p.waitForTimeout(900);
 out.push(...await p.evaluate(id=>[...document.querySelectorAll('li.node')].map(li=>{const t=li.querySelector('.nt:not(.warnt):not(.liqt)');return t?id+'|'+li.dataset.node+'|'+t.textContent:null}).filter(Boolean),id));}
console.log(out.join('\n'));await b.close()})();
