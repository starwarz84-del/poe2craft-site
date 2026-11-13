# G9 2026-11-13: LilBotQ 5옵션 에메랄드(Hcb_HcWDUOA, 23:43) 플로우차트 생성기 — 영상 고급 제작 에메랄드(Luminous Delirium) 성공 회차 한 줄
# 근거: scratchpad review/G9/lilbotq-emerald-v2/timeline.md, frames/ (영상 화면 대조)
# 실행: cd scripts/graphs && python3 gen_lilbotq_emerald.py  → lilbotq-emerald-v2.json (gen_batch9.py 끝에서 자동 호출, 그 파일의 이 아이템 구간을 대신함)
# 상자 id는 옛 단계 레시피(recipes_v5_lilbotq-emerald.py: l1~l9·l5b)와 겹치지 않게 j0~j8.
# 등급: 밸런스만(사용자 확정 2026-11-10 — 영상의 가성비 방법은 비싼 베이스를 사서 하는 도박이라 에센셜 없음).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/lilbotq-emerald-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

HER = L('p', '전령 스킬 피해 (15—25)% 증가', 'Herald Skills deal (15—25)% increased Damage', 'j')
QST = L('p', '육척봉 사용 시 피해 (6—16)% 증가', '(6—16)% increased Damage with Quarterstaves', 'j')
CD = L('s', '공격 피해의 치명타 피해 보너스 (10—20)% 증가', '(10—20)% increased Critical Damage Bonus for Attack Damage', 'n', ['critD'])
MS = L('s', '이동 속도 (1—2)% 증가', '(1—2)% increased Movement Speed', 'n', ['ms'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
CC = L('s', '공격 치명타 명중 확률 (6—16)% 증가 (훼손)', '(6—16)% increased Critical Hit Chance for Attacks (desecrated)', 'd', ['critA'])
ATK = L('p', '공격 피해 (5—15)% 증가', '(5—15)% increased Attack Damage', 'n', ['atk'])
FER = L('p', '접미어 효과 (40—60)% 증가', '(40—60)% increased Effect of Suffixes', 'c', ['fer'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'lilbotq-emerald-v2', 'recipe': 'lilbotq-emerald-v2', 'cls': 'Emerald', 'base': 'Emerald', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 2.5},   # 15:00 자막 '하나에 2~3 div'(좋은 접미 2개 에메랄드)
 'note': ('2026-11-13 G9 영상 전체 대조(근거 scratchpad review/G9/lilbotq-emerald-v2/timeline.md). 고급 제작(9:10~21:30) 중 끝까지 간 에메랄드(Luminous Delirium) 한 줄: '
          '공격 치명타 피해 보너스 + 이동 속도 접미, 접두 잡옵 2개(전령 스킬 피해·육척봉 피해) 희귀 에메랄드 구입(15:00, 2~3 div) → 위력적인 액체 경멸(15:26, 전령 피해가 지워지고 +1 접미 허용 — 실패면 버림, 영상 4개 중 1개 성공) → '
          '우측 강령술 + 보존된 두개골(15:34) → 심연의 메아리 공개(16:00 빗나감, 빛의 징조 반복 17:20~18:00, 공격 치명타 명중 확률) → 좌측 소멸의 징조 + 소멸의 오브(19:15, 빗나가 육척봉 피해가 지워짐) → '
          '좌측 말소의 징조 + 카오스(19:25, +1 접미 허용이 지워짐) → 엑잘(19:35) → 카오스 반복(접미가 한도를 넘어 접두만 바뀜, 20:40 공격 피해) → 위력적인 액체 흉포함(20:45 50:50 성공). 신성한 오브(21:10 말만)는 뺌. '
          '11-13 오후 새 정책 A: 공개 목표 = 공격 치명타 명중 확률·공격 속도 중 하나(18:00 자막: 메아리로 공격 속도도 나왔지만 치명타 확률을 고름 — 둘 다 받는 옵션). 화면·카드는 성공 회차의 공격 치명타 명중 확률.'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [{'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
               'desc': K('영상: 빛의 징조로 다시 공개, 좌측 소멸의 징조로 경멸 옵션 제거, 카오스로 공격 피해 → 액체 흉포함', 'Video: Light retries, Sinistral Annulment for the contempt line, Chaos for attack damage, then Ferocity')}],
 'tags': {'critD': {'gi': 5}, 'ms': {'gi': 45}, 'critA': {'gi': 4}, 'as': {'gi': 7},
          'rev': {'anyOf': ['critA', 'as'], 'shown': 'critA', 'label': K('공격 치명타 명중 확률 증가·공격 속도 증가', 'Attack crit chance or attack speed')}, 'atk': {'gi': 6},
          'contS': {'gi': 119, 'slot': {'s': 1}}, 'contP': {'gi': 120, 'slot': {'p': 1}}, 'fer': {'gi': 117}},
 'require': {'all': [{'has': 'critD'}, {'has': 'ms'}, {'has': 'rev'}, {'has': 'atk'}, {'has': 'fer'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'j0',
 'cap': {'p': 2, 's': 2},
 'finals': [{'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'atk'}, {'tag': 'fer'}, {'tag': 'critD'}, {'tag': 'ms'}, {'tag': 'rev', 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='j0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'rare', 'mods': ['critD', 'ms', {'junk': 'p'}, {'junk': 'p'}]},
  label=K('공격 치명타 피해 보너스 + 이동 속도 접미, 접두 2개 희귀 에메랄드 구입 (아이템 레벨 82)', 'Buy a rare Emerald: attack crit damage bonus + movement speed suffixes, two prefixes (item level 82)'),
  item=[HER, QST, CD, MS])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='j1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[HER, QST, CD, MS])
A(id='j1', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed'),
  showText=[K('접두 잡옵이 지워지면 성공, 접미가 지워지면 실패', 'A junk prefix goes: success; a suffix goes: miss')],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'critD'}, {'has': 'ms'}]}, 'to': 'j2', 'res': 'ok'},
         {'to': 'j1x', 'res': 'fail', 'label': K('접미가 지워짐', 'A suffix removed')}],
  item=[QST, CONT, CD, MS])
A(id='j1x', kind='exit', group='main', pos=[1, 2.4], simTo='j0', variant='fail', label=K('새 에메랄드', 'New Emerald'),
  note=K('접미어 +1개가 붙지 않으면 그 주얼은 버리고 새 주얼로', 'No +1 suffix: set the jewel aside and buy a new one'))
A(id='j2', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Cranium', omens=['Omen_of_Dextral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'j3'}],
  item=[QST, CONT, CD, MS, UN('s')])
A(id='j3', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev',
  label=K('공개', 'Reveal'), goal=K('접미 공격 치명타 명중 확률', 'Attack crit chance suffix'), show=['rev'],
  edges=[{'if': {'added': 'rev'}, 'to': 'j4', 'res': 'ok'}, {'to': 'j3x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[QST, CONT, CD, MS, CC])
A(id='j3x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'j2', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='j4', kind='act', group='main', pos=[0, 5.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'],
  label=ANN, goal=K('접미어 속성 부여의 최대 개수 +1개 지우기 — 접두 2개 중 하나', 'Remove +1 Suffix Modifier allowed: one of the two prefixes'),
  target=K('접미어 속성 부여의 최대 개수 +1개 제거', 'Remove +1 Suffix Modifier allowed'),
  ask=K('어느 접두가 지워짐?', 'Which prefix went?'),
  edges=[{'if': {'has': 'contS'}, 'to': 'j4e', 'res': 'fail', 'label': K('다른 접두가 지워짐', 'The other prefix went')},
         {'to': 'j5', 'res': 'ok', 'label': K('접미어 +1개가 지워짐', '+1 suffix line removed')}],
  item=[CONT, CD, MS, CC])   # 영상(19:15)은 빗나감 → 4.A가 아니라 다음 상자(좌측 말소 카오스)가 주 경로
A(id='j4e', kind='act', group='main', pos=[0, 6.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Sinistral_Erasure'],
  label=K('카오스', 'Chaos'), goal=K('남은 접미어 속성 부여의 최대 개수 +1개 바꾸기 — 접두가 그 옵션뿐이라 확정', 'Reroll the remaining +1 Suffix Modifier allowed: it is the only prefix'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'j5'}], item=[J('p'), CD, MS, CC])
A(id='j5', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Exalted_Orb',
  label=K('엑잘', 'Exalt'), goal=K('접두 두 번째 옵션 — 접미가 한도를 넘어 접두로', 'Second prefix: suffixes are over the limit'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  skipIf={'full': 'p'}, skipTo='j6', skipNote=K('접두가 꽉 차 있으면 건너뜀', 'Skip when the prefixes are full'),
  edges=[{'to': 'j6'}], item=[J('p'), J('p'), CD, MS, CC])
A(id='j6', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb',
  label=K('카오스', 'Chaos'), goal=K('접두 공격 피해 증가 — 접미가 한도를 넘어 접두만 바뀜', 'Attack damage prefix: only prefixes change'), show=['atk'],
  skipIf={'has': 'atk'}, skipTo='j7', skipNote=K('공격 피해가 이미 있으면 건너뜀', 'Skip when attack damage is already there'),
  edges=[{'if': {'has': 'atk'}, 'to': 'j7', 'res': 'ok'}, {'to': 'j6', 'res': 'fail', 'hide': True}],
  item=[ATK, J('p'), CD, MS, CC])
A(id='j7', kind='act', group='main', pos=[0, 9.4], act='essence', cur='Potent_Liquid_Ferocity', ess='fer', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 효과 증가', 'Increased Effect of Suffixes'),
  showText=[K('접두 잡옵이 지워지면 성공, 공격 피해가 지워지면 실패', 'The junk prefix goes: success; attack damage goes: miss')],
  edges=[{'if': {'has': 'atk'}, 'to': 'ok', 'res': 'ok'}, {'to': 'j6', 'res': 'fail', 'label': K('공격 피해가 지워짐 — 다시 카오스', 'Attack damage gone: Chaos again')}],
  item=[ATK, FER, CD, MS, CC])
A(id='ok', kind='done', group='main', pos=[0, 10.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['j2', 'j3', 'j3x'], 'kr': '훼손 공개', 'en': 'Reveal'},
              {'id': 'L2', 'nodes': ['j6', 'j7'], 'kr': '흉포함', 'en': 'Ferocity'}]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
