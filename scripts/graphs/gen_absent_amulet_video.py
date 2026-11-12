# W29 2026-11-13: SL 부재 목걸이 심연의 에센스(jr6-YLMJsC8) 플로우차트 생성기 — 영상 실전 회차(11:12~19:12) 한 줄
# 근거: scratchpad review/W29-absent-amulet-video/timeline.md, frames/ (영상 0:00~21:19 화면 대조)
# 실행: cd scripts/graphs && python3 gen_absent_amulet_video.py  → absent-amulet-video-v2.json (gen_batch16.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/absent-amulet-video-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SPn = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'n', ['spirit'])          # 분열 전
SP = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'f', ['spirit'])           # 분열
MQ = L('p', '최대 퀄리티 +20%', '+20% to Maximum Quality', 'c', ['mq'])
SL = L('s', '모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills', 'n', ['spell'])
ESP = L('p', '에너지 보호막 최대치 (45—50)% 증가', '(45—50)% increased maximum Energy Shield', 'n', ['esp'])   # 18:10 영상 결과
KQ = L('s', '모든 스킬의 퀄리티 +(3—5)%', '+(3—5)% to Quality of all Skills', 'd', ['kq'])
MK = lambda s: L(s, '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkp' if s == 'p' else 'mks'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
UNu = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')   # 같은 미공개 줄이 앞 상자에도 있을 때 graph2recipe가 새 줄로 읽게(접미 훼손 쪽 판단)
DJ = L('s', '소환수의 재사용 대기시간 회복 속도 (16—20)% 증가', '(16—20)% increased Minion Cooldown Recovery Rate', 'd')   # 15:15 공개 결과(자리 막기)
LIGHT = K('소멸의 오브 사용', 'Use an Orb of Annulment')
GPL = K('에너지 보호막 %·방어도 %·생명력·주문 피해', 'Energy Shield %, Armour %, Life or Spell Damage')

g = {
 'id': 'absent-amulet-video-v2', 'recipe': 'absent-amulet-video-v2', 'cls': 'Amulets', 'base': 'Absent Amulet', 'ilvl': 82,
 'note': ('2026-11-13 W29 영상 전체 화면 대조(0:00~21:19). 실전 회차 한 줄: 정신력 +50만 있는 레어 부재 목걸이 구입(11:32, 아이템 레벨 82는 14:34 툴팁) → '
          '우측 찬미 + 상위 찬미 + 완벽한 엑잘(11:39~11:53, 접미 모든 능력치·생명력 재생) → 보존된 빗장뼈(12:02) → 분열(12:18, 정신력) → 분열 + 잡옵 1개(12:40, 정리 장면은 화면에 없음) → '
          '카오스로 주문 +3(14:12, 약 2,000개) → 좌측 찬미 + 엑잘티드 오브 접두 잡옵(14:34) → 좌측 결정화 + 균열의 에센스(14:44) → 쇳소리 기폭제 40%(14:56) → '
          '검은 피의 징조 + 보존된 빗장뼈(15:05) → 메아리 공개 빗나감, 빛의 징조 없이 그대로(15:15, 슬라이드 3:48 "딱 1번만") → 절사 + 완벽한 카오스로 최대 퀄리티 → 접두 잡옵(15:25) → '
          '빛의 징조로 훼손 제거(15:35) → 좌측 결정화 + 심연의 에센스로 징표 반복(15:45~18:10: 접두 징표면 빗장뼈 + 빛의 징조 → 좌측 찬미 + 완벽한 엑잘, 접미 징표면 완벽한 엑잘) → 에너지 보호막 % 1티어(18:10) → '
          '검은 피의 징조 + 보존된 빗장뼈로 접미 징표 훼손(18:26) → 메아리 공개 반복(빗나가면 빛의 징조, 18:44) → 모든 스킬의 퀄리티(19:05). 완벽한 유동체·쥬얼러·할당·축성(19:15~20:30)은 정책 14장대로 뺌. '
          '내부 결정: 접두 목표는 영상이 멈추겠다고 말한 옵션(에너지 보호막 %·방어도 %·생명력 1티어, 14:50 주문 피해 1티어) 중 먼저 뜬 것. '
          '접미 징표 + 접두 빗나감(16:45)은 영상 화면대로 검은 피 없이 빗장뼈 + 빛의 징조(영상은 검은 피를 켜려다 실수했다고 말함). 첫 공개에서 모든 스킬의 퀄리티가 뜨는 경우는 플로우차트에 넣지 않음(시뮬은 같은 줄로 진행).'),
 'params': {'pT': {'kr': '접두 두번째 옵션', 'en': 'Second prefix', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}, {'id': 'bal', 'params': {'pT': 2}}],
 'versions': [{'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'pT': 2}, 'tier': 'bal',
               'desc': K('접두 두번째 옵션 1~2티어', 'Second prefix T1–2')},
              {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
               'desc': K('영상: 접두 두번째 옵션 1티어', 'Video: T1 second prefix')}],
 'tags': {'spirit': {'gi': 28, 'tmax': 1}, 'spell': {'gi': 17, 'tmax': 1}, 'mq': {'gi': 81}, 'kq': {'gi': 46},
          'mkp': {'gi': 79}, 'mks': {'gi': 80}, 'mark': {'anyOf': ['mkp', 'mks']},
          'esp': {'gi': 16, 'tmax': '$pT'}, 'arp': {'gi': 14, 'tmax': '$pT'}, 'lf': {'gi': 9, 'tmax': '$pT'}, 'sd': {'gi': 31, 'tmax': '$pT'},
          'gp': {'anyOf': ['esp', 'arp', 'lf', 'sd'], 'label': GPL},
          'esp1': {'gi': 16, 'tmax': 1}, 'arp1': {'gi': 14, 'tmax': 1}, 'lf1': {'gi': 9, 'tmax': 1}, 'sd1': {'gi': 31, 'tmax': 1},
          'esp2': {'gi': 16, 'tmax': 2}, 'arp2': {'gi': 14, 'tmax': 2}, 'lf2': {'gi': 9, 'tmax': 2}, 'sd2': {'gi': 31, 'tmax': 2},
          'gp1': {'anyOf': ['esp1', 'arp1', 'lf1', 'sd1'], 'label': K('에너지 보호막 %·방어도 %·생명력·주문 피해 1티어', 'T1 Energy Shield %, Armour %, Life or Spell Damage')},
          'gp2': {'anyOf': ['esp2', 'arp2', 'lf2', 'sd2'], 'label': K('에너지 보호막 %·방어도 %·생명력·주문 피해 1~2티어', 'T1–2 Energy Shield %, Armour %, Life or Spell Damage')}},
 'require': {'all': [{'has': 'spirit'}, {'has': 'spell'}, {'has': 'gp'}, {'has': 'kq'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'spirit', 'fr': True}, {'tag': 'gp1'}, {'tag': 'spell'}, {'tag': 'kq', 'des': True}]},
            {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'spirit', 'fr': True}, {'tag': 'gp2'}, {'tag': 'spell'}, {'tag': 'kq', 'des': True}]}],
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='b1', start={'rar': 'rare', 'mods': [{'tag': 'spirit'}], 'quality': 0},
  label=K('정신력 +50 부재 목걸이 구입 (아이템 레벨 82)', 'Buy a +50 Spirit Absent Amulet (item level 82)'), item=[SPn])
A(id='b1', kind='act', group='prep', pos=[0, 1], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Dextral_Exaltation', 'Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵 2개', 'Two junk suffixes'), showText=[{'s': 's', 'kr': '잡옵 2개', 'en': 'Two junk'}],
  edges=[{'to': 'b2'}], item=[SPn, J('s'), J('s')])
A(id='b2', kind='act', group='prep', pos=[0, 2], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('접두 훼손 옵션 (미공개, 분열되지 않음)', 'Prefix desecration (unrevealed, cannot fracture)')], edges=[{'to': 'pf'}],
  item=[SPn, UN('p'), J('s'), J('s')])
A(id='pf', kind='act', group='prep', pos=[0, 3], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('정신력이 분열되면 성공', 'Success when Spirit fractures')],
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'spirit'}, 'to': 'b11', 'res': 'ok', 'label': K('정신력 분열', 'Spirit fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[SP, UN('p'), J('s'), J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 3], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='b11', kind='cleanup', group='prep', pos=[0, 4], keep=[], maxJunk=1, label=LIGHT, goal=LIGHT,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[SP, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 5.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 6.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫번째 옵션', 'First suffix'), show=['spell'],
  edges=[{'if': {'has': 'spell'}, 'to': 'q1', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[SP, SL])
A(id='q1', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 잡옵', 'A junk prefix'), showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}], edges=[{'to': 'q2'}], item=[SP, J('p'), SL])
A(id='q2', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 최대 퀄리티 +20%', 'The junk prefix goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'q3'}], item=[SP, MQ, SL])
A(id='q3', kind='act', group='main', pos=[0, 9.4], act='quality', cur='Sibilant_Catalyst', count=40, label=K('퀄리티', 'Quality'),
  goal=K('시전 퀄리티 40%', 'Caster quality 40%'), showText=[K('쇳소리 기폭제 40개', '40 Sibilant Catalysts')], edges=[{'to': 'd1'}], item=[SP, MQ, SL])
A(id='d1', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_the_Blackblooded'],
  label=K('훼손', 'Desecrate'), goal=K('접미 두번째 옵션(훼손)', 'Second suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'r1'}], item=[SP, MQ, SL, UN('s')])
A(id='r1', kind='act', group='main', pos=[0, 11.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='kq', label=K('공개', 'Reveal'),
  goal=K('접미 훼손 옵션 확인 — 한 번만, 빗나가도 그대로', 'Reveal the suffix desecration: once, a miss stays'), show=['kq'],
  edges=[{'to': 'w1'}], item=[SP, MQ, SL, DJ])
A(id='w1', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('카오스', 'Chaos'),
  goal=K('최대 퀄리티를 지우고 접두 두번째 옵션', 'Maximum Quality out, second prefix'), show=['gp'],
  edges=[{'if': {'all': [{'has': 'gp'}, {'has': 'kq'}]}, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'has': 'gp'}, 'to': 's2x', 'res': 'ok', 'hide': True},
         {'to': 'm0', 'res': 'fail', 'label': K('접두 잡옵', 'Junk prefix')}],
  item=[SP, J('p'), SL, DJ])
# 접두 두번째 옵션 루프(접힘): 빛의 징조 → 좌측 결정화 + 심연의 에센스(징표 50:50) → 접두 징표: 빗장뼈 + 빛의 징조 → 좌측 찬미 + 완벽한 엑잘 / 접미 징표: 완벽한 엑잘
A(id='m0', kind='act', group='main', pos=[0, 13.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('접미 훼손 옵션 제거', 'Remove the suffix desecration'), edges=[{'to': 'm1'}], item=[SP, J('p'), SL])
A(id='m1', kind='act', group='main', pos=[0, 14.4], act='essence', cur='Essence_of_the_Abyss', ess='mkp', alt='mks', mark=True,
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접두 잡옵을 지우고 징표 — 접두·접미 반반', 'The junk prefix goes for the Mark: prefix or suffix, 50/50'),
  showText=[K('심연의 군주의 징표', 'Mark of the Abyssal Lord')],
  edges=[{'if': {'has': 'mkp'}, 'to': 'm2', 'label': K('접두 징표', 'Prefix Mark')}, {'to': 'm4', 'label': K('접미 징표', 'Suffix Mark')}],
  item=[SP, SL, MK('s')])
A(id='m2', kind='act', group='main', pos=[2, 15.4], act='desecrate', cur='Preserved_Collarbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('접두 징표 훼손', 'Desecrate the prefix Mark'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'm3'}], item=[SP, UN('p'), SL])
A(id='m3', kind='act', group='main', pos=[2, 16.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('접두 훼손 옵션 제거', 'Remove the prefix desecration'), edges=[{'to': 'm3e'}], item=[SP, SL])
A(id='m3e', kind='act', group='main', pos=[2, 17.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째 옵션', 'Second prefix'), show=['gp'],
  edges=[{'if': {'added': 'gp'}, 'to': 's1m', 'res': 'ok'}, {'to': 'm1', 'res': 'fail', 'label': K('빗나감 — 다시 심연의 에센스', 'Miss: Essence of the Abyss again')}],
  item=[SP, ESP, SL])
A(id='m4', kind='act', group='main', pos=[0, 15.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째 옵션 — 접미가 차서 접두로', 'Second prefix: the suffixes are full'), show=['gp'],
  edges=[{'if': {'added': 'gp'}, 'to': 's1m', 'res': 'ok'}, {'to': 'm5', 'res': 'fail'}],
  item=[SP, ESP, SL, MK('s')])
A(id='m5', kind='act', group='main', pos=[1, 16.4], act='desecrate', cur='Preserved_Collarbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('접미 징표 훼손', 'Desecrate the suffix Mark'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'm6'}], item=[SP, UNu('s'), J('p'), SL])
A(id='m6', kind='act', group='main', pos=[1, 17.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('접미 훼손 옵션 제거', 'Remove the suffix desecration'), edges=[{'to': 'm1'}])
# ---------------- 접미 마무리: 모든 스킬의 퀄리티 ----------------
A(id='s1m', kind='act', group='main', pos=[0, 18.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_the_Blackblooded'], fromMark=True,
  label=K('훼손', 'Desecrate'), goal=K('접미 징표 훼손', 'Desecrate the suffix Mark'),
  skipIf={'not': {'has': 'mks'}}, skipTo='s1', skipNote=K('접미 징표가 없으면 건너뜀', 'Skipped without a suffix Mark'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 's1'}], item=[SP, ESP, SL, UN('s')])
A(id='s1', kind='act', group='main', pos=[0, 19.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_the_Blackblooded'],
  label=K('훼손', 'Desecrate'), goal=K('접미 두번째 옵션(훼손)', 'Second suffix (desecrated)'),
  skipIf={'unrevSide': 's'}, skipTo='s2', skipNote=K('미공개 훼손 옵션이 있으면 건너뜀', 'Skipped with an unrevealed desecration on'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 's2'}], item=[SP, ESP, SL, UNu('s')])
A(id='s2', kind='act', group='main', pos=[0, 20.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='kq', label=K('공개', 'Reveal'),
  goal=K('접미 모든 스킬의 퀄리티', 'Quality of all Skills suffix'), show=['kq'],
  edges=[{'if': {'added': 'kq'}, 'to': 'ok', 'res': 'ok'}, {'to': 's2x', 'res': 'fail'}], item=[SP, ESP, SL, KQ])
A(id='s2x', kind='act', group='main', pos=[1, 20.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 's1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 21.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['m0', 'm1', 'm2', 'm3', 'm3e', 'm4', 'm5', 'm6'], 'kr': '접두 두번째 옵션', 'en': 'Second prefix', 'fold': True,
  'goal': K('접두 두번째 옵션 1티어 — 에너지 보호막 %·방어도 %·생명력·주문 피해 중 먼저 뜬 것', 'T1 second prefix: Energy Shield %, Armour %, Life or Spell Damage, whichever comes first'),
  'goalBy': {'high': K('접두 두번째 옵션 1티어 — 에너지 보호막 %·방어도 %·생명력·주문 피해 중 먼저 뜬 것', 'T1 second prefix: Energy Shield %, Armour %, Life or Spell Damage, whichever comes first'),
             'bal': K('접두 두번째 옵션 1~2티어 — 에너지 보호막 %·방어도 %·생명력·주문 피해 중 먼저 뜬 것', 'T1–2 second prefix: Energy Shield %, Armour %, Life or Spell Damage, whichever comes first')},
  'steps': [K('빛의 징조로 접미 훼손 옵션 제거 (처음 한 번)', 'Omen of Light removes the suffix desecration (first pass only)') | {'node': 'm0'},
            K('좌측 결정화 + 심연의 에센스로 접두 잡옵을 징표로', 'Sinistral Crystallisation + Essence of the Abyss turns the junk prefix into the Mark') | {'node': 'm1'},
            K('접두 징표 — 보존된 빗장뼈로 훼손', 'Prefix Mark: Preserved Collarbone desecrates it') | {'node': 'm2'},
            K('빛의 징조로 그 훼손 옵션 제거', 'Omen of Light removes that desecration') | {'node': 'm3'},
            K('좌측 찬미 + 완벽한 엑잘로 접두 — 빗나가면 다시 심연의 에센스', 'Sinistral Exaltation + Perfect Exalt for the prefix: a miss means the Essence of the Abyss again') | {'node': 'm3e'},
            K('접미 징표 — 완벽한 엑잘이 접두로', 'Suffix Mark: a Perfect Exalt lands on the prefix') | {'node': 'm4'},
            K('빗나가면 보존된 빗장뼈로 징표 훼손', 'On a miss, Preserved Collarbone desecrates the Mark') | {'node': 'm5'},
            K('빛의 징조로 제거, 다시 심연의 에센스', 'Omen of Light removes it, then the Essence of the Abyss again') | {'node': 'm6'}],
  'item': [SP, ESP, SL, MK('s')]},
 {'id': 'L2', 'nodes': ['s1', 's2', 's2x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
