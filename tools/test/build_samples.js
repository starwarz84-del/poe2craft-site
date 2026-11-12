// Builds data/samples.json: each registered recipe's final item as English advanced (Ctrl+Alt+C) item text
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const out=await p.evaluate(()=>{const R=__rec;
  const mid = (t,k=1) => t.replace(/\((\d+(?:\.\d+)?)—(\d+(?:\.\d+)?)\)/g,(m,a,b)=>{ const x=(+a + +b)/2*k; return String(/\./.test(a+b)?(Math.floor(x*10)/10).toFixed(1):Math.floor(k>1?x:Math.round(x))); });
  const res=[];
  const known=new Set(R.index.groups.flatMap(g=>g.classes.map(c=>c.id)));
  for(const r of R.recipes.filter(x=>!x.draft && known.has(x.cls))){ let a; try{ a=R.analyse(r); }catch(e){ continue; }
    const D=R.cls[r.cls], b=D.bases[r.base]; const L=[];
    L.push(`Item Class: ${D.en}`,'Rarity: Rare','Recipe Sample',b.en,'--------');
    if(a.qual?.v) { L.push(`Quality${a.qual.type?` (${a.qual.type[0].toUpperCase()+a.qual.type.slice(1)} Modifiers)`:''}: +${a.qual.v}% (augmented)`,'--------'); }
    const sk = a.sockets ?? r.sockets ?? ((b.sock||0)+(r.exceptional?.sockets||0)); if(sk) L.push('Sockets: '+Array(sk).fill('S').join(' '),'--------');
    L.push(`Item Level: ${r.ilvl||82}`,'--------');
    const imp=(b.imp?.[0]||[]); if(imp.length){ imp.forEach(x=>L.push('{ Implicit Modifier }', mid(x)+' (implicit)')); L.push('--------'); }
    let n=0;
    for(const m of a.final){ if(m.gi==null) continue; const g=D.groups[m.gi]; const okT=Math.max(0,g.t.findIndex(x=>x[0]<=(r.ilvl||82))); const tn=(String(m.tag||'').match(/\d+/)||[])[0]; const ti=Math.min(g.t.length-1, Math.max(okT, tn?+tn-1:okT)); const t=g.t[ti];
      const side=g.g==='p'?'Prefix':'Suffix'; const kind=m.fr?'Fractured ':m.des?'Desecrated ':'';
      L.push(`{ ${kind}${side} Modifier "${t[3]}"${g.s==='n'?` (Tier: ${ti+1})`:''} }`);
      const k = a.qual?.type && g.tg.includes(a.qual.type) ? 1+a.qual.v/100 : 1; t[5].split('\n').forEach(x=>L.push(mid(x,k)+(m.fr?' (fractured)':m.des?' (desecrated)':''))); n++; }
    /* 2026-11-12: 랜덤 옵션·'물리 또는 원소' 같은 고르는 줄도 실제 완성품처럼 채움(빠지면 리버스가 빈자리로 보고 훨씬 싸게 계산함) — 그쪽에서 가장 흔한 옵션의 4티어쯤 */
    const used=new Set((a.final||[]).filter(m=>m.gi!=null).flatMap(m=>D.groups[m.gi].f||[])), ilv=r.ilvl||82;
    for(const m of (a.finalState||[]).filter(x=>x.gi==null && (x.side==='p'||x.side==='s'))){
      const c=D.groups.map((g,gi)=>({g,gi})).filter(({g,gi})=>(m.any?.length ? m.any.includes(gi) : g.s==='n') && g.g===m.side && !(g.f||[]).some(f=>used.has(f)) && g.t.some(t=>t[0]<=ilv && t[1]>0))
        .sort((x,y)=>y.g.t.reduce((s,t)=>s+(t[0]<=ilv?t[1]:0),0)-x.g.t.reduce((s,t)=>s+(t[0]<=ilv?t[1]:0),0))[0]; if(!c) continue;
      (c.g.f||[]).forEach(f=>used.add(f)); const ok=c.g.t.map((t,i)=>({t,i})).filter(x=>x.t[0]<=ilv && x.t[1]>0), pick=ok[Math.min(3, ok.length-1)];
      L.push(`{ ${m.des?'Desecrated ':''}${m.side==='p'?'Prefix':'Suffix'} Modifier "${pick.t[3]}" (Tier: ${pick.i+1}) }`); pick.t[5].split('\n').forEach(x=>L.push(mid(x)+(m.des?' (desecrated)':''))); n++; }
    res.push({id:r.id, title:r.title, base:{kr:b.kr,en:b.en}, n, text:L.join('\n')}); }
  return res;});
fs.writeFileSync('/home/claude/poe2data/site/data/samples.json', JSON.stringify({samples:out}));
console.log(out.length, out.map(x=>x.id+':'+x.n).join(' ')); console.log(out[0].text); await b.close();})();
