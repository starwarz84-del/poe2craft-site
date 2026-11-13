# W22 2026-11-13: Diztoh 엔드게임 육척봉(YfGJyBrObxI) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W22-endgame-staff/timeline.md, frames/ (영상 0:00~17:42 화면 대조)
# 실행: cd scripts/graphs && python3 gen_diztoh_endgame_quarterstaff.py  → diztoh-endgame-quarterstaff-v2.json (gen_batch8.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-endgame-quarterstaff-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

ML = L('s', '모든 근접 스킬 레벨 +5 (분열)', '+5 to Level of all Melee Skills (fractured)', 'f', ['melee'])
FLAT = L('p', '물리 피해 (23—35)~(39—59) 추가', 'Adds (23—35) to (39—59) Physical Damage', 'n', ['pflat'])
PCT = L('p', '물리 피해 (155—169)% 증가', '(155—169)% increased Physical Damage', 'n', ['ppct'])
FIRE = L('p', '화염 피해 (56—70)~(84—107) 추가', 'Adds (56—70) to (84—107) Fire Damage', 'n')
LPH = L('s', '명중한 적 하나당 생명력 5 획득', 'Grants 5 Life per Enemy Hit', 'j')
AS = L('s', '공격 속도 (17—19)% 증가', '(17—19)% increased Attack Speed', 'n', ['as'])
LPK = L('s', '처치한 적 하나당 생명력 획득', 'Gain Life per enemy killed', 'j')
UN = L('s', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
CD = L('s', '치명타 피해 보너스 +(23—25)% (훼손)', '+(23—25)% to Critical Damage Bonus (desecrated)', 'd', ['cdmg'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

P1H = K('물리 피해 추가 1~3티어·물리 피해 증가 1티어·물리 피해 증가와 정확도 1티어', 'T1–3 flat physical, T1 % physical or T1 % physical and accuracy')
P1B = K('물리 피해 추가 1~3티어·물리 피해 증가 1~2티어·물리 피해 증가와 정확도 1~2티어', 'T1–3 flat physical, T1–2 % physical or T1–2 % physical and accuracy')

g = {
 'id': 'diztoh-endgame-quarterstaff-v2', 'recipe': 'diztoh-endgame-quarterstaff-v2', 'cls': 'Quarterstaves', 'base': 'Sinister Quarterstaff', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 28},
 'note': ('2026-11-13 W22 영상 전체 화면 대조(근거 scratchpad review/W22-endgame-staff/timeline.md). 성공 회차(Kraken Bane) 한 줄: '
          '근접 스킬 +5 분열 험악한 육척봉(아이템 레벨 82, 28 div, 1:58) → 소멸의 오브로 분열 + 잡옵 1개, 퀄리티 20%·소켓 2개(2:10~2:36) → '
          '상위 카오스 오브로 물리 접두(3:24 툴팁, 성공 회차 7:31 물리 피해 추가 3티어) → 상위 엑잘 + 좌측 찬미, 빗나가면 소멸의 오브(7:36 정확도 → 7:38·7:39 소멸 2번 → 7:40 상위 엑잘 = 물리 피해 증가 2티어 158%) → '
          '완벽한 엑잘 + 좌측 찬미로 세 번째 접두(8:32 화염 5티어) → 절사 + 완벽한 카오스(8:38, 새 옵션이 접미로) → 다시 엑잘(8:50 화염 4티어) → 절사 + 좌측 말소 미리보기에서 물리 피해 추가와 같은 레벨이라 그대로(9:22) → '
          '우측 말소 + 상위 카오스 반복(9:50 구입, 9:59 툴팁) → 공격 속도 4티어(10:06) → 고대 턱뼈 + 우측 강령술(11:28) → '
          '공개 빗나감(11:58 생명력 흡수) → 빛의 징조 + 소멸 → 다시 훼손(12:10) → 심연의 메아리 공개 → 치명타 피해 보너스 1티어(13:42). 사용자 결정 11-13: 영상 10:20의 엑잘(접미 채우기)을 빼고 빈 접미 자리에 훼손, 공개 빗나감은 항상 빛의 징조 + 소멸의 오브(영상 13:00 우측 소멸의 징조 50:50은 빼고 꿀팁으로). '
          '영상은 치명타 확률을 노렸지만 치명타 피해 보너스를 받아들임(13:35). 룬(완벽한 철 룬)·신성한 오브·바알 대장장이의 주입기 퀄리티 30%(14:00~17:20)는 정책 9·14장대로 뺌. '
          '등급 C17: 하이엔드 = 물리 % 1티어·공격 속도/치명타 확률 1티어·훼손 1티어, 세 번째 접두는 가장 낮은 레벨일 때만 절사 + 완벽한 카오스(영상 8:38), '
          '밸런스 = 1~2티어, 세 번째 접두는 결과 그대로. 세 번째 접두는 두 등급 모두 랜덤 옵션(절사가 물리 접두와 같은 레벨이면 영상처럼 멈춤 — 정책 10장 2번 예외).'),
 'params': {
   'xT': {'kr': '물리 피해 증가·복합', 'en': '% physical / hybrid', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'sT': {'kr': '공격 속도·치명타 확률', 'en': 'Attack speed / crit chance', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'dT': {'kr': '훼손 치명타', 'en': 'Desecrated crit', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'g': {'kr': '세 번째 접두', 'en': 'Third prefix', 'values': {'1': K('가장 낮은 레벨이면 절사로 다시', 'Whittle while it is the lowest'), '0': K('랜덤 옵션', 'Random option')}}},
 'strategies': [{'id': 'high', 'params': {'xT': 1, 'sT': 1, 'dT': 1, 'g': 1}}, {'id': 'bal', 'params': {'xT': 2, 'sT': 2, 'dT': 2, 'g': 0}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'xT': 2, 'sT': 2, 'dT': 2, 'g': 0}, 'tier': 'bal',
    'desc': K('물리 피해 증가·공격 속도·훼손 치명타 1~2티어, 세 번째 접두는 나오는 대로', 'T1–2 % physical, attack speed and desecrated crit; third prefix as it comes')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'xT': 1, 'sT': 1, 'dT': 1, 'g': 1}, 'tier': 'high',
    'desc': K('물리 피해 증가·공격 속도·훼손 치명타 1티어, 세 번째 접두는 가장 낮은 레벨일 때 절사로 다시', 'T1 % physical, attack speed and desecrated crit; whittle the third prefix while it is the lowest')}],
 'tags': {
   'melee': {'gi': 10, 'tmax': 1},
   'pflat': {'gi': 3, 'tmax': 3}, 'ppct': {'gi': 8, 'tmax': '$xT'}, 'hyb': {'gi': 9, 'tmax': '$xT'},
   'ppct1': {'gi': 8, 'tmax': 1}, 'hyb1': {'gi': 9, 'tmax': 1}, 'ppct2': {'gi': 8, 'tmax': 2}, 'hyb2': {'gi': 9, 'tmax': 2},
   'p1': {'anyOf': ['pflat', 'ppct', 'hyb'], 'label': K('물리 피해 추가 1~3티어·물리 피해 증가·물리 피해 증가와 정확도', 'T1–3 flat physical, % physical or % physical and accuracy')},
   'p1H': {'anyOf': ['pflat', 'ppct1', 'hyb1'], 'shown': ['pflat', 'ppct1'], 'label': P1H},
   'p1B': {'anyOf': ['pflat', 'ppct2', 'hyb2'], 'shown': ['pflat', 'ppct2'], 'label': P1B},
   'as': {'gi': 16, 'tmax': '$sT'}, 'crit': {'gi': 18, 'tmax': '$sT'},
   'as1': {'gi': 16, 'tmax': 1}, 'crit1': {'gi': 18, 'tmax': 1}, 'as2': {'gi': 16, 'tmax': 2}, 'crit2': {'gi': 18, 'tmax': 2},
   'sg': {'anyOf': ['as', 'crit'], 'label': K('공격 속도·치명타 확률', 'Attack speed or crit chance')},
   'sgH': {'anyOf': ['as1', 'crit1'], 'shown': 'as1', 'label': K('공격 속도·치명타 확률 1티어', 'T1 attack speed or crit chance')},
   'sgB': {'anyOf': ['as2', 'crit2'], 'shown': 'as2', 'label': K('공격 속도·치명타 확률 1~2티어', 'T1–2 attack speed or crit chance')},
   'critD': {'gi': 18, 'tmax': '$dT'}, 'cdmg': {'gi': 19, 'tmax': '$dT'},
   'critD1': {'gi': 18, 'tmax': 1}, 'cdmg1': {'gi': 19, 'tmax': 1}, 'critD2': {'gi': 18, 'tmax': 2}, 'cdmg2': {'gi': 19, 'tmax': 2},
   'cr': {'anyOf': ['critD', 'cdmg'], 'label': K('치명타 확률·치명타 피해 보너스', 'Crit chance or crit damage bonus')},
   'crH': {'anyOf': ['critD1', 'cdmg1'], 'shown': 'cdmg1', 'label': K('치명타 확률·치명타 피해 보너스 1티어', 'T1 crit chance or crit damage bonus')},
   'crB': {'anyOf': ['critD2', 'cdmg2'], 'shown': 'cdmg2', 'label': K('치명타 확률·치명타 피해 보너스 1~2티어', 'T1–2 crit chance or crit damage bonus')},
   'asc': {'anyOf': ['as', 'crit', 'cdmg']},
   'keepW': {'anyOf': ['p1', 'melee', 'sg']}},
 'conds': {'sDone': {'all': [{'added': 'cr'}, {'has': 'sg'}, {'count': {'tag': 'asc', 'min': 2}}]}},
 'require': {'all': [{'has': 'melee'}, {'count': {'tag': 'p1', 'min': 2}}, {'full': 'p'}, {'has': 'sg'}, {'count': {'tag': 'asc', 'min': 2}}, {'desSide': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='hc', start={'rar': 'rare', 'mods': [{'tag': 'melee', 'fr': True}, {'junk': 's'}, {'junk': 's'}], 'quality': 20},
  label=K('근접 스킬 +5 분열 험악한 육척봉 구입 (아이템 레벨 82, 퀄리티 20%)', 'Buy a Sinister Quarterstaff with fractured +5 melee skills (item level 82, quality 20%)'),
  item=[ML, J('s'), J('s')])
A(id='hc', kind='cleanup', group='prep', pos=[0, 1], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[ML, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ML, J('s')])
A(id='c1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Greater_Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 물리 피해 추가 3티어 — 물리 피해 접두 셋 중 먼저 뜬 것', 'T3 flat physical prefix: whichever of the three physical prefixes lands first'),
  show=['pflat', 'ppct', 'hyb'],
  edges=[{'if': {'has': 'p1'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[FLAT, ML])
A(id='e1', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 물리 피해 증가 2티어 — 남은 물리 피해 접두 중 먼저 뜬 것', 'T2 % physical prefix: whichever remaining physical prefix lands first'),
  show=['ppct', 'hyb', 'pflat'],
  edges=[{'if': {'count': {'tag': 'p1', 'min': 2}}, 'to': 'e2', 'res': 'ok'}, {'to': 'e1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[FLAT, PCT, ML])
A(id='e1x', kind='cleanup', group='main', pos=[1, 4.4], keep=['p1'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), ask=K('뭐가 지워짐?', 'What was removed?'),
  edges=[{'lost': 'p1', 'to': 'c1', 'res': 'fail', 'label': K('물리 피해 접두 지워짐 — 카오스부터', 'Physical prefix gone: back to Chaos')},
         {'to': 'e1', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='e2', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션', 'Third prefix option'), show=['hyb'],
  edges=[{'if': {'all': [{'param': {'g': 1}}, {'not': {'count': {'tag': 'p1', 'min': 3}}}, {'whittleSafe': {'tag': 'keepW'}}]}, 'to': 'e2b', 'res': 'fail',
          'label': K('가장 낮은 레벨이면 절사', 'Lowest level: Whittling')},
         {'to': 'sz', 'res': 'ok'}],
  item=[FLAT, PCT, FIRE, ML],
  over=[{'param': {'g': 0}, 'set': {'goal': K('접두 세 번째 옵션 (나오는 대로)', 'Third prefix option (keep what comes)'), 'show': [], 'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}]}}])
A(id='e2b', kind='act', group='main', pos=[1, 5.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('가장 낮은 레벨 옵션 다시 (물리 피해 접두와 같은 레벨이면 멈춤)', 'Reroll the lowest-level option (stop if it ties with a physical prefix)'), show=['hyb'],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 3}}, 'to': 'e2', 'res': 'fail', 'label': K('새 옵션이 접미로 — 다시 엑잘', 'New option on the suffix: exalt again')},
         {'if': {'count': {'tag': 'p1', 'min': 3}}, 'to': 'sz', 'res': 'ok', 'hide': True},
         {'if': {'whittleSafe': {'tag': 'keepW'}}, 'to': 'e2b', 'res': 'fail', 'hide': True},
         {'to': 'sz', 'res': 'ok', 'hide': True}])
# 영상에 없음: 접미 잡옵이 2개(접미 꽉 참)면 우측 소멸로 하나를 먼저 지움 — 다음 훼손이 빈자리로 가게(사용자 결정 11-13의 뒷받침)
A(id='sz', kind='act', group='main', pos=[0, 6.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=ANN, goal=ANN,
  target=K('접미가 꽉 차면 잡옵 하나 지우기', 'Suffixes full: remove one junk suffix'),
  skipIf={'sideLt': {'side': 's', 'n': 3}}, skipTo='s0', skipHide=True,
  skipNote=K('접미가 꽉 차지 않으면 건너뜀', 'Skipped unless the suffixes are full'),
  edges=[{'to': 's0'}])
A(id='s0', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째 옵션', 'Second suffix option'), show=['as', 'crit'],
  skipIf={'not': {'sideLt': {'side': 's', 'n': 2}}}, skipTo='s1', skipHide=True,
  skipNote=K('접미 잡옵이 이미 있으면 건너뜀', 'Skipped when a junk suffix is already there'),
  edges=[{'if': {'all': [{'has': 'sg'}, {'sideLt': {'side': 's', 'n': 3}}]}, 'to': 'd1', 'res': 'ok', 'hide': True}, {'to': 's1', 'res': 'fail', 'label': K('잡옵', 'Junk')}],
  item=[FLAT, PCT, FIRE, ML, LPH])
A(id='s1', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Greater_Chaos_Orb', omens=['Omen_of_Dextral_Erasure'], label=K('우측 말소 + 카오스', 'Dextral Erasure + Chaos'),
  goal=K('접미 공격 속도 — 공격 속도·치명타 확률 중 먼저 뜬 것', 'Attack speed suffix: attack speed or crit chance, whichever lands first'), show=['as', 'crit'],
  edges=[{'if': {'all': [{'has': 'sg'}, {'sideLt': {'side': 's', 'n': 3}}]}, 'to': 'd1', 'res': 'ok'}, {'to': 's1', 'res': 'fail', 'hide': True}],
  item=[FLAT, PCT, FIRE, ML, AS])
# 사용자 결정 11-13: 영상 10:20의 엑잘(접미 채우기)을 빼고 빈 접미 자리에 훼손 — 꽉 찬 접미를 밀어내지 않음
A(id='d1', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Ancient_Jawbone', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손) — 빈 접미 자리에', 'Third suffix (desecrated): into the empty suffix slot'),
  showText=[{'s': 's', 'kr': '접미 훼손 옵션 (미공개)', 'en': 'Suffix desecration (unrevealed)'}],
  skipIf={'des': True}, skipTo='lx', skipHide=True,
  edges=[{'to': 'r1'}], item=[UN, FLAT, PCT, FIRE, ML, AS])
A(id='r1', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cr', label=K('공개', 'Reveal'),
  goal=K('접미 치명타 피해 보너스 1티어 — 치명타 확률·치명타 피해 보너스 중 먼저 뜬 것', 'T1 crit damage bonus suffix: crit chance or crit damage bonus, whichever lands first'),
  show=['critD', 'cdmg'],
  edges=[{'if': {'ref': 'sDone'}, 'to': 'ok', 'res': 'ok'},
         {'if': {'not': {'has': 'sg'}}, 'to': 's1', 'res': 'fail', 'hide': True},
         {'to': 'lx', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[FLAT, PCT, FIRE, ML, AS, CD])
# 사용자 결정 11-13: 공개 빗나감은 항상 빛의 징조 + 소멸의 오브(영상 13:00의 우측 소멸 50:50은 꿀팁으로)
A(id='lx', kind='act', group='main', pos=[1, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 11.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L3', 'nodes': ['d1', 'r1', 'lx'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal', 'fold': True,
  'goal': K('접미 치명타 피해 보너스 (훼손) — 치명타 확률·치명타 피해 보너스 중 먼저 뜬 것', 'Desecrated crit damage bonus suffix: crit chance or crit damage bonus, whichever lands first'),
  'goalBy': {'high': K('접미 치명타 피해 보너스 1티어 (훼손) — 치명타 확률·치명타 피해 보너스 1티어 중 먼저 뜬 것', 'T1 desecrated crit damage bonus: T1 crit chance or crit damage bonus, whichever lands first'),
             'bal': K('접미 치명타 피해 보너스 1~2티어 (훼손) — 치명타 확률·치명타 피해 보너스 1~2티어 중 먼저 뜬 것', 'T1–2 desecrated crit damage bonus: T1–2 crit chance or crit damage bonus, whichever lands first')},
  'steps': [K('빈 접미 자리에 고대 턱뼈 + 우측 강령술의 징조로 훼손', 'Ancient Jawbone + Dextral Necromancy into the empty suffix slot') | {'node': 'd1'},   # 사용자 결정 11-13 (R1 검수: 화면 글에서 결정 표기 뺌)
            K('심연의 메아리의 징조로 공개', 'Reveal with Abyssal Echoes') | {'node': 'r1'},
            K('빗나가면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 다시 훼손', 'On a miss, Omen of Light + Orb of Annulment removes only the desecration; desecrate again') | {'node': 'lx'}],
  'item': [FLAT, PCT, FIRE, ML, AS, CD]},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'p1H'}, {'tag': 'p1H'}, {'side': 'p', 'random': True}, {'tag': 'melee', 'fr': True}, {'tag': 'sgH'}, {'tag': 'crH', 'des': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'p1B'}, {'tag': 'p1B'}, {'side': 'p', 'random': True}, {'tag': 'melee', 'fr': True}, {'tag': 'sgB'}, {'tag': 'crB', 'des': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
