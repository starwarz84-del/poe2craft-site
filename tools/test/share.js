// Shared recipes: register a Discover draft, see someone else's new recipe (badge + toast + NEW tag), reject unsafe data.
// Uses a fake in-memory db in place of the artifact runtime. Needs the test server (serve.sh start).
const {chromium}=require('playwright');
const fake = () => {
  if(window!==window.top) return;
  const store = {}, subs = [];
  const snap = () => ({docs:Object.keys(store).filter(k=>k.startsWith('shared/')).map(k=>({id:k.split('/')[1], exists:true, data:()=>store[k]})), metadata:{fromCache:false}});
  const fire = () => setTimeout(()=>subs.forEach(f=>f(snap())), 30);
  const db = {
    collection:p=>({onSnapshot:(f)=>{ subs.push(f); fire(); return ()=>{}; }}),
    doc:p=>({get:async()=>({exists:!!store[p], data:()=>store[p]}), set:async(v)=>{ store[p]=JSON.parse(JSON.stringify(v)); fire(); }})
  };
  const user = {id:async()=>'me1', can:async()=>true};
  window.__fake = {store, fire};
  window.claude = {use:async n=> n==='db'?db : n==='user'?user : null};
};
(async()=>{
  const b=await chromium.launch(), p=await b.newPage(); await p.route(/fonts\./,r=>r.abort());
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.addInitScript(fake);
  const rec = await (await fetch('http://localhost:8779/data/recipes.json')).json();
  const base = rec.recipes[0];
  await p.goto('http://localhost:8779/app.html#emulator');
  // a reverse draft group (flowchart + three grades, tools/test/items/draft-group.json) and an old draft without a flowchart
  const grp = JSON.parse(require('fs').readFileSync(__dirname+'/items/draft-group.json','utf8')); const G=grp.id;
  const reid = (x,id) => ({...x, id, tierGroup:'draft-test1'});
  const group = {...reid(grp,'draft-test1'), grades:grp.grades.map(x=>reid(x,'draft-test1'+x.tier))};
  await p.evaluate(([g,r])=>{ localStorage.setItem('poe2lang','kr'); localStorage.setItem('poe2r:drafts', JSON.stringify([g, {...r, id:'draft-old1'}])); localStorage.removeItem('poe2seen'); }, [group, base]);
  await p.goto('http://localhost:8779/app.html#r-draft-old1'); await p.waitForTimeout(3000);
  const fr = () => p.frames().find(f=>f.url().includes('recipes.html'));
  const ok = (c,m)=>console.log((c?'PASS ':'FAIL ')+m);
  ok(await fr().locator('[data-share]').count()===0, '플로우차트 없는 초안은 공유 버튼 없음');
  await p.evaluate(()=>{ location.hash='r-draft-test1'; }); await p.waitForTimeout(1500);
  ok(await fr().locator('[data-share]').count()===1, '초안에 "공유 레시피로 등록" 버튼');
  await fr().locator('[data-share]').click(); await p.waitForTimeout(1500);
  const st = await p.evaluate(()=>window.__fake.store);
  ok(st['shared/me1'] && st['shared/me1'].recipes['s-test1'], '저장소에 shared/me1 → s-test1 저장');
  { const sr=st['shared/me1']?.recipes['s-test1']?.recipe; ok(sr && sr.simInline?.graph?.nodes?.length && sr.grades?.length===2 && sr.grades.map(x=>x.id).join()==='s-test1bal,s-test1ess', '플로우차트 + 등급 3개가 한 묶음으로 저장'); }
  ok((await fr().evaluate(()=>window.__rec.recipes.filter(r=>r.tierGroup==='s-test1').map(r=>r.tier).join())) === 'high,bal,ess', '공유 레시피 등급 탭 3개');
  await fr().locator('[data-rtab="fc"]').click().catch(()=>{}); await p.waitForTimeout(800);
  ok(await fr().locator('.fcin, .simbox svg').count()>0, '공유 레시피 플로우차트 표시');
  ok(await fr().evaluate(()=>window.__rec.open==='s-test1' && document.querySelectorAll('.tag.shb').length>0), '등록 후 "내 공유 레시피" 표시');
  ok((await fr().evaluate(()=>JSON.parse(localStorage.getItem('poe2r:drafts')||'[]').map(x=>x.id).join()))==='draft-old1', '로컬 초안(묶음)은 지워짐');
  // someone else shares while I'm on another tab
  await p.evaluate(()=>{ location.hash='emulator'; }); await p.waitForTimeout(500);
  await p.evaluate(r=>{ window.__fake.store['shared/other']={recipes:{'s-other1':{recipe:{...r, id:'s-other1', tierGroup:'s-other1', grades:[], title:{kr:'남의 레시피 — 테스트',en:'Other — test'}}, at:Date.now()}}}; window.__fake.fire(); }, {...grp, grades:undefined});
  await p.waitForTimeout(800);
  ok((await p.locator('nav a[data-view=recipes] .nb').textContent())==='1', '레시피 탭 배지 1');
  ok(await p.locator('.toast').count()===1, '새 레시피 알림 표시');
  await p.locator('.toast').click(); await p.waitForTimeout(1500);
  ok(await fr().evaluate(()=>window.__rec.open)==='s-other1', '알림 클릭 → 그 레시피 열림');
  ok(await fr().locator('.tag.newb').count()>0, 'NEW 표시');
  ok(await p.locator('nav a[data-view=recipes] .nb').count()===0, '레시피 탭을 보면 배지 사라짐');
  // unsafe and broken data
  await p.evaluate(r=>{ window.__fake.store['shared/bad']={recipes:{
    's-bad1':{recipe:{...r, id:'s-bad1', grades:[], title:{kr:'<img src=x onerror="window.__x=1"> — 악성',en:'<img src=x onerror="window.__x=1"> — bad'}, patch:'<b>'}, at:Date.now()},
    's-nofc1':{recipe:{...r, id:'s-nofc1', grades:[], simInline:undefined}, at:Date.now()},
    's-bad2':{recipe:{id:'s-bad2', cls:'Nope', nodes:[]}, at:Date.now()},
    'x':{recipe:{...r, id:'../x'}, at:Date.now()} }}; window.__fake.fire(); }, {...grp, grades:undefined});
  await p.waitForTimeout(1200); await fr().evaluate(()=>{ location.hash=''; });
  const ids = await fr().evaluate(()=>window.__rec.recipes.filter(r=>r.shared).map(r=>r.id));
  ok(ids.includes('s-bad1') && !ids.includes('s-bad2') && !ids.includes('../x') && !ids.includes('s-nofc1'), '잘못된·플로우차트 없는 레시피는 거름: '+ids.join(','));
  ok(!(await fr().evaluate(()=>window.__x)) && !(await fr().locator('img[src=x]').count()), 'HTML 주입 차단');
  // unshare my own
  await fr().evaluate(()=>window.__rec.open); await p.evaluate(()=>{ location.hash='r-s-test1'; }); await p.waitForTimeout(800);
  await fr().locator('[data-unshare]').click(); await p.waitForTimeout(200);
  ok(!(await p.evaluate(()=>window.__fake.store['shared/me1'].recipes['s-test1']===undefined)), '한 번 누르면 아직 안 지움');
  await fr().locator('[data-unshare]').click(); await p.waitForTimeout(1200);
  ok(!(await p.evaluate(()=>window.__fake.store['shared/me1'].recipes['s-test1'])), '공유 취소 → 저장소에서 삭제');
  ok(!errs.length, '페이지 오류 없음 '+errs.join(' | '));
  await b.close();
})();
