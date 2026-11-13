// 리버스 틀 점검(W9, docs/reverse-pipeline.md 2-1): 등록 레시피 완성품(samples.json)을 붙여 넣고 _revscore와 같은 필수 옵션을 고른 뒤
//   ① 자기 틀: 그 레시피의 그래프가 틀 후보로 잡히고(옵션 0개 바꿈), 틀 그래프 시뮬 비용이 등록 시뮬(site/data/sim) 같은 등급 값의 ±5% 안
//   ② 고르기: bestDraftAsync가 틀(자기 그래프)을 고름 — PICK=1일 때만(느림)
// node _revtpl.js [id…]   (테스트 서버 필요, 기본 = 샘플이 있는 레시피 전부)   N=<시뮬 횟수, 기본 2000>
// 끝 줄 '문제 0'이 기준. 틀로 못 쓰는 레시피(완성 조건이 등급 매개변수뿐 등)는 '건너뜀'으로 따로 셈
const {chromium}=require('playwright'); const fs=require('fs'); const {registered, ROOT}=require('./_regcard.js');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const SAMP=new Set(JSON.parse(fs.readFileSync(ROOT+'/site/data/samples.json')).samples.map(s=>s.id));
const TPL=JSON.parse(fs.readFileSync(ROOT+'/site/data/revtpl.json')).g;
let IDS=process.argv.slice(2); if(!IDS.length) IDS=R.filter(r=>SAMP.has(r.id)).map(r=>r.id);
const N=+(process.env.N||2000);
(async()=>{ const b=await chromium.launch(); const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:'+(process.env.PORT||8779)+'/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
const rows=[]; let bad=0, skip=0;
for(const id of IDS){ const r=R.find(x=>x.id===id); if(!r) continue; const gid=r.simId||r.tierGroup||r.id;
  if(!TPL[gid]){ rows.push(`${id}: 건너뜀 (틀 목록에 없음)`); skip++; continue; }
  let reg; try{ reg=registered(r, 50); }catch(e){ rows.push(`${id}: 건너뜀 (${e.message})`); skip++; continue; }
  const sim=JSON.parse(fs.readFileSync(`${ROOT}/site/data/sim/${gid}.json`)), tier=r.tier||'high', st=sim.strategies.find(s=>s.id===tier) || sim.strategies.find(s=>!s.hidden), want=st?.res?.useDiv;
  const x=await p.evaluate(async([id,card,per,gid,tier,N,PICK])=>{ const S=__rev; const smp=S.recSamples.find(s=>s.id===id); if(!smp) return {skip:'샘플 없음'};
    const it=await S.parse(smp.text); if(it.err) return {skip:'읽기 실패'}; const an=S.analyse(it);
    S.need=new Set(); S.soft=new Set(); S.tsel={}; S.alt={}; S.altK={}; S.buy=new Set(); S.tplSkip=null;
    const took=new Set(); card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const i=an.rows.findIndex((r,k)=>!r.unrev && !took.has(k) && l.opts.some(o=>o.gi===r.m.gi)); if(i<0) return; const r=an.rows[i], o=l.opts.find(o=>o.gi===r.m.gi); took.add(i); if(r.m.fr) return;
      S.need.add(i); if(o.tmax) S.tsel[i]=Math.max(r.tierNo, Math.min(o.tmax, r.tierCnt)); if(l.opts.length>1) S.alt[i]=l.opts.filter(x=>x.gi!==r.m.gi).map(x=>({gi:x.gi, tmax:x.tmax||null})); });
    if(!S.need.size) return {skip:'필수 옵션 없음'};
    const a2=S.needAn(an,0,it), base0=S.makeDraft(it,a2,{market:1e9}); await S.loadTpl();
    const ms=S.tplMatch(it,a2), own=ms.find(m=>m.t.g===gid); const T=await S.tplDrafts(it,a2,base0), mine=T.find(x=>x.m.t.g===gid && x.m.grades.includes(tier)) || T.find(x=>x.m.t.g===gid);
    if(!own) return {miss:'자기 틀 짝짓기 실패', got:ms.map(m=>m.t.g)};
    if(!mine) return {miss:'자기 틀 탈락: '+(S.tplWhy?.[gid]||'?')};
    const ve=S.verifyDraft(it,a2,mine.d).filter(z=>z.lv==='err').map(z=>z.kr);
    const g=POE2GRAPH.fromDraft(mine.d, it.D, {grades:[tier]}), s0=g.strategies.find(s=>s.id===tier) || g.strategies[0];
    const res=POE2SIM.simulate({...g, maxSteps:3e5}, it.D, S.craft, S.prices, s0.params, N, 7);
    let pick=null; if(PICK){ S.tplSkip=null; const bd=await S.bestDraftAsync(it,a2,{market:1e9},null,0); pick={tpl:bd.d?.tpl?.g||null, cmp:bd.d?.tpl?.cmp||S.tplCmp||null}; }
    return {changed:own.changed, ve, grade:s0.id, div:res.useDiv, reqOk:res.reqOk, c1:Object.keys(res.c1||{}).length, pick};
  },[id,reg.card,reg.per,gid,tier,N,!!process.env.PICK]);
  if(x.skip){ rows.push(`${id}: 건너뜀 (${x.skip})`); skip++; continue; }
  if(x.miss){ rows.push(`${id}: 문제 — ${x.miss}${x.got?' · 잡힌 틀 '+x.got.join(','):''}`); bad++; continue; }
  const k=want>0 ? x.div/want : (x.div<0.05?1:9), off=Math.abs(k-1)>0.05 && Math.abs(x.div-want)>0.5;
  const pickBad = x.pick && x.pick.tpl!==gid;
  const probs=[x.changed?`옵션 ${x.changed}개 바뀜`:null, x.ve.length?'검산 오류 '+x.ve[0]:null, x.reqOk<0.98?`완성 조건 ${Math.round(x.reqOk*100)}%`:null, x.c1?'제작 옵션 한도':null, off?`비용 ${x.div.toFixed(1)} vs 등록 ${want.toFixed(1)} (${k.toFixed(2)}배)`:null, pickBad?`고른 초안 = ${x.pick.tpl||'생성 후보'} ${JSON.stringify(x.pick.cmp)}`:null].filter(Boolean);
  if(probs.length) bad++;
  rows.push(`${id}: ${probs.length?'문제 — '+probs.join(' · '):'통과'} · ${x.grade} ${x.div.toFixed(1)} div (등록 ${want!=null?want.toFixed(1):'-'})${x.pick?' · 고름 '+(x.pick.tpl||'생성')+(x.pick.cmp?' '+JSON.stringify(x.pick.cmp):''):''}`); }
await b.close();
console.log(rows.join('\n')); console.log(`자기 틀 ${IDS.length}개 · 건너뜀 ${skip} · 문제 ${bad}`);
})();
