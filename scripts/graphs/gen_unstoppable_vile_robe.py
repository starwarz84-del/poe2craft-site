# W34 2026-11-13: Unstoppable BTW 에너지 보호막 갑옷(swF5mwXmZ0k 5:45~24:15) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W34-unstoppable/timeline.md, frames/ (영상 화면 대조)
# 실행: cd scripts/graphs && python3 gen_unstoppable_vile_robe.py  → unstoppable-vile-robe-v2.json (gen_batch27.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/unstoppable-vile-robe-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

HYn = L('p', '에너지 보호막 최대치 +(26—30), 에너지 보호막 (39—42)% 증가', '+(26—30) to maximum Energy Shield, (39—42)% increased Energy Shield', 'n', ['hyb'])
HY = L('p', '에너지 보호막 최대치 +(26—30), 에너지 보호막 (39—42)% 증가 (분열)', '+(26—30) to maximum Energy Shield, (39—42)% increased Energy Shield (fractured)', 'f', ['hyb'])
EP = L('p', '에너지 보호막 (101—110)% 증가', '(101—110)% increased Energy Shield', 'n', ['esP'])
EF = L('p', '에너지 보호막 최대치 +(91—96) (훼손)', '+(91—96) to maximum Energy Shield (desecrated)', 'd', ['esF'])
LB = L('p', '생명력 최대치 +(70—84) (훼손)', '+(70—84) to maximum Life (desecrated)', 'd')
FR = L('s', '화염 저항 +(41—45)%', '+(41—45)% to Fire Resistance', 'n', ['fr'])
CR = L('s', '냉기 저항 +(41—45)%', '+(41—45)% to Cold Resistance', 'n', ['cr'])
LR = L('s', '번개 저항 +(41—45)%', '+(41—45)% to Lightning Resistance', 'n', ['lr'])
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkP'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'unstoppable-vile-robe-v2', 'recipe': 'unstoppable-vile-robe-v2', 'cls': 'Body_Armours_int', 'base': 'Vile Robe', 'ilvl': 82,
 'note': ('2026-11-13 W34 영상 화면 대조(근거 scratchpad review/W34-unstoppable/timeline.md). 성공 회차(Wrath Cloak) 한 줄: '
          '끔찍한 로브(아이템 레벨 82, 특출난 룬 소켓 3개, 5:57) → 소멸의 오브·확장으로 매직 에너지 보호막 복합 1티어 + 번개 저항 1티어(8:50) → 완벽한 제왕(9:20 에너지 보호막 최대치 4티어) → '
          '유동체로 번개 → 화염(10:28, 뺌) → 훼손으로 옵션 4개(10:46) → 분열의 오브(10:49) → 에너지 보호막 복합(최대치 +29·39~42%) 분열(10:52) → 소멸로 분열 + 옵션 1개 → '
          '카오스 오브 반복으로 저항 1티어(13:25 화염 42%) → 상위 찬미 + 우측 찬미 + 완벽한 엑잘로 접미 2개(13:40 냉기 1티어 + 잡옵, 11:02 상위 찬미 소모) → '
          '접두 훼손 공개로 생명력 자리 막기(15:00) → 완벽한 엑잘로 접두 에너지 보호막 증가 107% 1티어(15:55) → 빛의 징조 + 소멸로 막기 제거(16:18) → '
          '고대 갈비뼈 + 심연의 메아리 공개 반복(16:25~18:05, 17:52 고대 갈비뼈 10개 59 div) → 에너지 보호막 최대치 +93 1티어(18:25) → '
          '마지막 접미 잡옵(점화 지속시간)을 절사의 징조 + 우측 말소의 징조 + 완벽한 카오스 오브로 번개 저항 1티어(21:08~22:04, 21:25 우측 말소 10.8 div). '
          '11-11 판은 분열을 에너지 보호막 증가로 적었으나 10:46(분열 전 파랑) → 10:52(분열 뒤 옅은 색)·23:35 완성품 화면으로 복합 분열 확인. '
          '13:30~14:10 절사 카오스 시연(생명력이 접두로)·심연의 에센스로 징표를 만든 과정은 시연이라 성공 회차의 자리 막기를 빈 접두 훼손으로 줄임. '
          '유동체·신성한 오브·바알 오브·완벽한 룬(22:30~23:50)은 정책 14장대로 뺌.'),
 'params': {
   'pT': {'kr': '접두 에너지 보호막', 'en': 'Energy shield prefixes', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'rT': {'kr': '마지막 접미', 'en': 'Last suffix', 'values': {'1': K('번개 저항 1티어', 'T1 lightning resistance'), '2': K('랜덤 옵션', 'Random option')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1, 'rT': 1}}, {'id': 'bal', 'params': {'pT': 2, 'rT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'pT': 2, 'rT': 2}, 'tier': 'bal',
    'desc': K('저항 1티어 2개, 접두 에너지 보호막 1~2티어, 마지막 접미는 랜덤 옵션', 'Two T1 resistances, T1–2 energy shield prefixes, a random last suffix')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1, 'rT': 1}, 'tier': 'high',
    'desc': K('영상: 모든 옵션 1티어, 저항 3개', 'Video: every option T1, three resistances')}],
 'tags': {
   'hyb': {'gi': 9, 'tmax': 1},
   'esP': {'gi': 7, 'tmax': '$pT'}, 'esF': {'gi': 6, 'tmax': '$pT'},
   'esP1': {'gi': 7, 'tmax': 1}, 'esF1': {'gi': 6, 'tmax': 1}, 'esP2': {'gi': 7, 'tmax': 2}, 'esF2': {'gi': 6, 'tmax': 2},
   'gp': {'anyOf': ['esP', 'esF'], 'label': K('에너지 보호막 증가·에너지 보호막 최대치', 'Increased or maximum energy shield')},
   'fr': {'gi': 1, 'tmax': 1}, 'cr': {'gi': 2, 'tmax': 1}, 'lr': {'gi': 3, 'tmax': 1},
   'fr2': {'gi': 1, 'tmax': 2}, 'cr2': {'gi': 2, 'tmax': 2}, 'lr2': {'gi': 3, 'tmax': 2},
   'frT': {'gi': 1, 'tmax': '$rT'}, 'crT': {'gi': 2, 'tmax': '$rT'}, 'lrT': {'gi': 3, 'tmax': '$rT'},
   'res1': {'anyOf': ['fr', 'cr', 'lr'], 'label': K('화염·냉기·번개 저항 1티어', 'T1 fire, cold or lightning resistance')},
   'res2': {'anyOf': ['fr2', 'cr2', 'lr2'], 'label': K('화염·냉기·번개 저항 1~2티어', 'T1–2 fire, cold or lightning resistance')},
   'resT': {'anyOf': ['frT', 'crT', 'lrT']},
   'blk': {'anyOf': [{'gi': 5}, {'gi': 12}], 'label': K('생명력 최대치·물리 가시 피해', 'Maximum life or physical thorns')},
   'mkP': {'gi': 44}},
 'require': {'all': [{'has': 'hyb'}, {'count': {'tag': 'gp', 'min': 2}}, {'count': {'tag': 'res1', 'min': 2}}, {'any': [{'param': {'rT': 2}}, {'count': {'tag': 'resT', 'min': 3}}]}]},
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

# 매직 단계: 복합이 없으면 접두가 차 있을 때 소멸의 오브, 비어 있으면 확장 (영상 7:30)
def MG(vis):
    out = []
    for e in [{'if': {'all': [{'has': 'hyb'}, {'full': 's'}]}, 'to': 'ur'}, {'if': {'has': 'hyb'}, 'to': 'ua'},
              {'if': {'full': 'p'}, 'to': 'uax'}, {'to': 'ua'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# 접두 두 자리: 단계마다 아이템 상태를 다시 봄 (영상 14:30~18:25, 회피 조끼 42:10~45:55와 같은 방식)
def PR(vis):
    out = []; seen = set()
    for e in [{'if': {'count': {'tag': 'gp', 'min': 2}}, 'to': 'w9'},
              {'if': {'all': [{'unrevSide': 'p'}, {'count': {'tag': 'gp', 'min': 1}}]}, 'to': 'r2'},
              {'if': {'unrevSide': 'p'}, 'to': 'q1'},
              {'if': {'all': [{'has': 'mkP'}, {'desSide': 'p'}]}, 'to': 'q4'},
              {'if': {'has': 'mkP'}, 'to': 'q5'},
              {'if': {'all': [{'count': {'tag': 'gp', 'min': 1}}, {'sideLt': {'side': 'p', 'n': 3}}, {'des': False}]}, 'to': 'r1'},
              {'if': {'all': [{'count': {'tag': 'gp', 'min': 1}}, {'sideLt': {'side': 'p', 'n': 3}}]}, 'to': 'q2'},
              {'if': {'all': [{'count': {'tag': 'gp', 'min': 1}}, {'desSide': 'p'}]}, 'to': 'r0'},
              {'if': {'count': {'tag': 'gp', 'min': 1}}, 'to': 'q3'},
              {'if': {'all': [{'sideLt': {'side': 'p', 'n': 3}}, {'desSide': 'p'}]}, 'to': 'q2'},
              {'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'q0'},
              {'to': 'q3'}]:
        v = vis.get(e['to']); dup = e['to'] in seen; seen.add(e['to']); d = {'label': PL[e['to']]} if e['to'] in PL else {}
        out.append({**e, **d, **v, **({'hide': True} if dup else {})} if v is not None else {**e, **d, 'hide': True})
    return out

# ---------------- 베이스템 완성 ----------------
A(id='ub', kind='base', group='prep', pos=[0, 0], next='ut', start={'rar': 'normal', 'mods': []},
  label=K('끔찍한 로브 구입 (아이템 레벨 82, 특출난 룬 소켓 3개)', 'Buy a Vile Robe (item level 82, exceptional, three rune sockets)'), item=[])
A(id='ut', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=MG({'ua': {}}), item=[J('x')])
A(id='ua', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 에너지 보호막 복합 1티어', 'T1 hybrid energy shield prefix'), show=['hyb'],
  edges=MG({'ur': {'res': 'ok'}, 'uax': {'res': 'fail', 'label': K('다른 접두', 'Another prefix')}}), item=[HYn, J('s')])
A(id='uax', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'), edges=MG({'ua': {'label': K('다시 확장', 'Augment again')}}))
A(id='ur', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'ud'}], item=[HYn, J('p'), J('s')])
A(id='ud', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Rib',
  label=K('훼손', 'Desecrate'), goal=K('네번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')],
  edges=[{'if': {'has': 'hyb'}, 'to': 'uf'}, {'to': 'ux', 'hide': True}], item=[HYn, J('p'), UN('p'), J('s')])
A(id='uf', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('에너지 보호막 복합이 분열되면 성공', 'Success when the hybrid fractures')],
  edges=[{'if': {'fractured': 'hyb'}, 'to': 'uc', 'res': 'ok', 'label': K('복합 분열', 'Hybrid fractured')},
         {'to': 'ux', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[HY, J('p'), UN('p'), J('s')])
A(id='ux', kind='exit', group='prep', pos=[1, 5], simTo='ub', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('복합이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='uc', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[HY, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[HY, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 화염 저항 1티어 — 저항 셋 중 먼저 뜬 것', 'T1 fire resistance suffix: whichever of the three resistances lands first'), show=['fr', 'cr', 'lr'],
  skipIf={'has': 'res1'}, skipTo='k2', skipHide=True,
  edges=[{'if': {'has': 'res1'}, 'to': 'k2', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[HY, FR])
A(id='k2', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation', 'Omen_of_Dextral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 옵션 2개 — 냉기 저항 1티어 (남은 저항 중 먼저 뜬 것)', 'Two suffixes: T1 cold resistance (whichever remaining resistance lands first)'),
  show=['fr', 'cr', 'lr'],
  edges=[{'if': {'count': {'tag': 'res1', 'min': 2}}, 'to': 'q0', 'res': 'ok'},
         {'to': 'k2x', 'res': 'fail', 'label': K('저항 1개뿐', 'Only one resistance')}],
  item=[HY, FR, CR, J('s')])
A(id='k2x', kind='cleanup', group='main', pos=[1, 9.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개까지 지우기', 'Annul down to the fracture + one option'),
  edges=[{'to': 'k1', 'label': K('카오스부터', 'Back to Chaos')}])
# 접두 첫 옵션: 자리 막기 → 엑잘, 빗나가면 징표 → 훼손 → 다시 막기 (영상 14:30~15:55, 조끼 42:25~45:00)
A(id='q0', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('빈 접두 자리 훼손', 'Desecrate an empty prefix slot'), showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=PR({'q1': {}}), item=[HY, UN('p'), FR, CR, J('s')])
A(id='q1', kind='act', group='main', pos=[1, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='blk', label=K('공개', 'Reveal'),
  goal=K('생명력 최대치로 자리 막기 — 생명력·물리 가시 피해 중 먼저 뜬 것', 'Block with maximum life: life or thorns, whichever shows first'), show=['blk'],
  edges=PR({'q2': {'label': K('자리 막기 완료 — 엑잘', 'Blocker in place: exalt')}, 'q3': {'label': K('접두가 꽉 참 — 다시 징표', 'Prefixes full: Mark again')}}), item=[HY, LB, FR, CR, J('s')])
A(id='q2', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 에너지 보호막 증가 1티어 — 에너지 보호막 증가·최대치 중 먼저 뜬 것', 'T1 increased energy shield prefix: increased or maximum energy shield, whichever lands first'),
  show=['esP', 'esF'], edges=PR({'r0': {'res': 'ok'}, 'q3': {'res': 'fail'}}), item=[HY, LB, EP, FR, CR, J('s')])
A(id='q3', kind='act', group='main', pos=[1, 11.4], act='essence', cur='Essence_of_the_Abyss', ess='mkP', mark=True, omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('빗나간 접두를 지우고 심연의 군주의 징표', 'The missed prefix goes for the Mark of the Abyssal Lord'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=PR({'q4': {'label': K('막기가 남음', 'Blocker still there')}, 'q5': {'label': K('막기가 지워짐', 'Blocker removed')}}))
A(id='q4', kind='act', group='main', pos=[2, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('남은 막기 훼손 옵션 제거', 'Remove the old blocker'), edges=PR({'q5': {'label': K('막기 제거 뒤 징표 훼손', 'Blocker removed, then desecrate the Mark')}}))
A(id='q5', kind='act', group='main', pos=[1, 12.4], act='desecrate', cur='Preserved_Rib', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('접두 징표 훼손', 'Desecrate the prefix Mark'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=PR({'q1': {}}))
# 접두 두번째 옵션: 막기 제거 → 고대 갈비뼈 → 공개 (영상 16:18~18:25)
A(id='r0', kind='act', group='main', pos=[0, 13.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=PR({'r1': {}}), item=[HY, EP, FR, CR, J('s')])
A(id='r1', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('빈 접두 자리 훼손', 'Desecrate the empty prefix slot'), showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=PR({'r2': {}}), item=[HY, EP, UN('p'), FR, CR, J('s')])
A(id='r2', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='gp', label=K('공개', 'Reveal'),
  goal=K('접두 에너지 보호막 최대치 1티어', 'T1 maximum energy shield prefix'), show=['esF', 'esP'],
  edges=PR({'w9': {'res': 'ok'}, 'r0': {'res': 'fail', 'label': K('빗나감', 'Miss')}}), item=[HY, EP, EF, FR, CR, J('s')])
# 마지막 접미: 절사의 징조 + 우측 말소의 징조 + 완벽한 카오스 오브 (영상 21:00~22:04, 레벨 82 저항이 접미를 잠금 18:45)
A(id='w9', kind='act', group='main', pos=[0, 16.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling', 'Omen_of_Dextral_Erasure'],
  label=K('절사 + 우측 말소 + 카오스', 'Whittling + Dextral Erasure + Chaos'),
  goal=K('접미 번개 저항 1티어 — 마지막 잡옵 바꾸기', 'T1 lightning resistance suffix: reroll the last junk'), show=['frT', 'crT', 'lrT'],
  skipIf={'any': [{'param': {'rT': 2}}, {'count': {'tag': 'resT', 'min': 3}}]}, skipTo='ok', skipHide=True,
  skipNote=K('밸런스는 마지막 접미가 랜덤 옵션이라 건너뜀', 'Balance skips it: the last suffix is random'),
  edges=[{'if': {'count': {'tag': 'resT', 'min': 3}}, 'to': 'ok', 'res': 'ok'}, {'to': 'w9', 'res': 'fail', 'hide': True}],
  item=[HY, EP, EF, FR, CR, LR])
A(id='ok', kind='done', group='main', pos=[0, 17.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L0', 'nodes': ['k1', 'k2', 'k2x'], 'kr': '접미 저항 2개', 'en': 'Two resistances'},
 {'id': 'L1', 'nodes': ['q0', 'q1', 'q2', 'q3', 'q4', 'q5'], 'kr': '접두 첫번째 옵션', 'en': 'First prefix', 'fold': True,
  'goal': K('접두 에너지 보호막 증가 1티어 — 에너지 보호막 증가·최대치 중 먼저 뜬 것', 'T1 increased energy shield prefix: increased or maximum energy shield, whichever lands first'),
  'goalBy': {'high': K('접두 에너지 보호막 증가 1티어 — 에너지 보호막 증가·최대치 1티어 중 먼저 뜬 것', 'T1 increased energy shield: T1 increased or maximum energy shield, whichever lands first'),
             'bal': K('접두 에너지 보호막 증가 1~2티어 — 에너지 보호막 증가·최대치 1~2티어 중 먼저 뜬 것', 'T1–2 increased energy shield: T1–2 increased or maximum energy shield, whichever lands first')},
  'steps': [K('보존된 갈비뼈로 빈 접두 자리 훼손', 'Preserved Rib into an empty prefix slot') | {'node': 'q0'},
            K('심연의 메아리 공개로 생명력 최대치 자리 막기 (없으면 물리 가시 피해)', 'Reveal with Abyssal Echoes: block with maximum life (thorns if no life)') | {'node': 'q1'},
            K('완벽한 엑잘티드 오브로 접두 (접미가 꽉 차서 접두로)', 'Perfect Exalted Orb on the prefix (suffixes are full)') | {'node': 'q2'},
            K('빗나가면 좌측 결정화 + 심연의 에센스로 징표', 'On a miss: Sinistral Crystallisation + Essence of the Abyss for the Mark') | {'node': 'q3'},
            K('막기가 남아 있으면 빛의 징조 + 소멸의 오브로 제거', 'Blocker still there: Omen of Light + Orb of Annulment') | {'node': 'q4'},
            K('보존된 갈비뼈로 징표 훼손 → 다시 자리 막기', 'Preserved Rib on the Mark, then block again') | {'node': 'q5'}],
  'item': [HY, LB, EP, FR, CR, J('s')]},
 {'id': 'L2', 'nodes': ['r0', 'r1', 'r2'], 'kr': '접두 두번째 옵션(훼손)', 'en': 'Second prefix (desecrated)', 'fold': True,
  'goal': K('접두 에너지 보호막 최대치 1티어 (훼손)', 'T1 maximum energy shield (desecrated)'),
  'goalBy': {'high': K('접두 에너지 보호막 최대치 1티어 (훼손) — 남은 에너지 보호막 접두', 'T1 maximum energy shield (desecrated): the remaining energy shield prefix'),
             'bal': K('접두 에너지 보호막 최대치 1~2티어 (훼손) — 남은 에너지 보호막 접두', 'T1–2 maximum energy shield (desecrated): the remaining energy shield prefix')},
  'steps': [K('빛의 징조 + 소멸의 오브로 막기 제거', 'Omen of Light + Orb of Annulment removes the blocker') | {'node': 'r0'},
            K('고대 갈비뼈로 빈 접두 자리 훼손', 'Ancient Rib into the empty prefix slot') | {'node': 'r1'},
            K('심연의 메아리 공개 — 빗나가면 빛의 징조 + 소멸의 오브로 다시', 'Reveal with Abyssal Echoes; on a miss Omen of Light + Orb of Annulment and again') | {'node': 'r2'}],
  'item': [HY, EP, EF, FR, CR, J('s')]},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'hyb', 'fr': True}, {'tag': 'esP1'}, {'tag': 'esF1', 'des': True}, {'tag': 'fr'}, {'tag': 'cr'}, {'tag': 'lr'}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'hyb', 'fr': True}, {'tag': 'esP2'}, {'tag': 'esF2', 'des': True}, {'tag': 'res1'}, {'tag': 'res1'}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
