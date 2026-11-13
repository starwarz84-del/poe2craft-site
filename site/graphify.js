// Reverse crafting: a draft recipe (site/reverse.html makeDraft, the step list of recipes.html) → a flowchart graph (docs/graph-model.md)
// that site/sim.js can walk. 사용자 확정 2026-11-11: 리버스도 플로우차트 먼저 → 시뮬로 막힘·완성 조건·비용 확인 → 그 플로우차트 기준 레시피.
// Conversion follows the table in docs/graph-model.md ("기존 레시피 형식 → 간선 자동 변환 규칙"); probabilities are not copied, the simulator rolls them.
// Grades (정책 30·32): the draft is the top grade (the tiers the user picked); each lower grade widens only the lines made by a loop
// (a reveal, an omen-driven chaos / exalt, a step that may be retried) by one tier step, and the lowest one keeps a compromise result instead of retrying.
(function(root){
'use strict';
const K = (kr,en) => ({kr,en});
const VN = {high:K('하이엔드','High-end'), bal:K('밸런스','Balance'), ess:K('에센셜','Essential')};
const SIDE_OM = /Sinistral|Dextral/;
const omSide = (oms, re) => { const o=(oms||[]).find(x=>re.test(x)); return !o ? null : /Sinistral/.test(o) ? 'p' : 's'; };
const EXP = ['Omen_of_Whittling','Omen_of_Sinistral_Erasure','Omen_of_Dextral_Erasure','Omen_of_Sinistral_Annulment','Omen_of_Dextral_Annulment','Omen_of_Light','Hinekoras_Lock'];

// grades a group keeps by difficulty (정책 30): 5 = high, 4 = high + bal, 2–3 = bal + ess, ≤1 = ess
function gradesFor(diff){ return diff>=5 ? ['high'] : diff>=4 ? ['high','bal'] : diff>=2 ? ['bal','ess'] : ['ess']; }

function fromDraft(d, D, opt={}){
  const G=D.groups, N=d.nodes, byId={}; N.forEach(n=>byId[n.id]=n);
  const base=D.bases[d.base]||{};
  // ---------- tags: one per modifier group (gi); lines made by a loop get a per-grade tier parameter
  const tags={}, tagOf = gi => { const k='g'+gi; if(!tags[k]) tags[k]={gi}; return k; };
  const tmaxOf={};   // gi → tier the draft aims at (best = smallest)
  const note = (gi, t) => { if(gi==null) return; tagOf(gi); if(t) tmaxOf[gi] = tmaxOf[gi] ? Math.min(tmaxOf[gi], t) : t; };
  const loopGi = new Set();
  const isLoop = n => n.do==='reveal' || n.compromise || n.fallbackFor || (n.fail && n.do!=='chaos' && n.do!=='essence') || (n.omens||[]).some(o=>EXP.includes(o)) || (n.do==='chaos' && n.fail && (n.omens||[]).length);
  (d.start.mods||[]).forEach(m=>{ if(m.gi!=null) note(m.gi, m.tmax); });
  N.forEach(n=>{ const t=n.target||{};
    if(t.gi!=null){ note(t.gi, t.tmax); if(isLoop(n) && n.do!=='essence') loopGi.add(t.gi); }
    (t.anyOf||[]).forEach(x=>{ note(x.gi, x.tmax); if(isLoop(n)) loopGi.add(x.gi); });
    if(t.reveal?.gi!=null){ note(t.reveal.gi, t.reveal.tmax); loopGi.add(t.reveal.gi); }
    (t.reveal?.anyOf||[]).forEach(x=>{ note(x.gi, x.tmax); loopGi.add(x.gi); });
    if(t.mark){ note(t.mark.gi); if(t.mark.alt!=null) note(t.mark.alt); }
    if(t.removeGi!=null) note(t.removeGi); if(t.dropGi!=null) note(t.dropGi); });
  // the start (bought / fractured) lines are cheap: never widened (정책 32)
  (d.start.mods||[]).forEach(m=>{ if(m.gi!=null) loopGi.delete(m.gi); });
  const grades = opt.grades || gradesFor(d.difficulty||2);
  /* 등급별 티어(정책 10장 C17-1, 리버스 13장 사용자 확정 11-13 20:28, W5): 반복으로 찾는 자리만 — 하이엔드 = 사용자가 고른 티어, 밸런스 = 그 티어와 1~2티어 중 넓은 쪽,
     에센셜 = 1~4티어 중 넓은 쪽. '1티어' = 아이템 레벨로 붙을 수 있는 가장 좋은 티어(lo). 예전엔 등급 순번만큼(+0/+1/+2) 넓힘 */
  const loTier = gi => Math.max(1, G[gi].t.findIndex(t=>t[0]<=d.ilvl)+1), WIDE = {high:0, bal:1, ess:3};
  const P = {}; grades.forEach(v=>{ const p={}; for(const gi of loopGi){ const t0=tmaxOf[gi]||1; p['t'+gi] = String(Math.min(G[gi].t.length, Math.max(t0, loTier(gi) + (WIDE[v]??0)))); } P[v]=p; });
  for(const gi in tmaxOf){ const k='g'+gi; tags[k].tmax = loopGi.has(+gi) ? '$t'+gi : tmaxOf[gi]; }
  for(const gi of Object.keys(tags).map(k=>+k.slice(1))) if(tags['g'+gi].tmax==null && tmaxOf[gi]==null) delete tags['g'+gi].tmax;
  let anyN=0; const anyMemo={}; const anyTag = list => { const ks=[...new Set(list.map(x=>tagOf(x.gi)))]; if(ks.length===1) return ks[0]; const key=ks.slice().sort().join('|'); if(anyMemo[key]) return anyMemo[key]; const k='a'+(++anyN); tags[k]={anyOf:ks}; return anyMemo[key]=k; };
  const targetTag = t => !t ? null : t.anyOf ? anyTag(t.anyOf) : t.gi!=null ? tagOf(t.gi) : t.reveal ? (t.reveal.anyOf ? anyTag(t.reveal.anyOf) : tagOf(t.reveal.gi)) : t.mark ? tagOf(t.mark.gi) : null;
  // 여러 옵션을 차례로 노리는 묶음(2026-11-11 고침): '원하는 옵션 중 하나'(anyOf) 단계 뒤에 그 나머지를 노리는 단계들이 이어지면 한 묶음.
  // 예전엔 첫 단계에서 둘째 옵션이 먼저 붙으면 다음 단계가 '이미 있음'으로 건너뛰어 첫째 옵션 없이 완성으로 셌음 → 묶음 단계는 '묶음 옵션이 k개 이상이면 건너뜀', 완성 조건은 '묶음 옵션 n개'
  const chainOf={}, chainN={}; { const ROLL=['exalt','chaos','regal','transmute','augment'], setOf = n => { const t=n.target||{}; return t.junk ? [] : t.anyOf ? t.anyOf.map(x=>x.gi) : t.gi!=null ? [t.gi] : []; };
    const cand = N.filter(n=>ROLL.includes(n.do) && !n.fallbackFor && !n.onLost && !n.optional && setOf(n).length);
    cand.forEach((S,i)=>{ if(chainOf[S.id] || !S.target.anyOf || S.target.anyOf.length<2) return; const L=new Set(setOf(S)), root=anyTag(S.target.anyOf); let k=1;
      /* 같은 갈래(공개 성공 / 빗나감)끼리만 묶음(W5) — 예전엔 같은 갈래 주인이면 성공·빗나감 갈래 단계도 한 묶음이라 둘째 단계가 '이미 1개'로 건너뛰었음(MazBro 시전자 목걸이 하이엔드 0%) */
      const lnOf = x => x.branch ? x.branch.of+':'+x.branch.when : 'main';
      for(const T of cand.slice(i+1)){ if(chainOf[T.id] || lnOf(T)!==lnOf(S)) continue; const st=setOf(T); if((st.length<L.size || (S.pool && T.pool && st.length===L.size)) && st.every(g=>L.has(g))){ if(k===1) chainOf[S.id]={tag:root, idx:0}; chainOf[T.id]={tag:root, idx:k++}; } }
      if(k>1) chainN[root]=Math.min(k, L.size); });
    /* 묶음(K39): 묶음을 노리는 단계(굴림 + 훼손 공개) 수만큼 세어 완성 조건·완성품 칸에 씀 */
    const pc={}; N.forEach(n=>{ if(!n.pool || n.fallbackFor || n.onLost || n.optional || n.branch) return; const L=n.do==='reveal' ? n.target?.reveal?.anyOf : ROLL.includes(n.do) ? n.target?.anyOf : null; if(!L) return; const tg=anyTag(L); pc[tg]={k:(pc[tg]?.k||0)+1, n:L.length}; });
    for(const tg in pc) if(pc[tg].k>1) chainN[tg]=Math.min(pc[tg].k, pc[tg].n); }
  const tgOf = n => chainOf[n.id]?.tag || targetTag(n.target);

  // ---------- roles: fallbacks, branch blocks, the main lane
  const fb={}; N.forEach(n=>{ if(n.fallbackFor){ (fb[n.fallbackFor]=fb[n.fallbackFor]||[]).push(n); } });
  const skipNode = n => n.do==='manual' && n.target?.runeSwap;   // 정책 23: a rune of taste is left out
  const lane = n => n.branch ? n.branch.of+':'+n.branch.when : 'main';
  const isMainish = n => !n.fallbackFor && !n.onLost && !skipNode(n);
  const order = N.filter(isMainish);
  const lastOfBranch = of => { let k=-1; N.forEach((n,i)=>{ if(n.branch?.of===of) k=i; }); return k; };
  function nextMain(n){ const i=N.indexOf(n), L=lane(n);
    for(let j=i+1;j<N.length;j++){ const m=N[j]; if(!isMainish(m)) continue; if(lane(m)===L) return m.id; if(L==='main' && !m.branch) return m.id; if(L!=='main' && !m.branch) return m.id; }
    if(L!=='main'){ const of=n.branch.of, k=lastOfBranch(of); for(let j=k+1;j<N.length;j++){ const m=N[j]; if(isMainish(m) && !m.branch) return m.id; } }
    return 'ok'; }
  const branchFirst = (of, when) => { const m=N.find(x=>x.branch?.of===of && x.branch.when===when && isMainish(x)); return m?.id; };
  // tags made by the steps before a node (its lane and the main lane before it) — a removed one sends the craft back to the step that made it
  const startKeep = (d.start.mods||[]).filter(m=>m.gi!=null && !m.fr).map(m=>tagOf(m.gi));
  const dropped=new Set(); N.forEach(n=>{ const t=n.target||{}; if(t.removeGi!=null) dropped.add(tagOf(t.removeGi)); if(t.dropGi!=null) dropped.add(tagOf(t.dropGi)); });   // lines a later step removes on purpose (maximum quality) are not kept
  function keepBefore(n){ const out=startKeep.map(t=>({tag:t, maker:'h1'})), i=N.indexOf(n), L=lane(n);
    for(let j=0;j<i;j++){ const m=N[j]; if(!isMainish(m)) continue; if(m.branch && lane(m)!==L) continue; const t=m.target||{}; const tg=tgOf(m);
      if(t.removeGi!=null){ const k=tagOf(t.removeGi); const x=out.findIndex(o=>o.tag===k); if(x>=0) out.splice(x,1); }
      if(t.dropGi!=null){ const k=tagOf(t.dropGi); const x=out.findIndex(o=>o.tag===k); if(x>=0) out.splice(x,1); }
      if(tg && !t.junk && !out.some(o=>o.tag===tg) && !dropped.has(tg)) out.push({tag:tg, maker:m.id}); }
    return out; }

  // ---------- item lines along the main lane (left column of the chart)
  const lineOf = (gi, m, extra, tag) => { const g=G[gi], tm=tmaxOf[gi]||1, t=g.t[Math.min(g.t.length-1, Math.max(0,tm-1))]; const kr=(t?.[4]||'').replace(/\n/g,' / '), en=(t?.[5]||'').replace(/\n/g,' / ');
    return {s:g.g, kr: kr + (extra?' ('+extra.kr+')':''), en: en + (extra?' ('+extra.en+')':''), m, tags:[tag||tagOf(gi)], rep:tagOf(gi)}; };
  /* 묶음(anyOf) 목표: 아이템 칸에는 아직 없는 옵션을 차례로 보여 줌(사용자 2026-11-12: 같은 옵션 3개로 보였음) */
  const pickGi = list => { const have=new Set(cur.map(l=>l.rep).filter(Boolean)); return (list.find(x=>!have.has(tagOf(x.gi)))||list[0]).gi; };
  const J = s => ({s, kr:'잡옵', en:'Junk', m:'j'}), UN = s => ({s, kr:'훼손 옵션(미공개)', en:'Desecrated (unrevealed)', m:'u'});
  const RND = s => ({s, kr:'랜덤 옵션 1개', en:'One random line', m:'j'});
  let cur = (d.start.mods||[]).map(m=> m.junk ? J(m.junk) : m.unrev ? UN(m.unrev) : lineOf(m.gi, m.fr?'f':'n'));
  const dropOne = (pred) => { const i=cur.findIndex(pred); if(i>=0) cur.splice(i,1); return i>=0; };
  const dropJunk = s => dropOne(l=>l.m==='j' && (!s || l.s===s)) || false;
  const items={};

  // ---------- nodes
  const out=[], extra=[], pos={}; let row=1;
  const curName = id => { for(const k in (opt.craft||{})) for(const x of opt.craft[k]) if(x.id===id) return x; return null; };
  const cn = id => { const x=curName(id); return x ? K(x.kr, x.en) : K(id, id); };
  const DO2ACT = {transmute:'transmute', augment:'augment', regal:'regal', exalt:'exalt', chaos:'chaos', essence:'essence', desecrate:'desecrate', reveal:'reveal', remove:'annul', quality:'quality', manual:'rune', divine:'divine', socket:'rune', fracture:'fracture'};
  const LABEL = {transmute:K('진화','Transmute'), augment:K('확장','Augment'), regal:K('제왕','Regal'), exalt:K('엑잘','Exalt'), chaos:K('카오스','Chaos'), essence:K('에센스','Essence'), desecrate:K('훼손','Desecrate'), reveal:K('공개','Reveal'), annul:K('소멸','Annul'), quality:K('퀄리티','Quality'), rune:K('룬','Rune'), divine:K('신성','Divine'), fracture:K('분열','Fracture')};
  const sideWord = s => s==='p' ? K('접두','Prefix') : s==='s' ? K('접미','Suffix') : K('','');
  function goalOf(n, a){ const t=n.target||{}, tg=targetTag(t);
    const sd = t.side || (t.junk && typeof t.junk==='string' ? t.junk : null) || omSide(n.omens, /Exaltation|Coronation|Necromancy|Crystallisation|Erasure|Annulment/) || (t.gi!=null ? G[t.gi].g : t.unrev || null);
    const w=sideWord(sd);
    if(a==='reveal') return K('훼손 옵션 확인','Reveal the desecrated modifier');
    if(a==='desecrate') return K(`${w.kr} 옵션(훼손)`.trim(), `${w.en} (desecrated)`.trim());
    if(a==='quality') return K(`퀄리티 ${t.quality||20}%`, `Quality ${t.quality||20}%`);
    if(a==='annul') return t.removeDes ? K('훼손 옵션 제거','Remove the desecrated modifier') : K('소멸의 오브 사용','Use an Orb of Annulment');
    if(a==='rune') return n.label || K('룬 장착','Socket a rune');
    if(t.junk) return K(`${w.kr} 잡옵`.trim(), `${w.en} junk line`.trim());
    if(tg) return K(`${w.kr} 옵션`.trim(), `${w.en} modifier`.trim());
    return n.label || LABEL[a]; }
  const showOf = n => { const t=n.target||{}; const list = t.anyOf || t.reveal?.anyOf || (t.gi!=null ? [t] : t.reveal ? [t.reveal] : t.mark ? [t.mark] : []); return list.length ? [...new Set(list.map(x=>tagOf(x.gi)))] : null; };
  /* 2026-11-12(균열 반지 하이엔드가 끝나지 않던 원인): 분열 베이스의 첫 카오스가 만든 옵션을 잃으면, 잡옵이 여럿 쌓인 채 카오스로 돌아가지 않고
     소멸의 오브로 분열 옵션 + 잡옵 1개만 남긴 뒤 다시(정책 3장: 잡옵이 여러 개인 채로 카오스를 돌리지 않음) */
  const firstChaos = (()=>{ if(!(d.start.mods||[]).some(m=>m.fr)) return null; const m=N.find(x=>x.do!=='base' && x.do!=='note' && !x.fallbackFor && !x.branch); return m && m.do==='chaos' && m.fail?.goto==='self' ? m.id : null; })();
  const cleanTo = maker => { if(maker!==firstChaos) return maker; const id='cl'+maker;
    if(!extra.some(x=>x.id===id)) extra.push({id, kind:'cleanup', group:'main', keep:[], maxJunk:1, label:K('소멸의 오브 사용','Use an Orb of Annulment'), goal:K('잡옵 정리','Clear the junk'), target:K('분열 옵션 + 잡옵 1개만 남기고 다시 카오스','Keep the fracture and one junk line, then Chaos again'), edges:[{to:maker}], _row:2, _col:3});
    return id; };
  function lostEdges(n, keep){ // a kept line removed by this step → back to the step that made it
    return keep.filter(k=>k.maker!==n.id).map(k=>({if:{removed:k.tag}, to:cleanTo(k.maker), res:'fail', lost:k.tag, hide:true})); }
  let vN=0;
  function failPath(n, F, keep, r){ if(!F) return null; const go = F.goto==='self' ? n.id : (F.goto==='restart' || byId[F.goto]?.do==='base') ? 'h1' : F.goto;
    if(!F.via) return go;
    const id='v'+(++vN)+n.id, v=F.via, a = v.cur==='Orb_of_Annulment' ? 'annul' : /Bone|Jawbone|Rib|Collarbone|Cranium/.test(v.cur||'') ? 'desecrate' : 'annul';
    const lostTo = F.lost ? (byId[F.lost]?.do==='base' ? 'h1' : cleanTo(F.lost)) : null, lostTag = F.lost ? (keep.find(k=>k.maker===F.lost)?.tag || targetTag(byId[F.lost]?.target)) : null;
    /* 지운 옵션 확인 순서(W5): 낱개 옵션(산 베이스 옵션 등) 먼저, 그 단계가 노린 옵션은 뒤 — 묶음 태그(anyOf)가 산 옵션을 품으면(K39 희귀도 반지: 산 희귀도 접두가 묶음에 들어감)
       그 옵션이 지워져도 '노린 옵션이 지워짐'으로 읽혀 새 베이스 대신 엑잘로 돌아가고 완성품에 산 옵션이 없었음(33%) */
    const le=lostEdges({id}, keep).filter(e=>e.if.removed!==lostTag), lt = lostTo && lostTag ? [{if:{removed:lostTag}, to:lostTo, res:'fail', lost:lostTag}] : [];
    const edges = tags[lostTag]?.anyOf ? [...le, ...lt, {to:go}] : [...lt, ...le, {to:go}];
    extra.push({id, kind:'act', group:'main', act:a, cur:v.cur, omens:v.omens, label: a==='annul' ? K('소멸의 오브 사용','Use an Orb of Annulment') : LABEL[a],
      goal: (v.omens||[]).includes('Omen_of_Light') ? K('훼손 옵션 제거','Remove the desecrated modifier') : K('소멸의 오브 사용','Use an Orb of Annulment'), edges, _row:r, _col:2});
    return id; }

  /* 갈래 주인(공개 등) 뒤, 첫 갈래 단계 전에 본선 단계가 있으면(MazBro 시전자 목걸이: 공개 → 퀄리티·엑잘(본선) → 공개 결과로 갈래) 예전엔 공개에서 바로 갈래로 건너뛰어
     본선 단계를 거치지 않았고(접두 옵션 하나 덜 만듦, 하이엔드 완성 조건 0%) 본선 끝은 갈래를 모른 채 완성으로 갔음 → 공개 뒤 본선으로 이어 가고 본선 끝에서 공개 결과(원하는 옵션 있음)로 갈래 */
  const deferOf={}, joinOf={}; N.forEach((n,i)=>{ if(n.branch || !N.some(x=>x.branch?.of===n.id)) return; const b0=N.findIndex(x=>x.branch?.of===n.id);
    const mids=N.slice(i+1, b0).filter(m=>isMainish(m) && !m.branch && m.do!=='note' && DO2ACT[m.do]); if(!mids.length) return;
    deferOf[n.id]={next:mids[0].id}; joinOf[mids[mids.length-1].id]={owner:n, ok:branchFirst(n.id,'ok'), miss:branchFirst(n.id,'miss')}; });
  let hasCmp=false, hasCmpL=false, hasFx=false; const softTags=new Set();
  /* 그쪽 마지막 옵션: 이 단계 뒤 본선에 같은 쪽 옵션을 굴려 노리는 단계(엑잘·카오스·공개 등)가 없음 — 에센스·합금처럼 확정으로 붙는 단계는 세지 않음 */
  const sideOfT = t => { if(!t) return null; if(t.side) return t.side; const gi = t.gi ?? t.anyOf?.[0]?.gi ?? t.reveal?.gi ?? t.reveal?.anyOf?.[0]?.gi; return gi!=null && G[gi] ? G[gi].g : (typeof t.junk==='string' ? t.junk : t.unrev || null); };
  const lastOfSide = n => { const sd=sideOfT(n.target); if(!sd) return false; const i=N.indexOf(n);
    return !N.slice(i+1).some(m=>isMainish(m) && !m.optional && m.do!=='note' && ['exalt','chaos','reveal','regal','augment','transmute'].includes(m.do) && !(m.target||{}).junk && sideOfT(m.target)===sd); };
  const retry0 = n => n.fail || n.compromise || (fb[n.id]||[]).length || N.some(x=>x.branch?.of===n.id);
  const emit = (n, r, col) => {
    const a = DO2ACT[n.do]; if(!a) return null;
    const t=n.target||{}, ch=chainOf[n.id], tg=ch ? ch.tag : targetTag(t), keep=keepBefore(n);
    const o={id:n.id, kind:'act', group:'main', act:a, label:LABEL[a], goal:goalOf(n,a), edges:[]};
    if(n.cur) o.cur=n.cur; if(n.omens?.length) o.omens=[...n.omens];
    const sh=showOf(n); if(sh) o.show=sh;
    if(a==='essence'){ o.ess = tg || tagOf(t.gi); if(t.mark){ o.mark=true; if(t.mark.alt!=null) o.alt=tagOf(t.mark.alt); }
      // 액체(주얼): 먼저 무작위 옵션 하나를 지우고 붙음, 제작 옵션 아님. 경멸은 결과가 둘(+1 접미 허용 / +1 접두 허용) — 원하는 쪽이 붙어야 성공
      if((opt.craft?.liquids||[]).some(x=>x.id===n.cur)){ o.liquid=true;
        if(t.slots && t.gi!=null){ tags[tagOf(t.gi)].slot=t.slots; const nm=G[t.gi].t[0][3], ag=G.findIndex((x,i)=>i!==t.gi && x.s===G[t.gi].s && x.g!==G[t.gi].g && x.t[0]?.[3]===nm);
          if(ag>=0){ const sd=Object.keys(t.slots)[0]; o.alt=tagOf(ag); tags[o.alt].slot={[sd==='p'?'s':'p']:1}; } } } }
    if(a==='desecrate' && t.fromMark) o.fromMark=true;
    if(a==='reveal'){ o.want=tg; }
    if(a==='quality'){ o.count=t.quality||20; o.q=t.quality||20; }
    if(a==='rune'){ const rn=t.rune || (t.runeSwap||[])[0]; if(rn) o.rune=rn; if(t.slots) o.slots=t.slots; if(n.label) o.goal=n.label; }
    if(n.extra) o.extraUse=n.extra;
    /* 에센셜 접두 마무리(랜덤 옵션 채우기) = 상위 엑잘(리버스 13장 사용자 확정 11-13 20:22, W5): 다른 등급은 초안 오브 그대로 */
    if(n.junkFill && a==='exalt' && t.junk==='p' && n.cur!=='Greater_Exalted_Orb' && grades.includes('ess')){ o.fillEss=true; o.over=[{param:{fx:'g'}, set:{cur:'Greater_Exalted_Orb'}}]; hasFx=true; }
    /* K40(2026-11-12): 절사 반복 — 시뮬이 그때그때 절사·절사 + 말소·말소만(1/2)을 고름(잡옵이 지킬 옵션보다 높으면 말소만) */
    if(n.trim && a==='chaos'){ const kp = n.trim.keep?.length ? anyTag(n.trim.keep) : null; o.trim = {side:n.trim.side, ...(kp?{keep:kp}:{})}; o.omens=(o.omens||[]).filter(x=>!/Whittling|Erasure/.test(x)); if(!o.omens.length) delete o.omens; }
    // success condition
    const okIf = tg && !t.junk && ['transmute','augment','regal','exalt','chaos','reveal'].includes(a) ? (a==='reveal' && !n.pool ? {any:[{added:tg},{has:tg}]} : {added:tg}) : (a==='essence' && o.liquid && o.alt ? {added:tg} : null);   // a reveal: the wanted line may already be on the item
    const dj = deferOf[n.id];   /* 갈래 결정을 뒤로 미룸(W5): 갈래 전에 본선 단계가 더 있으면 성공·빗나감 모두 그 단계로, 갈래는 그 본선 끝(join)에서 */
    const nxt = dj ? dj.next : n.branch==null && N.some(x=>x.branch?.of===n.id) ? (branchFirst(n.id,'ok')||nextMain(n)) : nextMain(n);
    const missTo = dj ? dj.next : N.some(x=>x.branch?.of===n.id) ? branchFirst(n.id,'miss') : null;
    o.edges.push(...lostEdges(n, keep));
    const Fx = n.fail || n.compromise?.fail; if(okIf && retry0(n) && (a==='reveal' || (a!=='chaos' && !(fb[n.id]||[]).some(x=>x.do!=='note') && !Fx?.via))) o.edges.push({if:{famBlock:tg}, to:'h1', res:'fail', hide:true});   // nothing on the way back can clear the blocking line   // another line already holds the wanted family: a new base
    if(okIf) o.edges.push({if:okIf, to:nxt, res:'ok'});
    else if(!missTo) o.edges.push({to:nxt, res:'ok'});   // no line to look for: a removed kept line (above) is the only way back
    // failure
    const reals=(fb[n.id]||[]).filter(x=>x.do!=='note' && !skipNode(x)), notes=(fb[n.id]||[]).filter(x=>x.do==='note');
    const F = n.fail || n.compromise?.fail;
    const retry = missTo || (reals.length ? reals[0].id : failPath(n, F, keep, r));
    if(okIf || missTo){
      if(n.compromise?.soft && !missTo){ softTags.add(tg); o.edges.push({to:nxt, res:'fail'}); }   // 유효 옵션(사용자 확정 2026-11-11): 한 번만 시도하고 빗나가면 모든 등급에서 그대로
      else if((n.compromise || notes.length) && retry && !missTo){
        /* 갈림(W5, 정책 10장 C17-2·리버스 13장 20:22): 필수 훼손 공개는 등급과 상관없이 다시(빛의 징조·아스트리드), 그쪽 마지막 옵션(뒤에 그쪽을 굴리는 단계가 없음)은
           하이엔드만 다시 하고 밸런스·에센셜은 그대로(cmpl), 그 밖의 타협은 에센셜만 그대로(cmp) */
        const kind = a==='reveal' ? 'des' : lastOfSide(n) ? 'cmpl' : 'cmp';
        if(kind==='des') o.edges.push({to:retry, res:'fail'});
        else { (kind==='cmpl' ? (hasCmpL=true) : (hasCmp=true)); o.edges.push({if:{param:{[kind]:'retry'}}, to:retry, res:'fail'}, {to:nxt, res:'fail'}); } }
      else if(retry) o.edges.push({to:retry, res:'fail'});
      else o.edges.push({to:nxt, res:'fail'}); }
    // already done (a line that came back after a loss): skip the step
    if(t.skipHas!=null && !n.k42){ const c={has:tagOf(t.skipHas)}; o.skipIf = n.preCnt!=null && typeof t.junk==='string' ? {any:[c, {not:{sideLt:{side:t.junk, n:n.preCnt+1}}}]} : c; o.skipTo=nxt; }   /* K42: 빗나간 엑잘 자리에 이미 붙은 에센스 — 버릴 옵션·에센스 단계를 건너뜀 */
    else if(ch){ o.skipIf={count:{tag:ch.tag, min:ch.idx+1}}; o.skipTo=nxt; }
    else if(tg && !t.junk && !t.anyOf && a!=='reveal' && (okIf || a==='essence')) { o.skipIf={has:tg}; o.skipTo=nxt; }   // anyOf (policy 6: any single resistance) may already be met by another line
    else if(t.junk && ['exalt','chaos'].includes(a)){ const s=typeof t.junk==='string' ? t.junk : omSide(n.omens,/Exaltation/); if(s && a==='exalt'){ o.skipIf={full:s}; o.skipTo=nxt;
        /* 붙여 넣은 옵션 수만큼 채우는 엑잘(junkFill)인데 그쪽이 이미 꽉 참(앞 단계 카오스·타협이 반대쪽 대신 그쪽에 붙임) → 반대쪽 자리를 채우는 엑잘로(W5, MazBro 시전자 목걸이 밸런스 59%가 옵션 5개로 끝남) */
        if(n.junkFill){ const os = s==='p' ? 's' : 'p', tw={id:n.id+'o', kind:'act', group:'main', act:'exalt', cur:o.cur, label:o.label, goal:K(`${sideWord(os).kr} 랜덤 옵션`, `Random ${sideWord(os).en.toLowerCase()}`), skipIf:{full:os}, skipTo:nxt, edges:[{to:nxt, res:'ok'}], _row:r, _col:1};
          if(o.over) tw.over=o.over; extra.push(tw); o.skipTo=tw.id; } } }
    else if(a==='desecrate' && !t.fromMark){ const rv=N.slice(N.indexOf(n)+1).find(x=>x.do==='reveal'); const rt=rv && targetTag(rv.target); o.skipIf = rt ? {any:[{unrev:true}, rv.pool ? {count:{tag:rt, min:rv.pool}} : {has:rt}]} : {unrev:true}; o.skipTo=nxt; }
    o._row=r; o._col=col;
    return o; };

  // main lane in order, item lines tracked
  const mainOut=[];
  for(const n of N){
    if(n.do==='base'){ continue; }
    if(!isMainish(n) || n.do==='note') continue;
    const o=emit(n, row, 0); if(!o) continue;
    // item state after this step
    const t=n.target||{}, a=o.act, sdOm=omSide(n.omens, /Erasure|Crystallisation|Necromancy|Annulment/);
    if(t.removeGi!=null) dropOne(l=>l.tags?.includes(tagOf(t.removeGi)));
    if(t.dropGi!=null) dropOne(l=>l.tags?.includes(tagOf(t.dropGi)));
    /* 건너뛰는 단계(skipIf: 그 옵션이 이미 있음)가 노리는 옵션이 아이템 칸에 이미 다 있으면 같은 줄을 또 넣지 않음 — 완성 카드에 같은 옵션이 두 번 찍히던 것(2026-11-13 W4, 부재 목걸이 g16).
       같은 옵션 두 줄(붙여 넣은 아이템에 두 번, dupGi)은 그 수까지 */
    const full = gi => gi!=null && o.skipIf?.has===tagOf(gi) && cur.filter(l=>l.rep===tagOf(gi)).length >= Math.max(1, d.dupGi?.[gi]||0);
    if(full(t.gi) && ['chaos','transmute','augment','regal','exalt'].includes(a)){ o.item = cur.map(x=>({...x})); mainOut.push(o); row++; continue; }
    if(a==='chaos'){ if(t.removeGi==null) (dropJunk(sdOm)||dropJunk(null)); if(t.gi!=null) cur.push(lineOf(t.gi,'n',null,chainOf[n.id]?.tag)); else if(t.anyOf) cur.push(lineOf(pickGi(t.anyOf),'n',null,chainOf[n.id]?.tag || anyTag(t.anyOf))); else cur.push(RND(sdOm||'p')); }
    else if(['transmute','augment','regal','exalt'].includes(a)){ const sd=omSide(n.omens,/Exaltation|Coronation/); const k=(n.omens||[]).includes('Omen_of_Greater_Exaltation')?2:1;
      for(let i=0;i<k;i++){ if(i===0 && (t.gi!=null || t.anyOf)) cur.push(lineOf(t.gi??pickGi(t.anyOf),'n',null,chainOf[n.id]?.tag || (t.anyOf?anyTag(t.anyOf):null))); else cur.push(t.junk ? J(typeof t.junk==='string'?t.junk:(sd||'p')) : RND(sd||'p')); } }
    else if(a==='essence'){ const gi=t.mark ? t.mark.gi : t.gi;
      if(t.removeGi==null){ const s=omSide(n.omens,/Crystallisation/); if(s) dropJunk(s);
        /* 징조 없이 꽉 찬 쪽에 붙이면 그쪽 옵션 하나가 바뀜 — 성공 회차(잡옵이 바뀜)대로 잡옵 한 줄을 뺌. 접미가 4/3으로 보이던 것(2026-11-13 W4, Seek 장화) */
        else if(gi!=null){ const sd=G[gi].g, capS=(d.cap?.[sd]) ?? (3+((sd==='p'?base.pd:base.sd)||0)); if(cur.filter(l=>l.s===sd && l.m!=='r').length >= capS) dropJunk(sd); } } if(gi!=null) cur.push(lineOf(gi, t.mark?'c':'c', K(t.mark?'징표':'제작 옵션', t.mark?'mark':'crafted'))); }
    else if(a==='desecrate'){ const s=t.unrev||sdOm||'s'; if(t.fromMark) dropOne(l=>/징표/.test(l.kr)); cur.push(UN(s)); }
    else if(a==='reveal'){ const i=cur.findIndex(l=>l.m==='u'); const gi=t.reveal?.gi ?? (t.reveal?.anyOf ? pickGi(t.reveal.anyOf) : null); if(i>=0) cur.splice(i,1, gi!=null ? lineOf(gi,'d',null,targetTag(t)) : {...UN(cur[i].s), m:'d'}); }
    else if(a==='annul'){ if(t.removeDes) dropOne(l=>l.m==='d'||l.m==='u'); else if(t.dropGi==null) dropJunk(sdOm); }
    else if(a==='rune' && o.rune) cur.push({s:'r', kr:o.rune.kr, en:o.rune.en, m:'r'});
    o.item = cur.map(x=>({...x}));
    mainOut.push(o); row++; }
  // fallbacks (to the right of the step they back up)
  const fbOut=[];
  for(const n of N){ if(!n.fallbackFor || n.do==='note' || skipNode(n)) continue; const X=byId[n.fallbackFor], xo=mainOut.find(o=>o.id===X.id); if(!xo) continue;
    const o=emit(n, xo._row, 1); if(!o) continue;
    // its success goes on like the step it backs up
    const xn = nextMain(X); o.edges = o.edges.map(e=>e.res==='ok' ? {...e, to:xn} : e); if(o.skipTo) o.skipTo=xn;
    /* K42: 에센스를 붙이면 같은 엑잘로 돌아가고, 이미 붙어 있으면 그 엑잘의 평소 정리(다음 대체 단계 또는 실패 경로)로 */
    if(n.k42){ o.edges = o.edges.map(e=>e.res==='ok' ? {...e, to:X.id} : e); const rest=(fb[X.id]||[]).filter(x=>x!==n && x.do!=='note' && !skipNode(x));
      o.skipTo = rest.length ? rest[0].id : (failPath(X, X.fail, keepBefore(X), xo._row) || xn); }
    fbOut.push(o); }
  /* 미룬 갈래의 본선 끝(join): 그 단계의 다음(성공) 선을 공개 결과 갈래로 둘로 나눔 — 원하는 옵션이 있으면 성공 갈래, 없으면 빗나감 갈래 */
  for(const o of mainOut){ const J=joinOf[o.id]; if(!J) continue; const T=targetTag(J.owner.target), j0=nextMain(byId[o.id]);
    o.edges = o.edges.flatMap(e=>{ if(e.to!==j0 || e.hide || e.if?.removed) return [e]; const out=[];
      if(J.ok) out.push({...e, if: e.if ? {all:[e.if, {has:T}]} : {has:T}, to:J.ok}); out.push({...e, to:J.miss||J.ok||e.to}); return out; });
    if(o.skipTo===j0) o.skipTo = J.miss||J.ok||o.skipTo; }
  const all=[...mainOut, ...fbOut, ...extra];
  // positions: main lane rows, the rest to the right (one column per kind), sharing the row of the step they serve
  const taken={}; all.forEach(o=>{ let c=o._col||0; if(c>0){ while(taken[c+'|'+o._row]) c++; taken[c+'|'+o._row]=1; } o.pos=[c, o._row]; delete o._row; delete o._col; });
  const startItem = (d.start.mods||[]).map(m=> m.junk ? J(m.junk) : m.unrev ? UN(m.unrev) : lineOf(m.gi, m.fr?'f':'n'));
  const first = mainOut[0]?.id || 'ok';
  const baseLabel = d.start.rar==='magic' ? K('매직 베이스 구입','Buy a magic base') : (d.start.mods||[]).some(m=>m.fr) ? K('분열 베이스 구입','Buy a fractured base') : K('베이스 구입','Buy a base');
  const nodes=[{id:'h1', kind:'base', group:'prep', pos:[0,0], next:'ms', start:{rar:d.start.rar||'normal', mods:(d.start.mods||[]).map(m=> m.junk ? {junk:m.junk} : m.unrev ? {unrev:m.unrev} : (m.fr ? {tag:tagOf(m.gi), fr:true} : tagOf(m.gi)))}, label:baseLabel, item:startItem},
    {id:'ms', kind:'mark', group:'main', pos:[0,0.6], next:first, label:K('아이템 제작 시작','Item crafting starts'), item:startItem},
    ...all, {id:'ok', kind:'done', group:'main', pos:[0,row], label:K('완성','Finished')}];
  /* 묶음(anyOf) 태그의 성공 회차 옵션 = 붙여 넣은 옵션(2026-11-13 W4, 규칙 K·S4): 아이템 칸·완성 카드에 그 줄이 실제로 들어간 옵션(rep) 순서대로.
     화면은 'A 또는 B'(목표처럼 읽힘) 대신 붙여 넣은 옵션을 보여 주고, 레시피 글은 '대신 …도 성공으로 침' 꿀팁을 붙임. 시뮬은 shown을 읽지 않음 */
  { const sh={}; const take = l => { const k=l?.tags?.[0]; if(!k || !tags[k]?.anyOf || !l.rep || l.rep===k) return; (sh[k]=sh[k]||[]); if(!sh[k].includes(l.rep)) sh[k].push(l.rep); };
    nodes.forEach(n=>(n.item||[]).forEach(take)); cur.forEach(take);
    for(const [k,v] of Object.entries(sh)) if(v.length) tags[k].shown = v; }
  // the start lines' tiers are fixed (cheap: bought or fractured)
  // ---------- versions, strategies, finals, require
  const params={}; for(const gi of loopGi) params['t'+gi]={kr:'티어', en:'Tier', values:{}};
  grades.forEach(v=>{ for(const gi of loopGi){ const x=P[v]['t'+gi]; const lo=Math.max(1, G[gi].t.findIndex(t=>t[0]<=d.ilvl)+1), n=+x; params['t'+gi].values[x]=K(n<=lo?`${lo}티어`:`${lo}~${n}티어`, n<=lo?`T${lo}`:`T${lo}–${n}`); } });
  /* 갈림 등급(W5): cmp = 에센셜만 그대로, cmpl(그쪽 마지막 옵션) = 하이엔드만 다시(C17-2). 등급 이름으로 정함 — 예전엔 등급 목록의 마지막 하나만 그대로 */
  if(hasCmp){ params.cmp={kr:'빗나가면', en:'On a miss', values:{retry:K('다시 작업','Rework'), settle:K('타협 (그대로)','Settle (keep it)')}}; grades.forEach(v=>{ P[v].cmp = v==='ess' ? 'settle' : 'retry'; }); }
  if(hasCmpL){ params.cmpl={kr:'마지막 옵션이 빗나가면', en:'Last line missed', values:{retry:K('다시 굴림','Roll again'), settle:K('그대로','Keep it')}}; grades.forEach(v=>{ P[v].cmpl = v==='high' ? 'retry' : 'settle'; }); }
  if(hasFx){ params.fx={kr:'마무리 엑잘', en:'Finishing exalt', values:{p:K('초안 오브','Draft orb'), g:K('상위 엑잘티드 오브','Greater Exalted Orb')}}; grades.forEach(v=>{ P[v].fx = v==='ess' ? 'g' : 'p'; }); }
  const cmpBy = k => new Set(mainOut.filter(o=>o.edges.some(e=>e.if?.param?.[k])).flatMap(o=>[...(o.show||[]), targetTag(byId[o.id]?.target)].filter(Boolean)));
  const cmpT = {cmp:cmpBy('cmp'), cmpl:cmpBy('cmpl')}, cmpTags = new Set([...cmpT.cmp, ...cmpT.cmpl]);
  const settleOf = (v, t) => (P[v].cmp==='settle' && cmpT.cmp.has(t)) || (P[v].cmpl==='settle' && cmpT.cmpl.has(t));
  const finalTags = cur.filter(l=>l.tags).map(l=>l.tags[0]);
  const reqHas = [...new Set(finalTags)].filter(t=>!softTags.has(t) && !(tags[t]?.gi!=null && G[tags[t].gi].f.includes('ItemMaxQuality')));
  /* 같은 태그 두 줄(일반 + 훼손 같은 옵션, 2026-11-13 W1): 완성품에 그 수만큼 있어야 완성 */
  /* 같은 묶음(anyOf) 태그 두 줄(예: 아무 원소 저항 두 개, 2026-11-13 W5): 완성 카드에 그 태그 줄이 둘이면 완성 조건도 두 개(fincheck와 같음) */
  const leafN = t => new Set((tags[t]?.anyOf||[]).map(k=>tags[k]?.gi).filter(x=>x!=null)).size;   /* 묶음 잎 옵션 수 — 갈래(성공·빗나감 경로)가 같은 아이템 칸에 둘 다 쌓이면 줄이 잎 수보다 많아질 수 있음 */
  const occ = t => tags[t]?.gi!=null ? (d.dupGi?.[tags[t].gi]||0) : tags[t]?.anyOf ? Math.min(leafN(t), cur.filter(l=>l.tags?.[0]===t).length) : 0;   /* 붙여 넣은 아이템의 줄 수(완성 카드 줄은 중복이 생길 수 있어 쓰지 않음) */
  const need1 = t => { const n=Math.max(chainN[t]||0, occ(t)); return chainN[t] || n>1 ? {count:{tag:t, min:n}} : {has:t}; };
  const require = {all: reqHas.map(t=> cmpTags.has(t) ? {any:[need1(t), ...['cmp','cmpl'].filter(k=>cmpT[k].has(t)).map(k=>({param:{[k]:'settle'}}))]} : need1(t))};
  const desc = v => { const p=P[v], ws=[...loopGi].filter(gi=>p['t'+gi]!=='1'); const parts=[];
    if(ws.length) parts.push(K(`반복으로 찾는 옵션 ${ws.length}개를 넓은 티어로`, `${ws.length} looped line(s) at wider tiers`)); else parts.push(K('고른 티어 그대로','The tiers you picked'));
    if(p.cmp==='settle' || p.cmpl==='settle') parts.push(p.cmp==='settle' ? K('빗나가면 결과 그대로','keep a miss as it comes') : K('마지막 옵션은 결과 그대로','keep the last line as it comes'));
    return K(parts.map(x=>x.kr).join(' · '), parts.map(x=>x.en).join(' · ')); };
  /* 규칙 K(2026-11-13 W4): 빗나가도 그대로 두는 등급(cmp settle)에서 그 갈림길이 만든 자리는 완성 카드에 '랜덤 옵션' — 목표 옵션이 늘 붙는 것처럼 보이지 않게 */
  const settleLine = (v, l) => l.tags && [l.tags[0], l.rep, l._k].some(t=>t && settleOf(v, t));
  /* 완성 카드 줄 중복 빼기(W5, MazBro 시전자 목걸이: 공개 성공·빗나감 갈래가 같은 묶음 옵션을 둘 다 아이템 칸에 넣어 마나 최대치가 두 번 — 접두 4개): 같은 옵션 태그 줄은 붙여 넣은 줄 수(dupGi)까지 */
  const curF = (()=>{ const seen={}; return cur.filter(l=>{ const k=l.rep && l.rep!==l.tags?.[0] ? l.rep : null; const gi=k ? tags[k]?.gi : null; if(gi==null) return true; seen[k]=(seen[k]||0)+1; return seen[k] <= Math.max(1, d.dupGi?.[gi]||0); }); })();
  const finals = grades.map(v=>({id:v, kr:VN[v].kr+' 옵션', en:VN[v].en, lines: curF.map(l=>{ if(!l.tags) return l; const k = chainN[l.tags[0]] && l.rep ? l.rep : l.tags[0]; return {...l, _k:k}; }).map(l=> settleLine(v, l) ? {side:l.s, random:true, ...(l.m==='d'?{des:true}:{})} : l.tags ? {tag:l._k, tmax: tags[l._k].tmax && String(tags[l._k].tmax)[0]==='$' ? +P[v][String(tags[l._k].tmax).slice(1)] : tags[l._k].tmax, ...(l.m==='f'?{fr:true}:{}), ...(l.m==='d'?{des:true}:{})} : l.m==='r' ? null : {side:l.s, random:true}).filter(Boolean)}));
  const g={id:d.id, recipe:d.id, cls:d.cls, base:base.en||d.base, ilvl:d.ilvl, note:'리버스 크래프팅 초안에서 만든 플로우차트', params,
    strategies:grades.map(v=>({id:v, params:P[v]})), versions:[...grades].reverse().map(v=>({id:v, kr:VN[v].kr, en:VN[v].en, params:P[v], desc:desc(v)})),
    tags, require, groups:[{id:'prep',kr:'베이스템 완성',en:'Finished base',cols:[0,1]},{id:'main',kr:'옵션 추가 작업',en:'Adding modifiers',cols:[0,1]}],
    start:'h1', loops:[], finals, finalItem:{quality:d.start.quality||20, sockets:0}, nodes};
  if(d.cap) g.cap=d.cap;
  // 장착한 증강물(룬·영혼 핵)의 전용 옵션: 그 룬이 있어야 풀에 들어감(sim.js xsub). 엑잘·카오스로 노리는 단계가 있으면 그 풀에도(xroll)
  const xs=new Set(); (d.start.runes||[]).forEach(r=>r?.en && xs.add(r.en)); N.forEach(n=>{ const rn=n.target?.rune; if(rn?.en) xs.add(rn.en); });
  Object.values(tags).forEach(t=>{ const x=t.gi!=null && G[t.gi]; if(x && x.s==='x' && x.sub?.[1] && x.sub[1]!=='Otherworldly') xs.add(x.sub[1]); });
  const xsub=[...xs].filter(en=>G.some(x=>x.s==='x' && x.sub?.[1]===en));
  if(xsub.length){ g.xsub=xsub; const isX = t => !!t && [t.gi, ...(t.anyOf||[]).map(x=>x.gi)].some(gi=>gi!=null && G[gi].s==='x');
    if(N.some(n=>['exalt','chaos','regal','transmute','augment'].includes(n.do) && isX(n.target))) g.xroll=true; }
  if(/Astrid/.test(JSON.stringify([d.start.runes||[], N.map(n=>n.target?.rune||null)]))) g.astrid = !N.some(n=>/Astrid/.test(n.target?.rune?.en||''));   // 시작부터 장착돼 있으면 표시(정책 5장 C1 집계용)
  return g; }

// the drawing data the flowchart view reads (same fields as tools/sim/run.js writes)
function view(graph, D){ const tv={}; for(const [k,t] of Object.entries(graph.tags||{})){ if(t.anyOf){ tv[k]={anyOf:t.anyOf}; if(t.label){ tv[k].label=t.label; tv[k].s=t.side; } if(t.shown!=null) tv[k].shown=t.shown; if(t.shownBy) tv[k].shownBy=t.shownBy; continue; }   /* anyOf 묶음의 이름·성공 회차 옵션(tools/sim/run.js와 같은 칸, 2026-11-13 W4) */ const g=D.groups[t.gi]; if(!g) continue; const lo = graph.ilvl ? Math.max(1, g.t.findIndex(x=>x[0]<=graph.ilvl)+1) : 1; tv[k]={s:g.g, sec:g.s, tmax:t.tmax, gi:t.gi, tiers:g.t.slice(0,Math.max(5,lo+4)).map(x=>[x[4],x[5]]), ...(lo>1?{lo}:{})}; }   /* lo: 아이템 레벨로 붙을 수 있는 가장 좋은 티어(레벨 81 저항 = 2티어, 사용자 2026-11-12) */
  const pOnly=c=>{ if(!c) return; if(c.param) return c.param; if(c.all){ const o={}; c.all.forEach(x=>x.param&&Object.assign(o,x.param)); return Object.keys(o).length?o:undefined; } };
  return {tags:tv, finals:graph.finals, finalItem:graph.finalItem, basePrice:graph.basePrice, params:graph.params, groups:graph.groups, start:graph.start, loops:graph.loops, versions:graph.versions,
    /* 상자 칸은 tools/sim/run.js가 쓰는 것과 같게(2026-11-13 W4): 레시피를 플로우차트에서 읽는 fcread.js가 이 그림 데이터를 씀 */
    nodes:graph.nodes.map(n=>({id:n.id, kind:n.kind, act:n.act, cur:n.cur, curIf:n.curIf?.map(c=>c.cur), omens:n.omens, trim:n.trim?{side:n.trim.side,keepDes:n.trim.keepDes}:undefined, group:n.group, pos:n.pos, label:n.label,
      param:n.param, options:n.options, optStyle:n.optStyle, item:n.item, curRows:n.curRows, target:n.target, pAll:n.pAll, ask:n.ask, goal:n.goal, goalBy:n.goalBy, show:n.show, showText:n.showText, rune:n.rune, swapAstrid:n.swapAstrid, count:n.act==='rune'?n.count:undefined, fill:n.fill, showIf:n.showIf, over:n.over, once:n.once, skipNote:n.skipNote, skipLabel:n.skipLabel, skipHide:n.skipHide, gapBefore:n.gapBefore, variant:n.variant, note:n.note, attach:n.attach, tiers:n.kind==='side'?n.tiers:undefined, edgeLabels:n.edgeLabels, next:n.next, skipTo:n.skipTo, start:n.start,
      edges:(n.edges||[]).map(e=>({to:e.to, label:e.label, lost:e.lost, res:e.res, dash:e.dash, p:e.p, hide:e.hide, port:e.port, enter:e.enter, lane:e.lane, turn:e.turn, when:pOnly(e.if)}))}))}; }

// run every grade; problems a recipe must not have (a step with no way on, a finished item missing a must-have) come back in `issues`
function check(graph, D, craft, prices, SIM, N=2000, maxSteps=3e5){ const strategies=[], issues=[]; graph={...graph, maxSteps};
  for(const s of graph.strategies){ try{ const res=SIM.simulate(graph, D, craft, prices, s.params, N, 7);
      strategies.push({id:s.id, params:s.params, res});
      if(res.reqOk<0.98) issues.push({v:s.id, kr:`${VN[s.id].kr}: 완성품 ${Math.round((1-res.reqOk)*100)}%가 필수 옵션을 다 갖지 못함`, en:`${VN[s.id].en}: ${Math.round((1-res.reqOk)*100)}% of finished items miss a must-have`}); }
    catch(e){ const m=String(e.message||e), run=/^runaway at (.+)/.exec(m); strategies.push({id:s.id, params:s.params, error:m, runaway:run?run[1]:null});
      issues.push(run ? {v:s.id, kr:`${VN[s.id].kr}: ${run[1]} 단계 반복이 너무 많음 (사실상 만들 수 없는 목표)`, en:`${VN[s.id].en}: step ${run[1]} repeats far too often (practically out of reach)`}
        : {v:s.id, kr:`${VN[s.id].kr}: 진행이 막힘 (${m})`, en:`${VN[s.id].en}: the flow gets stuck (${m})`}); } }
  return {strategies, issues}; }

/* 난이도 표(정책 10장, 사용자 확정 2026-11-13 14:43 '난이도는 표로 통일' — tools/test/_difftable.py와 같은 경곗값, W5 2026-11-13).
   시뮬 결과 하나(가장 높은 등급)로: 가장 많이 한 단계(act 상자)의 시도 수, 비싼 징조 수, 평균 비용(div) 셋 중 가장 높은 단계.
   분열 상자가 있고 평균 베이스 2개 이상이면 최소 어려움(3). 리버스는 cost에 revCost(베이스 값 제외 + 매직 굴림)를 넘김 */
const DIFF_STEPS=[5,10,150,1500,20000], DIFF_OMENS=[0.5,1,15,25,300], DIFF_COST=[1,5,100,500,null];
function diffOf(res, graph, o={}){ if(!res) return null; const kinds={}; (graph?.nodes||[]).forEach(n=>kinds[n.id]=n.kind); const exp=new Set(o.expensive||EXP);
  let mx=0, mn=''; for(const [id,v] of Object.entries(res.nodes||{})){ if(['act','side'].includes(kinds[id]) && v.visits>mx){ mx=v.visits; mn=id; } }
  let om=0; for(const [k,v] of Object.entries(res.use||{})) if(exp.has(k)) om+=v;
  const cost = o.cost!=null ? o.cost : res.mean, C=[...DIFF_COST]; C[4]=o.mirror!=null ? o.mirror : Infinity;
  let lv=0; for(let i=0;i<5;i++) if(mx>=DIFF_STEPS[i] || om>=DIFF_OMENS[i] || cost>=C[i]) lv=i+1;
  const frac=(graph?.nodes||[]).some(n=>n.act==='fracture'); if(frac && (res.bases||1)>=2) lv=Math.max(lv,3);
  return {d:lv, steps:mx, node:mn, omens:om, cost, bases:res.bases||1}; }

/* 매직 베이스 굴림 비용(W2 → W5, 리버스 13장 사용자 확정 11-13 20:28·21:45): 노멀 베이스에서 진화 → 확장으로 산 매직 옵션을 만드는 기대 비용(div).
   ① 목표 옵션 둘 중 먼저 붙는 쪽을 첫 옵션으로 받고 확장은 남은 쪽을 노림(진화·확장 둘 다 '둘 중 아무거나' 묶음)
   ② 단일 원소 저항(화염·냉기·번개)은 같은 티어의 다른 원소 저항도 성공 → 끝에 유동체 단계(목표 원소가 아니면 사용, 시세 그대로)
   mode 'annul'(기본) = 빗나가면 소멸의 오브로 지우고 같은 베이스에 다시, 'restart' = 새 노멀 베이스로 처음부터(베이스 수 따로 — 참고값).
   오브 등급(일반·상위·완벽한)은 시뮬로 가장 싼 것. 결과 {div, bases} 또는 null */
const ELEM_F = {FireResistance:'Blazing_Flux', ColdResistance:'Chilling_Flux', LightningResistance:'Crackling_Flux'};
const MAGIC_ORB = {transmute:['Perfect_Orb_of_Transmutation','Greater_Orb_of_Transmutation','Orb_of_Transmutation'], augment:['Perfect_Orb_of_Augmentation','Greater_Orb_of_Augmentation','Orb_of_Augmentation']};
function magicCost(D, craft, prices, SIM, r, ms, mode='annul'){ ms=(ms||[]).filter(m=>m && (m.gi!=null || m.anyOf)); if(!ms.length || ms.length>2) return null;
  const G=D.groups, isEl = gi => { const g=G[gi]; return g && g.s==='n' && (g.f||[]).length===1 && ELEM_F[g.f[0]]; };
  const leaves = m => { const L=(m.anyOf || [m]).map(x=>({gi:x.gi, ...(x.tmax?{tmax:x.tmax}:{})})), out=[...L];
    if(!m.anyOf && isEl(m.gi)) G.forEach((g,gi)=>{ if(gi!==m.gi && isEl(gi) && g.g===G[m.gi].g && !out.some(x=>x.gi===gi)) out.push({gi, ...(m.tmax?{tmax:m.tmax}:{})}); });
    return out; };
  const all = ms.flatMap(leaves), two = ms.length>1, flux = ms.filter(m=>!m.anyOf && isEl(m.gi)).map(m=>({gi:m.gi, cur:ELEM_F[G[m.gi].f[0]]}));
  const fail = lost => mode==='restart' ? {goto:'restart'} : {goto:'self', via:{cur:'Orb_of_Annulment'}, ...(lost?{lost}:{})};
  const sim = (a, b) => { const nodes=[{id:'m0', phase:'base', do:'base', cost:'base'}, {id:'m1', phase:'magic', do:'transmute', cur:a, target:{anyOf:all}, ...(two?{pool:2}:{}), fail:fail()}];
    if(b) nodes.push({id:'m2', phase:'magic', do:'augment', cur:b, target:{anyOf:all}, pool:2, fail:fail('m1')});
    try{ const g=fromDraft({id:'mag', cls:r.cls, base:r.base, ilvl:r.ilvl, start:{rar:'normal', mods:[]}, nodes, difficulty:0}, D, {craft, grades:['high']});
      /* 유동체: 목표 원소가 아니면 바꿈(이미 목표 원소면 건너뜀) — 완성 직전에 끼움 */
      flux.forEach((f,i)=>{ const id='fx'+i, tg='g'+f.gi, nx = i+1<flux.length ? 'fx'+(i+1) : 'ok'; if(!g.tags[tg]) g.tags[tg]={gi:f.gi};
        g.nodes.forEach(n=>{ (n.edges||[]).forEach(e=>{ if(e.to==='ok' && i===0) e.to='fx0'; }); if(n.skipTo==='ok' && i===0) n.skipTo='fx0'; });
        g.nodes.splice(g.nodes.length-1, 0, {id, kind:'act', group:'main', act:'flux', cur:f.cur, label:{kr:'유동체',en:'Flux'}, skipIf:{has:tg}, skipTo:nx, edges:[{to:nx, res:'ok'}], pos:[0,8+i]}); });
      if(flux.length) g.require = {all:[...(g.require?.all||[]), ...flux.map(f=>({has:'g'+f.gi}))]};
      const x=SIM.simulate({...g, maxSteps:2e4}, D, craft, prices, g.strategies[0].params, 200, 3);
      return x.reqOk>=0.98 ? {div:x.useDiv, bases:x.bases} : null; }catch(_){ return null; } };
  const B = two ? MAGIC_ORB.augment[0] : null; let a0=MAGIC_ORB.transmute[0], v=null;
  for(const a of MAGIC_ORB.transmute){ const x=sim(a, B); if(x && (!v || x.div<v.div)){ v=x; a0=a; } }
  if(B) for(const b of MAGIC_ORB.augment.slice(1)){ const x=sim(a0, b); if(x && (!v || x.div<v.div)) v=x; }
  return v; }

const api={fromDraft, view, check, gradesFor, diffOf, magicCost};
if(typeof module!=='undefined' && module.exports) module.exports=api; else root.POE2GRAPH=api;
})(typeof window!=='undefined' ? window : globalThis);
