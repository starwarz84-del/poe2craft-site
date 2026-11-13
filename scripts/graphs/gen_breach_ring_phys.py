# G6 2026-11-13: 균열 반지 물리 플랫 분열 + 원소 플랫(사이트 운영자 제작 방식, 영상 없음) 플로우차트 생성기 — 새 기준(접힌 반복 상자, 등급별 카드)
# 원본 레시피 recipes_batch4.py 'breach-ring-phys', 옛 생성기 gen_batch24.py(끝에서 이 파일을 부름). 영상이 없어 화면 대조 대상 없음.
# 흐름은 옛 그래프 그대로(시뮬 가장 많이 지나는 길을 메인 줄로):
#   공격 시 물리 피해 1티어 분열 + 잡옵 균열 반지 → 카오스 오브(모든 원소 저항 1티어) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 균열의 에센스(최대 퀄리티)
#   → [접힘] 조프의 기폭제 60% + 촉진 + 우측 찬미 + 완벽한 엑잘(화염 저항), 빗나가면 우측 소멸 → 강탈자 기폭제 60%
#   → [접힘] 절사 + 카오스 오브로 최대 퀄리티 지우기, 새 옵션이 접미면 절사·말소 + 상위 카오스로 접미 자리 비우기
#   → 좌측 찬미 + 완벽한 엑잘(접두 채우기) → 좌측 결정화 + 재빠른 합금(공격 속도)
#   → [접힘] 접두 원소 피해 두 개: 완벽한 엑잘 → 절사·말소 + 완벽한 카오스 → 좌측 강령술 + 고대 빗장뼈 → 심연의 메아리 공개 → 빗나가면 빛의 징조 + 소멸.
# RV6 검수 11-13: 합금 상자(b9) 아이템 칸을 원소 피해 확정(I7)에서 남은 접두 랜덤(I8)으로 — 레시피 글 합금 목표가 화염 피해로 나오던 것.
# C2 11-13(RV6 감점 정리): 최악의 경우 선을 맨 위 베이스 대신 상자 옆 '새 베이스' 버림 상자(xw1·xw2)로, 합금 상자는 확정(원소 피해 남음/지워짐 갈래 이름표), 에센셜 화염 저항·공개는 결과 그대로(성공), 9.A 소멸 갈래 이름표.
# 바뀐 곳(옛 그래프 대비): 반복 세 곳을 상자 하나로 접음(옛 9.A·9.A.a 라우터 선과 5.A → 시작 긴 선이 교차하던 것), 완성 카드의 '또는' 줄을 묶음 태그로, 에센셜 훼손 색.
import os, json, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/breach-ring-phys-v2.json'
_src = open(f'{H}/gen_batch22.py').read(); exec(_src[:_src.index('# ---------- 1. 시한')])
_H0 = H
import tempfile
H = tempfile.mkdtemp()   # graph8은 H 폴더에 쓰므로 임시 폴더에서 만든 뒤 OUT으로 옮김(다른 아이템 JSON을 건드리지 않음)

c = 'Rings'; P = {'bal': {'eT': 3, 'fT': 2, 'v': 1}, 'ess': {'eT': 4, 'fT': 3, 'v': 2}}
tags = {'phys': {'gi': 13, 'tmax': 1}, 'allres': {'gi': 7, 'tmax': 1}, 'fres': {'gi': 4, 'tmax': '$fT'}, 'maxq': {'gi': 71}, 'alloy': {'gi': 73},
        'fire': {'gi': 15, 'tmax': '$eT'}, 'cold': {'gi': 17, 'tmax': '$eT'}, 'light': {'gi': 19, 'tmax': '$eT'},
        'ele': {'anyOf': ['fire', 'cold', 'light'], 'label': K('공격 시 화염·냉기·번개 피해 추가', 'Adds fire, cold or lightning damage to attacks')},
        'keepS': {'anyOf': ['allres', 'fres', 'alloy']}, 'keepP': {'anyOf': ['fire', 'cold', 'light']},
        'fire3': {'gi': 15, 'tmax': 3}, 'cold3': {'gi': 17, 'tmax': 3}, 'light3': {'gi': 19, 'tmax': 3},
        'ele3': {'anyOf': ['fire3', 'cold3', 'light3'], 'label': K('공격 시 화염·냉기·번개 피해 추가 1~3티어', 'T1–3 added fire, cold or lightning attack damage')},
        'fres2': {'gi': 4, 'tmax': 2}, 'fres3': {'gi': 4, 'tmax': 3}}
V1 = {'param': {'v': 1}}
PH = itg('p', c, 13, ['phys'], 'f'); AR = itg('s', c, 7, ['allres']); FR = itg('s', c, 4, ['fres'], ti=1)
MQ = itg('p', c, 71, ['maxq'], 'c', suffix=('균열의 에센스', 'Essence of the Breach')); AL = itg('s', c, 73, ['alloy'], 'c', suffix=('재빠른 합금', 'Swift Alloy'))
FI = itg('p', c, 15, ['fire'], ti=2); CO = itg('p', c, 17, ['cold'], ti=2)
I0 = [PH, J('s')]; I1 = [PH, AR]; I2 = [PH, J('p'), AR]; I3 = [PH, MQ, AR]; I4 = I3 + [FR]; I5 = [PH, R1('p'), AR, FR]; I6 = [PH, R1('p'), R1('p'), AR, FR]; I7 = [PH, FI, AR, FR, AL]; I8 = [PH, R1('p'), AR, FR, AL]; I9 = [PH, FI, CO, AR, FR, AL]
nodes = [base('ms', {'rar': 'rare', 'mods': [{'tag': 'phys', 'fr': True}, {'junk': 's'}]}, K('공격 시 물리 피해 1티어 분열 + 잡옵 1개 균열 반지 구입', 'Buy a Breach Ring with fractured T1 physical attack damage + one junk line'), I0),
 mark([0, 0.6], 'b2', I0),
 act('b2', 'main', [0, 1], 'chaos', 'Chaos_Orb', K('접미 첫 번째 옵션', 'First suffix'), None, K('카오스', 'Chaos'), [{'if': {'has': 'allres'}, 'to': 'b3', 'res': 'ok'}, {'to': 'b2', 'res': 'fail'}], I1, show=['allres']),
 act('b3', 'main', [0, 2], 'exalt', 'Exalted_Orb', K('에센스가 지울 접두', 'The prefix for the essence to remove'), [st('p', '랜덤 옵션 1개', 'One random line')], K('엑잘', 'Exalt'), [{'to': 'b4'}], I2, omens=['Omen_of_Sinistral_Exaltation']),
 act('b4', 'main', [0, 3], 'essence', 'Essence_of_the_Breach', K('접두 잡옵을 최대 퀄리티로', 'Swap the junk prefix for maximum quality'), [st('p', '최대 퀄리티 +20% (제작 옵션)', '+20% maximum quality (crafted)')], K('에센스', 'Essence'), [{'to': 'b5'}], I3, ess='maxq', omens=['Omen_of_Sinistral_Crystallisation']),
 act('b5', 'main', [0, 4], 'quality', 'Xophs_Catalyst', K('화염 퀄리티 60%', 'Fire quality 60%'), [st(None, '조프의 기폭제 60개', '60 Xoph’s Catalysts')], K('퀄리티', 'Quality'), [{'to': 'b6'}], I3, count=60),
 act('b6', 'main', [0, 5], 'exalt', 'Perfect_Exalted_Orb', K('접미 두 번째 옵션', 'Second suffix'), None, K('엑잘', 'Exalt'),
     [{'if': {'has': 'fres'}, 'to': 'b7', 'res': 'ok'}, {'if': V1, 'to': 'b6x', 'res': 'fail'}, {'to': 'b7', 'res': 'ok'}], I4, show=['fres'], omens=['Omen_of_Catalysing_Exaltation', 'Omen_of_Dextral_Exaltation'], cat='fres'),
 {'id': 'b6x', 'kind': 'act', 'group': 'main', 'pos': [1, 5], 'act': 'annul', 'cur': 'Orb_of_Annulment', 'omens': ['Omen_of_Dextral_Annulment'],
  'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'target': K('접미 하나 지우기', 'Remove one suffix'),
  'edges': [{'if': {'removed': 'allres'}, 'to': 'xw1', 'res': 'fail', 'lost': 'allres'}, {'to': 'b5', 'res': 'ok'}]},
 {'id': 'xw1', 'kind': 'exit', 'group': 'main', 'pos': [1, 4], 'simTo': 'h1', 'variant': 'fail', 'label': K('모든 원소 저항이 지워짐 — 새 베이스', 'All resistances removed — new base'),
  'note': K('새 베이스로 처음부터', 'Start over on a new base'),
  'over': [{'param': {'v': 2}, 'set': {'kind': 'mark'}}]},   # 에센셜은 4번 소멸이 없어 이 상자에 오는 선이 없음 — 표시 안 된 mark로 바꿔 플로우차트에서 빠지게(fcPrune은 지나지 않은 act·mark만 뺌)
 act('b7', 'main', [0, 6], 'quality', 'Reaver_Catalyst', K('공격 퀄리티 60%', 'Attack quality 60%'), [st(None, '강탈자 기폭제 60개', '60 Reaver Catalysts')], K('퀄리티', 'Quality'), [{'to': 'b8'}], I4, count=60),
 act('b8', 'main', [0, 7], 'chaos', 'Chaos_Orb', K('최대 퀄리티 지우기', 'Remove maximum quality'), [st(None, '최대 퀄리티(레벨이 가장 낮음)가 다른 옵션으로 바뀜', 'Maximum quality (lowest level) turns into another line')], K('카오스', 'Chaos'),
     [{'if': {'removed': 'allres'}, 'to': 'xw2', 'res': 'fail', 'lost': 'allres'}, {'if': {'all': [V1, {'removed': 'fres'}]}, 'to': 'xw2', 'res': 'fail', 'lost': 'fres', 'hide': True}, {'if': {'has': 'maxq'}, 'to': 'b8', 'res': 'fail', 'hide': True}, {'if': {'sideLt': {'side': 's', 'n': 3}}, 'to': 'b9a', 'res': 'ok'}, {'to': 'b8s', 'res': 'fail'}], I5, omens=['Omen_of_Whittling']),
 act('b8s', 'main', [1, 7], 'chaos', 'Greater_Chaos_Orb', K('접미 자리 비우기', 'Free a suffix slot'), [st('s', '접미 잡옵을 다른 옵션으로 (접두로 가면 성공)', 'The junk suffix into another line (done when it goes to the prefixes)')], K('카오스', 'Chaos'),
     [{'if': {'removed': 'allres'}, 'to': 'xw2', 'res': 'fail', 'lost': 'allres', 'hide': True}, {'if': {'all': [V1, {'removed': 'fres'}]}, 'to': 'xw2', 'res': 'fail', 'lost': 'fres', 'hide': True}, {'if': {'sideLt': {'side': 's', 'n': 3}}, 'to': 'b9a', 'res': 'ok'}, {'to': 'b8s', 'res': 'fail'}], None, trim={'side': 's', 'keep': 'keepS'}),
 act('b9a', 'main', [0, 8], 'exalt', 'Perfect_Exalted_Orb', K('접두 두 번째·세 번째 옵션 채우기', 'Fill the second and third prefixes'), [st('p', '랜덤 옵션 1개', 'One random line')], K('엑잘', 'Exalt'), [{'to': 'b9'}], I6, omens=['Omen_of_Sinistral_Exaltation'], skipIf={'full': 'p'}, skipTo='b9'),
 act('b9', 'main', [0, 9], 'essence', 'Swift_Alloy', K('접미 세 번째 옵션 — 접두 둘 중 하나가 지워짐', 'Third suffix: one of the two prefixes goes'), [st('s', '공격 속도 (7—9)% 증가 (제작 옵션)', '(7—9)% increased Attack Speed (crafted)')], K('합금', 'Alloy'),
     [{'if': {'has': 'ele'}, 'to': 'd1', 'res': 'ok', 'label': K('원소 피해가 남음', 'Elemental line kept')}, {'if': V1, 'to': 'e1', 'res': 'ok', 'label': K('원소 피해가 지워짐', 'Elemental line removed')}, {'to': 'd1', 'res': 'ok'}], I8, ess='alloy', omens=['Omen_of_Sinistral_Crystallisation']),
 act('e1', 'main', [0, 10], 'exalt', 'Perfect_Exalted_Orb', K('접두 세 번째 옵션', 'Third prefix'), None, K('엑잘', 'Exalt'),
     [{'if': {'all': [V1, {'has': 'ele'}]}, 'to': 'd1', 'res': 'ok'}, {'if': V1, 'to': 'e2', 'res': 'fail'}, {'to': 'ok', 'res': 'fail'}], None, show=['fire', 'cold', 'light'], omens=['Omen_of_Sinistral_Exaltation']),
 act('e2', 'main', [1, 10], 'chaos', 'Perfect_Chaos_Orb', K('접두 원소 피해 찾기', 'Find an elemental attack prefix'), None, K('카오스', 'Chaos'),
     [{'if': {'has': 'ele'}, 'to': 'd1', 'res': 'ok'}, {'to': 'e2', 'res': 'fail'}], None, show=['fire', 'cold', 'light'], trim={'side': 'p', 'keep': 'keepP'}),
 act('d1', 'main', [0, 11], 'desecrate', 'Ancient_Collarbone', K('접두 원소 피해(훼손)', 'Elemental attack prefix (desecrated)'), [st('p', '훼손 옵션(미공개) — 접두가 꽉 차 있으면 하나가 지워짐', 'Desecrated modifier (unrevealed) — a full prefix side loses one line')], K('훼손', 'Desecrate'), [{'to': 'd2'}], I7 + [UN('p')], omens=['Omen_of_Sinistral_Necromancy']),
 act('d2', 'main', [0, 12], 'reveal', None, K('접두 원소 피해(훼손) 공개', 'Reveal the elemental attack prefix'), None, K('공개', 'Reveal'),
     [{'if': {'count': {'tag': 'ele', 'min': 2}}, 'to': 'ok', 'res': 'ok'}, {'if': V1, 'to': 'd2x', 'res': 'fail'}, {'to': 'ok', 'res': 'ok'}], I9, want='ele', show=['fire', 'cold', 'light'], omens=['Omen_of_Abyssal_Echoes']),
 {'id': 'd2x', 'kind': 'act', 'group': 'main', 'pos': [1, 12], 'act': 'annul', 'cur': 'Orb_of_Annulment', 'omens': ['Omen_of_Light'],
  'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'target': K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  'edges': [{'if': {'has': 'ele'}, 'to': 'd1', 'res': 'ok', 'label': K('훼손 옵션만 지워짐 — 다시 훼손', 'Only the desecrated line removed: desecrate again')}, {'to': 'e1', 'res': 'fail', 'label': K('남은 원소 피해가 지워짐', 'The kept elemental line removed')}]},
 {'id': 'xw2', 'kind': 'exit', 'group': 'main', 'pos': [1, 7], 'simTo': 'h1', 'variant': 'fail', 'label': K('저항이 지워짐 — 새 베이스', 'Resistance removed — new base'),
  'note': K('새 베이스로 처음부터', 'Start over on a new base')},
 done([0, 13])]
g22('breach-ring-phys-v2', c, 'Breach Ring', 82,
  '균열 반지 물리 플랫 분열 + 원소 플랫(사이트 운영자 제작 방식, 영상 없음) — 카오스 오브(모든 원소 저항) → 좌측 결정화 + 균열의 에센스 → 조프의 기폭제 60% → 촉진 + 우측 찬미 + 완벽한 엑잘(화염 저항) → 강탈자 기폭제 60% → 절사 + 카오스 오브(최대 퀄리티 지우기, 접미로 가면 접미 잡옵 절사·말소 카오스로 자리 비움) → 좌측 찬미 + 완벽한 엑잘 → 좌측 결정화 + 재빠른 합금 → 접두 원소 피해 두 개(엑잘·절사 카오스·훼손 공개). 2026-11-13 G6 새 기준: 반복 세 곳 접음.',
  {'eT': {'kr': '공격 시 원소 피해', 'en': 'Elemental attack damage', 'values': TV({'3': ('1~3티어', 'T1–3'), '4': ('1~4티어', 'T1–4')})},
   'fT': {'kr': '화염 저항', 'en': 'Fire res', 'values': TV({'2': ('1~2티어', 'T1–2'), '3': ('1~3티어', 'T1–3')})},
   'v': {'kr': '진행', 'en': 'Route', 'values': TV({'1': ('원소 피해 2개까지', 'Until two elemental lines'), '2': ('결과 그대로', 'As it comes')})}}, P,
  {'bal': K('공격 시 원소 피해 2개(1~3티어), 화염 저항 1~2티어', 'Two elemental attack lines (T1–3), fire res T1–2'), 'ess': K('접두 훼손 한 번, 공개 결과 그대로, 화염 저항 빗나가도 그대로', 'One prefix desecration kept as revealed, fire res kept on a miss')},
  tags, nodes, [],
  FIN(VBE, lambda v: []),
  {'quality': 60, 'sockets': 0}, {'all': [{'has': 'phys'}, {'has': 'allres'}, {'has': 'alloy'}, {'any': [{'count': {'tag': 'ele', 'min': 2}}, {'param': {'v': 2}}]}, {'any': [{'has': 'fres'}, {'param': {'v': 2}}]}]}, VBE)
g = json.load(open(f'{H}/breach-ring-phys-v2.json'))
H = _H0
for v in g['versions']: v['tier'] = v['id']
g['loops'] = [
 {'id': 'L1', 'nodes': ['b5', 'b6', 'b6x'], 'kr': '접미 두 번째 옵션', 'en': 'Second suffix', 'fold': True,
  'goal': K('접미 화염 저항 1~2티어', 'T1–2 fire resistance suffix'),
  'goalBy': {'bal': K('접미 화염 저항 1~2티어', 'T1–2 fire resistance suffix'), 'ess': K('접미 두 번째 옵션 — 촉진 엑잘 결과 그대로', 'Second suffix: keep the catalysed exalt')},
  'steps': [K('조프의 기폭제 60개로 화염 퀄리티 60%', '60 Xoph’s Catalysts for 60% fire quality') | {'node': 'b5'},
            K('촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브', 'Omen of Catalysing Exaltation + Omen of Dextral Exaltation + Perfect Exalted Orb') | {'node': 'b6'},
            K('빗나가면 우측 소멸의 징조 + 소멸의 오브', 'A miss: Omen of Dextral Annulment + Orb of Annulment') | {'node': 'b6x'}],
  'worst': {'kr': '모든 원소 저항이 지워지면 새 베이스', 'en': 'All resistances gone: a new base', 'to': 'xw1'},
  'item': I4},
 {'id': 'L2', 'nodes': ['b8', 'b8s'], 'kr': '최대 퀄리티 지우기', 'en': 'Remove maximum quality', 'fold': True,
  'goal': K('최대 퀄리티를 다른 옵션으로, 접미 자리 하나 비우기', 'Maximum quality into another option, one suffix slot free'),
  'steps': [K('절사의 징조 + 카오스 오브로 최대 퀄리티(레벨이 가장 낮음)를 바꿈', 'Omen of Whittling + Chaos Orb turns maximum quality (lowest level) into another option') | {'node': 'b8'},
            K('새 옵션이 접미로 가면 절사·우측 말소의 징조 + 상위 카오스 오브로 접미 잡옵을 접두로', 'A new suffix: Whittling or Dextral Erasure + Greater Chaos Orb until the junk moves to the prefixes') | {'node': 'b8s'}],
  'worst': {'kr': '모든 원소 저항·화염 저항이 지워지면 새 베이스', 'en': 'Resistances gone: a new base', 'to': 'xw2'},
  'item': I5},
 {'id': 'L3', 'nodes': ['e1', 'e2', 'd1', 'd2', 'd2x'], 'kr': '접두 원소 피해 두 개', 'en': 'Two elemental attack prefixes', 'fold': True,
  'goal': K('접두 공격 시 원소 피해 1~3티어 두 개', 'Two T1–3 elemental attack prefixes'),
  'goalBy': {'bal': K('접두 공격 시 원소 피해 1~3티어 두 개', 'Two T1–3 elemental attack prefixes'), 'ess': K('빈 접두에 훼손 한 번 — 공개 결과 그대로', 'One desecration on the free prefix: keep the reveal')},
  'steps': [K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 빈 접두', 'Omen of Sinistral Exaltation + Perfect Exalted Orb on the free prefix') | {'node': 'e1'},
            K('원소 피해가 아니면 절사·좌측 말소의 징조 + 완벽한 카오스 오브', 'No elemental line: Whittling or Sinistral Erasure + Perfect Chaos Orb') | {'node': 'e2'},
            K('좌측 강령술의 징조 + 고대 빗장뼈 — 원소 피해와 잡옵 중 하나가 지워짐', 'Omen of Sinistral Necromancy + Ancient Collarbone: the elemental line or the junk goes') | {'node': 'd1'},
            K('심연의 메아리의 징조로 공개', 'Reveal with the Omen of Abyssal Echoes') | {'node': 'd2'},
            K('원소 피해 두 개가 아니면 빛의 징조 + 소멸의 오브', 'Not two elemental lines: Omen of Light + Orb of Annulment') | {'node': 'd2x'}],
  'item': I9},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'phys', 'fr': True}, {'tag': 'ele3'}, {'tag': 'ele3'}, {'tag': 'allres', 'tmax': 1}, {'tag': 'fres2'}, {'tag': 'alloy', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'phys', 'fr': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'allres', 'tmax': 1}, {'side': 's', 'random': True}, {'tag': 'alloy', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(g['nodes']), 'nodes')
