# RECIPE-D 2026-11-14: Kite_xdd 싼 ES 티아라 대량 제작(youtu.be/GQAf_p5GeiQ, 2026-09-13, 0.5.5, 러시아어 — 영어 자동 번역 자막) — 조사 g114(docs/craft-guides.md 6차)
# 영상 흐름 한 줄: 0:01 아이템 레벨 81 매직 선대의 티아라(접두 하나) → 0:52 완벽한 확장(카오스 저항이면 실패) → 1:39 완벽한 제왕 → 2:25 좌측 찬미 + 상위 엑잘(접두 ES)
#   → 3:55 좌측 강령술 + 가장 싼 뼈(접두 훼손, 공개는 나중) → 상위 엑잘(남은 접미) → 4:40 심연의 메아리로 공개 → 7:01 철의 룬(마무리라 뺌)
# 영상은 빗나간 것을 다시 하지 않고 그대로 팔아서(550 ES 하나 80 div, 나머지 7~18 div) 반복 구간이 없음 → 에센셜 하나.
# 실행: cd scripts/graphs && python3 gen_kite_budget_es_tiara.py  → kite-budget-es-tiara-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/kite-budget-es-tiara-v2.json'
CLS = 'Helmets_int'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

ESP = DB('p', 8, ['esP'], 'n', 0)       # 에너지 보호막 % 1티어(표본)
ESF = DB('p', 7, None, 'n', 0)          # 에너지 보호막 최대치 1티어(표본, 엑잘 결과)
INT = DB('s', 0, None, 'n', 0)          # 지능 1티어(표본, 확장 결과)
FR = DB('s', 1, None, 'n', 1)           # 화염 저항 2티어(표본, 제왕 결과)
CR = DB('s', 15, None, 'n', 0)          # 치명타 확률 1티어(표본, 마지막 엑잘)
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
HY = DB('p', 9, None, 'd', 0)           # 에너지 보호막 % + 생명력(훼손, 표본)

g = {
 'id': 'kite-budget-es-tiara-v2', 'recipe': 'kite-budget-es-tiara-v2', 'cls': CLS, 'base': 'Ancestral Tiara', 'ilvl': 81,
 'note': ('2026-11-14 RECIPE-D: Kite_xdd 싼 ES 티아라 대량 제작(youtu.be/GQAf_p5GeiQ, 조사 g114 — docs/craft-guides.md 6차). 러시아어 영상의 영어 자동 번역 자막으로 읽었고, '
          '자막의 "Tier 3/2" 화폐를 완벽한·상위 오브로 읽음(완벽한 확장 20 카오스·완벽한 제왕 5 카오스라는 값과 맞음). '
          '내부 결정: ① 매직 베이스의 접두 종류가 노트에 "접두 하나"뿐이라 에너지 보호막 %로 둠(표본 완성품의 일반 ES 접두 두 개 중 하나) '
          '② 제왕이 접두로 가면 좌측 강령술 훼손 자리가 없어 그 베이스는 그대로 팔고 다음 베이스(영상 "빗나간 건 그냥 팖"에 맞춤) '
          '③ 가장 싼 뼈는 아이템 레벨 81에 쓸 수 있는 보존된 갈비뼈(갉힌 뼈는 아이템 레벨 64까지) ④ 철의 룬(7:01)은 마무리라 뺌. '
          '베이스 값은 자막에 "1 카오스~20 엑잘"로 범위만 있어 넣지 않음. 저항이면 풍요의 에센스·희귀도면 저항 에센스로 레어를 만드는 더 싼 길은 꿀팁 후보.'),
 'params': {},
 'strategies': [{'id': 'ess', 'params': {}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {}, 'tier': 'ess',
               'desc': K('영상 그대로: 한 번씩, 결과 그대로 판매', 'As in the video: each step once, sold as it comes')}],
 'tags': {'esP': {'gi': 8}, 'chaosR': {'gi': 4}, 'esF': {'gi': 7}, 'esH': {'gi': 9}, 'esM': {'gi': 10},
          'esD': {'anyOf': ['esF', 'esP', 'esH', 'esM'], 'shown': 'esH', 'label': K('에너지 보호막 접두', 'Energy shield prefix')}},
 'require': {'all': [{'has': 'esP'}, {'des': True}, {'unrev': False}, {'full': 'p'}, {'full': 's'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)
A(id='b0', kind='base', group='prep', pos=[0, 0], next='a1', start={'rar': 'magic', 'mods': ['esP']},
  label=K('에너지 보호막 % 매직 선대의 티아라 구입 (아이템 레벨 81)', 'Buy a magic Ancestral Tiara with % energy shield (item level 81)'), item=[ESP])
A(id='a1', kind='act', group='prep', pos=[0, 1], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접미 1개 — 나오는 대로 (영상: 지능)', 'One suffix: keep what comes (video: intelligence)'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'if': {'added': 'chaosR'}, 'to': 'b0', 'res': 'fail', 'label': K('카오스 저항 → 다음 베이스', 'Chaos resistance: next base')},
         {'to': 'r1', 'res': 'ok', 'label': K('그 밖', 'Anything else')}],
  ask=K('카오스 저항?', 'Chaos resistance?'), item=[ESP, INT])
A(id='r1', kind='act', group='prep', pos=[0, 2], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 + 접미 1개 — 나오는 대로 (영상: 화염 저항)', 'Rare + one suffix: keep what comes (video: fire resistance)'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'if': {'not': {'sideLt': {'side': 'p', 'n': 2}}}, 'to': 'b0', 'res': 'fail', 'label': K('접두로 감 → 판매, 다음 베이스', 'Landed on a prefix: sell, next base')},
         {'to': 'ms', 'res': 'ok', 'label': K('접미', 'Suffix')}],
  ask=K('접미에 붙었나?', 'Landed on a suffix?'), item=[ESP, INT, FR])
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='x1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ESP, INT, FR])
A(id='x1', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 나오는 대로 (영상: 에너지 보호막 최대치 1티어)', 'Second prefix: keep what comes (video: T1 maximum energy shield)'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'd1'}], item=[ESP, ESF, INT, FR])
A(id='d1', kind='act', group='main', pos=[0, 5.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손, 공개는 나중)', 'Third prefix (desecrated, revealed later)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'x2'}], item=[ESP, ESF, UN, INT, FR])
A(id='x2', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('마지막 접미 — 나오는 대로 (영상: 치명타 확률)', 'Last suffix: keep what comes (video: critical hit chance)'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'd2'}], item=[ESP, ESF, UN, INT, FR, CR])
A(id='d2', kind='act', group='main', pos=[0, 7.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='esD', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 에너지 보호막 접두가 뜨면 그것 (영상: 에너지 보호막 % + 생명력)', 'Third prefix (desecrated): an energy shield prefix when offered (video: % energy shield and life)'),
  show=['esD'], edges=[{'to': 'ok', 'res': 'ok'}], item=[ESP, ESF, HY, INT, FR, CR])
A(id='ok', kind='done', group='main', pos=[0, 8.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'esP'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True, 'des': True},
            {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
