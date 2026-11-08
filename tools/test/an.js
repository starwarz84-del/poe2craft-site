const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(/fonts\./,r=>r.abort());
await p.goto('http://localhost:8779/recipes.html?lang=kr');await p.waitForTimeout(3000);
const res=await p.evaluate(()=>__rec.recipes.filter(r=>true).map(r=>{ try{ const a=__rec.analyse(r); return r.id+' bases='+a.bases.toFixed(2)+'\n'+a.nodes.map(o=>`  ${o.n.id} ${o.n.do} p=${o.pUnknown?'?':(+o.p).toFixed(4)}${o.warn?' WARN '+o.warn:''} P${o.state.filter(m=>m.side==='p').length}/${o.cap.p} S${o.state.filter(m=>m.side==='s').length}/${o.cap.s}`).join('\n')+'\n  final: '+a.final.map(m=>m.txt.replace(/\n/g,' ')).join(' | '); }catch(e){ return r.id+' ERR '+e.message+' '+e.stack.split('\n')[1]; } }));
console.log(res.join('\n'));console.log('errs',errs);await b.close();})();
