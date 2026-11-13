# W14 2026-11-13: SL 투사체 7옵션 장갑(세를의 승리 접미 4개) 플로우차트 생성기
# 영상 XMYJh3CnXuY(SL 게임연구소, 18:55). 영상 전체를 화면으로 확인, 근거 scratchpad review/W14-sl-gloves/timeline.md · frames/.
# 저장소에서: python3 scripts/graphs/gen_sl_proj7_gloves.py → scripts/graphs/sl-proj7-gloves-v2.json (옛 gen_batch18.py는 쓰지 않음)
#
# 완성품(17:56 툴팁): 사이렌비늘 장갑, 아이템 레벨 80, 퀄리티 25%, 룬 = 콜르의 사냥 + 세를의 승리
#   접두: 투사체 피해 34(31—40) T1 · 투사체 속도 39(31—40) T1 · 마나 최대치 +108(105—124) T1
#   접미: 모든 투사체 스킬 레벨 +2(분열) · 치명타 확률 29(28—34) T1 · 관통 63(51—100)% T1(훼손) · 잔류물 48%(팽창하는 합금, 제작 옵션)
# 슬라이드 제작 방법 10단계(4:58): 1 베이스 + 홈 2개 + 흰템 → 2 바알 방어구 장인의 주입기 25퀄 → 3 콜르의 사냥 + 세를의 승리, 매직 → 4 완벽 확장 + 소멸 반복(투사체 +2)
#   → 5 분열 → 6 카오스(접두 1티어) → 7 좌측 찬미 + 상위 찬미 + 완엑(접두 1티어 2개) → 8 상위 찬미 + 완엑(접미 1티어 1개, + 잡옵 1개)
#   → 9 우측 결정화 + 에센스(합금), 50%로 잡옵 지우기 → 10 훼손으로 마무리
# 성공 회차(9:50~17:56): 분열 뒤 투사체 속도 1티어가 남아 카오스 건너뜀 → 완엑(상위·좌측 찬미) → 투사체 피해 + 잡옵 → 소멸 반복 → 12:10 절사 + 카오스(꿀팁 후보)
#   → 완엑으로 마나 최대치 1티어 → 접미 완엑 → 잡옵마다 우측 결정화 + 심연의 에센스 → 갈비뼈 → 빛의 징조 + 소멸 → 상위 찬미 + 완엑 → 치명타 확률 1티어 + 추가 투사체 2티어
#   → 우측 결정화 + 팽창하는 합금(성공) → 갈비뼈 → 공개, 관통 1티어가 나올 때까지 빛의 징조 + 소멸로 다시.
# 영상과 다르게 정한 곳(내부 결정, 보고서에 적음):
#   1 세를의 승리: 영상(슬라이드 3번·성공 회차)은 분열 전에 장착. 시뮬은 매직 접미 1개만 다뤄(site/sim.js maxA) 분열 뒤에 장착 — 영상도 7:47에 이 순서를 권함.
#   2 12:10 절사 + 카오스(잡옵이 접두에서 가장 낮은 레벨일 때)는 플로우차트에 넣지 않고 꿀팁 후보.
#   3 합금이 치명타 확률을 지우면(영상에 없음, 4:47 '처음부터'만) 우측 소멸의 징조 + 소멸의 오브로 접미를 비우고 접미 엑잘부터 — 제작 옵션(합금)이 남아 있으면 심연의 에센스를 못 씀(정책 5장).
#   4 분열 전 훼손·정리 훼손의 뼈 = 보존된 갈비뼈(공개하지 않음), 관통 훼손 = 고대 갈비뼈(관통 1티어 레벨 75). 영상 화면에서 뼈 종류는 확인 못 함.
#   5 퀄리티는 옆 상자(비용 미포함), 접두 엑잘의 징조는 빈자리 2개면 상위 찬미 + 좌측 찬미, 1개면 좌측 찬미(화면 확인 못 함), 심연의 메아리 없음.
# 접두 세 옵션은 같은 방법(카오스·엑잘)으로 채우는 완성품 옵션이라 '남은 옵션 중 먼저 뜬 것'(정책 11장 붙는 순서 예외). 화면 순서는 성공 회차(속도 → 피해 → 마나).
# 등급: 난이도 극한 → 하이엔드만(정책 10장 C11).
import json, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/poe2craft-site/scripts/graphs/sl-proj7-gloves-v2.json'
CLS = 'Gloves_int'
D = json.load(open(f'/home/claude/poe2craft-site/site/data/c/{CLS}.json'))
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def DB(s, gi, tags, m='n', ti=0):   # DB 옵션 문구
    t = D['groups'][gi]['t'][ti]
    return L(s, t[4].replace('\n', ' / '), t[5].replace('\n', ' / '), m, tags)

KOL = L('r', '콜르의 사냥', "Kolr's Hunt", 'r')
SER = L('r', '세를의 승리', "Serle's Triumph", 'r')
PS = DB('p', 73, ['ps1'])          # 투사체 속도 (31—40)% 증가 1티어
PD = DB('p', 71, ['pd1'])          # 투사체 피해 (31—40)% 증가 1티어
MF = DB('p', 7, ['mf1'])           # 마나 최대치 +(105—124) 1티어
PRm = DB('s', 82, ['proj'])        # 모든 투사체 스킬 레벨 +2
PR = DB('s', 82, ['proj'], 'f')
CR = DB('s', 74, ['cr1'])          # 치명타 확률 (28—34)% 증가 1티어
PI = DB('s', 75, ['pie1'], 'd')    # (51—100)%의 확률로 적 관통 1티어(훼손)
RM = DB('s', 65, ['rem'])          # 잔류물을 (35—50)% 더 먼 곳에서 획득 가능(팽창하는 합금)
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
MK = L('s', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'n', ['mkS'])
FIRST = [K('투사체 피해·투사체 속도·세 번째 접두 1티어 중 먼저 뜬 것', 'Whichever of T1 projectile damage, projectile speed or a third prefix lands first')]
THIRD = K('공격 시 피해 추가·에너지 보호막·마나 최대치 1티어 중 먼저 뜬 것', 'Whichever of T1 flat attack damage, energy shield or maximum mana lands first')
REST = [K('남은 옵션 중 먼저 뜬 것', 'Whichever of the rest lands first')]
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'sl-proj7-gloves-v2', 'recipe': 'sl-proj7-gloves-v2', 'cls': CLS, 'base': 'Sirenscale Gloves', 'ilvl': 80,
 'note': ('SL 투사체 7옵션 장갑(XMYJh3CnXuY, 2026-11-13 W14 영상 전체 화면 대조) — 특출난 사이렌비늘 장갑(80) → 콜르의 사냥 → 완벽한 진화·확장 + 소멸(투사체 +2) → 완벽한 제왕 '
          '→ 보존된 갈비뼈 → 분열(투사체 +2) → 분열 + 옵션 1개 → 세를의 승리 → 카오스 오브(접두 1티어) → 상위·좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브) '
          '→ 상위 찬미 + 완벽한 엑잘(접미 치명타 확률, 잡옵마다 우측 결정화 + 심연의 에센스 → 보존된 갈비뼈 → 빛의 징조 + 소멸) → 우측 결정화 + 팽창하는 합금(1/2) '
          '→ 고대 갈비뼈 → 공개(관통 1티어, 빗나가면 빛의 징조 + 소멸). 하이엔드만(극한).'),
 'params': {'t': {'kr': '반복 목표', 'en': 'Loop target', 'values': {'1': K('1티어', 'T1')}}},
 'strategies': [{'id': 'high', 'params': {'t': 1}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {'t': 1},
               'desc': K('영상: 접두 3개·치명타 확률·관통 모두 1티어', 'Video: three prefixes, crit chance and pierce all T1')}],
 'tags': {
   'proj': {'gi': 82}, 'pd1': {'gi': 71, 'tmax': 1}, 'ps1': {'gi': 73, 'tmax': 1}, 'mf1': {'gi': 7, 'tmax': 1},
   'es1': {'gi': 8, 'tmax': 1}, 'esp1': {'gi': 9, 'tmax': 1}, 'ph1': {'gi': 13, 'tmax': 1}, 'fi1': {'gi': 15, 'tmax': 1}, 'co1': {'gi': 17, 'tmax': 1}, 'li1': {'gi': 19, 'tmax': 1},
   'third': {'anyOf': ['ph1', 'fi1', 'co1', 'li1', 'es1', 'esp1', 'mf1'], 'label': K('공격 시 피해 추가·에너지 보호막·마나 최대치 1티어', 'T1 flat attack damage, energy shield or maximum mana')},
   'pgood': {'anyOf': ['pd1', 'ps1', 'third'], 'label': K('투사체 피해·투사체 속도·세 번째 접두 1티어', 'T1 projectile damage, projectile speed or a third prefix')},
   'cr1': {'gi': 74, 'tmax': 1}, 'pie1': {'gi': 75, 'tmax': 1}, 'pieAny': {'gi': 75},
   'rem': {'gi': 65}, 'mkS': {'gi': 61},
 },
 'conds': {'pDone': {'all': [{'has': 'pd1'}, {'has': 'ps1'}, {'has': 'third'}]}, 'sClean': {'sideLt': {'side': 's', 'n': 2}}},
 'require': {'all': [{'has': 'proj'}, {'has': 'pd1'}, {'has': 'ps1'}, {'has': 'third'}, {'has': 'cr1'}, {'has': 'pie1'}, {'has': 'rem'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]}, {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0', 'xsub': ["Kolr's Hunt"], 'xroll': True,
 'finalItem': {'quality': 25, 'sockets': 2, 'exceptional': True},
}

N = []
A = lambda **d: N.append(d)
I_M1 = [KOL, PRm]; I_M2 = [KOL, J('p'), PRm]; I_R = [KOL, J('p'), PRm, J('s')]; I_D = I_R + [UN('s')]
I_F = [KOL, J('p'), PR, J('s'), UN('s')]; I0 = [KOL, PS, PR]
A(id='b0', kind='base', group='prep', pos=[0, 0], next='pk', start={'rar': 'normal', 'mods': [], 'quality': 25},
  label=K('특출난 사이렌비늘 장갑 구입 (노멀, 아이템 레벨 75 이상, 룬 소켓 2개)', 'Buy exceptional Sirenscale Gloves (normal, item level 75+, two sockets)'), item=[])
A(id='hq', kind='side', group='prep', pos=[1, 0.5], attach=['b0', 'pk'], cur='Vaal_Armourers_Infuser',
  goal=K('퀄리티 25% 이상, 비용 미포함', 'Quality 25%+, not costed'), label=K('퀄리티', 'Quality'))
A(id='pk', kind='act', group='prep', pos=[0, 1], act='rune', rune=K('콜르의 사냥', "Kolr's Hunt"),
  goal=K('콜르의 사냥 장착', "Socket Kolr's Hunt"), showText=[K('콜르 옵션이 붙을 수 있음', 'Kolr lines can roll')], label=K('룬', 'Rune'),
  edges=[{'to': 'm1'}], item=[KOL])
A(id='m1', kind='act', group='prep', pos=[0, 2], act='transmute', cur='Perfect_Orb_of_Transmutation',
  label=K('매직 첫 번째 옵션', 'First magic option'), goal=K('매직으로', 'Make it magic'), showText=[K('옵션 1개', 'One option')],
  edges=[{'to': 'm2'}], item=I_M1)
A(id='m2', kind='act', group='prep', pos=[0, 3], act='augment', cur='Perfect_Orb_of_Augmentation',
  label=K('매직 두 번째 옵션', 'Second magic option'), goal=K('접미 모든 투사체 스킬 레벨 +2', '+2 projectile skills suffix'), show=['proj'],
  edges=[{'if': {'has': 'proj'}, 'to': 'm3', 'res': 'ok'}, {'to': 'm2x', 'res': 'fail', 'label': K('빗나감 — 소멸의 오브', 'Miss: Orb of Annulment')}], item=I_M2)
A(id='m2x', kind='act', group='prep', pos=[1, 3], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('옵션 하나 지우기', 'Remove one option'), edges=[{'to': 'm2', 'label': K('다시 확장', 'Augment again')}])
A(id='m3', kind='act', group='prep', pos=[0, 4], act='regal', cur='Perfect_Regal_Orb', label=K('레어', 'Rare'), goal=K('분열하기 위해 레어로', 'Make it rare for the fracture'),
  showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'm4'}], item=I_R)
A(id='m4', kind='act', group='prep', pos=[0, 5], act='desecrate', cur='Preserved_Rib', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecration (unrevealed, cannot fracture)')], edges=[{'to': 'm5'}], item=I_D)
A(id='m5', kind='act', group='prep', pos=[0, 6], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'), showText=[K('투사체 +2가 분열되면 성공', 'Success when +2 projectile fractures')],
  edges=[{'if': {'fractured': 'proj'}, 'to': 'm6', 'res': 'ok', 'label': K('투사체 +2 분열', '+2 projectile fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another line fractured')}], item=I_F)
A(id='xj', kind='exit', group='prep', pos=[1, 6], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another line fractured: new base'),
  note=K('투사체 +2가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another line fractured: start over on a new base'))
A(id='m6', kind='cleanup', group='prep', pos=[0, 7], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=I0)
A(id='ms', kind='mark', group='main', pos=[0, 8], next='r1', label=K('아이템 제작 시작', 'Item crafting starts'), item=I0)
A(id='r1', kind='act', group='main', pos=[0, 9], act='rune', rune=K('세를의 승리', "Serle's Triumph"), slots={'s': 1},
  goal=K('세를의 승리 장착', "Socket Serle's Triumph"), showText=[K('접미 옵션 4개', 'Four suffixes')], label=K('룬', 'Rune'),
  edges=[{'to': 'c1'}], item=[KOL, SER, PS, PR])
A(id='c1', kind='act', group='main', pos=[0, 10], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'), goal=K('접두 첫 번째 옵션', 'First prefix'),
  show=['ps1'], showText=FIRST, skipIf={'has': 'pgood'}, skipTo='e1',
  skipNote=K('남은 옵션이 투사체 피해·속도·세 번째 접두 1티어면 건너뜀', 'Skip if the option left is T1 projectile damage, speed or a third prefix'),
  edges=[{'if': {'has': 'pgood'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail'}], item=[KOL, SER, PS, PR])
A(id='e1', kind='act', group='main', pos=[0, 11], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation', 'Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 두 번째·세 번째 옵션', 'Second and third prefixes'), show=['pd1', 'mf1'], showText=REST,
  edges=[{'if': {'ref': 'pDone'}, 'to': 's1', 'res': 'ok'}, {'to': 'e1x', 'res': 'fail', 'label': K('빗나감 — 소멸의 오브', 'Miss: Orb of Annulment')}],
  item=[KOL, SER, PS, PD, MF, PR])
A(id='e1x', kind='act', group='main', pos=[1, 11], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'if': {'not': {'has': 'pgood'}}, 'to': 'kz', 'res': 'fail', 'label': K('좋은 접두가 모두 지워짐 — 카오스부터', 'Every good prefix gone: back to Chaos')},
         {'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'e1', 'res': 'ok', 'label': K('접두 빈자리 2개 — 상위 찬미 + 좌측 찬미', 'Two prefixes free: Greater + Sinistral Exaltation')},
         {'to': 'e2', 'res': 'ok', 'label': K('접두 빈자리 1개 — 좌측 찬미', 'One prefix free: Sinistral Exaltation')}])
A(id='e2', kind='act', group='main', pos=[1, 12], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 세 번째 옵션', 'Third prefix'), show=['mf1'], showText=[THIRD],
  edges=[{'if': {'ref': 'pDone'}, 'to': 's1', 'res': 'ok'}, {'to': 'e1x', 'res': 'fail', 'label': K('빗나감 — 소멸의 오브', 'Miss: Orb of Annulment')}])
A(id='kz', kind='cleanup', group='main', pos=[2, 11], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep the fracture + one option'), edges=[{'to': 'c1'}])
I_S = [KOL, SER, PS, PD, MF, PR]
A(id='s1', kind='act', group='main', pos=[0, 13], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 두 번째 옵션', 'Second suffix'), show=['cr1'], showText=[K('잡옵 1개가 함께 붙음', 'One junk line comes with it')],
  edges=[{'if': {'has': 'cr1'}, 'to': 'a1', 'res': 'ok'}, {'to': 'mA', 'res': 'fail', 'label': K('빗나감 — 우측 결정화 + 심연의 에센스', 'Miss: Dextral Crystallisation + Essence of the Abyss')}],
  item=I_S + [CR, J('s')])
A(id='mA', kind='act', group='main', pos=[1, 13], act='essence', cur='Essence_of_the_Abyss', omens=['Omen_of_Dextral_Crystallisation'], ess='mkS', mark=True,
  label=K('심연', 'Abyss'), goal=K('접미 잡옵을 지우고 심연의 군주의 징표', 'A junk suffix goes for the Mark of the Abyssal Lord'),
  showText=[{'s': 's', 'kr': '심연의 군주의 징표', 'en': 'Mark of the Abyssal Lord'}], edges=[{'to': 'mB'}], item=I_S + [MK])
A(id='mB', kind='act', group='main', pos=[1, 14], act='desecrate', cur='Preserved_Rib', fromMark=True,
  label=K('훼손', 'Desecrate'), goal=K('접미 징표 훼손', 'Desecrate the suffix Mark'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'mL'}], item=I_S + [UN('s')])
A(id='mL', kind='act', group='main', pos=[1, 15], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'),
  edges=[{'if': {'ref': 'sClean'}, 'to': 's1', 'res': 'ok', 'label': K('접미 정리 끝 — 다시 엑잘', 'Suffixes clear: exalt again')},
         {'to': 'mA', 'res': 'fail', 'label': K('잡옵 남음 — 다시 심연', 'Junk left: Abyss again')}])
A(id='a1', kind='act', group='main', pos=[0, 14], act='essence', cur='Expansive_Alloy', omens=['Omen_of_Dextral_Crystallisation'], ess='rem',
  label=K('합금', 'Alloy'), goal=K('접미 잡옵을 지우고 잔류물 획득 거리', 'The junk suffix goes for remnant pickup range'),
  showText=[K('치명타 확률이 남으면 성공, 1/2', 'Success if crit chance stays, 1/2')],
  edges=[{'if': {'all': [{'has': 'cr1'}, {'not': {'has': 'pieAny'}}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'sR', 'res': 'fail', 'label': K('치명타 확률이 지워짐 — 우측 소멸의 징조', 'Crit chance gone: Omen of Dextral Annulment')}],
  item=I_S + [CR, RM])
A(id='sR', kind='act', group='main', pos=[1, 16], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=ANN, goal=ANN,
  target=K('접미를 투사체 +2만 남기기', 'Clear the suffixes down to the +2'),
  edges=[{'if': {'ref': 'sClean'}, 'to': 's1', 'res': 'ok', 'label': K('접미 정리 끝 — 다시 엑잘', 'Suffixes clear: exalt again')},
         {'to': 'sR', 'res': 'fail', 'hide': True}])
A(id='d1', kind='act', group='main', pos=[0, 17], act='desecrate', cur='Ancient_Rib', label=K('훼손', 'Desecrate'),
  goal=K('접미 네 번째 옵션(훼손)', 'Fourth suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=I_S + [CR, UN('s'), RM])
A(id='d2', kind='act', group='main', pos=[0, 18], act='reveal', label=K('공개', 'Reveal'), goal=K('훼손 옵션 확인', 'Reveal the desecrated modifier'),
  want='pie1', show=['pie1'], edges=[{'if': {'added': 'pie1'}, 'to': 'ok', 'res': 'ok'}, {'to': 'd2x', 'res': 'fail'}],
  item=I_S + [CR, PI, RM])
A(id='d2x', kind='act', group='main', pos=[1, 18], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 19], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [
  {'id': 'L0', 'nodes': ['m2', 'm2x'], 'kr': '투사체 +2 맞추기', 'en': '+2 projectile'},
  {'id': 'L1', 'nodes': ['e1', 'e1x', 'e2'], 'kr': '접두 1티어 3개', 'en': 'Three T1 prefixes', 'fold': True,
   'goal': K('접두 투사체 피해·투사체 속도 1티어 + 세 번째 접두(공격 시 피해 추가·에너지 보호막·마나 최대치 중 먼저 뜬 것) 1티어, 남은 옵션 중 먼저 뜬 것', 'T1 projectile damage and speed + a T1 third prefix (flat attack damage, energy shield or maximum mana), whichever lands first'),
   'steps': [K('상위 찬미 + 좌측 찬미 + 완벽한 엑잘티드 오브로 접두 2개', 'Greater + Sinistral Exaltation + Perfect Exalted Orb for two prefixes') | {'node': 'e1'},
             K('빗나간 접두는 징조 없는 소멸의 오브로 지움', 'A missed prefix goes with a plain Orb of Annulment') | {'node': 'e1x'},
             K('접두 빈자리가 1개면 좌측 찬미 + 완벽한 엑잘티드 오브', 'One prefix free: Sinistral Exaltation + Perfect Exalted Orb') | {'node': 'e2'}],
   'worst': K('좋은 접두가 모두 지워지면 소멸의 오브로 분열 + 옵션 1개까지 지우고 카오스 단계부터', 'Every good prefix gone: annul down to the fracture + one option, then back to Chaos') | {'to': 'kz'},
   'item': [KOL, SER, PS, PD, MF, PR]},
  {'id': 'L2', 'nodes': ['s1', 'mA', 'mB', 'mL', 'a1', 'sR'], 'kr': '접미 치명타 확률 + 합금', 'en': 'Crit chance suffix + alloy', 'fold': True,
   'goal': K('접미 치명타 확률 1티어 + 잔류물 획득 거리(팽창하는 합금)', 'T1 crit chance suffix + remnant pickup range (Expansive Alloy)'),
   'steps': [K('상위 찬미 + 완벽한 엑잘티드 오브로 접미 2개', 'Greater Exaltation + Perfect Exalted Orb for two suffixes') | {'node': 's1'},
             K('치명타 확률이 없으면 잡옵마다 우측 결정화 + 심연의 에센스', 'No crit chance: Dextral Crystallisation + Essence of the Abyss on each junk line') | {'node': 'mA'},
             K('보존된 갈비뼈로 징표를 훼손 옵션으로', 'Preserved Rib turns the Mark into a desecration') | {'node': 'mB'},
             K('빛의 징조 + 소멸의 오브로 훼손 옵션을 지우고, 접미가 투사체 +2만 남으면 다시 엑잘', 'Omen of Light + Annulment removes it; with only the +2 left, exalt again') | {'node': 'mL'},
             K('치명타 확률 + 잡옵 1개면 우측 결정화 + 팽창하는 합금, 1/2', 'Crit chance + one junk: Dextral Crystallisation + Expansive Alloy, 1/2') | {'node': 'a1'},
             K('합금이 치명타 확률을 지우면 우측 소멸의 징조 + 소멸의 오브로 접미를 비우고 다시', 'If the alloy took crit chance: Dextral Annulment until the suffixes are clear, then again') | {'node': 'sR'}],
   'item': [KOL, SER, PS, PD, MF, PR, CR, RM]},
  {'id': 'L3', 'nodes': ['d1', 'd2', 'd2x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]
g['finals'] = [{'id': 'high', 'tier': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
                'lines': [{'tag': 'pd1'}, {'tag': 'ps1'}, {'tag': 'third'}, {'tag': 'proj', 'fr': True}, {'tag': 'cr1'}, {'tag': 'pie1', 'des': True}, {'tag': 'rem', 'ess': True}]}]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
