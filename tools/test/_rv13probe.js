// 사용자 반지(마나·희귀도 2개·시전 속도, RV13) 틀 짝짓기 점검: NEED=<gi,…|all> [PICK=1] node _rv13probe.js — ms = 잡힌 등록 틀, pick = 고른 초안·비용
const {chromium}=require('playwright'); const fs=require('fs');
const TXT=process.env.ITEM ? fs.readFileSync(process.env.ITEM,'utf8') : "Item Class: Ring\nRarity: Rare\nKraken Grasp\nGold Ring\n--------\nQuality (Mana Modifiers): +20% (augmented)\n--------\nRequires: Level 60\n--------\nItem Level: 82\n--------\n12% increased Rarity of Items found (implicit)\n--------\n+211 to maximum Mana\n18% increased Rarity of Items found\n20% increased Cast Speed\n+39% to Lightning Resistance\n7% increased maximum Mana (crafted)\n17% increased Rarity of Items found (desecrated)\n"; const NEED=process.env.NEED||'all';
(async()=>{ const b=await chromium.launch(); const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
const x=await p.evaluate(async([txt,NEED,PICK])=>{ const S=__rev; const it=await S.parse(txt); const an=S.analyse(it);
 const rows=an.rows.map((r,i)=>({i,gi:r.m?.gi,side:r.g?.side||r.side,s:r.g?.s,how:r.how,fr:r.m?.fr,unrev:r.unrev,tier:r.tierNo,cnt:r.tierCnt,l:r.line||r.text||r.m?.l}));
 S.need=new Set(); S.soft=new Set(); S.tsel={}; S.alt={}; S.altK={}; S.buy=new Set(); S.tplSkip=null;
 an.rows.forEach((r,i)=>{ if(!r.unrev && !r.m.fr && r.g && (NEED==='all'? r.m.gi!==undefined : NEED.split(',').includes(String(r.m.gi)))) S.need.add(i); });
 const a2=S.needAn(an,0,it); await S.loadTpl(); const ms=S.tplMatch(it,a2).map(m=>({g:m.t.g,ch:m.changed,grades:m.grades}));
 const a2rows=a2.rows.map(r=>({gi:r.m?.gi,side:r.side,gs:r.g?.side,s:r.g?.s,how:r.how,soft:r.soft}));
 let pick=null; if(PICK){ const bd=await S.bestDraftAsync(it,a2,{market:1e9},null,0); pick={tpl:bd.d?.tpl?.g||null, cmp:bd.d?.tpl?.cmp||S.tplCmp||null, why:S.tplWhy}; }
 return {rows,need:[...S.need],a2rows,ms,pick}; },[TXT,NEED,!!process.env.PICK]);
console.log(JSON.stringify(x,null,0).replace(/\},\{/g,'},\n{')); await b.close(); })();
