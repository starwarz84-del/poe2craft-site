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

/* 유동체 경로(W7, 리버스 13장 사용자 확정 11-13 21:45): 원소 저항(화염·냉기·번개 — 일반·최대치)은 유동체로 바꿀 수 있으니 굴림·공개에서 같은 티어의 다른 원소 저항도 성공으로 보고
   완성 직전에 유동체 한 번(목표 원소가 아닌 줄을 모두 목표 원소로). 같은 옵션 두 줄(탱정 방패 화염 저항 최대치: 하나는 냉기·번개 저항 최대치 훼손 공개 뒤 맹렬한 유동체)은
   이 길이 아니면 공개 풀에 같은 계열이 없어 만들 수 없음. 유동체는 다른 원소 저항을 모두 바꾸니, 목표 원소 저항이 한 원소일 때만(다른 원소 저항이 목표면 쓰지 않음).
   바꾸는 단계 = 목표가 그 옵션 하나(gi, 한 옵션짜리 묶음, 공개). 에센스·합금·산 옵션은 그대로. d.noFlux = 쓰지 않는 후보 */
const RES_RE = /^(Maximum)?(Fire|Cold|Lightning|Chaos)(And(?:Fire|Cold|Lightning|Chaos))?(?:Damage)?Resist(?:ance)?$/;
const resOf = g => { if(!g || (g.f||[]).length!==1) return null; const m=RES_RE.exec(g.f[0]); return m ? {el:m[2], key:(m[1]||'')+'|'+(m[3]||'')} : null; };
const FLUX_TO = {Fire:'Blazing_Flux', Cold:'Chilling_Flux', Lightning:'Crackling_Flux'};
function fluxPlan(d, G, opt){ if(d.noFlux || opt.noFlux) return null; const N=d.nodes||[];
  const gisOf = t => !t ? [] : [t.gi, ...(t.anyOf||[]).map(x=>x.gi), t.reveal?.gi, ...(t.reveal?.anyOf||[]).map(x=>x.gi), t.mark?.gi].filter(x=>x!=null);
  const want = new Set([...(d.start.mods||[]).filter(m=>m.gi!=null && !m.fr).map(m=>m.gi), ...N.flatMap(n=>gisOf(n.target))]);
  const els = new Set([...want].map(gi=>resOf(G[gi])).filter(r=>r && r.el!=='Chaos').map(r=>r.el)); if(els.size!==1) return null;
  const el=[...els][0], cur=FLUX_TO[el];
  if([...want].some(gi=>{ const r=resOf(G[gi]); return r && r.el!==el && r.el!=='Chaos'; })) return null;
  const sibs = gi => { const g=G[gi], r=resOf(g); if(!r || r.el!==el || g.s!=='n' || r.key.endsWith('And'+el)) return null;
    const out=[]; G.forEach((x,i)=>{ if(i===gi || x.s!==g.s || x.g!==g.g) return; const q=resOf(x); if(q && q.key===r.key && q.el!==el && q.el!=='Chaos') out.push(i); }); return out.length ? out : null; };
  const wide = (spec) => { if(!spec) return null; const one = spec.gi!=null ? spec : spec.anyOf?.length===1 ? spec.anyOf[0] : null; if(!one) return null; const sb=sibs(one.gi); if(!sb) return null;
    return {E:one.gi, list:[{gi:one.gi, ...(one.tmax?{tmax:one.tmax}:{})}, ...sb.map(gi=>({gi, ...(one.tmax?{tmax:one.tmax}:{})}))]}; };
  const Es=new Set(); let k=0;
  const nodes = N.map(n=>{ const t=n.target; if(!t || n.do==='essence' || n.do==='base' || t.mark) return n;
    if(['transmute','augment','regal','exalt','chaos'].includes(n.do)){ const w=wide(t); if(!w) return n; Es.add(w.E); k++; const t2={...t, anyOf:w.list}; delete t2.gi; delete t2.tmax; return {...n, target:t2}; }
    if(n.do==='reveal' && t.reveal){ const w=wide(t.reveal); if(!w) return n; Es.add(w.E); k++; return {...n, target:{...t, reveal:{anyOf:w.list}}}; }
    return n; });
  return k ? {nodes, el, cur, Es} : null; }

/* 등록 레시피 틀(W9, 리버스 13장 사용자 확정 11-13 20:28 '비슷한 등록 레시피를 틀로 쓴 후보를 먼저'): 초안이 틀 그래프(tplRewrite 결과)를 갖고 있으면
   새로 만들지 않고 그 그래프를 그대로 씀 — 등급은 opt.grades와 겹치는 것만(겹치는 게 없으면 틀의 등급 그대로) */
function fromTemplate(d, opt){ const g=JSON.parse(JSON.stringify(d.tplGraph)); g.id=d.id; g.recipe=d.id; const ORD=['high','bal','ess'];
  const want=new Set((opt.grades||[]).filter(v=>!opt.top || ORD.indexOf(v)>=ORD.indexOf(opt.top))), keep=g.strategies.filter(s=>want.has(s.id)); if(keep.length && keep.length<g.strategies.length){ const ids=new Set(keep.map(s=>s.id));
    g.strategies=keep; g.versions=(g.versions||[]).filter(v=>ids.has(v.id)); g.finals=(g.finals||[]).filter(f=>ids.has(f.id)); }
  return g; }
/* 틀 다시 쓰기: map = {옛 gi: 새 gi}(같은 클래스 파일). 태그의 gi만 바꾸고 흐름·티어·등급은 그대로, 상자 글의 옵션 이름은 새 옵션 이름으로.
   게임 규칙을 어기는 틀은 {bad}: 쪽·분류(일반·훼손 전용)가 다른 옵션, 에센스·합금·룬 옵션(제작 옵션은 그 커런시만 붙임), 에센스 상자가 만드는 자리,
   군주 징조가 있는 훼손 자리, 아이템 레벨로 붙지 않는 옵션, 같은 계열 두 옵션. 뼈 최소 레벨·제작 옵션 한도·훼손 하나는 시뮬(sim.js 공개 풀·c1 집계)이 그대로 검사 */
function tplRewrite(graph, D, map, o={}){ const G=D.groups, g=JSON.parse(JSON.stringify(graph)), ch=Object.keys(map).map(Number).filter(k=>map[k]!==k);
  const LORD=/Omen_of_the_(Liege|Sovereign|Blackblooded)/, ilvl=o.ilvl||g.ilvl;
  for(const a of ch){ const A=G[a], B=G[map[a]]; if(!A || !B) return {bad:'옵션 없음'};
    if(A.g!==B.g) return {bad:'쪽이 다른 옵션'}; if(A.s!==B.s || !['n','d'].includes(A.s)) return {bad:'제작·증강물 옵션은 바꿀 수 없음'};
    if(!B.t.some(t=>t[0]<=ilvl && (t[1]>0 || B.s==='d'))) return {bad:'아이템 레벨로 붙지 않는 옵션'}; }
  const chTags=new Set(Object.entries(g.tags||{}).filter(([k,t])=>t.gi!=null && ch.includes(t.gi)).map(([k])=>k));
  for(const n of g.nodes||[]){ const js=JSON.stringify({...n, item:undefined, label:undefined, goal:undefined, goalBy:undefined});   /* 아이템 칸(지금 있는 줄 전부)은 그 상자가 만드는 자리가 아님 */ const hit=[...chTags].some(t=>js.includes('"'+t+'"'));
    if(!hit) continue; if(n.act==='essence') return {bad:'에센스·합금 상자가 만드는 자리'}; if(n.act==='reveal' && LORD.test(JSON.stringify(g.nodes.filter(x=>x.act==='desecrate').map(x=>x.omens||[])))) return {bad:'군주 징조 훼손 자리'}; }
  for(const t of Object.values(g.tags||{})) if(t.gi!=null && map[t.gi]!=null) t.gi=map[t.gi];
  /* 같은 계열 두 옵션(바꾼 뒤): 완성 조건의 잎 옵션끼리 */
  const leaf=(k,s=[])=>{ const t=g.tags[k]; if(!t || s.includes(k)) return []; if(t.anyOf) return t.anyOf.flatMap(x=>typeof x==='string'?leaf(x,[...s,k]):x?.gi!=null?[x.gi]:[]); return t.gi!=null?[t.gi]:[]; };
  const req=[]; (function w(c){ if(!c||typeof c!=='object') return; if(c.all) c.all.forEach(w); if(c.any) c.any.forEach(w); if(c.ref) w((g.conds||{})[c.ref]); if(c.has) req.push(c.has); if(c.count) req.push(c.count.tag); })(g.require);
  const one=req.map(k=>leaf(k)).filter(L=>L.length===1).map(L=>L[0]), fam=new Map();
  if(ch.length) for(const gi of new Set(one)){ for(const f of G[gi].f||[]){ if(fam.has(f) && fam.get(f)!==gi) return {bad:'같은 계열 두 옵션'}; fam.set(f, gi); } }
  /* 바꿔 넣은 옵션(또는 같은 계열)이 다른 자리의 묶음 잎에 이미 있으면 그 묶음이 그 옵션으로 채워져 자리 수가 줄어듦(균열 반지: 분열 물리 → 화염 피해 추가인데 '원소 피해 추가 2개' 묶음에 화염이 있음) */
  const newG=new Set(ch.map(a=>map[a])), newF=new Set([...newG].flatMap(gi=>G[gi].f||[]));
  for(const k of req){ const t=g.tags[k]; if(!t?.anyOf) continue; if(leaf(k).some(gi=>newG.has(gi) || (G[gi].f||[]).some(f=>newF.has(f)))) return {bad:'바꾼 옵션이 다른 자리 묶음에 들어 있음'}; }
  /* 상자 글: 옛 옵션 이름 → 새 이름(아이템 칸 줄은 태그로 다시 그려지지만 목표·이름표 글은 글자 그대로라) */
  const names=o.names||{}, rep=[];
  const strip={kr:s=>String(s||'').replace(/\s*\((분열|훼손|에센스|합금)[^)]*\)\s*$/,'').replace(/\s*\d+(~\d+)?티어$/,'').replace(/^(접두|접미)\s+/,'').trim(),
    en:s=>String(s||'').replace(/\s*\((fractured|desecrated|essence|alloy)[^)]*\)\s*$/i,'').replace(/^T\d+([–-]\d+)?\s+/,'').replace(/\s+(prefix|suffix)$/i,'').trim()};
  const seenOld=new Set();
  for(const n of graph.nodes||[]) for(const l of n.item||[]){ if(!l.tags || l.tags.length!==1) continue; const t=graph.tags?.[l.tags[0]]; if(t?.gi==null || !ch.includes(t.gi) || !names[map[t.gi]]) continue;
    const kr=strip.kr(l.kr), en=strip.en(l.en), key=kr+'|'+en; if(seenOld.has(key) || kr.length<2) continue; seenOld.add(key); const to=names[map[t.gi]]; rep.push({kr, en, to:{kr:to.kr, en:String(to.en||'').replace(/^to\s+/i,'')}}); }
  /* 옵션 이름(수치 뺀 것)과 끝 동사(추가·증가·감소)를 뺀 짧은 이름도(이름표가 '공격 시 물리 피해 1티어'처럼 줄여 쓰는 경우) */
  const clean=t=>String(t||'').split('\n').join(' / ').replace(/[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\)%?/g,'').replace(/[+\-]?\d[\d.]*%?/g,'').replace(/\s*~\s*/g,' ').replace(/\s+/g,' ').trim();
  const tail=t=>t.replace(/\s+(추가|증가|감소)$/,'').trim();
  for(const a of ch){ const A=G[a], B=G[map[a]]; if(!A || !B) continue; const ok=clean(A.t[0][4]), nk=clean(B.t[0][4]), oe=clean(A.t[0][5]), ne=clean(B.t[0][5]);
    if(ok.length>=4) rep.push({kr:ok, en:oe, to:{kr:nk, en:ne}}); if(tail(ok)!==ok && tail(ok).length>=4) rep.push({kr:tail(ok), en:'', to:{kr:tail(nk), en:ne}}); }
  rep.sort((a,b)=>b.kr.length-a.kr.length);
  /* 아이템 칸 줄의 글(태그로 다시 그리지만 티어 찾기에 씀)은 같은 티어의 새 옵션 글로 */
  for(const n of g.nodes||[]) for(const l of n.item||[]){ if(!l.tags || l.tags.length!==1) continue; const t0=graph.tags?.[l.tags[0]]; if(t0?.gi==null || !ch.includes(t0.gi)) continue;
    const A=G[t0.gi], B=G[map[t0.gi]], base=String(l.kr||'').replace(/\s*\([^)]*\)\s*$/,''), suf=String(l.kr||'').slice(base.length), sufE=(String(l.en||'').match(/\s*\([^)]*\)\s*$/)||[''])[0];
    const i=A.t.findIndex(x=>(x[4]||'').replace(/\n/g,' / ')===base); if(i<0) continue; const x=B.t[Math.min(i, B.t.length-1)]; l.kr=(x[4]||'').replace(/\n/g,' / ')+suf; l.en=(x[5]||'').replace(/\n/g,' / ')+sufE; l._tpl=1; }
  /* 영문 상자 글은 등록 그래프가 줄여 쓴 이름('crit chance', 'flat armour')이라 DB 이름으로는 안 맞음(W10) → 같은 규칙으로 줄인 이름을 옛·새 옵션 둘 다 만들어 짝으로 바꿈.
     한글이 바뀐 글에서만(그 글이 바꾼 옵션을 가리킨다는 표시), 대소문자 무시·단어 경계, 긴 것부터 */
  const enForms=t=>{ const s0=clean(t).replace(/^(\+|-|%|\s)+/,'').replace(/^Adds\s+to\s+/i,'Adds ').trim(), out=[];
    const core=s0.replace(/^(Adds|to|increased|reduced|additional|more|less)\s+/i,'').replace(/^Level of all (.+) Skills$/i,'$1 skills').replace(/^all\s+/i,'').trim();
    const nomax=core.replace(/^maximum\s+/i,''), abbr=nomax.replace(/Critical Hit/i,'crit').replace(/\s+Rating$/i,'').replace(/Resistances?$/i,m=>/s$/.test(m)?'resistances':'resistance');
    const noun=abbr.replace(/\s+Damage$/i,'').replace(/\s+skills$/i,' skills');
    const atk=core.replace(/\s+Damage(\s+to\s+(Attacks|Spells))?$/i,''), lvl=(core.match(/^(.+) skills$/i)||[])[1];
    [s0.replace(/^to\s+/i,''), core, nomax, abbr, noun, abbr.replace(/resistances?$/i,'res'), nomax.replace(/Critical Hit/i,'critical'), abbr.replace(/Energy Shield/i,'ES'),
     /^Adds\b/i.test(s0) ? atk+' flat' : '', /^Adds\b/i.test(s0) ? 'flat '+atk : '', /^all\s/i.test(s0.replace(/^to\s+/i,'')) ? 'all res' : '', lvl ? lvl+' skill levels' : '',
     /^Rarity of Items found$/i.test(core) ? 'item rarity' : '', /\s+for Spells$/i.test(abbr) ? 'Spell '+abbr.replace(/\s+for Spells$/i,'') : '', /\s+Damage with Attacks$/i.test(core) ? 'attack '+core.replace(/\s+Damage with Attacks$/i,'') : ''].forEach((f,i)=>{ out[i]=f; });
    /* 새 옵션 쪽에 그 형태가 없으면(힘 같은 짧은 이름) 가장 짧은 이름으로 */ return out; };
  const enRep=[]; for(const a of ch){ const A=G[a], B=G[map[a]]; if(!A || !B) continue; const fa=enForms((A.t[0]||[])[5]), fb=enForms((B.t[0]||[])[5]);
    fa.forEach((f,i)=>{ if(f && f.length>=4 && !enRep.some(r=>r.from.toLowerCase()===f.toLowerCase())) enRep.push({from:f, to:fb[i]||fb[4]||fb[1]||''}); }); }
  enRep.sort((a,b)=>b.from.length-a.from.length);
  const reEsc=t=>t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'), capLike=(src,to)=>/^[A-Z]/.test(src) ? to.charAt(0).toUpperCase()+to.slice(1) : /^[a-z]/.test(src) && !/^[A-Z]{2}/.test(to) ? to.charAt(0).toLowerCase()+to.slice(1) : to;
  const enFix=e=>{ let out=e; for(const r of enRep){ if(!r.to) continue; const re=new RegExp('(^|[^A-Za-z])('+reEsc(r.from)+')(?![A-Za-z])','gi'); if(re.test(out)){ out=out.replace(re,(m,p,w)=>p+'\u0000'+capLike(w, r.to)+'\u0001'); } }
    return out.replace(/\u0000|\u0001/g,''); };
  /* 한글 조사: 바꾼 이름 뒤 이/가·을/를·은/는·와/과·으로/로를 새 이름 받침에 맞춤('힘가 분열되면' → '힘이') */
  const jong=w=>{ const c=(w||'').trim().slice(-1).charCodeAt(0); return c>=0xAC00 && c<=0xD7A3 ? (c-0xAC00)%28 : /[0-9)%]$/.test(w) ? 1 : 0; };
  const J={이:['이','가'],가:['이','가'],을:['을','를'],를:['을','를'],은:['은','는'],는:['은','는'],과:['과','와'],와:['과','와']};
  const krFix=(k, r)=>k.split(r.kr).map((part,i)=>{ if(!i) return part; const m=part.match(/^(으로|로|이|가|을|를|은|는|과|와)(?![가-힣])/); if(!m) return part; const j=jong(r.to.kr), x=m[1];
      const y = x==='으로'||x==='로' ? (j && j!==8 ? '으로' : '로') : J[x][j?0:1]; return y+part.slice(x.length); }).join(r.to.kr);
  const fix=x=>{ if(Array.isArray(x)) return x.forEach(fix); if(!x || typeof x!=='object') return; if(typeof x.kr==='string' && typeof x.en==='string'){ const k0=x.kr, e0=x.en; for(const r of rep){ if(x.kr.includes(r.kr)) x.kr=krFix(x.kr, r); if(r.en.length>=3 && x.en.includes(r.en)) x.en=x.en.split(r.en).join(r.to.en); }
      if(x.kr!==k0 && x.en===e0) x.en=enFix(x.en); }
    for(const [k,v] of Object.entries(x)) if(k!=='tags' && v && typeof v==='object') fix(v); };
  const fixN=n=>{ for(const [k,v] of Object.entries(n)) if(k!=='item' && v && typeof v==='object') fix(v); };
  if(rep.length){ (g.nodes||[]).forEach(fixN); for(const t of Object.values(g.tags||{})) if(t.label) fix(t.label); fix(g.versions); }
  if(o.base) g.base=o.base; if(o.ilvl) g.ilvl=o.ilvl; g.tplOf=graph.id; g.note='등록 레시피 '+graph.id+' 틀로 만든 리버스 초안 플로우차트';
  return {g, changed:ch.length}; }

function fromDraft(d, D, opt={}){ if(d.tplGraph) return fromTemplate(d, opt);
  const G=D.groups, FX=fluxPlan(d, G, opt), N=FX ? FX.nodes : d.nodes, byId={}; N.forEach(n=>byId[n.id]=n);
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
  /* 결과 등급 = 사용자가 고른 필수 티어(리버스 13장 사용자 확정 11-14 04:17, W11): opt.top(1티어 → 하이엔드, 1~2티어 → 밸런스, 1~4티어 → 에센셜)이 있으면
     그 등급이 맨 위 — 위 등급은 만들지 않고, 그 등급의 티어는 고른 티어 그대로(넓히지 않음), 아래 등급만 C17로 넓힘 */
  const ORD=['high','bal','ess'], top = ORD.includes(opt.top) ? opt.top : null;
  let grades = opt.grades || gradesFor(d.difficulty||2);
  if(top){ grades = grades.filter(v=>ORD.indexOf(v)>=ORD.indexOf(top)); if(!grades.includes(top)) grades=[top, ...grades]; grades.sort((x,y)=>ORD.indexOf(x)-ORD.indexOf(y)); }
  /* 등급별 티어(정책 10장 C17-1, 리버스 13장 사용자 확정 11-13 20:28, W5): 반복으로 찾는 자리만 — 하이엔드 = 사용자가 고른 티어, 밸런스 = 그 티어와 1~2티어 중 넓은 쪽,
     에센셜 = 1~4티어 중 넓은 쪽. '1티어' = 아이템 레벨로 붙을 수 있는 가장 좋은 티어(lo). 예전엔 등급 순번만큼(+0/+1/+2) 넓힘 */
  const loTier = gi => Math.max(1, G[gi].t.findIndex(t=>t[0]<=d.ilvl)+1), WIDE = {high:0, bal:1, ess:3};
  const P = {}; grades.forEach(v=>{ const p={}; for(const gi of loopGi){ const t0=tmaxOf[gi]||1; p['t'+gi] = String(Math.min(G[gi].t.length, Math.max(t0, loTier(gi) + (v===top ? 0 : WIDE[v]??0)))); } P[v]=p; });
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
  const pickGi = list => { if(FX && FX.Es.has(list[0]?.gi)) return list[0].gi; const have=new Set(cur.map(l=>l.rep).filter(Boolean)); return (list.find(x=>!have.has(tagOf(x.gi)))||list[0]).gi; };
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
    /* 자리 = 목표 옵션 그룹 쪽이 먼저(W11, V2-하이엔드 셉터 9번: 좌측 결정화 + 에센스가 접미 합금 자리를 '접두 옵션'으로 씀) — 결정화·말소·소멸 징조의 좌측·우측은 지우는 쪽이라 목표 쪽이 없을 때만 */
    const tgi = t.gi ?? t.anyOf?.[0]?.gi ?? t.reveal?.gi ?? t.reveal?.anyOf?.[0]?.gi;
    const sd = t.side || (t.junk && typeof t.junk==='string' ? t.junk : null) || (tgi!=null && G[tgi] ? G[tgi].g : null) || omSide(n.omens, /Exaltation|Coronation|Necromancy|Crystallisation|Erasure|Annulment/) || t.unrev || null;
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
  const firstChaos = (()=>{ if(!(d.start.mods||[]).some(m=>m.fr)) return null; const m=N.find(x=>!['base','note','manual','socket','quality'].includes(x.do) && !x.fallbackFor && !x.branch);   /* 룬 장착·퀄리티 단계는 건너뛰고 봄(W8: SL 장갑은 세를의 승리 룬 단계가 먼저라 첫 카오스를 못 찾아, 잃으면 잡옵이 쌓인 채 카오스로 돌아가 끝나지 않았음) */ return m && m.do==='chaos' && m.fail?.goto==='self' ? m.id : null; })();
  /* 첫 카오스 옵션을 뒤에서 잃으면(W8, MazBro 셉터 frside 후보): 그사이에 같은 묶음을 노리는 엑잘 단계가 있으면 처음부터(정리 → 카오스) 대신 그 엑잘로 다시 붙임 — 다른 옵션은 그대로 */
  const reEx = (maker, pos) => { if(maker!==firstChaos || pos==null) return null; const i0=N.findIndex(x=>x.id===maker), tg=targetTag(byId[maker]?.target); if(!tg) return null;
    const X=N.slice(i0+1, pos).find(x=>x.do==='exalt' && !x.fallbackFor && !x.branch && targetTag(x.target)===tg); return X ? X.id : null; };
  const cleanTo = (maker, pos) => { if(maker!==firstChaos) return maker; const rx=reEx(maker, pos); if(rx) return rx; const id='cl'+maker;
    if(!extra.some(x=>x.id===id)) extra.push({id, kind:'cleanup', group:'main', keep:[], maxJunk:1, label:K('소멸의 오브 사용','Use an Orb of Annulment'), goal:K('잡옵 정리','Clear the junk'), target:K('분열 옵션 + 잡옵 1개만 남기고 다시 카오스','Keep the fracture and one junk line, then Chaos again'), edges:[{to:maker}], _row:2, _col:2});   /* 칸 2(W11: 칸 3은 그림 오른쪽 밖으로 잘림) */
    return id; };
  /* 자리를 늘리는 옵션(경멸: +1 접미 허용)을 일부러 지운 뒤(dropGi)에 그쪽 옵션을 잃으면 그쪽 자리가 모자라 만든 단계로 돌아가도 다시 못 붙임 → 새 베이스(W7, LilBotQ 에메랄드가 끝나지 않던 원인) */
  const slotDrop = N.findIndex(n=>{ const g=n.target?.dropGi; return g!=null && (n.target?.slots || N.some(x=>x.target?.gi===g && x.target?.slots)); });
  const slotSide = slotDrop>=0 ? (()=>{ const g=N[slotDrop].target.dropGi, mk=N.find(x=>x.target?.gi===g && x.target?.slots); return mk ? Object.keys(mk.target.slots)[0] : null; })() : null;
  const sideOfTag = tg => { const t=tags[tg]; if(!t) return null; const gi = t.gi ?? tags[t.anyOf?.[0]]?.gi; return gi!=null ? G[gi].g : null; };
  function lostEdges(n, keep, pos){ // a kept line removed by this step → back to the step that made it
    const at = pos ?? N.indexOf(n), late = slotSide && slotDrop>=0 && at>slotDrop;
    return keep.filter(k=>k.maker!==n.id).map(k=>({if:{removed:k.tag}, to: late && sideOfTag(k.tag)===slotSide && N.findIndex(x=>x.id===k.maker)<slotDrop ? 'h1' : cleanTo(k.maker, at), res:'fail', lost:k.tag, hide:true})); }
  let vN=0;
  /* 필수 훼손 반복 — 징표 방법(W7, 리버스 13장 사용자 확정 11-13 20:22: 빛의 징조로 다시 공개하거나 아스트리드의 창의성 룬으로 제작 옵션 2개):
     공개가 빗나가면 빛의 징조 + 소멸 대신 그쪽 결정화의 징조 + 심연의 에센스(그쪽 옵션 하나를 지우고 심연 군주의 징표) → 같은 뼈로 징표 자리 훼손 → 다시 공개(징표 자리는 한 티어 높게).
     지운 옵션이 좋은 옵션이면 그 옵션을 만든 단계로. 징표도 제작 옵션이라 이미 제작 옵션이 있으면 아스트리드의 창의성(룬 소켓 필요)이 있어야 하고 제작 옵션이 2개면 못 씀(5장 C1).
     반대쪽이 꽉 찼을 때만(그래야 징표가 지운 쪽에 붙음 — 반대쪽에 자리가 있으면 접두·접미 반반). d.desLoop==='mark' 후보 */
  function markLoop(n, F, keep, r){ if(d.desLoop!=='mark' || n.do!=='reveal' || !(F.via?.omens||[]).includes('Omen_of_Light')) return null;
    const sd=n.target?.side, oth = sd==='p' ? 's' : 'p'; if(!sd) return null;
    const mkGi=G.findIndex(g=>g.s==='e' && g.g===sd && /Abyssal Lord/.test(g.t[0]?.[5]||'')); if(mkGi<0) return null;
    const capO=(d.cap?.[oth]) ?? (3+((oth==='p'?base.pd:base.sd)||0)); if(cur.filter(l=>l.s===oth).length < capO) return null;
    const crafted=cur.filter(l=>l.m==='c').length, hasA=/Astrid/.test(JSON.stringify(d.start.runes||[])) || N.slice(0, N.indexOf(n)).some(x=>/Astrid/.test(x.target?.rune?.en||''));
    if(crafted>=2 || (crafted===1 && !hasA && !(d.sockets>0))) return null;
    const bone=byId[F.goto]?.cur; if(!bone) return null;
    const id='mk'+n.id, CR = sd==='p' ? 'Omen_of_Sinistral_Crystallisation' : 'Omen_of_Dextral_Crystallisation', le=lostEdges({id}, keep, N.indexOf(n));
    if(crafted===1 && !hasA) extra.push({id:id+'a', kind:'act', group:'main', act:'rune', rune:{kr:'아스트리드의 창의성', en:'Astrid’s Creativity'}, label:LABEL.rune, goal:K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),
      showText:[K('제작 옵션이 이미 있어 징표(제작 옵션)를 붙이려면 필요. 제작이 끝나면 원하는 룬으로 교체','A crafted line is already there, so the Mark (also crafted) needs it. Swap it for the rune you want once crafting is done')],
      skipIf:{rune:'Astrid'}, skipTo:id, skipHide:true, skipNote:K('이미 장착돼 있으면 건너뜀','Skipped when already socketed'), edges:[{to:id}], _row:r, _col:2});
    extra.push({id, kind:'act', group:'main', act:'essence', cur:'Essence_of_the_Abyss', omens:[CR], ess:tagOf(mkGi), mark:true, label:LABEL.essence, goal:K(`${sideWord(sd).kr} 징표`, `${sideWord(sd).en} Mark`),
      showText:[K(`${cn(CR).kr}: 빗나간 ${sideWord(sd).kr} 하나를 지우고 심연 군주의 징표 (빛의 징조 대신)`, `${cn(CR).en}: removes a ${sideWord(sd).en.toLowerCase()} (the miss, hopefully) and adds the Mark (instead of Omen of Light)`)],
      edges:[...le, {to:id+'b'}], _row:r, _col:crafted===1 && !hasA ? 3 : 2});
    extra.push({id:id+'b', kind:'act', group:'main', act:'desecrate', cur:bone, fromMark:true, label:LABEL.desecrate, goal:K('징표 자리 훼손','Desecrate the Mark'),
      showText:[K('징표 자리가 미공개 훼손 옵션으로 (한 티어 높게)','The Mark becomes an unrevealed desecration (one tier higher)')], edges:[{to:n.id}], _row:r+0.5, _col:2});
    return crafted===1 && !hasA ? id+'a' : id; }
  function failPath(n, F, keep, r){ if(!F) return null; const go = F.goto==='self' ? n.id : (F.goto==='restart' || byId[F.goto]?.do==='base') ? 'h1' : F.goto;
    if(!F.via) return go;
    const mk = markLoop(n, F, keep, r); if(mk) return mk;
    const id='v'+(++vN)+n.id, v=F.via, a = v.cur==='Orb_of_Annulment' ? 'annul' : /Bone|Jawbone|Rib|Collarbone|Cranium/.test(v.cur||'') ? 'desecrate' : 'annul';
    const lostTo = F.lost ? (byId[F.lost]?.do==='base' ? 'h1' : cleanTo(F.lost, N.indexOf(n))) : null, lostTag = F.lost ? (keep.find(k=>k.maker===F.lost)?.tag || targetTag(byId[F.lost]?.target)) : null;
    /* 지운 옵션 확인 순서(W5): 낱개 옵션(산 베이스 옵션 등) 먼저, 그 단계가 노린 옵션은 뒤 — 묶음 태그(anyOf)가 산 옵션을 품으면(K39 희귀도 반지: 산 희귀도 접두가 묶음에 들어감)
       그 옵션이 지워져도 '노린 옵션이 지워짐'으로 읽혀 새 베이스 대신 엑잘로 돌아가고 완성품에 산 옵션이 없었음(33%) */
    const le=lostEdges({id}, keep, N.indexOf(n)).filter(e=>e.if.removed!==lostTag), lt = lostTo && lostTag ? [{if:{removed:lostTag}, to:lostTo, res:'fail', lost:lostTag}] : [];
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
    /* 잡옵 상자 본문(W11, V2-하이엔드 8번 본문 빈칸): 목표 줄이 없으니 '잡옵 1개 — 나오는 대로' */
    if(t.junk && !o.show && ['exalt','chaos','regal','augment','transmute'].includes(a)){ const w=sideWord(typeof t.junk==='string' ? t.junk : omSide(n.omens,/Exaltation|Coronation/)); o.target=K(`${w.kr} 잡옵 1개 — 나오는 대로`.trim(), `${w.en ? w.en+' ' : ''}junk line — whatever comes`.trim()); }
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
    const Fx = n.fail || n.compromise?.fail; if(okIf && retry0(n) && (a==='reveal' || (a!=='chaos' && !(fb[n.id]||[]).some(x=>x.do!=='note') && !Fx?.via))) o.edges.push({if:{famBlock:tg, ...(a==='reveal' && n.pool ? {left:n.pool} : {})}, to:'h1', res:'fail', hide:true});   // nothing on the way back can clear the blocking line   // another line already holds the wanted family: a new base
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
    /* 공개할 훼손 옵션이 없는데 공개 목표가 이미 채워짐(앞 단계 카오스·엑잘이 그 쪽 목표 옵션을 다 붙임) → 공개도 건너뜀. 훼손 상자가 목표 충족으로 공개 상자로 넘기면 공개가 빗나감 → 빛의 소멸 → 훼손 건너뜀으로 끝없이 돌았음(RV12 2026-11-14, 마나·희귀도 반지 에센셜 'd6 반복') */
    else if(a==='reveal' && !t.fromMark){ const rt=targetTag(t); if(rt){ o.skipIf={all:[{unrev:false}, n.pool ? {count:{tag:rt, min:n.pool}} : {has:rt}]}; o.skipTo=nxt; o.skipNote=K('이미 목표 옵션 있음','Target modifier already there'); } }
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
    else if(a==='reveal'){ const i=cur.findIndex(l=>l.m==='u'); const gi=t.reveal?.gi ?? (t.reveal?.anyOf ? pickGi(t.reveal.anyOf) : null); if(i>=0) cur.splice(i,1, gi!=null ? lineOf(gi,'d',null,targetTag(t)) : {s:cur[i].s, kr:'훼손 옵션 (결과 그대로)', en:'Desecrated (as it comes)', m:'d'}); }
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
  const baseLabel = d.start.rar==='magic' ? K('매직 베이스 구입','Buy a magic base') : d.start.rar==='rare' && !(d.start.mods||[]).some(m=>m.fr) ? K('희귀 베이스 구입','Buy a rare base') : (d.start.mods||[]).some(m=>m.fr) ? K('분열 베이스 구입','Buy a fractured base') : K('베이스 구입','Buy a base');
  /* 분열 과정(W6, 리버스 13장 사용자 확정 11-13 20:16·22:37): 분열 옵션은 등록 레시피처럼 준비 구역에서 만듦 — 분열 대상 옵션 + 반대쪽 잡옵이 붙은 매직 베이스 구입 →
     제왕의 오브(옵션 3개) → 보존된 뼈(미공개 훼손, 분열되지 않음 → 옵션 4개) → 분열의 오브(공개된 옵션 3개 중 하나, 1/3) → 소멸의 오브로 분열 + 옵션 1개.
     빗나가면 규칙 G: 분열 아이템은 난이도가 늘 어려움 이상(평균 베이스 3개)이라 새 베이스로 처음부터. 비용 = 베이스 값 제외, 이 과정의 커런시는 포함 */
  const FP = d.fracPrep && (d.start.mods||[]).filter(m=>m.fr).length===1 ? d.fracPrep : null;
  let prepNodes = [], PRE = 0;
  if(FP){ const F=(d.start.mods||[]).find(m=>m.fr), T=tagOf(F.gi), sd=G[F.gi].g, oth=sd==='p'?'s':'p', boneK=cn(FP.bone);
    const lT = lineOf(F.gi,'n'), lF = lineOf(F.gi,'f'), it0 = FP.ess ? [J('p'), J('s')] : [lT, J(oth)], it1 = FP.ess ? [J('p'), J('s'), lineOf(F.gi,'n',K('에센스','essence'))] : [lT, J(oth), J('x')], it2=[...it1, UN('x')];
    /* 분열 옵션이 에센스 옵션이면(SaVeQ 집중구 '상위 주문의 에센스' 분열) 잡옵 2개 매직 베이스 → 그 에센스(매직 → 희귀 + 그 옵션)가 제왕 자리 */
    const up = FP.ess ? {id:'hr', kind:'act', group:'prep', pos:[0,1], act:'essence', cur:FP.ess, ess:T, label:LABEL.essence, goal:K('희귀 + 분열할 옵션 (에센스)','Rare + the line to fracture (essence)'), edges:[{to:'hb'}], item:it1}
      : {id:'hr', kind:'act', group:'prep', pos:[0,1], act:'regal', cur:'Regal_Orb', label:LABEL.regal, goal:K('세 번째 옵션 — 희귀로','Third line: to rare'), showText:[K('나오는 대로, 분열 조건 옵션 4개를 채우는 잡옵','As it comes: a junk line toward the four the fracture needs')], edges:[{to:'hb'}], item:it1};
    prepNodes = [
      {id:'h1', kind:'base', group:'prep', pos:[0,0], next:'hr', start:{rar:'magic', mods: FP.ess ? [{junk:'p'}, {junk:'s'}] : [T, {junk:oth}], ...(d.start.quality?{quality:d.start.quality}:{})}, label:K('매직 베이스 구입','Buy a magic base'),
        note: FP.ess ? K('옵션 2개 매직 베이스','A magic base with two lines') : K('분열할 옵션이 붙은 매직 베이스(옵션 2개)','A magic base with the line to fracture (two lines)'), item:it0},
      up,
      {id:'hb', kind:'act', group:'prep', pos:[0,2], act:'desecrate', cur:FP.bone, label:LABEL.desecrate, goal:K('네 번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth option (desecrated): the fracture needs four'),
        showText:[K(`${boneK.kr}: 훼손 옵션 (미공개, 분열되지 않음)`,`${boneK.en}: desecration (unrevealed, cannot fracture)`)], edges:[{to:'hf'}], item:it2},
      {id:'hf', kind:'act', group:'prep', pos:[0,3], act:'fracture', cur:'Fracturing_Orb', label:K('분열','Fracture'), goal:K('분열 (공개된 옵션 3개 중 하나)','Fracture (one of the three revealed options)'),
        showText:[K(`성공: ${lT.kr} 분열`, `Success: ${lT.en} fractures`)], ask:K('어느 옵션이 분열?','Which option fractured?'),
        edges:[{if:{fractured:T}, to:'hc', res:'ok', label:K('분열 성공','Fractured')}, {to:'hx', res:'fail', label:K('다른 옵션 분열','Another line fractured')}], item: FP.ess ? [J('p'), J('s'), lF, UN('x')] : [lF, J(oth), J('x'), UN('x')]},
      {id:'hx', kind:'exit', group:'prep', pos:[1,3], simTo:'h1', variant:'fail', label:K('다른 옵션 분열 — 새 베이스','Another line fractured: new base'), note:K('새 베이스로 처음부터','Start over on a new base')},
      {id:'hc', kind:'cleanup', group:'prep', pos:[0,4], keep:[], maxJunk:1, label:K('소멸의 오브 사용','Use an Orb of Annulment'), goal:K('소멸의 오브 사용','Use an Orb of Annulment'), target:K('분열 + 옵션 1개만 남기기','Keep only the fracture + one option'), edges:[{to:'hu'}], item:[lF, J('x')]},
      /* 남은 옵션이 준비용 미공개 훼손이면(약 1/3) 지우고 엑잘로 잡옵 하나 — 그대로 두면 본 작업의 훼손·공개가 이 줄에 걸림(시한 차유라 목걸이 완성 68%) */
      {id:'hu', kind:'act', group:'prep', pos:[0,5], act:'annul', cur:'Orb_of_Annulment', skipIf:{unrev:false}, skipTo:'ms', skipNote:K('남은 옵션이 일반 옵션','The line left is a regular one'), label:K('소멸의 오브 사용','Use an Orb of Annulment'), goal:K('남은 미공개 훼손 옵션 지우기','Remove the leftover unrevealed desecration'), target:K('남은 옵션이 미공개 훼손이면 지우기 (일반 옵션이면 건너뜀)','If the line left is the unrevealed desecration, remove it (skip otherwise)'), edges:[{to:'he'}], item:[lF]},
      {id:'he', kind:'act', group:'prep', pos:[0,6], act:'exalt', cur:'Exalted_Orb', label:LABEL.exalt, goal:K('잡옵 1개 다시 붙이기','Add one junk line back'), target:K('잡옵 1개 다시 붙이기 (나오는 대로)','Add one junk line back (as it comes)'), showText:[K('나오는 대로','As it comes')], edges:[{to:'ms'}], item:[lF, J('x')]}];
    PRE = 7; all.forEach(o=>{ o.pos=[o.pos[0], o.pos[1]+PRE]; }); }
  const nodes=[...(FP ? prepNodes : [{id:'h1', kind:'base', group:'prep', pos:[0,0], next:'ms', start:{rar:d.start.rar||'normal', mods:(d.start.mods||[]).map(m=> m.junk ? {junk:m.junk} : m.unrev ? {unrev:m.unrev} : (m.fr ? {tag:tagOf(m.gi), fr:true} : tagOf(m.gi)))}, label:baseLabel, item:startItem}]),
    {id:'ms', kind:'mark', group:'main', pos:[0,PRE+0.6], next:first, label:K('아이템 제작 시작','Item crafting starts'), item:startItem},
    ...all, {id:'ok', kind:'done', group:'main', pos:[0,row+PRE+(FX?1:0)], label:K('완성','Finished')}];
  /* 유동체 단계(W7, fluxPlan): 완성으로 가는 선을 모두 유동체 상자로 — 목표 원소 줄이 이미 다 있으면 건너뜀. 완성 칸·완성 조건은 목표 원소 옵션 그대로 */
  if(FX){ const isW = k => { const L=tags[k]?.anyOf; return !!L && L.some(x=>FX.Es.has(tags[x]?.gi)) && L.every(x=>{ const r=resOf(G[tags[x]?.gi]); return r && r.el!=='Chaos'; }); };
    cur.forEach(l=>{ if(l.tags && isW(l.tags[0]) && l.rep && FX.Es.has(tags[l.rep]?.gi)) l.tags=[l.rep]; });
    const need = [...FX.Es].map(gi=>({gi, n:Math.max(1, cur.filter(l=>l.tags?.[0]===tagOf(gi)).length)}));
    nodes.forEach(n=>{ (n.edges||[]).forEach(e=>{ if(e.to==='ok') e.to='fx'; }); if(n.skipTo==='ok') n.skipTo='fx'; if(n.next==='ok') n.next='fx'; });
    const fc=cn(FX.cur), el=K({Fire:'화염',Cold:'냉기',Lightning:'번개'}[FX.el], FX.el);
    nodes.splice(nodes.length-1, 0, {id:'fx', kind:'act', group:'main', pos:[0,row+PRE], act:'flux', cur:FX.cur, label:K('유동체','Flux'), goal:K(`다른 원소 저항 → ${el.kr} 저항`, `Other elements → ${el.en}`),
      showText:[K(`${fc.kr}: 다른 원소 저항 옵션을 같은 티어의 ${el.kr} 저항으로`, `${fc.en}: other elemental resistances become ${el.en} at the same tier`)],
      skipIf: need.length===1 ? {count:{tag:tagOf(need[0].gi), min:need[0].n}} : {all:need.map(x=>({count:{tag:tagOf(x.gi), min:x.n}}))}, skipTo:'ok', skipNote:K(`이미 ${el.kr} 저항`, `Already ${el.en}`),
      edges:[{to:'ok', res:'ok'}], item:cur.map(x=>({...x}))});
    /* 유동체 전 아이템 칸(W8, W7 넘김: 탱정 방패): 넓힌 묶음으로 만든 줄은 실제 상태대로 다른 원소 이름('냉기·번개 저항 최대치'), 유동체 상자부터 목표 원소. 성공 회차 옵션(rep)은 그대로 */
    { const EK={Fire:'화염',Cold:'냉기',Lightning:'번개'}, ek=Object.keys(EK).filter(e=>e!==FX.el);
      nodes.forEach(n=>{ if(n.id==='fx' || n.id==='ok') return; (n.item||[]).forEach(l=>{ if(!l.tags || !isW(l.tags[0]) || !FX.Es.has(tags[l.rep]?.gi) || l.fxPre) return;
        l.kr=String(l.kr||'').split(EK[FX.el]).join(ek.map(e=>EK[e]).join('·')); l.en=String(l.en||'').split(FX.el).join(ek.join('/')); l.fxPre=true; }); }); } }
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
    if(ws.length && v!==top) parts.push(K(`반복으로 찾는 옵션 ${ws.length}개를 넓은 티어로`, `${ws.length} looped line(s) at wider tiers`)); else parts.push(K('고른 티어 그대로','The tiers you picked'));
    if(p.cmp==='settle' || p.cmpl==='settle') parts.push(p.cmp==='settle' ? K('빗나가면 결과 그대로','keep a miss as it comes') : K('마지막 옵션은 결과 그대로','keep the last line as it comes'));
    return K(parts.map(x=>x.kr).join(' · '), parts.map(x=>x.en).join(' · ')); };
  /* 규칙 K(2026-11-13 W4): 빗나가도 그대로 두는 등급(cmp settle)에서 그 갈림길이 만든 자리는 완성 카드에 '랜덤 옵션' — 목표 옵션이 늘 붙는 것처럼 보이지 않게 */
  const settleLine = (v, l) => l.tags && [l.tags[0], l.rep, l._k].some(t=>t && settleOf(v, t));
  /* 완성 카드 줄 중복 빼기(W5, MazBro 시전자 목걸이: 공개 성공·빗나감 갈래가 같은 묶음 옵션을 둘 다 아이템 칸에 넣어 마나 최대치가 두 번 — 접두 4개): 같은 옵션 태그 줄은 붙여 넣은 줄 수(dupGi)까지 */
  /* 티어가 하나뿐인 제작 옵션(합금 등, W11 V2-하이엔드 '합금 줄 S1 → S'): 완성 카드에 티어를 적지 않음 */
  const oneTier = k => { const gi=tags[k]?.gi; return gi!=null && G[gi] && !['n','d'].includes(G[gi].s) && (G[gi].t||[]).length<=1; };
  const curF = (()=>{ const seen={}; return cur.filter(l=>{ const k=l.rep && l.rep!==l.tags?.[0] ? l.rep : null; const gi=k ? tags[k]?.gi : null; if(gi==null) return true; seen[k]=(seen[k]||0)+1; return seen[k] <= Math.max(1, d.dupGi?.[gi]||0); }); })();
  const finals = grades.map(v=>({id:v, kr:VN[v].kr+' 옵션', en:VN[v].en, lines: curF.map(l=>{ if(!l.tags) return l; const k = chainN[l.tags[0]] && l.rep && !(tags[l.tags[0]]?.shown?.length && tags[l.tags[0]].anyOf?.length>(tags[l.tags[0]].shown.length)) ? l.rep : l.tags[0];   /* 묶음에 붙여 넣은 옵션 말고 다른 유효 옵션(칩)이 있으면 묶음 태그 그대로 — 완성 카드가 성공 회차 옵션 + '대신 …도 성공으로 침' 꿀팁을 그림(W11, V2-하이엔드 접미 묶음 꿀팁 빠짐) */ return {...l, _k:k}; }).map(l=> settleLine(v, l) ? {side:l.s, random:true, ...(l.m==='d'?{des:true}:{})} : l.tags ? {tag:l._k, tmax: oneTier(l._k) ? undefined : tags[l._k].tmax && String(tags[l._k].tmax)[0]==='$' ? +P[v][String(tags[l._k].tmax).slice(1)] : tags[l._k].tmax, ...(l.m==='f'?{fr:true}:{}), ...(l.m==='d'?{des:true}:{})} : l.m==='r' ? null : {side:l.s, random:true, ...(l.m==='d'?{des:true}:{})}).filter(Boolean)}));
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
function view(graph, D){ const tv={}; for(const [k,t] of Object.entries(graph.tags||{})){ if(t.anyOf){ tv[k]={anyOf:t.anyOf}; if(t.label){ tv[k].label=t.label; tv[k].s=t.side; } if(t.shown!=null) tv[k].shown=t.shown; if(t.shownBy) tv[k].shownBy=t.shownBy; continue; }   /* anyOf 묶음의 이름·성공 회차 옵션(tools/sim/run.js와 같은 칸, 2026-11-13 W4) */ const g=D.groups[t.gi]; if(!g) continue; const lo = graph.ilvl ? Math.max(1, g.t.findIndex(x=>x[0]<=graph.ilvl)+1) : 1; tv[k]={s:g.g, sec:g.s, tmax:(!['n','d'].includes(g.s) && g.t.length<=1) ? undefined : t.tmax, gi:t.gi, tiers:g.t.slice(0,Math.max(5,lo+4)).map(x=>[x[4],x[5]]), ...(lo>1?{lo}:{})}; }   /* lo: 아이템 레벨로 붙을 수 있는 가장 좋은 티어(레벨 81 저항 = 2티어, 사용자 2026-11-12) */
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
    try{ const g=fromDraft({id:'mag', cls:r.cls, base:r.base, ilvl:r.ilvl, start:{rar:'normal', mods:[]}, nodes, difficulty:0}, D, {craft, grades:['high'], noFlux:true});
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

const api={fromDraft, tplRewrite, view, check, gradesFor, diffOf, magicCost, fluxPlan:(d,D)=>!!fluxPlan(d, D.groups, {})};
if(typeof module!=='undefined' && module.exports) module.exports=api; else root.POE2GRAPH=api;
})(typeof window!=='undefined' ? window : globalThis);
