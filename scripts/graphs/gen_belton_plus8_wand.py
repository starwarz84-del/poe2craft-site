# G7 2026-11-13: Belton +8 결투 마법봉(j0FeuX0NZQI, 33:42) 플로우차트 생성기 — 영상 성공 회차(자기 마법봉) 한 줄
# 근거: scratchpad review/G7/belton-plus8-wand-v2/timeline.md, frames/ (영상 0:00~33:42 화면 대조)
# 실행: cd scripts/graphs && python3 gen_belton_plus8_wand.py  → belton-plus8-wand-v2.json (gen_batch6.py 끝에서도 자동 호출, 이 아이템 구간을 대신함)
# 상자 id는 옛 레시피(recipes_v5_belton-plus8-wand.py, b1~b7)·옛 그래프(b3x·b3c·b6x·b6d)와 겹치지 않게 지음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/belton-plus8-wand-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상에 실제로 나온 옵션
L4 = L('s', '모든 주문 스킬 레벨 +4', '+4 to Level of all Spell Skills', 'n', ['l4'])                               # 0:40
SPE = L('p', '주문 피해 (75—89)% 증가 (상위 마술의 에센스)', '(75—89)% increased Spell Damage (Greater Essence of Sorcery)', 'c', ['sorc'])   # 0:48 78%
ALn = L('s', '시전 속도 (26—31)% 증가 · 원소 피해의 (7—11)%를 추가 냉기 피해로 획득 (초월의 합금)',
        '(26—31)% increased Cast Speed · Gain (7—11)% of Elemental Damage as Extra Cold Damage (Transcendent Alloy)', 'c', ['trans'])   # 0:58
AL = L('s', '시전 속도 (26—31)% 증가 · 원소 피해의 (7—11)%를 추가 냉기 피해로 획득 (초월의 합금, 분열)',
       '(26—31)% increased Cast Speed · Gain (7—11)% of Elemental Damage as Extra Cold Damage (Transcendent Alloy, fractured)', 'f', ['trans'])   # 2:20
FD = L('p', '화염 피해 (35—44)% 증가', '(35—44)% increased Fire Damage', 'j')                                       # 1:10 엑잘 결과(천공의 합금이 지움)
CE = L('p', '마나 최대치 +(142—188) · 모든 주문 스킬 레벨 +1 (천공의 합금)', '+(142—188) to maximum Mana · +1 to Level of all Spell Skills (Celestial Alloy)', 'c', ['cel'])   # 1:20
ED = L('p', '원소 피해 (74—89)% 증가 (훼손, 자리 막기)', '(74—89)% increased Elemental Damage (desecrated, blocker)', 'd', ['blk'])   # 3:06
XC = L('p', '피해의 (25—27)%를 추가 냉기 피해로 획득', 'Gain (25—27)% of Damage as Extra Cold Damage', 'n', ['xC2'])   # 4:00
MR = L('s', '마나 재생 속도 (60—69)% 증가 (훼손)', '(60—69)% increased Mana Regeneration Rate (desecrated)', 'd', ['rg1'])   # 6:18
CH = L('p', '카오스 피해 (75—89)% 증가', '(75—89)% increased Chaos Damage', 'j')                                   # 6:55 마지막 엑잘(그대로 둠)
RN = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V_ESS = {'param': {'L': 0}}

PREL = K('추가 화염·냉기·번개 피해, 주문 피해, 주문 피해와 마나', 'Extra fire, cold or lightning damage, spell damage, or spell damage + mana')
SUFL = K('마나 재생 속도·주문 치명타 명중 확률·주문 치명타 피해 보너스', 'Mana regeneration, spell crit chance or spell crit damage bonus')

g = {
 'id': 'belton-plus8-wand-v2', 'recipe': 'belton-plus8-wand-v2', 'cls': 'Wands', 'base': 'Dueling Wand', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 61},
 'note': ('2026-11-13 G7 영상 전체(0:00~33:42) 화면 대조. 성공 회차 = 자기 마법봉 한 줄: 모든 주문 +4 매직 결투 마법봉(아이템 레벨 82, 퀄리티 21%, 0:30 "61 디바인에 샀다", 0:40) → '
          '상위 마술의 에센스로 레어 + 주문 피해(0:44~0:48) → 아스트리드의 창의성(0:58 툴팁 "제작 옵션 1개 추가") → 좌측 결정화 + 초월의 합금(주문 피해를 지움, 0:56~0:58) → '
          '좌측 찬미 + 엑잘티드 오브(화염 피해 잡옵, 1:06~1:10) → 좌측 결정화 + 천공의 합금(1:16~1:20) → 좌측 강령술 + 군왕의 징조 + 보존된 턱뼈(1:24~1:30, 자막 "일반적인 턱뼈") → '
          '신성한 오브(1:58, 수치만 — 뺌) → 분열(2:13~2:20, 초월의 합금이 분열 = 영상이 말한 최악) → 심연의 메아리 공개 = 원소 피해 87%로 접두 자리 막기(2:58~3:06) → '
          '좌측 찬미 + 완벽한 엑잘(3:20~3:52 구입, 4:00 추가 냉기 26% 2티어) → 빛의 징조 + 소멸의 오브로 막기 제거(5:05~5:20) → 우측 강령술 + 고대 턱뼈 + 메아리(5:40, 채팅 소모 메시지) → '
          '공개 = 마나 재생 64% 1티어(5:45~5:49) → 완벽한 엑잘 마지막 접두 = 카오스 피해 84% 3티어, 그대로 둠(6:25~6:55). '
          '7:30~33:42는 설명(+4가 분열됐을 때 카오스로 주문 피해, Craft of Exile 시뮬, 룬 +1·알두르 +2로 +8, 노멀 마법봉에 진화·확장으로 +4 만들기 비용, 분열 기대값)이라 꿀팁 후보. '
          '분열 결과가 +4나 천공의 합금이면 같은 비용으로 이어 간다고 가정(영상 25:30 "셋 다 가치 있음", 분열 실패 = 없음). '
          '등급(정책 10장): 난이도 3 → 밸런스·에센셜. 밸런스 = 세 번째 접두 1~2티어(좌측 소멸의 징조로 다시), 접미 공개·마지막 접두는 나오는 대로(C17 2번, 영상도 3티어 그대로). '
          '11-13 오후 새 정책(P10): (B) 영상 5:43~5:49 접미 공개는 메아리 다시 뽑기 한 번으로 받고 빛의 징조로 다시 하지 않아 접미 공개 빛의 징조 반복(옛 13.A)을 뺌 — 두 등급 모두 결과 그대로(카드 랜덤 옵션). 막기 제거(빛의 징조 + 소멸)는 영상 장면이라 그대로. (D) 그러면 밸런스 95.1 vs 에센셜 87.1 div(약 8%)라 밸런스 하나만(옛 시뮬 106.7/87.1, 에센셜 = 반복 없이 상위 엑잘). '
          '에센셜 = 반복 없음, 공개·엑잘 결과 그대로, 엑잘은 상위 엑잘티드 오브.'),
 'params': {
  'L': {'kr': '반복', 'en': 'Repeats', 'values': {'1': K('빛의 징조·소멸의 징조로 다시', 'Retry with Light / Annulment omens'), '0': K('결과 그대로', 'Keep whatever comes')}},
  'xT': {'kr': '세 번째 접두', 'en': 'Third prefix', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('나오는 대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1, 'xT': 2}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1, 'xT': 2}, 'tier': 'bal',
   'desc': K('세 번째 접두 1~2티어까지 다시, 접미 공개·마지막 접두는 영상처럼 나오는 대로', 'Third prefix retried to T1–2; suffix reveal and last prefix kept as the video')}],
 'tags': {
  'l4': {'gi': 10, 'tmax': 1}, 'trans': {'gi': 60}, 'cel': {'gi': 59}, 'sorc': {'gi': 44}, 'blk': {'gi': 30},
  'xF': {'gi': 26, 'tmax': '$xT'}, 'xC': {'gi': 27, 'tmax': '$xT'}, 'xL': {'gi': 28, 'tmax': '$xT'}, 'sd': {'gi': 3, 'tmax': '$xT'}, 'hy': {'gi': 4, 'tmax': '$xT'},
  'pre': {'anyOf': ['xF', 'xC', 'xL', 'sd', 'hy'], 'shown': 'xC', 'label': PREL},
  # 아이템 칸·완성 카드용(고정 티어)
  'xC2': {'gi': 27, 'tmax': 2}, 'rg1': {'gi': 16, 'tmax': 1},
  'xF2': {'gi': 26, 'tmax': 2}, 'xL2': {'gi': 28, 'tmax': 2}, 'sd2': {'gi': 3, 'tmax': 2}, 'hy2': {'gi': 4, 'tmax': 2},
  'pre2': {'anyOf': ['xF2', 'xC2', 'xL2', 'sd2', 'hy2'], 'shown': 'xC2', 'label': K('추가 화염·냉기·번개 피해, 주문 피해, 주문 피해와 마나 1~2티어', 'T1–2 extra fire, cold or lightning damage, spell damage, or spell damage + mana')},
 },
 'require': {'all': [{'has': 'l4'}, {'has': 'trans'}, {'has': 'cel'}, {'full': 'p'}, {'full': 's'},
                     {'any': [V_ESS, {'has': 'pre'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 2]}],
 'start': 'z0',
 'finalItem': {'quality': 21, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 (영상 0:30~2:20) ----------------
A(id='z0', kind='base', group='prep', pos=[0, 0], next='z1', start={'rar': 'magic', 'mods': ['l4']},
  label=K('모든 주문 스킬 레벨 +4 매직 결투 마법봉 구입 (아이템 레벨 82, 퀄리티 21%)', 'Buy a magic Dueling Wand with +4 all spell skills (item level 82, 21% quality)'), item=[L4])
A(id='z1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Sorcery', ess='sorc', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 주문 피해', 'Rare + spell damage prefix'), showText=[{'s': 'p', 'kr': '주문 피해 (75—89)% 증가 (제작 옵션)', 'en': '(75—89)% increased Spell Damage (crafted)'}],
  edges=[{'to': 'zr'}], item=[SPE, L4])
A(id='zr', kind='act', group='prep', pos=[0, 2], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'z2'}], item=[SPE, L4, RN])
A(id='z2', kind='act', group='prep', pos=[0, 3], act='essence', cur='Transcendent_Alloy', ess='trans', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 주문 피해를 지우고 접미 초월의 합금', 'The spell damage prefix goes for the Transcendent Alloy suffix'),
  showText=[{'s': 's', 'kr': '시전 속도 · 원소 피해의 %를 추가 냉기 피해로 획득 (제작 옵션)', 'en': 'Cast speed · elemental damage as extra cold (crafted)'}],
  edges=[{'to': 'z3'}], item=[L4, ALn, RN])
A(id='z3', kind='act', group='prep', pos=[0, 4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 잡옵 1개 — 천공의 합금이 지울 자리', 'One junk prefix for the Celestial Alloy to remove'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'z4'}], item=[FD, L4, ALn, RN])
A(id='z4', kind='act', group='prep', pos=[0, 5], act='essence', cur='Celestial_Alloy', ess='cel', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 잡옵을 지우고 천공의 합금', 'The junk prefix goes for the Celestial Alloy'),
  showText=[{'s': 'p', 'kr': '마나 최대치 · 모든 주문 스킬 레벨 +1 (제작 옵션)', 'en': 'Maximum mana · +1 all spell skills (crafted)'}],
  edges=[{'to': 'z5'}], item=[CE, L4, ALn, RN])
A(id='z5', kind='act', group='prep', pos=[0, 6], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy', 'Omen_of_the_Liege'],
  label=K('훼손', 'Desecrate'), goal=K('접두 네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated prefix): the fracture needs four'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 아마나무)', 'en': 'Desecrated (unrevealed, Amanamu)'}], edges=[{'to': 'z6'}], item=[CE, UN('p'), L4, ALn, RN])
A(id='z6', kind='act', group='prep', pos=[0, 7], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('초월의 합금 분열', 'Transcendent Alloy fractures')],
  edges=[{'if': {'fractured': 'trans'}, 'to': 'ms', 'res': 'ok', 'label': K('초월의 합금 분열', 'Alloy fractured')},
         {'to': 'zs', 'res': 'ok', 'dash': True, 'label': K('+4·천공의 합금 분열', '+4 or Celestial fractured')}],
  item=[CE, UN('p'), L4, AL, RN])
A(id='zs', kind='assume', group='prep', pos=[1, 7], next='ms', swapFracture='trans', label=K('+4·천공의 합금 분열', '+4 or Celestial Alloy fractured'),
  note=K('영상 25:30: 셋 다 쓸 만한 분열, 같은 비용으로 이어 간다고 가정', 'Video 25:30: all three are fine; assumed to cost the same from here'))
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 8.4], next='n1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[CE, UN('p'), L4, AL, RN])
A(id='n1', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='blk', label=K('공개', 'Reveal'),
  goal=K('접두 원소 피해(훼손) — 화염·냉기·번개 피해 % 자리 막기', 'Elemental damage prefix (desecrated): blocks the fire, cold and lightning % families'), show=['blk'],
  edges=[{'to': 'n2'}], item=[CE, ED, L4, AL, RN])
A(id='n1d', kind='act', group='main', pos=[1, 9.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy', 'Omen_of_the_Liege'],
  label=K('훼손', 'Desecrate'), goal=K('접두 다시 훼손 (아마나무)', 'Desecrate the prefix again (Amanamu)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 아마나무)', 'en': 'Desecrated (unrevealed, Amanamu)'}], edges=[{'to': 'n1', 'label': K('다시 공개', 'Reveal again')}])
A(id='n2', kind='act', group='main', pos=[0, 10.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 추가 냉기 피해 — 추가 피해·주문 피해·주문 피해와 마나 중 먼저 뜬 것', 'Extra cold prefix: or any extra damage, spell damage or spell + mana, whichever lands first'), show=['pre'],
  over=[{'param': {'L': 0}, 'set': {'cur': 'Greater_Exalted_Orb', 'goal': K('접두 세 번째 옵션 — 나오는 대로', 'Third prefix: keep what comes'), 'showText': [{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], 'show': []}}],
  edges=[{'if': {'any': [{'added': 'pre'}, V_ESS]}, 'to': 'n3', 'res': 'ok'}, {'to': 'n2x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[CE, ED, XC, L4, AL, RN])
A(id='n2x', kind='act', group='main', pos=[1, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'if': {'removed': 'cel'}, 'to': 'n2c', 'res': 'fail', 'label': K('천공의 합금이 지워짐', 'Celestial Alloy gone')},
         {'if': {'removed': 'blk'}, 'to': 'n1d', 'res': 'fail', 'label': K('막기 옵션이 지워짐', 'Blocker gone')},
         {'to': 'n2', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='n2c', kind='act', group='main', pos=[2, 10.4], act='essence', cur='Celestial_Alloy', ess='cel', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('천공의 합금 다시', 'Celestial Alloy again'),
  showText=[{'s': 'p', 'kr': '마나 최대치 · 모든 주문 스킬 레벨 +1 (제작 옵션)', 'en': 'Maximum mana · +1 all spell skills (crafted)'}],
  edges=[{'if': {'removed': 'blk'}, 'to': 'n1d', 'res': 'fail', 'label': K('막기 옵션이 지워짐', 'Blocker gone')}, {'to': 'n2', 'res': 'ok'}])
A(id='n3', kind='act', group='main', pos=[0, 11.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN,
  goal=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecrated option'), target=K('자리 막기 훼손 옵션 제거', 'Remove the blocking desecrated option'),
  edges=[{'to': 'n4'}], item=[CE, XC, L4, AL, RN])
A(id='n4', kind='act', group='main', pos=[0, 12.4], act='desecrate', cur='Ancient_Jawbone', omens=['Omen_of_Dextral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'n5'}], item=[CE, XC, L4, AL, UN('s'), RN])
A(id='n5', kind='act', group='main', pos=[0, 13.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], label=K('공개', 'Reveal'),
  goal=K('접미 세 번째 옵션 공개 — 나오는 대로', 'Reveal the third suffix: keep what comes'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}],
  edges=[{'to': 'n6'}], item=[CE, XC, L4, AL, MR, RN])   # 11-13 P10 새 정책 B: 영상 5:43~5:49 메아리 다시 뽑기 한 번, 빛의 징조 반복 없음
A(id='n6', kind='act', group='main', pos=[0, 14.4], act='exalt', cur='Perfect_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 마지막 옵션 — 나오는 대로', 'Last prefix: keep what comes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  over=[{'param': {'L': 0}, 'set': {'cur': 'Greater_Exalted_Orb'}}],
  edges=[{'to': 'ok'}], item=[CE, XC, CH, L4, AL, MR, RN])
A(id='ok', kind='done', group='main', pos=[0, 15.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L2', 'nodes': ['n2', 'n2x', 'n2c'], 'kr': '접두 세 번째 옵션', 'en': 'Third prefix', 'fold': True,
  'goal': K('접두 추가 냉기 피해 — 추가 피해·주문 피해·주문 피해와 마나 1~2티어 중 먼저 뜬 것', 'Extra cold prefix: or any T1–2 extra damage, spell damage or spell + mana, whichever lands first'),
  'steps': [K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브', 'Omen of Sinistral Exaltation + Perfect Exalted Orb') | {'node': 'n2'},
            K('빗나가면 좌측 소멸의 징조 + 소멸의 오브', 'Miss: Omen of Sinistral Annulment + Orb of Annulment') | {'node': 'n2x'},
            K('천공의 합금이 지워지면 좌측 결정화의 징조 + 천공의 합금', 'Celestial Alloy gone: Omen of Sinistral Crystallisation + Celestial Alloy') | {'node': 'n2c'}],
  'worst': K('원소 피해 막기 옵션이 지워지면 다시 훼손', 'Elemental damage blocker gone: desecrate again') | {'to': 'n1d'},
  'item': [CE, ED, XC, L4, AL, RN]},
]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'cel', 'ess': True}, {'tag': 'pre2'}, {'side': 'p', 'random': True},
            {'tag': 'l4'}, {'tag': 'trans', 'fr': True}, {'side': 's', 'random': True}]},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
