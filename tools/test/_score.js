// 레시피 점수용 엔진 값: 레시피마다 비용(확정/추가 포함)·가중치 모름 단계·실패 처리 없는 확률 단계 → score_eng.json
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr&debug=1'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const res=await p.evaluate(()=>{ const R=__rec; const o={};
 for(const r of R.recipes){ if(r.draft) continue; delete r._an; try{ const a=R.analyse(r), c=R.recipeCost(r);
   const noFail=a.nodes.filter(x=>{ const n=x.n; if(['note','base','manual','quality','socket'].includes(n.do)) return false; if(!(x.p<0.995) || x.pUnknown) return false;
     return !(n.fail || n.compromise || n.optional || n.branch || n.expect || n.onLost || n.target?.asIs || n.target?.anyReveal || a.nodes.some(y=>y.n.fallbackFor===n.id)); }).map(x=>x.n.id);
   const mainAll=(()=>{ try{ return +R.divOf(a.totAll).v.toFixed(2); }catch(_){ return null; } })();   // 베이스 값·준비 비용을 뺀 옵션 추가 작업 구간(시뮬의 같은 구간과 비교)
   o[r.id]={v:c?+c.v.toFixed(2):null, all:c?+c.all.toFixed(2):null, main:mainAll, unk:a.nodes.filter(x=>x.pUnknown).map(x=>x.n.id), guess:a.nodes.filter(x=>x.pGuess && !x.pUnknown).map(x=>x.n.id), noFail};
 }catch(e){ o[r.id]={err:e.message}; } } return o; });
fs.writeFileSync('score_eng.json', JSON.stringify(res)); console.log(Object.keys(res).length); await b.close();})();
