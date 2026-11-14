# RECIPE-B 2026-11-14: SaVeQ ES·마나 장화(youtu.be/5ngxdC6xY6Q, 2026-09-18, 0.5.5) — 조사 g89(docs/craft-guides.md 5차)
# 영상 흐름 한 줄(접미 저항 분열 켤레): 호화로운 슬리퍼 → 완벽한 진화·확장 + 소멸로 저항 1티어 매직 → 완벽한 제왕 → 좌측 강령술 + 보존된 갈비뼈 → 분열(저항)
#   → 소멸로 분열만 남김 → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘(마나·에너지 보호막) 반복 → 좌측 강령술 + 고대 갈비뼈 + 메아리 + 빛 반복(이동 속도 35%)
#   → 아스트리드의 창의성 → 상위 찬미 + 엑잘로 접미 잡옵 2개 → 경악의 에센스·신비한 합금 → (선택) 축성
# 실행: cd scripts/graphs && python3 gen_saveq_es_mana_boots.py  → saveq-es-mana-boots-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-es-mana-boots-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
CLS = 'Boots_int'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, ti=0, m='n', tags=None, sfx=None):   # 클래스 파일 티어 글 그대로
    g = D['groups'][gi]; t = g['t'][ti]; kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if sfx: kr, en = kr + ' (' + sfx[0] + ')', en + ' (' + sfx[1] + ')'
    return L(g['g'], kr, en, m, tags)

LRn = T(3, 0, 'n', ['res1'])
LR = T(3, 0, 'f', ['res1'], ('분열', 'fractured'))
MN = T(6, 1, 'n', ['mnT'])
ES = T(8, 0, 'n', ['es8'])
MS = T(12, 0, 'd', ['msT'])
HOR = T(46, 0, 'c', ['hor'], ('경악의 에센스', 'Essence of Horror'))
MYS = T(51, 0, 'c', ['mys'], ('신비한 합금', 'Mystic Alloy'))
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
AS = L('r', '아스트리드의 창의성', "Astrid's Creativity", 'r')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'saveq-es-mana-boots-v2', 'recipe': 'saveq-es-mana-boots-v2', 'cls': CLS, 'base': 'Luxurious Slippers', 'ilvl': 82,
 'note': ('2026-11-14 RECIPE-B: SaVeQ ES·마나 장화(youtu.be/5ngxdC6xY6Q, 조사 g89 — docs/craft-guides.md 5차). 영상은 켤레 5개를 같은 방법으로 만들고 켤레마다 분열 옵션이 다름. '
          '플로우차트는 완성품 화면의 켤레(접미 번개 저항 분열) 한 줄: 2:03 호화로운 슬리퍼(약 1 div, 세케마 샌들은 15~35 div라 비추천) → 완벽한 진화 + 완벽한 확장 + 소멸 반복으로 저항 1티어 매직 → '
          '4:40 완벽한 제왕(에센스는 안 씀) → 5:11 좌측 강령술의 징조 + 보존된 갈비뼈(미공개 접두, 분열되지 않음) → 분열의 오브 → 저항 분열 → 소멸로 분열만 남김 → '
          '6:15 좌측 찬미 + 상위 찬미의 징조 + 완벽한 엑잘티드 오브(카오스 대신)로 접두 2개, 빗나가면 소멸로 분열만 남기고 다시 → 마나 최대치 2티어 + 에너지 보호막 증가 1티어 → '
          '8:18 좌측 강령술 + 고대 갈비뼈 + 심연의 메아리 → 이동 속도 35%, 빗나가면 빛의 징조로 다시(15:29 30%·25%를 넘기고 다섯 번째) → '
          '8:48 아스트리드의 창의성 → 상위 찬미 + 엑잘티드 오브로 접미 잡옵 2개(접두가 꽉 차서 결정화 필요 없음) → 경악의 에센스·신비한 합금으로 둘을 바꿈(접미가 꽉 차 있어 그쪽 옵션이 지워짐, 경악 옵션이 지워지면 다시) → 22:15 축성(선택). '
          '내부 결정: 분열이 저항이 아니면 새 베이스(영상은 다른 분열 켤레도 다른 완성품으로 이어 감 — 이 플로우차트는 저항 분열 켤레만 따름), '
          '분열 준비의 미공개 훼손은 공개하지 않고 소멸로 분열만 남김(영상 "공개에서 마나·에너지 보호막이 안 나오면 소멸로 분열만 남기고"의 빗나간 경우), 매직 단계는 저항 1티어만 맞추고 접두는 나오는 대로. '
          '축성은 시뮬에 규칙이 없어 선택 단계(비용 미포함). 신성한 오브·완벽한 철 룬·퀄리티는 정책 9·14장대로 뺌.'),
 'params': {'mT': {'kr': '접두 마나 최대치', 'en': 'Maximum mana prefix', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}},
            'eT': {'kr': '접두 에너지 보호막', 'en': 'Energy shield prefix', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}},
            'sT': {'kr': '이동 속도(훼손)', 'en': 'Movement speed (desecrated)', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('나오는 대로', 'As it comes')}},
            'v': {'kr': '공개가 빗나가면', 'en': 'Reveal miss', 'values': {'1': K('빛의 징조로 다시', 'Retry with Light'), '0': K('결과 그대로', 'Keep it')}}},
 'strategies': [{'id': 'bal', 'params': {'mT': 2, 'eT': 2, 'sT': 2, 'v': 1}}, {'id': 'ess', 'params': {'mT': 4, 'eT': 4, 'sT': 4, 'v': 0}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'mT': 2, 'eT': 2, 'sT': 2, 'v': 1}, 'tier': 'bal',
   'desc': K('영상 흐름: 마나 최대치·에너지 보호막·이동 속도 1~2티어, 빛의 징조로 다시 공개', 'Video flow: T1–2 maximum mana, energy shield and movement speed, reveal retried with Light')},
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'mT': 4, 'eT': 4, 'sT': 4, 'v': 0}, 'tier': 'ess',
   'desc': K('마나 최대치·에너지 보호막 1~4티어, 훼손 공개 결과 그대로', 'T1–4 maximum mana and energy shield, reveal kept as it comes')}],
 'tags': {
  'fr1': {'gi': 1, 'tmax': 1}, 'cr1': {'gi': 2, 'tmax': 1}, 'lr1': {'gi': 3, 'tmax': 1},
  'res1': {'anyOf': ['fr1', 'cr1', 'lr1'], 'shown': 'lr1', 'label': K('화염·냉기·번개 저항 1티어', 'T1 fire, cold or lightning resistance')},
  'mnT': {'gi': 6, 'tmax': '$mT'},
  'es8': {'gi': 8, 'tmax': '$eT'}, 'es7': {'gi': 7, 'tmax': '$eT'}, 'es9': {'gi': 9, 'tmax': '$eT'},
  'esT': {'anyOf': ['es8', 'es7', 'es9'], 'shown': 'es8', 'label': K('에너지 보호막 증가·최대치·복합', 'Increased, maximum or hybrid energy shield')},
  'msT': {'gi': 12, 'tmax': '$sT'},
  'hor': {'gi': 46}, 'mys': {'gi': 51}},
 'conds': {'preOk': {'all': [{'has': 'mnT'}, {'has': 'esT'}]}, 'magOk': {'all': [{'has': 'res1'}, {'full': 'p'}]}},
 'require': {'all': [{'has': 'res1'}, {'ref': 'preOk'}, {'any': [{'param': {'v': 0}}, {'has': 'msT'}]}, {'has': 'hor'}, {'has': 'mys'}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'basePrice': {'Divine_Orb': 1},
 'finalItem': {'quality': 20, 'sockets': 1},
}
N = []
A = lambda **kw: N.append(kw)

# 매직 단계 길잡이: 접미 저항 1티어 + 접두 하나가 되면 제왕, 저항이 있으면 확장, 저항이 아닌 접미가 있으면 소멸
def MG(vis):
    out = []
    for e in [{'if': {'ref': 'magOk'}, 'to': 'r1'}, {'if': {'has': 'res1'}, 'to': 'a1'},
              {'if': {'full': 's'}, 'to': 'ax'}, {'to': 'a1'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# ---------------- 베이스템 완성 (2:03~6:15) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='t1', start={'rar': 'normal', 'mods': []},
  label=K('호화로운 슬리퍼 구입 (노멀, 아이템 레벨 82)', 'Buy Luxurious Slippers (normal, item level 82)'), item=[])
A(id='t1', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 — 접미 저항 1티어 노림', 'Magic: aiming for a T1 resistance suffix'), show=['fr1', 'cr1', 'lr1'], edges=MG({'a1': {}}), item=[LRn])
A(id='a1', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접미 번개 저항 1티어 — 화염·냉기·번개 저항 1티어 중 먼저 뜬 것', 'T1 lightning resistance suffix: whichever T1 resistance lands first'), show=['fr1', 'cr1', 'lr1'],
  edges=MG({'r1': {'res': 'ok'}, 'ax': {'res': 'fail', 'label': K('저항이 아닌 접미', 'A non-resistance suffix')}}), item=[J('p'), LRn])
A(id='ax', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', label=ANN, goal=ANN,
  target=K('옵션 1개 제거', 'Remove one option'), edges=MG({'a1': {'label': K('다시 확장', 'Augment again')}}))
A(id='r1', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'd0'}], item=[J('p'), LRn, J('s')])
A(id='d0', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f0'}], item=[J('p'), UN('p'), LRn, J('s')])
A(id='f0', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'), showText=[K('저항 1티어가 분열되면 성공', 'Success when the T1 resistance fractures')],
  edges=[{'if': {'fractured': 'res1'}, 'to': 'ms', 'res': 'ok', 'label': K('저항 분열', 'Resistance fractured')},
         {'to': 'xf', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}], item=[J('p'), UN('p'), LR, J('s')])
A(id='xf', kind='exit', group='prep', pos=[1, 5], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('저항이 아닌 옵션이 분열되면 이 플로우차트에서는 새 베이스로 처음부터(영상은 다른 완성품으로 이어 감)', 'Another option fractured: this chart starts over on a new base (the video carries it on as a different item)'))
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 6.4], next='cl', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), UN('p'), LR, J('s')])
A(id='cl', kind='cleanup', group='main', pos=[0, 7.4], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('분열만 남기기', 'Keep only the fracture'), edges=[{'to': 'p1'}], item=[LR])
A(id='p1', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 옵션 2개 — 마나 최대치 2티어 + 에너지 보호막 증가 1티어', 'Two prefixes: T2 maximum mana + T1 increased energy shield'),
  goalBy={'bal': K('접두 옵션 2개 — 마나 최대치 1~2티어 + 에너지 보호막 1~2티어', 'Two prefixes: T1–2 maximum mana + T1–2 energy shield'),
          'ess': K('접두 옵션 2개 — 마나 최대치 1~4티어 + 에너지 보호막 1~4티어', 'Two prefixes: T1–4 maximum mana + T1–4 energy shield')},
  show=['mnT', 'esT'],
  edges=[{'if': {'ref': 'preOk'}, 'to': 'd1', 'res': 'ok'}, {'to': 'p1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[MN, ES, LR])
A(id='p1x', kind='cleanup', group='main', pos=[1, 8.4], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('분열만 남기기', 'Keep only the fracture'), edges=[{'to': 'p1', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='d1', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=[MN, ES, UN('p'), LR])
A(id='d2', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='msT', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 이동 속도 35%', 'Third prefix (desecrated): 35% movement speed'),
  goalBy={'bal': K('접두 세 번째 옵션(훼손) — 이동 속도 1~2티어 (영상: 35%)', 'Third prefix (desecrated): T1–2 movement speed (video: 35%)'),
          'ess': K('접두 세 번째 옵션(훼손) — 나오는 대로 (영상: 이동 속도 35%)', 'Third prefix (desecrated): keep what comes (video: 35% movement speed)')},
  show=['msT'],
  edges=[{'if': {'added': 'msT'}, 'to': 'rn', 'res': 'ok'}, {'if': {'param': {'v': 0}}, 'to': 'rn', 'res': 'fail', 'hide': True},
         {'to': 'd2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[MN, ES, MS, LR])
A(id='d2x', kind='act', group='main', pos=[1, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='rn', kind='act', group='main', pos=[0, 11.4], act='rune', rune={'kr': '아스트리드의 창의성', 'en': "Astrid's Creativity"}, label=K('룬', 'Rune'),
  goal=K('아스트리드의 창의성 장착', "Socket Astrid's Creativity"), showText=[K('제작 옵션 2개까지', 'Up to two crafted options')],
  edges=[{'to': 's1'}], item=[MN, ES, MS, LR, AS])
A(id='s1', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵 2개 — 에센스·합금이 바꿀 자리', 'Two junk suffixes for the essence and alloy to replace'), showText=[K('잡옵 2개', 'Two junk options')],
  edges=[{'to': 's2'}], item=[MN, ES, MS, LR, J('s'), J('s'), AS])
# 경악의 에센스·신비한 합금: 접미가 꽉 차 있어 그쪽 옵션 하나(분열 제외)가 지워짐 — 경악 옵션이 지워지면 다시 (영상 8:48~)
def CR(vis):
    out = []
    for e in [{'if': {'all': [{'has': 'hor'}, {'has': 'mys'}]}, 'to': 'ok'}, {'if': {'not': {'has': 'hor'}}, 'to': 's2'}, {'to': 's3'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out
A(id='s2', kind='act', group='main', pos=[0, 13.4], act='essence', cur='Essence_of_Horror', ess='hor', label=K('에센스', 'Essence'),
  goal=K('접미 장착된 증강물 아이템의 효과 60% — 잡옵 하나가 지워짐', 'Suffix 60% socketed augment effect: a junk suffix goes'),
  showText=[{'s': 's', 'kr': '장착된 증강물 아이템의 효과 60% 증가 (제작 옵션)', 'en': '60% increased effect of Socketed Augment Items (crafted)'}],
  edges=CR({'s3': {'res': 'ok'}, 'ok': {'res': 'ok'}}), item=[MN, ES, MS, LR, HOR, J('s'), AS])
A(id='s3', kind='act', group='main', pos=[0, 14.4], act='essence', cur='Mystic_Alloy', ess='mys', label=K('합금', 'Alloy'),
  goal=K('접미 정신력 — 남은 잡옵을 바꿈', 'Suffix Spirit: replace the last junk'),
  showText=[{'s': 's', 'kr': '정신력 +(10—15) (제작 옵션)', 'en': '+(10—15) to Spirit (crafted)'}],
  edges=CR({'ok': {'res': 'ok'}, 's2': {'res': 'fail', 'label': K('경악 옵션이 지워짐', 'Horror line removed')}}), item=[MN, ES, MS, LR, HOR, MYS, AS])
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
A(id='sx', kind='side', group='main', pos=[1, 15.4], attach=['ok', 'ok'], cur='Divine_Orb', omens=['Omen_of_Sanctification'],
  goal=K('축성으로 수치 올리기, 선택·비용 미포함', 'Sanctify for higher values, optional, not costed'), label=K('축성', 'Sanctify'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L0', 'nodes': ['t1', 'a1', 'ax'], 'kr': '매직 저항', 'en': 'Magic resistance'},
 {'id': 'L1', 'nodes': ['p1', 'p1x'], 'kr': '접두 2개', 'en': 'Two prefixes'},
 {'id': 'L2', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '이동 속도 공개', 'en': 'Movement speed reveal'},
 {'id': 'L3', 'nodes': ['s2', 's3'], 'kr': '제작 옵션 2개', 'en': 'Two crafted options'},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'mnT'}, {'tag': 'esT'}, {'tag': 'msT', 'des': True}, {'tag': 'res1', 'fr': True}, {'tag': 'hor', 'ess': True}, {'tag': 'mys', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'mnT'}, {'tag': 'esT'}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'res1', 'fr': True}, {'tag': 'hor', 'ess': True}, {'tag': 'mys', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
