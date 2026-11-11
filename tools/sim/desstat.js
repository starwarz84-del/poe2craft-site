// 훼손 출처 통계만 다시 계산해서 sim 파일에 넣음(비용 숫자는 그대로). usage: node tools/sim/desstat.js [graph id…] [N=3000]   (인자 없으면 sim 파일이 있는 그래프 전부)
const fs=require('fs'), path=require('path'), SIM=require('../../site/sim.js');
const ROOT=path.join(__dirname,'../..'); const args=process.argv.slice(2); const N=+(args.find(a=>/^\d+$/.test(a))||3000);
let ids=args.filter(a=>!/^\d+$/.test(a)); if(!ids.length) ids=fs.readdirSync(`${ROOT}/site/data/sim`).filter(f=>f.endsWith('.json')).map(f=>f.slice(0,-5));
const craft=JSON.parse(fs.readFileSync(`${ROOT}/site/data/crafting.json`,'utf8')), prices=JSON.parse(fs.readFileSync(`${ROOT}/site/data/prices.json`,'utf8'));
for(const id of ids){ const gf=`${ROOT}/scripts/graphs/${id}.json`, sf=`${ROOT}/site/data/sim/${id}.json`; if(!fs.existsSync(gf)||!fs.existsSync(sf)) continue;
  const g=JSON.parse(fs.readFileSync(gf,'utf8')), D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${g.cls}.json`,'utf8')), out=JSON.parse(fs.readFileSync(sf,'utf8'));
  for(const st of out.strategies){ const s=g.strategies.find(x=>x.id===st.id); if(!s) continue;
    try{ const r=SIM.simulate(g, D, craft, prices, s.params, N, 11); st.res.desStat=JSON.parse(JSON.stringify(r.desStat,(k,v)=>typeof v==='number'?+v.toFixed(3):v)); }catch(e){ console.log(id, st.id, e.message); } }
  fs.writeFileSync(sf, JSON.stringify(out)); console.log(id, out.strategies.map(x=>x.id+':'+JSON.stringify(x.res.desStat?.side)).join(' ')); }
