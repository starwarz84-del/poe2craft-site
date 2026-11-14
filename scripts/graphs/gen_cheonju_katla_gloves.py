# RECIPE-B 2026-11-14: 천주 화염파 젬링 장갑(youtu.be/UwlQO3Qf6ZI, 2026-09-28, 0.5.5) — 조사 g83(docs/craft-guides.md 5차)
# 영상 흐름 한 줄: 특출난 고정된 싸개 → 카틀라의 순흑 → 완벽한 진화·확장·제왕 → 카오스 반복(카틀라 접두 1티어) → 좌측 강령술 + 보존된 갈비뼈 → 분열
#   → 소멸로 분열만 남김 → 카오스 반복(둘째 카틀라 접두) → 좌측 강령술 + 보존된 갈비뼈 + 메아리 + 빛 반복(점화 강도)
#   → 상위 찬미 + 완벽한 엑잘(접미 2개) → 아스트리드의 창의성 → 우측 결정화 + 경악의 에센스·신비한 합금 → 완벽한 엑잘 + 우측 소멸 반복(저항)
# 실행: cd scripts/graphs && python3 gen_cheonju_katla_gloves.py  → cheonju-katla-gloves-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/cheonju-katla-gloves-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
CLS = 'Gloves_dex_int'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, ti=0, m='n', tags=None, sfx=None):   # 클래스 파일 티어 글 그대로
    g = D['groups'][gi]; t = g['t'][ti]; kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if sfx: kr, en = kr + ' (' + sfx[0] + ')', en + ' (' + sfx[1] + ')'
    return L(g['g'], kr, en, m, tags)

AMn = T(89, 0, 'n', ['kp1'])
AM = T(89, 0, 'f', ['kp1'], ('분열', 'fractured'))
FA = T(90, 0, 'n', ['kp1'])
IG = T(86, 0, 'd', ['kpT'])
FR = T(2, 2, 'n')
HOR = T(62, 0, 'c', ['hor'], ('경악의 에센스', 'Essence of Horror'))
AOE = T(72, 0, 'c', ['aoe'], ('신비한 합금', 'Mystic Alloy'))
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
JX = L('x', '잡옵', 'Junk', 'j')
KR = L('r', '카틀라의 순흑', 'Katla’s Gloom', 'r')
AS = L('r', '아스트리드의 창의성', "Astrid's Creativity", 'r')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'cheonju-katla-gloves-v2', 'recipe': 'cheonju-katla-gloves-v2', 'cls': CLS, 'base': 'Secured Wraps', 'ilvl': 82,
 'note': ('2026-11-14 RECIPE-B: 천주 화염파 젬링 장갑(youtu.be/UwlQO3Qf6ZI, 조사 g83 — docs/craft-guides.md 5차, 완성품 26:18 툴팁). '
          '1:12 고정된 싸개(노멀, 증강 홈 2개, 아이템 레벨 82) → 2:04 카틀라의 순흑 장착 → 완벽한 진화 + 완벽한 확장 + 완벽한 제왕 → 유효 옵션이 없으면 소멸 없이 옵션 3개 상태로 카오스 오브 반복 → '
          '3:05 카틀라 접두 1티어(상태 이상 강도·점화 강도·상태 이상 가속 중, 강도 26 미만은 넘김)가 뜨면 좌측 강령술의 징조 + 보존된 갈비뼈(접두가 꽉 차면 접미) → 분열의 오브(실패면 상점에 팔고 다음 베이스, 8:19 아홉 번째 성공) → '
          '8:49 소멸로 분열만 남김 → 카오스 반복 → 11:02 둘째 카틀라 접두 1티어(영상: 상태 이상 가속) → 좌측 강령술 + 보존된 갈비뼈 + 심연의 메아리(목표 레벨 45라 고대 갈비뼈 필요 없음), 빗나가면 빛의 징조(17:11 열한 번째 무렵 점화 강도) → '
          '19:10 상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 2개(잡옵) → 20:18 아스트리드의 창의성 → 21:20 우측 결정화의 징조 + 경악의 에센스, 우측 결정화 + 신비한 합금(한 번은 경악 옵션이 지워져 다시) → '
          '22:22 남은 접미 완벽한 엑잘(영상은 잡옵이면 우측 소멸의 징조 반복, 경악 옵션이 지워지면 우측 결정화 + 경악 다시 → 화염 저항 3티어에서 타협). '
          '등급: 난이도 3(어려움, 분열 빗나감으로 베이스 약 3개)이라 밸런스·에센셜(10장 C11). 마지막 옵션을 다시 굴리는 도박은 하이엔드만이라(C17-2) 두 등급 모두 마지막 접미는 랜덤 옵션 — 영상의 우측 소멸 반복은 꿀팁. 밸런스 = 영상 흐름(셋째 카틀라 접두 1티어까지 빛의 징조), 에센셜 = 공개 결과 그대로. '
          '카틀라 옵션은 공개 가중치가 없어 시뮬이 추정값을 씀 — 확률·비용은 추정. '
          '내부 결정: 분열 뒤 "훼손이 남은 상태로 카오스 한 번"은 정리 과정이라 소멸 정리에 묶음, 셋째 접두 공개는 남은 카틀라 유효 접두를 노림(영상 결과 점화 강도), 마지막 접미의 우측 말소 + 카오스 갈래는 꿀팁으로만. '
          '신성한 오브와 25:43 아스트리드 자리의 마무리 룬 교체는 정책 9·14장대로 뺌(완성 카드 소켓은 아스트리드의 창의성).'),
 'params': {
  'kT': {'kr': '셋째 카틀라 접두(훼손)', 'en': 'Third Katla prefix (desecrated)', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}},
  'v': {'kr': '공개가 빗나가면', 'en': 'Reveal miss', 'values': {'1': K('빛의 징조로 다시', 'Retry with Light'), '0': K('결과 그대로', 'Keep it')}}},
 'strategies': [{'id': 'bal', 'params': {'kT': 1, 'v': 1}}, {'id': 'ess', 'params': {'kT': 2, 'v': 0}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'kT': 2, 'v': 0}, 'tier': 'ess',
   'desc': K('셋째 접두 공개 결과 그대로, 마지막 접미는 랜덤 옵션', 'Third prefix reveal kept as it comes, a random last suffix')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'kT': 1, 'v': 1}, 'tier': 'bal',
   'desc': K('영상 흐름: 카틀라 접두 3개 1티어(셋째는 빛의 징조로 다시 공개), 마지막 접미는 랜덤 옵션', 'Video flow: three T1 Katla prefixes (the third retried with Light), a random last suffix')}],
 'tags': {
  'k89': {'gi': 89, 'tmax': 1}, 'k86': {'gi': 86, 'tmax': 1}, 'k90': {'gi': 90, 'tmax': 1},
  'kp1': {'anyOf': ['k89', 'k86', 'k90'], 'shown': ['k89', 'k90'], 'label': K('카틀라 접두 1티어(상태 이상 강도·점화 강도·상태 이상 가속)', 'T1 Katla prefix (ailment magnitude, ignite magnitude or faster ailments)')},
  'k89T': {'gi': 89, 'tmax': '$kT'}, 'k86T': {'gi': 86, 'tmax': '$kT'}, 'k90T': {'gi': 90, 'tmax': '$kT'},
  'kpT': {'anyOf': ['k89T', 'k86T', 'k90T'], 'shown': 'k86T', 'label': K('카틀라 접두(상태 이상 강도·점화 강도·상태 이상 가속)', 'Katla prefix (ailment magnitude, ignite magnitude or faster ailments)')},
  'hor': {'gi': 62}, 'aoe': {'gi': 72}},
 'require': {'all': [{'count': {'tag': 'kp1', 'min': 2}}, {'any': [{'param': {'v': 0}}, {'count': {'tag': 'kpT', 'min': 3}}]},
                     {'has': 'hor'}, {'has': 'aoe'}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0', 'xsub': ["Katla's Gloom"], 'xroll': True,
 'finalItem': {'quality': 20, 'sockets': 2, 'exceptional': True},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (1:12~8:49) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='rk', start={'rar': 'normal', 'mods': []},
  label=K('특출난 고정된 싸개 구입 (노멀, 아이템 레벨 82, 증강 홈 2개)', 'Buy exceptional Secured Wraps (normal, item level 82, two augment sockets)'), item=[])
A(id='rk', kind='act', group='prep', pos=[0, 1], act='rune', rune={'kr': '카틀라의 순흑', 'en': 'Katla’s Gloom'}, label=K('룬', 'Rune'),
  goal=K('카틀라의 순흑 장착', 'Socket Katla’s Gloom'), showText=[K('카틀라 옵션이 붙을 수 있음', 'Katla lines can roll')], edges=[{'to': 't1'}], item=[KR])
A(id='t1', kind='act', group='prep', pos=[0, 2], act='transmute', cur='Perfect_Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직', 'Magic'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'a1'}], item=[JX, KR])
A(id='a1', kind='act', group='prep', pos=[0, 3], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('매직 옵션 2개', 'Two magic options'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'r1'}], item=[J('p'), J('s'), KR])
A(id='r1', kind='act', group='prep', pos=[0, 4], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 옵션 3개', 'Rare with three options'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'c0'}], item=[J('p'), J('p'), J('s'), KR])
A(id='c0', kind='act', group='prep', pos=[0, 5], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 상태 이상 강도 1티어 — 카틀라 접두 1티어 중 먼저 뜬 것', 'T1 ailment magnitude prefix: whichever T1 Katla prefix lands first'),
  show=['k89', 'k86', 'k90'], skipIf={'has': 'kp1'}, skipTo='d0',
  edges=[{'if': {'all': [{'has': 'kp1'}, {'full': 'p'}]}, 'to': 'd0s', 'res': 'ok', 'label': K('접두가 꽉 참', 'Prefixes full')},
         {'if': {'has': 'kp1'}, 'to': 'd0', 'res': 'ok'}, {'to': 'c0', 'res': 'fail', 'hide': True}], item=[AMn, J('p'), J('s'), KR])
A(id='d0', kind='act', group='prep', pos=[0, 6], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')],
  skipIf={'full': 'p'}, skipTo='d0s',
  edges=[{'to': 'f0'}], item=[AMn, J('p'), UN('p'), J('s'), KR])
A(id='d0s', kind='act', group='prep', pos=[1, 6], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 접미에', 'Fourth option (desecrated) into a suffix'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'f0'}])
A(id='f0', kind='act', group='prep', pos=[0, 7], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'), showText=[K('카틀라 접두가 분열되면 성공', 'Success when the Katla prefix fractures')],
  edges=[{'if': {'fractured': 'kp1'}, 'to': 'ms', 'res': 'ok', 'label': K('카틀라 접두 분열', 'Katla prefix fractured')},
         {'to': 'xf', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}], item=[AM, J('p'), UN('p'), J('s'), KR])
A(id='xf', kind='exit', group='prep', pos=[1, 7], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 판매, 새 베이스', 'Another option fractured: sell it, new base'),
  note=K('카틀라 접두가 아닌 옵션이 분열되면 상점에 팔고 다음 베이스', 'Another option fractured: sell it to a vendor and take the next base'))
# ---------------- 옵션 추가 작업 (8:49~22:22) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8.4], next='cl', label=K('아이템 제작 시작', 'Item crafting starts'), item=[AM, J('p'), UN('p'), J('s'), KR])
A(id='cl', kind='cleanup', group='main', pos=[0, 9.4], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('분열만 남기기', 'Keep only the fracture'), edges=[{'to': 'c1'}], item=[AM, KR])
A(id='c1', kind='act', group='main', pos=[0, 10.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 상태 이상 가속 1티어 — 남은 카틀라 접두 1티어 중 먼저 뜬 것', 'T1 faster ailments prefix: whichever remaining T1 Katla prefix lands first'),
  show=['k86', 'k90'], skipIf={'count': {'tag': 'kp1', 'min': 2}}, skipTo='d1',
  edges=[{'if': {'count': {'tag': 'kp1', 'min': 2}}, 'to': 'd1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[AM, FA, KR])
A(id='d1', kind='act', group='main', pos=[0, 11.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=[AM, FA, UN('p'), KR])
A(id='d2', kind='act', group='main', pos=[0, 12.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='kpT', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 점화 강도 1티어', 'Third prefix (desecrated): T1 ignite magnitude'),
  goalBy={'ess': K('접두 세 번째 옵션(훼손) — 나오는 대로 (영상: 점화 강도)', 'Third prefix (desecrated): keep what comes (video: ignite magnitude)')},
  show=['k86T'],
  edges=[{'if': {'added': 'kpT'}, 'to': 's1', 'res': 'ok'}, {'if': {'param': {'v': 0}}, 'to': 's1', 'res': 'fail', 'hide': True},
         {'to': 'd2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[AM, FA, IG, KR])
A(id='d2x', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='s1', kind='act', group='main', pos=[0, 13.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 옵션 2개 — 나오는 대로 (영상: 잡옵 2개)', 'Two suffixes: keep what comes (video: two junk options)'), showText=[K('랜덤 옵션 2개', 'Two random options')],
  edges=[{'to': 'rn'}], item=[AM, FA, IG, J('s'), J('s'), KR])
A(id='rn', kind='act', group='main', pos=[0, 14.4], act='rune', rune={'kr': '아스트리드의 창의성', 'en': "Astrid's Creativity"}, label=K('룬', 'Rune'),
  goal=K('아스트리드의 창의성 장착', "Socket Astrid's Creativity"), showText=[K('제작 옵션 2개까지', 'Up to two crafted options')],
  edges=[{'to': 's2'}], item=[AM, FA, IG, J('s'), J('s'), KR, AS])
# 경악의 에센스·신비한 합금(우측 결정화) — 경악 옵션이 지워지면 다시, 둘 다 있으면 마지막 접미 (영상 21:20~22:22)
def CR(vis):
    out = []
    for e in [{'if': {'all': [{'has': 'hor'}, {'has': 'aoe'}]}, 'to': 's4'}, {'if': {'not': {'has': 'hor'}}, 'to': 's2'}, {'to': 's3'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out
A(id='s2', kind='act', group='main', pos=[0, 15.4], act='essence', cur='Essence_of_Horror', ess='hor', omens=['Omen_of_Dextral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접미 장착된 증강물 아이템의 효과 60% — 접미 잡옵 하나가 지워짐', 'Suffix 60% socketed augment effect: a junk suffix goes'),
  showText=[{'s': 's', 'kr': '장착된 증강물 아이템의 효과 60% 증가 (제작 옵션)', 'en': '60% increased effect of Socketed Augment Items (crafted)'}],
  edges=CR({'s3': {'res': 'ok'}, 's4': {'res': 'ok'}}), item=[AM, FA, IG, HOR, J('s'), KR, AS])
A(id='s3', kind='act', group='main', pos=[0, 16.4], act='essence', cur='Mystic_Alloy', ess='aoe', omens=['Omen_of_Dextral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('접미 공격 효과 범위 — 남은 잡옵을 바꿈', 'Suffix attack area of effect: replace the last junk'),
  showText=[{'s': 's', 'kr': '공격 효과 범위 (10—15)% 증가 (제작 옵션)', 'en': '(10—15)% increased Area of Effect for Attacks (crafted)'}],
  edges=CR({'s4': {'res': 'ok'}, 's2': {'res': 'fail', 'label': K('경악 옵션이 지워짐', 'Horror line removed')}}), item=[AM, FA, IG, HOR, AOE, KR, AS])
A(id='s4', kind='act', group='main', pos=[0, 17.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 세 번째 옵션 — 나오는 대로 (영상: 화염 저항)', 'Third suffix: keep what comes (video: fire resistance)'),
  showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'ok'}], item=[AM, FA, IG, HOR, AOE, FR, KR, AS])
A(id='ok', kind='done', group='main', pos=[0, 18.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L0', 'nodes': ['c0'], 'kr': '카틀라 접두 1티어', 'en': 'T1 Katla prefix'},
 {'id': 'L1', 'nodes': ['c1'], 'kr': '둘째 카틀라 접두', 'en': 'Second Katla prefix'},
 {'id': 'L2', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '훼손 공개', 'en': 'Reveal'},
 {'id': 'L3', 'nodes': ['s2', 's3'], 'kr': '제작 옵션 2개', 'en': 'Two crafted options'},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'kp1', 'fr': True}, {'tag': 'kp1'}, {'tag': 'kpT', 'des': True}, {'side': 's', 'random': True}, {'tag': 'hor', 'ess': True}, {'tag': 'aoe', 'ess': True}]},
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'kp1', 'fr': True}, {'tag': 'kp1'}, {'side': 'p', 'random': True, 'des': True}, {'side': 's', 'random': True}, {'tag': 'hor', 'ess': True}, {'tag': 'aoe', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
