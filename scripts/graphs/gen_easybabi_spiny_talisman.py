# W33 2026-11-13: EasyBabi 가시투성이 부적(fabBIuR6yhw) 플로우차트 생성기 — 영상 성공 회차(성스러운 장악) 한 줄
# 근거: scratchpad review/W33-easybabi/timeline.md, frames/ (영상 0:00~6:00 화면 대조)
# 실행: cd scripts/graphs && python3 gen_easybabi_spiny_talisman.py  → easybabi-spiny-talisman-v2.json (gen_batch23.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/easybabi-spiny-talisman-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 줄 — 영상에 나온 옵션(성공 회차 성스러운 장악, 방법 시연은 도깨비불붙이 전이)
CRIT = L('s', '치명타 확률 +(4.41—5)%', '+(4.41—5)% to Critical Hit Chance', 'n', ['crit'])
AS = L('s', '공격 속도 (23—25)% 증가 (상위 가속의 에센스)', '(23—25)% increased Attack Speed (Greater Essence of Haste)', 'c', ['as'])
BAT = L('s', '모든 공격 스킬 레벨 +3 (완벽한 전투의 에센스)', '+3 to Level of all Attack Skills (Perfect Essence of Battle)', 'c', ['battle'])
ACC = L('p', '정확도 +(168—236) (훼손)', '+(168—236) to Accuracy Rating (desecrated)', 'd', ['acc'])
EATK = L('p', '공격 스킬의 원소 피해 (100—119)% 증가', '(100—119)% increased Elemental Damage with Attacks', 'n', ['eatk'])
FIRE = L('p', '화염 피해 (39—53)~(59—80) 추가', 'Adds (39—53) to (59—80) Fire Damage', 'j')
LIGHT = L('p', '번개 피해 (1—6)~(93—122) 추가 (훼손)', 'Adds (1—6) to (93—122) Lightning Damage (desecrated)', 'd', ['light'])
COLD = L('p', '냉기 피해 (84—107)~(126—161) 추가', 'Adds (84—107) to (126—161) Cold Damage', 'n', ['cold'])
RUNE = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
UN = L('p', '접두 훼손 옵션 (미공개)', 'Prefix desecration (unrevealed)', 'n')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

ELEM = ['eatk', 'cold', 'light', 'fire']
PG_H = K('원소 피해 접두 1티어 — 공격 스킬의 원소 피해·냉기·번개·화염 피해 추가', 'T1 elemental prefix: elemental attack damage, or added cold, lightning or fire')
PG_B = K('원소 피해 접두 1~2티어 — 공격 스킬의 원소 피해·냉기·번개·화염 피해 추가', 'T1–2 elemental prefix: elemental attack damage, or added cold, lightning or fire')

g = {
 'id': 'easybabi-spiny-talisman-v2', 'recipe': 'easybabi-spiny-talisman-v2', 'cls': 'Talismans', 'base': 'Spiny Talisman', 'ilvl': 82,
 'astrid': False,
 'note': ('2026-11-13 W33 영상 전체 화면 대조(근거 scratchpad review/W33-easybabi/timeline.md). 영상은 6분짜리 설명 영상으로, 방법 시연은 도깨비불붙이 전이(아이템 레벨 81, 0:31 오른쪽 = 절사 실패작), '
          '성공 회차는 성스러운 장악(아이템 레벨 82, 0:31 왼쪽·4:19~4:24). 흐름: 치명타 확률 1티어 매직 구입(1:18 거래소, 2:08 접두 1·접미 1) → 상위 가속의 에센스로 레어 + 공격 속도(2:09) → '
          '아스트리드의 창의성(1:51 장착, 2:22 툴팁) → 좌측 결정화 + 완벽한 전투의 에센스로 접두 지우고 공격 스킬 +3(2:26) → 보존된 턱뼈로 접두 훼손(2:58·3:00) → 심연의 메아리 공개, 정확도(편집 자막 3:33: 물리 % + 정확도 말고 정확도만) → '
          '상위 찬미 + 완벽한 엑잘로 접두 2개(3:50 툴팁, 3:56 시연 결과) → 빛의 징조 + 소멸의 오브로 정확도 지우고 보존된 턱뼈 + 메아리 공개 반복(4:00 카드) → '
          '절사의 징조 + 완벽한 카오스 오브(4:09·4:20, 성공 회차 4:19 화염 5티어 → 0:31 냉기 2티어). 룬 교체·퀄리티·신성한 오브는 정책 9·14장대로 뺌. '
          '등급 C17: 하이엔드 = 원소 피해 접두 1티어(절사·공개), 밸런스 = 1~2티어. 엑잘로 붙은 접두가 빗나가도 가장 낮은 레벨이 아니면 절사를 못 써서 그대로 둠(영상 4:30 타협) — 카드의 엑잘 접두 2개는 랜덤 옵션(정책 10장 2번 예외, 시뮬에서 두 개 다 원소 피해인 비율 하이엔드 18%·밸런스 47%).'),
 'params': {
   'pT': {'kr': '원소 피해 접두', 'en': 'Elemental prefixes', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'pT': 1}}, {'id': 'bal', 'params': {'pT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'pT': 2}, 'tier': 'bal',
    'desc': K('원소 피해 접두 1~2티어', 'T1–2 elemental prefixes')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'pT': 1}, 'tier': 'high',
    'desc': K('원소 피해 접두 1티어', 'T1 elemental prefixes')}],
 'tags': {
   'crit': {'gi': 18, 'tmax': 1}, 'as': {'gi': 47}, 'battle': {'gi': 56}, 'acc': {'gi': 17},
   'eatk': {'gi': 23, 'tmax': '$pT'}, 'cold': {'gi': 5, 'tmax': '$pT'}, 'light': {'gi': 7, 'tmax': '$pT'}, 'fire': {'gi': 4, 'tmax': '$pT'},
   'eatk1': {'gi': 23, 'tmax': 1}, 'cold1': {'gi': 5, 'tmax': 1}, 'light1': {'gi': 7, 'tmax': 1}, 'fire1': {'gi': 4, 'tmax': 1},
   'eatk2': {'gi': 23, 'tmax': 2}, 'cold2': {'gi': 5, 'tmax': 2}, 'light2': {'gi': 7, 'tmax': 2}, 'fire2': {'gi': 4, 'tmax': 2},
   'pg': {'anyOf': ELEM, 'label': K('원소 피해 접두 — 공격 스킬의 원소 피해·냉기·번개·화염 피해 추가', 'Elemental prefix: elemental attack damage, or added cold, lightning or fire')},
   'pgH': {'anyOf': [t + '1' for t in ELEM], 'label': PG_H},
   'pgB': {'anyOf': [t + '2' for t in ELEM], 'label': PG_B},
   'keepW': {'anyOf': ['pg', 'crit', 'as', 'battle']}},
 'require': {'all': [{'has': 'crit'}, {'has': 'as'}, {'has': 'battle'}, {'full': 'p'}, {'count': {'tag': 'pg', 'min': 1}}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# 훼손 공개 결과가 원소 피해 접두(그 등급 티어)면 성공
WS = {'whittleSafe': {'tag': 'keepW', 'keepDes': True}}
DONE3 = {'count': {'tag': 'pg', 'min': 3}}

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'magic', 'mods': [{'tag': 'crit'}, {'junk': 'p'}]},
  label=K('치명타 확률 1티어 매직 가시투성이 부적 구입 (아이템 레벨 82, 접두 1개·접미 1개)', 'Buy a magic Spiny Talisman with T1 crit chance (item level 82, one prefix and one suffix)'),
  item=[J('p'), CRIT])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='es1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), CRIT])
A(id='es1', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Greater_Essence_of_Haste', ess='as', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 공격 속도', 'Rare + attack speed suffix'),
  showText=[{'s': 's', 'kr': '공격 속도 (23—25)% 증가 (제작 옵션)', 'en': '(23—25)% increased Attack Speed (crafted)'}],
  edges=[{'to': 'ru1'}], item=[J('p'), CRIT, AS])
A(id='ru1', kind='act', group='main', pos=[0, 3.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'es2'}], item=[J('p'), CRIT, AS, RUNE])
A(id='es2', kind='act', group='main', pos=[0, 4.4], act='essence', cur='Perfect_Essence_of_Battle', ess='battle', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 지우고 접미 공격 스킬 +3', 'Clear the prefix for +3 attack skills suffix'),
  showText=[{'s': 's', 'kr': '모든 공격 스킬 레벨 +3 (제작 옵션)', 'en': '+3 to Level of all Attack Skills (crafted)'}],
  edges=[{'to': 'bd1'}], item=[CRIT, AS, BAT, RUNE])
A(id='bd1', kind='act', group='main', pos=[0, 5.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 훼손 — 정확도 자리 막기', 'Prefix desecration: block accuracy'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=[{'to': 'bv1'}], item=[UN, CRIT, AS, BAT, RUNE])
A(id='bv1', kind='act', group='main', pos=[0, 6.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='acc', label=K('공개', 'Reveal'),
  goal=K('접두 정확도 (훼손)', 'Accuracy prefix (desecrated)'), show=['acc'],
  edges=[{'if': {'added': 'acc'}, 'to': 'ex1', 'res': 'ok'}, {'to': 'bl1', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[ACC, CRIT, AS, BAT, RUNE])
A(id='bl1', kind='act', group='main', pos=[1, 6.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'bd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ex1', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째·세번째 옵션', 'Second and third prefixes'),
  showText=[{'s': 'p', 'kr': '옵션 2개 (나오는 대로)', 'en': 'Two options (as they come)'}], edges=[{'to': 'bl2'}], item=[ACC, EATK, FIRE, CRIT, AS, BAT, RUNE])
A(id='bl2', kind='act', group='main', pos=[0, 8.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('정확도(훼손 옵션) 제거', 'Remove the accuracy (desecrated option)'), edges=[{'to': 'bd2'}], item=[EATK, FIRE, CRIT, AS, BAT, RUNE])
A(id='bd2', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션 (훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=[{'to': 'bv2'}], item=[EATK, FIRE, UN, CRIT, AS, BAT, RUNE])
A(id='bv2', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='pg', label=K('공개', 'Reveal'),
  goal=K('접두 번개 피해 추가 (훼손) — 남은 원소 피해 접두 중 먼저 뜬 것', 'Desecrated added lightning prefix: whichever remaining elemental prefix lands first'),
  show=ELEM,
  edges=[{'if': {'added': 'pg'}, 'to': 'wc1', 'res': 'ok'}, {'to': 'bl3', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[EATK, FIRE, LIGHT, CRIT, AS, BAT, RUNE])
A(id='bl3', kind='act', group='main', pos=[1, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'bd2', 'label': K('다시 훼손', 'Desecrate again')}])
# 영상 4:00·4:09: 엑잘로 붙은 옵션이 마음에 안 들고 가장 낮은 레벨이면 절사 — 성공 회차는 공개 뒤(4:19 접두 3개, 정확도 없음)에 절사
A(id='wc1', kind='act', group='main', pos=[0, 11.4], act='chaos', cur='Perfect_Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('가장 낮은 레벨 접두를 냉기 피해 추가로 — 원소 피해 접두 중 먼저 뜬 것', 'Lowest-level prefix into added cold: whichever elemental prefix lands first'),
  show=ELEM,
  skipIf={'any': [DONE3, {'not': WS}]}, skipTo='ok', skipHide=True,
  skipNote=K('접두 3개가 모두 원소 피해이거나 빗나간 옵션이 가장 낮은 레벨이 아니면 건너뜀', 'Skipped when all three prefixes are elemental or the miss is not the lowest level'),
  edges=[{'if': DONE3, 'to': 'ok', 'res': 'ok'}, {'if': WS, 'to': 'wc1', 'res': 'fail', 'hide': True}, {'to': 'ok', 'res': 'ok', 'hide': True}],
  item=[EATK, COLD, LIGHT, CRIT, AS, BAT, RUNE])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['bd1', 'bv1', 'bl1'], 'kr': '정확도 자리 막기', 'en': 'Accuracy blocker', 'fold': True,
  'goal': K('접두 정확도 (훼손) — 완벽한 엑잘에 잘 뜨는 정확도를 미리 막기', 'Desecrated accuracy prefix: block the accuracy that Perfect Exalts roll often'),
  'steps': [K('보존된 턱뼈로 접두 훼손', 'Preserved Jawbone on the prefix') | {'node': 'bd1'},
            K('심연의 메아리의 징조로 공개 — 정확도만 있는 옵션', 'Reveal with Abyssal Echoes: the accuracy-only option') | {'node': 'bv1'},
            K('빗나가면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 다시 훼손', 'On a miss, Omen of Light + Orb of Annulment removes only the desecration; desecrate again') | {'node': 'bl1'}],
  'item': [ACC, CRIT, AS, BAT, RUNE]},
 {'id': 'L2', 'nodes': ['bd2', 'bv2', 'bl3'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal', 'fold': True,
  'goal': K('접두 번개 피해 추가 (훼손) — 남은 원소 피해 접두 중 먼저 뜬 것', 'Desecrated added lightning prefix: whichever remaining elemental prefix lands first'),
  'goalBy': {'high': K('접두 원소 피해 1티어 (훼손) — 남은 원소 피해 접두 1티어 중 먼저 뜬 것', 'T1 desecrated elemental prefix: whichever remaining T1 elemental prefix lands first'),
             'bal': K('접두 원소 피해 1~2티어 (훼손) — 남은 원소 피해 접두 1~2티어 중 먼저 뜬 것', 'T1–2 desecrated elemental prefix: whichever remaining T1–2 elemental prefix lands first')},
  'steps': [K('보존된 턱뼈로 접두 훼손', 'Preserved Jawbone on the prefix') | {'node': 'bd2'},
            K('심연의 메아리의 징조로 공개', 'Reveal with Abyssal Echoes') | {'node': 'bv2'},
            K('빗나가면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 다시 훼손', 'On a miss, Omen of Light + Orb of Annulment removes only the desecration; desecrate again') | {'node': 'bl3'}],
  'item': [EATK, FIRE, LIGHT, CRIT, AS, BAT, RUNE]},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'pgH', 'des': True}, {'tag': 'crit'}, {'tag': 'as', 'ess': True}, {'tag': 'battle', 'ess': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'pgB', 'des': True}, {'tag': 'crit'}, {'tag': 'as', 'ess': True}, {'tag': 'battle', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
