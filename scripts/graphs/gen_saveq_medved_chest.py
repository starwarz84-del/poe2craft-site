# RECIPE-B 2026-11-14: SaVeQ 메드베드 정신력 갑옷(youtu.be/5puSqTO0AKM, 2026-10-11, 0.5.5) — 조사 g87(docs/craft-guides.md 5차)
# 영상 흐름 한 줄: 흐르는 의복 → 레어 카오스 반복으로 정신력 1티어 → 보존된 갈비뼈 미공개 훼손 → 분열(정신력) → 메드베드의 보살핌 장착 → 소멸로 분열만 남김
#   → 카오스 반복으로 메드베드 % 하나 → 좌측 찬미 + 완벽한 엑잘로 다른 하나(빗나가면 소멸) → 상위 찬미 + 완벽한 엑잘 접미 2개 → 말소·절사 + 카오스 → 뼈 훼손 + 메아리 + 빛 반복
# 실행: cd scripts/graphs && python3 gen_saveq_medved_chest.py  → saveq-medved-chest-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-medved-chest-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
CLS = 'Body_Armours_int'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, ti=0, m='n', tags=None, sfx=None):   # 클래스 파일 티어 글 그대로
    g = D['groups'][gi]; t = g['t'][ti]; kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if sfx: kr, en = kr + ' (' + sfx[0] + ')', en + ' (' + sfx[1] + ')'
    return L(g['g'], kr, en, m, tags)

SPn = T(14, 0, 'n', ['sp1'])
SP = T(14, 0, 'f', ['sp1'], ('분열', 'fractured'))
ISP = T(51, 0, 'n', ['isp'])
IMA = T(50, 0, 'n', ['ima'])
CR = T(2, 0, 'n', ['crT'])
IN = T(0, 0, 'n', ['inT'])
SRE = T(21, 0, 'd', ['sre'])
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
JX = L('x', '잡옵', 'Junk', 'j')
RN = L('r', '메드베드의 보살핌', 'Medved’s Tending', 'r')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'saveq-medved-chest-v2', 'recipe': 'saveq-medved-chest-v2', 'cls': CLS, 'base': 'Flowing Raiment', 'ilvl': 82,
 'note': ('2026-11-14 RECIPE-B: SaVeQ 스파크 토템용 지능 갑옷(youtu.be/5puSqTO0AKM, 조사 g87 — docs/craft-guides.md 5차). '
          '0:32 흐르는 의복 아이템 레벨 82(약 4 div) → 6:14 레어로 만들어 카오스 오브 반복으로 정신력 1티어(영상: 완벽한 진화·확장 + 소멸 반복보다 쌈, 약 700 카오스에 1티어 2개) → '
          '8:26 보존된 갈비뼈로 미공개 훼손(분열 조건 옵션 4개, 미공개라 분열되지 않음) → 분열의 오브(정신력이 분열되면 성공, 영상 3개 중 2개 성공, 실패 베이스는 판매) → '
          '9:30 메드베드의 보살핌 장착(정신력 %·최대 마나 % 옵션이 열림) → 소멸로 분열만 남김 → 카오스 반복으로 정신력 %·최대 마나 % 중 하나(평균 약 200 카오스) → '
          '다른 하나는 좌측 찬미의 징조 + 완벽한 엑잘티드 오브, 빗나가면 소멸(23:59 약 6번 만에 성공) → 24:30 상위 찬미의 징조 + 완벽한 엑잘로 접미 2개 → '
          '우측 말소·절사의 징조 + 카오스 오브로 잡옵 접미를 저항·지능으로(영상 5개) → 25:34 뼈 훼손 + 심연의 메아리, 빗나가면 빛의 징조 반복으로 스킬의 정신력 점유 효율(26:53 여덟 번째). '
          '자막의 "메드베드 영혼 핵"은 데이터 이름 메드베드의 보살핌(Medved’s Tending)으로 적음. 메드베드 옵션은 공개 가중치가 없어 시뮬이 추정값(일반 옵션 평균)을 씀 — 확률·비용은 추정. '
          '내부 결정: 레어로 만드는 오브 등급(진화·확장·제왕은 일반 등급으로, 영상은 "제왕으로 레어"만 말함), 마지막 훼손 뼈는 보존된 갈비뼈(영상은 "뼈"만 말함, 공개 옵션이 단일 티어라 등급 무관), '
          '좌측 찬미 엑잘이 빗나갔을 때 소멸로 잡옵을 지우고 메드베드 %가 남으면 다시 엑잘·지워지면 카오스부터(영상 "소멸 후 카오스로 돌아감"을 짧은 되돌림으로), 접미 다시 굴리기는 절사·말소 자동 선택(정책 4장 C13). '
          '신성한 오브·퀄리티·철 룬은 정책 9·14장대로 뺌.'),
 'params': {'sT': {'kr': '접미 저항·지능', 'en': 'Resistance / Intelligence suffixes', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'sT': 1}}, {'id': 'bal', 'params': {'sT': 2}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'sT': 2}, 'tier': 'bal',
   'desc': K('접미 저항·지능 1~2티어까지 받음', 'Resistance / Intelligence suffixes accepted at T1–2')},
  {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'sT': 1}, 'tier': 'high',
   'desc': K('영상: 접미 냉기 저항·지능 1티어', 'Video: T1 cold resistance and Intelligence suffixes')}],
 'tags': {
  'sp1': {'gi': 14, 'tmax': 1}, 'isp': {'gi': 51}, 'ima': {'gi': 50},
  'med': {'anyOf': ['isp', 'ima'], 'shown': ['isp', 'ima'], 'label': K('메드베드 정신력 %·최대 마나 %', 'Medved % Spirit or % maximum Mana')},
  'frT': {'gi': 1, 'tmax': '$sT'}, 'crT': {'gi': 2, 'tmax': '$sT'}, 'lrT': {'gi': 3, 'tmax': '$sT'}, 'chT': {'gi': 4, 'tmax': '$sT'}, 'inT': {'gi': 0, 'tmax': '$sT'},
  'sv': {'anyOf': ['frT', 'crT', 'lrT', 'chT', 'inT'], 'shown': ['crT', 'inT'], 'label': K('저항·지능', 'A resistance or Intelligence')},
  'sre': {'gi': 21}},
 'require': {'all': [{'has': 'sp1'}, {'count': {'tag': 'med', 'min': 2}}, {'count': {'tag': 'sv', 'min': 2}}, {'has': 'sre'}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0', 'xsub': ["Medved's Tending"], 'xroll': True,
 'basePrice': {'Divine_Orb': 4},
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (0:32~9:30) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='t1', start={'rar': 'normal', 'mods': []},
  label=K('흐르는 의복 구입 (노멀, 아이템 레벨 82)', 'Buy a Flowing Raiment (normal, item level 82)'), item=[])
A(id='t1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'a1'}], item=[JX])
A(id='a1', kind='act', group='prep', pos=[0, 2], act='augment', cur='Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('매직 옵션 2개', 'Two magic options'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'r1'}], item=[J('p'), J('s')])
A(id='r1', kind='act', group='prep', pos=[0, 3], act='regal', cur='Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 옵션 3개', 'Rare with three options'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'c0'}], item=[J('p'), J('p'), J('s')])
A(id='c0', kind='act', group='prep', pos=[0, 4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 정신력 1티어', 'T1 Spirit prefix'), show=['sp1'], skipIf={'has': 'sp1'}, skipTo='d0',
  edges=[{'if': {'has': 'sp1'}, 'to': 'd0', 'res': 'ok'}, {'to': 'c0', 'res': 'fail', 'hide': True}], item=[SPn, J('p'), J('s')])
A(id='d0', kind='act', group='prep', pos=[0, 5], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f0'}], item=[SPn, J('p'), J('s'), UN('s')])
A(id='f0', kind='act', group='prep', pos=[0, 6], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'), showText=[K('정신력이 분열되면 성공', 'Success when Spirit fractures')],
  edges=[{'if': {'fractured': 'sp1'}, 'to': 'ms', 'res': 'ok', 'label': K('정신력 분열', 'Spirit fractured')},
         {'to': 'xf', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}], item=[SP, J('p'), J('s'), UN('s')])
A(id='xf', kind='exit', group='prep', pos=[1, 6], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 판매, 새 베이스', 'Another option fractured: sell it, new base'),
  note=K('정신력이 아닌 옵션이 분열되면 그 베이스는 팔고 새 베이스로 처음부터', 'Another option fractured: sell that base and start over on a new one'))
# ---------------- 옵션 추가 작업 (9:30~26:53) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='rn', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, J('p'), J('s'), UN('s')])
A(id='rn', kind='act', group='main', pos=[0, 8.4], act='rune', rune={'kr': '메드베드의 보살핌', 'en': 'Medved’s Tending'}, label=K('룬', 'Rune'),
  goal=K('메드베드의 보살핌 장착', 'Socket Medved’s Tending'), showText=[K('메드베드 옵션이 붙을 수 있음', 'Medved lines can roll')],
  edges=[{'to': 'cl'}], item=[SP, J('p'), J('s'), UN('s'), RN])
A(id='cl', kind='cleanup', group='main', pos=[0, 9.4], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('분열만 남기기', 'Keep only the fracture'), edges=[{'to': 'c1'}], item=[SP, RN])
A(id='c1', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 정신력 % — 메드베드 정신력 %·최대 마나 % 중 먼저 뜬 것', 'Prefix % Spirit: Medved % Spirit or % maximum Mana, whichever lands first'),
  show=['isp', 'ima'], skipIf={'has': 'med'}, skipTo='e1',
  edges=[{'if': {'has': 'med'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[SP, ISP, RN])
A(id='e1', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 최대 마나 % — 남은 메드베드 옵션', 'Prefix % maximum Mana: the remaining Medved option'), show=['isp', 'ima'],
  edges=[{'if': {'count': {'tag': 'med', 'min': 2}}, 'to': 's1', 'res': 'ok'},
         {'to': 'e1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[SP, ISP, IMA, RN])
A(id='e1x', kind='cleanup', group='main', pos=[1, 11.4], keep=['med'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'lost': 'med', 'to': 'c1', 'label': K('메드베드 옵션이 지워짐 — 카오스부터', 'Medved line removed: back to Chaos')},
         {'to': 'e1', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='s1', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 옵션 2개 — 나오는 대로 (영상: 냉기 저항·에너지 보호막 재충전 속도)', 'Two suffixes: keep what comes (video: cold resistance, energy shield recharge)'),
  showText=[K('랜덤 옵션 2개', 'Two random options')], edges=[{'to': 's2'}], item=[SP, ISP, IMA, CR, J('s'), RN])
A(id='s2', kind='act', group='main', pos=[0, 13.4], act='chaos', cur='Chaos_Orb', trim={'side': 's', 'keep': 'sv'},
  label=K('절사·우측 말소 + 카오스', 'Whittling / Dextral Erasure + Chaos'),
  goal=K('접미 잡옵을 지능 1티어로 — 저항·지능 중 먼저 뜬 것', 'Turn the junk suffix into T1 Intelligence: a resistance or Intelligence, whichever lands first'),
  goalBy={'bal': K('접미 잡옵을 지능 1~2티어로 — 저항·지능 중 먼저 뜬 것', 'Turn the junk suffix into T1–2 Intelligence: a resistance or Intelligence, whichever lands first')},
  show=['frT', 'crT', 'lrT', 'chT', 'inT'], skipIf={'count': {'tag': 'sv', 'min': 2}}, skipTo='d1',
  skipNote=K('접미 저항·지능이 이미 2개면 건너뜀', 'Skipped when two resistance / Intelligence suffixes are already there'),
  edges=[{'if': {'count': {'tag': 'sv', 'min': 2}}, 'to': 'd1', 'res': 'ok'}, {'to': 's2', 'res': 'fail', 'hide': True}], item=[SP, ISP, IMA, CR, IN, RN])
A(id='d1', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=[SP, ISP, IMA, CR, IN, UN('s'), RN])
A(id='d2', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='sre', label=K('공개', 'Reveal'),
  goal=K('접미 세 번째 옵션(훼손) — 스킬의 정신력 점유 효율', 'Third suffix (desecrated): Spirit reservation efficiency of skills'), show=['sre'],
  edges=[{'if': {'added': 'sre'}, 'to': 'ok', 'res': 'ok'}, {'to': 'd2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[SP, ISP, IMA, CR, IN, SRE, RN])
A(id='d2x', kind='act', group='main', pos=[1, 15.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L0', 'nodes': ['c0'], 'kr': '정신력 1티어', 'en': 'T1 Spirit'},
 {'id': 'L1', 'nodes': ['c1', 'e1', 'e1x'], 'kr': '메드베드 접두 2개', 'en': 'Two Medved prefixes'},
 {'id': 'L2', 'nodes': ['s2'], 'kr': '접미 저항·지능', 'en': 'Resistance / Intelligence suffixes'},
 {'id': 'L3', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'sp1', 'fr': True}, {'tag': 'med'}, {'tag': 'med'}, {'tag': 'sv'}, {'tag': 'sv'}, {'tag': 'sre', 'des': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'sp1', 'fr': True}, {'tag': 'med'}, {'tag': 'med'}, {'tag': 'sv'}, {'tag': 'sv'}, {'tag': 'sre', 'des': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
