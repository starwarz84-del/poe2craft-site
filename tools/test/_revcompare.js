// 등록 레시피 vs 리버스 초안 비교(사용자 요청 2026-11-11: 난이도마다 2개씩 골라 같은 아이템을 리버스로 만들어 서로 비교)
// node _revcompare.js <레시피 id…>   (테스트 서버 필요) → revcompare.json, 그 뒤 python3 tools/test/revcompare_md.py → docs/reverse-compare.md
// 기준 = 등록 플로우차트의 완성 조건(require) 그대로. 레시피 단계가 노리는 옵션 중 등록 시뮬이 항상 만드는 줄을 리버스의 '필수'로 넣고 나머지는 잡옵.
// 두 쪽 모두 시뮬로, 같은 등급끼리 ① 완성 1개당 비용(useDiv = 베이스 값만 뺀 모든 커런시, 준비 구역 포함 + 매직 베이스 굴림 — W2 2026-11-13) ② 완성 조건을 만족한 비율(등록 쪽은 100%여야 함) ③ 비싼 징조 수를 잼.
const {chromium}=require('playwright'); const fs=require('fs'); const {registered, nm, divOf, topUse, EXP, TK, DIFF, ROOT}=require('./_regcard.js');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const stepTxt=(n,G)=>{ const t=n.target||{}, gs=[t.gi, ...(t.anyOf||[]).map(x=>x.gi), t.reveal?.gi, ...((t.reveal?.anyOf)||[]).map(x=>x.gi), t.mark?.gi].filter(x=>x!=null);
  const what = gs.length ? gs.slice(0,3).map(gi=>(G[gi]?.t[0][4]||'').split('\n')[0]).join(' / ')+(gs.length>3?' 등':'') : t.junk ? '잡옵' : t.unrev ? '훼손(미공개)' : t.rune ? t.rune.kr : t.quality ? `퀄리티 ${t.quality}%` : t.removeDes ? '훼손 옵션 제거' : t.removeJunk ? '잡옵 제거' : '';
  const cur=[...(n.omens||[]), n.cur].filter(Boolean).map(nm).join(' + '), f=n.fail||n.compromise?.fail;
  const fail = n.compromise ? ' · 빗나가면 그대로' : n.fallbackFor ? ' (앞 단계 실패 시)' : f?.via ? ` · 실패: ${[...(f.via.omens||[]), f.via.cur].map(nm).join(' + ')}` : f ? ' · 실패: 다시' : '';
  return `${cur || ({base:'베이스', manual:'룬 장착', note:'안내'})[n.do] || n.do}${what?' → '+what:''}${n.optional?' (선택)':''}${fail}`; };
let IDS=process.argv.slice(2);
(async()=>{ const out=[]; const b=await chromium.launch(); const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:'+(process.env.PORT||8779)+'/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
for(const id of IDS){ const r=R.find(x=>x.id===id); if(!r){ console.error('없는 레시피', id); continue; } let reg; try{ reg=registered(r, 1500); }catch(e){ console.error(id, '등록 그래프 오류', e.message); continue; }
  const D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${r.cls}.json`));
  const buy=((r.start||{}).mods||[]).filter(m=>m.gi!=null && !m.crafted).map(m=>m.gi);
  const tier=r.tier||'high'; const dr=await p.evaluate(async([id,card,qt,buy,EXP,per,rtags,rreq,tier])=>{ const S=__rev; const x=S.recSamples.find(s=>s.id===id); if(!x) return {err:'샘플 없음'}; const it=await S.parse(x.text); if(it.err) return {err:'분석 실패'}; const an=S.analyse(it); if(an.putrid) return {err:'훼손 옵션 2개'};
    S.need=new Set(); S.soft=new Set(); S.tsel={}; S.buy=new Set(); const miss=[];
    const took=new Set(); card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const i=an.rows.findIndex((r,k)=>!r.unrev && !took.has(k) && l.opts.some(o=>o.gi===r.m.gi)); if(i<0){ miss.push(ci); return; } const r=an.rows[i], o=l.opts.find(o=>o.gi===r.m.gi); took.add(i); if(r.m.fr) return;
      S.need.add(i); if(o.tmax) S.tsel[i]=Math.max(r.tierNo, Math.min(o.tmax, r.tierCnt)); if(buy.includes(r.m.gi) && r.how==='n') S.buy.add(i); });
    const a0=S.needAn(an,0,it), bs=new Set([...S.buy].map(i=>an.rows[i]?.m).filter(Boolean)); const t0=performance.now();
    let bd; try{ bd=await S.bestDraftAsync(it,a0,{market:1e9, ...(bs.size?{buy:bs}:{})},null,4000); }catch(e){ return {err:'초안 실패: '+e.message}; } const d=bd.d; if(!d) return {err:'초안 없음'};
    const c=S.verifyDraft(it,bd.an,d); const g=POE2GRAPH.fromDraft(d, it.D, {craft:S.craft, grades:['high','bal','ess']}); g.strategies=[g.strategies.find(s=>s.id===tier) || g.strategies[0]];   /* 같은 등급끼리(W2) */
    Object.assign(g.tags, qt, rtags); g.require=rreq || {all:card.map((l,i)=>({has:'q'+i}))};
    let ck=POE2GRAPH.check(g, it.D, S.craft, S.prices, POE2SIM, 40, 2e6), t1=performance.now(); if(ck.strategies[0]?.res && performance.now()-t0<60000) ck=POE2GRAPH.check(g, it.D, S.craft, S.prices, POE2SIM, 400, 2e6);
    const res=ck.strategies[0]?.res; let dbg=null; if(res && res.reqOk<0.98 && rreq?.all){ try{ const st=ck.strategies[0], run=POE2SIM.make(g,it.D,S.craft,st.params||{}), rn=POE2SIM.rng(5), c=rreq.all.map(()=>0); let n=0; for(let i=0;i<30;i++) run(rn,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done:(x,cond)=>{ n++; rreq.all.forEach((q,k)=>{ if(cond(q)) c[k]++; }); }}}); dbg=rreq.all.map((q,k)=>JSON.stringify(q)+' '+c[k]+'/'+n); }catch(e){ dbg=[e.message]; } }
    return {dbg, miss, nodes:d.nodes, start:d.start, verr:c.filter(z=>z.lv==='err').map(z=>z.kr), vwarn:c.filter(z=>z.lv==='warn').map(z=>z.kr), run:ck.strategies[0]?.runaway||ck.strategies[0]?.error||null,
      div:res?S.revCost(it,d,res):null, mag:res?S.magicDiv(it,d):0, p50:res?res.useMedian:null, p90:res?res.useP90:null, match:res?res.reqOk:null, use:res?res.use:null, pick:d.pick||null, knowhow:d.knowhow||null, tried:d.tried||null, diff:d.difficulty};
  },[id,reg.card,reg.qt,buy,EXP,reg.per,reg.rtags,reg.rreq,tier]);
  const o={id, title:r.title?.kr, cls:r.cls, tier:TK[r.tier||'high'], diff:DIFF[r.difficulty]||r.difficulty, src:r.source?.channel||r.author?.kr||'', reg:{div:reg.div, mag:reg.mag, bases:reg.bases, match:reg.match, om:reg.om, top:reg.top, card:reg.cardTxt, per:reg.per, rnd:reg.rnd, steps:r.nodes.map(n=>stepTxt(n,D.groups)), start:(r.start?.mods||[]).length}, buy:buy.length};
  if(dr.err) o.draft={err:dr.err}; else o.draft={div:dr.div, mag:dr.mag, p90:dr.p90, match:dr.match, om:dr.use?EXP.reduce((s,k)=>s+(dr.use[k]||0),0):null, top:dr.use?topUse(dr.use):[], steps:dr.nodes.map(n=>stepTxt(n,D.groups)), verr:dr.verr, vwarn:dr.vwarn, run:dr.run, pick:dr.pick, knowhow:dr.knowhow, tried:dr.tried, miss:dr.miss.map(i=>reg.cardTxt[i]), diff:DIFF[dr.diff]};
  if(dr.dbg) console.log('   조건별', dr.dbg.join(' | ')); out.push(o); const f=v=>v==null?'-':v>=10?Math.round(v):v.toFixed(1), pc=v=>v==null?'-':Math.round(v*100)+'%';
  console.log(`${id} [${o.diff}] 등록 ${f(reg.div)} div · 일치 ${pc(reg.match)} · 징조 ${f(reg.om)} | 리버스 ${dr.err||f(dr.div)+' div · 일치 '+pc(dr.match)+' · 징조 '+f(o.draft.om)+(dr.run?' · 시뮬 '+dr.run:'')+(dr.verr?.length?' · 검산 오류 '+dr.verr.length:'')}`); }
await b.close(); fs.writeFileSync(__dirname+'/revcompare.json', JSON.stringify(out,null,1)); })();
