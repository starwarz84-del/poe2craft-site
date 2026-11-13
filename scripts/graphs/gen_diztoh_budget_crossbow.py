# G14 2026-11-13: Diztoh 가성비 석궁(vk3pLFUov8U, 5:43) 플로우차트 생성기 — 영상 성공 회차 한 줄(영상은 석궁 하나)
# 근거: scratchpad review/G14/diztoh-budget-crossbow-v2/timeline.md · 캡처(영상 0:00~5:43 화면 대조, 자막 전체)
# 실행: cd scripts/graphs && python3 gen_diztoh_budget_crossbow.py → diztoh-budget-crossbow-v2.json (gen_batch7.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 성공 회차(화면): 0:45 노멀 특출난 공성 쇠뇌(아이템 레벨 82, 고유 옵션 수류탄 투사체 +1)
#   → 완벽한 진화·완벽한 확장(1:05, 창고 III 칸)·소멸의 오브(1:19)로 매직 다시(1:00 정확도 + 시야, 1:10 냉기 + 공격 속도)
#   → 1:27 접두 물리 피해 162% 2티어 + 접미 마나 흡수 8.69% 1티어
#   → 1:37 상위 마모의 에센스(자막) → 레어 + 물리 피해 35~52 추가 → 1:52 아스트리드의 창의성 장착(제작 옵션 하나 더)
#   → 우측 결정화의 징조 + 완벽한 전투의 에센스(2:00~2:08, 자막·화면 에센스 탭) → 접미 마나 흡수 대신 공격 스킬 +3
#   → 2:16 우측 강령술의 징조, 2:22 군왕의 징조(무기 훼손에 아마나무 확정), 보존된 턱뼈(자막, 뼈 장면 없음) → 미공개 훼손 접미
#   → 2:40 상위 찬미의 징조 + 완벽한 엑잘티드 오브(창고 III 칸) → 접두 정확도 4티어 + 접미 힘 2티어
#   → 2:53 심연의 메아리의 징조(3:08 채팅 소모) + 3:01 공개: 수류탄 24% 두 번 발동(선택지 1개)
#   → 3:16 아스트리드의 창의성을 철 룬으로 교체(뺌) → 3:32 절사의 징조 + 3:48 완벽한 카오스 오브 → 정확도 4티어가 화염 피해 추가 4티어로(4:03)
#   → 퀄리티·철 룬·바알 주입기·타락(4:00~5:43, 마무리라 뺌 — 타락으로 망가짐).
# 내부 결정: 난이도 1(쉬움) → 에센셜만. 매직 반복은 준비 구역(완벽한 진화·확장은 최소 레벨 70이라 물리 피해 %는 1~2티어만 나옴).
#   절사 카오스는 영상처럼 한 번(가장 낮은 옵션이 잡옵일 때만, 결과 그대로) — 에센셜이라 반복하지 않음. 심연의 메아리의 징조는 영상대로 넣음(군왕으로 아마나무 접미 2개뿐이라 효과 없음).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-budget-crossbow-v2.json'
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

PCT = DB('p', 8, ['ppct'], 'n', ti=1)       # 1:27 물리 피해 162% (155—169) 2티어
LEECH = DB('s', 12, None, 'j', ti=0)        # 1:27 마나 흡수 8.69% 1티어(잡옵)
FLAT = DB('p', 39, ['flatE'], 'c', ti=0)    # 1:37 물리 피해 35~52 추가 = 상위 마모의 에센스
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
ATK = DB('s', 53, ['battle'], 'c', ti=0)    # 모든 공격 스킬 레벨 +3 = 완벽한 전투의 에센스
UN = L('s', '접미 훼손 옵션 (미공개, 아마나무)', 'Suffix desecration (unrevealed, Amanamu)', 'u')
ACC = DB('p', 17, None, 'j', ti=3)          # 2:40 정확도 316 (4티어) — 엑잘 결과(잡옵)
STR = DB('s', 0, None, 'n', ti=1)           # 2:40 힘 28 (2티어) — 엑잘 결과, 카드에는 랜덤 옵션
GREN = DB('s', 30, ['gren'], 'd', ti=0)     # 3:01 수류탄 24% 두 번 발동 (아마나무 훼손)
FIRE = DB('p', 4, None, 'n', ti=3)          # 4:03 화염 피해 62~86 추가 (4티어) — 절사 카오스 결과, 카드에는 랜덤 옵션
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'diztoh-budget-crossbow-v2', 'recipe': 'diztoh-budget-crossbow-v2', 'cls': CLS, 'base': 'Siege Crossbow', 'ilvl': 82,
 'note': ('Diztoh 가성비 석궁(vk3pLFUov8U, 2026-11-13 G14 영상 전체 화면 대조) — 노멀 특출난 공성 쇠뇌(소켓 3, 아이템 레벨 82) '
          '→ 완벽한 진화·확장 + 소멸로 접두 물리 피해 %(2티어) → 상위 마모의 에센스(레어 + 물리 피해 추가) → 아스트리드의 창의성 '
          '→ 우측 결정화 + 완벽한 전투의 에센스(접미 잡옵을 지우고 공격 스킬 +3) → 우측 강령술 + 군왕의 징조 + 보존된 턱뼈 '
          '→ 상위 찬미 + 완벽한 엑잘(접두·접미 1개씩) → 심연의 메아리 + 공개(수류탄 두 번 발동) → 절사 + 완벽한 카오스(가장 낮은 잡옵 한 번). '
          '난이도 쉬움이라 에센셜 하나. 룬 교체·퀄리티·타락은 뺌.'),
 'params': {'v': {'kr': '흐름', 'en': 'Flow', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('영상 그대로: 엑잘과 절사 카오스는 결과 그대로', 'As the video: the exalt and the Whittling Chaos are kept as they come')}],
 'tags': {'ppct': {'gi': 8, 'tmax': 2}, 'flatE': {'gi': 39}, 'battle': {'gi': 53}, 'gren': {'gi': 30},
          'keep': {'anyOf': ['ppct', 'flatE', 'battle', 'gren']}},
 'require': {'all': [{'has': 'ppct'}, {'has': 'flatE'}, {'has': 'battle'}, {'has': 'gren'}, {'full': 'p'}, {'full': 's'}, {'desSide': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'sockets': 3},
}

N = []
A = lambda **kw: N.append(kw)
WS = {'whittleSafe': {'tag': 'keep', 'keepDes': True}}
# ---------------- 베이스템 완성 (영상 0:00~1:37) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='m1', start={'rar': 'normal', 'mods': []},
  label=K('노멀 특출난 공성 쇠뇌 구입 (소켓 3, 아이템 레벨 82)', 'Buy a normal exceptional Siege Crossbow (3 sockets, item level 82)'), item=[])
A(id='m1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 첫번째 옵션 — 접미가 붙으면 확장으로', 'First magic option: a suffix goes on to the Augmentation'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'if': {'any': [{'has': 'ppct'}, {'not': {'full': 'p'}}]}, 'to': 'm2', 'res': 'ok', 'label': K('물리 피해 % 또는 접미', '% physical or a suffix')},
         {'to': 'm1x', 'res': 'fail', 'label': K('다른 접두', 'Another prefix')}],
  ask=K('접두 자리가 비었거나 물리 피해 %?', 'Prefix free or % physical?'), item=[LEECH])
A(id='m1x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('옵션을 지워 노멀로', 'Annul back to normal'), edges=[{'to': 'm1'}])
A(id='m2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 물리 피해 %', '% physical damage prefix'), show=['ppct'],
  edges=[{'if': {'has': 'ppct'}, 'to': 'e1', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'm1x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
  ask=K('물리 피해 %?', '% physical?'), item=[PCT, LEECH])
A(id='e1', kind='act', group='prep', pos=[0, 3], act='essence', cur='Greater_Essence_of_Abrasion', ess='flatE', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 물리 피해 추가', 'Rare + added physical damage prefix'),
  showText=[{'s': 'p', 'kr': '물리 피해 (23—35)~(39—59) 추가 (제작 옵션)', 'en': 'Adds (23—35) to (39—59) Physical Damage (crafted)'}],
  edges=[{'to': 'ms'}], item=[PCT, FLAT, LEECH])
# ---------------- 옵션 추가 작업 (영상 1:45~4:03) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PCT, FLAT, LEECH])
A(id='k1', kind='act', group='main', pos=[0, 4.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'k2'}], item=[PCT, FLAT, LEECH, AST])
A(id='k2', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Perfect_Essence_of_Battle', ess='battle', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 공격 스킬 +3', 'Clear the junk suffix for +3 attack skills'),
  showText=[{'s': 's', 'kr': '모든 공격 스킬 레벨 +3 (제작 옵션)', 'en': '+3 to Level of all Attack Skills (crafted)'}],
  edges=[{'to': 'k3'}], item=[PCT, FLAT, ATK, AST])
A(id='k3', kind='act', group='main', pos=[0, 6.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Dextral_Necromancy', 'Omen_of_the_Liege'],
  label=K('훼손', 'Desecrate'), goal=K('접미 두번째 옵션(훼손, 아마나무)', 'Second suffix option (desecrated, Amanamu)'),
  showText=[{'s': 's', 'kr': '접미 훼손 옵션 (미공개, 아마나무)', 'en': 'Suffix desecration (unrevealed, Amanamu)'}],
  edges=[{'to': 'k4'}], item=[PCT, FLAT, ATK, UN, AST])
A(id='k4', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두·접미 옵션 1개씩 — 나오는 대로', 'One prefix and one suffix: keep what lands'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}, {'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'k5'}], item=[PCT, FLAT, ACC, ATK, UN, STR, AST])
A(id='k5', kind='act', group='main', pos=[0, 8.4], act='reveal', want='gren', omens=['Omen_of_Abyssal_Echoes'], label=K('공개', 'Reveal'),
  goal=K('접미 수류탄 두 번 발동 (아마나무, 훼손)', 'Grenade double activation suffix (Amanamu, desecrated)'), show=['gren'],
  edges=[{'to': 'k6', 'res': 'ok'}], item=[PCT, FLAT, ACC, ATK, GREN, STR, AST])
A(id='k6', kind='act', group='main', pos=[0, 9.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('가장 낮은 잡옵 다시 — 나오는 대로', 'Reroll the lowest junk option: keep what lands'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  skipIf={'not': WS}, skipTo='ok', skipHide=True,
  skipNote=K('가장 낮은 레벨 옵션이 잡옵이 아니면 건너뜀', 'Skipped when the lowest-level option is not junk'),
  edges=[{'to': 'ok', 'res': 'ok'}], item=[PCT, FLAT, FIRE, ATK, GREN, STR, AST])
A(id='ok', kind='done', group='main', pos=[0, 10.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['m1', 'm1x', 'm2'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'}]
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'ppct'}, {'tag': 'flatE', 'ess': True}, {'side': 'p', 'random': True},
            {'tag': 'battle', 'ess': True}, {'tag': 'gren', 'des': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
