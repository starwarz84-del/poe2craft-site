# RECIPE-A 2026-11-14: Hexxat Gaming 5옵션 사파이어(0yK4eN3KpBo, 2026-09-30) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: docs/craft-guides.md '5차 조사' g93(영어 자막 단계·화폐 값, 7:42 완성품 화면) + docs/craft-guides.json register(ok)
# 실행: cd scripts/graphs && python3 gen_hexxat_5mod_sapphire.py  → hexxat-5mod-sapphire-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/hexxat-5mod-sapphire-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CDn = L('s', '치명타 피해 보너스 (10—20)% 증가', '(10—20)% increased Critical Damage Bonus', 'n', ['cd'])
CD = dict(CDn, m='f')
CC = L('s', '치명타 확률 (5—15)% 증가', '(5—15)% increased Critical Hit Chance', 'n', ['c2'])
SCC = L('s', '주문 치명타 명중 확률 (5—15)% 증가', '(5—15)% increased Critical Hit Chance for Spells', 'd', ['rv'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
SD = L('p', '주문 피해 (5—15)% 증가', '(5—15)% increased Spell Damage', 'n', ['sd'])
FER = L('p', '접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes', 'c', ['fer'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'hexxat-5mod-sapphire-v2', 'recipe': 'hexxat-5mod-sapphire-v2', 'cls': 'Sapphire', 'base': 'Sapphire', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 4},   # 0:02 자막 '3~5 div'(치명타 피해 보너스가 최대 수치 근처인 사파이어) — 가운데 4 div
 'note': ('2026-11-14 RECIPE-A: Hexxat Gaming 5옵션 사파이어(2026-09-30, 0.5.5) 성공 회차 한 줄(근거 docs/craft-guides.md 5차 g93, 영어 자막 + 7:42 완성품 화면). '
          '치명타 피해 보너스 사파이어 구입(0:02, 3~5 div) → 옵션 4개 상태로 분열(1/4, 1:04 세 개 중 하나 성공) → 카오스로 접미 치명타 확률(1:34) → '
          '위력적인 액체 경멸(2:36, 분열 옵션은 안 지워져 약 66%, 실패하면 카오스로 다시) → 보존된 두개골 + 심연의 메아리로 접미 세 번째 옵션 주문 치명타 명중 확률(3:07) → '
          '좌측 소멸의 징조 + 소멸의 오브로 경멸 옵션 지우기(3:38, 실패해 하나 더) → 접두 2개(4:40) → 위력적인 액체 흉포함(50/50, 실패하면 카오스로 접두만 다시, 5:11) → 완성. '
          '신성한 오브 반복(5:42)은 수치 다듬기라 뺌. '
          '내부 결정(자막으로 개수·화폐를 확인 못 한 곳): ① 산 베이스는 옵션 4개 레어(분열 조건) ② 분열 뒤 카오스는 옵션 4개 그대로 접미 하나를 바꿈(영상 "소멸 → 카오스"의 소멸 개수가 자막에 없음) '
          '③ 경멸이 접미를 지우면 카오스로 다시(영상 말 그대로) ④ 공개가 빗나갔을 때 처리가 자막에 없어 결과 그대로(정책 10장 ⑤, 영상은 일반 치명타 확률도 받는다고 함) '
          '⑤ 경멸 옵션을 지운 뒤 접두 2개는 엑잘티드 오브, 주문 피해는 카오스(접미가 한도를 넘어 접두만 바뀜). '
          '등급: 난이도 3 → 밸런스·에센셜이지만 에센셜(카오스 없이 흉포함 한 번)이 밸런스와 10% 안이라 밸런스(영상) 하나만(정책 10장 ①).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],   # 에센셜(접두 카오스 없이 흉포함 한 번)은 빠른 시뮬 92.2 vs 밸런스 102.2 div(9.8%)라 정책 10장 ①로 밸런스 하나만
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 주문 피해까지 카오스, 흉포함이 주문 피해를 지우면 다시', 'Video: Chaos until spell damage, again when Ferocity takes it')}],
 'tags': {'cd': {'gi': 11}, 'cc': {'gi': 10}, 'scd': {'gi': 12}, 'cast': {'gi': 3},
          'c2': {'anyOf': ['cc', 'scd', 'cast'], 'shown': 'cc', 'label': K('치명타 확률·주문 치명타 피해 보너스·시전 속도', 'Critical Hit Chance, Critical Spell Damage Bonus or Cast Speed')},
          'scc': {'gi': 48}, 'rv': {'anyOf': ['scc', 'cc'], 'shown': 'scc', 'label': K('주문 치명타 명중 확률·치명타 확률', 'Spell Critical Hit Chance or Critical Hit Chance')},
          'sd': {'gi': 49}, 'fer': {'gi': 101},
          'contS': {'gi': 103, 'slot': {'s': 1}}, 'contP': {'gi': 104, 'slot': {'p': 1}}},
 'require': {'all': [{'has': 'cd'}, {'has': 'c2'}, {'has': 'fer'}, {'not': {'has': 'contS'}}, {'unrev': False},
                     {'any': [{'has': 'sd'}, {'param': {'v': 2}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},   # 주얼: 접두 2 · 접미 2(정책 8장)
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'sd'}, {'tag': 'fer'}, {'tag': 'cd', 'fr': True}, {'tag': 'c2'}, {'side': 's', 'random': True, 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='pf', start={'rar': 'rare', 'mods': [{'tag': 'cd'}, {'junk': 's'}, {'junk': 'p'}, {'junk': 'p'}]},
  label=K('치명타 피해 보너스 + 옵션 3개 레어 사파이어 구입 (아이템 레벨 82)', 'Buy a rare Sapphire with Critical Damage Bonus + three options (item level 82)'),
  item=[J('p'), J('p'), CDn, J('s')])
A(id='pf', kind='act', group='prep', pos=[0, 1], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (옵션 4개 중 하나)', 'Fracture (one of the four options)'),
  showText=[K('치명타 피해 보너스가 분열되면 성공', 'Success when Critical Damage Bonus fractures')],
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'cd'}, 'to': 'ms', 'res': 'ok', 'label': K('치명타 피해 보너스 분열', 'Critical Damage Bonus fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), J('p'), CD, J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 1], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('치명타 피해 보너스가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='a1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), J('p'), CD, J('s')])
A(id='a1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 두 번째 옵션', 'Second suffix'), show=['c2'],
  edges=[{'if': {'all': [{'has': 'c2'}, {'not': {'has': 'contP'}}, {'full': 'p'}]}, 'to': 'k1', 'res': 'ok'}, {'to': 'a1', 'res': 'fail', 'hide': True}],
  item=[J('p'), J('p'), CD, CC])
A(id='k1', kind='act', group='main', pos=[0, 4.4], act='essence', cur='Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed'),
  showText=[K('접두 잡옵이 지워지면 성공, 접미가 지워지면 실패', 'A junk prefix goes: success; a suffix goes: miss')],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'c2'}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'a1', 'res': 'fail', 'label': K('접미가 지워짐 — 다시 카오스', 'A suffix went: Chaos again')}],
  item=[J('p'), CONT, CD, CC])
A(id='d1', kind='act', group='main', pos=[0, 5.4], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '미공개 훼손 옵션 — 접두가 꽉 차서 접미로', 'en': 'Unrevealed desecration: prefixes are full, so a suffix'}],
  edges=[{'to': 'r1'}], item=[J('p'), CONT, CD, CC, UN('s')])
A(id='r1', kind='act', group='main', pos=[0, 6.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rv', label=K('공개', 'Reveal'),
  goal=K('접미 세 번째 옵션 공개 — 나오는 대로 (영상: 주문 치명타 명중 확률)', 'Reveal the third suffix: keep what comes (video: spell crit chance)'), show=['rv'],
  edges=[{'to': 'n1'}],
  item=[J('p'), CONT, CD, CC, SCC])
A(id='n1', kind='act', group='main', pos=[0, 7.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=K('소멸', 'Annul'), goal=ANN,
  target=K('접두 둘 중 접미어 속성 부여의 최대 개수 +1개 지우기', 'Remove +1 Suffix Modifier allowed, one of the two prefixes'),
  edges=[{'if': {'has': 'contS'}, 'to': 'n1', 'res': 'fail', 'label': K('다른 접두가 지워짐 — 다시', 'The other prefix went: again')}, {'to': 'g1', 'res': 'ok'}],
  item=[CD, CC, SCC])
A(id='g1', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 2개 채우기', 'Fill both prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 — 접미가 한도를 넘어 접두로', 'en': 'One random option: suffixes are over the limit'}],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'g1', 'hide': True}, {'to': 'c1'}],
  item=[J('p'), J('p'), CD, CC, SCC])
A(id='c1', kind='act', group='main', pos=[0, 9.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 주문 피해', 'Spell Damage prefix'), show=['sd'],
  showText=[K('접미가 한도를 넘어 접두만 바뀜', 'Suffixes are over the limit: only prefixes change')],
  skipIf={'any': [{'param': {'v': 2}}, {'has': 'sd'}]}, skipTo='f1', skipNote=K('주문 피해가 이미 있으면 건너뜀', 'Skipped when spell damage is already there'),
  edges=[{'if': {'all': [{'has': 'sd'}, {'has': 'fer'}]}, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'has': 'sd'}, 'to': 'f1', 'res': 'ok', 'label': K('흉포함 차례', 'Ferocity next')}, {'to': 'c1', 'res': 'fail', 'hide': True}],
  item=[SD, J('p'), CD, CC, SCC])
A(id='f1', kind='act', group='main', pos=[0, 10.4], act='essence', cur='Potent_Liquid_Ferocity', ess='fer', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes'),
  showText=[K('접두 잡옵이 지워지면 성공, 주문 피해가 지워지면 실패', 'The junk prefix goes: success; spell damage goes: miss')],
  edges=[{'if': {'has': 'sd'}, 'to': 'ok', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'label': K('주문 피해가 지워짐 — 다시 카오스', 'Spell damage gone: Chaos again')}],
  over=[{'param': {'v': 2}, 'set': {'showText': [K('접두 하나가 지워짐 — 결과 그대로', 'One prefix goes: keep the result')], 'edges': [{'to': 'ok', 'res': 'ok'}],
         'item': [J('p'), FER, CD, CC, SCC]}}],
  item=[SD, FER, CD, CC, SCC])
A(id='ok', kind='done', group='main', pos=[0, 11.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['a1', 'k1'], 'kr': '경멸', 'en': 'Contempt'},
              {'id': 'L2', 'nodes': ['c1', 'f1'], 'kr': '흉포함', 'en': 'Ferocity'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
