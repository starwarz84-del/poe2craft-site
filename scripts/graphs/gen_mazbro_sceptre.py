# W16 2026-11-13: MazBro BiS 셉터(UwzsARlgaFM) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W16-sceptre/timeline.md, frames/ (영상 0:00~59:50 화면 대조, 14:00~41:00 실패 회차는 자막 + 일부 화면)
# 실행: cd scripts/graphs && python3 gen_mazbro_sceptre.py  → mazbro-sceptre-v2.json (gen_batch21.py의 이 아이템 구간을 대신함)
# C4 2026-11-13(사용자 확정 15:21 ①): 하이엔드는 영상에 없어도 훼손 공개 빛의 징조 반복 유지 → 공개(b3)가 좋은 접미 1티어가 아니면
#   빛의 징조 + 소멸의 오브(bx)로 훼손 옵션만 지우고 보존된 턱뼈로 다시 훼손(bd) → 공개. 영상의 '빗나가면 자리 막기'(50:56·56:35)는 꿀팁 후보로 보고.
# D1 2026-11-13(사용자 확정 15:42 ①): 난이도 표 4(전문가) → 하이엔드·밸런스. 밸런스(C17): 비싼 반복 자리(정신력 상위 엑잘 + 소멸, 접미 완벽한 엑잘·에센스·합금·훼손 공개)는 1~2티어,
#   싸게 돌리는 자리(아군 피해 매직 단계, 마나 최대치 카오스)는 1티어 그대로. 훼손 공개 빗나감은 영상대로 자리 막기로 둠(빛의 징조는 영상에 없어 하이엔드만, 15:21 ①).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/mazbro-sceptre-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

DMn = L('p', '존재 범위 내 아군이 주는 피해 (105—119)% 증가', 'Allies in your Presence deal (105—119)% increased Damage', 'n', ['dmg'])
DM = L('p', '존재 범위 내 아군이 주는 피해 (105—119)% 증가 (분열)', 'Allies in your Presence deal (105—119)% increased Damage (fractured)', 'f', ['dmg'])
MA = L('p', '마나 최대치 +(150—164)', '+(150—164) to maximum Mana', 'n', ['mana'])
SP = L('p', '정신력 (61—65)% 증가', '(61—65)% increased Spirit', 'n', ['sp'])
AS = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
AUG = L('s', '장착 증강 아이템 효과 (20—30)% 증가 (군왕의 합금)', '(20—30)% increased effect of Socketed Augment Items (Sovereign Alloy)', 'c', ['aug'])
RG = L('s', '마나 재생 속도 (60—69)% 증가', '(60—69)% increased Mana Regeneration Rate', 'd', ['regen'])
CS = L('s', '존재 범위 내 아군의 시전 속도 (17—20)% 증가', 'Allies in your Presence have (17—20)% increased Cast Speed', 'n', ['cs'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'mazbro-sceptre-v2', 'recipe': 'mazbro-sceptre-v2', 'cls': 'Sceptres', 'base': 'Stoic Sceptre', 'ilvl': 82,
 'note': ('2026-11-13 W16 영상 전체 화면 대조. 성공 회차(Brood Crack) 한 줄: 노멀 엄숙한 셉터(아이템 레벨 82, 증강 소켓 2개, 2:00) → 완벽한 진화·완벽한 확장 + 소멸의 오브 반복으로 '
          '아군 피해 1티어 매직(2:10~8:10) → 완벽한 제왕(8:24) → 좌측 강령술 + 보존된 턱뼈로 접두 훼손(10:40~11:15) → 분열 1/3(11:35, 셉터 4개 중 Brood Crack 성공) → '
          '아스트리드의 창의성(25:50) → 소멸의 오브로 분열 + 옵션 1개(23:30) → 카오스로 마나 최대치 1티어(41:49) → 좌측 찬미 + 상위 엑잘로 정신력 증가 1티어(41:51) → '
          '접미는 완벽한 엑잘 하나씩, 빗나가면 우측 결정화 + 군왕의 합금·우측 결정화 + 심연의 에센스(징표 → 보존된 턱뼈 → 심연의 메아리 공개)·우측 소멸의 징조 + 소멸의 오브(48:40~57:52) → '
          '마나 재생 속도 1티어(훼손 공개 57:45)·아군 시전 속도 1티어(완벽한 엑잘 57:52)·장착 증강 효과(합금)로 완성. '
          '신성한 오브(8:40·9:30 분열 전 아군 피해 119%, 58:50 마무리)·바알 신비학자의 식각기·완벽한 유동체·완벽한 쥬얼러 오브(59:20~59:40)는 정책 14장대로 뺌. '
          '사용자 결정 11-13: 영상 계획대로 정신력은 정신력 증가·정신력과 마나 최대치 1티어 중 먼저 뜬 것, 접미는 마나 재생 속도·시전 속도·존재 범위·치명타 확률·치명타 피해 1티어 중 둘(3:00·16:00 계획). 상자·왼쪽 칸은 성공 회차 옵션. '
          '훼손 공개가 좋은 접미 1티어가 아니면 하이엔드라 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 다시 훼손(사용자 확정 11-13 15:21, 영상은 빗나간 공개를 자리 막기로 둠).'),
 'params': {'pT': {'kr': '목표 티어', 'en': 'Target tier', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}, {'id': 'bal', 'params': {'pT': 2}}],
 'versions': [{'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'pT': 2}, 'tier': 'bal',
               'desc': K('정신력·접미 좋은 옵션 1~2티어, 훼손 공개가 빗나가면 자리 막기로 둠', 'T1–2 Spirit and good suffixes, a missed reveal stays as the blocker')},
              {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
               'desc': K('영상: 접두 1티어 2개 + 접미 1티어 2개 + 장착 증강 효과', 'Video: two T1 prefixes, two T1 suffixes + socketed augment effect')}],
 'tags': {'dmg': {'gi': 10, 'tmax': 1}, 'mana': {'gi': 3, 'tmax': 1}, 'sp': {'gi': 19, 'tmax': '$pT'},
          'hyb': {'gi': 20, 'tmax': '$pT'}, 'regen': {'gi': 13, 'tmax': '$pT'}, 'cs': {'gi': 15, 'tmax': '$pT'}, 'aoe': {'gi': 21, 'tmax': '$pT'},
          'cr': {'gi': 16, 'tmax': '$pT'}, 'cd': {'gi': 17, 'tmax': '$pT'}, 'aug': {'gi': 34}, 'mkS': {'gi': 28},
          'spi': {'anyOf': ['sp', 'hyb'], 'shown': 'sp', 'label': K('정신력 증가·정신력과 마나 최대치 1티어', 'T1 increased Spirit or Spirit and Mana')},
          'sg': {'anyOf': ['regen', 'cs', 'aoe', 'cr', 'cd'], 'shown': ['regen', 'cs'], 'label': K('마나 재생 속도·시전 속도·존재 범위·치명타 확률·치명타 피해 1티어', 'T1 mana regeneration, cast speed, presence area, critical chance or critical damage')},
          'keepS': {'anyOf': ['regen', 'cs', 'aoe', 'cr', 'cd', 'aug']}},   # 사용자 결정 11-13: 영상 계획대로 넓게, 먼저 뜬 것
 'require': {'all': [{'has': 'dmg'}, {'has': 'mana'}, {'has': 'spi'}, {'has': 'aug'}, {'count': {'tag': 'sg', 'min': 2}}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'dmg', 'fr': True}, {'tag': 'mana'}, {'tag': 'spi'}, {'tag': 'aug', 'ess': True}, {'tag': 'sg'}, {'tag': 'sg'}]},
            {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'dmg', 'fr': True}, {'tag': 'mana'}, {'tag': 'spi'}, {'tag': 'aug', 'ess': True}, {'tag': 'sg'}, {'tag': 'sg'}]}],   # 사용자 결정 11-13: fincheck가 걸리는 줄은 anyOf label로(성공 회차는 정신력 증가·마나 재생 속도(훼손)·시전 속도)
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)

# 매직 단계: 아군 피해가 없으면 접두가 차 있을 때 소멸의 오브, 비어 있으면 확장 (영상 7:30 설명)
def MG(vis):
    out = []
    for e in [{'if': {'all': [{'has': 'dmg'}, {'full': 's'}]}, 'to': 'p3'}, {'if': {'has': 'dmg'}, 'to': 'p2'},
              {'if': {'full': 'p'}, 'to': 'p2x'}, {'to': 'p2'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# 접미 반복: 단계마다 아이템 상태를 다시 봄 (영상 44:30 노트: 완벽한 엑잘 하나씩, 빗나가면 심연의 에센스, 훼손으로 자리 막기 / 47:30 합금)
def RS(vis):
    js = {'junk': {'side': 's', 'tag': 'keepS'}}
    out = []
    for e in [{'if': {'unrevSide': 's'}, 'to': 'b3'}, {'if': {'has': 'mkS'}, 'to': 'b2'},
              {'if': {'all': [{'has': 'aug'}, {'count': {'tag': 'sg', 'min': 2}}]}, 'to': 'ok'},
              {'if': {'all': [{'any': [js, {'full': 's'}]}, {'not': {'has': 'aug'}}]}, 'to': 'aL'},
              {'if': {'all': [js, {'des': False}]}, 'to': 'mA'},
              {'if': {'any': [js, {'full': 's'}]}, 'to': 'da'},
              {'to': 's1'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='p1', start={'rar': 'normal', 'mods': []},
  label=K('엄숙한 셉터 구입 (아이템 레벨 82, 증강 소켓 2개)', 'Buy a Stoic Sceptre (item level 82, two augment sockets)'), item=[])
A(id='p1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=MG({'p2': {}}), item=[J('x')])
A(id='p2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 아군 피해 1티어', 'T1 ally damage prefix'), show=['dmg'],
  edges=MG({'p3': {'res': 'ok'}, 'p2x': {'res': 'fail', 'label': K('다른 접두', 'Another prefix')}}), item=[DMn, J('s')])
A(id='p2x', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'), edges=MG({'p2': {'label': K('다시 확장', 'Augment again')}}))
A(id='p3', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'p4'}], item=[DMn, J('s'), J('x')])
A(id='p4', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('접두 훼손 옵션 (미공개, 분열되지 않음)', 'Prefix desecration (unrevealed, cannot fracture)')],
  edges=[{'if': {'has': 'dmg'}, 'to': 'pf'}, {'to': 'xj', 'hide': True}], item=[DMn, UN('p'), J('s'), J('x')])
A(id='pf', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('아군 피해가 분열되면 성공', 'Success when ally damage fractures')],
  edges=[{'if': {'fractured': 'dmg'}, 'to': 'pc', 'res': 'ok', 'label': K('아군 피해 분열', 'Ally damage fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[DM, UN('p'), J('s'), J('x')])
A(id='xj', kind='exit', group='prep', pos=[1, 5], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('아군 피해가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[DM, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='r1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[DM, J('s')])
A(id='r1', kind='act', group='main', pos=[0, 8.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'c1'}], item=[DM, J('s'), AS])
A(id='c1', kind='act', group='main', pos=[0, 9.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 마나 최대치 1티어', 'T1 maximum Mana prefix'), show=['mana'],
  edges=[{'if': {'has': 'mana'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[DM, MA, AS])
A(id='e1', kind='act', group='main', pos=[0, 10.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 정신력 증가 1티어 — 정신력과 마나 최대치 1티어와 함께 먼저 뜬 것', 'T1 increased Spirit prefix: or T1 Spirit and Mana, whichever lands first'), show=['sp', 'hyb'],
  goalBy={'bal': K('접두 정신력 증가 1~2티어 — 정신력과 마나 최대치 1~2티어와 함께 먼저 뜬 것', 'T1–2 increased Spirit prefix: or T1–2 Spirit and Mana, whichever lands first')},
  edges=[{'if': {'has': 'spi'}, 'to': 's1', 'res': 'ok'}, {'to': 'e1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[DM, MA, SP, AS])
A(id='e1x', kind='act', group='main', pos=[1, 10.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기 — 마나 최대치가 지워지면 카오스부터', 'Remove the missed prefix: back to Chaos if maximum Mana goes'),
  edges=[{'if': {'not': {'has': 'mana'}}, 'to': 'c1', 'res': 'fail', 'label': K('마나 최대치가 지워짐', 'Maximum Mana gone')},
         {'to': 'e1', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='s1', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 옵션 하나 — 좋은 접미 다섯 중 먼저 뜬 것', 'One suffix: whichever of the five good suffixes lands first'), show=['regen', 'cs', 'aoe', 'cr', 'cd'],
  edges=RS({'ok': {'res': 'ok'}, 'aL': {'res': 'fail'}, 'mA': {'res': 'fail'}, 'da': {'res': 'fail'}}), item=[DM, MA, SP, CS, AS])
A(id='aL', kind='act', group='main', pos=[1, 11.4], act='essence', cur='Sovereign_Alloy', ess='aug', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('빗나간 접미를 지우고 장착 증강 아이템 효과', 'The missed suffix goes for socketed augment effect'),
  showText=[{'s': 's', 'kr': '장착 증강 아이템 효과 (20—30)% 증가 (제작 옵션)', 'en': '(20—30)% increased effect of Socketed Augment Items (crafted)'}],
  edges=RS({'s1': {}}), item=[DM, MA, SP, AUG, AS])
A(id='mA', kind='act', group='main', pos=[1, 12.4], act='essence', cur='Essence_of_the_Abyss', ess='mkS', mark=True, omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('빗나간 접미를 지우고 심연의 군주의 징표', 'The missed suffix goes for the Mark of the Abyssal Lord'),
  showText=[{'s': 's', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=RS({'b2': {}}),
  item=[DM, MA, SP, AUG, L('s', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkS']), AS])
A(id='b2', kind='act', group='main', pos=[1, 13.4], act='desecrate', cur='Preserved_Jawbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('접미 징표 훼손', 'Desecrate the suffix Mark'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=RS({'b3': {}}), item=[DM, MA, SP, AUG, UN('s'), AS])
A(id='b3', kind='act', group='main', pos=[1, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='sg', label=K('공개', 'Reveal'),
  goal=K('접미 좋은 옵션 1티어 — 마나 재생 속도·시전 속도·존재 범위·치명타 중 먼저 뜬 것', 'A good T1 suffix: whichever of mana regeneration, cast speed, presence area or critical lands first'), show=['regen', 'cs', 'aoe'],
  goalBy={'bal': K('접미 좋은 옵션 1~2티어 — 빗나가면 자리 막기로 둠', 'A good T1–2 suffix: a miss stays as the blocker')},
  over=[{'param': {'pT': 2}, 'set': {'edges': RS({'s1': {}})}}],   # 밸런스: 영상(50:56·56:35)처럼 빗나간 공개는 자리 막기 — 빛의 징조 반복 없음
  edges=[{'if': {'not': {'added': 'sg'}}, 'to': 'bx', 'res': 'fail', 'label': K('빗나감', 'Miss')}] + RS({'s1': {'res': 'ok'}}), item=[DM, MA, SP, AUG, RG, AS])
A(id='bx', kind='act', group='main', pos=[2, 14.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'bd', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='bd', kind='act', group='main', pos=[2, 13.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접미 빈자리 훼손', 'Desecrate the free suffix'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'b3'}], item=[DM, MA, SP, AUG, UN('s'), AS])
A(id='da', kind='act', group='main', pos=[2, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=ANN, goal=ANN,
  target=K('접미 하나 지우기', 'Remove one suffix'), edges=RS({'s1': {'res': 'ok'}}))
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['s1', 'aL', 'mA', 'b2', 'b3', 'bx', 'bd', 'da'], 'kr': '접미 세 자리', 'en': 'Three suffixes', 'fold': True,
  'goal': K('접미 좋은 옵션 1티어 2개 + 장착 증강 아이템 효과 — 마나 재생 속도·시전 속도·존재 범위·치명타 중 먼저 뜬 것', 'Two good T1 suffixes + socketed augment effect: whichever of mana regeneration, cast speed, presence area or critical lands first'),
  'goalBy': {'bal': K('접미 좋은 옵션 1~2티어 2개 + 장착 증강 아이템 효과 — 마나 재생 속도·시전 속도·존재 범위·치명타 중 먼저 뜬 것', 'Two good T1–2 suffixes + socketed augment effect: whichever of mana regeneration, cast speed, presence area or critical lands first')},
  'steps': [K('완벽한 엑잘로 접미 하나 — 남은 옵션 중 먼저 뜬 것', 'Perfect Exalt one suffix: whichever wanted option lands first') | {'node': 's1'},
            K('빗나감에 장착 증강 효과가 없으면 우측 결정화 + 군왕의 합금', 'On a miss without the augment effect: Dextral Crystallisation + Sovereign Alloy') | {'node': 'aL'},
            K('훼손 옵션이 없으면 우측 결정화 + 심연의 에센스로 징표', 'No desecration yet: Dextral Crystallisation + Essence of the Abyss for the Mark') | {'node': 'mA'},
            K('보존된 턱뼈로 징표 훼손', 'Preserved Jawbone on the Mark') | {'node': 'b2'},
            K('심연의 메아리 공개 — 좋은 접미 중 먼저 뜬 것', 'Reveal with Abyssal Echoes: whichever good suffix lands first') | {'node': 'b3'},
            K('빗나가면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 보존된 턱뼈로 다시 훼손', 'A miss: Omen of Light + Orb of Annulment removes only the desecration, then Preserved Jawbone again') | {'node': 'bx'},
            K('그 밖의 빗나감은 우측 소멸의 징조 + 소멸의 오브', 'Any other miss: Omen of Dextral Annulment + Orb of Annulment') | {'node': 'da'}],
  'item': [DM, MA, SP, AUG, RG, CS, AS]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
