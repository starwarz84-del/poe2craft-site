# W26 2026-11-13: SL 화염파 지팡이(6EzSVUItzsg) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W26-sl-staff/timeline.md, frames/ (영상 0:00~15:13 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sl_flamewave_staff.py  → sl-flamewave-staff-v2.json (gen_batch14.py 끝에서 자동 호출, 이 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sl-flamewave-staff-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

F7n = L('s', '모든 화염 주문 스킬 레벨 +7', '+7 to Level of all Fire Spell Skills', 'n', ['fire7'])
F7 = L('s', '모든 화염 주문 스킬 레벨 +7 (분열)', '+7 to Level of all Fire Spell Skills (fractured)', 'f', ['fire7'])
PF = L('p', '화염 피해 (209—238)% 증가', '(209—238)% increased Fire Damage', 'n', ['dfi'])
XC = L('p', '피해의 (55—60)%를 추가 냉기 피해로 획득', 'Gain (55—60)% of Damage as Extra Cold Damage', 'n', ['xco'])
XF = L('p', '피해의 (55—60)%를 추가 화염 피해로 획득 (훼손)', 'Gain (55—60)% of Damage as Extra Fire Damage (desecrated)', 'd', ['xfi'])
RN = L('r', '스루드의 완력', 'Thrud’s Might', 'r')
FM = L('s', '비고정 화염 속성 부여 규모 (15—20)% 증가', '(15—20)% increased Explicit Fire Modifier magnitudes', 'n', ['fm'])
AL = L('s', '시전 속도 (39—47)% 증가 · 원소 피해의 (11—16)%를 추가 냉기 피해로 획득 (초월의 합금)',
       '(39—47)% increased Cast Speed · Gain (11—16)% of Elemental Damage as Extra Cold Damage (Transcendent Alloy)', 'c', ['alloy'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
ALT = [{'s': 's', 'kr': '시전 속도 (39—47)% 증가 · 원소 피해의 (11—16)%를 추가 냉기 피해로 획득 (제작 옵션)',
        'en': '(39—47)% increased Cast Speed · Gain (11—16)% of Elemental Damage as Extra Cold Damage (crafted)'}]
V1 = {'param': {'v': 1}}; V2 = {'param': {'v': 2}}
PRE_T = lambda t: [{'s': 'p', 'kr': f'피해 증가·피해의 %를 추가 피해로 획득 {t[0]}', 'en': f'{t[1]} increased damage or damage gained as extra'}]
PD_T = lambda t: [{'s': 'p', 'kr': f'주문·화염·냉기·번개·카오스 피해 증가 {t[0]}', 'en': f'{t[1]} increased spell, fire, cold, lightning or chaos damage'}]
T1 = ('1티어', 'T1'); T12 = ('1~2티어', 'T1–2')
OVR = lambda f: [{'param': {'v': 2}, 'set': {'showText': f(T12)}}]

PDL = K('주문·화염·냉기·번개·카오스 피해 증가', 'Increased spell, fire, cold, lightning or chaos damage')
PREL = K('피해 증가·피해의 %를 추가 피해로 획득', 'Increased damage or damage gained as extra')

g = {
 'id': 'sl-flamewave-staff-v2', 'recipe': 'sl-flamewave-staff-v2', 'cls': 'Staves', 'base': 'Chiming Staff', 'ilvl': 81,
 'note': ('2026-11-13 W26 영상 전체 화면 대조(0:00~15:13). 성공 회차 한 줄: 특출난 차임벨 지팡이(아이템 레벨 81, 홈 3개, 2:22) → 매직, 완벽한 확장의 오브 + 소멸의 오브 반복으로 '
          '모든 화염 주문 +7(3:26) → 완벽한 확장으로 접두 아무거나(마나 최대치) → 완벽한 제왕(지능) → 보존된 턱뼈(3:53~3:56) → 분열(5:00, 영상은 실패 뒤 분열된 매물 구입 5:22) → '
          '소멸 2번(분열 + 능력치 요구사항 잡옵, 6:35) → 카오스 오브로 주문 피해 1티어(6:50) → 좌측 찬미 + 완벽한 엑잘 = 마나 최대치(7:10) → 소멸이 주문 피해를 지움(7:14) → '
          '카오스 오브로 화염 피해 1티어(7:32) → 좌측 찬미 + 완벽한 엑잘 = 추가 냉기 1티어(7:50) → 좌측 강령술 + 고대 턱뼈 + 심연의 메아리 공개 = 추가 화염 1티어(8:20~8:32, 빛의 징조 준비) → '
          '알두르의 배신(9:05) → 스루드의 완력(11:20) → 상위 찬미 + 완벽한 엑잘 접미 2개(11:20) → 절사의 징조 + 완벽한 카오스 오브 = 비고정 화염 속성 부여 규모 17%(12:20) → 초월의 합금(13:18). '
          '초월의 합금(13:18)은 사용자 결정(2026-11-13 06:40)대로 하이엔드 선택 단계(점선 상자, 비용 미포함) — 접미 하나를 1/2로 지워 화염 속성 부여 규모를 잃으면 절사 카오스를 다시 해야 해서 이 구간만 약 550 div. '
          '알두르의 배신(옵션을 카오스로 바꿈)·완벽한 유동체(스킬 20레벨)·퀄리티 20%·바알 오브(14:45)는 제작 확률과 무관해 뺌(정책 9·14장). '
          '밸런스 = 영상 9:13 가성비 마무리(스루드의 완력 없이 엑잘 접미 2개 + 초월의 합금) + 접두 반복 1~2티어, 공개 빗나감은 빛의 징조로 다시(10장 C17 3번).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('스루드의 완력', 'Thrud’s Might'), '2': K('가성비 마무리', 'Budget finish')}},
            'pT': {'kr': '접두 (카오스·엑잘·공개)', 'en': 'Prefixes (chaos, exalt, reveal)', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'v': 1, 'pT': 1}}, {'id': 'bal', 'params': {'v': 2, 'pT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 2, 'pT': 2}, 'tier': 'bal',
    'desc': K('영상의 가성비 마무리: 접두 1~2티어, 엑잘 접미 2개 + 초월의 합금', 'Video budget finish: T1–2 prefixes, two exalted suffixes + Transcendent Alloy')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'v': 1, 'pT': 1}, 'tier': 'high',
    'desc': K('영상: 접두 1티어 3개, 스루드의 완력으로 비고정 화염 속성 부여 규모, 초월의 합금은 선택', 'Video: three T1 prefixes, Thrud’s Might fire magnitudes, Transcendent Alloy optional')}],
 'tags': {
   'fire7': {'gi': 12, 'tmax': 1},
   'dsp': {'gi': 3, 'tmax': '$pT'}, 'dfi': {'gi': 5, 'tmax': '$pT'}, 'dco': {'gi': 6, 'tmax': '$pT'}, 'dli': {'gi': 7, 'tmax': '$pT'}, 'dch': {'gi': 8, 'tmax': '$pT'},
   'xfi': {'gi': 32, 'tmax': '$pT'}, 'xco': {'gi': 33, 'tmax': '$pT'}, 'xli': {'gi': 34, 'tmax': '$pT'},
   'pd': {'anyOf': ['dsp', 'dfi', 'dco', 'dli', 'dch'], 'label': PDL},
   'px': {'anyOf': ['xfi', 'xco', 'xli'], 'label': K('피해의 %를 추가 화염·냉기·번개 피해로 획득', 'Damage gained as extra fire, cold or lightning')},
   'pre': {'anyOf': ['pd', 'px'], 'label': PREL},
   # 완성 카드용(등급별 고정 티어)
   'dsp1': {'gi': 3, 'tmax': 1}, 'dfi1': {'gi': 5, 'tmax': 1}, 'dco1': {'gi': 6, 'tmax': 1}, 'dli1': {'gi': 7, 'tmax': 1}, 'dch1': {'gi': 8, 'tmax': 1},
   'xfi1': {'gi': 32, 'tmax': 1}, 'xco1': {'gi': 33, 'tmax': 1}, 'xli1': {'gi': 34, 'tmax': 1},
   'dsp2': {'gi': 3, 'tmax': 2}, 'dfi2': {'gi': 5, 'tmax': 2}, 'dco2': {'gi': 6, 'tmax': 2}, 'dli2': {'gi': 7, 'tmax': 2}, 'dch2': {'gi': 8, 'tmax': 2},
   'xfi2': {'gi': 32, 'tmax': 2}, 'xco2': {'gi': 33, 'tmax': 2}, 'xli2': {'gi': 34, 'tmax': 2},
   'pd1': {'anyOf': ['dsp1', 'dfi1', 'dco1', 'dli1', 'dch1'], 'label': K('주문·화염·냉기·번개·카오스 피해 증가 1티어', 'T1 increased spell, fire, cold, lightning or chaos damage')},
   'pre1': {'anyOf': ['dsp1', 'dfi1', 'dco1', 'dli1', 'dch1', 'xfi1', 'xco1', 'xli1'], 'label': K('피해 증가·피해의 %를 추가 피해로 획득 1티어', 'T1 increased damage or damage gained as extra')},
   'pd2': {'anyOf': ['dsp2', 'dfi2', 'dco2', 'dli2', 'dch2'], 'label': K('주문·화염·냉기·번개·카오스 피해 증가 1~2티어', 'T1–2 increased spell, fire, cold, lightning or chaos damage')},
   'pre2': {'anyOf': ['dsp2', 'dfi2', 'dco2', 'dli2', 'dch2', 'xfi2', 'xco2', 'xli2'], 'label': K('피해 증가·피해의 %를 추가 피해로 획득 1~2티어', 'T1–2 increased damage or damage gained as extra')},
   'fm': {'gi': 68}, 'alloy': {'gi': 65}, 'keep': {'anyOf': ['fm', 'alloy']}},
 'require': {'all': [{'has': 'fire7'}, {'has': 'pd'}, {'count': {'tag': 'pre', 'min': 3}}, {'any': [{'all': [V1, {'has': 'fm'}]}, {'all': [V2, {'has': 'alloy'}]}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 3},
 'xsub': ["Thrud's Might"], 'xroll': True,
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='t1', start={'rar': 'normal', 'mods': []},
  label=K('특출난 차임벨 지팡이 구입 (아이템 레벨 81, 홈 3개)', 'Buy an exceptional Chiming Staff (item level 81, three sockets)'), item=[])
A(id='t1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'if': {'has': 'fire7'}, 'to': 'a2', 'res': 'ok', 'hide': True}, {'to': 'x1', 'res': 'fail'}], item=[F7n])
A(id='x1', kind='cleanup', group='prep', pos=[1, 1.5], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), edges=[{'to': 'a1'}])
A(id='a1', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접미 모든 화염 주문 스킬 레벨 +7', '+7 fire spell skills suffix'), show=['fire7'],
  edges=[{'if': {'has': 'fire7'}, 'to': 'a2', 'res': 'ok'}, {'to': 'x1', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[F7n])
A(id='a2', kind='act', group='prep', pos=[0, 3], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 랜덤 옵션 1개 — 분열 조건 옵션 4개', 'One random prefix: the fracture needs four options'), showText=[K('랜덤 옵션 1개', 'One random option')],
  skipIf={'full': 'p'}, skipTo='rg', skipHide=True, edges=[{'to': 'rg'}], item=[J('p'), F7n])
A(id='rg', kind='act', group='prep', pos=[0, 4], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'ds'}], item=[J('p'), F7n, J('s')])
A(id='ds', kind='act', group='prep', pos=[0, 5], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'fr'}],
  item=[J('p'), F7n, J('s'), UN('x')])
A(id='fr', kind='act', group='prep', pos=[0, 6], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('화염 주문 +7이 분열되면 성공', 'Success when the +7 fire spell skills fractures')],
  edges=[{'if': {'fractured': 'fire7'}, 'to': 'pc', 'res': 'ok', 'label': K('화염 주문 +7 분열', '+7 fire spells fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), F7, J('s'), UN('x')])
A(id='xj', kind='exit', group='prep', pos=[1, 6], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('화염 주문 +7이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 7], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[F7, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[F7, J('s')])
A(id='c1', kind='act', group='main', pos=[0, 9.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 화염 피해 증가 — 주문·냉기·번개·카오스 피해 증가와 함께 먼저 뜬 것', 'Increased fire damage prefix: or spell, cold, lightning or chaos, whichever lands first'),
  showText=PD_T(T1), over=OVR(PD_T),
  edges=[{'if': {'has': 'pd'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[F7, PF])
A(id='e1', kind='act', group='main', pos=[0, 10.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 추가 냉기 피해 — 피해 증가·추가 피해 중 먼저 뜬 것', 'Extra cold prefix: whichever increased or extra damage lands first'),
  showText=PRE_T(T1), over=OVR(PRE_T),
  edges=[{'if': {'count': {'tag': 'pre', 'min': 2}}, 'to': 'd1', 'res': 'ok'}, {'to': 'e1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[F7, PF, XC])
A(id='e1x', kind='act', group='main', pos=[1, 10.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기 — 피해 증가가 지워지면 카오스부터', 'Remove the missed prefix: back to Chaos if the damage prefix goes'),
  edges=[{'if': {'has': 'pre'}, 'to': 'e1', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')},
         {'to': 'c1', 'res': 'fail', 'label': K('피해 증가가 지워짐', 'Damage prefix gone')}])
A(id='d1', kind='act', group='main', pos=[0, 11.4], act='desecrate', cur='Ancient_Jawbone', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'd2'}], item=[UN('p'), F7, PF, XC])
A(id='d2', kind='act', group='main', pos=[0, 12.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='pre', label=K('공개', 'Reveal'),
  goal=K('접두 추가 화염 피해(훼손) — 피해 증가·추가 피해 중 먼저 뜬 것', 'Extra fire prefix (desecrated): whichever increased or extra damage lands first'), showText=PRE_T(T1), over=OVR(PRE_T),
  edges=[{'if': {'all': [{'added': 'pre'}, V1]}, 'to': 'r1', 'res': 'ok'},
         {'if': {'added': 'pre'}, 'to': 'b1', 'res': 'ok'},
         {'to': 'dx', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[F7, PF, XC, XF])
A(id='dx', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
# 하이엔드 (영상)
A(id='r1', kind='act', group='main', pos=[0, 13.4], act='rune', label=K('룬', 'Rune'), goal=K('스루드의 완력 장착', 'Socket Thrud’s Might'),
  showText=[K('파괴 속성 부여 가능', 'Can roll Destruction modifiers')], rune=K('스루드의 완력', 'Thrud’s Might'),
  edges=[{'to': 's1'}], item=[F7, PF, XC, XF, RN])
A(id='s1', kind='act', group='main', pos=[0, 14.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 잡옵 2개', 'Two junk suffixes'), showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'if': {'has': 'fm'}, 'to': 'ok', 'hide': True}, {'to': 's2'}], item=[F7, PF, XC, XF, J('s'), J('s'), RN])
A(id='s2', kind='act', group='main', pos=[0, 15.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'],
  label=K('절사 + 카오스', 'Whittling + Chaos'), goal=K('접미 비고정 화염 속성 부여 규모', 'Explicit fire modifier magnitudes suffix'), show=['fm'],
  edges=[{'if': {'has': 'fm'}, 'to': 'ok', 'res': 'ok'}, {'to': 's2', 'res': 'fail', 'hide': True}], item=[F7, PF, XC, XF, FM, J('s'), RN])
# 초월의 합금 = 선택 단계(사용자 결정 2026-11-13 06:40): 시뮬·비용에서 빠짐. 영상 13:18
A(id='hs3', kind='side', group='main', pos=[1, 16.9], attach=['ok', 'ok'], cur='Transcendent_Alloy',   # attach[0]은 두 등급 모두에 있는 상자(s2는 밸런스에서 빠져 그림 오류)
  goal=K('하이엔드 합금 도박, 선택·비용 미포함', 'High-end alloy gamble, optional, not costed'),   # 접미 하나를 1/2로 지움 — 규모가 지워지면 절사 카오스 다시
  label=K('합금', 'Alloy'))
# 밸런스 (영상 9:13 가성비 마무리)
A(id='b1', kind='act', group='main', pos=[0, 13.9], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 두번째 옵션(잡옵)', 'Second suffix (junk)'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'b1b'}], item=[F7, PF, XC, XF, J('s')])
A(id='b1b', kind='act', group='main', pos=[0, 14.9], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 세번째 옵션(잡옵)', 'Third suffix (junk)'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'b2'}], item=[F7, PF, XC, XF, J('s'), J('s')])
A(id='b2', kind='act', group='main', pos=[0, 15.9], act='essence', cur='Transcendent_Alloy', ess='alloy', label=K('합금', 'Alloy'),
  goal=K('접미 잡옵 하나를 지우고 초월의 합금', 'A junk suffix goes for the Transcendent Alloy'), showText=ALT,
  edges=[{'to': 'ok'}], item=[F7, PF, XC, XF, J('s'), AL])
A(id='ok', kind='done', group='main', pos=[0, 16.9], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['a1', 'x1'], 'kr': '매직 화염 주문 +7', 'en': 'Magic +7 fire spells'},
 {'id': 'L2', 'nodes': ['e1', 'e1x'], 'kr': '접두 두번째 옵션', 'en': 'Second prefix'},
 {'id': 'L3', 'nodes': ['d1', 'd2', 'dx'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal'},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'pd1'}, {'tag': 'pre1'}, {'tag': 'pre1', 'des': True}, {'tag': 'fire7', 'fr': True}, {'tag': 'fm'}, {'side': 's', 'random': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'pd2'}, {'tag': 'pre2'}, {'tag': 'pre2', 'des': True}, {'tag': 'fire7', 'fr': True}, {'side': 's', 'random': True}, {'tag': 'alloy', 'ess': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
