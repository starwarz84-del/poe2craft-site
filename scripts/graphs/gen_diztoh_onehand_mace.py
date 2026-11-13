# G3 2026-11-13: Diztoh 한손 둔기 — 제작 옵션 2개(WDEkEIQFgT4) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G3/diztoh-onehand-mace-v2/timeline.md, frames/ (영상 0:00~8:00 화면 대조)
# 실행: cd scripts/graphs && python3 gen_diztoh_onehand_mace.py  → diztoh-onehand-mace-v2.json (gen_batch7.py 끝에서 자동 호출)
# D3 2026-11-13(사용자 확정 15:42, 난이도 표 4 전문가 = 하이엔드·밸런스): 하이엔드 새로 — 첫 물리 접두 1티어까지 좌측 말소 + 상위 카오스, 세 번째 접두는 가장 낮은 레벨일 때 절사로 피해 추가 1티어까지.
#   훼손 공개 빛의 징조 반복(15:21 ①)은 이 레시피에선 빗나갈 수 없음: 검은 피의 징조로 쿠르갈 접두 3개가 모두 보이고 그중 물리 피해 증가를 고름(같은 계열 물리 피해 증가가 접두에 있을 때만 막힘 — 그땐 빛의 징조로 다시 해도 같음).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-onehand-mace-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 줄 — 영상 성공 회차에 나온 옵션
CRIT = L('s', '치명타 확률 +(4.41—5)%', '+(4.41—5)% to Critical Hit Chance', 'n', ['crit'])
ELE = L('p', '공격 스킬의 원소 피해 (87—100)% 증가', '(87—100)% increased Elemental Damage with Attacks', 'j')
AS = L('s', '공격 속도 (23—25)% 증가 (상위 가속의 에센스)', '(23—25)% increased Attack Speed (Greater Essence of Haste)', 'c', ['as'])
ATK = L('s', '모든 공격 스킬 레벨 +2 (완벽한 전투의 에센스)', '+2 to Level of all Attack Skills (Perfect Essence of Battle)', 'c', ['atk'])
FIREj = L('p', '화염 피해 추가 (낮은 티어)', 'Adds Fire Damage (low tier)', 'j')
HYB = L('p', '물리 피해 (65—74)% 증가 + 정확도 +(150—174)', '(65—74)% increased Physical Damage, +(150—174) to Accuracy Rating', 'n', ['hyb'])
UN = L('p', '접두 훼손 옵션 (미공개, 쿠르갈)', 'Prefix desecration (unrevealed, Kurgal)', 'n')
KP = L('p', '물리 피해 (110—154)% 증가, 공격 속도 15% 감소 (훼손)', '(110—154)% increased Physical Damage, 15% reduced Attack Speed (desecrated)', 'd', ['kp'])
LIGHTj = L('p', '번개 피해 추가 (낮은 티어)', 'Adds Lightning Damage (low tier)', 'j')
FIRE = L('p', '화염 피해 (88—101)~(133—154) 추가', 'Adds (88—101) to (133—154) Fire Damage', 'n', ['fire1'])
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

PB = K('물리 피해 증가와 정확도·물리 피해 추가', '% physical with accuracy or flat physical')
FB = K('물리·화염·냉기·번개 피해 추가', 'Added physical, fire, cold or lightning damage')

g = {
 'id': 'diztoh-onehand-mace-v2', 'recipe': 'diztoh-onehand-mace-v2', 'cls': 'One_Hand_Maces', 'base': 'Marauding Mace', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 3},
 'note': ('2026-11-13 G3 영상 전체 화면 대조(근거 scratchpad review/G3/diztoh-onehand-mace-v2/timeline.md). 성공 회차 한 줄: '
          '노멀 특출난 약탈하는 철퇴 구입(3 div, 아이템 레벨 82, 퀄리티 26%) → 완벽한 진화·확장 + 소멸 반복(0:13~1:43) → 치명타 확률 1티어(1:43) + 접두 잡옵(1:52) → '
          '상위 가속의 에센스로 레어 + 공격 속도(2:08) → 아스트리드의 창의성(2:35) → 좌측 결정화 + 완벽한 전투의 에센스로 접두 지우고 공격 스킬 +2(2:45~3:10) → '
          '상위 엑잘 빗나감(3:17 화염 낮은 티어) → 좌측 말소 + 상위 카오스 반복 → 물리 피해 증가와 정확도 2티어(3:42~3:51) → 검은 피의 징조 + 보존된 턱뼈(4:26~4:30) → '
          '상위 엑잘(4:41 번개 낮은 티어) → 공개, 쿠르갈 물리 피해 113%(4:50) → 절사의 징조 + 상위 카오스 2번 → 화염 피해 추가 1티어(5:00~5:09). '
          '신성한 오브·완벽한 철 룬·타락(5:12~8:00)은 정책 9·14장대로 뺌. '
          '내부 결정: 접두 물리 옵션은 물리 피해 증가와 정확도·물리 피해 추가만 셈(물리 피해 증가는 쿠르갈 물리 피해와 같은 계열이라 공개를 막음). 검은 피의 징조 공개는 접두 쿠르갈 옵션이 3개뿐이라 늘 물리 피해 증가가 나옴(같은 계열이 있을 때만 빗나감, 그대로 진행). '
          '완성 카드의 훼손 줄은 쿠르갈 접두 셋 묶음(세 번째 접두 엑잘이 물리 피해 증가를 붙이면 같은 계열이라 공개에 물리 피해가 안 나옴 — 시뮬 밸런스 97%·에센셜 96%가 물리 피해). '
          '11-13 오후 새 정책(P8, A 표시): 물리 접두·쿠르갈 공개·피해 추가 묶음은 판정은 묶음 그대로, 화면은 영상 성공 회차 옵션(물리 피해 증가와 정확도·물리 피해 증가와 공격 속도 감소·화염 피해 추가, shown), 나머지는 꿀팁 줄. '
          '등급(난이도 표 4 전문가, 11-13 15:42): 하이엔드 = 첫 물리 접두 1티어까지 좌측 말소 + 상위 카오스, 세 번째 접두는 가장 낮은 레벨일 때 절사 + 상위 카오스로 피해 추가 1티어까지(그렇지 않으면 랜덤 옵션 — 말소는 물리·쿠르갈 옵션을 지울 수 있어 C17-2 예외) / 밸런스 = 첫 물리 접두 1~2티어까지 좌측 말소 + 상위 카오스, 세 번째 접두는 가장 낮은 레벨일 때만 절사 + 상위 카오스 / 에센셜 = 상위 엑잘 결과 그대로.'),
 'params': {
   'pT': {'kr': '첫 물리 접두', 'en': 'First physical prefix', 'values': {'1': K('1티어까지 좌측 말소로 다시', 'Sinistral Erasure until T1'), '2': K('1~2티어까지 좌측 말소로 다시', 'Sinistral Erasure until T1–2'), '0': K('나오는 대로', 'As it comes')}},
   'g': {'kr': '세 번째 접두', 'en': 'Third prefix', 'values': {'2': K('가장 낮은 레벨이면 절사로 피해 추가 1티어까지', 'Whittle while it is the lowest, until T1 added damage'), '1': K('가장 낮은 레벨이면 절사로 다시', 'Whittle while it is the lowest'), '0': K('나오는 대로', 'As it comes')}},
   'fT': {'kr': '피해 추가 티어', 'en': 'Added damage tier', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1, 'g': 2, 'fT': 1}}, {'id': 'bal', 'params': {'pT': 2, 'g': 1, 'fT': 2}}, {'id': 'ess', 'params': {'pT': 0, 'g': 0, 'fT': 2}}],
 'versions': [
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1, 'g': 2, 'fT': 1}, 'tier': 'high',
    'desc': K('첫 물리 접두 1티어까지 좌측 말소, 세 번째 접두는 가장 낮은 레벨일 때 절사로 피해 추가 1티어까지', 'Sinistral Erasure until a T1 physical prefix; whittle the third prefix while it is the lowest, until T1 added damage')},
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'pT': 0, 'g': 0, 'fT': 2}, 'tier': 'ess',
    'desc': K('상위 엑잘 결과 그대로', 'Greater Exalts kept as they come')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'pT': 2, 'g': 1, 'fT': 2}, 'tier': 'bal',
    'desc': K('첫 물리 접두 1~2티어까지 좌측 말소, 세 번째 접두는 가장 낮은 레벨일 때 절사로 다시', 'Sinistral Erasure until a T1–2 physical prefix; whittle the third prefix while it is the lowest')}],
 'tags': {
   'crit': {'gi': 17, 'tmax': 1}, 'as': {'gi': 44}, 'atk': {'gi': 54}, 'kp': {'gi': 25},
   'hyb': {'gi': 8, 'tmax': '$pT'}, 'pflat': {'gi': 2, 'tmax': '$pT'},
   'phys': {'anyOf': ['hyb', 'pflat'], 'shown': 'hyb', 'label': PB},
   'fl2': {'gi': 2, 'tmax': '$fT'}, 'fire1': {'gi': 3, 'tmax': 1}, 'fire2': {'gi': 3, 'tmax': '$fT'}, 'cold2': {'gi': 4, 'tmax': '$fT'}, 'light2': {'gi': 6, 'tmax': '$fT'},
   'flat': {'anyOf': ['fl2', 'fire2', 'cold2', 'light2'], 'shown': 'fire2', 'label': FB},
   'ke': {'gi': 26}, 'kc': {'gi': 27},
   'kAny': {'anyOf': ['kp', 'ke', 'kc'], 'shown': 'kp', 'label': K('쿠르갈 접두 — 물리 피해 증가와 공격 속도 감소·강화 공격 피해·냉기 관통', 'Kurgal prefix: % physical with reduced attack speed, Empowered Attack damage or cold penetration')},
   'keepW': {'anyOf': ['crit', 'as', 'atk', 'kp', 'phys', 'flat']}},
 'conds': {'magicOk': {'has': 'crit'}},
 'require': {'all': [{'has': 'crit'}, {'has': 'as'}, {'has': 'atk'}, {'full': 'p'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h1',
 'finalItem': {'quality': 26, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
WS = {'whittleSafe': {'tag': 'keepW', 'keepDes': True}}
# ---------------- 베이스템 완성 ----------------
A(id='h1', kind='base', group='prep', pos=[0, 0], next='h2', start={'rar': 'normal', 'mods': [], 'quality': 26},
  label=K('노멀 특출난 약탈하는 철퇴 구입 (아이템 레벨 82, 퀄리티 26%)', 'Buy a normal exceptional Marauding Mace (item level 82, quality 26%)'), item=[])
A(id='h2', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation',
  label=K('매직 첫 번째 옵션', 'First magic option'), goal=K('접미 치명타 확률 1티어', 'T1 crit chance suffix'), show=['crit'],
  edges=[{'if': {'has': 'crit'}, 'to': 'h3', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'h2x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
  ask=K('원하는 옵션?', 'Wanted option?'), item=[CRIT])
A(id='h2x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), edges=[{'to': 'h2b'}])
A(id='h2b', kind='act', group='prep', pos=[1, 2], act='augment', cur='Perfect_Orb_of_Augmentation',
  label=K('확장', 'Augment'), goal=K('접미 치명타 확률 1티어', 'T1 crit chance suffix'), show=['crit'],
  edges=[{'if': {'has': 'crit'}, 'to': 'h3', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'h2x', 'res': 'fail', 'label': K('빗나감', 'miss')}])
A(id='h3', kind='act', group='prep', pos=[0, 3], act='augment', cur='Perfect_Orb_of_Augmentation',
  label=K('매직 두 번째 옵션', 'Second magic option'), goal=K('접두 잡옵 (에센스가 지울 자리)', 'Junk prefix (the slot an essence clears later)'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'h4'}], item=[ELE, CRIT])
A(id='h4', kind='act', group='prep', pos=[0, 4], act='essence', cur='Greater_Essence_of_Haste', ess='as',
  label=K('에센스', 'Essence'), goal=K('레어 + 접미 공격 속도', 'Rare + attack speed suffix'),
  showText=[{'s': 's', 'kr': '공격 속도 (23—25)% 증가 (제작 옵션)', 'en': '(23—25)% increased Attack Speed (crafted)'}],
  edges=[{'to': 'ms'}], item=[ELE, CRIT, AS])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 5.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ELE, CRIT, AS])
A(id='k1', kind='act', group='main', pos=[0, 6.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'k2'}], item=[ELE, CRIT, AS, AST])
A(id='k2', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Perfect_Essence_of_Battle', ess='atk', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 접미 공격 스킬 +2', 'Clear the junk prefix for +2 attack skills suffix'),
  showText=[{'s': 's', 'kr': '모든 공격 스킬 레벨 +2 (제작 옵션)', 'en': '+2 to Level of all Attack Skills (crafted)'}],
  edges=[{'to': 'k3'}], item=[CRIT, AS, ATK, AST])
A(id='k3', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 물리 피해 증가와 정확도 1~2티어', 'T1–2 % physical with accuracy prefix'),
  
  show=['phys'],
  edges=[{'if': {'any': [{'has': 'phys'}, {'param': {'pT': 0}}]}, 'to': 'k5', 'res': 'ok'},
         {'to': 'k4', 'res': 'fail', 'label': K('빗나감 — 좌측 말소', 'Miss: Sinistral Erasure')}],
  item=[FIREj, CRIT, AS, ATK, AST],
  over=[{'param': {'pT': 1}, 'set': {'goal': K('접두 물리 피해 증가와 정확도 1티어', 'T1 % physical with accuracy prefix')}},
        {'param': {'pT': 0}, 'set': {'goal': K('접두 첫 번째 옵션 (나오는 대로)', 'First prefix option (keep what comes)'), 'show': [], 'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}]}}])
A(id='k4', kind='act', group='main', pos=[1, 8.4], act='chaos', cur='Greater_Chaos_Orb', omens=['Omen_of_Sinistral_Erasure'], label=K('좌측 말소 + 카오스', 'Sinistral Erasure + Chaos'),
  goal=K('접두 다시 — 물리 피해 증가와 정확도 1~2티어', 'Reroll the prefix: T1–2 % physical with accuracy'), show=['phys'],
  over=[{'param': {'pT': 1}, 'set': {'goal': K('접두 다시 — 물리 피해 증가와 정확도 1티어', 'Reroll the prefix: T1 % physical with accuracy')}}],
  edges=[{'if': {'has': 'phys'}, 'to': 'k5', 'res': 'ok'}, {'to': 'k4', 'res': 'fail', 'hide': True}],
  item=[HYB, CRIT, AS, ATK, AST])
A(id='k5', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_the_Blackblooded'], label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손, 쿠르갈)', 'Second prefix option (desecrated, Kurgal)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개, 공개 3개 모두 쿠르갈)', 'en': 'Prefix desecration (unrevealed, all three options Kurgal)'}],
  edges=[{'to': 'k6'}], item=[HYB, UN, CRIT, AS, ATK, AST])
A(id='k6', kind='act', group='main', pos=[0, 10.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션', 'Third prefix option'), showText=[{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}],
  edges=[{'to': 'k7'}], item=[HYB, UN, LIGHTj, CRIT, AS, ATK, AST])
A(id='k7', kind='act', group='main', pos=[0, 11.4], act='reveal', want='kp', label=K('공개', 'Reveal'),
  goal=K('접두 물리 피해 증가, 공격 속도 감소 (훼손)', '% physical with reduced attack speed prefix (desecrated)'), show=['kAny'],
  edges=[{'to': 'k8', 'res': 'ok'}], item=[HYB, KP, LIGHTj, CRIT, AS, ATK, AST])
A(id='k8', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Greater_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('세 번째 접두를 화염 피해 추가 1~2티어로', 'Third prefix into T1–2 added fire damage'),
  over=[{'param': {'pT': 1}, 'set': {'goal': K('세 번째 접두를 화염 피해 추가 1티어로', 'Third prefix into T1 added fire damage')}}],
  show=['flat'],
  skipIf={'any': [{'param': {'g': 0}}, {'has': 'flat'}, {'not': WS}]}, skipTo='ok', skipHide=True,
  skipNote=K('피해 추가가 이미 있거나 세 번째 접두가 가장 낮은 레벨이 아니면 건너뜀', 'Skipped when added damage is there or the third prefix is not the lowest level'),
  edges=[{'if': {'has': 'flat'}, 'to': 'ok', 'res': 'ok'}, {'if': WS, 'to': 'k8', 'res': 'fail', 'hide': True}, {'to': 'ok', 'res': 'ok', 'hide': True}],
  item=[HYB, KP, FIRE, CRIT, AS, ATK, AST])
A(id='ok', kind='done', group='main', pos=[0, 13.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['h2', 'h2x', 'h2b'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'phys'}, {'tag': 'kAny', 'des': True}, {'side': 'p', 'random': True}, {'tag': 'crit'}, {'tag': 'as', 'ess': True}, {'tag': 'atk', 'ess': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'phys'}, {'tag': 'kAny', 'des': True}, {'side': 'p', 'random': True}, {'tag': 'crit'}, {'tag': 'as', 'ess': True}, {'tag': 'atk', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'side': 'p', 'random': True}, {'tag': 'kAny', 'des': True}, {'side': 'p', 'random': True}, {'tag': 'crit'}, {'tag': 'as', 'ess': True}, {'tag': 'atk', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
