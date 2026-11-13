/* 리버스 분석 정확도 점검(W1, 2026-11-13): 등록 레시피 완성품(samples.json) 전부를 붙여 넣어
   고급 복사 + 머리줄을 뺀 일반 복사 두 번씩. ① 인식 못 한 줄 0 ② 고급 복사 머리줄 수 = 인식한 옵션 수(쪽별) ③ 분열·훼손·제작 표시가 그대로 읽힘
   ④ 같은 계열 두 줄(탱정 방패 화염 저항 최대치 일반 + 훼손) ⑤ 검산 오류 0 을 봄. 문제 0이어야 함.
   사용: node _revparse.js [레시피 id…]   (테스트 서버 :8779, PORT=로 바꿀 수 있음) */
const {chromium}=require('playwright');
const PORT = process.env.PORT || 8779, only = process.argv.slice(2);
(async()=>{ const b=await chromium.launch(); const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto(`http://localhost:${PORT}/discover.html?lang=kr`); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
const r = await p.evaluate(async(only)=>{ const S=__rev;
  [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready;
  const out=[]; let nOk=0;
  for(const x of S.recSamples){ if(only.length && !only.some(o=>x.id.startsWith(o))) continue;
   for(const simple of [false,true]){ const id=x.id+(simple?' (일반 복사)':''), txt=simple ? x.text.split('\n').filter(l=>!l.startsWith('{')).join('\n') : x.text;
    const prob=[]; let it, an;
    try{ it=await S.parse(txt); if(it.err){ out.push({id, prob:['분석 실패: '+it.err]}); continue; } an=S.analyse(it); }catch(e){ out.push({id, prob:['오류: '+e.message]}); continue; }
    /* 머리줄에서 기대값: 쪽·분열·훼손·제작(crafted 표시 줄) */
    const L=x.text.split('\n'), want=[]; for(let i=0;i<L.length;i++){ const h=L[i]; if(!/^\{ .*(Prefix|Suffix) Modifier/.test(h)) continue;
      const body=[]; for(let k=i+1;k<L.length && !L[k].startsWith('{') && !/^-{4,}$/.test(L[k]) && L[k].trim();k++) body.push(L[k]);
      want.push({side:/Prefix/.test(h)?'p':'s', fr:/Fractured/.test(h), des:/Desecrated/.test(h), crafted:body.some(l=>/\(crafted\)\s*$/.test(l)), unrev:body.some(l=>/unrevealed/i.test(l)), h}); }
    const unk=(it.other||[]).filter(o=>o.k==='?'); if(unk.length) prob.push(`인식 못 한 줄 ${unk.length}개: ${unk.map(o=>o.l).join(' | ')}`);
    const mods=it.mods;
    for(const sd of ['p','s']){ const w=want.filter(m=>m.side===sd).length, h=mods.filter(m=>m.side===sd).length; if(w!==h) prob.push(`${sd==='p'?'접두':'접미'} ${w}개인데 ${h}개 인식`); }
    for(const k of ['fr','des']){ const w=want.filter(m=>m[k]).length, h=mods.filter(m=>k==='fr'?m.fr:(m.desTag||m.unrev)).length; if(w!==h) prob.push(`${k==='fr'?'분열':'훼손'} 표시 ${w}개인데 ${h}개`); }
    { const w=want.filter(m=>m.crafted).length, h=mods.filter(m=>m.crafted).length; if(w!==h) prob.push(`제작 표시 ${w}개인데 ${h}개`); }
    /* 같은 옵션(gi) 두 줄 */
    const dup=mods.filter((m,i)=>m.gi!=null && mods.findIndex(y=>y.gi===m.gi)!==i).length;
    let ver=null; try{ const d=S.makeDraft(it,an); if(d){ const c=S.verifyDraft(it,an,d); ver=c.filter(z=>z.lv==='err').map(z=>z.kr); if(ver.length) prob.push('검산 오류: '+ver.join(' / ')); } }catch(e){ prob.push('초안 오류: '+e.message); }
    if(!prob.length) nOk++;
    out.push({id, n:mods.length, dup, prob}); } }
  return {out, nOk}; }, only);
const bad=r.out.filter(x=>x.prob.length);
for(const x of bad) console.log('# '+x.id+'\n  '+x.prob.join('\n  '));
const dups=r.out.filter(x=>x.dup).map(x=>x.id); if(dups.length) console.log('같은 옵션 두 줄 인식: '+dups.join(', '));
const tj=r.out.filter(x=>/^tankjung-kitava-shield/.test(x.id)); if(tj.length && tj.some(x=>!x.dup)) console.log('문제: 탱정 방패 화염 저항 최대치 두 줄 중 하나를 놓침');
const nProb = bad.length + (tj.some(x=>!x.dup)?1:0);
console.log(`레시피 완성품 ${r.out.length}개 · 통과 ${r.nOk} · 문제 ${nProb}`);
await b.close(); process.exit(nProb?1:0); })();
