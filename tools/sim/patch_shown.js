/* 성공 회차 옵션(S4, 2026-11-13): 그래프 태그의 shown·shownBy를 시뮬 파일(site/data/sim/<id>.json) graph.tags에 옮김.
   화면 표시만 바뀌는 필드(태그 shown·shownBy, 완성 카드 finals, 상자 show)라 시뮬(run.js)을 다시 돌리지 않아도 됨 — run.js도 같은 필드를 옮김. 파일 형식은 run.js와 같게(JSON.stringify).
   node tools/sim/patch_shown.js <그래프 id…>   (id 없으면 그래프 모두) */
const fs=require('fs'), path=require('path'); const R=path.resolve(__dirname,'../..');
const ids=process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(`${R}/scripts/graphs`).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5));
for(const i of ids){ const gp=`${R}/scripts/graphs/${i}.json`, sp=`${R}/site/data/sim/${i}.json`; if(!fs.existsSync(gp) || !fs.existsSync(sp)) continue;
  const g=JSON.parse(fs.readFileSync(gp,'utf8')), raw=fs.readFileSync(sp,'utf8'), d=JSON.parse(raw), T=d.graph?.tags||{}; let ch=0;
  for(const [k,t] of Object.entries(g.tags||{})){ if(!t || !T[k]) continue;
    for(const f of ['shown','shownBy']){ const a=t[f]==null?undefined:JSON.stringify(t[f]), b=T[k][f]==null?undefined:JSON.stringify(T[k][f]); if(a===b) continue; if(a===undefined) delete T[k][f]; else T[k][f]=t[f]; ch++; } }
  /* 같이 옮기는 화면 전용 필드: 완성 카드(finals)·상자 고르는 옵션(show) — 묶음 태그로 되돌린 카드·상자 */
  if(JSON.stringify(g.finals)!==JSON.stringify(d.graph.finals)){ d.graph.finals=g.finals; ch++; }
  const byId=Object.fromEntries((g.nodes||[]).map(n=>[n.id,n])); (d.graph.nodes||[]).forEach(n=>{ const s=byId[n.id]; if(s && JSON.stringify(s.show)!==JSON.stringify(n.show)){ if(s.show===undefined) delete n.show; else n.show=s.show; ch++; } if(s && JSON.stringify(s.goalBy)!==JSON.stringify(n.goalBy)){ if(s.goalBy===undefined) delete n.goalBy; else n.goalBy=s.goalBy; ch++; } });   /* 일반 상자 goalBy도(2026-11-13 S6) */
  if(ch){ fs.writeFileSync(sp+'.tmp', JSON.stringify(d)+(raw.endsWith('\n')?'\n':'')); fs.renameSync(sp+'.tmp', sp); console.log(i, 'tags', ch); } }
