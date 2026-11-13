# G13 2026-11-13: LilBotQ 가성비 장화(S-7YHuq3-P4 앞부분 0:00~4:10) 플로우차트 생성기 — 영상 성공 회차 한 줄(영상은 샌들 하나)
# 근거: scratchpad review/G13/lilbotq-budget-boots-v2/timeline.md · 캡처 18장(영상 0:00~4:10 화면 대조, 자막 전체). 4:10 뒤는 고급 장화(lilbotq-boots-v2, G6)
# 실행: cd scripts/graphs && python3 gen_lilbotq_budget_boots.py → lilbotq-budget-boots-v2.json (gen_batch5.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 성공 회차(화면): 0:25 매직 모래맹세 샌들(아이템 레벨 82, 이동 속도 35% 1티어 + 냉기 저항 42% 1티어, 자막 '신성한 오브 1개에 삼')
#   → 2:01 붉은 에센스(상위 절연의 에센스, 2:26 스택 10 → 9) → 2:07 레어 + 화염 저항 32%(3티어)
#   → 2:17 상위 엑잘티드 오브 툴팁 · 2:21 우측 강령술의 징조 툴팁 · 2:26 보존된 갈비뼈 툴팁 → 2:30 미공개 훼손 접미(D)
#   → 2:56 접두 두 개가 한 번에: 생명력 최대치 +99(3티어)·에너지 보호막 71%(3티어) — 상위 찬미의 징조는 자막만(징조 툴팁 장면 없음)
#   → 3:16 심연의 메아리의 징조 툴팁 → 3:32 영혼의 우물 공개 선택지(번개 저항 40% / 힘 및 지능 / 기절 한계치) → 3:37 번개 저항 40%(2티어), 첫 시도
#   → 4:08 퀄리티 20%(방어구 장인의 고철은 자막, 사용 장면 없음). 숙련공의 오브(소켓)는 제작과 관계없어 뺌.
# 내부 결정: 사이트 난이도 1(쉬움 — 복사된 레시피 값, difficulty.py의 옛 id 값 2는 v2에 안 붙음) → 에센셜만(정책 10장, build_recipes _gkeep).
#   에센셜 = 영상 흐름 그대로, 공개는 한 번(빛의 징조 없음, 영상도 첫 공개에 번개 저항 2티어). 베이스 매직 옵션은 영상대로 1티어.
#   옛 사용자 확정(11-10: 공개에서 카오스 듀얼 저항·카오스 저항도 성공)은 확정 옵션 규칙(11-12 20:56)과 부딪쳐 영상에 나온 번개 저항 하나로 — 묶음 비용은 보고서 의문.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/lilbotq-budget-boots-v2.json'
CLS = 'Boots_int'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

MS = DB('p', 12, ['ms'])                 # 0:25 이동 속도 35% 1티어
COLD = DB('s', 2, ['cold'])              # 0:25 냉기 저항 42% 1티어
FIRE = DB('s', 41, ['fire'], 'c')        # 2:07 화염 저항 32% (31—35) = 상위 절연의 에센스
LIFE = DB('p', 5, None, 'j', ti=2)       # 2:56 생명력 최대치 +99 (85—99) 3티어 — 엑잘 결과, 카드에는 랜덤 옵션
ESP = DB('p', 8, None, 'j', ti=2)        # 2:56 에너지 보호막 71% (68—79) 3티어 — 엑잘 결과, 카드에는 랜덤 옵션
LRES = DB('s', 3, None, 'd', ti=1)   # 3:37 번개 저항 40% (36—40) 2티어(훼손)
UN = L('s', '접미 훼손 옵션 (미공개)', 'Suffix desecration (unrevealed)', 'u')

g = {
 'id': 'lilbotq-budget-boots-v2', 'recipe': 'lilbotq-budget-boots-v2', 'cls': CLS, 'base': 'Sandsworn Sandals', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 1},   # 0:10 자막 '신성한 오브 1개에 이 아이템을 구입'
 'note': ('LilBotQ 가성비 장화(S-7YHuq3-P4 0:00~4:10, 2026-11-13 G13 영상 화면 대조) — 이동 속도 + 냉기 저항 1티어 매직 모래맹세 샌들(1 div) → 상위 절연의 에센스(레어 + 화염 저항) '
          '→ 우측 강령술의 징조 + 보존된 갈비뼈 → 상위 찬미의 징조 + 상위 엑잘티드 오브(접두 두 개 나오는 대로) → 심연의 메아리의 징조로 공개(번개 저항) → 방어구 장인의 고철로 퀄리티 20%. '
          '쉬움이라 에센셜 하나: 공개는 한 번, 결과 그대로.'),
 'params': {'v': {'kr': '흐름', 'en': 'Flow', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('영상 그대로: 엑잘은 나오는 대로, 훼손 공개 한 번', 'As the video: exalts kept, one reveal')}],
 'tags': {'ms': {'gi': 12, 'tmax': 1}, 'cold': {'gi': 2, 'tmax': 1}, 'fire': {'gi': 41}, 'lres': {'gi': 3, 'tmax': 2}},
 'require': {'all': [{'has': 'ms'}, {'has': 'cold'}, {'has': 'fire'}, {'full': 'p'}, {'full': 's'}, {'desSide': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finalItem': {'quality': 20, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 0:10~2:07) ----------------
A(id='k0', kind='base', group='prep', pos=[0, 0], next='k1', start={'rar': 'magic', 'mods': [{'tag': 'ms'}, {'tag': 'cold'}], 'quality': 0},
  label=K('이동 속도 + 냉기 저항 1티어 매직 모래맹세 샌들 구입 (아이템 레벨 82)', 'Buy magic Sandsworn Sandals with T1 movement speed + T1 cold resistance (item level 82)'),
  item=[MS, COLD])
A(id='k1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Insulation', ess='fire', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 화염 저항', 'Rare + fire resistance suffix'),
  showText=[{'s': 's', 'kr': '화염 저항 +(31—35)% (제작 옵션)', 'en': '+(31—35)% to Fire Resistance (crafted)'}],
  edges=[{'to': 'ms'}], item=[MS, COLD, FIRE])
# ---------------- 옵션 추가 작업 (영상 2:10~4:08) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='k2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MS, COLD, FIRE])
A(id='k2', kind='act', group='main', pos=[0, 2.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecration (unrevealed)'}],
  edges=[{'to': 'k3'}], item=[MS, COLD, FIRE, UN])
A(id='k3', kind='act', group='main', pos=[0, 3.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째·세번째 옵션 — 나오는 대로', 'Second and third prefixes: keep what lands'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'k4'}], item=[MS, LIFE, ESP, COLD, FIRE, UN])
A(id='k4', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='lres', label=K('공개', 'Reveal'),
  goal=K('접미 세번째 옵션(훼손) — 공개 결과 그대로', 'Third suffix (desecrated): keep the reveal'), show=['lres'],
  edges=[{'to': 'q1'}],
  item=[MS, LIFE, ESP, COLD, LRES, FIRE])
A(id='q1', kind='act', group='main', pos=[0, 6.4], act='quality', cur='Armourers_Scrap', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 20%', 'Quality 20%'), showText=[K('방어구 장인의 고철 20개', '20 Armourer’s Scraps')],
  edges=[{'to': 'ok'}], item=[MS, LIFE, ESP, COLD, LRES, FIRE])
A(id='ok', kind='done', group='main', pos=[0, 7.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'ms'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'cold'}, {'side': 's', 'random': True, 'des': True}, {'tag': 'fire', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
