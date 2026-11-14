// 리버스 빠른 시험(TOOL1 2026-11-14): 아이템 글 하나 → 발굴 탭 화면 그대로(붙여 넣기 → 분석 → 필수 고르기 → 초안 → 플로우차트 → 등급 레시피) → 짧은 보고서
// node tools/test/revtry.js <아이템.txt | 폴더 | ->   (표준 입력도 됨: cat item.txt | node revtry.js)
//   NEED=모두(기본 — 인식한 옵션 중 분열·미공개가 아닌 것 전부) | 'gi,gi'(그 옵션 그룹만 필수)     ※ 화면은 기본 필수가 없어 사용자가 고름
//   TIER=1|2|4 (또는 high|bal|ess): 필수 일반·훼손 옵션 티어 폭(1 = 하이엔드, 1~2 = 밸런스, 1~4 = 에센셜). 없으면 붙여 넣은 티어 그대로
//   CHIP=1: 필수 행마다 '다른 옵션도 성공' 칩 첫 번째를 고름     FAST=0: 초안 최소 10초(화면과 같음, 기본은 0초)
//   SHOT=1: 분석·플로우차트·레시피 스크린샷 → tools/test/revtry_out/<이름>-{an,fc,rc}.png     PORT=8779
// 결과: 화면에 요약 블록(여럿이면 끝에 표) + tools/test/revtry_out/<이름>.json. 테스트 서버(serve.sh)가 꺼져 있으면 켜고, 끝나도 끄지 않음
const {chromium}=require('playwright'); const fs=require('fs'), path=require('path'), {execSync}=require('child_process'), http=require('http');
const ROOT='/home/claude/poe2data', PORT=+(process.env.PORT||8779), OUT=__dirname+'/revtry_out';
const VN={high:'하이엔드', bal:'밸런스', ess:'에센셜'}, HOW={n:'일반', d:'훼손', e:'제작', fr:'분열', sc:'영혼핵', x:'별세계', lq:'액체'};
const fd=v=>v==null?'—':v>=100?Math.round(v).toLocaleString():v>=10?v.toFixed(0):v.toFixed(1);

function inputs(){ const a=process.argv[2];
  if(!a || a==='-'){ if(process.stdin.isTTY){ console.error('사용법: node tools/test/revtry.js <아이템.txt | 폴더 | ->'); process.exit(1); } return [{name:'stdin', txt:fs.readFileSync(0,'utf8')}]; }
  const st=fs.statSync(a); if(st.isDirectory()) return fs.readdirSync(a).filter(f=>/\.txt$/i.test(f)).sort().map(f=>({name:f.replace(/\.txt$/i,''), txt:fs.readFileSync(path.join(a,f),'utf8')}));
  return [{name:path.basename(a).replace(/\.[^.]+$/,''), txt:fs.readFileSync(a,'utf8')}]; }
const up=()=>new Promise(r=>{ const q=http.get(`http://localhost:${PORT}/discover.html`, s=>{ s.resume(); r(s.statusCode===200); }); q.on('error',()=>r(false)); q.setTimeout(1500,()=>{ q.destroy(); r(false); }); });

(async()=>{ const items=inputs(); if(!items.length){ console.error('아이템 글(.txt)이 없음'); process.exit(1); } fs.mkdirSync(OUT,{recursive:true});
  if(!(await up())){ execSync(`bash ${ROOT}/tools/test/serve.sh start`, {stdio:'ignore'}); for(let i=0;i<20 && !(await up());i++) await new Promise(r=>setTimeout(r,300)); }
  const b=await chromium.launch(), p=await b.newPage({viewport:{width:1400, height:1000}}); const perr=[]; p.on('pageerror',e=>perr.push(e.message));
  await p.goto(`http://localhost:${PORT}/discover.html?lang=kr`); await p.waitForFunction(()=>window.__rev && __rev.recSamples);
  const all=[];
  for(const itm of items){ const t0=Date.now(); perr.length=0; const name=itm.name.replace(/[^\w가-힣.-]+/g,'_');
    await p.evaluate(()=>{ __rev.last=null; }); await p.fill('#txt', itm.txt); await p.click('#go'); await p.waitForFunction(t=>__rev.last && __rev.txt===t && document.querySelector('#mk, #sum .empty.bad'), itm.txt, {timeout:30000}).catch(()=>{});   /* 앞 아이템 S.last가 남아 있으면 그걸 읽음 — 비우고 새 글로 다시 그려질 때까지 */
    /* 화면에서 필수·티어·칩을 고른 것처럼 상태를 맞추고 확인 칸 두 개를 체크한 상태로 다시 그림 */
    const pre=await p.evaluate(([NEED,TIER,CHIP,FAST])=>{ const HOWK={n:'일반', d:'훼손', e:'제작', fr:'분열', sc:'영혼핵', x:'별세계', lq:'액체'}; const S=__rev, a=S.last; if(a.err) return {err:a.err}; const it=a.it, an=a.an;
      const want = !NEED || /^(모두|all|auto)$/i.test(NEED) ? null : new Set(NEED.split(',').map(x=>+x.trim()));
      an.rows.forEach((r,i)=>{ if(r.unrev || r.m.fr || !r.g) return; if(want && !want.has(r.m.gi)) return; S.need.add(i); });
      const W = {1:1,2:2,4:4,high:1,bal:2,ess:4}[TIER];
      if(W) for(const i of S.need){ const r=an.rows[i]; if(!r.g?.t || !['n','d'].includes(r.how)) continue; const lo=Math.max(1, r.g.t.findIndex(t=>t[0]<=(it.ilvl||82))+1); S.tsel[i]=Math.max(r.tierNo, Math.min(lo+W-1, r.tierCnt)); }
      const chips=[]; if(CHIP) for(const i of S.need){ const x=S.altRecs(it, an, i)[0]; if(x){ S.alt[i]=x.list; S.altK[i]=x.k; chips.push({row:i, n:x.list.length, src:x.src?.kr||null}); } }
      S.okQR=true; S.unkOk=true; S.minDraftMs = FAST ? 0 : 10000;
      const rows=an.rows.map((r,i)=>({i, gi:r.m.gi, side:r.m.side, how:r.unrev?'미공개':(HOWK[r.how]||r.how), tier:r.tierNo, cnt:r.tierCnt, tsel:S.tsel[i]||null, need:S.need.has(i), txt:(r.t?.[4]||r.t?.[2]||'').replace(/\n/g,' / ')}));
      return {rows, chips, putrid:!!an.putrid, unrec:an.unrec||0, other:(it.other||[]).filter(o=>o.k==='?').map(o=>o.l||o.line||o.t||''), cls:it.cls, base:it.b?.kr, ilvl:it.ilvl, name:it.name}; }, [process.env.NEED||'', process.env.TIER||'', !!+(process.env.CHIP||0), process.env.FAST!=='0']).catch(e=>({err:e.message}));
    let res;
    if(pre.err || pre.putrid) res={...pre, probs:[pre.err||'훼손 옵션 2개(진행 불가 아이템)']};   /* 필수 없음(분열 옵션만 고름 등)도 화면처럼 그대로 초안 — 분열 옵션은 이미 붙어 있음 */
    else { /* render는 __rev에 없어서 다시 그리지 않고 #mk를 바로 누름 — 클릭 핸들러가 S.need·S.tsel·S.alt·S.okQR를 그대로 읽음 */
      await p.waitForSelector('#mk', {timeout:10000}); await p.evaluate(()=>{ const S=__rev; S.flow=null; S.draft=null; S.check=null; S.lastC=null; S.tplCmp=null; S.tplWhy={}; const m=document.querySelector('#mkmsg'); if(m) m.innerHTML=''; document.querySelector('#mk').click(); });
      const done = await p.waitForFunction(()=>{ const S=__rev; return S.flow && !S.flow.wait && S.draft && document.querySelector('#mkmsg .flow, #mkmsg .check') ? true : (document.querySelector('#mkmsg .mkwarn') ? 'warn' : false); }, null, {timeout:170000, polling:250}).then(h=>h.jsonValue()).catch(()=>'timeout');
      if(done!==true) res={...pre, probs:[done==='warn' ? '초안 버튼이 막힘: '+(await p.textContent('#mkmsg .mkwarn')) : '시간 초과(170초)']};
      else res=await p.evaluate(async(pre)=>{ for(let i=0;i<40 && __rev.boardR===undefined;i++) await new Promise(r=>setTimeout(r,100));
        /* reverse.html similarRecipes 복사본(__rev에 안 내보냄, 2026-11-14 기준) — 화면 '비슷한 등록 레시피' 목록과 같은 계산 */
        const simRec=(S, it, an)=>{ const B=S.boardR; if(!B) return []; const famK=gi=>{ const g=it.D.groups[gi]; return g ? g.f.join('+') : null; };
          const rows=an.rows.map((r,i)=>({r,i})).filter(({r})=>!r.unrev && r.g), marked=S.need.size || S.soft?.size;
          const want=rows.filter(({r,i})=>r.m.fr || !marked || S.need.has(i) || S.soft?.has(i)), must=rows.filter(({r,i})=>r.m.fr || S.need.has(i));
          const W=new Set(want.map(({r})=>r.g.f.join('+'))), FR=new Set(rows.filter(({r})=>r.m.fr).map(({r})=>r.g.f.join('+'))), out=[];
          for(const [id,b] of Object.entries(B)){ if(b.c!==it.cls || !b.f) continue; const lines=b.f.filter(x=>x.gi!=null), R=new Map(); lines.forEach(x=>{ const k=famK(x.gi); if(k) R.set(k, x); });
            const inter=[...W].filter(k=>R.has(k)).length, uni=new Set([...W, ...R.keys()]).size, sc=uni ? inter/uni : 0, rFR=new Set(lines.filter(x=>x.fr).map(x=>famK(x.gi)));
            const sameFr=FR.size===rFR.size && [...FR].every(k=>rFR.has(k));
            const same=must.length>0 && sameFr && must.every(({r,i})=>{ const x=R.get(r.g.f.join('+')); if(!x) return false; const w=Math.max(r.tierNo, S.tsel[i]||r.tierNo), tm=x.tm ?? r.g.t.length; return x.fr || tm<=w; });
            if(same || sc>=0.4) out.push({id, b, sc, same}); }
          out.sort((a,c)=>(c.same-a.same) || (c.sc-a.sc) || (a.b.d-c.b.d)); return out.slice(0,4); };
        const S=__rev, it=S.last.it, an=S.last.an, d=S.draft, F=S.flow, ck=S.check||[];
        const ord=['high','bal','ess'], gr=(F.res||[]).filter(x=>!F.off?.[x.id]).map(x=>({id:x.id, cost:x.cost??null, med:x.res?.useMedian??null, p90:x.res?.useP90??null, bases:x.res?.bases??null, reqOk:x.res?.reqOk??null, merged:F.merged?.[x.id]||null, none:!x.res}));
        /* 비슷한 등록 레시피(화면 '비슷한 등록 레시피' 칸과 같은 목록) — 그 레시피 플로우차트 시뮬 비용, 같은 등급 초안 비용과 나란히 */
        const sim=[]; for(const x of simRec(S, it, an)){ let c=null; try{ const j=await fetch(`data/sim/${encodeURIComponent(x.b.g)}.json`).then(r=>r.ok?r.json():null); const st=j && (j.strategies.find(s=>s.id===x.b.tr && !s.hidden) || j.strategies.find(s=>!s.hidden)); c=st?.res ? (st.res.useDiv ?? st.res.mean) : null; }catch(_){}
          const mine=gr.find(g=>g.id===x.b.tr && g.cost!=null) || null; sim.push({id:x.id, g:x.b.g, ti:x.b.ti?.kr||x.id, tr:x.b.tr, same:!!x.same, sc:+x.sc.toFixed(2), reg:c, draft:mine?mine.cost:null, k:(c && mine?.cost!=null) ? +(Math.max(mine.cost,1)/Math.max(c,1)).toFixed(2) : null}); }
        const tp=d?.tpl, cand=(S.lastC||[]).length, okC=(S.lastC||[]).filter(c=>!c.bad && c.n).length;
        const how = tp ? {kind:'tpl', g:tp.g, ti:tp.ti?.kr||tp.g, changed:tp.changed||0, gen:tp.cmp?.gen??null} : {kind:'gen', key:((d?.knowhow||[]).join(',')||'-')+'|'+(d?.pick ? (typeof d.pick==='string'?d.pick:(d.pick.k||'-')) : '-'), pick:d?.pick||null, tplCmp:S.tplCmp||null};
        const probs=[]; ck.filter(z=>z.lv==='err').forEach(z=>probs.push('검산 오류: '+z.kr)); (F.issues||[]).forEach(z=>probs.push('플로우차트: '+z.kr)); if(F.err) probs.push('플로우차트 실패: '+F.err);
        gr.forEach(g=>{ if(g.none) probs.push(`${g.id}: 진행 불가`); else if(!g.merged && g.reqOk!=null && g.reqOk<0.98) probs.push(`${g.id}: 필수 옵션 충족 ${Math.round(g.reqOk*100)}%`); });
        if(pre.unrec) probs.push(`인식 못 한 옵션 ${pre.unrec}개(잡옵으로 봄)`); if(!F.group) probs.push('올리기 불가(플로우차트 통과 실패)');
        const top=sim.find(s=>s.same) || sim[0]; if(top && top.k!=null && top.k>1.5) probs.push(`비슷한 등록 「${top.ti}」보다 ${top.k}배 비쌈`);
        const warns=ck.filter(z=>z.lv==='warn').map(z=>z.kr);
        return {...pre, top:d?.topGrade||null, diff:F.diff?.d??null, how, cand, okC, steps:F.lead?.nodes ? F.lead.nodes.filter(n=>n.do!=='note').length : (d?.nodes||[]).length, grades:gr, sim, warns, nErr:ck.filter(z=>z.lv==='err').length, probs,
          tplWhy:S.tplWhy||null, start:d?.start ? {rar:d.start.rar, mods:(d.start.mods||[]).length} : null, nodes:(F.lead?.nodes||d?.nodes||[]).map(n=>[n.id, n.do, n.cur||'', (n.omens||[]).join('+'), (n.note?.kr||'').slice(0,80)].join(' | '))}; }, pre);
      if(process.env.SHOT==='1' && res.grades){ try{ await p.locator('#mods').screenshot({path:`${OUT}/${name}-an.png`}); }catch(_){}
        try{ await p.locator('#mkmsg .flow').first().screenshot({path:`${OUT}/${name}-fc.png`, timeout:8000}); }catch(e){ (res.probs=res.probs||[]).push('스크린샷(플로우차트) 실패: '+e.message.split('\n')[0]); }
        try{ await p.waitForTimeout(1500); await p.locator('#pvf').screenshot({path:`${OUT}/${name}-rc.png`}); }catch(_){} } }
    res.name=itm.name; res.sec=+((Date.now()-t0)/1000).toFixed(1); if(perr.length) (res.probs=res.probs||[]).push('페이지 오류: '+perr[0]);
    fs.writeFileSync(`${OUT}/${name}.json`, JSON.stringify(res,null,1)); all.push(res); console.log(block(res)); }
  await b.close();
  if(all.length>1){ const L=['', '| 아이템 | 등급 | 비용(div) | 틀 | 문제 | 초 |', '|---|---|---|---|---|---|'];
    for(const r of all){ const g=(r.grades||[]).filter(x=>!x.merged && !x.none); L.push(`| ${r.name} | ${g.map(x=>VN[x.id]).join('·')||'—'} | ${g.map(x=>fd(x.cost)).join(' · ')||'—'} | ${r.how?.kind==='tpl'?'틀':r.how?'생성':'—'} | ${(r.probs||[]).length} | ${r.sec} |`); }
    console.log(L.join('\n')); }
})();

function block(r){ const o=[`■ ${r.name}${r.name!==r.base&&r.base?` — ${r.base}`:''}${r.cls?` (${r.cls}, 아이템 레벨 ${r.ilvl})`:''} · ${r.sec}초`];
  if(r.rows){ o.push('옵션'); for(const x of r.rows) o.push(`  ${x.need?'필수':'    '} ${x.side==='p'?'접두':x.side==='s'?'접미':'  ? '} ${x.how.padEnd(2)} T${x.tier}/${x.cnt}${x.tsel?`→T${x.tsel}`:''}  ${x.txt}  [gi ${x.gi}]`);
    if(r.chips?.length) o.push('  칩: '+r.chips.map(c=>`행 ${c.row} +${c.n}개${c.src?`(「${c.src}」)`:''}`).join(', ')); }
  if(r.how) o.push(r.how.kind==='tpl' ? `방법: 틀 「${r.how.ti}」 · ${r.how.changed?`옵션 ${r.how.changed}개 바꿈`:'옵션 그대로'}${r.how.gen!=null?` · 생성 후보 최저 ${fd(r.how.gen)} div`:''} · 후보 ${r.okC}/${r.cand}`
    : `방법: 생성 후보 ${r.how.key}${r.how.tplCmp?.tpl!=null?` · 틀 ${fd(r.how.tplCmp.tpl)} div보다 쌈`:''} · 후보 ${r.okC}/${r.cand}`);
  if(r.grades){ o.push(`결과 등급 ${VN[r.top]||VN[(r.grades.find(g=>!g.none&&!g.merged)||{}).id]||'—'} · 난이도 ${['입문','쉬움','보통','어려움','전문가','극한'][r.diff]||'—'} · 레시피 ${r.steps}단계 · 검산 오류 ${r.nErr} 주의 ${r.warns.length}`);
    for(const g of r.grades) o.push(`  ${(VN[g.id]||g.id).padEnd(4)} ${g.none?'진행 불가':g.merged?`${VN[g.merged]}와 합침`:`평균 ${fd(g.cost)} · 중앙 ${fd(g.med)} · 90% ${fd(g.p90)} div · 베이스 ${g.bases?.toFixed(1)} · 필수 ${g.reqOk>=0.98?'✓':Math.round(g.reqOk*100)+'%'}`}`); }
  if(r.sim?.length){ o.push('비슷한 등록 레시피'); for(const s of r.sim) o.push(`  ${s.same?'같은 구조':`비슷 ${Math.round(s.sc*100)}%`} 「${s.ti}」 ${VN[s.tr]||s.tr} ${fd(s.reg)} div${s.draft!=null?` · 초안 ${fd(s.draft)} (${s.k}배)`:''}`); }
  if(r.warns?.length) o.push('주의: '+r.warns.slice(0,4).join(' / ')+(r.warns.length>4?` 외 ${r.warns.length-4}`:''));
  o.push((r.probs||[]).length ? '문제\n'+r.probs.map(x=>'  - '+x).join('\n') : '문제 없음'); return o.join('\n'); }
