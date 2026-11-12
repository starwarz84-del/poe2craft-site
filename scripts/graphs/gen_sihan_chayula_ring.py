# W32 2026-11-13: 시한 차율라 반지(GgD_vxKgNsw, 5:03) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W32-sihan-ring/timeline.md, frames/ (영상 0:00~5:03 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_chayula_ring.py  → sihan-chayula-ring-v2.json (gen_batch22.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-chayula-ring-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(3:18~4:34)에 실제로 나온 옵션
FR = L('s', '잔류물을 (44—51)% 더 먼 곳에서 획득 가능 (분열)', 'Remnants can be collected from (44—51)% further away (fractured)', 'f', ['far'])
MQ = L('p', '최대 퀄리티 +20% (균열의 에센스)', '+20% to Maximum Quality (Essence of the Breach)', 'c', ['maxq'])
RS = L('s', '모든 원소 저항 +(12—14)%', '+(12—14)% to all Elemental Resistances', 'n', ['res'])
CHD = L('p', '카오스 피해 (27—30)% 증가', '(27—30)% increased Chaos Damage', 'n', ['chaos'])
LIFE = L('p', '생명력 최대치 +(100—119)', '+(100—119) to maximum Life', 'n')
EF = L('p', '플레이어가 생성하는 잔류물의 효과 (8—15)% 증가 (훼손)', 'Remnants you create have (8—15)% increased effect (desecrated)', 'd', ['eff'])
MK = L('s', '처치한 적 하나당 마나 (21—27) 획득', 'Gain (21—27) Mana per enemy killed', 'n')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'sihan-chayula-ring-v2', 'recipe': 'sihan-chayula-ring-v2', 'cls': 'Rings', 'base': 'Breach Ring', 'ilvl': 81, 'basePrice': {},
 'note': ('2026-11-13 W32 영상 전체 화면 대조. 성공 회차 한 줄: 균열 반지(부패하는 감개, 아이템 레벨 81, 잔류물 거리 분열 + 마나 최대치 잡옵, 1:38) → '
          '균열의 에센스로 최대 퀄리티 +20%(2:07) → 차율라의 기폭제 60개로 카오스 퀄리티 60%(1:56 구입, 2:02~2:08) → '
          '카오스 오브로 모든 원소 저항·카오스 피해 중 먼저 뜬 것(성공 회차 3:18~3:25 모든 원소 저항 +12 2티어) → '
          '상위 찬미 + 좌측 찬미 + 완벽한 엑잘로 카오스 피해 1티어·생명력 1티어(3:28, 채팅 소모 메시지 3:32) → '
          '좌측 강령술 + 군왕의 징조 + 보존된 빗장뼈로 접두 훼손(3:37~3:54) → 완벽한 엑잘로 마지막 옵션(처치 시 마나, 4:01) → '
          '심연의 메아리의 징조로 공개, 잔류물 효과 14%(4:27~4:34). '
          '첫 회차(2:32~3:15): 카오스 피해가 먼저 떴을 때 상위 찬미 + 우측 찬미(2:39), 빗나가면 소멸의 오브(2:48·3:03), 자리가 한쪽에 하나면 상위 찬미만(2:58). '
          '등급(영상 4:30 기준 = 카오스 피해 1티어·모든 원소 저항 2티어 이상): 하이엔드 = 영상 기준, 밸런스 = 카오스 피해 1~2티어·모든 원소 저항 1~3티어. '
          '나머지 두 옵션은 영상대로 랜덤 옵션(1:10 "나머지 두 줄은 랜덤").'),
 'params': {
  'rT': {'kr': '모든 원소 저항', 'en': 'All resistances', 'values': {'2': K('1~2티어', 'T1–2'), '3': K('1~3티어', 'T1–3')}},
  'cT': {'kr': '카오스 피해', 'en': 'Chaos damage', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
 },
 'strategies': [{'id': 'high', 'params': {'rT': 2, 'cT': 1}}, {'id': 'bal', 'params': {'rT': 3, 'cT': 2}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'rT': 3, 'cT': 2}, 'tier': 'bal',
   'desc': K('카오스 피해 1~2티어, 모든 원소 저항 1~3티어', 'Chaos damage T1–2, all resistances T1–3')},
  {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'rT': 2, 'cT': 1}, 'tier': 'high',
   'desc': K('영상: 카오스 피해 1티어, 모든 원소 저항 1~2티어', 'Video: chaos damage T1, all resistances T1–2')}],
 'tags': {
  'far': {'gi': 106}, 'maxq': {'gi': 71}, 'eff': {'gi': 37},
  'res': {'gi': 7, 'tmax': '$rT'}, 'resH': {'gi': 7, 'tmax': 2}, 'resB': {'gi': 7, 'tmax': 3},
  'chaos': {'gi': 33, 'tmax': '$cT'}, 'chaosH': {'gi': 33, 'tmax': 1}, 'chaosB': {'gi': 33, 'tmax': 2},
  'RC': {'anyOf': ['res', 'chaos'], 'label': K('모든 원소 저항·카오스 피해', 'All resistances or chaos damage')},
 },
 'require': {'all': [{'has': 'far'}, {'has': 'res'}, {'has': 'chaos'}, {'has': 'eff'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [
  {'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
   'lines': [{'tag': 'chaosH'}, {'side': 'p', 'random': True}, {'tag': 'eff', 'des': True},
             {'tag': 'far', 'fr': True}, {'tag': 'resH'}, {'side': 's', 'random': True}]},
  {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'chaosB'}, {'side': 'p', 'random': True}, {'tag': 'eff', 'des': True},
             {'tag': 'far', 'fr': True}, {'tag': 'resB'}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 60, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# 매 단계 아이템을 다시 봄(영상 2:32~3:32): 둘 다 있고 접두 자리가 남으면 훼손, 하나만 있으면 그쪽 빈자리에 맞는 엑잘,
# 자리가 없으면 소멸의 오브, 둘 다 없으면 분열 + 옵션 1개까지 정리한 뒤 카오스
R, C = {'has': 'res'}, {'has': 'chaos'}
sl = lambda sd, n: {'sideLt': {'side': sd, 'n': n}}
BOTH = {'all': [R, C]}
ROOM2 = {'any': [sl('p', 2), sl('s', 2), {'all': [sl('p', 3), sl('s', 3)]}]}   # 빈자리 2개 이상
BARE = {'any': [{'all': [sl('p', 1), sl('s', 3)]}, {'all': [sl('p', 2), sl('s', 2)]}]}   # 분열 + 옵션 1개 이하
NEEDC = {'all': [R, {'not': C}, {'not': {'famBlock': 'chaos'}}]}
NEEDR = {'all': [C, {'not': R}, {'not': {'famBlock': 'res'}}]}

def route(ok_to=None):
    E = [{'if': {'all': [BOTH, sl('p', 3)]}, 'to': 'k6', 'res': 'ok'},
         {'if': BOTH, 'to': 'k5', 'res': 'ok', 'hide': True},
         {'if': {'all': [NEEDC, sl('p', 2)]}, 'to': 'k4'},
         {'if': {'all': [NEEDR, sl('s', 2)]}, 'to': 'k4d'},
         {'if': {'all': [{'any': [NEEDC, NEEDR]}, ROOM2]}, 'to': 'k4g'},
         {'if': {'any': [R, C]}, 'to': 'k5'},
         {'if': BARE, 'to': 'k3', 'res': 'fail'},
         {'to': 'k5c', 'res': 'fail'}]
    for e in E:
        if 'res' not in e: e['res'] = 'fail'
        e.setdefault('hide', True)
    E[0]['hide'] = False
    return E

# ---------------- 베이스템 완성 (영상 1:30~2:30) ----------------
A(id='k0', kind='base', group='prep', pos=[0, 0], next='k1',
  start={'rar': 'rare', 'mods': [{'tag': 'far', 'fr': True}, {'junk': 'p'}]},
  label=K('균열 반지 구입 (아이템 레벨 81, 잔류물 거리 분열 + 잡옵 1개)', 'Buy a Breach Ring (item level 81, fractured remnant pickup range + one junk option)'),
  item=[J('p'), FR])
A(id='k1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Essence_of_the_Breach', ess='maxq', label=K('에센스', 'Essence'),
  goal=K('최대 퀄리티 +20%', '+20% maximum quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'k2'}], item=[MQ, FR])
A(id='k2', kind='act', group='prep', pos=[0, 2], act='quality', cur='Chayulas_Catalyst', count=60, label=K('퀄리티', 'Quality'),
  goal=K('카오스 퀄리티 60%', '60% chaos quality'), edges=[{'to': 'km'}], item=[MQ, FR])

# ---------------- 옵션 추가 작업 ----------------
A(id='km', kind='mark', group='main', pos=[0, 3.4], next='k3', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MQ, FR])
# 성공 회차 3:18~3:25: 분열 + 옵션 1개에 카오스 오브 반복 → 모든 원소 저항 +12(2티어). 첫 회차는 카오스 피해 1티어가 먼저(2:38)
A(id='k3', kind='act', group='main', pos=[0, 4.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('모든 원소 저항·카오스 피해 중 먼저 뜬 것', 'All resistances or chaos damage, whichever lands first'), show=['res', 'chaos'],
  edges=[{'if': R, 'to': 'k4', 'res': 'ok'}, {'if': C, 'to': 'k4d', 'res': 'ok', 'hide': True}, {'to': 'k3', 'res': 'fail', 'hide': True}],
  item=[FR, RS])
# 남은 하나(영상 3:26~3:32 성공 회차: 좌측 찬미, 2:32~3:15 첫 회차: 우측 찬미·소멸의 오브·상위 찬미만)
A(id='k4', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation', 'Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 2개 — 카오스 피해', 'Two prefixes: chaos damage'), show=['chaos'], showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=route(), item=[CHD, LIFE, FR, RS])
A(id='k4d', kind='act', group='main', pos=[1, 5.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation', 'Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 2개 — 모든 원소 저항', 'Two suffixes: all resistances'), show=['res'], edges=route())
A(id='k4g', kind='act', group='main', pos=[1, 6.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('옵션 2개 — 남은 모든 원소 저항·카오스 피해', 'Two options: the missing all resistances or chaos damage'), show=['res', 'chaos'], edges=route())
A(id='k5', kind='act', group='main', pos=[2, 5.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove a missed option'), edges=route())
A(id='k5c', kind='cleanup', group='main', pos=[2, 6.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'k3', 'res': 'fail'}])
# 마무리(영상 3:37~4:34): 좌측 강령술 + 군왕의 징조 + 보존된 빗장뼈 → 완벽한 엑잘 → 심연의 메아리 공개
A(id='k6', kind='act', group='main', pos=[0, 7.4], act='desecrate', cur='Preserved_Collarbone',
  omens=['Omen_of_Sinistral_Necromancy', 'Omen_of_the_Liege'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션 — 아마나무 훼손', 'Third prefix: Amanamu desecration'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'k7'}],
  item=[CHD, LIFE, UN('p'), FR, RS])
A(id='k7', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('마지막 옵션', 'Last option'), showText=[K('랜덤 옵션 1개', 'One random option')],
  skipIf={'all': [{'full': 'p'}, {'full': 's'}]}, skipTo='k8', skipHide=True,
  edges=[{'to': 'k8'}], item=[CHD, LIFE, UN('p'), FR, RS, MK])
A(id='k8', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='eff', label=K('공개', 'Reveal'),
  goal=K('접두 세번째 옵션(훼손) — 플레이어가 생성하는 잔류물의 효과', 'Third prefix (desecrated): remnant effect'), show=['eff'],
  edges=[{'if': {'added': 'eff'}, 'to': 'ok', 'res': 'ok'}, {'to': 'ok', 'res': 'fail', 'hide': True}],
  item=[CHD, LIFE, EF, FR, RS, MK])
A(id='ok', kind='done', group='main', pos=[0, 10.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['k4', 'k4d', 'k4g', 'k5', 'k5c'], 'kr': '남은 하나', 'en': 'The other one', 'fold': True,
  'goal': K('접두 카오스 피해 1티어 — 모든 원소 저항·카오스 피해 중 남은 것', 'T1 chaos damage prefix: whichever of all resistances or chaos damage is missing'),
  'goalBy': {'high': K('접두 카오스 피해 1티어 — 모든 원소 저항·카오스 피해 중 남은 것', 'T1 chaos damage prefix: whichever of all resistances or chaos damage is missing'),
             'bal': K('접두 카오스 피해 1~2티어 — 모든 원소 저항·카오스 피해 중 남은 것', 'T1–2 chaos damage prefix: whichever of all resistances or chaos damage is missing')},
  'steps': [K('상위 찬미의 징조 + 좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 2개', 'Omen of Greater Exaltation + Omen of Sinistral Exaltation + Perfect Exalted Orb for two prefixes') | {'node': 'k4'},
            K('카오스 피해가 먼저 떴으면 우측 찬미의 징조로 접미 2개', 'Chaos damage came first: Omen of Dextral Exaltation for two suffixes') | {'node': 'k4d'},
            K('빗나가면 소멸의 오브', 'A miss: Orb of Annulment') | {'node': 'k5'},
            K('필요한 쪽 빈자리가 하나뿐이면 상위 찬미의 징조만', 'Only one free slot on the needed side: Omen of Greater Exaltation alone') | {'node': 'k4g'},
            K('둘 다 지워지면 분열 + 옵션 1개까지 소멸의 오브', 'Both gone: annul down to the fracture + one option') | {'node': 'k5c'}],
  'worst': {'kr': '모든 원소 저항·카오스 피해가 모두 지워지면 카오스 단계부터', 'en': 'All resistances and chaos damage both gone: back to the Chaos step', 'to': 'k3'},
  'item': [CHD, LIFE, FR, RS]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
