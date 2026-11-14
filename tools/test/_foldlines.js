// 접힌 루프 상자(그래프 loops fold:true)마다 밖으로 나가는 선이 그려졌는지 전수 점검(2026-11-12): 성공 선 1개 이상 + worst.to 선(있을 때)
// 테스트 서버 :8779 필요. node _foldlines.js [그래프 id…] (인자 없으면 git으로 바뀐 그래프만, ALL=1이면 전체) → 콘솔 + foldlines.txt (문제 0이어야 함)
const {chromium}=require('playwright'), fs=require('fs');
const SIM=require('path').join(__dirname,'../../site/data/sim');   /* 어느 폴더에서 돌려도(2026-11-13 S2) */
/* 인자 없으면 git으로 바뀐 그래프만, ALL=1이면 전체(RT 2026-11-14) */ const ids=process.argv.slice(2).length ? process.argv.slice(2) : (require('./_changed.js').changedGraphs() || fs.readdirSync(SIM).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5)));
(async()=>{ const b=await chromium.launch(), p=await b.newPage({viewport:{width:1600,height:1000}}); const out=[]; let bad=0, boxes=0;
  for(const id of ids){ const g=JSON.parse(fs.readFileSync(`${SIM}/${id}.json`,'utf8')).graph; const folds=(g.loops||[]).filter(L=>L.fold && L.nodes?.length>=2); if(!folds.length) continue;
    await p.goto('about:blank'); await p.goto(`http://localhost:8779/recipes.html?lang=kr#r-${id}`); await p.waitForFunction(()=>window.__rec && __rec.booted);
    if(!await p.$('[data-rtab="fc"]')){ out.push(`${id}: 플로우차트 탭 없음`); bad++; continue; }
    await p.click('[data-rtab="fc"]'); await p.waitForSelector('.fcpane .fcn');
    const vers=await p.$$eval('[data-simver]', xs=>[...new Set(xs.map(x=>x.dataset.simver))]);
    for(const v of (vers.length?vers:[null])){ if(v){ await p.click(`[data-simver="${v}"]`); await p.waitForTimeout(150); }
      const r=await p.evaluate(fl=>{ const {edges,rects}=window.__fcLast, has=new Set(rects.map(x=>x.id)), res=[];
        fl.forEach(L=>{ const h=L.nodes[0]; if(!has.has(h)) return; if(!document.querySelector(`.fcn.k-fold[data-fcn="${h}"]`)) return;   /* 이 버전에서 루프가 풀려(fcPrune) 접힌 상자가 아님 — 오탐(2026-11-13 S2) */ const outs=edges.filter(e=>e.a===h && e.b!==h && e.on);
          const ok=outs.filter(e=>e.kind==='ok'), w=L.worst?.to;
          res.push({h, ok:ok.map(e=>e.b), worst:w||null, worstOn: !w || outs.some(e=>e.b===w) || !has.has(w)}); }); return res; }, folds);
      for(const x of r){ boxes++; const prob=[]; if(!x.ok.length) prob.push('성공 선 없음'); if(!x.worstOn) prob.push(`최악의 경우 선 없음(→ ${x.worst})`);
        if(prob.length){ bad++; out.push(`${id} [${v}] ${x.h}: ${prob.join(', ')}`); } } } }
  out.push(`접힌 상자 ${boxes}개(버전별) · 문제 ${bad}`); fs.writeFileSync(require('path').join(__dirname,'foldlines.txt'), out.join('\n')); console.log(out.join('\n')); await b.close(); })();
