// 목록 카드가 요약(board.json)으로 그린 것과 원래 계산이 같은지, 목록에서 클래스 파일을 받지 않는지 점검
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(); let bad=0;
 for(const lang of ['kr','en']) for(const sort of ['views','price']){
  const run=async(block)=>{ const p=await b.newPage({viewport:{width:1400,height:900}}); const cls=[]; const errs=[];
   p.on('pageerror',e=>errs.push(e.message)); p.on('request',r=>{ if(/\/data\/c\//.test(r.url())) cls.push(r.url()); });
   if(block) await p.route('**/data/board.json', r=>r.abort());
   await p.goto(`http://localhost:8779/recipes.html?lite&lang=${lang}`); await p.waitForFunction(()=>window.__rec&&__rec.booted);
   if(sort!=='views') await p.click(`#sort [data-sort="${sort}"]`);
   const h=await p.evaluate(()=>[document.querySelector('#board').innerHTML.replace(/<img src="[^"]*"/g,'<img'), document.querySelector('#stats').innerHTML, document.querySelector('#tags').innerHTML, [...__rec.statOpts.keys()].join(',')]);
   await p.close(); return {h, cls:cls.length, errs}; };
  const x=await run(false), y=await run(true);
  const same=x.h.every((v,i)=>v===y.h[i]);
  console.log(lang, sort, '같음', same, '| 요약 사용 시 클래스 파일', x.cls, '| 원래', y.cls, x.errs.concat(y.errs).join(' ')); if(!same||x.cls) bad++;
  if(!same){ const a=x.h[0], c=y.h[0]; let i=0; while(a[i]===c[i]) i++; console.log(' 다른 곳:', a.slice(i-80,i+120), '\n vs', c.slice(i-80,i+120)); }
 }
 await b.close(); process.exit(bad?1:0);})();
