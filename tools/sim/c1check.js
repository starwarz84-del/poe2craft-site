// 제작 옵션 규칙 점검(정책 5장 C1, 사용자 확정 2026-11-11): 제작 옵션이 이미 있는데 아스트리드의 창의성 없이 에센스·합금을 쓰는 단계 찾기
// node tools/sim/c1check.js [그래프 id…] → tools/sim/c1check.json (그래프·전략·단계별 완성 1개당 위반 횟수), 0이어야 함
const fs=require('fs'), path=require('path'), SIM=require('../../site/sim.js'); const ROOT=path.join(__dirname,'../..');
const craft=JSON.parse(fs.readFileSync(`${ROOT}/site/data/crafting.json`,'utf8')), prices=JSON.parse(fs.readFileSync(`${ROOT}/site/data/prices.json`,'utf8'));
let ids=process.argv.slice(2); if(!ids.length) ids=fs.readdirSync(`${ROOT}/scripts/graphs`).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5));
const out={}; const nm=id=>{ for(const k in craft) for(const x of craft[k]) if(x.id===id) return x.kr; return id; };
for(const id of ids){ const g=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${id}.json`,'utf8')); if(!fs.existsSync(`${ROOT}/site/data/sim/${id}.json`)) continue;
  const D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${g.cls}.json`,'utf8'));
  for(const s of g.strategies){ if(s.hidden) continue; try{ const r=SIM.simulate({...g, maxSteps:3e5}, D, craft, prices, s.params, 200, 7);
      for(const [n,v] of Object.entries(r.c1||{})) if(v>0.005){ const nd=g.nodes.find(x=>x.id===n); (out[id]=out[id]||[]).push({v:s.id, node:n, cur:nm(nd.cur), per:+v.toFixed(2)}); } }catch(e){ } } }
fs.writeFileSync(`${__dirname}/c1check.json`, JSON.stringify(out,null,1));
for(const [id,x] of Object.entries(out)) console.log(id, [...new Set(x.map(y=>y.node+' '+y.cur))].join(' · '));
console.log('위반 그래프', Object.keys(out).length, '/', ids.length);
