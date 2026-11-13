# G7 2026-11-13: BigDaddyGaming 번개 +5 결투 마법봉(글 + 글에 붙은 영상 3Ux1lq8OaFk, 10:09) 플로우차트 생성기 — 글의 가성비 길(+6) 한 줄
# 근거: scratchpad review/G7/bigdaddy-lightning-wand-v2/timeline.md, frames/ (글 6/22판 캡처 + 영상 0:00~10:09 화면 대조)
# 실행: cd scripts/graphs && python3 gen_bigdaddy_lightning_wand.py  → bigdaddy-lightning-wand-v2.json (gen_batch26.py 끝에서도 자동 호출, 이 아이템 구간을 대신함)
# 상자 id는 옛 레시피(recipes_v5_bigdaddy-wand.py, w0~w10)와 겹치지 않게 지음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/bigdaddy-lightning-wand-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상에 실제로 나온 옵션(2:20 분열 + 주문 치명타, 3:12 초월의 합금, 9:25 마지막 공개 추가 번개)
L5n = L('s', '모든 번개 주문 스킬 레벨 +5', '+5 to Level of all Lightning Spell Skills', 'n', ['l5'])
L5 = L('s', '모든 번개 주문 스킬 레벨 +5 (분열)', '+5 to Level of all Lightning Spell Skills (fractured)', 'f', ['l5'])
CR = L('s', '주문 치명타 명중 확률 (60—73)% 증가', '(60—73)% increased Critical Hit Chance for Spells', 'n', ['crit'])
SPD = L('p', '주문 피해 (65—74)% 증가', '(65—74)% increased Spell Damage', 'j')   # 2:40 좌측 찬미 엑잘 결과(합금이 지움)
AL = L('s', '시전 속도 (26—31)% 증가 · 원소 피해의 (7—11)%를 추가 냉기 피해로 획득 (초월의 합금)',
       '(26—31)% increased Cast Speed · Gain (7—11)% of Elemental Damage as Extra Cold Damage (Transcendent Alloy)', 'c', ['trans'])
MA = L('p', '마나 최대치 (훼손)', 'Maximum Mana (desecrated)', 'd', ['blk'])
XL = L('p', '피해의 (25—27)%를 추가 번개 피해로 획득 (훼손)', 'Gain (25—27)% of Damage as Extra Lightning Damage (desecrated)', 'd', ['xl2'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V_BAL = {'param': {'L': 1}}; V_ESS = {'param': {'L': 0}}

GPL = K('주문 피해·번개 피해·주문 피해와 마나·추가 번개 피해', 'Spell, lightning, spell + mana or extra lightning damage')

g = {
 'id': 'bigdaddy-lightning-wand-v2', 'recipe': 'bigdaddy-lightning-wand-v2', 'cls': 'Wands', 'base': 'Dueling Wand', 'ilvl': 81,
 'note': ('2026-11-13 G7 글(6/22판) 전체 + 글에 붙은 영상(3Ux1lq8OaFk, 10:09) 전체 화면 대조. 글의 가성비 길(+6) 한 줄: '
          '결투 마법봉 아이템 레벨 81, 번개 주문 +5와 옵션 2개 + 턱뼈 훼손으로 옵션 4개를 만들어 분열 1/3(글·영상 1:30 말로만, 화면 없음) → '
          '분열 + 옵션 1개만 남기고 카오스 오브로 주문 치명타(영상 2:20 1티어 60%) → 좌측 찬미 + 엑잘로 접두 하나(2:40 주문 피해) → '
          '좌측 결정화 + 초월의 합금(2:48~3:12) → 보존된 턱뼈 + 심연의 메아리로 마나 최대치를 공개해 접두 자리 막기 → 상위 찬미 + 엑잘로 접두 2개 → '
          '빛의 징조 + 소멸의 오브로 막기 제거 → 보존된 턱뼈 → 마지막 접두 공개(글 Prefix cheap 1~6, 영상 3:28~3:55 말로만). '
          '영상 4:00~9:30은 글의 비싼 길(+7: 아스트리드의 창의성 → 완벽한 엑잘 = 주문 피해·마나 복합 → 좌측 결정화 + 천공의 합금 → 턱뼈로 복합 막기 → '
          '완벽한 엑잘 → 빛의 징조 → 고대 턱뼈 공개 = 추가 번개 2티어)이라 플로우차트에 넣지 않고 꿀팁 후보로만. '
          '분열 전 +5 매직 마법봉을 어떻게 만드는지는 글·영상에 없어 +5 매직 구입으로 정함(내부 결정, 정책 1장 매직 구입 시작). '
          '등급(정책 10장): 난이도 3 → 밸런스·에센셜. 카오스 주문 치명타는 카오스 오브 반복이라 두 등급 모두 1티어(C15, 영상도 1티어). '
          '밸런스 = 마나 막기·마지막 공개를 빛의 징조로 다시, 마지막 접두 1~2티어, 완벽한 엑잘. 에센셜 = 공개 결과 그대로, 상위 엑잘(글: Greater/Perfect).'),
 'params': {
  'L': {'kr': '훼손 공개', 'en': 'Desecration reveals', 'values': {'1': K('빛의 징조로 다시', 'Retry with Omen of Light'), '0': K('결과 그대로', 'Keep whatever comes')}},
  'pT': {'kr': '마지막 접두', 'en': 'Last prefix', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('나오는 대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1, 'pT': 2}}, {'id': 'ess', 'params': {'L': 0, 'pT': 4}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0, 'pT': 4}, 'tier': 'ess',
   'desc': K('훼손 공개 결과 그대로, 접두 2개는 상위 엑잘티드 오브', 'Keep both reveals; Greater Exalted Orbs for the two prefixes')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1, 'pT': 2}, 'tier': 'bal',
   'desc': K('마나 막기·마지막 접두 1~2티어까지 빛의 징조로 다시, 완벽한 엑잘티드 오브', 'Retry the mana blocker and a T1–2 last prefix with Omen of Light; Perfect Exalted Orbs')}],
 'tags': {
  'l5': {'gi': 13, 'tmax': 1}, 'crit': {'gi': 20, 'tmax': 1}, 'trans': {'gi': 60}, 'blk': {'gi': 1},
  'sd': {'gi': 3, 'tmax': '$pT'}, 'ld': {'gi': 7, 'tmax': '$pT'}, 'hy': {'gi': 4, 'tmax': '$pT'}, 'xl': {'gi': 28, 'tmax': '$pT'},
  'gp': {'anyOf': ['sd', 'ld', 'hy', 'xl'], 'label': GPL},
  # 완성 카드용(밸런스 1~2티어 고정)
  'sd2': {'gi': 3, 'tmax': 2}, 'ld2': {'gi': 7, 'tmax': 2}, 'hy2': {'gi': 4, 'tmax': 2}, 'xl2': {'gi': 28, 'tmax': 2},
  'gp2': {'anyOf': ['sd2', 'ld2', 'hy2', 'xl2'], 'label': K('주문 피해·번개 피해·주문 피해와 마나·추가 번개 피해 1~2티어', 'T1–2 spell, lightning, spell + mana or extra lightning damage')},
 },
 'require': {'all': [{'has': 'l5'}, {'has': 'crit'}, {'has': 'trans'}, {'full': 'p'}, {'any': [V_ESS, {'has': 'gp'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 0, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 (글 Base and prep, 영상 1:30 말로만) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='a1', start={'rar': 'magic', 'mods': ['l5']},
  label=K('모든 번개 주문 스킬 레벨 +5 매직 결투 마법봉 구입 (아이템 레벨 81)', 'Buy a magic Dueling Wand with +5 lightning spell skills (item level 81)'), item=[L5n])
A(id='a1', kind='act', group='prep', pos=[0, 1], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접두 랜덤 옵션 1개 — 분열 조건 옵션 4개', 'One random prefix: the fracture needs four options'), showText=[K('랜덤 옵션 1개', 'One random option')],
  skipIf={'full': 'p'}, skipTo='rg', skipHide=True, edges=[{'to': 'rg'}], item=[J('p'), L5n])
A(id='rg', kind='act', group='prep', pos=[0, 2], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'ds'}], item=[J('p'), L5n, J('s')])
A(id='ds', kind='act', group='prep', pos=[0, 3], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'fr'}],
  item=[J('p'), L5n, J('s'), UN('x')])
A(id='fr', kind='act', group='prep', pos=[0, 4], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('번개 주문 +5가 분열되면 성공', 'Success when the +5 lightning spell skills fractures')],
  edges=[{'if': {'fractured': 'l5'}, 'to': 'pc', 'res': 'ok', 'label': K('번개 주문 +5 분열', '+5 lightning spells fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), L5, J('s'), UN('x')])
A(id='xj', kind='exit', group='prep', pos=[1, 4], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('번개 주문 +5가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 5], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[L5, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 6.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[L5, J('s')])
A(id='c1', kind='act', group='main', pos=[0, 7.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 주문 치명타 명중 확률 — 분열 외 유일한 옵션', 'Spell crit chance suffix: the only option besides the fracture'), show=['crit'],
  skipIf={'has': 'crit'}, skipTo='e1', skipHide=True,
  edges=[{'if': {'has': 'crit'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[L5, CR])
A(id='e1', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 잡옵 1개 — 합금이 지울 자리', 'One junk prefix for the alloy to remove'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'al'}], item=[SPD, L5, CR])
A(id='al', kind='act', group='main', pos=[0, 9.4], act='essence', cur='Transcendent_Alloy', ess='trans', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 잡옵을 지우고 접미 세번째 옵션', 'The junk prefix goes, third suffix'),
  showText=[{'s': 's', 'kr': '시전 속도 · 원소 피해의 %를 추가 냉기 피해로 획득 (제작 옵션)', 'en': 'Cast speed · elemental damage as extra cold (crafted)'}],
  edges=[{'to': 'd1'}], item=[L5, CR, AL])
A(id='d1', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 자리 막기(훼손)', 'Prefix slot blocker (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'd2'}], item=[UN('p'), L5, CR, AL])
A(id='d2', kind='act', group='main', pos=[0, 11.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='blk', label=K('공개', 'Reveal'),
  goal=K('접두 마나 최대치(훼손) — 복합 말고 마나로 자리 막기', 'Maximum mana prefix (desecrated): plain mana, not the hybrid, blocks mana'), show=['blk'],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 자리 막기 공개 — 나오는 대로', 'Reveal the blocker: keep what comes'), 'showText': [{'s': 'p', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}], 'show': []}}],
  edges=[{'if': {'any': [{'added': 'blk'}, V_ESS]}, 'to': 'e2', 'res': 'ok'},
         {'to': 'd2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[MA, L5, CR, AL])
A(id='d2x', kind='act', group='main', pos=[1, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='e2', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 두번째·세번째 옵션 — 마나가 막혀 피해 옵션이 잘 뜸', 'Second and third prefixes: mana is blocked'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  over=[{'param': {'L': 0}, 'set': {'cur': 'Greater_Exalted_Orb'}}],
  edges=[{'to': 'lx'}], item=[MA, J('p'), J('p'), L5, CR, AL])
A(id='lx', kind='act', group='main', pos=[0, 13.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN,
  goal=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecrated option'), target=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecrated option'),
  edges=[{'to': 'd3'}], item=[J('p'), J('p'), L5, CR, AL])
A(id='d3', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 마지막 옵션(훼손)', 'Last prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'd4'}], item=[J('p'), J('p'), UN('p'), L5, CR, AL])
A(id='d4', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='gp', label=K('공개', 'Reveal'),
  goal=K('접두 추가 번개 피해(훼손) — 주문·번개 피해 증가, 주문 피해와 마나 중 먼저 뜬 것', 'Extra lightning prefix (desecrated): or spell, lightning or spell + mana damage, whichever shows first'), show=['gp'],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 마지막 옵션 공개 — 나오는 대로', 'Reveal the last prefix: keep what comes'), 'showText': [{'s': 'p', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}], 'show': []}}],
  edges=[{'if': {'any': [{'added': 'gp'}, V_ESS]}, 'to': 'ok', 'res': 'ok'},
         {'to': 'd4x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[J('p'), J('p'), XL, L5, CR, AL])
A(id='d4x', kind='act', group='main', pos=[1, 15.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'd3', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '접두 자리 막기', 'en': 'Prefix blocker'},
 {'id': 'L2', 'nodes': ['d3', 'd4', 'd4x'], 'kr': '접두 마지막 옵션(훼손)', 'en': 'Last prefix (desecrated)'},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'gp2', 'des': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'l5', 'fr': True}, {'tag': 'crit'}, {'tag': 'trans', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'l5', 'fr': True}, {'tag': 'crit'}, {'tag': 'trans', 'ess': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
