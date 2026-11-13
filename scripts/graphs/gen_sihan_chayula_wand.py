# G1 2026-11-13: 시한 차율라 마법봉(rSs4fumlHo4, 9:29) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G1/sihan-chayula-wand-v2/timeline.md, frames/ (영상 0:00~9:29 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_chayula_wand.py  → sihan-chayula-wand-v2.json (gen_batch22.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-chayula-wand-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(2:45~8:08)에 실제로 나온 옵션
CH = L('p', '카오스 피해 (105—119)% 증가 (분열)', '(105—119)% increased Chaos Damage (fractured)', 'f', ['chaos'])
SC = L('s', '주문 치명타 명중 확률 (60—73)% 증가', '(60—73)% increased Critical Hit Chance for Spells', 'n', ['scrit'])
IN = L('s', '지능 +(28—30)', '+(28—30) to Intelligence', 'n', ['int'])
S3 = L('s', '모든 주문 스킬 레벨 +3 (완벽한 마술의 에센스)', '+3 to Level of all Spell Skills (Perfect Essence of Sorcery)', 'c', ['sp3'])
CE = L('p', '마나 최대치 +(142—188) / 모든 주문 스킬 레벨 +1 (천공의 합금)', '+(142—188) to maximum Mana / +1 to Level of all Spell Skills (Celestial Alloy)', 'c', ['cel'])
UL = L('p', '피해의 (21—25)%를 추가 물리 피해로 획득 (훼손)', 'Gain (21—25)% of Damage as Extra Physical Damage (desecrated)', 'd', ['ula'])
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')
V1 = {'param': {'v': 1}}

g = {
 'id': 'sihan-chayula-wand-v2', 'recipe': 'sihan-chayula-wand-v2', 'cls': 'Wands', 'base': 'Attuned Wand', 'ilvl': 82, 'basePrice': {},
 'note': ('2026-11-13 G1 영상 전체 화면 대조. 성공 회차 한 줄: 특출난 조율된 마법봉(아이템 레벨 82, 룬 소켓 2, 카오스 피해 1티어 분열 + 지능 잡옵, 2:45) → '
          '카오스 오브로 주문 치명타 명중 확률 64% 1티어(3:24) → 우측 찬미 + 완벽한 엑잘로 접미 두번째 옵션, 빗나가면 소멸의 오브(3:20·3:37, 성공 5:01~5:26 지능 +28 2티어) → '
          '좌측 찬미 + 엑잘로 접두 잡옵(설명 1:00·5:52·8:20 — 영상 성공 회차는 절사 카오스 데모에서 마나 최대치가 접두로 떠서 그대로 씀, 4:50) → '
          '좌측 결정화 + 완벽한 마술의 에센스로 접두 잡옵을 지우고 접미 주문 +3(6:10~6:28) → 아스트리드의 창의성(6:35) → 보존된 턱뼈로 접두 미공개 훼손(6:44~6:52) → '
          '좌측 결정화 + 천공의 합금으로 미공개 훼손을 지우고 마나 최대치·주문 +1(7:00~7:14) → 군주의 징조 + 보존된 턱뼈(7:32~7:40) → 심연의 메아리 공개, 추가 물리 23%(7:44~7:57). '
          '3:44~4:50 절사의 징조 + 카오스 데모는 영상에서 "절삭한 건 잊어 주세요"(5:30)라 넣지 않음. '
          '등급(난이도 3 = 밸런스·에센셜, 정책 10장 C17): 밸런스 = 주문 치명타 1~2티어(영상 3:00 "1티어 혹은 2티어"), 접미 두번째 옵션 = 지능 1~2티어 반복(영상 성공 회차) '
          '에센셜 = 주문 치명타 1~4티어(영상 8:00 "2티어 3티어도 괜찮습니다"), 접미 두번째 옵션은 결과 그대로. 공개는 군주의 징조로 울라만 접두 3개 중 추가 물리 피해가 확정이라 두 등급 같음.'),
 'params': {
  'cT': {'kr': '주문 치명타 명중 확률', 'en': 'Spell crit chance', 'values': {'2': K('1~2티어', 'T1–2'), '4': K('1~4티어', 'T1–4')}},
  'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('반복', 'Repeat'), '2': K('결과 그대로', 'As it comes')}},
 },
 'strategies': [{'id': 'bal', 'params': {'cT': 2, 'v': 1}}, {'id': 'ess', 'params': {'cT': 4, 'v': 2}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'cT': 4, 'v': 2}, 'tier': 'ess',
   'desc': K('주문 치명타 1~4티어, 접미 두번째 옵션 결과 그대로', 'T1–4 spell crit; second suffix kept as it comes')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'cT': 2, 'v': 1}, 'tier': 'bal',
   'desc': K('영상: 주문 치명타 1~2티어, 지능 1~2티어, 추가 물리 피해', 'Video: T1–2 spell crit, T1–2 intelligence, extra physical damage')}],
 'tags': {
  'chaos': {'gi': 8, 'tmax': 1}, 'scrit': {'gi': 20, 'tmax': '$cT'}, 'scrit2': {'gi': 20, 'tmax': 2}, 'scrit4': {'gi': 20, 'tmax': 4},
  'int': {'gi': 0, 'tmax': 2}, 'sp3': {'gi': 50}, 'cel': {'gi': 59}, 'ula': {'gi': 43},
 },
 'require': {'all': [{'has': 'chaos'}, {'has': 'scrit'}, {'has': 'sp3'}, {'has': 'cel'}, {'has': 'ula'}, {'any': [{'not': V1}, {'has': 'int'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 0, 'sockets': 2},   # 영상 8:08 완성품 툴팁에 퀄리티 줄 없음(RV4 11-13)
 'finals': [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'chaos', 'fr': True}, {'tag': 'cel', 'ess': True}, {'tag': 'ula', 'des': True},
             {'tag': 'scrit2'}, {'tag': 'int'}, {'tag': 'sp3', 'ess': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'chaos', 'fr': True}, {'tag': 'cel', 'ess': True}, {'tag': 'ula', 'des': True},
             {'tag': 'scrit4'}, {'side': 's', 'random': True}, {'tag': 'sp3', 'ess': True}]}],
}

N = []
RND = L('s', '랜덤 옵션', 'Random option', 'j')
def A(**kw):
    # 에센셜은 접미 두번째 옵션을 결과 그대로 — 왼쪽 아이템 칸의 지능을 랜덤 옵션으로
    if IN in kw.get('item', []):
        o = next((x for x in kw.setdefault('over', []) if x['param'] == {'v': 2}), None)
        if not o: o = {'param': {'v': 2}, 'set': {}}; kw['over'].append(o)
        o['set']['item'] = [RND if x is IN else x for x in kw['item']]
    N.append(kw)

# ---------------- 베이스템 완성 (영상 2:45) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms',
  start={'rar': 'rare', 'mods': [{'tag': 'chaos', 'fr': True}, {'junk': 's'}]},
  label=K('특출난 조율된 마법봉 구입 (아이템 레벨 82, 룬 소켓 2, 카오스 피해 분열 + 잡옵 1개)',
          'Buy an exceptional Attuned Wand (item level 82, two rune sockets, fractured chaos damage + one junk option)'),
  item=[CH, J('s')])

# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='w2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[CH, J('s')])
# 2:58~3:24 카오스 오브 반복: 지능 +13 → 주문 피해·마나 → 주문 치명타 64%(1티어)
A(id='w2', kind='act', group='main', pos=[0, 2.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫번째 옵션 — 주문 치명타 명중 확률', 'First suffix: spell critical hit chance'), show=['scrit'],
  edges=[{'if': {'has': 'scrit'}, 'to': 'w3', 'res': 'ok'}, {'to': 'w2', 'res': 'fail', 'hide': True}], item=[CH, SC])
# 3:20 우측 찬미 + 3:36 완벽한 엑잘(처치 시 마나 = 빗나감) → 3:37 소멸 → … 5:01 우측 찬미 + 완벽한 엑잘 → 5:26 지능 +28
A(id='w3', kind='act', group='main', pos=[0, 3.4], act='exalt', cur='Perfect_Exalted_Orb', omens=['Omen_of_Dextral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접미 두번째 옵션 — 지능', 'Second suffix: intelligence'), show=['int'],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접미 두번째 옵션', 'Second suffix'), 'show': [], 'showText': [{'s': 's', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}]}}],
  edges=[{'if': {'param': {'v': 2}}, 'to': 'w4', 'res': 'ok', 'hide': True}, {'if': {'has': 'int'}, 'to': 'w4', 'res': 'ok'},
         {'to': 'w3x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[CH, SC, IN])
A(id='w3x', kind='act', group='main', pos=[1, 3.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('빗나간 접미 지우기 — 주문 치명타가 지워지면 카오스부터', 'Remove the missed suffix: back to Chaos if spell crit goes'),
  edges=[{'if': {'has': 'scrit'}, 'to': 'w3', 'res': 'ok', 'label': K('주문 치명타 남음', 'Spell crit kept')},
         {'to': 'w2', 'res': 'fail', 'label': K('주문 치명타가 지워짐', 'Spell crit gone')}])
# 설명 1:00·5:52·8:20: 좌측 찬미 + 엑잘로 접두 잡옵(영상 성공 회차는 4:50 카오스로 뜬 마나 최대치를 그대로 씀)
A(id='w4', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'],
  label=K('엑잘', 'Exalt'), goal=K('접두 잡옵 — 에센스가 지울 자리', 'Junk prefix for the essence to remove'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}], edges=[{'to': 'w5'}], item=[CH, J('p'), SC, IN])
# 6:10 좌측 결정화 + 6:18 완벽한 마술의 에센스 → 6:28 접두 잡옵 사라지고 접미 주문 +3
A(id='w5', kind='act', group='main', pos=[0, 5.4], act='essence', cur='Perfect_Essence_of_Sorcery', ess='sp3',
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('에센스', 'Essence'),
  goal=K('접두 잡옵을 지우고 접미 모든 주문 스킬 레벨 +3', 'Swap the junk prefix for +3 to all spell skills (suffix)'),
  showText=[{'s': 's', 'kr': '모든 주문 스킬 레벨 +3 (제작 옵션)', 'en': '+3 to Level of all Spell Skills (crafted)'}],
  edges=[{'to': 'w6'}], item=[CH, SC, IN, S3])
# 6:35 아스트리드의 창의성
A(id='w6', kind='act', group='main', pos=[0, 6.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'w7'}], item=[CH, SC, IN, S3, AST])
# 6:44 보존된 턱뼈 → 6:52 접두 미공개 훼손(공개하지 않음)
A(id='w7', kind='act', group='main', pos=[0, 7.4], act='desecrate', cur='Preserved_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 두번째 옵션(훼손) — 합금이 지울 자리', 'Second prefix (desecrated) for the alloy to remove'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'w8'}], item=[CH, UN('p'), SC, IN, S3, AST])
# 7:00 좌측 결정화 + 천공의 합금 → 7:14 마나 최대치 +145 / 주문 +1
A(id='w8', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Celestial_Alloy', ess='cel',
  omens=['Omen_of_Sinistral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('미공개 훼손을 지우고 천공의 합금', 'Swap the unrevealed desecration for the Celestial Alloy'),
  showText=[{'s': 'p', 'kr': '마나 최대치 +(142—188) / 모든 주문 스킬 레벨 +1 (제작 옵션)', 'en': '+(142—188) to maximum Mana / +1 to Level of all Spell Skills (crafted)'}],
  edges=[{'to': 'w9'}], item=[CH, CE, SC, IN, S3, AST])
# 7:32 군주의 징조 + 7:40 보존된 턱뼈
A(id='w9', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_the_Sovereign'],
  label=K('훼손', 'Desecrate'), goal=K('접두 세번째 옵션 — 울라만 훼손', 'Third prefix: Ulaman desecration'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'w10'}], item=[CH, CE, UN('p'), SC, IN, S3, AST])
# 7:44 심연의 메아리 → 7:57 공개 3개 중 추가 물리 피해 23%
A(id='w10', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='ula', label=K('공개', 'Reveal'),
  goal=K('접두 세번째 옵션(훼손) — 피해의 %를 추가 물리 피해로 획득', 'Third prefix (desecrated): damage gained as extra physical'), show=['ula'],
  edges=[{'to': 'ok', 'res': 'ok'}], item=[CH, CE, UL, SC, IN, S3, AST])   # 군주의 징조 = 공개 3개가 모두 울라만 옵션, 마법봉 울라만 접두는 3개라 확정(영상 2:10 "확정으로 뜹니다", 7:57 선택지 3개)
A(id='ok', kind='done', group='main', pos=[0, 11.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['w3', 'w3x'], 'kr': '접미 두번째 옵션', 'en': 'Second suffix'},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
