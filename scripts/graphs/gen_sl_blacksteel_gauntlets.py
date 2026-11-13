# W13 2026-11-13: SL 딜용 장갑 — 룬벼림 검은강철 건틀릿 플로우차트(새 기준) 생성기
# 영상 J7J8Jo7ibvE(SL 게임연구소, 0.5.5 검은 화염파 세팅) 6:08~6:22 장갑 슬라이드. 영상 전체(0:00~12:51)를 화면으로 확인,
# 근거 scratchpad review/W13-blacksteel/timeline.md · frames/. 영상에는 실제 제작 장면이 없고 슬라이드의 '제작 방법' 14단계와 완성품 툴팁만 있음.
# 저장소 사본: scripts/graphs/에서 python3 gen_sl_blacksteel_gauntlets.py → scripts/graphs/sl-blacksteel-gauntlets-v2.json
#
# 완성품(6:08 툴팁): 아이템 레벨 82, 퀄리티 29%, 룬 수호 182(룬벼림), 룬 = 카틀라의 순흑 + 페누무스의 고갈의 룬(노란 칸).
#   접두: 피해를 주는 상태 이상의 피해 20(14—20)%만큼 가속 · 점화 강도 50(35—50)% · 플레이어가 유발하는 상태 이상의 강도 32(26—32)% — 셋 다 카틀라 1티어
#   접미: 저주 강도 29(22—29)% — 분열 색(금색), 카틀라 1티어 · 화염 저항 +44(41—45)% 1티어 · 위축 강도 26(25—35)% 카틀라 1티어
#   → 분열 옵션 = 접미 저주 강도. 슬라이드 10번 갈래('분열된 옵션이 접미라면 좌측 강령술 + 고대 갈비뼈로 접두 마저')를 따르고 13번 갈래는 꿀팁 후보.
# 슬라이드 14단계(6:12): 1 검은강철 건틀릿 82+ 홈 2개 흰템 → 2 바알 방어구 장인의 주입기 25퀄+(실패 시 1로) → 3 카틀라의 순흑 → 4 완벽 진화
#   → 5 완벽 확장 + 소멸 반복, 원하는 1티어 2개 → 6 완벽 제왕 or 상위 풍요의 에센스 → 7 보존된 갈비뼈 + 분열 오브(원하는 1티어 아무거나, 실패 시 1로)
#   → 8 (분열 제외 1줄 남기고) 카오스로 접두 1줄 → 9 좌측 찬미 + 완엑 접두 1줄(실패 시 소멸, 소멸도 실패 시 7로) → 10 (분열이 접미) 좌측 강령술 + 고대 갈비뼈 접두 마저
#   → 11 상위 찬미 + 완엑 원하는 접미 1줄(실패 시 우측 소멸 징조 2개) → 12 절사 + 우측 말소 + 완카 접미 1티어 → 13 (분열이 접두) 고대 갈비뼈 접미 마저 → 14 룬벼림.
# 영상에 없어 정한 것(내부 결정): 퀄리티는 옆 상자(비용 미포함, W1 같은 베이스와 같음), 제왕 = 완벽한 제왕의 오브(정책 2장), 접두 1티어가 분열되면 13번 갈래 = 같은 비용 가정,
#   분열 뒤 남은 옵션이 접두 1티어면 카오스 건너뜀, '소멸도 실패 시 7로' = 분열 + 옵션 1개 상태 → 카오스 단계, 공개가 빗나가면 빛의 징조 + 소멸(정책 10장 하이엔드),
#   심연의 메아리 없음(슬라이드에 없음), 룬벼림·페누무스의 고갈의 룬은 뺌(제작 옵션과 무관, 꿀팁 후보).
# P5 새 정책(2026-11-13 14:17): (B) 슬라이드 10번은 고대 갈비뼈로 '접두 마저'뿐이고 빗나갔을 때 다시 하는 말이 없음 → 공개 빛의 징조 반복을 빼고 결과 그대로(세 번째 접두 = 랜덤 옵션).
# C1 사용자 확정(2026-11-13 15:21 ①): 하이엔드는 영상에 없어도 훼손 공개 빛의 징조 반복 유지 → 위 (B) 되돌림. 세 번째 접두 = 남은 카틀라 접두 1티어(영상 완성품 상태 이상의 강도), 카드도 그 옵션.
#   (E) 베이스 가격이 영상에 없음 → 미정(옛 12 div는 MazBro 장갑 그래프 값을 빌린 것). (A) 슬라이드 5·8·9·11·12번 '원하는 1티어'는 카틀라 접두 묶음·접미 묶음(anyOf) 그대로, 화면은 툴팁 순서(shown).
# 접두 3개·접미 2개는 같은 카틀라 1티어 묶음이라 '남은 옵션 중 먼저 뜬 것'(정책 11장 붙는 순서 예외, K39). 화면 순서는 슬라이드 툴팁 순서 — 실제 붙은 순서는 영상에 없음.
# 등급: 난이도 극한 → 하이엔드만(정책 10장 C11). 카틀라의 순흑 옵션 가중치는 공개되지 않아 일반 티어 평균으로 추정(xroll).
import json, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/poe2craft-site/scripts/graphs/sl-blacksteel-gauntlets-v2.json'
CLS = 'Gloves_str_dex'
D = json.load(open(f'/home/claude/poe2craft-site/site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags, m='n', ti=0, suffix=None):   # DB 옵션 문구(1티어)
    t = D['groups'][gi]['t'][ti]; kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if suffix: kr += f' ({suffix[0]})'; en += f' ({suffix[1]})'
    return L(s, kr, en, m, tags)

KAT = L('r', '카틀라의 순흑', 'Katla’s Gloom', 'r')
FA = DB('p', 86, ['mp'])            # 피해를 주는 상태 이상의 피해 (14—20)%만큼 가속
IG = DB('p', 82, ['mp'])            # 점화 강도 (35—50)% 증가
AM = DB('p', 85, ['mp'], 'd')      # 플레이어가 유발하는 상태 이상의 강도 (26—32)% 증가 — 세 번째 접두(훼손), 영상 완성품
CUm = DB('s', 92, ['cu1'])           # 저주 강도 (22—29)% 증가
CU = DB('s', 92, ['cu1'], 'f')
FR = DB('s', 2, ['s2'])             # 화염 저항 +(41—45)%
WI = DB('s', 91, ['s2'])            # 위축 강도 (25—35)% 증가
MP = L('p', '카틀라 접두 1티어 중 먼저 뜬 것', 'Whichever T1 Katla prefix lands first', 'n', ['mp'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
FIRST = [K('피해 가속·점화 강도·상태 이상의 강도 1티어 중 먼저 뜬 것', 'Whichever of T1 faster ailments, ignite or ailment magnitude lands first')]
REST = [K('남은 옵션 중 먼저 뜬 것', 'Whichever of the rest lands first')]
RESTS = [K('위축 강도·화염 저항 1티어 중 먼저 뜬 것', 'Whichever of T1 withered or fire resistance lands first')]

g = {
 'id': 'sl-blacksteel-gauntlets-v2', 'recipe': 'sl-blacksteel-gauntlets-v2', 'cls': CLS, 'base': 'Blacksteel Gauntlets', 'ilvl': 82,
 'note': ('SL 딜용 장갑(J7J8Jo7ibvE 6:08~6:22 슬라이드, 2026-11-13 W13 영상 전체 화면 대조) — 검은강철 건틀릿(82+, 홈 2개) → 바알 방어구 장인의 주입기 25%+ → 카틀라의 순흑 '
          '→ 완벽한 진화·확장 + 소멸(매직 저주 강도 1티어 + 카틀라 접두 1티어) → 완벽한 제왕 → 보존된 갈비뼈 + 분열(저주 강도) → 분열 + 옵션 1개 → 카오스 오브(카틀라 접두 1티어) '
          '→ 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸) → 좌측 강령술 + 고대 갈비뼈 → 공개(남은 카틀라 접두, 빗나가면 빛의 징조) → 상위 찬미 + 완벽한 엑잘(접미, 빗나가면 우측 소멸의 징조 2개) '
          '→ 절사 + 우측 말소 + 완벽한 카오스(남은 접미 1티어). 하이엔드만(극한). 카틀라 옵션 가중치는 추정.'),
 'params': {'t': {'kr': '반복 목표', 'en': 'Loop target', 'values': {'1': K('1티어', 'T1')}}},
 'strategies': [{'id': 'high', 'params': {'t': 1}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'t': 1},
               'desc': K('영상 슬라이드: 카틀라 옵션·화염 저항 모두 1티어', 'Video slide: every Katla line and fire resistance at T1')}],
 'tags': {
   'am1': {'gi': 85, 'tmax': 1}, 'ig1': {'gi': 82, 'tmax': 1}, 'fa1': {'gi': 86, 'tmax': 1},
   'mp': {'anyOf': ['am1', 'ig1', 'fa1'], 'shown': ['fa1', 'ig1', 'am1'], 'label': K('상태 이상의 강도·점화 강도·피해 가속 1티어', 'T1 ailment magnitude, ignite magnitude or faster ailments')},
   'cu1': {'gi': 92, 'tmax': 1}, 'wi1': {'gi': 91, 'tmax': 1}, 'fr1': {'gi': 2, 'tmax': 1},
   's2': {'anyOf': ['wi1', 'fr1'], 'shown': ['fr1', 'wi1'], 'label': K('위축 강도·화염 저항 1티어', 'T1 withered magnitude or fire resistance')},
   'magicGood': {'anyOf': ['mp', 'cu1'], 'label': K('카틀라 접두·저주 강도 1티어', 'T1 Katla prefix or curse magnitude')},
 },
 'conds': {'magicDone': {'all': [{'has': 'mp'}, {'has': 'cu1'}]}},
 'require': {'all': [{'has': 'cu1'}, {'count': {'tag': 'mp', 'min': 3}}, {'count': {'tag': 's2', 'min': 2}}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 2]}, {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h1', 'xsub': ["Katla's Gloom"], 'xroll': True,
 'finalItem': {'quality': 29, 'sockets': 2, 'exceptional': True},
}

N = []
A = lambda **d: N.append(d)
I_M1 = [KAT, CUm]; I_M2 = [KAT, MP, CUm]; I_R = [KAT, MP, J('p'), CUm]; I_D = I_R + [UN('s')]
I_F = [KAT, MP, J('p'), CU, UN('s')]; I0 = [KAT, J('p'), CU]
A(id='h1', kind='base', group='prep', pos=[0, 0], next='pk', start={'rar': 'normal', 'mods': [], 'quality': 29},
  label=K('특출난 검은강철 건틀릿 구입 (노멀, 아이템 레벨 82 이상, 룬 소켓 2개)', 'Buy exceptional Blacksteel Gauntlets (normal, item level 82+, two sockets)'), item=[])
A(id='hq', kind='side', group='prep', pos=[1, 0.5], attach=['h1', 'pk'], cur='Vaal_Armourers_Infuser',
  goal=K('퀄리티 25% 이상, 비용 미포함', 'Quality 25%+, not costed'), label=K('퀄리티', 'Quality'))
A(id='pk', kind='act', group='prep', pos=[0, 1], act='rune', rune=K('카틀라의 순흑', 'Katla’s Gloom'),
  goal=K('카틀라의 순흑 장착', 'Socket Katla’s Gloom'), showText=[K('카틀라 옵션이 붙을 수 있음', 'Katla lines can roll')], label=K('룬', 'Rune'),
  edges=[{'to': 'm1'}], item=[KAT])
A(id='m1', kind='act', group='prep', pos=[0, 2], act='transmute', cur='Perfect_Orb_of_Transmutation',
  label=K('매직 첫 번째 옵션', 'First magic option'), goal=K('접미 저주 강도 1티어', 'T1 curse magnitude suffix'), show=['cu1'],
  edges=[{'if': {'added': 'magicGood'}, 'to': 'm2', 'res': 'ok', 'label': K('성공', 'hit')}, {'to': 'm1x', 'res': 'fail', 'label': K('빗나감', 'miss')}], item=I_M1)
A(id='m1x', kind='cleanup', group='prep', pos=[1, 2], keep=[], maxJunk=0, label=K('소멸의 오브 사용', 'Use an Orb of Annulment'), goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), edges=[{'to': 'm2'}])
A(id='m2', kind='act', group='prep', pos=[0, 3], act='augment', cur='Perfect_Orb_of_Augmentation',
  label=K('매직 두 번째 옵션', 'Second magic option'), goal=K('접두 카틀라의 순흑 옵션 1티어', 'T1 Katla’s Gloom prefix'), showText=FIRST,
  edges=[{'if': {'ref': 'magicDone'}, 'to': 'm3', 'res': 'ok', 'label': K('성공', 'hit')}, {'to': 'm2x', 'res': 'fail', 'label': K('빗나감', 'miss')}], item=I_M2)
A(id='m2x', kind='cleanup', group='prep', pos=[1, 3], keep=['magicGood'], maxJunk=0, label=K('소멸의 오브 사용', 'Use an Orb of Annulment'), goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  edges=[{'lost': 'magicGood', 'to': 'm2y', 'res': 'fail', 'label': K('원하는 옵션 지워짐', 'wanted option gone')}, {'to': 'm2', 'res': 'ok', 'label': K('잡옵 지워짐', 'junk gone')}])
A(id='m2y', kind='cleanup', group='prep', pos=[2, 3], keep=[], maxJunk=0, label=K('소멸의 오브 사용', 'Use an Orb of Annulment'), goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  target=K('남은 옵션 지우기', 'Remove the remaining option'), edges=[{'to': 'm2'}])
A(id='m3', kind='act', group='prep', pos=[0, 4], act='regal', cur='Perfect_Regal_Orb', label=K('레어', 'Rare'), goal=K('분열하기 위해 레어로', 'Make it rare for the fracture'),
  showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'm4'}], item=I_R)
A(id='m4', kind='act', group='prep', pos=[0, 5], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'm5'}], item=I_D)
A(id='m5', kind='act', group='prep', pos=[0, 6], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'), showText=[K('저주 강도가 분열되면 성공', 'Success when the curse magnitude fractures')],
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'cu1'}, 'to': 'm6', 'res': 'ok', 'label': K('저주 강도 분열', 'curse fractured')},
         {'if': {'fractured': 'mp'}, 'to': 'xs', 'res': 'ok', 'dash': True, 'label': K('카틀라 접두 분열', 'Katla prefix fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('잡옵 분열', 'junk fractured')}], item=I_F)
A(id='xs', kind='exit', group='prep', pos=[1, 6], simTo='m6', swapFracture='cu1', variant='ok', label=K('카틀라 접두 분열', 'Katla prefix fractured'),
  note=K('슬라이드 13번 갈래: 접두를 먼저 채우고 고대 갈비뼈로 접미 마저 (비용은 같다고 가정)', 'Slide branch 13: prefixes first, then an Ancient Rib for the last suffix (assumed to cost the same)'))
A(id='xj', kind='exit', group='prep', pos=[1, 7], simTo='h1', variant='fail', label=K('잡옵 분열 — 새 베이스', 'Junk fractured: new base'),
  note=K('제왕의 오브로 붙은 잡옵이 분열되면 새 베이스로 처음부터', 'If the regal junk fractures, start over on a new base'))
A(id='m6', kind='cleanup', group='prep', pos=[0, 8], keep=[], maxJunk=1, label=K('소멸의 오브 사용', 'Use an Orb of Annulment'), goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=I0)
A(id='ms', kind='mark', group='main', pos=[0, 9], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=I0)
A(id='k1', kind='act', group='main', pos=[0, 10], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'), goal=K('접두 첫 번째 옵션', 'First prefix'),
  show=['mp'], skipIf={'has': 'mp'}, skipTo='k2', skipNote=K('남은 옵션이 카틀라 접두 1티어면 건너뜀', 'Skip if the option left is a T1 Katla prefix'),
  edges=[{'if': {'has': 'mp'}, 'to': 'k2', 'res': 'ok'}, {'to': 'k1', 'res': 'fail'}], item=[KAT, FA, CU])
A(id='k2', kind='act', group='main', pos=[0, 11], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), show=['mp'],
  edges=[{'if': {'count': {'tag': 'mp', 'min': 2}}, 'to': 'k5', 'res': 'ok'}, {'to': 'k2x', 'res': 'fail', 'label': K('빗나감 — 소멸의 오브', 'Miss: Orb of Annulment')}], item=[KAT, FA, IG, CU])
A(id='k2x', kind='act', group='main', pos=[1, 11], act='annul', cur='Orb_of_Annulment', omens=[], label=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'), target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'if': {'has': 'mp'}, 'to': 'k2', 'res': 'ok', 'label': K('빗나간 접두 지워짐 — 다시 엑잘', 'Missed prefix gone: exalt again')},
         {'to': 'k1', 'res': 'fail', 'label': K('카틀라 접두가 지워짐 — 카오스부터', 'Katla prefix gone: back to Chaos')}])
A(id='k5', kind='act', group='main', pos=[0, 12], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[K('훼손 옵션 (미공개)', 'Desecrated (unrevealed)')], edges=[{'to': 'k6'}], item=[KAT, FA, IG, UN('p'), CU])
A(id='k6', kind='act', group='main', pos=[0, 13], act='reveal', label=K('공개', 'Reveal'), goal=K('훼손 옵션 확인', 'Reveal the desecrated modifier'),
  want='mp', show=['mp'],
  edges=[{'if': {'added': 'mp'}, 'to': 'k3', 'res': 'ok'}, {'to': 'k6x', 'res': 'fail'}], item=[KAT, FA, IG, AM, CU])
A(id='k6x', kind='act', group='main', pos=[1, 13], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'k5', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='k3', kind='act', group='main', pos=[0, 14], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션', 'Second and third suffixes'), show=['s2'],
  edges=[{'if': {'has': 's2'}, 'to': 'k4', 'res': 'ok'}, {'to': 'k3x', 'res': 'fail', 'label': K('빗나감 — 우측 소멸의 징조', 'Miss: Omen of Dextral Annulment')}],
  item=[KAT, FA, IG, AM, CU, FR, L('s', '랜덤 옵션 1개', 'One random option', 'j')])
A(id='k3x', kind='act', group='main', pos=[1, 14], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'), target=K('빗나간 접미 2개 지우기', 'Remove both missed suffixes'),
  edges=[{'if': {'sideLt': {'side': 's', 'n': 2}}, 'to': 'k3', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}, {'to': 'k3x', 'res': 'fail', 'hide': True}])
A(id='k4', kind='act', group='main', pos=[0, 15], act='chaos', cur='Perfect_Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 세 번째 옵션', 'Third suffix'), show=['s2'],
  trim={'side': 's', 'keep': 's2'}, skipIf={'count': {'tag': 's2', 'min': 2}}, skipTo='ok', skipNote=K('위축 강도·화염 저항이 모두 있으면 건너뜀', 'Skip if both withered and fire resistance are on'),
  edges=[{'if': {'count': {'tag': 's2', 'min': 2}}, 'to': 'ok', 'res': 'ok'}, {'to': 'k4', 'res': 'fail'}], item=[KAT, FA, IG, AM, CU, FR, WI])
A(id='ok', kind='done', group='main', pos=[0, 16], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
  {'id': 'L0', 'nodes': ['m1', 'm1x', 'm2', 'm2x', 'm2y'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'},
  {'id': 'L1', 'nodes': ['k5', 'k6', 'k6x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]
g['finals'] = [{'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
                'lines': [{'tag': 'mp'}, {'tag': 'mp'}, {'tag': 'mp', 'des': True}, {'tag': 'cu1', 'fr': True}, {'tag': 's2'}, {'tag': 's2'}]}]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
