# G3 2026-11-13: Diztoh 60% 소켓 효과 +2 투사체 장갑(CI7zQO_Ml_s) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G3/diztoh-socket-gloves-v2/timeline.md, frames/ (영상 0:00~8:50 화면 대조)
# 실행: cd scripts/graphs && python3 gen_diztoh_socket_gloves.py  → diztoh-socket-gloves-v2.json (gen_batch11.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-socket-gloves-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 줄 — 영상 성공 회차에 나온 옵션
ES = L('p', '에너지 보호막 최대치 +(48—60)', '+(48—60) to maximum Energy Shield', 'n', ['esf'])
PROJ = L('s', '모든 투사체 스킬 레벨 +2', '+2 to Level of all Projectile Skills', 'n', ['proj2'])
RARm = L('s', '아이템 희귀도 (15—18)% 증가 (상위 풍요의 에센스)', '(15—18)% increased Rarity of Items found (Greater Essence of Opulence)', 'c', ['rar'])
RARf = L('s', '아이템 희귀도 (15—18)% 증가 (상위 풍요의 에센스)', '(15—18)% increased Rarity of Items found (Greater Essence of Opulence)', 'f', ['rar'])
SOCK = L('s', '장착된 증강물 효과 60% 증가 (경악의 에센스)', '60% increased effect of Socketed Augment Items (Essence of Horror)', 'c', ['sock'])
PSPD = L('p', '투사체 속도 (21—30)% 증가', '(21—30)% increased Projectile Speed', 'n')   # 태그 없음: 엑잘은 나오는 대로
PDMG = L('p', '투사체 피해 (21—30)% 증가 (훼손)', '(21—30)% increased Projectile Damage (desecrated)', 'd', ['pdmg'])
BLK = L('p', '공격에 물리 피해 추가 (훼손, 자리 막기)', 'Adds Physical Damage to Attacks (desecrated, blocker)', 'j')
UN = L('p', '접두 훼손 옵션 (미공개)', 'Prefix desecration (unrevealed)', 'n')
KOLR = L('r', '콜르의 사냥', 'Kolr’s Hunt', 'r')
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

REV_B = K('투사체 피해 증가·에너지 보호막 % 증가 1~2티어', 'T1–2 projectile damage or % energy shield')

g = {
 'id': 'diztoh-socket-gloves-v2', 'recipe': 'diztoh-socket-gloves-v2', 'cls': 'Gloves_int', 'base': 'Sirenscale Gloves', 'ilvl': 81,
 'xsub': ["Kolr's Hunt"], 'xroll': True,
 'note': ('2026-11-13 G3 영상 전체 화면 대조(근거 scratchpad review/G3/diztoh-socket-gloves-v2/timeline.md). 성공 회차 한 줄: '
          '특출난 사이렌비늘 장갑(아이템 레벨 81)에 콜르의 사냥 장착·퀄리티 20%(0:17~0:37) → 완벽한 진화 + 소멸 반복(0:40~1:44) → 완벽한 확장으로 ES 최대치 +48(1:45)·투사체 +2(1:46) → '
          '상위 풍요의 에센스로 레어 + 희귀도 18%(2:08) → 좌측 강령술 + 보존된 갈비뼈로 접두 훼손(2:52~2:56) → 신성한 오브(선택, 3:05~3:32) → 분열 = 희귀도(3:43) → '
          '아스트리드의 창의성(4:05) → 좌측 결정화 + 경악의 에센스, 훼손이 지워지고 장착 증강 효과 60%(4:47) → 고대 갈비뼈 → 메아리 공개 빗나감, 물리 피해 추가를 자리 막기로 받음(5:17~5:33) → '
          '완벽한 엑잘로 투사체 속도 28%(5:45~5:49) → 빛의 징조 + 소멸 → 고대 갈비뼈 → 공개 ES 68%(3티어) → 빛의 징조 + 소멸 → 고대 갈비뼈 → 공개 투사체 피해 27%(2티어, 6:20). '
          '룬 교체(페누무스 회전의 룬)·바알 방어구 장인의 주입기·타락(6:32~8:50)은 정책 9·14장대로 뺌. '
          '내부 결정: 분열은 세 옵션 중 무엇이 분열돼도 같은 흐름(영상 = 희귀도, 의도 = 투사체 +2)이라 카드에 분열 표시를 하지 않음. '
          '경악의 에센스가 에너지 보호막 최대치를 지우면(영상은 지우지 않음) 새 베이스. 두 번째 훼손부터 강령술 징조는 접미가 꽉 차 뺌. '
          '등급(난이도 3): 밸런스 = 훼손 공개 투사체 피해·ES % 1~2티어까지 빛의 징조로 다시(영상: 3티어 ES를 버리고 2티어 투사체 피해), 엑잘 접두는 랜덤 옵션 / 에센셜 = 공개 한 번, 결과 그대로.'),
 'params': {
   'dT': {'kr': '훼손 접두', 'en': 'Desecrated prefix', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어, 한 번', 'T1–4, once')}},
   'g': {'kr': '훼손 다시', 'en': 'Redo the desecration', 'values': {'1': K('빛의 징조로 다시', 'Omen of Light retries'), '0': K('한 번', 'Once')}}},
 'strategies': [{'id': 'bal', 'params': {'dT': 2, 'g': 1}}, {'id': 'ess', 'params': {'dT': 4, 'g': 0}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'dT': 4, 'g': 0}, 'tier': 'ess',
    'desc': K('훼손 공개 한 번, 결과 그대로', 'One reveal, kept as it comes')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'dT': 2, 'g': 1}, 'tier': 'bal',
    'desc': K('훼손 접두 투사체 피해·에너지 보호막 % 1~2티어까지 빛의 징조로 다시', 'Omen of Light retries until a T1–2 projectile damage or % ES desecration')}],
 'tags': {
   'esf': {'gi': 8, 'tmax': 1}, 'proj2': {'gi': 82, 'tmax': 1}, 'rar': {'gi': 57, 'tmax': 1}, 'sock': {'gi': 59},
   'magicGood': {'anyOf': ['esf', 'proj2'], 'label': K('에너지 보호막 최대치 1티어·모든 투사체 스킬 레벨 +2', 'T1 flat energy shield or +2 projectile skills')},
   'pdmg': {'gi': 71, 'tmax': '$dT'}, 'esp': {'gi': 9, 'tmax': '$dT'}, 'pspd': {'gi': 73},
   'pdmg2': {'gi': 71, 'tmax': 2}, 'esp2': {'gi': 9, 'tmax': 2},
   'rev': {'anyOf': ['pdmg', 'esp'], 'label': K('투사체 피해 증가·에너지 보호막 % 증가', 'Projectile damage or % energy shield')},
   'revB': {'anyOf': ['pdmg2', 'esp2'], 'label': REV_B}},
 'conds': {'magicDone': {'all': [{'has': 'esf'}, {'has': 'proj2'}]}},
 'require': {'all': [{'has': 'esf'}, {'has': 'proj2'}, {'has': 'rar'}, {'has': 'sock'}, {'full': 'p'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 2]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h1',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h1', kind='base', group='prep', pos=[0, 0], next='h2',
  start={'rar': 'normal', 'mods': [], 'quality': 20, 'runes': [K('콜르의 사냥', "Kolr's Hunt")]},
  label=K('특출난 사이렌비늘 장갑 구입 (아이템 레벨 81), 콜르의 사냥 장착, 퀄리티 20%', 'Buy exceptional Sirenscale Gloves (item level 81), socket Kolr’s Hunt, quality 20%'),
  item=[KOLR])
A(id='h2', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation',
  label=K('매직 첫 번째 옵션', 'First magic option'), goal=K('접두 에너지 보호막 최대치 1티어', 'T1 flat energy shield prefix'), show=['esf'],
  edges=[{'if': {'added': 'magicGood'}, 'to': 'h3', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'h2x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
  ask=K('원하는 옵션?', 'Wanted option?'), item=[ES, KOLR])
A(id='h2x', kind='cleanup', group='prep', pos=[1, 1], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  note=K('옵션이 없는 매직 아이템이 되어 다음은 확장의 오브', 'The item stays magic with no options, so augment next'),
  edges=[{'to': 'h3'}])
A(id='h3', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation',
  label=K('매직 두 번째 옵션', 'Second magic option'), goal=K('접미 모든 투사체 스킬 레벨 +2', '+2 projectile skills suffix'), show=['proj2'],
  edges=[{'if': {'ref': 'magicDone'}, 'to': 'h4', 'res': 'ok', 'label': K('성공', 'hit')},
         {'to': 'h3x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
  ask=K('둘 다 맞음?', 'Both options?'), item=[ES, PROJ, KOLR])
A(id='h3x', kind='cleanup', group='prep', pos=[1, 2], keep=['magicGood'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'), ask=K('뭐가 지워짐?', 'What was removed?'),
  edges=[{'lost': 'magicGood', 'to': 'h3y', 'res': 'fail', 'label': K('원하는 옵션 지워짐', 'wanted option gone')},
         {'to': 'h3', 'res': 'ok', 'label': K('잡옵 지워짐', 'junk gone')}])
A(id='h3y', kind='cleanup', group='prep', pos=[2, 2], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('남은 옵션 지우기', 'Remove the remaining option'), edges=[{'to': 'h3'}])
A(id='h4', kind='act', group='prep', pos=[0, 3], act='essence', cur='Greater_Essence_of_Opulence', ess='rar',
  label=K('에센스', 'Essence'), goal=K('레어 + 접미 아이템 희귀도', 'Rare + item rarity suffix'),
  showText=[{'s': 's', 'kr': '아이템 희귀도 (15—18)% 증가 (제작 옵션)', 'en': '(15—18)% increased Rarity of Items found (crafted)'}],
  edges=[{'to': 'h5'}], item=[ES, PROJ, RARm, KOLR])
A(id='h5', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('접두 훼손 옵션 (미공개, 분열되지 않음)', 'Prefix desecration (unrevealed, cannot fracture)')],
  edges=[{'to': 'h7'}], item=[UN, ES, PROJ, RARm, KOLR])
A(id='h6', kind='side', group='prep', pos=[1, 4.5], act='divine', cur='Divine_Orb', attach=['h5', 'h7'],
  label=K('수치 올리기', 'Divine the values'), goal=K('옵션 수치 다시 굴리기 (선택)', 'Reroll option values (optional)'),
  showText=[K('모든 옵션 수치 다시 굴림', 'Rerolls every value')])
A(id='h7', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb',
  label=K('분열', 'Fracture'), goal=K('아이템 희귀도 분열 — 공개된 옵션 3개 중 하나', 'Fracture the item rarity: one of the three revealed options'),
  showText=[K('투사체 +2·에너지 보호막 최대치가 분열돼도 같은 흐름', 'Same route if +2 projectile or the flat ES fractures')],
  edges=[{'to': 'ms'}], item=[UN, ES, PROJ, RARf, KOLR])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 6.4], next='m1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[UN, ES, PROJ, RARf, KOLR])
A(id='m1', kind='act', group='main', pos=[0, 7.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'm2'}], item=[UN, ES, PROJ, RARf, KOLR, AST])
A(id='m2', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Essence_of_Horror', ess='sock', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 훼손 옵션을 지우고 접미 장착된 증강물 효과 60%', 'Clear the prefix desecration for 60% socketed augment effect'),
  showText=[{'s': 's', 'kr': '장착된 증강물 효과 60% 증가 (제작 옵션)', 'en': '60% increased effect of Socketed Augment Items (crafted)'}],
  ask=K('뭐가 지워짐?', 'What was removed?'),
  edges=[{'if': {'has': 'esf'}, 'to': 'm3', 'res': 'ok', 'label': K('훼손 옵션 지워짐', 'desecration gone')},
         {'to': 'xe', 'res': 'fail', 'label': K('에너지 보호막 최대치 지워짐', 'flat ES gone')}],
  item=[ES, PROJ, RARf, SOCK, KOLR, AST])
A(id='xe', kind='exit', group='main', pos=[1, 8.4], simTo='h1', variant='fail', label=K('에너지 보호막 지워짐', 'Flat ES gone'),
  note=K('새 베이스로 처음부터', 'Start over on a new base'))
A(id='m3', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손)', 'Second prefix option (desecrated)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=[{'to': 'm4'}], item=[UN, ES, PROJ, RARf, SOCK, KOLR, AST])
A(id='m4', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev', label=K('공개', 'Reveal'),
  goal=K('접두 에너지 보호막 % 증가 — 빗나가면 아무 옵션이나 받아 자리 막기', '% energy shield prefix: on a miss take any option as a blocker'),
  show=['esp', 'pdmg'],
  edges=[{'if': {'added': 'rev'}, 'to': 'm5h', 'res': 'ok', 'label': K('목표 옵션', 'wanted option')},
         {'to': 'm5', 'res': 'fail', 'label': K('빗나감 — 자리 막기', 'Miss: keep as a blocker')}],
  item=[ES, BLK, PROJ, RARf, SOCK, KOLR, AST])
A(id='m5h', kind='act', group='main', pos=[1, 10.9], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션 — 완성', 'Third prefix option: finished'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], edges=[{'to': 'ok', 'res': 'ok'}])
A(id='m5', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션', 'Third prefix option'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}],
  edges=[{'if': {'param': {'g': 0}}, 'to': 'ok', 'res': 'ok'}, {'to': 'm6', 'res': 'ok'}],
  item=[ES, BLK, PSPD, PROJ, RARf, SOCK, KOLR, AST])
A(id='m6', kind='act', group='main', pos=[0, 12.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('자리 막기 훼손 옵션 제거', 'Remove the blocker desecration'), edges=[{'to': 'm7'}],
  item=[ES, PSPD, PROJ, RARf, SOCK, KOLR, AST])
A(id='m7', kind='act', group='main', pos=[0, 13.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix option (desecrated)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=[{'to': 'm8'}], item=[ES, UN, PSPD, PROJ, RARf, SOCK, KOLR, AST])
A(id='m8', kind='act', group='main', pos=[0, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev', label=K('공개', 'Reveal'),
  goal=K('접두 투사체 피해 증가 2티어 (훼손) — 투사체 피해·에너지 보호막 % 중 먼저 뜬 것', 'T2 projectile damage prefix (desecrated): projectile damage or % ES, whichever lands first'),
  show=['pdmg', 'esp'],
  edges=[{'if': {'added': 'rev'}, 'to': 'ok', 'res': 'ok'}, {'to': 'm9', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[ES, PDMG, PSPD, PROJ, RARf, SOCK, KOLR, AST])
A(id='m9', kind='act', group='main', pos=[1, 14.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'm7', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['h2', 'h2x', 'h3', 'h3x', 'h3y'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'},
 {'id': 'L2', 'nodes': ['m7', 'm8', 'm9'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal', 'fold': True,
  'goal': K('접두 투사체 피해 증가 2티어 (훼손) — 투사체 피해·에너지 보호막 % 중 먼저 뜬 것', 'T2 projectile damage prefix (desecrated): projectile damage or % ES, whichever lands first'),
  'goalBy': {'bal': K('접두 투사체 피해 증가 2티어 (훼손) — 투사체 피해·에너지 보호막 % 1~2티어 중 먼저 뜬 것', 'T2 projectile damage prefix (desecrated): T1–2 projectile damage or % ES, whichever lands first')},
  'steps': [K('고대 갈비뼈로 빈 접두에 훼손', 'Ancient Rib into the empty prefix') | {'node': 'm7'},
            K('심연의 메아리의 징조로 공개', 'Reveal with Abyssal Echoes') | {'node': 'm8'},
            K('빗나가면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 다시 훼손', 'On a miss, Omen of Light + Orb of Annulment removes only the desecration; desecrate again') | {'node': 'm9'}],
  'item': [ES, PDMG, PSPD, PROJ, RARf, SOCK, KOLR, AST]},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'esf'}, {'side': 'p', 'random': True}, {'tag': 'revB', 'des': True}, {'tag': 'proj2'}, {'tag': 'rar', 'ess': True}, {'tag': 'sock', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'esf'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'proj2'}, {'tag': 'rar', 'ess': True}, {'tag': 'sock', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
