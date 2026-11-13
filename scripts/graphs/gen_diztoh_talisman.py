# G11 2026-11-13: Diztoh +5 마지 부적(영상 p6HIFmJ9mRU, 8:18) 플로우차트 생성기 — 영상 한 회차 그대로(완성품 5:16)
# 근거: scratchpad review/G11/diztoh-talisman-v2/timeline.md, frames/*.jpg (영상 전체, 화면 확대)
# 실행: cd scripts/graphs && python3 gen_diztoh_talisman.py  → diztoh-talisman-v2.json (gen_batch6.py 끝에서 자동 호출)
# 상자 id는 옛 단계 레시피(t1~t11·t5b)와 겹치지 않게.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-talisman-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
C = json.load(open(f'{H}/../../site/data/c/Talismans.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, tier=1):
    t = C['groups'][gi]['t'][tier - 1]
    return t[4].replace('\n', ' · '), t[5].replace('\n', ' · ')

MEL = L('s', *T(10), 'n', ['melee'])
FIRE = L('p', *T(4, 3), 'n', ['fire3'])
CRIT = L('s', T(51)[0] + ' (제작 옵션)', T(51)[1] + ' (crafted)', 'c', ['crit'])
UN = L('s', '훼손 옵션 (미공개, 아마나무)', 'Desecrated (unrevealed, Amanamu)', 'u')
AS = L('s', T(32)[0] + ' (훼손)', T(32)[1] + ' (desecrated)', 'd', ['as'])
LT = L('p', '번개 피해 추가 1~2티어', 'T1–2 added lightning damage', 'n', ['light2'])
RPJ = L('p', '랜덤 옵션', 'Random option', 'j')    # m 'j': graph2recipe가 엑잘 자리(접두)를 이 줄에서 읽음
RSJ = L('s', '랜덤 옵션', 'Random option', 'j')
RP = L('p', '랜덤 옵션', 'Random option', 'n')

g = {
 'id': 'diztoh-talisman-v2', 'recipe': 'diztoh-talisman-v2', 'cls': 'Talismans', 'base': 'Maji Talisman', 'ilvl': 81,
 'note': ('2026-11-13 G11 영상 전체 화면 대조(p6HIFmJ9mRU 8:18, 근거 scratchpad review/G11/diztoh-talisman-v2/timeline.md). 영상 한 회차: '
          '거래소 매직 마지 부적(근접 +5 1티어 + 화염 피해 추가 3티어, 아이템 레벨 81, 0:20~0:48) → 상위 추구의 에센스 = 치명타 확률 +3.68%(1:04) → 우측 강령술의 징조(1:12)·군왕의 징조(1:20) + 턱뼈(1:23, 사용 장면 편집) → '
          '공개: 아마나무 접미 3개 = 공격 속도(1:36, 심연의 메아리는 실수로 켰다고 말함) → 상위 찬미의 징조 + 완벽한 엑잘(2:22~2:32, 공격 원소 피해 1티어·번개 피해) → 숫돌 퀄리티 20%·신성한 오브·철 룬(2:45~3:23, 마무리) → '
          '여유가 있으면: 좌측 소멸의 징조 + 소멸의 오브 3번으로 접두 3개 모두 지움(3:28~3:44, 징조 4→1) → 완벽한 엑잘 = 번개 피해 2티어(3:56, 별로면 좌측 말소의 징조 + 카오스 오브) → 상위 찬미 + 완벽한 엑잘 = 물리·냉기 피해 3티어(4:18~4:28) → '
          '세를의 승리(4:44) → 완벽한 엑잘 = 정확도·시야 반경(5:05~5:16, 치명타 피해 노림, 그대로 둠). 5:20 이후 사원 타락·건축가의 오브(가시 부적이 됨)는 레시피 밖. '
          '내부 결정: 턱뼈 등급 = 보존된 턱뼈(화면 이름 확인 못 함), 숫돌 개수 20개(희귀 1%씩 가정), 철 룬·신성한 오브는 마무리라 뺌(정책 9장, 신성한 오브는 선택 상자), 말소 카오스 = 카오스 오브(자막 그대로, 등급 확인 못 함). '
          '등급(밸런스·에센셜): 밸런스 = 영상 완성품 길, 첫 접두를 피해 접두 7개 중 하나 1~2티어까지 좌측 말소 + 카오스로 다시(11-13 오후 새 정책 A: 영상 3:56 "별로면" = 좋은 피해 옵션이면 받아들임, 카드는 영상 결과 번개 피해 2티어), 에센셜 = 영상 3:20의 가성비 길(첫 상위 찬미 엑잘 결과 그대로, 접두 지우기 건너뜀).'),
 'params': {'L': {'kr': '첫 접두', 'en': 'First prefix', 'values': {'1': K('피해 접두 1~2티어까지 다시', 'Reroll to a T1–2 damage prefix'), '0': K('나오는 대로', 'Keep what comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1}}, {'id': 'ess', 'params': {'L': 0}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0}, 'tier': 'ess',
               'desc': K('영상 3:20 가성비 길: 첫 상위 찬미 엑잘 결과 그대로, 세를의 승리 + 엑잘', 'The video’s budget path (3:20): keep the first double exalt, then Serle’s Triumph + exalt')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1}, 'tier': 'bal',
               'desc': K('영상 완성품: 첫 접두가 피해 옵션 1~2티어가 될 때까지 좌측 말소 + 카오스', 'The video item: Sinistral Erasure + Chaos until the first prefix is a T1–2 damage modifier')}],
 'tags': {'melee': {'gi': 10, 'tmax': 1}, 'fire3': {'gi': 4, 'tmax': 3}, 'crit': {'gi': 51}, 'as': {'gi': 32}, 'light2': {'gi': 7, 'tmax': 2},
          # 11-13 오후 새 정책 A: 3:56 '별로면 좌측 말소 + 카오스' = 피해 접두면 받아들임 → 성공 조건은 피해 접두 7개 중 하나(1~2티어). 상자·카드는 영상 성공 회차의 번개 피해(light2)
          'phys2': {'gi': 3, 'tmax': 2}, 'fire2': {'gi': 4, 'tmax': 2}, 'cold2': {'gi': 5, 'tmax': 2}, 'pinc2': {'gi': 8, 'tmax': 2}, 'pacc2': {'gi': 9, 'tmax': 2}, 'aele2': {'gi': 23, 'tmax': 2},
          'dmg2': {'anyOf': ['light2', 'phys2', 'fire2', 'cold2', 'pinc2', 'pacc2', 'aele2'],
                   'shown': 'light2',   # 성공 회차 옵션(S4 shown): 영상 3:56 번개 피해 2티어
                   'label': K('피해 접두 1~2티어(번개·물리·화염·냉기 추가, 물리 %, 물리 % + 정확도, 공격 원소 %)', 'T1–2 damage prefix (added lightning, physical, fire or cold, physical %, physical % + accuracy, attack elemental %)')}},
 'require': {'all': [{'has': 'melee'}, {'has': 'crit'}, {'has': 'as'}, {'full': 'p'}, {'full': 's'}, {'any': [{'param': {'L': 0}}, {'has': 'dmg2'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (0:20~0:48) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'magic', 'mods': [{'tag': 'fire3'}, {'tag': 'melee'}]},
  label=K('근접 +5 + 화염 피해 추가 매직 마지 부적 구입 (아이템 레벨 81)', 'Buy a magic Maji Talisman with +5 melee and added fire (item level 81)'), item=[FIRE, MEL])
# ---------------- 옵션 추가 작업 (1:04~5:16) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='e1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[FIRE, MEL])
A(id='e1', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Greater_Essence_of_Seeking', ess='crit', label=K('에센스', 'Essence'),
  goal=K('레어로 + 접미 두 번째 옵션', 'Make it rare + second suffix'),
  showText=[{'s': 's', 'kr': T(51)[0] + ' (제작 옵션)', 'en': T(51)[1] + ' (crafted)'}], edges=[{'to': 'd1'}], item=[FIRE, MEL, CRIT])
A(id='d1', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Dextral_Necromancy', 'Omen_of_the_Liege'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세 번째 옵션(훼손, 아마나무)', 'Third suffix (desecrated, Amanamu)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개, 아마나무)', 'en': 'Desecrated (unrevealed, Amanamu)'}], edges=[{'to': 'r1'}], item=[FIRE, MEL, CRIT, UN])
A(id='r1', kind='act', group='main', pos=[0, 4.4], act='reveal', want='as', label=K('공개', 'Reveal'),
  goal=K('접미 공격 속도 (아마나무 옵션 3개가 모두 나옴)', 'Attack speed suffix (all three Amanamu options show)'), show=['as'],
  edges=[{'to': 'x1'}], item=[FIRE, MEL, CRIT, AS])
A(id='x1', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째·세 번째 옵션', 'Second and third prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'q1'}], item=[FIRE, RPJ, RPJ, MEL, CRIT, AS])
A(id='q1', kind='act', group='main', pos=[0, 6.4], act='quality', cur='Blacksmiths_Whetstone', count=20, q=20, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 20%', 'Quality 20%'), showText=[K('대장장이의 숫돌 20개', '20 Blacksmith’s Whetstones')], edges=[{'to': 'a1'}],
  item=[FIRE, RP, RP, MEL, CRIT, AS])
A(id='dv', kind='side', group='main', pos=[1, 6.9], act='divine', cur='Divine_Orb', attach=['q1', 'a1'],
  label=K('수치 올리기', 'Divine the values'), goal=K('옵션 수치 다시 굴리기 (선택)', 'Reroll option values (optional)'),
  showText=[K('공격 속도 17% 이상 노림', 'Aim for 17% attack speed or more')])
A(id='a1', kind='act', group='main', pos=[0, 7.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  goal=K('좌측 소멸의 징조로 접두 3개 모두 지우기', 'Sinistral Annulment until all three prefixes are gone'),
  skipIf={'param': {'L': 0}}, skipTo='rn', skipNote=K('에센셜은 건너뜀 — 앞 엑잘 결과 그대로', 'Essential skips this: keep the earlier exalt'),
  showText=[{'s': 'p', 'kr': '접두 3개 제거 (3번)', 'en': 'Remove all three prefixes (three times)'}],
  edges=[{'if': {'sideLt': {'side': 'p', 'n': 1}}, 'to': 'x2'}, {'to': 'a1', 'hide': True}], item=[MEL, CRIT, AS])
A(id='x2', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 첫 번째 옵션 — 번개 피해 추가 1~2티어', 'First prefix: T1–2 added lightning'), show=['dmg2'],
  edges=[{'if': {'added': 'dmg2'}, 'to': 'x3', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'x3', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'x2c', 'res': 'fail'}], item=[LT, MEL, CRIT, AS],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 첫 번째 옵션 — 나오는 대로', 'First prefix: keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [RP, MEL, CRIT, AS]}}])
A(id='x2c', kind='act', group='main', pos=[1, 8.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Sinistral_Erasure'], label=K('좌측 말소 + 카오스', 'Sinistral Erasure + Chaos'),
  goal=K('접두 다시 굴리기', 'Reroll the prefix'), show=['dmg2'],
  edges=[{'if': {'has': 'dmg2'}, 'to': 'x3', 'res': 'ok'}, {'to': 'x2c', 'res': 'fail', 'hide': True}])
A(id='x3', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째·세 번째 옵션', 'Second and third prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'rn'}], item=[LT, RPJ, RPJ, MEL, CRIT, AS], over=[{'param': {'L': 0}, 'set': {'item': [RP, RPJ, RPJ, MEL, CRIT, AS]}}])
A(id='rn', kind='act', group='main', pos=[0, 10.4], act='rune', label=K('룬', 'Rune'), goal=K('세를의 승리 장착 (접미 +1)', 'Socket Serle’s Triumph (+1 suffix)'),
  showText=[K('접미 옵션 4개', 'Four suffixes')], rune=K('세를의 승리', 'Serle’s Triumph'), slots={'s': 1}, edges=[{'to': 'x4'}],
  item=[LT, RP, RP, MEL, CRIT, AS], over=[{'param': {'L': 0}, 'set': {'item': [FIRE, RP, RP, MEL, CRIT, AS]}}])
A(id='x4', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 네 번째 옵션', 'Fourth suffix'), showText=[{'s': 's', 'kr': '랜덤 옵션', 'en': 'Random option'}],
  edges=[{'to': 'ok'}], item=[LT, RP, RP, MEL, CRIT, AS, RSJ], over=[{'param': {'L': 0}, 'set': {'item': [FIRE, RP, RP, MEL, CRIT, AS, RSJ]}}])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['x2', 'x2c'], 'kr': '접두 첫 번째 옵션', 'en': 'First prefix'}]
g['finals'] = [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'dmg2'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
             {'tag': 'melee'}, {'tag': 'crit'}, {'tag': 'as', 'des': True}, {'side': 's', 'random': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'fire3'}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
             {'tag': 'melee'}, {'tag': 'crit'}, {'tag': 'as', 'des': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
