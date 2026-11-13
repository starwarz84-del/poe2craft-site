# W12 2026-11-13: 반지깎는노인 주문 +6 부재 목걸이(Yi1u0LhJztI) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W12-absent-amulet/timeline.md, frames/ (영상 0:00~42:38 화면 대조)
# 실행: cd scripts/graphs && python3 gen_absent_amulet_spell6.py  → absent-amulet-spell6-v2.json (gen_batch20.py의 이 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/absent-amulet-spell6-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SPn = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'n', ['spirit'])          # 분열 전
SP = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'f', ['spirit'])           # 분열
MQ = L('p', '최대 퀄리티 +20%', '+20% to Maximum Quality', 'c', ['mq'])
SL = L('s', '모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills', 'n', ['spell'])
MANA = L('p', '마나 최대치 +(180—189)', '+(180—189) to maximum Mana', 'n', ['mana'])
CS = L('s', '시전 속도 (25—28)% 증가', '(25—28)% increased Cast Speed', 'd', ['cs'])
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkp'])
DEX = L('s', '민첩 +(31—33)', '+(31—33) to Dexterity', 'd')               # 28:25 공개 결과(자리 막기)
FIRE = L('s', '화염 저항 +(31—35)%', '+(31—35)% to Fire Resistance', 'd')  # 31:21 공개 결과(자리 막기)
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'absent-amulet-spell6-v2', 'recipe': 'absent-amulet-spell6-v2', 'cls': 'Amulets', 'base': 'Absent Amulet', 'ilvl': 82,
 'note': ('2026-11-13 W12 영상 전체 화면 대조(0:00~42:38). 성공 회차(맹공 심장) 한 줄: 노멀 부재 목걸이(아이템 레벨 82, 2:40) → 제왕(옵션 1개, 2:30) → 균열의 에센스(3:35) → '
          '쇳소리 기폭제 40%·바알 촉진시키는 주입기 48%(7:25, 첫 목걸이는 44%에서 타락 5:20) → 카오스로 정신력 1티어(9:22) → 접미 잡옵 → 균열의 에센스(9:46) → 접미 잡옵(9:57) → '
          '보존된 빗장뼈(10:13) → 정신력 분열(영상은 히네코라의 머리카락으로 미리 보기 12:00~19:00, 사용자 결정 11-13: 머리카락 없이 1/3, 실패하면 새 베이스) → 분열 + 잡옵 1개(20:30) → 카오스 주문 +3(20:58) → 좌측 찬미 엑잘 접두 잡옵(21:51) → '
          '좌측 결정화 + 균열의 에센스(21:55) → 주입기 50%(25:30~26:00, 영상은 히네코라로 확인 — 사용자 결정 11-13: 주입기만) → 좌측 강령술 + 보존된 빗장뼈로 최대 퀄리티 밀어내기(27:20) → 좌측 결정화 + 심연의 에센스로 징표(27:28) → '
          '보존된 빗장뼈(28:08, 훼손이 접미로) → 메아리 공개 민첩(28:25, 자리 막기) → 상위 엑잘 접두 마나(29:15 정확도 빗나감) → 빛의 징조 → 좌측 결정화 + 심연 → 빗장뼈 → 공개를 세 바퀴(30:00 번개 저항, 30:56 카오스 저항, 31:17 화염 저항), '
          '상위 엑잘 마나 최대치 1티어(31:21) → 빛의 징조 + 고대 빗장뼈 + 메아리 공개 반복으로 시전 속도(33:50). 성유·완벽한 유동체·신성한 오브·축성(22:30~42:30)은 정책 14장대로 뺌. '
          '내부 결정: 징표 단계는 공용 시뮬이 징표 자리에 훼손을 두므로 접미 징표(mks)로 계산 — 영상은 징표가 접두에 보였지만 훼손은 매번 접미에 붙음(30:28·30:56·31:16 공개 선택지가 모두 접미 옵션). '
          '접두 루프 중 시전 속도가 공개돼도 다음 빗나감에서는 영상처럼 빛의 징조로 지우고 계속함(좌측 소멸의 징조로 접두만 지우는 길은 한 번에 약 20 div라 더 비쌈 — 시뮬 비교).'),
 'params': {'pT': {'kr': '목표 티어', 'en': 'Target tier', 'values': {'1': K('1티어', 'T1')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
               'desc': K('영상: 마나 최대치·시전 속도 1티어', 'Video: T1 maximum Mana and cast speed')}],
 'tags': {'spirit': {'gi': 28, 'tmax': 1}, 'spell': {'gi': 17, 'tmax': 1}, 'mq': {'gi': 81},
          'mana': {'gi': 11, 'tmax': '$pT'}, 'cs': {'gi': 32, 'tmax': '$pT'},
          'mkp': {'gi': 79}, 'mks': {'gi': 80}},
 'require': {'all': [{'has': 'spirit'}, {'has': 'spell'}, {'has': 'mana'}, {'has': 'cs'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'spirit', 'fr': True}, {'tag': 'mana', 'tmax': 1}, {'tag': 'spell'}, {'tag': 'cs', 'tmax': 1, 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},   # 사용자 결정 11-13 02:24: 퀄리티 50%·축성 빼고 전문가로
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='b1', start={'rar': 'normal', 'mods': [], 'quality': 0},
  label=K('부재 목걸이 구입 (아이템 레벨 82)', 'Buy an Absent Amulet (item level 82)'), item=[])
A(id='b1', kind='act', group='prep', pos=[0, 1], act='regal', cur='Perfect_Regal_Orb', label=K('레어', 'Rare'),
  goal=K('레어로 (매직 단계 없음)', 'Straight to rare (no magic step)'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'b2'}], item=[J('x')])
A(id='b2', kind='act', group='prep', pos=[0, 2], act='essence', cur='Essence_of_the_Breach', ess='mq', label=K('에센스', 'Essence'),
  goal=K('랜덤 옵션을 지우고 최대 퀄리티 +20%', 'The random option goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'b5'}], item=[MQ])
A(id='b5', kind='act', group='prep', pos=[0, 5], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 정신력 1티어', 'T1 Spirit prefix'), show=['spirit'],
  edges=[{'if': {'has': 'spirit'}, 'to': 'b6', 'res': 'ok'}, {'to': 'b5', 'res': 'fail', 'hide': True}], item=[SPn])
A(id='b6', kind='act', group='prep', pos=[0, 6], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵', 'A junk suffix'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}], edges=[{'to': 'b7'}], item=[SPn, J('s')])
A(id='b7', kind='act', group='prep', pos=[0, 7], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 최대 퀄리티 +20%', 'The junk suffix goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'b8'}], item=[SPn, MQ])
A(id='b8', kind='act', group='prep', pos=[0, 8], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵', 'A junk suffix'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}], edges=[{'to': 'b9'}], item=[SPn, MQ, J('s')])
A(id='b9', kind='act', group='prep', pos=[0, 9], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('접미 훼손 옵션 (미공개, 분열되지 않음)', 'Suffix desecration (unrevealed, cannot fracture)')], edges=[{'to': 'pf'}],
  item=[SPn, MQ, J('s'), UN('s')])
# 사용자 결정 11-13: 히네코라의 머리카락 없이 분열(1/3), 정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터 (영상은 머리카락으로 미리 보기, 10:30~19:00)
A(id='pf', kind='act', group='prep', pos=[0, 10], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('정신력이 분열되면 성공', 'Success when Spirit fractures')],
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'spirit'}, 'to': 'b11', 'res': 'ok', 'label': K('정신력 분열', 'Spirit fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[SP, MQ, J('s'), UN('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 10], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='b11', kind='cleanup', group='prep', pos=[0, 11], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[SP, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 12.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 13.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫 번째 옵션', 'First suffix'), show=['spell'],
  edges=[{'if': {'has': 'spell'}, 'to': 'q1', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[SP, SL])
A(id='q1', kind='act', group='main', pos=[0, 14.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 잡옵', 'A junk prefix'), showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}], edges=[{'to': 'q2'}], item=[SP, J('p'), SL])
A(id='q2', kind='act', group='main', pos=[0, 15.4], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 최대 퀄리티 +20%', 'The junk prefix goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'm1'}], item=[SP, MQ, SL])
A(id='m1', kind='act', group='main', pos=[0, 17.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('최대 퀄리티를 훼손으로 밀어내기', 'Push out Maximum Quality with a desecration'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'm1e'}], item=[SP, UN('p'), SL])
# 공용 시뮬은 뼈가 징표 자리에 훼손을 둠. 영상은 징표가 접두에 보였지만 훼손은 매번 접미로 감 → 시뮬에서는 접미 징표(mks)로 계산해 같은 흐름이 되게 함
A(id='m1e', kind='act', group='main', pos=[0, 18.4], act='essence', cur='Essence_of_the_Abyss', ess='mks', mark=True,
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접두 훼손 옵션을 지우고 징표', 'The prefix desecration goes for the Mark'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'm1d'}], item=[SP, MK, SL])
A(id='m1d', kind='act', group='main', pos=[0, 19.4], act='desecrate', cur='Preserved_Collarbone', fromMark=True,
  label=K('훼손', 'Desecrate'), goal=K('징표 훼손 — 접미로', 'Desecrate the Mark: to the suffix'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'c1'}], item=[SP, SL, UN('s')])
A(id='c1', kind='act', group='main', pos=[0, 20.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cs', label=K('공개', 'Reveal'),
  goal=K('접미 훼손 옵션 확인 — 빗나가면 자리 막기', 'Reveal the suffix desecration: a miss stays as the blocker'), show=['cs'],
  edges=[{'to': 'm2'}], item=[SP, SL, DEX])
A(id='m2', kind='act', group='main', pos=[0, 21.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), show=['mana'],
  edges=[{'if': {'added': 'mana'}, 'to': 'm3', 'res': 'ok', 'label': K('마나 최대치 1티어', 'T1 maximum Mana')},
         {'to': 'm2l', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SP, MANA, SL, DEX])
A(id='m2l', kind='act', group='main', pos=[1, 21.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('접미 훼손 옵션 제거', 'Remove the suffix desecration'), edges=[{'to': 'm2e'}])
A(id='m2e', kind='act', group='main', pos=[1, 22.4], act='essence', cur='Essence_of_the_Abyss', ess='mks', mark=True,
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('빗나간 접두를 지우고 징표', 'The missed prefix goes for the Mark'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'm2d'}], item=[SP, MK, SL])
A(id='m2d', kind='act', group='main', pos=[1, 23.4], act='desecrate', cur='Preserved_Collarbone', fromMark=True,
  label=K('훼손', 'Desecrate'), goal=K('징표 훼손 — 접미로', 'Desecrate the Mark: to the suffix'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'm2r'}], item=[SP, SL, UN('s')])
A(id='m2r', kind='act', group='main', pos=[1, 24.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cs', label=K('공개', 'Reveal'),
  goal=K('접미 훼손 옵션 확인 — 빗나가면 자리 막기', 'Reveal the suffix desecration: a miss stays as the blocker'), show=['cs'],
  edges=[{'to': 'm2', 'label': K('다시 상위 엑잘', 'Greater Exalt again')}], item=[SP, SL, DEX])
A(id='m3', kind='act', group='main', pos=[0, 25.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('접미 자리 막기 훼손 옵션 제거', 'Remove the suffix blocker'), skipIf={'has': 'cs'}, skipTo='ok',
  skipNote=K('시전 속도 1티어가 이미 공개됐으면 건너뜀', 'Skipped if T1 cast speed was already revealed'), edges=[{'to': 'm3d'}])
A(id='m3d', kind='act', group='main', pos=[0, 26.4], act='desecrate', cur='Ancient_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접미 두 번째 옵션(훼손)', 'Second suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'm3r'}], item=[SP, MANA, SL, UN('s')])
A(id='m3r', kind='act', group='main', pos=[0, 27.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cs', label=K('공개', 'Reveal'),
  goal=K('접미 시전 속도 1티어', 'T1 cast speed suffix'), show=['cs'],
  edges=[{'if': {'added': 'cs'}, 'to': 'ok', 'res': 'ok'}, {'to': 'm3x', 'res': 'fail'}], item=[SP, MANA, SL, CS])
A(id='m3x', kind='act', group='main', pos=[1, 27.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'm3d', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 28.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['m2', 'm2l', 'm2e', 'm2d', 'm2r'], 'kr': '접두 마나 최대치', 'en': 'Maximum Mana prefix', 'fold': True,
  'goal': K('접두 마나 최대치 1티어', 'T1 maximum Mana prefix'),
  'steps': [K('상위 엑잘로 접두 마나 최대치 (접미가 막혀 접두로)', 'Greater Exalt for the Mana prefix (the suffix is blocked)') | {'node': 'm2'},
            K('빗나가면 빛의 징조로 접미 훼손 옵션 제거', 'On a miss, Omen of Light removes the suffix desecration') | {'node': 'm2l'},
            K('좌측 결정화 + 심연의 에센스로 빗나간 접두를 징표로', 'Sinistral Crystallisation + Essence of the Abyss turns the missed prefix into the Mark') | {'node': 'm2e'},
            K('보존된 빗장뼈로 징표 훼손 — 훼손은 접미로', 'Preserved Collarbone on the Mark: the desecration goes to the suffix') | {'node': 'm2d'},
            K('심연의 메아리 공개 — 시전 속도가 아니면 자리 막기, 다시 상위 엑잘', 'Reveal with Abyssal Echoes: no cast speed means a blocker, Greater Exalt again') | {'node': 'm2r'}],
  'item': [SP, MANA, SL, FIRE]},
 {'id': 'L2', 'nodes': ['m3d', 'm3r', 'm3x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
