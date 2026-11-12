# W23 2026-11-13: Master T 5옵션 오래된 에메랄드(GNNkhSENp6Q) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W23-mastert-emerald/timeline.md, frames/ (영상 0:00~35:12 화면 대조)
# 실행: cd scripts/graphs && python3 gen_mastert_timelost_emerald.py  → mastert-timelost-emerald-v2.json (gen_batch12.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/mastert-timelost-emerald-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

N_ = '반경 내 주요 패시브 스킬이 '
FRC = L('s', N_ + '공격 치명타 명중 확률 7% 증가도 부여 (분열)', 'Notable Passive Skills in Radius also grant 7% increased Critical Hit Chance for Attacks (fractured)', 'f', ['cc'])
CD = L('s', N_ + '공격 피해의 치명타 피해 보너스 (5—10)% 증가도 부여', 'Notable Passive Skills in Radius also grant (5—10)% increased Critical Damage Bonus for Attack Damage', 'n', ['cd'])
CS = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
MS = L('s', N_ + '이동 속도 1% 증가도 부여', 'Notable Passive Skills in Radius also grant 1% increased Movement Speed', 'd', ['ms'])
AIL = L('p', N_ + '플레이어가 유발하는 상태 이상의 강도 (3—7)% 증가도 부여', 'Notable Passive Skills in Radius also grant (3—7)% increased Magnitude of Ailments you inflict', 'n', ['p6'])
RAD = L('p', '반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large', 'c', ['rad'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

REVB = ['s11', 's17', 'ms', 's3', 's2']   # 영상 11:00~11:30 오래된 주얼에서 남겨도 좋은 접미(공격 속도·활 공격 속도·이동 속도·주요 패시브 효과·소형 패시브 효과)
REVB_LABEL = K('공격 속도·활 사용 시 공격 속도·이동 속도·주요 패시브 스킬 효과·소형 패시브 스킬 효과',
               'Attack speed, attack speed with bows, movement speed, notable effect or small passive effect')
PRE_LABEL = K('상태 이상의 강도·감전의 강도', 'Magnitude of Ailments or Magnitude of Shock')

g = {
 'id': 'mastert-timelost-emerald-v2', 'recipe': 'mastert-timelost-emerald-v2', 'cls': 'Time-Lost_Emerald', 'base': 'Time-Lost Emerald', 'ilvl': 80,
 'note': ('2026-11-13 W23 영상 전체 화면 대조(오래된 에메랄드 Sol Curio 성공 회차, 일반 에메랄드와 동시 제작). '
          '공격 치명타 확률 7% 분열 오래된 에메랄드 구입(5:00, 아이템 레벨 80) → 소멸의 오브로 분열 + 옵션 1개(5:30~5:47) → 카오스 반복으로 공격 피해의 치명타 피해 보너스(7:50) → '
          '엑잘 하나로 접두 잡옵(8:08) → 고대 위력적인 액체 경멸 50:50(8:52 접미 +1 성공) → 우측 강령술 + 보존된 두개골(10:05) → 심연의 메아리 공개(12:09 실패, 빛의 징조로 다시) → 이동 속도(13:52) → '
          '좌측 말소의 징조 + 카오스(15:21) → 엑잘(15:26) → 카오스 반복으로 접두만 바뀜(17:00~19:56, 감전의 강도) → 고대 위력적인 액체 우울(21:44 실패: 감전 강도가 지워짐) → '
          '카오스 반복(21:58 상태 이상의 강도) → 우울 성공(22:13). 신성한 오브 마무리(22:40~24:52)는 정책 14장대로 뺌. '
          '하이엔드 = 영상(이동 속도까지 빛의 징조로 다시), 밸런스 = 영상 11:00 설명의 남겨도 좋은 접미 다섯 중 먼저 뜬 것.'),
 'params': {'v': {'kr': '공개 목표', 'en': 'Reveal target', 'values': {'1': K('이동 속도', 'Movement speed'), '2': K('좋은 접미 다섯 중 하나', 'One of five good suffixes')}}},
 'strategies': [{'id': 'high', 'params': {'v': 1}}, {'id': 'bal', 'params': {'v': 2}}],
 'versions': [{'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 2}, 'tier': 'bal',
               'desc': K('공개는 영상이 꼽은 좋은 접미 다섯 중 먼저 뜬 것', 'The reveal takes whichever of the five good suffixes from the video lands first')},
              {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'v': 1}, 'tier': 'high',
               'desc': K('영상: 이동 속도가 나올 때까지 빛의 징조로 다시 공개', 'Video: Omen of Light until movement speed shows')}],
 'tags': {'cc': {'gi': 8}, 'cd': {'gi': 9}, 'ms': {'gi': 48}, 'rad': {'gi': 99},
          'contS': {'gi': 101, 'slot': {'s': 1}}, 'contP': {'gi': 102, 'slot': {'p': 1}},
          'p6': {'gi': 6}, 'p62': {'gi': 62}, 's11': {'gi': 11}, 's17': {'gi': 17}, 's3': {'gi': 3}, 's2': {'gi': 2},
          'pre': {'anyOf': ['p6', 'p62'], 'label': PRE_LABEL},   # 영상 18:00 계획: 감전의 강도 또는 상태 이상의 강도, 먼저 뜬 것
          'revB': {'anyOf': REVB, 'label': REVB_LABEL}},
 'require': {'all': [{'has': 'cc'}, {'has': 'cd'}, {'has': 'pre'}, {'has': 'rad'}, {'has': 'revB'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'cap': {'p': 2, 's': 2},
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'pre'}, {'tag': 'rad', 'ess': True}, {'tag': 'cc', 'fr': True}, {'tag': 'cd'}, {'tag': 'ms', 'des': True}]},
            {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'pre'}, {'tag': 'rad', 'ess': True}, {'tag': 'cc', 'fr': True}, {'tag': 'cd'}, {'tag': 'revB', 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='pc', start={'rar': 'rare', 'mods': [{'tag': 'cc', 'fr': True}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('공격 치명타 확률 7% 분열 오래된 에메랄드 구입', 'Buy a Time-Lost Emerald with fractured 7% attack critical chance'), item=[FRC, J('p'), J('s')])
A(id='pc', kind='cleanup', group='prep', pos=[0, 1], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[FRC, J('x')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FRC, J('x')])
A(id='c1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 두번째 옵션', 'Second suffix'), show=['cd'],
  edges=[{'if': {'has': 'cd'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[FRC, CD])
A(id='e1', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 잡옵 1개', 'One junk prefix'), showText=[K('접미가 꽉 차 접두로 랜덤 옵션 1개', 'Suffixes are full: one random prefix')],
  edges=[{'to': 'l1'}], item=[J('p'), FRC, CD])
A(id='l1', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Ancient_Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed'),
  showText=[K('접두 잡옵이 지워지면 성공, 치명타 피해가 지워지면 실패', 'The junk prefix goes: success; the critical damage goes: miss')],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'cd'}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'l1x', 'res': 'fail', 'label': K('치명타 피해가 지워짐', 'Critical damage gone')}], item=[CS, FRC, CD])
A(id='l1x', kind='cleanup', group='main', pos=[1, 5.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기고 카오스부터', 'Keep the fracture + one option, back to Chaos'),
  edges=[{'to': 'c1', 'label': K('다시 카오스', 'Chaos again')}])
A(id='d1', kind='act', group='main', pos=[0, 6.4], act='desecrate', cur='Preserved_Cranium', omens=['Omen_of_Dextral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'r1'}], item=[CS, FRC, CD, UN('s')])
RV_OK = {'res': 'ok'}
A(id='r1', kind='act', group='main', pos=[0, 7.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='ms', label=K('공개', 'Reveal'),
  goal=K('접미 이동 속도', 'Movement speed suffix'), show=['ms'],
  edges=[{'if': {'added': 'ms'}, 'to': 'x1', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  over=[{'param': {'v': 2}, 'set': {'want': 'revB', 'show': REVB,
         'goal': K('접미 좋은 옵션 — 공격 속도·활 공격 속도·이동 속도·주요·소형 패시브 효과 중 먼저 뜬 것', 'A good suffix: whichever of attack speed, bow attack speed, movement speed, notable or small passive effect lands first'),
         'edges': [{'if': {'added': 'revB'}, 'to': 'x1', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}]}}],
  item=[CS, FRC, CD, MS])
A(id='r1x', kind='act', group='main', pos=[1, 7.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='x1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Sinistral_Erasure'], label=K('카오스', 'Chaos'),
  goal=K('접미어 속성 부여의 최대 개수 +1개 지우기', 'Remove +1 Suffix Modifier allowed'),
  showText=[K('접미가 한도를 넘어 새 옵션은 접두로', 'Suffixes are over the limit: the new option is a prefix')],
  edges=[{'if': {'has': 'contS'}, 'to': 'x1', 'res': 'fail', 'hide': True}, {'to': 'e2', 'res': 'ok'}], item=[J('p'), FRC, CD, MS])
A(id='e2', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째 옵션', 'Second prefix'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'if': {'has': 'pre'}, 'to': 'l2', 'res': 'ok', 'hide': True}, {'to': 'c2'}], item=[J('p'), J('p'), FRC, CD, MS])
A(id='c2', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 상태 이상의 강도 — 감전의 강도와 함께 먼저 뜬 것', 'Magnitude of Ailments prefix: or Magnitude of Shock, whichever lands first'),
  showText=[K('접미가 한도를 넘어 접두만 바뀜', 'Suffixes are over the limit: only prefixes change')], show=['p6', 'p62'],
  edges=[{'if': {'all': [{'has': 'pre'}, {'has': 'rad'}]}, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'has': 'pre'}, 'to': 'l2', 'res': 'ok'}, {'to': 'c2', 'res': 'fail', 'hide': True}], item=[AIL, J('p'), FRC, CD, MS])
A(id='l2', kind='act', group='main', pos=[0, 11.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large'),
  showText=[K('접두 잡옵이 지워지면 성공, 좋은 접두가 지워지면 실패', 'The junk prefix goes: success; the good prefix goes: miss')],
  edges=[{'if': {'has': 'pre'}, 'to': 'ok', 'res': 'ok'}, {'to': 'c2', 'res': 'fail', 'label': K('좋은 접두가 지워짐 — 다시 카오스', 'Good prefix gone: Chaos again')}],
  item=[AIL, RAD, FRC, CD, MS])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'},
              {'id': 'L2', 'nodes': ['c2', 'l2'], 'kr': '우울', 'en': 'Melancholy'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
