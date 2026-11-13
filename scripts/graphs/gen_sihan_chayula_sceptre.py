# G7 2026-11-13: 시한 차율라 셉터(-F7pV0Y7BMA, 6:18) 플로우차트 생성기 — 영상 성공 회차(4:20~6:17, 다시 카오스부터 한 회차) 한 줄
# 근거: scratchpad review/G7/sihan-chayula-sceptre-v2/timeline.md, frames/ (영상 0:00~6:18 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_chayula_sceptre.py  → sihan-chayula-sceptre-v2.json (gen_batch7.py 끝에서도 자동 호출, 이 아이템 구간을 대신함)
# 상자 id는 옛 레시피(recipes_v5_sihan-chayula-sceptre.py, s1~s7·p1~p4)·옛 그래프(p4x·p4d)와 겹치지 않게 지음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-chayula-sceptre-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차에 실제로 나온 옵션
SP = L('p', '정신력 (56—60)% 증가 (분열)', '(56—60)% increased Spirit (fractured)', 'f', ['sp'])            # 1:04
AOE = L('s', '접근 효과 범위 (66—80)% 증가', '(66—80)% increased Presence Area of Effect', 'n', ['aoe'])     # 5:10 74%
ALJ = L('p', '접근해 있는 동료들이 주는 공격 물리 피해 추가', 'Allies in your Presence deal added Physical Attack Damage', 'j')   # 5:07 첫 엑잘(합금이 지움)
WD = L('s', '최대 룬 수호 +(51—74) (보호의 합금)', '+(51—74) to maximum Runic Ward (Protective Alloy)', 'c', ['ward'])  # 5:23 +61
MA = L('p', '마나 최대치 +(105—124)', '+(105—124) to maximum Mana', 'j')                                   # 5:23 +109(에센스가 지움)
ALD = L('p', '접근해 있는 동료가 주는 피해 (75—89)% 증가', 'Allies in your Presence deal (75—89)% increased Damage', 'j')     # 6:17 83% T3(랜덤 옵션)
AU = L('s', '오라 스킬의 강도 (15—20)% 증가 (완벽한 지휘의 에센스)', 'Aura Skills have (15—20)% increased Magnitudes (Perfect Essence of Command)', 'c', ['aura'])  # 5:27 19%
HY = L('p', '정신력 (23—26)% 증가 · 마나 최대치 +(29—33) (훼손)', '(23—26)% increased Spirit · +(29—33) to maximum Mana (desecrated)', 'd', ['hyv'])  # 6:17 T4
HY2 = L('p', '정신력 (31—38)% 증가 · 마나 최대치 +(38—45) (훼손)', '(31—38)% increased Spirit · +(38—45) to maximum Mana (desecrated)', 'd', ['hy2'])   # 밸런스 목표(1~2티어, C17)
RN = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V_ESS = {'param': {'L': 0}}

g = {
 'id': 'sihan-chayula-sceptre-v2', 'recipe': 'sihan-chayula-sceptre-v2', 'cls': 'Sceptres', 'base': 'Stoic Sceptre', 'ilvl': 82,
 'note': ('2026-11-13 G7 영상 전체(0:00~6:18) 화면 대조. 시작 = 정신력 % 2티어 분열 + 미공개 훼손이 남은 레어 엄숙한 셉터 구입(1:04, 아이템 레벨 82) → 아스트리드의 창의성(1:14) → '
          '카오스 오브로 접근 효과 범위 1티어(1:32·5:10) → 좌측 찬미 + 상위 엑잘 접두 잡옵 → 좌측 결정화 + 보호의 합금(룬 수호, 잡옵을 지움) → 좌측 찬미 + 상위 엑잘 두 번(마나 최대치·동료 물리 피해) → '
          '좌측 결정화 + 완벽한 지휘의 에센스(오라 강도, 접두 하나를 1/2로 지움 — 성공 회차는 마나가 지워짐, 5:27) → 상위 엑잘 접두(5:47) → 좌측 강령술 + 보존된 턱뼈(접두가 꽉 차 잡옵 하나를 지움) → '
          '심연의 메아리 공개 = 정신력 + 마나 복합 4티어(6:06~6:17). 첫 회차(1:00~4:20)는 3:34 공개가 7티어라 징조 없는 소멸의 오브로 지우다(4:00 "빛의 징조는 돈이 아까워서") 접근 효과까지 지워져 카오스부터 다시 — '
          '이 되돌림을 밸런스 접힌 상자의 순서로 넣음(영상대로 징조 없는 소멸의 오브). 퀄리티 20%(3:05~3:34)는 쓴 커런시를 확인 못 해 비용에서 뺌. '
          '등급(정책 10장): 난이도 3 → 밸런스·에센셜. 카오스 접근 효과는 카오스 오브 반복이라 두 등급 모두 1티어(C15). 밸런스 = 복합 1~2티어까지 다시(정책 10장 C17 — 영상 2:50은 "3티어 이상이면 된다", 완성 4티어. 영상 기준 1~4티어면 시뮬 54 div, 의문으로 보고), 에센셜 = 공개 결과 그대로.'),
 'params': {
  'L': {'kr': '공개', 'en': 'Reveal', 'values': {'1': K('소멸의 오브로 다시', 'Retry with Orbs of Annulment'), '0': K('결과 그대로', 'Keep whatever comes')}},
  'hT': {'kr': '정신력 + 마나 복합', 'en': 'Spirit + mana hybrid', 'values': {'2': K('1~2티어', 'T1–2'), '7': K('나오는 대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1, 'hT': 2}}, {'id': 'ess', 'params': {'L': 0, 'hT': 7}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0, 'hT': 7}, 'tier': 'ess',
   'desc': K('공개 결과 그대로', 'Keep the reveal')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1, 'hT': 2}, 'tier': 'bal',
   'desc': K('정신력 + 마나 복합 1~2티어까지 징조 없는 소멸의 오브로 다시', 'Plain Orbs of Annulment until a T1–2 spirit + mana hybrid')}],
 'tags': {
  'sp': {'gi': 19, 'tmax': 2}, 'aoe': {'gi': 21, 'tmax': 1}, 'ward': {'gi': 31}, 'aura': {'gi': 29},
  'hyb': {'gi': 20, 'tmax': '$hT'}, 'hyv': {'gi': 20, 'tmax': 4}, 'hy2': {'gi': 20, 'tmax': 2},
  'keepS': {'anyOf': ['aoe', 'ward', 'aura']},
 },
 'require': {'all': [{'has': 'sp'}, {'has': 'aoe'}, {'has': 'ward'}, {'has': 'aura'}, {'full': 'p'}, {'any': [V_ESS, {'has': 'hyb'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'q0',
 'finalItem': {'quality': 20, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)

A(id='q0', kind='base', group='prep', pos=[0, 0], next='qr', start={'rar': 'rare', 'mods': [{'tag': 'sp', 'fr': True}, {'junk': 'p'}]},
  label=K('정신력 % 2티어 분열 엄숙한 셉터 구입 (아이템 레벨 82, 미공개 훼손 1개)', 'Buy a Stoic Sceptre with fractured T2 % Spirit (item level 82, one unrevealed desecration)'),
  item=[SP, UN('p')])
A(id='qr', kind='act', group='prep', pos=[0, 1], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'ms'}], item=[SP, UN('p'), RN])
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='q1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, UN('p'), RN])
A(id='q1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 접근 효과 범위', 'Presence area of effect suffix'), show=['aoe'],
  edges=[{'if': {'has': 'aoe'}, 'to': 'q2', 'res': 'ok'}, {'to': 'q1', 'res': 'fail', 'hide': True}], item=[SP, AOE, RN])
A(id='q2', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 잡옵 1개 — 합금이 지울 자리', 'One junk prefix for the alloy to remove'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'q3'}], item=[SP, ALJ, AOE, RN])
A(id='q3', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Protective_Alloy', ess='ward', omens=['Omen_of_Sinistral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('접두 잡옵을 지우고 접미 룬 수호', 'The junk prefix goes for the runic ward suffix'),
  showText=[{'s': 's', 'kr': '최대 룬 수호 (제작 옵션)', 'en': 'Maximum runic ward (crafted)'}], edges=[{'to': 'q4'}], item=[SP, AOE, WD, RN])
A(id='q4', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'q5'}], item=[SP, MA, AOE, WD, RN])
A(id='q5', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션 — 에센스가 지울 자리', 'Third prefix for the essence to remove'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'q6'}], item=[SP, MA, ALJ, AOE, WD, RN])
A(id='q6', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Perfect_Essence_of_Command', ess='aura', omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접두 하나를 지우고 접미 오라 스킬의 강도', 'A prefix goes for the aura magnitude suffix'),
  showText=[{'s': 's', 'kr': '오라 스킬의 강도 (15—20)% 증가 (제작 옵션)', 'en': 'Aura Skills have (15—20)% increased Magnitudes (crafted)'}],
  edges=[{'to': 'q7'}], item=[SP, ALJ, AOE, WD, AU, RN])
A(id='q7', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션', 'Third prefix'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'q8'}],
  item=[SP, ALJ, ALD, AOE, WD, AU, RN])
A(id='q8', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 마지막 옵션(훼손) — 접두가 꽉 차 잡옵 하나가 지워짐', 'Last prefix (desecrated): the prefixes are full, so a junk prefix makes way'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'q9'}], item=[SP, ALD, UN('p'), AOE, WD, AU, RN])
A(id='q9', kind='act', group='main', pos=[0, 11.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='hyb', label=K('공개', 'Reveal'),
  goal=K('접두 정신력 + 마나 복합(훼손)', 'Spirit + mana hybrid prefix (desecrated)'), show=['hyb'],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 마지막 옵션 공개 — 나오는 대로', 'Reveal the last prefix: keep what comes'), 'showText': [{'s': 'p', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}], 'show': []}}],
  edges=[{'if': {'any': [{'added': 'hyb'}, V_ESS]}, 'to': 'ok', 'res': 'ok'}, {'to': 'x1', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SP, ALD, HY, AOE, WD, AU, RN])
# 빗나감 처리(영상 3:34~4:20): 징조 없는 소멸의 오브 — 지워진 옵션에 따라 다시 붙이고, 접근 효과가 지워지면 카오스부터
A(id='x1', kind='act', group='main', pos=[1, 11.4], act='annul', cur='Orb_of_Annulment', label=ANN, goal=ANN,
  target=K('빗나간 훼손 옵션 지우기 (징조 없음)', 'Remove the missed desecration (no omen)'),
  edges=[{'if': {'all': [{'des': False}, {'sideLt': {'side': 'p', 'n': 2}}]}, 'to': 'q7', 'res': 'ok', 'label': K('훼손 옵션·잡옵이 모두 지워짐', 'Desecration and junk both gone')},
         {'if': {'des': False}, 'to': 'q8', 'res': 'ok', 'label': K('훼손 옵션이 지워짐', 'Desecration gone')},
         {'if': {'removed': 'aura'}, 'to': 'x2', 'res': 'fail', 'label': K('오라 강도가 지워짐', 'Aura magnitude gone')},
         {'if': {'removed': 'ward'}, 'to': 'x3', 'res': 'fail', 'label': K('룬 수호가 지워짐', 'Runic ward gone')},
         {'if': {'removed': 'aoe'}, 'to': 'xc', 'res': 'fail', 'label': K('접근 효과가 지워짐', 'Presence area gone')},
         {'to': 'x1', 'res': 'fail', 'label': K('잡옵이 지워짐', 'Junk gone')}])
A(id='x2', kind='act', group='main', pos=[2, 11.4], act='essence', cur='Perfect_Essence_of_Command', ess='aura', omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('오라 강도 다시 — 접두 하나가 지워짐', 'Aura magnitude again: a prefix goes'),
  showText=[{'s': 's', 'kr': '오라 스킬의 강도 (제작 옵션)', 'en': 'Aura magnitude (crafted)'}],
  edges=[{'if': {'all': [{'des': False}, {'sideLt': {'side': 'p', 'n': 2}}]}, 'to': 'q7', 'res': 'ok'}, {'if': {'des': False}, 'to': 'q8', 'res': 'ok'}, {'to': 'x1', 'res': 'fail'}])
A(id='x3', kind='act', group='main', pos=[2, 12.4], act='essence', cur='Protective_Alloy', ess='ward', omens=['Omen_of_Sinistral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('룬 수호 다시 — 접두 하나가 지워짐', 'Runic ward again: a prefix goes'),
  showText=[{'s': 's', 'kr': '최대 룬 수호 (제작 옵션)', 'en': 'Maximum runic ward (crafted)'}],
  edges=[{'if': {'all': [{'des': False}, {'sideLt': {'side': 'p', 'n': 2}}]}, 'to': 'q7', 'res': 'ok'}, {'if': {'des': False}, 'to': 'q8', 'res': 'ok'}, {'to': 'x1', 'res': 'fail'}])
A(id='xc', kind='cleanup', group='main', pos=[1, 3.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'q1', 'label': K('카오스부터 다시', 'Back to Chaos')}])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['q7', 'q8', 'q9', 'x1', 'x2', 'x3'], 'kr': '접두 세 번째 옵션·마지막 옵션(훼손)', 'en': 'Third and last prefix (desecrated)', 'fold': True,
  'goal': K('접두 정신력 + 마나 복합(훼손) 1~2티어', 'T1–2 spirit + mana hybrid prefix (desecrated)'),
  'goalBy': {'bal': K('접두 정신력 + 마나 복합(훼손) 1~2티어', 'T1–2 spirit + mana hybrid prefix (desecrated)'),
             'ess': K('접두 마지막 옵션 공개 — 나오는 대로', 'Reveal the last prefix: keep what comes')},
  'steps': [K('상위 엑잘티드 오브로 접두 세 번째 옵션', 'Greater Exalted Orb for a third prefix') | {'node': 'q7'},
            K('좌측 강령술의 징조 + 보존된 턱뼈', 'Omen of Sinistral Necromancy + Preserved Jawbone') | {'node': 'q8'},
            K('심연의 메아리의 징조 + 공개', 'Omen of Abyssal Echoes + reveal') | {'node': 'q9'},
            K('빗나가면 소멸의 오브(징조 없음)', 'Miss: Orb of Annulment (no omen)') | {'node': 'x1'},
            K('오라 강도가 지워지면 좌측 결정화의 징조 + 완벽한 지휘의 에센스', 'Aura magnitude gone: Omen of Sinistral Crystallisation + Perfect Essence of Command') | {'node': 'x2'},
            K('룬 수호가 지워지면 좌측 결정화의 징조 + 보호의 합금', 'Runic ward gone: Omen of Sinistral Crystallisation + Protective Alloy') | {'node': 'x3'}],
  'worst': K('접근 효과 범위가 지워지면 분열 + 옵션 1개까지 지우고 카오스부터', 'Presence area gone: annul down to the fracture + one option, then Chaos again') | {'to': 'xc'},
  'item': [SP, ALD, HY, AOE, WD, AU, RN],
  'itemBy': {'bal': [SP, ALD, HY2, AOE, WD, AU, RN], 'ess': [SP, ALD, L('p', '랜덤 옵션 1개 (훼손)', 'One random option (desecrated)', 'd'), AOE, WD, AU, RN]}},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'sp', 'fr': True}, {'side': 'p', 'random': True}, {'tag': 'hy2', 'des': True},
            {'tag': 'aoe'}, {'tag': 'ward', 'ess': True}, {'tag': 'aura', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'sp', 'fr': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'aoe'}, {'tag': 'ward', 'ess': True}, {'tag': 'aura', 'ess': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
