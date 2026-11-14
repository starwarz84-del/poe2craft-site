# RING 2026-11-14: 사용자(Atom1q84) 직접 제작 순서 — 마나·희귀도·시전 속도 황금 반지(영상 없음, 운영자 레시피)
# 근거: 사용자 붙여 넣은 아이템(11-14 14:36) + 사용자 순서 1~7(scratchpad review/RING_BRIEF.md)
# 실행: cd scripts/graphs && python3 gen_atom_mana_rarity_ring.py  → atom-mana-rarity-ring-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/atom-mana-rarity-ring-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 사용자 아이템에 실제로 있는 옵션(퀄리티 반영 전 원래 수치)
MA = L('p', '마나 최대치 +(165—179)', '+(165—179) to maximum Mana', 'n', ['mana'])
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
JK = L('p', '잡옵', 'Junk', 'j')
PM = L('p', '최대 마나 (4—6)% 증가 (완벽한 정신의 에센스)', '(4—6)% increased maximum Mana (Perfect Essence of the Mind)', 'c', ['pmana'])
RD = L('p', '발견하는 아이템 희귀도 (16—19)% 증가', '(16—19)% increased Rarity of Items found', 'd', ['rarD'])
CS = L('s', '시전 속도 (19—21)% 증가', '(19—21)% increased Cast Speed', 'n', ['cast'])
RE = L('s', '발견하는 아이템 희귀도 (15—18)% 증가 (상위 풍요의 에센스)', '(15—18)% increased Rarity of Items found (Greater Essence of Opulence)', 'c', ['rarE'])
LR = L('s', '번개 저항 +(36—40)%', '+(36—40)% to Lightning Resistance', 'n')

g = {
 'id': 'atom-mana-rarity-ring-v2', 'recipe': 'atom-mana-rarity-ring-v2', 'cls': 'Rings', 'base': 'Gold Ring', 'ilvl': 82,
 'note': ('2026-11-14 RING: 사용자 Atom1q84가 직접 만든 순서(영상 없음). 매직 황금 반지(마나 최대치 + 시전 속도) 구입 → 상위 풍요의 에센스(레어 + 접미 희귀도) → '
          '좌측 강령술의 징조 + 보존된 빗장뼈(접두 미공개 훼손) → 완벽한 엑잘티드 오브 + 상위 찬미의 징조(접두 잡옵 1개 + 접미 랜덤 옵션 1개) → '
          '완벽한 정신의 에센스(접두가 꽉 차서 접두 3개 중 하나가 지워짐: 잡옵이면 그대로, 훼손 옵션이면 다시 훼손, 마나 최대치면 새 베이스) → '
          '심연의 메아리의 징조 + 공개(희귀도가 아니면 소멸의 오브 + 빛의 징조로 다시) → 신경 기폭제 퀄리티 20%. '
          '상위 풍요의 에센스 줄은 사용자 아이템에 완벽한 정신의 에센스 줄과 함께 있어 제작 옵션 한도(C1)에 세지 않음(notCrafted, 정책 5장과 충돌 — 보고). '
          '등급: 난이도 표 2(보통) → 밸런스·에센셜(C11). 하이엔드(공개 희귀도 1티어·시전 속도 1티어 베이스)는 시뮬 78.3 div로 만들어 봤지만 표에 없는 등급이라 뺌. '
          '사용자 꿀팁(퀄리티 + 촉진하는 찬미의 징조로 접미 저항)은 접미 셋째가 모든 등급 랜덤 옵션이라 시뮬 이득 없음 → 꿀팁 줄.'),
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
  'mana': {'gi': 10, 'tmax': 1}, 'cast': {'gi': 34, 'tmax': 2}, 'rarE': {'gi': 66}, 'pmana': {'gi': 67},
  'rarD': {'gi': 28, 'tmax': '$rT'},
 },
 'require': {'all': [{'has': 'mana'}, {'has': 'pmana'}, {'has': 'cast'}, {'has': 'rarE'}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'a0',
 'finalItem': {'quality': 20, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (사용자 순서 1~3: 확정 제작) ----------------
A(id='a0', kind='base', group='prep', pos=[0, 0], next='a1', start={'rar': 'magic', 'mods': ['mana', 'cast']},
  label=K('접두 마나 최대치 + 접미 시전 속도 매직 황금 반지 구입 (아이템 레벨 82)', 'Buy a magic Gold Ring with prefix maximum mana + suffix cast speed (item level 82)'),
  item=[MA, CS])
A(id='a1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Opulence', ess='rarE', notCrafted=True, label=K('에센스', 'Essence'),
  goal=K('레어 + 접미 희귀도', 'Rare + rarity suffix'),
  showText=[{'s': 's', 'kr': '발견하는 아이템 희귀도 (제작 옵션)', 'en': 'Item rarity (crafted)'}], edges=[{'to': 'a2'}], item=[MA, CS, RE])
A(id='a2', kind='act', group='prep', pos=[0, 2], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손)', 'Second prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'ms'}], item=[MA, UN, CS, RE])
# ---------------- 옵션 추가 작업 (사용자 순서 4~7) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='a3', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MA, UN, CS, RE])
A(id='a3', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째·접미 세 번째 옵션 — 나오는 대로 (사용자: 번개 저항)', 'Third prefix and third suffix: keep what comes (user: lightning resistance)'),
  showText=[K('잡옵 1개 + 랜덤 옵션 1개', 'One junk option + one random option')], edges=[{'to': 'a4'}], item=[MA, UN, JK, CS, RE, LR])
A(id='a4', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Perfect_Essence_of_the_Mind', ess='pmana', label=K('에센스', 'Essence'),
  goal=K('접두 최대 마나 % — 접두 3개 중 하나가 지워짐', 'Prefix % maximum mana: one of the three prefixes goes'),
  showText=[{'s': 'p', 'kr': '최대 마나 (4—6)% 증가 (제작 옵션)', 'en': '(4—6)% increased maximum Mana (crafted)'}],
  edges=[{'if': {'not': {'has': 'mana'}}, 'to': 'xb', 'res': 'fail', 'label': K('마나 최대치가 지워짐', 'Maximum mana gone')},
         {'if': {'unrev': False}, 'to': 'a5', 'res': 'fail', 'label': K('훼손 옵션이 지워짐', 'Desecrated option gone')},
         {'to': 'a6', 'res': 'ok', 'label': K('잡옵이 지워짐', 'Junk gone')}])
A(id='xb', kind='exit', group='main', pos=[1, 5.4], simTo='a0', variant='fail', label=K('마나 최대치가 지워짐 — 새 베이스', 'Maximum mana gone: new base'),
  note=K('마나 최대치가 지워지면 새 매직 베이스 구입부터', 'Maximum mana gone: buy a new magic base and start over'))
A(id='a5', kind='act', group='main', pos=[1, 6.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('다시 훼손 — 접두가 꽉 차 있으면 하나를 지우고 들어감', 'Desecrate again: a full prefix side gives up one option'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'if': {'not': {'has': 'mana'}}, 'to': 'xb', 'res': 'fail', 'label': K('마나 최대치가 지워짐', 'Maximum mana gone')},
         {'if': {'not': {'has': 'pmana'}}, 'to': 'a4', 'res': 'fail', 'label': K('최대 마나 %가 지워짐', '% maximum mana gone')},
         {'to': 'a6', 'res': 'ok'}])
A(id='a6', kind='act', group='main', pos=[0, 6.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rarD', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 아이템 희귀도', 'Third prefix (desecrated): item rarity'),
  goalBy={'bal': K('접두 세 번째 옵션(훼손) — 아이템 희귀도 1~2티어', 'Third prefix (desecrated): T1–2 item rarity'),
          'ess': K('접두 세 번째 옵션(훼손) — 나오는 대로 (사용자: 아이템 희귀도)', 'Third prefix (desecrated): keep what comes (user: item rarity)')},
  show=['rarD'],
  edges=[{'if': {'added': 'rarD'}, 'to': 'a7', 'res': 'ok'},
         {'if': {'param': {'v': 1}}, 'to': 'a6x', 'res': 'fail'},
         {'to': 'a7', 'res': 'fail', 'hide': True}])
A(id='a6x', kind='act', group='main', pos=[1, 7.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'a6d'}])
A(id='a6d', kind='act', group='main', pos=[1, 8.4], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('다시 훼손 — 접두 빈자리', 'Desecrate again: the open prefix'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'a6'}])
A(id='a7', kind='act', group='main', pos=[0, 7.4], act='quality', cur='Neural_Catalyst', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('마나 퀄리티 20%', '20% mana quality'), edges=[{'to': 'ok'}], item=[MA, PM, RD, CS, RE, LR])
A(id='ok', kind='done', group='main', pos=[0, 8.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [{'id': 'L1', 'nodes': ['a4', 'a5', 'a6', 'a6x', 'a6d'], 'kr': '최대 마나 % + 훼손 공개', 'en': '% maximum mana + reveal', 'fold': True,
  'goal': K('접두 최대 마나 % + 훼손 아이템 희귀도', 'Prefixes: % maximum mana + desecrated item rarity'),
  'goalBy': {'bal': K('접두 최대 마나 % + 훼손 아이템 희귀도 1~2티어', 'Prefixes: % maximum mana + T1–2 desecrated item rarity'),
             'ess': K('접두 최대 마나 % + 훼손 옵션 나오는 대로', 'Prefixes: % maximum mana + the desecrated option as it comes')},
  'steps': [K('완벽한 정신의 에센스로 최대 마나 % — 접두 3개 중 하나가 지워짐', 'Perfect Essence of the Mind for % maximum mana: one of the three prefixes goes') | {'node': 'a4'},
            K('훼손 옵션이 지워지면 좌측 강령술의 징조 + 보존된 빗장뼈로 다시 훼손, 최대 마나 %가 지워지면 에센스부터', 'Desecrated option gone: Omen of Sinistral Necromancy + Preserved Collarbone again; % maximum mana gone: essence again') | {'node': 'a5'},
            K('심연의 메아리의 징조 + 공개로 아이템 희귀도 1~2티어', 'Omen of Abyssal Echoes + reveal for T1–2 item rarity') | {'node': 'a6'},
            K('빗나가면 소멸의 오브 + 빛의 징조로 훼손 옵션 제거', 'A miss: Orb of Annulment + Omen of Light removes the desecrated option') | {'node': 'a6x'},
            K('보존된 빗장뼈로 접두 빈자리에 다시 훼손', 'Preserved Collarbone desecrates the open prefix again') | {'node': 'a6d'}],
  'stepsBy': {'ess': [K('완벽한 정신의 에센스로 최대 마나 % — 접두 3개 중 하나가 지워짐', 'Perfect Essence of the Mind for % maximum mana: one of the three prefixes goes') | {'node': 'a4'},
                      K('훼손 옵션이 지워지면 좌측 강령술의 징조 + 보존된 빗장뼈로 다시 훼손, 최대 마나 %가 지워지면 에센스부터', 'Desecrated option gone: Omen of Sinistral Necromancy + Preserved Collarbone again; % maximum mana gone: essence again') | {'node': 'a5'},
                      K('심연의 메아리의 징조 + 공개, 결과 그대로', 'Omen of Abyssal Echoes + reveal, kept as it comes') | {'node': 'a6'}]},
  'worst': {'kr': '마나 최대치가 지워지면 새 매직 베이스부터', 'en': 'Maximum mana gone: a new magic base', 'to': 'xb'},
  'item': [MA, PM, RD, CS, RE, LR],
  'itemBy': {'ess': [MA, PM, L('p', '발견하는 아이템 희귀도 (16—19)% 증가', '(16—19)% increased Rarity of Items found', 'd'), CS, RE, LR]}}]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'mana'}, {'tag': 'pmana', 'ess': True}, {'tag': 'rarD', 'des': True},
            {'tag': 'cast'}, {'tag': 'rarE', 'ess': True}, {'side': 's', 'random': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'mana'}, {'tag': 'pmana', 'ess': True}, {'side': 'p', 'random': True, 'des': True},
            {'tag': 'cast'}, {'tag': 'rarE', 'ess': True}, {'side': 's', 'random': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
