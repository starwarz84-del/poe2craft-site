// 등급 레시피(하이엔드·밸런스·에센셜)의 완성품이 서로 같은지 점검 — 같으면 정책 32 위반(카드가 똑같이 보임)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(); const p=await b.newPage();
 await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
 const r=await p.evaluate(()=>{ const S=window.__rec, all=S.recipes||S.list||[]; const by={};
  all.forEach(x=>{ if(x.tierGroup) (by[x.tierGroup]=by[x.tierGroup]||[]).push(x); });
  const key=x=>{ try{ const a=S.analyse(x), f=a.nodes[a.nodes.length-1].state||[];
    return f.map(m=>m.junk?('J'+m.side):(m.unrev?'U'+m.side:`${m.gi}:${m.tmax||''}:${m.tmin||''}${m.fr?'F':''}`)).sort().join(','); }catch(e){ return 'ERR '+e.message; } };
  const out=[]; for(const [g,xs] of Object.entries(by)){ if(xs.length<2) continue; const ks=xs.map(x=>[x.tier||x.id,key(x)]);
   for(let i=0;i<ks.length;i++) for(let j=i+1;j<ks.length;j++) if(ks[i][1]===ks[j][1]) out.push(`${g}: ${ks[i][0]} = ${ks[j][0]}`); }
  return {n:Object.keys(by).length, out}; });
 console.log('등급 그룹', r.n, '· 완성품이 같은 쌍', r.out.length); r.out.forEach(x=>console.log(' ',x));
 await b.close(); process.exit(r.out.length?1:0);})();
