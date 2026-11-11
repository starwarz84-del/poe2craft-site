// 느린 회선(내려받기 20Mbps·지연 50ms)으로 탭마다 첫 로딩 시간 비교: node tools/test/_loadslow.js <포트> [포트2]
const {chromium}=require('playwright');
const ports=process.argv.slice(2).length?process.argv.slice(2):['8790'];
const TABS=['recipes','discover','emulator','builder','bases','about'];
(async()=>{const b=await chromium.launch(); const res={};
 for(const port of ports) for(const t of TABS){ const ctx=await b.newContext(); const p=await ctx.newPage(); let bytes=0;
  p.on('response',async r=>{ try{ bytes+=(await r.body()).length; }catch(_){ } });
  const cdp=await ctx.newCDPSession(p); await cdp.send('Network.enable'); await cdp.send('Network.emulateNetworkConditions',{offline:false, latency:50, downloadThroughput:20e6/8, uploadThroughput:5e6/8});
  const t0=Date.now(); await p.goto(`http://localhost:${port}/#${t}`); await p.waitForLoadState('networkidle').catch(()=>{});
  (res[t]=res[t]||[]).push(`${((Date.now()-t0-500)/1000).toFixed(1)}초 ${(bytes/1048576).toFixed(1)}MB`); await ctx.close(); }
 for(const t of TABS) console.log(t.padEnd(9), res[t].join('  →  '));
 await b.close();})();
