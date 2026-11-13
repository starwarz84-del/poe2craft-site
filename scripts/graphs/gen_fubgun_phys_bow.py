# G10 2026-11-13: Fubgun 가성비 물리 활(비치명타, mobalytics 0.5.5 Ice Shot Deadeye 빌드 글의 Crafting Guide 'Non-crit Bow - ilvl 75' 1~3단계) 플로우차트 생성기
# 근거: scratchpad review/G10/fubgun-phys-bow-v2/timeline.md, frames/guide-noncrit-bow-steps-1-3.jpg (글 전체 다시 읽음)
# 실행: cd scripts/graphs && python3 gen_fubgun_phys_bow.py  → fubgun-phys-bow-v2.json (gen_batch26.py 끝에서 자동 호출)
# 상자 id는 옛 레시피(recipes_v5_fubgun-055.py b1~b6)와 겹치지 않게 pn·pe·pd·pv·px.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-phys-bow-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
TV = lambda d: {k: K(*v) for k, v in d.items()}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

PP = L('p', '물리 피해 (155—169)% 증가', '(155—169)% increased Physical Damage', 'n', ['pp'])
FA = L('p', '물리 피해 (16—24)~(28—42) 추가 (제작 옵션)', 'Adds (16—24) to (28—42) Physical Damage (crafted)', 'c', ['flat'])
CO = L('p', '냉기 피해 (55—69)~(83—106) 추가', 'Adds (55—69) to (83—106) Cold Damage', 'd', ['cold'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
RP = L('p', '랜덤 옵션', 'Random option', 'j')
RS = L('s', '랜덤 옵션', 'Random option', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
ESS = {'param': {'L': 0}}

P = {'bal': {'L': 1}, 'ess': {'L': 0}}
g = {
 'id': 'fubgun-phys-bow-v2', 'recipe': 'fubgun-phys-bow-v2', 'cls': 'Bows', 'base': 'Warmonger Bow', 'ilvl': 77,
 'note': ('2026-11-13 G10 글 전체 다시 대조(mobalytics Fubgun 0.5.5 Ice Shot Deadeye, Crafting Guide의 Non-crit Bow - ilvl 75 1~3단계, 캡처 guide-noncrit-bow-steps-1-3). '
          '글: 물리 피해 %가 높은 매직 활(확장까지, 구입 또는 진화·확장, 베이스 절멸자 활·전쟁광 활) → ① 상위 마모의 에센스(물리 피해 추가 3티어) '
          '② 좌측 강령술 + 턱뼈로 접두 훼손, 시세에 따라 심연의 메아리, 높은 원소 피해 추가(냉기가 가장 좋음) ③ 상위 찬미 + 상위·완벽한 엑잘로 남은 2자리. '
          '확정 옵션(정책 11장): 공개 = 냉기 피해 추가(글 \'cold is best\', 장비 미리보기 활도 냉기). '
          '내부 결정: 베이스 = 전쟁광 활, 아이템 레벨 77(전쟁광 활 베이스 레벨이 77이라 글의 75로는 못 나옴, 75~77 사이 달라지는 접두·접미는 정확도·처치당 생명력뿐), '
          '물리 피해 %는 구입 매직의 이 레벨 최고 티어(2티어, 정책 10장 C15 베이스에 있는 옵션), 턱뼈 = 보존된 턱뼈. '
          '등급(난이도 2 → 밸런스·에센셜, C17): 밸런스 = 심연의 메아리로 공개, 완벽한 엑잘, 에센셜 = 메아리 없이 공개, 상위 엑잘. 두 등급 모두 공개 결과 그대로. '
          '새 정책(2026-11-13 14:17): 공개 목표는 글의 \'높은 원소 피해 추가(냉기가 가장 좋음)\'대로 화염·냉기·번개 피해 추가 묶음(2~3티어 = 이 아이템 레벨의 상위 두 티어, 1티어는 레벨 81), '
          '왼쪽 칸은 냉기 피해 추가, 카드는 공개가 결과 그대로라 랜덤 옵션. 공개 빗나감의 빛의 징조 반복은 뺌(글에 없음).'),
 'params': {'L': {'kr': '심연의 메아리', 'en': 'Abyssal Echoes', 'values': TV({'1': ('사용', 'Use'), '0': ('없음', 'None')})}},
 'strategies': [{'id': 'bal', 'params': P['bal']}, {'id': 'ess', 'params': P['ess']}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': P['ess'], 'tier': 'ess',
               'desc': K('메아리 없이 공개, 마무리 상위 엑잘', 'Reveal without Echoes, Greater Exalts to finish')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': P['bal'], 'tier': 'bal',
               'desc': K('심연의 메아리로 공개, 마무리 완벽한 엑잘', 'Reveal with Abyssal Echoes, Perfect Exalts to finish')}],
 'tags': {'pp': {'gi': 7, 'tmax': 2}, 'flat': {'gi': 39}, 'cold': {'gi': 4, 'tmax': 3}, 'cold3': {'gi': 4, 'tmax': 3},
          'eany': {'anyOf': [{'gi': 3, 'tmax': 3}, {'gi': 4, 'tmax': 3}, {'gi': 6, 'tmax': 3}]}},
 'require': {'all': [{'has': 'pp'}, {'has': 'flat'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'pn',
 'finals': [{'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'pp'}, {'tag': 'flat'}, {'side': 'p', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
            {'id': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
             'lines': [{'tag': 'pp'}, {'tag': 'flat'}, {'side': 'p', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 0, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (글 머리말·1단계) ----------------
A(id='pn', kind='base', group='prep', pos=[0, 0], next='pe', start={'rar': 'magic', 'mods': [{'tag': 'pp'}, {'junk': 's'}]},
  label=K('물리 피해 % 2티어 매직 전쟁광 활 구입 (확장까지, 아이템 레벨 77)', 'Buy a magic Warmonger Bow with T2 % physical (augmented, item level 77)'), item=[PP, J('s')])
A(id='pe', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Abrasion', ess='flat', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 물리 피해 추가', 'Rare + flat physical prefix'), showText=[{'s': 'p', 'kr': '물리 피해 (16—24)~(28—42) 추가 (제작 옵션)', 'en': 'Adds (16—24) to (28—42) Physical Damage (crafted)'}],
  edges=[{'to': 'ms'}], item=[PP, FA, J('s')])
# ---------------- 옵션 추가 작업 (글 2·3단계) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='pd', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PP, FA, J('s')])
A(id='pd', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'pv'}], item=[PP, FA, UN('p'), J('s')])
A(id='pv', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='eany', label=K('공개', 'Reveal'),
  goal=K('접두 냉기 피해 추가 — 없으면 결과 그대로', 'Flat cold prefix, otherwise keep what comes'), show=['cold'],
  edges=[{'to': 'px'}], item=[PP, FA, CO, J('s')],
  over=[{'param': {'L': 0}, 'set': {'omens': [], 'goal': K('훼손 옵션 공개 — 나오는 대로', 'Reveal the desecration: keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [PP, FA, RP, J('s')]}}])
A(id='px', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션 — 나오는 대로', 'Second and third suffixes: keep what comes'), showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'ok'}], item=[PP, FA, CO, J('s'), RS, RS],
  over=[{'param': {'L': 0}, 'set': {'cur': 'Greater_Exalted_Orb', 'item': [PP, FA, RP, J('s'), RS, RS]}}])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []

# 규칙 J(사용자 확정 2026-11-13 14:43, S5): 밸런스·에센셜 완성품 카드가 같아 밸런스 하나로 합침 — 에센셜(메아리 없이 공개, 상위 엑잘)은 뺌
g['strategies'] = [x for x in g['strategies'] if x['id'] != 'ess']; g['versions'] = [x for x in g['versions'] if x['id'] != 'ess']; g['finals'] = [x for x in g['finals'] if x['id'] != 'ess']
g['params']['L']['values'] = {'1': g['params']['L']['values']['1']}
# D4 2026-11-13: 난이도 표 1(쉬움) → 에센셜만(정책 10장 C11·사용자 확정 15:42 ④) — 남은 등급(메아리 공개·완벽한 엑잘) 내용은 그대로, 이름만 에센셜로
for _x in g['strategies'] + g['versions'] + g['finals']: _x['id'] = 'ess'
for _x in g['versions']: _x.update(tier='ess', kr='에센셜', en='Essential')
for _x in g['finals']: _x.update(tier='ess', kr='에센셜 옵션', en='Essential')
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
