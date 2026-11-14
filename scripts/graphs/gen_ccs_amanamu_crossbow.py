# RECIPE-D 2026-11-14: ccs 오일 수류탄 정신력 석궁(youtu.be/72ckN2hCgCU, 2026-09-12, 0.5.5) — 조사 g107(docs/craft-guides.md 6차)
# 영상 흐름 한 줄: 홈 3개 노멀 석궁 → 변화의 오브(옵션 하나) → 상위 가속의 에센스(레어 + 공격 속도) → 우측 강령술 + 군왕의 징조 + 보존된 턱뼈 → 공개(아마나무 접미 = 스킬 정신력 점유 효율)
# 바알 오브로 홈 4개(3:09)·영혼 핵 4개·추출의 오브는 시뮬·엔진에 규칙이 없어 뺌(타락). 표본 완성품 tools/test/guides/g107-ccs-amanamu-spirit-crossbow.txt
# 실행: cd scripts/graphs && python3 gen_ccs_amanamu_crossbow.py  → ccs-amanamu-crossbow-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/ccs-amanamu-crossbow-v2.json'
CLS = 'Crossbows'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

LGT = DB('p', 7, None, 'j', ti=1)            # 표본: 번개 피해 1~260 추가(2티어) — 변화의 오브 결과(잡옵)
AS = DB('s', 44, ['as'], 'c', ti=0)          # 공격 속도 (14—16)% = 상위 가속의 에센스
UN = L('s', '접미 훼손 옵션 (미공개, 아마나무)', 'Suffix desecration (unrevealed, Amanamu)', 'u')
SPI = DB('s', 29, ['spirit'], 'd', ti=0)     # 스킬 정신력 점유 효율 (5—10)% (아마나무 훼손)
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'ccs-amanamu-crossbow-v2', 'recipe': 'ccs-amanamu-crossbow-v2', 'cls': CLS, 'base': 'Cannonade Crossbow', 'ilvl': 79,
 'basePrice': {'Exalted_Orb': 1.5},   # 1:02 '홈 3개 일반 1~2 엑잘'
 'note': ('2026-11-14 RECIPE-D: ccs 오일 수류탄 정신력 석궁(youtu.be/72ckN2hCgCU, 조사 g107 — docs/craft-guides.md 6차, 영어 자막). '
          '1:02 홈 3개 노멀 석궁(아무 종류, 표본은 연속 포격 석궁 아이템 레벨 79) → 1:33 변화의 오브로 옵션 하나(연금술은 화염 피해가 붙을 수 있어 쓰지 않음) '
          '→ 2:03 에센스로 레어(자막 "아무 에센스", 표본 공격 속도 14% = 상위 가속의 에센스로 읽음) → 2:03 우측 강령술의 징조 + 군왕의 징조 + 보존된 턱뼈(자막 "턱뼈 5 엑잘") '
          '→ 공개: 석궁 아마나무 접미는 정신력 점유 효율·수류탄 두 번 작동 둘뿐이라 늘 고를 수 있음. '
          '내부 결정: 자막에 징조가 하나 더 나오는데 이름이 뒤틀려 확인 못 함 → 넣지 않음. 변화의 오브가 공격 속도(일반)를 붙이면 같은 계열이라 에센스를 못 쓰니 소멸 후 다시 변화(영상에 없음). '
          '3:09 바알 오브로 홈 4개(실패면 새 베이스)·영혼 핵 4개(정신력 60)·추출의 오브 회수는 시뮬·엔진에 타락 규칙이 없어 뺌. 난이도 0이라 에센셜 하나.'),
 'params': {},
 'strategies': [{'id': 'ess', 'params': {}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {}, 'tier': 'ess',
               'desc': K('영상 그대로: 한 번씩, 결과 그대로', 'As in the video: each step once, kept as it comes')}],
 'tags': {'as': {'gi': 44}, 'asN': {'gi': 16}, 'spirit': {'gi': 29}},
 'require': {'all': [{'has': 'as'}, {'has': 'spirit'}, {'unrev': False}, {'desSide': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'sockets': 3},
}

N = []
A = lambda **kw: N.append(kw)
A(id='b0', kind='base', group='prep', pos=[0, 0], next='t1', start={'rar': 'normal', 'mods': []},
  label=K('홈 3개 노멀 석궁 구입 (연속 포격 석궁, 아이템 레벨 79)', 'Buy a normal crossbow with 3 sockets (Cannonade Crossbow, item level 79)'), item=[])
A(id='t1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 옵션 1개 — 나오는 대로 (영상: 번개 피해 추가)', 'One magic option: keep what comes (video: added lightning damage)'),
  showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'if': {'has': 'asN'}, 'to': 't1x', 'res': 'fail', 'label': K('공격 속도', 'Attack speed')},
         {'to': 'e1', 'res': 'ok', 'label': K('그 밖', 'Anything else')}],
  ask=K('공격 속도가 붙었나?', 'Attack speed landed?'), item=[LGT])
A(id='t1x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('옵션을 지워 노멀로', 'Annul back to normal'), edges=[{'to': 't1'}])
A(id='e1', kind='act', group='prep', pos=[0, 2], act='essence', cur='Greater_Essence_of_Haste', ess='as', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 공격 속도', 'Rare + attack speed suffix'),
  showText=[{'s': 's', 'kr': '공격 속도 (14—16)% 증가 (제작 옵션)', 'en': '(14—16)% increased Attack Speed (crafted)'}],
  edges=[{'to': 'ms'}], item=[LGT, AS])
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='d1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[LGT, AS])
A(id='d1', kind='act', group='main', pos=[0, 4.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Dextral_Necromancy', 'Omen_of_the_Liege'],
  label=K('훼손', 'Desecrate'), goal=K('접미 두 번째 옵션(훼손, 아마나무)', 'Second suffix option (desecrated, Amanamu)'),
  showText=[{'s': 's', 'kr': '접미 훼손 옵션 (미공개, 아마나무)', 'en': 'Suffix desecration (unrevealed, Amanamu)'}],
  edges=[{'to': 'd2'}], item=[LGT, AS, UN])
A(id='d2', kind='act', group='main', pos=[0, 5.4], act='reveal', want='spirit', label=K('공개', 'Reveal'),
  goal=K('접미 스킬 정신력 점유 효율 (아마나무, 훼손)', 'Spirit reservation efficiency suffix (Amanamu, desecrated)'), show=['spirit'],
  edges=[{'to': 'ok', 'res': 'ok'}], item=[LGT, AS, SPI])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'random': True}, {'tag': 'as', 'ess': True}, {'tag': 'spirit', 'des': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
