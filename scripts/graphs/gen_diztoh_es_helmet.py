# G11 2026-11-13: Diztoh 엔드게임 에너지 보호막 투구(영상 yegMdBTuEtY, 8:01) 플로우차트 생성기 — 영상 한 회차 그대로(모든 단계 첫 시도 성공)
# 근거: scratchpad review/G11/diztoh-es-helmet-v2/timeline.md, frames/*.jpg (영상 전체, 화면 확대)
# 실행: cd scripts/graphs && python3 gen_diztoh_es_helmet.py  → diztoh-es-helmet-v2.json (gen_batch6.py 끝에서 자동 호출)
# 상자 id는 옛 단계 레시피(e1~e7)와 겹치지 않게.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-es-helmet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
C = json.load(open(f'{H}/../../site/data/c/Helmets_int.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, tier=1):
    t = C['groups'][gi]['t'][tier - 1]
    return t[4].replace('\n', ' · '), t[5].replace('\n', ' · ')

ESF = L('p', *T(7), 'f', ['esf'])
ESFn = L('p', *T(7), 'n', ['esf'])
RARS = L('s', *T(16), 'n', ['rarS'])
INT = L('s', T(38)[0] + ' (제작 옵션)', T(38)[1] + ' (crafted)', 'c', ['int'])
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
REC = L('s', '랜덤 옵션', 'Random option', 'j')     # m 'j': graph2recipe가 우측 찬미 엑잘 자리를 이 줄에서 읽음(영상: 에너지 보호막 재충전 속도)
ESP = L('p', '에너지 보호막 % 증가 1~3티어', 'T1–3 % energy shield', 'n', ['esp3'])
RARP = L('p', T(17)[0] + ' (훼손)', T(17)[1] + ' (desecrated)', 'd', ['rarP'])
RP = L('p', '랜덤 옵션', 'Random option', 'n')
RPD = L('p', '랜덤 옵션', 'Random option', 'd')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'diztoh-es-helmet-v2', 'recipe': 'diztoh-es-helmet-v2', 'cls': 'Helmets_int', 'base': 'Kamasan Tiara', 'ilvl': 81,
 'note': ('2026-11-13 G11 영상 전체 화면 대조(yegMdBTuEtY 8:01, 근거 scratchpad review/G11/diztoh-es-helmet-v2/timeline.md). 영상 한 회차, 모든 단계 첫 시도 성공: '
          '특출난 카마사의 티아라 노멀(0:20, 아이템 레벨 81) → 완벽한 진화의 오브 = 에너지 보호막 최대치 1티어(0:29, 창고 III 209→208) → 완벽한 확장의 오브 = 아이템 희귀도 1티어(0:33, III 166→165) → '
          '상위 무한의 에센스 = 지능 +26(0:55) → 좌측 강령술의 징조(1:04) + 고대 갈비뼈(거래소 1:17, 사용 장면은 편집으로 잘림, 1:22 미공개 접두) → 신성한 오브로 수치(1:22~1:44, 선택) → '
          '분열의 오브(1:45~1:52, 최대치 분열 — 툴팁 색, 창고 2→1) → 우측 찬미의 징조 + 상위 엑잘(2:42~2:50, 에너지 보호막 재충전 속도, 상위 70→69) → 상위 엑잘(3:03, 에너지 보호막 % 3티어 78%, 상위 69→68) → '
          '심연의 메아리의 징조 + 공개(3:45, 접두 희귀도 1티어) → 방어구 장인의 고철로 퀄리티 20%(3:54~4:16). 곰 우상(4:32)·완벽한 사막 룬(5:08)은 마무리 룬이라 뺌(정책 9장), 5:20~8:01 사원 타락(소켓)은 레시피 밖. '
          '내부 결정(영상에 없음): 매직 빗나감은 소멸의 오브로 지우고 다시(치명타 투구와 같은 틀), 분열이 희귀도·지능이면 새 베이스, 접두 엑잘 빗나감은 좌측 소멸의 징조 + 소멸의 오브(영상 2:05 말: 소멸 또는 카오스) — '
          '훼손 옵션이 지워지면 고대 갈비뼈로 다시, 공개 빗나감은 빛의 징조 + 소멸의 오브 → 고대 갈비뼈(밸런스만), 고철 개수 20개(희귀 아이템 1%씩 가정). '
          '접두 엑잘은 영상 말(2:52 희귀도나 에너지 보호막 %)대로 둘 중 먼저 뜬 것, 공개가 남은 것(붙는 순서 예외, 정책 11장). 등급(분열 시작 → 어려움, 밸런스·에센셜): 밸런스 = 접두 에너지 보호막 % 1~3티어(영상 결과 3티어)·접두 희귀도까지 다시, 에센셜 = 접두 엑잘·공개 결과 그대로.'),
 'params': {'L': {'kr': '접두 엑잘·공개', 'en': 'Prefix exalt and reveal', 'values': {'1': K('원하는 옵션까지 다시', 'Retry for the wanted options'), '0': K('결과 그대로', 'Keep what comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1}}, {'id': 'ess', 'params': {'L': 0}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0}, 'tier': 'ess',
               'desc': K('접두 엑잘·훼손 공개 결과 그대로', 'Keep the prefix exalt and the reveal as they come')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1}, 'tier': 'bal',
               'desc': K('영상 완성품: 접두 에너지 보호막 % 1~3티어, 접두 희귀도까지 다시', 'The video item: T1–3 % energy shield and prefix rarity, retried')}],
 'tags': {'esf': {'gi': 7, 'tmax': 1}, 'rarS': {'gi': 16, 'tmax': 1},
          'magicGood': {'anyOf': ['esf', 'rarS'], 'label': K('에너지 보호막 최대치 1티어·아이템 희귀도 1티어', 'T1 flat energy shield or T1 item rarity')},
          'int': {'gi': 38}, 'esp3': {'gi': 8, 'tmax': 3}, 'rarP': {'gi': 17, 'tmax': 1},
          'pre2': {'anyOf': ['esp3', 'rarP'], 'label': K('에너지 보호막 % 증가 1~3티어·접두 아이템 희귀도', 'T1–3 % energy shield or prefix item rarity')}},
 'conds': {'magicDone': {'all': [{'has': 'esf'}, {'has': 'rarS'}]}, 'preDone': {'all': [{'has': 'esp3'}, {'has': 'rarP'}]}},
 'require': {'all': [{'has': 'esf'}, {'has': 'rarS'}, {'has': 'int'}, {'full': 'p'}, {'full': 's'},
                     {'any': [{'param': {'L': 0}}, {'all': [{'has': 'esp3'}, {'has': 'rarP'}]}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 2]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (0:20~1:52) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='m1', start={'rar': 'normal', 'mods': []},
  label=K('특출난 카마사의 티아라 구입 (아이템 레벨 81)', 'Buy an exceptional Kamasan Tiara (item level 81)'), item=[])
A(id='m1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('매직 첫 번째 옵션', 'First magic option'),
  goal=K('접두 에너지 보호막 최대치 1티어', 'T1 flat energy shield prefix'), show=['esf'],
  edges=[{'if': {'added': 'magicGood'}, 'to': 'm2', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'm1x', 'res': 'fail', 'label': K('빗나감', 'miss')}], item=[ESFn])
A(id='m1x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), edges=[{'to': 'm2'}])
A(id='m2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('매직 두 번째 옵션', 'Second magic option'),
  goal=K('접미 아이템 희귀도 1티어', 'T1 item rarity suffix'), show=['rarS'],
  edges=[{'if': {'ref': 'magicDone'}, 'to': 's1', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'm2x', 'res': 'fail', 'label': K('빗나감', 'miss')}], item=[ESFn, RARS])
A(id='m2x', kind='cleanup', group='prep', pos=[1, 2], keep=['magicGood'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  edges=[{'lost': 'magicGood', 'to': 'm2y', 'res': 'fail', 'label': K('원하는 옵션 지워짐', 'wanted option gone')},
         {'to': 'm2', 'res': 'ok', 'label': K('잡옵 지워짐', 'junk gone')}])
A(id='m2y', kind='cleanup', group='prep', pos=[2, 2], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('남은 옵션 지우기', 'Remove the remaining option'), edges=[{'to': 'm2'}])
A(id='s1', kind='act', group='prep', pos=[0, 3], act='essence', cur='Greater_Essence_of_the_Infinite', ess='int', label=K('에센스', 'Essence'),
  goal=K('레어로 + 접미 두 번째 옵션', 'Make it rare + second suffix'),
  showText=[{'s': 's', 'kr': T(38)[0] + ' (제작 옵션)', 'en': T(38)[1] + ' (crafted)'}], edges=[{'to': 'd0'}], item=[ESFn, RARS, INT])
A(id='d0', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Second prefix (desecrated): the fracture needs four'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 분열되지 않음)', 'en': 'Desecrated (unrevealed, cannot fracture)'}], edges=[{'to': 'f1'}],
  item=[ESFn, UN, RARS, INT])
A(id='dv', kind='side', group='prep', pos=[1, 4.5], act='divine', cur='Divine_Orb', attach=['d0', 'f1'],
  label=K('수치 올리기', 'Divine the values'), goal=K('옵션 수치 다시 굴리기 (선택)', 'Reroll option values (optional)'),
  showText=[K('모든 옵션 수치 다시 굴림', 'Rerolls every value')])
A(id='f1', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('에너지 보호막 최대치가 분열되면 성공', 'Success when the flat energy shield fractures')], ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'esf'}, 'to': 'ms', 'res': 'ok', 'label': K('최대치 분열', 'flat fractured')},
         {'if': {'fractured': 'rarS'}, 'to': 'xs', 'res': 'ok', 'dash': True, 'label': K('희귀도 분열', 'rarity fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('지능 분열', 'intelligence fractured')}],
  item=[ESF, UN, RARS, INT])
A(id='xs', kind='exit', group='prep', pos=[1, 5], simTo='b0', variant='ok', label=K('희귀도 분열', 'Rarity fractured'),
  note=K('다른 제작에 쓰거나 판매, 새 베이스로 처음부터', 'Use it for another craft or sell it; start over on a new base'))
A(id='xj', kind='exit', group='prep', pos=[1, 6], simTo='b0', variant='fail', label=K('지능 분열', 'Intelligence fractured'),
  note=K('새 베이스로 처음부터', 'Start over on a new base'))
# ---------------- 옵션 추가 작업 (2:42~4:16) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7], next='x1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ESF, UN, RARS, INT])
A(id='x1', kind='act', group='main', pos=[0, 8], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 세 번째 옵션', 'Third suffix'),
  showText=[{'s': 's', 'kr': '랜덤 옵션', 'en': 'Random option'}], edges=[{'to': 'x2'}], item=[ESF, UN, RARS, INT, REC])
A(id='x2', kind='act', group='main', pos=[0, 9], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션 — 에너지 보호막 % 증가 1~3티어·접두 아이템 희귀도 중 먼저 뜬 것(영상: 에너지 보호막 %)', 'Third prefix: T1–3 % energy shield or prefix rarity, whichever comes first (the video: % energy shield)'), show=['esp3', 'rarP'],
  edges=[{'if': {'added': 'pre2'}, 'to': 'r1', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'r1', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'x2x', 'res': 'fail'}], item=[ESF, ESP, UN, RARS, INT, REC],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 세 번째 옵션 — 에너지 보호막 % 노림, 나오는 대로', 'Third prefix: aiming for % energy shield, keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [ESF, RP, UN, RARS, INT, REC]}}])
A(id='x2x', kind='act', group='main', pos=[1, 9], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=ANN, goal=ANN,
  target=K('좌측 소멸의 징조로 빗나간 접두 지우기 — 훼손 옵션이 지워질 수 있음', 'Sinistral Annulment removes the missed prefix (it can take the desecration)'),
  ask=K('뭐가 지워짐?', 'What was removed?'),
  edges=[{'if': {'unrev': False}, 'to': 'x2d', 'res': 'fail', 'label': K('훼손 옵션 지워짐', 'desecration gone')},
         {'to': 'x2', 'res': 'ok', 'label': K('빗나간 접두 지워짐 — 다시 엑잘', 'missed prefix gone: exalt again')}])
A(id='x2d', kind='act', group='main', pos=[2, 9], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 훼손 옵션 다시', 'Desecrate the prefix again'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'x2', 'label': K('다시 엑잘', 'exalt again')}])
A(id='r1', kind='act', group='main', pos=[0, 10], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='pre2', label=K('공개', 'Reveal'),
  goal=K('접두 남은 옵션 — 영상: 아이템 희귀도', 'The remaining prefix (the video: item rarity)'), show=['rarP'],
  edges=[{'if': {'ref': 'preDone'}, 'to': 'q1', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'q1', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'r1x', 'res': 'fail'}], item=[ESF, ESP, RARP, RARS, INT, REC],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 훼손 옵션 공개 — 나오는 대로', 'Reveal the prefix desecration: keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [ESF, RP, RPD, RARS, INT, REC]}}])
A(id='r1x', kind='act', group='main', pos=[1, 10], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'r1d'}])
A(id='r1d', kind='act', group='main', pos=[1, 10.6], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 훼손 옵션 다시', 'Desecrate the prefix again'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'r1', 'label': K('다시 공개', 'reveal again')}])
A(id='q1', kind='act', group='main', pos=[0, 11.4], act='quality', cur='Armourers_Scrap', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 20%', 'Quality 20%'), showText=[K('방어구 장인의 고철 20개', '20 Armourer’s Scraps')], edges=[{'to': 'ok'}],
  item=[ESF, ESP, RARP, RARS, INT, REC], over=[{'param': {'L': 0}, 'set': {'item': [ESF, RP, RPD, RARS, INT, REC]}}])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
  {'id': 'L1', 'nodes': ['m1', 'm1x', 'm2', 'm2x', 'm2y'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'},
  {'id': 'L2', 'nodes': ['x2', 'x2x', 'x2d'], 'kr': '접두 세 번째 옵션', 'en': 'Third prefix', 'fold': True,
   'goal': K('접두 에너지 보호막 % 증가 1~3티어·접두 아이템 희귀도 중 먼저 뜬 것', 'T1–3 % energy shield or prefix rarity, whichever comes first'),
   'steps': [{'kr': '상위 엑잘티드 오브로 접두 에너지 보호막 % 증가·아이템 희귀도', 'en': 'Greater Exalted Orb for % energy shield or rarity', 'node': 'x2'},
             {'kr': '빗나가면 좌측 소멸의 징조 + 소멸의 오브', 'en': 'On a miss: Sinistral Annulment + Orb of Annulment', 'node': 'x2x'},
             {'kr': '미공개 훼손 옵션이 지워졌으면 좌측 강령술의 징조 + 고대 갈비뼈로 다시 훼손', 'en': 'If the unrevealed desecration went: Sinistral Necromancy + Ancient Rib again', 'node': 'x2d'}],
   'item': [ESF, ESP, UN, RARS, INT, REC]},
  {'id': 'L3', 'nodes': ['r1', 'r1x', 'r1d'], 'kr': '훼손 공개', 'en': 'Reveal'},
]
g['finals'] = [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'esf', 'fr': True}, {'tag': 'esp3'}, {'tag': 'rarP'}, {'tag': 'rarS'}, {'tag': 'int'}, {'side': 's', 'random': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'esf', 'fr': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'rarS'}, {'tag': 'int'}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
