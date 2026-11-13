# G8 2026-11-13: Diztoh 5옵션 에메랄드(s70CV_nvjXg) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G8/diztoh-5mod-emerald-v2/timeline.md, frames/ (첫 번째 에메랄드 Behemoth Delirium 0:00~11:30 화면 대조)
# H2 11-13: review/H2/diztoh-5mod-emerald-v2/ — 1:19~2:51, 7:24~8:17, 13:08~14:25, 15:50~16:35 화면 대조
# 실행: cd scripts/graphs && python3 gen_diztoh_5mod_emerald.py  → diztoh-5mod-emerald-v2.json (gen_batch9.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-5mod-emerald-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CD = L('s', '공격 피해의 치명타 피해 보너스 (10—20)% 증가', '(10—20)% increased Critical Damage Bonus for Attack Damage', 'f', ['critD'])
QAS = L('s', '육척봉 사용 시 공격 속도 (2—4)% 증가', '(2—4)% increased Attack Speed with Quarterstaves', 'n', ['qas'])
AS = L('s', '공격 속도 (2—4)% 증가', '(2—4)% increased Attack Speed', 'd', ['as'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
ATK = L('p', '공격 피해 (5—15)% 증가', '(5—15)% increased Attack Damage', 'n', ['atk'])
FER = L('p', '접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes', 'c', ['fer'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
RS = lambda s: L(s, '랜덤 옵션', 'Random option', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'diztoh-5mod-emerald-v2', 'recipe': 'diztoh-5mod-emerald-v2', 'cls': 'Emerald', 'base': 'Emerald', 'ilvl': 80,
 'basePrice': {'Divine_Orb': 65},   # 0:36 거래소 'Behemoth Delirium' 65 div(분열 공격 치명타 피해 보너스 19% + 원소 피해), 0:52~1:06 같은 매물 65~70 div
 'note': ('2026-11-13 G8 영상 화면 대조(근거 scratchpad review/G8/diztoh-5mod-emerald-v2/timeline.md). 에메랄드 2개 중 첫 번째(Behemoth Delirium, 아이템 레벨 80) 성공 회차 한 줄: '
          '분열 공격 치명타 피해 보너스 19% + 원소 피해 접두 레어 에메랄드 구입(0:36 65 div) → 카오스 반복으로 육척봉 공격 속도(1:19 카오스 오브, 1:24 결과) → 엑잘 2번 접두(2:49 회피·투사체 피해, 2:51 "옵션 자리 없음" 채팅) → '
          '위력적인 액체 경멸(2:48 툴팁, 2:52 성공) → 보존된 두개골(3:23, 접두가 꽉 차 접미로) → 심연의 메아리 공개(빛의 징조 반복, 4:30 빛의 징조를 다 씀, 6:02 공격 속도) → '
          '좌측 소멸의 징조 + 소멸의 오브로 경멸 옵션(6:02 채팅) → 엑잘 접두(6:02 위험 피해) → 카오스로 접두 공격 피해(접미가 한도를 넘어 접두만, 6:00~9:35) → '
          '위력적인 액체 흉포함(8:00 실패 = 공격 피해가 지워짐 → 카오스 다시, 9:48 원소 피해가 지워지고 성공). 신성한 오브·제련된 강탈자 기폭제(11:30)·두 번째 에메랄드(12:30~)·타락(26:00~)은 뺌. '
          'H2 11-13 화면 대조(근거 scratchpad review/H2/diztoh-5mod-emerald-v2/): 시작은 소멸·우측 찬미가 아니라 카오스 반복(1:19~1:24), 경멸 실패 처리는 세 번째 에메랄드 16:02~16:10 화면대로 분열 + 옵션 1개로 줄인 뒤 카오스부터, 흉포함 실패(8:17 육척봉 피해가 지워짐)는 카오스 다시. 카오스 접두 목표는 영상이 받아들인 피해 접두 셋 중 하나(공격 피해·육척봉 사용 시 피해·희귀 및 고유 적 명중 시 피해, 정책 11장 11-13 14:17), 화면·카드는 성공 회차의 공격 피해. 내부 결정: 좌측 소멸이 좋은 접두를 지우면 같은 징조로 다시.'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('공개 결과 그대로, 접두 카오스 없이 흉포함 한 번', 'Keep the reveal, one Ferocity without the prefix Chaos')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 빛의 징조로 다시 공개, 공격 피해까지 카오스', 'Video: Omen of Light on a missed reveal, Chaos until attack damage')}],
 'tags': {'critD': {'gi': 5}, 'qas': {'gi': 55}, 'as': {'gi': 7}, 'atk': {'gi': 6}, 'fer': {'gi': 117},
          'qsd': {'gi': 53}, 'rare': {'gi': 10},
          # H2 11-13: 영상이 받아들인 피해 접두 셋(7:24 희귀 및 고유 적 피해 '보스용', 7:55·14:16 육척봉 피해, 9:35 공격 피해) — 성공 조건은 그중 하나(정책 11장 2026-11-13 14:17)
          'pd': {'anyOf': ['atk', 'qsd', 'rare'], 'label': K('공격 피해·육척봉 사용 시 피해·희귀 및 고유 적 명중 시 피해', 'Attack damage, quarterstaff damage or damage against rare and unique enemies')},
          'contS': {'gi': 119, 'slot': {'s': 1}}, 'contP': {'gi': 120, 'slot': {'p': 1}}},
 'require': {'all': [{'has': 'critD'}, {'has': 'qas'}, {'has': 'fer'}, {'not': {'has': 'contS'}},
                     {'any': [{'all': [{'has': 'as'}, {'has': 'pd'}]}, {'param': {'v': 2}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},   # 주얼: 접두 2 · 접미 2(정책 8장)
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'atk'}, {'tag': 'fer'}, {'tag': 'critD', 'fr': True}, {'tag': 'qas'}, {'tag': 'as', 'des': True}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'side': 'p', 'random': True}, {'tag': 'fer'}, {'tag': 'critD', 'fr': True}, {'tag': 'qas'}, {'side': 's', 'random': True, 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'rare', 'mods': [{'tag': 'critD', 'fr': True}, {'junk': 'p'}]},
  label=K('분열 공격 치명타 피해 보너스와 접두 1개가 붙은 아이템 레벨 80 레어 에메랄드 구입', 'Buy an item level 80 rare Emerald with fractured attack crit damage and one prefix'),
  item=[J('p'), CD])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='a2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), CD])
# H2 11-13 화면 대조: 1:19 카오스 오브 툴팁 → 1:21~1:23 분열 옵션이 아닌 옵션이 계속 바뀜(마나 흡수·투사체 피해·중독 지속시간) → 1:24 육척봉 공격 속도. 소멸·우측 찬미는 쓰지 않음
A(id='a2', kind='act', group='main', pos=[0, 2.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 육척봉 공격 속도', 'Attack Speed with Quarterstaves suffix'), show=['qas'],
  showText=[K('분열 옵션은 그대로, 다른 옵션 1개만 바뀜', 'The fracture stays; only the other option changes')],
  edges=[{'if': {'has': 'qas'}, 'to': 'a3', 'res': 'ok'}, {'to': 'a2', 'res': 'fail', 'hide': True}], item=[CD, QAS])
A(id='a3', kind='act', group='main', pos=[0, 3.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 첫 번째 옵션', 'First prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 꽉 차 접두로)', 'en': 'One random option (suffixes are full)'}],
  edges=[{'to': 'a4'}], item=[J('p'), CD, QAS])
A(id='a4', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 꽉 차 접두로)', 'en': 'One random option (suffixes are full)'}],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'a4', 'hide': True}, {'to': 'k1'}], item=[J('p'), J('p'), CD, QAS])
A(id='k1', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed'),
  showText=[K('접두 잡옵이 지워지면 성공, 접미가 지워지면 실패', 'A junk prefix goes: success; a suffix goes: miss')],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'qas'}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'k1x', 'res': 'fail', 'label': K('육척봉 공격 속도가 지워짐', 'Quarterstaff attack speed removed')}],
  item=[J('p'), CONT, CD, QAS])
# H2 11-13 화면 대조(세 번째 에메랄드 16:02~16:10): 경멸이 공격 속도 접미를 지우고 '접두어 +1개'가 붙음 → 분열 + 옵션 1개로 줄인 뒤 카오스 반복(16:10~16:16)
A(id='k1x', kind='cleanup', group='main', pos=[1, 5.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기고 카오스부터', 'Keep only the fracture + one option, back to Chaos'), edges=[{'to': 'a2', 'label': K('카오스부터', 'Back to Chaos')}])
A(id='d1', kind='act', group='main', pos=[0, 6.4], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개) — 접두가 꽉 차 접미로', 'en': 'Desecrated (unrevealed): prefixes are full, so a suffix'}],
  edges=[{'to': 'r1'}], item=[J('p'), CONT, CD, QAS, UN('s')])
A(id='r1', kind='act', group='main', pos=[0, 7.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='as', label=K('공개', 'Reveal'),
  goal=K('접미 공격 속도', 'Attack Speed suffix'), show=['as'],
  edges=[{'if': {'added': 'as'}, 'to': 'n1', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접미 세 번째 옵션 — 공개 결과 그대로', 'Third suffix: keep the reveal'), 'show': [],
         'item': [J('p'), CONT, CD, QAS, RS('s')],
         'edges': [{'if': {'added': 'as'}, 'to': 'n1', 'res': 'ok'}, {'to': 'n1', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')}]}}],
  item=[J('p'), CONT, CD, QAS, AS])
A(id='r1x', kind='act', group='main', pos=[1, 7.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='n1', kind='act', group='main', pos=[0, 8.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=K('소멸', 'Annul'),
  goal=K('접미어 속성 부여의 최대 개수 +1개 지우기 (접두 2개 중 하나)', 'Remove +1 Suffix Modifier allowed (one of two prefixes)'),
  edges=[{'if': {'has': 'contS'}, 'to': 'n1', 'res': 'fail', 'label': K('다른 접두가 지워짐 — 다시', 'The other prefix went: again')}, {'to': 'g1', 'res': 'ok'}],
  item=[J('p'), CD, QAS, AS], over=[{'param': {'v': 2}, 'set': {'item': [J('p'), CD, QAS, RS('s')]}}])
A(id='g1', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션', 'Second prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 한도를 넘어 접두로)', 'en': 'One random option (suffixes over the limit)'}],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'g1', 'hide': True}, {'to': 'c1'}],
  item=[J('p'), J('p'), CD, QAS, AS], over=[{'param': {'v': 2}, 'set': {'item': [J('p'), J('p'), CD, QAS, RS('s')]}}])
A(id='c1', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 공격 피해', 'Attack Damage prefix'), show=['atk'],
  showText=[K('접미가 한도를 넘어 접두만 바뀜', 'Suffixes are over the limit: only prefixes change')],
  skipIf={'param': {'v': 2}}, skipTo='f1',
  edges=[{'if': {'all': [{'has': 'pd'}, {'has': 'fer'}]}, 'to': 'ok', 'res': 'ok', 'hide': True},
         {'if': {'has': 'pd'}, 'to': 'f1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}],
  item=[ATK, J('p'), CD, QAS, AS])
A(id='f1', kind='act', group='main', pos=[0, 11.4], act='essence', cur='Potent_Liquid_Ferocity', ess='fer', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes'),
  showText=[K('접두 잡옵이 지워지면 성공, 공격 피해가 지워지면 실패', 'The junk prefix goes: success; attack damage goes: miss')],
  edges=[{'if': {'has': 'pd'}, 'to': 'ok', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'label': K('공격 피해가 지워짐 — 다시 카오스', 'Attack damage gone: Chaos again')}],
  over=[{'param': {'v': 2}, 'set': {'showText': [K('접두 하나가 지워짐 — 결과 그대로', 'One prefix goes: keep the result')], 'edges': [{'to': 'ok', 'res': 'ok'}],
         'item': [RS('p'), FER, CD, QAS, RS('s')]}}],
  item=[ATK, FER, CD, QAS, AS])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'},
              {'id': 'L2', 'nodes': ['c1', 'f1'], 'kr': '흉포함', 'en': 'Ferocity'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
