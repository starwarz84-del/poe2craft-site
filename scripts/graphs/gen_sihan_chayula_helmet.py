# G1 2026-11-13: 시한 차율라 투구(z_r1uAYIusk, 12:18) 플로우차트 생성기 — 영상 방법 + 성공 회차 옵션
# 근거: scratchpad review/G1/sihan-chayula-helmet-v2/timeline.md, frames/ (영상 0:00~12:18 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_chayula_helmet.py  → sihan-chayula-helmet-v2.json (gen_batch22.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-chayula-helmet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(룬 문자 별 웃는 가면, 4:53~11:02)에 실제로 나온 옵션
PC = L('p', '회피 및 에너지 보호막 (92—100)% 증가 (분열)', '(92—100)% increased Evasion and Energy Shield (fractured)', 'f', ['pct'])
HY = L('p', '회피 및 에너지 보호막 (39—42)% 증가 / 생명력 최대치 +(42—49)', '(39—42)% increased Evasion and Energy Shield / +(42—49) to maximum Life', 'n', ['hyb'])
FL = L('p', '회피 +(79—94) / 에너지 보호막 최대치 +(26—29) (훼손)', '+(79—94) to Evasion Rating / +(26—29) to maximum Energy Shield (desecrated)', 'd', ['flat'])
DF = L('s', '회피의 (21—23)%와 동일한 튕겨내기 평점 획득', 'Gain Deflection Rating equal to (21—23)% of Evasion Rating', 'n', ['defl'])
RS = L('s', '랜덤 옵션', 'Random option', 'j')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V1 = {'param': {'v': 1}}; V2 = {'param': {'v': 2}}

g = {
 'id': 'sihan-chayula-helmet-v2', 'recipe': 'sihan-chayula-helmet-v2', 'cls': 'Helmets_dex_int', 'base': 'Grinning Mask', 'ilvl': 82, 'basePrice': {},
 'note': ('2026-11-13 G1 영상 전체 화면 대조. 영상 방법(0:00~2:30·4:10 "원래는") + 성공 회차 옵션(룬 문자 별 웃는 가면 4:53~11:02). '
          '영상은 분열 준비(매직 가면·훼손 → 분열)가 세 번 실패해(3:30~4:05) 분열 없이 만들었지만, 방법 설명대로 회피 및 에너지 보호막 % 1티어 분열 + 잡옵 1개 베이스 구입부터 시작. '
          '성공 회차 순서: 회피 및 에너지 보호막 93% 1티어(4:53) → 상위 찬미 + 완벽한 엑잘로 접미 2개(5:13~5:22, 튕겨내기 22% 1티어 · 번개 저항 → 공허 유동체로 카오스 저항 7:00~7:12) → '
          '완벽한 엑잘 접두(7:32 마나 최대치 빗나감) → 고대 갈비뼈(8:06) → 메아리 공개 빗나감(8:16~8:32, 회피 및 에너지 보호막 % + 마나) → 소멸의 오브(9:00, 마나 지워짐) → 완벽한 엑잘(9:26 회피 및 에너지 보호막 % + 생명력 1티어) → '
          '빛의 징조 + 소멸, 고대 갈비뼈(10:00~10:16) → 메아리 공개(10:30~10:48, 회피·에너지 보호막 최대치 1티어). '
          '튕겨내기는 영상 방법대로 카오스 오브(1:00), 성공 회차는 엑잘로 떴음. 등급(난이도 3 = 밸런스·에센셜, C17): 밸런스 = 튕겨내기·접두 엑잘·공개 1~2티어, 공개 빗나감은 빛의 징조로 다시. '
          '에센셜 = 튕겨내기 1~4티어, 접두 엑잘·공개 결과 그대로(빛의 징조 없음). 접미 나머지 두 옵션은 영상대로 랜덤(2:20).'),
 'params': {
  'dT': {'kr': '튕겨내기 평점', 'en': 'Deflection', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}},
  'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('반복', 'Repeat'), '2': K('결과 그대로', 'As it comes')}},
 },
 'strategies': [{'id': 'bal', 'params': {'dT': 2, 'v': 1}}, {'id': 'ess', 'params': {'dT': 4, 'v': 2}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'dT': 4, 'v': 2}, 'tier': 'ess',
   'desc': K('튕겨내기 1~4티어, 접두 엑잘과 공개 결과 그대로', 'T1–4 deflection; prefix exalt and reveal kept as they come')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'dT': 2, 'v': 1}, 'tier': 'bal',
   'desc': K('영상: 튕겨내기·회피 및 에너지 보호막 % + 생명력·회피와 에너지 보호막 최대치 1~2티어', 'Video: T1–2 deflection, evasion/ES % + life and flat evasion/ES')}],
 'tags': {
  'pct': {'gi': 9, 'tmax': 1}, 'defl': {'gi': 21, 'tmax': '$dT'}, 'defl2': {'gi': 21, 'tmax': 2}, 'defl4': {'gi': 21, 'tmax': 4},
  'hyb': {'gi': 10, 'tmax': 2}, 'flat': {'gi': 8, 'tmax': 2},
 },
 'require': {'all': [{'has': 'pct'}, {'has': 'defl'}, {'full': 'p'}, {'full': 's'}, {'any': [V2, {'all': [{'has': 'hyb'}, {'has': 'flat'}]}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 0, 'sockets': 1},
 'finals': [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'pct', 'fr': True}, {'tag': 'hyb'}, {'tag': 'flat', 'des': True},
             {'tag': 'defl2'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'pct', 'fr': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
             {'tag': 'defl4'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
}

N = []
RP = L('p', '랜덤 옵션', 'Random option', 'j')
RPD = L('p', '랜덤 옵션 (공개된 훼손 옵션)', 'Random option (revealed desecration)', 'j')
def A(**kw):
    # 에센셜은 접두 엑잘·공개 결과 그대로 — 왼쪽 아이템 칸을 랜덤 옵션으로
    it = kw.get('item', [])
    if HY in it or FL in it:
        o = next((x for x in kw.setdefault('over', []) if x['param'] == {'v': 2}), None)
        if not o: o = {'param': {'v': 2}, 'set': {}}; kw['over'].append(o)
        o['set']['item'] = [RP if x is HY else RPD if x is FL else x for x in it]
    N.append(kw)

# ---------------- 베이스템 완성 (영상 0:40 방법 — 영상 자체 분열은 3:30~4:05에 세 번 실패) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms',
  start={'rar': 'rare', 'mods': [{'tag': 'pct', 'fr': True}, {'junk': 's'}]},
  label=K('웃는 가면 구입 (아이템 레벨 82, 회피 및 에너지 보호막 % 1티어 분열 + 잡옵 1개)',
          'Buy a Grinning Mask (item level 82, fractured T1 evasion and energy shield % + one junk option)'),
  item=[PC, J('s')])

# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='h2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PC, J('s')])
# 1:00 카오스로 접미 튕겨내기 평점(성공 회차 결과 5:22 튕겨내기 22% 1티어)
A(id='h2', kind='act', group='main', pos=[0, 2.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫 번째 옵션 — 튕겨내기 평점', 'First suffix: deflection rating'), show=['defl'],
  edges=[{'if': {'has': 'defl'}, 'to': 'h7', 'res': 'ok'}, {'to': 'h2', 'res': 'fail', 'hide': True}], item=[PC, DF])
# 5:16 상위 찬미의 징조(10/10) + 5:13 완벽한 엑잘(12/20) → 5:22 접미 2개(번개 저항·튕겨내기). 영상 2:20 "나머지 두 줄은 랜덤"
A(id='h7', kind='act', group='main', pos=[0, 3.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation', 'Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션', 'Second and third suffixes'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'h4'}], item=[PC, DF, RS, RS])
# 7:32 완벽한 엑잘(접두, 마나 최대치 빗나감) → 9:00 소멸의 오브(마나 지워짐) → 9:26 완벽한 엑잘 = 회피 및 에너지 보호막 % + 생명력 1티어
A(id='h4', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 회피 및 에너지 보호막 % + 생명력', 'Second prefix: evasion/ES % + life'), show=['hyb'],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접두 두 번째 옵션', 'Second prefix'), 'show': [], 'showText': [{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}]}}],
  edges=[{'if': V2, 'to': 'h5', 'res': 'ok', 'hide': True}, {'if': {'has': 'hyb'}, 'to': 'h5', 'res': 'ok'},
         {'to': 'h4x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[PC, HY, DF, RS, RS])
A(id='h4x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'if': {'not': {'has': 'defl'}}, 'to': 'h4c', 'res': 'fail', 'label': K('튕겨내기가 지워짐', 'Deflection gone')},
         {'if': {'all': [{'sideLt': {'side': 'p', 'n': 2}}, {'full': 's'}]}, 'to': 'h4', 'res': 'ok', 'label': K('빗나간 접두가 지워짐', 'Missed prefix gone')},
         {'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'h4s', 'res': 'fail', 'label': K('접미 랜덤 옵션이 지워짐', 'A random suffix gone')},
         {'to': 'h4x', 'res': 'fail', 'hide': True}])
A(id='h4s', kind='act', group='main', pos=[1, 5.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 빈자리 채우기', 'Refill the empty suffix'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'if': {'full': 's'}, 'to': 'h4', 'res': 'ok'}, {'to': 'h4s', 'res': 'fail', 'hide': True}])
A(id='h4c', kind='cleanup', group='main', pos=[1, 6.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'h2', 'res': 'fail', 'label': K('카오스부터', 'Back to Chaos')}])
# 8:06·10:12 고대 갈비뼈(접미가 꽉 차 접두로)
A(id='h5', kind='act', group='main', pos=[0, 7.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'h6'}], item=[PC, HY, UN('p'), DF, RS, RS])
# 8:16→8:22·10:30→10:48 메아리로 선택지 다시(빗나감 8:32, 성공 10:48 회피 +82 / 에너지 보호막 +27)
A(id='h6', kind='act', group='main', pos=[0, 8.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='flat', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 회피·에너지 보호막 최대치', 'Third prefix (desecrated): flat evasion and energy shield'), show=['flat'],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), 'show': [], 'showText': [{'s': 'p', 'kr': '공개 결과 그대로', 'en': 'Keep the reveal'}]}}],
  edges=[{'if': V2, 'to': 'ok', 'res': 'ok', 'hide': True}, {'if': {'added': 'flat'}, 'to': 'ok', 'res': 'ok'},
         {'to': 'h6x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[PC, HY, FL, DF, RS, RS])
A(id='h6x', kind='act', group='main', pos=[1, 8.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'h5', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 9.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['h4', 'h4x', 'h4s', 'h4c'], 'kr': '접두 두 번째 옵션', 'en': 'Second prefix', 'fold': True,
  'goal': K('접두 두 번째 옵션 — 회피 및 에너지 보호막 % + 생명력', 'Second prefix: evasion/ES % + life'),
  'goalBy': {'bal': K('접두 두 번째 옵션 — 회피 및 에너지 보호막 % + 생명력 1~2티어', 'Second prefix: T1–2 evasion/ES % + life'),
             'ess': K('접두 두 번째 옵션 — 랜덤 옵션', 'Second prefix: random option')},
  'steps': [K('완벽한 엑잘티드 오브로 접두 하나', 'Perfect Exalted Orb for one prefix') | {'node': 'h4'},
            K('빗나가면 소멸의 오브, 빗나간 접두가 남으면 한 번 더', 'A miss: Orb of Annulment, again while the missed prefix stays') | {'node': 'h4x'},
            K('접미 랜덤 옵션이 지워지면 우측 찬미의 징조 + 엑잘티드 오브로 접미 3개까지 채움', 'Random suffixes gone: Omen of Dextral Exaltation + Exalted Orb until three suffixes') | {'node': 'h4s'},
            K('튕겨내기가 지워지면 분열 + 옵션 1개까지 소멸의 오브', 'Deflection gone: annul down to the fracture + one option') | {'node': 'h4c'}],
  'worst': {'kr': '튕겨내기가 지워지면 카오스 단계부터', 'en': 'Deflection gone: back to the Chaos step', 'to': 'h2'},
  'item': [PC, HY, DF, RS, RS], 'itemBy': {'ess': [PC, RP, DF, RS, RS]}},
 {'id': 'L2', 'nodes': ['h5', 'h6', 'h6x'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
