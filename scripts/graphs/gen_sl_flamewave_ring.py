# W30 2026-11-13: SL 검은 화염파 반지(UAF91gEFRkM) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W30-sl-ring/timeline.md · frames/ (영상 0:00~11:20 화면 대조, 3:05·3:56 중간 광고 건너뜀)
# 실행: python3 scripts/graphs/gen_sl_flamewave_ring.py → scripts/graphs/sl-flamewave-ring-v2.json (gen_batch16.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
#
# 슬라이드 제작 방법 8단계(2:58): 1 황금 반지 + 82레벨 + 모든 원소 저항 16% 매직 구입 → 2 분열의 오브(모든 원소 저항) → 3 균열의 에센스 + 차율라의 기폭제 40%
#   → 4 소멸로 옵션 1개만 남기고 카오스 오브로 접두 1개 → 5 좌측 찬미 + 완벽한 엑잘(실패 시 소멸, 소멸도 실패 시 3으로) → 6 좌측 강령술 + 뒤바뀐 빗장뼈(주문이 피해의 %를 카오스 피해로 획득)
#   → 7 상위 찬미 + 완벽한 엑잘로 아무 저항 1티어 → 8 절사 + 말소 + 완벽한 카오스 오브로 접미 희귀도(슬라이드 글은 '좌측 말소', 실제 화면 10:22는 우측 말소의 징조)
# 성공 회차(화면): 3:05 매직 반지 3개(번개 피해 + 모든 원소 저항 16) → 3:10 제왕 → 3:16 보존된 빗장뼈 → 3:20 분열의 오브(세 개 모두 실패, 3:40 분열된 반지 구입)
#   → 3:46 균열의 에센스(카오스 피해가 지워지고 최대 퀄리티) → 3:51 차율라의 기폭제 40% → 4:05 바알 촉진시키는 주입기 1번(45%) → 4:30·4:32 소멸 2번(최대 퀄리티·정확도, 미공개 훼손 남음)
#   → 4:36~7:05 카오스 오브(창고 카오스 오브 363 → 176) — 희귀도·카오스 피해 1티어, 5:41 좌측 찬미 + 완벽한 엑잘 → 빗나가면 징조 없는 소멸, 희귀도가 지워지면 카오스부터(5:52, 6:40, 7:03)
#   → 7:05 카오스 피해 1티어 → 7:09 엑잘 희귀도 1티어 → 7:21 좌측 강령술 + 7:23 뒤바뀐 빗장뼈 → 7:33 심연의 메아리 공개 → 빗나감 2번(7:41, 8:21), 8:12 빛의 징조 + 소멸의 오브 → 8:27 주문이 피해의 10%를 카오스 피해로 획득
#   → 8:36 상위 찬미 + 완벽한 엑잘(접미 2개) → 빗나가면 우측 소멸의 징조 + 소멸의 오브 2번으로 접미를 분열 옵션만 남기고 다시(8:46~8:51, 징조 6 → 4 → 2) → 10:06 번개 저항 1티어 + 시전 속도 1티어
#   → 10:22 절사의 징조 + 우측 말소의 징조 + 완벽한 카오스 오브(시전 속도가 바뀜) 5번 → 10:52 냉기 저항 1티어에서 멈춤(비용 때문, 희귀도 접미는 못 띄움).
# 영상과 다르게 정한 곳(내부 결정, 보고서에 적음):
#   1 분열 준비: 영상은 세 번 모두 실패하고 분열된 반지를 삼(3:40). 플로우차트는 슬라이드 2번대로 직접 분열(1/3, 실패하면 새 베이스). 제왕의 오브 등급은 편집으로 화면에 없어 완벽한 제왕의 오브(정책 2장).
#   2 바알 촉진시키는 주입기는 옆 상자(선택, 비용 미포함) — 영상 '자본에 여유가 있으면', 실패하면 처음부터.
#   3 하이엔드 마지막 접미 = 슬라이드 8번·제작 목표물(0:22)의 희귀도 1티어까지 절사 카오스 반복. 영상은 다섯 번 뒤 냉기 저항 1티어에서 멈춤 → 밸런스는 마지막 접미 랜덤 옵션.
#   4 공허 유동체(단일 원소 저항 1티어 → 카오스 저항 1티어, 0:47 슬라이드 설명)는 영상에서 쓰지 않아 플로우차트에 넣지 않음 — 꿀팁 후보.
# 등급(정책 10장, 전문가 → 하이엔드·밸런스): 하이엔드 = 저항 1티어 + 희귀도 접미 1티어, 밸런스 = 저항 1~2티어(8:55 '2티어로 만족해도') + 접두 생명력 1티어도 받음(6:20) + 마지막 접미 랜덤 옵션.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sl-flamewave-ring-v2.json'
CLS = 'Rings'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags, m='n', ti=0, tail=None):   # DB 옵션 문구(티어 ti)
    t = D['groups'][gi]['t'][ti]
    kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if tail: kr, en = f'{kr} ({tail[0]})', f'{en} ({tail[1]})'
    return L(s, kr, en, m, tags)

AR = DB('s', 7, ['ar'])                                   # 모든 원소 저항 +(15—16)% 1티어
ARf = DB('s', 7, ['ar'], 'f')
MQ = DB('p', 71, ['mq'], 'c')
CD = DB('p', 33, ['cd'])                                  # 카오스 피해 (27—30)% 증가 1티어
RP = DB('p', 28, ['rp'])                                  # 발견하는 아이템 희귀도 (16—19)% 증가 1티어(접두)
OC = DB('p', 86, ['oc'], 'd')  # 주문이 피해의 (8—12)%를 카오스 피해로 획득
LR = DB('s', 6, ['li'])                                   # 번개 저항 +(41—45)% 1티어
CS = DB('s', 34, [])                                      # 시전 속도 (22—24)% 증가 1티어(성공 회차에서 함께 붙은 옵션)
RS = DB('s', 27, ['rs'])                                  # 발견하는 아이템 희귀도 (15—18)% 증가 1티어(접미)
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V1 = {'param': {'v': 1}}; V2 = {'param': {'v': 2}}
RES = ['fi', 'co', 'li', 'ch']

g = {
 'id': 'sl-flamewave-ring-v2', 'recipe': 'sl-flamewave-ring-v2', 'cls': CLS, 'base': 'Gold Ring', 'ilvl': 82,
 'note': ('SL 검은 화염파 반지(UAF91gEFRkM, 2026-11-13 W30 영상 전체 화면 대조) — 모든 원소 저항 1티어 매직 황금 반지(82) → 완벽한 제왕 → 보존된 빗장뼈 → 분열(모든 원소 저항, 1/3) '
          '→ 균열의 에센스 → 차율라의 기폭제 40%(바알 촉진시키는 주입기는 선택) → 소멸로 분열 + 옵션 1개 → 카오스 오브(카오스 피해·희귀도 1티어 중 먼저 뜬 것) '
          '→ 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸, 좋은 접두가 지워지면 카오스부터) → 좌측 강령술 + 뒤바뀐 빗장뼈 → 심연의 메아리 공개(주문이 피해의 %를 카오스 피해로 획득, 빗나가면 빛의 징조 + 소멸) '
          '→ 상위 찬미 + 완벽한 엑잘(저항, 빗나가면 우측 소멸의 징조 + 소멸로 접미 비우기) → 절사 + 우측 말소 + 완벽한 카오스 오브(희귀도). '
          '하이엔드 = 저항 1티어 + 희귀도 접미 1티어(슬라이드·제작 목표물), 밸런스 = 저항 1~2티어, 접두 생명력 1티어도 받음, 마지막 접미 랜덤 옵션(영상은 냉기 저항에서 멈춤).'),
 'params': {'v': {'kr': '마지막 접미', 'en': 'Last suffix', 'values': {'1': K('희귀도 1티어', 'T1 rarity'), '2': K('랜덤 옵션', 'Random')}},
            'pT': {'kr': '접미 저항', 'en': 'Suffix resistance', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'v': 1, 'pT': 1}}, {'id': 'bal', 'params': {'v': 2, 'pT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 2, 'pT': 2}, 'tier': 'bal',
    'desc': K('저항 1~2티어, 접두 생명력 1티어도 받음, 마지막 접미는 나오는 대로', 'T1–2 resistance, T1 life is a fine prefix, last suffix as it comes')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'v': 1, 'pT': 1}, 'tier': 'high',
    'desc': K('저항 1티어 + 접미 희귀도 1티어(슬라이드 목표)', 'T1 resistance + T1 rarity suffix (the slide target)')}],
 'tags': {
   'ar': {'gi': 7, 'tmax': 1}, 'mq': {'gi': 71}, 'cd': {'gi': 33, 'tmax': 1}, 'rp': {'gi': 28, 'tmax': 1}, 'lf': {'gi': 9, 'tmax': 1}, 'oc': {'gi': 86},
   'fi': {'gi': 4, 'tmax': '$pT'}, 'co': {'gi': 5, 'tmax': '$pT'}, 'li': {'gi': 6, 'tmax': '$pT'}, 'ch': {'gi': 8, 'tmax': '$pT'},
   'res': {'anyOf': RES, 'label': K('화염·냉기·번개·카오스 저항', 'Fire, cold, lightning or chaos resistance')},
   'rs': {'gi': 27, 'tmax': 1},
   'gpre': {'anyOf': ['cd', 'rp'], 'shown': 'cd', 'label': K('카오스 피해·발견하는 아이템 희귀도 1티어', 'T1 chaos damage or item rarity')},
   'gpreB': {'anyOf': ['cd', 'rp', 'lf'], 'shown': 'rp', 'label': K('카오스 피해·발견하는 아이템 희귀도·생명력 최대치 1티어', 'T1 chaos damage, item rarity or maximum life')},
   # 완성 카드용(등급별 고정 티어)
   'fi1': {'gi': 4, 'tmax': 1}, 'co1': {'gi': 5, 'tmax': 1}, 'li1': {'gi': 6, 'tmax': 1}, 'ch1': {'gi': 8, 'tmax': 1},
   'fi2': {'gi': 4, 'tmax': 2}, 'co2': {'gi': 5, 'tmax': 2}, 'li2': {'gi': 6, 'tmax': 2}, 'ch2': {'gi': 8, 'tmax': 2},
   'res1': {'anyOf': ['fi1', 'co1', 'li1', 'ch1'], 'shown': 'li1', 'label': K('화염·냉기·번개·카오스 저항 1티어', 'T1 fire, cold, lightning or chaos resistance')},
   'res2': {'anyOf': ['fi2', 'co2', 'li2', 'ch2'], 'shown': 'li2', 'label': K('화염·냉기·번개·카오스 저항 1~2티어', 'T1–2 fire, cold, lightning or chaos resistance')},
 },
 'conds': {'sClean': {'sideLt': {'side': 's', 'n': 2}}},
 'require': {'all': [{'has': 'ar'}, {'has': 'oc'}, {'has': 'res'}, {'has': 'gpre'}, {'count': {'tag': 'gpreB', 'min': 2}},
                     {'any': [V2, {'count': {'tag': 'gpre', 'min': 2}}]}, {'any': [V2, {'has': 'rs'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
I_M = [J('p'), AR]
A(id='b0', kind='base', group='prep', pos=[0, 0], next='rg', start={'rar': 'magic', 'mods': [{'tag': 'ar'}, {'junk': 'p'}]},
  label=K('모든 원소 저항 1티어 매직 황금 반지 구입 (아이템 레벨 82)', 'Buy a magic Gold Ring with T1 all elemental resistances (item level 82)'), item=I_M)
A(id='rg', kind='act', group='prep', pos=[0, 1], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('분열하기 위해 레어로', 'Make it rare for the fracture'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'bn'}], item=[J('p'), J('p'), AR])
A(id='bn', kind='act', group='prep', pos=[0, 2], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'fr'}],
  item=[J('p'), J('p'), AR, UN('s')])
A(id='fr', kind='act', group='prep', pos=[0, 3], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('모든 원소 저항이 분열되면 성공', 'Success when all elemental resistances fractures')],
  edges=[{'if': {'fractured': 'ar'}, 'to': 'es', 'res': 'ok', 'label': K('모든 원소 저항 분열', 'All res fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), J('p'), ARf, UN('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 3], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('모든 원소 저항이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='es', kind='act', group='prep', pos=[0, 4], act='essence', cur='Essence_of_the_Breach', ess='mq', label=K('에센스', 'Essence'),
  goal=K('접두 잡옵을 지우고 최대 퀄리티', 'A junk prefix goes for max quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'ct'}],
  item=[MQ, J('p'), ARf, UN('s')])
A(id='ct', kind='act', group='prep', pos=[0, 5], act='quality', cur='Chayulas_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('카오스 퀄리티 40%', 'Chaos quality 40%'), showText=[K('차율라의 기폭제 40개', '40 Chayula’s Catalysts')], edges=[{'to': 'cl'}],
  item=[MQ, J('p'), ARf, UN('s')])
A(id='vi', kind='side', group='prep', pos=[1, 5.5], attach=['ct', 'cl'], cur='Vaal_Catalysing_Infuser',
  goal=K('퀄리티 45%, 선택·비용 미포함', 'Quality 45%, optional, not costed'), label=K('퀄리티', 'Quality'))
A(id='cl', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[ARf, UN('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='ca', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ARf, UN('s')])
A(id='ca', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 첫 번째 옵션 — 카오스 피해·희귀도 1티어 중 먼저 뜬 것', 'First prefix: T1 chaos damage or rarity, whichever lands first'), show=['cd'],
  edges=[{'if': {'has': 'gpre'}, 'to': 'ex', 'res': 'ok'}, {'to': 'ca', 'res': 'fail', 'hide': True}], item=[CD, ARf])
A(id='ex', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 두 번째 옵션 — 남은 옵션', 'Second prefix: the other one'), show=['rp'],
  edges=[{'if': {'count': {'tag': 'gpre', 'min': 2}}, 'to': 'dn', 'res': 'ok'},
         {'if': {'all': [V2, {'has': 'gpre'}, {'has': 'lf'}]}, 'to': 'dn', 'res': 'ok', 'hide': True},
         {'to': 'ea', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[CD, RP, ARf])
A(id='ea', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기 — 좋은 접두가 지워지면 카오스부터', 'Remove the missed prefix: back to Chaos if the good one goes'),
  edges=[{'if': {'has': 'gpre'}, 'to': 'ex', 'res': 'ok', 'label': K('좋은 접두 남음', 'Good prefix kept')},
         {'to': 'ca', 'res': 'fail', 'label': K('좋은 접두가 지워짐', 'Good prefix gone')}])
A(id='dn', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Altered_Collarbone', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'rv'}], item=[CD, RP, UN('p'), ARf])
A(id='rv', kind='act', group='main', pos=[0, 11.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='oc', label=K('공개', 'Reveal'),
  goal=K('훼손 옵션 확인', 'Reveal the desecrated modifier'), show=['oc'],
  edges=[{'if': {'added': 'oc'}, 'to': 'sx', 'res': 'ok'}, {'to': 'rx', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[CD, RP, OC, ARf])
A(id='rx', kind='act', group='main', pos=[1, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'dn', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='sx', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 두 번째·세 번째 옵션 — 저항 하나', 'Second and third suffixes: one resistance'), show=['li'],
  showText=[K('랜덤 옵션 1개가 함께 붙음', 'One random option comes with it')],
  edges=[{'if': {'has': 'res'}, 'to': 'wc', 'res': 'ok'}, {'to': 'sR', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[CD, RP, OC, ARf, LR, CS])
A(id='sR', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=ANN, goal=ANN,
  target=K('접미를 분열 옵션만 남기기', 'Clear the suffixes down to the fracture'),
  edges=[{'if': {'ref': 'sClean'}, 'to': 'sx', 'res': 'ok', 'label': K('접미 정리 끝 — 다시 엑잘', 'Suffixes clear: exalt again')},
         {'to': 'sR', 'res': 'fail', 'hide': True}])
A(id='wc', kind='act', group='main', pos=[0, 13.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling', 'Omen_of_Dextral_Erasure'],
  label=K('절사 + 카오스', 'Whittling + Chaos'), goal=K('접미 세 번째 옵션', 'Third suffix'), show=['rs'],
  skipIf={'any': [V2, {'has': 'rs'}]}, skipTo='ok', skipNote=K('희귀도 접미가 이미 있으면 건너뜀', 'Skip if the rarity suffix is already there'),
  edges=[{'if': {'has': 'rs'}, 'to': 'ok', 'res': 'ok'}, {'to': 'wc', 'res': 'fail', 'hide': True}],
  item=[CD, RP, OC, ARf, LR, RS])
A(id='ok', kind='done', group='main', pos=[0, 14.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L1', 'nodes': ['ex', 'ea'], 'kr': '접두 두 번째 옵션', 'en': 'Second prefix'},
 {'id': 'L2', 'nodes': ['dn', 'rv', 'rx'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal'},
 {'id': 'L3', 'nodes': ['sx', 'sR'], 'kr': '접미 저항', 'en': 'Suffix resistance'},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'cd'}, {'tag': 'rp'}, {'tag': 'oc', 'des': True}, {'tag': 'ar', 'fr': True}, {'tag': 'res1'}, {'tag': 'rs'}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'gpre'}, {'tag': 'gpreB'}, {'tag': 'oc', 'des': True}, {'tag': 'ar', 'fr': True}, {'tag': 'res2'}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
