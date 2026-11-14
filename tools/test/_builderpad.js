/* 속성부여 패드·휴대폰 배치 점검(2026-11-14): 1151px 이상 = 베이스 목록 고정, 그보다 좁으면 서랍 + 아이템·옵션 목록 나란히 */
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); let bad=0;
 for(const [w,h,n] of [[1520,950,'wide'],[1100,900,'pad'],[1024,1366,'ipad'],[820,1180,'pad-s'],[390,844,'mob']]){ const p=await b.newPage({viewport:{width:w,height:h}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/builder.html?lang=kr'); await p.waitForSelector('#list .row',{timeout:15000}); await p.waitForTimeout(500);
  const r=await p.evaluate(()=>{ const R=s=>document.querySelector(s).getBoundingClientRect(); const c=R('#card'), l=R('.pool'), d=R('#drawer');
    return {side: Math.abs(c.top-l.top)<4 && l.left>c.right-2, drawerShown: d.right>2, btn: getComputedStyle(document.querySelector('#base-open')).display!=='none', hs: document.documentElement.scrollWidth>innerWidth+1}; });
  let ok = !r.hs && !errs.length;
  if(w>=1151) ok = ok && r.drawerShown && !r.btn && r.side;
  else { ok = ok && !r.drawerShown && r.btn && (w<=760 || r.side);
    await p.click('#base-open'); await p.waitForTimeout(350);
    const open=await p.evaluate(()=>document.querySelector('#drawer').getBoundingClientRect().left>=-1);
    await p.screenshot({path:`shots/bld-${n}-drawer.png`});
    await p.fill('#bq','sapph'); await p.waitForTimeout(150); const hits=await p.$$eval('#bsearch [data-bi]',x=>x.length);
    await p.fill('#bq',''); await p.click('#bases .base >> nth=2'); await p.waitForTimeout(500);
    const closed=await p.evaluate(()=>document.querySelector('#drawer').getBoundingClientRect().right<=2);
    ok = ok && open && closed && hits>0; Object.assign(r,{open,closed,hits}); }
  await p.screenshot({path:`shots/bld-${n}.png`}); if(!ok) bad++; console.log(n, ok?'OK':'문제', JSON.stringify(r), errs); await p.close(); }
 console.log('문제', bad); await b.close(); })();
