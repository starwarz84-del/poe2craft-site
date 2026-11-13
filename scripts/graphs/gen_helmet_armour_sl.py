# G6 2026-11-13: SL 게임연구소 #2 종결급 투구(p0fChSu91uI, 11:12) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G6/helmet-armour-sl-v2/timeline.md · 캡처(영상 0:00~11:12 화면 대조)
# 실행: cd scripts/graphs && python3 gen_helmet_armour_sl.py → helmet-armour-sl-v2.json (옛 JSON을 손으로 고치던 것을 대신함)
#
# 성공 회차(화면): 1:04 목표 투구 슬라이드 → 3:00 노멀 제국의 대헬름 4개, 바알 방어구 장인의 주입기로 26%(선택, 1개 오염) → 4:00 완벽한 진화 + 완벽한 확장 + 소멸 반복
#   → 4:26 방어도 % 1티어 + 방어도의 원소 피해 적용 1티어 → 4:31 상위 풍요의 에센스(레어 + 희귀도) → 4:40 신성한 오브(선택) → 5:53 보존된 갈비뼈(미공개 훼손이 접미로)
#   → 5:56 분열의 오브 → 6:06 방어도의 원소 피해 적용 분열 → 6:20~6:54 상위 찬미 + 완벽한 엑잘 한 번 도박(접두 2·3티어, 빗나감) → 소멸로 분열 + 옵션 1개
#   → 7:05~8:41 카오스 오브(생명력 1티어) → 좌측 찬미 + 완벽한 엑잘(정확도 빗나감 → 소멸 → 방어도 +205 1티어) → 8:48 좌측 강령술 + 고대 갈비뼈 → 9:04 심연의 메아리 공개, 방어도 % 1티어
#   → 9:12~9:56 상위 찬미 + 완벽한 엑잘(저항 3티어 둘 → 우측 소멸 → … 냉기 1티어 + 능력치 요구사항 잡옵) → 10:03~10:08 유동체로 냉기 → 번개 저항
#   → 10:11~10:52 절사 + 우측 말소 + 완벽한 카오스 오브 6번 → 희귀도 1티어 접미(완성).
# 내부 결정(보고서에 적음):
#   1 분열: 영상 말대로 세 옵션 모두 유효 — 다른 옵션이 분열되면 같은 흐름(비용 같다고 가정, 옛 그래프 그대로).
#   2 접두 세 자리는 생명력·방어도·방어도 % 중 남은 것 먼저 뜬 것부터(영상 7:20 '셋 중 아무거나').
#   3 난이도 3 → 밸런스·에센셜(정책 10장). 영상 마지막 희귀도 절사(전문가급 비싼 징조 반복)는 C17-2(마지막 옵션 도박은 하이엔드만)라 선택 상자로.
#   4 유동체 상자: 저항이 하나뿐일 때만(영상 5:30 저항 두 줄이면 합쳐짐 주의). 영상은 치직대는 유동체로 번개 — 유동체 이름은 화면으로 못 봄(결과로 판단).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/helmet-armour-sl-v2.json'
CLS = 'Helmets_str'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags, m='n', ti=0):
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

AP = DB('p', 9, ['armP'])                 # 방어도 (92—100)% 증가
APd = DB('p', 9, ['armP'], 'd')
AE = DB('s', 20, ['armEle'])              # 방어도의 +(38—43)%가 원소 피해에도 적용
AEf = DB('s', 20, ['armEle'], 'f')
RAe = DB('s', 45, ['rarE'], 'c')          # 상위 풍요의 에센스 희귀도
LF = DB('p', 6, ['life1'])                 # 생명력 최대치 +(150—174)
FA = DB('p', 8, ['flat'])                 # 방어도 +(191—221)
CO = DB('s', 3, ['cold'])                 # 냉기 저항 1티어(영상 9:56)
LT = DB('s', 4, ['light'])                # 번개 저항 1티어(유동체 뒤)
RAs = DB('s', 17, ['rarS'])               # 희귀도 접미(영상 10:52)
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V1 = {'param': {'v': 1}}; V2 = {'param': {'v': 2}}
P3L = K('생명력 최대치·방어도·방어도 % 증가', 'Maximum life, flat armour or % armour')

g = {
 'id': 'helmet-armour-sl-v2', 'recipe': 'helmet-armour-sl-v2', 'cls': CLS, 'base': 'Imperial Greathelm', 'ilvl': 82, 'basePrice': {},
 'note': ('SL #2 종결급 투구(p0fChSu91uI) — 2026-11-13 G6 영상 0:00~11:12 화면 대조. 노멀 제국의 대헬름(82, 홈 2개) → 완벽한 진화·확장 + 소멸(방어도 % 1티어 + 방어도의 원소 피해 적용 1티어) '
          '→ 상위 풍요의 에센스 → 보존된 갈비뼈 → 분열(세 옵션 모두 유효) → 소멸로 분열 + 옵션 1개 → 카오스 오브(접두 1티어) → 좌측 찬미 + 완벽한 엑잘(접두, 빗나가면 소멸) '
          '→ 좌측 강령술 + 고대 갈비뼈 → 심연의 메아리 공개(밸런스는 빛의 징조로 다시) → 상위 찬미 + 완벽한 엑잘(저항, 밸런스는 빗나가면 우측 소멸) → 유동체(저항 하나일 때) '
          '→ 선택: 절사 + 우측 말소 + 완벽한 카오스(희귀도 접미, 영상). 바알 주입기·신성한 오브·첫 도박 엑잘은 선택.'),
 'params': {'v': {'kr': '반복', 'en': 'Loops',
                  'values': {'1': K('유효 옵션 1~2티어까지 (영상)', 'Until T1–2 wanted lines (video)'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('카오스 오브 접두 하나 뒤로는 엑잘·공개 결과 그대로', 'After the Chaos prefix, every exalt and reveal as it comes')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('접두 셋·저항 1~2티어(빛의 징조·우측 소멸로 다시), 마지막 접미는 나오는 대로', 'Three prefixes and a resistance at T1–2 (Light, Dextral Annulment), last suffix as it comes')}],
 'tags': {
   'armP': {'gi': 9, 'tmax': 1}, 'armEle': {'gi': 20, 'tmax': 1}, 'magicGood': {'anyOf': ['armP', 'armEle']},
   'rarE': {'gi': 45}, 'rarS': {'gi': 17, 'tmax': 1},
   'life1': {'gi': 6, 'tmax': 1}, 'flat1': {'gi': 8, 'tmax': 1}, 'armP1': {'gi': 9, 'tmax': 1},
   'life': {'gi': 6, 'tmax': 2}, 'flat': {'gi': 8, 'tmax': 2}, 'armP2': {'gi': 9, 'tmax': 2},
   'P3c': {'anyOf': ['life1', 'flat1', 'armP1'], 'label': K('생명력 최대치·방어도·방어도 % 증가 1티어', 'T1 maximum life, flat armour or % armour')},
   'P3': {'anyOf': ['life', 'flat', 'armP2'], 'label': K('생명력 최대치·방어도·방어도 % 증가 1~2티어', 'T1–2 maximum life, flat armour or % armour')},
   'fire': {'gi': 2, 'tmax': 2}, 'cold': {'gi': 3, 'tmax': 2}, 'light': {'gi': 4, 'tmax': 2},
   'RES': {'anyOf': ['fire', 'cold', 'light'], 'label': K('화염·냉기·번개 저항 1~2티어', 'T1–2 fire, cold or lightning resistance')},
   'fireA': {'gi': 2}, 'coldA': {'gi': 3}, 'lightA': {'gi': 4}, 'ELE': {'anyOf': ['fireA', 'coldA', 'lightA']},
   'light2': {'gi': 4, 'tmax': 2},
   'sKeep': {'anyOf': ['armEle', 'RES']},
 },
 'require': {'all': [{'has': 'armEle'}, {'full': 'p'}, {'full': 's'}, {'has': 'P3c'},
                     {'any': [V2, {'all': [{'sideAll': {'side': 'p', 'tag': 'P3'}}, {'has': 'RES'}]}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 2]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'h1',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 3:00~7:00) ----------------
A(id='h1', kind='base', group='prep', pos=[0, 0], next='m1', start={'rar': 'normal', 'mods': [], 'quality': 20},
  label=K('노멀 특출난 제국의 대헬름 구입 (아이템 레벨 82, 홈 2개)', 'Buy a normal exceptional Imperial Greathelm (item level 82, two sockets)'), item=[])
A(id='hq', kind='side', group='prep', pos=[1, 0.5], attach=['h1', 'm1'], cur='Vaal_Armourers_Infuser', label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 25% 이상, 선택 — 오염되면 버림', 'Quality 25%+, optional: a corrupted one is thrown away'))
A(id='m1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('방어도 % 증가 1티어, 방어도의 원소 피해 적용 1티어 중 먼저 뜬 것', 'T1 % armour or T1 armour applying to elemental damage, whichever lands first'), show=['armP', 'armEle'],
  edges=[{'if': {'added': 'magicGood'}, 'to': 'm2', 'res': 'ok'}, {'to': 'm1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[AP])
A(id='m1x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('옵션을 모두 지우고 다시 진화', 'Clear the options and transmute again'), edges=[{'to': 'm1'}])
A(id='m2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('남은 옵션 — 방어도 % 증가 1티어 또는 방어도의 원소 피해 적용 1티어', 'The other one: T1 % armour or T1 armour applying to elemental damage'), show=['armP', 'armEle'],
  edges=[{'if': {'all': [{'has': 'armP'}, {'has': 'armEle'}]}, 'to': 'r1', 'res': 'ok'}, {'to': 'm2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[AP, AE])
A(id='m2x', kind='cleanup', group='prep', pos=[1, 2], keep=['magicGood'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  edges=[{'lost': 'magicGood', 'to': 'm1x', 'label': K('좋은 옵션이 지워짐', 'The good option went')}, {'to': 'm2', 'label': K('다시 확장', 'Augment again')}])
A(id='r1', kind='act', group='prep', pos=[0, 3], act='essence', cur='Greater_Essence_of_Opulence', ess='rarE', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 희귀도', 'Rare + rarity suffix'), showText=[{'s': 's', 'kr': '발견하는 아이템 희귀도 (15—18)% 증가 (제작 옵션)', 'en': '(15—18)% increased Rarity of Items found (crafted)'}],
  edges=[{'to': 'f1'}], item=[AP, AE, RAe])
A(id='rd', kind='side', group='prep', pos=[1, 3.5], attach=['r1', 'f1'], cur='Divine_Orb', label=K('신성', 'Divine'),
  goal=K('분열 전 수치 올리기 (선택)', 'Raise the rolls before the fracture (optional)'))
A(id='f1', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f2'}], item=[AP, AE, RAe, UN('s')])
A(id='f2', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 모두 유효 옵션)', 'Fracture (all three revealed options are wanted)'),
  showText=[K('방어도의 원소 피해 적용 분열', 'Armour applying to elemental damage fractures')],
  edges=[{'if': {'fractured': 'armEle'}, 'to': 'f4', 'res': 'ok', 'label': K('원소 피해 적용 분열', 'Armour-to-elemental fractured')},
         {'to': 'xs', 'res': 'ok', 'dash': True, 'label': K('다른 유효 옵션 분열', 'Another wanted option fractured')}],
  item=[AP, AEf, RAe, UN('s')])
A(id='xs', kind='assume', group='prep', pos=[1, 5], next='f4', swapFracture='armEle', variant='ok', label=K('다른 유효 옵션 분열 — 같은 흐름', 'Another wanted option fractured: same flow'),
  note=K('방어도 % 또는 희귀도가 분열돼도 같은 방법으로 진행 (비용은 같다고 가정)', 'Armour % or rarity fractured: the same method around that option (assumed to cost the same)'))
A(id='fg', kind='side', group='prep', pos=[1, 6.5], attach=['f2', 'f4'], cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('한 번 도박, 선택 — 1티어 두 옵션이면 팔기', 'One gamble, optional: two T1 options means a sale'))
A(id='f4', kind='cleanup', group='prep', pos=[0, 7], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('p'), AEf])
# ---------------- 옵션 추가 작업 (영상 7:05~10:52) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8], next='b1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), AEf])
A(id='b1', kind='act', group='main', pos=[0, 9], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 첫 번째 옵션 — 생명력 최대치·방어도·방어도 % 증가 1티어 중 먼저 뜬 것', 'First prefix: T1 life, flat armour or % armour, whichever lands first'), show=['life1', 'flat1', 'armP1'],
  edges=[{'if': {'added': 'P3c'}, 'to': 'b2', 'res': 'ok'}, {'to': 'b1', 'res': 'fail', 'hide': True}], item=[LF, AEf])
A(id='b2', kind='act', group='main', pos=[0, 10], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 남은 두 옵션 중 먼저 뜬 것', 'Second prefix: one of the remaining two'), show=['life', 'flat', 'armP2'],
  edges=[{'if': {'added': 'P3'}, 'to': 'b3', 'res': 'ok'}, {'if': V2, 'to': 'b3', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')},
         {'to': 'b2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[LF, FA, AEf])
A(id='b2x', kind='cleanup', group='main', pos=[1, 10], keep=['P3c'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'lost': 'P3c', 'to': 'b1', 'label': K('첫 번째 접두가 지워짐', 'The first prefix went')}, {'to': 'b2', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='b3', kind='act', group='main', pos=[0, 11], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'b4'}], item=[LF, FA, UN('p'), AEf])
A(id='b4', kind='act', group='main', pos=[0, 12], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='P3', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 남은 한 옵션', 'Third prefix (desecrated): the last of the three'), show=['life', 'flat', 'armP2'],
  edges=[{'if': {'added': 'P3'}, 'to': 's1', 'res': 'ok'}, {'if': V2, 'to': 's1', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')},
         {'to': 'b4x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[LF, FA, APd, AEf])
A(id='b4x', kind='act', group='main', pos=[1, 12], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('빗나간 훼손 옵션 지우기', 'Remove the missed desecration'), edges=[{'to': 'b3'}])
A(id='s1', kind='act', group='main', pos=[0, 13], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션 — 저항 하나', 'Second and third suffix: one resistance'), show=['fire', 'cold', 'light'],
  edges=[{'if': {'has': 'RES'}, 'to': 'sf', 'res': 'ok'}, {'if': V2, 'to': 'sf', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')},
         {'to': 's1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[LF, FA, APd, AEf, CO, J('s')])
A(id='s1x', kind='act', group='main', pos=[1, 13], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=ANN, goal=ANN,
  target=K('빗나간 접미 지우기', 'Remove a missed suffix'), edges=[{'to': 's1'}])
A(id='sf', kind='act', group='main', pos=[0, 14], act='flux', cur='Crackling_Flux', label=K('유동체', 'Flux'),
  goal=K('원소 저항을 번개 저항으로 — 저항이 하나일 때만', 'The elemental resistance becomes lightning: only with a single resistance'), show=['light'],
  skipIf={'any': [{'not': {'has': 'ELE'}}, {'count': {'tag': 'ELE', 'min': 2}}]}, skipTo='ok', skipNote=K('저항이 없거나 둘이면 건너뜀', 'Skipped with no resistance or two'),
  edges=[{'to': 'ok'}], item=[LF, FA, APd, AEf, LT, J('s')])
A(id='ok', kind='done', group='main', pos=[0, 15], label=K('완성', 'Finished'))
A(id='sw', kind='side', group='main', pos=[1, 14.5], attach=['sf', 'ok'], cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling', 'Omen_of_Dextral_Erasure'], label=K('카오스', 'Chaos'),
  goal=K('선택 — 접미 잡옵을 희귀도 1티어로 (영상 6번)', 'Optional: the junk suffix to T1 rarity (six tries in the video)'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['m1', 'm1x', 'm2', 'm2x'], 'kr': '매직 옵션 두 개', 'en': 'Two magic options', 'fold': True,
  'goal': K('접두 방어도 % 증가 1티어 + 접미 방어도의 원소 피해 적용 1티어 — 먼저 뜬 것부터', 'T1 % armour prefix + T1 armour-to-elemental suffix: whichever lands first'),
  'steps': [K('완벽한 진화의 오브', 'Perfect Orb of Transmutation') | {'node': 'm1'},
            K('완벽한 확장의 오브로 남은 옵션', 'Perfect Orb of Augmentation for the other one') | {'node': 'm2'},
            K('빗나가면 소멸의 오브', 'A miss: Orb of Annulment') | {'node': 'm2x'},
            K('좋은 옵션이 지워지면 모두 지우고 다시 진화', 'The good option gone: clear it and transmute again') | {'node': 'm1x'}],
  'item': [AP, AE]},
 {'id': 'L2', 'nodes': ['b1', 'b2', 'b2x'], 'kr': '접두 첫 번째·두 번째 옵션', 'en': 'First and second prefix', 'fold': True,
  'goal': K('접두 생명력 최대치 1티어 + 방어도 1~2티어 — 먼저 뜬 것부터', 'T1 life + T1–2 flat armour prefixes: whichever lands first'),
  'goalBy': {'bal': K('접두 생명력 최대치 1티어 + 방어도 1~2티어 — 먼저 뜬 것부터', 'T1 life + T1–2 flat armour prefixes: whichever lands first'),
             'ess': K('접두 생명력 최대치 1티어 + 엑잘 결과 그대로', 'T1 life prefix + whatever the exalt adds')},
  'steps': [K('카오스 오브로 접두 하나 1티어', 'Chaos Orb for one T1 prefix') | {'node': 'b1'},
            K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브', 'Omen of Sinistral Exaltation + Perfect Exalted Orb') | {'node': 'b2'},
            K('빗나가면 소멸의 오브 — 첫 번째 접두가 지워지면 카오스부터', 'A miss: Orb of Annulment; the first prefix gone means Chaos again') | {'node': 'b2x'}],
  'item': [LF, FA, AEf]},
 {'id': 'L3', 'nodes': ['b3', 'b4', 'b4x'], 'kr': '접두 세 번째 옵션(훼손)', 'en': 'Third prefix (desecrated)', 'fold': True,
  'goal': K('접두 방어도 % 증가 1~2티어(훼손)', 'T1–2 % armour prefix (desecrated)'),
  'goalBy': {'bal': K('접두 방어도 % 증가 1~2티어(훼손) — 빛의 징조로 다시', 'T1–2 % armour prefix (desecrated): Omen of Light retries'),
             'ess': K('접두 세 번째 옵션(훼손) — 공개 결과 그대로', 'Third prefix (desecrated): keep the reveal')},
  'steps': [K('좌측 강령술의 징조 + 고대 갈비뼈', 'Omen of Sinistral Necromancy + Ancient Rib') | {'node': 'b3'},
            K('심연의 메아리의 징조로 공개', 'Reveal with the Omen of Abyssal Echoes') | {'node': 'b4'},
            K('빗나가면 빛의 징조 + 소멸의 오브', 'A miss: Omen of Light + Orb of Annulment') | {'node': 'b4x'}],
  'item': [LF, FA, APd, AEf]},
 {'id': 'L4', 'nodes': ['s1', 's1x'], 'kr': '접미 두 자리', 'en': 'Two suffixes', 'fold': True,
  'goal': K('접미 저항 1~2티어 + 랜덤 옵션', 'T1–2 resistance suffix + a random option'),
  'goalBy': {'bal': K('접미 저항 1~2티어 + 랜덤 옵션', 'T1–2 resistance suffix + a random option'),
             'ess': K('접미 두 자리 — 엑잘 결과 그대로', 'Two suffixes: keep the exalt')},
  'steps': [K('상위 찬미의 징조 + 완벽한 엑잘티드 오브', 'Omen of Greater Exaltation + Perfect Exalted Orb') | {'node': 's1'},
            K('빗나가면 우측 소멸의 징조 + 소멸의 오브', 'A miss: Omen of Dextral Annulment + Orb of Annulment') | {'node': 's1x'}],
  'item': [LF, FA, APd, AEf, CO, J('s')]},
]

g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'life'}, {'tag': 'flat'}, {'tag': 'armP2'}, {'tag': 'armEle', 'fr': True}, {'tag': 'RES'}, {'side': 's', 'random': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'P3c'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'armEle', 'fr': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
