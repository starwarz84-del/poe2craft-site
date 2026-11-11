// 건너뛴 과정 점검 (2026-11-11, 사용자: "중간과정을 건너뛰고 완성했다고 넘어간 경우가 없는지 전부 확인")
// 레시피마다 엔진(analyse)으로 단계별 아이템 상태를 따라가며 확인:
//  A 완성 상태에 미공개 훼손(U)·징표(M)가 남음  B 어떤 단계도 만들지 않은 옵션이 갑자기 생김(note·manual 단계에서 생기거나 목표가 아닌 옵션)
//  C 확률 0 단계  D 마지막 단계 뒤에도 빈자리(정보)  E 시작 상태와 완성 상태가 같음(아무것도 안 함)
// 실행: bash tools/test/serve.sh start → node tools/test/skipcheck.js > tools/test/skipcheck.txt
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(),p=await b.newPage();
await p.goto('http://localhost:8779/recipes.html?debug=1&lang=kr');await p.waitForFunction(()=>window.__rec&&__rec.booted,{timeout:60000});
const out=await p.evaluate(async()=>{
 const R=__rec, res=[];
 for(const r of R.recipes){
  if(r.draft) continue;
  let a; try{ if(R.loadCls) await R.loadCls(r.cls); a=R.analyse(r);}catch(e){ res.push({id:r.id,err:String(e).slice(0,120)}); continue; }
  const main=a.nodes.filter(o=>!o.n.fallbackFor && !o.n.onLost && !(o.n.branch && o.n.branch.when==='miss') && !o.n.optional);
  const key=m=>m.gi!=null?'g'+m.gi:(m.unrev?'U'+m.side:(m.mark?'M'+m.side:(m.junk?'J'+m.side:'?')));
  const issues=[]; let prev=(a.start||a.nodes[0]?.prev||[]);
  const st0=(main[0]?.state||[]);
  for(let i=0;i<main.length;i++){ const o=main[i], n=o.n, st=o.state||[]; const before=i?(main[i-1].state||[]):null;
    if(o.p===0 && n.do!=='note') issues.push(`C ${n.id} 확률 0 (${n.do} ${n.cur||''})`);
    if(before){ const bk=new Set(before.filter(m=>m.gi!=null).map(m=>m.gi));
      const tg=new Set([n.target?.gi, ...(n.target?.anyOf||[]).map(x=>x.gi), ...(n.target?.all||[]).map(x=>x.gi), n.target?.reveal?.gi, ...((n.target?.reveal?.anyOf)||[]).map(x=>x.gi)].filter(x=>x!=null));
      for(const m of st) if(m.gi!=null && !bk.has(m.gi) && !m.fr){
        if(n.do==='note'||n.do==='manual') issues.push(`B ${n.id} '${n.do}' 단계에서 옵션 gi${m.gi} 생김`);
        else if(tg.size && !tg.has(m.gi) && !['chaos','exalt','reveal','divine','essence','desecrate'].includes(n.do)) issues.push(`B ${n.id} ${n.do}: 목표가 아닌 gi${m.gi} 생김`);
      } } }
  const last=main[main.length-1], fin=last?.state||[];
  const U=fin.filter(m=>m.unrev).length, M=fin.filter(m=>m.mark).length;
  if(U) issues.push(`A 완성에 미공개 훼손 ${U}개`); if(M) issues.push(`A 완성에 징표 ${M}개`);
  const cnt=s=>fin.filter(m=>m.side===s).length, cap=a.cap||r.cap||{};
  if(cap.p!=null && (cnt('p')<cap.p || cnt('s')<cap.s)) issues.push(`D 빈자리 P ${cnt('p')}/${cap.p} S ${cnt('s')}/${cap.s}`);
  if(JSON.stringify(st0.map(key).sort())===JSON.stringify(fin.map(key).sort()) && main.length>2) issues.push('E 시작=완성');
  res.push({id:r.id, n:main.length, issues});
 }
 return res;});
let bad=0; for(const x of out){ if(x.err){console.log(x.id,'ERR',x.err); bad++; continue;} const real=x.issues.filter(s=>!s.startsWith('D')); if(x.issues.length) console.log(x.id, `(${x.n}단계)`, '\n   '+x.issues.join('\n   ')); if(real.length) bad++; }
console.log(`\n${out.length} recipes, ${bad} with A/B/C/E issues`);
await b.close();})();
