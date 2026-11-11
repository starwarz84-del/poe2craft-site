// rune limits (emulator, via the real click handler) + builder rules
const { chromium } = require('playwright');
(async () => {
  const br = await chromium.launch(); const pg = await br.newPage({ viewport: { width: 1400, height: 1000 } });
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto('http://localhost:8801/emu.html'); await pg.waitForFunction(() => window.__E && __E.S.item);
  const R = await pg.evaluate(async () => {
    const E = __E, S = E.S, R = []; const log = (n, ok, i = '') => R.push(`${ok ? 'OK ' : 'XX '} ${n}${i ? ' — ' + i : ''}`);
    const warnTxt = () => { const w = document.querySelector('#warn'); const t = w.hidden ? '' : document.querySelector('#warn-m').textContent; w.hidden = true; return t; };
    async function setup(cls) { await E.loadClass(cls); S.item.rarity = 'rare'; S.item.sockets = Math.max(2, E.maxSockets()); S.item.runes = []; S.ctab = 'rune'; S.mode = 'cur'; E.renderShelves(); }
    const find = name => { const rl = E.runesList(); for (let ri = 0; ri < rl.length; ri++) { const ti = rl[ri].t.findIndex(t => t[1] === name); if (ti >= 0) return { ri, ti }; } return null; };
    function sock(i, name) { const r = find(name); if (!r) return 'NO RUNE ' + name; S.sockSel = i; E.renderShelves(); const b = document.querySelector(`[data-rune="${r.ri}:${r.ti}"]`); if (!b) return 'NO BUTTON'; b.click(); return warnTxt(); }
    const names = () => S.item.runes.slice(0, S.item.sockets).map(r => r && E.runeAt(r)?.[1]);
    // body armour (2 sockets)
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, 'Desert Rune'); let w = sock(1, 'Desert Rune');
    log('일반 룬은 같은 것 2개 가능', !w && names().join() === 'Desert Rune,Desert Rune', w + ' ' + names());
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, 'Soul Core of Jiquani'); w = sock(1, 'Soul Core of Jiquani');
    log('Limited to 1 영혼핵 2개 막힘', !!w, w + ' ' + names());
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, 'Soul Core of Atmohua'); w = sock(1, 'Soul Core of Atmohua');
    log('제한 없는 영혼핵 2개 가능', !w, w + ' ' + names());
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, "Amanamu's Gaze"); w = sock(1, "Ulaman's Gaze");
    log('고대 증강물 2개 막힘', !!w, w + ' ' + names());
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, 'Legacy of Ashrend'); w = sock(1, 'Legacy of Blackbraid');
    log('유산 룬 2개 막힘', !!w, w + ' ' + names());
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, "Astrid's Creativity"); w = sock(1, "Astrid's Creativity");
    log('아스트리드의 창의성 2개 막힘', !!w, w + ' ' + names());
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, "Serle's Triumph"); w = sock(0, 'Desert Rune');
    log('세를의 승리(소켓 귀속) 덮어쓰기: 다른 빈 소켓으로', names()[0] === "Serle's Triumph", w + ' ' + names());
    sock(1, "Medved's Tending"); w = sock(0, 'Desert Rune');
    log('귀속 룬만 남으면 교체 막힘', !!w, w + ' ' + names());
    log('세를의 승리 → 접미 4', E.rareCap('s') === 4, 's cap ' + E.rareCap('s'));
    // same slot overwrite with same limited rune is fine
    await setup('Body_Armours_str'); S.item.sockets = 2;
    sock(0, 'Soul Core of Jiquani'); w = sock(0, 'Soul Core of Jiquani');
    log('같은 소켓에 같은 제한 룬 다시 끼우기 가능', !w, w);
    // Aldur runes: rare weapon only, empty socket
    await setup('Bows'); S.item.sockets = 2; S.item.rarity = 'magic';
    w = sock(0, 'Breath of Aldur'); log('알두르: 마법 무기 막힘', !!w, w);
    S.item.rarity = 'rare'; sock(0, 'Desert Rune') ; w = sock(0, 'Breath of Aldur'); log('알두르: 룬 있는 소켓 막힘', !!w || names()[0] === 'Breath of Aldur' && false, w + ' ' + names());
    w = sock(1, 'Breath of Aldur'); log('알두르: 희귀 무기 빈 소켓 가능', !w, w + ' ' + names());
    // all weapons have Aldur runes (사용자 확정 2026-11-11)
    const weapons = S.index.groups.filter(g => g.id === 'weapon' || g.id === 'weapon2').flatMap(g => g.classes.map(c => c.id));
    const miss = [];
    for (const c of weapons) { await E.loadClass(c); if (!E.maxSockets() || c === 'Traps') continue;   /* 덫은 무기 룬 대상인지 미확인 */ if (!find('Breath of Aldur')) miss.push(c); }
    log('알두르 룬: 소켓 있는 모든 무기에 있음', !miss.length, miss.join(','));
    // corrupted item: runes still socketable
    await setup('Body_Armours_str'); S.item.sockets = 2; S.item.corrupted = true; w = sock(0, 'Desert Rune');
    log('타락 아이템에 룬 장착 가능', !w, w);
    return R;
  });
  console.log(R.join('\n'));
  // ---------- builder ----------
  await pg.goto('http://localhost:8801/bld.html'); await pg.waitForFunction(() => window.__B && __B.S.data);
  const B = await pg.evaluate(async () => {
    const X = __B, S = X.S, R = []; const log = (n, ok, i = '') => R.push(`${ok ? 'OK ' : 'XX '} [속성부여] ${n}${i ? ' — ' + i : ''}`);
    const toastTxt = () => document.querySelector('#toast')?.textContent || '';
    async function cls(id) { await X.loadClass(id); }
    const groups = (pred) => S.data.groups.map((g, i) => ({ g, i })).filter(x => pred(x.g));
    await cls('Body_Armours_str');
    const des = groups(g => g.s === 'd' && g.t.some(t => t[0] <= S.ilvl));
    const d1 = des[0], d2 = des.find(x => !x.g.f.some(f => d1.g.f.includes(f)));
    X.assignAffix(d1.i); const r2 = X.reason(d2.i);
    log('훼손 옵션 2개 막힘', !!r2, r2 || '두 번째 훼손 허용됨');
    await cls('Body_Armours_str');
    const ess = groups(g => g.cr && g.s === 'e' && g.t.some(t => t[0] <= S.ilvl));
    X.assignAffix(ess[0].i); const e2 = ess.find(x => !x.g.f.some(f => ess[0].g.f.includes(f)) && x.g.g !== ess[0].g.g) || ess[1];
    log('제작 옵션 2개 막힘', !!X.reason(e2.i), X.reason(e2.i));
    await cls('Sapphire');
    log('주얼 접두 2·접미 2', X.maxOf('p') === 2 && X.maxOf('s') === 2, `${X.maxOf('p')}/${X.maxOf('s')}`);
    const liq = groups(g => g.cr && g.s === 'x');
    const l1 = liq.find(x => /Diluted Liquid Ire/.test(x.g.t[0][3])), l2 = liq.find(x => /Diluted Liquid Guilt/.test(x.g.t[0][3]));
    X.assignAffix(l1.i); log('액체 2개 가능(제작 옵션 한도에 안 셈)', !X.reason(l2.i), X.reason(l2.i));
    await cls('Sapphire');
    const con = liq.find(x => x.g.g === 'p' && /Contempt/.test(x.g.t[0][3]));
    X.assignAffix(con.i); log('경멸(+1 접미 허용) → 접미 3', X.maxOf('s') === 3, 's ' + X.maxOf('s'));
    // runes in builder
    await cls('Body_Armours_str');
    const find = name => { const rl = X.runesList(); for (let ri = 0; ri < rl.length; ri++) { const ti = rl[ri].t.findIndex(t => t[1] === name); if (ti >= 0) return { ri, ti }; } return null; };
    const two = (a, b) => { S.slots.k = [null, null, null, null]; const A = find(a), Bq = find(b); X.assignRune(A.ri, A.ti); X.assignRune(Bq.ri, Bq.ti); return S.slots.k.filter(Boolean).length; };
    log('Limited to 1 영혼핵 2개 막힘', two('Soul Core of Jiquani', 'Soul Core of Jiquani') === 1);
    log('고대 증강물 2개 막힘', two("Amanamu's Gaze", "Ulaman's Gaze") === 1);
    log('유산 룬 2개 막힘', two('Legacy of Ashrend', 'Legacy of Blackbraid') === 1);
    log('일반 룬 2개 가능', two('Desert Rune', 'Desert Rune') === 2);
    await cls('Bows'); S.slots.k = [null, null, null, null];
    log('알두르의 유산(고유 전용) 막힘', (() => { const A = find("Aldur's Legacy"); if (!A) return true; X.assignRune(A.ri, A.ti); return !S.slots.k.some(Boolean); })());
    // breach essence max quality
    await cls('Rings');
    const breach = groups(g => g.t.some(t => /to Maximum Quality/.test(t[5])) && g.s !== 'n');
    if (breach.length) { X.assignAffix(breach[0].i); log('균열의 에센스 최대 퀄리티 반영', X.maxQuality() >= 40, 'max ' + X.maxQuality()); }
    return R;
  });
  console.log(B.join('\n')); console.log('errors', errs);
  await br.close();
})();
