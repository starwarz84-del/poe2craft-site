// 리버스 등급 규칙 점검(W5 2026-11-13, docs/reverse-pipeline.md 2-4 · 정책 10장 C17·C11·난이도 표 · 13장 11-13 20:22·20:28)
//   node _revgrades.js            A만: 등록 그래프 시뮬 파일 전부에 JS 난이도 표(graphify.js diffOf)를 돌려 _difftable.py와 같은 값인지(테스트 서버 필요 없음)
//   node _revgrades.js <레시피 id…>  A + B: 등록 완성품을 리버스로 돌려(테스트 서버 :8779) 등급 결과 점검
//     B 항목: ① 등급 수 = 난이도 표(C11) ② 반복 자리 티어 = 하이엔드 고른 티어 · 밸런스 max(고른, 1~2) · 에센셜 max(고른, 1~4)
//             ③ 마지막 옵션 도박(cmpl 갈림)은 하이엔드만 다시 · 필수 훼손 공개는 모든 등급 다시 ④ 남은 두 등급의 완성 카드가 같으면 안 됨(J)
//             ⑤ 완성 조건이 붙여 넣은 아이템의 같은 묶음 옵션 수만큼(count) ⑥ 에센셜 마무리 엑잘 = 상위 엑잘
const fs=require('fs'); const ROOT='/home/claude/poe2data', GRAPH=require(ROOT+'/site/graphify.js');
const budget=JSON.parse(fs.readFileSync(ROOT+'/site/data/budget.json')), prices=JSON.parse(fs.readFileSync(ROOT+'/site/data/prices.json'));
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const DIFFSET=JSON.parse(/DIFFSET\s*=\s*(\{[^}]*\})/.exec(fs.readFileSync(ROOT+'/scripts/difficulty.py','utf8'))[1].replace(/'/g,'"'));
const ORDER=['high','bal','ess'], MIRROR=prices.p.Mirror_of_Kalandra/prices.divine;
let bad=0; const A=[];
for(const f of fs.readdirSync(ROOT+'/site/data/sim').filter(f=>f.endsWith('.json')).sort()){ const d=JSON.parse(fs.readFileSync(ROOT+'/site/data/sim/'+f)), gid=d.id;
  const have=new Set(R.filter(r=>(r.tierGroup||r.id)===gid).map(r=>r.tier)), S=Object.fromEntries(d.strategies.map(s=>[s.id,s]));
  const pick=ORDER.find(t=>S[t] && (have.has(t) || !have.size)) || Object.keys(S)[0];
  const x=GRAPH.diffOf(S[pick].res, d.graph, {expensive:budget.expensive, mirror:MIRROR});
  if(DIFFSET[gid]==null) continue; if(x.d!==DIFFSET[gid]) A.push(`${gid} ${pick}: JS ${x.d} · 표 ${DIFFSET[gid]} (시도 ${x.steps.toFixed(0)} 징조 ${x.omens.toFixed(1)} 비용 ${x.cost.toFixed(1)} 베이스 ${x.bases.toFixed(2)})`); }
const n=Object.keys(DIFFSET).length;
console.log(`A 난이도 표 JS = DIFFSET: 그래프 ${n}개 중 다른 것 ${A.length}`); A.forEach(l=>console.log('  '+l));
/* _difftable.py가 DIFFSET과 다르다고 하는 그래프는 JS도 같은 값이면 됨(표를 다시 재지 않은 것) — 파이썬 값과 비교 */
let py=null; try{ py=require('child_process').execSync('python3 '+ROOT+'/tools/test/_difftable.py --set').toString(); }catch(_){ }
if(py){ const P=JSON.parse(py.trim().replace(/'/g,'"')), dif=A.filter(l=>{ const g=l.split(' ')[0], js=+/JS (\d)/.exec(l)[1]; return P[g]!==js; }); console.log(`  파이썬 _difftable.py 값과 다른 것 ${dif.length}`); dif.forEach(l=>console.log('  !! '+l)); bad+=dif.length; }
const IDS=process.argv.slice(2);
if(!IDS.length){ console.log('문제 '+bad); process.exit(bad?1:0); }

const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(), p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
  await p.goto('http://localhost:'+(process.env.PORT||8779)+'/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
  await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
  /* 필수 옵션 고르기는 _revscore.js와 같음: 등록 레시피 완성 카드에서 등록 시뮬이 늘(98% 이상) 만드는 줄 = 필수, 그 티어 범위 */
  const {registered}=require('./_regcard.js');
  for(const id of IDS){ const r=R.find(x=>x.id===id); let reg; try{ reg=registered(r, 200); }catch(e){ console.log(`B ${id}: 등록 그래프 ${e.message}`); continue; }
    const buy=((r.start||{}).mods||[]).filter(m=>m.gi!=null && !m.crafted).map(m=>m.gi);
    const x=await p.evaluate(async([id,card,per,buy])=>{ const S=__rev, sm=S.recSamples.find(s=>s.id===id); if(!sm) return {skip:'샘플 없음'};
      const it=await S.parse(sm.text); if(it.err) return {skip:'분석 실패'}; const an=S.analyse(it); S.need=new Set(); S.soft=new Set(); S.tsel={}; S.buy=new Set(); S.noTpl=true;   /* 등록 틀(W9)은 등록 그래프 그대로라 이 점검(생성 후보의 등급 규칙) 대상이 아님 */
      const took=new Set(); card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const i=an.rows.findIndex((r,k)=>!r.unrev && !took.has(k) && l.opts.some(o=>o.gi===r.m.gi)); if(i<0) return; const r=an.rows[i], o=l.opts.find(o=>o.gi===r.m.gi); took.add(i); if(r.m.fr) return;
        S.need.add(i); if(o.tmax) S.tsel[i]=Math.max(r.tierNo, Math.min(o.tmax, r.tierCnt)); if(buy.includes(r.m.gi) && r.how==='n') S.buy.add(i); });
      const bs=new Set([...S.buy].map(i=>an.rows[i]?.m).filter(Boolean));
      const a2=S.needAn(an,0,it); const bd=await S.bestDraftAsync(it,a2,bs.size?{buy:bs}:{},null,0), d=bd.d; if(!d) return {skip:'초안 없음'};
      const F=S.runFlow(it,d); if(F.err) return {err:F.err};
      const g=F.g, P=Object.fromEntries(g.strategies.map(s=>[s.id,s.params])), out=[], note=[];
      /* ② 티어: 반복 자리 파라미터 */
      for(const k of Object.keys(g.params||{}).filter(k=>/^t\d+$/.test(k))){ const h=+P.high?.[k], bl=+P.bal?.[k], es=+P.ess?.[k], gi=+k.slice(1), G=it.D.groups[gi], lo=Math.max(1, G.t.findIndex(t=>t[0]<=d.ilvl)+1), cnt=G.t.length;
        const wb=Math.min(cnt, Math.max(h, lo+1)), we=Math.min(cnt, Math.max(h, lo+3)); if(bl!==wb || es!==we) out.push(`티어 ${k}: 하이 ${h} 밸 ${bl}(기대 ${wb}) 에센 ${es}(기대 ${we})`); }
      /* ③ 갈림 파라미터 */
      if(P.high?.cmpl && P.high.cmpl!=='retry') out.push('하이엔드 마지막 옵션이 도박 안 함');
      for(const v of ['bal','ess']) if(P[v]?.cmpl && P[v].cmpl!=='settle') out.push(v+' 마지막 옵션 도박');
      const desRetry=g.nodes.filter(n=>n.act==='reveal' && n.edges.some(e=>e.if?.param?.cmp||e.if?.param?.cmpl) && n._req); if(desRetry.length) out.push('필수 훼손 공개에 타협 갈림: '+desRetry.map(n=>n.id));
      /* ① 등급 수 */
      const want=POE2GRAPH.gradesFor(F.diff?.d ?? d.difficulty), kept=(F.lead?[F.lead.tier, ...(F.group?.grades||[]).map(x=>x.tier)]:[]);
      if(kept.some(t=>!want.includes(t)) && F.res.some(x=>want.includes(x.id) && x.res && x.res.reqOk>=0.98)) out.push(`표에 없는 등급 ${kept.join('/')} (난이도 ${F.diff?.d} → ${want.join('/')})`);
      /* ④ 같은 카드 */
      const cards=[F.lead, ...(F.group?.grades||[])].filter(Boolean).map(r=>[r.tier, JSON.stringify((r.fc?.lines||[]).map(l=>[l.tag?r.fc.tags[l.tag]?.gi:null, l.tag?r.fc.tags[l.tag]?.tmax:null, !!l.random, l.side, !!l.fr, !!l.des]).sort())]);
      for(let i=0;i<cards.length;i++) for(let j=i+1;j<cards.length;j++) if(cards[i][1]===cards[j][1]) out.push(`완성 카드 같음 ${cards[i][0]} = ${cards[j][0]}`);
      /* ⑤ 같은 묶음 두 줄 */
      const req=JSON.stringify(g.require); for(const [k,t] of Object.entries(g.tags)){ if(!t.anyOf) continue; const leaves=new Set(t.anyOf.map(x=>g.tags[x]?.gi)); const nPaste=an.rows.filter(r=>!r.unrev && leaves.has(r.m.gi)).length, nLine=(g.finals[0]?.lines||[]).filter(l=>l.tag===k).length;
        if(nLine>1 && !new RegExp(`"tag":"${k}","min":${nLine}`).test(req)) out.push(`묶음 ${k} 완성 카드 ${nLine}줄인데 완성 조건이 ${nLine}개를 요구하지 않음`); }
      /* ⑥ 에센셜 마무리 */
      const essFill=g.nodes.filter(n=>n.act==='exalt' && n.fillEss); if(essFill.length && (P.ess?.fx!=='g' || essFill.some(n=>!(n.over||[]).some(o=>o.param?.fx==='g' && o.set?.cur==='Greater_Exalted_Orb')))) out.push('에센셜 마무리 엑잘이 상위 엑잘이 아님');
      const fillP=d.nodes.filter(n=>n.junkFill && n.target?.junk==='p' && n.cur!=='Greater_Exalted_Orb').length; if(fillP && P.ess && !essFill.length) out.push('접두 마무리 엑잘이 있는데 에센셜 상위 엑잘 표시 없음');
      /* ⑦ 완성품 옵션 수 = 완성 카드 줄 수(남은 등급마다 시뮬 200회, 쪽별) — W4 보고: 셉터 에센셜 3%가 카드보다 옵션 적게 끝남 */
      for(const R0 of [F.lead, ...(F.group?.grades||[])].filter(Boolean)){ const st=g.strategies.find(x=>x.id===R0.tier), fin=g.finals.find(f=>f.id===R0.tier); if(!st||!fin) continue;
        const want={p:0,s:0}; fin.lines.forEach(l=>{ const sd=l.side || (l.tag ? (g.tags[l.tag]?.gi!=null ? it.D.groups[g.tags[l.tag].gi].g : null) : null) || (l.tag && g.tags[l.tag]?.anyOf ? it.D.groups[g.tags[g.tags[l.tag].anyOf[0]]?.gi]?.g : null); if(want[sd]!=null) want[sd]++; });
        try{ const run=POE2SIM.make({...g, maxSteps:3e5}, it.D, S.craft, st.params), rn=POE2SIM.rng(3); let n=0, short=0;
          for(let i=0;i<200;i++) run(rn,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},c1(){},done:(x)=>{ n++; const c={p:0,s:0}; x.mods.forEach(m=>{ if(c[m.side]!=null) c[m.side]++; }); if(c.p<want.p || c.s<want.s) short++; }}});
          if(n && short/n>0.01) out.push(`${R0.tier}: 완성품 ${Math.round(short/n*100)}%가 카드(접두 ${want.p}·접미 ${want.s})보다 옵션이 적음`); }catch(e){ (/^runaway/.test(e.message) ? note : out).push(`${R0.tier}: 시뮬 200회 중 끝나지 않은 회차 (${e.message})`); } }
      const rows=F.res.map(r=>`${r.id} ${r.res?(r.cost??r.res.mean).toFixed(1)+' div '+Math.round(r.res.reqOk*100)+'%':'진행 불가'}${F.merged?.[r.id]?' →'+F.merged[r.id]:''}`);
      return {diff:F.diff, kept, rows, out, note, issues:F.issues.map(i=>i.kr)}; }, [id, reg.card, reg.per, buy]);
    if(x.skip||x.err){ console.log(`B ${id}: ${x.skip||x.err}`); if(x.err) bad++; continue; }
    console.log(`B ${id}: 난이도 ${x.diff?.d} (시도 ${Math.round(x.diff?.steps||0)} 징조 ${(x.diff?.omens||0).toFixed(1)} 비용 ${(x.diff?.cost||0).toFixed(1)}) → 등급 ${x.kept.join('/')} · ${x.rows.join(' · ')}`);
    x.issues.forEach(i=>console.log('   검사: '+i)); (x.note||[]).forEach(i=>console.log('   주의: '+i)); x.out.forEach(o=>console.log('   !! '+o)); bad+=x.out.length; }
  await b.close(); console.log('문제 '+bad); process.exit(bad?1:0); })();
