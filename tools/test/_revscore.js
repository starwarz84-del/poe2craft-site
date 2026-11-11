// 리버스 크래프팅 점수(100점, docs/policies.md 15장): 등록 레시피의 완성품으로 초안 → 검산 → 플로우차트 → 시뮬 → 등록 레시피의 시뮬 비용과 비교
// node _revscore.js [id…]   (테스트 서버 필요)  → revscore.json + 요약 출력.  V=old 이면 복구 후보 비교 없이(예전 초안)
//   검산 20: 오류 0            시뮬 완주 20: 막힘 없음 10 + 필수 옵션 98% 이상 10
//   비용 배수 30: 초안 ÷ 등록 레시피(옵션 추가 작업 구간 시뮬 평균) 1.2배 안 30 · 1.5배 25 · 2배 20 · 3배 12 · 5배 5
//   비싼 징조 10: 등록 레시피보다 더 쓴 비싼 징조 수      가중치 근거 10: 모르는 단계 하나마다 -5      정책 준수 10: 검산 경고 하나마다 -3
const {chromium}=require('playwright'); const fs=require('fs'); const ROOT='/home/claude/poe2data';
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const SAMP=new Set(JSON.parse(fs.readFileSync(ROOT+'/site/data/samples.json')).samples.map(s=>s.id));
const EXP=['Omen_of_Whittling','Omen_of_Sinistral_Erasure','Omen_of_Dextral_Erasure','Omen_of_Sinistral_Annulment','Omen_of_Dextral_Annulment','Omen_of_Light','Hinekoras_Lock'];
// 레시피가 노리는 옵션 = 필수(레시피 티어 범위), '결과 그대로' 옵션 = 유효
const LV={};
const add=(d,t,soft)=>{ if(!t||typeof t!=='object') return; if(Number.isInteger(t.gi)){ (soft?d.soft:d.must).push(t.gi); if(t.tmax) d.tmax[t.gi]=Math.max(d.tmax[t.gi]||0,t.tmax); }
  for(const k of ['anyOf','all']) (t[k]||[]).forEach(x=>add(d,x,soft)); if(t.reveal&&typeof t.reveal==='object') add(d,t.reveal,soft); };
for(const r of R){ if(!SAMP.has(r.id)) continue; const d={must:[],soft:[],tmax:{}};
  ((r.start||{}).mods||[]).forEach(m=>{ if(m.gi!=null && !m.fr) add(d,m,false); });
  d.buy=((r.start||{}).mods||[]).some(m=>m.fr) ? ((r.start||{}).mods||[]).filter(m=>m.gi!=null && !m.fr && !m.crafted).map(m=>m.gi) : [];   // 분열 베이스에 붙여 사는 옵션 = '베이스에 포함'
  // 실패 처리(다시 하기)가 없는 확률 단계 = 결과 그대로 받는 옵션 → 유효
  const fbk=new Set(r.nodes.filter(n=>n.fallbackFor && n.do!=='note').map(n=>n.fallbackFor));
  r.nodes.forEach(n=>{ const t=n.target||{}, roll=['exalt','reveal','regal','transmute','augment','chaos'].includes(n.do);
    add(d,t,!!(t.asIs||t.anyReveal||n.optional||(roll && !n.fail && !fbk.has(n.id) && !n.expect))); });
  d.must=[...new Set(d.must)]; d.soft=[...new Set(d.soft)].filter(g=>!d.must.includes(g)); LV[r.id]=d; }
// 등록 레시피의 시뮬 값(그 등급, 옵션 추가 작업 구간만 — 초안은 준비가 끝난 베이스에서 시작)
const KT={'하이엔드':'high','밸런스':'bal','에센셜':'ess'};
function orig(r){ const f=`${ROOT}/site/data/sim/${r.simId||r.tierGroup||r.id}.json`; if(!fs.existsSync(f)) return null; const d=JSON.parse(fs.readFileSync(f));
  const v=(d.graph.versions||[]).find(v=>(v.tier||KT[v.kr])===(r.tier||'high')); if(!v) return null;
  const s=d.strategies.find(s=>Object.entries(v.params).every(([k,x])=>s.params[k]===x)); if(!s) return null;
  const grp={}; d.graph.nodes.forEach(n=>grp[n.id]=n.group); let div=0, om=0;
  for(const [id,n] of Object.entries(s.res.nodes)){ if(grp[id]==='prep') continue; div+=n.div||0; for(const k of EXP) om+=(n.use||{})[k]||0; }
  return {div, om}; }
let IDS=process.argv.slice(2); if(!IDS.length) IDS=Object.keys(LV);
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
const out=[];
for(const id of IDS){ const lv=LV[id]; if(!lv) continue;
  const r=await Promise.race([p.evaluate(async([id,lv,EXP,OLD])=>{ const S=__rev; const x=S.recSamples.find(s=>s.id===id); if(!x) return {id,skip:'no sample'}; const it=await S.parse(x.text); if(it.err) return {id,skip:'parse'}; const an=S.analyse(it); if(an.putrid) return {id,skip:'putrid'};
    S.need=new Set(); S.soft=new Set(); S.tsel={}; S.buy=new Set(); S.noVariants=!!OLD;
    an.rows.forEach((r,i)=>{ if(r.unrev||r.m.fr) return; if(lv.tmax[r.m.gi]) S.tsel[i]=Math.max(r.tierNo, Math.min(lv.tmax[r.m.gi], r.tierCnt)); if(lv.must.includes(r.m.gi)) S.need.add(i); else if(lv.soft.includes(r.m.gi)) S.soft.add(i); if((lv.buy||[]).includes(r.m.gi) && r.how==='n') S.buy.add(i); });
    if(!S.need.size) an.rows.forEach((r,i)=>{ if(!r.unrev && !r.m.fr && !S.soft.has(i)) S.need.add(i); });
    let a2=S.needAn(an,0,it), d=null; const t0=performance.now();
    try{ const bs=new Set([...S.buy].filter(i=>S.need.has(i)).map(i=>an.rows[i]?.m).filter(Boolean)); const o={market:1e9, ...(bs.size?{buy:bs}:{})}; const bd = OLD ? S.bestDraft(it,a2,o) : await S.bestDraftAsync(it,a2,o,null,0); /* 화면과 같은 후보 계산(최소 대기 없이) */ d=bd.d; a2=bd.an; }catch(e){ return {id,err:['초안 실패: '+e.message]}; }
    if(!d) return {id,err:['초안 없음']};
    const c=S.verifyDraft(it,a2,d), err=c.filter(z=>z.lv==='err').map(z=>z.kr), warn=c.filter(z=>z.lv==='warn').map(z=>z.kr);
    const g=POE2GRAPH.fromDraft(d, it.D, {craft:S.craft, grades:['high']}); let t1=performance.now(), ck=POE2GRAPH.check(g, it.D, S.craft, S.prices, POE2SIM, 40, 2e6);   // 긴 반복(카오스 오브 수천 번)도 끝까지: 먼저 적게 돌리고, 빠르면 300번
    if(!ck.issues.length && performance.now()-t1 < 4000) ck=POE2GRAPH.check(g, it.D, S.craft, S.prices, POE2SIM, 300, 2e6);
    const res=ck.strategies[0]?.res, use=res?.use||{}; let om=0; for(const k of EXP) om+=use[k]||0;
    const top=Object.entries(use).map(([k,v])=>[k, v*(k==='Exalted_Orb'?1:(S.prices.p[k]||0))/S.prices.divine]).sort((a,b)=>b[1]-a[1]).slice(0,3).map(([k,v])=>k+' '+v.toFixed(1));
    const ra=ck.strategies[0]?.runaway, bn=ra && (d.nodes.find(n=>n.id===ra) || d.nodes.find(n=>ra.endsWith(n.id))), gs = t => !t ? [] : [t.gi, ...(t.anyOf||[]).map(x=>x.gi), t.reveal?.gi, ...((t.reveal?.anyOf)||[]).map(x=>x.gi)].filter(x=>x!=null).map(gi=>it.D.groups[gi].s+(it.D.groups[gi].sub?':'+it.D.groups[gi].sub:'')+' T'+((t.tmax)||'')+' '+(it.D.groups[gi].t[0][5]||'').slice(0,40));
    const bad = ra ? {at:ra, do:bn?.do, cur:bn?.cur, omens:bn?.omens, tg:gs(bn?.target), fail:bn?.fail&&JSON.stringify(bn.fail).slice(0,120), runes:(d.start.runes||[]).map(x=>x.en)} : null;
    return {id, bad, err, warn, issues:ck.issues.map(z=>z.kr), div:res?res.mean:null, reqOk:res?res.reqOk:null, om, top, pick:d.pick||null, knowhow:d.knowhow||null, steps:d.nodes.length, ms:Math.round(performance.now()-t0), d};
  },[id,lv,EXP,process.env.V==='old']), new Promise(z=>setTimeout(()=>z({id,err:['시간 초과']}),120000))]);
  out.push(r); }
// 가중치 모르는 단계 수는 레시피 엔진으로
await p.goto('http://localhost:8779/recipes.html?lang=kr&debug=1'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const unk=await p.evaluate(ds=>{ const R=__rec, o={}; for(const d of ds){ try{ d.likes=0; d.success=0; const a=R.analyse(d); o[d.id]=a.nodes.filter(n=>n.pUnknown).length; }catch(e){ o[d.id]=0; } } return o; }, out.filter(x=>x.d).map(x=>x.d));
await b.close();
const byId={}; R.forEach(r=>byId[r.id]=r);
const rows=out.map(x=>{ if(x.skip) return {id:x.id, skip:x.skip}; const o=orig(byId[x.id]), pts={}, why=[];
  pts.ver = x.err?.length ? 0 : 20; if(x.err?.length) why.push('검산 오류: '+x.err[0]);
  const stuck=(x.issues||[]).length>0 || x.div==null; pts.sim = (stuck?0:10) + (x.reqOk!=null && x.reqOk>=0.98 ? 10 : 0); if(stuck) why.push('시뮬 '+((x.issues||[])[0]||'없음')); else if(!(x.reqOk>=0.98)) why.push('필수 옵션 '+Math.round((x.reqOk||0)*100)+'%');
  const k = x.div!=null && o ? Math.max(x.div,1)/Math.max(o.div,1) : null;   // 1 div 아래는 같은 값으로 봄(베이스 값·시세 오차보다 작음)
  pts.cost = k==null ? 0 : k<=1.2 ? 30 : k<=1.5 ? 25 : k<=2 ? 20 : k<=3 ? 12 : k<=5 ? 5 : 0; if(k==null) why.push('비용 비교 불가'); else if(k>1.5) why.push(`비용 ${k.toFixed(1)}배 (${x.div.toFixed(1)} vs ${o.div.toFixed(1)} div)`);
  const dOm = x.div!=null && o ? x.om - o.om : null;
  pts.om = dOm==null ? 0 : dOm<=0.5 ? 10 : x.om<=o.om*2+1 ? 7 : x.om<=o.om*5+3 ? 4 : 0; if(dOm>0.5) why.push(`비싼 징조 ${x.om.toFixed(1)}개 (등록 ${o.om.toFixed(1)})`);
  const u = x.d ? unk[x.d.id]||0 : 0; pts.w = Math.max(0, 10-5*u); if(u) why.push(`가중치 모름 ${u}단계`);
  const wn=(x.warn||[]).length; pts.pol = Math.max(0, 10-3*wn); if(wn) why.push(`검산 경고 ${wn}`);
  const score=Object.values(pts).reduce((s,v)=>s+v,0);
  return {id:x.id, bad:x.bad, score, pts, k:k==null?null:+k.toFixed(2), div:x.div, orig:o?.div??null, om:x.om, top:x.top, pick:x.pick, knowhow:x.knowhow, why, ms:x.ms}; });
if(!process.env.NOSAVE) fs.writeFileSync(__dirname+'/revscore'+(process.env.V==='old'?'-old':'')+'.json', JSON.stringify(rows));   // NOSAVE=1: 일부만 돌려 보는 빠른 점검(tools/release.sh)
const ok=rows.filter(r=>r.score!=null), ks=ok.map(r=>r.k).filter(v=>v!=null).sort((a,b)=>a-b);
console.log(`초안 ${ok.length}개 · 평균 ${(ok.reduce((s,r)=>s+r.score,0)/ok.length).toFixed(1)}점 · 70점 미만 ${ok.filter(r=>r.score<70).length}개 · 비용 배수 중앙값 ${ks[Math.floor(ks.length/2)]} · 1.5배 안 ${ks.filter(k=>k<=1.5).length} · 5배 넘음 ${ks.filter(k=>k>5).length} · 검산 오류 ${ok.filter(r=>!r.pts.ver).length} · 시뮬 문제 ${ok.filter(r=>r.pts.sim<20).length}`);
})();
