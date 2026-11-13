# G8 2026-11-13: Diztoh 5옵션 사파이어(-YZm55-QuoQ) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G8/diztoh-5mod-sapphire-v2/timeline.md, frames/ (영상 0:00~8:53 화면 대조)
# 실행: cd scripts/graphs && python3 gen_diztoh_5mod_sapphire.py  → diztoh-5mod-sapphire-v2.json (gen_batch9.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-5mod-sapphire-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SCC = L('s', '주문 치명타 명중 확률 (5—15)% 증가', '(5—15)% increased Critical Hit Chance for Spells', 'n', ['scc'])
CC = L('s', '치명타 확률 (5—15)% 증가', '(5—15)% increased Critical Hit Chance', 'n', ['c2'])
CAST = L('s', '시전 속도 (2—4)% 증가', '(2—4)% increased Cast Speed', 'd', ['cast'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
COLD = L('p', '냉기 피해 (5—15)% 증가', '(5—15)% increased Cold Damage', 'n', ['cold'])
FER = L('p', '접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes', 'c', ['fer'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
RS = lambda s: L(s, '랜덤 옵션', 'Random option', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'diztoh-5mod-sapphire-v2', 'recipe': 'diztoh-5mod-sapphire-v2', 'cls': 'Sapphire', 'base': 'Sapphire', 'ilvl': 79,
 'note': ('2026-11-13 G8 영상 전체 화면 대조(근거 scratchpad review/G8/diztoh-5mod-sapphire-v2/timeline.md). 주얼 하나(Apocalypse Shine, 아이템 레벨 79) 성공 회차 한 줄: '
          '옵션 4개 레어 사파이어(0:08) → 소멸의 오브로 정리 → 카오스 접미(0:20~1:50, 성공 회차 2:42 주문 치명타 명중 확률 14%) → 우측 찬미 + 엑잘로 치명타 확률(빗나가면 소멸의 오브 0:47·1:02) → '
          '엑잘 2번 접두(2:50) → 위력적인 액체 경멸(2:02 툴팁, 2:32 실패 = 접두어 +1개 → 모두 지우고 카오스부터, 3:03 성공) → 보존된 두개골(3:16, 접두가 꽉 차 접미로) → '
          '심연의 메아리 공개(3:38 빗나감 → 빛의 징조 + 소멸의 오브 반복, 4:38 시전 속도) → 좌측 소멸의 징조 + 소멸의 오브로 경멸 옵션(5:12) → 상위 엑잘(5:16) → '
          '카오스로 접두 냉기 피해(6:05~6:58, 접미가 한도를 넘어 접두만 바뀜) → 위력적인 액체 흉포함(7:05 최대 에너지 보호막이 지워짐) → 완성(7:12). '
          '영상과 다르게 정한 점: 5:50 첫 흉포함(카오스 전 시범, 그 옵션은 카오스로 지워짐)은 뺌, 신성한 오브·제련된 달리는 기폭제(8:00~8:18)는 마무리라 뺌, '
          '좌측 소멸의 징조가 좋은 접두를 지운 경우는 영상에 없어 같은 징조로 다시(내부 결정), 시작 정리는 옵션 1개까지(영상은 모두 지운 뒤 카오스 — 화면 편집으로 확인 못 함). '
          '11-13 오후 새 정책(P12, 정책 3장 아무거나): 두 번째 접미는 치명타 확률 또는 치명타 피해 보너스(묶음 c2) — 첫 회차(1:50 주문 치명타 14% + 치명타 피해 보너스 14%)를 그대로 엑잘 2번(1:58)·경멸(2:02)까지 이어 가서 화면 근거가 있는 두 옵션만. '
          '화면은 성공 회차 치명타 확률(shown). 첫 접미(주문 치명타 명중 확률, 두 회차 모두)·공개(시전 속도)·접두(냉기 피해)는 다른 옵션을 받은 화면이 없어 그대로.'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('공개 결과 그대로, 접두 카오스 없이 흉포함 한 번', 'Keep the reveal, one Ferocity without the prefix Chaos')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 빛의 징조로 다시 공개, 냉기 피해까지 카오스', 'Video: Omen of Light on a missed reveal, Chaos until cold damage')}],
 'tags': {'scc': {'gi': 48}, 'cc': {'gi': 10}, 'cdb': {'gi': 11},
          'c2': {'anyOf': ['cc', 'cdb'], 'shown': 'cc', 'label': K('치명타 확률·치명타 피해 보너스', 'Critical Hit Chance or Critical Damage Bonus')}, 'cast': {'gi': 3}, 'cold': {'gi': 6}, 'fer': {'gi': 101},
          'contS': {'gi': 103, 'slot': {'s': 1}}, 'contP': {'gi': 104, 'slot': {'p': 1}}},
 'require': {'all': [{'has': 'scc'}, {'has': 'c2'}, {'has': 'fer'}, {'not': {'has': 'contS'}},
                     {'any': [{'all': [{'has': 'cast'}, {'has': 'cold'}]}, {'param': {'v': 2}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},   # 주얼: 접두 2 · 접미 2(정책 8장)
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'cold'}, {'tag': 'fer'}, {'tag': 'scc'}, {'tag': 'c2'}, {'tag': 'cast', 'des': True}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'side': 'p', 'random': True}, {'tag': 'fer'}, {'tag': 'scc'}, {'tag': 'c2'}, {'side': 's', 'random': True, 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='pc', start={'rar': 'rare', 'mods': [{'junk': 's'}, {'junk': 'p'}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('옵션 4개 레어 사파이어', 'Rare Sapphire with four options'), item=[J('p'), J('p'), J('s'), J('s')])
A(id='pc', kind='cleanup', group='prep', pos=[0, 1], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('옵션 1개만 남기기', 'Keep only one option'), edges=[{'to': 'ms'}], item=[J('x')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='a1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('x')])
A(id='a1', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 주문 치명타 명중 확률', 'Spell Critical Hit Chance suffix'), show=['scc'],
  edges=[{'if': {'has': 'scc'}, 'to': 'a2', 'res': 'ok'}, {'to': 'a1', 'res': 'fail', 'hide': True}], item=[SCC])
A(id='a2', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 치명타 확률', 'Critical Hit Chance suffix'), show=['c2'],
  edges=[{'if': {'has': 'c2'}, 'to': 'a3', 'res': 'ok'}, {'to': 'a2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[SCC, CC])
A(id='a2x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,   # F2a 11-13: 정리 상자(확정)였지만 접미 둘 중 하나라 절반은 주문 치명타가 지워짐 → 확률 상자
  target=K('빗나간 접미 지우기', 'Remove the missed suffix'),
  edges=[{'if': {'not': {'has': 'scc'}}, 'to': 'a1', 'res': 'fail', 'label': K('주문 치명타 명중 확률이 지워짐 — 다시 카오스', 'Spell crit chance gone: Chaos again')},
         {'to': 'a2', 'res': 'ok', 'port': 'right', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='a3', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 첫 번째 옵션', 'First prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 — 접미가 꽉 차서 접두로', 'en': 'One random option: suffixes are full'}],
  edges=[{'to': 'a4'}], item=[J('p'), SCC, CC])
A(id='a4', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 — 접미가 꽉 차서 접두로', 'en': 'One random option: suffixes are full'}],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'a4', 'hide': True}, {'to': 'k1'}], item=[J('p'), J('p'), SCC, CC])
A(id='k1', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed'),
  showText=[K('접두 잡옵이 지워지면 성공, 접미가 지워지면 실패', 'A junk prefix goes: success; a suffix goes: miss')],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'scc'}, {'has': 'c2'}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'k1x', 'res': 'fail', 'label': K('접미가 지워짐', 'A suffix removed')}],
  item=[J('p'), CONT, SCC, CC])
A(id='k1x', kind='cleanup', group='main', pos=[1, 7.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('옵션 1개만 남기고 카오스부터', 'Keep one option, Chaos again'), edges=[{'to': 'a1', 'label': K('다시 카오스', 'Chaos again')}])
A(id='d1', kind='act', group='main', pos=[0, 8.4], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '미공개 훼손 옵션 — 접두가 꽉 차서 접미로', 'en': 'Unrevealed desecration: prefixes are full, so a suffix'}],
  edges=[{'to': 'r1'}], item=[J('p'), CONT, SCC, CC, UN('s')])
A(id='r1', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cast', label=K('공개', 'Reveal'),
  goal=K('접미 시전 속도', 'Cast Speed suffix'), show=['cast'],
  edges=[{'if': {'added': 'cast'}, 'to': 'n1', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접미 세 번째 옵션 공개', 'Reveal the third suffix'), 'show': [],
                  'edges': [{'if': {'added': 'cast'}, 'to': 'n1', 'res': 'ok'}, {'to': 'n1', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')}]}}],
  item=[J('p'), CONT, SCC, CC, CAST])
A(id='r1x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='n1', kind='act', group='main', pos=[0, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=K('소멸', 'Annul'), goal=ANN,   # F2a 11-13: 제목과 목표가 같은 괄호 글이던 것
  target=K('접두 둘 중 접미어 속성 부여의 최대 개수 +1개 지우기', 'Remove +1 Suffix Modifier allowed, one of the two prefixes'),
  edges=[{'if': {'has': 'contS'}, 'to': 'n1', 'res': 'fail', 'label': K('다른 접두가 지워짐 — 다시', 'The other prefix went: again')}, {'to': 'g1', 'res': 'ok'}],
  item=[J('p'), SCC, CC, CAST])
A(id='g1', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 — 접미가 한도를 넘어 접두로', 'en': 'One random option: suffixes are over the limit'}],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'g1', 'hide': True}, {'to': 'c1'}],
  item=[J('p'), J('p'), SCC, CC, CAST])
A(id='c1', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 냉기 피해', 'Cold Damage prefix'), show=['cold'],
  showText=[K('접미가 한도를 넘어 접두만 바뀜', 'Suffixes are over the limit: only prefixes change')],
  skipIf={'param': {'v': 2}}, skipTo='f1',
  edges=[{'if': {'all': [{'has': 'cold'}, {'has': 'fer'}]}, 'to': 'ok', 'res': 'ok', 'hide': True, 'label': K('접미어 효과 증가가 남아 있으면 완성', 'Suffix effect still there: finished')},
         {'if': {'has': 'cold'}, 'to': 'f1', 'res': 'ok', 'label': K('흉포함 차례', 'Ferocity next')}, {'to': 'c1', 'res': 'fail', 'hide': True}],
  item=[COLD, J('p'), SCC, CC, CAST])
A(id='f1', kind='act', group='main', pos=[0, 13.4], act='essence', cur='Potent_Liquid_Ferocity', ess='fer', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes'),
  showText=[K('접두 잡옵이 지워지면 성공, 냉기 피해가 지워지면 실패', 'The junk prefix goes: success; cold damage goes: miss')],
  edges=[{'if': {'has': 'cold'}, 'to': 'ok', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'label': K('냉기 피해가 지워짐 — 다시 카오스', 'Cold damage gone: Chaos again')}],
  over=[{'param': {'v': 2}, 'set': {'showText': [K('접두 하나가 지워짐 — 결과 그대로', 'One prefix goes: keep the result')], 'edges': [{'to': 'ok', 'res': 'ok'}],
         'item': [J('p'), FER, SCC, CC, CAST]}}],
  item=[COLD, FER, SCC, CC, CAST])
A(id='ok', kind='done', group='main', pos=[0, 14.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'},
              {'id': 'L2', 'nodes': ['c1', 'f1'], 'kr': '흉포함', 'en': 'Ferocity'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
