# G5 2026-11-13: SaVeQ 부재 목걸이(S4sflKbsA8A, 20:20, 0.5.5) 플로우차트 생성기 — 영상 성공 회차(근접 목걸이 'Pain Scarab') 한 줄
# 근거: scratchpad review/G5/saveq-absent-amulet-v2/timeline.md, frames/ (영상 0:00~20:20 화면 대조)
# 실행: cd scripts/graphs && python3 gen_saveq_absent_amulet.py  → saveq-absent-amulet-v2.json
# 등급: 난이도 3(어려움, scripts/difficulty.py) → 밸런스·에센셜(정책 10장 C11). 하이엔드는 build_recipes가 어차피 뺌.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-absent-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CRn = L('s', '치명타 피해 보너스 (35—39)% 증가', '(35—39)% increased Critical Damage Bonus', 'n', ['crit'])   # 분열 전
CR = L('s', '치명타 피해 보너스 (35—39)% 증가', '(35—39)% increased Critical Damage Bonus', 'f', ['crit'])    # 분열
ML = L('s', '모든 근접 스킬 레벨 +3', '+3 to Level of all Melee Skills', 'n', ['melee'])                        # 12:02 영상 결과(근접 목걸이)
MQ = L('p', '최대 퀄리티 +20%', '+20% to Maximum Quality', 'c', ['maxQ'])
DEF = L('p', '전역 방어도, 회피, 에너지 보호막 (20—30)% 증가', '(20—30)% increased Global Armour, Evasion and Energy Shield', 'c', ['def'])
SP = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'd', ['spirit'])                                          # 18:15 가격 확인 화면: 정신력 47 1티어
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
LIGHT = K('소멸의 오브 사용', 'Use an Orb of Annulment')
SKL = K('모든 근접·투사체 스킬 레벨 +3', '+3 to Level of all Melee or Projectile Skills')

g = {
 'id': 'saveq-absent-amulet-v2', 'recipe': 'saveq-absent-amulet-v2', 'cls': 'Amulets', 'base': 'Absent Amulet', 'ilvl': 79,
 'basePrice': {'Divine_Orb': 36},
 'note': ('2026-11-13 G5 영상 전체 화면 대조(0:00~20:20). 성공 회차 = 근접 목걸이(Pain Scarab, 18:15 가격 확인 화면: 정신력 47 1티어·전역 방어 22%·치명타 피해 보너스 39%·근접 +4·아이템 레벨 79). '
          '준비: 아이템 레벨 79 노멀 부재 목걸이(6:10, 개당 35~38 div 자막 8:00) → 옵션 1개 레어(제왕 장면은 화면에 없음, 이미 준비한 베이스) → 카오스 오브 반복으로 치명타 피해 보너스 1티어(7:32 창고·인벤토리 카오스 오브, 7:50 38%) → '
          '엑잘로 옵션 2개(9:08 화면: 주문 피해 13% 접두·지능 +12 접미, 오브 등급·징조는 화면에 없음 — 상위 찬미 가정) → 빗장뼈 훼손(접두, 뼈 등급은 화면에 없음 — 보존된 빗장뼈 가정) → 분열 6개 중 3개 성공(9:29) → 분열 + 옵션 1개(9:58 화면: 최대 마나, 정리 장면은 화면에 없음). '
          '본 제작: 카오스 오브 반복으로 근접·투사체 +3 중 먼저 뜬 것(12:02 근접 +3) → 좌측 찬미(12:22 채팅) + 엑잘티드 오브(12:10 툴팁, 일반 등급) → 접두 주문 피해 5티어 → 좌측 결정화 + 균열의 에센스로 최대 퀄리티(12:25 채팅) → '
          '공격 퀄리티 40%(12:33 27%·12:40 40%, 기폭제 이름 툴팁은 못 봄 — 품질 종류 Attack Modifiers라 강탈자 기폭제) → 절사의 징조(12:45 채팅) + 카오스 오브로 최대 퀄리티 제거·새 접두(자막: 마나) → 좌측 결정화 + 완벽한 강화의 에센스(12:48 툴팁)로 전역 방어 22%, 근접 +4(12:53) → '
          '고대 빗장뼈(자막 13:40·15:00, 툴팁은 못 봄) 훼손 + 심연의 메아리 공개(14:26 채팅) 정신력, 빗나가면 빛의 징조 + 소멸의 오브(15:18 채팅, 14:44 소멸의 오브 툴팁) — 두 목걸이 합쳐 약 28번(17:35 자막). '
          '두 번째 목걸이(투사체 +3)는 같은 흐름에 방어 퀄리티(13:20 Defence Modifiers 36%) — 꿀팁 후보. 완벽한 유동체·신성한 오브(18:00~19:10)는 정책 14장대로 뺌, 축성(19:30 둘 다 실패)은 완성 뒤 선택 상자(비용 미포함). '
          '내부 결정: 카오스 목표 = 근접·투사체 +3 중 먼저 뜬 것(영상 10:00 자막 "둘 중 아무거나"), 11-13 오후 새 정책(P10) A: 상자·아이템 칸·카드는 성공 회차 근접 +3(shown), 투사체는 꿀팁 줄. B: 정신력 공개는 영상이 빛의 징조로 다시 해서(15:18, 약 28번) 밸런스 반복 유지. D: 밸런스 780 vs 에센셜 683(12.5%), 카드의 정신력 줄이 달라 둘 다 유지. 분열 준비 엑잘 등급·징조와 첫 훼손 뼈 등급은 화면에 없어 가정.'),
 'params': {'spT': {'kr': '정신력', 'en': 'Spirit', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('공개 한 번, 나오는 대로', 'One reveal, keep what comes')}}},
 'strategies': [{'id': 'bal', 'params': {'spT': 2}}, {'id': 'ess', 'params': {'spT': 4}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'spT': 4}, 'tier': 'ess',
               'desc': K('접두 훼손 공개 한 번, 빛의 징조 없음', 'One prefix reveal, no Omen of Light')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'spT': 2}, 'tier': 'bal',
               'desc': K('정신력 1~2티어까지 빛의 징조로 다시 (영상은 1티어)', 'Spirit T1–2 with Omen of Light retries (the video went for T1)')}],
 'tags': {'crit': {'gi': 25, 'tmax': 1}, 'melee': {'gi': 19, 'tmax': 1}, 'proj': {'gi': 20, 'tmax': 1},
          'SK': {'anyOf': ['melee', 'proj'], 'shown': 'melee', 'label': SKL},
          'maxQ': {'gi': 81}, 'def': {'gi': 74}, 'spirit': {'gi': 28, 'tmax': '$spT'}, 'spirit2': {'gi': 28, 'tmax': 2}},
 'require': {'all': [{'has': 'crit'}, {'has': 'SK'}, {'has': 'def'}, {'any': [{'has': 'spirit'}, {'param': {'spT': 4}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h0',
 'finals': [{'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'def'}, {'tag': 'spirit2', 'des': True}, {'tag': 'crit', 'fr': True}, {'tag': 'SK'}]},
            {'id': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
             'lines': [{'tag': 'def'}, {'side': 'p', 'random': True}, {'tag': 'crit', 'fr': True}, {'tag': 'SK'}]}],
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h0', kind='base', group='prep', pos=[0, 0], next='r0', start={'rar': 'normal'},
  label=K('아이템 레벨 79 노멀 부재 목걸이', 'Item level 79 normal Absent Amulet'), item=[])
A(id='r0', kind='act', group='prep', pos=[0, 1], act='regal', cur='Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 전환 (옵션 1개)', 'Rare with one modifier'), showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}],
  edges=[{'to': 'c1'}], item=[J('p')])
A(id='c1', kind='act', group='prep', pos=[0, 2], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('치명타 피해 보너스 1티어', 'T1 Critical Damage Bonus'), show=['crit'],
  edges=[{'if': {'added': 'crit'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[CRn])
A(id='e1', kind='act', group='prep', pos=[0, 3], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('잡옵 2개', 'Two junk modifiers'), showText=[{'kr': '잡옵 2개', 'en': 'Two junk'}],
  edges=[{'to': 'f1'}], item=[J('p'), CRn, J('s')])
A(id='f1', kind='act', group='prep', pos=[0, 4], act='desecrate', cur='Preserved_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 분열되지 않음)', 'en': 'Desecrated (unrevealed, cannot fracture)'}],
  edges=[{'to': 'f2'}], item=[J('p'), UN('p'), CRn, J('s')])
A(id='f2', kind='act', group='prep', pos=[0, 5], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('치명타 피해 보너스가 분열되면 성공', 'Success when the Critical Damage Bonus fractures')],
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'crit'}, 'to': 'f4', 'res': 'ok', 'label': K('치명타 피해 보너스 분열', 'Critical Damage Bonus fractured')},
         {'to': 'xs', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), UN('p'), CR, J('s')])
A(id='xs', kind='exit', group='prep', pos=[1, 5], simTo='h0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('잘못 분열된 목걸이는 재련하거나 되팔고 새 베이스로 처음부터', 'Reforge or sell it, then start over on a new base'))
A(id='f4', kind='cleanup', group='prep', pos=[0, 6], keep=[], maxJunk=1, label=LIGHT, goal=LIGHT,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('p'), CR])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 7.4], next='v2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), CR])
A(id='v2', kind='act', group='main', pos=[0, 8.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 두 번째 옵션 — 모든 근접 스킬 레벨 +3', 'Second suffix: +3 to Level of all Melee Skills'), show=['SK'],   # 11-13 P10 새 정책 A: 성공 조건은 근접·투사체 묶음(SK), 화면은 성공 회차 근접(shown), 투사체는 자동 꿀팁 줄
  edges=[{'if': {'has': 'SK'}, 'to': 'v3', 'res': 'ok'}, {'to': 'v2', 'res': 'fail', 'hide': True}], item=[CR, ML])
A(id='v3', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 잡옵', 'A junk prefix'), showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}], edges=[{'to': 'v4'}], item=[J('p'), CR, ML])
A(id='v4', kind='act', group='main', pos=[0, 10.4], act='essence', cur='Essence_of_the_Breach', ess='maxQ', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 최대 퀄리티 +20%', 'The junk prefix goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'v5'}], item=[MQ, CR, ML])
A(id='v5', kind='act', group='main', pos=[0, 11.4], act='quality', cur='Reaver_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('공격 퀄리티 40% — 근접 스킬 +4', 'Attack quality 40%: Melee Skills +4'), showText=[K('강탈자 기폭제 40개', '40 Reaver Catalysts')],
  edges=[{'to': 'v6'}], item=[MQ, CR, ML])
A(id='v6', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Whittling'], label=K('카오스', 'Chaos'),
  goal=K('최대 퀄리티를 지우고 접두 잡옵', 'Maximum Quality out, a junk prefix in'), showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}],
  edges=[{'to': 'v7'}], item=[J('p'), CR, ML])
A(id='v7', kind='act', group='main', pos=[0, 13.4], act='essence', cur='Perfect_Essence_of_Enhancement', ess='def', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 전역 방어 %', 'The junk prefix goes for global defences %'),
  showText=[{'s': 'p', 'kr': '전역 방어도, 회피, 에너지 보호막 % (제작 옵션)', 'en': 'Global Armour, Evasion and Energy Shield % (crafted)'}],
  edges=[{'to': 'v8'}], item=[DEF, CR, ML])
A(id='v8', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Ancient_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손)', 'Second prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'v9'}], item=[DEF, UN('p'), CR, ML])
A(id='v9', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='spirit2', label=K('공개', 'Reveal'),
  goal=K('접두 정신력', 'Spirit prefix'), show=['spirit2'],
  edges=[{'if': {'added': 'spirit'}, 'to': 'ok', 'res': 'ok'}, {'if': {'param': {'spT': 4}}, 'to': 'ok', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'v9x', 'res': 'fail'}], item=[DEF, SP, CR, ML],
  over=[{'param': {'spT': 4}, 'set': {'goal': K('접두 훼손 옵션 공개 — 나오는 대로', 'Reveal the prefix desecration: keep what comes'), 'show': [],
         'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [DEF, L('p', '랜덤 옵션', 'Random option', 'd'), CR, ML]}}])
A(id='v9x', kind='act', group='main', pos=[1, 15.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'v8', 'label': K('다시 훼손', 'Desecrate again')}])
# 축성 = 선택 단계(정책 14장: 마지막 '선택' 한 줄, 비용 미포함). 영상 19:30 두 목걸이 모두 실패
A(id='vs', kind='side', group='main', pos=[1, 16.4], attach=['ok', 'ok'], cur='Divine_Orb', omens=['Omen_of_Sanctification'],
  goal=K('축성으로 스킬 레벨 올리기, 선택·비용 미포함', 'Sanctify for a higher skill level, optional, not costed'), label=K('축성', 'Sanctify'))
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['v8', 'v9', 'v9x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
