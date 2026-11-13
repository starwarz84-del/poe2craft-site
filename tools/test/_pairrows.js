// 시작·완성 카드 줄 맞춤 점검(2026-11-14 도과장): node _pairrows.js [레시피id…] (테스트 서버 8779) → 구분선 높이(1px이어야 함)·접두 첫 줄 위치 차이, 스크린샷 shots/pair-<id>.png
const {chromium}=require('playwright'); const fs=require('fs');
const R=(x=>x.recipes||x)(JSON.parse(fs.readFileSync('/home/claude/poe2data/site/data/recipes.json')));
const ids=process.argv.slice(2).length?process.argv.slice(2):R.filter(r=>!r.tierGroup||R.find(y=>y.tierGroup===r.tierGroup)===r).map(r=>r.id);
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1600,height:1000}}); let bad=0;
  await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForTimeout(4000);
  for(const id of ids){ await p.evaluate(id=>{ location.hash='r-'+id; }, id); await p.waitForTimeout(1200);
    const x=await p.evaluate(()=>{ const box=document.querySelector('[data-pair]'); if(!box) return null; const [a,b]=[...box.querySelectorAll('.tt-body')]; if(!a||!b) return null;
      const seps=[...box.querySelectorAll('.tt-sep')].filter(e=>e.offsetParent).map(e=>e.getBoundingClientRect().height); const big=seps.filter(h=>h>2).length;
      const top=t=>[...t.children].find(c=>/tt-mod/.test(c.className) && c.previousElementSibling && /tt-sep/.test(c.previousElementSibling.className) && [...t.children].indexOf(c)>[...t.children].findIndex(z=>z.classList.contains('tt-ench')));
      const pa=top(a), pb=top(b); const dy = pa&&pb ? Math.round(pa.getBoundingClientRect().top-pb.getBoundingClientRect().top) : null;
      return {big, dy}; });
    if(x && (x.big || (x.dy!=null && Math.abs(x.dy)>1))){ bad++; console.log(id, JSON.stringify(x)); const el=await p.$('[data-pair]'); if(el) await el.screenshot({path:__dirname+`/shots/pair-${id}.png`}); } }
  console.log('레시피', ids.length, '문제', bad); await b.close(); })();
