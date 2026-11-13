# G10 2026-11-13: Fubgun 가성비 화살통(mobalytics 0.5.5 Ice Shot Deadeye 빌드 글의 Crafting Guide 'Quiver - ilvl 75' 1~5단계) 플로우차트 생성기
# 근거: scratchpad review/G10/fubgun-quiver-v2/timeline.md, frames/guide-quiver-steps-1-5.jpg (글 전체 다시 읽음)
# 실행: cd scripts/graphs && python3 gen_fubgun_quiver.py  → fubgun-quiver-v2.json (gen_batch26.py 끝에서 자동 호출)
# 상자 id는 옛 레시피(recipes_v5_fubgun-055.py q1~q6)와 겹치지 않게 qn·qt·qa·qx·qr·qc·qd·qv·ql·qe.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-quiver-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
TV = lambda d: {k: K(*v) for k, v in d.items()}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

FL = L('p', '공격 시 물리 피해 (12—19)~(22—32) 추가', 'Adds (12—19) to (22—32) Physical Damage to Attacks', 'n', ['flat'])
PJ = L('s', '모든 투사체 스킬 레벨 +1', '+1 to Level of all Projectile Skills', 'n', ['proj'])
AS = L('s', '공격 속도 (14—16)% 증가', '(14—16)% increased Attack Speed', 'n', ['as'])
CR = L('s', '공격 치명타 명중 확률 (35—38)% 증가', '(35—38)% increased Critical Hit Chance for Attacks', 'd', ['crit'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
RP = L('p', '랜덤 옵션', 'Random option', 'j')
RS = L('s', '랜덤 옵션', 'Random option', 'j')
RX = L('x', '랜덤 옵션', 'Random option', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
ESS = {'param': {'L': 0}}

P = {'bal': {'aT': 2, 'cT': 2, 'L': 1}, 'ess': {'aT': 4, 'cT': 4, 'L': 0}}
g = {
 'id': 'fubgun-quiver-v2', 'recipe': 'fubgun-quiver-v2', 'cls': 'Quivers', 'base': 'Visceral Quiver', 'ilvl': 75,
 'note': ('2026-11-13 G10 글 전체 다시 대조(mobalytics Fubgun 0.5.5 Ice Shot Deadeye, Crafting Guide의 Quiver - ilvl 75 1~5단계, 캡처 guide-quiver-steps-1-5). '
          '글: ① 완벽한 진화·확장으로 좋은 옵션 2개(접두 피해 추가 또는 활 스킬 피해, 접미 +1·치명타·공격 속도) ② 완벽한 제왕으로 세 번째 좋은 옵션(접미가 이상적) '
          '③ 빗나가면 상위 카오스 오브로 그 옵션 교체 시도(2/3은 망함) ④ 우측 강령술 + 턱뼈, 좋은 옵션 3개면 심연의 메아리 ⑤ 좋은 접미가 뜨면 완벽한 엑잘 + 상위 찬미로 마무리. '
          '확정 옵션(정책 11장): 매직 = 물리 피해 추가 1티어 + 모든 투사체 +1(옛 레시피·글의 비싼 방법 \'t1 Flat\'), 제왕 = 접미 공격 속도, 공개 = 공격 치명타 확률(본능적인 화살통 설명의 치명타). '
          '내부 결정(글에 없음): 베이스 = 본능적인 화살통(빌드 글 장비 설명), 매직 단계 빗나감은 새 베이스(소멸의 오브 147 ex보다 진화 + 확장이 쌈, 글 \'until\'), '
          '상위 카오스 오브가 물리 피해 추가나 +1을 지우면 새 베이스, 턱뼈 = 보존된 턱뼈. 옛 그래프의 좌측 대관식의 징조(제왕을 접두로 고정)는 글과 반대라 뺌 — 접미 2개 상태의 우측 강령술 턱뼈는 빈자리로 들어가 좋은 접미를 지우지 않음. '
          '등급(난이도 2~3 → 밸런스·에센셜, C17): 밸런스 = 공격 속도 1~2티어까지 상위 카오스 오브, 공개 치명타 1~2티어까지 빛의 징조로 다시(글의 비싼 방법), '
          '에센셜 = 반복 없이 제왕·공개 결과 그대로(글: 좋은 옵션 3개가 아니면 메아리 없이), 마무리 상위 엑잘.'),
 'params': {'aT': {'kr': '공격 속도', 'en': 'Attack speed', 'values': TV({'2': ('1~2티어', 'T1–2'), '4': ('나오는 대로', 'As it comes')})},
            'cT': {'kr': '공격 치명타 확률', 'en': 'Attack crit chance', 'values': TV({'2': ('1~2티어', 'T1–2'), '4': ('나오는 대로', 'As it comes')})},
            'L': {'kr': '반복', 'en': 'Retries', 'values': TV({'1': ('다시', 'Retry'), '0': ('결과 그대로', 'Keep what comes')})}},
 'strategies': [{'id': 'bal', 'params': P['bal']}, {'id': 'ess', 'params': P['ess']}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': P['ess'], 'tier': 'ess',
               'desc': K('제왕·공개 결과 그대로, 마무리 상위 엑잘', 'Regal and reveal kept as they come, Greater Exalts to finish')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': P['bal'], 'tier': 'bal',
               'desc': K('공격 속도 1~2티어까지 상위 카오스, 치명타 1~2티어까지 빛의 징조로 다시', 'Greater Chaos until T1–2 attack speed, Omen of Light until T1–2 crit')}],
 'tags': {'flat': {'gi': 2, 'tmax': 1}, 'proj': {'gi': 9},
          'as': {'gi': 12, 'tmax': '$aT'}, 'crit': {'gi': 14, 'tmax': '$cT'},
          'as2': {'gi': 12, 'tmax': 2}, 'crit2': {'gi': 14, 'tmax': 2}},
 'require': {'all': [{'has': 'flat'}, {'has': 'proj'}, {'full': 'p'}, {'full': 's'},
                     {'any': [ESS, {'all': [{'has': 'as'}, {'has': 'crit'}]}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'qn',
 'finals': [{'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'flat'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'proj'}, {'tag': 'as2'}, {'tag': 'crit2'}]},
            {'id': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
             'lines': [{'tag': 'flat'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'proj'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
MAG = {'all': [{'has': 'flat'}, {'has': 'proj'}]}
# ---------------- 베이스템 완성 (글 1단계) ----------------
A(id='qn', kind='base', group='prep', pos=[0, 0], next='qt', start={'rar': 'normal', 'mods': []},
  label=K('본능적인 화살통 구입 (노멀, 아이템 레벨 75)', 'Buy a Visceral Quiver (normal, item level 75)'), item=[])
A(id='qt', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 — 물리 피해 추가 1티어·모든 투사체 스킬 레벨 +1 중 먼저 뜬 것', 'Magic: T1 flat physical or +1 projectile skills, whichever comes first'), show=['flat', 'proj'],
  edges=[{'if': {'any': [{'has': 'flat'}, {'has': 'proj'}]}, 'to': 'qa', 'res': 'ok'},
         {'to': 'qx', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[FL])
A(id='qa', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('남은 옵션', 'The other one'), show=['flat', 'proj'],
  edges=[{'if': MAG, 'to': 'ms', 'res': 'ok'}, {'to': 'qx', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[FL, PJ])
A(id='qx', kind='exit', group='prep', pos=[1, 1.5], simTo='qn', variant='fail', label=K('새 베이스', 'New base'),
  note=K('진화·확장이 빗나가거나 상위 카오스 오브가 좋은 옵션을 지우면 새 베이스로', 'A missed Transmute or Augment, or Greater Chaos taking a good option: a new base'))
# ---------------- 옵션 추가 작업 (글 2~5단계) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='qr', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FL, PJ])
A(id='qr', kind='act', group='main', pos=[0, 4.4], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 + 접미 공격 속도 1~2티어', 'Rare + T1–2 attack speed suffix'), show=['as'],
  edges=[{'if': {'has': 'as'}, 'to': 'qd', 'res': 'ok'}, {'if': ESS, 'to': 'qd', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'qc', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[FL, PJ, AS],
  over=[{'param': {'L': 0}, 'set': {'goal': K('레어 + 세번째 옵션 — 나오는 대로', 'Rare + a third option: keep what comes'), 'show': [],
                                    'showText': [K('랜덤 옵션 1개', 'One random option')], 'item': [FL, PJ, RX]}}])
A(id='qc', kind='act', group='main', pos=[1, 4.4], act='chaos', cur='Greater_Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('빗나간 옵션 교체 시도 — 공격 속도가 뜰 때까지, 좋은 옵션이 지워지면 새 베이스', 'Try to replace the miss: until attack speed, a lost good option means a new base'), show=['as'],
  edges=[{'if': {'not': MAG}, 'to': 'qx', 'res': 'fail', 'label': K('좋은 옵션 지워짐', 'Good option lost')},
         {'if': {'has': 'as'}, 'to': 'qd', 'res': 'ok'}, {'to': 'qc', 'res': 'fail', 'hide': True}])
A(id='qd', kind='act', group='main', pos=[0, 5.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세번째 옵션(훼손)', 'Third suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'qv'}], item=[FL, PJ, AS, UN('s')], over=[{'param': {'L': 0}, 'set': {'item': [FL, PJ, RX, UN('x')]}}])
A(id='qv', kind='act', group='main', pos=[0, 6.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='crit', label=K('공개', 'Reveal'),
  goal=K('접미 공격 치명타 명중 확률 1~2티어', 'T1–2 attack crit chance suffix'), show=['crit'],
  edges=[{'if': {'has': 'crit'}, 'to': 'qe', 'res': 'ok'}, {'if': ESS, 'to': 'qe', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'ql', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[FL, PJ, AS, CR],
  over=[{'param': {'L': 0}, 'set': {'omens': [], 'goal': K('훼손 옵션 공개 — 나오는 대로', 'Reveal the desecration: keep what comes'), 'show': [],
                                    'showText': [K('랜덤 옵션', 'Random option')], 'item': [FL, PJ, RX, RX]}}])
A(id='ql', kind='act', group='main', pos=[1, 6.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'qd', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='qe', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('남은 두 자리 — 나오는 대로', 'The last two slots: keep what comes'), showText=[K('랜덤 옵션 2개', 'Two random options')],
  edges=[{'to': 'ok'}], item=[FL, RP, RP, PJ, AS, CR],
  over=[{'param': {'L': 0}, 'set': {'cur': 'Greater_Exalted_Orb', 'item': [FL, RX, RX, PJ, RX, RX]}}])
A(id='ok', kind='done', group='main', pos=[0, 8.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['qd', 'qv', 'ql'], 'kr': '접미 세번째 옵션(훼손)', 'en': 'Third suffix (desecrated)'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
