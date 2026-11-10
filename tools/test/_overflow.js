// 영문 화면에서 글자가 상자 밖으로 나가거나 짧은 이름표가 두 줄로 꺾이는 곳 찾기 → overflow.txt + shots/ov-*.png
// node tools/test/_overflow.js [탭…]   (배포 폴더 서버: cd web && python3 -m http.server 8790)
const {chromium}=require('playwright'), fs=require('fs');
const B='http://localhost:8790', TABS=process.argv.slice(2).length?process.argv.slice(2):['recipes','discover','emulator','builder','bases','about','r-xeno-phys-crossbow-v2','r-diztoh-crit-helmet-v2'];
const W=[1600,1280,1024,390];
(async()=>{ const br=await chromium.launch(), out=[];
  for(const w of W){ const p=await br.newPage({viewport:{width:w,height:900}});
    await p.addInitScript(()=>{ try{localStorage.setItem('poe2lang','en')}catch(e){} });
    for(const t of TABS){ await p.goto(`${B}/?lang=en&_=${t}${w}#${t}`); await p.waitForTimeout(t.startsWith('r-')?3500:2200);
      for(const f of p.frames()){ if(f===p.mainFrame()&&TABS.length) {} 
        let res=[]; try{ res=await f.evaluate(()=>{ const bad=[], seen=new Set();
          const vis=e=>{ const r=e.getBoundingClientRect(); return r.width>0&&r.height>0&&getComputedStyle(e).visibility!=='hidden'; };
          const name=e=>(e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(e.className&&typeof e.className==='string'?'.'+e.className.trim().split(/\s+/).slice(0,2).join('.'):''));
          for(const e of document.querySelectorAll('button,label,th,td,a,span,b,small,h1,h2,h3,h4,.chip,.badge,option,select,input,div')){
            if(!vis(e)) continue; const cs=getComputedStyle(e); const txt=(e.innerText||e.value||'').trim(); if(!txt||txt.length>60) continue;
            const kids=[...e.children].filter(vis);
            // 1) 글자가 자기 상자 밖으로 (잘리지 않게 한 곳)
            if(e.scrollWidth>e.clientWidth+2 && cs.textOverflow!=='ellipsis' && !['auto','scroll'].includes(cs.overflowX) && e.clientWidth>0 && kids.length===0){ bad.push(['넘침',name(e),txt.slice(0,40),e.scrollWidth+'>'+e.clientWidth]); continue; }
            // 2) 짧은 이름표가 줄바꿈
            if(e.querySelector('img,svg,canvas')||/\bbase\b|cbtn/.test(e.className)) continue; if(['BUTTON','LABEL','TH','A'].includes(e.tagName)||/btn|chip|tab|badge|pill|tag/.test(e.className)){ const lh=parseFloat(cs.lineHeight)||parseFloat(cs.fontSize)*1.3;
              if(txt.length<=24 && !txt.includes('\n') && e.getBoundingClientRect().height>lh*1.8+parseFloat(cs.paddingTop)+parseFloat(cs.paddingBottom)) bad.push(['줄바꿈',name(e),txt,Math.round(e.getBoundingClientRect().height)+'px']); }
          }
          // 3) 가로 스크롤
          if(document.documentElement.scrollWidth>innerWidth+1) bad.push(['가로스크롤','html','',document.documentElement.scrollWidth+'>'+innerWidth]);
          return bad; }); }catch(e){}
        const fn=f.url().split('/').pop().split('?')[0]||'shell';
        res.forEach(r=>{ const k=[w,t,fn,...r].join(' | '); out.push(k); });
      }
      if(w===1280||w===390) await p.screenshot({path:`tools/test/shots/ov-${t}-${w}.png`});
    }
    await p.close(); }
  const u=[...new Set(out)]; fs.writeFileSync('tools/test/overflow.txt',u.join('\n')+'\n'); console.log(u.length+' issues'); await br.close(); })();
