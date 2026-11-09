// Simulate one recipe graph for each of its strategies → site/data/sim/<id>.json (the flowchart view reads it).
// usage: node tools/sim/run.js <graph id> [runs=20000]      (graph: scripts/graphs/<id>.json)
// The engine's expected values (recipes.html analyse) are added when tools/sim/engine/<id>.json exists (node tools/test/_eng_one.js <recipe id> > that file).
const fs=require('fs'), path=require('path'), SIM=require('../../site/sim.js');
const ROOT=path.join(__dirname,'../..'), id=process.argv[2], N=+(process.argv[3]||20000);
const graph=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${id}.json`,'utf8'));
const D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${graph.cls}.json`,'utf8'));
const craft=JSON.parse(fs.readFileSync(`${ROOT}/site/data/crafting.json`,'utf8'));
const prices=JSON.parse(fs.readFileSync(`${ROOT}/site/data/prices.json`,'utf8'));
const r4 = x => typeof x==='number' ? +x.toPrecision(5) : x;
const round = o => JSON.parse(JSON.stringify(o, (k,v)=>r4(v)));
// tag → modifier text per tier (the flowchart shows what each step is after)
const tagView={}; for(const [k,t] of Object.entries(graph.tags||{})){ if(t.anyOf){ tagView[k]={anyOf:t.anyOf}; continue; }
  const g=D.groups.find(g=>g.f.join('+')===t.fam && (!t.sec || g.s===t.sec) && (!t.side || g.g===t.side)); if(!g) continue;
  tagView[k]={s:g.g, sec:g.s, tmax:t.tmax, tiers:g.t.slice(0,5).map(x=>[x[4],x[5]])}; }
const out={id:graph.id, recipe:graph.recipe, runs:N, generated:new Date().toISOString().slice(0,10), prices:prices.fetched||null,
  graph:{tags:tagView, basePrice:graph.basePrice, params:graph.params, groups:graph.groups, start:graph.start, loops:graph.loops, versions:graph.versions,
    nodes:graph.nodes.map(n=>({id:n.id, kind:n.kind, act:n.act, cur:n.cur, curIf:n.curIf?.map(c=>c.cur), omens:n.omens, trim:!!n.trim, group:n.group, pos:n.pos, label:n.label,
      param:n.param, options:n.options, optStyle:n.optStyle, item:n.item, curRows:n.curRows, target:n.target, ask:n.ask, goal:n.goal, show:n.show, showText:n.showText, skipNote:n.skipNote, skipLabel:n.skipLabel, variant:n.variant, note:n.note, attach:n.attach, edgeLabels:n.edgeLabels, next:n.next, skipTo:n.skipTo,
      edges:(n.edges||[]).map(e=>({to:e.to, label:e.label, lost:e.lost, res:e.res, dash:e.dash, p:e.p, hide:e.hide}))}))},
  strategies:[]};
for(const s of graph.strategies){ const t=Date.now(); const res=SIM.simulate(graph, D, craft, prices, s.params, N, 7);
  out.strategies.push({id:s.id, params:s.params, hidden:!!s.hidden, res:round(res)});
  console.log(s.id.padEnd(18), 'mean', res.mean.toFixed(1), 'median', res.median.toFixed(1), 'p90', res.p90.toFixed(1), 'bases', res.bases.toFixed(2), 'req', res.reqOk, (Date.now()-t)+'ms', res.missing.length?'missing '+res.missing:''); }
const ef=`${__dirname}/engine/${graph.recipe}.json`; if(fs.existsSync(ef)) out.engine=round(JSON.parse(fs.readFileSync(ef,'utf8')));
fs.mkdirSync(`${ROOT}/site/data/sim`,{recursive:true}); fs.writeFileSync(`${ROOT}/site/data/sim/${id}.json`, JSON.stringify(out));
console.log('wrote site/data/sim/'+id+'.json');
