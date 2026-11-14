# RECIPE-D 2026-11-14: SaVeQ 황혼 반지 공격 플랫 4개(youtu.be/CZepweLtKwA, 2026-09-23, 0.5.5) — 조사 g109(docs/craft-guides.md 6차, 영어 자막)
# 영상 흐름 한 줄(성공 회차):
#   준비 3:04 레어 황혼 반지(접두 4·접미 2, 아이템 레벨 79, 1 엑잘) → 4:35 소멸로 옵션 1개 → 카오스 반복으로 원소 공격 플랫 1티어(영상: 화염)
#     → 6:13 좌측 찬미 + 상위 찬미 + 엑잘(접두 2개) → 아무 뼈로 훼손 → 분열의 오브(1/3, 8개 중 2개 성공 — 실패면 새 반지)
#   본 제작 8:30 소멸로 분열만 → 카오스 반복으로 냉기·번개 1티어(영상: 번개) → 10:49 엑잘 접미 잡옵 → 우측 결정화 + 균열의 에센스(최대 퀄리티 +20%)
#     → 강탈자 기폭제 40% → 좌측 찬미 + 촉진하는 찬미 + 완벽한 엑잘(영상: 물리 플랫 3티어) → 12:22 기폭제 40% 다시 → 절사 + 카오스로 균열 옵션(레벨 1)을 옮김(영상: 접미 마나 재생)
#     → 13:07 좌측 강령술 + 메아리 + 고대 빗장뼈 → 공개 냉기 플랫, 빗나가면 빛의 징조 + 소멸(10번 뒤 2티어 타협) → 16:15 우측 결정화 + 재빠른 합금 → 완벽한 엑잘(영상: 지능)
# 실행: cd scripts/graphs && python3 gen_saveq_dusk_flat_ring.py  → saveq-dusk-flat-ring-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-dusk-flat-ring-v2.json'
CLS = 'Rings'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

J1 = L('p', '잡옵', 'Junk option', 'j'); J2 = L('p', '잡옵', 'Junk option', 'j'); J3 = L('s', '잡옵', 'Junk option', 'j')
FI = DB('p', 15, ['efr'], 'n', 0); FIF = DB('p', 15, ['efr'], 'f', 0)        # 화염 플랫 1티어(분열)
LG = DB('p', 19, ['ef2'], 'n', 0)                                          # 번개 플랫 1티어
PH = DB('p', 13, None, 'n', 2)                                             # 물리 플랫 3티어(촉진 엑잘 결과)
MQ = L('p', '최대 퀄리티 +20% (균열의 에센스)', '+20% to Maximum Quality (Essence of the Breach)', 'c', ['maxq'])
UNP = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
UNA = L('s', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
CO = DB('p', 17, ['eD'], 'd', 1)                                          # 냉기 플랫 2티어(훼손, 영상 타협)
MR = DB('s', 21, None, 'j', 0)                                             # 마나 재생(절사 카오스 결과, 잡옵)
AS = L('s', '공격 속도 (7—9)% 증가 (재빠른 합금)', '(7—9)% increased Attack Speed (Swift Alloy)', 'c', ['as'])
INT = DB('s', 2, None, 'n', 1)                                             # 지능 2티어(마지막 엑잘)
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
LIGHT = K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light')
EF = K('공격 시 화염·냉기·번개 피해 추가 1티어', 'T1 fire, cold or lightning flat to attacks')

g = {
 'id': 'saveq-dusk-flat-ring-v2', 'recipe': 'saveq-dusk-flat-ring-v2', 'cls': CLS, 'base': 'Dusk Ring', 'ilvl': 79,
 'basePrice': {'Exalted_Orb': 1},   # 3:04 '1 엑잘'
 'note': ('2026-11-14 RECIPE-D: SaVeQ 황혼 반지 공격 플랫 4개(youtu.be/CZepweLtKwA, 조사 g109 — docs/craft-guides.md 6차 단계 노트·완성 툴팁 17:01). '
          '분열 자리는 원소 플랫(가중치 200)이라 물리 플랫(400)보다 늦게 뜨는 쪽을 먼저 잡는다는 영상 판단(3:04) 그대로, 성공 조건은 원소 플랫 1티어 중 하나(영상: 화염). '
          '내부 결정: ① 구입한 반지의 옵션 수가 노트에 없어 잡옵 3개로 두고 소멸 정리 ② "아무 훼손"은 아이템 레벨 79에 쓸 수 있는 가장 싼 보존된 빗장뼈 '
          '③ "엑잘로 아무 접미"는 결정화가 지울 접미가 필요해 우측 찬미의 징조를 붙임 ④ 12:22 "촉진 주입기로 40% 다시"는 강탈자 기폭제로 셈(무료라고만 나옴) '
          '⑤ 절사 카오스의 새 옵션이 접두로 가면 접두가 꽉 차 강령술 훼손을 못 하니 절사·말소 자동 선택 + 카오스로 접두 잡옵을 다시 옮김(영상은 한 번에 접미) '
          '⑥ 촉진 엑잘에 냉기 플랫이 붙으면 공개는 결과 그대로. 등급(난이도 4): 하이엔드 = 번개·냉기 1티어, 밸런스 = 1~2티어(영상: 10번 공개 뒤 냉기 2티어 타협). '
          '분열 준비 카오스는 두 등급 모두 1티어(분열 대상, C15).'),
 'params': {
  'cT': {'kr': '카오스 냉기·번개 플랫', 'en': 'Chaos cold/lightning flat', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
  'dT': {'kr': '공개 냉기 플랫', 'en': 'Revealed cold flat', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'cT': 1, 'dT': 1}}, {'id': 'bal', 'params': {'cT': 2, 'dT': 2}}],
 'versions': [
  {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'cT': 1, 'dT': 1}, 'tier': 'high',
   'desc': K('번개·냉기 플랫 모두 1티어', 'Lightning and cold flats both T1')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'cT': 2, 'dT': 2}, 'tier': 'bal',
   'desc': K('영상: 냉기 플랫 2티어 타협, 번개·냉기 1~2티어', 'Video: settle for T2 cold, T1–2 lightning and cold')}],
 'tags': {
  'fire1': {'gi': 15, 'tmax': 1}, 'cold1': {'gi': 17, 'tmax': 1}, 'lgt1': {'gi': 19, 'tmax': 1},
  'efr': {'anyOf': ['fire1', 'cold1', 'lgt1'], 'shown': 'fire1', 'label': EF},
  'coldC': {'gi': 17, 'tmax': '$cT'}, 'lgtC': {'gi': 19, 'tmax': '$cT'},
  'fireC': {'gi': 15, 'tmax': '$cT'},
  'ef2': {'anyOf': ['fireC', 'coldC', 'lgtC'], 'shown': 'lgtC', 'label': K('공격 시 화염·냉기·번개 피해 추가', 'Fire, cold or lightning flat to attacks')},
  'fireD': {'gi': 15, 'tmax': '$dT'}, 'coldD': {'gi': 17, 'tmax': '$dT'}, 'lgtD': {'gi': 19, 'tmax': '$dT'}, 'coldAny': {'gi': 17},
  'eD': {'anyOf': ['fireD', 'coldD', 'lgtD'], 'shown': 'coldD', 'label': K('남은 원소 공격 플랫(화염·냉기·번개 피해 추가)', 'The remaining elemental attack flat (fire, cold or lightning)')},
  'eAny': {'anyOf': ['fireA', 'coldAny', 'lgtA']},
  'physA': {'gi': 13}, 'fireA': {'gi': 15}, 'lgtA': {'gi': 19},
  'atk': {'anyOf': ['physA', 'fireA', 'coldAny', 'lgtA']},
  'maxq': {'gi': 71}, 'as': {'gi': 73},
  'keep': {'anyOf': ['efr', 'ef2']},
 },
 'require': {'all': [{'has': 'efr'}, {'count': {'tag': 'ef2', 'min': 2}}, {'has': 'as'}, {'full': 'p'}, {'full': 's'}, {'unrev': False}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 3:04~8:30) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='p0', start={'rar': 'rare', 'mods': [{'junk': 'p'}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('레어 황혼 반지 구입 (아이템 레벨 79, 접두 4·접미 2)', 'Buy a rare Dusk Ring (item level 79, four prefixes and two suffixes)'), item=[J1, J2, J3])
A(id='p0', kind='cleanup', group='prep', pos=[0, 1], keep=[], maxJunk=1, label=ANN, goal=K('옵션 1개만 남기기', 'Leave one option'),
  target=K('옵션 1개만 남기기', 'Leave one option'), edges=[{'to': 'p1'}], item=[J1])
A(id='p1', kind='act', group='prep', pos=[0, 2], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('원소 공격 플랫 1티어 (영상: 화염)', 'T1 elemental attack flat (video: fire)'), show=['efr'],
  edges=[{'if': {'has': 'efr'}, 'to': 'p2', 'res': 'ok'}, {'to': 'p1', 'res': 'fail'}], item=[FI])
A(id='p2', kind='act', group='prep', pos=[0, 3], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 잡옵 2개', 'Two junk prefixes'), showText=[{'s': 'p', 'kr': '잡옵 2개', 'en': 'Two junk options'}],
  edges=[{'to': 'p3'}], item=[FI, J1, J2])
A(id='p3', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(분열 확률 1/3)', 'Fourth option (fracture odds 1/3)'), showText=[K('훼손 옵션 (미공개)', 'Desecrated (unrevealed)')],
  edges=[{'to': 'p4'}], item=[FI, J1, J2, UNA])
A(id='p4', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('원소 공격 플랫 분열', 'Fracture the elemental attack flat'), show=['efr'],
  edges=[{'if': {'fractured': 'efr'}, 'to': 'p5', 'res': 'ok'},
         {'to': 'b0', 'res': 'fail', 'label': K('다른 옵션 분열 → 새 반지', 'Another line fractured: a new ring')}],
  ask=K('원소 플랫이 분열됐나?', 'Elemental flat fractured?'), item=[FIF, J1, J2, UNA])
A(id='p5', kind='cleanup', group='prep', pos=[0, 6], keep=['efr'], maxJunk=0, label=ANN, goal=K('분열 옵션만 남기기', 'Leave only the fractured option'),
  target=K('분열 옵션만 남기기', 'Leave only the fractured option'), edges=[{'lost': 'efr', 'to': 'b0', 'hide': True}, {'to': 'ms'}], item=[FIF])
# ---------------- 옵션 추가 작업 (영상 8:30~17:01) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='m1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FIF])
A(id='m1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 두 번째 옵션 — 냉기·번개 공격 플랫 (영상: 번개 1티어)', 'Second prefix: cold or lightning attack flat (video: T1 lightning)'), show=['ef2'],
  edges=[{'if': {'count': {'tag': 'ef2', 'min': 2}}, 'to': 'm2', 'res': 'ok'}, {'to': 'm1', 'res': 'fail'}], item=[FIF, LG])
A(id='m2', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('결정화가 지울 접미 잡옵', 'A junk suffix for the Crystallisation'), showText=[{'s': 's', 'kr': '잡옵 1개', 'en': 'One junk option'}],
  edges=[{'to': 'm3'}], item=[FIF, LG, J3])
A(id='m3', kind='act', group='main', pos=[0, 10.4], act='essence', cur='Essence_of_the_Breach', ess='maxq', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 최대 퀄리티 +20%', 'Clear the junk suffix for +20% maximum quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'm4'}], item=[FIF, LG, MQ])
A(id='m4', kind='act', group='main', pos=[0, 11.4], act='quality', cur='Reaver_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('공격 퀄리티 40%', '40% attack quality'), edges=[{'to': 'm5'}], item=[FIF, LG, MQ])
A(id='m5', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Catalysing_Exaltation'], cat='atk',
  label=K('엑잘', 'Exalt'), goal=K('접두 네 번째 옵션 — 나오는 대로 (영상: 물리 플랫 3티어)', 'Fourth prefix: keep what comes (video: T3 physical flat)'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'm6'}], item=[FIF, LG, MQ, PH])
A(id='m6', kind='act', group='main', pos=[0, 13.4], act='quality', cur='Reaver_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('공격 퀄리티 40% 다시', '40% attack quality again'), edges=[{'to': 'm7'}], item=[FIF, LG, MQ, PH])
A(id='m7', kind='act', group='main', pos=[0, 14.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('최대 퀄리티(레벨 1)를 바꿈 — 새 옵션은 접미로 (영상: 마나 재생)', 'Turn maximum quality (level 1) into a suffix (video: mana regeneration)'),
  showText=[{'s': 's', 'kr': '잡옵 1개', 'en': 'One junk option'}],
  edges=[{'if': {'has': 'maxq'}, 'to': 'm7', 'res': 'fail', 'hide': True}, {'if': {'full': 'p'}, 'to': 'm7x', 'res': 'fail', 'label': K('접두로 감', 'Went to a prefix')}, {'to': 'm8', 'res': 'ok'}],
  ask=K('새 옵션이 접미로?', 'New option on a suffix?'), item=[FIF, LG, PH, MR])
A(id='m7x', kind='act', group='main', pos=[1, 14.4], act='chaos', cur='Chaos_Orb', trim={'side': 'p', 'keep': 'keep'}, label=K('절사·말소 + 카오스', 'Whittling/Erasure + Chaos'),
  goal=K('접두 잡옵을 다시 옮김', 'Move the junk prefix again'),
  edges=[{'if': {'not': {'count': {'tag': 'ef2', 'min': 2}}}, 'to': 'm7c', 'res': 'fail', 'label': K('원소 플랫이 지워짐', 'An elemental flat was removed')}, {'if': {'has': 'maxq'}, 'to': 'm7', 'res': 'fail', 'hide': True}, {'if': {'full': 'p'}, 'to': 'm7x', 'res': 'fail'}, {'to': 'm8', 'res': 'ok'}])
A(id='m7c', kind='cleanup', group='main', pos=[2, 14.4], keep=['efr'], maxJunk=0, label=ANN, goal=K('분열 옵션만 남기고 카오스부터', 'Back to the fractured option, then Chaos again'),
  target=K('분열 옵션만 남기기', 'Leave only the fractured option'), edges=[{'lost': 'efr', 'to': 'b0', 'hide': True}, {'to': 'm1', 'hide': True}])
A(id='m8', kind='act', group='main', pos=[0, 15.4], act='desecrate', cur='Ancient_Collarbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 네 번째 옵션(훼손)', 'Fourth prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'm9'}], item=[FIF, LG, PH, UNP, MR])
A(id='m9', kind='act', group='main', pos=[0, 16.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='eD', label=K('공개', 'Reveal'),
  goal=K('접두 남은 원소 공격 플랫(훼손) — 영상: 냉기', 'Prefix: the remaining elemental attack flat (desecrated, video: cold)'), show=['eD'],
  edges=[{'if': {'added': 'eD'}, 'to': 'm10', 'res': 'ok'},
         {'if': {'any': [{'count': {'tag': 'eD', 'min': 3}}, {'famBlock': 'eD', 'left': 3}]}, 'to': 'm10', 'res': 'ok', 'hide': True},
         {'to': 'm9x', 'res': 'fail'}],
  item=[FIF, LG, PH, CO, MR])
A(id='m9x', kind='act', group='main', pos=[1, 16.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'm8', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='m10', kind='act', group='main', pos=[0, 17.4], act='essence', cur='Swift_Alloy', ess='as', omens=['Omen_of_Dextral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('접미 잡옵을 공격 속도로', 'Turn the junk suffix into attack speed'),
  showText=[{'s': 's', 'kr': '공격 속도 (7—9)% 증가 (제작 옵션)', 'en': '(7—9)% increased Attack Speed (crafted)'}],
  edges=[{'to': 'm11'}], item=[FIF, LG, PH, CO, AS])
A(id='m11', kind='act', group='main', pos=[0, 18.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('마지막 접미 — 나오는 대로 (영상: 지능)', 'Last suffix: keep what comes (video: intelligence)'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'ok'}], item=[FIF, LG, PH, CO, AS, INT])
A(id='ok', kind='done', group='main', pos=[0, 19.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L2', 'nodes': ['m8', 'm9', 'm9x'], 'kr': '훼손 공개', 'en': 'Reveal'}]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'efr', 'fr': True}, {'tag': 'ef2'}, {'side': 'p', 'random': True}, {'tag': 'eD', 'des': True},
            {'tag': 'as', 'ess': True}, {'side': 's', 'random': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'efr', 'fr': True}, {'tag': 'ef2'}, {'side': 'p', 'random': True}, {'tag': 'eD', 'des': True},
            {'tag': 'as', 'ess': True}, {'side': 's', 'random': True}]}]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
