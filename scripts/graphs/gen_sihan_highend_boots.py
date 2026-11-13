# W19 2026-11-13: 시한 하이엔드 장화(dlrD21AcCUE, 17:50) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W19-sihan-boots/timeline.md, frames/ (영상 0:00~17:50 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_highend_boots.py  → sihan-highend-boots-v2.json (옛 JSON을 손으로 고치던 것을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-highend-boots-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(기적의 발걸음)에 실제로 나온 옵션
ARMn = L('p', '방어도 (92—100)% 증가', '(92—100)% increased Armour', 'n', ['armP'])
ARM = L('p', '방어도 (92—100)% 증가 (분열)', '(92—100)% increased Armour (fractured)', 'f', ['armP'])
ELE = L('s', '방어도의 +(38—43)%가 원소 피해에도 적용', '+(38—43)% of Armour also applies to Elemental Damage', 'n', ['armEle'])
STR = L('s', '힘 +(28—30)', '+(28—30) to Strength', 'n', ['str'])
CHR = L('s', '카오스 저항 +(20—23)% (공허 유동체)', '+(20—23)% to Chaos Resistance (Void Flux)', 'n', ['chaosR'])
MS = L('p', '이동 속도 35% 증가', '35% increased Movement Speed', 'n', ['ms'])
LIFE = L('p', '생명력 최대치 +(120—149) (훼손)', '+(120—149) to maximum Life (desecrated)', 'd', ['life'])
MARK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mark'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'sihan-highend-boots-v2', 'recipe': 'sihan-highend-boots-v2', 'cls': 'Boots_str', 'base': 'Tasalian Greaves', 'ilvl': 82, 'basePrice': {},
 'note': ('2026-11-13 W19 영상 전체 화면 대조. 성공 회차(기적의 발걸음) 한 줄: 노멀 타살리오의 각반 3개(아이템 레벨 82, 증강 가능한 홈 2개, 7:20~7:56) → '
          '완벽한 진화·완벽한 확장 + 소멸의 오브로 방어도 % 증가 매직(8:13~8:42) → 완벽한 제왕(8:50) → 훼손(9:03, 뼈 종류 화면 확인 못 함) → '
          '신성한 오브로 방어도 100%(9:39, 선택) → 분열 1/3(9:49, 순간은 편집으로 빠짐) → 소멸의 오브 2번으로 분열 + 옵션 1개(10:00) → '
          '카오스 오브로 방어도의 원소 피해 적용 1티어(10:20) → 우측 찬미 + 완벽한 엑잘로 접미, 원소 저항이면 공허 유동체로 카오스 저항, 빗나가면 소멸의 오브(10:27~11:48) → '
          '의뢰인 요청으로 힘(12:00~13:06: 상위 카오스·소멸·완벽한 엑잘 반복, 최종 힘 2티어·냉기 저항 → 공허 유동체 카오스 저항 2티어) → '
          '접두 완벽한 엑잘 빗나감(방어도+기절 한계치, 13:38) → 좌측 결정화 + 심연의 에센스로 징표(13:42) → 완벽한 엑잘 이동 속도 35% 1티어(13:50) → '
          '징표에 고대 갈비뼈 + 심연의 메아리 공개(15:30~16:10, 생명력 87 3티어 — 빗나감) → 빛의 징조 + 소멸의 오브(16:24) → 빈자리에 고대 갈비뼈 공개 생명력 133 1티어(16:30). '
          '내부 결정: 접미 둘째·셋째 자리는 힘·원소 저항 중 먼저 뜬 것(영상은 의뢰인 요청으로 힘을 상위 카오스로 나중에 넣음), 접두 엑잘·훼손은 이동 속도·생명력 중 먼저 뜬 것과 남은 것.'),
 'params': {
  'strT': {'kr': '힘 목표', 'en': 'Strength target', 'values': {'2': K('1~2티어', 'T1–2'), '3': K('1~3티어', 'T1–3')}},
  'resT': {'kr': '카오스 저항 목표', 'en': 'Chaos Resistance target', 'values': {'2': K('1~2티어', 'T1–2'), '3': K('1~3티어', 'T1–3')}},
  'desT': {'kr': '훼손 접두 목표', 'en': 'Desecrated prefix target', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
 },
 'strategies': [{'id': 'high', 'params': {'strT': 2, 'resT': 2, 'desT': 1}}, {'id': 'bal', 'params': {'strT': 3, 'resT': 3, 'desT': 2}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'strT': 3, 'resT': 3, 'desT': 2}, 'tier': 'bal',
   'desc': K('마지막 접두(훼손) 1~2티어, 힘·카오스 저항 1~3티어', 'Last prefix (desecrated) T1–2, Strength and Chaos Resistance T1–3')},
  {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'strT': 2, 'resT': 2, 'desT': 1}, 'tier': 'high',
   'desc': K('영상: 마지막 접두(훼손) 1티어, 힘·카오스 저항 1~2티어', 'Video: last prefix (desecrated) T1, Strength and Chaos Resistance T1–2')}],
 'tags': {
  'armP': {'gi': 8, 'tmax': 1}, 'armEle': {'gi': 18, 'tmax': 1},
  'str': {'gi': 0, 'tmax': '$strT'}, 'strH': {'gi': 0, 'tmax': 2}, 'strB': {'gi': 0, 'tmax': 3},
  'fire': {'gi': 1}, 'cold': {'gi': 2}, 'light': {'gi': 3}, 'chaosR': {'gi': 4, 'tmax': '$resT'}, 'chaosRH': {'gi': 4, 'tmax': 2}, 'chaosRB': {'gi': 4, 'tmax': 3},
  'ELE': {'anyOf': ['fire', 'cold', 'light']},
  'ms': {'gi': 12}, 'life': {'gi': 5},
  'msD': {'gi': 12, 'tmax': '$desT'}, 'lifeD': {'gi': 5, 'tmax': '$desT'},
  'msD1': {'gi': 12, 'tmax': 1}, 'lifeD1': {'gi': 5, 'tmax': 1}, 'msD2': {'gi': 12, 'tmax': 2}, 'lifeD2': {'gi': 5, 'tmax': 2},
  'PRE': {'anyOf': ['ms', 'life'], 'label': K('이동 속도·생명력 최대치', 'Movement speed or maximum Life')},
  'PRED': {'anyOf': ['msD', 'lifeD']},
  'PREDh': {'anyOf': ['msD1', 'lifeD1'], 'label': K('이동 속도·생명력 최대치 1티어', 'T1 movement speed or maximum Life')},
  'PREDb': {'anyOf': ['msD2', 'lifeD2'], 'label': K('이동 속도·생명력 최대치 1~2티어', 'T1–2 movement speed or maximum Life')},
  'mark': {'gi': 47},
 },
 'conds': {'sufDone': {'all': [{'has': 'armEle'}, {'has': 'str'}, {'has': 'chaosR'}]}},
 'require': {'all': [{'has': 'armP'}, {'has': 'armEle'}, {'has': 'str'}, {'has': 'chaosR'}, {'count': {'tag': 'PRE', 'min': 2}}, {'has': 'PRED'}, {'full': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 2]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'b0',
 'finals': [
  {'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
   'lines': [{'tag': 'armP', 'fr': True}, {'tag': 'PRE'}, {'tag': 'PREDh', 'des': True}, {'tag': 'armEle'}, {'tag': 'strH'}, {'tag': 'chaosRH'}]},
  {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'armP', 'fr': True}, {'tag': 'PRE'}, {'tag': 'PREDb', 'des': True}, {'tag': 'armEle'}, {'tag': 'strB'}, {'tag': 'chaosRB'}]}],
 'finalItem': {'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 (영상 7:20~9:50) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='m1', start={'rar': 'normal', 'mods': []},
  label=K('특출난 타살리오의 각반 구입 (아이템 레벨 82)', 'Buy exceptional Tasalian Greaves (item level 82)'), item=[])
A(id='m1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('접두 방어도 % 증가 1티어', 'T1 % increased Armour prefix'), show=['armP'],
  edges=[{'if': {'has': 'armP'}, 'to': 'm2', 'res': 'ok'}, {'to': 'm1x', 'res': 'fail', 'label': K('다른 옵션', 'Another option')}], item=[ARMn])
A(id='m1x', kind='act', group='prep', pos=[1, 1], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), edges=[{'to': 'm1', 'label': K('다시 진화', 'Transmute again')}])
A(id='m2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('남은 자리 채우기', 'Fill the other slot'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'r1'}], item=[ARMn, J('s')])
A(id='r1', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'f1'}], item=[ARMn, J('s'), J('x')])
A(id='f1', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 확률 1/3', 'Fourth option (desecrated): fracture odds 1/3'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f2'}], item=[ARMn, J('s'), J('x'), UN('x')])
A(id='rd', kind='side', group='prep', pos=[1, 4.5], attach=['f1', 'f2'], cur='Divine_Orb', label=K('신성', 'Divine'),
  goal=K('방어도 % 증가 수치 올리기 (선택)', 'Raise the % Armour roll (optional)'))
A(id='f2', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('방어도 % 증가가 분열되면 성공', 'Success when % Armour fractures')],
  edges=[{'if': {'fractured': 'armP'}, 'to': 'f4', 'res': 'ok', 'label': K('방어도 % 분열', '% Armour fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[ARM, J('s'), J('x'), UN('x')])
A(id='xj', kind='exit', group='prep', pos=[1, 5.5], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('방어도 % 증가가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='f4', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[ARM, J('x')])

# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='s1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ARM, J('x')])
A(id='s1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 방어도의 원소 피해 적용 1티어', 'T1 armour applies to elemental damage suffix'), show=['armEle'],
  skipIf={'has': 'armEle'}, skipTo='s2', skipHide=True,
  edges=[{'if': {'has': 'armEle'}, 'to': 's2', 'res': 'ok'}, {'to': 's1', 'res': 'fail', 'hide': True}], item=[ARM, ELE])
# 접미 반복(영상 10:27~13:06): 우측 찬미 + 완벽한 엑잘, 원소 저항이면 공허 유동체로 카오스 저항, 빗나가면 소멸의 오브
A(id='s2', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 힘·원소 저항 — 남은 옵션 중 먼저 뜬 것', 'Strength or an elemental resistance suffix: whichever is still missing lands first'),
  show=['str', 'fire', 'cold', 'light'],
  edges=[{'if': {'all': [{'added': 'ELE'}, {'not': {'has': 'chaosR'}}]}, 'to': 'sf', 'res': 'ok', 'label': K('원소 저항', 'Elemental resistance')},
         {'if': {'ref': 'sufDone'}, 'to': 'p1', 'res': 'ok'},
         {'if': {'any': [{'added': 'str'}, {'added': 'chaosR'}]}, 'to': 's2', 'res': 'ok', 'hide': True},
         {'to': 's2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[ARM, ELE, STR])
A(id='sf', kind='act', group='main', pos=[1, 9.4], act='flux', cur='Void_Flux', label=K('유동체', 'Flux'),
  goal=K('원소 저항을 카오스 저항으로', 'The elemental resistance becomes Chaos Resistance'), show=['chaosR'],
  skipIf={'not': {'has': 'ELE'}}, skipTo='s2', skipHide=True,
  edges=[{'if': {'ref': 'sufDone'}, 'to': 'p1', 'res': 'ok'}, {'to': 's2', 'label': K('다시 엑잘', 'Exalt again')}], item=[ARM, ELE, STR, CHR])
A(id='s2x', kind='cleanup', group='main', pos=[1, 10.4], keep=['armEle', 'str', 'chaosR'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 접미 지우기', 'Remove the missed suffix'),
  edges=[{'lost': 'armEle', 'to': 's0', 'res': 'fail', 'label': K('방어도의 원소 피해 적용이 지워짐', 'Armour to elemental gone')},
         {'lost': 'str', 'to': 's2', 'res': 'ok', 'hide': True}, {'lost': 'chaosR', 'to': 'sf', 'res': 'ok', 'hide': True},
         {'to': 's2', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='s0', kind='cleanup', group='main', pos=[2, 10.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 's1'}])
# 접두 엑잘(영상 13:10~13:50): 빗나가면 좌측 결정화 + 심연의 에센스로 징표, 징표를 둔 채 다시 엑잘(14:00~14:45 설명: 또 빗나가면 징표 훼손 → 빛의 징조 + 소멸 → 다시 징표)
A(id='p1', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 이동 속도·생명력 최대치 중 먼저 뜬 것', 'Second prefix: movement speed or maximum Life, whichever lands first'), show=['ms', 'life'],
  edges=[{'if': {'added': 'PRE'}, 'to': 'p2', 'res': 'ok', 'hide': True}, {'to': 'q1', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[ARM, MS, ELE, STR, CHR])
A(id='q1', kind='act', group='main', pos=[1, 11.4], act='essence', cur='Essence_of_the_Abyss', ess='mark', mark=True,
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('빗나간 접두를 지우고 심연의 군주의 징표', 'The missed prefix goes for the Mark of the Abyssal Lord'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'q4'}], item=[ARM, MARK, ELE, STR, CHR])
A(id='q4', kind='act', group='main', pos=[1, 12.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('징표를 둔 채 접두 이동 속도·생명력 최대치', 'Movement speed or maximum Life prefix, the Mark kept'), show=['ms', 'life'],
  edges=[{'if': {'added': 'PRE'}, 'to': 'p8m', 'res': 'ok'}, {'to': 'q4b', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[ARM, MS, MARK, ELE, STR, CHR])
A(id='q4b', kind='act', group='main', pos=[2, 12.4], act='desecrate', cur='Preserved_Rib', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표 훼손 — 지울 준비', 'Desecrate the Mark to remove it'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'q4l'}])
A(id='q4l', kind='act', group='main', pos=[2, 13.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우기 — 빗나간 접두를 다시 징표로', 'Remove the desecration: the missed prefix becomes the Mark again'), edges=[{'to': 'q1'}])
# 마지막 접두 훼손(영상 14:30~16:40): 징표에 고대 갈비뼈(한 티어 높게) → 심연의 메아리 공개 → 빗나가면 빛의 징조 + 소멸 → 빈자리에 고대 갈비뼈
A(id='p8m', kind='act', group='main', pos=[0, 13.4], act='desecrate', cur='Ancient_Rib', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표에 고대 갈비뼈 — 한 티어 높게', 'Ancient Rib on the Mark: one tier higher'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'p3'}], item=[ARM, MS, UN('p'), ELE, STR, CHR])
A(id='p2', kind='act', group='main', pos=[1, 14.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('빈 접두에 고대 갈비뼈', 'Ancient Rib on the empty prefix'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'p3'}])
A(id='p3', kind='act', group='main', pos=[0, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='PRED', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 남은 이동 속도·생명력 최대치', 'Third prefix (desecrated): the remaining movement speed or maximum Life'), show=['life', 'ms'],
  edges=[{'if': {'added': 'PRED'}, 'to': 'ok', 'res': 'ok'}, {'to': 'p3x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[ARM, MS, LIFE, ELE, STR, CHR])
A(id='p3x', kind='act', group='main', pos=[1, 15.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('빗나간 훼손 옵션 지우기', 'Remove the missed desecration'), edges=[{'to': 'p2'}])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L2', 'nodes': ['s2', 'sf', 's2x', 's0'], 'kr': '접미 두 자리', 'en': 'Two more suffixes', 'fold': True,
  'goal': K('접미 힘 + 카오스 저항 1~2티어 — 먼저 뜬 것부터', 'T1–2 Strength + Chaos Resistance suffixes: whichever lands first'),
  'goalBy': {'high': K('접미 힘 + 카오스 저항 1~2티어 — 먼저 뜬 것부터', 'T1–2 Strength + Chaos Resistance suffixes: whichever lands first'),
             'bal': K('접미 힘 + 카오스 저항 1~3티어 — 먼저 뜬 것부터', 'T1–3 Strength + Chaos Resistance suffixes: whichever lands first')},
  'steps': [K('우측 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 하나', 'Omen of Dextral Exaltation + Perfect Exalted Orb for one suffix') | {'node': 's2'},
            K('화염·냉기·번개 저항이면 공허 유동체로 카오스 저항', 'Fire, cold or lightning resistance: Void Flux turns it into Chaos Resistance') | {'node': 'sf'},
            K('빗나가면 소멸의 오브', 'A miss: Orb of Annulment') | {'node': 's2x'},
            K('방어도의 원소 피해 적용이 지워지면 분열 + 옵션 1개까지 소멸의 오브', 'Armour to elemental gone: annul down to the fracture + one option') | {'node': 's0'}],
  'worst': {'kr': '방어도의 원소 피해 적용이 지워지면 카오스 단계부터', 'en': 'Armour to elemental gone: back to the Chaos step', 'to': 's1'},
  'item': [ARM, ELE, STR, CHR]},
 {'id': 'L4', 'nodes': ['p1', 'q1', 'q4', 'q4b', 'q4l'], 'kr': '접두 두 번째 옵션', 'en': 'Second prefix', 'fold': True,
  'goal': K('접두 이동 속도·생명력 최대치 — 먼저 뜬 것', 'Movement speed or maximum Life prefix: whichever lands first'),
  'steps': [K('완벽한 엑잘티드 오브로 접두 하나', 'Perfect Exalted Orb for one prefix') | {'node': 'p1'},
            K('빗나가면 좌측 결정화의 징조 + 심연의 에센스로 징표', 'A miss: Omen of Sinistral Crystallisation + Essence of the Abyss for the Mark') | {'node': 'q1'},
            K('징표를 둔 채 완벽한 엑잘티드 오브', 'Perfect Exalted Orb with the Mark kept') | {'node': 'q4'},
            K('또 빗나가면 보존된 갈비뼈로 징표 훼손', 'Another miss: Preserved Rib on the Mark') | {'node': 'q4b'},
            K('빛의 징조 + 소멸의 오브로 훼손 옵션을 지우고 다시 징표', 'Omen of Light + Orb of Annulment removes it, then the Mark again') | {'node': 'q4l'}],
  'item': [ARM, MS, MARK, ELE, STR, CHR]},
 {'id': 'L5', 'nodes': ['p8m', 'p2', 'p3', 'p3x'], 'kr': '접두 세 번째 옵션(훼손)', 'en': 'Third prefix (desecrated)', 'fold': True,
  'goal': K('접두 생명력 최대치 1티어(훼손) — 남은 이동 속도·생명력 최대치', 'T1 maximum Life prefix (desecrated): the remaining movement speed or maximum Life'),
  'goalBy': {'high': K('접두 생명력 최대치 1티어(훼손) — 남은 이동 속도·생명력 최대치', 'T1 maximum Life prefix (desecrated): the remaining movement speed or maximum Life'),
             'bal': K('접두 생명력 최대치 1~2티어(훼손) — 남은 이동 속도·생명력 최대치', 'T1–2 maximum Life prefix (desecrated): the remaining movement speed or maximum Life')},
  'steps': [K('징표에 고대 갈비뼈 — 한 티어 높게', 'Ancient Rib on the Mark: one tier higher') | {'node': 'p8m'},
            K('심연의 메아리의 징조로 공개', 'Reveal with the Omen of Abyssal Echoes') | {'node': 'p3'},
            K('빗나가면 빛의 징조 + 소멸의 오브', 'A miss: Omen of Light + Orb of Annulment') | {'node': 'p3x'},
            K('빈 접두에 고대 갈비뼈 다시', 'Ancient Rib again on the empty prefix') | {'node': 'p2'}],
  'item': [ARM, MS, LIFE, ELE, STR, CHR]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
