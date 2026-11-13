# G13 2026-11-13: XTheFarmerX 리그 초반 번개 지팡이(ITBexsgq2NI 10:00~15:40) 플로우차트 생성기 — 영상 성공 회차 한 줄(지팡이 하나)
# 근거: scratchpad review/G13/farmer-starter-staff-v2/timeline.md · 캡처 14장(영상 10:00~15:40 화면 대조, 자막 전체)
# 실행: cd scripts/graphs && python3 gen_farmer_starter_staff.py → farmer-starter-staff-v2.json (gen_farmer.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 성공 회차(화면): 11:45 거래소 매물 '지옥의 신성한 지팡이 - 전압'(아이템 레벨 73, 추가 화염 피해 49% 2티어 + 번개 주문 +5)
#   → 12:08 상위 마법의 에센스 툴팁 → 12:25 레어 + 주문 피해 151%(제작)
#   → 14:32 채팅 '좌측 강령술의 징조 소모'(보존된 턱뼈는 자막, 뼈 툴팁·사용 장면 없음)
#   → 14:40 영혼의 우물 첫 공개(마나 / 추가 냉기 49% / 원소 주입) → 14:48 심연의 메아리로 다시 뽑기(추가 카오스 50% / 번개 피해 % / 추가 번개 27%) → 14:56 추가 카오스 피해 50%(훼손) 선택
#   → 15:23 상위 엑잘티드 오브 툴팁(창고), 15:32 엑잘티드 오브(20개) 들고 사용 → 15:35 접미 능력치 요구사항 30% 감소·지능 +26 두 개.
# 내부 결정: 사이트 난이도 1(쉬움, 복사된 레시피 값) → 에센셜만(정책 10장). 에센셜 = 영상 흐름 그대로, 공개는 한 번(메아리 다시 뽑기 포함) 결과 그대로.
#   접미 두 옵션은 엑잘티드 오브(일반) 두 번 — 상위 찬미의 징조는 화면·자막에 없어 넣지 않음(옛 그래프에는 있었음), 엑잘 개수는 화면으로 확인 못 함(결과 두 개로 정함).
#   베이스 가격은 사용자 확정(2026-11-10) 카오스 오브 1개 그대로(영상 매물은 엑잘 1개, 자막은 '리그 초반엔 1 div쯤').
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/farmer-starter-staff-v2.json'
CLS = 'Staves'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

FIRE = DB('p', 32, ['fire'], 'n', ti=1)   # 11:45 추가 화염 피해 49% (49—54) 2티어
L5 = DB('s', 17, ['l5'])                  # 11:45 번개 주문 +5 (5—6)
SPELL = DB('p', 49, ['spell'], 'c')       # 12:25 주문 피해 151% (149—188) = 상위 마법의 에센스
CHAOS = DB('p', 35, None, 'd')            # 14:56 추가 카오스 피해 50% (훼손) — 공개 결과, 카드에는 랜덤 옵션
ATR = DB('s', 2, None, 'j', ti=1)         # 15:35 능력치 요구사항 30% 감소 — 엑잘 결과, 카드에는 랜덤 옵션
INT = DB('s', 0, None, 'j', ti=2)         # 15:35 지능 +26 — 엑잘 결과, 카드에는 랜덤 옵션
UN = L('p', '접두 훼손 옵션 (미공개)', 'Prefix desecration (unrevealed)', 'u')

g = {
 'id': 'farmer-starter-staff-v2', 'recipe': 'farmer-starter-staff-v2', 'cls': CLS, 'base': 'Sanctified Staff', 'ilvl': 73,
 'basePrice': {'Chaos_Orb': 1},   # 사용자 2026-11-10 거래소: 번개 주문 매직 지팡이 카오스 오브 1개(영상 11:45 매물은 엑잘 1개)
 'note': ('XTheFarmerX 리그 초반 번개 지팡이(ITBexsgq2NI 10:00~15:40, 2026-11-13 G13 영상 화면 대조) — 추가 화염 피해 2티어 + 번개 주문 +5 매직 축성된 지팡이(아이템 레벨 73) '
          '→ 상위 마술의 에센스(레어 + 주문 피해) → 좌측 강령술의 징조 + 보존된 턱뼈 → 심연의 메아리의 징조로 공개(영상은 추가 카오스 피해) → 엑잘티드 오브로 접미 두 개 나오는 대로. '
          '쉬움이라 에센셜 하나: 공개·엑잘 모두 결과 그대로.'),
 'params': {'v': {'kr': '흐름', 'en': 'Flow', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('영상 그대로: 훼손 공개 한 번, 접미 엑잘 두 번 나오는 대로', 'As the video: one reveal, two suffix exalts kept')}],
 'tags': {'fire': {'gi': 32, 'tmax': 2}, 'l5': {'gi': 17, 'tmax': 1}, 'spell': {'gi': 49}, 'chaos': {'gi': 35}},
 'require': {'all': [{'has': 'fire'}, {'has': 'l5'}, {'has': 'spell'}, {'full': 'p'}, {'full': 's'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'f0',
 'finalItem': {'quality': 0, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 11:00~12:25) ----------------
A(id='f0', kind='base', group='prep', pos=[0, 0], next='f1', start={'rar': 'magic', 'mods': [{'tag': 'fire'}, {'tag': 'l5'}], 'quality': 0},
  label=K('추가 화염 피해 + 번개 주문 레벨 매직 축성된 지팡이 구입 (아이템 레벨 73)', 'Buy a magic Sanctified Staff with extra fire damage + lightning spell levels (item level 73)'),
  item=[FIRE, L5])
A(id='f1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Sorcery', ess='spell', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 주문 피해', 'Rare + spell damage prefix'),
  showText=[{'s': 'p', 'kr': '주문 피해 (149—188)% 증가 (제작 옵션)', 'en': '(149—188)% increased Spell Damage (crafted)'}],
  edges=[{'to': 'ms'}], item=[FIRE, SPELL, L5])
# ---------------- 옵션 추가 작업 (영상 14:20~15:35) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='f2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FIRE, SPELL, L5])
A(id='f2', kind='act', group='main', pos=[0, 2.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecration (unrevealed)'}],
  edges=[{'to': 'f3'}], item=[FIRE, SPELL, UN, L5])
A(id='f3', kind='act', group='main', pos=[0, 3.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='chaos', label=K('공개', 'Reveal'),
  goal=K('접두 세번째 옵션(훼손) — 공개 결과 그대로', 'Third prefix (desecrated): keep the reveal'), show=['chaos'],
  edges=[{'to': 'f4'}], item=[FIRE, CHAOS, SPELL, L5])
A(id='f4', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 두번째 옵션 — 나오는 대로', 'Second suffix: keep what lands'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'f5'}], item=[FIRE, CHAOS, SPELL, L5, ATR])
A(id='f5', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 세번째 옵션 — 나오는 대로', 'Third suffix: keep what lands'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'ok'}], item=[FIRE, CHAOS, SPELL, L5, ATR, INT])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'fire'}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'spell', 'ess': True},
            {'tag': 'l5'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
