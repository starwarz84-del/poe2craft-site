// 리버스 크래프팅 점수(100점, docs/policies.md 15장) — 2026-11-11 기준 고침: 목표를 등록 레시피의 완성품 카드로
// node _revscore.js [id…]   (테스트 서버 필요)  → revscore.json + 요약.  NOSAVE=1: 저장 안 함(빠른 점검)  REGN=<횟수>: 등록 레시피 시뮬 횟수(기본 400)
// 방법: 등록 레시피 완성품(samples.json)을 붙여 넣은 것처럼 분석 → 레시피 단계가 노리는 옵션(티어 범위·'A 또는 B' 포함) 중 등록 시뮬이 항상(98% 이상) 만드는 줄을 '필수', 나머지는 잡옵,
//       등록 레시피가 베이스에 붙여 사는 옵션은 '베이스에 포함' → 화면과 같은 후보 계산(bestDraftAsync) → 검산 → 플로우차트 → 시뮬.
//       완성 조건은 두 쪽 모두 등록 플로우차트의 require(등록 쪽은 항상 100% — 사용자 지적 2026-11-11: 레시피대로 하면 같은 결과가 나옴. 예전의 '카드 일치율로 나눈 환산'은 잘못된 측정이라 없앰)
//   검산 20: 오류 0            시뮬 완주 20: 막힘 없음 10 + 초안 완성품이 등록 레시피의 완성 조건을 만족(98% 이상) 10
//   비용 배수 30: 초안 ÷ 등록 레시피, 같은 등급끼리. 비용 = 시뮬 useDiv(베이스 값만 뺌, 준비 구역·분열 과정 포함)(화면 revCost와 같음 — 매직 베이스 굴림은 13장 11-13 22:37부터 비용에 넣지 않고 참고 mag·regMag). 완성 조건 98% 미만이면 0,
//     0.5배 아래는 덜 만든 옵션·인식 못 한 옵션이 없을 때만 점수. 1.2배 안 30 · 1.5배 25 · 2배 20 · 3배 12 · 5배 5. 1 div 아래는 같은 값
//   비싼 징조 10: 등록 레시피보다 더 쓴 비싼 징조 수      가중치 근거 10: 모르는 단계 하나마다 -5      정책 준수 10: 검산 경고 하나마다 -3, 인식 못 한 옵션·덜 만든 옵션 하나마다 -5
const {chromium}=require('playwright'); const fs=require('fs'); const {registered, EXP, ROOT}=require('./_regcard.js');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const SAMP=new Set(JSON.parse(fs.readFileSync(ROOT+'/site/data/samples.json')).samples.map(s=>s.id));
let IDS=process.argv.slice(2); if(!IDS.length) IDS=R.filter(r=>SAMP.has(r.id)).map(r=>r.id);
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:'+(process.env.PORT||8779)+'/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
const out=[];
for(const id of IDS){ const r=R.find(x=>x.id===id); if(!r || !SAMP.has(id)) continue; let reg; try{ reg=registered(r, +(process.env.REGN||400)); }catch(e){ out.push({id, skip:'등록 그래프: '+e.message}); continue; }
  if(!reg.fromReq){ out.push({id, skip:'완성 조건에 옵션 지정이 없음(아무 옵션이나 채우면 완성)'}); continue; }
  const buy=((r.start||{}).mods||[]).filter(m=>m.gi!=null && !m.crafted).map(m=>m.gi);
  /* 등록 레시피가 목표 옵션이 다 붙은 분열 희귀 베이스를 사서 시작(시한 차유라 목걸이: 0.2 div) — 리버스는 그 옵션을 만들어야 해서 비용·완성 조건(등록 산 줄은 티어 고정, 리버스 밸런스는 C17로 넓힘) 모두 비교 기준이 아님(W8) */
  { const s0=r.start||{}, ms=s0.mods||[]; if(s0.rar==='rare' && ms.some(m=>m.fr) && ms.filter(m=>m.gi!=null && !m.fr && !m.crafted).length>=2){ out.push({id, skip:'등록 레시피가 목표 옵션이 붙은 분열 베이스 구입으로 시작 — 비교 기준 아님'}); continue; } }
  const tier=r.tier||'high'; const x=await Promise.race([p.evaluate(async([id,card,qt,buy,EXP,OLD,per,rtags,rreq,NOK42,tier,NOALT])=>{ const S=__rev; const x=S.recSamples.find(s=>s.id===id); if(!x) return {skip:'no sample'}; const it=await S.parse(x.text); if(it.err) return {skip:'parse'}; const an=S.analyse(it); if(an.putrid) return {skip:'putrid'};
    S.need=new Set(); S.soft=new Set(); S.tsel={}; S.alt={}; S.altK={}; S.buy=new Set(); S.noVariants=!!OLD; S.noK42=NOK42; const miss=[];
    const took=new Set(); card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const i=an.rows.findIndex((r,k)=>!r.unrev && !took.has(k) && l.opts.some(o=>o.gi===r.m.gi)); if(i<0){ miss.push(ci); return; } const r=an.rows[i], o=l.opts.find(o=>o.gi===r.m.gi); took.add(i); if(r.m.fr) return;
      S.need.add(i); if(o.tmax) S.tsel[i]=Math.max(r.tierNo, Math.min(o.tmax, r.tierCnt)); if(buy.includes(r.m.gi) && r.how==='n') S.buy.add(i);
      /* 유효 옵션군(W8): 등록 완성 조건이 그 자리를 '이 중 아무거나'로 받으면 화면에서 같은 묶음 칩을 고른 것처럼(다른 줄에 있는 옵션·계열은 altOf가 뺌) */ if(l.opts.length>1 && !NOALT){ (S.alt=S.alt||{})[i]=l.opts.filter(x=>x.gi!==r.m.gi).map(x=>({gi:x.gi, tmax:x.tmax||null})); } });
    if(!S.need.size) return {skip:'목표 옵션이 완성품에 없음'};
    let a2=S.needAn(an,0,it), d=null; const t0=performance.now(), bs=new Set([...S.buy].map(i=>an.rows[i]?.m).filter(Boolean)), o={market:1e9, ...(bs.size?{buy:bs}:{})};
    try{ const bd = OLD ? S.bestDraft(it,a2,o) : await S.bestDraftAsync(it,a2,o,null,0); d=bd.d; a2=bd.an; }catch(e){ return {err:['초안 실패: '+e.message]}; }
    if(!d) return {err:['초안 없음']};
    const c=S.verifyDraft(it,a2,d), err=c.filter(z=>z.lv==='err').map(z=>z.kr), warn=c.filter(z=>z.lv==='warn').map(z=>z.kr);
    /* 같은 등급끼리 비교(W2): 초안 그래프를 세 등급으로 만들고 등록 레시피의 등급만 돌림(없으면 하이엔드) */
    const g=POE2GRAPH.fromDraft(d, it.D, {craft:S.craft, grades:['high','bal','ess']}); g.strategies=[g.strategies.find(s=>s.id===tier) || g.strategies[0]]; Object.assign(g.tags, qt, rtags); g.require=rreq || {all:card.map((l,i)=>({has:'q'+i}))};
    let t1=performance.now(), ck=POE2GRAPH.check(g, it.D, S.craft, S.prices, POE2SIM, 40, 2e6); if(ck.strategies[0]?.res && performance.now()-t1 < 4000) ck=POE2GRAPH.check(g, it.D, S.craft, S.prices, POE2SIM, 300, 2e6);
    const st=ck.strategies[0]||{}, res=st.res, use=res?.use||{}; let om=0; for(const k of EXP) om+=use[k]||0;
    /* 덜 만든 옵션(W2): 초안 완성품의 쪽별 옵션 수(시뮬 40회 평균)가 붙여 넣은 아이템보다 적은 만큼. 인식 못 한 줄 = 분석이 버린 줄 */
    const unk=(it.other||[]).filter(o=>o.k==='?').length, want={p:0,s:0}; it.mods.forEach(m=>{ if(want[m.side]!=null) want[m.side]++; }); let short=0;
    if(res){ try{ const run=POE2SIM.make({...g, maxSteps:2e6}, it.D, S.craft, st.params||{}), rn=POE2SIM.rng(9), got={p:0,s:0}; let n=0;
      for(let i=0;i<40;i++) run(rn,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done:(x)=>{ n++; x.mods.forEach(m=>{ if(got[m.side]!=null) got[m.side]++; }); }}});
      if(n) for(const sd of ['p','s']) short+=Math.max(0, Math.round(want[sd]-got[sd]/n)); }catch(_){ } }
    const cost = res ? S.revCost(it, d, res) : null, mag = res ? S.magicDiv(it, d) : 0;
    const top=Object.entries(use).map(([k,v])=>[k, v*(k==='Exalted_Orb'?1:(S.prices.p[k]||0))/S.prices.divine]).sort((a,b)=>b[1]-a[1]).slice(0,3).map(([k,v])=>k+' '+v.toFixed(1));
    return {err, warn, unk, short, mag, tier:g.strategies[0].id, stuck:st.runaway||st.error||null, div:cost, match:res?res.reqOk:null, om, top, miss:miss.length, pick:d.pick||null, knowhow:d.knowhow||null, steps:d.nodes.length, ms:Math.round(performance.now()-t0), d};
  },[id,reg.card,reg.qt,buy,EXP,process.env.V==='old',reg.per,reg.rtags,reg.rreq,!!process.env.NOK42,tier,!!process.env.NOALT]), new Promise(z=>setTimeout(()=>z({err:['시간 초과']}),180000))]);
  out.push({id, reg, ...x}); }
await p.goto('http://localhost:'+(process.env.PORT||8779)+'/recipes.html?lang=kr&debug=1'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const unk=await p.evaluate(ds=>{ const R=__rec, o={}; for(const d of ds){ try{ d.likes=0; d.success=0; const a=R.analyse(d); o[d.id]=a.nodes.filter(n=>n.pUnknown).length; }catch(e){ o[d.id]=0; } } return o; }, out.filter(x=>x.d).map(x=>x.d));
await b.close();
const rows=out.map(x=>{ if(x.skip) return {id:x.id, skip:x.skip}; const reg=x.reg, o={div:reg.div, om:reg.om, raw:reg.div, match:reg.match}, pts={}, why=[];
  pts.ver = x.err?.length ? 0 : 20; if(x.err?.length) why.push('검산 오류: '+x.err[0]);
  const stuck=!!x.stuck || x.div==null, okM = x.match!=null && x.match>=0.98; pts.sim = (stuck?0:10) + (okM?10:0);
  if(stuck) why.push('시뮬이 끝나지 않음'+(x.stuck?` (${String(x.stuck).slice(0,40)})`:'')); else if(!okM) why.push(`완성 조건 일치 ${Math.round((x.match||0)*100)}%`);
  const k = x.div!=null ? Math.max(x.div,1)/Math.max(o.div,1) : null;
  /* 등록보다 2배 넘게 싸면(0.5배 아래) 완성 조건·옵션 수를 확인한 뒤에만 만점 — 덜 만든 초안이 싸 보이는 것 방지(W2, 6장 결정 6) */
  const cheapBad = k!=null && k<0.5 && (x.short>0 || x.unk>0);
  pts.cost = k==null || !okM || cheapBad ? 0 : k<=1.2 ? 30 : k<=1.5 ? 25 : k<=2 ? 20 : k<=3 ? 12 : k<=5 ? 5 : 0; if(k==null) why.push('비용 비교 불가'); else if(!okM) why.push('완성 조건 98% 미만이라 비용 점수 0'); else if(cheapBad) why.push(`등록보다 ${(1/k).toFixed(1)}배 싸지만 옵션 수가 모자라 비용 점수 0`); else if(k>1.5) why.push(`비용 ${k.toFixed(1)}배 (${x.div.toFixed(1)} vs ${o.div.toFixed(1)} div)`);
  const dOm = x.div!=null ? x.om - o.om : null;
  pts.om = dOm==null ? 0 : dOm<=0.5 ? 10 : x.om<=o.om*2+1 ? 7 : x.om<=o.om*5+3 ? 4 : 0; if(dOm>0.5) why.push(`비싼 징조 ${x.om.toFixed(1)}개 (등록 ${o.om.toFixed(1)})`);
  const u = x.d ? unk[x.d.id]||0 : 0; pts.w = Math.max(0, 10-5*u); if(u) why.push(`가중치 모름 ${u}단계`);
  const wn=(x.warn||[]).length; pts.pol = Math.max(0, 10-3*wn-5*(x.unk||0)-5*(x.short||0)); if(wn) why.push(`검산 경고 ${wn}`); if(x.unk) why.push(`인식 못 한 옵션 ${x.unk}개`); if(x.short) why.push(`덜 만든 옵션 ${x.short}개`);
  if(x.miss) why.push(`목표 옵션 ${x.miss}개가 완성품 글에 없음`);
  return {id:x.id, score:Object.values(pts).reduce((s,v)=>s+v,0), pts, k:k==null?null:+k.toFixed(2), div:x.div, orig:o.div, tier:x.tier, mag:x.mag, regMag:reg.mag, unk:x.unk, short:x.short, regRaw:o.raw, regMatch:o.match, match:x.match, om:x.om, top:x.top, pick:x.pick, knowhow:x.knowhow, why, ms:x.ms}; });
if(process.env.DUMP) fs.writeFileSync(process.env.DUMP, JSON.stringify(rows,null,1));
if(!process.env.NOSAVE) fs.writeFileSync(__dirname+'/revscore'+(process.env.V==='old'?'-old':'')+'.json', JSON.stringify(rows));
const ok=rows.filter(r=>r.score!=null), ks=ok.map(r=>r.k).filter(v=>v!=null).sort((a,b)=>a-b);
console.log(`초안 ${ok.length}개 · 평균 ${(ok.reduce((s,r)=>s+r.score,0)/Math.max(1,ok.length)).toFixed(1)}점 · 70점 미만 ${ok.filter(r=>r.score<70).length}개 · 비용 배수 중앙값 ${ks[Math.floor(ks.length/2)]} · 1.5배 안 ${ks.filter(k=>k<=1.5).length} · 5배 넘음 ${ks.filter(k=>k>5).length} · 검산 오류 ${ok.filter(r=>!r.pts.ver).length} · 시뮬 문제 ${ok.filter(r=>r.pts.sim<20).length}`);
})();
