// every flowchart × version: line crossings, overlapping parallel lines and lines through boxes → fclines.txt   (인자 없으면 git으로 바뀐 그래프만, ALL=1이면 전체)
const {chromium}=require('playwright'), fs=require('fs');
/* 인자 없으면 git으로 바뀐 그래프만, ALL=1이면 전체(RT 2026-11-14) */ const ids=process.argv.slice(2).length ? process.argv.slice(2) : (require('./_changed.js').changedGraphs() || fs.readdirSync(require('path').join(__dirname,'../../site/data/sim')).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5)));
(async()=>{ const b=await chromium.launch(); let p=await b.newPage({viewport:{width:1700,height:1000}}); p.setDefaultTimeout(60000); const out=[]; let tot=0;
  /* 인자 없이 전체를 돌 때 한 그래프에서 시간 초과·페이지 오류가 나도 멈추지 않고 그 줄만 '오류'로 적고 다음으로(2026-11-13 S2) */
  for(const id of ids){ try{ await p.goto(`http://localhost:8779/recipes.html?lang=kr&_=${encodeURIComponent(id)}#r-${id}`); await p.waitForFunction(()=>window.__rec && __rec.booted);
    if(!await p.$('[data-rtab="fc"]')){ out.push(`${id}: no flowchart`); continue; }
    await p.click('[data-rtab="fc"]'); await p.waitForSelector('.fcpane .fcn');
    const vers=await p.$$eval('[data-simver]', xs=>xs.map(x=>x.dataset.simver));
    for(const v of vers){ await p.click(`[data-simver="${v}"]`); await p.waitForTimeout(80);
      const r=await p.evaluate(()=>{ const {edges,rects}=window.__fcLast, segs=[]; edges.forEach((e,ei)=>{ for(let i=0;i<e.pts.length-1;i++) segs.push({a:e.pts[i],b:e.pts[i+1],e,ei,i,n:e.pts.length-1}); });
        const iss=[]; const nm=e=>`${e.a}→${e.b}`;
        for(let x=0;x<segs.length;x++) for(let y=x+1;y<segs.length;y++){ const s=segs[x], t=segs[y]; if(s.ei===t.ei) continue; const same = s.e.b===t.e.b || (s.e.lane && s.e.lane===t.e.lane) || s.e.a===t.e.a;
          const v1=s.a[0]===s.b[0], v2=t.a[0]===t.b[0];
          if(v1!==v2){ if(same) continue; const [V,H]=v1?[s,t]:[t,s]; const vx=V.a[0], hy=H.a[1];
            if(vx>Math.min(H.a[0],H.b[0])+1 && vx<Math.max(H.a[0],H.b[0])-1 && hy>Math.min(V.a[1],V.b[1])+1 && hy<Math.max(V.a[1],V.b[1])-1) iss.push(`교차 ${nm(s.e)} × ${nm(t.e)}`); }
          else { if(same) continue; const k=v1?0:1, o=1-k; if(Math.abs(s.a[k]-t.a[k])>=7) continue; const ov=Math.min(Math.max(s.a[o],s.b[o]),Math.max(t.a[o],t.b[o]))-Math.max(Math.min(s.a[o],s.b[o]),Math.min(t.a[o],t.b[o])); if(ov>4) iss.push(`겹침 ${nm(s.e)} ∥ ${nm(t.e)} (${Math.round(ov)}px)`); } }
        for(const s of segs){ if(s.i===0 || s.i===s.n-1) continue; const x0=Math.min(s.a[0],s.b[0]), x1=Math.max(s.a[0],s.b[0]), y0=Math.min(s.a[1],s.b[1]), y1=Math.max(s.a[1],s.b[1]);
          for(const r of rects) if(x1>r.x+2 && x0<r.x+r.w-2 && y1>r.y+2 && y0<r.y+r.h-2) iss.push(`상자 통과 ${nm(s.e)} / ${r.id}`); }
        return [...new Set(iss)]; });
      tot+=r.length; if(r.length) out.push(`${id} [${v}] ${r.length}\n  `+r.join('\n  ')); }
    }catch(e){ out.push(`${id}: 오류 ${String(e).split('\n')[0].slice(0,120)}`); try{ await p.close(); }catch(_){} p=await b.newPage({viewport:{width:1700,height:1000}}); p.setDefaultTimeout(60000); } }
  out.push(`TOTAL ${tot}`); fs.writeFileSync(require('path').join(__dirname,'fclines.txt'), out.join('\n')); console.log(out.slice(-1)[0]); await b.close(); })();
