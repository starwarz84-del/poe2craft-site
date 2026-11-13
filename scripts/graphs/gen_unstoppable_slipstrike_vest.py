# W34 2026-11-13: Unstoppable BTW 회피 갑옷(swF5mwXmZ0k 40:00~46:30) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W34-unstoppable/timeline.md, frames/ (영상 화면 대조), H2 11-13 review/H2/unstoppable-slipstrike-vest-v2/ (40:00~45:02 화면)
# 실행: cd scripts/graphs && python3 gen_unstoppable_slipstrike_vest.py  → unstoppable-slipstrike-vest-v2.json (gen_batch27.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/unstoppable-slipstrike-vest-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

EVn = L('p', '회피 (101—110)% 증가', '(101—110)% increased Evasion Rating', 'n', ['evP'])
EV = L('p', '회피 (101—110)% 증가 (분열)', '(101—110)% increased Evasion Rating (fractured)', 'f', ['evP'])
FL = L('p', '회피 +(262—300)', '+(262—300) to Evasion Rating', 'n', ['evF'])
HB = L('p', '회피 +(71—90), 회피 (39—42)% 증가 (훼손)', '+(71—90) to Evasion Rating, (39—42)% increased Evasion Rating (desecrated)', 'd', ['hyb'])
LB = L('p', '생명력 최대치 +(150—174) (훼손)', '+(150—174) to maximum Life (desecrated)', 'd')
FR = L('s', '화염 저항 +(41—45)%', '+(41—45)% to Fire Resistance', 'n', ['fr'])
CR = L('s', '냉기 저항 +(41—45)%', '+(41—45)% to Cold Resistance', 'n', ['cr'])
DF = L('s', '회피의 (21—23)%와 동일한 튕겨내기 평점 획득', 'Gain Deflection Rating equal to (21—23)% of Evasion Rating', 'n', ['dfl2'])
DF1 = L('s', '회피의 (24—26)%와 동일한 튕겨내기 평점 획득', 'Gain Deflection Rating equal to (24—26)% of Evasion Rating', 'n', ['dfl1'])   # H1 11-13: 하이엔드 튕겨내기 1티어(C17-1)
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'unstoppable-slipstrike-vest-v2', 'recipe': 'unstoppable-slipstrike-vest-v2', 'cls': 'Body_Armours_dex', 'base': 'Slipstrike Vest', 'ilvl': 83,
 'note': ('2026-11-13 W34 영상 화면 대조(근거 scratchpad review/W34-unstoppable/timeline.md). 성공 회차(Behemoth Ward) 한 줄: '
          '미끄러진 타격 조끼(아이템 레벨 83, 룬 소켓 3개) → 매직 회피 증가 1티어(40:00 자막) → 제왕·훼손으로 옵션 4개(41:08: 회피 110%·생명력·능력치 요구사항·미공개 훼손) → '
          '분열의 오브로 회피 110% 분열(41:20) → 소멸로 분열 + 옵션 1개 → 카오스로 화염 저항 1티어 → 상위 찬미 + 우측 찬미 + 완벽한 엑잘로 접미 2개(41:35 튕겨내기 2티어 + 점화 지속시간, 엑잘 장면은 확인 못 함) → '
          '절사의 징조 + 카오스로 점화 지속시간 → 냉기 저항 1티어(41:45 절사 미리보기, 42:02 결과) → 완벽한 엑잘로 접두(42:25 회피 +230 2티어 빗나감) → '
          '좌측 결정화 + 심연의 에센스 → 징표 훼손 → 공개로 자리 막기 → 다시 엑잘 반복(42:30~45:00 자막) → 생명력 자리 막기 상태에서 회피 +275 1티어(45:02) → '
          '빛의 징조 + 소멸로 막기 제거(45:32) → 고대 갈비뼈(45:55) → 공개로 회피 복합 1티어(46:05 완성). '
          '신성한 오브·바알 오브·퀄리티 30%·네 번째 소켓 도박(46:30~48:40)은 정책 14장대로 뺌. '
          'H1 11-13: 하이엔드 튕겨내기는 1티어(C17-1 — 절사 카오스 반복으로 찾는 옵션). 영상 완성품은 튕겨내기 2티어(21%)라 하이엔드는 절사 카오스를 한 번 더(튕겨내기 2티어가 접미에서 레벨 66으로 가장 낮음). '
          '8번 엑잘은 두 등급 모두 튕겨내기 1~2티어면 다음으로(sGE). 9번의 k3e·k3d(절사 카오스 새 옵션이 접두로 갔을 때)는 영상에 없음 — 접두가 비어 있는 동안 절사 카오스가 접두에 옵션을 붙이면 '
          '접미 빈자리가 생겨 끝나지 않으므로 넣은 무한 반복 방지 단계. 아이템 레벨 83(41:08)으로 레시피 파일도 맞춤. '
          'H2 11-13 화면 대조(근거 scratchpad review/H2/unstoppable-slipstrike-vest-v2/): 40:00~40:55는 앞 아이템(회피·에너지 보호막 갑옷), 40:58 매직(회피 증가 없음) → 41:00 매직 회피 101% 1티어 → 41:01 확장으로 능력치 요구사항 → 41:12 레어(생명력 +200, 접두 미공개 훼손) → 41:15 분열 + 능력치 요구사항만 남김 → 41:15~41:23 카오스 반복, 41:23 화염 저항 → 41:26 상위 찬미 툴팁, 41:29 채팅 우측 찬미·상위 찬미 소모 + 튕겨내기 21%·점화 → 42:32 좌측 결정화, 42:39 심연의 메아리, 42:46 보존된 갈비뼈 → 43:20 공개 +211 회피(낮은 티어) → 43:36 빛의 징조로 제거 → 43:40 엑잘 정신력(빗나감) → 43:48 공개 가시·회피 선택지 → 44:04 생명력 막기 + 엑잘 회피 복합 2티어(하이엔드 빗나감) → 44:30 채팅 메아리·빛·좌측 결정화 소모 → 44:40 가시 막기 → 45:02 생명력 +165 막기. 단계 흐름은 그대로 맞음, 엑잘·카오스 오브 등급은 화면에 안 나옴.'),
 'params': {
   'pT': {'kr': '접두 회피', 'en': 'Evasion prefixes', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'rT': {'kr': '마지막 접미', 'en': 'Last suffix', 'values': {'1': K('냉기 저항 1티어', 'T1 cold resistance'), '2': K('랜덤 옵션', 'Random option')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1, 'rT': 1}}, {'id': 'bal', 'params': {'pT': 2, 'rT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'pT': 2, 'rT': 2}, 'tier': 'bal',
    'desc': K('저항 1티어 1개, 접두 회피와 두 번째 접미는 1~2티어, 마지막 접미는 랜덤 옵션', 'One T1 resistance, T1–2 evasion prefixes and second suffix, a random last suffix')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1, 'rT': 1}, 'tier': 'high',
    'desc': K('영상: 접두 회피 1티어 3개, 저항 1티어 2개 + 튕겨내기', 'Video: three T1 evasion prefixes, two T1 resistances + deflection')}],
 'tags': {
   'evP': {'gi': 7, 'tmax': 1},
   'evF': {'gi': 6, 'tmax': '$pT'}, 'hyb': {'gi': 9, 'tmax': '$pT'},
   'evF1': {'gi': 6, 'tmax': 1}, 'hyb1': {'gi': 9, 'tmax': 1}, 'evF2': {'gi': 6, 'tmax': 2}, 'hyb2': {'gi': 9, 'tmax': 2},
   'gp': {'anyOf': ['evF', 'hyb'], 'label': K('회피·회피 복합', 'Flat or hybrid evasion')},
   'fr': {'gi': 1, 'tmax': 1}, 'cr': {'gi': 2, 'tmax': 1}, 'lr': {'gi': 3, 'tmax': 1},
   'fr2': {'gi': 1, 'tmax': 2}, 'cr2': {'gi': 2, 'tmax': 2}, 'lr2': {'gi': 3, 'tmax': 2},
   'frT': {'gi': 1, 'tmax': '$rT'}, 'crT': {'gi': 2, 'tmax': '$rT'}, 'lrT': {'gi': 3, 'tmax': '$rT'},
   'dfl': {'gi': 18, 'tmax': '$pT'}, 'dfl2': {'gi': 18, 'tmax': 2}, 'dfl1': {'gi': 18, 'tmax': 1},
   'res1': {'anyOf': ['fr', 'cr', 'lr'], 'label': K('화염·냉기·번개 저항 1티어', 'T1 fire, cold or lightning resistance')},
   'res2': {'anyOf': ['fr2', 'cr2', 'lr2'], 'label': K('화염·냉기·번개 저항 1~2티어', 'T1–2 fire, cold or lightning resistance')},
   'resT': {'anyOf': ['frT', 'crT', 'lrT']},
   'sG': {'anyOf': ['frT', 'crT', 'lrT', 'dfl']},
   'sGE': {'anyOf': ['frT', 'crT', 'lrT', 'dfl2']},   # H1 11-13: 접미 세 번째 옵션 반복에 들어가는 조건은 두 등급 모두 튕겨내기 1~2티어(영상 41:35 튕겨내기 2티어)
   'sG1': {'anyOf': ['fr', 'cr', 'lr', 'dfl1'], 'label': K('저항·튕겨내기 1티어', 'T1 resistance or deflection')},
   'sG2': {'anyOf': ['fr2', 'cr2', 'lr2', 'dfl2'], 'label': K('저항·튕겨내기 1~2티어', 'T1–2 resistance or deflection')},
   'blk': {'anyOf': [{'gi': 5}, {'gi': 12}], 'label': K('생명력 최대치·물리 가시 피해', 'Maximum life or physical thorns')},
   'mkP': {'gi': 45},
   'lifeB': {'gi': 5}},   # H2 11-13: 자리 막기 성공 회차 옵션(45:02 생명력 +165)
 'conds': {'sDone': {'any': [{'all': [{'param': {'rT': 2}}, {'has': 'res1'}, {'count': {'tag': 'sG', 'min': 2}}, {'full': 's'}]},
                             {'all': [{'has': 'res1'}, {'count': {'tag': 'resT', 'min': 2}}, {'count': {'tag': 'sG', 'min': 3}}]}]}},
 'require': {'all': [{'has': 'evP'}, {'count': {'tag': 'gp', 'min': 2}}, {'ref': 'sDone'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'ub',
 'finalItem': {'quality': 20, 'sockets': 3, 'exceptional': True},
}

N = []
A = lambda **kw: N.append(kw)

PL = {'ok': K('접두 완성', 'Prefixes done'), 'w9': K('접두 완성', 'Prefixes done'), 'r2': K('공개', 'Reveal'), 'q1': K('자리 막기 공개', 'Reveal for a blocker'),
      'q4': K('막기가 남음', 'Blocker still there'), 'q5': K('징표 훼손', 'Desecrate the Mark'), 'r1': K('빈 접두 자리 훼손', 'Desecrate the empty prefix'),
      'q2': K('엑잘', 'Exalt'), 'r0': K('막기 제거', 'Remove the blocker'), 'q3': K('징표 만들기', 'Make the Mark'), 'q0': K('빈 접두 자리 훼손', 'Desecrate an empty prefix')}

# 매직 단계: 회피 증가가 없으면 접두가 차 있을 때 소멸의 오브, 비어 있으면 확장 (영상 26:00·40:00 자막)
def MG(vis):
    out = []
    for e in [{'if': {'all': [{'has': 'evP'}, {'full': 's'}]}, 'to': 'ur'}, {'if': {'has': 'evP'}, 'to': 'ua'},
              {'if': {'full': 'p'}, 'to': 'uax'}, {'to': 'ua'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# 접미 세 자리: 저항 2개 + 좋은 접미 하나 (영상 41:20~42:02)
def SR(vis):
    out = []
    seen = set()
    for e in PR({}):   # 접미가 끝나면 접두 상태에 맞는 단계로 (카오스가 접두에 남긴 옵션 포함)
        to = e['to']; c = {'all': [{'ref': 'sDone'}, e['if']]} if e.get('if') else {'ref': 'sDone'}
        v = vis.get(to); dup = to in seen; seen.add(to)
        d = {'label': K('접미 완성 — ' + e['label']['kr'], 'Suffixes done: ' + e['label']['en'])} if e.get('label') else {}
        out.append({'if': c, 'to': to, **d, **(({**v, 'hide': True} if dup else v) if v is not None else {'hide': True})})
    SL = {'k3e': K('접미 빈자리 — 엑잘', 'Empty suffix: exalt'), 'k3': K('좋은 접미 2개 + 잡옵', 'Two good suffixes + junk'),
          'k3d': K('접두에 옵션 있음', 'A prefix option is there'), 'k2x': K('좋은 접미 1개뿐 — 카오스부터', 'Only one good suffix: back to Chaos')}
    for e in [{'if': {'not': {'full': 's'}}, 'to': 'k3e'},
              {'if': {'all': [{'has': 'res1'}, {'count': {'tag': 'sGE', 'min': 2}}, {'sideLt': {'side': 'p', 'n': 2}}]}, 'to': 'k3'},
              {'if': {'all': [{'has': 'res1'}, {'count': {'tag': 'sGE', 'min': 2}}]}, 'to': 'k3d'},
              {'to': 'k2x'}]:
        v = vis.get(e['to']); d = {'label': SL[e['to']]}
        out.append({**e, **d, **v} if v is not None else {**e, **d, 'hide': True})
    return out

# 접두 두 자리: 단계마다 아이템 상태를 다시 봄 (영상 42:10~46:05)
def PR(vis):
    out = []; seen = set()
    for e in [{'if': {'count': {'tag': 'gp', 'min': 2}}, 'to': 'ok'},
              {'if': {'all': [{'unrevSide': 'p'}, {'count': {'tag': 'gp', 'min': 1}}]}, 'to': 'r2'},
              {'if': {'unrevSide': 'p'}, 'to': 'q1'},
              {'if': {'all': [{'has': 'mkP'}, {'desSide': 'p'}]}, 'to': 'q4'},
              {'if': {'has': 'mkP'}, 'to': 'q5'},
              {'if': {'all': [{'count': {'tag': 'gp', 'min': 1}}, {'sideLt': {'side': 'p', 'n': 3}}, {'des': False}]}, 'to': 'r1'},
              {'if': {'all': [{'count': {'tag': 'gp', 'min': 1}}, {'sideLt': {'side': 'p', 'n': 3}}]}, 'to': 'q2'},
              {'if': {'all': [{'count': {'tag': 'gp', 'min': 1}}, {'desSide': 'p'}]}, 'to': 'r0'},
              {'if': {'count': {'tag': 'gp', 'min': 1}}, 'to': 'q3'},
              {'if': {'all': [{'sideLt': {'side': 'p', 'n': 3}}, {'desSide': 'p'}]}, 'to': 'q2'},
              {'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'q2'},
              {'to': 'q3'}]:
        v = vis.get(e['to']); dup = e['to'] in seen; seen.add(e['to']); d = {'label': PL[e['to']]} if e['to'] in PL else {}
        out.append({**e, **d, **v, **({'hide': True} if dup else {})} if v is not None else {**e, **d, 'hide': True})
    return out

# ---------------- 베이스템 완성 ----------------
A(id='ub', kind='base', group='prep', pos=[0, 0], next='ut', start={'rar': 'normal', 'mods': []},
  label=K('아이템 레벨 83, 룬 소켓 3개 특출난 미끄러진 타격 조끼 구입', 'Buy an item level 83 exceptional Slipstrike Vest with three rune sockets'), item=[])
A(id='ut', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=MG({'ua': {}}), item=[J('x')])
A(id='ua', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 회피 증가 1티어', 'T1 increased evasion prefix'), show=['evP'],
  edges=MG({'ur': {'res': 'ok'}, 'uax': {'res': 'fail', 'label': K('다른 접두', 'Another prefix')}}), item=[EVn, J('s')])
A(id='uax', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'), edges=MG({'ua': {'label': K('다시 확장', 'Augment again')}}))
A(id='ur', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'ud'}], item=[EVn, J('p'), J('s')])
A(id='ud', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Rib',
  label=K('훼손', 'Desecrate'), goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')],
  edges=[{'if': {'has': 'evP'}, 'to': 'uf'}, {'to': 'ux', 'hide': True}], item=[EVn, J('p'), UN('p'), J('s')])
A(id='uf', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('회피 증가가 분열되면 성공', 'Success when increased evasion fractures')],
  edges=[{'if': {'fractured': 'evP'}, 'to': 'uc', 'res': 'ok', 'label': K('회피 증가 분열', 'Increased evasion fractured')},
         {'to': 'ux', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[EV, J('p'), UN('p'), J('s')])
A(id='ux', kind='exit', group='prep', pos=[1, 5], simTo='ub', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('회피 증가가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='uc', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[EV, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[EV, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 화염 저항 1티어 — 저항 셋 중 먼저 뜬 것', 'T1 fire resistance suffix: whichever of the three resistances lands first'), show=['fr'],
  skipIf={'has': 'res1'}, skipTo='k2', skipHide=True,
  edges=[{'if': {'has': 'res1'}, 'to': 'k2', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[EV, FR])
A(id='k2', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation', 'Omen_of_Dextral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 옵션 2개 — 튕겨내기 1~2티어 + 잡옵', 'Two suffixes: T1–2 deflection + junk'),
  show=['dfl2'],
  edges=SR({'k3': {'res': 'ok', 'label': K('좋은 접미 2개 + 잡옵', 'Two good suffixes + junk')},
            'k2x': {'res': 'fail', 'label': K('좋은 접미 1개뿐', 'Only one good suffix')}}),
  item=[EV, FR, DF, J('s')])
A(id='k2x', kind='cleanup', group='main', pos=[1, 9.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개까지 지우기', 'Annul down to the fracture + one option'),
  edges=[{'to': 'k1', 'label': K('카오스부터', 'Back to Chaos')}])
A(id='k3', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('접미 냉기 저항 1티어 — 가장 낮은 레벨 잡옵 바꾸기', 'T1 cold resistance suffix: reroll the lowest-level junk'), show=['cr'],
  edges=SR({'q2': {'res': 'ok'}, 'k3e': {'res': 'fail', 'label': K('새 옵션이 접두로', 'New option went to a prefix')},
            'k3d': {'res': 'fail', 'label': K('접두에 옵션 있음', 'A prefix option is there')}}),
  item=[EV, FR, CR, DF1])
A(id='k3d', kind='act', group='main', pos=[2, 10.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling', 'Omen_of_Dextral_Erasure'],
  label=K('절사 + 우측 말소 + 카오스', 'Whittling + Dextral Erasure + Chaos'),
  goal=K('접두에 옵션이 있으면 접미 잡옵만 바꾸기', 'With a prefix option present: reroll only the suffix junk'), show=['cr'],
  edges=SR({}))
A(id='k3e', kind='act', group='main', pos=[1, 10.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('빈 접미 채우기', 'Fill the empty suffix'), show=['cr'], edges=SR({}))
# 접두: 엑잘 → 빗나가면 징표 → 훼손 → 자리 막기 → 다시 엑잘 (영상 42:10~45:02)
A(id='q2', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 회피 1티어 — 회피·회피 복합 중 먼저 뜬 것', 'T1 flat evasion prefix: flat or hybrid evasion, whichever lands first'),
  show=['evF'], edges=PR({'r0': {'res': 'ok'}, 'q3': {'res': 'fail'}}), item=[EV, FL, FR, CR, DF1],
  over=[{'param': {'rT': 2}, 'set': {'item': [EV, FL, FR, DF, J('s')]}}])
A(id='q3', kind='act', group='main', pos=[1, 11.4], act='essence', cur='Essence_of_the_Abyss', ess='mkP', mark=True, omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('빗나간 접두를 지우고 심연의 군주의 징표', 'The missed prefix goes for the Mark of the Abyssal Lord'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=PR({'q4': {'label': K('막기가 남음', 'Blocker still there')}, 'q5': {'label': K('막기가 지워짐', 'Blocker removed')}}))
A(id='q4', kind='act', group='main', pos=[2, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('남은 막기 훼손 옵션 제거', 'Remove the old blocker'), edges=PR({'q5': {'label': K('막기 제거 뒤 징표 훼손', 'Blocker removed, then desecrate the Mark')}}))
A(id='q5', kind='act', group='main', pos=[1, 12.4], act='desecrate', cur='Preserved_Rib', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('접두 징표 훼손', 'Desecrate the prefix Mark'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=PR({'q1': {}}))
A(id='q1', kind='act', group='main', pos=[2, 12.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='blk', label=K('공개', 'Reveal'),
  goal=K('생명력 최대치로 자리 막기 — 생명력·물리 가시 피해 중 먼저 뜬 것', 'Block with maximum life: life or thorns, whichever shows first'), show=['lifeB'],
  edges=PR({'q2': {'label': K('자리 막기 완료 — 엑잘', 'Blocker in place: exalt')}, 'q3': {'label': K('접두가 꽉 참 — 다시 징표', 'Prefixes full: Mark again')}}))
# 접두 두 번째 옵션: 막기 제거 → 고대 갈비뼈 → 공개 (영상 45:32~46:05)
A(id='r0', kind='act', group='main', pos=[0, 13.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=PR({'r1': {}}), item=[EV, FL, FR, CR, DF1],
  over=[{'param': {'rT': 2}, 'set': {'item': [EV, FL, FR, DF, J('s')]}}])
A(id='r1', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('빈 접두 자리 훼손', 'Desecrate the empty prefix slot'), showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=PR({'r2': {}}), item=[EV, FL, UN('p'), FR, CR, DF1],
  over=[{'param': {'rT': 2}, 'set': {'item': [EV, FL, UN('p'), FR, DF, J('s')]}}])
A(id='r2', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='gp', label=K('공개', 'Reveal'),
  goal=K('접두 회피 복합 1티어', 'T1 hybrid evasion prefix'), show=['hyb'],
  edges=PR({'ok': {'res': 'ok'}, 'r0': {'res': 'fail', 'label': K('빗나감', 'Miss')}}), item=[EV, FL, HB, FR, CR, DF1],
  over=[{'param': {'rT': 2}, 'set': {'item': [EV, FL, HB, FR, DF, J('s')]}}])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L0', 'nodes': ['k1', 'k2', 'k2x'], 'kr': '접미 저항·튕겨내기', 'en': 'Resistance and deflection'},
 {'id': 'L1', 'nodes': ['k3', 'k3e', 'k3d'], 'kr': '접미 세 번째 옵션', 'en': 'Third suffix', 'fold': True,
  'goal': K('접미 냉기 저항 1티어 — 저항 2개 + 좋은 접미 하나', 'T1 cold resistance: two resistances + one more good suffix'),
  'goalBy': {'high': K('접미 냉기 저항 1티어 — 저항 1티어 2개 + 저항·튕겨내기 1티어 중 먼저 뜬 것', 'T1 cold resistance: two T1 resistances + a T1 resistance or deflection, whichever lands first'),
             'bal': K('밸런스는 건너뜀 — 마지막 접미는 랜덤 옵션', 'Balance skips it: the last suffix is random')},
  'steps': [K('절사의 징조 + 완벽한 카오스 오브로 가장 낮은 레벨 접미 바꾸기, 잡옵 다음에는 튕겨내기 2티어가 바뀜', 'Omen of Whittling + Perfect Chaos Orb rerolls the lowest-level suffix: the junk first, then T2 deflection') | {'node': 'k3'},
            K('새 옵션이 접두로 가면 우측 찬미 + 완벽한 엑잘로 빈 접미 채우기', 'New option on a prefix: Dextral Exaltation + Perfect Exalted Orb fills the suffix') | {'node': 'k3e'},
            K('접두에 옵션이 생긴 뒤에는 우측 말소의 징조를 더해 접미만 바꾸기', 'Once a prefix option exists, add Omen of Dextral Erasure so only the suffix changes') | {'node': 'k3d'}],
  'item': [EV, FR, CR, DF1]},
 {'id': 'L2', 'nodes': ['q2', 'q3', 'q4', 'q5', 'q1'], 'kr': '접두 첫 번째 옵션', 'en': 'First prefix', 'fold': True,
  'goal': K('접두 회피 1티어 — 회피·회피 복합 중 먼저 뜬 것', 'T1 flat evasion prefix: flat or hybrid evasion, whichever lands first'),
  'goalBy': {'high': K('접두 회피 1티어 — 회피·회피 복합 1티어 중 먼저 뜬 것', 'T1 flat evasion: T1 flat or hybrid evasion, whichever lands first'),
             'bal': K('접두 회피 1~2티어 — 회피·회피 복합 1~2티어 중 먼저 뜬 것', 'T1–2 flat evasion: T1–2 flat or hybrid evasion, whichever lands first')},
  'steps': [K('완벽한 엑잘티드 오브로 접두 (접미가 꽉 차서 접두로)', 'Perfect Exalted Orb on the prefix (suffixes are full)') | {'node': 'q2'},
            K('빗나가면 좌측 결정화 + 심연의 에센스로 징표', 'On a miss: Sinistral Crystallisation + Essence of the Abyss for the Mark') | {'node': 'q3'},
            K('막기가 남아 있으면 빛의 징조 + 소멸의 오브로 제거', 'Blocker still there: Omen of Light + Orb of Annulment') | {'node': 'q4'},
            K('보존된 갈비뼈로 징표 훼손', 'Preserved Rib on the Mark') | {'node': 'q5'},
            K('심연의 메아리 공개로 생명력 최대치 자리 막기 (없으면 물리 가시 피해) → 다시 엑잘', 'Reveal with Abyssal Echoes: block with maximum life (thorns if no life), then exalt again') | {'node': 'q1'}],
  'item': [EV, LB, FL, FR, CR, DF1], 'itemBy': {'bal': [EV, LB, FL, FR, DF, J('s')]}},
 {'id': 'L3', 'nodes': ['r0', 'r1', 'r2'], 'kr': '접두 두 번째 옵션(훼손)', 'en': 'Second prefix (desecrated)', 'fold': True,
  'goal': K('접두 회피 복합 1티어 (훼손)', 'T1 hybrid evasion (desecrated)'),
  'goalBy': {'high': K('접두 회피 복합 1티어 (훼손) — 남은 회피 접두', 'T1 hybrid evasion (desecrated): the remaining evasion prefix'),
             'bal': K('접두 회피 복합 1~2티어 (훼손) — 남은 회피 접두', 'T1–2 hybrid evasion (desecrated): the remaining evasion prefix')},
  'steps': [K('빛의 징조 + 소멸의 오브로 막기 제거', 'Omen of Light + Orb of Annulment removes the blocker') | {'node': 'r0'},
            K('고대 갈비뼈로 빈 접두 자리 훼손', 'Ancient Rib into the empty prefix slot') | {'node': 'r1'},
            K('심연의 메아리 공개 — 빗나가면 빛의 징조 + 소멸의 오브로 다시', 'Reveal with Abyssal Echoes; on a miss Omen of Light + Orb of Annulment and again') | {'node': 'r2'}],
  'item': [EV, FL, HB, FR, CR, DF1], 'itemBy': {'bal': [EV, FL, HB, FR, DF, J('s')]}},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'evP', 'fr': True}, {'tag': 'evF1'}, {'tag': 'hyb1', 'des': True}, {'tag': 'fr'}, {'tag': 'cr'}, {'tag': 'dfl1'}]},   # H2 11-13: 카드는 성공 회차 옵션(정책 11장 11-13 14:17)
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'evP', 'fr': True}, {'tag': 'evF2'}, {'tag': 'hyb2', 'des': True}, {'tag': 'fr'}, {'tag': 'dfl2'}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
