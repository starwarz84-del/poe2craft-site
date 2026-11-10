// 새 레시피 상세 스크린샷: node _newrec.js id1,id2 [en]
const {chromium}=require('playwright');
(async()=>{ const br=await chromium.launch(); const ids=process.argv[2].split(','), en=process.argv[3]==='en';
 for(const id of ids){ const p=await br.newPage({viewport:{width:1280,height:2400}}); await p.addInitScript(l=>{ try{localStorage.setItem('poe2lang',l)}catch(e){} }, en?'en':'kr');
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto(`http://localhost:8790/?_=${id}#r-${id}`); await p.waitForTimeout(3500);
  await p.screenshot({path:`shots/new-${id}${en?'-en':''}.png`}); console.log(id, errs.length?errs:'ok'); await p.close(); }
 await br.close(); })();
