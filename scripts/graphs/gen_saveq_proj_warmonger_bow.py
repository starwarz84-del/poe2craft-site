# RECIPE-C 2026-11-14: SaVeQ 투사체 물리 활(youtu.be/35uKJrlkZuo, 2026-10-26, 0.5.5, A-Z #3) — 조사 g105(docs/craft-guides.md 6차)
# 영상 흐름 한 줄: 전쟁광 활(아이템 레벨 81) 퀄리티 30% → 진화 + 완벽한 확장 + 소멸로 투사체 +4 매직 → 완벽한 제왕 → 보존된 턱뼈 → 분열(투사체 +4)
#   → 소멸로 분열만 → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘(접두) → 완벽한 엑잘 세 번째 접두 → 아스트리드의 창의성
#   → 우측 결정화 + 심연의 에센스(접미 징표) → 보존된 턱뼈 → 공개(치명타 확률), 빗나가면 우측 결정화 + 보호의 합금으로 덮고 다시 → 완벽한 엑잘 마지막 접미
# 실행: cd scripts/graphs && python3 gen_saveq_proj_warmonger_bow.py  → saveq-proj-warmonger-bow-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-proj-warmonger-bow-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
CLS = 'Bows'
D = json.load(open(f'{H}/../../site/data/c/{CLS}.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, ti=0, m='n', tags=None, sfx=None):   # 클래스 파일 티어 글 그대로
    g = D['groups'][gi]; t = g['t'][ti]; kr, en = t[4].replace('\n', ' / '), t[5].replace('\n', ' / ')
    if sfx: kr, en = kr + ' (' + sfx[0] + ')', en + ' (' + sfx[1] + ')'
    return L(g['g'], kr, en, m, tags)

PJm = T(9, 0, 'n', ['proj'])                              # 5:36 매직 투사체 +4
PJ = T(9, 0, 'f', ['proj'], ('분열', 'fractured'))        # 6:08 분열
PP = T(7, 1, 'n', ['pp'])                                 # 21:02 물리 피해 167% T2
HY = T(8, 3, 'n')                                         # 하이브리드 T4 (나오는 대로)
FL = T(2, 3, 'n')                                         # 물리 피해 추가 T4 (나오는 대로)
MK = L('s', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mks'])
CR = T(17, 1, 'd', ['crit'])                              # 19:47 치명타 확률 +3.91% T2 (훼손)
RW = T(58, 0, 'c', ['rw'], ('보호의 합금', 'Protective Alloy'))
LE = T(11, 0, 'n')                                        # 마나 흡수 T1 (나오는 대로)
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
AS = L('r', '아스트리드의 창의성', "Astrid's Creativity", 'r')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'saveq-proj-warmonger-bow-v2', 'recipe': 'saveq-proj-warmonger-bow-v2', 'cls': CLS, 'base': 'Warmonger Bow', 'ilvl': 81,
 'note': ('2026-11-14 RECIPE-C: SaVeQ 투사체 물리 활(youtu.be/35uKJrlkZuo, A-Z #3, 조사 g105 — docs/craft-guides.md 6차). '
          '0:30 아이템 레벨 81 전쟁광 활(82는 25 div라 피함) 3 카오스짜리 여러 개 → 1:31 퀄리티 30%(타락으로 여러 개를 잃고 둘 남음) → '
          '2:34 진화 + 소멸 + 완벽한 확장 반복으로 투사체 +4 → 5:36 신성 오브 → 6:08 완벽한 제왕 → 보존된 턱뼈로 아무 훼손(옵션 4개) → 바로 분열의 오브 → 투사체 +4 분열 → '
          '7:09 소멸로 줄이고 좌측 찬미 + 상위 찬미 + 완벽한 엑잘로 접두, 빗나가면 소멸 → 접두는 물리 % 2티어·나머지 타협 → '
          '9:13 아스트리드의 창의성 → 우측 결정화 + 심연의 에센스(접미 징표) → 보존된 턱뼈로 징표 훼손 → 공개, 빗나가면 우측 결정화 + 보호의 합금으로 훼손 옵션을 덮고 다시 심연의 에센스(빛의 징조 없음) → '
          '19:47 치명타 확률 1티어 20번 넘게 실패 → 2티어로 타협 → 마지막 접미 엑잘(마나 흡수) → 21:02 완성 툴팁. 약 370 div, 900 div 등록. '
          '내부 결정: 매직 단계는 투사체 +4만 맞춤(영상은 좋은 접두도 같이 노렸지만 분열 뒤 소멸로 지워져 완성품과 상관없음), 분열이 투사체 +4가 아니면 새 베이스. '
          '접두 빗나감 정리는 소멸로 분열만 남기고 다시(영상은 카오스·절사도 두 번 씀 — 결과가 같은 되돌림이라 소멸 하나로 합침), 성공 조건 = 물리 피해 % 3티어 이상, 두 번째·세 번째 접두는 결과 그대로(완성 카드 랜덤 옵션). '
          '세 번째 접두·마지막 접미 엑잘의 오브 등급은 자막에 없어 완벽한 엑잘티드 오브로 둠. 덮는 쪽은 보호의 합금(영상은 완벽한 신속의 에센스도 같이 씀). '
          '퀄리티 30%·신성 오브·마무리 룬은 선택 단계(비용 미포함, 정책 9장).'),
 'params': {'cT': {'kr': '치명타 확률(훼손)', 'en': 'Crit chance (desecrated)',
                   'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}}},
 'strategies': [{'id': 'bal', 'params': {'cT': 2}}, {'id': 'ess', 'params': {'cT': 4}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'cT': 2}, 'tier': 'bal',
   'desc': K('영상 흐름: 치명타 확률 훼손 1~2티어', 'Video flow: T1–2 desecrated crit chance')},
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'cT': 4}, 'tier': 'ess',
   'desc': K('치명타 확률 훼손 1~4티어', 'T1–4 desecrated crit chance')}],
 'tags': {'proj': {'gi': 9, 'tmax': 1}, 'pp': {'gi': 7, 'tmax': 3}, 'crit': {'gi': 17, 'tmax': '$cT'},
          'mks': {'gi': 57}, 'rw': {'gi': 58}},
 'require': {'all': [{'has': 'proj'}, {'has': 'pp'}, {'has': 'crit'}, {'des': True}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'pb',
 'basePrice': {'Chaos_Orb': 3},
 'finalItem': {'quality': 30, 'sockets': 2},
}
N = []
A = lambda **kw: N.append(kw)

# 매직 단계 길잡이: 투사체 +4 + 접두 하나 → 제왕, 투사체 +4만 → 확장, 다른 접미 → 소멸
def MG(vis):
    out = []
    for e in [{'if': {'all': [{'has': 'proj'}, {'full': 'p'}]}, 'to': 'pr'}, {'if': {'has': 'proj'}, 'to': 'pa'},
              {'if': {'full': 's'}, 'to': 'px'}, {'to': 'pa'}]:
        v = vis.get(e['to'])
        out.append({**e, **v} if v is not None else {**e, 'hide': True})
    return out

# ---------------- 베이스템 완성 ----------------
A(id='pb', kind='base', group='prep', pos=[0, 0], next='pt', start={'rar': 'normal', 'mods': [], 'quality': 30},
  label=K('전쟁광 활 구입 (노멀, 아이템 레벨 81)', 'Buy a Warmonger Bow (normal, item level 81)'), item=[])
A(id='hq', kind='side', group='prep', pos=[1, 0.5], attach=['pb', 'pt'], cur='Vaal_Blacksmiths_Infuser', label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 30%, 선택·비용 미포함 — 타락하면 버림', 'Quality 30%, optional, not costed: a corrupted one is thrown away'))
A(id='pt', kind='act', group='prep', pos=[0, 1], act='transmute', cur='Orb_of_Transmutation', label=K('진화', 'Transmute'),
  goal=K('매직 — 접미 투사체 +4 노림', 'Magic: aiming for the +4 projectile suffix'), show=['proj'], edges=MG({'pa': {}}), item=[PJm])
A(id='pa', kind='act', group='prep', pos=[0, 2], act='augment', cur='Perfect_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('접미 모든 투사체 스킬 레벨 +4', 'Suffix +4 to all projectile skills'), show=['proj'],
  edges=MG({'pr': {'res': 'ok'}, 'px': {'res': 'fail', 'label': K('투사체 +4가 아닌 접미', 'A suffix other than +4 projectiles')}}), item=[J('p'), PJm])
A(id='px', kind='act', group='prep', pos=[1, 2], act='annul', cur='Orb_of_Annulment', label=ANN, goal=ANN,
  target=K('옵션 1개 제거', 'Remove one option'), edges=MG({'pa': {'label': K('다시 확장', 'Augment again')}}))
A(id='pr', kind='act', group='prep', pos=[0, 3], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'pd'}], item=[J('p'), PJm, J('s')])
A(id='pv', kind='side', group='prep', pos=[1, 3.5], attach=['pr', 'pd'], cur='Divine_Orb', label=K('신성', 'Divine'),
  goal=K('투사체 +4 수치, 선택·비용 미포함', 'Values on +4 projectiles, optional, not costed'))
A(id='pd', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')], edges=[{'to': 'pf'}], item=[J('p'), UN('p'), PJm, J('s')])
A(id='pf', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'), showText=[K('투사체 +4가 분열되면 성공', 'Success when +4 projectiles fractures')],
  edges=[{'if': {'fractured': 'proj'}, 'to': 'pc', 'res': 'ok', 'label': K('투사체 +4 분열', '+4 projectiles fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}], item=[J('p'), UN('p'), PJ, J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 5], simTo='pb', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('투사체 +4가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('분열만 남기기', 'Keep only the fracture'), edges=[{'to': 'ms'}], item=[PJ])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 6.6], next='p1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PJ])
A(id='p1', kind='act', group='main', pos=[0, 7.6], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation', 'Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 옵션 2개 — 물리 피해 % 3티어 이상', 'Two prefixes: T3 or better % physical damage'), show=['pp'],
  edges=[{'if': {'has': 'pp'}, 'to': 'p2', 'res': 'ok'}, {'to': 'p1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[PP, HY, PJ])
A(id='p1x', kind='cleanup', group='main', pos=[1, 7.6], keep=[], maxJunk=0, label=ANN, goal=ANN,
  target=K('분열만 남기기', 'Keep only the fracture'), edges=[{'to': 'p1', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='p2', kind='act', group='main', pos=[0, 8.6], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션 — 나오는 대로 (영상: 물리 피해 추가)', 'Third prefix: keep what comes (video: flat physical)'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'rn'}], item=[PP, HY, FL, PJ])
A(id='rn', kind='act', group='main', pos=[0, 9.6], act='rune', rune={'kr': '아스트리드의 창의성', 'en': "Astrid's Creativity"}, label=K('룬', 'Rune'),
  goal=K('아스트리드의 창의성 장착', "Socket Astrid's Creativity"), showText=[K('제작 옵션 2개까지', 'Up to two crafted options')],
  edges=[{'to': 'k2'}], item=[PP, HY, FL, PJ, AS])
A(id='k2', kind='act', group='main', pos=[0, 10.6], act='essence', cur='Essence_of_the_Abyss', ess='mks', mark=True, omens=['Omen_of_Dextral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접미 징표', 'Suffix Mark'),
  showText=[{'s': 's', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'k3'}], item=[PP, HY, FL, PJ, MK, AS])
A(id='k3', kind='act', group='main', pos=[0, 11.6], act='desecrate', cur='Preserved_Jawbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표 훼손 — 접미로', 'Desecrate the Mark: to the suffix'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'k4'}], item=[PP, HY, FL, PJ, UN('s'), AS])
A(id='k4', kind='act', group='main', pos=[0, 12.6], act='reveal', want='crit', label=K('공개', 'Reveal'),
  goal=K('접미 두 번째 옵션(훼손) — 치명타 확률', 'Second suffix (desecrated): crit chance'),
  goalBy={'bal': K('접미 두 번째 옵션(훼손) — 치명타 확률 1~2티어 (영상: 2티어)', 'Second suffix (desecrated): T1–2 crit chance (video: T2)'),
          'ess': K('접미 두 번째 옵션(훼손) — 치명타 확률 1~4티어', 'Second suffix (desecrated): T1–4 crit chance')},
  show=['crit'],
  edges=[{'if': {'added': 'crit'}, 'to': 'u1', 'res': 'ok'}, {'to': 'k4x', 'res': 'fail', 'label': K('빗나감', 'Miss')}], item=[PP, HY, FL, PJ, CR, AS])
A(id='k4x', kind='act', group='main', pos=[1, 12.6], act='essence', cur='Protective_Alloy', ess='rw', omens=['Omen_of_Dextral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('빗나간 훼손 옵션을 합금으로 덮기', 'Cover the missed desecration with the alloy'),
  showText=[{'s': 's', 'kr': '최대 룬 수호 +(51—74) (제작 옵션)', 'en': '+(51—74) to maximum Runic Ward (crafted)'}],
  edges=[{'to': 'k2', 'label': K('다시 징표', 'Mark again')}])
A(id='u1', kind='act', group='main', pos=[0, 13.6], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 세 번째 옵션 — 나오는 대로 (영상: 마나 흡수)', 'Third suffix: keep what comes (video: mana leech)'), showText=[K('랜덤 옵션 1개', 'One random option')],
  edges=[{'to': 'ok'}], item=[PP, HY, FL, PJ, CR, LE, AS])
A(id='ok', kind='done', group='main', pos=[0, 14.6], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
 {'id': 'L0', 'nodes': ['pt', 'pa', 'px'], 'kr': '매직 투사체 +4', 'en': 'Magic +4 projectiles'},
 {'id': 'L1', 'nodes': ['p1', 'p1x'], 'kr': '접두 2개', 'en': 'Two prefixes'},
 {'id': 'L2', 'nodes': ['k2', 'k3', 'k4', 'k4x'], 'kr': '치명타 확률 훼손', 'en': 'Desecrated crit chance', 'fold': True,
  'goal': K('접미 치명타 확률 훼손 — 빛의 징조 없이 반복', 'Suffix desecrated crit chance: repeated without Light'),
  'goalBy': {'bal': K('접미 치명타 확률 1~2티어 훼손 — 빛의 징조 없이 반복', 'Suffix T1–2 desecrated crit chance: repeated without Light'),
             'ess': K('접미 치명타 확률 1~4티어 훼손 — 빛의 징조 없이 반복', 'Suffix T1–4 desecrated crit chance: repeated without Light')},
  'steps': [K('우측 결정화 + 심연의 에센스로 접미 징표', 'Dextral Crystallisation + Essence of the Abyss for a suffix Mark') | {'node': 'k2'},
            K('보존된 턱뼈로 징표 훼손', 'Preserved Jawbone on the Mark') | {'node': 'k3'},
            K('공개 — 징표 자리라 한 티어 높게', 'Reveal: one tier higher on the Mark') | {'node': 'k4'},
            K('빗나가면 우측 결정화 + 보호의 합금으로 덮고 징표부터', 'On a miss, Dextral Crystallisation + Protective Alloy covers it, then the Mark again') | {'node': 'k4x'}],
  'item': [PP, HY, FL, PJ, CR, AS]},
]
g['finals'] = [
 {'id': t, 'tier': t, 'kr': nm + ' 옵션', 'en': en,
  'lines': [{'tag': 'pp'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
            {'tag': 'proj', 'fr': True}, {'tag': 'crit', 'des': True}, {'side': 's', 'random': True}]}
 for t, nm, en in (('bal', '밸런스', 'Balance'), ('ess', '에센셜', 'Essential'))]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
