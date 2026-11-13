# G14 2026-11-13: XTheFarmerX 리그 초반 에너지 보호막 갑옷(UWrIgHklsPg, 14:31) 플로우차트 생성기 — 영상 성공 회차 한 줄(영상은 갑옷 하나)
# 근거: scratchpad review/G14/farmer-budget-armour-v2/timeline.md · 캡처(영상 0:00~14:31 화면 대조, 자막 전체)
# 실행: cd scripts/graphs && python3 gen_farmer_budget_armour.py → farmer-budget-armour-v2.json (gen_farmer.py 끝에서 자동 호출, 갑옷 구간을 대신함)
#
# 성공 회차(화면): 3:16 거래소 매직 섬광의 흐르는 의복(아이템 레벨 79, 에너지 보호막 최대치 +76 3티어, 고유 옵션 마나 재생 50%) 1 엑잘티드 오브
#   → 3:26 상위 확장의 오브(창고 II 칸) → 3:30 접미 출혈 지속시간 58% 감소 1티어(잡옵)
#   → 3:45 상위 강화의 에센스(자막, 툴팁 장면 없음) → 3:56 레어 + 에너지 보호막 76% 증가 4티어
#   → 4:00 좌측 강령술의 징조 활성 + 갈비뼈(10 → 9, 4:03), 4:04 채팅 '좌측 강령술의 징조 소모' → 미공개 훼손 접두
#   → 4:14 영혼의 우물: 에너지 보호막 혼합(+26 / 41% 1티어) · 생명력 +19 · 정신력 +52 중 혼합 선택
#   → 4:57 상위 찬미의 징조 활성 + 상위 엑잘티드 오브(최소 속성 레벨 35) → 5:09 접미 에너지 보호막 재충전 속도 3티어 · 생명력 재생 4티어(결과 그대로)
# 내부 결정: 난이도 1(쉬움) → 에센셜만(정책 10장). 영상은 공개를 한 번에 맞혔고 실패하면 '여러 베이스로 시도'라고만 말함 → 에센셜은 반복 없이
#   공개 결과 그대로(완성 카드 랜덤 옵션). 갈비뼈 종류는 툴팁 장면이 없지만 공개에 생명력 +19(13티어, 레벨 1)가 나와 고대 갈비뼈(레벨 40+)는 아니고,
#   아이템 레벨 79라 갉힌 갈비뼈(아이템 레벨 64 이하)도 아님 → 보존된 갈비뼈. 상위 철 룬 2개(4:20)는 취향이라 뺌(정책 9장). 퀄리티는 툴팁에 없음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/farmer-budget-armour-v2.json'
CLS = 'Body_Armours_int'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

FLAT = DB('p', 6, ['flat'], 'n', ti=2)      # 3:30 에너지 보호막 최대치 +76 (74—80) 3티어
BLEED = DB('s', 15, None, 'j', ti=0)        # 3:30 출혈 지속시간 58% 감소 1티어 — 상위 확장 결과(잡옵)
ESS = DB('p', 31, ['ess'], 'c', ti=0)       # 3:56 에너지 보호막 76% 증가 (68—79) = 상위 강화의 에센스
UN = L('p', '접두 훼손 옵션 (미공개)', 'Prefix desecration (unrevealed)', 'u')
HYB = DB('p', 9, ['hyb'], 'd', ti=0)        # 4:14 에너지 보호막 최대치 +26 / 에너지 보호막 41% 증가 1티어(훼손)
RECH = DB('s', 18, None, 'n', ti=2)         # 5:09 에너지 보호막 재충전 속도 16% 3티어 — 엑잘 결과, 카드에는 랜덤 옵션
REGEN = DB('s', 13, None, 'n', ti=3)        # 5:09 생명력 재생 20.8 4티어 — 엑잘 결과, 카드에는 랜덤 옵션

g = {
 'id': 'farmer-budget-armour-v2', 'recipe': 'farmer-budget-armour-v2', 'cls': CLS, 'base': 'Flowing Raiment', 'ilvl': 79,
 'basePrice': {'Exalted_Orb': 1},   # 3:16 거래소 매물(산 물건과 같은 툴팁) 1 엑잘티드 오브
 'note': ('XTheFarmerX 리그 초반 에너지 보호막 갑옷(UWrIgHklsPg, 2026-11-13 G14 영상 전체 화면 대조) — 에너지 보호막 최대치 3티어 매직 흐르는 의복(아이템 레벨 79, 1 엑잘티드 오브) '
          '→ 상위 확장의 오브(접미 잡옵) → 상위 강화의 에센스(레어 + 에너지 보호막 %) → 좌측 강령술의 징조 + 보존된 갈비뼈 → 공개(에너지 보호막 혼합 1티어) '
          '→ 상위 찬미의 징조 + 상위 엑잘티드 오브(접미 2개 결과 그대로). 난이도 쉬움이라 에센셜 하나, 공개는 반복 없이 결과 그대로. 상위 철 룬은 뺌.'),
 'params': {'v': {'kr': '흐름', 'en': 'Flow', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('영상 그대로: 공개와 엑잘은 결과 그대로', 'As the video: the reveal and the exalt are kept as they come')}],
 'tags': {'flat': {'gi': 6, 'tmax': 3}, 'ess': {'gi': 31}, 'hyb': {'gi': 9}},
 'require': {'all': [{'has': 'flat'}, {'has': 'ess'}, {'full': 'p'}, {'full': 's'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 3:00~3:56) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='g1', start={'rar': 'magic', 'mods': [{'tag': 'flat'}]},
  label=K('에너지 보호막 최대치 3티어 매직 흐르는 의복 구입 (아이템 레벨 79)', 'Buy a magic Flowing Raiment with T3 maximum energy shield (item level 79)'),
  item=[FLAT])
A(id='g1', kind='act', group='prep', pos=[0, 1], act='augment', cur='Greater_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접미 잡옵 1개', 'One junk suffix'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'g2'}], item=[FLAT, BLEED])
A(id='g2', kind='act', group='prep', pos=[0, 2], act='essence', cur='Greater_Essence_of_Enhancement', ess='ess', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 에너지 보호막 % 증가', 'Rare + % energy shield prefix'),
  showText=[{'s': 'p', 'kr': '방어도, 회피, 에너지 보호막 (68—79)% 증가 (제작 옵션)', 'en': '(68—79)% increased Armour, Evasion and Energy Shield (crafted)'}],
  edges=[{'to': 'ms'}], item=[FLAT, ESS, BLEED])
# ---------------- 옵션 추가 작업 (영상 4:00~5:09) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='g3', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FLAT, ESS, BLEED])
A(id='g3', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix option (desecrated)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=[{'to': 'g4'}], item=[FLAT, ESS, UN, BLEED])
A(id='g4', kind='act', group='main', pos=[0, 4.4], act='reveal', want='hyb', label=K('공개', 'Reveal'),
  goal=K('접두 에너지 보호막 혼합 (훼손) — 선택지에 없으면 나오는 대로', 'Hybrid energy shield prefix (desecrated): if it is not offered, keep what comes'),
  show=['hyb'], edges=[{'to': 'g5'}], item=[FLAT, ESS, HYB, BLEED])
A(id='g5', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션 — 나오는 대로', 'Second and third suffix options: keep what lands'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'ok'}], item=[FLAT, ESS, HYB, BLEED, RECH, REGEN])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'flat'}, {'tag': 'ess', 'ess': True}, {'side': 'p', 'random': True},
            {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
