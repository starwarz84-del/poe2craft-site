// 에뮬레이터 커런시 점검: 균열 반지 최대 퀄리티·균열의 에센스·심연의 에센스 징표·뼈 규칙 + 무작위 사용 반복(자리·계열·퀄리티 상한 확인)
// node tools/test/_emucur.js   (테스트 서버 8779)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1500,height:950}}); const errs=[]; p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8779/emulator.html?lang=kr&debug'); await p.waitForFunction(()=>window.__emu&&__emu.S.data);
 const out=await p.evaluate(async()=>{ const E=__emu, S=E.S, R=[]; const ok=(name,c,info='')=>R.push((c?'PASS ':'FAIL ')+name+(info?' — '+info:''));
  const cur=en=>Object.values(S.byId).find(x=>x.en===en);
  const omen=en=>{ const o=cur(en); S.omens.add(o.omen||o.id); };
  const warnOff=()=>{ const w=document.getElementById('warn'); if(w) w.hidden=true; };
  const use=(en)=>{ const c=cur(en); const why=E.check(c); if(why){ warnOff(); return why; } E.apply(c); return ''; };
  const pick=en=>{ const i=S.data.bases.findIndex(b=>b.en===en); E.newItem(i); };
  const makeRare=()=>{ use('Orb of Transmutation'); use('Regal Orb'); };
  await E.loadClass('Rings');
  // 1) 균열 반지: 기본 20 + 고정 20 = 40, 균열의 에센스 +20 = 60, 옵션이 지워져도 퀄리티 유지
  pick('Breach Ring'); ok('균열 반지 최대 퀄리티 40%', E.qmax()===40, E.qmax());
  makeRare(); const w=use('Essence of the Breach'); ok('균열의 에센스 사용', !w, w);
  ok('균열의 에센스 뒤 최대 60%', E.qmax()===60, E.qmax());
  const cat=Object.values(S.byId).find(x=>x.act==='catalyst' && x.on==='jewellery');
  for(let i=0;i<200 && !E.check(cat);i++) E.apply(cat); warnOff();
  ok('기폭제로 60%까지', S.item.quality===60, S.item.quality);
  const inf=cur('Vaal Catalysing Infuser'); ok('최대에서 기폭제는 막히고 주입기는 가능', !!E.check(cat) && !E.check(inf), E.check(inf));
  const mq=S.item.mods.find(m=>/Maximum Quality/.test(E.grp(m).t[m.ti][5]));
  S.item.mods.splice(S.item.mods.indexOf(mq),1); E.render();
  ok('옵션을 지워도 퀄리티 60% 유지', S.item.quality===60 && E.qmax()===40, `${S.item.quality}% / max ${E.qmax()}`);
  // 촉진하는 찬미의 징조: 퀄리티 0%, 최대 퀄리티 옵션은 남고, 다시 채우면 옵션이 있을 때만 60%까지
  pick('Breach Ring'); makeRare(); use('Essence of the Breach'); for(let i=0;i<200 && !E.check(cat);i++) E.apply(cat); warnOff();
  omen('Omen of Catalysing Exaltation'); const cw=use('Exalted Orb');
  ok('촉진 엑잘: 퀄리티 0%, 최대 퀄리티 옵션 유지', !cw && S.item.quality===0 && E.qmax()===60, cw||`${S.item.quality}% / max ${E.qmax()}`);
  for(let i=0;i<200 && !E.check(cat);i++) E.apply(cat); warnOff(); ok('다시 채우면 60%', S.item.quality===60, S.item.quality);
  omen('Omen of Catalysing Exaltation'); use('Exalted Orb'); const mq2=S.item.mods.find(m=>/Maximum Quality/.test(E.grp(m).t[m.ti][5])); S.item.mods.splice(S.item.mods.indexOf(mq2),1); E.render();
  for(let i=0;i<200 && !E.check(cat);i++) E.apply(cat); warnOff(); ok('옵션이 지워진 뒤엔 40%까지만', S.item.quality===40, S.item.quality);
  pick('Iron Ring'); makeRare(); omen('Omen of Catalysing Exaltation'); ok('퀄리티 없으면 촉진 엑잘 막힘', !!E.check(cur('Exalted Orb'))); S.omens.clear();
  pick('Refined Breach Ring'); ok('제련된 균열 반지 최대 45%', E.qmax()===45, E.qmax());
  makeRare(); use('Essence of the Breach'); ok('제련된 + 균열의 에센스 65%', E.qmax()===65, E.qmax());
  pick('Iron Ring'); ok('일반 반지 20%', E.qmax()===20, E.qmax());
  // 2) 심연의 에센스: 징표가 접두·접미 양쪽에 나옴, 뼈는 징표 자리를 훼손 옵션으로
  const sides={p:0,s:0};
  for(let k=0;k<40;k++){ pick('Iron Ring'); makeRare(); use('Orb of Augmentation'); if(use('Essence of the Abyss')) continue; const mk=S.item.mods.find(E.isMark); if(mk) sides[E.genOf(mk)]++; }
  ok('심연의 군주의 징표 양쪽 면', sides.p>3 && sides.s>3, JSON.stringify(sides));
  pick('Iron Ring'); makeRare(); use('Essence of the Abyss'); const mk=S.item.mods.find(E.isMark), g0=mk&&E.genOf(mk), n0=S.item.mods.length;
  const bone=Object.values(S.byId).find(x=>x.act==='desecrate' && x.part==='collar');
  const bw=use(bone.en); const un=S.item.mods.find(m=>m.unrev);
  ok('뼈: 징표가 훼손 옵션으로', !bw && !S.item.mods.some(E.isMark) && un && un.unrev===g0 && S.item.mods.length===n0, bw||`${g0} → ${un&&un.unrev}, ${n0}→${S.item.mods.length}`);
  // 3) 꽉 찬 면에 뼈: 그 면 옵션 하나가 지워지고 들어감
  pick('Iron Ring'); makeRare(); for(let i=0;i<8;i++) use('Exalted Orb');
  const full=['p','s'].every(g=>S.item.mods.filter(m=>E.genOf(m)===g).length===E.maxAff(g));
  const before=S.item.mods.length; const bw2=use(bone.en);
  ok('꽉 찬 아이템에 뼈 사용', full && !bw2 && S.item.mods.length===before && S.item.mods.some(m=>m.unrev), bw2||`${before}→${S.item.mods.length}`);
  // 4) 군주 징조는 무기·장신구만
  await E.loadClass('Body_Armours_str'); E.newItem(0); makeRare(); omen('Omen of the Liege');
  const rib=Object.values(S.byId).find(x=>x.act==='desecrate' && x.part==='rib' && !x.maxilvl); ok('갑옷에 군주 징조 막힘', !!E.check(rib), E.check(rib)); S.omens.clear();
  // 5) 무작위 사용: 클래스마다 커런시·징조를 아무거나 골라 쓰고 자리·계열·퀄리티 상한 확인
  const C=Object.values(S.byId).filter(x=>x.act && !['mirror','hinekora'].includes(x.act));
  const OM=Object.values(S.byId).filter(x=>x.omen);
  let n=0, bad=[];
  for(const cls of ['Rings','Amulets','Body_Armours_int','Bows','Wands','Gloves_str','Jewels','Quivers','Foci']){
    if(!S.index.groups.some(g=>g.classes.some(c=>c.id===cls))) continue;
    await E.loadClass(cls);
    for(let run=0;run<6;run++){ E.newItem(Math.floor(Math.random()*S.data.bases.length));
      for(let step=0;step<60;step++){
        if(S.reveal){ if(!S.reveal.opts.length){ const um=S.item.mods.find(m=>m.unrev); bad.push(`${cls}: 공개할 옵션 없음 (${um.unrev}${um.lord?' '+um.lord:''}, 뼈 ${um.bone})`); S.reveal=null; S.item.mods.splice(S.item.mods.indexOf(um),1); continue; } E.chooseReveal(Math.floor(Math.random()*S.reveal.opts.length)); continue; }
        if(S.item.mods.some(m=>m.unrev)){ E.startReveal(); continue; }
        if(Math.random()<0.3){ const o=OM[Math.floor(Math.random()*OM.length)]; S.omens.add(o.omen); }
        const ok2=C.filter(c=>!E.check(c)); if(!ok2.length) break; const c=ok2[Math.floor(Math.random()*ok2.length)];
        try{ E.apply(c); n++; }catch(e){ bad.push(cls+' '+c.en+': '+e.message); break; }
        const it=S.item;
        for(const g of ['p','s']){ const k=it.mods.filter(m=>E.genOf(m)===g).length; if(k>E.maxAff(g)) bad.push(`${cls} ${c.en}: ${g} ${k}>${E.maxAff(g)}`); }
        const fams=it.mods.filter(m=>!m.unrev).flatMap(m=>E.grp(m).f); if(new Set(fams).size!==fams.length) bad.push(`${cls} ${c.en}: 같은 계열 2개`);
        if(it.quality>E.qmax()+10 && !(it.corrupted)) bad.push(`${cls} ${c.en}: 퀄리티 ${it.quality} > ${E.qmax()+10}`);
        if(E.craftedCount()>E.craftedLimit()) bad.push(`${cls} ${c.en}: 제작 옵션 ${E.craftedCount()}>${E.craftedLimit()}`);
        if(it.rarity==='magic' && it.mods.length>2) bad.push(`${cls} ${c.en}: 마법 옵션 ${it.mods.length}`);
        if(it.corrupted || it.mirrored || it.sanctified) break;
      } S.omens.clear(); }
  }
  ok(`무작위 사용 ${n}번`, !bad.length, [...new Set(bad)].slice(0,12).join(' | '));
  return R; });
 out.forEach(x=>console.log(x)); console.log('페이지 오류', errs.length, errs.slice(0,3).join(' / ')); await b.close();
 process.exit(out.some(x=>x.startsWith('FAIL'))||errs.length?1:0); })();
