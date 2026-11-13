# W28 2026-11-13: MazBro +5 주문 목걸이(kULlZJBSec4) 플로우차트 생성기 — 영상 성공 회차(Demon Choker) 한 줄
# 근거: scratchpad review/W28-mazbro-spell5/timeline.md, frames/ (영상 8:00~29:40 제작 구간 화면 대조, 축성 구간은 표본)
# 실행: cd scripts/graphs && python3 gen_mazbro_spell5_amulet.py  → mazbro-spell5-amulet-v2.json (gen_batch15.py 끝에서 자동 호출, 그 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/mazbro-spell5-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SPn = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'n', ['spirit'])
SP = L('p', '정신력 +(47—50) (분열)', '+(47—50) to Spirit (fractured)', 'f', ['spirit'])
MQ = L('p', '최대 퀄리티 +20% (균열의 에센스)', '+20% to Maximum Quality (Essence of the Breach)', 'c', ['mq'])
ES = L('p', '에너지 보호막 최대치 (26—30)% 증가', '(26—30)% increased maximum Energy Shield', 'j')
RW = L('p', '룬 수호 최대치 (6—10)% 증가 (룬 합금)', '(6—10)% increased maximum Runic Ward (Runic Alloy)', 'c', ['rw'])
SL = L('s', '모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills', 'n', ['spell'])
CS = L('s', '시전 속도 (25—28)% 증가 (훼손)', '(25—28)% increased Cast Speed (desecrated)', 'd', ['cs'])
J = lambda s='x': L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

FIN = K('시전 속도·치명타 확률·치명타 피해·모든 원소 저항·희귀도 1티어·모든 스킬의 퀄리티',
        'T1 cast speed, critical chance, critical damage, all elemental resistances, rarity or quality of all skills')

g = {
 'id': 'mazbro-spell5-amulet-v2', 'recipe': 'mazbro-spell5-amulet-v2', 'cls': 'Amulets', 'base': 'Absent Amulet', 'ilvl': 80,
 'note': ('2026-11-13 W28 영상 화면 대조(제작 구간 8:00~29:40 전부, 축성 구간은 표본). 성공 회차 = 영상 가이드(화면 메모 1~4단계)를 따라 '
          '훼손 공개까지 간 Demon Choker: 노멀 부재 목걸이(아이템 레벨 80, 원소 상태 이상 시 시전, 9:20) → 제왕의 오브(9:27) → 카오스로 정신력 1티어(5,000개 묶음, 10:27) → '
          '신성한 오브로 +50(10:33) → 상위 찬미의 징조 + 상위 엑잘로 옵션 2개(징조 3개 소모, 11:31) → 보존된 빗장뼈로 4개(11:51) → 분열(3개 중 2개 성공, 12:07) → '
          '소멸로 옵션 1개 → 균열의 에센스(12:27) → 쇳소리 기폭제 40%(13:20) → 카오스로 주문 +3(치명타 1티어가 떴을 때 우측 찬미 + 상위 엑잘 시도 → 화염 저항, 14:24·14:26, '
          '+3은 17:32 카오스) → 좌측 찬미 + 상위 엑잘(에너지 보호막 4티어, 27:17) → 좌측 결정화 + 룬 합금(29:13 화면 룬 수호 10%) → 고대 빗장뼈(29:20) → 공개 시전 속도 1티어(29:31). '
          '촉진 엑잘 실험(17:40~24:00)·실험 목걸이 정리(24:00~28:00)는 꿀팁 후보. 완벽한 유동체·완벽한 쥬얼러·신성한 오브(30:00~37:50)는 정책 14장대로 뺌. '
          '축성(축성의 징조 + 신성한 오브, 37:45 Hypnotic Noose +5)은 영상 제목이라 사용자 결정(2026-11-13 06:40)대로 완성 뒤 선택 단계(점선 상자, 비용 미포함). 성유(30:12 자로크의 선물)는 축성 뒤엔 못 하므로 같은 상자에 그 전에 한다고만 적음.'),
 # 2026-11-13 P13 새 정책 D: 하이엔드 404.2 / 밸런스 369.4 div(차이 8.6%) → 하이엔드만
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'high', 'params': {'v': 1}}],
 'versions': [
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'v': 1}, 'tier': 'high',
    'desc': K('영상: 마지막 접미는 좋은 옵션 1티어, 빗나가면 빛의 징조로 다시', 'Video: a good T1 last suffix, Light retries a miss')}],
 'tags': {
   'spirit': {'gi': 28, 'tmax': 1}, 'spell': {'gi': 17, 'tmax': 1}, 'mq': {'gi': 81}, 'rw': {'gi': 82},
   'cs': {'gi': 32, 'tmax': 1}, 'cr': {'gi': 24, 'tmax': 1}, 'cd': {'gi': 25, 'tmax': 1},
   'ar': {'gi': 7, 'tmax': 1}, 'rs': {'gi': 26, 'tmax': 1}, 'kq': {'gi': 46},
   'fin': {'anyOf': ['cs', 'cr', 'cd', 'ar', 'rs', 'kq'], 'shown': 'cs', 'label': FIN},
   # 카오스 단계에서 우측 찬미 + 상위 엑잘을 시도할 접미(영상 화면 메모 3단계: T1 Cast Speed/CritHit/CritDmg)
   'anc': {'anyOf': ['cs', 'cr', 'cd'], 'label': K('시전 속도·치명타 확률·치명타 피해 1티어', 'T1 cast speed, critical chance or critical damage')}},
 'require': {'all': [{'has': 'spell'}, {'has': 'rw'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'z1',
 'finals': [
   {'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
    'lines': [{'tag': 'spirit', 'fr': True}, {'tag': 'rw', 'ess': True}, {'tag': 'spell'}, {'tag': 'fin', 'des': True}]}],
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='z1', kind='base', group='prep', pos=[0, 0], next='z1r', start={'rar': 'normal', 'mods': []},
  label=K('부재 목걸이 구입 (노멀, 아이템 레벨 75 이상, 원하는 부여 스킬)', 'Buy an Absent Amulet (normal, item level 75+, the granted skill you want)'), item=[])
A(id='z1r', kind='act', group='prep', pos=[0, 1], act='regal', cur='Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'z2'}], item=[J('x')])
A(id='z2', kind='act', group='prep', pos=[0, 2], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 정신력 1티어', 'T1 Spirit prefix'), show=['spirit'],
  edges=[{'if': {'has': 'spirit'}, 'to': 'z3', 'res': 'ok'}, {'to': 'z2', 'res': 'fail', 'hide': True}], item=[SPn])
A(id='z3', kind='act', group='prep', pos=[0, 3], act='divine', cur='Divine_Orb', count=4, label=K('신성', 'Divine'),
  goal=K('정신력 +50', '+50 Spirit'), showText=[K('수치 47~50 중 50 (평균 4개)', '50 out of 47–50 (about four on average)')],
  edges=[{'to': 'z4'}], item=[SPn])
A(id='z4', kind='act', group='prep', pos=[0, 4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('옵션 두 개 더 — 분열 조건 옵션 4개', 'Two more options: the fracture needs four'), showText=[K('랜덤 옵션 2개', 'Two random options')],
  edges=[{'to': 'z5'}], item=[SPn, J('p'), J('s')])
A(id='z5', kind='act', group='prep', pos=[0, 5], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손)', 'Fourth option (desecrated)'), showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')],
  edges=[{'to': 'z6'}], item=[SPn, J('p'), J('s'), UN('s')])
A(id='z6', kind='act', group='prep', pos=[0, 6], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('정신력이 분열되면 성공', 'Success when Spirit fractures')],
  edges=[{'if': {'fractured': 'spirit'}, 'to': 'z6c', 'res': 'ok', 'label': K('정신력 분열', 'Spirit fractured')},
         {'to': 'z6x', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[SP, J('p'), J('s'), UN('s')])
A(id='z6x', kind='exit', group='prep', pos=[1, 6], simTo='z1', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='z6c', kind='cleanup', group='prep', pos=[0, 7], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[SP, J('x')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8.4], next='z7', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, J('x')])
A(id='z7', kind='act', group='main', pos=[0, 9.4], act='essence', cur='Essence_of_the_Breach', ess='mq', label=K('에센스', 'Essence'),
  goal=K('잡옵을 지우고 최대 퀄리티', 'The junk goes for max quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'z8'}], item=[SP, MQ])
A(id='z8', kind='act', group='main', pos=[0, 10.4], act='quality', cur='Sibilant_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('시전 퀄리티 40%', 'Caster quality 40%'), edges=[{'to': 'z9'}], item=[SP, MQ])
# 3단계: 카오스 스팸 + 드문 접미 1티어에 반대쪽 엑잘(접힌 상자 L0)
A(id='z9', kind='act', group='main', pos=[0, 11.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('최대 퀄리티를 지우고 접미 모든 주문 스킬 레벨 +3', 'Max quality out, +3 to Level of all Spell Skills suffix'), show=['spell'],
  edges=[{'if': {'has': 'spell'}, 'to': 'z10', 'res': 'ok'}, {'if': {'has': 'anc'}, 'to': 'c2', 'res': 'ok'}, {'to': 'z9', 'res': 'fail', 'hide': True}],
  item=[SP, SL])
A(id='c2', kind='act', group='main', pos=[1, 11.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 1티어를 두고 모든 주문 스킬 레벨 +3', 'Keep the T1 suffix, +3 Spell Skills'), show=['spell'],
  edges=[{'if': {'added': 'spell'}, 'to': 'z10', 'res': 'ok'}, {'to': 'c3', 'res': 'fail'}])
A(id='c3', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접미 지우기 — 1티어가 지워지면 카오스부터', 'Remove the missed suffix: back to Chaos if the T1 goes'),
  edges=[{'if': {'has': 'anc'}, 'to': 'c2'}, {'to': 'z9'}])
# 3단계 2·3: 접두
A(id='z10', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'z11'}], item=[SP, ES, SL])
A(id='z11', kind='act', group='main', pos=[0, 13.4], act='essence', cur='Runic_Alloy', ess='rw', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('잡옵 접두를 지우고 룬 수호 최대치 증가', 'The junk prefix goes for increased maximum Runic Ward'),
  showText=[{'s': 'p', 'kr': '룬 수호 최대치 (6—10)% 증가 (제작 옵션)', 'en': '(6—10)% increased maximum Runic Ward (crafted)'}],
  edges=[{'to': 'z12'}], item=[SP, RW, SL])
# 4단계: 마지막 접미 훼손
A(id='z12', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Ancient_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접미 두 번째 옵션(훼손)', 'Second suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  skipIf={'full': 's'}, skipTo='ok', edges=[{'to': 'z13'}], item=[SP, RW, SL, UN('s')])
A(id='z13', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='fin', label=K('공개', 'Reveal'),
  goal=K('접미 시전 속도 1티어 — 좋은 접미 여섯 중 먼저 뜬 것', 'T1 cast speed suffix: whichever of the six good suffixes lands first'),
  show=['cs', 'cr', 'cd', 'ar', 'rs', 'kq'],
  edges=[{'if': {'added': 'fin'}, 'to': 'ok', 'res': 'ok'}, {'to': 'z13x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SP, RW, SL, CS])
A(id='z13x', kind='act', group='main', pos=[1, 15.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'z12', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
# 축성 = 선택 단계(사용자 결정 2026-11-13 06:40, 영상 제목 '축성으로 +5'): 시뮬·비용에서 빠짐. 37:45 Hypnotic Noose 축성 +5
A(id='zs', kind='side', group='main', pos=[1, 16.4], attach=['ok', 'ok'], cur='Divine_Orb', omens=['Omen_of_Sanctification'],
  goal=K('축성으로 +5 노리기, 선택·비용 미포함', 'Sanctify for +5, optional, not costed'),   # 축성 뒤엔 수정 불가 — 성유는 그 전에
  label=K('축성', 'Sanctify'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L0', 'nodes': ['z9', 'c2', 'c3'], 'kr': '카오스 스팸', 'en': 'Chaos spam', 'fold': True,
  'goal': K('최대 퀄리티를 지우고 접미 모든 주문 스킬 레벨 +3', 'Max quality out, +3 to Level of all Spell Skills suffix'),
  'steps': [K('카오스 오브로 모든 주문 스킬 레벨 +3', 'Chaos Orb for +3 Spell Skills') | {'node': 'z9'},
            K('접미에 시전 속도·치명타 확률·치명타 피해 1티어가 뜨면 우측 찬미 + 상위 엑잘로 +3', 'A T1 cast speed, crit chance or crit damage suffix: Dextral Exaltation + Greater Exalt for +3') | {'node': 'c2'},
            K('빗나가면 소멸의 오브, 1티어가 남으면 다시 엑잘, 지워지면 카오스부터', 'A miss: Orb of Annulment; exalt again while the T1 stays, Chaos again once it goes') | {'node': 'c3'}],
  'item': [SP, SL]},
 {'id': 'L1', 'nodes': ['z12', 'z13', 'z13x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
