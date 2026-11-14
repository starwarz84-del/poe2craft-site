# RECIPE-C 2026-11-14: 시한 젬링 저격용 힘 투구(youtu.be/iXL71H94AdM, 2026-10-10, 0.5.5) — 조사 g101(docs/craft-guides.md 6차)
# 영상 흐름 한 줄(투구 제작 6:33~): 방어도 % 접두 분열 제국의 대헬름 → 카오스로 접미 치명타 확률 → 우측 소멸의 징조 + 소멸 → 엑잘 반복으로 방어도 원소 적용·세 번째 접미
#   → 좌측 결정화 + 심연의 에센스로 접두 징표 → 완벽한 엑잘 접두(생명력) → 고대 갈비뼈로 징표 훼손 + 심연의 메아리 → 빗나가면 빛의 징조 + 소멸 → 고대 갈비뼈 다시
# 실행: cd scripts/graphs && python3 gen_sihan_gemling_greathelm.py  → sihan-gemling-greathelm-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-gemling-greathelm-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
CLS = 'Helmets_str'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, ti=0, m='n', tags=None, sfx=None):   # 클래스 파일 티어 글 그대로
    g = D['groups'][gi]; t = g['t'][ti]; kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if sfx: kr, en = kr + ' (' + sfx[0] + ')', en + ' (' + sfx[1] + ')'
    return L(g['g'], kr, en, m, tags)

AR = T(9, 0, 'f', ['ar9'], ('분열', 'fractured'))       # 33:30 방어도 98% T1 (분열)
CR = T(16, 0, 'n', ['crit'])                             # 치명타 확률 30% T1
AE = T(20, 1, 'n', ['ae'])                               # 방어도 37% 원소 적용 T2
IN = T(1, 2, 'n')                                        # 지능 +29 T3 (세 번째 접미, 나오는 대로)
LF = T(6, 1, 'n', ['life'])                              # 생명력 +148 T2 (완벽한 엑잘, 나오는 대로)
FA = T(8, 0, 'd', ['fa'])                                # 방어도 +203 T1 (훼손)
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mkp'])
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'sihan-gemling-greathelm-v2', 'recipe': 'sihan-gemling-greathelm-v2', 'cls': CLS, 'base': 'Imperial Greathelm', 'ilvl': 80,
 'note': ('2026-11-14 RECIPE-C: 시한 젬링 저격용 힘 투구(youtu.be/iXL71H94AdM, 조사 g101 — docs/craft-guides.md 6차). 투구 제작은 6:33부터. '
          '7:24 접미 분열·접두 분열을 모두 해 본 뒤 접두 분열로 결론 → 영상은 방어도 % 접두가 분열된 제국의 대헬름(아이템 레벨 80)에서 시작 → '
          '10:03 카오스 오브 반복(1,000개 준비)으로 접미 치명타 확률 또는 방어도 원소 적용 2티어 이상, 접두는 보지 않음 → '
          '10:52 우측 소멸의 징조 + 소멸의 오브로 빗나간 접미를 지우고 엑잘티드 오브 한 개씩, 치명타가 지워지면 카오스로 돌아감, 세 번째 접미는 나오는 대로 → 20:43 접미 완성(지능 T3·치명 T1·방원소 T2) → '
          '22:54 좌측 결정화의 징조 + 심연의 에센스로 접두 잡옵 하나를 지우고 군주의 징표 → 23:10 완벽한 엑잘티드 오브로 접두(영상: 한 번에 생명력 T2) → '
          '24:07 고대 갈비뼈로 징표 훼손 + 심연의 메아리 → 방어도 플랫, 빗나가면 빛의 징조 + 소멸의 오브 후 고대 갈비뼈 다시 → 32:47 방어도 +203. 분열 이후 약 220 div(시한 예상 300~400). '
          '내부 결정: 분열 옵션은 영상이 분열된 베이스에서 시작해 화면 표시로 확인하지 않음 — 완성 접두 셋 중 방어도 플랫은 훼손, 생명력은 23:10 완벽한 엑잘로 붙어 남는 방어도 %가 분열 옵션. '
          '시작 상태(분열 + 잡옵 3개)와 분열 베이스 가격은 영상에서 확인 못 해 정하지 않음(베이스 가격 미정). '
          '23:10 완벽한 엑잘은 영상에서 한 번에 성공해 다시 하는 방법이 나오지 않음 → 결과 그대로(완성 카드 랜덤 옵션), 접두가 이미 꽉 차 있으면 건너뜀. '
          '완벽한 엑잘로 방어도 플랫이 먼저 붙으면 마지막 훼손 공개는 생명력으로 받음(같은 묶음 태그 fa2).'),
 'params': {'sT': {'kr': '치명타 확률·방어도 원소 적용·방어도 플랫', 'en': 'Crit chance, armour to elemental and flat armour',
                   'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'sT': 1}}, {'id': 'bal', 'params': {'sT': 2}}],
 'versions': [
  {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'sT': 1}, 'tier': 'high',
   'desc': K('치명타 확률·방어도 원소 적용 1티어, 방어도 플랫 훼손을 빛의 징조로 다시', 'T1 crit chance and armour to elemental, flat armour reveal retried with Light')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'sT': 2}, 'tier': 'bal',
   'desc': K('영상 흐름: 치명타 확률·방어도 원소 적용·방어도 플랫 1~2티어, 훼손 공개를 빛의 징조로 다시', 'Video flow: T1–2 crit chance, armour to elemental and flat armour, reveal retried with Light')}],
 'tags': {
  'ar9': {'gi': 9, 'tmax': 1},
  'crit': {'gi': 16, 'tmax': '$sT'}, 'ae': {'gi': 20, 'tmax': '$sT'},
  'cs': {'anyOf': ['crit', 'ae'], 'shown': 'crit', 'label': K('치명타 확률·방어도 원소 적용', 'Crit chance or armour applying to elemental damage')},
  'life': {'gi': 6, 'tmax': 2}, 'fa': {'gi': 8, 'tmax': '$sT'},
  'fa2': {'anyOf': ['fa', 'life'], 'shown': 'fa', 'label': K('방어도 플랫·생명력', 'Flat armour or life')},
  'mkp': {'gi': 47}},
 'conds': {'sufOk': {'all': [{'has': 'crit'}, {'has': 'ae'}]}},
 'require': {'all': [{'has': 'ar9'}, {'ref': 'sufOk'}, {'has': 'fa2'}, {'des': True}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 1},
}
N = []
A = lambda **kw: N.append(kw)

# 접미 구간 길잡이: 치명타·방원소 둘 다 + 접미 꽉 참 → 결정화, 둘 다 있고 자리 남음 → 엑잘, 꽉 찼는데 하나 모자람 → 우측 소멸, 둘 다 지워짐 → 카오스
def SR(vis):
    out = []
    for e in [{'if': {'not': {'has': 'cs'}}, 'to': 'c1'},
              {'if': {'all': [{'ref': 'sufOk'}, {'full': 's'}]}, 'to': 'e1'},
              {'if': {'ref': 'sufOk'}, 'to': 's2'},
              {'if': {'full': 's'}, 'to': 's1'},
              {'to': 's2'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms',
  start={'rar': 'rare', 'quality': 20, 'mods': [{'tag': 'ar9', 'fr': True}, {'junk': 'p'}, {'junk': 's'}, {'junk': 's'}]},
  label=K('방어도 % 분열 제국의 대헬름 (아이템 레벨 80)', 'Imperial Greathelm with fractured % armour (item level 80)'), item=[AR, J('p'), J('s'), J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[AR, J('p'), J('s'), J('s')])
A(id='c1', kind='act', group='main', pos=[0, 2.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫 번째 옵션 — 치명타 확률 (방어도 원소 적용도 성공)', 'First suffix: crit chance (armour to elemental also counts)'),
  goalBy={'high': K('접미 첫 번째 옵션 — 치명타 확률·방어도 원소 적용 1티어', 'First suffix: T1 crit chance or armour to elemental'),
          'bal': K('접미 첫 번째 옵션 — 치명타 확률·방어도 원소 적용 1~2티어', 'First suffix: T1–2 crit chance or armour to elemental')},
  show=['cs'], edges=SR({'s1': {'res': 'ok'}, 'c1': {'res': 'fail', 'hide': True}}), item=[AR, J('p'), CR, J('s'), J('s')])
A(id='s1', kind='act', group='main', pos=[0, 3.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'],
  label=K('소멸의 오브 + 우측 소멸의 징조', 'Orb of Annulment + Omen of Dextral Annulment'), goal=K('접미 잡옵 지우기', 'Remove a junk suffix'),
  target=K('접미 옵션 1개 제거', 'Remove one suffix'), skipIf={'not': {'full': 's'}}, skipTo='s2',
  skipNote=K('접미 자리가 남아 있으면 건너뜀', 'Skipped while a suffix slot is open'),
  edges=SR({'s2': {'res': 'ok'}, 'c1': {'res': 'fail', 'label': K('치명타 확률이 지워짐 — 카오스부터', 'Crit chance gone: back to Chaos')}}), item=[AR, J('p'), CR, J('s')])
A(id='s2', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션 — 방어도 원소 적용, 마지막은 나오는 대로', 'Second and third suffix: armour to elemental, the last as it comes'),
  goalBy={'high': K('접미 두 번째·세 번째 옵션 — 방어도 원소 적용 1티어, 마지막은 나오는 대로', 'Second and third suffix: T1 armour to elemental, the last as it comes'),
          'bal': K('접미 두 번째·세 번째 옵션 — 방어도 원소 적용 1~2티어, 마지막은 나오는 대로', 'Second and third suffix: T1–2 armour to elemental, the last as it comes')},
  show=['ae'], edges=SR({'e1': {'res': 'ok'}, 's1': {'res': 'fail', 'label': K('빗나감', 'Miss')}}), item=[AR, J('p'), CR, AE, IN])
A(id='e1', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Essence_of_the_Abyss', ess='mkp', mark=True, omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 징표', 'The junk prefix goes for the Mark'),
  showText=[{'s': 'p', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'x1'}], item=[AR, MK, CR, AE, IN])
A(id='x1', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션 — 나오는 대로 (영상: 생명력)', 'Third prefix: keep what comes (video: life)'), showText=[K('랜덤 옵션 1개', 'One random option')],
  skipIf={'full': 'p'}, skipTo='d1', skipNote=K('접두가 이미 꽉 차 있으면 건너뜀', 'Skipped when the prefixes are already full'),
  edges=[{'to': 'd1'}], item=[AR, LF, MK, CR, AE, IN])
A(id='d1', kind='act', group='main', pos=[0, 7.4], act='desecrate', cur='Ancient_Rib', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표 훼손 — 접두로', 'Desecrate the Mark: to the prefix'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=[AR, LF, UN('p'), CR, AE, IN])
A(id='d2', kind='act', group='main', pos=[0, 8.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='fa2', label=K('공개', 'Reveal'),
  goal=K('접두 훼손 옵션 — 방어도 플랫 1티어', 'Desecrated prefix: T1 flat armour'),
  goalBy={'bal': K('접두 훼손 옵션 — 방어도 플랫 1~2티어 (영상: 1티어)', 'Desecrated prefix: T1–2 flat armour (video: T1)')},
  show=['fa2'],
  edges=[{'if': {'added': 'fa2'}, 'to': 'ok', 'res': 'ok'}, {'to': 'd2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[AR, LF, FA, CR, AE, IN])
A(id='d2x', kind='act', group='main', pos=[1, 8.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'),
  goal=K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light'), target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'to': 'd3', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='d3', kind='act', group='main', pos=[1, 7.4], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}])
A(id='ok', kind='done', group='main', pos=[0, 9.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L1', 'nodes': ['s1', 's2'], 'kr': '접미 채우기', 'en': 'Filling the suffixes'},
 {'id': 'L2', 'nodes': ['d2', 'd2x', 'd3'], 'kr': '방어도 플랫 공개', 'en': 'Flat armour reveal'},
]
g['finals'] = [
 {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
  'lines': [{'tag': 'ar9', 'fr': True}, {'side': 'p', 'random': True}, {'tag': 'fa2', 'des': True},
            {'tag': 'crit'}, {'tag': 'ae'}, {'side': 's', 'random': True}]},
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'ar9', 'fr': True}, {'side': 'p', 'random': True}, {'tag': 'fa2', 'des': True},
            {'tag': 'crit'}, {'tag': 'ae'}, {'side': 's', 'random': True}]}
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
