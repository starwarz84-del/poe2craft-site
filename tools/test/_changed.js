// 바뀐 그래프 id 목록(RT 2026-11-14, 사용자: 테스팅 구간 줄이기) — 플로우차트 전체 점검(_fclines·_foldlines·_fccardsame)을 인자 없이 돌릴 때 씀.
// 바뀜 = origin/main 대비 커밋된 차이 + 커밋 안 한 수정 + 새 파일 중 scripts/graphs/<id>.json · site/data/sim/<id>.json
// ALL=1이면 null(= 전체). 화면 그리는 공용 코드(site/recipes.html·sim.js·graph2recipe.py)가 바뀌었으면 알림만 띄움(전체는 ALL=1로).
const {execSync}=require('child_process'), path=require('path'), fs=require('fs');
const ROOT=path.join(__dirname,'../..');
function changedGraphs(){ if(process.env.ALL) return null;
  const sh=c=>{ try{ return execSync(c,{cwd:ROOT,encoding:'utf8',stdio:['ignore','pipe','ignore']}); }catch(e){ return ''; } };
  const files=new Set([...sh('git diff --name-only origin/main -- scripts/graphs site/data/sim site/recipes.html site/sim.js scripts/graph2recipe.py').split('\n'), ...sh('git ls-files --others --exclude-standard -- scripts/graphs site/data/sim').split('\n')].filter(Boolean));
  const ids=new Set(); for(const f of files){ const m=f.match(/^(?:scripts\/graphs|site\/data\/sim)\/([^/]+)\.json$/); if(m && fs.existsSync(`${ROOT}/site/data/sim/${m[1]}.json`)) ids.add(m[1]); }
  const shared=[...files].filter(f=>!/^(scripts\/graphs|site\/data\/sim)\//.test(f)); if(shared.length) console.error(`알림: 공용 코드 바뀜(${shared.join(', ')}) — 모든 그래프를 보려면 ALL=1`);
  console.error(ids.size ? `바뀐 그래프만 ${ids.size}개: ${[...ids].join(', ')} (전체는 ALL=1)` : '바뀐 그래프 없음 — 전체는 ALL=1');
  return [...ids]; }
module.exports={changedGraphs};
