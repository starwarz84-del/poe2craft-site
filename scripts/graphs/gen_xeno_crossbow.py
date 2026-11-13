# W17 2026-11-13: XenoARPG 멀티 미러 물리 석궁(1TP4aGqxU7Q, 11:09, 자막 없음) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W17-crossbow/timeline.md, frames/ (영상 0:00~11:09 화면 대조)
# 실행: cd scripts/graphs && python3 gen_xeno_crossbow.py  → xeno-phys-crossbow-v2.json (gen_batch21.py의 이 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/xeno-phys-crossbow-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CRITn = L('s', '치명타 확률 +(4.41—5)%', '+(4.41—5)% to Critical Hit Chance', 'n', ['crit'])
CRIT = L('s', '치명타 확률 +(4.41—5)% (분열)', '+(4.41—5)% to Critical Hit Chance (fractured)', 'f', ['crit'])
PP = L('p', '물리 피해 (170—179)% 증가', '(170—179)% increased Physical Damage', 'n', ['pp'])
HYB = L('p', '물리 피해 (75—79)% 증가 + 정확도 +(175—200)', '(75—79)% increased Physical Damage + (175—200) to Accuracy Rating', 'n', ['hyb'])
EATK = L('p', '공격 스킬의 원소 피해 (120—139)% 증가 (훼손, 자리 막기)', '(120—139)% increased Elemental Damage with Attacks (desecrated, blocker)', 'd', ['eatk'])
EATKn = L('p', '공격 스킬의 원소 피해 (120—139)% 증가', '(120—139)% increased Elemental Damage with Attacks', 'j')   # 1:48 확장의 오브로 붙은 접두(잡옵)
FLAT = L('p', '물리 피해 (37—55)~(63—94) 추가 (훼손)', 'Adds (37—55) to (63—94) Physical Damage (desecrated)', 'd', ['flat'])
PROJ = L('s', '모든 투사체 스킬 레벨 +5', '+5 to Level of all Projectile Skills', 'n', ['proj'])
AS = L('s', '공격 속도 (17—19)% 증가', '(17—19)% increased Attack Speed', 'n', ['as'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'xeno-phys-crossbow-v2', 'recipe': 'xeno-phys-crossbow-v2', 'cls': 'Crossbows', 'base': 'Desolate Crossbow', 'ilvl': 82,
 'note': ('2026-11-13 W17 영상 전체 화면 대조(0:00~11:09, 자막 없음). 성공 회차 한 줄: 특출난 황량한 석궁(1:20) → 상위 진화의 오브 + 소멸의 오브·완벽한 확장의 오브로 접미 치명타 확률 1티어(1:23~1:40) → '
          '완벽한 확장의 오브 접두(공격 원소 피해, 1:48) → 완벽한 제왕(1:50, 냉기 피해 추가) → 보존된 턱뼈(1:59) → 신성한 오브로 치명타 5%(2:04~2:50) → 히네코라의 머리카락 미리 보기 + 분열의 오브(2:40~2:54, 치명타 분열) → '
          '소멸(2:58~3:01, 분열 + 공격 원소 피해) → 카오스 오브로 물리 피해 % 1티어(3:04~4:16) → 완벽한 엑잘(4:26, 정확도 +498) → 절사 카오스(4:36, 처치 시 생명력) → '
          '좌측 강령술 + 보존된 턱뼈 + 심연의 메아리 공개, 빛의 징조로 다시(4:50~5:32, 정확도 1티어 목표 → 공격 원소 피해 133%로 받음) → 절사 + 완벽한 카오스로 접두 복합 1티어(5:44~6:00) → '
          '완벽한 엑잘 접미 잡옵(6:20) → 절사 + 완벽한 카오스로 투사체 +7(6:28~7:13, 약 200개) → 완벽한 엑잘(7:38, 볼트 2개 추가 장전 82 = 절사로 못 지움). '
          '사용자 확정 11-09 순서: 영상은 여기서 빛의 징조 → 턱뼈(8:06 보존된, 8:50 고대) → 물리 피해 추가 41~70(9:08)을 먼저 하고 우측 말소 + 카오스(9:48)·절사 + 상위 카오스로 공격 속도(9:54~10:26)를 했지만, '
          '10:06에 물리 피해 추가(레벨 75)가 절사 대상이 되어 위험 → 공격 속도까지 끝낸 뒤 막기를 지우고 물리 피해 추가를 마지막에 공개. '
          '내부 결정: 4:36의 절사 카오스 한 번은 접두 복합 반복(절사 + 완벽한 카오스)과 같은 동작이라 그 반복으로 묶음, 자리 막기 공개는 사용자 결정 11-13대로 정확도·공격 원소 피해 1티어 중 먼저 뜬 것(영상 5:18 정확도 목표 → 5:26 공격 원소 피해로 바꿈, 성공 회차 = 공격 원소 피해 133%), 막기 판정은 접두 훼손 옵션(desSide), 숫돌(퀄리티 20%)은 값싼 마무리라 비용 밖, '
          '마지막 공격 속도 반복의 절사·우측 말소는 trim 자동 선택(볼트 2개처럼 투사체보다 높은 잡옵이면 영상 9:48처럼 우측 말소 1/2). '
          '신성한 오브(2:04~2:50, 10:26)·히네코라의 머리카락 미리 보기(2:40, 9:32)·숫돌·상위 철 룬 3개(9:40)는 뺌.'),
 'params': {'pT': {'kr': '목표 티어', 'en': 'Target tier', 'values': {'1': K('1티어', 'T1')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
               'desc': K('영상: 접두 3개·접미 2개 모두 1티어, 물리 피해 추가는 마지막 훼손 공개', 'Video: every prefix and suffix at T1, flat physical revealed last')}],
 'tags': {'crit': {'gi': 18, 'tmax': 1}, 'pp': {'gi': 8, 'tmax': 1}, 'hyb': {'gi': 9, 'tmax': 1}, 'flat': {'gi': 3, 'tmax': 1},
          'eatk': {'gi': 23, 'tmax': 1}, 'acc': {'gi': 17, 'tmax': 1}, 'proj': {'gi': 10, 'tmax': 1}, 'as': {'gi': 16, 'tmax': 1},
          'blk': {'anyOf': ['eatk', 'acc'], 'label': K('공격 스킬의 원소 피해·정확도 1티어', 'T1 elemental damage with attacks or accuracy')},
          'keepP': {'anyOf': ['pp', 'hyb'], 'label': K('물리 피해 % 1티어·복합 1티어', 'T1 % physical or T1 hybrid')},
          'keepS': {'anyOf': ['proj', 'as'], 'label': K('모든 투사체 스킬 레벨·공격 속도 1티어', 'T1 projectile skills or attack speed')}},
 'require': {'all': [{'has': 'pp'}, {'has': 'hyb'}, {'has': 'flat'}, {'has': 'crit'}, {'has': 'proj'}, {'has': 'as'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'pp'}, {'tag': 'hyb'}, {'tag': 'flat', 'des': True}, {'tag': 'crit', 'fr': True}, {'tag': 'proj'}, {'tag': 'as'}]}],
 'finalItem': {'quality': 20, 'sockets': 3},
}

W1E = [{'if': {'not': {'has': 'pp'}}, 'to': 'hc', 'res': 'fail', 'hide': True},
       {'if': {'all': [{'has': 'hyb'}, {'desSide': 'p'}]}, 'to': 's2', 'res': 'ok'},
       {'if': {'all': [{'not': {'desSide': 'p'}}, {'not': {'full': 'p'}}]}, 'to': 'b1', 'res': 'fail', 'hide': True},
       {'if': {'not': {'desSide': 'p'}}, 'to': 'wc', 'res': 'fail', 'label': K('막기가 지워지고 접두가 꽉 참', 'Blocker gone, prefixes full')},
       {'if': {'full': 'p'}, 'to': 'w1p', 'res': 'fail', 'label': K('접두가 잡옵으로 꽉 참', 'Prefixes full with junk')},
       {'to': 'w1', 'res': 'fail', 'hide': True}]
N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='t1', start={'rar': 'normal', 'mods': [], 'quality': 0},
  label=K('특출난 황량한 석궁 구입 (아이템 레벨 82)', 'Buy an exceptional Desolate Crossbow (item level 82)'), item=[])
A(id='t1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Greater_Orb_of_Transmutation', label=K('매직', 'Magic'),
  goal=K('접미 치명타 확률 1티어', 'T1 crit chance suffix'), show=['crit'], ask=K('원하는 옵션?', 'Wanted option?'),
  edges=[{'if': {'has': 'crit'}, 'to': 't2', 'res': 'ok', 'label': K('성공', 'Hit')},
         {'to': 't2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[CRITn])
A(id='t2x', kind='cleanup', group='prep', pos=[1, 1.5], keep=['crit'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), edges=[{'to': 't2'}])
A(id='t2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('매직 두 번째 옵션', 'Second magic option'),
  goal=K('치명타 확률이 없으면 치명타 확률, 있으면 접두 옵션', 'Crit chance first, then any prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}],
  ask=K('치명타 확률 + 접두?', 'Crit chance + a prefix?'),
  edges=[{'if': {'all': [{'has': 'crit'}, {'full': 'p'}]}, 'to': 'r1', 'res': 'ok', 'label': K('치명타 확률 + 접두', 'Crit chance + prefix')},
         {'if': {'has': 'crit'}, 'to': 't2', 'res': 'ok', 'hide': True},
         {'to': 't2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[EATKn, CRITn])
A(id='r1', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('레어', 'Rare'),
  goal=K('분열하기 위해 레어로', 'Make it rare for the fracture'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'd0'}], item=[EATKn, J('p'), CRITn])
A(id='d0', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f0'}],
  item=[EATKn, J('p'), CRITn, UN('s')])
A(id='sd', kind='side', group='prep', pos=[1, 4.5], act='divine', cur='Divine_Orb', attach=['d0', 'f0'],
  label=K('수치 올리기', 'Divine the values'), goal=K('옵션 수치 다시 굴리기 (선택)', 'Reroll option values (optional)'),
  showText=[K('모든 옵션 수치 다시 굴림', 'Rerolls every value')])
A(id='f0', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('치명타 확률이 분열되면 성공', 'Success when crit chance fractures')], ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'crit'}, 'to': 'hc', 'res': 'ok', 'label': K('치명타 확률 분열', 'Crit chance fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[EATKn, J('p'), CRIT, UN('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 5.6], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('치명타 확률이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='hc', kind='cleanup', group='prep', pos=[0, 6.6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[EATKn, CRIT])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[EATKn, CRIT])
A(id='c1', kind='act', group='main', pos=[0, 9], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 물리 피해 % 1티어', 'T1 % physical damage prefix'), show=['pp'],
  edges=[{'if': {'has': 'pp'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[PP, CRIT])
A(id='e1', kind='act', group='main', pos=[0, 10], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('세 번째 옵션 — 절사로 바꿀 잡옵', 'Third option: a junk line for Whittling'), showText=[K('랜덤 옵션', 'Random option')],
  edges=[{'to': 'b1'}], item=[PP, J('p'), CRIT])
A(id='b1', kind='act', group='main', pos=[0, 11], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 훼손 — 자리 막기', 'Prefix desecration: the blocker'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'rv'}],
  item=[PP, J('p'), UN('p'), CRIT])
A(id='rv', kind='act', group='main', pos=[0, 12], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='blk', label=K('공개', 'Reveal'),
  goal=K('접두 공격 스킬의 원소 피해 1티어 — 자리 막기', 'T1 elemental damage with attacks prefix: the blocker'), show=['eatk'], showText=[K('공격 스킬의 원소 피해·정확도 1티어 중 먼저 뜬 것', 'Whichever of T1 elemental damage with attacks or accuracy lands first')],
  edges=[{'if': {'not': {'has': 'pp'}}, 'to': 'hc', 'res': 'fail', 'hide': True},
         {'if': {'added': 'blk'}, 'to': 'w1', 'res': 'ok'},
         {'to': 'rvx', 'res': 'fail'}],
  item=[PP, J('p'), EATK, CRIT])
A(id='rvx', kind='act', group='main', pos=[1, 12], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'),
  edges=[{'if': {'famBlock': 'blk'}, 'to': 'wc', 'res': 'fail', 'hide': True}, {'to': 'b1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='w1', kind='act', group='main', pos=[0, 13], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('접두 세 번째 옵션', 'Third prefix'), show=['hyb'], skipIf={'all': [{'has': 'hyb'}, {'desSide': 'p'}]}, skipTo='s2',
  skipNote=K('엑잘에서 복합 옵션이 붙었으면 건너뜀', 'Skipped if the exalt already gave the hybrid'),
  edges=W1E)
A(id='w1p', kind='act', group='main', pos=[1, 13.5], act='chaos', cur='Perfect_Chaos_Orb', trim={'side': 'p', 'keep': 'keepP', 'keepDes': True},
  label=K('절사/좌측 말소 + 카오스', 'Whittling / Sinistral Erasure + Chaos'), goal=K('접두 잡옵 바꾸기', 'Reroll the junk prefix'), show=['hyb'],
  edges=W1E)
A(id='wc', kind='cleanup', group='main', pos=[2, 13], keep=['pp', 'hyb'], maxJunk=0, label=ANN, goal=ANN,
  target=K('잡옵 지우기 — 다시 자리 막기 (영상에 없음 — 시뮬 되돌림)', 'Remove the junk, then block again (not in the video: simulation fallback)'),
  edges=[{'lost': 'pp', 'to': 'hc', 'res': 'fail', 'hide': True}, {'lost': 'hyb', 'to': 'wc', 'res': 'fail', 'hide': True},
         {'to': 'b1', 'res': 'ok', 'hide': True, 'label': K('막기가 지워짐 — 자리 막기부터', 'Blocker gone: block again')}])
A(id='s2', kind='act', group='main', pos=[0, 14], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째 옵션', 'Second suffix'), show=['proj'], skipIf={'has': 'proj'}, skipTo='s3',
  edges=[{'if': {'any': [{'has': 'proj'}, {'has': 'as'}]}, 'to': 's3', 'res': 'ok', 'label': K('성공', 'Hit')},
         {'to': 'w2', 'res': 'fail', 'label': K('빗나감', 'Miss')}])
A(id='w2', kind='act', group='main', pos=[1, 14.5], act='chaos', cur='Perfect_Chaos_Orb', trim={'side': 's', 'keep': 'keepS'},
  label=K('절사 + 카오스', 'Whittling + Chaos'), goal=K('접미 두 번째 옵션', 'Second suffix'), show=['proj'],
  edges=[{'if': {'any': [{'has': 'proj'}, {'has': 'as'}]}, 'to': 's3', 'res': 'ok', 'label': K('투사체 +5', 'Projectile +5')},
         {'to': 'w2', 'res': 'fail', 'hide': True}])
A(id='s3', kind='act', group='main', pos=[0, 15.5], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 세 번째 옵션', 'Third suffix'), show=['as'], skipIf={'full': 's'}, skipTo='w3',
  skipNote=K('접미가 꽉 차 있으면 건너뜀', 'Skipped when the suffixes are full'),
  edges=[{'if': {'all': [{'has': 'proj'}, {'has': 'as'}]}, 'to': 'f1', 'res': 'ok', 'label': K('성공', 'Hit')},
         {'to': 'w3', 'res': 'fail', 'label': K('빗나감', 'Miss')}])
A(id='w3', kind='act', group='main', pos=[1, 16], act='chaos', cur='Greater_Chaos_Orb', trim={'side': 's', 'keep': 'keepS'},
  label=K('절사/우측 말소 + 카오스', 'Whittling / Dextral Erasure + Chaos'), goal=K('접미 세 번째 옵션', 'Third suffix'), show=['as'],
  edges=[{'if': {'all': [{'has': 'proj'}, {'has': 'as'}]}, 'to': 'f1', 'res': 'ok', 'label': K('공격 속도 1티어', 'T1 attack speed')},
         {'if': {'not': {'has': 'proj'}}, 'to': 'w2', 'res': 'fail', 'label': K('투사체가 지워짐 — 두 번째 접미부터', 'Projectile gone: back to the second suffix')},
         {'to': 'w3', 'res': 'fail', 'hide': True}])
A(id='f1', kind='act', group='main', pos=[0, 17], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecration'), edges=[{'to': 'f2'}], item=[PP, HYB, CRIT, PROJ, AS])
A(id='f2', kind='act', group='main', pos=[0, 18], act='desecrate', cur='Ancient_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'f3'}],
  item=[PP, HYB, UN('p'), CRIT, PROJ, AS])
A(id='f3', kind='act', group='main', pos=[0, 19], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='flat', label=K('공개', 'Reveal'),
  goal=K('접두 물리 피해 추가 1티어', 'T1 flat physical damage prefix'), show=['flat'],
  edges=[{'if': {'added': 'flat'}, 'to': 'ok', 'res': 'ok'}, {'to': 'f3x', 'res': 'fail'}],
  item=[PP, HYB, FLAT, CRIT, PROJ, AS])
A(id='f3x', kind='act', group='main', pos=[1, 19], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'f2', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 20], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['t2', 't2x'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'},
 {'id': 'L2', 'nodes': ['b1', 'rv', 'rvx'], 'kr': '자리 막기', 'en': 'Blocker'},
 {'id': 'L4', 'nodes': ['w1', 'w1p', 'wc'], 'kr': '접두 세 번째 옵션', 'en': 'Third prefix', 'fold': True,
  'goal': K('접두 물리 피해 % + 정확도 1티어', 'T1 % physical + accuracy prefix'),
  'steps': [K('절사의 징조 + 완벽한 카오스 오브로 접두 복합 옵션', 'Omen of Whittling + Perfect Chaos Orb for the hybrid prefix') | {'node': 'w1'},
            K('접두가 잡옵으로 꽉 차면 절사의 징조(필요하면 좌측 말소의 징조도) + 완벽한 카오스 오브', 'Prefixes full with junk: Omen of Whittling (plus Sinistral Erasure when needed) + Perfect Chaos Orb') | {'node': 'w1p'},
            K('막기가 지워지고 접두가 꽉 차면 소멸의 오브로 잡옵을 지우고 자리 막기부터 (영상에 없음 — 시뮬 되돌림)', 'Blocker gone and prefixes full: annul the junk and block again (not in the video: simulation fallback)') | {'node': 'wc'}],
  'worst': K('물리 피해 %가 지워지면 분열 + 옵션 1개로 정리한 뒤 카오스부터', 'Physical % gone: clear down to the fracture + one option, then Chaos again') | {'to': 'hc'},
  'item': [PP, HYB, EATK, CRIT]},
 {'id': 'L5', 'nodes': ['s2', 'w2', 's3', 'w3'], 'kr': '접미 두 번째·세 번째 옵션', 'en': 'Second and third suffixes', 'fold': True,
  'goal': K('접미 투사체 +5 + 공격 속도 1티어', 'Projectile +5 and T1 attack speed suffixes'),
  'steps': [K('완벽한 엑잘티드 오브로 접미 투사체 (접두가 꽉 차 접미로)', 'Perfect Exalt for the projectile suffix (prefixes are full)') | {'node': 's2'},
            K('빗나가면 절사의 징조 + 완벽한 카오스 오브로 투사체까지', 'On a miss, Omen of Whittling + Perfect Chaos Orb until projectile') | {'node': 'w2'},
            K('완벽한 엑잘티드 오브로 접미 공격 속도', 'Perfect Exalt for the attack speed suffix') | {'node': 's3'},
            K('빗나가면 절사의 징조 + 상위 카오스 오브, 볼트 2개 추가 장전처럼 높은 잡옵이면 우측 말소의 징조(1/2) — 투사체가 지워지면 2번부터', 'On a miss, Omen of Whittling + Greater Chaos Orb; a high junk line like two extra bolts takes Dextral Erasure (1 in 2), and losing projectile goes back to 2') | {'node': 'w3'}],
  'item': [PP, HYB, EATK, CRIT, PROJ, AS]},
 {'id': 'L3', 'nodes': ['f2', 'f3', 'f3x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
