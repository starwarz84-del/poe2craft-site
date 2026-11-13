# G9 2026-11-13: LilBotQ 방어도 2000 방패(4YOSSAa53UU, 10:46) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G9/lilbotq-armour-shield-v2/timeline.md, frames/ (영상 화면 대조)
# 실행: cd scripts/graphs && python3 gen_lilbotq_armour_shield.py  → lilbotq-armour-shield-v2.json (gen_batch6.py 끝에서 자동 호출, 그 파일의 이 아이템 구간을 대신함)
# 상자 id는 옛 단계 레시피(recipes_v5_lilbotq-armour-shield.py: l1~l8)와 겹치지 않게 k0~k9.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/lilbotq-armour-shield-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

FL = L('p', '방어도 +(249—277)', '+(249—277) to Armour', 'n', ['flat'])
FLr = L('p', '방어도 +(249—277) (분열)', '+(249—277) to Armour (fractured)', 'f', ['flat'])
FIR = L('s', '화염 저항 최대치 +3%', '+3% to Maximum Fire Resistance', 'j')
ESS = L('p', '방어도, 회피, 에너지 보호막 (68—79)% 증가 (상위 강화의 에센스)', '(68—79)% increased Armour, Evasion and Energy Shield (Greater Essence of Enhancement)', 'c', ['essP'])
PC = L('p', '방어도 (101—110)% 증가', '(101—110)% increased Armour', 'n', ['pct'])
HY = L('p', '방어도 (39—42)% 증가, 기절 한계치 +(95—136) (훼손)', '(39—42)% increased Armour, +(95—136) to Stun Threshold (desecrated)', 'd', ['hyb1'])
CHR = L('s', '카오스 저항 +(24—27)%', '+(24—27)% to Chaos Resistance', 'n')
CLR = L('s', '냉기 저항 +(26—30)%', '+(26—30)% to Cold Resistance', 'n')
PDR = L('s', '받는 물리 피해 8% 추가 감소', '8% additional Physical Damage Reduction', 'n')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'lilbotq-armour-shield-v2', 'recipe': 'lilbotq-armour-shield-v2', 'cls': 'Shields_str', 'base': 'Tawhoan Tower Shield', 'ilvl': 81,
 'note': ('2026-11-13 G9 영상 전체 대조(근거 scratchpad review/G9/lilbotq-armour-shield-v2/timeline.md). 성공 회차 한 줄: '
          '특출난 타호아의 거대 방패(홈 2개, 아이템 레벨 81, 퀄리티 20%, 1:02) → 바알 방어구 장인의 주입기 2개로 28%(1:28) → 완벽한 진화 = 방어도 1티어(1:36, 한 번에 성공) → '
          '완벽한 확장 = 화염 저항 최대치(4:05) → 상위 강화의 에센스(4:32) → 좌측 강령술 + 보존된 갈비뼈(4:48) → 신성한 오브(5:00, 방어도 277) → 분열의 오브 = 방어도(5:14) → '
          '소멸의 오브로 옵션 1개만(5:40) → 카오스 오브 = 방어도 % 1티어(7:36) → 좌측 강령술 + 고대 갈비뼈 + 심연의 메아리 공개(7:50 3티어 → 빛의 징조로 다시, 8:38 1티어) → '
          '상위 찬미 + 완벽한 엑잘(9:44) → 완벽한 엑잘(10:05). 6:00~7:30의 곁가지(카오스로 먼저 뜬 복합 1티어를 두고 훼손 → 69% 공개 → 소멸의 오브가 복합을 지움 → 카오스 다시)는 영상도 선택이라 꿀팁 후보로. '
          '완벽한 철 룬 2개·신성한 오브 마무리(8:30~9:00)는 정책 9장대로 뺌. 밸런스 = 공개 복합 1~2티어까지 빛의 징조(영상 7:50~8:38 빛의 징조로 다시, C17-3). '
          '11-13 오후 새 정책 D: 에센셜(공개 결과 그대로) 72.2 div와 밸런스 74.4 div가 3% 차이라 밸런스 하나만.'),
 'params': {'hT': {'kr': '공개 복합 옵션', 'en': 'Revealed hybrid', 'values': {'2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'bal', 'params': {'hT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'hT': 2}, 'tier': 'bal',
    'desc': K('공개 복합 옵션 1~2티어까지 빛의 징조로 다시 (영상은 1티어)', 'Reveal again with Omen of Light until a T1–2 hybrid (the video went to T1)')}],
 'tags': {'flat': {'gi': 6, 'tmax': 1}, 'pct': {'gi': 7, 'tmax': 1}, 'essP': {'gi': 38},
          'hyb': {'gi': 8, 'tmax': '$hT'}, 'hyb1': {'gi': 8, 'tmax': 1}, 'hyb2': {'gi': 8, 'tmax': 2}},
 'require': {'all': [{'has': 'flat'}, {'has': 'pct'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'flat', 'fr': True}, {'tag': 'pct'}, {'tag': 'hyb2', 'des': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 28, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='k0', kind='base', group='prep', pos=[0, 0], next='k1', start={'rar': 'normal', 'mods': [], 'quality': 20},
  label=K('노멀 특출난 타호아의 거대 방패 구입 (아이템 레벨 81, 홈 2개, 퀄리티 20%)', 'Buy a normal exceptional Tawhoan Tower Shield (item level 81, two sockets, 20% quality)'), item=[])
A(id='k1', kind='act', group='prep', pos=[0, 1], act='quality', cur='Vaal_Armourers_Infuser', count=2, q=28, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 28%', 'Quality 28%'), showText=[K('바알 방어구 장인의 주입기 2개', '2 Vaal Armourer’s Infusers')], edges=[{'to': 'k2'}], item=[])
A(id='k2', kind='act', group='prep', pos=[0, 2], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('접두 방어도 1티어', 'T1 flat armour prefix'), show=['flat'],
  edges=[{'if': {'has': 'flat'}, 'to': 'k3', 'res': 'ok'}, {'to': 'k2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[FL])
A(id='k2x', kind='cleanup', group='prep', pos=[1, 2], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('옵션을 지우고 완벽한 확장의 오브로 다시', 'Clear it and try again with a Perfect Augmentation'), edges=[{'to': 'k2a'}])
A(id='k2a', kind='act', group='prep', pos=[1, 2.6], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 방어도 1티어', 'T1 flat armour prefix'), show=['flat'],
  edges=[{'if': {'has': 'flat'}, 'to': 'k3', 'res': 'ok'}, {'to': 'k2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}])
A(id='k3', kind='act', group='prep', pos=[0, 3], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접미 옵션 하나 — 결과 그대로', 'One suffix: keep whatever comes'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'k4'}], item=[FL, FIR])
A(id='k4', kind='act', group='prep', pos=[0, 4], act='essence', cur='Greater_Essence_of_Enhancement', ess='essP', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 방어도·회피·에너지 보호막 % 증가 (제작 옵션)', 'Rare + % armour, evasion and energy shield prefix (crafted)'),
  showText=[{'s': 'p', 'kr': '방어도, 회피, 에너지 보호막 (68—79)% 증가 (제작 옵션)', 'en': '(68—79)% increased Armour, Evasion and Energy Shield (crafted)'}],
  edges=[{'to': 'k5'}], item=[FL, ESS, FIR])
A(id='k5', kind='act', group='prep', pos=[0, 5], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 분열되지 않음)', 'en': 'Desecrated (unrevealed, cannot fracture)'}],
  edges=[{'to': 'k6'}], item=[FL, ESS, UN('p'), FIR])
A(id='k6', kind='act', group='prep', pos=[0, 6], act='divine', cur='Divine_Orb', count=2, label=K('수치 올리기', 'Divine the values'),
  goal=K('분열 전에 방어도 수치 올리기', 'Raise the armour value before the fracture'),
  showText=[K('신성한 오브 2개 (영상: 방어도 277)', 'Two Divine Orbs (the video: 277 armour)')], edges=[{'to': 'k7'}], item=[FL, ESS, UN('p'), FIR])
A(id='k7', kind='act', group='prep', pos=[0, 7], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 — 공개된 옵션 3개 중 접두 방어도', 'Fracture: the flat armour prefix, one of three revealed options'),
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'flat'}, 'to': 'ms', 'res': 'ok', 'label': K('방어도 분열', 'Flat armour fractured')},
         {'to': 'kx', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[FLr, ESS, UN('p'), FIR])
A(id='kx', kind='exit', group='prep', pos=[1, 7], simTo='k0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('에센스 옵션이 남아 있어 완전히 버리지는 않음, 이 레시피는 새 베이스로 처음부터', 'The essence line keeps it usable; for this recipe start over on a new base'))
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8.4], next='k8', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FLr, ESS, UN('p'), FIR])
A(id='k8', kind='cleanup', group='main', pos=[0, 9.4], keep=[], maxJunk=1, label=ANN, goal=K('분열 옵션 + 잡옵 1개만 남기기', 'Keep the fractured line and one junk option'),
  target=K('소멸의 오브로 옵션 1개만 남김', 'Annul down to one option'), edges=[{'to': 'k9'}], item=[FLr, J('s')])
A(id='k9', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 방어도 % 증가 1티어', 'T1 % armour prefix'), show=['pct'],
  edges=[{'if': {'has': 'pct'}, 'to': 'k10', 'res': 'ok'}, {'to': 'k9', 'res': 'fail', 'hide': True}], item=[FLr, PC])
A(id='k10', kind='act', group='main', pos=[0, 11.4], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'k11'}], item=[FLr, PC, UN('p')])
A(id='k11', kind='act', group='main', pos=[0, 12.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='hyb',
  label=K('공개', 'Reveal'), goal=K('접두 방어도 % 증가 + 기절 한계치', '% armour + stun threshold prefix'), show=['hyb'],
  edges=[{'if': {'added': 'hyb'}, 'to': 'k12', 'res': 'ok'},
         {'to': 'k11x', 'res': 'fail', 'label': K('빗나감 — 빛의 징조로 다시', 'Miss: again with Omen of Light')}],
  item=[FLr, PC, HY])
A(id='k11x', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'k10', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='k12', kind='act', group='main', pos=[0, 13.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 옵션 2개 — 결과 그대로', 'Two suffixes: keep whatever comes'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'k13'}], item=[FLr, PC, HY, CHR, CLR])
A(id='k13', kind='act', group='main', pos=[0, 14.4], act='exalt', cur='Perfect_Exalted_Orb',
  label=K('엑잘', 'Exalt'), goal=K('접미 세 번째 옵션 — 결과 그대로', 'Third suffix: keep whatever comes'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'ok'}], item=[FLr, PC, HY, CHR, CLR, PDR])
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L0', 'nodes': ['k2x', 'k2a'], 'kr': '매직 옵션', 'en': 'Magic option'},
              {'id': 'L1', 'nodes': ['k10', 'k11', 'k11x'], 'kr': '훼손 공개', 'en': 'Reveal'}]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
