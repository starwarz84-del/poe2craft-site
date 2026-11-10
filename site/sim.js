// POE2 craft graph simulator (shared by node scripts and, later, the site).
// A recipe graph (docs/graph-model.md) is walked many times with real rolls from the class data:
// weights, levels, families (one per item), slots per side, minimum modifier level of Greater/Perfect orbs,
// random removal, side omens, Whittling (lowest required level, ties random), Erasure, bones, reveal (3 groups, Abyssal Echoes = one redraw),
// fracture (a random revealed line). Rules follow site/emulator.html and docs/game-rules.md; the reveal pool is the same as recipes.html revealChance.
(function(root){
'use strict';
function rng(seed){ let a=seed>>>0; return ()=>{ a=(a+0x6D2B79F5)>>>0; let t=a; t=Math.imul(t^(t>>>15), t|1); t^=t+Math.imul(t^(t>>>7), t|61); return ((t^(t>>>14))>>>0)/4294967296; }; }
const pickW = (rnd, xs) => { let s=0; for(const x of xs) s+=x.w; let v=rnd()*s; for(const x of xs){ v-=x.w; if(v<=0) return x; } return xs[xs.length-1]; };

// build a simulator for one graph. D = class file (site/data/c/<cls>.json), craft = crafting.json, params = strategy settings
function make(graph, D, craft, params){
  const byId={}; for(const k in craft) for(const x of craft[k]) byId[x.id]=x;
  const minOf = id => +(byId[id]?.min||0);
  const base = D.bases.find(b=>b.en===graph.base || b.id===graph.base) || {};
  const cap = graph.cap ? {...graph.cap} : {p:3+(base.pd||0), s:3+(base.sd||0)}, ilvl=graph.ilvl;   // graph.cap: jewels are 2/2
  const G = D.groups;
  // desecrated-only groups weigh 1000 on the game's scale; in a flat-weight class (jewels: every modifier weighs the same) they weigh what an average normal group does (recipes.html dWeight)
  const xTW = (()=>{ const ws=G.filter(g=>g.s==='n').flatMap(g=>g.t.map(t=>t[1])).filter(w=>w>0); return ws.reduce((a,w)=>a+w,0)/Math.max(1,ws.length); })();   // graph.xroll: a socketed rune's lines roll on exalts/chaos too, each tier at the average normal tier weight (estimate)
  const dW = (()=>{ const ns=G.filter(g=>g.s==='n'), ws=new Set(ns.flatMap(g=>g.t.map(t=>t[1]))); if(ws.size!==1) return 1000; const tot=ns.map(g=>g.t.filter(t=>t[0]<=graph.ilvl).reduce((a,t)=>a+t[1],0)).filter(x=>x>0); return tot.reduce((a,x)=>a+x,0)/Math.max(1,tot.length); })();
  const P = v => typeof v==='string' && v[0]==='$' ? params[v.slice(1)] : v;
  // tags: named modifier specs, resolved to group indexes once
  const tags={};
  const resolve = (name, t) => { if(t.anyOf) return {anyOf:t.anyOf.map(x=>typeof x==='string' ? x : resolve(null,x))};
    const gi=t.gi!=null ? t.gi : G.findIndex(g=>g.f.join('+')===t.fam && (!t.sec || g.s===t.sec) && (!t.side || g.g===t.side));
    if(gi<0) throw new Error('tag '+(name||'')+': no group '+t.fam); return {gi, tmax:P(t.tmax)}; };
  for(const k in graph.tags){ tags[k]=resolve(k, graph.tags[k]); if(graph.tags[k].slot) tags[k].slot=graph.tags[k].slot; }   // slot: a line that opens one (Potent Liquid Contempt: +1 suffix / prefix allowed)
  const match = (m, tag) => { if(!m || m.unrev) return false; const t = typeof tag==='string' ? tags[tag] : tag; if(!t) throw new Error('unknown tag '+tag);
    if(t.anyOf) return t.anyOf.some(x=>match(m,x)); return m.gi===t.gi && (!t.tmax || m.ti < t.tmax); };
  const nodes={}; graph.nodes.forEach(n=>{ const o=(n.over||[]).find(o=>Object.entries(o.param||{}).every(([k,v])=>params[k]===v)); nodes[n.id]=o ? {...n, ...o.set} : n; });   // over: per-version node fields

  return function run(rnd, hooks){
    let it={rar:'normal', mods:[]}, last={added:[], removed:[], fr:null};
    const side = m => m.side, lvl = m => G[m.gi].t[m.ti][0];
    const count = s => it.mods.filter(m=>m.side===s).length;
    let capR={...cap};   // slots this run (a rune such as Serle's Triumph adds one)
    const maxA = s => it.rar==='normal'?0 : it.rar==='magic'?1 : capR[s] + it.mods.reduce((a,m)=>a+(m.slot?.[s]||0),0);
    const over = () => ['p','s'].filter(s=>count(s)>maxA(s));   // a side above its limit (contempt line removed): Chaos then only rerolls the other side (Diztoh 5-mod jewel)
    const fams = () => { const f=new Set(); it.mods.forEach(m=>{ if(!m.unrev) G[m.gi].f.forEach(x=>f.add(x)); }); return f; };
    // eligible tiers per group for a minimum level (cached): a family's highest allowed tier always stays in
    const gcache={};
    const groupsFor = (minLvl, sec, xs=[]) => { const k=minLvl+'|'+sec+'|'+xs.join(','); if(gcache[k]) return gcache[k];
      const out=[]; G.forEach((g,gi)=>{ if(!sec.includes(g.s)) return; if(g.s==='x' && !xs.includes(g.sub?.[1])) return; const top=g.t.findIndex(t=>t[0]<=ilvl && (t[1]>0 || g.s==='d'));
        const ts=[]; g.t.forEach((t,ti)=>{ if(t[0]<=ilvl && (t[0]>=minLvl || ti===top) && (t[1]>0 || g.s==='d')) ts.push({gi, ti, w:g.s==='d'?1:g.s==='x'?xTW:t[1]}); });
        if(ts.length) out.push({gi, side:g.g, f:g.f, ts, w:ts.reduce((a,x)=>a+x.w,0), d:g.s==='d'||g.s==='x'}); });
      return gcache[k]=out; };
    // x (augment / Otherworldly) lines join only for the socketed rune (graph.xsub) or an Altered bone, weighted like desecrated-only lines
    // candidate groups now: free side, family not on the item
    function pool(sides, minLvl, sections=['n'], xs=[]){
      const F=fams(), free=(sides||['p','s']).filter(s=>count(s)<maxA(s));
      return groupsFor(minLvl, sections.join(''), xs).filter(g=>free.includes(g.side) && !g.f.some(x=>F.has(x))); }
    const add = (sides, minLvl) => { const gs=graph.xroll ? pool(sides, minLvl, ['n','x'], graph.xsub||[]) : pool(sides, minLvl); if(!gs.length) return null; const g=pickW(rnd, gs), p=pickW(rnd, g.ts); const m={gi:p.gi, ti:p.ti, side:g.side}; it.mods.push(m); last.added.push(m); return m; };
    const take = m => { it.mods.splice(it.mods.indexOf(m),1); last.removed.push(m); return m; };
    const takeRandom = f => { const c=it.mods.filter(m=>!m.fr && (!f || f(m))); if(!c.length) return null; return take(c[Math.floor(rnd()*c.length)]); };
    const sideOm = (oms, a, b) => oms.some(o=>a.test(o)) ? 'p' : oms.some(o=>b.test(o)) ? 's' : null;
    // conditions on the state after a step (and on what that step added / removed / fractured)
    function cond(c){ if(!c) return true;
      if(c.ref) return cond(graph.conds[c.ref]);
      if(c.all) return c.all.every(cond); if(c.any) return c.any.some(cond); if(c.not) return !cond(c.not);
      if(c.has) return it.mods.some(m=>match(m,P(c.has)));
      if(c.added) return last.added.some(m=>match(m,P(c.added)));
      if(c.removed) return last.removed.some(m=>match(m,c.removed));
      if(c.unrev!=null) return it.mods.some(m=>m.unrev)===!!c.unrev;
      if(c.fractured) return !!last.fr && match(last.fr, c.fractured);
      if(c.full) return count(c.full)>=maxA(c.full);
      if(c.sideLt) return count(c.sideLt.side) < c.sideLt.n;
      if(c.count) return it.mods.filter(m=>match(m,c.count.tag)).length>=c.count.min;
      if(c.allMods) return it.mods.every(m=>m.unrev || match(m,c.allMods));
      if(c.sideAll){ const xs=it.mods.filter(m=>m.side===c.sideAll.side && !m.fr); return xs.every(m=>match(m,c.sideAll.tag)); }
      if(c.whittleSafe){ const ws=c.whittleSafe.tag!=null ? c.whittleSafe : {tag:c.whittleSafe}, cs=it.mods.filter(m=>!m.fr && !m.unrev && (!ws.side || m.side===ws.side)); if(!cs.length) return false; const lo=Math.min(...cs.map(lvl)); return cs.filter(m=>lvl(m)===lo).every(m=>!match(m,P(ws.tag))); }   // Whittling would hit only lines outside this tag ({tag, side}: with a side Erasure omen, that side only)
      if(c.param) return Object.entries(c.param).every(([k,v])=>params[k]===v);
      throw new Error('bad condition '+JSON.stringify(c)); }
    const pickEdge = n => (n.edges||[]).find(e=>cond(e.if));
    // Whittling / Erasure choice (policy 23 ④): the junk line is the lowest → Whittling; lowest of its side only → Whittling + that side's Erasure;
    // a wanted line of that side is lower → Erasure alone (1/2)
    function trimOmens(n){ const sd=n.trim.side, keep=n.trim.keep;
      const junk=it.mods.filter(m=>m.side===sd && !m.fr && !m.unrev && !match(m,keep)); if(junk.length!==1) return [sd==='p'?'Omen_of_Sinistral_Erasure':'Omen_of_Dextral_Erasure'];
      const lj=lvl(junk[0]), others=it.mods.filter(m=>!m.fr && !m.unrev && m!==junk[0]), same=others.filter(m=>m.side===sd);
      const er = sd==='p'?'Omen_of_Sinistral_Erasure':'Omen_of_Dextral_Erasure';
      if(same.some(m=>lvl(m)<=lj)) return [er];
      if(others.every(m=>lvl(m)>lj)) return ['Omen_of_Whittling'];
      return ['Omen_of_Whittling', er]; }
    function act(n){ const a=n.act, oms=[...(n.omens||[])]; let cur=n.cur;
      for(const c of (n.curIf||[])) if(cond(c.if)){ cur=c.cur; break; }
      if(n.trim) oms.push(...trimOmens(n));
      const use={}; const u=id=>{ use[id]=(use[id]||0)+1; }; if(cur) use[cur]=n.count||1; oms.forEach(u);
      const mn = minOf(cur);
      if(a==='transmute'){ it.rar='magic'; add(null, mn); }
      else if(a==='augment') add(null, mn);
      else if(a==='regal'){ it.rar='rare'; add(sideOm(oms,/Sinistral_Coronation/,/Dextral_Coronation/) ? [sideOm(oms,/Sinistral_Coronation/,/Dextral_Coronation/)] : null, mn); }
      else if(a==='exalt'){ const sd=sideOm(oms,/Sinistral_Exaltation/,/Dextral_Exaltation/); const k=oms.includes('Omen_of_Greater_Exaltation')?2:1; for(let i=0;i<k;i++) add(sd?[sd]:null, mn); }
      else if(a==='chaos'){ const er=sideOm(oms,/Sinistral_Erasure/,/Dextral_Erasure/);
        if(oms.includes('Omen_of_Whittling')){ const c=it.mods.filter(m=>!m.fr && !m.unrev && (!er || m.side===er)); if(c.length){ const lo=Math.min(...c.map(lvl)), xs=c.filter(m=>lvl(m)===lo); take(xs[Math.floor(rnd()*xs.length)]); } }
        else { const ov=over(); takeRandom(er ? (m=>m.side===er) : ov.length ? (m=>!ov.includes(m.side)) : null); }
        add(null, mn); }
      else if(a==='essence'){ const tn = n.alt && rnd()<0.5 ? n.alt : n.ess, t=tags[tn], sd=G[t.gi].g, cr=sideOm(oms,/Sinistral_Crystallisation/,/Dextral_Crystallisation/);   // magic → rare + the essence line (top tier); on a rare one line goes first (Crystallisation picks its side)
        if(it.rar==='rare') takeRandom(cr ? (m=>m.side===cr) : n.anyRemove ? null : count(sd)>=maxA(sd) ? (m=>m.side===sd) : null);   // anyRemove: a liquid that takes any line (SL 5-mod jewel: 1/3) it.rar='rare';   // its own side full: a line of that side makes way (발굴 규칙 6)
        const m={gi:t.gi, ti:0, side:sd, ess:!n.liquid, mark:!!n.mark}; if(t.slot) m.slot=t.slot; it.mods.push(m); last.added.push(m); }
      else if(a==='annul'){ const sd=sideOm(oms,/Sinistral_Annulment/,/Dextral_Annulment/);
        takeRandom(oms.includes('Omen_of_Light') ? (m=>m.unrev||m.des||G[m.gi]?.s==='d') : sd ? (m=>m.side===sd) : null); }
      else if(a==='desecrate' && n.fromMark){ const mk=it.mods.find(m=>m.mark); if(mk){ take(mk); const m={unrev:true, side:mk.side, bone:cur, min:mn, marked:true}; it.mods.push(m); last.added.push(m); } }   // a bone on the Abyssal Lord's Mark: the mark becomes the unrevealed desecrated line
      else if(a==='desecrate'){ const sd=sideOm(oms,/Sinistral_Necromancy/,/Dextral_Necromancy/), ss=sd?[sd]:['p','s'];
        let free=ss.filter(s=>count(s)<maxA(s)), s;
        if(free.length) s=free[Math.floor(rnd()*free.length)];
        else { s=ss[Math.floor(rnd()*ss.length)]; takeRandom(m=>m.side===s); }   // a full side: one of its lines makes way
        const lord=oms.includes('Omen_of_the_Liege')?'amanamu':oms.includes('Omen_of_the_Sovereign')?'ulaman':oms.includes('Omen_of_the_Blackblooded')?'kurgal':null;   // an Abyssal lord omen: one revealed option is that lord's
        const m={unrev:true, side:s, bone:cur, min:mn, lord}; it.mods.push(m); last.added.push(m); }
      else if(a==='reveal'){ const m=it.mods.find(x=>x.unrev); if(m){ it.mods.splice(it.mods.indexOf(m),1);
        const gs0=pool([m.side], m.min, ['n','d','x'], [...(graph.xsub||[]), ...(/^Altered_/.test(m.bone||'')?['Otherworldly']:[])]);   // x lines have no published weight: counted like desecrated-only lines (dW)   // reveal: 3 groups without repeats, desecrated-only groups weigh 1000 (recipes.html revealChance, emulator revealOptions)
        const draw = () => { let gs=gs0.map(g=>({g, w:g.d?dW:g.w})), out=[];
          if(m.lord){ const lg=gs.filter(x=>x.g.d && (G[x.g.gi].tg||[]).includes(m.lord+'_mod')); if(lg.length) gs=lg; }   // an Abyssal lord omen: every option is that lord's (영상 확인 2026-11-10) — recipes.html revealChance
          while(out.length<3 && gs.length){ const x=pickW(rnd, gs); gs=gs.filter(y=>y!==x); out.push(pickW(rnd, x.g.ts)); } return out; };
        const wt=P(n.want), want = o => wt && match({gi:o.gi, ti:o.ti}, wt);
        let os=draw(); if(!os.some(want) && oms.includes('Omen_of_Abyssal_Echoes')) os=draw();
        const o=os.find(want)||os[0]; const nm={gi:o.gi, ti:o.ti, side:m.side, des:true}; it.mods.push(nm); last.added.push(nm); } }
      else if(a==='fracture'){ const c=it.mods.filter(m=>!m.unrev && !m.fr); const m=c[Math.floor(rnd()*c.length)]; if(m){ m.fr=true; last.fr=m; } }
      else if(a==='rune'){ for(const k in (n.slots||{})) capR[k]+=n.slots[k]; }   // a socketed rune that opens a slot (Serle's Triumph: one more suffix)
      else if(a==='divine' || a==='quality'){ /* values / catalyst quality only */ }
      else throw new Error('unknown act '+a);
      return use; }

    // walk
    const tally = hooks.tally; let id=graph.start, steps=0;
    while(true){ if(++steps>2e6) throw new Error('runaway at '+id);
      const n=nodes[id]; if(!n) throw new Error('no node '+id);
      last={added:[], removed:[], fr:null}; tally.visit(id); if(hooks.enter) hooks.enter(id, it);
      if(n.kind==='done'){ tally.done(it, cond); return it; }
      if(n.kind==='mark'){ tally.edge(id, n.next); id=n.next; continue; }   // a milestone on the chart (starting item of the main craft)
      if(n.kind==='exit'){ if(n.swapFracture){ it.mods.forEach(m=>{ if(m.fr) delete m.fr; }); const m=it.mods.find(x=>match(x,n.swapFracture)); if(m) m.fr=true; } tally.edge(id, n.simTo); id=n.simTo; continue; }   // this item is set aside (sold / thrown away): the cost goes on from simTo
      if(n.kind==='base'){ it={rar:'normal', mods:[]}; capR={...cap}; if(n.start){ it.rar=n.start.rar||'normal';
          // a start line: a tag name, or {tag, fr, ess} (fractured / crafted), {unrev:'p'|'s', bone, lord} (an unrevealed desecration), {junk:'p'|'s'} (a random line)
          (n.start.mods||[]).forEach(x=>{ if(typeof x==='string') x={tag:x};
            if(x.unrev){ it.mods.push({unrev:true, side:x.unrev, bone:x.bone, min:minOf(x.bone), lord:x.lord||null}); return; }
            if(x.junk){ add([x.junk], 0); return; }
            const t=tags[x.tag], m={gi:t.gi, ti:Math.max(0,(P(t.tmax)||1)-1), side:G[t.gi].g}; if(x.fr) m.fr=true; if(x.ess) m.ess=true; it.mods.push(m); });
          for(let i=0;i<(n.start.random||0);i++) add(null,0); } tally.base(id); tally.edge(id, n.next); id=n.next; continue; }
      if(n.kind==='choice'){ const v=params[n.param], to=n.options[v]; if(!to) throw new Error(n.id+': no option '+v); tally.edge(id, to); id=to; continue; }
      if(n.kind==='assume'){ if(n.swapFracture){ it.mods.forEach(m=>{ if(m.fr) delete m.fr; }); const m=it.mods.find(x=>match(x,n.swapFracture)); if(m) m.fr=true; } tally.edge(id, n.next); id=n.next; continue; }
      if(n.kind==='cleanup'){   // plain Annulment until at most maxJunk lines outside `keep` are left; a kept line going ends it
        const cs=n.side, cu=cs ? {Orb_of_Annulment:1, [cs==='p'?'Omen_of_Sinistral_Annulment':'Omen_of_Dextral_Annulment']:1} : {Orb_of_Annulment:1};   // side: a side Annulment omen each time
        let lost=null; while(true){ const junk=it.mods.filter(m=>!m.fr && (!cs || !m.unrev && m.side===cs) && !(n.keep||[]).some(k=>match(m,k))); if(junk.length<=(n.maxJunk||0)) break;
          last={added:[], removed:[], fr:null}; takeRandom(cs ? (m=>m.side===cs) : null); tally.use(id, cu);
          const r=last.removed[0]; lost=(n.keep||[]).find(k=>match(r,k)); if(lost) break; }
        const e=(n.edges||[]).find(e=>lost ? e.lost===lost : !e.lost); if(!e) throw new Error(n.id+': no edge for '+(lost||'done')); tally.edge(id, e.to); id=e.to; continue; }
      if(n.kind==='act'){
        if(n.skipIf && cond(n.skipIf)){ tally.skip(id); tally.edge(id, n.skipTo); id=n.skipTo; continue; }
        const use=act(n); tally.use(id, use);
        const e=pickEdge(n); if(!e) throw new Error(n.id+': no edge matched'); if((n.curIf||n.trim) && tally.byCur){ const ck = n.trim ? Object.keys(use).filter(k=>/Whittling|Erasure/.test(k)).sort().join('+') : [...n.curIf.map(c=>c.cur), n.cur].find(k=>use[k]); if(ck) tally.byCur(id, ck, e.res==='ok'); } tally.edge(id, e.to); id=e.to; continue; }
      throw new Error('unknown kind '+n.kind);
    }
  };
}

// many runs → per-success averages, cost distribution, node reach. prices: site/data/prices.json (ex), basePrice in currency units
function simulate(graph, D, craft, prices, params, N=20000, seed=1){
  const run=make(graph, D, craft, params), rnd=rng(seed);
  const ex = id => id==='Exalted_Orb' ? 1 : prices.p[id]!=null ? +prices.p[id] : null, missing=new Set();
  const div = use => { let v=0; for(const k in use){ const e=ex(k); if(e==null) missing.add(k); else v+=use[k]*e; } return v/prices.divine; };
  const baseDiv = div(graph.basePrice||{});
  const tot={}, nodeUse={}, visits={}, skips={}, byCur={}, reach={}, edges={}, costs=[]; let bases=0, ok=0, okReq=0;
  for(let r=0;r<N;r++){ const seen=new Set(), runUse={}; let runBases=0;
    const tally={ visit:id=>{ visits[id]=(visits[id]||0)+1; seen.add(id); },
      use:(id,u)=>{ const x=nodeUse[id]=nodeUse[id]||{}; for(const k in u){ x[k]=(x[k]||0)+u[k]; runUse[k]=(runUse[k]||0)+u[k]; } },
      base:()=>{ runBases++; }, skip:id=>{ skips[id]=(skips[id]||0)+1; }, byCur:(id,k,ok)=>{ const b=(byCur[id]=byCur[id]||{})[k]=byCur[id]?.[k]||{t:0,ok:0}; b.t++; if(ok) b.ok++; }, edge:(a,b)=>{ const k=a+'>'+b; edges[k]=(edges[k]||0)+1; },
      done:(it, cond)=>{ ok++; if(!graph.require || cond(graph.require)) okReq++; } };
    run(rnd, {tally});
    seen.forEach(id=>reach[id]=(reach[id]||0)+1);
    for(const k in runUse) tot[k]=(tot[k]||0)+runUse[k]; bases+=runBases;
    costs.push(div(runUse)+runBases*baseDiv); }
  costs.sort((a,b)=>a-b);
  const q = f => costs[Math.min(costs.length-1, Math.floor(f*costs.length))];
  const avg = o => { const x={}; for(const k in o) x[k]=o[k]/N; return x; };
  const nodes={}; for(const id in visits){ const u=avg(nodeUse[id]||{}); nodes[id]={reach:reach[id]/N, visits:visits[id]/N, use:u, skips:(skips[id]||0)/N, byCur:byCur[id], div:div(u) + (graph.nodes.find(n=>n.id===id)?.kind==='base' ? visits[id]/N*baseDiv : 0)}; }
  const e2={}; for(const k in edges) e2[k]=edges[k]/N;
  return {N, seed, mean:costs.reduce((s,x)=>s+x,0)/N, median:q(0.5), p90:q(0.9), p10:q(0.1), bases:bases/N, baseDiv, use:avg(tot), useDiv:div(avg(tot)), nodes, edges:e2, reqOk:okReq/Math.max(1,ok), missing:[...missing]};
}
const api={rng, make, simulate};
if(typeof module!=='undefined' && module.exports) module.exports=api; else root.POE2SIM=api;
})(typeof window!=='undefined' ? window : globalThis);
