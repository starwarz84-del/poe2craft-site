# RECIPE-A 2026-11-14: Fubgun 젬링 +4 목걸이(bz5DJ0csq58, 2026-09-09) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: docs/craft-guides.md '5차 조사' g90(영어 자막 + 1:09 단계 설명 = 5:28 실제 제작, 9:52 완성품 툴팁) + docs/craft-guides.json register(ok)
# 실행: cd scripts/graphs && python3 gen_fubgun_gemling_amulet.py  → fubgun-gemling-amulet-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-gemling-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SL = L('s', '모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills', 'f', ['spell'])
SPI = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'n', ['sp'])
MQ = L('p', '최대 퀄리티 +20%', '+20% to Maximum Quality', 'c', ['mq'])
LF = L('p', '생명력 최대치 +(100—119)', '+(100—119) to maximum Life', 'n', ['life'])
GD = L('p', '전역 방어도, 회피, 에너지 보호막 (20—30)% 증가', '(20—30)% increased Global Armour, Evasion and Energy Shield', 'c', ['gd'])
RS = L('s', '번개 저항 +(36—40)%', '+(36—40)% to Lightning Resistance', 'n', ['res'])
KQ = L('s', '모든 스킬의 퀄리티 +(3—5)%', '+(3—5)% to Quality of all Skills', 'd', ['kq'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = L('s', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
LIGHT = K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light')

g = {
 'id': 'fubgun-gemling-amulet-v2', 'recipe': 'fubgun-gemling-amulet-v2', 'cls': 'Amulets', 'base': 'Gold Amulet', 'ilvl': 80,
 'basePrice': {'Divine_Orb': 30},   # 1:09 자막: 주문 +3 분열 베이스를 직접 만들면 베이스 8~9 div, 1/3, 평균 30 div(6:03 세 번째에 성공)
 'note': ('2026-11-14 RECIPE-A: Fubgun 젬링 +4 목걸이(2026-09-09, 0.5.5) 성공 회차 한 줄(근거 docs/craft-guides.md 5차 g90, 영어 자막 + 1:09 단계 설명 = 5:28 실제 제작 + 9:52 완성품 툴팁). '
          '모든 주문 스킬 레벨 +3 분열 황금 목걸이(직접 분열하면 평균 30 div, 6:03 세 번째에 성공) → 소멸의 오브로 분열 + 옵션 1개 → 카오스로 정신력 1~2티어(6:35) → '
          '우측 찬미의 징조 + 엑잘티드 오브로 접미 잡옵 → 우측 결정화의 징조 + 균열의 에센스(최대 퀄리티 +20%) → 육체 기폭제 퀄리티 40% → 촉진하는 찬미의 징조 + 완벽한 엑잘티드 오브로 생명력(다른 옵션이면 소멸의 오브, 정신력이 지워지면 카오스부터) → '
          '쇳소리 기폭제 퀄리티 34%(주문 +3 → +4) → 절사의 징조 + 카오스 오브로 균열 옵션(레벨 1)을 지우고 새 옵션이 접미로 가길 바람(접두로 가면 다시 절사, 정신력이 지워지면 처음부터, 생명력이 지워지면 기폭제부터) → '
          '우측 결정화의 징조 + 완벽한 강화의 에센스로 그 접미를 지우고 전역 방어 → 완벽한 엑잘티드 오브 한 번 → 우측 말소의 징조 + 상위 카오스 오브 반복으로 저항(5~6번) → '
          '빗장뼈 + 검은 피의 징조 + 심연의 메아리로 모든 스킬의 퀄리티(빛의 징조 10개까지 예상, 9:48 두 번째에 성공) → 완성(9:52). 신성한 오브는 수치 다듬기라 뺌. '
          '내부 결정: ① 분열 준비 과정(베이스 옵션·네 번째 옵션 만드는 법)이 자막에 없어 분열 베이스 구입으로 두고 값은 영상이 말한 평균 30 div ② 생명력 엑잘이 빗나가면 징조 없는 소멸의 오브 — 최대 퀄리티가 지워지면 균열의 에센스부터, 빗나간 옵션이 지워지면 기폭제부터 '
          '③ 빗장뼈 등급이 자막에 없어 보존된 빗장뼈(쿠르갈 옵션 레벨 65, 검은 피의 징조로 쿠르갈만 나옴) ④ 저항은 화염·냉기·번개 중 먼저 뜬 것(영상: 번개). '
          '등급: 난이도 3(카오스 약 390개·비싼 징조 약 17개) → 밸런스(영상: 저항 2~3티어 — 아이템 레벨 80이라 1티어(레벨 82)는 못 붙음, 영상 번개 저항 38% = 2티어, 퀄리티까지 빛의 징조) · 에센셜(저항 엑잘·공개 한 번씩 결과 그대로).'),
 'params': {'rT': {'kr': '저항', 'en': 'Resistance', 'values': {'3': K('2~3티어', 'T2–3'), '9': K('나오는 대로', 'As it comes')}},
            'v': {'kr': '공개', 'en': 'Reveal', 'values': {'1': K('빛의 징조로 다시', 'Retry with Light'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'rT': 3, 'v': 1}}, {'id': 'ess', 'params': {'rT': 9, 'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'rT': 9, 'v': 2}, 'tier': 'ess',
    'desc': K('저항 엑잘 한 번·공개 한 번, 결과 그대로', 'One resistance exalt and one reveal, kept as they come')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'rT': 3, 'v': 1}, 'tier': 'bal',
    'desc': K('영상: 저항까지 우측 말소 + 상위 카오스(2~3티어), 퀄리티까지 빛의 징조', 'Video: Dextral Erasure + Greater Chaos until a resistance (T2–3), Omen of Light until quality')}],
 'tags': {'spell': {'gi': 17, 'tmax': 1}, 'sp': {'gi': 28, 'tmax': 2}, 'mq': {'gi': 81},
          'lf': {'gi': 9}, 'lp': {'gi': 10},
          'life': {'anyOf': ['lf', 'lp'], 'shown': 'lf', 'label': K('생명력 최대치·최대 생명력 %', 'Maximum Life or % maximum Life')},
          'gd': {'gi': 74},
          'fr': {'gi': 4, 'tmax': '$rT'}, 'cr': {'gi': 5, 'tmax': '$rT'}, 'lr': {'gi': 6, 'tmax': '$rT'},
          'res': {'anyOf': ['fr', 'cr', 'lr'], 'shown': 'lr', 'label': K('화염·냉기·번개 저항', 'Fire, Cold or Lightning Resistance')},
          'kq': {'gi': 46}},
 'require': {'all': [{'has': 'spell'}, {'has': 'sp'}, {'has': 'life'}, {'has': 'gd'}, {'not': {'has': 'mq'}}, {'unrev': False}, {'full': 's'},
                     {'any': [{'all': [{'has': 'res'}, {'has': 'kq'}]}, {'param': {'v': 2}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'sp'}, {'tag': 'life'}, {'tag': 'gd', 'ess': True}, {'tag': 'spell', 'fr': True}, {'tag': 'res'}, {'tag': 'kq', 'des': True}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'tag': 'sp'}, {'tag': 'life'}, {'tag': 'gd', 'ess': True}, {'tag': 'spell', 'fr': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True, 'des': True}]}],
 'finalItem': {'quality': 34, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='a0', start={'rar': 'rare', 'mods': [{'tag': 'spell', 'fr': True}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('모든 주문 스킬 레벨 +3 분열 황금 목걸이 (아이템 레벨 80)', 'A Gold Amulet with fractured +3 Spell Skills (item level 80)'), item=[J('p'), SL, J('s')])
A(id='a0', kind='cleanup', group='prep', pos=[0, 1], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('p'), SL])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), SL])
A(id='k1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 첫 번째 옵션 — 정신력 1~2티어', 'First prefix: T1–2 Spirit'), show=['sp'],
  edges=[{'if': {'has': 'sp'}, 'to': 'e1', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[SPI, SL])
A(id='e1', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵 — 에센스가 지울 자리', 'A junk suffix for the essence to remove'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}],
  edges=[{'to': 'q1'}], item=[SPI, SL, J('s')])
A(id='q1', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 최대 퀄리티 +20%', 'The junk suffix goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'q2'}], item=[SPI, MQ, SL])
A(id='q2', kind='act', group='main', pos=[0, 6.4], act='quality', cur='Flesh_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('생명력 퀄리티 40%', 'Life quality 40%'), showText=[K('육체 기폭제 40개', '40 Flesh Catalysts')], edges=[{'to': 'e2'}], item=[SPI, MQ, SL])
A(id='e2', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation'], cat='life',
  label=K('엑잘', 'Exalt'), goal=K('접두 세 번째 옵션 — 생명력', 'Third prefix: life'), show=['life'],
  edges=[{'if': {'added': 'life'}, 'to': 'q3', 'res': 'ok'}, {'to': 'e2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SPI, MQ, LF, SL])
A(id='e2x', kind='act', group='main', pos=[1, 7.4], act='annul', cur='Orb_of_Annulment', label=ANN, goal=ANN,
  target=K('빗나간 옵션 지우기', 'Remove the missed option'),
  edges=[{'if': {'not': {'has': 'sp'}}, 'to': 'kc', 'res': 'fail', 'label': K('정신력이 지워짐', 'Spirit went')},
         {'if': {'not': {'has': 'mq'}}, 'to': 'q1', 'res': 'fail', 'label': K('최대 퀄리티가 지워짐 — 에센스부터', 'Maximum Quality went: essence again')},
         {'if': {'any': [{'not': {'sideLt': {'side': 'p', 'n': 3}}}, {'not': {'sideLt': {'side': 's', 'n': 2}}}]}, 'to': 'e2x', 'res': 'fail', 'hide': True},
         {'to': 'q2', 'res': 'ok', 'label': K('빗나간 옵션이 지워짐 — 기폭제 다시', 'The missed option went: catalysts again')}])
A(id='kc', kind='cleanup', group='main', pos=[2, 7.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기고 카오스부터', 'Keep the fracture + one option, Chaos again'), edges=[{'to': 'k1', 'label': K('다시 카오스', 'Chaos again')}])
A(id='q3', kind='act', group='main', pos=[0, 8.4], act='quality', cur='Sibilant_Catalyst', count=34, q=34, label=K('퀄리티', 'Quality'),
  goal=K('시전 퀄리티 34% — 주문 +3이 +4로', 'Caster quality 34%: +3 becomes +4'), showText=[K('쇳소리 기폭제 34개', '34 Sibilant Catalysts')], edges=[{'to': 'w1'}], item=[SPI, MQ, LF, SL])
A(id='w1', kind='act', group='main', pos=[0, 9.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('균열 옵션(레벨 1)을 지우고 새 옵션을 접미로', 'The breach line (level 1) goes, a new option to a suffix'),
  showText=[{'s': 's', 'kr': '잡옵 — 다음 에센스가 지울 자리', 'en': 'Junk for the next essence to remove'}],
  edges=[{'if': {'not': {'has': 'sp'}}, 'to': 'kc', 'res': 'fail', 'label': K('정신력이 지워짐 — 처음부터', 'Spirit went: start over')},
         {'if': {'not': {'has': 'life'}}, 'to': 'q2', 'res': 'fail', 'label': K('생명력이 지워짐 — 기폭제부터', 'Life went: catalysts again')},
         {'if': {'sideLt': {'side': 'p', 'n': 3}}, 'to': 'q4', 'res': 'ok'},
         {'to': 'w1', 'res': 'fail', 'label': K('새 옵션이 접두로 — 다시 절사', 'The new option went to a prefix: Whittling again')}],
  item=[SPI, LF, SL, J('s')])
A(id='q4', kind='act', group='main', pos=[0, 10.4], act='essence', cur='Perfect_Essence_of_Enhancement', ess='gd', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 접두 전역 방어', 'The junk suffix goes, Global defences prefix in'),
  showText=[{'s': 'p', 'kr': '전역 방어도, 회피, 에너지 보호막 % (제작 옵션)', 'en': 'Global Armour, Evasion and Energy Shield % (crafted)'}], edges=[{'to': 'e3'}], item=[SPI, LF, GD, SL])
A(id='e3', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째 옵션 — 접두가 꽉 차서 접미로', 'Second suffix: prefixes are full'), showText=[{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  skipIf={'not': {'sideLt': {'side': 's', 'n': 2}}}, skipTo='k2', skipNote=K('앞 단계에서 남은 접미가 있으면 건너뜀', 'Skipped when an earlier suffix is still there'),
  edges=[{'if': {'has': 'res'}, 'to': 'd1', 'res': 'ok', 'label': K('저항이 바로 뜨면 훼손', 'A resistance right away: desecrate')}, {'to': 'k2'}], item=[SPI, LF, GD, SL, J('s')],
  over=[{'param': {'v': 2}, 'set': {'edges': [{'to': 'd1', 'res': 'ok'}], 'item': [SPI, LF, GD, SL, J('s')]}}])
A(id='k2', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Greater_Chaos_Orb', omens=['Omen_of_Dextral_Erasure'], label=K('우측 말소 + 카오스', 'Dextral Erasure + Chaos'),
  goal=K('접미 두 번째 옵션 — 저항', 'Second suffix: a resistance'), show=['res'],
  skipIf={'any': [{'param': {'v': 2}}, {'has': 'res'}]}, skipTo='d1', skipHide=True,
  goalBy={'bal': K('접미 두 번째 옵션 — 저항 2~3티어', 'Second suffix: a T2–3 resistance')},
  edges=[{'if': {'has': 'res'}, 'to': 'd1', 'res': 'ok'}, {'to': 'k2', 'res': 'fail', 'hide': True}], item=[SPI, LF, GD, SL, RS])
A(id='d1', kind='act', group='main', pos=[0, 13.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_the_Blackblooded'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세 번째 옵션(훼손) — 쿠르갈 옵션', 'Third suffix (desecrated): a Kurgal option'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'r1'}], item=[SPI, LF, GD, SL, RS, UN])
A(id='r1', kind='act', group='main', pos=[0, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='kq', label=K('공개', 'Reveal'),
  goal=K('접미 모든 스킬의 퀄리티', 'Quality of all Skills suffix'), show=['kq'],
  goalBy={'ess': K('접미 훼손 옵션 공개 — 나오는 대로 (영상: 모든 스킬의 퀄리티)', 'Reveal the suffix desecration: keep what comes (video: Quality of all Skills)')},
  edges=[{'if': {'added': 'kq'}, 'to': 'ok', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[SPI, LF, GD, SL, RS, KQ],
  over=[{'param': {'v': 2}, 'set': {'edges': [{'to': 'ok', 'res': 'ok'}]}}])
A(id='r1x', kind='act', group='main', pos=[1, 14.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 15.6], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['q2', 'e2', 'e2x'], 'kr': '생명력', 'en': 'Life'},
              {'id': 'L2', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
