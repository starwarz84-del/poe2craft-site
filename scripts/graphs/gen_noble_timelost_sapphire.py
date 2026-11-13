# W25 2026-11-13: 노블이 오래된 사파이어 5옵션(zEV8kWwveYQ) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W25-noble-sapphire/timeline.md, frames/ (영상 0:00~13:21 화면 대조)
# 실행: cd scripts/graphs && python3 gen_noble_timelost_sapphire.py  → noble-timelost-sapphire-v2.json (gen_batch13.py 끝에서 자동 호출, 그 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/noble-timelost-sapphire-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

RADL = L('p', '반경이 대형으로 업그레이드', 'Upgrades Radius to Large', 'n', ['radL'])
CCn = L('s', '반경 내 주요 패시브 스킬이 주문 치명타 명중 확률 (3—7)% 증가도 부여', 'Notable Passive Skills in Radius also grant (3—7)% increased Critical Hit Chance for Spells', 'n', ['cc'])
CC = dict(CCn, m='f')   # 같은 글 + 분열 표시(왼쪽 칸이 같은 옵션으로 이어서 보게)
SCD = L('s', '반경 내 주요 패시브 스킬이 주문 치명타 피해 보너스 (5—10)% 증가도 부여', 'Notable Passive Skills in Radius also grant (5—10)% increased Critical Spell Damage Bonus', 'n', ['scd'])
CD = L('s', '반경 내 주요 패시브 스킬이 치명타 피해 보너스 (5—10)% 증가도 부여', 'Notable Passive Skills in Radius also grant (5—10)% increased Critical Damage Bonus', 'n', ['cd'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개 (고대 위력적인 액체 경멸)', '+1 Suffix Modifier allowed (Ancient Potent Liquid Contempt)', 'n', ['contS'])
RAD = L('p', '반경이 매우 넓은 반경으로 업그레이드 (고대 위력적인 액체 우울)', 'Upgrades Radius to Very Large (Ancient Potent Liquid Melancholy)', 'n', ['rad'])
MANA = L('p', '반경 내 주요 패시브 스킬이 최대 마나 1% 증가도 부여 (훼손)', 'Notable Passive Skills in Radius also grant 1% increased maximum Mana (desecrated)', 'd', ['mana'])
J = lambda s='x': L(s, '잡옵', 'Junk', 'j')
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'noble-timelost-sapphire-v2', 'recipe': 'noble-timelost-sapphire-v2', 'cls': 'Time-Lost_Sapphire', 'base': 'Time-Lost Sapphire', 'ilvl': 79,
 'basePrice': {'Divine_Orb': 1},   # 1:38 거래소 매물 '우수한 오래된 사파이어 - 절멸' B/O 1 DIVINE(영상 구입 베이스)
 'note': ('2026-11-13 W25 영상 전체 화면 대조(0:00~13:21, 근거 scratchpad review/W25-noble-sapphire/timeline.md). 성공 회차 한 줄: '
          '매직 오래된 사파이어 구입(1:38 반경 대형 + 주문 치명타 명중 확률 7%, 1 div) → 제왕·엑잘로 옵션 4개(2:02) → 분열 = 주문 치명타 명중 확률(2:08, 한 번에) → '
          '소멸의 오브로 분열 + 옵션 1개(2:40) → 카오스로 주문 치명타 피해 보너스(3:20, 일반 치명타 피해가 먼저 떠도 보냄 2:52) → 엑잘 1번(접두, 3:30) → '
          '고대 위력적인 액체 경멸(3:58 성공, 5:48 실패 = 주문 치명타 피해 지워짐 → 소멸로 분열 + 옵션 1개 → 카오스부터) → 우측 찬미 + 엑잘로 치명타 피해 보너스'
          '(4:56 빗나감 = 마나 재생 → 소멸의 오브가 경멸 옵션을 지움(5:18) → 카오스(5:42, 빗나간 접미가 접두로) → 경멸 다시, 8:06 성공) → '
          '좌측 말소의 징조 + 카오스로 경멸 옵션 지우기(8:43) → 엑잘(9:13) → 반경 정리 카오스 → 고대 위력적인 액체 우울(9:26) → 보존된 두개골(9:47) → '
          '심연의 메아리 공개(10:07 빗나감 → 카오스로 훼손 옵션이 지워질 때까지 → 우울 → 두개골 반복, 11:54 최대 마나). '
          '영상과 다르게 정한 점: 두개골에 좌측 강령술의 징조(영상 화면엔 징조 활성 표시 없음, 시뮬이 한도를 넘은 접미에도 뼈를 넣어서 쪽 고정), '
          '재련된 쇳소리 기폭제 20개(12:00~13:06 퀄리티 20%)는 뺌. 2026-11-10 사용자 확정 "경멸 전 엑잘 2번"은 영상(1번)대로 되돌림 — 보고서 참고.'),
 'params': {'v': {'kr': '최대 마나', 'en': 'Maximum mana', 'values': {'1': K('나올 때까지 다시', 'Retry until it lands'), '2': K('공개 결과 그대로', 'Keep the reveal')}}},
 'strategies': [{'id': 'high', 'params': {'v': 1}}, {'id': 'bal', 'params': {'v': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 2}, 'tier': 'bal',
    'desc': K('훼손 공개 결과 그대로, 나머지는 영상대로', 'Keep the reveal, the rest as in the video')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'v': 1}, 'tier': 'high',
    'desc': K('영상: 최대 마나가 나올 때까지 카오스로 훼손 옵션을 지우고 다시', 'Video: Chaos the desecrated line away and retry until maximum mana')}],
 'tags': {'cc': {'gi': 50}, 'scd': {'gi': 16}, 'cd': {'gi': 15},
          'contS': {'gi': 84, 'slot': {'s': 1}}, 'contP': {'gi': 85, 'slot': {'p': 1}},
          'rad': {'gi': 82}, 'mana': {'gi': 69},
          'radM': {'gi': 0}, 'radL': {'gi': 1},
          'radLo': {'anyOf': ['radM', 'radL'], 'label': K('반경 중형·대형 업그레이드', 'Radius to Medium or Large')}},
 'require': {'all': [{'has': 'cc'}, {'has': 'scd'}, {'has': 'cd'}, {'has': 'rad'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'b0',
 'finals': [
   {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
    'lines': [{'tag': 'mana', 'des': True}, {'tag': 'rad'}, {'tag': 'cc', 'fr': True}, {'tag': 'scd'}, {'tag': 'cd'}]},
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'side': 'p', 'random': True}, {'tag': 'rad'}, {'tag': 'cc', 'fr': True}, {'tag': 'scd'}, {'tag': 'cd'}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
 'cap': {'p': 2, 's': 2},   # 주얼: 접두 2 · 접미 2(정책 8장)
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='p1', start={'rar': 'magic', 'mods': [{'tag': 'radL'}, {'tag': 'cc'}]},
  label=K('매직 오래된 사파이어 구입 (반경 대형 + 주문 치명타 명중 확률 7%)', 'Buy a magic Time-Lost Sapphire (Large radius + 7% spell crit chance)'),
  item=[RADL, CCn])
A(id='p1', kind='act', group='prep', pos=[0, 1], act='regal', cur='Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'p2'}], item=[RADL, J('x'), CCn])
A(id='p2', kind='act', group='prep', pos=[0, 2], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('네 번째 옵션 — 분열 조건 옵션 4개', 'Fourth option: the fracture needs four'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'pf'}], item=[RADL, J('x'), CCn, J('x')])
A(id='pf', kind='act', group='prep', pos=[0, 3], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (옵션 4개 중 하나)', 'Fracture (one of the four options)'),
  showText=[K('주문 치명타 명중 확률이 분열되면 성공', 'Success when spell crit chance fractures')],
  edges=[{'if': {'fractured': 'cc'}, 'to': 'pc', 'res': 'ok', 'label': K('주문 치명타 명중 확률 분열', 'Spell crit chance fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[RADL, J('x'), CC, J('x')])
A(id='xj', kind='exit', group='prep', pos=[1, 3], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('주문 치명타 명중 확률이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[CC, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 5.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[CC, J('s')])
A(id='c1', kind='act', group='main', pos=[0, 6.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 주문 치명타 피해 보너스', 'Spell crit damage suffix'), show=['scd'],
  skipIf={'has': 'scd'}, skipTo='e1', skipHide=True,
  edges=[{'if': {'has': 'scd'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[CC, SCD])
A(id='e1', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 옵션 1개 — 경멸이 지울 자리', 'One prefix: the line Contempt takes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 꽉 차 접두로)', 'en': 'One random option (suffixes are full)'}],
  edges=[{'to': 'k4'}], item=[J('p'), CC, SCD])
A(id='k4', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Ancient_Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개 (1/2)', '+1 Suffix Modifier allowed (1 in 2)'),
  showText=[{'s': 'p', 'kr': '접미어 속성 부여의 최대 개수 +1개', 'en': '+1 Suffix Modifier allowed'}],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'scd'}]}, 'to': 'k5', 'res': 'ok', 'label': K('접두 잡옵이 지워짐', 'The junk prefix went')},
         {'to': 'k4x', 'res': 'fail', 'label': K('주문 치명타 피해가 지워짐', 'Spell crit damage went')}],
  item=[CONT, CC, SCD])
A(id='k4x', kind='cleanup', group='main', pos=[1, 7.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'c1'}])
A(id='k5', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 치명타 피해 보너스', 'Crit damage suffix'), show=['cd'],
  edges=[{'if': {'has': 'cd'}, 'to': 'k6', 'res': 'ok'}, {'to': 'k5x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[CONT, CC, SCD, CD])
A(id='k5x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('셋 중 하나 지우기 — 빗나간 접미가 지워지면 다시 엑잘', 'One of three goes: the missed suffix going means exalt again'),
  edges=[{'if': {'not': {'has': 'contS'}}, 'to': 'k5c', 'res': 'fail', 'label': K('경멸 옵션이 지워짐', 'The Contempt line went')},
         {'if': {'not': {'has': 'scd'}}, 'to': 'k4x', 'res': 'fail', 'label': K('주문 치명타 피해가 지워짐', 'Spell crit damage went')},
         {'to': 'k5', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='k5c', kind='act', group='main', pos=[2, 9.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('빗나간 접미를 접두로 넘기기 (1/2)', 'Move the missed suffix to a prefix (1 in 2)'),
  edges=[{'if': {'has': 'scd'}, 'to': 'k4', 'res': 'ok', 'label': K('경멸 다시', 'Contempt again')},
         {'to': 'k4x', 'res': 'fail', 'label': K('주문 치명타 피해가 지워짐', 'Spell crit damage went')}])
A(id='k6', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Sinistral_Erasure'],
  label=K('좌측 말소 + 카오스', 'Sinistral Erasure + Chaos'), goal=K('경멸 옵션 지우기', 'Remove the Contempt line'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 한도를 넘어 접두로)', 'en': 'One random option (suffixes over the limit)'}],
  edges=[{'to': 'k7'}], item=[J('p'), CC, SCD, CD])
A(id='k7', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 한도를 넘어 접두로)', 'en': 'One random option (suffixes over the limit)'}],
  edges=[{'to': 'm1'}], item=[J('p'), J('p'), CC, SCD, CD])
# 최대 마나 반복: 반경·훼손 옵션 정리 카오스 → 액체 우울 → 두개골 → 공개
A(id='m1', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 반경·훼손 옵션 지우기', 'Clear the radius and desecrated prefixes'),
  target=K('반경 중형·대형과 훼손 옵션이 없어질 때까지', 'Until no Medium/Large radius and no desecrated line is left'),
  skipIf={'not': {'any': [{'has': 'radLo'}, {'desSide': 'p'}]}}, skipTo='m2', skipHide=True,
  edges=[{'if': {'any': [{'has': 'radLo'}, {'desSide': 'p'}]}, 'to': 'm1', 'res': 'fail', 'hide': True},
         {'if': {'has': 'rad'}, 'to': 'm3', 'label': K('매우 넓은 반경이 남음', 'Very Large radius kept')},
         {'to': 'm2', 'res': 'ok'}],
  item=[J('p'), J('p'), CC, SCD, CD])
A(id='m2', kind='act', group='main', pos=[0, 13.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('고대 위력적인 액체 우울 (접두 하나가 지워짐)', 'Ancient Potent Liquid Melancholy (one prefix goes)'),
  showText=[{'s': 'p', 'kr': '반경이 매우 넓은 반경으로 업그레이드', 'en': 'Upgrades Radius to Very Large'}],
  edges=[{'if': {'all': [{'has': 'mana'}, {'has': 'rad'}]}, 'to': 'ok', 'res': 'ok', 'hide': True}, {'to': 'm3', 'res': 'ok'}],
  item=[J('p'), RAD, CC, SCD, CD])
A(id='m3', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Preserved_Cranium', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 훼손 (접두 하나가 지워짐)', 'Prefix desecration (one prefix goes)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'm4'}], item=[UN, RAD, CC, SCD, CD])
A(id='m4', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='mana',
  label=K('공개', 'Reveal'), goal=K('접두 최대 마나 % 증가', 'Maximum mana % prefix'), show=['mana'],
  edges=[{'if': {'all': [{'added': 'mana'}, {'has': 'rad'}]}, 'to': 'ok', 'res': 'ok'},
         {'if': {'added': 'mana'}, 'to': 'm2', 'res': 'ok', 'label': K('반경이 지워짐 — 우울 다시 (1/2)', 'Radius gone: Melancholy again (1 in 2)')},
         {'to': 'm1', 'res': 'fail', 'label': K('빗나감 — 카오스로 훼손 옵션 지우기', 'Miss: Chaos the desecrated line away')}],
  item=[MANA, RAD, CC, SCD, CD],
  over=[{'param': {'v': 2}, 'set': {'edges': [{'if': {'has': 'rad'}, 'to': 'ok', 'res': 'ok'},
                                             {'to': 'm5', 'res': 'fail', 'label': K('반경이 지워짐', 'Radius gone')}],
                                   'show': [], 'showText': [{'s': 'p', 'kr': '공개 결과 그대로', 'en': 'Keep the reveal'}]}}])
A(id='m5', kind='act', group='main', pos=[1, 15.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('고대 위력적인 액체 우울 다시', 'Ancient Potent Liquid Melancholy again'),
  showText=[{'s': 'p', 'kr': '반경이 매우 넓은 반경으로 업그레이드', 'en': 'Upgrades Radius to Very Large'}],
  edges=[{'to': 'ok'}])
A(id='ok', kind='done', group='main', pos=[0, 16.6], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['k4', 'k5', 'k5x', 'k5c'], 'kr': '경멸 + 접미 세 번째 옵션', 'en': 'Contempt + third suffix', 'fold': True,
  'goal': K('접미어 속성 부여의 최대 개수 +1개 + 접미 치명타 피해 보너스', '+1 Suffix Modifier allowed + crit damage suffix'),
  'steps': [K('고대 위력적인 액체 경멸 — 접두 잡옵이 지워지면 성공(1/2)', 'Ancient Potent Liquid Contempt: success when the junk prefix goes (1 in 2)') | {'node': 'k4'},
            K('우측 찬미의 징조 + 엑잘티드 오브로 치명타 피해 보너스', 'Dextral Exaltation + Exalted Orb for crit damage') | {'node': 'k5'},
            K('빗나가면 소멸의 오브 — 빗나간 접미가 지워지면 다시 엑잘', 'Miss: Orb of Annulment; if the missed suffix goes, exalt again') | {'node': 'k5x'},
            K('경멸 옵션이 지워지면 카오스 오브로 빗나간 접미를 접두로 넘기고 경멸 다시', 'The Contempt line went: Chaos moves the missed suffix to a prefix, then Contempt again') | {'node': 'k5c'}],
  'worst': K('주문 치명타 피해 보너스가 지워지면 소멸의 오브로 분열 + 옵션 1개 → 카오스부터', 'Spell crit damage gone: annul to the fracture + one option, back to Chaos') | {'to': 'k4x'},
  'item': [CONT, CC, SCD, CD]},
 {'id': 'L2', 'nodes': ['m1', 'm2', 'm3', 'm4', 'm5'], 'kr': '반경 + 최대 마나', 'en': 'Radius + maximum mana', 'fold': True,
  'goal': K('접두 매우 넓은 반경 + 최대 마나 % 증가(훼손)', 'Very Large radius + maximum mana % prefix (desecrated)'),
  'goalBy': {'high': K('접두 매우 넓은 반경 + 최대 마나 % 증가(훼손)', 'Very Large radius + maximum mana % prefix (desecrated)'),
             'bal': K('접두 매우 넓은 반경 + 공개 결과 그대로', 'Very Large radius + whatever the reveal gives')},
  'steps': [K('반경 중형·대형이나 훼손 옵션이 있으면 카오스 오브로 지우기', 'Chaos away a Medium/Large radius or a desecrated line') | {'node': 'm1'},
            K('고대 위력적인 액체 우울로 매우 넓은 반경 — 공개 뒤 반경이 지워졌으면 다시', 'Ancient Potent Liquid Melancholy for the Very Large radius; again if the reveal finds it gone') | {'node': 'm2'},
            K('좌측 강령술의 징조 + 보존된 두개골 — 접두 하나가 지워짐', 'Sinistral Necromancy + Preserved Cranium: one prefix goes') | {'node': 'm3'},
            K('심연의 메아리의 징조로 공개 — 최대 마나 % 증가 노림', 'Reveal with Abyssal Echoes, aiming at maximum mana %') | {'node': 'm4'}],
  'item': [MANA, RAD, CC, SCD, CD],
  'itemBy': {'high': [MANA, RAD, CC, SCD, CD], 'bal': [L('p', '랜덤 옵션', 'Random option', 'j'), RAD, CC, SCD, CD]}},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
