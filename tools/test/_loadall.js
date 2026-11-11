// 탭마다 첫 로딩: 받은 파일 수·크기, 네트워크가 조용해질 때까지 시간, 큰 파일
// node tools/test/_loadall.js [탭…]   (배포 폴더 서버: cd web && python3 -m http.server 8790)
const {chromium}=require('playwright');
const TABS=process.argv.slice(2).length?process.argv.slice(2):['recipes','discover','emulator','builder','bases','about'];
(async()=>{const b=await chromium.launch();
 for(const t of TABS){ const ctx=await b.newContext(); const p=await ctx.newPage(); const reqs=[]; const t0=Date.now();
  p.on('response',async r=>{ try{ const body=await r.body(); reqs.push({u:r.url().replace(/^https?:\/\/[^/]+/,''), s:body.length, t:Date.now()-t0}); }catch(_){ } });
  await p.goto('http://localhost:8790/#'+t); await p.waitForLoadState('networkidle').catch(()=>{});
  const tot=reqs.reduce((a,r)=>a+r.s,0), last=Math.max(...reqs.map(r=>r.t));
  console.log(`\n[${t}] ${reqs.length}개 ${Math.round(tot/1024)}KB, 마지막 파일 ${last}ms`);
  reqs.sort((a,b)=>b.s-a.s).slice(0,8).forEach(r=>console.log(String(Math.round(r.s/1024)).padStart(6),'KB',String(r.t).padStart(6),'ms',r.u));
  await ctx.close(); }
 await b.close();})();
