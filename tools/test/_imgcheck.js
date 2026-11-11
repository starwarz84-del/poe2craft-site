// 배포 폴더 탭마다 깨진 그림·404·콘솔 경고(미리 받기 안 씀 등) 점검
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(); let bad=0;
 for(const t of ['recipes','emulator','builder','bases','discover','about']){ const p=await b.newPage({viewport:{width:1400,height:900}}); const msgs=[], miss=[];
  p.on('console',m=>{ if(/warn|error/.test(m.type())) msgs.push(m.text().slice(0,140)); }); p.on('response',r=>{ if(r.status()>=400) miss.push(r.status()+' '+r.url()); });
  await p.goto('http://localhost:8790/#'+t); await p.waitForLoadState('networkidle'); await p.waitForTimeout(800);
  const fr=p.frames().find(f=>f.url().includes((t==='about'?'about':t)+'.html')) || p.mainFrame();
  const im=await fr.evaluate(()=>{ const a=[...document.images].filter(i=>i.getAttribute('src')); return {n:a.length, broken:a.filter(i=>i.complete && !i.naturalWidth).map(i=>i.getAttribute('src').slice(0,60))}; });
  const ok=!im.broken.length && !miss.length; if(!ok) bad++;
  console.log(t, '그림', im.n, '깨짐', im.broken.length, im.broken.slice(0,2).join(' '), '| 404', miss.slice(0,3).join(' '), '| 경고', msgs.filter(x=>!/googleapis/.test(x)).slice(0,3).join(' / '));
  await p.close(); }
 await b.close(); process.exit(bad?1:0);})();
