# G2 2026-11-13: MazBro 캐스터 반지(o3Fh1DJmxBA, 42:15) 플로우차트 생성기 — 영상 가이드 화면(1:00~3:20) + 성공 회차(Storm Knot) 한 줄
# 근거: scratchpad review/G2/mazbro-caster-ring-v2/timeline.md, frames/
# 실행: cd scripts/graphs && python3 gen_mazbro_caster_ring.py  → mazbro-caster-ring-v2.json (gen_batch10.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/mazbro-caster-ring-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 성공 회차 Storm Knot(21:45 카오스 → 23:38 제작 끝 → 30:12 훼손 전 → 31:08 완성)에 실제로 나온 옵션
CS0 = L('s', '시전 속도 (22—24)% 증가', '(22—24)% increased Cast Speed', 'n', ['cast'])
CS = L('s', '시전 속도 (22—24)% 증가 (분열)', '(22—24)% increased Cast Speed (fractured)', 'f', ['cast'])
JP = L('p', '잡옵', 'Junk', 'j')
JS = L('s', '잡옵', 'Junk', 'j')
MK = L('p', '심연의 군주의 징표', 'Mark of the Abyssal Lord', 'c', ['mk'])
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
MQ = L('p', '최대 퀄리티 +20% (균열의 에센스)', '+20% to Maximum Quality (Essence of the Breach)', 'c', ['maxq'])
RG = L('s', '마나 재생 속도 (60—69)% 증가', '(60—69)% increased Mana Regeneration Rate', 'n', ['regen'])
PM = L('p', '최대 마나 (4—6)% 증가 (완벽한 정신의 에센스)', '(4—6)% increased maximum Mana (Perfect Essence of the Mind)', 'c', ['pmana'])
RP = L('p', '발견하는 아이템 희귀도 (16—19)% 증가', '(16—19)% increased Rarity of Items found', 'n', ['rarP'])
CR = L('s', '냉기 저항 +(41—45)%', '+(41—45)% to Cold Resistance', 'n')
PMu = L('p', '최대 마나 (4—6)% 증가 (완벽한 정신의 에센스)', '(4—6)% increased maximum Mana (Perfect Essence of the Mind)', 'c')   # 태그 없는 칸: 다음 상자 목표 글이 이 옵션을 새 목표로 읽지 않게
RPu = L('p', '발견하는 아이템 희귀도 (16—19)% 증가', '(16—19)% increased Rarity of Items found', 'n')
MA = L('p', '마나 최대치 +(165—179) (훼손)', '+(165—179) to maximum Mana (desecrated)', 'd', ['mana'])
ANN = K('소멸의 오브', 'Orb of Annulment')
LIGHT = K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light')
GOOD = K('마나 재생 속도·아이템 희귀도·모든 원소 저항 1티어', 'T1 mana regeneration, item rarity or all elemental resistances')

g = {
 'id': 'mazbro-caster-ring-v2', 'recipe': 'mazbro-caster-ring-v2', 'cls': 'Rings', 'base': 'Mnemonic Ring', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 2},   # 4:00 자막 '보통 2 div 이하일 때만 산다'(이 회차 매물 1~5 div)
 'note': ('2026-11-13 G2 영상 대조(0:00~42:15, 자막 전체 + 단계별 화면). 영상 화면 가이드(1:00~3:20, 1~10단계)대로 한 줄. '
          '준비: 시전 속도 22~24% 기억 반지(아이템 레벨 82, 옵션 4개, 3:35 필터) → 좌측 결정화 + 심연의 에센스로 접두 잡옵 자리에 징표(7:25~8:40) → 보존된 빗장뼈(9:00) → '
          '분열 1/3(9:20~10:00, 미공개 훼손은 분열되지 않음) → 좌측 결정화 + 균열의 에센스(11:05) → 신경 기폭제 40% + 바알 촉진시키는 주입기 1회(11:15~11:50). '
          '본 제작 성공 회차 = 두 번째 반지 Storm Knot의 마지막 회차(21:45~23:38): 소멸로 분열 + 옵션 1개 → 카오스로 마나 재생 1티어(21:48) → '
          '좌측 찬미 + 상위 엑잘(잡옵) → 좌측 결정화 + 완벽한 정신의 에센스로 최대 마나 %(22:32) → 좌측 찬미 + 상위 엑잘을 소멸과 번갈아 희귀도 접두 1티어(22:46) → '
          '우측 찬미 + 완벽한 엑잘로 남은 접미 하나(성공 회차 23:30은 마나 재생이 지워진 뒤라 상위 찬미까지 써서 냉기 저항·마나 재생, 접미가 하나 남으면 상위 찬미는 끔 — 18:00 자막) → 플랫 마나가 없으니 고대 빗장뼈(30:00) → 메아리 공개, 빛의 징조로 다시 → 마나 최대치 1티어(31:08 자막). '
          '신성한 오브(6:00 시전 속도 24%, 36:30 최대 마나 8%)·축복받은 자의 징조·속성 변환의 징조(37:30)는 비용 밖(수치 다듬기). '
          '플랫 마나 1티어가 엑잘로 먼저 붙으면 뒤바뀐 빗장뼈로 생명력 대신 마나(가이드 7단계, 33:00~36:05 네 번째 반지)는 꿀팁 후보. '
          '등급(정책 10장): 카오스는 모든 등급 1티어(C15), 희귀도 접두·공개 마나는 반복이라 밸런스 1~2티어(C17-1), 에센셜은 한 번씩 결과 그대로, 마지막 접미는 랜덤 옵션(C17-2).'),
 'params': {
  'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('반복', 'Repeat'), '2': K('결과 그대로', 'As it comes')}},
  'gT': {'kr': '희귀도 접두·공개 마나', 'en': 'Rarity prefix and revealed mana', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1, 'gT': 2}}, {'id': 'ess', 'params': {'v': 2, 'gT': 4}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2, 'gT': 4}, 'tier': 'ess',
   'desc': K('희귀도 접두 엑잘·공개 한 번, 결과 그대로', 'One rarity exalt and one reveal, kept as they come')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1, 'gT': 2}, 'tier': 'bal',
   'desc': K('영상: 희귀도 접두는 소멸과 번갈아, 공개는 빛의 징조로 다시(1~2티어)', 'Video: rarity prefix with Annulment retries, reveal retried with Light (T1–2)')}],
 'tags': {
  'cast': {'gi': 34, 'tmax': 1}, 'maxq': {'gi': 71}, 'mk': {'gi': 69},
  'regen': {'gi': 21, 'tmax': 1}, 'rarS': {'gi': 27, 'tmax': 1}, 'res': {'gi': 7, 'tmax': 1},
  'good': {'anyOf': ['regen', 'rarS', 'res'], 'label': GOOD},
  'pmana': {'gi': 67}, 'rarP': {'gi': 28, 'tmax': '$gT'}, 'mana': {'gi': 10, 'tmax': '$gT'},
 },
 'require': {'all': [{'has': 'cast'}, {'has': 'good'}, {'has': 'pmana'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'pmana', 'ess': True}, {'tag': 'rarP'}, {'tag': 'mana', 'des': True},
             {'tag': 'cast', 'fr': True}, {'tag': 'good'}, {'side': 's', 'random': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'pmana', 'ess': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True},
             {'tag': 'cast', 'fr': True}, {'tag': 'good'}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 41, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
V1 = {'param': {'v': 1}}
# ---------------- 베이스템 완성 (영상 3:30~11:50, 가이드 1~4단계) ----------------
A(id='k0', kind='base', group='prep', pos=[0, 0], next='k1',
  start={'rar': 'rare', 'mods': [{'tag': 'cast'}, {'junk': 's'}, {'junk': 'p'}, {'junk': 'p'}]},
  label=K('기억 반지 매물 구입 (아이템 레벨 82, 시전 속도 22~24% + 잡옵 3개)', 'Buy a Mnemonic Ring listing (item level 82: 22–24% cast speed + three junk options)'),
  item=[JP, JP, CS0, JS])
A(id='k1', kind='act', group='prep', pos=[0, 1], act='essence', cur='Essence_of_the_Abyss', ess='mk', mark=True,
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('심연', 'Abyss'),
  goal=K('접두 잡옵 자리에 징표 — 분열 조건 옵션 4개', 'The Mark takes a junk prefix spot: the fracture needs four options'),
  showText=[K('심연의 군주의 징표', 'Mark of the Abyssal Lord')], edges=[{'to': 'k2'}], item=[JP, MK, CS0, JS])
A(id='k2', kind='act', group='prep', pos=[0, 2], act='desecrate', cur='Preserved_Collarbone', fromMark=True, label=K('훼손', 'Desecrate'),
  goal=K('징표를 훼손 옵션으로 — 분열되지 않는 옵션', 'The Mark becomes a desecrated option, which cannot fracture'),
  showText=[K('훼손 옵션 (미공개)', 'Desecrated (unrevealed)')], edges=[{'to': 'k3'}], item=[JP, UN('p'), CS0, JS])
A(id='k3', kind='act', group='prep', pos=[0, 3], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나) — 시전 속도', 'Fracture (one of the three revealed options): cast speed'),
  ask=K('어느 옵션이 분열?', 'Which option fractured?'),
  edges=[{'if': {'fractured': 'cast'}, 'to': 'k4', 'res': 'ok', 'label': K('시전 속도 분열', 'Cast speed fractured')},
         {'to': 'xj', 'res': 'fail', 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[JP, UN('p'), CS, JS])
A(id='xj', kind='exit', group='prep', pos=[1, 3], simTo='k0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('시전 속도가 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='k4', kind='act', group='prep', pos=[0, 4], act='essence', cur='Essence_of_the_Breach', ess='maxq', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 지우고 최대 퀄리티 +20%', 'The junk prefix goes for +20% Maximum Quality'),
  showText=[{'s': 'p', 'kr': '최대 퀄리티 +20% (제작 옵션)', 'en': '+20% to Maximum Quality (crafted)'}], edges=[{'to': 'k5'}],
  item=[MQ, UN('p'), CS, JS])
A(id='k5', kind='act', group='prep', pos=[0, 5], act='quality', cur='Neural_Catalyst', count=40, q=40, label=K('퀄리티', 'Quality'),
  goal=K('마나 퀄리티 40%', '40% mana quality'), edges=[{'to': 'k6'}], item=[MQ, UN('p'), CS, JS])
A(id='k6', kind='act', group='prep', pos=[0, 6], act='quality', cur='Vaal_Catalysing_Infuser', count=1, q=41, label=K('퀄리티', 'Quality'),
  goal=K('퀄리티 41% — 첫 1개는 타락 없음', 'Quality 41%: the first one never corrupts'), edges=[{'to': 'km'}], item=[MQ, UN('p'), CS, JS])
# ---------------- 옵션 추가 작업 (가이드 5~7단계, 성공 회차 21:45~23:38) ----------------
A(id='km', kind='mark', group='main', pos=[0, 7.4], next='m1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[MQ, UN('p'), CS, JS])
A(id='m1', kind='cleanup', group='main', pos=[0, 8.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'm2'}], item=[CS, JS])
A(id='m2', kind='act', group='main', pos=[0, 9.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 두번째 옵션 — 마나 재생 속도 1티어', 'Second suffix: T1 mana regeneration'),
  showText=[K('마나 재생 속도·아이템 희귀도·모든 원소 저항 1티어 중 먼저 뜬 것', 'Whichever T1 mana regeneration, item rarity or all resistances lands first')],
  edges=[{'if': {'has': 'good'}, 'to': 'm3', 'res': 'ok'}, {'to': 'm2', 'res': 'fail'}], item=[CS, RG])
A(id='m3', kind='act', group='main', pos=[0, 10.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('에센스가 지울 접두', 'The prefix for the essence to remove'), showText=[K('잡옵 1개', 'One junk option')],
  edges=[{'to': 'm4'}])
A(id='m4', kind='act', group='main', pos=[0, 11.4], act='essence', cur='Perfect_Essence_of_the_Mind', ess='pmana', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('에센스', 'Essence'), goal=K('접두 잡옵을 최대 마나 %로', 'The junk prefix becomes % maximum mana'),
  showText=[{'s': 'p', 'kr': '최대 마나 (4—6)% 증가 (제작 옵션)', 'en': '(4—6)% increased maximum Mana (crafted)'}], edges=[{'to': 'm5'}])
A(id='m5', kind='act', group='main', pos=[0, 12.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째 옵션 — 아이템 희귀도', 'Second prefix: item rarity'), show=['rarP'],
  edges=[{'if': {'has': 'rarP'}, 'to': 'm6', 'res': 'ok'}, {'if': V1, 'to': 'm5x', 'res': 'fail'}, {'to': 'm6', 'res': 'ok', 'label': K('에센셜: 결과 그대로', 'Essential: keep it')}])
A(id='m5x', kind='act', group='main', pos=[1, 12.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기 (셋 중 하나)', 'Remove the missed prefix (one of three)'),
  edges=[{'if': {'not': {'has': 'good'}}, 'to': 'm1', 'res': 'fail'},
         {'if': {'not': {'has': 'pmana'}}, 'to': 'm4', 'res': 'fail'},
         {'to': 'm5', 'res': 'fail'}])
A(id='m6', kind='act', group='main', pos=[0, 13.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 세번째 옵션', 'Third suffix'), showText=[K('랜덤 옵션', 'Random option')],
  edges=[{'to': 'm7'}], item=[PMu, RPu, CS, RG, CR])
A(id='m7', kind='act', group='main', pos=[0, 14.4], act='desecrate', cur='Ancient_Collarbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'm8'}],
  item=[PMu, RPu, UN('p'), CS, RG, CR])
A(id='m8', kind='act', group='main', pos=[0, 15.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='mana', label=K('공개', 'Reveal'),
  goal=K('접두 세번째 옵션(훼손) — 마나 최대치', 'Third prefix (desecrated): maximum mana'), show=['mana'],
  edges=[{'if': {'added': 'mana'}, 'to': 'ok', 'res': 'ok'},
         {'if': V1, 'to': 'm8x', 'res': 'fail'},
         {'to': 'ok', 'res': 'fail', 'hide': True}],
  item=[PMu, RPu, MA, CS, RG, CR])
A(id='m8x', kind='act', group='main', pos=[1, 15.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'm7', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='ok', kind='done', group='main', pos=[0, 16.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['m3', 'm4', 'm5', 'm5x'], 'kr': '접두 두 자리', 'en': 'Two prefixes', 'fold': True,
  'goal': K('접두 최대 마나 % + 아이템 희귀도', 'Prefixes: % maximum mana + item rarity'),
  'goalBy': {'bal': K('접두 최대 마나 % + 아이템 희귀도 1~2티어', 'Prefixes: % maximum mana + T1–2 item rarity'),
             'ess': K('접두 최대 마나 % + 랜덤 옵션 1개', 'Prefixes: % maximum mana + one random option')},
  'steps': [K('좌측 찬미의 징조 + 상위 엑잘티드 오브로 접두 잡옵', 'Omen of Sinistral Exaltation + Greater Exalted Orb for a junk prefix') | {'node': 'm3'},
            K('좌측 결정화의 징조 + 완벽한 정신의 에센스로 그 잡옵을 최대 마나 %로', 'Omen of Sinistral Crystallisation + Perfect Essence of the Mind turns it into % maximum mana') | {'node': 'm4'},
            K('좌측 찬미의 징조 + 상위 엑잘티드 오브로 아이템 희귀도', 'Omen of Sinistral Exaltation + Greater Exalted Orb for item rarity') | {'node': 'm5'},
            K('빗나가면 소멸의 오브, 최대 마나 %가 지워지면 에센스부터', 'A miss: Orb of Annulment; % maximum mana gone, essence again') | {'node': 'm5x'}],
  'worst': {'kr': '마나 재생 속도가 지워지면 분열 + 옵션 1개부터', 'en': 'Mana regeneration gone: back to the fracture + one option', 'to': 'm1'},
  'item': [PM, RP, CS, RG], 'itemBy': {'ess': [PM, RP, CS, RG]}},
 {'id': 'L2', 'nodes': ['m7', 'm8', 'm8x'], 'kr': '훼손 공개', 'en': 'Reveal'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
