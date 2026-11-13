# G13 2026-11-13: 라그나 아샷 활(m0eHw6nq24Q, 6:34) 플로우차트 생성기 — 영상 성공 회차 한 줄(영상은 활 하나)
# 근거: scratchpad review/G13/ragna-ashot-bow-v2/timeline.md · 캡처 19장(영상 0:00~6:34 화면 대조, 자막 전체)
# 실행: cd scripts/graphs && python3 gen_ragna_ashot_bow.py → ragna-ashot-bow-v2.json (gen_batch5.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 성공 회차(화면): 2:12 매직 전쟁광 활(물리 피해 178% 1티어 + 접미 정확도·시야 반경 잡옵, 아이템 레벨 82)
#   → 2:13 상위 마모의 에센스 → 2:26 레어 + 물리 피해 추가 3티어(제작), 퀄리티 20%(퀄리티를 올리는 장면은 편집, 툴팁 변화로 확인)
#   → 2:32 상위 엑잘티드 오브(최소 속성 레벨 35) + 2:48 좌측 찬미의 징조 소모(채팅) → 2:50 접두 물리 % + 정확도 복합 4티어
#   → 4:10 군왕의 징조(툴팁) + 보존된 턱뼈(자막, 뼈 툴팁 장면 없음) → 4:22 미공개 훼손 접미
#   → 4:52 상위 엑잘티드 오브(인벤토리 II 아이콘) → 4:59 접미 생명력 흡수 1티어
#   → 5:08 영혼의 우물 공개: 아마나무 접미 3개(공격 속도 + 반려수 공격 속도 / 관통 / 정신력 점유 효율) 중 공격 속도 14% 선택.
# 내부 결정: 등급은 난이도 1(쉬움, difficulty.py) → 에센셜만(정책 10장). 영상에 반복 구간이 없어 에센셜 = 영상 흐름 그대로.
#   엑잘 두 번은 나오는 대로(완성 카드 랜덤 옵션), 공개는 군왕의 징조라 아마나무 3개가 모두 나와 반복 없음.
#   소켓의 룬(물리 피해 36% 증가)은 제작과 관계없어 뺌(정책 9장). 퀄리티 20%는 시작 상태(start.quality).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/ragna-ashot-bow-v2.json'
CLS = 'Bows'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags=None, m='n', ti=0):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

PCT = DB('p', 7, ['pct'])                  # 2:26 물리 피해 178% (170—179) 1티어
FLAT = DB('p', 39, ['flat'], 'c')          # 2:26 물리 피해 추가 (16—24)~(28—42) 3티어 = 상위 마모의 에센스
HYB = DB('p', 8, None, 'j', ti=3)          # 2:50 물리 % + 정확도 복합 4티어 — 엑잘 결과, 카드에는 랜덤 옵션
ACL = DB('s', 19, None, 'j')               # 2:26 정확도 + 시야 반경(베이스 접미 잡옵)
LEECH = DB('s', 10, None, 'j')             # 4:59 생명력 흡수 1티어 — 엑잘 결과, 카드에는 랜덤 옵션
AS = DB('s', 29, ['as'], 'd')              # 5:08 공격 속도 + 반려수 공격 속도(아마나무, 훼손)
UN = L('s', '접미 훼손 옵션 (미공개)', 'Suffix desecration (unrevealed)', 'u')

g = {
 'id': 'ragna-ashot-bow-v2', 'recipe': 'ragna-ashot-bow-v2', 'cls': CLS, 'base': 'Warmonger Bow', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 10},   # 1:30 자막 '8딥, 10딥, 15딥 정도'(물리 % 매직 활 시세), 1:40 화면 매물은 5티어 절멸자 활 8 div — 가운데 10 div
 'note': ('라그나 아샷 활(m0eHw6nq24Q, 2026-11-13 G13 영상 전체 화면 대조) — 물리 피해 % 1티어 매직 전쟁광 활(아이템 레벨 82, 퀄리티 20%) → 상위 마모의 에센스(레어 + 물리 피해 추가) '
          '→ 좌측 찬미의 징조 + 상위 엑잘티드 오브(접두 나오는 대로) → 군왕의 징조 + 보존된 턱뼈(접미 아마나무 훼손) → 상위 엑잘티드 오브(접미 나오는 대로) '
          '→ 영혼의 우물 공개: 아마나무 3개가 모두 나와 공격 속도 + 반려수 공격 속도. 영상에 반복이 없어 에센셜(난이도 쉬움) 하나. 소켓 룬은 뺌.'),
 'params': {'v': {'kr': '흐름', 'en': 'Flow', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('영상 그대로: 엑잘 두 번은 나오는 대로, 공개는 아마나무 공격 속도', 'As the video: both exalts kept, the reveal takes Amanamu attack speed')}],
 'tags': {'pct': {'gi': 7, 'tmax': 1}, 'flat': {'gi': 39}, 'as': {'gi': 29}},
 'require': {'all': [{'has': 'pct'}, {'has': 'flat'}, {'full': 'p'}, {'full': 's'}, {'desSide': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 1:30~2:26) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='e1', start={'rar': 'magic', 'mods': [{'tag': 'pct'}, {'junk': 's'}], 'quality': 20},
  label=K('물리 피해 % 1티어 매직 전쟁광 활 구입 (아이템 레벨 82, 퀄리티 20%)', 'Buy a magic Warmonger Bow with T1 % physical damage (item level 82, quality 20%)'),
  item=[PCT, ACL])
A(id='e1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Abrasion', ess='flat', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 물리 피해 추가', 'Rare + flat physical damage prefix'),
  showText=[{'s': 'p', 'kr': '물리 피해 (16—24)~(28—42) 추가 (제작 옵션)', 'en': 'Adds (16—24) to (28—42) Physical Damage (crafted)'}],
  edges=[{'to': 'ms'}], item=[PCT, FLAT, ACL])
# ---------------- 옵션 추가 작업 (영상 2:30~5:10) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='x1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PCT, FLAT, ACL])
A(id='x1', kind='act', group='main', pos=[0, 2.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세번째 옵션 — 나오는 대로', 'Third prefix: keep what lands'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'd1'}], item=[PCT, HYB, FLAT, ACL])
A(id='d1', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_the_Liege'], label=K('훼손', 'Desecrate'),
  goal=K('접미 두번째 옵션(아마나무 훼손)', 'Second suffix (Amanamu desecration)'),
  showText=[{'s': 's', 'kr': '아마나무 훼손 옵션 (미공개)', 'en': 'Amanamu desecration (unrevealed)'}],
  edges=[{'to': 'x2'}], item=[PCT, HYB, FLAT, ACL, UN])
A(id='x2', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 세번째 옵션 — 나오는 대로', 'Third suffix: keep what lands'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'v1'}], item=[PCT, HYB, FLAT, ACL, UN, LEECH])
A(id='v1', kind='act', group='main', pos=[0, 5.4], act='reveal', want='as', label=K('공개', 'Reveal'),
  goal=K('접미 공격 속도 + 반려수 공격 속도 (아마나무, 훼손)', 'Attack speed + companion attack speed suffix (Amanamu, desecrated)'), show=['as'],
  edges=[{'to': 'ok'}], item=[PCT, HYB, FLAT, ACL, AS, LEECH])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'pct'}, {'tag': 'flat', 'ess': True}, {'side': 'p', 'random': True},
            {'tag': 'as', 'des': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
