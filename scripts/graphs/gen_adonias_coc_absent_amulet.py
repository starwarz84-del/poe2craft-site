# RECIPE-A 2026-11-14: AdoniasHope 치명타 시 시전 부재 목걸이(SOddUyQPIxQ, 2026-10-02) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: docs/craft-guides.md '5차 조사' g97(영어 자막 단계·빗나감 처리·대체 경로, 가격 확인 화면) + docs/craft-guides.json register(ok)
# 실행: cd scripts/graphs && python3 gen_adonias_coc_absent_amulet.py  → adonias-coc-absent-amulet-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/adonias-coc-absent-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SP = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'f', ['spirit'])
SL = L('s', '모든 주문 스킬 레벨 +3', '+3 to Level of all Spell Skills', 'n', ['spell'])
MANA = L('p', '마나 최대치 +(170—179)', '+(170—179) to maximum Mana', 'n', ['pv'])
ACC = L('p', '정확도 +(311—400)', '+(311—400) to Accuracy Rating', 'n')   # 4:06 엑잘 빗나감(영상)
CAST = L('s', '시전 속도 (25—28)% 증가', '(25—28)% increased Cast Speed', 'd', ['cast'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = L('s', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
LIGHT = K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light')
PVL = K('마나 최대치·최대 마나 %·주문 피해', 'Maximum Mana, % maximum Mana or Spell Damage')

g = {
 'id': 'adonias-coc-absent-amulet-v2', 'recipe': 'adonias-coc-absent-amulet-v2', 'cls': 'Amulets', 'base': 'Absent Amulet', 'ilvl': 82,
 'note': ('2026-11-14 RECIPE-A: AdoniasHope 치명타 시 시전 부재 목걸이(2026-10-02, 0.5.5) 성공 회차 한 줄(근거 docs/craft-guides.md 5차 g97, 영어 자막 + 가격 화면). '
          '정신력 분열 부재 목걸이 구입(2:34, 직접 분열 대신) → 카오스 반복으로 모든 주문 스킬 레벨 +3(3:06, 영상 약 300 div어치, 근접 +3은 넘김) → '
          '좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 시전자 옵션 도박(4:06, 정확도로 빗나감) → 절사의 징조 + 카오스 오브 → 마나 최대치 2티어 → '
          '고대 빗장뼈 + 심연의 메아리로 접미 훼손(5:08), 빗나가면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 다시 → 시전 속도 1티어(25% 이상). '
          '뺀 것: 신성한 오브(28%)·기름부음·축성(9:43, 수치 다듬기와 타락 — 14장), 접두가 나쁠 때의 대체 경로(12:19 좌측 결정화 + 완벽한 강화의 에센스, 검은 피의 징조 퀄리티 훼손)는 꿀팁 후보로만. '
          '내부 결정: 산 베이스는 분열 정신력 + 잡옵 1개(카오스로 바꿀 옵션), 베이스 값은 자막에 없어 미정(10장 ③). 절사 카오스의 오브 등급은 자막에 없어 카오스 오브, 절사가 주문 +3을 바꾸면 소멸의 오브로 분열 + 옵션 1개까지 지우고 카오스부터(정책 3장). '
          '접두 두 번째 옵션은 영상처럼 엑잘 도박 한 번 + 빗나가면 절사 카오스 한 번(영상은 마나 최대치 2티어를 그대로 받음, 다시 하는 장면 없음) — 완성 카드는 랜덤 옵션, 노린 옵션은 꿀팁(정책 10장 ⑬). 절사로 나온 새 옵션이 접미로 가면 다시 절사(접미 자리는 훼손용). '
          '등급: 난이도 4(카오스 약 1,700개) → 하이엔드(영상: 시전 속도 1티어) · 밸런스(1~2티어).'),
 'params': {'cT': {'kr': '시전 속도', 'en': 'Cast speed', 'values': {'1': K('1티어', 'T1'), '2': K('1~2티어', 'T1–2')}}},
 'strategies': [{'id': 'high', 'params': {'cT': 1}}, {'id': 'bal', 'params': {'cT': 2}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'cT': 2}, 'tier': 'bal',
    'desc': K('시전 속도 1~2티어까지 빛의 징조로 다시', 'Omen of Light until T1–2 cast speed')},
   {'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'cT': 1}, 'tier': 'high',
    'desc': K('영상: 시전 속도 1티어(25% 이상)까지 빛의 징조로 다시', 'Video: Omen of Light until T1 cast speed (25%+)')}],
 'tags': {'spirit': {'gi': 28, 'tmax': 1}, 'spell': {'gi': 17, 'tmax': 1},
          'mana': {'gi': 11, 'tmax': 2}, 'mp': {'gi': 12, 'tmax': 2}, 'sd': {'gi': 31, 'tmax': 2},
          'pv': {'anyOf': ['mana', 'mp', 'sd'], 'shown': 'mana', 'label': PVL},
          'cast': {'gi': 32, 'tmax': '$cT'}},
 'require': {'all': [{'has': 'spirit'}, {'has': 'spell'}, {'unrev': False}, {'full': 'p'}, {'full': 's'},
                     {'has': 'cast'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finals': [
   {'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
    'lines': [{'tag': 'spirit', 'fr': True}, {'side': 'p', 'random': True}, {'tag': 'spell'}, {'tag': 'cast', 'des': True}]},
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'spirit', 'fr': True}, {'side': 'p', 'random': True}, {'tag': 'spell'}, {'tag': 'cast', 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'rare', 'mods': [{'tag': 'spirit', 'fr': True}, {'junk': 's'}]},
  label=K('분열 정신력 + 잡옵 1개 부재 목걸이 구입 (아이템 레벨 82)', 'Buy an Absent Amulet with fractured Spirit + one junk option (item level 82)'),
  item=[SP, J('s')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SP, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 2.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 모든 주문 스킬 레벨 +3', '+3 Spell Skills suffix'), show=['spell'],
  edges=[{'if': {'has': 'spell'}, 'to': 'e1', 'res': 'ok'}, {'to': 'k1', 'res': 'fail', 'hide': True}], item=[SP, SL])
A(id='e1', kind='act', group='main', pos=[0, 3.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 시전자 옵션 도박', 'Second prefix: a caster option gamble'), show=['pv'],
  edges=[{'if': {'has': 'pv'}, 'to': 'd1', 'res': 'ok'},
         {'to': 'w1', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SP, ACC, SL])
A(id='w1', kind='act', group='main', pos=[0, 4.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Whittling'], label=K('절사 + 카오스', 'Whittling + Chaos'),
  goal=K('가장 낮은 옵션(빗나간 접두) 바꾸기 — 나오는 대로 (영상: 마나 최대치 2티어)', 'Reroll the lowest option (the missed prefix): keep what comes (video: T2 maximum mana)'),
  showText=[K('💡 노린 옵션은 접두 시전자 옵션(주문 피해가 가장 좋음) — 영상은 한 번에 마나 최대치 2티어를 받음', '💡 The aim is a caster prefix (spell damage is best); the video took T2 maximum mana on the first try')],
  edges=[{'if': {'not': {'has': 'spell'}}, 'to': 'kx', 'res': 'fail', 'lost': 'spell', 'label': K('주문 +3이 바뀜', 'The +3 changed')},
         {'if': {'all': [{'full': 'p'}, {'sideLt': {'side': 's', 'n': 2}}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'w1', 'res': 'fail', 'label': K('새 옵션이 접미로 — 다시 절사', 'The new option went to a suffix: Whittling again')}],
  item=[SP, MANA, SL])
A(id='kx', kind='cleanup', group='main', pos=[1, 4.4], keep=[], maxJunk=1, label=K('소멸의 오브 사용', 'Use an Orb of Annulment'), goal=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  target=K('분열 + 옵션 1개만 남기고 카오스부터', 'Keep the fracture + one option, Chaos again'), edges=[{'to': 'k1', 'label': K('다시 카오스', 'Chaos again')}])
A(id='d1', kind='act', group='main', pos=[0, 5.4], act='desecrate', cur='Ancient_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접미 두 번째 옵션(훼손)', 'Second suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개) — 빈자리가 접미뿐', 'en': 'Desecrated (unrevealed): the only free slot'}], edges=[{'to': 'r1'}], item=[SP, MANA, SL, UN])
A(id='r1', kind='act', group='main', pos=[0, 6.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='cast', label=K('공개', 'Reveal'),
  goal=K('접미 시전 속도 1티어', 'T1 cast speed suffix'), show=['cast'],
  goalBy={'bal': K('접미 시전 속도 1~2티어', 'T1–2 cast speed suffix')},
  edges=[{'if': {'added': 'cast'}, 'to': 'ok', 'res': 'ok'},
         {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[SP, MANA, SL, CAST])
A(id='r1x', kind='act', group='main', pos=[1, 6.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 7.6], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L2', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
