/* 성공 회차 옵션(S4, 2026-11-13): 그래프 태그의 shown·shownBy를 시뮬 파일(site/data/sim/<id>.json) graph.tags에 옮김.
   화면 표시만 바뀌는 필드(태그 shown·shownBy, 완성 카드 finals, 상자 show·goal·goalBy, 접힌 루프 goal·steps·item·worst와 등급별 …By)라 시뮬(run.js)을 다시 돌리지 않아도 됨 — run.js도 같은 필드를 옮김. 파일 형식은 run.js와 같게(JSON.stringify).
   node tools/sim/patch_shown.js <그래프 id…>   (id 없으면 그래프 모두) */
const fs=require('fs'), path=require('path'); const R=path.resolve(__dirname,'../..');
const ids=process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(`${R}/scripts/graphs`).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5));
for(const i of ids){ const gp=`${R}/scripts/graphs/${i}.json`, sp=`${R}/site/data/sim/${i}.json`; if(!fs.existsSync(gp) || !fs.existsSync(sp)) continue;
  const g=JSON.parse(fs.readFileSync(gp,'utf8')), raw=fs.readFileSync(sp,'utf8'), d=JSON.parse(raw), T=d.graph?.tags||{}; let ch=0;
  for(const [k,t] of Object.entries(g.tags||{})){ if(!t || !T[k]) continue;
    for(const f of ['shown','shownBy']){ const a=t[f]==null?undefined:JSON.stringify(t[f]), b=T[k][f]==null?undefined:JSON.stringify(T[k][f]); if(a===b) continue; if(a===undefined) delete T[k][f]; else T[k][f]=t[f]; ch++; } }
  /* 같이 옮기는 화면 전용 필드: 완성 카드(finals)·상자 고르는 옵션(show) — 묶음 태그로 되돌린 카드·상자 */
  if(JSON.stringify(g.finals)!==JSON.stringify(d.graph.finals)){ d.graph.finals=g.finals; ch++; }
  const byId=Object.fromEntries((g.nodes||[]).map(n=>[n.id,n])); (d.graph.nodes||[]).forEach(n=>{ const s=byId[n.id]; if(s && JSON.stringify(s.show)!==JSON.stringify(n.show)){ if(s.show===undefined) delete n.show; else n.show=s.show; ch++; } if(s && JSON.stringify(s.goalBy)!==JSON.stringify(n.goalBy)){ if(s.goalBy===undefined) delete n.goalBy; else n.goalBy=s.goalBy; ch++; } if(s && JSON.stringify(s.goal)!==JSON.stringify(n.goal)){ if(s.goal===undefined) delete n.goal; else n.goal=s.goal; ch++; } if(s && s.target && typeof s.target==='object' && 'kr' in s.target && JSON.stringify(s.target)!==JSON.stringify(n.target)){ n.target=s.target; ch++; } });   /* 상자 목표 글(target {kr,en})도 화면 전용(2026-11-13 S9) */   /* 상자 제목(goal)도 화면 전용(2026-11-13 S7) */   /* 일반 상자 goalBy도(2026-11-13 S6) */
  /* 선 이름(label)도 화면 전용 — 같은 상자의 선이 수·순서·도착·결과가 같을 때만 옮김(2026-11-13 S9) */
  (d.graph.nodes||[]).forEach(n=>{ const s=byId[n.id]; if(!s || !Array.isArray(s.edges) || !Array.isArray(n.edges) || s.edges.length!==n.edges.length) return;
    n.edges.forEach((e,i)=>{ const f=s.edges[i]; if(f.to!==e.to || f.res!==e.res) return; if(JSON.stringify(f.label)===JSON.stringify(e.label)) return; if(f.label===undefined) delete e.label; else e.label=f.label; ch++; }); });
  /* 접힌 루프의 화면 필드(목표 글·순서 줄·아이템 칸·최악의 경우, 등급별 goalBy·stepsBy·itemBy 포함, 2026-11-13 S8) — 소속 상자(nodes)는 시뮬과 묶여 있어 그대로 */
  const LF=['goal','goalBy','steps','stepsBy','item','itemBy','worst'], gL=Object.fromEntries((g.loops||[]).map(L=>[L.id,L]));
  (d.graph.loops||[]).forEach(L=>{ const s=gL[L.id]; if(!s) return; LF.forEach(f=>{ if(JSON.stringify(s[f])===JSON.stringify(L[f])) return; if(s[f]===undefined) delete L[f]; else L[f]=s[f]; ch++; }); });
  if(ch){ fs.writeFileSync(sp+'.tmp', JSON.stringify(d)+(raw.endsWith('\n')?'\n':'')); fs.renameSync(sp+'.tmp', sp); console.log(i, 'tags', ch); } }
