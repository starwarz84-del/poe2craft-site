// 에뮬레이터 '다음 결과 확률·기록·사용량' 칸에 한 번에 보이는 줄 수 + 스크린샷 (배포 폴더 껍데기 안, 8790)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(); for(const [w,h] of [[1920,1000],[1440,860]]){ const p=await b.newPage({viewport:{width:w,height:h}});
 await p.goto('http://localhost:8790/#emulator'); await p.waitForTimeout(2500);
 const f=p.frames().find(x=>x.url().includes('emulator.html'));
 await f.evaluate(()=>{ const c=[...document.querySelectorAll('.cur,[data-cid],button')].find(e=>/진화의 오브|Transmutation/.test(e.title||e.getAttribute('aria-label')||e.textContent)); });
 const vis=async sel=>f.evaluate(sel=>{ const P=document.querySelector('#pane'); const r=P.getBoundingClientRect(); return {h:Math.round(r.height), rows:[...P.querySelectorAll(sel)].filter(e=>{const q=e.getBoundingClientRect(); return q.bottom<=r.bottom+1 && q.top>=r.top-1;}).length, all:P.querySelectorAll(sel).length}; }, sel);
 console.log(w+'x'+h, '확률', JSON.stringify(await vis('.odds-row')));
 await p.evaluate(()=>scrollTo(0,document.body.scrollHeight)); await p.waitForTimeout(400);
 await p.screenshot({path:`shots/emupane-${w}.png`}); await p.close(); }
 await b.close(); })();
