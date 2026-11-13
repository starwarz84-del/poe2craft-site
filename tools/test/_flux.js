// 에뮬레이터 유동체 점검(2026-11-13 도과장): node _flux.js  (테스트 서버 8779) → 반지에 저항 옵션을 붙이고 유동체 4종 적용, 스크린샷 shots/flux-*.png
const {chromium}=require('playwright');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1400,height:950}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  await p.goto('http://localhost:8779/emulator.html?lang=kr&debug'); await p.waitForFunction(()=>window.__emu && __emu.S.data,null,{timeout:60000});
  const out=await p.evaluate(async()=>{ const E=__emu, S=E.S; await E.loadClass('Rings');
    const G=S.data.groups, fam=f=>G.findIndex(g=>g.f.length===1 && g.f[0]===f && g.s==='n');
    const fire=fam('FireResistance'), cold=fam('ColdResistance'), mfire=fam('MaximumFireResistance');
    S.item.rarity='rare'; S.item.mods=[{gi:fire,ti:2,roll:.5},{gi:cold,ti:0,roll:.5,fr:true}].concat(mfire>=0?[{gi:mfire,ti:0,roll:.5}]:[]); E.render();
    const txt=()=>S.item.mods.map(m=>(m.fr?'[분열] ':'')+G[m.gi].f[0]+' T'+(m.ti+1)+' '+(G[m.gi].t[m.ti][5]||'')).join(' / ');
    const r={start:txt(), fluxIds:S.flux.map(x=>x.id+':'+x.kr)};
    for(const id of ['Void_Flux','Blazing_Flux']){ const c=S.byId[id]; r['check '+id]=E.check(c)||'ok'; E.apply(c); r['after '+id]=txt(); }
    S.item.mods=[{gi:fam('Strength'),ti:0,roll:.5}]; r['저항 없음']=E.check(S.byId.Chilling_Flux); S.item.rarity='normal'; r['일반']=E.check(S.byId.Chilling_Flux); return r; });
  console.log(JSON.stringify(out,null,1));
  await p.evaluate(()=>{ const E=__emu; E.S.item.rarity='rare'; E.S.item.mods=[{gi:E.S.data.groups.findIndex(g=>g.f[0]==='LightningResistance'&&g.s==='n'),ti:1,roll:.5}]; E.S.ctab='orb'; E.render(); });
  await p.screenshot({path:__dirname+'/shots/flux-orb.png', fullPage:false}); console.log('오류', errs); await b.close(); })();
