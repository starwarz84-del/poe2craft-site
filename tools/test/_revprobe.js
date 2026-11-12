// 리버스 초안 후보 들여다보기(2026-11-12 도과장): node _revprobe.js <레시피id> [후보키]  (테스트 서버 필요)
// 후보마다 노하우·변형 키, 1차 시뮬 평균, 탈락 여부, 그리고 [후보키]를 주면 그 후보의 초안 단계를 출력
const {chromium}=require('playwright'); const fs=require('fs'); const {registered, ROOT}=require('./_regcard.js');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync(ROOT+'/site/data/recipes.json')));
const [id, want]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage(); p.on('pageerror',e=>console.error('E',e.message));
await p.goto('http://localhost:8779/discover.html?lang=kr'); await p.waitForFunction(()=>window.__rev && __rev.recSamples && __rev.recSamples.length);
await p.evaluate(async()=>{ const S=__rev; [S.index,S.craft]=await Promise.all([fetch('data/index.json').then(r=>r.json()),fetch('data/crafting.json').then(r=>r.json())]); S.priority=await fetch('data/priority.json').then(r=>r.json()); await S.ready; });
const r=R.find(x=>x.id===id), reg=registered(r, 200), buy=((r.start||{}).mods||[]).filter(m=>m.gi!=null && !m.crafted).map(m=>m.gi);
console.log('등록 div', reg.div.toFixed(1));
const x=await p.evaluate(async([id,card,buy,per,want])=>{ const S=__rev; const x=S.recSamples.find(s=>s.id===id); const it=await S.parse(x.text); const an=S.analyse(it);
  S.need=new Set(); S.soft=new Set(); S.tsel={}; S.buy=new Set(); S.noVariants=false; const took=new Set();
  card.forEach((l,ci)=>{ if(per[ci]<0.98) return; const i=an.rows.findIndex((r,k)=>!r.unrev && !took.has(k) && l.opts.some(o=>o.gi===r.m.gi)); if(i<0) return; const r=an.rows[i], o=l.opts.find(o=>o.gi===r.m.gi); took.add(i); if(r.m.fr) return;
    S.need.add(i); if(o.tmax) S.tsel[i]=Math.max(r.tierNo, Math.min(o.tmax, r.tierCnt)); if(buy.includes(r.m.gi) && r.how==='n') S.buy.add(i); });
  const rows=an.rows.map((r,i)=>(S.need.has(i)?'*':' ')+r.how+' '+r.m.side+' T'+r.tierNo+'/'+r.tierCnt+' '+(r.t?.[2]||'')+(r.m.fr?' [분열]':''));
  let a2=S.needAn(an,0,it); const bs=new Set([...S.buy].map(i=>an.rows[i]?.m).filter(Boolean)), o={market:1e9, ...(bs.size?{buy:bs}:{})};
  const bd=await S.bestDraftAsync(it,a2,o,null,0);
  const C=(S.lastC||[]).map(c=>({k:(c.K.k.join(',')||'-')+'|'+(c.k||'-'), mean:c.n?+(c.sum/c.n).toFixed(1):null, bad:c.bad, ok:!!c.ok}));
  let steps=null; const pick=(S.lastC||[]).find(c=>((c.K.k.join(',')||'-')+'|'+(c.k||'-'))===want);
  const show=d=>d.nodes.map(n=>[n.id, n.do, n.cur||'', (n.omens||[]).join('+'), JSON.stringify(n.target||{}).slice(0,90), JSON.stringify(n.fail||{}).slice(0,80), n.note?.kr?.slice(0,60)||''].join(' | '));
  if(pick){ const d=S.makeDraft(it, pick.K.a, {...o, ...pick.o}); steps=show(d); }
  return {rows, C, pick:bd.d.pick, kh:bd.d.knowhow, steps, best:show(bd.d)}; },[id,reg.card,buy,reg.per,want]);
console.log(x.rows.join('\n')); console.log('고른 것', JSON.stringify(x.pick), x.kh);
x.C.sort((a,b)=>(a.mean??1e9)-(b.mean??1e9)).forEach(c=>console.log((c.bad?'X ':c.ok?'✓ ':'  ')+c.k.padEnd(28)+c.mean));
console.log('--- 고른 초안'); console.log(x.best.join('\n'));
if(x.steps){ console.log('--- '+want); console.log(x.steps.join('\n')); }
await b.close(); })();
