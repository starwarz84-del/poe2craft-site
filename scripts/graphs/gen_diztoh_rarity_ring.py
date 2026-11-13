# G12 2026-11-13: Diztoh 희귀도 황금 반지(GDLDxn6yxEs, 10:08) 플로우차트 생성기 — 영상 성공 회차(첫 반지, 자기 장비) 한 줄
# 근거: scratchpad review/G12/diztoh-rarity-ring-v2/timeline.md, frames/ (영상 0:00~10:08 화면 대조)
# 실행: cd scripts/graphs && python3 gen_diztoh_rarity_ring.py  → diztoh-rarity-ring-v2.json
# 상자 id는 옛 레시피(recipes_v5_diztoh-rarity-ring-v2.py, g1~g7)·옛 그래프(h1·g2~g6·g4x)와 겹치지 않게 q0~q6으로 지음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-rarity-ring-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 첫 반지(성공 회차)에 실제로 나온 옵션
RP = L('p', '발견하는 아이템 희귀도 (8—11)% 증가', '(8—11)% increased Rarity of Items found', 'n', ['rp'])          # 1:06·1:35 접두 3티어 11%
CR = L('s', '냉기 저항 +(36—40)%', '+(36—40)% to Cold Resistance', 'n', ['cres'])                                       # 1:06·1:35 접미 2티어 +40%
RE = L('s', '발견하는 아이템 희귀도 (15—18)% 증가 (상위 풍요의 에센스)', '(15—18)% increased Rarity of Items found (Greater Essence of Opulence)', 'c', ['rarE'])   # 1:46 16%
UN = L('s', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')                                                     # 2:40
AR = L('s', '모든 원소 저항 +(6—8)%', '+(6—8)% to all Elemental Resistances', 'd', ['allres'])        # 3:35 공개 4티어 +8%
CA = L('p', '공격 시 냉기 피해 (9—10)~(15—17) 추가', 'Adds (9—10) to (15—17) Cold damage to Attacks', 'j')            # 5:30 5티어 10~17
EV = L('p', '회피 +(108—141)', '+(108—141) to Evasion Rating', 'j')                                                    # 5:30 4티어 122

g = {
 'id': 'diztoh-rarity-ring-v2', 'recipe': 'diztoh-rarity-ring-v2', 'cls': 'Rings', 'base': 'Gold Ring', 'ilvl': 81,
 'basePrice': {'Divine_Orb': 5},   # 1:06 거래소 '까치의 얼음 황금 반지(아이템 레벨 81, 희귀도 14% 내재 · 11% · 냉기 저항 +40%) ~b/o 5 divine', 1:35에 그 반지
 'note': ('2026-11-13 G12 영상 전체(0:00~10:08) 화면 대조. 성공 회차 = 첫 반지(자기 장비, 0:30~5:45): 접두 희귀도 3티어(11%) + 접미 냉기 저항 2티어(+40%) 매직 황금 반지 구입(아이템 레벨 81, 5 div, 1:06·1:35) → '
          '상위 풍요의 에센스(1:35 거래소 1:3 카오스) = 레어 + 접미 희귀도 16%(1:46, 접두에 희귀도가 있어서 접미로 감 — 6:10 자막) → 우측 강령술의 징조(2:32 툴팁, 10 → 9) + 보존된 빗장뼈(2:37 툴팁) = 접미 미공개 훼손(2:40) → '
          '심연의 메아리의 징조 + 공개(3:35 선택지: 마나 회복 2% / 생명력 17 / 모든 원소 저항 +8%, 채팅 메아리 소모, 다시 굴리지 않음) = 모든 원소 저항 +8%(4티어, 그대로 받음 — 3:55 자막) → '
          '툴의 기폭제로 냉기 퀄리티 20%(4:32 툴팁, 5:22 툴팁) → 촉진하는 찬미의 징조 + 상위 찬미의 징조(5:10 툴팁) + 상위 엑잘티드 오브(자막 5:00) = 접두 공격 시 냉기 피해 추가 10~17(5티어) · 회피 122(4티어), 그대로(5:30). '
          '6:20~8:50 두 번째 반지(판매용, 좌측 강령술 + 빗장뼈, 상위 엑잘 2개, 오싹한 유동체로 번개 → 냉기)와 9:00~10:00 우상은 꿀팁 후보. '
          '등급(정책 10장): 난이도 2(보통, 사용자 확정 11-13 14:33 하이엔드 없음). 11-13 오후 새 정책: (B) 영상은 공개를 한 번 하고 다시 굴리지 않아(3:35~4:00) 빛의 징조 반복 없음, 공개 결과 그대로 '
          '(D) 그러면 밸런스·에센셜 비용이 같아(10% 이내) 밸런스 하나만. 마지막 접두 2개도 결과 그대로(C17-2). 촉진하는 찬미의 징조 효과(냉기 옵션 쪽으로 기울임)는 시뮬에 없음 — 결과를 그대로 받아 비용엔 영향 없음.'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
   'desc': K('영상 그대로: 공개·엑잘 결과 그대로', 'As the video: keep the reveal and the exalt as they come')}],
 'tags': {
  'rarP': {'gi': 28, 'tmax': 3}, 'rp': {'gi': 28}, 'cres': {'gi': 5, 'tmax': 2}, 'rarE': {'gi': 66}, 'allres': {'gi': 7},
 },
 'require': {'all': [{'has': 'rarP'}, {'has': 'cres'}, {'has': 'rarE'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'q0',
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 1:06~1:46) ----------------
A(id='q0', kind='base', group='prep', pos=[0, 0], next='q1', start={'rar': 'magic', 'mods': ['rarP', 'cres']},
  label=K('접두 희귀도 + 접미 냉기 저항 매직 황금 반지 구입 (아이템 레벨 81)', 'Buy a magic Gold Ring with prefix rarity + suffix cold resistance (item level 81)'),
  item=[RP, CR])
A(id='q1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Opulence', ess='rarE', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 희귀도', 'Rare + rarity suffix'),
  showText=[{'s': 's', 'kr': '발견하는 아이템 희귀도 (제작 옵션)', 'en': 'Item rarity (crafted)'}], edges=[{'to': 'ms'}], item=[RP, CR, RE])
# ---------------- 옵션 추가 작업 (영상 2:20~5:30) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='q2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[RP, CR, RE])
A(id='q2', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'q3'}], item=[RP, CR, RE, UN])
A(id='q3', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], label=K('공개', 'Reveal'),
  goal=K('접미 세 번째 옵션 공개 — 나오는 대로', 'Reveal the third suffix: keep what comes'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}],
  edges=[{'to': 'q4'}],
  item=[RP, CR, RE, AR])
A(id='q4', kind='act', group='main', pos=[0, 5.4], act='quality', cur='Tuls_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('냉기 퀄리티 20%', '20% cold quality'), edges=[{'to': 'q5'}], item=[RP, CR, RE, AR])
A(id='q5', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 두 번째·세 번째 옵션 — 공격 시 냉기 피해 추가·회피', 'Second and third prefixes: cold damage to attacks, evasion'),
  showText=[K('랜덤 옵션 2개', 'Two random options')], edges=[{'to': 'ok'}], item=[RP, CA, EV, CR, RE, AR])
A(id='ok', kind='done', group='main', pos=[0, 7.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = []
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'rarP'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'cres'}, {'tag': 'rarE', 'ess': True}, {'side': 's', 'random': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
