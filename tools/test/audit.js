const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.route(/fonts\./,r=>r.abort());
await p.goto('http://localhost:8779/recipes.html?lang=kr');await p.waitForTimeout(2500);
const res=await p.evaluate(async()=>{
  const C=await fetch('data/crafting.json').then(r=>r.json()); const names=new Set(); const walk=x=>{ if(Array.isArray(x)) x.forEach(walk); else if(x&&typeof x==='object'){ if(x.kr&&x.id) names.add(x.kr); Object.values(x).forEach(walk);} }; walk(C);
  const out=[];
  for(const r of __rec.recipes){ const a=__rec.analyse(r), iss=[];
    (r.start?.mods||[]).forEach(m=>{ if(m.junk) iss.push(`시작 아이템에 잡옵(${m.junk})`); });
    a.nodes.forEach((o,i)=>{ const n=o.n, t=n.target||{}, no=i+1, kr=(n.note&&n.note.kr)||'';
      if(o.warn) iss.push(`#${no} 경고: ${o.warn}`);
      if(n.do==='fracture'){ const ko=n.after?.keepOnly; if(!ko) iss.push(`#${no} 분열 후 정리(keepOnly) 없음`); else if(ko.length>2 || (ko.length===2 && ko[1]!=='junk1')) iss.push(`#${no} 분열 후 남기는 줄: ${JSON.stringify(ko)}`); }
      const specs=[]; const add=x=>{ if(!x) return; if(x.gi!=null) specs.push(x); (x.anyOf||[]).forEach(add); (x.all||[]).forEach(add); }; add(t); add(t.reveal);
      specs.forEach(sp=>{ if(sp.tmax && sp.tmax>2) iss.push(`#${no} 목표 티어 ${sp.tmax}티어까지 허용`); });
      if(o.pUnknown) iss.push(`#${no} 가중치 미확인`);
      if(/분열이라|지워지지 않음|안 지워짐/.test(kr)) iss.push(`#${no} 기본 상식 설명: "${kr.match(/.{0,15}(분열이라|지워지지 않음|안 지워짐).{0,10}/)[0]}"`);
      (kr.match(/[가-힣]+(?: [가-힣]+){0,3} (?:오브|에센스|징조|기폭제|합금)(?=[^가-힣]|$)/g)||[]).forEach(w=>{ const k=w.replace(/^(으로|로|와|과|및|후|그|이|첫|다음|한|두|세|각|더|약|또는|이후|아니면|먼저)\s/,''); if(![...names].some(nm=>k.endsWith(nm))) iss.push(`#${no} 이름 확인: "${k}"`); });
      const om=n.omens||[]; [['좌측 찬미','Sinistral_Exaltation'],['우측 찬미','Dextral_Exaltation'],['좌측 강령술','Sinistral_Necromancy'],['우측 강령술','Dextral_Necromancy'],['좌측 결정화','Sinistral_Crystallisation'],['우측 결정화','Dextral_Crystallisation']].forEach(([k,id])=>{ if(kr.includes(k) && !om.some(x=>x.includes(id)) && !JSON.stringify(n.fail||{}).includes(id)) iss.push(`#${no} 설명엔 "${k}"가 있는데 단계 징조엔 없음`); });
    });
    out.push({id:r.id, title:(r.title&&r.title.kr)||'', n:a.nodes.length, iss}); }
  return out; });
for(const r of res){ console.log(`\n## ${r.id} (${r.n}단계) ${r.title}`); r.iss.forEach(x=>console.log('  - '+x)); }
await b.close();})();
