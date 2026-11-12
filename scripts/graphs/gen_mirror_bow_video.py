# W15 2026-11-13: 반지깎는노인 미러 활(J0LF3MRssh0) 플로우차트 생성기 — 영상 성공 회차(독사의 비) 한 줄
# 근거: scratchpad review/W15-mirror-bow/timeline.md, frames/ (영상 0:00~35:20 화면 대조)
# 실행: cd scripts/graphs && python3 gen_mirror_bow_video.py  → mirror-bow-video-v2.json (gen_batch20.py 끝에서도 이 파일을 실행해 덮어씀)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/mirror-bow-video-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 옵션 줄 (문구는 Bows 클래스 파일 1티어 그대로, 수치는 영상 화면)
FLm = L('p', '물리 피해 (26—39)~(44—66) 추가', 'Adds (26—39) to (44—66) Physical Damage', 'n', ['flat'])        # 9:52 매직
CRm = L('s', '치명타 확률 +(4.41—5)%', '+(4.41—5)% to Critical Hit Chance', 'n', ['crit'])                           # 9:52 매직
CR = L('s', '치명타 확률 +(4.41—5)%', '+(4.41—5)% to Critical Hit Chance', 'f', ['crit'])                            # 13:58 분열
PP = L('p', '물리 피해 (170—179)% 증가', '(170—179)% increased Physical Damage', 'n', ['pp'])                         # 17:18
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkp'])                                            # 19:08
BLK = L('p', '공격 스킬의 원소 피해 (87—100)% 증가', '(87—100)% increased Elemental Damage with Attacks', 'd', ['eatk'])  # 22:12 공개 97%
HY = L('p', '물리 피해 (75—79)% 증가 + 정확도 +(175—200)', '(75—79)% increased Physical Damage + (175—200) to Accuracy Rating', 'n', ['hyb'])   # 23:51
PJ = L('s', '모든 투사체 스킬 레벨 +4', '+4 to Level of all Projectile Skills', 'n', ['proj'])                         # 25:40
AR = L('s', '추가 화살을 발사할 초과 확률 +(175—200)%', '+(175—200)% Surpassing chance to fire an additional Arrow', 'n', ['arr'])   # 29:20
CD = L('s', '치명타 피해 보너스 +(23—25)%', '+(23—25)% to Critical Damage Bonus', 'n', ['cdm'])                       # 30:08
FL = L('p', '물리 피해 (26—39)~(44—66) 추가', 'Adds (26—39) to (44—66) Physical Damage', 'd', ['flat'])             # 34:35 공개 32~62
SE = L('r', '세를의 승리', 'Serle’s Triumph', 'r')                                                                      # 28:02~28:10
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'mirror-bow-video-v2', 'recipe': 'mirror-bow-video-v2', 'cls': 'Bows', 'base': 'Warmonger Bow', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 35},   # 사용자 결정 11-13: 퀄리티 30% 특출난 전쟁광 활 35 div (영상 7:30 '30~40 div')
 'note': ('2026-11-13 W15 영상 전체 화면 대조(0:00~35:20). 성공 회차(독사의 비) 한 줄: 퀄리티 30% 전쟁광 활 구입(8:00, 8:55 아이템 레벨 82) → 완벽한 진화·확장으로 매직 물리 피해 추가 1티어 + 치명타 확률 1티어(8:10~9:52) → '
          '완벽한 제왕(10:18) → 신성한 오브로 치명타 5%(10:55~11:45, 비용 미포함) → 뼈로 네번째 옵션(11:52) → 분열의 오브(13:32, 치명타 분열 13:58·14:30) → 카오스 오브로 물리 피해 % 1티어(15:45~17:18, 빈자리 3개) → '
          '우측 결정화 + 심연의 에센스로 접미 잡옵을 지우고 징표(19:01~19:08, 징표 접두) → 고대 턱뼈로 징표 훼손 → 메아리 공개(20:58~21:06 빗나감: 정확도 +205) → 절사 + 상위 카오스로 빗나간 옵션 교체(21:35~21:38) → '
          '우측 결정화 + 심연의 에센스(21:40~21:53) → 고대 턱뼈(21:55) → 공개 공격 스킬의 원소 피해 97%(22:12, 자리 막기) → 좌측 찬미 + 완벽한 엑잘(23:30~23:36) → 절사 + 상위 카오스로 물리 피해 + 정확도 1티어(23:42~23:51) → '
          '완벽한 엑잘 접미 잡옵(25:05) → 우측 말소 + 상위 카오스로 투사체 +4(25:00~25:40) → 완벽한 엑잘 접미 잡옵(26:15~26:45, 27:10~27:55 절사 시도) → 세를의 승리(28:02~28:10) → 엑잘 네번째 접미(28:20) → '
          '절사 + 상위 카오스로 화살 초과 1티어(29:20)·치명타 피해 1티어(30:08) → 빛의 징조 + 소멸로 자리 막기 제거(31:20) → 고대 턱뼈 + 메아리 공개 반복(31:27~34:35) → 물리 피해 추가 32~62(34:35). '
          '내부 결정: 징표는 게임에서 접두·접미 50/50이지만 영상 성공 회차 두 번 모두 접두라 접두 징표(mkp)로 계산. 분열 전 뼈 종류는 확인 못 해 보존된 턱뼈(정책 6장). '
          '27:10~27:55의 접미 세 자리 절사 시도는 세를의 승리 뒤 같은 반복(u6)에 합침. '
          '사용자 결정 11-13: 세번째 접두는 물리 피해 + 정확도·물리 피해 추가 1티어 중 먼저 뜬 것(영상 22:30), 물리 피해 추가가 먼저면 마지막 훼손 공개 목표는 물리 피해 + 정확도(일반 옵션이라 훼손 공개 선택지에 나옴).'),
 'params': {'pT': {'kr': '목표 티어', 'en': 'Target tier', 'values': {'1': K('1티어', 'T1')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
               'desc': K('영상: 모든 옵션 1티어', 'Video: every option T1')}],
 'tags': {'pp': {'gi': 7, 'tmax': 1}, 'crit': {'gi': 17, 'tmax': 1}, 'flat': {'gi': 2, 'tmax': 1},
          'hyb': {'gi': 8, 'tmax': 1}, 'eatk': {'gi': 21, 'tmax': 1}, 'proj': {'gi': 9, 'tmax': 1},
          'arr': {'gi': 20, 'tmax': 1}, 'cdm': {'gi': 18, 'tmax': 1}, 'mkp': {'gi': 56}, 'mks': {'gi': 57},
          'p3': {'anyOf': ['hyb', 'flat'], 'label': K('물리 피해 + 정확도 1티어 또는 물리 피해 추가 1티어', 'T1 physical + accuracy or T1 flat physical')},
          'keepP': {'anyOf': ['pp', 'p3']},
          'keepS': {'anyOf': ['proj', 'arr', 'cdm']},
          'lastS': {'anyOf': ['arr', 'cdm'], 'label': K('추가 화살을 발사할 초과 확률·치명타 피해 보너스 1티어', 'T1 additional Arrow chance or Critical Damage Bonus')}},
 'require': {'all': [{'has': 'crit'}, {'has': 'pp'}, {'has': 'hyb'}, {'has': 'flat'}, {'has': 'proj'}, {'has': 'arr'}, {'has': 'cdm'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'pb',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'pp'}, {'tag': 'hyb'}, {'tag': 'flat', 'des': True}, {'tag': 'crit', 'fr': True},
                       {'tag': 'proj'}, {'tag': 'arr'}, {'tag': 'cdm'}]}],
 'finalItem': {'quality': 30, 'sockets': 3},
}

# 아이템 상태마다 다음 단계 (숨은 선) — 다른 옵션이 지워졌을 때만 지나감
DESLOW = {'not': {'whittleSafe': {'tag': 'mks', 'keepDes': True}}}   # 빗나간 훼손 옵션이 레벨이 가장 낮아 절사로 바뀜
FIN = {'all': [{'has': 'p3'}, {'has': 'proj'}, {'has': 'arr'}, {'has': 'cdm'}]}
def route(skip=()):
    R = [({'not': {'has': 'pp'}}, 'k1', K('물리 피해 % 지워짐 — 카오스부터', '% physical gone: back to Chaos')),
         ({'any': [{'has': 'mkp'}, {'has': 'mks'}]}, 'k3', K('징표 훼손', 'Desecrate the Mark')),
         ({'all': [{'unrevSide': 'p'}, FIN]}, 'z3', K('훼손 옵션 확인', 'Reveal')),
         ({'unrevSide': 'p'}, 'k4', K('훼손 옵션 확인', 'Reveal')),
         ({'all': [{'famBlock': 'eatk'}, {'not': FIN}]}, 'k4w', K('공격 스킬의 원소 피해 낮은 티어가 자리를 차지 — 절사로 교체', 'A low tier attack elemental holds the family: Whittle it away')),
         ({'all': [{'has': 'eatk'}, {'not': {'des': True}}, {'not': FIN}]}, 'q1w', K('공격 스킬의 원소 피해가 일반 옵션으로 붙음 — 절사로 교체', 'Attack elemental landed as a normal option: Whittle it away')),
         ({'all': [{'not': {'has': 'eatk'}}, {'not': FIN}, {'des': True}, DESLOW]}, 'k4w', K('빗나간 훼손 옵션 교체', 'Replace the missed desecration')),
         ({'all': [{'not': {'has': 'eatk'}}, {'not': FIN}, {'des': True}]}, 'k4x', K('빗나간 옵션 레벨이 높음 — 빛의 징조로 제거', 'The miss is high level: Omen of Light removes it')),
         ({'all': [{'not': {'has': 'eatk'}}, {'not': FIN}]}, 'k2', K('자리 막기가 지워짐 — 다시 징표', 'Blocker gone: Mark again')),
         ({'all': [{'not': {'has': 'p3'}}, {'full': 'p'}]}, 'q1w', K('접두 잡옵 교체', 'Replace the junk prefix')),
         ({'not': {'has': 'p3'}}, 'q1', K('접두 세번째 옵션', 'Third prefix')),
         ({'all': [{'not': {'has': 'proj'}}, {'sideLt': {'side': 's', 'n': 2}}]}, 'u1', K('접미 잡옵', 'A junk suffix')),
         ({'not': {'has': 'proj'}}, 'u2', K('투사체 +4가 지워짐', '+4 projectiles gone')),
         ({'all': [{'not': {'rune': 'Serle'}}, {'sideLt': {'side': 's', 'n': 3}}]}, 'u3', K('접미 잡옵', 'A junk suffix')),
         ({'not': {'rune': 'Serle'}}, 'u4', K('세를의 승리', 'Serle’s Triumph')),
         ({'sideLt': {'side': 's', 'n': 4}}, 'u5', K('접미 잡옵', 'A junk suffix')),
         ({'not': {'all': [{'has': 'arr'}, {'has': 'cdm'}]}}, 'u6', K('접미 옵션 교체', 'Replace a suffix')),
         ({'has': 'eatk'}, 'z1', K('자리 막기 제거', 'Remove the blocker')),
         ({'all': [{'has': 'hyb'}, {'has': 'flat'}]}, 'ok', K('완성', 'Finished')),
         ({'des': True}, 'z3x', K('빗나간 훼손 옵션 제거', 'Remove the missed desecration')),
         (None, 'z2', K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'))]
    out = []
    for c, to, lab in R:
        if to in skip: continue
        e = {'to': to, 'hide': True, 'label': lab}
        if c: e['if'] = c
        out.append(e)
    return out

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='pb', kind='base', group='prep', pos=[0, 0], next='pt', start={'rar': 'normal', 'mods': [], 'quality': 30},
  label=K('전쟁광 활 구입 (아이템 레벨 82, 퀄리티 30%)', 'Buy a Warmonger Bow (item level 82, 30% quality)'), item=[])
BOTH = {'all': [{'has': 'flat'}, {'has': 'crit'}]}
EMPTY = {'all': [{'sideLt': {'side': 'p', 'n': 1}}, {'sideLt': {'side': 's', 'n': 1}}]}
A(id='pt', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 물리 피해 추가·치명타 확률 1티어', 'Magic T1 flat physical and crit chance'), show=['flat', 'crit'],
  edges=[{'if': {'any': [{'has': 'flat'}, {'has': 'crit'}]}, 'to': 'pa', 'res': 'ok'}, {'to': 'px', 'res': 'fail'}], item=[FLm])
A(id='pa', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('매직 두번째 옵션', 'Second magic option'), show=['flat', 'crit'],
  edges=[{'if': BOTH, 'to': 'pr', 'res': 'ok'},
         {'if': {'any': [{'all': [{'has': 'flat'}, {'sideLt': {'side': 's', 'n': 1}}]}, {'all': [{'has': 'crit'}, {'sideLt': {'side': 'p', 'n': 1}}]}]}, 'to': 'pa', 'res': 'fail', 'hide': True},
         {'to': 'px', 'res': 'fail'}], item=[FLm, CRm])
A(id='px', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  edges=[{'if': {'all': [{'not': {'has': 'flat'}}, {'not': {'has': 'crit'}}, {'not': EMPTY}]}, 'to': 'px'}, {'to': 'pa'}])
A(id='pr', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('레어', 'Rare'),
  goal=K('레어로 (세번째 옵션 랜덤)', 'To rare (third option random)'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'pd'}], item=[FLm, CRm, J('s')])
A(id='pv', kind='side', group='prep', pos=[1, 3.5], attach=['pr', 'pd'], cur='Divine_Orb', label=K('신성', 'Divine'),
  goal=K('치명타 확률 5.00%, 선택·비용 미포함', 'Crit chance 5.00%, optional, not costed'))
A(id='pd', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')], edges=[{'to': 'pf'}],
  item=[FLm, UN('p'), CRm, J('s')])
A(id='pf', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('치명타 확률이 분열되면 성공', 'Success when crit chance fractures')], ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'crit'}, 'to': 'pc', 'res': 'ok', 'label': K('치명타 확률 분열', 'Crit chance fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[FLm, UN('p'), CR, J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 5], simTo='pb', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('치명타 확률이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=2, label=ANN, goal=ANN,
  target=K('분열 + 옵션 2개만 남기기 (빈자리 3개)', 'Keep the fracture + two options (three open slots)'), edges=[{'to': 'ms'}],
  item=[J('p'), CR, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 6.6], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), CR, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 7], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 첫번째 옵션', 'First prefix'), show=['pp'],
  edges=[{'if': {'has': 'pp'}, 'to': 'k2', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[PP, CR, J('s')])
A(id='k2', kind='act', group='main', pos=[0, 8], act='essence', cur='Essence_of_the_Abyss', ess='mkp', mark=True,
  omens=['Omen_of_Dextral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접미 잡옵을 지우고 징표', 'The junk suffix goes for the Mark'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'k3'}], item=[PP, MK, CR])
A(id='k3', kind='act', group='main', pos=[0, 9], act='desecrate', cur='Ancient_Jawbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표 훼손 — 접두로', 'Desecrate the Mark: to the prefix'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'k4'}], item=[PP, UN('p'), CR])
A(id='k4', kind='act', group='main', pos=[0, 10], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='eatk', label=K('공개', 'Reveal'),
  goal=K('접두 두번째 옵션(자리 막기)', 'Second prefix (blocker)'), show=['eatk'],
  edges=[{'if': {'added': 'eatk'}, 'to': 'q1', 'res': 'ok'}, {'if': DESLOW, 'to': 'k4w', 'res': 'fail', 'label': K('빗나감', 'Miss')}]
        + [{'if': {'des': True}, 'to': 'k4x', 'res': 'fail', 'label': K('빗나감 — 레벨이 높은 옵션', 'Miss: a high-level option')}]
        + [e for e in route() if e['to'] in ('k4w', 'k1', 'q1')],
  item=[PP, BLK, CR])
A(id='k4w', kind='act', group='main', pos=[1, 10], act='chaos', cur='Greater_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('카오스', 'Chaos'),
  goal=K('빗나간 훼손 옵션 교체', 'Replace the missed desecration'),
  showText=[K('레벨이 가장 낮은 옵션 교체', 'The lowest-level option is replaced')],
  edges=[{'if': {'all': [{'has': 'pp'}, {'not': {'des': True}}, {'not': {'has': 'eatk'}}]}, 'to': 'k2', 'label': K('다시 징표', 'Mark again')}] + route())
A(id='k4x', kind='act', group='main', pos=[1, 11], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('빗나간 훼손 옵션 제거', 'Remove the missed desecration'),
  edges=[{'if': {'all': [{'has': 'pp'}, {'not': {'des': True}}, {'not': {'has': 'eatk'}}, {'not': {'famBlock': 'eatk'}}]}, 'to': 'k2', 'label': K('다시 징표', 'Mark again')}] + route())
A(id='q1', kind='act', group='main', pos=[0, 12], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세번째 옵션', 'Third prefix'), show=['hyb'],
  showText=[K('물리 피해 + 정확도 1티어·물리 피해 추가 1티어 중 먼저 뜬 것', 'T1 physical + accuracy or T1 flat physical, whichever comes first')],
  skipIf={'full': 'p'}, skipTo='q1w', skipNote=K('접두가 꽉 차 있으면 건너뜀', 'Skipped when the prefixes are full'),
  edges=[{'if': {'added': 'p3'}, 'to': 'u1', 'res': 'ok'}, {'to': 'q1w', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[PP, BLK, HY, CR])
A(id='q1w', kind='act', group='main', pos=[1, 12], act='chaos', cur='Greater_Chaos_Orb', trim={'side': 'p', 'keep': 'keepP', 'keepDes': True}, label=K('카오스', 'Chaos'),
  goal=K('접두 세번째 옵션', 'Third prefix'), show=['hyb'],
  showText=[K('물리 피해 + 정확도 1티어·물리 피해 추가 1티어 중 먼저 뜬 것', 'T1 physical + accuracy or T1 flat physical, whichever comes first')],
  edges=[{'if': {'all': [{'has': 'pp'}, {'has': 'eatk'}, {'des': True}, {'has': 'p3'}]}, 'to': 'u1', 'res': 'ok'},
         {'if': {'all': [{'has': 'pp'}, {'has': 'eatk'}, {'des': True}, {'full': 'p'}]}, 'to': 'q1w', 'res': 'fail', 'hide': True}] + route())
A(id='u1', kind='act', group='main', pos=[0, 13], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵', 'A junk suffix'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}],
  skipIf={'not': {'sideLt': {'side': 's', 'n': 2}}}, skipTo='u2', skipNote=K('접미 잡옵이 이미 있으면 건너뜀', 'Skipped if a junk suffix is already there'),
  edges=[{'to': 'u2'}], item=[PP, BLK, HY, CR, J('s')])
A(id='u2', kind='act', group='main', pos=[0, 14], act='chaos', cur='Greater_Chaos_Orb', omens=['Omen_of_Dextral_Erasure'], label=K('카오스', 'Chaos'),
  goal=K('접미 두번째 옵션', 'Second suffix'), show=['proj'],
  edges=[{'if': {'all': [{'has': 'proj'}, {'has': 'pp'}, {'has': 'p3'}, {'has': 'eatk'}]}, 'to': 'u3', 'res': 'ok'},
         {'if': {'all': [{'not': {'has': 'proj'}}, {'has': 'pp'}, {'has': 'p3'}, {'has': 'eatk'}]}, 'to': 'u2', 'res': 'fail', 'hide': True}] + route(),
  item=[PP, BLK, HY, CR, PJ])
A(id='u3', kind='act', group='main', pos=[0, 15], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵', 'A junk suffix'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}],
  skipIf={'not': {'sideLt': {'side': 's', 'n': 3}}}, skipTo='u4', skipNote=K('접미 세번째 옵션이 이미 있으면 건너뜀', 'Skipped if a third suffix is already there'),
  edges=[{'to': 'u4'}], item=[PP, BLK, HY, CR, PJ, J('s')])
A(id='u4', kind='act', group='main', pos=[0, 16], act='rune', rune=K('세를의 승리', 'Serle’s Triumph'), slots={'s': 1}, label=K('룬', 'Rune'),
  goal=K('세를의 승리 장착 (접미 +1)', 'Socket Serle’s Triumph (+1 suffix)'), showText=[K('접미 옵션 4개', 'Four suffixes')],
  skipIf={'rune': 'Serle'}, skipTo='u5', skipHide=True,
  edges=[{'to': 'u5'}], item=[PP, BLK, HY, CR, PJ, J('s'), SE])
A(id='u5', kind='act', group='main', pos=[0, 17], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵', 'A junk suffix'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}],
  skipIf={'not': {'sideLt': {'side': 's', 'n': 4}}}, skipTo='u6', skipNote=K('접미 네번째 옵션이 이미 있으면 건너뜀', 'Skipped if a fourth suffix is already there'),
  edges=[{'to': 'u6'}], item=[PP, BLK, HY, CR, PJ, J('s'), J('s'), SE])
A(id='u6', kind='act', group='main', pos=[0, 18], act='chaos', cur='Greater_Chaos_Orb', trim={'side': 's', 'keep': 'keepS'}, label=K('카오스', 'Chaos'),
  goal=K('접미 세번째·네번째 옵션 — 남은 옵션 중 먼저 뜬 것', 'Third and fourth suffix: whichever is left comes first'), show=['arr', 'cdm'],
  edges=[{'if': {'all': [{'has': 'pp'}, {'has': 'p3'}, {'has': 'eatk'}, {'has': 'proj'}, {'has': 'arr'}, {'has': 'cdm'}]}, 'to': 'z1', 'res': 'ok'},
         {'if': {'all': [{'has': 'pp'}, {'has': 'p3'}, {'has': 'eatk'}, {'has': 'proj'}]}, 'to': 'u6', 'res': 'fail', 'hide': True}] + route(),
  item=[PP, BLK, HY, CR, PJ, AR, CD, SE])
A(id='z1', kind='act', group='main', pos=[0, 19], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecration'),
  skipIf={'not': {'des': True}}, skipTo='z2', edges=[{'to': 'z2'}], item=[PP, HY, CR, PJ, AR, CD, SE])
A(id='z2', kind='act', group='main', pos=[0, 20], act='desecrate', cur='Ancient_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'z3'}],
  item=[PP, HY, UN('p'), CR, PJ, AR, CD, SE])
A(id='z3', kind='act', group='main', pos=[0, 21], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='p3', label=K('공개', 'Reveal'),
  goal=K('접두 세번째 옵션 1티어', 'T1 third prefix'), show=['flat'],
  showText=[K('물리 피해 추가가 먼저 붙었으면 물리 피해 + 정확도', 'Physical + accuracy if flat physical came first')],
  edges=[{'if': {'all': [{'has': 'hyb'}, {'has': 'flat'}]}, 'to': 'ok', 'res': 'ok'}, {'to': 'z3x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[PP, HY, FL, CR, PJ, AR, CD, SE])
A(id='z3x', kind='act', group='main', pos=[1, 21], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'if': FIN, 'to': 'z2', 'label': K('다시 훼손', 'Desecrate again')}] + route())
A(id='ok', kind='done', group='main', pos=[0, 22], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L0', 'nodes': ['pt', 'pa', 'px'], 'kr': '매직 두 옵션', 'en': 'Two magic options', 'fold': True,
  'goal': K('매직 물리 피해 추가 1티어 + 치명타 확률 1티어', 'Magic T1 flat physical + T1 crit chance'),
  'steps': [K('완벽한 진화의 오브로 매직', 'Perfect Orb of Transmutation') | {'node': 'pt'},
            K('빗나간 옵션은 소멸의 오브', 'A missed option: Orb of Annulment') | {'node': 'px'},
            K('빈자리는 완벽한 확장의 오브', 'An open slot: Perfect Orb of Augmentation') | {'node': 'pa'}],
  'item': [FLm, CRm]},
 {'id': 'L1', 'nodes': ['k2', 'k3', 'k4', 'k4w', 'k4x'], 'kr': '자리 막기', 'en': 'Blocker', 'fold': True,
  'goal': K('접두 자리 막기 — 공격 스킬의 원소 피해 1티어', 'Prefix blocker: T1 attack elemental damage'),
  'steps': [K('우측 결정화 + 심연의 에센스로 징표', 'Dextral Crystallisation + Essence of the Abyss for the Mark') | {'node': 'k2'},
            K('고대 턱뼈로 징표 훼손', 'Ancient Jawbone on the Mark') | {'node': 'k3'},
            K('심연의 메아리 공개', 'Reveal with Abyssal Echoes') | {'node': 'k4'},
            K('빗나가면 레벨이 가장 낮은 옵션을 절사 + 상위 카오스 오브로 바꾸고 징표부터', 'On a miss, Whittling + Greater Chaos replaces the lowest option, then the Mark again') | {'node': 'k4w'},
            K('빗나간 옵션 레벨이 높으면 빛의 징조 + 소멸의 오브 후 징표부터 (영상에 없음)', 'A high-level miss: Omen of Light + Annulment, then the Mark again (not in the video)') | {'node': 'k4x'}],
  'worst': K('물리 피해 %가 지워지면 카오스 단계부터', '% physical gone: back to the Chaos step') | {'to': 'k1'},
  'item': [PP, BLK, CR]},
 {'id': 'L2', 'nodes': ['z2', 'z3', 'z3x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
