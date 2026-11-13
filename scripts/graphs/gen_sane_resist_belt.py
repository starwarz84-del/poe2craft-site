# G12 2026-11-13: TheSaneExile 저항 허리띠(Zop328DR50Q, 6:11) 플로우차트 생성기 — 영상 성공 회차(룬 자물쇠 섬세한 허리띠) 한 줄
# 근거: scratchpad review/G12/sane-resist-belt-v2/timeline.md, frames/ (영상 0:00~6:11 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sane_resist_belt.py  → sane-resist-belt-v2.json (gen_batch5.py 끝에서도 자동 호출, 이 아이템 구간을 대신함)
# 상자 id는 옛 레시피(recipes_v5_sane-resist-belt.py, b1~b6)·옛 그래프(h1·b2~b5·b4x)와 겹치지 않게 t0~t4로 지음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sane-resist-belt-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차에 실제로 나온 옵션
LF = L('p', '생명력 최대치 +(150—174)', '+(150—174) to maximum Life', 'n', ['lf'])                       # 0:14 1티어 +161
LR = L('s', '번개 저항 +(36—40)%', '+(36—40)% to Lightning Resistance', 'n', ['lr'])                   # 0:14 2티어 +38%
CH = L('s', '카오스 저항 +(16—19)% (상위 폐허의 에센스)', '+(16—19)% to Chaos Resistance (Greater Essence of Ruin)', 'c', ['cres'])   # 1:40 +16%
UN = L('s', '훼손 옵션 (미공개, 울라만)', 'Desecrated (unrevealed, Ulaman)', 'n')                     # 1:40
UL = L('s', '번개 및 카오스 저항 +(13—17)%', '+(13—17)% to Lightning and Chaos Resistances', 'd', ['ul'])   # 2:40 공개 +13%
MN = L('p', '마나 최대치 +(35—54)', '+(35—54) to maximum Mana', 'j')                                     # 4:15 6티어 +46
FL = L('p', '플라스크 생명력 회복 속도 (5—10)% 증가', '(5—10)% increased Flask Life Recovery rate', 'j')   # 4:15 6티어 8%

g = {
 'id': 'sane-resist-belt-v2', 'recipe': 'sane-resist-belt-v2', 'cls': 'Belts', 'base': 'Fine Belt', 'ilvl': 81,
 'basePrice': {'Divine_Orb': 1},   # 4:10 자막 '벨트 베이스는 저 같은 경우 1 디바인'(매직 베이스 실시간 검색은 보통 0.5 div)
 'note': ('2026-11-13 G12 영상 전체(0:00~6:11) 화면 대조. 성공 회차 = 룬 자물쇠 섬세한 허리띠 한 줄: 생명력 1티어(+161) + 번개 저항 2티어(+38%) 매직 섬세한 허리띠(부적 칸 2개, 0:14 툴팁, 아이템 레벨 81 — 3:20 시세 도구) → '
          '상위 폐허의 에센스(1:30 툴팁) = 레어 + 접미 카오스 저항 +16% → 우측 강령술의 징조(1:35 툴팁) + 군주의 징조 + 보존된 빗장뼈(1:38 툴팁) = 접미 미공개 훼손(1:40, 채팅 두 징조 소모) → '
          '심연의 메아리의 징조 + 공개(2:40 선택지: 번개 및 카오스 저항 13% / 중독 지속시간 26% 감소 / 힘과 민첩 +13, 채팅 메아리 소모) = 번개 및 카오스 저항 +13%(3:06) → '
          '접두 두 자리 = 마나 최대치 +46(6티어) · 플라스크 생명력 회복 8%(6티어)(4:15 툴팁, 엑잘 장면은 3:52~3:54 편집으로 안 보임). '
          '접두 마무리는 사용자 확정(11-10) 상위 찬미의 징조 + 엑잘을 따르되 오브는 일반 엑잘티드 오브: 나온 두 옵션이 레벨 25·1이라 상위 엑잘티드 오브(최소 레벨 35)로는 붙을 수 없음. '
          '5:20~6:00 반지(자수정 반지, 메아리 없이 처치 시 생명력 회복이 붙음)는 꿀팁 후보. '
          '등급(정책 10장): 난이도 1 → 에센셜만. 영상에 반복이 없음(군주의 징조로 울라만 접미 4개 중 3개가 보이고 메아리로 한 번 더) — 공개는 결과 그대로(빛의 징조 없음, C17-3).'),
 'params': {'L': {'kr': '훼손 공개', 'en': 'Desecration reveal', 'values': {'0': K('결과 그대로', 'Keep whatever comes')}}},
 'strategies': [{'id': 'ess', 'params': {'L': 0}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0}, 'tier': 'ess',
   'desc': K('영상 그대로: 공개·엑잘 결과 그대로', 'As the video: keep the reveal and the exalt as they come')}],
 'tags': {
  'life': {'gi': 5, 'tmax': 1}, 'lres': {'gi': 3, 'tmax': 2}, 'lf': {'gi': 5}, 'lr': {'gi': 3}, 'cres': {'gi': 40}, 'ul': {'gi': 35},
 },
 'require': {'all': [{'has': 'life'}, {'has': 'lres'}, {'has': 'cres'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 't0',
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 0:14~1:30) ----------------
A(id='t0', kind='base', group='prep', pos=[0, 0], next='t1', start={'rar': 'magic', 'mods': ['life', 'lres']},
  label=K('생명력 + 번개 저항 매직 섬세한 허리띠 구입 (호신부 슬롯 2개)', 'Buy a magic Fine Belt with life + lightning resistance (two charm slots)'), item=[LF, LR])
A(id='t1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Ruin', ess='cres', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 카오스 저항', 'Rare + chaos resistance suffix'),
  showText=[{'s': 's', 'kr': '카오스 저항 (제작 옵션)', 'en': 'Chaos resistance (crafted)'}], edges=[{'to': 'ms'}], item=[LF, LR, CH])
# ---------------- 옵션 추가 작업 (영상 1:35~4:15) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='t2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[LF, LR, CH])
A(id='t2', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Dextral_Necromancy', 'Omen_of_the_Sovereign'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세번째 옵션(훼손, 울라만)', 'Third suffix (desecrated, Ulaman)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개, 울라만)', 'en': 'Desecrated (unrevealed, Ulaman)'}], edges=[{'to': 't3'}], item=[LF, LR, CH, UN])
A(id='t3', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='ul', label=K('공개', 'Reveal'),
  goal=K('접미 세번째 옵션(훼손) — 번개 및 카오스 저항', 'Third suffix (desecrated): lightning and chaos resistance'), show=['ul'],
  edges=[{'if': {'param': {'L': 0}}, 'to': 't4', 'res': 'ok'}], item=[LF, LR, UL, CH])
A(id='t4', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째·세번째 옵션 — 마나 최대치·플라스크 생명력 회복', 'Second and third prefixes: maximum mana, flask life recovery'),
  showText=[K('랜덤 옵션 2개', 'Two random options')], edges=[{'to': 'ok'}], item=[LF, MN, FL, LR, UL, CH])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'life'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'lres'}, {'tag': 'cres', 'ess': True}, {'side': 's', 'random': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
