// 룬 태그 수 = 소켓 수(장착 룬 + 빈 소켓)인지 모든 레시피에서 확인, 첫 문제 레시피는 스크린샷
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1000}});
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const ids=await p.evaluate(()=>__rec.recipes.filter(r=>(r.sockets||r.exceptional)).map(r=>r.id));
let bad=0, shot=0;
for(const id of ids){
  await p.goto('http://localhost:8779/recipes.html?lang=kr#r-'+id); await p.reload(); await p.waitForFunction(()=>window.__rec&&__rec.booted);
  await p.waitForTimeout(300);
  const r=await p.evaluate(()=>{const all=[...document.querySelectorAll('.tt-mod.rune .tier.r, .tt-mod.slot0 .tier.r')]; const vis=all.filter(e=>getComputedStyle(e).visibility!=='hidden').length; return {lines:document.querySelectorAll('.tt-mod.rune').length, vis};});
  if(r.lines>r.vis){ console.log(id, 'lines', r.lines, 'tags', r.vis); if(!shot++){ const el=await p.$('.tt-mod.rune'); if(el) await el.evaluate(e=>e.scrollIntoView()); await p.screenshot({path:'/tmp/claude-0/-home-claude/ddca7bd4-ffaf-59ce-a614-4adeacb1bf58/scratchpad/rune.png'}); } }
}
console.log('checked', ids.length); await b.close();})();
