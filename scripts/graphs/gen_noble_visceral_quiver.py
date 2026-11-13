# W20 2026-11-13: 노블이 본능적인 화살통(2PUEwoePtRs, 0.4 영상 → 0.5 데이터) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W20-noble-quiver/timeline.md, frames/ (영상 0:00~11:46 화면 대조, 자막 없는 영상이라 화면 자막·툴팁으로 확인)
# 실행: cd scripts/graphs && python3 gen_noble_visceral_quiver.py  → noble-visceral-quiver-v2.json (gen_batch8.py의 이 아이템 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/noble-visceral-quiver-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

LFn = L('p', '공격 시 번개 피해 (1—4)~(60—71) 추가', 'Adds (1—4) to (60—71) Lightning damage to Attacks', 'n', ['light'])
LF = L('p', '공격 시 번개 피해 (1—4)~(60—71) 추가 (분열)', 'Adds (1—4) to (60—71) Lightning damage to Attacks (fractured)', 'f', ['light'])
CA = L('s', '공격 치명타 명중 확률 (35—38)% 증가', '(35—38)% increased Critical Hit Chance for Attacks', 'n', ['critA'])
CD = L('s', '공격 피해의 치명타 피해 보너스 (35—39)% 증가', '(35—39)% increased Critical Damage Bonus for Attack Damage', 'n', ['critD'])
PS = L('p', '투사체 속도 (42—46)% 증가', '(42—46)% increased Projectile Speed', 'n', ['pspd'])
BW = L('p', '활 스킬로 주는 피해 (51—59)% 증가', '(51—59)% increased Damage with Bow Skills', 'n', ['bow'])
PH = L('p', '잡옵', 'Junk', 'j')
BL1 = L('s', '이동 중 투사체 공격 시 (8—12)% 확률로 투사체 2개 추가 발사 (훼손, 자리 막기)', 'Projectile Attacks have a (8—12)% chance to fire two additional Projectiles while moving (desecrated, blocker)', 'd')
BL2 = L('s', '민첩 +(28—30) (훼손, 자리 막기)', '+(28—30) to Dexterity (desecrated, blocker)', 'd')
PJ = L('s', '모든 투사체 스킬 레벨 +1 (훼손)', '+1 to Level of all Projectile Skills (desecrated)', 'd', ['proj'])
RP = L('p', '랜덤 옵션', 'Random option', 'j')
RS_ = L('s', '랜덤 옵션 (공개된 훼손 옵션)', 'Random option (revealed desecration)', 'j')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

P = {'high': {'cT': 1, 'dT': 1, 'pT': 1, 'g': 1}, 'bal': {'cT': 2, 'dT': 2, 'pT': 2, 'g': 0}}
TV = lambda d: {k: K(*v) for k, v in d.items()}
G1 = {'param': {'g': 1}}; G0 = {'param': {'g': 0}}
S1 = {'count': {'tag': 'suf', 'min': 1}}; S2 = {'count': {'tag': 'suf', 'min': 2}}
SJ = {'junk': {'side': 's', 'tag': 'sf1'}}
PD = {'any': [{'all': [G1, {'count': {'tag': 'pre', 'min': 2}}]}, {'all': [G0, {'has': 'pre'}, {'full': 'p'}]}]}

g = {
 'id': 'noble-visceral-quiver-v2', 'recipe': 'noble-visceral-quiver-v2', 'cls': 'Quivers', 'base': 'Visceral Quiver', 'ilvl': 82,
 'note': ('2026-11-13 W20 영상 전체 화면 대조(자막 없는 영상, 화면 자막·툴팁). 성공 회차 한 줄: 노멀 본능적인 화살통(아이템 레벨 82, 0:35) → 완벽한 진화·완벽한 확장 + 소멸의 오브 반복으로 '
          '번개 피해 추가 1티어 매직(0:35~2:10) → 완벽한 제왕 + 보존된 턱뼈(2:55) → 분열 1/3(3:15, 번개 피해 추가 분열) → 소멸의 오브로 분열 + 옵션 1개(5:20) → '
          '카오스 오브·완벽한 엑잘·소멸의 오브로 접미 치명타 확률·치명타 피해 1티어(7:20~7:52) → 우측 강령술 + 보존된 턱뼈로 접미 훼손(8:02) → 완벽한 엑잘 2개로 접두(8:11, 투사체 속도 1티어) → '
          '공개는 가장 높은 레벨 옵션으로 자리 막기(8:32) → 완벽한 카오스 + 절사로 접두 잡옵 다시, 잡옵 레벨이 막기 옵션과 같으면 빛의 징조 + 소멸의 오브로 막기 옵션을 지우고 다시 훼손(8:50~10:54, 민첩 66으로 막고 활 스킬 피해 1티어) → '
          '빛의 징조 + 소멸의 오브로 막기 옵션 제거 → 보존된 턱뼈 + 공개로 모든 투사체(10:56~11:20). '
          '0.5 데이터에는 영상의 모든 투사체 +2(훼손)가 없어 일반 옵션 모든 투사체 +1(레벨 5)을 마지막 공개로 찾음 — 레벨이 가장 낮아 절사보다 먼저 붙이면 안 되므로 첫 공개는 투사체가 나와도 막기 옵션으로 받음(내부 결정). '
          '첫 접미는 영상 계획(5:20 화면 자막: 치명타 확률·치명타 피해·투사체 중 하나)대로 셋 중 먼저 뜬 것(사용자 결정 2026-11-13 06:40) — 모든 투사체 +1이 먼저 뜨면 치명타 둘을 엑잘로 채워 접미가 차므로 막기·마지막 공개를 건너뜀, 완성 카드의 투사체 줄은 훼손 표시 없이. '
          '신성한 오브(2:15 매직 단계 번개 피해 최대치)는 비용에서 뺌. 하이엔드 = 영상(모두 1티어), 밸런스 = 1~2티어, 마지막 접두·접미는 랜덤 옵션.'),
 'params': {'cT': {'kr': '공격 치명타 확률', 'en': 'Attack crit chance', 'values': TV({'1': ('1티어', 'T1'), '2': ('1~2티어', 'T1–2')})},
            'dT': {'kr': '치명타 피해', 'en': 'Crit damage', 'values': TV({'1': ('1티어', 'T1'), '2': ('1~2티어', 'T1–2')})},
            'pT': {'kr': '접두 (투사체 속도·활 스킬 피해)', 'en': 'Prefixes', 'values': TV({'1': ('1티어', 'T1'), '2': ('1~2티어', 'T1–2')})},
            'g': {'kr': '마지막 접두·접미', 'en': 'Last prefix and suffix', 'values': TV({'1': ('목표 옵션까지 반복', 'Repeat until the wanted option'), '0': ('랜덤 옵션', 'Random option')})}},
 'strategies': [{'id': 'high', 'params': P['high']}, {'id': 'bal', 'params': P['bal']}],
 'versions': [{'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': P['bal'], 'tier': 'bal',
               'desc': K('치명타·접두 1~2티어, 마지막 접두·접미는 랜덤 옵션', 'T1–2 crit and prefixes, the last prefix and suffix random')},
              {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': P['high'], 'tier': 'high',
               'desc': K('영상: 모두 1티어, 마지막 접미는 모든 투사체 공개까지', 'Video: all T1, the last suffix revealed until projectile levels')}],
 'tags': {'light': {'gi': 8, 'tmax': 1},
          'critA': {'gi': 14, 'tmax': '$cT'}, 'critD': {'gi': 15, 'tmax': '$dT'},
          'critA1': {'gi': 14, 'tmax': 1}, 'critD1': {'gi': 15, 'tmax': 1}, 'critA2': {'gi': 14, 'tmax': 2}, 'critD2': {'gi': 15, 'tmax': 2},
          'sf1': {'anyOf': ['critA', 'critD', 'proj'], 'label': K('공격 치명타 명중 확률·공격 피해의 치명타 피해 보너스·모든 투사체 스킬 레벨', 'Attack critical hit chance, critical damage bonus or projectile skill levels')},   # 첫 접미 = 영상 계획(5:20)의 셋 중 먼저 뜬 것(사용자 결정 2026-11-13 06:40)
          'suf': {'anyOf': ['critA', 'critD'], 'label': K('공격 치명타 명중 확률·공격 피해의 치명타 피해 보너스', 'Attack critical hit chance or critical damage bonus')},
          'pspd': {'gi': 18, 'tmax': '$pT'}, 'bow': {'gi': 19, 'tmax': '$pT'},
          'pspd1': {'gi': 18, 'tmax': 1}, 'bow1': {'gi': 19, 'tmax': 1}, 'pspd2': {'gi': 18, 'tmax': 2}, 'bow2': {'gi': 19, 'tmax': 2},
          'pre': {'anyOf': ['pspd', 'bow'], 'label': K('투사체 속도·활 스킬로 주는 피해', 'Projectile speed or bow skill damage')},
          'pre2': {'anyOf': ['pspd2', 'bow2'], 'shown': 'pspd2', 'label': K('투사체 속도·활 스킬로 주는 피해 1~2티어', 'T1–2 projectile speed or bow skill damage')},
          'proj': {'gi': 9},
          'keep': {'anyOf': ['critA', 'critD', 'pspd', 'bow']}},
 'require': {'all': [{'has': 'light'}, S2, {'full': 's'},
                     {'any': [{'all': [G1, {'has': 'pspd'}, {'has': 'bow'}, {'has': 'proj'}]}, {'all': [G0, {'has': 'pre'}, {'full': 'p'}]}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'light', 'fr': True}, {'tag': 'pspd1'}, {'tag': 'bow1'}, {'tag': 'critA1'}, {'tag': 'critD1'}, {'tag': 'proj'}]},
            {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'light', 'fr': True}, {'tag': 'pre2'}, {'side': 'p', 'random': True}, {'tag': 'critA2'}, {'tag': 'critD2'}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

def vis_(E, vis):
    out = []
    for e in E:
        v = vis.get(e['to'])
        if v is not None and not any(o['to'] == e['to'] and not o.get('hide') for o in out): out.append({**e, **v})
        else: out.append({**e, 'hide': True})
    return out

# 매직 단계: 번개 피해 추가가 없으면 접두가 차 있을 때 소멸의 오브, 비어 있으면 확장 (영상 0:35 화면 자막)
def MG(vis):
    return vis_([{'if': {'all': [{'has': 'light'}, {'full': 's'}]}, 'to': 'p3'}, {'if': {'has': 'light'}, 'to': 'p2'},
                 {'if': {'full': 'p'}, 'to': 'p2x'}, {'to': 'p2'}], vis)

# 옵션 추가 작업: 단계마다 아이템 상태를 다시 봄
#  접미 치명타 둘(카오스·완벽한 엑잘·소멸, 영상 5:20·7:20~7:52) → 접미 훼손(8:02) → 완벽한 엑잘로 접두(8:11) → 공개 = 자리 막기(8:32)
#  → 접두 잡옵을 완벽한 카오스 + 절사로 다시(8:50, 10:38). 잡옵 레벨이 막기 옵션 이상이면 막기 옵션을 지우고 다시 훼손(9:00~10:22), 잡옵이 치명타 옵션보다 높으면 좌측 말소의 징조(시뮬 trim 자동)
#  → 하이엔드: 막기 옵션을 지우고 모든 투사체 공개(10:56~11:20)
def R(vis):
    return vis_([{'if': {'not': {'has': 'sf1'}}, 'to': 's1'},
                 {'if': {'all': [{'not': S2}, {'any': [SJ, {'full': 's'}]}]}, 'to': 's2x'},
                 {'if': {'not': S2}, 'to': 's2'},
                 {'if': {'all': [{'sideLt': {'side': 's', 'n': 3}}, {'des': False}, {'not': {'unrevSide': 's'}}]}, 'to': 'd1'},
                 {'if': {'sideLt': {'side': 'p', 'n': 3}}, 'to': 'e1'},
                 {'if': {'unrevSide': 's'}, 'to': 'd1r'},
                 {'if': {'all': [{'not': PD}, {'whittleSafe': {'tag': 'keep', 'keepDes': True}}]}, 'to': 'w1'},
                 {'if': {'all': [{'not': PD}, {'des': True}, {'whittleSafe': {'tag': 'keep'}}]}, 'to': 'r1'},
                 {'if': {'not': PD}, 'to': 'w1'},
                 {'if': {'not': {'has': 'proj'}}, 'to': 'f1'},
                 {'to': 'ok'}], vis)

# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='p1', start={'rar': 'normal', 'mods': []},
  label=K('본능적인 화살통 구입 (노멀, 아이템 레벨 82)', 'Buy a Visceral Quiver (normal, item level 82)'), item=[])   # 0:35 화면 자막 '본능적인 화살통 82렙 일반 베이스'
A(id='p1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=MG({'p2': {}}), item=[J('x')])   # 0:35 '완벽한 진화의 오브 한번씩'
A(id='p2', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 번개 피해 추가 1티어', 'T1 flat lightning prefix'), show=['light'],
  edges=MG({'p3': {'res': 'ok'}, 'p2x': {'res': 'fail', 'label': K('다른 접두', 'Another prefix')}}), item=[LFn, J('s')])   # 0:35 '완벽한 확장의 오브와 소멸의 오브로 번피추 타겟', 2:35 매직 툴팁 번개 피해 + 공격 속도
A(id='p2x', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'), edges=MG({'p2': {'label': K('다시 확장', 'Augment again')}}))   # 1:05 '지워졌다. 다시 하면 된다'
A(id='hd', kind='side', group='prep', pos=[1, 3], attach=['p2', 'p3'], cur='Divine_Orb',
  goal=K('번개 피해 추가 수치 최대, 선택·비용 미포함', 'Max the lightning roll, optional, not costed'), label=K('신성', 'Divine'))   # 2:15 '매직상태에서 딥질', 4~60 → 4~71
A(id='p3', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'p4'}], item=[LFn, J('s'), J('x')])   # 2:55 '완벽한 제왕의 오브 던져주고'
A(id='p4', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')],
  edges=[{'to': 'pf'}], item=[LFn, J('s'), J('x'), UN('x')])   # 2:55 '보존된 턱뼈 발라주고', 3:15 툴팁 물리·번개·민첩 + 미공개 훼손
A(id='pf', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('번개 피해 추가가 분열되면 성공', 'Success when flat lightning fractures')],
  edges=[{'if': {'fractured': 'light'}, 'to': 'pc', 'res': 'ok', 'label': K('번개 피해 추가 분열', 'Flat lightning fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[LF, J('s'), J('x'), UN('x')])   # 3:15 '번피추 분열이 3개 중에 한개만 붙었다'
A(id='xj', kind='exit', group='prep', pos=[1, 5], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('번개 피해 추가가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))   # 3:25 물리·민첩 분열 2개는 재조합기(0.4)로 살림 — 꿀팁 후보
A(id='pc', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[LF, J('p')])   # 5:20 '소멸의 오브로 옵션 1자리 빼고 지워주고', 5:22 번개(분열) + 물리 7~9
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='s1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[LF, J('p')])
A(id='s1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫 옵션 — 공격 치명타 확률·치명타 피해·모든 투사체 스킬 레벨 중 먼저 뜬 것', 'First suffix: attack crit chance, crit damage or projectile skill levels, whichever lands first'), show=['critA', 'critD', 'proj'],
  edges=R({'s2': {'res': 'ok'}}), item=[LF, CA])   # 5:20 계획 자막, 7:20~7:34 카오스 반복 화면
A(id='s2', kind='act', group='main', pos=[1, 8.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('남은 접미 치명타 옵션 — 투사체가 먼저 떴으면 치명타 둘', 'The remaining crit suffix: both if projectile levels came first'), show=['critA', 'critD'],
  edges=R({'d1': {'res': 'ok'}, 's2x': {'res': 'fail', 'label': K('빗나감 — 소멸', 'Miss: annul')}}), item=[LF, CA, CD])   # 7:36 공격 치명타 확률 36%(1티어), 7:48 치명타 피해 38%(1티어)
A(id='s2x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기 — 좋은 접미가 모두 지워지면 카오스부터', 'Remove the miss: back to Chaos if no good suffix is left'),
  edges=R({'s2': {'label': K('다시 엑잘', 'Exalt again')}, 's1': {'res': 'fail', 'label': K('좋은 접미가 모두 지워짐', 'No good suffix left')}}))   # 7:40~7:46 소멸로 물리·투사체 속도·마나 획득 제거
A(id='d1', kind='act', group='main', pos=[0, 11], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=R({'e1': {}}), item=[LF, CA, CD, UN('s')])   # 8:02 '우측 강령술+ 보존된 턱뼈로 접미에 훼손을 미리 입히자'
A(id='e1', kind='act', group='main', pos=[0, 12], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 개 — 투사체 속도·활 스킬 피해 중 먼저 뜬 것', 'Two prefixes: projectile speed or bow damage, whichever lands first'), show=['pspd', 'bow'],
  edges=R({'d1r': {}}), item=[LF, PH, PS, CA, CD, UN('s')])   # 8:11 완벽한 엑잘 → 물리 피해, 8:14 → 투사체 속도 42%(1티어)
A(id='d1r', kind='act', group='main', pos=[0, 13], act='reveal', missPick='lvl', label=K('공개', 'Reveal'),
  goal=K('접미 자리 막기 — 가장 높은 레벨 옵션', 'Suffix blocker: the highest-level option'),
  showText=[{'s': 's', 'kr': '가장 높은 레벨 옵션 (모든 투사체 +1은 레벨 5라 받지 않음)', 'en': 'Highest-level option (+1 projectile skills is level 5, not taken)'}],
  edges=R({'w1': {}}), item=[LF, PH, PS, CA, CD, BL1])   # 8:32 공개 3개(투사체 +1·처치 시 생명력·이동 중 투사체 2개) → 레벨 65 훼손 옵션
A(id='w1', kind='act', group='main', pos=[0, 14], act='chaos', cur='Perfect_Chaos_Orb', trim={'side': 'p', 'keep': 'pre', 'keepDes': True},
  label=K('카오스', 'Chaos'), goal=K('접두 잡옵 다시 — 남은 접두 옵션', 'Reroll the junk prefix: the other prefix'), show=['pspd', 'bow'],
  edges=R({'f1': {'res': 'ok'}, 'r1': {'res': 'fail'}}), item=[LF, BW, PS, CA, CD, BL2])   # 8:50 '절사로 접두 옵션을 돌릴 수 있다. 완벽한 카오스', 8:58 냉기 2티어(레벨 65), 10:38~10:54 활 스킬 피해 57%
A(id='r1', kind='act', group='main', pos=[1, 14], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('막기 옵션 지우기 — 접두 잡옵과 레벨이 같거나 낮을 때', 'Remove the blocker: when it is no higher than the junk prefix'), edges=[{'to': 'r2'}])   # 9:00 '플렛 2티어는 65렙… 훼손을 한번씩 더 볼거다', 9:22 빛의 징조
A(id='r2', kind='act', group='main', pos=[1, 15], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접미 훼손 다시', 'Desecrate the suffix again'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'r3'}])
A(id='r3', kind='act', group='main', pos=[1, 16], act='reveal', missPick='lvl', label=K('공개', 'Reveal'),
  goal=K('더 높은 레벨 옵션으로 다시 막기', 'Block again with a higher-level option'),
  showText=[{'s': 's', 'kr': '가장 높은 레벨 옵션', 'en': 'Highest-level option'}], edges=R({'w1': {}}))   # 9:38·10:06 실패(마나 소모 효율 등), 10:22 민첩 +28(2티어, 레벨 66)
A(id='f1', kind='act', group='main', pos=[0, 18.6], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('막기 옵션 지우기', 'Remove the blocker'), edges=[{'to': 'f2'}], item=[LF, BW, PS, CA, CD],
  skipIf=G0, skipTo='ok', skipHide=True, skipNote=K('밸런스는 막기 옵션을 랜덤 옵션으로 두고 건너뜀', 'Balance keeps the blocker as the random option'))   # 10:56~10:58 빛의 징조 3 → 2, 소멸의 오브 17 → 16
A(id='f2', kind='act', group='main', pos=[0, 19.6], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'f3'}], item=[LF, BW, PS, CA, CD, UN('s')])   # 10:59 보존된 턱뼈 14/20, 11:14 13/20
A(id='f3', kind='act', group='main', pos=[0, 20.6], act='reveal', want='proj', label=K('공개', 'Reveal'),
  goal=K('접미 모든 투사체 스킬 레벨', 'Projectile skill levels suffix'), show=['proj'],
  edges=[{'if': {'has': 'proj'}, 'to': 'ok', 'res': 'ok'}, {'to': 'f1', 'res': 'fail', 'label': K('빗나감 — 빛의 징조', 'Miss: Omen of Light')}],
  item=[LF, BW, PS, CA, CD, PJ])   # 11:08 빗나감(마나 소모 효율·생명력 소모 전환), 11:20 모든 투사체 +2(0.4)
A(id='ok', kind='done', group='main', pos=[0, 21.6], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['s1', 's2', 's2x'], 'kr': '접미 치명타 두 옵션', 'en': 'Two crit suffixes', 'fold': True,
  'goal': K('접미 공격 치명타 명중 확률·공격 피해의 치명타 피해 보너스 1티어 — 모든 투사체 스킬 레벨까지 셋 중 먼저 뜬 것부터', 'T1 attack crit chance and crit damage suffixes: start from whichever of the three, projectile levels included, lands first'),
  'goalBy': {'high': K('접미 공격 치명타 명중 확률·공격 피해의 치명타 피해 보너스 1티어 — 모든 투사체 스킬 레벨까지 셋 중 먼저 뜬 것부터', 'T1 attack crit chance and crit damage suffixes: start from whichever of the three, projectile levels included, lands first'),
             'bal': K('접미 공격 치명타 명중 확률·공격 피해의 치명타 피해 보너스 1~2티어 — 모든 투사체 스킬 레벨까지 셋 중 먼저 뜬 것부터', 'T1–2 attack crit chance and crit damage suffixes: start from whichever of the three, projectile levels included, lands first')},
  'steps': [K('카오스 오브로 분열 외 옵션 하나 다시 — 치명타 확률·치명타 피해·모든 투사체 스킬 레벨 중 하나', 'Chaos the one unfractured option: crit chance, crit damage or projectile levels') | {'node': 's1'},
            K('완벽한 엑잘로 남은 치명타 옵션', 'Perfect Exalt for the remaining crit suffixes') | {'node': 's2'},
            K('접미 잡옵이 붙으면 소멸의 오브 — 좋은 접미가 모두 지워지면 1번부터', 'A junk suffix: Orb of Annulment, back to step 1 if no good suffix is left') | {'node': 's2x'}],
  'item': [LF, CA, CD]},
 {'id': 'L2', 'nodes': ['w1', 'r1', 'r2', 'r3'], 'kr': '접두 마지막 옵션', 'en': 'Last prefix', 'fold': True,
  'goal': K('접두 투사체 속도·활 스킬로 주는 피해 1티어 둘 — 남은 옵션', 'T1 projectile speed and bow damage prefixes: the one still missing'),
  'goalBy': {'high': K('접두 투사체 속도·활 스킬로 주는 피해 1티어 둘 — 남은 옵션', 'T1 projectile speed and bow damage prefixes: the one still missing'),
             'bal': K('접두 투사체 속도·활 스킬로 주는 피해 1~2티어 하나 + 랜덤 옵션', 'One T1–2 projectile speed or bow damage prefix + a random option')},
  'steps': [K('완벽한 카오스 오브 + 절사의 징조로 접두 잡옵 다시 — 잡옵이 치명타 옵션보다 높으면 좌측 말소의 징조도', 'Perfect Chaos + Omen of Whittling on the junk prefix: add Sinistral Erasure if the junk outranks a crit option') | {'node': 'w1'},
            K('잡옵 레벨이 막기 옵션 이상이면 빛의 징조 + 소멸의 오브로 막기 옵션 지우기', 'Junk at or above the blocker level: Omen of Light + Orb of Annulment on the blocker') | {'node': 'r1'},
            K('보존된 턱뼈로 접미 훼손 다시', 'Preserved Jawbone on the suffix again') | {'node': 'r2'},
            K('공개 — 가장 높은 레벨 옵션으로 다시 막기', 'Reveal: block again with the highest-level option') | {'node': 'r3'}],
  'item': [LF, BW, PS, CA, CD, BL2],
  'itemBy': {'high': [LF, BW, PS, CA, CD, BL2], 'bal': [LF, PS, RP, CA, CD, RS_]}},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
