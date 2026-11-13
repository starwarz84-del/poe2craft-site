# G5 2026-11-13: Fubgun 투사체 +3 목걸이(mobalytics 0.5.5 Ice Shot Deadeye 빌드 글의 Crafting Guide 'Amulet' 1~9단계) 플로우차트 생성기
# 근거: scratchpad review/G5/fubgun-proj-amulet-v2/timeline.md, frames/guide-amulet-steps-1-9.jpg (글 전체 다시 읽음)
# 실행: cd scripts/graphs && python3 gen_fubgun_proj_amulet.py  → fubgun-proj-amulet-v2.json (gen_batch26.py 끝에서 자동 호출)
# 글이라 화면 결과가 없음: 왼쪽 아이템 칸·완성 카드의 접미는 글이 말한 묶음(저항·치명타·희귀도), 마지막 접두는 생명력·에너지 보호막 묶음(글은 '원하는 접두').
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-proj-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

PJ = L('s', '모든 투사체 스킬 레벨 +3', '+3 to Level of all Projectile Skills', 'f', ['pj'])
SPI = L('p', '정신력 +(43—50)', '+(43—50) to Spirit', 'n', ['sp'])
EN = L('p', '전역 방어도, 회피, 에너지 보호막 (20—30)% 증가', '(20—30)% increased Global Armour, Evasion and Energy Shield', 'c', ['enh'])
GS = L('s', '저항·치명타 확률·희귀도', 'Resistance, crit chance or rarity', 'n', ['gs'])
GP = L('p', '생명력·에너지 보호막', 'Life or energy shield', 'd', ['gp'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
RS = L('s', '랜덤 옵션', 'Random option', 'n')
RP = L('p', '랜덤 옵션', 'Random option', 'd')
LIGHT = K('소멸의 오브 사용', 'Use an Orb of Annulment')
ESS = lambda item: [{'param': {'L': 0}, 'set': {'item': item}}]

g = {
 'id': 'fubgun-proj-amulet-v2', 'recipe': 'fubgun-proj-amulet-v2', 'cls': 'Amulets', 'base': 'Gold Amulet', 'ilvl': 82,
 'note': ('2026-11-13 G5 글 전체 다시 대조(mobalytics Fubgun 0.5.5 Ice Shot Deadeye, Crafting Guide의 Amulet 1~9단계, 화면 캡처 guide-amulet-steps-1-9). '
          '글: 아이템 레벨 80 또는 82(82는 1티어 저항) → ① 투사체 +3 분열 목걸이(분열 또는 구입) ② 소멸의 오브로 분열 + 옵션 1개 ③ 카오스로 정신력 1~2티어 ④ 우측 찬미 + 엑잘 ⑤ 우측 결정화 + 강화의 에센스 '
          '⑥ 원소 기폭제(툴·조프·에쉬)로 퀄리티 20% ⑦ 촉진하는 찬미 + 우측 찬미 + 완벽한 엑잘(저항) ⑧ 저항이면 같은 기폭제로 한 번 더, 저항·치명타·희귀도가 아니면 소멸의 오브 또는 빗장뼈 + 우측 강령술 + 빛의 징조로 지우고 다시 '
          '⑨ 빗장뼈 + 심연의 메아리 + 빛의 징조로 마지막 접두. '
          '내부 결정(글에 없음): 베이스 = 황금 목걸이(글은 이름 없음, 장비 미리보기는 별의 목걸이), 구입 분열 베이스의 다른 옵션은 접두·접미 잡옵 1개씩, 강화의 에센스는 레어에 쓰므로 완벽한 강화의 에센스(게임 규칙), '
          '기폭제 = 조프의 기폭제(화염), 빗나간 접미는 우측 소멸의 징조 + 소멸의 오브(빗장뼈는 접미에 빈자리가 있으면 그 자리로 들어가 지우지 못함), 빗장뼈 = 보존된 빗장뼈, 마지막 접두 = 생명력·에너지 보호막 최대치·에너지 보호막 %. '
          '등급(난이도 3 → 밸런스·에센셜): 밸런스 = 글대로 반복(접미 저항·치명타·희귀도, 마지막 접두 1~2티어), 에센셜 = 반복 없이 결과 그대로(C17).'),
 'params': {'L': {'kr': '반복', 'en': 'Retries', 'values': {'1': K('글대로 다시', 'Retry as the guide'), '0': K('결과 그대로', 'Keep what comes')}},
            'pT': {'kr': '마지막 접두', 'en': 'Last prefix', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('나오는 대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1, 'pT': 2}}, {'id': 'ess', 'params': {'L': 0, 'pT': 4}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0, 'pT': 4}, 'tier': 'ess',
               'desc': K('접미 두 번과 마지막 접두 공개 모두 결과 그대로', 'Both suffix slams and the last reveal kept as they come')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1, 'pT': 2}, 'tier': 'bal',
               'desc': K('글대로: 접미 저항·치명타·희귀도까지, 마지막 접두 1~2티어까지 다시', 'As the guide: suffixes until resist, crit or rarity, last prefix retried to T1–2')}],
 'tags': {'pj': {'gi': 20, 'tmax': 1}, 'sp': {'gi': 28, 'tmax': 2}, 'enh': {'gi': 74},
          'catR': {'anyOf': [{'gi': 4}, {'gi': 7}]},
          'gs': {'anyOf': [{'gi': 4}, {'gi': 5}, {'gi': 6}, {'gi': 7}, {'gi': 8}, {'gi': 24}, {'gi': 26}], 'label': K('저항·치명타 확률·희귀도', 'Resistance, crit chance or rarity')},
          'gp': {'anyOf': [{'gi': 9, 'tmax': '$pT'}, {'gi': 13, 'tmax': '$pT'}, {'gi': 16, 'tmax': '$pT'}], 'label': K('생명력·에너지 보호막', 'Life or energy shield')},
          'gp2': {'anyOf': [{'gi': 9, 'tmax': 2}, {'gi': 13, 'tmax': 2}, {'gi': 16, 'tmax': 2}], 'label': K('생명력·에너지 보호막 1~2티어', 'T1–2 life or energy shield')}},
 'require': {'all': [{'has': 'pj'}, {'has': 'sp'}, {'has': 'enh'}, {'full': 'p'}, {'full': 's'},
                     {'any': [{'param': {'L': 0}}, {'count': {'tag': 'gs', 'min': 2}}]}, {'any': [{'param': {'L': 0}}, {'has': 'gp'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'sp'}, {'tag': 'enh'}, {'tag': 'gp2', 'des': True}, {'tag': 'pj', 'fr': True}, {'tag': 'gs'}, {'tag': 'gs'}]},
            {'id': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
             'lines': [{'tag': 'sp'}, {'tag': 'enh'}, {'side': 'p', 'random': True}, {'tag': 'pj', 'fr': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 20, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (글 1·2단계) ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='a0', start={'rar': 'rare', 'mods': [{'tag': 'pj', 'fr': True}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('모든 투사체 스킬 레벨 +3 분열 황금 목걸이 구입 (아이템 레벨 82)', 'Buy a Gold Amulet with fractured +3 Projectile Skills (item level 82)'), item=[J('p'), PJ, J('s')])
A(id='a0', kind='cleanup', group='prep', pos=[0, 1], keep=[], maxJunk=1, label=LIGHT, goal=LIGHT,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('p'), PJ])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='a1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), PJ])
A(id='a1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 첫 번째 옵션 — 정신력 1~2티어', 'First prefix: T1–2 Spirit'), show=['sp'],
  edges=[{'if': {'has': 'sp'}, 'to': 'a2', 'res': 'ok'}, {'to': 'a1', 'res': 'fail', 'hide': True}], item=[SPI, PJ])
A(id='a2', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵', 'A junk suffix'), showText=[{'s': 's', 'kr': '잡옵', 'en': 'Junk'}], edges=[{'to': 'a3'}], item=[SPI, PJ, J('s')])
A(id='a3', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Perfect_Essence_of_Enhancement', ess='enh', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 잡옵을 지우고 접두 두 번째 옵션', 'The junk suffix goes, second prefix in'),
  showText=[{'s': 'p', 'kr': '전역 방어도, 회피, 에너지 보호막 % (제작 옵션)', 'en': 'Global Armour, Evasion and Energy Shield % (crafted)'}], edges=[{'to': 'a4'}], item=[SPI, EN, PJ])
A(id='a4', kind='act', group='main', pos=[0, 6.4], act='quality', cur='Xophs_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('화염 퀄리티 20%', 'Fire quality 20%'), showText=[K('조프의 기폭제 20개', '20 Xoph\'s Catalysts')], edges=[{'to': 'a5'}], item=[SPI, EN, PJ])
A(id='a5', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation', 'Omen_of_Dextral_Exaltation'], cat='catR',
  label=K('엑잘', 'Exalt'), goal=K('접미 두 번째 옵션 — 저항·치명타 확률·희귀도 중 먼저 뜬 것', 'Second suffix: resistance, crit chance or rarity, whichever comes first'), show=['gs'],
  edges=[{'if': {'added': 'gs'}, 'to': 'a6', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'a6', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'a5x', 'res': 'fail'}], item=[SPI, EN, PJ, GS],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접미 두 번째 옵션 — 저항 노림, 나오는 대로', 'Second suffix: aiming for a resistance, keep what comes'), 'show': [],
                                    'showText': [{'s': 's', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [SPI, EN, PJ, RS]}}])
A(id='a5x', kind='act', group='main', pos=[1, 7.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=LIGHT, goal=LIGHT,
  target=K('우측 소멸의 징조로 빗나간 접미 지우기', 'Dextral Annulment removes the missed suffix'), edges=[{'to': 'a4', 'label': K('기폭제 다시', 'Catalysts again')}])
A(id='a6', kind='act', group='main', pos=[0, 8.4], act='quality', cur='Xophs_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('화염 퀄리티 다시 20%', 'Fire quality back to 20%'), showText=[K('조프의 기폭제 20개', '20 Xoph\'s Catalysts')], edges=[{'to': 'a7'}], item=[SPI, EN, PJ, GS],
  over=ESS([SPI, EN, PJ, RS]))
A(id='a7', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation', 'Omen_of_Dextral_Exaltation'], cat='catR',
  label=K('엑잘', 'Exalt'), goal=K('접미 세 번째 옵션 — 저항·치명타 확률·희귀도 중 먼저 뜬 것', 'Third suffix: resistance, crit chance or rarity, whichever comes first'), show=['gs'],
  edges=[{'if': {'added': 'gs'}, 'to': 'a8', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'a8', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'a7x', 'res': 'fail'}], item=[SPI, EN, PJ, GS, GS],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접미 세 번째 옵션 — 저항 노림, 나오는 대로', 'Third suffix: aiming for a resistance, keep what comes'), 'show': [],
                                    'showText': [{'s': 's', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [SPI, EN, PJ, RS, RS]}}])
A(id='a7x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=LIGHT, goal=LIGHT,
  target=K('우측 소멸의 징조로 빗나간 접미 지우기 — 앞 접미가 지워지면 두 번째부터', 'Dextral Annulment removes the missed suffix: losing the earlier one sends you back'),
  edges=[{'if': {'count': {'tag': 'gs', 'min': 1}}, 'to': 'a6', 'label': K('기폭제 다시', 'Catalysts again')},
         {'to': 'a4'}])
A(id='a8', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'a9'}], item=[SPI, EN, UN('p'), PJ, GS, GS], over=ESS([SPI, EN, UN('p'), PJ, RS, RS]))
A(id='a9', kind='act', group='main', pos=[0, 11.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='gp', label=K('공개', 'Reveal'),
  goal=K('접두 생명력·에너지 보호막 1~2티어', 'T1–2 life or energy shield prefix'), show=['gp'],
  edges=[{'if': {'added': 'gp'}, 'to': 'ok', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'ok', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'a9x', 'res': 'fail'}], item=[SPI, EN, GP, PJ, GS, GS],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 훼손 옵션 공개 — 나오는 대로', 'Reveal the prefix desecration: keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [SPI, EN, RP, PJ, RS, RS]}}])
A(id='a9x', kind='act', group='main', pos=[1, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'a8', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['a4', 'a5', 'a5x'], 'kr': '접미 두 번째 옵션', 'en': 'Second suffix'},
              {'id': 'L2', 'nodes': ['a8', 'a9', 'a9x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
