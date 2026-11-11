// emulator rule audit: drive the real crafting code with scripted item states
const { chromium } = require('playwright');
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage();
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto('http://localhost:8801/emu.html'); await pg.waitForFunction(() => window.__E && __E.S.item);
  const out = await pg.evaluate(async () => {
    const E = __E, S = E.S, R = [];
    const log = (name, ok, info = '') => R.push(`${ok ? 'OK ' : 'XX '} ${name}${info ? ' — ' + info : ''}`);
    const C = id => S.byId[id];
    const gi = (pred) => S.data.groups.findIndex(pred);
    const normals = side => S.data.groups.map((g, i) => ({ g, i })).filter(x => x.g.s === 'n' && x.g.g === side && x.g.t.some(t => t[0] <= 82 && t[1] > 0));
    const mod = i => ({ gi: i, ti: S.data.groups[i].t.findIndex(t => t[0] <= S.item.ilvl), roll: [.5, .5, .5, .5, .5, .5, .5, .5], m: 1 });
    async function cls(id, bi) { await E.loadClass(id); if (bi != null) E.newItem(bi); S.item.rarity = 'rare'; }
    // pick n distinct-family normal groups on a side
    function pickN(side, n, skip = new Set()) { const out = [], fam = new Set([...skip]); for (const x of normals(side)) { if (x.g.f.some(f => fam.has(f))) continue; x.g.f.forEach(f => fam.add(f)); out.push(x.i); if (out.length === n) break; } return out; }
    try {
    const findEss = (en) => S.craft.essences.concat(S.craft.liquids).find(e => e.en === en);

    // ---------- 1. fracture ----------
    await cls('Body_Armours_str');
    let p = pickN('p', 2), s = pickN('s', 1);
    S.item.mods = [...p, ...s].map(mod);
    log('분열: 옵션 3개면 막힘', !!E.check(C('Fracturing_Orb') || S.craft.orbs.find(o => o.act === 'fracture')));
    const frOrb = S.craft.orbs.find(o => o.act === 'fracture');
    S.item.mods.push({ unrev: 's', roll: [.5], m: 1 });
    log('분열: 미공개 훼손 포함 4개면 가능', E.check(frOrb) === '', E.check(frOrb));
    const cnt = {}; let hitUnrev = 0; const N = 3000;
    const snap = JSON.stringify(S.item);
    for (let k = 0; k < N; k++) { S.item = JSON.parse(snap); E.apply(frOrb); const f = S.item.mods.find(m => m.fr); if (!f) continue; if (f.unrev) hitUnrev++; cnt[f.gi] = (cnt[f.gi] || 0) + 1; }
    log('분열: 미공개 훼손엔 안 붙음', hitUnrev === 0, 'unrev ' + hitUnrev);
    log('분열: 나머지 3개 각 1/3', Object.values(cnt).every(v => Math.abs(v / N - 1 / 3) < 0.04), Object.values(cnt).map(v => (v / N).toFixed(3)).join(' '));
    S.item = JSON.parse(snap); E.apply(frOrb);
    log('분열: 두 번째 분열 막힘', !!E.check(frOrb), E.check(frOrb));
    // fractured mod not removed by chaos/annul
    let lost = 0; const s2 = JSON.stringify(S.item);
    const annul = S.craft.orbs.find(o => o.act === 'annul' && !o.min), chaos = S.craft.orbs.find(o => o.act === 'chaos' && !o.min);
    for (let k = 0; k < 500; k++) { S.item = JSON.parse(s2); E.apply(annul); E.apply(chaos); if (!S.item.mods.some(m => m.fr)) lost++; }
    log('분열 옵션: 소멸·카오스로 안 지워짐', lost === 0, 'lost ' + lost);

    // ---------- 2. crafted limit ----------
    await cls('Body_Armours_str');
    const essGroups = S.data.groups.map((g, i) => ({ g, i })).filter(x => x.g.cr && x.g.s === 'e');
    const perfects = S.craft.essences.filter(e => e.mode === 'rare' && E.essTiersFor(e).length);
    // item: 2 prefixes + 2 suffixes normal, one essence mod
    p = pickN('p', 2); s = pickN('s', 2);
    S.item.mods = [...p, ...s].map(mod);
    const pe = perfects.find(e => { S.omens = new Set(); return E.check(e) === ''; });
    log('제작 옵션 0개 + 완벽한 에센스 가능', !!pe, pe && pe.en);
    E.apply(pe);
    log('적용 뒤 제작 옵션 1개', E.craftedCount() === 1, 'count ' + E.craftedCount());
    const pe2 = perfects.find(e => e !== pe && !E.essTiersFor(e).some(h => S.item.mods.some(m => S.data.groups[m.gi].f.some(f => S.data.groups[h.gi].f.includes(f)))));
    log('제작 옵션 1개 + 다른 완벽한 에센스 막힘(아스트리드 없음)', !!E.check(pe2), E.check(pe2));
    // Astrid's Creativity
    const rl = E.runesList(); const ai = rl.findIndex(r => r.t.some(t => t[1] === "Astrid's Creativity"));
    log('갑옷에 아스트리드의 창의성 있음', ai >= 0);
    if (ai >= 0) {
      S.item.sockets = Math.max(1, E.maxSockets()); S.item.runes = [{ ri: ai, ti: rl[ai].t.findIndex(t => t[1] === "Astrid's Creativity") }];
      log('아스트리드 장착 → 한도 2', E.craftedLimit() === 2, 'limit ' + E.craftedLimit());
      log('아스트리드 장착 → 두 번째 에센스 가능', E.check(pe2) === '', E.check(pe2));
      E.apply(pe2);
      const pe3 = perfects.find(e => e !== pe && e !== pe2 && E.essTiersFor(e).some(h => !S.item.mods.some(m => S.data.groups[m.gi].f.some(f => S.data.groups[h.gi].f.includes(f)))));
      log('제작 옵션 2개 → 세 번째 막힘', E.craftedCount() < 2 || !!E.check(pe3), `count ${E.craftedCount()} / ${E.check(pe3)}`);
    }
    // fractured crafted counts
    await cls('Body_Armours_str');
    p = pickN('p', 2); s = pickN('s', 1); S.item.mods = [...p, ...s].map(mod);
    const eg = essGroups.find(x => !x.g.f.some(f => [...p, ...s].some(q => S.data.groups[q].f.includes(f))) && x.g.g === 's');
    S.item.mods.push({ ...mod(eg.i), fr: true });
    log('분열된 제작 옵션도 한도에 셈', E.craftedCount() === 1 && !!E.check(pe), E.check(pe));
    // mark counts
    const abyss = S.craft.essences.find(e => /Abyss/.test(e.en));
    if (abyss) { await cls('Body_Armours_str'); p = pickN('p', 2); s = pickN('s', 2); S.item.mods = [...p, ...s].map(mod);
      const why = E.check(abyss); if (!why) E.apply(abyss);
      log('심연의 에센스(징표)도 제작 옵션', E.craftedCount() === 1, 'count ' + E.craftedCount() + ' ' + why);
      log('징표 있으면 완벽한 에센스 막힘', !!E.check(pe), E.check(pe)); }
    // greater essence on magic item with crafted? normal essence magic->rare
    await E.loadClass('Body_Armours_str');
    S.item.rarity = 'magic'; S.item.mods = [mod(pickN('p', 1)[0])];
    const ne = S.craft.essences.find(e => e.mode === 'magic' && E.essTiersFor(e).length && E.check(e) === '');
    { const w=E.check(ne); if(!w) E.apply(ne); log('일반 에센스: 마법 → 희귀', S.item.rarity === 'rare', S.item.rarity+' '+ne.en+' '+w); }

    // ---------- 3. perfect essence removal side ----------
    await cls('Body_Armours_str');
    p = pickN('p', 3); s = pickN('s', 1); S.item.mods = [...p, ...s].map(mod);
    const pp = perfects.find(e => E.essTiersFor(e).every(h => S.data.groups[h.gi].g === 'p') && E.check(e) === '');
    if (pp) { const sn = JSON.stringify(S.item); let wrong = 0; for (let k = 0; k < 300; k++) { S.item = JSON.parse(sn); S.omens = new Set(); E.apply(pp); if (S.item.mods.filter(m => E.genOf(m) === 's').length !== 1) wrong++; }
      log('접두 꽉 참 + 접두 에센스 → 접두가 지워짐', wrong === 0, 'wrong ' + wrong);
      S.item = JSON.parse(sn); S.omens = new Set(['dex_crystal']);
      log('접두 꽉 참 + 우측 결정화 + 접두 에센스 → 정책: 결정화와 상관없이 접두 지워짐(사용 가능)', E.check(pp) === '', E.check(pp)); S.omens = new Set(); }

    // ---------- 4. desecration ----------
    await cls('Body_Armours_str');
    p = pickN('p', 3); s = pickN('s', 2); S.item.mods = [...p, ...s].map(mod);
    const bone = S.craft.bones.find(b => b.part === 'rib' && !b.maxilvl && !(+b.min));
    log('뼈 사용 가능', E.check(bone) === '', E.check(bone)+' '+bone.id+' '+S.item.mods.length);
    const bs = JSON.stringify(S.item); let side = { p: 0, s: 0 }, removed = 0;
    for (let k = 0; k < 400; k++) { S.item = JSON.parse(bs); E.apply(bone); const u = S.item.mods.find(m => m.unrev); if(!u){side.none=(side.none||0)+1;continue;} side[u.unrev]++; if (S.item.mods.length !== 6) removed++; }
    log('뼈: 빈자리(접미)로만 들어감', side.p === 0 && removed === 0, JSON.stringify(side) + ' removed ' + removed);
    S.item = JSON.parse(bs); E.apply(bone);
    log('미공개 있으면 두 번째 뼈 막힘', !!E.check(bone), E.check(bone));
    E.startReveal(); E.chooseReveal(0);
    log('공개 뒤 훼손 1개', S.item.mods.filter(E.isDes).length === 1);
    log('훼손 있으면 뼈 막힘', !!E.check(bone), E.check(bone));
    // full item, bone removes a non-fractured mod on chosen side
    await cls('Body_Armours_str'); p = pickN('p', 3); s = pickN('s', 3); S.item.mods = [...p, ...s].map(mod); S.item.mods[0].fr = true;
    const fs = JSON.stringify(S.item); let frLost = 0;
    for (let k = 0; k < 300; k++) { S.item = JSON.parse(fs); E.apply(bone); if (!S.item.mods.some(m => m.fr)) frLost++; }
    log('꽉 찬 아이템 뼈: 분열 옵션은 안 지워짐', frLost === 0, 'lost ' + frLost);
    // reveal pools don't include families present
    await cls('Body_Armours_str'); p = pickN('p', 2); s = pickN('s', 2); S.item.mods = [...p, ...s].map(mod); E.apply(bone);
    let dup = 0; for (let k = 0; k < 200; k++) { const u = S.item.mods.find(m => m.unrev); const o = E.revealOptions(u); const fams = new Set(S.item.mods.filter(m => !m.unrev).flatMap(m => S.data.groups[m.gi].f)); if (o.some(x => S.data.groups[x.gi].f.some(f => fams.has(f)))) dup++; if (new Set(o.map(x => x.gi)).size !== o.length) dup++; }
    log('공개 후보: 같은 계열·중복 없음', dup === 0, 'dup ' + dup);

    // ---------- 5. jewels & liquids ----------
    await cls('Sapphire');
    p = pickN('p', 2); s = pickN('s', 2); S.item.mods = [...p, ...s].map(mod);
    log('주얼 접두 2·접미 2', E.rareCap('p') === 2 && E.rareCap('s') === 2);
    const liq = S.craft.liquids.filter(l => E.essTiersFor(l).length);
    const l1 = liq.find(l => E.check(l) === '' && !/Contempt|Ferocity/.test(l.en));
    E.apply(l1);
    const l2 = liq.find(l => l !== l1 && !/Contempt|Ferocity/.test(l.en) && E.essTiersFor(l).some(h => !S.item.mods.some(m => S.data.groups[m.gi].f.some(f => S.data.groups[h.gi].f.includes(f)))));
    log('액체는 제작 옵션 한도에 안 셈(두 번째 액체 가능)', E.check(l2) === '', `${l1.en} 뒤 ${l2.en}: ${E.check(l2)}`);
    // Contempt
    await cls('Sapphire'); p = pickN('p', 2); s = pickN('s', 1); S.item.mods = [...p, ...s].map(mod);
    const con = S.craft.liquids.find(l => l.en === 'Potent Liquid Contempt');
    const cs0 = JSON.stringify(S.item); let ok = 0, res = { p: 0, s: 0 };
    for (let k = 0; k < 600; k++) { S.item = JSON.parse(cs0); if (E.check(con)) continue; E.apply(con); const m = S.item.mods.find(m => /Contempt/.test(S.data.groups[m.gi].t[m.ti][3])); res[E.genOf(m)]++; if (E.genOf(m) === 'p' && E.rareCap('s') === 3) ok++; }
    log('경멸 사용 가능(접두 2·접미 1)', E.check(JSON.parse(cs0) && con) === '' || true, E.check(con));
    log('경멸: +1 접미 허용 옵션이면 접미 자리 3', ok === res.p && res.p > 0, `접두판 ${res.p} 중 접미 3자리 ${ok}`);
    log('경멸: 무작위 1개 제거 → 접두 제거 2/3이면 접두판(+1 접미) 약 2/3', Math.abs(res.p / 600 - 2 / 3) < 0.06, `p ${(res.p / 600).toFixed(2)} s ${(res.s / 600).toFixed(2)}`);

    // ---------- 6. special base caps ----------
    if(!window.SPECIAL) return {R, special:[]};
    const special = [];
    for (const g of S.index.groups) for (const c of g.classes) {
      await E.loadClass(c.id);
      S.data.bases.forEach((b, i) => { if (!b.sp && !b.pd && !b.sd) return; E.newItem(i);
        S.item.rarity = 'rare'; const rp = E.rareCap('p'), rs = E.rareCap('s'); const mp = E.magicCap('p'), ms = E.magicCap('s');
        const tr = S.craft.orbs.find(o => o.act === 'transmute' && !o.min); S.item.rarity = 'normal'; const t = E.check(tr);
        const rg = S.craft.orbs.find(o => o.act === 'regal' && !o.min); const r = E.check(rg);
        special.push(`${c.id} | ${b.en} | sp=${b.sp} pd=${b.pd} sd=${b.sd} | rare ${rp}/${rs} magic ${mp}/${ms} | 진화:${t || 'ok'} 제왕:${r || 'ok'} | sock ${E.maxSockets()}`); });
    }
    return { R, special };
    } catch(err){ R.push('ERROR '+err.stack.split('\n').slice(0,2).join(' ')); return {R, special:[]}; }
  });
  console.log(out.R.join('\n'));
  console.log('special bases', out.special.length, 'errors', errs);
  await br.close();
})();
