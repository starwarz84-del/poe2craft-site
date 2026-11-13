# G6 2026-11-13: LilBotQ 고급 장화(S-7YHuq3-P4, 14:13) 플로우차트 생성기 — 영상 고급 제작(4:00~13:00) 성공 회차 한 줄
# 근거: scratchpad review/G6/lilbotq-boots-v2/timeline.md · 캡처 33장(영상 4:10~13:35 화면 대조, 0:00~4:00은 가성비 장화 lilbotq-budget-boots 구간)
# 실행: cd scripts/graphs && python3 gen_lilbotq_boots.py → lilbotq-boots-v2.json (gen_batch10.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 성공 회차(화면): 4:22 노멀 특출난 타살리오의 각반(홈 2개) → 5:56 방어구 장인의 고철로 퀄리티 20%(고철 20 → 1) → 6:20~6:35 바알 방어구 장인의 주입기 4개(10 → 6)로 26%
#   → 6:45 우트레드의 성좌 장착 → 6:52 완벽한 진화의 오브 · 완벽한 확장의 오브 + 소멸의 오브 반복(7:20 마나, 7:42 충전 접미 — 빗나감) → 7:58 이동 속도·둔화 감소 1티어 + 번개 저항 1티어
#   → 8:27 상위 풍요의 에센스로 레어 + 희귀도 1티어(8:50) → 9:51 보존된 갈비뼈(좌측 강령술의 징조는 자막) → 9:57 미공개 훼손 접두 → 10:02 분열의 오브 → 10:07 이동 속도 분열
#   → 11:08 아스트리드의 창의성 → 11:20 좌측 결정화의 징조 + 신비한 합금 → 11:46 정신력 +13(제작), 미공개 훼손이 지워짐 → 11:56 완벽한 엑잘 방어도 +162(1티어)
#   → 12:26 고대 갈비뼈 미공개 훼손(뼈 이름은 자막) → 12:34 공개 빗나감(방어도 %·질주 이동 속도·마나) → 빛의 징조 4개(자막, 반복 장면은 편집) → 12:40 회피 구르기 거리 +0.4(2티어)
#   → 13:05 아스트리드를 다른 룬으로 교체(이동 속도 5%, 선택이라 뺌).
# 내부 결정(보고서에 적음):
#   1 매직 단계는 영상 말대로(7:05 'a tier one resistance' — 화염·냉기·번개 저항 1티어 아무거나, 성공 회차 = 번개, 11-13 오후 정책 A) '좋은 옵션 둘이 나올 때까지' 진화·확장 + 소멸 — 이동 속도·둔화 감소 1티어와 번개 저항 1티어 중 먼저 뜬 것부터(정책 11장 붙는 순서 예외).
#   2 접두 두 번째 옵션은 영상(12:05 '대부분 완벽한 엑잘 결과 그대로')대로 모든 등급 랜덤 옵션. 좌측 말소 + 카오스 반복은 꿀팁 후보.
#   3 신성한 오브(9:40 '필요하면')와 마지막 룬 교체(13:05)는 넣지 않음. 바알 방어구 장인의 주입기 4개는 영상대로 단계(오염 위험은 시뮬에 없음).
# 등급(난이도 3 → 밸런스·에센셜): 밸런스 = 영상(빛의 징조로 회피 구르기 거리까지 다시 공개, 1~2티어) / 에센셜 = 공개 결과 그대로(빛의 징조 없음, 정책 10장 C17-3).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/lilbotq-boots-v2.json'
CLS = 'Boots_str'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags, m='n', ti=0, tail=None):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if tail: kr, en = f'{kr} ({tail[0]})', f'{en} ({tail[1]})'
    return L(s, kr, en, m, tags)

MS = DB('p', 55, ['ms'])
MSf = DB('p', 55, ['ms'], 'f')
LT = DB('s', 3, ['res'])                  # 영상 7:58 성공 회차 = 번개 저항 1티어(성공 조건은 원소 저항 1티어 아무거나, 11-13 오후 정책 A)
RA = DB('s', 44, ['ra'], 'c')
SP = DB('s', 51, ['sp'], 'c')
AR = DB('p', 7, [])                       # 영상 12:00 완벽한 엑잘 결과(방어도 +162, 1티어) — 카드에는 랜덤 옵션
DG = DB('p', 57, ['dg'], 'd', ti=1)       # 영상 12:40 회피 구르기 거리 +0.4(2티어)
UH = L('r', '우트레드의 성좌', "Uhtred's Sidereus", 'r')
AST = L('r', '아스트리드의 창의성', "Astrid's Creativity", 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V1 = {'param': {'v': 1}}; V2 = {'param': {'v': 2}}

g = {
 'id': 'lilbotq-boots-v2', 'recipe': 'lilbotq-boots-v2', 'cls': CLS, 'base': 'Tasalian Greaves', 'ilvl': 82, 'basePrice': {},
 'xsub': ["Uhtred's Sidereus"], 'xroll': True,
 'note': ('LilBotQ 고급 장화(S-7YHuq3-P4, 2026-11-13 G6 영상 4:00~13:00 화면 대조) — 노멀 특출난 타살리오의 각반(홈 2개) → 방어구 장인의 고철 20% → 바알 방어구 장인의 주입기 4개 26% '
          '→ 우트레드의 성좌 → 완벽한 진화·확장 + 소멸 반복(이동 속도·둔화 감소 1티어 + 번개 저항 1티어) → 상위 풍요의 에센스(레어 + 희귀도) → 좌측 강령술 + 보존된 갈비뼈 → 분열(이동 속도, 1/3, 실패하면 새 베이스) '
          '→ 아스트리드의 창의성 → 좌측 결정화 + 신비한 합금(미공개 훼손을 지우고 정신력) → 완벽한 엑잘(접두, 결과 그대로) → 고대 갈비뼈 → 심연의 메아리 공개(회피 구르기 거리, 밸런스는 빛의 징조 + 소멸로 다시). '
          '우트레드 옵션은 가중치가 없어 엑잘·진화 풀은 일반 티어 평균, 공개 풀은 훼손 전용 옵션과 같은 무게로 추정. 신성한 오브·마지막 룬 교체는 뺌.'),
 'params': {'v': {'kr': '회피 구르기 거리 공개', 'en': 'Dodge roll reveal',
                  'values': {'1': K('빛의 징조로 다시 (영상)', 'Retry with Omen of Light (video)'), '2': K('결과 그대로', 'Keep it')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('훼손 공개 결과 그대로', 'Keep the first reveal')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 빛의 징조로 회피 구르기 거리까지 다시 공개', 'Video: Omen of Light until dodge roll distance')}],
 'tags': {
   'ms': {'gi': 55, 'tmax': 1}, 'fr': {'gi': 1, 'tmax': 1}, 'cr': {'gi': 2, 'tmax': 1}, 'lt': {'gi': 3, 'tmax': 1},
   'res': {'anyOf': ['fr', 'cr', 'lt'], 'shown': 'lt', 'label': K('화염·냉기·번개 저항 1티어', 'T1 fire, cold or lightning resistance')}, 'ra': {'gi': 44}, 'sp': {'gi': 51}, 'dg': {'gi': 57},
   'good': {'anyOf': ['ms', 'res'], 'label': K('이동 속도·둔화 감소 1티어, 원소 저항 1티어', 'T1 movement speed with slow reduction, T1 elemental resistance')},
 },
 'require': {'all': [{'has': 'ms'}, {'has': 'res'}, {'has': 'ra'}, {'has': 'sp'}, {'full': 'p'}, {'any': [V2, {'has': 'dg'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 26, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 4:22~10:07) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='q1', start={'rar': 'normal', 'mods': [], 'quality': 0},
  label=K('노멀 특출난 타살리오의 각반 구입 (아이템 레벨 82, 홈 2개)', 'Buy a normal exceptional Tasalian Greaves (item level 82, two sockets)'), item=[])
A(id='q1', kind='act', group='prep', pos=[0, 1], act='quality', cur='Armourers_Scrap', count=19, q=20, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 20%', 'Quality 20%'), showText=[K('방어구 장인의 고철 19개', '19 Armourer’s Scraps')], edges=[{'to': 'q2'}], item=[])
A(id='q2', kind='act', group='prep', pos=[0, 2], act='quality', cur='Vaal_Armourers_Infuser', count=4, q=26, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 26%', 'Quality 26%'), showText=[K('바알 방어구 장인의 주입기 4개', '4 Vaal Armourer’s Infusers')],
  edges=[{'to': 'u1'}], item=[])
A(id='u1', kind='act', group='prep', pos=[0, 3], act='rune', label=K('룬', 'Rune'), goal=K('우트레드의 성좌 장착', "Socket Uhtred's Sidereus"),
  showText=[K('시간술 옵션이 붙을 수 있음 (뺄 수 없음)', 'Chronomancy modifiers can roll (cannot be removed)')], rune=K('우트레드의 성좌', "Uhtred's Sidereus"),
  edges=[{'to': 'm1'}], item=[UH])
# 매직 반복(영상 6:52~7:58): 완벽한 진화 → 완벽한 확장, 빗나간 옵션은 소멸의 오브 — 좋은 옵션 둘 중 먼저 뜬 것부터
A(id='m1', kind='act', group='prep', pos=[0, 4], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('이동 속도·둔화 감소 1티어, 원소 저항 1티어 중 먼저 뜬 것', 'T1 movement speed with slow reduction or T1 elemental resistance, whichever lands first'), show=['ms', 'res'],
  edges=[{'if': {'has': 'good'}, 'to': 'm2', 'res': 'ok'}, {'to': 'm1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[MS, UH])
A(id='m1x', kind='cleanup', group='prep', pos=[1, 4], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('옵션을 모두 지우고 다시 진화', 'Clear the options and transmute again'), edges=[{'to': 'm1'}])
A(id='m2', kind='act', group='prep', pos=[0, 5], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('남은 옵션 — 이동 속도·둔화 감소 1티어 또는 원소 저항 1티어', 'The other one: T1 movement speed with slow reduction or T1 elemental resistance'), show=['ms', 'res'],
  edges=[{'if': {'all': [{'has': 'ms'}, {'has': 'res'}]}, 'to': 'e1', 'res': 'ok'}, {'to': 'm2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[MS, LT, UH])
A(id='m2x', kind='cleanup', group='prep', pos=[1, 5], keep=['good'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  edges=[{'lost': 'good', 'to': 'm1x', 'label': K('좋은 옵션이 지워짐', 'The good option went')}, {'to': 'm2', 'label': K('다시 확장', 'Augment again')}])
A(id='e1', kind='act', group='prep', pos=[0, 6], act='essence', cur='Greater_Essence_of_Opulence', ess='ra', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 희귀도 1티어', 'Rare + T1 rarity suffix'), showText=[{'s': 's', 'kr': '발견하는 아이템 희귀도 (15—18)% 증가 (제작 옵션)', 'en': '(15—18)% increased Rarity of Items found (crafted)'}],
  edges=[{'to': 'd1'}], item=[MS, LT, RA, UH])
A(id='d1', kind='act', group='prep', pos=[0, 7], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 확률 1/3', 'Fourth option (desecrated): fracture odds 1/3'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 분열되지 않음)', 'en': 'Desecration (unrevealed, cannot fracture)'}], edges=[{'to': 'f1'}], item=[MS, UN('p'), LT, RA, UH])
A(id='f1', kind='act', group='prep', pos=[0, 8], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('이동 속도·둔화 감소가 분열되면 성공', 'Success when the movement speed line fractures')],
  edges=[{'if': {'fractured': 'ms'}, 'to': 'ms0', 'res': 'ok', 'label': K('이동 속도 분열', 'Movement speed fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[MSf, UN('p'), LT, RA, UH])
A(id='xj', kind='exit', group='prep', pos=[1, 8], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('이동 속도·둔화 감소가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
# ---------------- 옵션 추가 작업 (영상 11:00~12:46) ----------------
A(id='ms0', kind='mark', group='main', pos=[0, 9.4], next='a1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MSf, UN('p'), LT, RA, UH])
A(id='a1', kind='act', group='main', pos=[0, 10.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', "Socket Astrid's Creativity"),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', "Astrid's Creativity"),
  edges=[{'to': 'a2'}], item=[MSf, UN('p'), LT, RA, UH, AST])
A(id='a2', kind='act', group='main', pos=[0, 11.4], act='essence', cur='Mystic_Alloy', ess='sp', omens=['Omen_of_Sinistral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('미공개 훼손 접두를 지우고 접미 정신력', 'The unrevealed desecrated prefix goes for a Spirit suffix'),
  showText=[{'s': 's', 'kr': '정신력 +(10—15) (제작 옵션)', 'en': '+(10—15) to Spirit (crafted)'}], edges=[{'to': 'p1'}], item=[MSf, LT, RA, SP, UH, AST])
A(id='p1', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 나오는 대로', 'Second prefix: keep what lands'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'p2'}], item=[MSf, AR, LT, RA, SP, UH, AST])
# 마지막 접두 훼손(영상 12:15~12:40): 고대 갈비뼈 → 심연의 메아리 공개 → 밸런스는 빗나가면 빛의 징조 + 소멸의 오브로 지우고 다시
A(id='p2', kind='act', group='main', pos=[0, 13.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('빈 접두에 고대 갈비뼈', 'Ancient Rib on the empty prefix'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'p3'}], item=[MSf, AR, UN('p'), LT, RA, SP, UH, AST])
A(id='p3', kind='act', group='main', pos=[0, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='dg', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), show=['dg'],
  edges=[{'if': {'has': 'dg'}, 'to': 'ok', 'res': 'ok'}, {'if': V1, 'to': 'p3x', 'res': 'fail', 'label': K('빗나감', 'Miss')},
         {'to': 'ok', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')}],
  item=[MSf, AR, DG, LT, RA, SP, UH, AST])
A(id='p3x', kind='act', group='main', pos=[1, 14.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('빗나간 훼손 옵션 지우기', 'Remove the missed desecration'), edges=[{'to': 'p2'}])
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L0', 'nodes': ['m1', 'm1x', 'm2', 'm2x'], 'kr': '매직 옵션 두 개', 'en': 'Two magic options', 'fold': True,
  'goal': K('접두 이동 속도·둔화 감소 1티어 + 접미 원소 저항 1티어 — 먼저 뜬 것부터', 'T1 movement speed with slow reduction prefix + T1 elemental resistance suffix: whichever lands first'),
  'steps': [K('완벽한 진화의 오브', 'Perfect Orb of Transmutation') | {'node': 'm1'},
            K('완벽한 확장의 오브로 남은 옵션', 'Perfect Orb of Augmentation for the other one') | {'node': 'm2'},
            K('빗나가면 소멸의 오브', 'A miss: Orb of Annulment') | {'node': 'm2x'},
            K('좋은 옵션이 지워지면 모두 지우고 다시 진화', 'The good option gone: clear it and transmute again') | {'node': 'm1x'}],
  'item': [MS, LT, UH]},
 {'id': 'L1', 'nodes': ['p2', 'p3', 'p3x'], 'kr': '접두 세 번째 옵션(훼손)', 'en': 'Third prefix (desecrated)', 'fold': True,
  'goal': K('접두 회피 구르기 거리(훼손)', 'Dodge roll distance prefix (desecrated)'),
  'goalBy': {'bal': K('접두 회피 구르기 거리(훼손) — 빛의 징조로 다시', 'Dodge roll distance prefix (desecrated): Omen of Light retries'),
             'ess': K('접두 세 번째 옵션(훼손) — 공개 결과 그대로', 'Third prefix (desecrated): keep the reveal')},
  'steps': [K('빈 접두에 고대 갈비뼈', 'Ancient Rib on the empty prefix') | {'node': 'p2'},
            K('심연의 메아리의 징조로 공개', 'Reveal with the Omen of Abyssal Echoes') | {'node': 'p3'},
            K('빗나가면 빛의 징조 + 소멸의 오브', 'A miss: Omen of Light + Orb of Annulment') | {'node': 'p3x'}],
  'item': [MSf, AR, DG, LT, RA, SP, UH, AST]},
]

g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'ms', 'fr': True}, {'side': 'p', 'random': True}, {'tag': 'dg', 'des': True, 'tmax': 2}, {'tag': 'res'}, {'tag': 'ra', 'ess': True}, {'tag': 'sp', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'ms', 'fr': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'res'}, {'tag': 'ra', 'ess': True}, {'tag': 'sp', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
