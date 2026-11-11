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
  const tierCnt = gi => G[gi].t.filter(t=>t[0]<=d.ilvl).length || G[gi].t.length;
  const P = {}; grades.forEach((v,i)=>{ const p={}; for(const gi of loopGi){ const t0=tmaxOf[gi]||1; p['t'+gi] = String(Math.min(tierCnt(gi), t0 + i)); } P[v]=p; });
  for(const gi in tmaxOf){ const k='g'+gi; tags[k].tmax = loopGi.has(+gi) ? '$t'+gi : tmaxOf[gi]; }
  for(const gi of Object.keys(tags).map(k=>+k.slice(1))) if(tags['g'+gi].tmax==null && tmaxOf[gi]==null) delete tags['g'+gi].tmax;
  let anyN=0; const anyMemo={}; const anyTag = list => { const ks=[...new Set(list.map(x=>tagOf(x.gi)))]; if(ks.length===1) return ks[0]; const key=ks.slice().sort().join('|'); if(anyMemo[key]) return anyMemo[key]; const k='a'+(++anyN); tags[k]={anyOf:ks}; return anyMemo[key]=k; };
  const targetTag = t => !t ? null : t.anyOf ? anyTag(t.anyOf) : t.gi!=null ? tagOf(t.gi) : t.reveal ? (t.reveal.anyOf ? anyTag(t.reveal.anyOf) : tagOf(t.reveal.gi)) : t.mark ? tagOf(t.mark.gi) : null;
  // 여러 옵션을 차례로 노리는 묶음(2026-11-11 고침): '원하는 옵션 중 하나'(anyOf) 단계 뒤에 그 나머지를 노리는 단계들이 이어지면 한 묶음.
  // 예전엔 첫 단계에서 둘째 옵션이 먼저 붙으면 다음 단계가 '이미 있음'으로 건너뛰어 첫째 옵션 없이 완성으로 셌음 → 묶음 단계는 '묶음 옵션이 k개 이상이면 건너뜀', 완성 조건은 '묶음 옵션 n개'
  const chainOf={}, chainN={}; { const ROLL=['exalt','chaos','regal','transmute','augment'], setOf = n => { const t=n.target||{}; return t.junk ? [] : t.anyOf ? t.anyOf.map(x=>x.gi) : t.gi!=null ? [t.gi] : []; };
    const cand = N.filter(n=>ROLL.includes(n.do) && !n.fallbackFor && !n.onLost && !n.optional && setOf(n).length);
    cand.forEach((S,i)=>{ if(chainOf[S.id] || !S.target.anyOf || S.target.anyOf.length<2) return; const L=new Set(setOf(S)), root=anyTag(S.target.anyOf); let k=1;
      for(const T of cand.slice(i+1)){ if(chainOf[T.id] || (T.branch?.of||'')!==(S.branch?.of||'')) continue; const st=setOf(T); if(st.length<L.size && st.every(g=>L.has(g))){ if(k===1) chainOf[S.id]={tag:root, idx:0}; chainOf[T.id]={tag:root, idx:k++}; } }
      if(k>1) chainN[root]=Math.min(k, L.size); }); }
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
  function lostEdges(n, keep){ // a kept line removed by this step → back to the step that made it
    return keep.filter(k=>k.maker!==n.id).map(k=>({if:{removed:k.tag}, to:k.maker, res:'fail', lost:k.tag, hide:true})); }
  let vN=0;
  function failPath(n, F, keep, r){ if(!F) return null; const go = F.goto==='self' ? n.id : (F.goto==='restart' || byId[F.goto]?.do==='base') ? 'h1' : F.goto;
    if(!F.via) return go;
    const id='v'+(++vN)+n.id, v=F.via, a = v.cur==='Orb_of_Annulment' ? 'annul' : /Bone|Jawbone|Rib|Collarbone|Cranium/.test(v.cur||'') ? 'desecrate' : 'annul';
    const lostTo = F.lost ? (byId[F.lost]?.do==='base' ? 'h1' : F.lost) : null, lostTag = F.lost ? (keep.find(k=>k.maker===F.lost)?.tag || targetTag(byId[F.lost]?.target)) : null;
    const edges=[...(lostTo && lostTag ? [{if:{removed:lostTag}, to:lostTo, res:'fail', lost:lostTag}] : []), ...lostEdges({id}, keep).filter(e=>e.if.removed!==lostTag), {to:go}];
    extra.push({id, kind:'act', group:'main', act:a, cur:v.cur, omens:v.omens, label: a==='annul' ? K('소멸의 오브 사용','Use an Orb of Annulment') : LABEL[a],
      goal: (v.omens||[]).includes('Omen_of_Light') ? K('훼손 옵션 제거','Remove the desecrated modifier') : K('소멸의 오브 사용','Use an Orb of Annulment'), edges, _row:r, _col:2});
    return id; }

  let hasCmp=false; const softTags=new Set();
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
    // success condition
    const okIf = tg && !t.junk && ['transmute','augment','regal','exalt','chaos','reveal'].includes(a) ? (a==='reveal' ? {any:[{added:tg},{has:tg}]} : {added:tg}) : (a==='essence' && o.liquid && o.alt ? {added:tg} : null);   // a reveal: the wanted line may already be on the item
    const nxt = n.branch==null && N.some(x=>x.branch?.of===n.id) ? (branchFirst(n.id,'ok')||nextMain(n)) : nextMain(n);
    const missTo = N.some(x=>x.branch?.of===n.id) ? branchFirst(n.id,'miss') : null;
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
      else if((n.compromise || notes.length) && retry && !missTo){ hasCmp=true; o.edges.push({if:{param:{cmp:'retry'}}, to:retry, res:'fail'}, {to:nxt, res:'fail'}); }
      else if(retry) o.edges.push({to:retry, res:'fail'});
      else o.edges.push({to:nxt, res:'fail'}); }
    // already done (a line that came back after a loss): skip the step
    if(ch){ o.skipIf={count:{tag:ch.tag, min:ch.idx+1}}; o.skipTo=nxt; }
    else if(tg && !t.junk && !t.anyOf && a!=='reveal' && (okIf || a==='essence')) { o.skipIf={has:tg}; o.skipTo=nxt; }   // anyOf (policy 6: any single resistance) may already be met by another line
    else if(t.junk && ['exalt','chaos'].includes(a)){ const s=typeof t.junk==='string' ? t.junk : omSide(n.omens,/Exaltation/); if(s && a==='exalt'){ o.skipIf={full:s}; o.skipTo=nxt; } }
    else if(a==='desecrate' && !t.fromMark){ const rv=N.slice(N.indexOf(n)+1).find(x=>x.do==='reveal'); const rt=rv && targetTag(rv.target); o.skipIf = rt ? {any:[{unrev:true},{has:rt}]} : {unrev:true}; o.skipTo=nxt; }
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
    if(a==='chaos'){ if(t.removeGi==null) (dropJunk(sdOm)||dropJunk(null)); if(t.gi!=null) cur.push(lineOf(t.gi,'n',null,chainOf[n.id]?.tag)); else if(t.anyOf) cur.push(lineOf(t.anyOf[0].gi,'n',null,chainOf[n.id]?.tag || anyTag(t.anyOf))); else cur.push(RND(sdOm||'p')); }
    else if(['transmute','augment','regal','exalt'].includes(a)){ const sd=omSide(n.omens,/Exaltation|Coronation/); const k=(n.omens||[]).includes('Omen_of_Greater_Exaltation')?2:1;
      for(let i=0;i<k;i++){ if(i===0 && (t.gi!=null || t.anyOf)) cur.push(lineOf(t.gi??t.anyOf[0].gi,'n',null,chainOf[n.id]?.tag || (t.anyOf?anyTag(t.anyOf):null))); else cur.push(t.junk ? J(typeof t.junk==='string'?t.junk:(sd||'p')) : RND(sd||'p')); } }
    else if(a==='essence'){ if(t.removeGi==null){ const s=omSide(n.omens,/Crystallisation/); if(s) dropJunk(s); }
      const gi=t.mark ? t.mark.gi : t.gi; if(gi!=null) cur.push(lineOf(gi, t.mark?'c':'c', K(t.mark?'징표':'제작 옵션', t.mark?'mark':'crafted'))); }
    else if(a==='desecrate'){ const s=t.unrev||sdOm||'s'; if(t.fromMark) dropOne(l=>/징표/.test(l.kr)); cur.push(UN(s)); }
    else if(a==='reveal'){ const i=cur.findIndex(l=>l.m==='u'); const gi=t.reveal?.gi ?? t.reveal?.anyOf?.[0]?.gi; if(i>=0) cur.splice(i,1, gi!=null ? lineOf(gi,'d',null,targetTag(t)) : {...UN(cur[i].s), m:'d'}); }
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
    fbOut.push(o); }
  const all=[...mainOut, ...fbOut, ...extra];
  // positions: main lane rows, the rest to the right (one column per kind), sharing the row of the step they serve
  const taken={}; all.forEach(o=>{ let c=o._col||0; if(c>0){ while(taken[c+'|'+o._row]) c++; taken[c+'|'+o._row]=1; } o.pos=[c, o._row]; delete o._row; delete o._col; });
  const startItem = (d.start.mods||[]).map(m=> m.junk ? J(m.junk) : m.unrev ? UN(m.unrev) : lineOf(m.gi, m.fr?'f':'n'));
  const first = mainOut[0]?.id || 'ok';
  const baseLabel = d.start.rar==='magic' ? K('매직 베이스 구입','Buy a magic base') : (d.start.mods||[]).some(m=>m.fr) ? K('분열 베이스 구입','Buy a fractured base') : K('베이스 구입','Buy a base');
  const nodes=[{id:'h1', kind:'base', group:'prep', pos:[0,0], next:'ms', start:{rar:d.start.rar||'normal', mods:(d.start.mods||[]).map(m=> m.junk ? {junk:m.junk} : m.unrev ? {unrev:m.unrev} : (m.fr ? {tag:tagOf(m.gi), fr:true} : tagOf(m.gi)))}, label:baseLabel, item:startItem},
    {id:'ms', kind:'mark', group:'main', pos:[0,0.6], next:first, label:K('아이템 제작 시작','Item crafting starts'), item:startItem},
    ...all, {id:'ok', kind:'done', group:'main', pos:[0,row], label:K('완성','Finished')}];
  // the start lines' tiers are fixed (cheap: bought or fractured)
  // ---------- versions, strategies, finals, require
  const params={}; for(const gi of loopGi) params['t'+gi]={kr:'티어', en:'Tier', values:{}};
  grades.forEach(v=>{ for(const gi of loopGi){ const x=P[v]['t'+gi]; params['t'+gi].values[x]=K(x==='1'?'1티어':`1~${x}티어`, x==='1'?'T1':`T1–${x}`); } });
  if(hasCmp){ params.cmp={kr:'빗나가면', en:'On a miss', values:{retry:K('다시 작업','Rework'), settle:K('타협 (그대로)','Settle (keep it)')}};
    grades.forEach((v,i)=>{ P[v].cmp = i===grades.length-1 && grades.length>1 ? 'settle' : 'retry'; }); if(grades.length===1) P[grades[0]].cmp='retry'; }
  const cmpTags = new Set(mainOut.filter(o=>o.edges.some(e=>e.if?.param?.cmp)).flatMap(o=>[...(o.show||[]), targetTag(byId[o.id]?.target)].filter(Boolean)));
  const finalTags = cur.filter(l=>l.tags).map(l=>l.tags[0]);
  const reqHas = [...new Set(finalTags)].filter(t=>!softTags.has(t) && !(tags[t]?.gi!=null && G[tags[t].gi].f.includes('ItemMaxQuality')));
  const need1 = t => chainN[t] ? {count:{tag:t, min:chainN[t]}} : {has:t};
  const require = {all: reqHas.map(t=> cmpTags.has(t) ? {any:[need1(t),{param:{cmp:'settle'}}]} : need1(t))};
  const desc = v => { const p=P[v], ws=[...loopGi].filter(gi=>p['t'+gi]!=='1'); const parts=[];
    if(ws.length) parts.push(K(`반복으로 찾는 옵션 ${ws.length}개를 넓은 티어로`, `${ws.length} looped line(s) at wider tiers`)); else parts.push(K('고른 티어 그대로','The tiers you picked'));
    if(p.cmp==='settle') parts.push(K('빗나가면 결과 그대로','keep a miss as it comes'));
    return K(parts.map(x=>x.kr).join(' · '), parts.map(x=>x.en).join(' · ')); };
  const finals = grades.map(v=>({id:v, kr:VN[v].kr+' 옵션', en:VN[v].en, lines: cur.map(l=>{ if(!l.tags) return l; const k = chainN[l.tags[0]] && l.rep ? l.rep : l.tags[0]; return {...l, _k:k}; }).map(l=> l.tags ? {tag:l._k, tmax: tags[l._k].tmax && String(tags[l._k].tmax)[0]==='$' ? +P[v][String(tags[l._k].tmax).slice(1)] : tags[l._k].tmax, ...(l.m==='f'?{fr:true}:{}), ...(l.m==='d'?{des:true}:{})} : l.m==='r' ? null : {side:l.s, random:true}).filter(Boolean)}));
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
function view(graph, D){ const tv={}; for(const [k,t] of Object.entries(graph.tags||{})){ if(t.anyOf){ tv[k]={anyOf:t.anyOf}; continue; } const g=D.groups[t.gi]; if(!g) continue; tv[k]={s:g.g, sec:g.s, tmax:t.tmax, gi:t.gi, tiers:g.t.slice(0,5).map(x=>[x[4],x[5]])}; }
  const pOnly=c=>{ if(!c) return; if(c.param) return c.param; if(c.all){ const o={}; c.all.forEach(x=>x.param&&Object.assign(o,x.param)); return Object.keys(o).length?o:undefined; } };
  return {tags:tv, finals:graph.finals, finalItem:graph.finalItem, basePrice:graph.basePrice, params:graph.params, groups:graph.groups, start:graph.start, loops:graph.loops, versions:graph.versions,
    nodes:graph.nodes.map(n=>({id:n.id, kind:n.kind, act:n.act, cur:n.cur, omens:n.omens, group:n.group, pos:n.pos, label:n.label, item:n.item, goal:n.goal, show:n.show, rune:n.rune, next:n.next, start:n.start,
      edges:(n.edges||[]).map(e=>({to:e.to, label:e.label, lost:e.lost, res:e.res, hide:e.hide, when:pOnly(e.if)}))}))}; }

// run every grade; problems a recipe must not have (a step with no way on, a finished item missing a must-have) come back in `issues`
function check(graph, D, craft, prices, SIM, N=2000, maxSteps=3e5){ const strategies=[], issues=[]; graph={...graph, maxSteps};
  for(const s of graph.strategies){ try{ const res=SIM.simulate(graph, D, craft, prices, s.params, N, 7);
      strategies.push({id:s.id, params:s.params, res});
      if(res.reqOk<0.98) issues.push({v:s.id, kr:`${VN[s.id].kr}: 완성품 ${Math.round((1-res.reqOk)*100)}%가 필수 옵션을 다 갖지 못함`, en:`${VN[s.id].en}: ${Math.round((1-res.reqOk)*100)}% of finished items miss a must-have`}); }
    catch(e){ const m=String(e.message||e), run=/^runaway at (.+)/.exec(m); strategies.push({id:s.id, params:s.params, error:m, runaway:run?run[1]:null});
      issues.push(run ? {v:s.id, kr:`${VN[s.id].kr}: ${run[1]} 단계 반복이 너무 많음 (사실상 만들 수 없는 목표)`, en:`${VN[s.id].en}: step ${run[1]} repeats far too often (practically out of reach)`}
        : {v:s.id, kr:`${VN[s.id].kr}: 진행이 막힘 (${m})`, en:`${VN[s.id].en}: the flow gets stuck (${m})`}); } }
  return {strategies, issues}; }

const api={fromDraft, view, check, gradesFor};
if(typeof module!=='undefined' && module.exports) module.exports=api; else root.POE2GRAPH=api;
})(typeof window!=='undefined' ? window : globalThis);
