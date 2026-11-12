# W27 2026-11-13: MazBro 캐스터 BiS 목걸이(4PazhuHwdL8) 플로우차트 생성기 — 영상 성공 회차(첫 목걸이 Hate Heart) 한 줄
# 근거: scratchpad review/W27-mazbro-amulet/timeline.md, frames/ (영상 0:00~39:40 화면 대조)
# 실행: cd scripts/graphs && python3 gen_mazbro_caster_amulet.py  → mazbro-caster-amulet-v2.json (gen_batch14.py 끝에서 자동 호출, 그 구간을 대신함)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/mazbro-caster-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SPn = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'n', ['spirit'])
SP = L('p', '정신력 +(47—50) (분열)', '+(47—50) to Spirit (fractured)', 'f', ['spirit'])
RAR = L('p', '발견하는 아이템 희귀도 (16—19)% 증가', '(16—19)% increased Rarity of Items found', 'j', ['rp1'])
SD2 = L('p', '주문 피해 (23—26)% 증가', '(23—26)% increased Spell Damage', 'j')
MQ = L('p', '최대 퀄리티 +20% (균열의 에센스)', '+20% to Maximum Quality (Essence of the Breach)', 'c', ['mq'])
MF = L('p', '마나 최대치 +(180—189)', '+(180—189) to maximum Mana', 'n', ['mf'])
SD = L('p', '주문 피해 (27—30)% 증가', '(27—30)% increased Spell Damage', 'n', ['sd'])
SL = L('s', '모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills', 'n', ['spell'])
DEX = L('s', '민첩 +(31—33) (훼손, 자리 막기)', '+(31—33) to Dexterity (desecrated, blocker)', 'd', ['blk'])
CS = L('s', '시전 속도 (25—28)% 증가', '(25—28)% increased Cast Speed', 'n', ['cs'])
KQ = L('s', '모든 스킬의 퀄리티 +(3—5)%', '+(3—5)% to Quality of all Skills', 'd', ['kq'])
J = lambda s='x': L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

GP = K('마나 최대치·최대 마나 %·주문 피해', 'maximum Mana, % maximum Mana or Spell Damage')
GS = K('시전 속도·치명타 확률·치명타 피해', 'Cast Speed, Critical Hit Chance or Critical Damage')

g = {
 'id': 'mazbro-caster-amulet-v2', 'recipe': 'mazbro-caster-amulet-v2', 'cls': 'Amulets', 'base': 'Solar Amulet', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 5},
 'note': ('2026-11-13 W27 영상 전체 화면 대조(0:00~39:40). 성공 회차 = 영상 가이드(화면 메모 1~11단계)를 따라간 첫 목걸이 Hate Heart: '
          '정신력 50 태양 목걸이(아이템 레벨 82, 옵션 3~4개) 구입·보존된 빗장뼈로 4개 → 분열(3개 중 1개 성공, 4:40~5:00) → 소멸로 분열 + 옵션 1개(5:10) → '
          '카오스로 접두 희귀도 1티어, 우측 찬미 + 상위 엑잘로 접미 주문 +3(영상 6:25·11:30 설명, 미리 만든 목걸이) → 좌측 찬미 + 상위 엑잘(주문 피해 2티어) → '
          '좌측 결정화 + 균열의 에센스(희귀도가 지워짐, 13:15) → 우측 강령술 + 보존된 빗장뼈 → 메아리 공개 민첩(자리 막기, 14:33) → 달리는 기폭제 40% → '
          '촉진 + 우측 찬미 + 완벽한 엑잘(마나 재생 1티어, 영상은 개인용으로 받음 16:43) → 신경 기폭제 40%(19:35) → 좌측 소멸의 징조(최대 퀄리티가 지워짐, 20:08) → '
          '좌측 결정화 + 균열의 에센스(주문 피해 2티어를 지움) → 촉진 + 완벽한 엑잘(마나 최대치 1티어, 20:30) → 쇳소리 기폭제 40%(24:18) → '
          '절사 + 완벽한 카오스 반복, 필요할 때 좌측 말소(25:40)로 주문 피해 1티어(26:38) → 빛의 징조 + 소멸(민첩) → 검은 피 + 고대 빗장뼈 → 메아리 공개 반복 → 모든 스킬의 퀄리티(28:05). '
          '신성한 오브·축복받은 자의 징조(28:15~29:00)는 정책 14장대로 뺌. 두 번째 목걸이(29:00~38:40)는 같은 방법, 접미는 희귀도 1티어로 타협(33:40) — 꿀팁 후보.'),
 'params': {
   'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video'), '2': K('결과 그대로', 'As it comes')}},
   'pT': {'kr': '시전 속도·마나 등', 'en': 'Cast speed, mana etc.', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'v': 1, 'pT': 1}}, {'id': 'bal', 'params': {'v': 2, 'pT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 2, 'pT': 2}, 'tier': 'bal',
    'desc': K('촉진 엑잘 1~2티어, 절사 카오스 한 번(랜덤 옵션), 쿠르갈 공개 결과 그대로', 'Catalysed exalts at T1–2, one Whittling chaos (random option), Kurgal reveal kept')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'v': 1, 'pT': 1}, 'tier': 'high',
    'desc': K('영상: 촉진 엑잘·절사 카오스 1티어, 쿠르갈 공개는 빛의 징조로 다시', 'Video: T1 catalysed exalts and Whittling chaos, Light retries the Kurgal reveal')}],
 'tags': {
   'spirit': {'gi': 28, 'tmax': 1}, 'spell': {'gi': 17, 'tmax': 1}, 'mq': {'gi': 81},
   'cs': {'gi': 32, 'tmax': '$pT'}, 'cr': {'gi': 24, 'tmax': '$pT'}, 'cd': {'gi': 25, 'tmax': '$pT'},
   'gs': {'anyOf': ['cs', 'cr', 'cd'], 'label': GS},
   'mp': {'gi': 12, 'tmax': '$pT'}, 'mf': {'gi': 11, 'tmax': '$pT'}, 'sd': {'gi': 31, 'tmax': '$pT'},
   'gp': {'anyOf': ['mp', 'mf', 'sd'], 'label': GP},
   'keep': {'anyOf': ['gp']},
   # 촉진 대상(기폭제 태그): 달리는 기폭제 = 속도(시전 속도만), 신경 기폭제 = 마나(마나 최대치·최대 마나 %) — 티어 제한 없음(완벽한 엑잘 최소 레벨)
   'csCat': {'gi': 32}, 'mfCat': {'gi': 11}, 'mpCat': {'gi': 12}, 'manaCat': {'anyOf': ['mfCat', 'mpCat']},
   # 카오스 단계에서 반대쪽 엑잘을 시도할 접두 1티어(영상 2단계 메모 + 성공 회차의 희귀도 1티어)
   'mp1': {'gi': 12, 'tmax': 1}, 'mf1': {'gi': 11, 'tmax': 1}, 'sd1': {'gi': 31, 'tmax': 1}, 'rp1': {'gi': 27, 'tmax': 1},
   'anc': {'anyOf': ['mp1', 'mf1', 'sd1', 'rp1'], 'label': K('최대 마나 %·마나 최대치·주문 피해·희귀도 1티어', 'T1 % maximum Mana, maximum Mana, Spell Damage or Rarity')},
   # 자리 막기(영상 5단계 메모: 생명력 재생 > 힘·지능·민첩·화염·냉기·번개 저항 > 모든 능력치)
   'blk': {'anyOf': [{'gi': 21}, {'gi': 0}, {'gi': 1}, {'gi': 2}, {'gi': 4}, {'gi': 5}, {'gi': 6}, {'gi': 3}],
           'label': K('생명력 재생·힘·민첩·지능·화염·냉기·번개 저항·모든 능력치', 'Life regeneration, Str, Dex, Int, fire, cold or lightning res, all Attributes')},
   'kq': {'gi': 46}},
 'require': {'all': [{'has': 'spell'}, {'has': 'gs'}, {'has': 'gp'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'a1',
 'finals': [
   {'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
    'lines': [{'tag': 'spirit', 'fr': True}, {'tag': 'gp'}, {'tag': 'gp'}, {'tag': 'spell'}, {'tag': 'gs'}, {'tag': 'kq', 'des': True}]},
   {'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'spirit', 'fr': True}, {'tag': 'gp'}, {'side': 'p', 'random': True}, {'tag': 'spell'}, {'tag': 'gs'}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
V1 = {'param': {'v': 1}}

# 접미 두 자리 구간(영상 5·6·6B단계): 단계마다 아이템 상태를 다시 봄. vis = 그릴 선
def R1(vis):
    out = []
    for e in [{'if': {'not': {'has': 'spell'}}, 'to': 'cz'},
              {'if': {'not': {'has': 'mq'}}, 'to': 'a10e'},
              {'if': {'unrevSide': 's'}, 'to': 'a8'},
              {'if': {'all': [{'des': False}, {'sideLt': {'side': 's', 'n': 3}}]}, 'to': 'a7'},
              {'if': {'all': [{'has': 'gs'}, {'des': True}]}, 'to': 'a11'},
              {'if': {'full': 's'}, 'to': 'a10x'},
              {'to': 'a9'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# ---------------- 베이스템 완성 ----------------
A(id='a1', kind='base', group='prep', pos=[0, 0], next='a2', start={'rar': 'rare', 'mods': [{'tag': 'spirit'}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('태양 목걸이 구입 (아이템 레벨 82, 정신력 +50, 옵션 3개)', 'Buy a Solar Amulet (item level 82, +50 Spirit, three options)'),
  item=[SPn, J('p'), J('s')])
A(id='a2', kind='act', group='prep', pos=[0, 1], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')],
  edges=[{'to': 'a3'}], item=[SPn, J('p'), J('s'), UN('x')])
A(id='a3', kind='act', group='prep', pos=[0, 2], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('정신력이 분열되면 성공', 'Success when Spirit fractures')],
  edges=[{'if': {'fractured': 'spirit'}, 'to': 'pc', 'res': 'ok', 'label': K('정신력 분열', 'Spirit fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[SP, J('p'), J('s'), UN('x')])
A(id='xj', kind='exit', group='prep', pos=[1, 2], simTo='a1', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 3], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[SP, J('x')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 4.4], next='a4', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, J('x')])
A(id='cz', kind='cleanup', group='main', pos=[1, 4.9], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'a4'}])
# 2단계: 카오스 스팸 + 반대쪽 엑잘(접힌 상자 L0)
A(id='a4', kind='act', group='main', pos=[0, 5.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills suffix'), show=['spell'],
  edges=[{'if': {'has': 'spell'}, 'to': 'a5', 'res': 'ok'}, {'if': {'has': 'anc'}, 'to': 'c2', 'res': 'ok'}, {'to': 'a4', 'res': 'fail', 'hide': True}],
  item=[SP, RAR, SL])
A(id='c2', kind='act', group='main', pos=[1, 5.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 1티어를 두고 접미 모든 주문 스킬 레벨 +3', 'Keep the T1 prefix, +3 Spell Skills suffix'), show=['spell'],
  edges=[{'if': {'added': 'spell'}, 'to': 'a5', 'res': 'ok'}, {'to': 'c3', 'res': 'fail'}])
A(id='c3', kind='act', group='main', pos=[1, 6.4], act='chaos', cur='Greater_Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('빗나간 접미 다시', 'Reroll the missed suffix'), show=['spell'],
  edges=[{'if': {'has': 'spell'}, 'to': 'a5', 'res': 'ok'}, {'if': {'has': 'anc'}, 'to': 'c3', 'res': 'fail', 'hide': True}, {'to': 'c4', 'res': 'fail'}])
A(id='c4', kind='act', group='main', pos=[1, 7.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('접두 1티어가 지워지면 옵션 1개 남기기', 'T1 prefix gone: back to one option'), edges=[{'to': 'a4'}])
# 3·4단계
A(id='a5', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세번째 옵션', 'Third prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  skipIf={'full': 'p'}, skipTo='a6', edges=[{'to': 'a6'}], item=[SP, RAR, SD2, SL])
A(id='a6', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 하나를 지우고 최대 퀄리티', 'A prefix goes for max quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}],
  edges=[{'to': 'a7'}], item=[SP, SD2, MQ, SL])
# 5·6·6B단계: 자리 막기 + 촉진 엑잘(접힌 상자 L1)
A(id='a7', kind='act', group='main', pos=[0, 8.4], act='desecrate', cur='Preserved_Collarbone', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 두번째 옵션(훼손)', 'Second suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=R1({'a8': {}}), item=[SP, SD2, MQ, SL, UN('s')])
A(id='a8', kind='act', group='main', pos=[1, 8.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='blk', label=K('공개', 'Reveal'),
  goal=K('자리 막기 옵션 — 생명력 재생·능력치·저항', 'Blocker: life regeneration, attribute or resistance'), show=['blk'],
  edges=[{'if': {'not': {'added': 'blk'}}, 'to': 'a8x', 'res': 'fail', 'label': K('빗나감', 'Miss')}] + R1({'a9': {'res': 'ok'}}))
A(id='a8x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'a7', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='a9', kind='act', group='main', pos=[1, 10.4], act='quality', cur='Skittering_Catalyst', count=40, label=K('퀄리티', 'Quality'),
  goal=K('속도 퀄리티 40%', 'Speed quality 40%'), edges=[{'to': 'a10'}])
A(id='a10', kind='act', group='main', pos=[1, 11.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation', 'Omen_of_Dextral_Exaltation'],
  cat='csCat', label=K('엑잘', 'Exalt'), goal=K('접미 세번째 옵션', 'Third suffix'), show=['cs', 'cr', 'cd'],
  edges=[{'if': {'added': 'gs'}, 'to': 'a11', 'res': 'ok'}, {'to': 'a10x', 'res': 'fail', 'label': K('빗나감', 'Miss')}])
A(id='a10x', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접미 지우기', 'Remove the missed suffix'),
  edges=R1({'a9': {'res': 'ok'}, 'cz': {'res': 'fail'}, 'a10e': {'res': 'fail'}, 'a7': {'res': 'fail'}}))
A(id='a10e', kind='act', group='main', pos=[1, 13.4], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 하나를 지우고 최대 퀄리티', 'A prefix goes for max quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=R1({'a9': {}}))
# 7·7B단계: 접두 촉진 엑잘(접힌 상자 L2)
A(id='a11', kind='act', group='main', pos=[0, 9.4], act='quality', cur='Neural_Catalyst', count=40, label=K('퀄리티', 'Quality'),
  goal=K('마나 퀄리티 40%', 'Mana quality 40%'), edges=[{'to': 'a11x'}], item=[SP, MF, MQ, SL, DEX, CS])
A(id='a11x', kind='act', group='main', pos=[2, 9.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=ANN, goal=ANN,
  target=K('잡옵 접두 지우기', 'Remove the junk prefix'), skipIf={'sideLt': {'side': 'p', 'n': 3}}, skipTo='a12',
  edges=[{'if': {'has': 'mq'}, 'to': 'a12', 'res': 'ok'}, {'to': 'a11e', 'res': 'fail', 'label': K('최대 퀄리티가 지워짐', 'Max quality gone')}])
A(id='a11e', kind='act', group='main', pos=[2, 10.4], act='essence', cur='Essence_of_the_Breach', ess='mq', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 하나를 지우고 최대 퀄리티', 'A prefix goes for max quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'a12'}])
A(id='a12', kind='act', group='main', pos=[2, 11.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Catalysing_Exaltation'], cat='manaCat',
  label=K('엑잘', 'Exalt'), goal=K('접두 두번째 옵션', 'Second prefix'), show=['mp', 'mf', 'sd'],
  edges=[{'if': {'added': 'gp'}, 'to': 'a13', 'res': 'ok'}, {'to': 'a11', 'res': 'fail', 'label': K('빗나감', 'Miss')}])
# 8·10단계
A(id='a13', kind='act', group='main', pos=[0, 10.4], act='quality', cur='Sibilant_Catalyst', count=40, label=K('퀄리티', 'Quality'),
  goal=K('시전 퀄리티 40%', 'Caster quality 40%'), edges=[{'to': 'a14'}], item=[SP, MF, MQ, SL, DEX, CS])
A(id='a14', kind='act', group='main', pos=[0, 11.4], act='chaos', cur='Perfect_Chaos_Orb', trim={'side': 'p', 'keep': 'keep'}, label=K('카오스', 'Chaos'),
  goal=K('최대 퀄리티를 지우고 접두 세번째 옵션', 'Max quality out, third prefix'), show=['mp', 'mf', 'sd'],
  edges=[{'if': {'count': {'tag': 'gp', 'min': 2}}, 'to': 'a15', 'res': 'ok'},
         {'if': {'param': {'v': 2}}, 'to': 'a15', 'res': 'fail', 'hide': True},
         {'to': 'a14', 'res': 'fail'}], item=[SP, MF, SD, SL, DEX, CS])
# 11단계: 쿠르갈
A(id='a15', kind='act', group='main', pos=[0, 12.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecration'), edges=[{'to': 'a16'}], item=[SP, MF, SD, SL, CS])
A(id='a16', kind='act', group='main', pos=[0, 13.4], act='desecrate', cur='Ancient_Collarbone', omens=['Omen_of_the_Blackblooded'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세번째 옵션(훼손)', 'Third suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'a17'}], item=[SP, MF, SD, SL, CS, UN('s')])
A(id='a17', kind='act', group='main', pos=[0, 14.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='kq', label=K('공개', 'Reveal'),
  goal=K('접미 모든 스킬의 퀄리티', 'Quality of all Skills suffix'), show=['kq'],
  edges=[{'if': {'added': 'kq'}, 'to': 'ok', 'res': 'ok'}, {'if': V1, 'to': 'a17x', 'res': 'fail'}, {'to': 'ok', 'res': 'fail', 'hide': True}],
  item=[SP, MF, SD, SL, CS, KQ])
A(id='a17x', kind='act', group='main', pos=[1, 14.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'a16', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L0', 'nodes': ['a4', 'c2', 'c3', 'c4'], 'kr': '카오스 스팸', 'en': 'Chaos spam', 'fold': True,
  'goal': K('접미 모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills suffix'),
  'steps': [K('카오스 오브로 모든 주문 스킬 레벨 +3', 'Chaos Orb for +3 Spell Skills') | {'node': 'a4'},
            K('접두에 최대 마나 %·마나 최대치·주문 피해·희귀도 1티어가 뜨면 우측 찬미 + 상위 엑잘로 접미 +3', 'A T1 % mana, flat mana, spell damage or rarity prefix: Dextral Exaltation + Greater Exalt for the +3 suffix') | {'node': 'c2'},
            K('빗나가면 상위 카오스 오브, 접두 1티어가 남아 있으면 다시', 'A miss: Greater Chaos Orb, again while the T1 prefix stays') | {'node': 'c3'},
            K('접두 1티어가 지워지면 소멸의 오브로 옵션 1개 남기고 카오스부터', 'T1 prefix gone: Orb of Annulment down to one option, then Chaos again') | {'node': 'c4'}],
  'item': [SP, RAR, SL]},
 {'id': 'L1', 'nodes': ['a7', 'a8', 'a8x', 'a9', 'a10', 'a10x', 'a10e'], 'kr': '접미 두 자리', 'en': 'Two suffixes', 'fold': True,
  'goal': K('자리 막기 훼손 + 접미 시전 속도·치명타 확률·치명타 피해 1티어 중 먼저 뜬 것', 'Desecrated blocker + whichever T1 cast speed, crit chance or crit damage suffix lands first'),
  'goalBy': {'high': K('자리 막기 훼손 + 접미 시전 속도·치명타 확률·치명타 피해 1티어 중 먼저 뜬 것', 'Desecrated blocker + whichever T1 cast speed, crit chance or crit damage suffix lands first'),
             'bal': K('자리 막기 훼손 + 접미 시전 속도·치명타 확률·치명타 피해 1~2티어 중 먼저 뜬 것', 'Desecrated blocker + whichever T1–2 cast speed, crit chance or crit damage suffix lands first')},
  'steps': [K('우측 강령술의 징조 + 보존된 빗장뼈로 접미 훼손', 'Omen of Dextral Necromancy + Preserved Collarbone on a suffix') | {'node': 'a7'},
            K('심연의 메아리 공개 — 생명력 재생·능력치·저항으로 자리 막기, 하나도 없으면 빛의 징조 + 소멸의 오브로 다시', 'Reveal with Abyssal Echoes: life regen, attribute or resistance blocks; none of them, Omen of Light + Annulment and again') | {'node': 'a8'},
            K('달리는 기폭제로 속도 퀄리티 40%', 'Skittering Catalyst to 40% speed quality') | {'node': 'a9'},
            K('촉진하는 찬미 + 우측 찬미 + 완벽한 엑잘티드 오브', 'Catalysing + Dextral Exaltation + Perfect Exalted Orb') | {'node': 'a10'},
            K('빗나가면 소멸의 오브, 자리 막기가 지워지면 훼손부터', 'A miss: Orb of Annulment; blocker gone, desecrate again') | {'node': 'a10x'},
            K('최대 퀄리티가 지워지면 좌측 결정화 + 균열의 에센스', 'Max quality gone: Sinistral Crystallisation + Essence of the Breach') | {'node': 'a10e'}],
  'worst': {'kr': '모든 주문 스킬 레벨 +3이 지워지면 카오스 스팸부터', 'en': '+3 Spell Skills gone: back to the chaos spam', 'to': 'cz'},
  'item': [SP, SD2, MQ, SL, DEX, CS]},
 {'id': 'L2', 'nodes': ['a11', 'a11x', 'a11e', 'a12'], 'kr': '접두 촉진 엑잘', 'en': 'Catalysed prefix', 'fold': True,
  'goal': K('접두 마나 최대치·최대 마나 %·주문 피해 1티어 중 먼저 뜬 것', 'Whichever T1 flat mana, % mana or spell damage prefix lands first'),
  'goalBy': {'high': K('접두 마나 최대치·최대 마나 %·주문 피해 1티어 중 먼저 뜬 것', 'Whichever T1 flat mana, % mana or spell damage prefix lands first'),
             'bal': K('접두 마나 최대치·최대 마나 %·주문 피해 1~2티어 중 먼저 뜬 것', 'Whichever T1–2 flat mana, % mana or spell damage prefix lands first')},
  'steps': [K('신경 기폭제로 마나 퀄리티 40%', 'Neural Catalyst to 40% mana quality') | {'node': 'a11'},
            K('좌측 소멸의 징조 + 소멸의 오브로 잡옵 접두 지우기', 'Omen of Sinistral Annulment + Annulment on the junk prefix') | {'node': 'a11x'},
            K('최대 퀄리티가 지워지면 좌측 결정화 + 균열의 에센스', 'Max quality gone: Sinistral Crystallisation + Essence of the Breach') | {'node': 'a11e'},
            K('촉진하는 찬미 + 완벽한 엑잘티드 오브, 빗나가면 기폭제부터 다시', 'Catalysing Exaltation + Perfect Exalted Orb; a miss goes back to the catalyst') | {'node': 'a12'}],
  'item': [SP, MF, MQ, SL, DEX, CS]},
 {'id': 'L3', 'nodes': ['a16', 'a17', 'a17x'], 'kr': '쿠르갈 공개', 'en': 'Kurgal reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
