// 에뮬레이터 커런시 빠짐 점검(2026-11-13 도과장): node _emucover.js (테스트 서버 8779) — 모든 클래스·커런시 탭을 돌며 화면에 나온 버튼을 모아 crafting.json 전체와 비교
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:950}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/emulator.html?lang=kr&debug'); await p.waitForFunction(()=>window.__emu && __emu.S.data,null,{timeout:60000});
  const r=await p.evaluate(async()=>{ const E=__emu, S=E.S, seen=new Set(), classes=(await fetch('data/index.json').then(r=>r.json())).groups.flatMap(g=>g.classes.map(c=>c.id));
    for(const id of classes){ try{ await E.loadClass(id); }catch(e){ continue; } for(const rar of ['normal','magic','rare']){ S.item.rarity=rar; for(const t of ['orb','ess','breach','delir','exped','abyss','temple']){ S.ctab=t; E.render(); document.querySelectorAll('#shelves [data-id]').forEach(b=>seen.add(b.dataset.id)); document.querySelectorAll('#shelves [data-omen]').forEach(b=>seen.add('omen:'+b.dataset.omen)); } } }
    const C=S.craft, all=[]; for(const k of ['special','cats','liquids','qual','sac','orbs','bones','essences']) C[k].forEach(x=>all.push([k,x.id,x.kr])); C.omens.forEach(o=>all.push(['omens',o.id,o.kr]));
    const sample=[...seen].filter(x=>x.startsWith('omen')).slice(0,3);
    return {classes:classes.length, seen:seen.size, sample, missing:all.filter(([k,id])=>!seen.has(id) && !seen.has(id.replace('omen:',''))).map(x=>x.join(':'))}; });
  console.log(JSON.stringify(r,null,1)); console.log('오류', errs.slice(0,3)); await b.close(); })();
