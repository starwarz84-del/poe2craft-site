# RING 2026-11-14: 사용자(Atom1q84) 직접 제작 순서 — 마나·희귀도·시전 속도 황금 반지(영상 없음, 운영자 레시피)
# 근거: 사용자 붙여 넣은 아이템(11-14 14:36) + 사용자 정정 순서(11-14 15:37, scratchpad review/RING_BRIEF.md '사용자 정정')
# 실행: cd scripts/graphs && python3 gen_atom_mana_rarity_ring.py  → atom-mana-rarity-ring-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/atom-mana-rarity-ring-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 사용자 아이템에 있는 옵션(퀄리티 반영 전 원래 수치)
MA = L('p', '마나 최대치 +(165—179)', '+(165—179) to maximum Mana', 'n', ['mana'])
JK = L('p', '잡옵', 'Junk', 'j')
PM = L('p', '최대 마나 (4—6)% 증가 (완벽한 정신의 에센스)', '(4—6)% increased maximum Mana (Perfect Essence of the Mind)', 'c', ['pmana'])
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
RD = L('p', '발견하는 아이템 희귀도 (16—19)% 증가', '(16—19)% increased Rarity of Items found', 'd', ['rarD'])
RS = L('s', '발견하는 아이템 희귀도 (15—18)% 증가', '(15—18)% increased Rarity of Items found', 'n', ['rarS'])
CS = L('s', '시전 속도 (19—21)% 증가', '(19—21)% increased Cast Speed', 'n', ['cast'])
LR = L('s', '번개 저항 +(36—40)%', '+(36—40)% to Lightning Resistance', 'n')

g = {
 'id': 'atom-mana-rarity-ring-v2', 'recipe': 'atom-mana-rarity-ring-v2', 'cls': 'Rings', 'base': 'Gold Ring', 'ilvl': 82,
 'note': ('2026-11-14 RING: 사용자 Atom1q84가 직접 만든 순서(영상 없음, 15:37 정정). 매직 황금 반지(접두 마나 최대치 + 접미 아이템 희귀도) 구입 → 제왕의 오브 → '
          '달리는 기폭제 퀄리티 20% + 촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 시전 속도 → 접두 잡옵이 있으면 좌측 결정화의 징조 + 완벽한 정신의 에센스(접두 2개 중 하나가 지워짐, 마나 최대치면 새 베이스) → '
          '접두 훼손 + 심연의 메아리 공개(빗나가면 소멸의 오브 + 빛의 징조) → 접미 셋째(툴의 기폭제 + 촉진하는 찬미의 징조로 저항 노림, 랜덤 옵션) → 신경 기폭제 퀄리티 20%. '
          '상위 풍요의 에센스는 완벽한 정신의 에센스와 제작 옵션 한도(C1)가 겹쳐 뺌(사용자 정정). '
          '내부 결정(빈칸, 시뮬): 시전 속도 엑잘이 빗나가면 접미에 빈자리가 있으면 다시 엑잘, 꽉 차면 소멸의 오브(우측 소멸의 징조는 3,708 ex라 뺌) / 제왕의 오브가 접두를 안 붙였으면 좌측 찬미의 징조 + 엑잘티드 오브로 접두 잡옵 / '
          '접미 셋째는 훼손 뒤(사용자 순서, 접두가 꽉 차서 우측 찬미의 징조 필요 없음) / 정신의 에센스에 좌측 결정화의 징조(16:41 정정: 접두에 빈자리가 있으면 아무 옵션이나 지워짐 — 징조 없이는 접미 시전 속도·희귀도도 지워져 끝나지 않음, 접두를 3개로 채우는 길은 밸런스 83.3 div vs 징조 62.6 div) / 기폭제는 데이터 태그 중 가장 싼 것(시전 속도 = 달리는, 저항 = 툴의).'),
 'params': {
  'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('빛의 징조로 다시', 'Retry with Light'), '2': K('결과 그대로', 'As it comes')}},
  'rT': {'kr': '공개 희귀도', 'en': 'Revealed rarity', 'values': {'2': K('1~2티어', 'T1–2'), '3': K('아무 티어', 'Any tier')}},
 },
 'strategies': [{'id': 'bal', 'params': {'v': 1, 'rT': 2}},
                {'id': 'ess', 'params': {'v': 2, 'rT': 3}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1, 'rT': 2}, 'tier': 'bal',
   'desc': K('공개 희귀도 1~2티어까지 빛의 징조로 다시', 'Reveal retried with Light until T1–2 rarity')},
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2, 'rT': 3}, 'tier': 'ess',
   'desc': K('공개 한 번, 결과 그대로', 'One reveal, kept as it comes')}],
 'tags': {
  'mana': {'gi': 10, 'tmax': 1}, 'rarS': {'gi': 27, 'tmax': 1}, 'cast': {'gi': 34, 'tmax': 2}, 'pmana': {'gi': 67},
  'rarD': {'gi': 28, 'tmax': '$rT'}, 'cres': {'gi': 5},
 },
 'require': {'all': [{'has': 'mana'}, {'has': 'pmana'}, {'has': 'cast'}, {'has': 'rarS'}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (사용자 0~1) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='b1', start={'rar': 'magic', 'mods': ['mana', 'rarS']},
  label=K('접두 마나 최대치 + 접미 아이템 희귀도 매직 황금 반지 구입 (아이템 레벨 82)', 'Buy a magic Gold Ring with prefix maximum mana + suffix item rarity (item level 82)'),
  item=[MA, RS])
A(id='b1', kind='act', group='prep', pos=[0, 1], act='regal', cur='Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 + 옵션 1개 — 나오는 대로 (사용자: 접두 잡옵)', 'Rare + one option: keep what comes (user: a junk prefix)'),
  showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'if': {'famBlock': 'cast'}, 'to': 'xb', 'res': 'fail', 'hide': True}, {'to': 'ms'}], item=[MA, JK, RS])
# ---------------- 옵션 추가 작업 (사용자 2~5) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MA, JK, RS])
A(id='c1', kind='act', group='main', pos=[0, 3.4], act='quality', cur='Skittering_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('속도 퀄리티 20%', '20% speed quality'), skipIf={'has': 'cast'}, skipTo='e1', edges=[{'to': 'c2'}])
A(id='c2', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation', 'Omen_of_Dextral_Exaltation'], cat='cast',
  label=K('엑잘', 'Exalt'), goal=K('접미 두 번째 옵션 — 시전 속도 1~2티어', 'Second suffix: T1–2 cast speed'), show=['cast'],
  edges=[{'if': {'added': 'cast'}, 'to': 'e1', 'res': 'ok'},
         {'if': {'not': {'full': 's'}}, 'to': 'c1', 'res': 'fail', 'label': K('빗나감 — 접미 빈자리 남음', 'Miss: a suffix slot left')},
         {'to': 'c2x', 'res': 'fail', 'label': K('빗나감 — 접미 꽉 참', 'Miss: suffixes full')}])
A(id='c2x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', label=K('소멸의 오브', 'Orb of Annulment'),
  goal=K('소멸의 오브', 'Orb of Annulment'), target=K('옵션 1개 제거 — 잡옵이면 다시 엑잘', 'Remove one option: junk gone, exalt again'),
  edges=[{'if': {'any': [{'not': {'has': 'mana'}}, {'not': {'has': 'rarS'}}]}, 'to': 'xb', 'res': 'fail', 'label': K('마나 최대치·희귀도가 지워짐', 'Maximum mana or rarity gone')},
         {'if': {'full': 's'}, 'to': 'c2x', 'res': 'fail'},
         {'to': 'c1', 'res': 'ok'}])
A(id='e1', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('에센스가 지울 접두 잡옵', 'A junk prefix for the essence to remove'), showText=[K('잡옵 1개', 'One junk option')],
  skipIf={'not': {'sideLt': {'side': 'p', 'n': 2}}}, skipTo='e2', skipNote=K('접두 잡옵이 이미 있으면 건너뜀', 'Skipped when a junk prefix is already there'),
  edges=[{'to': 'e2'}], item=[MA, JK, RS, CS])
A(id='e2', kind='act', group='main', pos=[0, 6.4], act='essence', cur='Perfect_Essence_of_the_Mind', ess='pmana', omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접두 최대 마나 % — 접두 2개 중 하나가 지워짐', 'Prefix % maximum mana: one of the two prefixes goes'),
  showText=[{'s': 'p', 'kr': '최대 마나 (4—6)% 증가 (제작 옵션)', 'en': '(4—6)% increased maximum Mana (crafted)'}],
  edges=[{'if': {'not': {'has': 'mana'}}, 'to': 'xb', 'res': 'fail', 'label': K('마나 최대치가 지워짐', 'Maximum mana gone')},
         {'to': 'd1', 'res': 'ok', 'label': K('잡옵이 지워짐', 'Junk gone')}],
  item=[MA, PM, RS, CS])
A(id='xb', kind='exit', group='main', pos=[1, 6.4], simTo='b0', variant='fail', label=K('새 베이스', 'New base'),
  note=K('마나 최대치나 접미 희귀도가 지워지면 새 매직 베이스 구입부터', 'Maximum mana or the rarity suffix gone: a new magic base'))
A(id='d1', kind='act', group='main', pos=[0, 7.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'd2'}], item=[MA, PM, UN, RS, CS])
A(id='d2', kind='act', group='main', pos=[0, 8.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rarD', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 아이템 희귀도', 'Third prefix (desecrated): item rarity'),
  goalBy={'bal': K('접두 세 번째 옵션(훼손) — 아이템 희귀도 1~2티어', 'Third prefix (desecrated): T1–2 item rarity'),
          'ess': K('접두 세 번째 옵션(훼손) — 나오는 대로 (사용자: 아이템 희귀도)', 'Third prefix (desecrated): keep what comes (user: item rarity)')},
  show=['rarD'],
  edges=[{'if': {'added': 'rarD'}, 'to': 's0', 'res': 'ok'},
         {'if': {'param': {'v': 1}}, 'to': 'd2x', 'res': 'fail'},
         {'to': 's0', 'res': 'fail', 'hide': True}],
  item=[MA, PM, RD, RS, CS])
A(id='d2x', kind='act', group='main', pos=[1, 8.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='s0', kind='act', group='main', pos=[0, 9.4], act='quality', cur='Tuls_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('냉기 퀄리티 20% — 저항 노리기', '20% cold quality to aim at a resistance'), skipIf={'full': 's'}, skipTo='q5',
  skipNote=K('접미가 이미 꽉 찼으면 건너뜀', 'Skipped when the suffixes are already full'), edges=[{'to': 's1'}])
A(id='s1', kind='act', group='main', pos=[0, 10.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation'], cat='cres',
  label=K('엑잘', 'Exalt'), goal=K('접미 세 번째 옵션 — 나오는 대로 (사용자: 번개 저항)', 'Third suffix: keep what comes (user: lightning resistance)'),
  showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'q5'}], item=[MA, PM, RD, RS, CS, LR])
A(id='q5', kind='act', group='main', pos=[0, 11.4], act='quality', cur='Neural_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('마나 퀄리티 20%', '20% mana quality'), edges=[{'to': 'ok'}], item=[MA, PM, RD, RS, CS, LR])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['c1', 'c2', 'c2x'], 'kr': '시전 속도', 'en': 'Cast speed', 'fold': True,
  'goal': K('접미 시전 속도 1~2티어', 'Suffix: T1–2 cast speed'),
  'steps': [K('달리는 기폭제로 속도 퀄리티 20%', 'Skittering Catalyst for 20% speed quality') | {'node': 'c1'},
            K('촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 시전 속도', 'Omen of Catalysing Exaltation + Omen of Dextral Exaltation + Perfect Exalted Orb for cast speed') | {'node': 'c2'},
            K('빗나가고 접미가 꽉 차면 소멸의 오브로 옵션 1개 제거, 잡옵이 지워질 때까지', 'A miss that fills the suffixes: Orb of Annulment until a junk option goes') | {'node': 'c2x'}],
  'worst': {'kr': '마나 최대치나 접미 희귀도가 지워지면 새 매직 베이스부터', 'en': 'Maximum mana or the rarity suffix gone: a new magic base', 'to': 'xb'},
  'item': [MA, JK, RS, CS]},
 {'id': 'L2', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'mana'}, {'tag': 'pmana', 'ess': True}, {'tag': 'rarD', 'des': True},
            {'tag': 'cast'}, {'tag': 'rarS'}, {'side': 's', 'random': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'mana'}, {'tag': 'pmana', 'ess': True}, {'side': 'p', 'random': True, 'des': True},
            {'tag': 'cast'}, {'tag': 'rarS'}, {'side': 's', 'random': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
