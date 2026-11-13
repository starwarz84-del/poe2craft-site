# G14 2026-11-13: Diztoh 가성비 양손 둔기(ITbefGq6V18, 4:59) 플로우차트 생성기 — 영상 성공 회차 한 줄(영상은 둔기 하나)
# 근거: scratchpad review/G14/diztoh-budget-mace-v2/timeline.md · 캡처(영상 0:00~4:59 화면 대조, 자막 전체)
# 실행: cd scripts/graphs && python3 gen_diztoh_budget_mace.py → diztoh-budget-mace-v2.json (gen_batch5.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 성공 회차(화면): 0:12 거래소 특출난 거대한 대망치(소켓 3) 노멀 매물 3 엑잘티드 오브 → 0:25 완벽한 진화의 오브(630 → 629, 0:41)
#   → 진화·완벽한 확장의 오브·소멸의 오브로 매직 옵션 다시(0:27 치명타, 0:31 정확도 + 치명타, 0:33 노멀로 되돌림, 0:35·0:40 번개 + 처치 시 회복)
#   → 0:45 접미 정확도 + 시야 반경 → 완벽한 확장 → 0:48 접두 물리 % + 정확도 복합 2티어(아이템 레벨 84)
#   → 0:57 정수 탭 상위 마모의 에센스(자막) → 1:00 레어 + 물리 피해 추가 3티어
#   → 1:04 좌측 강령술의 징조, 1:08 검은 피의 징조 → 1:19 채팅 '두 징조 소모' + 미공개 훼손 접두(뼈 장면은 편집으로 없음)
#   → 1:41 아스트리드의 창의성 → 1:45 장착(제작 옵션 하나 더) → 1:54 우측 결정화의 징조 + 2:06 완벽한 전투의 에센스 → 2:12 접미 정확도 + 시야 반경을 지우고 공격 스킬 +3
#   → 2:33 영혼의 우물: 쿠르갈 3개(물리 피해 154%·공격 속도 15% 감소 / 강화 공격 피해 / 냉기 관통) 중 물리 피해
#   → 2:52 완벽한 엑잘티드 오브 + 상위 찬미의 징조(자막, 두 옵션이 한 번에 붙음) → 3:19 접미 기절 지속시간 · 처치 시 마나(결과 그대로)
#   → 3:32~4:10 우측 소멸의 징조로 접미를 바꾸는 시연(꿀팁 후보, 플로우차트에서 뺌) → 4:28 상위 철 룬(취향, 뺌).
# 내부 결정: 난이도 1(쉬움) → 에센셜만. 매직 단계 반복(완벽한 진화·확장 + 소멸)은 싸게 돌리는 준비 구간이라 접지 않고 준비 구역에 둠.
#   완벽한 진화·확장(최소 레벨 70)이라 복합은 1~2티어만 나옴(영상 2티어). 공개는 검은 피의 징조로 쿠르갈 접두 3개가 모두 나와 반복 없음.
#   뼈 종류는 화면에 없어 옛 기록대로 보존된 턱뼈. 아스트리드의 창의성은 결정화 에센스 전에 장착(룬 상자 rune 필드 — 옛 c1check 위반 d7 고침).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-budget-mace-v2.json'
CLS = 'Two_Hand_Maces'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

HYB = DB('p', 8, ['hyb'], 'n', ti=1)        # 0:48 물리 피해 70% + 정확도 163 (2티어)
ACC = DB('s', 19, None, 'j', ti=0)          # 0:45 정확도 41 + 시야 반경 15% (잡옵)
FLAT = DB('p', 39, ['flat'], 'c', ti=0)     # 1:00 물리 피해 34~52 추가 = 상위 마모의 에센스
UN = L('p', '접두 훼손 옵션 (미공개, 쿠르갈)', 'Prefix desecration (unrevealed, Kurgal)', 'u')
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
ATK = DB('s', 53, ['battle'], 'c', ti=0)    # 2:12 모든 공격 스킬 레벨 +3 = 완벽한 전투의 에센스
KP = DB('p', 26, ['kp'], 'd', ti=0)         # 2:33 물리 피해 154%, 공격 속도 15% 감소 (쿠르갈 훼손)
STUN = DB('s', 20, None, 'n', ti=1)         # 3:19 기절 지속시간 26% (2티어) — 엑잘 결과, 카드에는 랜덤 옵션
MANA = DB('s', 13, None, 'n', ti=1)         # 3:19 처치 시 마나 34 (2티어) — 엑잘 결과, 카드에는 랜덤 옵션
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'diztoh-budget-mace-v2', 'recipe': 'diztoh-budget-mace-v2', 'cls': CLS, 'base': 'Massive Greathammer', 'ilvl': 84,
 'basePrice': {'Exalted_Orb': 3},   # 0:12 거래소 특출난 거대한 대망치 노멀 매물 3 엑잘티드 오브(산 장면은 편집)
 'note': ('Diztoh 가성비 양손 둔기(ITbefGq6V18, 2026-11-13 G14 영상 전체 화면 대조) — 노멀 특출난 거대한 대망치(소켓 3, 아이템 레벨 84) '
          '→ 완벽한 진화·확장 + 소멸로 접두 물리 복합(2티어) → 상위 마모의 에센스(레어 + 물리 피해 추가) → 좌측 강령술 + 검은 피의 징조 + 보존된 턱뼈 '
          '→ 아스트리드의 창의성 → 우측 결정화 + 완벽한 전투의 에센스(접미 잡옵을 지우고 공격 스킬 +3) → 공개(쿠르갈 물리 피해) '
          '→ 상위 찬미 + 완벽한 엑잘(접미 2개 결과 그대로). 난이도 쉬움이라 에센셜 하나. 우측 소멸 시연·철 룬은 뺌.'),
 'params': {'v': {'kr': '흐름', 'en': 'Flow', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('영상 그대로: 마지막 엑잘은 결과 그대로', 'As the video: the last exalt is kept as it comes')}],
 'tags': {'hyb': {'gi': 8, 'tmax': 2}, 'flat': {'gi': 39}, 'kp': {'gi': 26}, 'battle': {'gi': 53}},
 'require': {'all': [{'has': 'hyb'}, {'has': 'flat'}, {'has': 'kp'}, {'has': 'battle'}, {'full': 'p'}, {'full': 's'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'sockets': 3},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 0:00~1:00) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='m1', start={'rar': 'normal', 'mods': []},
  label=K('노멀 특출난 거대한 대망치 구입 (소켓 3, 아이템 레벨 84)', 'Buy a normal exceptional Massive Greathammer (3 sockets, item level 84)'), item=[])
A(id='m1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 첫번째 옵션 — 접미가 붙으면 확장으로', 'First magic option: a suffix goes on to the Augmentation'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'if': {'any': [{'has': 'hyb'}, {'not': {'full': 'p'}}]}, 'to': 'm2', 'res': 'ok', 'label': K('접두 복합 또는 접미', 'Hybrid prefix or a suffix')},
         {'to': 'm1x', 'res': 'fail', 'label': K('다른 접두', 'Another prefix')}],
  ask=K('접두 자리가 비었거나 복합?', 'Prefix free or hybrid?'), item=[ACC])
A(id='m1x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('옵션을 지워 노멀로', 'Annul back to normal'), edges=[{'to': 'm1'}])
A(id='m2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 물리 % + 정확도 복합', 'Hybrid % physical + accuracy prefix'), show=['hyb'],
  edges=[{'if': {'has': 'hyb'}, 'to': 'e1', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'm1x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
  ask=K('복합?', 'Hybrid?'), item=[HYB, ACC])
A(id='e1', kind='act', group='prep', pos=[0, 3], act='essence', cur='Greater_Essence_of_Abrasion', ess='flat', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 물리 피해 추가', 'Rare + added physical damage prefix'),
  showText=[{'s': 'p', 'kr': '물리 피해 (23—35)~(39—59) 추가 (제작 옵션)', 'en': 'Adds (23—35) to (39—59) Physical Damage (crafted)'}],
  edges=[{'to': 'ms'}], item=[HYB, FLAT, ACC])
# ---------------- 옵션 추가 작업 (영상 1:04~3:19) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[HYB, FLAT, ACC])
A(id='k1', kind='act', group='main', pos=[0, 4.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy', 'Omen_of_the_Blackblooded'],
  label=K('훼손', 'Desecrate'), goal=K('접두 세번째 옵션(훼손, 쿠르갈)', 'Third prefix option (desecrated, Kurgal)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개, 공개 3개 모두 쿠르갈)', 'en': 'Prefix desecration (unrevealed, all three options Kurgal)'}],
  edges=[{'to': 'k2'}], item=[HYB, FLAT, UN, ACC])
A(id='k2', kind='act', group='main', pos=[0, 5.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'k3'}], item=[HYB, FLAT, UN, ACC, AST])
A(id='k3', kind='act', group='main', pos=[0, 6.4], act='essence', cur='Perfect_Essence_of_Battle', ess='battle', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 공격 스킬 +3', 'Clear the junk suffix for +3 attack skills'),
  showText=[{'s': 's', 'kr': '모든 공격 스킬 레벨 +3 (제작 옵션)', 'en': '+3 to Level of all Attack Skills (crafted)'}],
  edges=[{'to': 'k4'}], item=[HYB, FLAT, UN, ATK, AST])
A(id='k4', kind='act', group='main', pos=[0, 7.4], act='reveal', want='kp', label=K('공개', 'Reveal'),
  goal=K('접두 물리 피해 증가, 공격 속도 감소 (훼손)', '% physical with reduced attack speed prefix (desecrated)'), show=['kp'],
  edges=[{'to': 'k5', 'res': 'ok'}], item=[HYB, FLAT, KP, ATK, AST])
A(id='k5', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두번째·세번째 옵션 — 나오는 대로', 'Second and third suffix options: keep what lands'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'ok'}], item=[HYB, FLAT, KP, ATK, STUN, MANA, AST])
A(id='ok', kind='done', group='main', pos=[0, 9.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['m1', 'm1x', 'm2'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'}]
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'hyb'}, {'tag': 'flat', 'ess': True}, {'tag': 'kp', 'des': True},
            {'tag': 'battle', 'ess': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
