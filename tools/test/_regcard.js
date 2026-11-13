// 등록 레시피의 목표 옵션(단계 target)·완성 조건(플로우차트 require)과 시뮬 값: 리버스 비교(_revcompare.js)·리버스 점수(_revscore.js) 공용
const fs=require('fs'); const ROOT='/home/claude/poe2data'; const SIM=require(ROOT+'/site/sim.js');
const craft=JSON.parse(fs.readFileSync(ROOT+'/site/data/crafting.json')), prices=JSON.parse(fs.readFileSync(ROOT+'/site/data/prices.json'));
const EXP=['Omen_of_Whittling','Omen_of_Sinistral_Erasure','Omen_of_Dextral_Erasure','Omen_of_Sinistral_Annulment','Omen_of_Dextral_Annulment','Omen_of_Light','Hinekoras_Lock'];
const nm=id=>{ for(const k in craft) for(const x of craft[k]) if(x.id===id) return x.kr; return id; };
const KT={'하이엔드':'high','밸런스':'bal','에센셜':'ess'}, TK={high:'하이엔드', bal:'밸런스', ess:'에센셜'}, DIFF=['입문','쉬움','보통','어려움','전문가','극한'];
const divOf=use=>{ let v=0; for(const k in use) v+=use[k]*(k==='Exalted_Orb'?1:(prices.p[k]||0)); return v/prices.divine; };
const topUse=use=>Object.entries(use).map(([k,v])=>[k,v,v*(k==='Exalted_Orb'?1:(prices.p[k]||0))/prices.divine]).sort((a,b)=>b[2]-a[2]).slice(0,4).map(([k,v,d])=>`${nm(k)} ${v>=10?Math.round(v):v.toFixed(1)}개(${d>=10?Math.round(d):d.toFixed(1)} div)`);
/* 비용 기준(W2, 13장 사용자 확정 11-13 20:16·20:28) = 시뮬 useDiv(베이스 구입비만 뺀 모든 커런시, 준비 구역의 분열 과정 포함) + 매직 베이스를 사서 시작하면 그 매직 옵션 굴림 비용.
   리버스 화면(reverse.html magicDiv·revCost)과 같은 계산: 진화 → 확장, 빗나가면 소멸의 오브로 지우고 같은 베이스에 다시, 오브 등급은 시뮬로 가장 싼 것 */
const GRAPH=require(ROOT+'/site/graphify.js');
/* W5(11-13 21:45): 리버스와 같은 graphify.js magicCost — 먼저 붙는 목표를 첫 옵션으로, 단일 원소 저항은 다른 원소도 성공 + 유동체 */
function magicDiv(D, r, ms){ if(!ms.length) return 0; const tg = m => m.anyOf ? {anyOf:m.anyOf} : {gi:m.gi, ...(m.tmax?{tmax:m.tmax}:{})};
  const v=GRAPH.magicCost(D, craft, prices, SIM, {cls:r.cls, base:r.base, ilvl:r.ilvl}, ms.map(tg)); return v ? v.div : 0; }
function goals(r){ const gid=r.simId||r.tierGroup||r.id, g=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${gid}.json`)), D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${g.cls}.json`)), G=D.groups;
  const dropped=new Set(r.nodes.flatMap(n=>[n.target?.removeGi, n.target?.dropGi]).filter(x=>x!=null));
  const card=[], seen=new Set(), put=(opts, fl)=>{ opts=opts.filter(o=>o && o.gi!=null && !dropped.has(o.gi) && !(G[o.gi].f||[]).includes('ItemMaxQuality')); if(!opts.length) return; const k=opts.map(o=>o.gi).sort().join(','); if(seen.has(k)) return; if(opts.length===1 && [...seen].some(x=>x.split(',').includes(String(opts[0].gi)))) return; seen.add(k); card.push({...fl, opts:opts.map(o=>({gi:o.gi, tmax:o.tmax||null}))}); };
  ((r.start||{}).mods||[]).forEach(m=>{ if(m.gi!=null) put([m], {fr:!!m.fr, des:false}); });
  r.nodes.forEach(n=>{ const t=n.target||{}; if(n.optional || n.onLost || t.asIs || t.anyReveal || t.rand || t.junk || t.mark) return;
    if(['transmute','augment','regal','exalt','chaos','essence'].includes(n.do)) put(t.anyOf || (t.gi!=null ? [t] : []), {fr:false, des:false});
    else if(n.do==='reveal' && t.reveal) put(t.reveal.anyOf || [t.reveal], {fr:false, des:true}); });
  return card; }
function registered(r, N=1500, card){ const gid=r.simId||r.tierGroup||r.id, g=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${gid}.json`)), D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${g.cls}.json`)), G=D.groups;
  const v=(g.versions||[]).find(v=>(v.tier||KT[v.kr])===(r.tier||'high')); const st=g.strategies.find(s=>Object.entries(v.params).every(([k,x])=>s.params[k]===x)); const fin=(g.finals||[]).find(f=>f.id===v.id);
  const P=x=>typeof x==='string'&&x[0]==='$'?+st.params[x.slice(1)]:x;
  const leaf=(name,tm)=>{ const t=g.tags[name]; if(!t) return []; if(t.anyOf) return t.anyOf.flatMap(x=>typeof x==='string'?leaf(x,tm):[{gi:x.gi,tmax:tm??P(x.tmax)}]);
    const gi=t.gi!=null?t.gi:G.findIndex(x=>x.f.join('+')===t.fam && (!t.sec||x.s===t.sec) && (!t.side||x.g===t.side)); return gi<0?[]:[{gi, tmax:tm??P(t.tmax)??null}]; };
  // 기준(2026-11-11 고침, 사용자 지적: 등록 레시피는 따라가면 100% 같은 결과가 나옴) = 등록 플로우차트의 완성 조건 그대로.
  // card = 레시피 단계가 노리는 옵션과 티어 범위 중 완성품에 남는 줄. per = 완성품이 그 줄을 갖는 비율(98% 아래면 레시피가 '빗나가도 받는' 자리 → 리버스 필수에서 뺌).
  // 처음엔 완성품 카드의 대표 옵션 한 줄(가장 좋은 티어)로 비교해서 'A 또는 B'·'1~2티어' 자리를 틀린 것으로 셌음 — 잘못된 측정이었음.
  let fromReq=false;
  if(!card){ /* 목표 줄 = 완성 조건(require)이 요구하는 옵션. has → 1줄, count → n줄, any → 등록 시뮬에서 가장 자주 맞는 갈래 */
    const rate=new Map(), anys=[]; (function walk(c){ if(!c||typeof c!=='object') return; if(c.ref) return walk((g.conds||{})[c.ref]); if(c.all) c.all.forEach(walk); if(c.any){ anys.push(c); c.any.forEach(walk); } })(g.require);
    if(anys.length){ const run=SIM.make(g,D,craft,st.params), rn=SIM.rng(3); anys.forEach(a=>a.any.forEach(x=>rate.set(x,0))); for(let i=0;i<200;i++) run(rn,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done:(it,cond)=>{ for(const x of rate.keys()) if(cond(x)) rate.set(x,rate.get(x)+1); }}}); }
    const frs=new Set(((r.start||{}).mods||[]).filter(m=>m.fr&&m.gi!=null).map(m=>m.gi)), PT=x=>typeof x==='string'&&x[0]==='$'?st.params[x.slice(1)]:x;
    const line=tag=>{ const opts=leaf(PT(tag)); return opts.length ? [{fr:opts.length===1&&frs.has(opts[0].gi), des:opts.every(o=>G[o.gi].s==='d'), opts}] : []; };
    const lines=c=>{ if(!c||typeof c!=='object') return []; if(c.ref) return lines((g.conds||{})[c.ref]); if(c.all) return c.all.flatMap(lines); if(c.any) return lines([...c.any].sort((x,y)=>rate.get(y)-rate.get(x))[0]);
      if(c.has) return line(c.has); if(c.count) return Array.from({length:c.count.min},()=>line(c.count.tag)[0]).filter(Boolean); return []; };
    card=lines(g.require); fromReq=card.length>0; if(!card.length) card=goals(r); }
  const rnd=fin ? fin.lines.filter(l=>!l.tag).length : 0;
  const qt={}; card.forEach((l,i)=>{ qt['q'+i]={anyOf:l.opts.map(o=>({gi:o.gi, ...(o.tmax?{tmax:o.tmax}:{})}))}; });
  /* 완성 조건은 등록 플로우차트의 것 그대로(레시피가 스스로 정한 완성). q 태그는 옵션별 비율을 재는 데만 씀 */
  const g2={...g, tags:{...g.tags, ...qt}};
  /* 같은 완성 조건을 리버스 초안 그래프에 옮겨 쓸 수 있게 태그 이름에 R_를 붙이고 $매개변수를 값으로 바꿈 */
  const PS=x=>typeof x==='string'&&x[0]==='$'?st.params[x.slice(1)]:x, rtags={};
  for(const [k,t] of Object.entries(g.tags)){ const o={...t}; if(o.tmax!=null) o.tmax=P(o.tmax); if(o.anyOf) o.anyOf=o.anyOf.map(x=>typeof x==='string'?'R_'+x:{...x, ...(x.tmax!=null?{tmax:P(x.tmax)}:{})}); rtags['R_'+k]=o; }
  const ren=c=>{ if(!c || typeof c!=='object') return c; if(c.full || c.sideLt) return {all:[]}; /* 빈 자리를 랜덤 옵션으로 채우는 마무리는 초안 그래프에 없어 비교에서 뺌 */ if(c.ref) return ren((g.conds||{})[c.ref]); const o={};
    for(const [k,v] of Object.entries(c)){ if(k==='all'||k==='any') o[k]=v.map(ren); else if(k==='not') o[k]=ren(v); else if(k==='has'||k==='allMods') o[k]='R_'+PS(v); else if(k==='count'||k==='sideAll') o[k]={...v, tag:'R_'+PS(v.tag)}; else o[k]=v; } return o; };
  const rreq=ren(g.require);
  const res=SIM.simulate(g2, D, craft, prices, st.params, N, 7);
  /* 예전(~11-13): 준비 구역(prep) 상자를 뺀 사용량 → 초안(베이스 포함 평균)과 기준이 달랐음. 이제 양쪽 모두 useDiv(준비 포함, 베이스 제외) + 매직 굴림 */
  const use=res.use, h=g.nodes.find(n=>n.id===g.start), s0=h?.start||{};
  const mags = s0.rar==='magic' ? (s0.mods||[]).map(m=>typeof m==='string' ? m : m?.tag).filter(Boolean).map(t=>leaf(t)).filter(l=>l.length).map(l=>l.length>1 ? {anyOf:l.map(o=>({gi:o.gi, ...(o.tmax?{tmax:o.tmax}:{})}))} : l[0]) : [];
  const mag = magicDiv(D, r, mags);
  // 카드 옵션별로 완성품이 그 옵션을 갖는 비율(등록 레시피가 '대표 옵션' 하나만 카드에 적고 실제로는 여러 옵션 중 하나를 받는 자리를 찾음)
  const per=card.map(()=>0); let nDone=0; { const run=SIM.make(g2,D,craft,st.params), rnd=SIM.rng(5); for(let i=0;i<500;i++) run(rnd,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done:(it,cond)=>{ nDone++; card.forEach((_,k)=>{ if(cond({has:'q'+k})) per[k]++; }); }}}); }
  const txt=l=>l.opts.map(o=>(G[o.gi].t[0][4]||'').split('\n')[0]+(o.tmax?` T1${o.tmax>1?'~'+o.tmax:''}`:'')).join(' 또는 ');
  return {gid, card, cardTxt:card.map(l=>(l.fr?'[분열] ':l.des?'[훼손] ':'')+txt(l)), rnd, per:per.map(x=>x/Math.max(1,nDone)), div:res.useDiv, mag,   /* 매직 굴림은 비용에 넣지 않고 참고(13장 11-13 22:37) */ all:res.mean, bases:res.bases, match:res.reqOk, fromReq, rtags, rreq, om:EXP.reduce((s,k)=>s+(use[k]||0),0), top:topUse(use), qt};
}
module.exports={goals, registered, magicDiv, nm, divOf, topUse, EXP, KT, TK, DIFF, craft, prices, ROOT};
