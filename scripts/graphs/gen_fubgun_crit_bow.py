# G10 2026-11-13: Fubgun 가성비 치명타 활(mobalytics 0.5.5 Ice Shot Deadeye 빌드 글의 Crafting Guide 'Crit Bow - ilvl 75' 1~3단계) 플로우차트 생성기
# 근거: scratchpad review/G10/fubgun-crit-bow-v2/timeline.md, frames/guide-crit-bow-steps-1-3.jpg (글 전체 다시 읽음)
# 실행: cd scripts/graphs && python3 gen_fubgun_crit_bow.py  → fubgun-crit-bow-v2.json (gen_batch26.py 끝에서 자동 호출)
# 상자 id는 옛 레시피(recipes_v5_fubgun-055.py b1~b6)와 겹치지 않게 cn·ce·cd·cv·cl·cx.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-crit-bow-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
TV = lambda d: {k: K(*v) for k, v in d.items()}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

PP = L('p', '물리 피해 (155—169)% 증가', '(155—169)% increased Physical Damage', 'n', ['pp'])
CR = L('s', '치명타 확률 +(3.11—3.8)% (제작 옵션)', '+(3.11—3.8)% to Critical Hit Chance (crafted)', 'c', ['crit'])
FP = L('p', '물리 피해 (26—39)~(44—66) 추가', 'Adds (26—39) to (44—66) Physical Damage', 'd', ['fp'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
RP = L('p', '랜덤 옵션', 'Random option', 'j')
RS = L('s', '랜덤 옵션', 'Random option', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
ESS = {'param': {'L': 0}}

P = {'bal': {'fT': 2, 'L': 1}, 'ess': {'fT': 4, 'L': 0}}
g = {
 'id': 'fubgun-crit-bow-v2', 'recipe': 'fubgun-crit-bow-v2', 'cls': 'Bows', 'base': 'Warmonger Bow', 'ilvl': 77,
 'note': ('2026-11-13 G10 글 전체 다시 대조(mobalytics Fubgun 0.5.5 Ice Shot Deadeye, Crafting Guide의 Crit Bow - ilvl 75 1~3단계, 캡처 guide-crit-bow-steps-1-3). '
          '글: 물리 피해 %가 높은 매직 활(확장까지, 구입 또는 진화·확장, 베이스 절멸자 활·전쟁광 활) → ① 상위 추구의 에센스(치명타 확률 3티어) '
          '② 좌측 강령술 + 턱뼈로 접두 훼손, 시세에 따라 심연의 메아리(리그 초반엔 고대 턱뼈도 쌈), 높은 물리 피해 추가(높은 원소 피해 추가도 됨) ③ 상위 찬미 + 상위·완벽한 엑잘로 남은 2자리. '
          '확정 옵션(정책 11장): 공개 = 물리 피해 추가(글이 먼저 꼽은 옵션). '
          '내부 결정: 베이스 = 전쟁광 활, 아이템 레벨 77(전쟁광 활 베이스 레벨 77), 물리 피해 %는 구입 매직의 이 레벨 최고 2티어(C15), 턱뼈 = 보존된 턱뼈. '
          '등급(난이도 2 → 밸런스·에센셜, C17): 밸런스 = 메아리 + 빛의 징조로 물리 피해 추가 1~2티어, 완벽한 엑잘, 에센셜 = 공개 결과 그대로(메아리 없음), 상위 엑잘.'),
 'params': {'fT': {'kr': '물리 피해 추가', 'en': 'Flat physical', 'values': TV({'2': ('1~2티어', 'T1–2'), '4': ('나오는 대로', 'As it comes')})},
            'L': {'kr': '반복', 'en': 'Retries', 'values': TV({'1': ('빛의 징조로 다시', 'Retry with Omen of Light'), '0': ('결과 그대로', 'Keep what comes')})}},
 'strategies': [{'id': 'bal', 'params': P['bal']}, {'id': 'ess', 'params': P['ess']}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': P['ess'], 'tier': 'ess',
               'desc': K('공개 결과 그대로, 마무리 상위 엑잘', 'Reveal kept as it comes, Greater Exalts to finish')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': P['bal'], 'tier': 'bal',
               'desc': K('물리 피해 추가 1~2티어까지 빛의 징조로 다시, 마무리 완벽한 엑잘', 'Omen of Light until T1–2 flat physical, Perfect Exalts to finish')}],
 'tags': {'pp': {'gi': 7, 'tmax': 2}, 'crit': {'gi': 49}, 'fp': {'gi': 2, 'tmax': '$fT'}, 'fp2': {'gi': 2, 'tmax': 2}},
 'require': {'all': [{'has': 'pp'}, {'has': 'crit'}, {'full': 'p'}, {'full': 's'}, {'any': [ESS, {'has': 'fp'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'cn',
 'finals': [{'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'pp'}, {'tag': 'fp2'}, {'side': 'p', 'random': True}, {'tag': 'crit'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
            {'id': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
             'lines': [{'tag': 'pp'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'crit'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 0, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (글 머리말·1단계) ----------------
A(id='cn', kind='base', group='prep', pos=[0, 0], next='ce', start={'rar': 'magic', 'mods': [{'tag': 'pp'}, {'junk': 's'}]},
  label=K('물리 피해 % 2티어 매직 전쟁광 활 구입 (확장까지, 아이템 레벨 77)', 'Buy a magic Warmonger Bow with T2 % physical (augmented, item level 77)'), item=[PP, J('s')])
A(id='ce', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Seeking', ess='crit', label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 치명타 확률', 'Rare + crit chance suffix'), showText=[{'s': 's', 'kr': '치명타 확률 +(3.11—3.8)% (제작 옵션)', 'en': '+(3.11—3.8)% to Critical Hit Chance (crafted)'}],
  edges=[{'to': 'ms'}], item=[PP, J('s'), CR])
# ---------------- 옵션 추가 작업 (글 2·3단계) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='cd', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PP, J('s'), CR])
A(id='cd', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손)', 'Second prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'cv'}], item=[PP, UN('p'), J('s'), CR])
A(id='cv', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='fp', label=K('공개', 'Reveal'),
  goal=K('접두 물리 피해 추가 1~2티어', 'T1–2 flat physical prefix'), show=['fp'],
  edges=[{'if': {'has': 'fp'}, 'to': 'cx', 'res': 'ok'}, {'if': ESS, 'to': 'cx', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'cl', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[PP, FP, J('s'), CR],
  over=[{'param': {'L': 0}, 'set': {'omens': [], 'goal': K('훼손 옵션 공개 — 나오는 대로', 'Reveal the desecration: keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [PP, RP, J('s'), CR]}}])
A(id='cl', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'cd', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='cx', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('남은 접두·접미 1개씩 — 나오는 대로', 'The last prefix and suffix: keep what comes'), showText=[K('랜덤 옵션 2개', 'Two random options')],
  edges=[{'to': 'ok'}], item=[PP, FP, RP, J('s'), CR, RS],
  over=[{'param': {'L': 0}, 'set': {'cur': 'Greater_Exalted_Orb', 'item': [PP, RP, RP, J('s'), CR, RS]}}])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['cd', 'cv', 'cl'], 'kr': '접두 두 번째 옵션(훼손)', 'en': 'Second prefix (desecrated)'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
