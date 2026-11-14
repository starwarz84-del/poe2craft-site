// 작업 중 빠른 횟수로 돌린 시뮬 결과(site/data/sim/*.json quick:true) 목록 — RT 2026-11-14
// node tools/sim/quickcheck.js          목록 + '빠른 시뮬 n개'
// node tools/sim/quickcheck.js --rerun  그 그래프를 run.js --final로 다시 돌림 (release.sh --full이 씀)
const fs=require('fs'), path=require('path'), {execFileSync}=require('child_process');
const ROOT=path.join(__dirname,'../..'), dir=ROOT+'/site/data/sim';
const q=fs.readdirSync(dir).filter(f=>f.endsWith('.json')).filter(f=>{ try{ return JSON.parse(fs.readFileSync(dir+'/'+f,'utf8')).quick; }catch(e){ return false; } }).map(f=>f.slice(0,-5));
if(process.argv.includes('--rerun')){ for(const id of q){ const t=Date.now(); execFileSync('node',[__dirname+'/run.js',id,'--final'],{stdio:'ignore'}); console.log(`다시 돌림 ${id} ${((Date.now()-t)/1000).toFixed(0)}초`); }
  const left=fs.readdirSync(dir).filter(f=>f.endsWith('.json')&&JSON.parse(fs.readFileSync(dir+'/'+f,'utf8')).quick).length; console.log(`빠른 시뮬 ${left}개 (다시 돌린 것 ${q.length}개)`); process.exit(left?1:0); }
for(const id of q) console.log(id); console.log(`빠른 시뮬 ${q.length}개`);
