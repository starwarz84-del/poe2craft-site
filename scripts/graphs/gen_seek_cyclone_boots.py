# G4 2026-11-13: 시크의 Seek 돌개바람 장화(cj9o8_LuFQs) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G4/seek-cyclone-boots-v2/timeline.md, frames/ (영상 0:00~12:15 화면 대조)
# 영상은 분열 성공 장화 2개로 마무리 방법 두 가지를 보여 줌: 사도 레깅스 = 접두 훼손 마무리(가성비, 에센셜), 충실한 레깅스 = 세를의 승리 + 접미 훼손(밸런스).
# 실행: cd scripts/graphs && python3 gen_seek_cyclone_boots.py  → seek-cyclone-boots-v2.json (gen_batch11.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/seek-cyclone-boots-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

ELEn = L('s', '방어도의 +(38—43)%가 원소 피해에도 적용', '+(38—43)% of Armour also applies to Elemental Damage', 'n', ['ele'])
ELE = L('s', '방어도의 +(38—43)%가 원소 피해에도 적용', '+(38—43)% of Armour also applies to Elemental Damage', 'f', ['ele'])
CHG = L('s', '스킬이 (7—10)% 확률로 충전을 제거하지 않고도 소모한 것으로 간주', 'Skills have a (7—10)% chance to not remove Charges but still count as consuming them', 'n', ['chg'])
SPI = L('s', '정신력 +(10—15)', '+(10—15) to Spirit', 'c', ['spirit'])
DUR = L('s', '스킬 효과 지속시간 (20—29)% 증가', '(20—29)% increased Skill Effect Duration', 'd', ['dur'])
AES = L('p', '방어도 +(72—85) / 에너지 보호막 최대치 +(22—25)', '+(72—85) to Armour / +(22—25) to maximum Energy Shield', 'd', ['aes'])
UHT = L('r', '우트레드의 성좌', "Uhtred's Sidereus", 'r')
SER = L('r', '세를의 승리', 'Serle’s Triumph', 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V1 = {'param': {'v': 1}}
V2 = {'param': {'v': 2}}

g = {
 'id': 'seek-cyclone-boots-v2', 'recipe': 'seek-cyclone-boots-v2', 'cls': 'Boots_str_int', 'base': 'Faithful Leggings', 'ilvl': 81,
 'basePrice': {},   # 영상에 매물 가격 없음(1:10 장화 8개를 구해 옴)
 'xsub': ["Uhtred's Sidereus"], 'xroll': True,   # 우트레드 옵션(충전 미소모·지속시간)은 공개 가중치가 없어 훼손 전용과 같은 기준(추정), 카오스·엑잘 풀에는 일반 티어 평균(추정)
 'note': ('2026-11-13 G4 영상 전체 화면 대조(근거 scratchpad review/G4/seek-cyclone-boots-v2/timeline.md). '
          '방어도의 원소 피해 적용 + 옵션 2개 장화(홈 2개) 8개 구입(1:10~2:20) → 보존된 갈비뼈로 미공개 훼손(2:30~3:45, 분열 조건 옵션 4개) → 분열 1/3(3:50~4:05, 성공 2개) → 소멸의 오브로 옵션 1개만 남김(4:15) → '
          '우트레드의 성좌 장착(4:30) → 카오스로 충전 미소모(5:40~6:03) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘 접두 2개(6:30~6:45) → 좌측 결정화 + 신비한 합금 정신력(7:15~7:55). '
          '마무리 두 방법: 사도 레깅스 = 좌측 찬미 + 상위 찬미 + 완벽한 엑잘 → 좌측 강령술 + 보존된 갈비뼈 → 메아리 공개 방어도·에너지 보호막(7:30~8:50, 에센셜), '
          '충실한 레깅스 = 세를의 승리 → 우측 강령술 + 보존된 갈비뼈 → 메아리 공개, 빛의 징조 + 소멸로 다시 → 스킬 효과 지속시간 2티어(8:50~10:45) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘 접두 2개, 이동 속도 계열이 나와도 타협(10:50~11:40, 밸런스). '
          '회오리바람 합금(지속시간)은 정신력 대신 고를 수 있는 길로 영상에서 말만 함 — 꿀팁 후보. '
          '11-13 오후 새 정책(P11): (C) 에센셜 시작 베이스를 영상 가성비 방법의 장화인 사도 레깅스로(0850, 그래프 베이스·시뮬은 충실한 레깅스와 같은 일반 베이스라 비용 같음 — b0 상자 글과 레시피 베이스만 바꿈). '
          '빛의 징조 반복은 영상 9:35~10:45 충실한 레깅스에서 빛의 징조 + 소멸로 다시 하는 장면이 있어 밸런스에 그대로.'),
 'params': {'v': {'kr': '마무리', 'en': 'Finish', 'values': {'1': K('세를의 승리 + 접미 훼손', 'Serle’s Triumph + suffix desecration'), '2': K('접두 훼손 (가성비)', 'Prefix desecration (budget)')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('영상 가성비 마무리(사도 레깅스): 접두 훼손 한 번, 공개 결과 그대로', 'Video budget finish (Apostle Leggings): one prefix desecration, keep the reveal')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 세를의 승리 + 접미 훼손, 지속시간까지 빛의 징조로 다시', 'Video: Serle’s Triumph + suffix desecration, Omen of Light until duration')}],
 'tags': {'ele': {'gi': 20, 'tmax': 1}, 'chg': {'gi': 60, 'tmax': 2}, 'spirit': {'gi': 53}, 'dur': {'gi': 55, 'tmax': 2}, 'aes': {'gi': 8},
          'r2': {'gi': 2, 'tmax': 2}, 'r3': {'gi': 3, 'tmax': 2}, 'r4': {'gi': 4, 'tmax': 2},
          'rev': {'anyOf': ['dur', 'r2', 'r3', 'r4'], 'shown': 'dur', 'label': K('스킬 효과 지속시간·화염 저항·냉기 저항·번개 저항', 'Skill Effect Duration, Fire, Cold or Lightning Resistance')}},   # 9:30 자막: 저항을 챙겨도 되고 지속시간이 가장 좋음
 'require': {'all': [{'has': 'ele'}, {'has': 'chg'}, {'has': 'spirit'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
              {'tag': 'ele', 'tmax': 1, 'fr': True}, {'tag': 'chg', 'tmax': 2}, {'tag': 'spirit', 'ess': True}, {'tag': 'rev', 'des': True}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True, 'des': True},
              {'tag': 'ele', 'tmax': 1, 'fr': True}, {'tag': 'chg', 'tmax': 2}, {'tag': 'spirit', 'ess': True}]}],
 'finalItem': {'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='p1', start={'rar': 'rare', 'mods': ['ele', {'junk': 'p'}, {'junk': 's'}]},
  label=K('방어도의 원소 피해 적용 + 옵션 2개 레어 충실한 레깅스 구입 (특출난 베이스, 홈 2개)', 'Buy a rare Faithful Leggings: armour applies to elemental + two options (exceptional, two sockets)'),
  over=[{'param': {'v': 2}, 'set': {'label': K('방어도의 원소 피해 적용 + 옵션 2개 레어 사도 레깅스 구입 (특출난 베이스, 홈 2개)', 'Buy a rare Apostle Leggings: armour applies to elemental + two options (exceptional, two sockets)')}}],   # 2026-11-13 P11 정책 C: 영상 에센셜(가성비) 방법은 사도 레깅스(0850)
  item=[J('p'), ELEn, J('s')])
A(id='p1', kind='act', group='prep', pos=[0, 1], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')], edges=[{'to': 'pf'}],
  item=[J('p'), ELEn, J('s'), UN('s')])
A(id='pf', kind='act', group='prep', pos=[0, 2], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('방어도의 원소 피해 적용이 분열되면 성공', 'Success when armour applies to elemental fractures')],
  edges=[{'if': {'fractured': 'ele'}, 'to': 'pc', 'res': 'ok', 'label': K('원소 피해 적용 분열', 'Armour-to-elemental fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), ELE, J('s'), UN('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 2], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('다른 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 3], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('x'), ELE])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 4.4], next='u1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('x'), ELE])
A(id='u1', kind='act', group='main', pos=[0, 5.4], act='rune', rune=K('우트레드의 성좌', "Uhtred's Sidereus"), label=K('룬', 'Rune'),
  goal=K('우트레드의 성좌 장착', "Socket Uhtred's Sidereus"), showText=[K('시간술 속성 부여 가능', 'Chronomancy modifiers can roll')],
  skipIf={'rune': 'Uhtred'}, skipTo='c1', edges=[{'to': 'c1'}], item=[J('x'), ELE])
A(id='c1', kind='act', group='main', pos=[0, 6.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 충전 미소모 1~2티어', 'Charges not removed suffix, tier 1–2'), show=['chg'],
  edges=[{'if': {'has': 'chg'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[ELE, CHG])
A(id='e1', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('합금이 지울 접두 2개', 'Two prefixes for the alloy to remove from'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'a1'}], item=[J('p'), J('p'), ELE, CHG])
A(id='a1', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Mystic_Alloy', ess='spirit', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('정신력 +(10—15)', '+(10—15) to Spirit'),
  showText=[K('접두 하나가 지워지고 접미에 정신력', 'A prefix goes, Spirit lands as a suffix')], edges=[{'if': V1, 'to': 'r1'}, {'to': 'x1'}], item=[J('p'), ELE, CHG, SPI])
# 에센셜 = 사도 레깅스 마무리(7:30~8:50)
A(id='x1', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 채우기', 'Fill the prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  skipIf=V1, skipTo='r1', edges=[{'to': 'x2'}], item=[J('p'), J('p'), J('p'), ELE, CHG, SPI])
A(id='x2', kind='act', group='main', pos=[0, 10.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 하나를 훼손 옵션으로', 'Turn a prefix into a desecrated option'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  skipIf=V1, skipTo='r1', edges=[{'to': 'x3'}], item=[J('p'), J('p'), UN('p'), ELE, CHG, SPI])
A(id='x3', kind='act', group='main', pos=[0, 11.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='aes', label=K('공개', 'Reveal'),
  goal=K('접두 방어도·에너지 보호막 — 공개 결과 그대로', 'Armour and energy shield prefix: keep the reveal'), show=['aes'],
  skipIf=V1, skipTo='r1',
  edges=[{'if': {'added': 'aes'}, 'to': 'ok', 'res': 'ok'}, {'to': 'ok', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')}],
  item=[J('p'), J('p'), AES, ELE, CHG, SPI])
# 밸런스 = 충실한 레깅스 마무리(8:50~11:40)
A(id='r1', kind='act', group='main', pos=[0, 12.4], act='rune', rune=K('세를의 승리', 'Serle’s Triumph'), slots={'s': 1}, label=K('룬', 'Rune'),
  goal=K('세를의 승리 장착 (접미 +1)', 'Socket Serle’s Triumph (+1 suffix)'), showText=[K('접미 옵션 4개', 'Four suffixes')],
  skipIf={'any': [V2, {'rune': 'Serle'}]}, skipTo='ok', edges=[{'to': 'd1'}], item=[J('p'), ELE, CHG, SPI])
A(id='d1', kind='act', group='main', pos=[0, 13.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Dextral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접미 네 번째 옵션(훼손)', 'Fourth suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'd2'}],
  item=[J('p'), ELE, CHG, SPI, UN('s')])
A(id='d2', kind='act', group='main', pos=[0, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev', label=K('공개', 'Reveal'),
  goal=K('접미 스킬 효과 지속시간 — 원소 저항과 함께 먼저 뜬 것 (1~2티어)', 'Skill Effect Duration suffix: or an elemental resistance, whichever lands first (tier 1–2)'), show=['dur', 'r2', 'r3', 'r4'],
  edges=[{'if': {'added': 'rev'}, 'to': 'e2', 'res': 'ok'}, {'to': 'd2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[J('p'), ELE, CHG, SPI, DUR])
A(id='d2x', kind='act', group='main', pos=[1, 14.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='e2', kind='act', group='main', pos=[0, 15.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 채우기 — 결과 그대로', 'Fill the prefixes: keep the result'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'ok'}],
  item=[J('p'), J('p'), J('p'), ELE, CHG, SPI, DUR])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
