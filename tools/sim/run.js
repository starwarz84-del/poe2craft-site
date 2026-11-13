// Simulate one recipe graph for each of its strategies → site/data/sim/<id>.json (the flowchart view reads it).
const pOnly=c=>{ if(!c) return; if(c.param) return c.param; if(c.all){ const o={}; c.all.forEach(x=>x.param&&Object.assign(o,x.param)); return Object.keys(o).length?o:undefined; } };
// usage: node tools/sim/run.js <graph id> [runs]   runs default by difficulty (user 2026-11-13): 쉬움 500 · 보통 1000 · 어려움 2000 · 전문가 이상 5000      (graph: scripts/graphs/<id>.json)
// The engine's expected values (recipes.html analyse) are added when tools/sim/engine/<id>.json exists (node tools/test/_eng_one.js <recipe id> > that file).
const fs=require('fs'), path=require('path'), SIM=require('../../site/sim.js');
const ROOT=path.join(__dirname,'../..'), id=process.argv[2];
const RUNS_BY_DIFF={0:500,1:500,2:1000,3:2000,4:5000,5:5000};
const N=+(process.argv[3]||(()=>{ try{ const g0=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${id}.json`,'utf8')); const R=JSON.parse(fs.readFileSync(`${ROOT}/site/data/recipes.json`,'utf8')).recipes;
  const ds=R.filter(r=>r.id===(g0.recipe||id)||(r.tierGroup&&r.tierGroup===(g0.recipe||id))||r.id.startsWith((g0.recipe||id)+'-')).map(r=>+r.difficulty).filter(x=>!isNaN(x)); return ds.length?RUNS_BY_DIFF[Math.max(...ds)]||5000:5000; }catch(e){ return 5000; } })());
const graph=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${id}.json`,'utf8'));
const D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${graph.cls}.json`,'utf8'));
const craft=JSON.parse(fs.readFileSync(`${ROOT}/site/data/crafting.json`,'utf8'));
const prices=JSON.parse(fs.readFileSync(`${ROOT}/site/data/prices.json`,'utf8'));
const r4 = x => typeof x==='number' ? +x.toPrecision(5) : x;
const round = o => JSON.parse(JSON.stringify(o, (k,v)=>r4(v)));
// tag → modifier text per tier (the flowchart shows what each step is after)
const tagView={}; for(const [k,t] of Object.entries(graph.tags||{})){ if(t.anyOf){ tagView[k]={anyOf:t.anyOf}; if(t.label){ tagView[k].label=t.label; tagView[k].s=t.side; } if(t.shown!=null) tagView[k].shown=t.shown; if(t.shownBy) tagView[k].shownBy=t.shownBy;   /* 성공 회차 옵션(S4 2026-11-13, 화면만) */ continue; }
  const g=t.gi!=null ? D.groups[t.gi] : D.groups.find(g=>g.f.join('+')===t.fam && (!t.sec || g.s===t.sec) && (!t.side || g.g===t.side)); if(!g) continue;
  tagView[k]={s:g.g, sec:g.s, tmax:t.tmax, gi:D.groups.indexOf(g), tiers:g.t.slice(0,5).map(x=>[x[4],x[5]])}; }
const out={id:graph.id, recipe:graph.recipe, runs:N, generated:new Date().toISOString().slice(0,10), prices:prices.fetched||null,
  graph:{tags:tagView, finals:graph.finals, finalItem:graph.finalItem, basePrice:graph.basePrice, params:graph.params, groups:graph.groups, start:graph.start, loops:graph.loops, versions:graph.versions,
    nodes:graph.nodes.map(n=>({id:n.id, kind:n.kind, act:n.act, cur:n.cur, curIf:n.curIf?.map(c=>c.cur), omens:n.omens, trim:n.trim?{side:n.trim.side,keepDes:n.trim.keepDes}:undefined, group:n.group, pos:n.pos, label:n.label,
      param:n.param, options:n.options, optStyle:n.optStyle, item:n.item, curRows:n.curRows, target:n.target, pAll:n.pAll, ask:n.ask, goal:n.goal, goalBy:n.goalBy /* 일반 상자 등급별 목표 글(2026-11-13 S6 — 빠져서 플로우차트에 반영되지 않았음) */, show:n.show, showText:n.showText, rune:n.rune, swapAstrid:n.swapAstrid, count:n.act==='rune'?n.count:undefined, fill:n.fill, showIf:n.showIf, over:n.over, once:n.once, skipNote:n.skipNote, skipLabel:n.skipLabel, skipHide:n.skipHide, gapBefore:n.gapBefore, variant:n.variant, note:n.note, attach:n.attach, tiers:n.kind==='side'?n.tiers:undefined, edgeLabels:n.edgeLabels, next:n.next, skipTo:n.skipTo,
      edges:(n.edges||[]).map(e=>({to:e.to, label:e.label, lost:e.lost, res:e.res, dash:e.dash, p:e.p, hide:e.hide, port:e.port, enter:e.enter, lane:e.lane, turn:e.turn, when:pOnly(e.if)}))}))},
  strategies:[]};
const prevOut = process.env.GRAPH_ONLY ? JSON.parse(fs.readFileSync(`${ROOT}/site/data/sim/${id}.json`,'utf8')) : null;   // GRAPH_ONLY=1: keep the simulated numbers, refresh only the drawing data
if(prevOut){ out.strategies=prevOut.strategies; out.runs=prevOut.runs; }
else for(const s of graph.strategies){ const t=Date.now(); const res=SIM.simulate(graph, D, craft, prices, s.params, N, 7);
  out.strategies.push({id:s.id, params:s.params, hidden:!!s.hidden, res:round(res)});
  console.log(s.id.padEnd(18), 'mean', res.mean.toFixed(1), 'median', res.median.toFixed(1), 'p90', res.p90.toFixed(1), 'bases', res.bases.toFixed(2), 'req', res.reqOk, (Date.now()-t)+'ms', res.missing.length?'missing '+res.missing:''); }
const ef=`${__dirname}/engine/${graph.recipe}.json`; if(fs.existsSync(ef)) out.engine=round(JSON.parse(fs.readFileSync(ef,'utf8')));
fs.mkdirSync(`${ROOT}/site/data/sim`,{recursive:true}); fs.writeFileSync(`${ROOT}/site/data/sim/${id}.json`, JSON.stringify(out));
console.log('wrote site/data/sim/'+id+'.json');
