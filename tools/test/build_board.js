// data/board.json: 크래프팅 목록 카드용 요약(레시피마다 완성 옵션 줄·소모량·난이도·베이스) — 목록을 클래스 파일 없이 그려 첫 로딩을 빠르게
// 레시피를 바꿨으면 build_recipes.py 뒤에 실행(테스트 서버 필요). 레시피 내용이 바뀐 것은 화면이 해시로 알아채고 원래 계산을 씀
const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('pageerror',e=>console.log('E',e.message));
await p.goto('http://localhost:8779/recipes.html?lang=kr'); await p.waitForFunction(()=>window.__rec&&__rec.booted);
const out=await p.evaluate(async()=>{const R=__rec; const raw=(await fetch('data/recipes.json').then(r=>r.json())).recipes; const res={}; let bad=0;
  for(const r0 of raw){ const r=R.recipes.find(x=>x.id===r0.id); if(!r) continue;
    try{ await R.loadCls(r.cls); const lg=R.lang, by={};
      for(const k of ['kr','en']){ R.lang=k; delete r._an; by[k]=R.analyse(r); }
      R.lang=lg; delete r._an; const a=by.kr, ae=by.en, bs=R.baseOf(r);
      res[r.id]={h:R.recHash(r0), d:R.difficulty(r), c:r.cls, g:r.tierGroup||r.id, tr:r.tier||'high', ti:r.title, b:{kr:bs.kr, en:bs.en, img:bs.img},
        f:a.final.map((m,i)=>({gi:m.gi, x:[m.txt, ae.final[i].txt], tag:m.tag, tm:typeof m.tmax==='number'?m.tmax:null, fr:m.fr, des:m.des, ess:m.ess, max:m.max, g:m.g.g, s:m.g.s, tg:m.g.tg, t:[m.g.t[0][4], m.g.t[0][5]]})),
        fx:(a.finalX||[]).map((m,i)=>({x:[m.txt, (ae.finalX||[])[i]?.txt||m.txt], s:m.side, des:m.des, rnd:m.rnd, ...(m.fr?{fr:true}:{}), ...(m.tmax?{tm:m.tmax}:{})})),
        q:a.qual, tot:a.tot, totAll:a.totAll, manual:a.manual, bases:a.bases};
    }catch(e){ bad++; console.log('skip', r.id, e.message); } }
  return {res, bad};});
// 베이스 그림(data URI)은 파일로 빼서 주소만 남김 — 같은 베이스는 한 파일, 목록이 그림을 기다리지 않음
const crypto=require('crypto'), dir='/home/claude/poe2data/site/data/bimg'; fs.rmSync(dir,{recursive:true,force:true}); fs.mkdirSync(dir,{recursive:true});
for(const v of Object.values(out.res)){ const m=(v.b.img||'').match(/^data:image\/(\w+);base64,(.+)$/); if(!m) continue;
  const buf=Buffer.from(m[2],'base64'), f=crypto.createHash('sha1').update(buf).digest('hex').slice(0,12)+'.'+m[1]; fs.writeFileSync(dir+'/'+f, buf); v.b.img='data/bimg/'+f; }
fs.writeFileSync('/home/claude/poe2data/site/data/board.json', JSON.stringify({r:out.res}));
console.log(Object.keys(out.res).length, 'recipes, skipped', out.bad, Math.round(fs.statSync('/home/claude/poe2data/site/data/board.json').size/1024)+'KB'); await b.close();})();
