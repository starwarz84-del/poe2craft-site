# G12 2026-11-13: Icesly 가성비 +7 마법봉(gtxAqZfCxxI, 8:10) 플로우차트 생성기 — 영상 성공 회차(자기 마법봉) 한 줄
# 근거: scratchpad review/G12/icesly-budget-wand-v2/timeline.md, frames/ (영상 0:00~8:10 화면 대조)
# 실행: cd scripts/graphs && python3 gen_icesly_budget_wand.py  → icesly-budget-wand-v2.json (gen_batch5.py 끝에서도 자동 호출, 이 아이템 구간을 대신함)
# 상자 id는 옛 레시피(recipes_v5_icesly-budget-wand.py, i1~i9)·옛 그래프(h1·i2~i9d)와 겹치지 않게 c0~c9로 지음.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/icesly-budget-wand-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차에 실제로 나온 옵션
L5 = L('s', '모든 번개 주문 스킬 레벨 +5', '+5 to Level of all Lightning Spell Skills', 'n', ['l5'])                    # 1:42 매직 결투 마법봉
JP = L('p', '마나 최대치 +11', '+11 to maximum Mana', 'j')                                                            # 1:42 접두 잡옵(11티어)
MK = L('s', '적 처치 시 마나 33 획득', 'Gain 33 Mana per enemy killed', 'j')                                         # 1:53 제왕 결과(2티어)
TR = L('s', '시전 속도 (26—31)% 증가 · 원소 피해의 (7—11)%를 추가 냉기 피해로 획득 (초월의 합금)',
       '(26—31)% increased Cast Speed · Gain (7—11)% of Elemental Damage as Extra Cold Damage (Transcendent Alloy)', 'c', ['trans'])   # 3:06
LD = L('p', '번개 피해 (75—89)% 증가', '(75—89)% increased Lightning Damage', 'n', ['lin'])                          # 3:18 첫 엑잘(3티어 87%)
XL = L('p', '피해의 (22—24)%를 추가 번개 피해로 획득', 'Gain (22—24)% of Damage as Extra Lightning Damage', 'n', ['xL'])   # 3:32 두 번째 엑잘(3티어 24%)
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')                                                    # 3:54 보존된 턱뼈
RN = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')                                                       # 4:59
CE = L('p', '마나 최대치 +(142—188) · 모든 주문 스킬 레벨 +1 (천공의 합금)', '+(142—188) to maximum Mana · +1 to Level of all Spell Skills (Celestial Alloy)', 'c', ['cel'])   # 5:15
XC = L('p', '피해의 (28—30)%를 추가 냉기 피해로 획득 (훼손)', 'Gain (28—30)% of Damage as Extra Cold Damage (desecrated)', 'd', ['xC1'])   # 5:52 공개(1티어 28%)

g = {
 'id': 'icesly-budget-wand-v2', 'recipe': 'icesly-budget-wand-v2', 'cls': 'Wands', 'base': 'Dueling Wand', 'ilvl': 81,
 'basePrice': {'Divine_Orb': 13},   # 1:18 거래소 '베릴 결투 마법봉(아이템 레벨 81, 마나 +11 · 번개 +5) 13 divine', 1:42에 같은 마법봉
 'note': ('2026-11-13 G12 영상 전체(0:00~8:10) 화면 대조. 성공 회차 = 자기 마법봉 한 줄: 번개 주문 +5(1티어) 매직 결투 마법봉 구입(아이템 레벨 81, 접두 마나 +11 잡옵, 1:18 13 div, 1:42) → '
          '완벽한 제왕의 오브(창고 III 3 → 2, 징조 없음 — 인벤토리에 징조 없음, 1:48~1:53) = 접미 적 처치 시 마나 33(잡옵) → '
          '좌측 결정화의 징조 + 초월의 합금(접두 마나 잡옵이 지워짐, 3:06, 징조 3 → 2·합금 10 → 9) → 엑잘티드 오브 2번(창고 일반 엑잘 2192 → 2191 → 2190, 징조 없음 — 접미가 꽉 차서 접두로): '
          '번개 피해 87%(3티어, 3:18) · 추가 번개 피해 24%(3티어, 3:32) → 보존된 턱뼈(3:53 툴팁, 3:54 미공개 훼손 접두) → 아스트리드의 창의성(4:59) → '
          '좌측 결정화의 징조 + 천공의 합금(5:15, 채팅 소모 메시지, 추가 번개 피해가 지워짐 — 접두 3개 중 하나) → 심연의 메아리의 징조 + 공개(5:52 선택지: 주문 피해·하수인 / 추가 냉기 28% / 추가 화염 25%, 5:56 채팅 소모) = 추가 냉기 피해 28%(1티어) → 완성(6:20). '
          '3:52 자막 캡션: 엑잘이 나쁘면 훼손하지 말고 천공의 합금이 1/2로 지우게 함(꿀팁 후보, 성공 회차는 두 엑잘 모두 유효). 6:20~8:10은 설명. '
          '제왕의 오브는 영상에서 징조 없이 접미로 갔고, 접두로 가는 경우(약 4할)도 시뮬은 같은 흐름으로 굴림(초월의 합금이 접두 잡옵 하나를 지우고 이어 감). '
          '등급(정책 10장): 난이도 2 → 밸런스. 11-13 오후 새 정책: (B) 영상은 공개를 한 번 하고(5:52) 빗나감 처리가 없어 빛의 징조 반복 없음, 공개 결과 그대로 '
          '(D) 그러면 밸런스·에센셜 비용이 같아(10% 이내) 밸런스 하나만. 엑잘 두 번도 영상처럼 결과 그대로(소멸 징조 20 div — 가성비 레시피라 반복하지 않음, 사용자 확정 11-10 비싼 오브 없이).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
   'desc': K('영상 그대로: 엑잘·천공의 합금·공개 결과 그대로', 'As the video: keep each exalt, the Celestial Alloy and the reveal as they come')}],
 'tags': {
  'l5': {'gi': 13, 'tmax': 1}, 'trans': {'gi': 60}, 'cel': {'gi': 59},
  'lin': {'gi': 7}, 'xL': {'gi': 28}, 'xC1': {'gi': 27, 'tmax': 1},
 },
 'require': {'all': [{'has': 'l5'}, {'has': 'trans'}, {'has': 'cel'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'c0',
 'finalItem': {'quality': 0, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 1:18~3:06) ----------------
A(id='c0', kind='base', group='prep', pos=[0, 0], next='c1', start={'rar': 'magic', 'mods': ['l5', {'junk': 'p'}]},
  label=K('모든 번개 주문 스킬 레벨 +5 매직 결투 마법봉 구입 (아이템 레벨 81, 접두 잡옵 1개)', 'Buy a magic Dueling Wand with +5 lightning spell skills (item level 81, one junk prefix)'),
  item=[JP, L5])
A(id='c1', kind='act', group='prep', pos=[0, 1], act='regal', cur='Perfect_Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어 + 잡옵 1개 — 접미 적 처치 시 마나', 'Rare + one junk option: mana per kill suffix'),
  showText=[K('잡옵 1개', 'One junk option')], edges=[{'to': 'c2'}], item=[JP, L5, MK])
A(id='c2', kind='act', group='prep', pos=[0, 2], act='essence', cur='Transcendent_Alloy', ess='trans', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 잡옵을 지우고 접미 초월의 합금', 'The junk prefix goes for the Transcendent Alloy suffix'),
  showText=[{'s': 's', 'kr': '시전 속도 · 원소 피해의 %를 추가 냉기 피해로 획득 (제작 옵션)', 'en': 'Cast speed · elemental damage as extra cold (crafted)'}],
  edges=[{'to': 'ms'}], item=[L5, MK, TR])
# ---------------- 옵션 추가 작업 (영상 3:12~5:56) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='c3', label=K('아이템 제작 시작', 'Item crafting starts'), item=[L5, MK, TR])
# R3-12(11-13): 성공 선을 param 조건으로 — 레시피 글 목표가 1티어 글('번개 피해 (105—119)%')이 아니라 '아무 옵션 1개'(결과 그대로)
A(id='c3', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 첫 번째 옵션 — 번개 피해 증가', 'First prefix: increased lightning damage'),
  showText=[K('결과 그대로', 'Keep whatever comes')], edges=[{'if': {'param': {'v': 1}}, 'to': 'c4', 'res': 'ok'}], item=[LD, L5, MK, TR])
A(id='c4', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 추가 번개 피해', 'Second prefix: extra lightning damage'),
  showText=[K('결과 그대로', 'Keep whatever comes')], edges=[{'if': {'param': {'v': 1}}, 'to': 'c5', 'res': 'ok'}], item=[LD, XL, L5, MK, TR])
A(id='c5', kind='act', group='main', pos=[0, 6.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'c6'}], item=[LD, XL, UN, L5, MK, TR])
A(id='c6', kind='act', group='main', pos=[0, 7.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'c7'}], item=[LD, XL, UN, L5, MK, TR, RN])
A(id='c7', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Celestial_Alloy', ess='cel', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 3개 중 하나를 지우고 천공의 합금 — 추가 번개 피해가 지워짐', 'One of the three prefixes goes for the Celestial Alloy: the extra lightning damage'),
  showText=[{'s': 'p', 'kr': '마나 최대치 · 모든 주문 스킬 레벨 +1 (제작 옵션)', 'en': 'Maximum mana · +1 all spell skills (crafted)'}],
  edges=[{'if': {'any': [{'unrevSide': 'p'}, {'unrevSide': 's'}]}, 'to': 'c8', 'res': 'ok', 'label': K('남은 훼손 공개', 'Reveal the desecration left')},
         {'to': 'ok', 'res': 'ok', 'label': K('미공개 훼손이 지워짐', 'The unrevealed desecration went')}],
  item=[LD, UN, CE, L5, MK, TR, RN])
A(id='c8', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션 공개 — 나오는 대로', 'Reveal the third prefix: keep what comes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}],
  edges=[{'to': 'ok'}],
  item=[LD, XC, CE, L5, MK, TR, RN])
A(id='ok', kind='done', group='main', pos=[0, 11.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = []
_card = lambda: [{'tag': 'cel', 'ess': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
                 {'tag': 'l5'}, {'tag': 'trans', 'ess': True}, {'side': 's', 'random': True}]
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance', 'lines': _card()},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
