# RECIPE-E 2026-11-14: D3lebronjames 아크 토템 마나 기억 반지(youtube JeA3cg79qZY, 2026-09-12, 0.5.5) — 조사 g126(docs/craft-guides.md 7차, 영어 자막 + 18:08 화면 단계표 + 완성 툴팁)
# 영상 흐름 한 줄(성공 회차):
#   분열 전 1:21 시전 속도 1티어 4옵션 기억 반지(1~2 div) → 3:24 좌측 결정화 + 심연의 에센스(접두 하나를 지우고 군주의 징표) → 빗장뼈로 징표 훼손(공개 안 함)
#     → 분열의 오브(훼손 옵션은 분열되지 않아 1/3, 4:55 베이스 4개 중 1개 성공)
#   제작 5:15 소멸 2번(분열 + 옵션 1개) → 5:35 균열의 에센스(지울 옵션이 하나뿐이라 징조 없이 그 옵션이 최대 퀄리티) → 신경 기폭제 40
#     → 6:00 카오스 반복(약 230개) → 9:44 최대 마나 1티어 → 우측 찬미 + 엑잘(아무 접미, 영상: 생명력 재생)
#     → 10:05 우측 결정화 + 완벽한 정신의 에센스(그 접미를 지우고 접두 최대 마나 %) → 12:10 우측 찬미 + 상위 찬미 + 완벽한 엑잘(접미 2개, 영상: 둘 다 잡옵)
#     → 13:13 뒤바뀐 빗장뼈 + 메아리로 빈 접두 훼손 → 공개(별세계 획득 피해 중 카오스, 3~5번에 한 번), 빗나가면 빛의 징조 + 소멸(14:35 네 번째에 12%)
#     → 15:41 접미 정리: 우측 소멸 2번 → 완벽한 엑잘(우측·상위 찬미) 다시 잡옵 → 소멸 2번 → 완벽한 엑잘(카오스 저항 + 민첩) → 절사 + 우측 말소 + 카오스(민첩 → 모든 원소 저항)
# 실행: cd scripts/graphs && python3 gen_d3lebron_mnemonic_ring.py  → d3lebron-mnemonic-ring-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/d3lebron-mnemonic-ring-v2.json'
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

J = lambda s: L(s, '잡옵', 'Junk option', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
CS = DB('s', 34, ['cs']); CSF = DB('s', 34, ['cs'], 'f')                  # 시전 속도 (22—24)% 1티어(분열)
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkp'])
MQ = DB('p', 71, ['mq'], 'c')                                             # 최대 퀄리티 +20% (균열의 에센스)
MN = DB('p', 10, ['mn'])                                                  # 마나 최대치 +(165—179) 1티어
MP = DB('p', 67, ['mp'], 'c')                                             # 최대 마나 (4—6)% (완벽한 정신의 에센스)
CG = DB('p', 86, ['cg'], 'd')                                             # 주문이 피해의 (8—12)%를 카오스 피해로 획득(별세계 훼손)
CR = DB('s', 8, ['vs'], 'n', 1)                                           # 카오스 저항 +(20—23)% 2티어(영상 +20%)
AR = DB('s', 7, ['vs'], 'n', 1)                                           # 모든 원소 저항 +(12—14)% 2티어(영상 +14%)
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
VS = K('카오스 저항·모든 원소 저항·마나 재생·지능', 'Chaos resistance, all elemental resistances, mana regeneration or intelligence')

g = {
 'id': 'd3lebron-mnemonic-ring-v2', 'recipe': 'd3lebron-mnemonic-ring-v2', 'cls': CLS, 'base': 'Mnemonic Ring', 'ilvl': 79,
 'basePrice': {'Divine_Orb': 1.5},   # 1:21 '시전 속도 1티어 4옵션 베이스 1~2 div' — 범위의 가운데(내부 결정)
 'note': ('2026-11-14 RECIPE-E: D3lebronjames 아크 토템 마나 기억 반지(youtube JeA3cg79qZY, 조사 g126 — docs/craft-guides.md 7차 단계 노트·18:08 화면 단계표·완성 툴팁). '
          '분열 전에 좌측 결정화 + 심연의 에센스로 접두 하나를 징표로 바꾸고 빗장뼈로 훼손(미공개)해 분열 확률을 1/3로 올림, 균열의 에센스 + 신경 기폭제 40, '
          '우측 결정화 + 완벽한 정신의 에센스로 빗나간 접미 자리를 접두 최대 마나 %로 옮김, 뒤바뀐 빗장뼈 별세계 카오스 획득. '
          '내부 결정: ① 구입 베이스는 시전 속도 + 접두 잡옵 2개 + 접미 잡옵 1개(옵션 4개, 노트에 자리 배분 없음), 값 1~2 div의 가운데 1.5 div, 신성 오브로 24 맞추기는 뺌 '
          '② 징표를 훼손한 뼈는 아이템 레벨 79에 쓸 수 있는 가장 싼 보존된 빗장뼈 ③ 15:41 "우측 말소 2번 → 완벽한 엑잘 접미 2개"는 접미 두 자리가 비어야 하므로 우측 소멸의 징조 + 소멸로 봄(마지막 절사는 우측 말소의 징조 그대로) '
          '④ 접미 정리는 영상 순서대로: 유효 옵션이 없으면 우측 소멸로 비우고 다시 완벽한 엑잘, 하나면 절사 + 우측 말소 + 카오스 반복. '
          '등급: 하이엔드 = 최대 마나 1티어 + 유효 접미 2개 1~2티어(영상 결과 카오스 저항 +20%·모든 원소 저항 +14% 모두 2티어), 밸런스 = 최대 마나 1~2티어 + 유효 접미 2개 1~4티어. '
          '분열 대상 시전 속도는 두 등급 모두 1티어(구입 베이스).'),
 'params': {
  'cT': {'kr': '카오스 최대 마나', 'en': 'Chaos maximum mana', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
  'sT': {'kr': '유효 접미', 'en': 'Useful suffixes', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}}},
 'strategies': [{'id': 'high', 'params': {'cT': 1, 'sT': 2}}, {'id': 'bal', 'params': {'cT': 2, 'sT': 4}}],
 'versions': [
  {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'cT': 1, 'sT': 2}, 'tier': 'high',
   'desc': K('최대 마나 1티어, 유효 접미 2개 1~2티어(영상 결과)', 'T1 maximum mana, two useful suffixes at T1–2 (the video result)')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'cT': 2, 'sT': 4}, 'tier': 'bal',
   'desc': K('최대 마나 1~2티어, 유효 접미 2개 1~4티어', 'T1–2 maximum mana, two useful suffixes at T1–4')}],
 'tags': {
  'cs': {'gi': 34, 'tmax': 1}, 'mkp': {'gi': 69}, 'mq': {'gi': 71}, 'mp': {'gi': 67}, 'cg': {'gi': 86},
  'mn': {'gi': 10, 'tmax': '$cT'}, 'mn1': {'gi': 10, 'tmax': 1}, 'mn2': {'gi': 10, 'tmax': 2},
  'cr': {'gi': 8, 'tmax': '$sT'}, 'ar': {'gi': 7, 'tmax': '$sT'}, 'mr': {'gi': 21, 'tmax': '$sT'}, 'in': {'gi': 2, 'tmax': '$sT'},
  'vs': {'anyOf': ['cr', 'ar', 'mr', 'in'], 'shown': 'cr', 'label': VS},
  'cr2': {'gi': 8, 'tmax': 2}, 'ar2': {'gi': 7, 'tmax': 2}, 'mr2': {'gi': 21, 'tmax': 2}, 'in2': {'gi': 2, 'tmax': 2},
  'cr4': {'gi': 8, 'tmax': 4}, 'ar4': {'gi': 7, 'tmax': 4}, 'mr4': {'gi': 21, 'tmax': 4}, 'in4': {'gi': 2, 'tmax': 4},
  'vs2': {'anyOf': ['cr2', 'ar2', 'mr2', 'in2'], 'shown': 'cr2', 'label': K('카오스 저항·모든 원소 저항·마나 재생·지능 1~2티어', 'T1–2 chaos resistance, all elemental resistances, mana regeneration or intelligence')},
  'vs4': {'anyOf': ['cr4', 'ar4', 'mr4', 'in4'], 'shown': 'cr4', 'label': K('카오스 저항·모든 원소 저항·마나 재생·지능 1~4티어', 'T1–4 chaos resistance, all elemental resistances, mana regeneration or intelligence')},
 },
 'require': {'all': [{'has': 'cs'}, {'has': 'mn'}, {'has': 'mp'}, {'has': 'cg'}, {'count': {'tag': 'vs', 'min': 2}},
                     {'full': 'p'}, {'full': 's'}, {'unrev': False}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 1:21~5:15) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='p1',
  start={'rar': 'rare', 'mods': [{'tag': 'cs'}, {'junk': 'p'}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('시전 속도 1티어 레어 기억 반지 구입 (옵션 4개, 아이템 레벨 79)', 'Buy a rare Mnemonic Ring with T1 cast speed (four options, item level 79)'),
  item=[J('p'), J('p'), CS, J('s')])
A(id='p1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Essence_of_the_Abyss', ess='mkp', mark=True, omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵 하나를 지우고 심연의 군주의 징표', 'A junk prefix goes for the Mark of the Abyssal Lord'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'p2'}], item=[MK, J('p'), CS, J('s')])
A(id='p2', kind='act', group='prep', pos=[0, 2], act='desecrate', cur='Preserved_Collarbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표 훼손 — 공개하지 않음(분열 확률 1/3)', 'Desecrate the Mark, left unrevealed (fracture odds 1/3)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 분열되지 않음)', 'en': 'Desecrated (unrevealed, cannot fracture)'}],
  edges=[{'to': 'p3'}], item=[UN('p'), J('p'), CS, J('s')])
A(id='p3', kind='act', group='prep', pos=[0, 3], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('시전 속도 분열 (공개된 옵션 3개 중 하나)', 'Fracture cast speed (one of the three revealed options)'), show=['cs'],
  edges=[{'if': {'fractured': 'cs'}, 'to': 'p4', 'res': 'ok', 'label': K('시전 속도 분열', 'Cast speed fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  ask=K('시전 속도가 분열됐나?', 'Cast speed fractured?'), item=[UN('p'), J('p'), CSF, J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 3], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('시전 속도가 아닌 옵션이 분열되면 새 베이스로 처음부터(영상: 4개 중 1개 성공)', 'Another option fractured: start over on a new base (video: one of four worked)'))
A(id='p4', kind='cleanup', group='prep', pos=[0, 4], keep=[], maxJunk=1, label=ANN, goal=K('분열 + 옵션 1개만 남기기', 'Keep the fracture + one option'),
  target=K('분열 + 옵션 1개만 남기기', 'Keep the fracture + one option'), edges=[{'to': 'p5'}], item=[J('p'), CSF])
A(id='p5', kind='act', group='prep', pos=[0, 5], act='essence', cur='Essence_of_the_Breach', ess='mq', label=K('에센스', 'Essence'),
  goal=K('남은 옵션을 지우고 최대 퀄리티 +20%', 'The remaining option goes for +20% maximum quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'p6'}], item=[MQ, CSF])
A(id='p6', kind='act', group='prep', pos=[0, 6], act='quality', cur='Neural_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('마나 퀄리티 40%', '40% mana quality'), showText=[K('신경 기폭제 40개', '40 Neural Catalysts')], edges=[{'to': 'ms'}], item=[MQ, CSF])
# ---------------- 옵션 추가 작업 (영상 6:00~18:08) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='m1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MQ, CSF])
A(id='m1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 첫 번째 옵션 — 최대 마나', 'First prefix: maximum mana'),
  goalBy={'high': K('접두 첫 번째 옵션 — 최대 마나 1티어', 'First prefix: T1 maximum mana'), 'bal': K('접두 첫 번째 옵션 — 최대 마나 1~2티어', 'First prefix: T1–2 maximum mana')},
  show=['mn'], edges=[{'if': {'has': 'mn'}, 'to': 'm2', 'res': 'ok'}, {'to': 'm1', 'res': 'fail', 'hide': True}], item=[MN, CSF])
A(id='m2', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('결정화가 지울 접미 잡옵 (영상: 생명력 재생)', 'A junk suffix for the Crystallisation (video: life regeneration)'),
  showText=[{'s': 's', 'kr': '잡옵 1개', 'en': 'One junk option'}], edges=[{'to': 'm3'}], item=[MN, CSF, J('s')])
A(id='m3', kind='act', group='main', pos=[0, 10.4], act='essence', cur='Perfect_Essence_of_the_Mind', ess='mp', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 접두 최대 마나 %', 'Clear the junk suffix for a maximum mana % prefix'),
  showText=[{'s': 'p', 'kr': '최대 마나 (4—6)% 증가 (제작 옵션)', 'en': '(4—6)% increased maximum Mana (crafted)'}], edges=[{'to': 'm4'}], item=[MN, MP, CSF])
A(id='m4', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 두 번째·세 번째 옵션 — 나오는 대로 (영상: 둘 다 잡옵)', 'Second and third suffixes: keep what comes (video: both junk)'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'm5'}], item=[MN, MP, CSF, J('s'), J('s')])
A(id='m5', kind='act', group='main', pos=[0, 12.4], act='desecrate', cur='Altered_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('빈 접두 훼손', 'Desecrate the empty prefix'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'm6'}], item=[MN, MP, UN('p'), CSF, J('s'), J('s')])
A(id='m6', kind='act', group='main', pos=[0, 13.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cg', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 주문 카오스 획득', 'Third prefix (desecrated): spell damage gained as chaos'), show=['cg'],
  edges=[{'if': {'all': [{'added': 'cg'}, {'count': {'tag': 'vs', 'min': 2}}]}, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'all': [{'added': 'cg'}, {'has': 'vs'}]}, 'to': 's3', 'res': 'ok', 'hide': True},
         {'if': {'added': 'cg'}, 'to': 's1', 'res': 'ok'},
         {'to': 'm6x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[MN, MP, CG, CSF, J('s'), J('s')])
A(id='m6x', kind='act', group='main', pos=[1, 13.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'm5', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='s1', kind='cleanup', group='main', pos=[0, 14.4], side='s', keep=[], maxJunk=0, label=K('소멸의 오브 + 우측 소멸의 징조', 'Orb of Annulment + Omen of Dextral Annulment'),
  goal=K('접미 잡옵 2개 지우기', 'Remove both junk suffixes'), target=K('접미를 분열 옵션만 남기기', 'Clear the suffixes down to the fracture'),
  edges=[{'to': 's2'}], item=[MN, MP, CG, CSF])
A(id='s2', kind='act', group='main', pos=[0, 15.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 두 번째·세 번째 옵션 — 유효 옵션 (영상: 세 번째에 카오스 저항 + 민첩)', 'Second and third suffixes: useful options (video: chaos resistance + dexterity on the third try)'),
  goalBy={'high': K('접미 두 번째·세 번째 옵션 — 유효 옵션 1~2티어 (영상: 세 번째에 카오스 저항 + 민첩)', 'Second and third suffixes: T1–2 useful options (video: chaos resistance + dexterity on the third try)'),
          'bal': K('접미 두 번째·세 번째 옵션 — 유효 옵션 1~4티어', 'Second and third suffixes: T1–4 useful options')},
  show=['vs'], edges=[{'if': {'count': {'tag': 'vs', 'min': 2}}, 'to': 'ok', 'res': 'ok', 'hide': True},
                      {'if': {'has': 'vs'}, 'to': 's3', 'res': 'ok'},
                      {'to': 's1', 'res': 'fail', 'label': K('둘 다 잡옵', 'Both junk')}],
  item=[MN, MP, CG, CSF, CR, J('s')])
A(id='s3', kind='act', group='main', pos=[0, 16.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Whittling', 'Omen_of_Dextral_Erasure'],
  label=K('절사 + 카오스', 'Whittling + Chaos'), goal=K('접미 잡옵을 유효 옵션으로 (영상: 민첩 → 모든 원소 저항)', 'Turn the junk suffix into a useful option (video: dexterity into all elemental resistances)'),
  show=['vs'], edges=[{'if': {'count': {'tag': 'vs', 'min': 2}}, 'to': 'ok', 'res': 'ok'},
                      {'if': {'has': 'vs'}, 'to': 's3', 'res': 'fail', 'hide': True},
                      {'to': 's1', 'res': 'fail', 'hide': True}],
  item=[MN, MP, CG, CSF, CR, AR])
A(id='ok', kind='done', group='main', pos=[0, 17.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L1', 'nodes': ['m5', 'm6', 'm6x'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal'},
 {'id': 'L2', 'nodes': ['s1', 's2'], 'kr': '접미 유효 옵션', 'en': 'Useful suffixes'},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'mn1'}, {'tag': 'mp', 'ess': True}, {'tag': 'cg', 'des': True}, {'tag': 'cs', 'fr': True}, {'tag': 'vs2'}, {'tag': 'vs2'}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'mn2'}, {'tag': 'mp', 'ess': True}, {'tag': 'cg', 'des': True}, {'tag': 'cs', 'fr': True}, {'tag': 'vs4'}, {'tag': 'vs4'}]}]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
