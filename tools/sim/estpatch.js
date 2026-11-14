/* 가중치 추정 옵션 비용 나누기(사용자 확정 2026-11-14 21:06) — site/data/sim/<id>.json 각 등급 res에 est:{div, names}를 넣음.
   node tools/sim/estpatch.js [id…]   (인자 없으면 전부, release.sh 1단계가 돌림) */
const fs=require('fs'), path=require('path'), S=require('../../site/sim.js');
const ROOT=path.join(__dirname,'..','..'), SIM=path.join(ROOT,'site','data','sim'), GR=path.join(ROOT,'scripts','graphs');
const ids=process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(SIM).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5));
let n=0, withEst=0;
for(const id of ids){ const sf=path.join(SIM,id+'.json'), gf=path.join(GR,id+'.json'); if(!fs.existsSync(sf) || !fs.existsSync(gf)) continue;
  const sim=JSON.parse(fs.readFileSync(sf,'utf8')), g=JSON.parse(fs.readFileSync(gf,'utf8')); let D; try{ D=JSON.parse(fs.readFileSync(path.join(ROOT,'site','data','c',g.cls+'.json'),'utf8')); }catch(_){ continue; }
  let ch=false, any=false;
  for(const st of sim.strategies||[]){ if(!st.res) continue; const e=S.estSplit(g, D, st.res); const v=e.div>0.005 ? {div:+e.div.toFixed(3), names:e.names} : null;
    if(JSON.stringify(st.res.est||null)!==JSON.stringify(v)){ if(v) st.res.est=v; else delete st.res.est; ch=true; } if(v) any=true; }
  if(any) withEst++; if(ch){ fs.writeFileSync(sf, JSON.stringify(sim)); n++; } }
console.log(`추정 옵션 비용: 시뮬 파일 ${n}개 고침 · 추정 옵션이 있는 레시피 ${withEst}개`);
