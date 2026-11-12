// 플로우차트 완성품 카드(.fcfin)와 그 등급 레시피 탭 완성 카드가 똑같이 보이는지 전수 점검(2026-11-12, 사용자: 두 카드가 같아야 함)
// 테스트 서버 :8779 필요. node _fccardsame.js [레시피 id…] → 콘솔 + fccardsame.txt (차이 0이어야 함)
// 비교: 이름, 베이스 정보 줄(방어도·퀄리티·아이템 레벨·룬 소켓 등), 줄 순서·개수, P/S/R 표시와 티어 태그, 문구, 계산된 색·기울임, 소켓·룬 줄, P/S/R 개수 줄, 스킬 부여·성유 줄
const {chromium}=require('playwright'), fs=require('fs');
const want=process.argv.slice(2);
(async()=>{ const b=await chromium.launch(), p=await b.newPage({viewport:{width:1500,height:1100}}); const out=[]; let tot=0, cards=0;
  const errs=[]; p.on('pageerror',e=>errs.push(String(e).slice(0,200)));
  await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec && __rec.booted);
  const all=await p.evaluate(()=>__rec.recipes.filter(r=>r.sim).map(r=>({id:r.id, grp:r.tierGroup||r.id})));
  const groups=[...new Set(all.map(r=>r.grp))].filter(g=>!want.length || want.includes(g) || all.some(r=>r.grp===g && want.includes(r.id)));
  const read = sel => p.$eval(sel, tt=>{ const rows=[]; const cs=e=>{ const c=getComputedStyle(e); return c.color+(c.fontStyle==='italic'?' italic':''); };
    rows.push('이름 | '+(tt.querySelector('.tt-name')?.innerText||'').trim());
    tt.querySelectorAll('.tt-body > *').forEach(e=>{
      if(e.classList.contains('tt-art')) return;
      if(e.classList.contains('tt-props')){ e.querySelectorAll('.tt-prop').forEach(x=>rows.push('속성 | '+x.innerText.replace(/\s+/g,' ').trim()+' | '+cs(x.querySelector('b')||x))); return; }
      if(e.classList.contains('tt-sep')){ rows.push('구분선'); return; }
      if(e.classList.contains('tt-gap')){ rows.push('간격'); return; }
      if(e.classList.contains('tt-cnt')){ rows.push('개수 | '+e.innerText.replace(/\s+/g,' ').trim()); return; }
      if(e.classList.contains('tt-ench')){ e.querySelectorAll('.tt-mod').forEach(x=>rows.push('부여 | '+x.innerText.replace(/\s+/g,' ').trim()+' | '+cs(x))); return; }
      if(e.classList.contains('tt-mod')){ const t=e.querySelector('.tier'); rows.push(`옵션 | ${t?t.innerText.trim():''} | ${e.innerText.replace(t?t.innerText:'','').replace(/\s+/g,' ').trim()} | ${cs(e)} | 티어색 ${t?getComputedStyle(t).color:''}`); return; }
      rows.push('기타 | '+e.className+' | '+e.innerText.replace(/\s+/g,' ').trim()); });
    return rows; });
  for(const g of groups){
    await p.goto('about:blank'); await p.goto(`http://localhost:8779/recipes.html?lang=kr#r-${g}`); await p.waitForFunction(()=>window.__rec && __rec.booted); await p.waitForSelector('#detail .ovw', {timeout:15000}).catch(()=>{});
    const tabs=await p.$$eval('[data-rtab]', xs=>[...new Set(xs.map(x=>x.getAttribute('data-rtab')).filter(t=>t!=='fc'))]);
    const rec={};
    for(const t of tabs){ await p.click(`.rtabs [data-rtab="${t}"], [data-rtab="${t}"]`); await p.waitForTimeout(500);
      rec[t]=await read('#detail .ovw .ostart > div:last-child .tt').catch(()=>null); }
    if(!await p.$('[data-rtab="fc"]')){ out.push(`${g}: 플로우차트 탭 없음`); continue; }
    await p.click('[data-rtab="fc"]'); await p.waitForSelector('.fcfins .fcfin', {timeout:15000}).catch(()=>{});
    const fins=await p.$$eval('.fcfins .fcfin', xs=>xs.map(x=>x.getAttribute('data-rtab')));
    for(const t of tabs){ cards++;
      if(!rec[t]){ out.push(`${g} [${t}] 레시피 탭 완성 카드 없음`); tot++; continue; }
      if(!fins.includes(t)){ out.push(`${g} [${t}] 플로우차트 완성품 카드 없음(카드: ${fins.join(', ')})`); tot++; continue; }
      const F=await read(`.fcfins .fcfin[data-rtab="${t}"] .tt`);
      const R=rec[t], n=Math.max(R.length, F.length), diff=[];
      for(let i=0;i<n;i++) if(R[i]!==F[i]) diff.push(`  ${i+1}번째 줄\n    레시피: ${R[i]??'(없음)'}\n    플로차트: ${F[i]??'(없음)'}`);
      if(R.length!==F.length) diff.unshift(`  줄 수 레시피 ${R.length} · 플로우차트 ${F.length}`);
      if(diff.length){ tot++; out.push(`${g} [${t}] 차이 ${diff.length}\n${diff.join('\n')}`); } } }
  out.push(`카드 ${cards}장 · 다른 카드 ${tot}장 · 페이지 오류 ${errs.length}${errs.length?' — '+errs.slice(0,3).join(' | '):''}`);
  fs.writeFileSync('fccardsame.txt', out.join('\n')); console.log(out.slice(-1)[0]); await b.close(); })();
