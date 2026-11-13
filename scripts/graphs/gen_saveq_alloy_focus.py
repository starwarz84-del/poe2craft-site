# G9 2026-11-13: SaVeQ 합금 집중구(uCbyTF-LJ5I, 16:40, 0.5) 플로우차트 생성기 — 영상 1번 집중구(5:00~8:36) 성공 회차 한 줄
# 근거: scratchpad review/G9/saveq-alloy-focus-v2/timeline.md, frames/ (영상 화면 대조)
# 실행: cd scripts/graphs && python3 gen_saveq_alloy_focus.py  → saveq-alloy-focus-v2.json (gen_batch7.py 끝에서 자동 호출, 그 파일의 이 아이템 구간을 대신함)
# 상자 id는 옛 단계 레시피(recipes_v5_saveq-alloy-focus.py: v1~v7·vr1~vr3·vm1)와 겹치지 않게 s0~s10.
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-alloy-focus-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

ESF = L('p', '에너지 보호막 최대치 +(61—73)', '+(61—73) to maximum Energy Shield', 'n', ['esf'])
ESFr = L('p', '에너지 보호막 최대치 +(61—73) (분열)', '+(61—73) to maximum Energy Shield (fractured)', 'f', ['esf'])
LVL = L('s', '모든 주문 스킬 레벨 +2', '+2 to Level of all Spell Skills', 'n', ['lvl'])
CR = L('s', '주문 치명타 명중 확률 (47—53)% 증가 (상위 추구의 에센스)', '(47—53)% increased Critical Hit Chance for Spells (Greater Essence of Seeking)', 'c', ['critE'])
ESP = L('p', '에너지 보호막 (92—100)% 증가 (훼손)', '(92—100)% increased Energy Shield (desecrated)', 'd', ['esp1'])
MANA = L('p', '최대 마나 +(125—149)', '+(125—149) to maximum Mana', 'n')   # 엑잘 결과 그대로라 태그 없음(레시피 목표가 랜덤으로 읽히게)
CS = L('s', '시전 속도 (26—31)% 증가, 원소 피해의 (7—11)%를 추가 냉기 피해로 획득 (초월의 합금)', '(26—31)% increased Cast Speed, Gain (7—11)% of Elemental Damage as Extra Cold Damage (Transcendent Alloy)', 'c', ['cs'])
AS = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
REV_LABEL = K('에너지 보호막 % 증가·주문 피해 증가 1~2티어', 'T1–2 % Energy Shield or spell damage')

g = {
 'id': 'saveq-alloy-focus-v2', 'recipe': 'saveq-alloy-focus-v2', 'cls': 'Foci', 'base': 'Tasalian Focus', 'ilvl': 84,
 'basePrice': {'Divine_Orb': 3.5},   # 2:20 자막 '4 div 또는 3 div'(에너지 보호막 최대치 3티어 + 모든 주문 +2 매직)
 'note': ('2026-11-13 G9 영상 전체 대조(근거 scratchpad review/G9/saveq-alloy-focus-v2/timeline.md). 집중구 3개 중 1번(5:00~8:36) 한 줄: '
          '에너지 보호막 최대치 3티어 + 모든 주문 스킬 +2 매직 타살리안 집중구 구입(아이템 레벨 84, 약 3.5 div) → 상위 추구의 에센스(5:29) → 좌측 강령술 + 고대 갈비뼈(5:38) → '
          '분열의 오브 = 에너지 보호막 최대치(6:00) → 심연의 메아리 공개 = 에너지 보호막 95%(6:46) → 소켓 + 아스트리드의 창의성(7:00) → 좌측 찬미 + 완벽한 엑잘 = 마나 2티어(7:25) → '
          '좌측 결정화 + 초월의 합금(7:45, 1/2에서 공개 옵션이 지워짐) → 고대 갈비뼈 다시 + 메아리 공개 = 에너지 보호막 95%(8:24). '
          '분열이 다른 옵션에 걸려도 그 베이스로 계속(사용자 확정 2026-11-13 14:33 — 보통이라 영상 2·3번 집중구처럼 진행, 그 뒤 합금이 접두 3개 중 하나를 지움). '
          '합금이 훼손 옵션이 아닌 접두를 지우면 완벽한 엑잘로 빈 접두(영상 2번 10:20과 같은 처리). '
          '11-13 오후 새 정책: 영상 공개 두 번 모두 한 번에 1티어라 빛의 징조 반복 없음(B) → 밸런스·에센셜 과정이 같아 밸런스 하나만(D). 공개는 심연의 메아리로 에너지 보호막 %·주문 피해가 있으면 고르고, 없으면 결과 그대로.'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 분열이 다른 옵션이어도 계속, 공개·엑잘 결과 그대로', 'Video: carry on whatever fractures, keep the reveal and Exalt results')}],
 'tags': {
   'esf': {'gi': 6, 'tmax': 3}, 'lvl': {'gi': 16, 'tmax': 1}, 'critE': {'gi': 47}, 'cs': {'gi': 59},
   'esp1': {'gi': 7, 'tmax': 1}, 'mana2': {'gi': 5, 'tmax': 2},
   'esp2': {'gi': 7, 'tmax': 2}, 'spell2': {'gi': 10, 'tmax': 2},
   'rev': {'anyOf': ['esp2', 'spell2'], 'shown': 'esp2', 'label': REV_LABEL}},
 'require': {'all': [{'has': 'lvl'}, {'has': 'critE'}, {'has': 'cs'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 's0',
 'finalItem': {'quality': 0, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='s0', kind='base', group='prep', pos=[0, 0], next='s1', start={'rar': 'magic', 'mods': ['esf', 'lvl']},
  label=K('에너지 보호막 최대치 3티어 + 모든 주문 스킬 +2 매직 타살리안 집중구 구입 (아이템 레벨 84)', 'Buy a magic Tasalian Focus: T3 flat Energy Shield + all spell skills +2 (item level 84)'),
  item=[ESF, LVL])
A(id='s1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Greater_Essence_of_Seeking', ess='critE',
  label=K('에센스', 'Essence'), goal=K('레어 + 접미 주문 치명타 명중 확률 (제작 옵션)', 'Rare + spell crit chance suffix (crafted)'),
  showText=[{'s': 's', 'kr': '주문 치명타 명중 확률 (47—53)% 증가 (제작 옵션)', 'en': '(47—53)% increased Critical Hit Chance for Spells (crafted)'}],
  edges=[{'to': 's2'}], item=[ESF, LVL, CR])
A(id='s2', kind='act', group='prep', pos=[0, 2], act='desecrate', cur='Ancient_Rib', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 두 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Second prefix (desecrated): the fracture needs four options'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개, 분열되지 않음)', 'en': 'Desecrated (unrevealed, cannot fracture)'}],
  edges=[{'to': 's3'}], item=[ESF, UN('p'), LVL, CR])
A(id='s3', kind='act', group='prep', pos=[0, 3], act='fracture', cur='Fracturing_Orb',
  label=K('분열', 'Fracture'), goal=K('분열 — 공개된 옵션 3개 중 하나, 영상은 접두 에너지 보호막 최대치', 'Fracture: one of three revealed options, the video got the flat Energy Shield prefix'),
  showText=[K('다른 옵션이 분열돼도 이 베이스로 계속', 'Carry on with this base whatever fractures')],
  edges=[{'to': 's4'}],
  item=[ESFr, UN('p'), LVL, CR])
A(id='s4', kind='act', group='prep', pos=[0, 4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev',
  label=K('공개', 'Reveal'), goal=K('접두 훼손 옵션 공개 — 결과 그대로', 'Reveal the prefix: keep what comes'),
  show=['esp1'],
  edges=[{'to': 'ms'}],
  item=[ESFr, ESP, LVL, CR])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 5.4], next='s5', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ESFr, ESP, LVL, CR])
A(id='s5', kind='act', group='main', pos=[0, 6.4], act='rune', cur='Artificers_Orb',
  label=K('룬', 'Rune'), goal=K('숙련공의 오브로 소켓 추가, 아스트리드의 창의성 장착', 'Add a socket with an Artificer’s Orb, socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 's6'}], item=[ESFr, ESP, LVL, CR, AS])
A(id='s6', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 세 번째 옵션 — 합금이 1/2로 지울 옵션, 결과 그대로', 'Third prefix: the one the Alloy removes 1 in 2, keep whatever comes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 's7'}], item=[ESFr, ESP, MANA, LVL, CR, AS])
A(id='s7', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Transcendent_Alloy', ess='cs', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 하나를 지우고 시전 속도 (제작 옵션) — 분열 옵션은 남음', 'A prefix goes for Cast Speed (crafted): the fractured one stays'),
  showText=[{'s': 's', 'kr': '시전 속도 (26—31)% 증가, 원소 피해의 (7—11)%를 추가 냉기 피해로 획득 (제작 옵션)', 'en': '(26—31)% increased Cast Speed, Gain (7—11)% of Elemental Damage as Extra Cold Damage (crafted)'}],
  ask=K('어느 접두가 지워짐?', 'Which prefix went?'),
  edges=[{'if': {'des': True}, 'to': 's10', 'res': 'ok', 'label': K('훼손 옵션이 남음', 'The desecrated option stays')},
         {'to': 's8', 'res': 'fail', 'label': K('훼손 옵션이 지워짐', 'The desecrated option went')}],
  item=[ESFr, MANA, LVL, CR, CS, AS])
A(id='s8', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Ancient_Rib',
  label=K('훼손', 'Desecrate'), goal=K('접두 세 번째 옵션(훼손) — 접미가 꽉 차 접두로', 'Third prefix (desecrated): the suffixes are full'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 's9'}], item=[ESFr, MANA, UN('p'), LVL, CR, CS, AS])
A(id='s9', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev',
  label=K('공개', 'Reveal'), goal=K('접두 훼손 옵션 공개 — 결과 그대로', 'Reveal the prefix: keep what comes'),
  show=['esp1'],
  edges=[{'to': 'ok'}],
  item=[ESFr, MANA, ESP, LVL, CR, CS, AS])
A(id='s10', kind='act', group='main', pos=[1, 8.8], act='exalt', cur='Perfect_Exalted_Orb',
  label=K('엑잘', 'Exalt'), goal=K('빈 접두 채우기 — 결과 그대로', 'Fill the free prefix: keep whatever comes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'ok'}])
A(id='ok', kind='done', group='main', pos=[0, 11.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = []
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'esf', 'fr': True}, {'side': 'p', 'random': True, 'des': True}, {'side': 'p', 'random': True}, {'tag': 'lvl'}, {'tag': 'critE', 'ess': True}, {'tag': 'cs', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
