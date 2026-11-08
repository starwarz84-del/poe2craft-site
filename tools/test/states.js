const {chromium}=require('playwright');(async()=>{const b=await chromium.launch(),p=await b.newPage();await p.goto('http://localhost:8779/recipes.html?debug=1&lang=kr');await p.waitForTimeout(2500);
const ids=process.argv.slice(2);
console.log(await p.evaluate(ids=>ids.map(id=>{const r=__rec.recipes.find(x=>x.id==id);const a=__rec.analyse(r);
 const lab=m=>(m.fr?'F':'')+(m.junk&&!m.des&&!m.unrev?'J':'')+(m.unrev?'U':'')+(m.des?'D':'')+(m.ess?'C':'')+(m.mark?'M':'')+(m.gi!=null?m.gi:'');
 return '# '+id+' cap '+JSON.stringify(r.cap||'')+'\n'+a.nodes.map((o,i)=>{const n=o.n;const st=o.state||[];
  return `${i+1} ${n.id}${n.branch?'['+n.branch.when+']':''}${n.fallbackFor?'[fb]':''} ${n.do} ${n.cur||''}${(n.omens||[]).length?'+'+n.omens.map(x=>x.replace('Omen_of_','')).join('+'):''} T=${JSON.stringify(n.target||{}).slice(0,90)} F=${JSON.stringify(n.fail||'')} p=${o.p?.toFixed?.(3)} | P[${st.filter(m=>m.side==='p').map(lab)}] S[${st.filter(m=>m.side==='s').map(lab)}] R=${(o.runes||[]).length}/${o.sockets||0}`}).join('\n')}).join('\n'),ids));await b.close()})();
