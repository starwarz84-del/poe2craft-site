# Step notes are short (사용자 확정 2026-11-09): a step shows only its target and currency (head + target line on screen);
# a note is kept only for the start, the finish, and forks/choices, and then says just the branch. None = no note.
# Steps that already show a currency and a target hide their note in recipes.html, so only these steps need text.
SHORT = {
 ('mirror-bow-video','e3'): ('완성. 남은 룬 2자리는 취향껏.','Done. The two free rune sockets are up to you.'),
 ('absent-amulet-video','a12b'): ('가성비 마무리: 좌측 결정화의 징조 + 완벽한 강화의 에센스.','Budget finish: Sinistral Crystallisation + Perfect Essence of Enhancement.'),
 ('absent-amulet-video','a16c'): ('가성비 마무리: 좌측 결정화의 징조 + 완벽한 강화의 에센스.','Budget finish: Sinistral Crystallisation + Perfect Essence of Enhancement.'),
 ('absent-amulet-video','a19'): ('완벽한 유동체(부여 스킬 20레벨) + 완벽한 보석세공사의 오브(5홈). 축성은 선택.','Perfect Liquid (granted skill level 20) + Perfect Jeweller (5 sockets). Sanctify optional.'),
 ('breach-ring-video','c7'): ('바알 촉진시키는 주입기: 1회는 안전, 그 뒤는 타락 위험(70%까지 권장).','Vaal Catalysing Infuser: the first is safe, then corruption risk (70% recommended).'),
 ('breach-ring-video','c16'): ('선택: 신성한 오브 → 축성 또는 타락.','Optional: Divine, then sanctify or corrupt.'),
 ('gold-amulet-6line','g9'): ('완성.','Done.'),
 ('grasping-mail-spell1','p2b'): None, ('grasping-mail-spell1','m8'): None,
 ('grasping-mail-spell1','m9'): ('완성.','Done.'),
 ('absent-amulet-spell6','e1'): ('완벽한 유동체로 부여 스킬 20레벨.','Perfect Liquid: granted skill level 20.'),
 ('absent-amulet-spell6','q3'): ('히네코라의 머리카락으로 확인 → 바알 촉진시키는 주입기, 50%까지.','Hinekora\'s Lock to foresee, then Vaal Catalysing Infuser, up to 50%.'),
 ('absent-amulet-spell6','e2'): ('성유: 자로크의 선물.','Anoint: Zarokh\'s Gift.'),
 ('absent-amulet-spell6','e4'): ('선택: 신성한 오브 → 축성(주문 +4 → +6 노림).','Optional: Divine, then sanctify (aiming +4 → +6 spells).'),
 ('absent-amulet-spell6','e9'): ('완성.','Done.'),
 ('mazbro-caster-ring','r7'): ('바알 촉진시키는 주입기 1회(안전).','One Vaal Catalysing Infuser (safe).'),
 ('mazbro-caster-ring','r15'): ('완성.','Done.'),
 ('mazbro-caster-amulet','a18'): ('신성한 오브 + 축복받은 자의 징조(고정 옵션 정신력 15). 완성.','Divine + Omen of the Blessed (implicit Spirit 15). Done.'),
 ('mazbro-bis-chest','c7'): ('영혼 핵 장착: 마나 %·정신력 %·복합 저항.','Socket the Soul Core: % mana, % Spirit, hybrid resistances.'),
 ('mazbro-bis-chest','c17'): ('신성한 오브(마나 %·정신력 %) + 축복받은 자의 징조(고정 옵션 정신력 30). 완성.','Divine (% mana, % Spirit) + Omen of the Blessed (implicit Spirit 30). Done.'),
 ('mazbro-proj-gloves','g8'): None,
 ('mazbro-proj-gloves','g17'): ('신성한 오브로 수치 정리, 아스트리드의 창의성 → 원하는 룬. 완성.','Divine the values, Astrid\'s Ingenuity → the rune you want. Done.'),
 ('diztoh-twister-spear','s1'): ('투사체 스킬 +4 분열 희귀 아코야의 창.','A rare Akoya Spear with fractured +4 projectile skills.'),
 ('diztoh-twister-spear','s5'): None, ('diztoh-twister-spear','s8'): None,
 ('diztoh-twister-spear','s11'): ('신성한 오브·퀄리티로 마무리. 타락(2소켓)은 선택.','Finish with Divines and quality. Corrupting for 2 sockets is optional.'),
 ('diztoh-iceshot-bow','w9'): ('번개 1티어면 알두르의 숨결로 화염·번개 → 냉기.','If T1 lightning landed: Aldur\'s Breath turns fire/lightning into cold.'),
 ('diztoh-iceshot-bow','w10'): None,
 ('diztoh-iceshot-bow','w16'): ('신성한 오브로 수치 정리, 아스트리드의 창의성 → 물리 룬. 완성.','Divine the values, Astrid\'s Ingenuity → a physical rune. Done.'),
 ('diztoh-budget-mace','d1'): ('특출난 거대한 대망치(소켓 3), 노멀.','Exceptional Massive Greathammer (3 sockets), normal.'),
 ('diztoh-budget-mace','d6'): None,
 ('diztoh-budget-mace','d10'): ('상위 철 룬 3개 → 완벽한 철 룬. 완성.','Three Greater Iron Runes → a Perfect Iron Rune. Done.'),
 ('diztoh-grenade-crossbow','x1'): ('노멀 공성 석궁.','A normal Siege Crossbow.'),
 ('diztoh-grenade-crossbow','x5'): None,
 ('diztoh-grenade-crossbow','x11'): ('퀄리티 20%, 완벽한 철 룬. 완성.','Quality 20%, Perfect Iron Rune. Done.'),
 ('diztoh-crit-helmet','h13'): ('신성한 오브로 수치 정리. 완성.','Divine the values. Done.'),
 ('diztoh-5mod-sapphire','j7'): ('좌측 소멸의 징조 + 소멸의 오브: "+1 접미 허용" 제거(1/2).','Sinistral Annulment + Annulment: remove "+1 suffix allowed" (1/2).'),
 ('diztoh-5mod-sapphire','j12'): ('완성.','Done.'),
 ('ragna-spell4-amulet','g1'): ('정신력 +50 분열 + 모든 주문 스킬 +3 태양의 목걸이.','Solar Amulet with fractured +50 Spirit and +3 all spell skills.'),
 ('ragna-spell4-amulet','g6b'): ('타협: 접미는 그대로, 접두 훼손 → 공개 → 절사의 징조 + 상위 카오스 오브로 마무리.','Settle: keep the suffixes, desecrate and reveal a prefix, finish with Whittling + Greater Chaos.'),
 ('breach-ring-phys','b1'): ('공격 시 물리 피해 1티어 분열 + 잡옵 1줄.','Fractured T1 flat physical to attacks plus one junk line.'),
 ('breach-ring-phys','b6b'): ('쓸 만한 접미면 그대로 두고 접두로.','A usable suffix: keep it and move to prefixes.'),
 ('ragna-ashot-bow','w1'): ('물리 피해 % 1티어 매직 전쟁광 활.','A magic Warmonger Bow with T1 % physical damage.'),
 ('ragna-ashot-bow','w7'): ('완성. 안 좋게 나오면 팔고 다시.','Done. Sell a bad roll and start over.'),
 ('diztoh-5mod-emerald','e1'): ('공격 치명타 피해 보너스 접미 희귀 에메랄드.','A rare Emerald with an attack crit damage bonus suffix.'),
 ('diztoh-5mod-emerald','e7'): ('좌측 소멸의 징조 + 소멸의 오브: "+1 접미 허용" 제거(1/2).','Sinistral Annulment + Annulment: remove "+1 suffix allowed" (1/2).'),
 ('diztoh-5mod-emerald','e12'): ('완성. 타락은 선택.','Done. Corruption optional.'),
 ('diztoh-rarity-ring','g1'): ('접두 희귀도 + 접미 냉기 저항 매직 황금 반지.','A magic Gold Ring with prefix rarity and suffix cold resistance.'),
 ('diztoh-rarity-ring','g7'): ('완성.','Done.'),
 ('diztoh-socket-gloves','d7'): None,
 ('diztoh-socket-gloves','d12'): ('아스트리드의 창의성 → 페누무스의 회전의 룬. 완성.','Astrid\'s Ingenuity → a cast speed rune. Done.'),
 ('diztoh-vile-robe','v1'): ('정신력 분열 특출난 끔찍한 로브(룬 소켓 3), 퀄리티 20%.','Exceptional Vile Robe (3 rune sockets) with fractured Spirit, quality 20%.'),
 ('diztoh-vile-robe','v4'): None,
 ('diztoh-vile-robe','v9'): ('신성한 오브로 정신력 점유 효율, 룬 정리. 완성.','Divine for Spirit reservation efficiency, set the runes. Done.'),
 ('mazbro-sceptre','z9'): None,
 ('mazbro-sceptre','z14b'): ('실패 시: 우측 결정화의 징조 + 심연의 에센스 → 보존된 턱뼈 → 심연의 메아리로 아군 생명력 재생을 막고 완벽한 엑잘티드 오브.','On a miss: Dextral Crystallisation + Essence of the Abyss, Preserved Jawbone, block ally life regen with Abyssal Echoes, then Perfect Exalt.'),
 ('mazbro-sceptre','z15'): ('신성한 오브로 수치 정리, 아스트리드의 창의성 → 존재 범위 증강물. 완성.','Divine the values, Astrid\'s Ingenuity → a presence area augment. Done.'),
 ('mazbro-spell5-amulet','z9b'): ('다른 방법: 시전 퀄리티 40% → 촉진하는 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 주문 +3·시전 속도.','Alternative: 40% caster quality, then Catalysing Exaltation + Perfect Exalt for +3 spells or cast speed.'),
 ('mazbro-spell5-amulet','z14'): ('성유: 자로크의 선물.','Anoint: Zarokh\'s Gift.'),
 ('mazbro-spell5-amulet','z15'): ('완벽한 유동체(부여 스킬 20레벨) + 완벽한 보석세공사의 오브(5홈).','Perfect Liquid (granted skill level 20) + Perfect Jeweller (5 sockets).'),
 ('mazbro-spell5-amulet','z17'): ('축성의 징조 + 신성한 오브: 대박(+5) → 완성, 아니면 다른 목걸이로 다시.','Omen of Sanctification + Divine: jackpot (+5) → done, otherwise try another amulet.'),
 ('mazbro-spell5-amulet','z18'): ('완성.','Done.'),
 ('sl-5mod-jewel','s1'): ('피해를 주는 상태 이상 가속 분열 사파이어 + 잡옵 1줄.','A Sapphire with fractured damaging ailment speed plus one junk line.'),
 ('sl-5mod-jewel','s8'): ('우측 소멸의 징조 + 소멸의 오브: "접두 +1 허용" 제거.','Dextral Annulment + Annulment: remove "+1 prefix allowed".'),
 ('sl-5mod-jewel','s10'): ('신성한 오브로 접두 3줄 수치 정리.','Divine the three prefixes.'),
 ('sl-5mod-jewel','s13'): ('선택: 바알 오브 타락. 완성.','Optional: Vaal Orb. Done.'),
 ('sl-flamewave-ring','q3'): ('선택: 바알 촉진시키는 주입기(두 번까지 거의 안전).','Optional: Vaal Catalysing Infuser (two are nearly safe).'),
 ('sl-flamewave-staff','r1'): None, ('sl-flamewave-staff','r2'): None, ('sl-flamewave-staff','f1'): None,
 ('sl-flamewave-staff','r1b'): ('가성비 마무리: 산울마녀 아산드라의 지혜의 룬 + 지콰니의 물결 영혼 핵, 접미는 엑잘티드 오브 2줄 + 초월의 합금(화염 주문 +7).','Budget finish: a +1 spell skill rune and Soul Core, suffixes with two Exalts and an Alloy (+7 fire spells).'),
 ('sl-flamewave-staff','f2'): ('선택: 바알 오브 타락(소켓 +1) → 지콰니의 물결 영혼 핵.','Optional: Vaal Orb (+1 socket), then a skill-level Soul Core.'),
 ('sl-proj7-gloves','v1b'): None,
 ('sl-proj7-gloves','v8'): ('완성.','Done.'),
}
for _r in R:
    for _n in _r['nodes']:
        _k = (_r['id'], _n['id'])
        if _k in SHORT:
            if SHORT[_k] is None: _n.pop('note', None)
            else: _n['note'] = K(*SHORT[_k])

# Short branch lines for steps whose currency and target are already on screen but whose outcome forks (대박/실패 갈림길).
BRANCH = {
 ('mirror-bow-video','b4'): ('없으면: 빛의 징조 + 소멸의 오브 → 아래 재시도 구간 → 다시 공개.','None: Light + Annulment, the retry loop below, then reveal again.'),
 ('absent-amulet-video','a11'): ('좋은 옵션 → 완성. 아니면 갈림길(아래 두 방법).','A good mod → done. Otherwise the fork below.'),
 ('absent-amulet-video','a16'): ('에너지 보호막 → 완성. 아니면 갈림길(아래 두 방법).','Energy shield → done. Otherwise the fork below.'),
 ('breach-ring-video','c13'): ('너무 안 뜨면 2티어로 타협.','If it drags on, settle for T2.'),
 ('ragna-spell4-amulet','g6'): ('시전 속도 → 완성. 아니면 갈림길: ① 우측 소멸의 징조 + 소멸의 오브 후 기폭제 다시 채우고 재도전 ② 타협(아래).','Cast speed → done. Otherwise: ① Dextral Annulment + Annulment, refill quality, retry ② settle (below).'),
 ('mazbro-proj-gloves','g10'): ('실패: 우측 결정화의 징조 + 군왕의 합금·발작의 에센스로 잡옵을 바꿔 두 번 더, 다 실패하면 소멸의 오브.','Miss: Dextral Crystallisation + alloy/essence to swap the junk twice more, then annul.'),
 ('mazbro-sceptre','z13'): ('한 번만 봄: 성공 → 마지막 접미, 실패 → 그대로 두고 마지막 접미 먼저, 훼손은 마지막에 다시.','One look: hit → last suffix; miss → leave it, do the last suffix first, redo the desecration last.'),
 ('mazbro-sceptre','z14'): ('빗나가서 지운 줄이 장착 증강 효과면 합금 단계부터.','If the annul takes the augment-effect line, redo the alloy step.'),
 ('diztoh-socket-gloves','d8'): ('훼손 줄이 지워지면 → 아래 성공 경로, 에너지 보호막이 지워지면 → 빈 접두 2자리를 엑잘로 채우고 남은 훼손은 마지막에 공개.','Desecration removed → success path; energy shield removed → exalt the two free prefixes, reveal the old desecration last.'),
 ('diztoh-socket-gloves','dm3'): ('남아 있던 훼손을 공개. 안 나오면 빛의 징조 + 소멸의 오브 → 고대 갈비뼈 → 다시 공개.','Reveal the old desecration; on a miss, Light + Annulment, Ancient Rib, reveal again.'),
 ('diztoh-socket-gloves','d11'): ('실패: 좌측 소멸의 징조 + 소멸의 오브 → 다시. 에너지 보호막이 지워지면 그 자리도 엑잘로(에너지 보호막 최대치 포함), 공개한 훼손이 지워지면 {#d9}번부터.','Miss: Sinistral Annulment + Annulment, retry. If energy shield goes, exalt that slot too (flat ES counts); if the revealed desecration goes, back to step {#d9}.'),
 ('sl-flamewave-staff','s3'): ('합금이 화염 속성 부여 규모를 지우면(1/2): 합금 줄은 남으니 절사 단계만 다시.','If the alloy takes the fire magnitude line (1/2): the alloy line stays, so only redo the Whittling step.'),
 ('diztoh-iceshot-bow','w12'): ('실패: 우측 결정화의 징조 + 완벽한 가속의 에센스 → 심연의 에센스(징표) → 다시 훼손.','Miss: Dextral Crystallisation + Perfect Essence of Haste, Essence of the Abyss (Mark), desecrate again.'),
 ('diztoh-iceshot-bow','w15'): ('공격 속도·치명타 피해·초과 화살 → 대박.','Attack speed, crit damage or extra arrows → jackpot.'),
 ('diztoh-vile-robe','v6'): ('실패: 우측 결정화의 징조 + 완벽한 추구의 에센스 → 우측 결정화의 징조 + 심연의 에센스(징표) → 다시 공개.','Miss: Dextral Crystallisation + Perfect Essence, then Dextral Crystallisation + Essence of the Abyss (Mark), reveal again.'),
 ('diztoh-5mod-sapphire','j4'): ('"+1 접미 허용" → 성공, "+1 접두 허용" → 소멸의 오브로 비우고 처음부터.','"+1 suffix allowed" → success; "+1 prefix allowed" → annul and start over.'),
 ('diztoh-5mod-emerald','e4'): ('"+1 접미 허용" → 성공, 아니면 처음부터.','"+1 suffix allowed" → success, otherwise start over.'),
 ('diztoh-5mod-emerald','e9'): ('중간에 소멸의 오브 금지(접미가 상한 초과).','No Annulment in between (suffixes are over the cap).'),
 ('ragna-ashot-bow','w3'): ('물리 % + 정확도 복합 → 대박.','% physical + accuracy hybrid → jackpot.'),
 ('sl-proj7-gloves','v5'): ('접미 잡옵이 지워지면 성공(1/2), 치명타 확률이 지워지면 접미 작업 처음부터.','Junk suffix removed → success (1/2); crit chance removed → redo the suffixes.'),
}
for _r in R:
    for _n in _r['nodes']:
        _k = (_r['id'], _n['id'])
        if _k in BRANCH: _n['br'] = K(*BRANCH[_k])

# Tip numbers under a step (hover shows the tip): step → tip ids from tips.json (사용자 요청 2026-11-09)
TIPREF = {('diztoh-vile-robe','v4'):['desecrate-reroll-no-light'], ('diztoh-iceshot-bow','w10'):['desecrate-reroll-no-light'],
 ('sl-flamewave-ring','s2'):['erasure-chaos-cheaper','min-level-lock-tier'], ('mazbro-sceptre','z13'):['reveal-miss-exalt-first'], ('diztoh-socket-gloves','d11'):['reveal-miss-exalt-first'],
 ('absent-amulet-video','a18'):['reveal-miss-exalt-first'], ('ragna-ashot-bow','w5'):['min-level-lock-tier'], ('breach-ring-phys','b6'):['single-res-catalyst'], ('mazbro-sceptre','z11'):['augment-effect-alloy'], ('mazbro-spell5-amulet','z17'):['sanctify-checklist'],
 ('helmet-armour-sl','s1'):['liquid-resist-swap'], ('sl-flamewave-ring','s1'):['liquid-resist-swap'], ('mazbro-caster-amulet','a4'):['chaos-side-swap','sell-offtarget'], ('gold-amulet-6line','k1'):['sell-offtarget'],
 ('sane-resist-belt','b3'):['liege-omen-resist-jewellery'], ('lilbotq-armour-shield','l1'):['fracture-safety-line'], ('sihan-highend-boots','h1'):['fracture-percent-line'],
 ('sihan-highend-boots','s1'):['low-weight-first'], ('sihan-highend-boots','s4'):['liquid-resist-swap'], ('sihan-highend-boots','m1'):['cheap-junk-removal'],
 ('saveq-focus','q1'):['low-ilvl-base'], ('saveq-focus','q4'):['unrevealed-filler'], ('icesly-budget-wand','i6'):['unrevealed-filler'], ('icesly-budget-wand','i8'):['side-omen-save'],
 ('barricade-quarterstaff','q1'):['low-ilvl-base'], ('barricade-quarterstaff','p4'):['whittle-stuck'], ('belton-plus8-wand','b1'):['fracture-sellable-lines','low-ilvl-base'], ('belton-plus8-wand','b2'):['block-high-weight'],
 ('farmer-budget-armour','f8'):['greater-exalt-omen-price'], ('farmer-starter-staff','w5'):['greater-exalt-omen-price'], ('farmer-budget-armour','f1'):['cheap-resist-essence'],
 ('seek-cyclone-boots','k2'):['augment-rune-before-chaos'], ('farmer-starter-staff','w3'):['putrefaction-gamble']}
for _r in R:
    for _n in _r['nodes']:
        _k=(_r['id'],_n['id'])
        if _k in TIPREF: _n['tips']=TIPREF[_k]

# Automatic tip links (사용자 확정 2026-11-09: tips live in tips.json, a step shows only "제작 꿀팁 #n" with the text on hover).
# A tip is linked to a step only in recipes the tip lists, by what the step uses.
_TJ = json.load(open('/home/claude/poe2data/site/data/tips.json'))['tips']
def _uses(n, *ids):
    s = json.dumps({k:n.get(k) for k in ('cur','omens','fail','withEach','target','label','cost')}, ensure_ascii=False)
    return any(i in s for i in ids)
def _note(n): return (n.get('note') or {}).get('kr','')
def _kw(n, *ws): return any(w in _note(n) for w in ws)
# (tip, rule, only in the tip's own recipes?)
AUTO = [
 ('whittle-side-first', lambda n,i: _uses(n,'Omen_of_Whittling'), True),
 ('catalyst-steer', lambda n,i: _uses(n,'Omen_of_Catalysing_Exaltation'), True),
 ('light-annul-count', lambda n,i: n['do']=='reveal' and _uses(n,'Omen_of_Light'), True),
 ('after-fracture-chaos', lambda n,i: n['do']=='chaos' and i<=2, True),
 ('low-weight-first', lambda n,i: n['do']=='chaos' and i<=2, True),
 ('block-high-weight', lambda n,i: n['do']=='reveal', True),
 ('divine-before-sanctify', lambda n,i: _uses(n,'sanctify','축성'), True),
 ('zarokh-anoint', lambda n,i: _uses(n,'anoint','성유'), True),
 ('hinekora-before-big', lambda n,i: _uses(n,'Hinekoras_Lock','히네코라') or _kw(n,'히네코라'), False),
 ('hinekora-after-changes', lambda n,i: _uses(n,'Hinekoras_Lock') or _kw(n,'히네코라'), True),
 ('vaal-infuser-plan', lambda n,i: n.get('cost')=='vaal' or _uses(n,'주입기') or _kw(n,'주입기'), True),
 ('side-omen-save', lambda n,i: _kw(n,'징조 없이','징조 불필요','징조 없는 소멸','강령술의 징조는 필요 없음','징조는 필요 없음'), False),
 ('erasure-chaos-cheaper', lambda n,i: _uses(n,'Erasure') and _uses(n,'Greater_Chaos_Orb') and n['do']=='chaos', False),
 ('cheap-junk-removal', lambda n,i: _kw(n,'싼 순서','더 쌈') and _kw(n,'심연의 에센스'), False),
 ('abyss-before-crafted', lambda n,i: _kw(n,'심연의 에센스') and _kw(n,'못 씀','못 써','먹지 않음','안 먹','쓸 수 없음'), False),
 ('maxq-chaos-slot', lambda n,i: n['do']=='chaos' and _kw(n,'최대 퀄리티') and _kw(n,'그대로','유지','남음'), False),
 ('mark-wrong-side', lambda n,i: _kw(n,'징표') and _kw(n,'뼈') and _kw(n,'다시') and n['do'] in ('essence','remove'), False),
 ('jewel-five-mods', lambda n,i: _kw(n,'경멸','흉포함','상한보다 많은'), False),
 ('cheap-catalyst', lambda n,i: n['do']=='quality' and _kw(n,'싼','쌈'), False),
 ('augment-effect-alloy', lambda n,i: n['do']=='essence' and _kw(n,'증강 효과'), False),
 ('spell-quality-34', lambda n,i: n['do']=='quality' and _kw(n,'+4'), False),
 ('sanctify-checklist', lambda n,i: _uses(n,'Omen_of_Sanctification') or _kw(n,'축성의 징조','축성할지'), False),
 ('desecrate-reroll-no-light', lambda n,i: _kw(n,'빛 없이'), False),
 ('single-res-catalyst', lambda n,i: _kw(n,'원소 무관 3종'), False),
]
for _r in R:
    for _i, _n in enumerate(_r['nodes']):
        for _tid, _f, _own in AUTO:
            _t = next((t for t in _TJ if t['id']==_tid), None)
            if _t and (not _own or _r['id'] in _t.get('recipes',[])) and _f(_n,_i) and _tid not in _n.get('tips',[]):
                _n.setdefault('tips',[]).append(_tid)
