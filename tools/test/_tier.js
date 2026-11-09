// Policy 22: per recipe - difficulty, expected cost (div, base price included), price tier, and how much trying it takes
// (largest single-step average uses, total tries on the main path, expensive omens). Writes tier.txt (tab separated).
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted&&__rec.prices);
const rows=await p.evaluate(()=>{ const S=__rec, P=S.prices, B=S.budget, exp=new Set(B.expensive);
  const tiers=B.tiers, mir=(P.p.Mirror_of_Kalandra||0)/P.divine, tmax=t=>t.max==='mirror'?mir:t.max;
  const ex=id=>id==='Exalted_Orb'?1:P.p[id];
  return S.recipes.filter(r=>!r.draft).map(r=>{ r._an=null; const a=S.analyse(r); let v=0; const miss=[];
    for(const k in a.tot){ const x=ex(k); if(x==null) miss.push(k); else v+=a.tot[k]*x; }
    v=v/P.divine; for(const [u,x] of Object.entries(a.manual)) v+= u==='Divine_Orb'?x:(ex(u)||0)*x/P.divine;
    if(!Object.keys(a.manual).length && r.basePrice) v+=r.basePrice*a.bases;
    const t=tiers.find(t=>tmax(t)==null||v<tmax(t));
    let maxU=0, maxN='', tot=0, reps=0, unk=0, pmax=0;
    const walk=(A,tag)=>A.nodes.forEach((o,i)=>{ const n=o.n; if(n.optional||n.onLost||['note','base','manual'].includes(n.do)) return; if(o.pUnknown) unk++; const u=(o.useTries||0)*(o.passes||1)*(tag?1:1); tot+=u; if(u>=2) reps++; if(tag) pmax=Math.max(pmax,u); if(u>maxU){ maxU=u; maxN=(tag||'')+(i+1)+':'+(n.cur||n.do); } });
    walk(a,''); const pr=S.prepRecipe?.(r); if(pr){ pr._an=null; walk(S.analyse(pr),'준비'); }
    const fr = !!r.prep || (r.start?.mods||[]).some(m=>m.fr);
    const om=[...exp].reduce((s,k)=>s+(a.tot[k]||0),0);
    return {id:r.id, d:r.difficulty, div:v, tier:t.id, maxU, maxN, tot, reps, om, bases:a.bases, miss, bp:r.basePrice||null, unk, fr, pmax}; }); });
const DN=['입문','쉬움','보통','어려움','전문가','극한'];
const L=rows.map(x=>[x.id, x.d+' '+DN[x.d], x.div.toFixed(1), x.tier, Math.round(x.maxU), x.maxN, Math.round(x.tot), x.reps, x.om.toFixed(1), x.bases.toFixed(2), x.bp??'-', x.miss.join('+'), x.unk, x.fr?1:0, Math.round(x.pmax)].join('\t'));
fs.writeFileSync('tier.txt', ['id\tdiff\tdiv\ttier\tmaxStepUses\tmaxStep\ttotalTries\trepeatSteps\texpOmens\tbases\tbasePrice\tnoPrice\tunknownSteps\tfractured\tprepMax', ...L].join('\n')+'\n');
console.log(fs.readFileSync('tier.txt','utf8'));
await b.close();})();
