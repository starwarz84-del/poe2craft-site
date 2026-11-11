// 완성품 점검: node tools/sim/fincheck.js [id…] — 전략마다 완성품이 완성품 카드(finals)의 옵션을 실제로 갖는 비율, 미공개 훼손·빈자리 남음
const fs=require('fs'),path=require('path'),SIM=require('../../site/sim.js'); const R=path.join(__dirname,'../..');
const ids=process.argv.slice(2).length?process.argv.slice(2):fs.readdirSync(`${R}/site/data/sim`).map(f=>f.replace('.json',''));
const c=JSON.parse(fs.readFileSync(`${R}/site/data/crafting.json`));
for(const id of ids){ let g; try{ g=JSON.parse(fs.readFileSync(`${R}/scripts/graphs/${id}.json`)); }catch(_){ continue; }
  const D=JSON.parse(fs.readFileSync(`${R}/site/data/c/${g.cls}.json`));
  for(const s of g.strategies){ if(s.hidden) continue;
    const fin=(g.finals||[]).find(f=>f.id===s.id || f.id===(s.final||'') || (s.id.startsWith(f.id))); if(!fin) { console.log(id,s.id,'완성품 카드 없음'); continue; }
    const tags=fin.lines.filter(l=>l.tag).map(l=>l.tag); const cnt={}, N=1500; let n=0, unrev=0, few=0; const want=fin.lines.length;
    const run=SIM.make(g,D,c,s.params), rnd=SIM.rng(5);
    let err=null; for(let i=0;i<N&&!err;i++) try{ run(rnd,{tally:{visit(){},use(){},base(){},skip(){},byCur(){},edge(){},done:(it,cond)=>{ n++;
      if(it.mods.some(m=>m.unrev||m.mark)) unrev++; if(it.mods.filter(m=>!m.rune).length<want) few++;
      for(const t of tags){ let ok=false; try{ ok=cond({has:t}); }catch(_){ } if(ok) cnt[t]=(cnt[t]||0)+1; } }}}); }catch(e){ err=e.message; }
    if(err){ console.log(id.padEnd(34),s.id.padEnd(12),'오류',err); continue; }
    const bad=tags.filter(t=>(cnt[t]||0)/n<0.999).map(t=>`${t} ${((cnt[t]||0)/n*100).toFixed(1)}%`);
    if(bad.length||unrev||few) console.log(id.padEnd(34),s.id.padEnd(12),'카드 옵션',bad.join(', ')||'-','| 미공개·징표',unrev,'| 옵션 부족',few,'/',n);
  } }
