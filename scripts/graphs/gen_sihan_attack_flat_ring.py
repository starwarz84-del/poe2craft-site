# G2 2026-11-13: 시한 공격 플랫 3줄 반지(bpXgZGw4WQo, 19:04) 플로우차트 생성기 — 영상 성공 회차(구입한 태풍 손아귀) 한 줄
# 근거: scratchpad review/G2/sihan-attack-flat-ring-v2/timeline.md, frames/ (영상 0:00~19:04 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_attack_flat_ring.py  → sihan-attack-flat-ring-v2.json (gen_batch22.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-attack-flat-ring-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(9:55 매물 → 18:40 완성)에 실제로 나온 옵션
PH = L('p', '공격 시 물리 피해 (12—19)~(22—32) 추가 (분열)', 'Adds (12—19) to (22—32) Physical Damage to Attacks (fractured)', 'f', ['phys'])
STR = L('s', '힘 +(28—30)', '+(28—30) to Strength', 'j')
MQ = L('p', '최대 퀄리티 +20% (균열의 에센스)', '+20% to Maximum Quality (Essence of the Breach)', 'c', ['maxq'])
CO = L('p', '공격 시 냉기 피해 (21—24)~(32—37) 추가', 'Adds (21—24) to (32—37) Cold Damage to Attacks', 'n', ['cold'])
MR = L('s', '마나 재생 속도 (60—69)% 증가', '(60—69)% increased Mana Regeneration Rate', 'j')
AS = L('s', '공격 속도 (7—9)% 증가 (재빠른 합금)', '(7—9)% increased Attack Speed (Swift Alloy)', 'c', ['as'])
INT = L('s', '지능 +(31—33)', '+(31—33) to Intelligence', 'n')
RES = L('s', '모든 원소 저항 +(12—14)%', '+(12—14)% to all Elemental Resistances', 'n')
LG = L('p', '공격 시 번개 피해 (1—4)~(60—71) 추가 (훼손)', 'Adds (1—4) to (60—71) Lightning Damage to Attacks (desecrated)', 'd', ['lgt'])
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
LIGHT = K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light')
FLAT = K('공격 시 화염·냉기·번개 피해 추가', 'Adds fire, cold or lightning damage to attacks')

g = {
 'id': 'sihan-attack-flat-ring-v2', 'recipe': 'sihan-attack-flat-ring-v2', 'cls': 'Rings', 'base': 'Unset Ring', 'ilvl': 80,
 'basePrice': {'Divine_Orb': 75},   # 9:55 거래소 '~b/o 75 divine'
 'note': ('2026-11-13 G2 영상 전체 화면 대조(0:00~19:04). 성공 회차 = 거래소에서 산 태풍 손아귀(9:55, 아이템 레벨 80, 공격 시 물리 피해 15~32 분열 + 힘 +28, 75 div). '
          '10:30~13:45 직접 분열 시연(노멀 반지 → 완벽한 진화·확장 → 분열 실패, 13:35)은 성공 회차가 아니라 꿀팁 후보. '
          '균열의 에센스로 힘이 지워지고 최대 퀄리티 +20%(14:02~14:26) → 강탈자 기폭제로 공격 퀄리티 40%(14:15~14:32, 채팅 "퀄리티가 이미 최대") → '
          '카오스 반복으로 최대 퀄리티 옵션 자리에 원소 공격 피해 추가 1티어(14:30~14:58, 성공 회차 냉기 22~37) → '
          '우측 찬미 + 엑잘로 잡옵 접미(마나 재생 속도, 15:31, 채팅 우측 찬미 소모) → 우측 결정화 + 재빠른 합금으로 공격 속도(15:42) → '
          '상위 + 우측 찬미 + 완벽한 엑잘로 접미 2개(지능 1티어·모든 원소 저항 2티어, 16:16 — 영상 기준 랜덤) → 고대 빗장뼈(17:06) → '
          '심연의 메아리 공개(17:59 번개 2~64 1티어), 빗나가면 빛의 징조로 지우고 다시(18:35 자막). '
          '등급(정책 10장): 카오스 반복은 분열 뒤 싼 반복이라 모든 등급 1티어(C15), 공개는 빛의 징조 반복이라 밸런스 1~2티어 · 에센셜은 결과 그대로(C17-1·3), '
          '마지막 접미 2개는 영상대로 랜덤 옵션(C17-2).'),
 'params': {
  'v': {'kr': '공개', 'en': 'Reveal', 'values': {'1': K('빛의 징조로 다시', 'Retry with Omen of Light'), '2': K('결과 그대로', 'As it comes')}},
  'fT': {'kr': '공개 원소 공격 피해', 'en': 'Revealed elemental flat', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1, 'fT': 2}}, {'id': 'ess', 'params': {'v': 2, 'fT': 4}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2, 'fT': 4}, 'tier': 'ess',
   'desc': K('공개 결과 그대로', 'Keep the reveal as it comes')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1, 'fT': 2}, 'tier': 'bal',
   'desc': K('영상: 공개가 빗나가면 빛의 징조로 다시, 원소 공격 피해 1~2티어', 'Video: Omen of Light retries the reveal, T1–2 elemental flat')}],
 'tags': {
  'phys': {'gi': 13, 'tmax': 1}, 'maxq': {'gi': 71}, 'as': {'gi': 73},
  'fire1': {'gi': 15, 'tmax': 1}, 'cold1': {'gi': 17, 'tmax': 1}, 'lgt1': {'gi': 19, 'tmax': 1},
  'fireR': {'gi': 15, 'tmax': '$fT'}, 'coldR': {'gi': 17, 'tmax': '$fT'}, 'lgtR': {'gi': 19, 'tmax': '$fT'},
  'cold': {'gi': 17}, 'lgt': {'gi': 19},
  'flat1': {'anyOf': ['fire1', 'cold1', 'lgt1'], 'shown': 'cold1', 'label': K('공격 시 화염·냉기·번개 피해 추가 1티어', 'T1 fire, cold or lightning flat to attacks')},
  'flatR': {'anyOf': ['fireR', 'coldR', 'lgtR'], 'label': FLAT},
  'flatB': {'anyOf': ['fire1', 'cold1', 'lgt1', 'fireR', 'coldR', 'lgtR'], 'shown': 'lgt1', 'label': K('공격 시 화염·냉기·번개 피해 추가 1~2티어', 'T1–2 fire, cold or lightning flat to attacks')},
 },
 'require': {'all': [{'has': 'phys'}, {'has': 'flat1'}, {'has': 'as'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'phys', 'fr': True}, {'tag': 'flat1'}, {'tag': 'flatB', 'des': True},
             {'tag': 'as', 'ess': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'phys', 'fr': True}, {'tag': 'flat1'}, {'side': 'p', 'random': True},
             {'tag': 'as', 'ess': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 40, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (영상 9:55~14:32) ----------------
A(id='k0', kind='base', group='prep', pos=[0, 0], next='k1',
  start={'rar': 'rare', 'mods': [{'tag': 'phys', 'fr': True}, {'junk': 's'}]},
  label=K('무보석 반지 매물 구입 (아이템 레벨 80, 공격 시 물리 피해 추가 1티어 분열 + 잡옵 1개)',
          'Buy an Unset Ring listing (item level 80: fractured T1 physical flat + one junk option)'),
  item=[PH, STR])
A(id='k1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Essence_of_the_Breach', ess='maxq', label=K('에센스', 'Essence'),
  goal=K('최대 퀄리티 +20%', '+20% maximum quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'k2'}], item=[PH, MQ])
A(id='k2', kind='act', group='prep', pos=[0, 2], act='quality', cur='Reaver_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('공격 퀄리티 40%', '40% attack quality'), edges=[{'to': 'km'}], item=[PH, MQ])
# ---------------- 옵션 추가 작업 ----------------
A(id='km', kind='mark', group='main', pos=[0, 3.4], next='k3', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PH, MQ])
# 14:30~14:58 카오스 반복(최대 퀄리티 자리 → 냉기 1티어). 영상 설명 0:30·2:30: 물리·냉기·번개·화염 아무거나 1티어
A(id='k3', kind='act', group='main', pos=[0, 4.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 두 번째 옵션 — 공격 시 냉기 피해 추가 1티어', 'Second prefix: T1 cold flat to attacks'),
  showText=[K('남은 원소 공격 피해 추가 1티어 중 먼저 뜬 것', 'Whichever T1 elemental flat lands first')],
  edges=[{'if': {'has': 'flat1'}, 'to': 'k4', 'res': 'ok'}, {'to': 'k3', 'res': 'fail'}],
  item=[PH, CO])
A(id='k4', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('합금이 지울 접미', 'The suffix for the alloy to remove'), showText=[K('잡옵 1개', 'One junk option')],
  edges=[{'to': 'k5'}], item=[PH, CO, MR])
A(id='k5', kind='act', group='main', pos=[0, 6.4], act='essence', cur='Swift_Alloy', ess='as', omens=['Omen_of_Dextral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('접미 첫 번째 옵션 — 공격 속도', 'First suffix: attack speed'),
  showText=[{'s': 's', 'kr': '공격 속도 (7—9)% 증가 (제작 옵션)', 'en': '(7—9)% increased Attack Speed (crafted)'}],
  edges=[{'to': 'k6'}], item=[PH, CO, AS])
A(id='k6', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation', 'Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션', 'Second and third suffixes'), showText=[K('랜덤 옵션 2개', 'Two random options')],
  edges=[{'to': 'k7'}], item=[PH, CO, AS, INT, RES])
A(id='k7', kind='act', group='main', pos=[0, 8.4], act='desecrate', cur='Ancient_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'k8'}], item=[PH, CO, UN('p'), AS, INT, RES])
A(id='k8', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='flatR', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 공격 시 번개 피해 추가', 'Third prefix (desecrated): lightning flat to attacks'),
  showText=[K('남은 원소 공격 피해 추가 중 먼저 뜬 것', 'Whichever remaining elemental flat lands first')],
  edges=[{'if': {'added': 'flatR'}, 'to': 'ok', 'res': 'ok'},
         {'if': {'param': {'v': 1}}, 'to': 'k8x', 'res': 'fail'},
         {'to': 'ok', 'res': 'fail', 'hide': True}],
  item=[PH, CO, LG, AS, INT, RES])
A(id='k8x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'k7', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 10.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['k7', 'k8', 'k8x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
