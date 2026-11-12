# W18 2026-11-13: 반지깎는노인 미러 지팡이(vT482uJFESs, 9:46) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W18-mirror-staff/timeline.md, frames/ (영상 0:00~9:46 화면 대조)
# 실행: cd scripts/graphs && python3 gen_banzino_mirror_staff.py  → banzino-mirror-staff-v2.json (gen_batch25.py의 이 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/banzino-mirror-staff-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SPD = L('p', '주문 피해 (209—238)% 증가', '(209—238)% increased Spell Damage', 'f', ['spd'])
XL = L('p', '피해의 (55—60)%를 추가 번개 피해로 획득', 'Gain (55—60)% of Damage as Extra Lightning Damage', 'n', ['xl'])
XLD = L('p', '피해의 (55—60)%를 추가 번개 피해로 획득', 'Gain (55—60)% of Damage as Extra Lightning Damage', 'd', ['xl'])   # 9:26 공개 결과(훼손)
XF = L('p', '피해의 (55—60)%를 추가 화염 피해로 획득', 'Gain (55—60)% of Damage as Extra Fire Damage', 'j')                   # 6:27·7:16 절사 중 접두로 간 옵션(잡옵)
LP = L('p', '번개 피해 (209—238)% 증가', '(209—238)% increased Lightning Damage', 'n', ['light'])
MANA = L('p', '마나 최대치 +(159—178)', '+(159—178) to maximum Mana', 'd', ['mana'])                                        # 9:15 공개로 받은 마나(훼손, T5)
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['markP'])
L7 = L('s', '모든 번개 주문 스킬 레벨 +7', '+7 to Level of all Lightning Spell Skills', 'n', ['l7'])
CAST = L('s', '시전 속도 (50—52)% 증가', '(50—52)% increased Cast Speed', 'n', ['cast'])
CRIT = L('s', '주문 치명타 명중 확률 (90—109)% 증가', '(90—109)% increased Critical Hit Chance for Spells', 'n', ['crit'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
LOST = lambda tag, to: {'if': {'removed': tag}, 'to': to, 'res': 'fail', 'lost': tag, 'hide': True}
BOTH = {'all': [{'has': 'light'}, {'has': 'xl'}]}
OPENP = {'sideLt': {'side': 'p', 'n': 3}}

g = {
 'id': 'banzino-mirror-staff-v2', 'recipe': 'banzino-mirror-staff-v2', 'cls': 'Staves', 'base': 'Voltaic Staff', 'ilvl': 81,
 'note': ('2026-11-13 W18 영상 전체 화면 대조(0:00~9:46). 실제 제작 장면이 아니라 설명 영상(가중치표·엑셀·예시 아이템 툴팁)이라 예시 아이템 툴팁이 이어지는 흐름을 성공 회차로 봄: '
          '주문 피해 % 1티어 분열 전도성 지팡이(아이템 레벨 81, 퀄리티 20%, 옵션 6개 모두 찬 상태 6:27) → 카오스 오브로 모든 번개 주문 +7(5:50) → 절사로 시전 속도(6:20) → 절사로 주문 치명타(6:25, 6:40 접미 완성) '
          '— 절사 중 접두로 간 추가 번개·추가 화염 1티어를 그대로 둠(6:50, 7:16) → 좌측 결정화 + 심연의 에센스(7:13, 8:01 징조 툴팁, 1/2로 추가 화염이 지워짐) → 징표 훼손 → 공개 빗나감(8:06: 번개 피해 148%·원소 주입·추가 화염 49%) '
          '→ 빛의 징조로 훼손 옵션 제거 → 좌측 결정화 + 심연(추가 번개가 지워짐, 7:45~8:00) → 공개로 마나 최대치(8:20, 9:15 T5 166) → 완벽한 엑잘로 번개 피해 % 1티어(9:15 217) '
          '→ 빛의 징조로 마나 제거 → 빈 접두에 훼손 → 공개 추가 번개 60%(9:26) → 완성(9:39). '
          '내부 결정: 공개는 심연의 메아리의 징조와 함께(영상에서 확인 못 함), 절사와 함께 쓰는 카오스 오브는 완벽한 카오스 오브(인벤토리에 상위·완벽 카오스 오브가 보이나 어느 쪽을 썼는지 확인 못 함), '
          '뼈는 고대 턱뼈(아이콘만 보임), 번개 피해 %가 훼손으로 붙으면 남은 접두는 완벽한 엑잘로 채운 뒤 절사(영상 9:10 설명, 화면 없음). '
          '데이터 한계: 지팡이 베이스별 옵션 제한(전도성 지팡이는 번개 계열만, 영상 1:05~5:30)이 클래스 데이터에 없어 카오스 오브 단계 확률이 영상 계산보다 낮게 나옴.'),
 'params': {'pT': {'kr': '목표 티어', 'en': 'Target tier', 'values': {'1': K('1티어', 'T1')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
               'desc': K('영상: 모든 옵션 1티어', 'Video: every option at T1')}],
 'tags': {'spd': {'gi': 3, 'tmax': 1}, 'l7': {'gi': 16, 'tmax': 1}, 'cast': {'gi': 25, 'tmax': 1}, 'crit': {'gi': 26, 'tmax': 1},
          'light': {'gi': 7, 'tmax': 1}, 'xl': {'gi': 34, 'tmax': 1}, 'mana': {'gi': 1}, 'markP': {'gi': 56},
          'pg': {'anyOf': ['light', 'xl'], 'label': K('번개 피해 % 또는 추가 번개 1티어', 'T1 lightning % or extra lightning')}},
 'require': {'all': [{'has': 'spd'}, {'has': 'l7'}, {'has': 'cast'}, {'has': 'crit'}, {'has': 'light'}, {'has': 'xl'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'spd', 'fr': True}, {'tag': 'light', 'tmax': 1}, {'tag': 'xl', 'tmax': 1, 'des': True},
                       {'tag': 'l7', 'tmax': 1}, {'tag': 'cast', 'tmax': 1}, {'tag': 'crit', 'tmax': 1}]}],
 'finalItem': {'quality': 20, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
# 6:27 툴팁: 전도성 지팡이 아이템 레벨 81, 퀄리티 20%, 주문 피해 233 분열 + 옵션 6개. 분열을 잡는 과정은 영상에 없음(5:40 '주문 피해 1티어 분열로 시작'만)
A(id='h0', kind='base', group='prep', pos=[0, 0], next='ms',
  start={'rar': 'rare', 'quality': 20, 'mods': [{'tag': 'spd', 'fr': True}, {'junk': 'p'}, {'junk': 'p'}, {'junk': 's'}, {'junk': 's'}, {'junk': 's'}]},
  label=K('주문 피해 % 1티어 분열 전도성 지팡이 (아이템 레벨 81, 옵션 6개 모두 찬 상태)', 'Voltaic Staff with fractured T1 spell damage (item level 81, all six slots filled)'),
  item=[SPD, J('p'), J('p'), J('s'), J('s'), J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 0.6], next='s1', label=K('아이템 제작 시작', 'Item crafting starts'),
  item=[SPD, J('p'), J('p'), J('s'), J('s'), J('s')])
# 5:50 '카오스 오브로 번개 주문 +7', 6:05 '자리를 모두 채운 채로 돌리면 이미 있는 옵션은 다시 안 나옴'
A(id='s1', kind='act', group='main', pos=[0, 1], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫번째 옵션', 'First suffix'), show=['l7'],
  edges=[{'if': {'has': 'l7'}, 'to': 's2', 'res': 'ok'}, {'to': 's1', 'res': 'fail', 'hide': True}],
  item=[SPD, J('p'), J('p'), L7, J('s'), J('s')])
# 6:20 절사로 시전 속도 → 6:25 주문 치명타(번개 주문 +7 레벨 81, 시전 속도 80이라 절사에 안 지워짐)
A(id='s2', kind='act', group='main', pos=[0, 2], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('카오스', 'Chaos'),
  goal=K('접미 두번째 옵션', 'Second suffix'), show=['cast'], skipIf={'has': 'cast'}, skipTo='s3',
  edges=[LOST('l7', 's1'), {'if': {'has': 'cast'}, 'to': 's3', 'res': 'ok'}, {'to': 's2', 'res': 'fail', 'hide': True}],
  item=[SPD, J('p'), J('p'), L7, CAST, J('s')])
# 6:50~7:05 절사 중 새 옵션이 접두로 가서 추가 번개 1티어(레벨 80)가 붙으면 그대로 둠 → 7:16 접두 추가 번개·추가 화염
A(id='s3', kind='act', group='main', pos=[0, 3], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('카오스', 'Chaos'),
  goal=K('접미 세번째 옵션', 'Third suffix'), show=['crit'],
  edges=[LOST('l7', 's1'), LOST('cast', 's2'),
         {'if': {'all': [{'has': 'crit'}, BOTH]}, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'all': [{'has': 'crit'}, {'has': 'light'}]}, 'to': 'pT', 'res': 'ok', 'hide': True},
         {'if': {'has': 'crit'}, 'to': 'p1', 'res': 'ok'},
         {'to': 's3', 'res': 'fail', 'hide': True}],
  item=[SPD, XL, XF, L7, CAST, CRIT])
# ---- 접두 번개 피해 % 1티어 (접힌 반복, 7:13~9:20) ----
A(id='p1', kind='act', group='main', pos=[0, 4], act='essence', cur='Essence_of_the_Abyss', ess='markP', mark=True,
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접두 하나를 지우고 징표', 'One prefix goes for the Mark'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'p2'}], item=[SPD, XL, MK, L7, CAST, CRIT])
A(id='p2', kind='act', group='main', pos=[1, 4], act='desecrate', cur='Ancient_Jawbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표 훼손', 'Desecrate the Mark'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'p3'}], item=[SPD, XL, UN('p'), L7, CAST, CRIT])
A(id='p3', kind='act', group='main', pos=[1, 5], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='pg', label=K('공개', 'Reveal'),
  goal=K('접두 번개 피해 % 1티어', 'T1 lightning % prefix'), show=['light'],
  edges=[{'if': BOTH, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'all': [{'added': 'pg'}, {'full': 'p'}]}, 'to': 'pT', 'res': 'ok', 'label': K('번개 피해 % 훼손 + 접두 꽉 참', 'Lightning % desecrated, prefixes full')},
         {'if': {'added': 'pg'}, 'to': 'p5x', 'res': 'ok', 'label': K('번개 피해 % 훼손 + 빈 접두', 'Lightning % desecrated, open prefix')},
         {'if': {'all': [{'added': 'mana'}, OPENP]}, 'to': 'p5', 'res': 'ok', 'label': K('빈 접두 + 마나 최대치', 'Open prefix + maximum Mana')},
         {'to': 'p4', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SPD, MANA, L7, CAST, CRIT])
A(id='p4', kind='act', group='main', pos=[1, 6], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'),
  edges=[{'if': BOTH, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'all': [{'has': 'light'}, OPENP]}, 'to': 'd1', 'res': 'ok', 'label': K('번개 피해 % + 빈 접두', 'Lightning % + open prefix')},
         {'to': 'p1', 'res': 'fail', 'label': K('다시 결정화', 'Crystallise again')}],
  item=[SPD, LP, L7, CAST, CRIT])
# 8:20~9:15 공개에서 마나 최대치를 받아 두면 완벽한 엑잘 풀이 좁아짐(마나 가중치 1000, 8:25)
A(id='p5', kind='act', group='main', pos=[2, 5], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('빈 접두에 번개 피해 % 1티어', 'T1 lightning % into the open prefix'), show=['light'],
  edges=[{'if': {'added': 'light'}, 'to': 'p4', 'res': 'ok', 'label': K('번개 피해 % 1티어', 'T1 lightning %')},
         {'to': 'p4', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SPD, MANA, LP, L7, CAST, CRIT])
# 9:05~9:20 설명: 공개로 번개 피해 %가 붙으면 나머지 한 자리는 절사(화면 없음). 빈 접두는 절사가 채우지 못해 완벽한 엑잘을 먼저 씀(영상에 없음)
A(id='p5x', kind='act', group='main', pos=[2, 6], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('빈 접두 채우기', 'Fill the open prefix'), show=['xl'],
  edges=[{'if': BOTH, 'to': 'ok', 'res': 'ok', 'hide': True}, {'to': 'pT', 'res': 'fail', 'label': K('남은 접두는 절사로', 'Whittle the last prefix')}])
A(id='pT', kind='act', group='main', pos=[1, 7], act='chaos', cur='Perfect_Chaos_Orb', trim={'side': 'p', 'keep': 'pg', 'keepDes': True},
  label=K('카오스', 'Chaos'), goal=K('접두 남은 옵션', 'The remaining prefix'), show=['light', 'xl'],
  edges=[LOST('l7', 's1'), LOST('cast', 's2'), LOST('crit', 's3'),
         {'if': BOTH, 'to': 'ok', 'res': 'ok'}, {'to': 'pT', 'res': 'fail', 'hide': True}],
  item=[SPD, LP, XL, L7, CAST, CRIT])
# ---- 9:20~9:39 빈 접두에 훼손 → 추가 번개 ----
A(id='d1', kind='act', group='main', pos=[0, 7], act='desecrate', cur='Ancient_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'd2'}], item=[SPD, LP, UN('p'), L7, CAST, CRIT])
A(id='d2', kind='act', group='main', pos=[0, 8], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='pg', label=K('공개', 'Reveal'),
  goal=K('접두 추가 번개 1티어', 'T1 extra lightning prefix'), show=['xl'],
  edges=[{'if': BOTH, 'to': 'ok', 'res': 'ok'}, {'to': 'd3', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SPD, LP, XLD, L7, CAST, CRIT])
A(id='d3', kind='act', group='main', pos=[1, 8], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 9], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['p1', 'p2', 'p3', 'p4', 'p5', 'p5x'], 'kr': '접두 번개 피해 %', 'en': 'Lightning % prefix', 'fold': True,
  'goal': K('접두 번개 피해 % 1티어', 'T1 lightning % prefix'),
  'steps': [K('좌측 결정화 + 심연의 에센스로 접두 하나를 징표로 — 추가 번개·추가 화염이면 1/2로 추가 번개가 남음', 'Sinistral Crystallisation + Essence of the Abyss turns a prefix into the Mark: with extra lightning and extra fire, extra lightning stays half the time') | {'node': 'p1'},
            K('고대 턱뼈로 징표 훼손', 'Ancient Jawbone on the Mark') | {'node': 'p2'},
            K('심연의 메아리 공개 — 번개 피해 % 1티어', 'Reveal with Abyssal Echoes: T1 lightning %') | {'node': 'p3'},
            K('빗나가면 빛의 징조로 훼손 옵션 제거 후 1번부터', 'On a miss, Omen of Light removes the desecration, then back to step 1') | {'node': 'p4'},
            K('빈 접두가 있을 때 공개에 마나 최대치가 나오면 마나를 받고 완벽한 엑잘로 번개 피해 %, 끝나면 빛의 징조로 마나 제거', 'With an open prefix and maximum Mana on offer, take the Mana, Perfect Exalt for lightning %, then Omen of Light removes the Mana') | {'node': 'p5'},
            K('번개 피해 %가 훼손으로 붙고 빈 접두가 있으면 완벽한 엑잘로 채움', 'Lightning % as the desecration with an open prefix: Perfect Exalt fills it') | {'node': 'p5x'}],
  'item': [SPD, LP, L7, CAST, CRIT]},
 {'id': 'L2', 'nodes': ['d1', 'd2', 'd3'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
