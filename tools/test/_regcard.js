// 등록 레시피의 완성품 카드(그래프 finals, 그 등급)와 시뮬 값: 리버스 비교(_revcompare.js)·리버스 점수(_revscore.js) 공용
const fs=require('fs'); const ROOT='/home/claude/poe2data'; const SIM=require(ROOT+'/site/sim.js');
const craft=JSON.parse(fs.readFileSync(ROOT+'/site/data/crafting.json')), prices=JSON.parse(fs.readFileSync(ROOT+'/site/data/prices.json'));
const EXP=['Omen_of_Whittling','Omen_of_Sinistral_Erasure','Omen_of_Dextral_Erasure','Omen_of_Sinistral_Annulment','Omen_of_Dextral_Annulment','Omen_of_Light','Hinekoras_Lock'];
const nm=id=>{ for(const k in craft) for(const x of craft[k]) if(x.id===id) return x.kr; return id; };
const KT={'하이엔드':'high','밸런스':'bal','에센셜':'ess'}, TK={high:'하이엔드', bal:'밸런스', ess:'에센셜'}, DIFF=['입문','쉬움','보통','어려움','전문가','극한'];
const divOf=use=>{ let v=0; for(const k in use) v+=use[k]*(k==='Exalted_Orb'?1:(prices.p[k]||0)); return v/prices.divine; };
const topUse=use=>Object.entries(use).map(([k,v])=>[k,v,v*(k==='Exalted_Orb'?1:(prices.p[k]||0))/prices.divine]).sort((a,b)=>b[2]-a[2]).slice(0,4).map(([k,v,d])=>`${nm(k)} ${v>=10?Math.round(v):v.toFixed(1)}개(${d>=10?Math.round(d):d.toFixed(1)} div)`);
function registered(r, N=1500){ const gid=r.simId||r.tierGroup||r.id, g=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${gid}.json`)), D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${g.cls}.json`)), G=D.groups;
  const v=(g.versions||[]).find(v=>(v.tier||KT[v.kr])===(r.tier||'high')); const st=g.strategies.find(s=>Object.entries(v.params).every(([k,x])=>s.params[k]===x)); const fin=(g.finals||[]).find(f=>f.id===v.id);
  const P=x=>typeof x==='string'&&x[0]==='$'?+st.params[x.slice(1)]:x;
  const leaf=(name,tm)=>{ const t=g.tags[name]; if(!t) return []; if(t.anyOf) return t.anyOf.flatMap(x=>typeof x==='string'?leaf(x,tm):[{gi:x.gi,tmax:tm??P(x.tmax)}]);
    const gi=t.gi!=null?t.gi:G.findIndex(x=>x.f.join('+')===t.fam && (!t.sec||x.s===t.sec) && (!t.side||x.g===t.side)); return gi<0?[]:[{gi, tmax:tm??P(t.tmax)??null}]; };
  const card=fin.lines.filter(l=>l.tag).map(l=>({fr:!!l.fr, des:!!l.des, opts:leaf(l.tag, l.tmax??undefined)})).filter(l=>l.opts.length);
  const rnd=fin.lines.filter(l=>!l.tag).length;
  const qt={}; card.forEach((l,i)=>{ qt['q'+i]={anyOf:l.opts.map(o=>({gi:o.gi, ...(o.tmax?{tmax:o.tmax}:{})}))}; });
  const g2={...g, tags:{...g.tags, ...qt}, require:{all:card.map((_,i)=>({has:'q'+i}))}};
  const res=SIM.simulate(g2, D, craft, prices, st.params, N, 7); const grp={}; g.nodes.forEach(n=>grp[n.id]=n.group);
  let use={}; for(const [id,n] of Object.entries(res.nodes)){ if(grp[id]==='prep') continue; for(const k in n.use) use[k]=(use[k]||0)+n.use[k]; }
  // 카드 옵션별로 완성품이 그 옵션을 갖는 비율(등록 레시피가 '대표 옵션' 하나만 카드에 적고 실제로는 여러 옵션 중 하나를 받는 자리를 찾음)
  const per=card.map(()=>0); let nDone=0; { const run=SIM.make(g2,D,craft,st.params), rnd=SIM.rng(5); for(let i=0;i<500;i++) run(rnd,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done:(it,cond)=>{ nDone++; card.forEach((_,k)=>{ if(cond({has:'q'+k})) per[k]++; }); }}}); }
  const txt=l=>l.opts.map(o=>(G[o.gi].t[0][4]||'').split('\n')[0]+(o.tmax?` T1${o.tmax>1?'~'+o.tmax:''}`:'')).join(' 또는 ');
  return {gid, card, cardTxt:card.map(l=>(l.fr?'[분열] ':l.des?'[훼손] ':'')+txt(l)), rnd, per:per.map(x=>x/Math.max(1,nDone)), div:divOf(use), all:res.mean, match:res.reqOk, om:EXP.reduce((s,k)=>s+(use[k]||0),0), top:topUse(use), qt};
}
module.exports={registered, nm, divOf, topUse, EXP, KT, TK, DIFF, craft, prices, ROOT};
