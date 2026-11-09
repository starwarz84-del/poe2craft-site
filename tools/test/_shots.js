const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1000}}); p.on('pageerror',e=>console.log('E',e.message));
// 1. mirror bow: folded base preparation, opened
await p.goto('http://localhost:8779/recipes.html?lang=kr#r-mirror-bow-video'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
await p.waitForSelector('#detail .prep'); 
await p.screenshot({path:'shots/mirror-bow-closed.png', clip:await (await p.$('#detail .phase')).boundingBox()});
await p.click('#detail .prep summary'); await p.waitForTimeout(200);
const ph=await p.$('#detail .phase'); await ph.scrollIntoViewIfNeeded(); await p.screenshot({path:'shots/mirror-bow-prep.png', clip:await ph.boundingBox()});
console.log('prep:', await p.$eval('#detail .prep', e=>e.innerText));
console.log('phase heads:', await p.$$eval('#detail .phase h4', es=>es.map(e=>e.innerText.replace(/\n/g,' / '))));
// 2. sandsworn draft
const txt=fs.readFileSync('items/sandsworn-rune.txt','utf8');
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev);
const d=await p.evaluate(async(txt)=>{ const S=__rev; if(!S.index)[S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json());
  const it=await S.parse(txt); return S.makeDraft(it,S.analyse(it)); }, txt);
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
await p.evaluate(d=>window.postMessage({type:'poe2-draft', recipe:d},'*'), d); await p.waitForSelector('#detail .flow'); await p.waitForTimeout(300);
await p.addStyleTag({content:'[data-dhead]{position:static!important}'}); const fl=await p.$('#detail .flow'); await p.screenshot({path:'shots/sandsworn-flow.png', fullPage:true, clip:await fl.boundingBox()}); const ph3=(await p.$$('#detail .phase')).pop(); await p.screenshot({path:'shots/sandsworn-opt.png', fullPage:true, clip:await ph3.boundingBox()});
console.log('sandal heads:', await p.$$eval('#detail .phase h4', es=>es.map(e=>e.innerText.replace(/\n/g,' / '))));
console.log('nav:', await p.$$eval('#detail .nv .nt2', es=>es.map(e=>e.textContent)));
await p.evaluate(()=>document.querySelector('#detail [data-totbox]').open=true); await p.waitForTimeout(100);
const tb=await p.$('#detail [data-totbox]'); await tb.scrollIntoViewIfNeeded(); await p.screenshot({path:'shots/sandsworn-total.png', clip:await tb.boundingBox()});
console.log('total:', await tb.evaluate(e=>e.innerText.replace(/\n/g,' | ')));
const nv=await p.$('#detail .dnav'); await p.screenshot({path:'shots/sandsworn-nav.png', clip:await nv.boundingBox()});
await b.close();})();
