# W21 2026-11-13: Barricade 험악한 육척봉(B4yShuKydt0) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W21-barricade/timeline.md, frames/ (영상 0:00~24:13 화면 대조. 10:05~10:36 두 번째 베이스 과정은 편집으로 빠짐)
# 실행: cd scripts/graphs && python3 gen_barricade_quarterstaff.py  → barricade-quarterstaff-v2.json (gen_batch8.py 끝에서 자동 호출, 그 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/barricade-quarterstaff-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CRn = L('s', '치명타 확률 +(4.41—5)%', '+(4.41—5)% to Critical Hit Chance', 'n', ['crit'])
CR = L('s', '치명타 확률 +(4.41—5)% (분열)', '+(4.41—5)% to Critical Hit Chance (fractured)', 'f', ['crit'])
ME = L('s', '모든 근접 스킬 레벨 +5', '+5 to Level of all Melee Skills', 'n', ['melee'])
AS = L('s', '공격 속도 (26—28)% 증가 (훼손)', '(26—28)% increased Attack Speed (desecrated)', 'd', ['as'])
EA = L('p', '공격 스킬의 원소 피해 (120—139)% 증가', '(120—139)% increased Elemental Damage with Attacks', 'n', ['eatk'])
FI = L('p', '화염 피해 (135—156)~(205—236) 추가', 'Adds (135—156) to (205—236) Fire Damage', 'n', ['fire'])
CO = L('p', '냉기 피해 (112—124)~(168—189) 추가', 'Adds (112—124) to (168—189) Cold Damage', 'n', ['cold'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
R = lambda s: L(s, '랜덤 옵션', 'Random option', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
P = {'high': {'rT': 1, 'eT': 1}, 'bal': {'rT': 2, 'eT': 2}}

g = {
 'id': 'barricade-quarterstaff-v2', 'recipe': 'barricade-quarterstaff-v2', 'cls': 'Quarterstaves', 'base': 'Sinister Quarterstaff', 'ilvl': 81, 'basePrice': {'Divine_Orb': 7},   # 4:52 거래소 약 7 div
 'note': ('2026-11-13 W21 영상 전체 화면 대조. 성공 회차(Corpse Mast) 한 줄: 특출난 험악한 육척봉(아이템 레벨 81, 소켓 3개, 노멀, 약 7 div, 4:52) → '
          '대장장이의 숫돌 20%(5:45) → 진화(7:36 정확도) → 제왕(7:42 근접 스킬 +3) → '
          '소멸의 오브로 옵션 하나만(7:50) → 카오스로 치명타 확률 1티어(8:02) → 엑잘 2번 + 보존된 턱뼈(9:35 공격 속도·정확도와 빛 반경·접두 미공개 훼손) → 분열 1/3(10:00, 첫 베이스는 공격 속도 분열로 실패 10:02) → '
          '두 번째 베이스 치명타 분열(10:24) → 분열 + 근접 스킬 +5 두 옵션(10:36, 중간 과정은 편집으로 빠짐) → 우측 강령술 + 보존된 턱뼈(12:02) → 심연의 메아리 공개, 빗나가면 빛의 징조 + 소멸의 오브(12:50 처치 시 생명력) → '
          '공격 속도 28%(13:06) → 상위 찬미 + 완벽한 엑잘(14:50 공격 원소 피해 1티어 + 화염 5티어) → 절사 + 완벽한 카오스(15:42 번개 3티어 … 16:35 화염 1티어) → '
          '완벽한 엑잘(17:28 물리 피해 추가 4티어) → 절사 + 완벽한 카오스(17:39 번개 2티어 → 17:46 물리 %·정확도 1티어) → 좌측 소멸의 징조 + 소멸의 오브(19:32~19:36) → 완벽한 엑잘(19:46 냉기 5티어) → '
          '절사 + 완벽한 카오스(20:05 번개 2티어 … 20:43 냉기 1티어 완성). 신성한 오브(8:30 치명타 4.8 → 5%)는 정책 14장대로 뺌. 룬·영혼 핵 3개(23:40)·세를의 승리(21:00 말로만)·히네코라 + 바알 오브(23:50 말로만)는 제작과 무관해 뺌. '
          '바알 대장장이의 주입기로 30%(6:28 21% → 6:52 30%, 주입기 10 → 2개)는 사용자 결정(2026-11-13 06:40)대로 뺌, 퀄리티 20% 베이스. '
          '접두 목표는 영상 계획(3:00·15:50 공격 원소 피해·화염·냉기·번개 피해 추가 1티어 중 셋)대로 먼저 뜬 것, 접미 훼손은 공격 속도·치명타 피해 1티어 중 먼저 뜬 것(12:00).'),
 'params': {'rT': {'kr': '공격 속도·치명타 피해', 'en': 'Attack speed or crit damage', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
            'eT': {'kr': '원소 피해 접두', 'en': 'Elemental prefixes', 'values': {'1': K('1티어 옵션 3개', 'Three T1 options'), '2': K('1~2티어 옵션 2개, 세 번째는 랜덤 옵션', 'Two T1–2 options, the third random')}}},
 'strategies': [{'id': 'high', 'params': P['high']}, {'id': 'bal', 'params': P['bal']}],
 'versions': [{'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': P['bal'], 'tier': 'bal',
               'desc': K('원소 피해 접두 1~2티어 2개 + 랜덤 옵션, 훼손 공격 속도·치명타 피해 1~2티어', 'Two T1–2 elemental prefixes + a random one, T1–2 desecrated attack speed or crit damage')},
              {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': P['high'], 'tier': 'high',
               'desc': K('영상: 원소 피해 접두 1티어 3개 + 훼손 공격 속도 1티어', 'Video: three T1 elemental prefixes + T1 desecrated attack speed')}],
 'tags': {'crit': {'gi': 18, 'tmax': 1}, 'melee': {'gi': 10, 'tmax': 1},
          'as': {'gi': 16, 'tmax': '$rT'}, 'cdmg': {'gi': 19, 'tmax': '$rT'},
          'rev': {'anyOf': ['as', 'cdmg'], 'label': K('공격 속도·치명타 피해', 'Attack speed or critical damage bonus')},
          'as1': {'gi': 16, 'tmax': 1}, 'cdmg1': {'gi': 19, 'tmax': 1}, 'as2': {'gi': 16, 'tmax': 2}, 'cdmg2': {'gi': 19, 'tmax': 2},
          'rev1': {'anyOf': ['as1', 'cdmg1'], 'label': K('공격 속도·치명타 피해 보너스 1티어', 'T1 attack speed or critical damage bonus')},
          'rev2': {'anyOf': ['as2', 'cdmg2'], 'label': K('공격 속도·치명타 피해 보너스 1~2티어', 'T1–2 attack speed or critical damage bonus')},
          'eatk': {'gi': 23, 'tmax': '$eT'}, 'fire': {'gi': 4, 'tmax': '$eT'}, 'cold': {'gi': 5, 'tmax': '$eT'}, 'lflat': {'gi': 7, 'tmax': '$eT'},
          'ele': {'anyOf': ['eatk', 'fire', 'cold', 'lflat'], 'label': K('공격 스킬의 원소 피해·화염·냉기·번개 피해 추가', 'Elemental damage with attacks or added fire, cold or lightning damage')},
          'eatk1': {'gi': 23, 'tmax': 1}, 'fire1': {'gi': 4, 'tmax': 1}, 'cold1': {'gi': 5, 'tmax': 1}, 'lflat1': {'gi': 7, 'tmax': 1},
          'eatk2': {'gi': 23, 'tmax': 2}, 'fire2': {'gi': 4, 'tmax': 2}, 'cold2': {'gi': 5, 'tmax': 2}, 'lflat2': {'gi': 7, 'tmax': 2},
          'ele1': {'anyOf': ['eatk1', 'fire1', 'cold1', 'lflat1'], 'label': K('공격 스킬의 원소 피해·화염·냉기·번개 피해 추가 1티어', 'T1 elemental damage with attacks or added fire, cold or lightning damage')},
          'ele2': {'anyOf': ['eatk2', 'fire2', 'cold2', 'lflat2'], 'label': K('공격 스킬의 원소 피해·화염·냉기·번개 피해 추가 1~2티어', 'T1–2 elemental damage with attacks or added fire, cold or lightning damage')},
          'keep': {'anyOf': ['melee', 'rev', 'ele']}},   # 사용자 경향 11-13: 영상 계획이 '넷 중 아무거나'라 먼저 뜬 것
 'require': {'all': [{'has': 'melee'}, {'has': 'rev'}, {'count': {'tag': 'ele', 'min': 2}}, {'any': [{'param': {'eT': 2}}, {'count': {'tag': 'ele', 'min': 3}}]}, {'full': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'ele1'}, {'tag': 'ele1'}, {'tag': 'ele1'}, {'tag': 'crit', 'fr': True}, {'tag': 'melee'}, {'tag': 'rev1', 'des': True}]},
            {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'ele2'}, {'tag': 'ele2'}, {'side': 'p', 'random': True}, {'tag': 'crit', 'fr': True}, {'tag': 'melee'}, {'tag': 'rev2', 'des': True}]}],
 'finalItem': {'quality': 20, 'sockets': 3},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='q1', start={'rar': 'normal', 'mods': [], 'quality': 0},
  label=K('특출난 험악한 육척봉 구입 (아이템 레벨 81, 소켓 3개)', 'Buy an exceptional Sinister Quarterstaff (item level 81, three sockets)'), item=[])
A(id='q1', kind='act', group='prep', pos=[0, 1], act='quality', cur='Blacksmiths_Whetstone', count=4, q=20, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 20%', 'Quality 20%'), showText=[K('대장장이의 숫돌 4개', 'Four Blacksmith’s Whetstones')], edges=[{'to': 't1'}], item=[])
A(id='t1', kind='act', group='prep', pos=[0, 3], act='transmute', cur='Orb_of_Transmutation', label=K('매직', 'Magic'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'r1'}], item=[J('x')])
A(id='r1', kind='act', group='prep', pos=[0, 4], act='regal', cur='Regal_Orb', label=K('레어', 'Rare'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'a1'}], item=[J('x'), J('s')])
A(id='a1', kind='cleanup', group='prep', pos=[0, 5], keep=['crit'], maxJunk=1, label=ANN, goal=ANN,
  target=K('옵션 1개만 남기기', 'Keep only one option'), edges=[{'to': 'c0'}], item=[J('s')])
A(id='c0', kind='act', group='prep', pos=[0, 6], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 치명타 확률 1티어', 'T1 critical hit chance suffix'), show=['crit'],
  edges=[{'if': {'has': 'crit'}, 'to': 'e0', 'res': 'ok'}, {'to': 'c0', 'res': 'fail', 'hide': True}], item=[CRn])
A(id='e0', kind='act', group='prep', pos=[0, 7], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('두 번째 옵션 — 분열 조건 옵션 4개', 'Second option: the fracture needs four'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'e0b'}], item=[CRn, J('s')])
A(id='e0b', kind='act', group='prep', pos=[0, 8], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('세 번째 옵션 — 분열 조건 옵션 4개', 'Third option: the fracture needs four'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'd0'}], item=[CRn, J('s'), J('s')])
A(id='d0', kind='act', group='prep', pos=[0, 9], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 확률 1/3', 'Fourth option (desecrated): fracture odds 1 in 3'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f0'}],
  item=[UN('p'), CRn, J('s'), J('s')])
A(id='f0', kind='act', group='prep', pos=[0, 10], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('치명타 확률이 분열되면 성공', 'Success when critical hit chance fractures')],
  edges=[{'if': {'fractured': 'crit'}, 'to': 'hc', 'res': 'ok', 'label': K('치명타 확률 분열', 'Critical hit chance fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[UN('p'), CR, J('s'), J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 10.6], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('치명타 확률이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='hc', kind='cleanup', group='prep', pos=[0, 11.6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[CR, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 13], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[CR, J('s')])
A(id='c1', kind='act', group='main', pos=[0, 14], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 근접 스킬 +5', '+5 melee skills suffix'), show=['melee'],
  edges=[{'if': {'has': 'melee'}, 'to': 'b1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[CR, ME])
A(id='b1', kind='act', group='main', pos=[0, 15], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Dextral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'rv'}], item=[CR, ME, UN('s')])
A(id='rv', kind='act', group='main', pos=[0, 16], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev', label=K('공개', 'Reveal'),
  goal=K('접미 공격 속도 1티어 — 치명타 피해 보너스 1티어와 함께 먼저 뜬 것', 'T1 attack speed suffix: or T1 critical damage bonus, whichever lands first'),
  show=['as', 'cdmg'],
  edges=[{'if': {'added': 'rev'}, 'to': 'p1', 'res': 'ok'}, {'to': 'rvx', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[CR, ME, AS])
A(id='rvx', kind='act', group='main', pos=[1, 16], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'b1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='p1', kind='act', group='main', pos=[0, 17], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 옵션 2개', 'Two prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'if': {'count': {'tag': 'ele', 'min': 2}}, 'to': 'p4', 'res': 'ok'}, {'to': 'p2', 'res': 'fail'}], item=[EA, J('p'), CR, ME, AS])
A(id='p2', kind='act', group='main', pos=[0, 18], act='chaos', cur='Perfect_Chaos_Orb', trim={'side': 'p', 'keep': 'keep'}, label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('가장 낮은 접두를 원소 피해로 — 먼저 뜬 것', 'The lowest prefix into elemental damage: whichever lands first'),
  show=['fire', 'cold', 'lflat', 'eatk'],
  edges=[{'if': {'count': {'tag': 'ele', 'min': 2}}, 'to': 'p4', 'res': 'ok'}, {'to': 'p2', 'res': 'fail', 'hide': True}], item=[EA, FI, CR, ME, AS])
A(id='p4', kind='act', group='main', pos=[0, 19], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션', 'Third prefix'), show=['cold', 'lflat', 'fire', 'eatk'],
  edges=[{'if': {'count': {'tag': 'ele', 'min': 3}}, 'to': 'ok', 'res': 'ok'},
         {'if': {'all': [{'param': {'eT': 1}}, {'whittleSafe': {'tag': 'keep'}}]}, 'to': 'p5', 'res': 'fail'},
         {'if': {'param': {'eT': 1}}, 'to': 'p5x', 'res': 'fail'},
         {'to': 'ok', 'res': 'fail', 'label': K('랜덤 옵션', 'Random option')}],
  item=[EA, FI, CO, CR, ME, AS])
A(id='p5', kind='act', group='main', pos=[1, 19], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('가장 낮은 접두를 원소 피해로', 'The lowest prefix into elemental damage'), show=['cold', 'lflat', 'fire', 'eatk'],
  edges=[{'if': {'count': {'tag': 'ele', 'min': 3}}, 'to': 'ok', 'res': 'ok'},
         {'if': {'whittleSafe': {'tag': 'keep'}}, 'to': 'p5', 'res': 'fail'},
         {'to': 'p5x', 'res': 'fail'}])
A(id='p5x', kind='act', group='main', pos=[2, 19], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=ANN, goal=ANN,
  target=K('접두 옵션 하나 지우기', 'Remove one prefix'), edges=[{'to': 'p4'}])
A(id='ok', kind='done', group='main', pos=[0, 20], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['b1', 'rv', 'rvx'], 'kr': '훼손 공개', 'en': 'Reveal'},
 {'id': 'L2', 'nodes': ['p4', 'p5', 'p5x'], 'kr': '접두 세 번째 옵션', 'en': 'Third prefix', 'fold': True,
  'goal': K('접두 원소 피해 1티어 세 번째 — 냉기·번개·화염 피해 추가·공격 스킬의 원소 피해 중 먼저 뜬 것', 'A third T1 elemental prefix: whichever of added cold, lightning, fire or elemental damage with attacks lands first'),
  'goalBy': {'high': K('접두 원소 피해 1티어 세 번째 — 냉기·번개·화염 피해 추가·공격 스킬의 원소 피해 중 먼저 뜬 것', 'A third T1 elemental prefix: whichever of added cold, lightning, fire or elemental damage with attacks lands first'),
             'bal': K('접두 세 번째 옵션 — 완벽한 엑잘 한 번, 랜덤 옵션', 'Third prefix: one Perfect Exalt, a random option')},
  'steps': [K('완벽한 엑잘로 접두 세 번째 옵션', 'Perfect Exalt for the third prefix') | {'node': 'p4'},
            K('빗나간 접두가 가장 낮은 옵션이면 절사 + 완벽한 카오스 반복', 'Missed prefix is the lowest option: Whittling + Perfect Chaos, again and again') | {'node': 'p5'},
            K('잡옵이 가장 낮은 옵션이 아니면 좌측 소멸의 징조 + 소멸의 오브 → 1번부터', 'Junk is not the lowest: Omen of Sinistral Annulment + Annulment, then from step 1') | {'node': 'p5x'}],
  'item': [EA, FI, CO, CR, ME, AS],
  'itemBy': {'high': [EA, FI, CO, CR, ME, AS], 'bal': [EA, FI, R('p'), CR, ME, AS]}},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
