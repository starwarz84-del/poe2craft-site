// debug: node tools/sim/dbg.js <graph> <strategy> [runs] — prints finished items that miss the graph's require
const fs=require('fs'),path=require('path'),SIM=require('../../site/sim.js'); const R=path.join(__dirname,'../..');
const [id,sid,n]=process.argv.slice(2); const g=JSON.parse(fs.readFileSync(`${R}/scripts/graphs/${id}.json`));
const D=JSON.parse(fs.readFileSync(`${R}/site/data/c/${g.cls}.json`)),c=JSON.parse(fs.readFileSync(`${R}/site/data/crafting.json`));
const s=g.strategies.find(x=>x.id===sid); const run=SIM.make(g,D,c,s.params), rnd=SIM.rng(3); let shown=0;
for(let i=0;i<(+n||300)&&shown<4;i++){ run(rnd,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},done:(it,cond)=>{ if(g.require && !cond(g.require)){ shown++; console.log(it.mods.map(m=>m.unrev?`${m.side}:UNREV`:`${m.side}:${m.gi}T${m.ti+1}${m.fr?'F':''}${m.ess?'E':''}`).join('  '), '|', (D.groups[it.mods.find(m=>!m.unrev)?.gi]||{}).t?.[0]?.[5]?.slice(0,0)); } }}}); }
