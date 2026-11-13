# W6 2026-11-12: Diztoh 치명타 투구 플로우차트(새 기준) 생성기 — 영상 QuW8BOSpPpo 성공 회차 한 줄
# (마스터 11-13: 저장소 사본 — scripts/graphs/에서 python3 gen_diztoh_crit_helmet.py)
# 출력: /home/claude/poe2craft-site/scripts/graphs/diztoh-crit-helmet-v2.json
import json, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/poe2craft-site/scripts/graphs/diztoh-crit-helmet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

FLAT = L('p', '회피·에너지 보호막 최대치 1티어', 'T1 flat evasion and ES', 'f', ['flatT1'])
FLATn = L('p', '회피·에너지 보호막 최대치 1티어', 'T1 flat evasion and ES', 'n', ['flatT1'])
RAR = L('s', '아이템 희귀도 1티어', 'T1 item rarity', 'n', ['rarS1'])
JUNK = lambda s='x': L(s, '잡옵', 'Junk', 'j')
UNREV = L('s', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
CRIT = L('s', '치명타 확률 1티어', 'T1 crit chance', 'n', ['critT1'])
PCT = L('p', '회피·에너지 보호막 % 증가', '% evasion and ES', 'n', ['pct'])
HYB = L('p', '회피·에너지 보호막 % + 마나', '% evasion and ES + mana', 'n', ['hybM'])
CDMG = L('s', '치명타 피해 보너스 (훼손)', 'Crit damage bonus (desecrated)', 'd', ['cdmg'])
RND = L('s', '랜덤 옵션 (8번에서 남긴 옵션이 있으면 그 옵션)', 'Random option (or the option kept at step 8)', 'j')
LASTH = L('s', '희귀도·화염 저항·카오스 저항 1티어', 'T1 rarity, fire res or chaos res', 'n', ['lastS'])   # m 'j': graph2recipe가 엑잘 자리(접미)를 이 줄에서 읽음

g = {
 'id': 'diztoh-crit-helmet-v2', 'recipe': 'diztoh-crit-helmet-v2', 'cls': 'Helmets_dex_int', 'base': 'Grinning Mask', 'ilvl': 82,
 'basePrice': {'Chaos_Orb': 8},
 'note': ('2026-11-12 W6 영상 전체 재대조(0:00~22:39, 근거 scratchpad review/W6-crit-helmet/timeline.md). 성공 회차 한 줄: '
          '매직 최대치 1티어(1:29) + 희귀도 1티어(1:41) → 완벽한 제왕(1:47) → 보존된 갈비뼈 + 우측 강령술(2:07) → 분열 = 최대치(2:59) → 소멸 2번(3:01~3:08) → '
          '카오스로 치명타 확률 1티어(7:23) → 완벽한 엑잘 + 좌측 찬미: 정확도(잡옵, 7:29)·% 증가 94%(7:32) → 좌측 말소 + 상위 카오스(9:09, % 증가가 지워지고 냉기 저항이 접미로) → 소멸 2번(9:17~9:26) → '
          '완벽한 엑잘 % 증가 80%(2티어, 9:32)·% + 마나 1티어(9:41) → 고대 갈비뼈(10:03) + 심연의 메아리 공개, 빛의 징조 + 소멸 2번 → 치명타 피해 보너스(11:25) → 완벽한 엑잘 화염 저항(12:03). 사용자 결정 2026-11-13: 8번 좌측 말소 + 상위 카오스의 새 옵션이 접미의 화염·냉기·번개 저항 3티어 이상이면 공허 유동체로 카오스 저항(1~2티어)으로 바꿔 마지막 접미로 남기고 11번을 건너뜀, 카오스 저항 3티어 이상·아이템 희귀도도 그대로 남김(영상 9:11 냉기 저항 40%는 영상에서는 지움). 사용자 결정 2026-11-13 00:05: 마지막 접미는 배포판처럼 하이엔드 희귀도·화염·카오스 저항 1티어, 빗나가면 가장 낮은 레벨일 때만 절사(+우측 말소) + 상위 카오스로 다시.'),
 'params': {
   'bT': {'kr': '회피·에너지 보호막 % 증가', 'en': '% evasion and ES', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'hT': {'kr': '회피·에너지 보호막 % + 마나', 'en': '% evasion and ES + mana', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
   'g': {'kr': '마지막 접미', 'en': 'Last suffix', 'values': {'1': K('희귀도·화염·카오스 저항 1티어까지 다시', 'Reroll for T1 rarity, fire or chaos res'), '0': K('랜덤 옵션', 'Random option')}}},
 'strategies': [{'id': 'high', 'params': {'bT': 1, 'hT': 1, 'g': 1}}, {'id': 'bal', 'params': {'bT': 2, 'hT': 2, 'g': 0}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'bT': 2, 'hT': 2, 'g': 0}, 'tier': 'bal',
    'desc': K('접두 % 증가·% + 마나 1~2티어(영상 완성품: % 증가 2티어)', 'Prefix % and %+mana at T1–2 (the video item: % at T2)')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'bT': 1, 'hT': 1, 'g': 1}, 'tier': 'high',
    'desc': K('접두 % 증가·% + 마나 1티어, 마지막 접미 희귀도·화염·카오스 저항 1티어까지', 'Prefix % and %+mana T1, last suffix T1 rarity, fire or chaos res')}],
 'tags': {
   'flatT1': {'gi': 8, 'tmax': 1}, 'rarS1': {'gi': 17, 'tmax': 1},
   'magicGood': {'anyOf': ['flatT1', 'rarS1'], 'label': K('회피·에너지 보호막 최대치 1티어·아이템 희귀도 1티어', 'T1 flat evasion/ES or T1 rarity')},
   'critT1': {'gi': 16, 'tmax': 1},
   'pct': {'gi': 9, 'tmax': '$bT'}, 'pct1': {'gi': 9, 'tmax': 1}, 'pct2': {'gi': 9, 'tmax': 2},
   'hybM': {'gi': 11, 'tmax': '$hT'}, 'hybM1': {'gi': 11, 'tmax': 1}, 'hybM2': {'gi': 11, 'tmax': 2},
   'cdmg': {'gi': 33, 'tmax': 1},
   'fire3': {'gi': 2, 'tmax': 3}, 'cold3': {'gi': 3, 'tmax': 3}, 'light3': {'gi': 4, 'tmax': 3},
   'eleR3': {'anyOf': ['fire3', 'cold3', 'light3'], 'label': K('화염·냉기·번개 저항 1~3티어', 'T1–3 fire, cold or lightning resistance')},
   'chaos2': {'gi': 5, 'tmax': 2}, 'chaos3': {'gi': 5, 'tmax': 3}, 'rarK': {'gi': 17, 'tmax': 3},
   'lastKeep': {'anyOf': ['rarK', 'chaos3'], 'label': K('아이템 희귀도·카오스 저항 1~3티어', 'Item rarity or T1–3 chaos res')},
   'fire1': {'gi': 2, 'tmax': 1}, 'chaos1': {'gi': 5, 'tmax': 1},
   'lastS': {'anyOf': ['rarS1', 'fire1', 'chaos1'], 'label': K('희귀도·화염 저항·카오스 저항 1티어', 'T1 rarity, fire res or chaos res')},
   'lastAny': {'anyOf': ['rarK', 'fire1', 'chaos3'], 'label': K('희귀도·화염 저항·카오스 저항', 'Rarity, fire res or chaos res')},
   'keepS3': {'anyOf': ['critT1', 'cdmg', 'lastS']}},
 'conds': {'magicDone': {'all': [{'has': 'flatT1'}, {'has': 'rarS1'}]},
           'pDone': {'all': [{'has': 'pct'}, {'has': 'hybM'}]}},
 'require': {'all': [{'has': 'flatT1'}, {'has': 'critT1'}, {'has': 'pct'}, {'has': 'hybM'}, {'has': 'cdmg'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 2]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h1',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
# ---------------- 준비 구역 ----------------
N.append({'id': 'h1', 'kind': 'base', 'group': 'prep', 'pos': [0, 0], 'next': 'h2', 'start': {'rar': 'normal', 'mods': [], 'quality': 20},
          'label': K('특출난 웃는 가면 구입, 퀄리티 20%', 'Buy an exceptional Grinning Mask, quality 20%'), 'item': []})
N.append({'id': 'h2', 'kind': 'act', 'group': 'prep', 'pos': [0, 1], 'act': 'transmute', 'cur': 'Perfect_Orb_of_Transmutation',
          'label': K('매직 첫 번째 옵션', 'First magic option'), 'goal': K('접두 회피·에너지 보호막 최대치 1티어', 'T1 flat evasion/ES prefix'),
          'show': ['flatT1'],
          'edges': [{'if': {'added': 'magicGood'}, 'to': 'h3', 'res': 'ok', 'label': K('성공', 'hit')},
                    {'to': 'h2x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
          'ask': K('원하는 옵션?', 'Wanted option?'), 'item': [FLATn]})
N.append({'id': 'h2x', 'kind': 'cleanup', 'group': 'prep', 'pos': [1, 1], 'keep': [], 'maxJunk': 0,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('빗나간 옵션 지우기', 'Remove the missed option'),
          'note': K('옵션이 없는 매직 아이템이 되어 다음은 확장의 오브', 'The item stays magic with no options, so augment next'),
          'edges': [{'to': 'h3'}]})
N.append({'id': 'h3', 'kind': 'act', 'group': 'prep', 'pos': [0, 2], 'act': 'augment', 'cur': 'Perfect_Orb_of_Augmentation',
          'label': K('매직 두 번째 옵션', 'Second magic option'), 'goal': K('접미 아이템 희귀도 1티어', 'T1 item rarity suffix'),
          'show': ['rarS1'],
          'edges': [{'if': {'ref': 'magicDone'}, 'to': 'h4', 'res': 'ok', 'label': K('성공', 'hit')},
                    {'to': 'h3x', 'res': 'fail', 'label': K('빗나감', 'miss')}],
          'ask': K('둘 다 맞음?', 'Both options?'), 'item': [FLATn, RAR]})
N.append({'id': 'h3x', 'kind': 'cleanup', 'group': 'prep', 'pos': [1, 2], 'keep': ['magicGood'], 'maxJunk': 0,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('빗나간 옵션 지우기', 'Remove the missed option'), 'ask': K('뭐가 지워짐?', 'What was removed?'),
          'edges': [{'lost': 'magicGood', 'to': 'h3y', 'res': 'fail', 'label': K('원하는 옵션 지워짐', 'wanted option gone')},
                    {'to': 'h3', 'res': 'ok', 'label': K('잡옵 지워짐', 'junk gone')}]})
N.append({'id': 'h3y', 'kind': 'cleanup', 'group': 'prep', 'pos': [2, 2], 'keep': [], 'maxJunk': 0,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('남은 옵션 지우기', 'Remove the remaining option'), 'edges': [{'to': 'h3'}]})
N.append({'id': 'h4', 'kind': 'act', 'group': 'prep', 'pos': [0, 3], 'act': 'regal', 'cur': 'Perfect_Regal_Orb',
          'label': K('레어', 'Rare'), 'goal': K('분열하기 위해 레어로', 'Make it rare for the fracture'),
          'showText': [K('랜덤 옵션 1개', 'One random option')], 'edges': [{'to': 'h5'}], 'item': [FLATn, JUNK('p'), RAR]})
N.append({'id': 'h5', 'kind': 'act', 'group': 'prep', 'pos': [0, 4], 'act': 'desecrate', 'cur': 'Preserved_Rib', 'omens': ['Omen_of_Dextral_Necromancy'],
          'label': K('훼손', 'Desecrate'), 'goal': K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
          'showText': [K('접미 훼손 옵션 (미공개, 분열되지 않음)', 'Suffix desecration (unrevealed, cannot fracture)')], 'edges': [{'to': 'h7'}],
          'item': [FLATn, JUNK('p'), RAR, UNREV]})
N.append({'id': 'h6', 'kind': 'side', 'group': 'prep', 'pos': [1, 5], 'act': 'divine', 'cur': 'Divine_Orb', 'attach': ['h5', 'h7'],
          'label': K('수치 올리기', 'Divine the values'), 'goal': K('옵션 수치 다시 굴리기 (선택)', 'Reroll option values (optional)'),
          'showText': [K('모든 옵션 수치 다시 굴림', 'Rerolls every value')]})
N.append({'id': 'h7', 'kind': 'act', 'group': 'prep', 'pos': [0, 6], 'act': 'fracture', 'cur': 'Fracturing_Orb',
          'label': K('분열', 'Fracture'), 'goal': K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
          'showText': [K('회피·에너지 보호막 최대치가 분열되면 성공', 'Success when the flat evasion/ES fractures')],
          'ask': K('어느 옵션이 분열?', 'Which option fractured?'),
          'edges': [{'if': {'fractured': 'flatT1'}, 'to': 'h8', 'res': 'ok', 'label': K('최대치 분열', 'flat fractured')},
                    {'if': {'fractured': 'rarS1'}, 'to': 'xs', 'res': 'ok', 'dash': True, 'label': K('희귀도 분열', 'rarity fractured')},
                    {'to': 'xj', 'res': 'fail', 'label': K('잡옵 분열', 'junk fractured')}],
          'item': [FLAT, JUNK('p'), RAR, UNREV]})
N.append({'id': 'xs', 'kind': 'exit', 'group': 'prep', 'pos': [1, 6], 'simTo': 'h1', 'variant': 'ok', 'label': K('희귀도 분열', 'Rarity fractured'),
          'note': K('다른 제작에 쓰거나 판매, 새 베이스로 처음부터', 'Use it for another craft or sell it; start over on a new base')})
N.append({'id': 'xj', 'kind': 'exit', 'group': 'prep', 'pos': [1, 7], 'simTo': 'h1', 'variant': 'fail', 'label': K('잡옵 분열', 'Junk fractured'),
          'note': K('새 베이스로 처음부터', 'Start over on a new base')})
N.append({'id': 'h8', 'kind': 'cleanup', 'group': 'prep', 'pos': [0, 8], 'keep': [], 'maxJunk': 1,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), 'edges': [{'to': 'ms'}], 'item': [FLAT, JUNK('x')]})
# ---------------- 옵션 추가 작업 ----------------
N.append({'id': 'ms', 'kind': 'mark', 'group': 'main', 'pos': [0, 9], 'next': 'c1', 'label': K('아이템 제작 시작', 'Item crafting starts'), 'item': [FLAT, JUNK('x')]})
N.append({'id': 'c1', 'kind': 'act', 'group': 'main', 'pos': [0, 10.4], 'act': 'chaos', 'cur': 'Chaos_Orb',
          'label': K('카오스', 'Chaos'), 'goal': K('접미 치명타 확률 1티어', 'T1 crit chance suffix'), 'show': ['critT1'],
          'edges': [{'if': {'has': 'critT1'}, 'to': 'p1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}],
          'item': [FLAT, CRIT]})
N.append({'id': 'cz', 'kind': 'cleanup', 'group': 'main', 'pos': [1, 9.9], 'keep': [], 'maxJunk': 1,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('분열 + 옵션 1개만 남기기', 'Keep the fracture + one option'), 'edges': [{'to': 'c1'}]})
PDONE = {'ref': 'pDone'}
N.append({'id': 'p1', 'kind': 'act', 'group': 'main', 'pos': [0, 11.4], 'act': 'exalt', 'cur': 'Perfect_Exalted_Orb', 'omens': ['Omen_of_Sinistral_Exaltation'],
          'label': K('엑잘', 'Exalt'), 'goal': K('접두 회피·에너지 보호막 % 증가', '% evasion and ES prefix'), 'show': ['pct'],
          'skipIf': {'has': 'pct'}, 'skipTo': 'p2', 'skipHide': True,
          'edges': [{'if': {'all': [{'added': 'pct'}, {'not': {'full': 'p'}}]}, 'to': 'p2', 'res': 'ok', 'label': K('% 증가 성공', '% hit')},
                    {'if': PDONE, 'to': 'd1', 'res': 'ok', 'hide': True},
                    {'if': {'full': 'p'}, 'to': 'p3', 'res': 'fail', 'label': K('잡옵으로 접두가 꽉 참 — 좌측 말소', 'Prefixes full with junk: Sinistral Erasure')},
                    {'to': 'p1', 'res': 'fail', 'hide': True}]})
N.append({'id': 'p2', 'kind': 'act', 'group': 'main', 'pos': [0, 12.4], 'act': 'exalt', 'cur': 'Perfect_Exalted_Orb', 'omens': ['Omen_of_Sinistral_Exaltation'],
          'label': K('엑잘', 'Exalt'), 'goal': K('접두 회피·에너지 보호막 % + 마나', '% evasion and ES + mana prefix'), 'show': ['hybM'],
          'skipIf': PDONE, 'skipTo': 'd1', 'skipHide': True,
          'edges': [{'if': {'all': [{'has': 'pct'}, {'has': 'hybM'}]}, 'to': 'd1', 'res': 'ok', 'label': K('접두 완성', 'prefixes done')},
                    {'to': 'p3', 'res': 'fail', 'label': K('빗나감 — 좌측 말소', 'miss: Sinistral Erasure')}]})
N.append({'id': 'p3', 'kind': 'act', 'group': 'main', 'pos': [1, 11.9], 'act': 'chaos', 'cur': 'Greater_Chaos_Orb', 'omens': ['Omen_of_Sinistral_Erasure'],
          'label': K('좌측 말소 + 카오스', 'Sinistral Erasure + Chaos'), 'goal': K('접두 잡옵 바꾸기 (1/2)', 'Reroll the junk prefix (1 in 2)'),
          'show': ['pct', 'hybM'],
          'edges': [{'if': PDONE, 'to': 'd1', 'res': 'ok', 'label': K('접두 완성', 'prefixes done')},
                    {'if': {'all': [{'not': {'full': 'p'}}, {'count': {'tag': 'lastKeep', 'min': 2}}]}, 'to': 'p3z', 'res': 'fail', 'label': K('남길 접미가 둘 — 하나만', 'Two kept suffixes: keep one')},
                    {'if': {'all': [{'added': 'eleR3'}, {'not': {'full': 'p'}}, {'not': {'has': 'lastKeep'}}]}, 'to': 'fx', 'res': 'fail',
                     'label': K('접미에 원소 저항 3티어 이상 — 공허 유동체', 'T1–3 elemental res on the suffix: Void Flux')},
                    {'if': {'any': [{'removed': 'pct'}, {'removed': 'hybM'}, {'not': {'full': 'p'}}]}, 'to': 'p3x', 'res': 'fail',
                     'label': K('원하는 접두가 지워지거나 새 옵션이 접미로', 'A wanted prefix went, or the new option went to the suffix')},
                    {'to': 'p3', 'res': 'fail', 'hide': True}]})
N.append({'id': 'fx', 'kind': 'act', 'group': 'main', 'pos': [2, 11.9], 'act': 'flux', 'cur': 'Void_Flux',
          'label': K('유동체', 'Flux'), 'goal': K('접미 원소 저항 → 카오스 저항', 'Suffix elemental res → chaos res'), 'show': ['chaos2'],
          'edges': [{'to': 'p3x', 'label': K('카오스 저항은 두고 잡옵 정리', 'Keep the chaos res, clear the junk')}]})
N.append({'id': 'p3z', 'kind': 'cleanup', 'group': 'main', 'pos': [2, 12.9], 'keep': ['critT1', 'pct', 'hybM'], 'maxJunk': 1,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('남길 접미가 둘이면 하나만 남기기', 'Two kept suffixes: keep one'),
          'edges': [{'lost': 'critT1', 'to': 'cz', 'res': 'fail', 'hide': True}, {'lost': 'pct', 'to': 'p3z', 'res': 'fail', 'hide': True},
                    {'lost': 'hybM', 'to': 'p3z', 'res': 'fail', 'hide': True}, {'to': 'p3x', 'res': 'ok', 'hide': True}]})
N.append({'id': 'p3x', 'kind': 'cleanup', 'group': 'main', 'pos': [1, 12.9], 'keep': ['critT1', 'pct', 'hybM', 'lastKeep'], 'maxJunk': 0,
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('잡옵 지우기 (치명타 확률·% 증가·% + 마나·희귀도·카오스 저항은 유지)', 'Remove the junk (keep crit chance, %, %+mana, rarity and chaos res)'),
          'ask': K('뭐가 지워짐?', 'What was removed?'),
          'edges': [{'lost': 'critT1', 'to': 'cz', 'res': 'fail', 'label': K('치명타 확률 지워짐 — 카오스부터', 'Crit chance gone: back to Chaos')},
                    {'lost': 'pct', 'to': 'p3x', 'res': 'fail', 'hide': True}, {'lost': 'hybM', 'to': 'p3x', 'res': 'fail', 'hide': True}, {'lost': 'lastKeep', 'to': 'p3x', 'res': 'fail', 'hide': True},
                    {'to': 'p1', 'res': 'ok', 'label': K('잡옵 지워짐 — 다시 엑잘', 'Junk gone: exalt again')}]})
N.append({'id': 'd1', 'kind': 'act', 'group': 'main', 'pos': [0, 13.6], 'act': 'desecrate', 'cur': 'Ancient_Rib',
          'label': K('훼손', 'Desecrate'), 'goal': K('접미 두 번째 옵션(훼손)', 'Second suffix option (desecrated)'),
          'showText': [K('접미 훼손 옵션 (미공개)', 'Suffix desecration (unrevealed)')], 'edges': [{'to': 'd2'}],
          'item': [UNREV, FLAT, PCT, HYB, CRIT]})   # 미공개 줄을 앞에: graph2recipe가 첫 새 줄로 훼손 자리(접미)를 읽음, 화면은 접두·접미 순으로 정렬
N.append({'id': 'd2', 'kind': 'act', 'group': 'main', 'pos': [0, 14.6], 'act': 'reveal', 'omens': ['Omen_of_Abyssal_Echoes'], 'want': 'cdmg',
          'label': K('공개', 'Reveal'), 'goal': K('접미 치명타 피해 보너스', 'Crit damage bonus suffix'), 'show': ['cdmg'],
          'edges': [{'if': {'added': 'cdmg'}, 'to': 'f1', 'res': 'ok'}, {'to': 'dx', 'res': 'fail'}],
          'item': [FLAT, PCT, HYB, CRIT, CDMG]})
N.append({'id': 'dx', 'kind': 'act', 'group': 'main', 'pos': [1, 14.6], 'act': 'annul', 'cur': 'Orb_of_Annulment', 'omens': ['Omen_of_Light'],
          'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
          'target': K('훼손 옵션 제거', 'Remove the desecrated option'), 'edges': [{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}]})
N.append({'id': 'f1', 'kind': 'act', 'group': 'main', 'pos': [0, 15.6], 'act': 'exalt', 'cur': 'Perfect_Exalted_Orb',
          'label': K('엑잘', 'Exalt'), 'goal': K('접미 세 번째 옵션', 'Third suffix option'), 'show': ['rarS1', 'fire1', 'chaos1'],
          'skipIf': {'full': 's'}, 'skipTo': 'ok',
          'skipNote': K('8번에서 남긴 접미가 있으면(접미가 꽉 차면) 건너뜀', 'Skipped if a suffix was kept at step 8 (suffixes full)'),
          'edges': [{'if': {'all': [{'param': {'g': 1}}, {'not': {'has': 'lastS'}}, {'whittleSafe': {'tag': 'keepS3', 'side': 's'}}]}, 'to': 'f2', 'res': 'fail',
                     'label': K('빗나감 — 가장 낮은 레벨이면 다시', 'Miss: reroll while it is the lowest level')},
                    {'to': 'ok', 'res': 'ok'}],
          'item': [FLAT, PCT, HYB, CRIT, CDMG, LASTH],
          'over': [{'param': {'g': 0}, 'set': {'item': [FLAT, PCT, HYB, CRIT, CDMG, RND], 'show': [], 'showText': [{'s': 's', 'kr': '랜덤 옵션', 'en': 'Random option'}]}}]})
N.append({'id': 'f2', 'kind': 'act', 'group': 'main', 'pos': [1, 15.6], 'act': 'chaos', 'cur': 'Greater_Chaos_Orb', 'trim': {'side': 's', 'keep': 'keepS3'},
          'label': K('절사/우측 말소 + 카오스', 'Whittling / Dextral Erasure + Chaos'), 'goal': K('마지막 접미 다시 (가장 낮은 레벨일 때)', 'Reroll the last suffix (while it is the lowest level)'),
          'show': ['rarS1', 'fire1', 'chaos1'],
          'edges': [{'if': {'has': 'lastS'}, 'to': 'ok', 'res': 'ok'},
                    {'if': {'whittleSafe': {'tag': 'keepS3', 'side': 's'}}, 'to': 'f2', 'res': 'fail', 'hide': True},
                    {'to': 'ok', 'res': 'ok', 'hide': True}]})
N.append({'id': 'ok', 'kind': 'done', 'group': 'main', 'pos': [0, 16.6], 'label': K('완성', 'Finished')})
g['nodes'] = N

g['loops'] = [
  {'id': 'L1', 'nodes': ['h2', 'h2x', 'h3', 'h3x', 'h3y'], 'kr': '매직 옵션 맞추기', 'en': 'Magic options'},
  {'id': 'L2', 'nodes': ['p1', 'p2', 'p3', 'fx', 'p3z', 'p3x'], 'kr': '접두 두 번째·세 번째 옵션', 'en': 'Second and third prefixes', 'fold': True,
   'goal': K('접두 회피·에너지 보호막 % 증가 + % + 마나', '% evasion/ES and %+mana prefixes'),
   'goalBy': {'high': K('접두 회피·에너지 보호막 % 증가 1티어 + % + 마나 1티어', 'T1 % evasion/ES and T1 %+mana prefixes'),
              'bal': K('접두 회피·에너지 보호막 % 증가 1~2티어 + % + 마나 1~2티어', 'T1–2 % evasion/ES and T1–2 %+mana prefixes')},
   'steps': [
     {'kr': '완벽한 엑잘티드 오브 + 좌측 찬미의 징조로 접두 회피·에너지 보호막 % 증가', 'en': 'Perfect Exalt + Sinistral Exaltation for the % evasion/ES prefix', 'node': 'p1'},
     {'kr': '완벽한 엑잘티드 오브 + 좌측 찬미의 징조로 접두 회피·에너지 보호막 % + 마나', 'en': 'Perfect Exalt + Sinistral Exaltation for the %+mana prefix', 'node': 'p2'},
     {'kr': '잡옵으로 접두가 꽉 차면 좌측 말소의 징조 + 상위 카오스 오브(1/2)', 'en': 'Prefixes full with junk: Sinistral Erasure + Greater Chaos (1 in 2)', 'node': 'p3'},
     {'kr': '새 옵션이 접미로 가면 아이템 희귀도·카오스 저항 3티어 이상은 남기고, 화염·냉기·번개 저항 3티어 이상은 공허 유동체로 카오스 저항(마지막 접미)', 'en': 'New option on the suffix: keep item rarity or a T1–3 chaos res; Void Flux turns a T1–3 fire/cold/lightning res into chaos res (last suffix)', 'node': 'fx'},
     {'kr': '원하는 접두가 지워지거나 새 옵션이 접미로 가면 소멸의 오브로 잡옵을 지우고 1번부터(남긴 접미는 그대로)', 'en': 'A wanted prefix went, or the new option went to the suffix: annul the junk (the kept suffix stays) and go back to 1', 'node': 'p3x'}],
   'worst': {'kr': '치명타 확률이 지워지면 카오스 단계부터', 'en': 'Crit chance gone: back to the Chaos step', 'to': 'cz'},
   'item': [FLAT, PCT, HYB, CRIT]},
  {'id': 'L5', 'nodes': ['d1', 'd2', 'dx'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal'},
]
g['finals'] = [
  {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
   'lines': [{'tag': 'flatT1', 'fr': True}, {'tag': 'pct1'}, {'tag': 'hybM1'}, {'tag': 'critT1'}, {'tag': 'cdmg', 'des': True}, {'side': 's', 'random': True}]},
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'flatT1', 'fr': True}, {'tag': 'pct2'}, {'tag': 'hybM2'}, {'tag': 'critT1'}, {'tag': 'cdmg', 'des': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
