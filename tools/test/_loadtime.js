// 크래프팅 탭 첫 로딩 측정: 받은 파일(크기·시간)과 목록이 그려질 때까지 걸린 시간, 긴 자바스크립트 작업
// node tools/test/_loadtime.js [주소]   (배포 폴더 서버: cd web && python3 -m http.server 8790)
const {chromium}=require('playwright');
const URL=process.argv[2]||'http://localhost:8790/';
(async()=>{const b=await chromium.launch(); const ctx=await b.newContext(); const p=await ctx.newPage();
 const reqs=[]; p.on('response',async r=>{ try{ const h=await r.allHeaders(); reqs.push({u:r.url().replace(/^https?:\/\/[^/]+/,''), s:+(h['content-length']||0)||(await r.body()).length, t:Date.now()}); }catch(_){ } });
 const cdp=await ctx.newCDPSession(p); await cdp.send('Performance.enable');
 const t0=Date.now(); await p.goto(URL);
 const fr=await (async()=>{ for(let i=0;i<200;i++){ const f=p.frames().find(f=>/recipes/.test(f.url())); if(f){ try{ if(await f.evaluate(()=>document.querySelectorAll('.card,.rcard,[data-id]').length>3)) return f; }catch(_){} } await p.waitForTimeout(100); } return null; })();
 const tList=Date.now()-t0; await p.waitForTimeout(1500);
 const m=(await cdp.send('Performance.getMetrics')).metrics.reduce((a,x)=>(a[x.name]=x.value,a),{});
 console.log('목록 보일 때까지', tList,'ms  | JS 실행', Math.round(m.ScriptDuration*1000),'ms  | 레이아웃', Math.round(m.LayoutDuration*1000),'ms');
 const tot=reqs.reduce((a,r)=>a+r.s,0); console.log('받은 파일', reqs.length,'개', Math.round(tot/1024),'KB');
 reqs.sort((a,b)=>b.s-a.s).slice(0,15).forEach(r=>console.log(String(Math.round(r.s/1024)).padStart(6),'KB', String(r.t-t0).padStart(6),'ms', r.u));
 if(fr){ const prof=await fr.evaluate(()=>performance.getEntriesByType('measure').map(x=>x.name+' '+Math.round(x.duration)).join(' | ')); if(prof) console.log(prof); }
 await b.close();})();
