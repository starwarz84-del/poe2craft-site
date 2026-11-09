// Exact odds for one reveal step of a graph: node tools/sim/reveal_odds.js <graph id> <desecrate node id> <want gi> [strategy]
// Captures the item when the desecrate step is first reached, then: 3 groups drawn without repeats (weighted), one tier each;
// Abyssal Echoes = a second, independent draw of 3. Desecrated-only groups' weight is unknown → shown for several assumptions.
const fs=require('fs'), path=require('path'), SIM=require('../../site/sim.js'), ROOT=path.join(__dirname,'../..');
const [id, at, wgi, sid='high']=process.argv.slice(2);
const graph=JSON.parse(fs.readFileSync(`${ROOT}/scripts/graphs/${id}.json`,'utf8')), D=JSON.parse(fs.readFileSync(`${ROOT}/site/data/c/${graph.cls}.json`,'utf8'));
const craft=JSON.parse(fs.readFileSync(`${ROOT}/site/data/crafting.json`,'utf8'));
const st=graph.strategies.find(s=>s.id===sid), run=SIM.make(graph, D, craft, st.params);
let item=null; const noop=()=>{}; let seed=1; const rnd=()=>{ seed=(seed*16807)%2147483647; return seed/2147483647; };
try{ run(rnd, {tally:{visit:noop, use:noop, edge:noop, base:noop, done:noop}, enter:(nid,it)=>{ if(nid===at && !item){ item=JSON.parse(JSON.stringify(it)); throw 'got'; } }}); }catch(e){ if(e!=='got') throw e; }
const G=D.groups, node=graph.nodes.find(n=>n.id===at), bone=craft.bones.find(b=>b.id===(process.env.BONE||node.cur)), minL=bone.min||0, ilvl=graph.ilvl;
const side=(graph.nodes.find(n=>n.id===at).showText||[{}])[0].s || 'p';
const F=new Set(); item.mods.forEach(m=>{ if(!m.unrev) G[m.gi].f.forEach(x=>F.add(x)); });
console.log('item at', at, item.mods.map(m=>`${m.side}:${G[m.gi]?.f.join('+')}${m.fr?'(fr)':''}`).join(', '), '| side', side, '| bone min', minL);
const wantT = +(process.argv[6]||1);
for(const dw of [1, 100, 500, 1000]){
  const gs=[]; G.forEach((g,gi)=>{ if(!['n','d'].includes(g.s) || g.g!==side || g.f.some(x=>F.has(x))) return; const top=g.t.findIndex(t=>t[0]<=ilvl && (t[1]>0||g.s==='d'));
    const ts=g.t.map((t,ti)=>({ti,lv:t[0],w:g.s==='d'?1:t[1]})).filter(t=>t.lv<=ilvl && (t.lv>=minL || t.ti===top) && t.w>0); if(!ts.length) return;
    gs.push({gi, w: g.s==='d'?dw : ts.reduce((a,x)=>a+x.w,0), ts, name:g.t[0][4]}); });
  const tot=gs.reduce((a,g)=>a+g.w,0); let pg=0;   // P(want group among 3 without repeats)
  for(const a of gs) for(const b of gs) if(b!==a) for(const c of gs) if(c!==a && c!==b){ if(![a,b,c].some(g=>g.gi==wgi)) continue;
    pg += a.w/tot * b.w/(tot-a.w) * c.w/(tot-a.w-b.w); }
  const W=gs.find(g=>g.gi==wgi); const pT = W.ts.filter(t=>t.ti<wantT).reduce((a,x)=>a+x.w,0)/W.ts.reduce((a,x)=>a+x.w,0);
  const q=pg*pT, p2=1-(1-q)**2;
  console.log(`desecrated-only weight ${dw}: groups ${gs.length} (desecrated-only ${gs.filter(g=>G[g.gi].s==='d').length}) · group shown ${(pg*100).toFixed(1)}% · T1..${wantT} given shown ${(pT*100).toFixed(1)}% · one look ${(q*100).toFixed(2)}% · with Echoes ${(p2*100).toFixed(2)}% → ${(1/p2).toFixed(1)} tries`);
  if(dw===1) console.log('  want tiers:', W.ts.map(t=>`T${t.ti+1} lv${t.lv} w${t.w}`).join(', '), '| pool:', gs.map(g=>G[g.gi].s+':'+g.name.slice(0,14)+'='+g.w).join(' / '));
}
