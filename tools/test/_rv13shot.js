// RV13 사용자 반지 화면 점검: 붙여 넣기 → 쪽 표시(접두·접미 희귀도) → 필수 5개 → 초안 → '등록 레시피 「…」를 틀로 씀' 확인, 스크린샷 shots/rv13-*.png
const {chromium}=require('playwright'); const fs=require('fs');
const TXT=require('fs').readFileSync(0,'utf8');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:1000}}); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:'+(process.env.PORT||8779)+'/discover.html?lang='+(process.env.LANG2||'kr')); await p.waitForFunction(()=>window.__rev);
await p.fill('#txt', TXT); await p.click('#go'); await p.waitForSelector('#mods .mod');
const rows=await p.$$eval('#mods .mod .ml', e=>e.map(x=>x.textContent)); console.log(rows.join('\n'));
console.log('flip buttons', await p.$$eval('[data-flip]', e=>e.map(x=>x.dataset.flip)));
await p.screenshot({path:'shots/rv13-mods.png', fullPage:true});
for(const i of (process.env.NEEDI||'0,1,2,4,5').split(',')){ await p.click(`[data-lv="${i}:must"]`); }
await p.check('#qrok'); await p.click('#mk');
await p.waitForFunction(()=>/틀로 씀|as the template|진행 불가|오류/.test(document.body.innerText), null, {timeout:300000}).catch(()=>console.log('timeout'));
const t=await p.evaluate(()=>{ const m=document.body.innerText.match(/.*틀로 씀.*|.*template.*/); return m?m[0]:null; }); console.log('TPL:', t);
await p.waitForTimeout(1500); await p.screenshot({path:'shots/rv13-draft.png', fullPage:true}); await b.close(); })();
