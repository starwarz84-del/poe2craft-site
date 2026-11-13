# G1 2026-11-13: 시한 차율라 장갑(Sf-2cvWhQY0, 10:27) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G1/sihan-chayula-gloves-v2/timeline.md, frames/ (영상 0:00~10:27 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_chayula_gloves.py  → sihan-chayula-gloves-v2.json (gen_batch22.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-chayula-gloves-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(시신의 손아귀 고정된 싸개, 4:00~9:20)에 실제로 나온 옵션
KAT = L('r', '카틀라의 순흑', 'Katla’s Gloom', 'r')
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
PO = L('p', '플레이어가 유발하는 중독의 강도 (30—42)% 증가 (분열)', '(30—42)% increased Magnitude of Poison you inflict (fractured)', 'f', ['pois'])
CU = L('s', '저주 활성화 속도 (20—30)% 가속', '(20—30)% faster Curse Activation', 'n', ['curse'])
RW = L('p', '룬 수호 (24—30)% 증가 (군왕의 합금)', '(24—30)% increased Runic Ward (Sovereign Alloy)', 'c', ['rward'])
PE = L('p', '피해가 (9—15)%의 원소 저항 관통 (분광 합금)', 'Damage Penetrates (9—15)% Elemental Resistances (Prismatic Alloy)', 'c', ['pen'])
FA = L('p', '피해를 주는 상태 이상의 피해 (14—20)%만큼 가속 (훼손)', 'Damaging Ailments deal damage (14—20)% faster (desecrated)', 'd', ['fast'])
RS = L('s', '랜덤 옵션', 'Random option', 'j')
RD = L('p', '랜덤 옵션 (공개된 훼손 옵션)', 'Random option (revealed desecration)', 'j')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
V1 = {'param': {'v': 1}}; V2 = {'param': {'v': 2}}

g = {
 'id': 'sihan-chayula-gloves-v2', 'recipe': 'sihan-chayula-gloves-v2', 'cls': 'Gloves_dex_int', 'base': 'Secured Wraps', 'ilvl': 83, 'basePrice': {},
 'xsub': ["Katla's Gloom"], 'xroll': True,
 'note': ('2026-11-13 G1 영상 전체 화면 대조. 성공 회차(시신의 손아귀 고정된 싸개, 아이템 레벨 83) 한 줄: 카틀라의 순흑 장착 + 중독의 강도 42% 1티어 분열(2:35~2:45) → 소멸로 분열 + 옵션 1개(3:58) → '
          '카오스 오브로 저주 활성화 속도 25%(4:00~4:06, 첫 시도 3:00은 21%) → 상위 찬미 + 완벽한 엑잘로 접미 2개·접두 2개 랜덤(4:10~5:46, 성공 회차 접미 = 지능 29 · 카오스 저항 26) → '
          '아스트리드의 창의성(6:22) → 좌측 결정화 + 군왕의 합금(6:26~6:38 룬 수호 28%, 자막 “군항의 합금”) → 좌측 결정화 + 분광 합금(6:50~7:02, 남은 잡옵이 없을 때까지 두 합금으로 덮음, 자막 6:45 "두 줄 될 때까지") → '
          '좌측 강령술 + 보존된 갈비뼈(7:10, 메아리 없음) → 공개 빗나감(7:30) → 분광 합금으로 다시 덮고 보존된 갈비뼈(7:20~7:40) → 피해를 주는 상태 이상의 피해 18% 가속(7:44~7:50). '
          '3:00~3:58 첫 시도(정확도·상태 이상 강도 접두, 저항 접미)와 4:20~5:40 중간 정리(깡 소멸, 심연의 에센스 징표 → 갈비뼈 → 공개)는 결과가 모두 합금으로 덮여 플로우차트에 넣지 않음. '
          '등급(난이도 3 = 밸런스·에센셜, C17): 밸런스 = 마지막 공개 상태 이상 피해 가속 반복(카틀라 옵션은 2티어뿐), 에센셜 = 공개 결과 그대로. 엑잘로 붙인 접미 2개는 영상대로 랜덤(1:40 "3 유효 정도만").'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('반복', 'Repeat'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
  {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
   'desc': K('마지막 훼손 공개 결과 그대로', 'Keep the last desecration reveal as it comes')},
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
   'desc': K('영상: 중독 강도·저주 활성화 속도 + 공개 상태 이상 피해 가속', 'Video: poison magnitude, curse activation and a revealed faster ailment damage')}],
 'tags': {
  'pois': {'gi': 88, 'tmax': 1}, 'curse': {'gi': 99, 'tmax': 1}, 'fast': {'gi': 90, 'tmax': 2},
  'rward': {'gi': 73}, 'pen': {'gi': 71},
  'craft': {'anyOf': ['rward', 'pen'], 'label': K('룬 수호 증가·원소 저항 관통 중 남은 제작 옵션', 'Whichever crafted line stays: runic ward or elemental penetration')},
  'pkeep': {'anyOf': ['pois', 'rward', 'pen']},
 },
 'require': {'all': [{'has': 'pois'}, {'has': 'curse'}, {'has': 'craft'}, {'full': 'p'}, {'full': 's'}, {'any': [V2, {'has': 'fast'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finalItem': {'quality': 20, 'sockets': 2},
 'finals': [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'pois', 'fr': True}, {'tag': 'fast', 'des': True}, {'tag': 'craft', 'ess': True, 'des': False},
             {'tag': 'curse'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
  {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
   'lines': [{'tag': 'pois', 'fr': True}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'craft', 'ess': True, 'des': False},
             {'tag': 'curse'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
}

N = []
def A(**kw):
    # 에센셜은 마지막 공개 결과 그대로 — 왼쪽 아이템 칸의 상태 이상 피해 가속을 랜덤 옵션으로
    it = kw.get('item', [])
    if FA in it:
        o = next((x for x in kw.setdefault('over', []) if x['param'] == {'v': 2}), None)
        if not o: o = {'param': {'v': 2}, 'set': {}}; kw['over'].append(o)
        o['set']['item'] = [RD if x is FA else x for x in it]
    N.append(kw)

# ---------------- 베이스템 완성 (영상 0:10~0:40 방법, 2:35~3:58 성공 회차 베이스) ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='pk',
  start={'rar': 'rare', 'mods': [{'tag': 'pois', 'fr': True}, {'junk': 's'}]},
  label=K('특출난 고정된 싸개 구입 (아이템 레벨 83, 룬 소켓 2, 중독의 강도 1티어 분열 + 잡옵 1개)', 'Buy exceptional Secured Wraps (item level 83, two rune sockets, fractured T1 poison magnitude + one junk option)'),
  item=[PO, J('s')])
A(id='pk', kind='act', group='prep', pos=[0, 1], act='rune', rune=K('카틀라의 순흑', 'Katla’s Gloom'), label=K('룬', 'Rune'),
  goal=K('카틀라의 순흑 장착', 'Socket Katla’s Gloom'), showText=[K('카틀라 옵션이 붙을 수 있음', 'Katla lines can roll')],
  edges=[{'to': 'ms'}], item=[PO, J('s'), KAT])

# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 2.4], next='g2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PO, J('s'), KAT])
# 4:00~4:06 카오스 오브 → 저주 활성화 속도 25%
A(id='g2', kind='act', group='main', pos=[0, 3.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 첫번째 옵션 — 저주 활성화 속도', 'First suffix: curse activation speed'), show=['curse'],
  edges=[{'if': {'has': 'curse'}, 'to': 'g4', 'res': 'ok'}, {'to': 'g2', 'res': 'fail', 'hide': True}], item=[PO, CU, KAT])
# 3:30 자막 "전미어 두 줄 랜덤", 5:00 상위 찬미(2/10) → 성공 회차 접미 지능 29 · 카오스 저항 26(5:46)
A(id='g4', kind='act', group='main', pos=[0, 4.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation', 'Omen_of_Dextral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접미 두번째·세번째 옵션', 'Second and third suffixes'), showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}],
  edges=[{'to': 'g3'}], item=[PO, CU, RS, RS, KAT])
# 3:10~3:20·4:20 상위 찬미 + 완벽한 엑잘 접두 2개(성공 회차는 출혈·점화 강도, 회피·에너지 보호막 — 모두 합금으로 덮임)
A(id='g3', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Perfect_Exalted_Orb',
  omens=['Omen_of_Greater_Exaltation', 'Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 두번째·세번째 옵션 — 합금이 지울 자리', 'Second and third prefixes for the alloys to replace'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'r1'}], item=[PO, J('p'), J('p'), CU, RS, RS, KAT])
# 6:22 아스트리드의 창의성
A(id='r1', kind='act', group='main', pos=[0, 6.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'),
  showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
  edges=[{'to': 'a1'}], item=[PO, J('p'), J('p'), CU, RS, RS, KAT, AST])
# 6:26~6:38 좌측 결정화 + 군왕의 합금(자막 '군항의 합금', 6:26에 룬 합금 툴팁도 보임 — 장갑 룬 수호는 군왕의 합금) → 룬 수호 28%, 6:50~7:02 좌측 결정화 + 분광 합금 → 원소 저항 관통(남은 잡옵이 없을 때까지)
A(id='a1', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Sovereign_Alloy', ess='rward', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('접두 잡옵 하나를 지우고 룬 수호 증가', 'A junk prefix goes for increased runic ward'),
  showText=[{'s': 'p', 'kr': '룬 수호 (24—30)% 증가 (제작 옵션)', 'en': '(24—30)% increased Runic Ward (crafted)'}],
  skipIf={'has': 'rward'}, skipTo='a2', skipHide=True, edges=[{'to': 'a2'}], item=[PO, RW, J('p'), CU, RS, RS, KAT, AST])
A(id='a2', kind='act', group='main', pos=[0, 8.4], act='essence', cur='Prismatic_Alloy', ess='pen', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('남은 접두 잡옵을 지우고 원소 저항 관통', 'The last junk prefix goes for elemental penetration'),
  showText=[{'s': 'p', 'kr': '피해가 (9—15)%의 원소 저항 관통 (제작 옵션)', 'en': 'Damage Penetrates (9—15)% Elemental Resistances (crafted)'}],
  skipIf={'has': 'pen'}, skipTo='d1', skipHide=True,
  edges=[{'if': {'sideAll': {'side': 'p', 'tag': 'pkeep'}}, 'to': 'd1', 'res': 'ok'},
         {'to': 'a1', 'res': 'fail', 'label': K('룬 수호가 지워짐', 'Runic ward gone')}],
  item=[PO, RW, PE, CU, RS, RS, KAT, AST])
# 7:10 좌측 강령술(8/10) + 보존된 갈비뼈 — 접두가 꽉 차 제작 옵션 하나가 지워짐(영상은 원소 저항 관통), 메아리 없음(자막 7:05)
A(id='d1', kind='act', group='main', pos=[0, 9.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 세번째 옵션(훼손) — 제작 옵션 하나를 지우고 들어감', 'Third prefix (desecrated): replaces one crafted line'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'rv'}], item=[PO, RW, UN('p'), CU, RS, RS, KAT, AST])
# 7:30 빗나감 → 7:44~7:50 피해를 주는 상태 이상의 피해 18% 가속
A(id='rv', kind='act', group='main', pos=[0, 10.4], act='reveal', want='fast', label=K('공개', 'Reveal'),
  goal=K('접두 세번째 옵션(훼손) — 피해를 주는 상태 이상의 피해 가속', 'Third prefix (desecrated): faster damaging ailments'), show=['fast'],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'), 'show': [], 'showText': [{'s': 'p', 'kr': '공개 결과 그대로', 'en': 'Keep the reveal'}]}}],
  edges=[{'if': V2, 'to': 'ok', 'res': 'ok', 'hide': True}, {'if': {'added': 'fast'}, 'to': 'ok', 'res': 'ok'},
         {'if': {'has': 'pen'}, 'to': 'rx2', 'res': 'fail', 'label': K('빗나감', 'Miss')},
         {'to': 'rx', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[PO, RW, FA, CU, RS, RS, KAT, AST])
# 7:20 "또 분광으로 해 주고 다시 보존" — 빗나간 훼손 옵션을 합금으로 덮고 다시 갈비뼈
A(id='rx', kind='act', group='main', pos=[1, 10.4], act='essence', cur='Prismatic_Alloy', ess='pen', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('빗나간 훼손 옵션을 분광 합금으로 덮기', 'Cover the missed desecration with a Prismatic Alloy'),
  edges=[{'if': {'sideAll': {'side': 'p', 'tag': 'pkeep'}}, 'to': 'd1', 'res': 'ok', 'label': K('다시 훼손', 'Desecrate again')},
         {'to': 'rx2', 'res': 'fail', 'hide': True}])
A(id='rx2', kind='act', group='main', pos=[1, 11.4], act='essence', cur='Sovereign_Alloy', ess='rward', omens=['Omen_of_Sinistral_Crystallisation'],
  label=K('합금', 'Alloy'), goal=K('남은 접두를 군왕의 합금으로 덮기', 'Cover the remaining prefix with a Sovereign Alloy'),
  edges=[{'if': {'sideAll': {'side': 'p', 'tag': 'pkeep'}}, 'to': 'd1', 'res': 'ok', 'label': K('다시 훼손', 'Desecrate again')},
         {'to': 'rx', 'res': 'fail', 'hide': True}])
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = [
 {'id': 'L1', 'nodes': ['a1', 'a2'], 'kr': '합금으로 접두 덮기', 'en': 'Cover prefixes with alloys'},
 {'id': 'L2', 'nodes': ['d1', 'rv', 'rx', 'rx2'], 'kr': '훼손 공개', 'en': 'Desecrate and reveal', 'fold': True,
  'goal': K('접두 세번째 옵션(훼손) — 피해를 주는 상태 이상의 피해 가속', 'Third prefix (desecrated): faster damaging ailments'),
  'goalBy': {'bal': K('접두 세번째 옵션(훼손) — 피해를 주는 상태 이상의 피해 가속', 'Third prefix (desecrated): faster damaging ailments'),
             'ess': K('접두 세번째 옵션(훼손) — 공개 결과 그대로', 'Third prefix (desecrated): keep the reveal')},
  'steps': [K('좌측 강령술의 징조 + 보존된 갈비뼈로 제작 옵션 하나를 지우고 훼손', 'Omen of Sinistral Necromancy + Preserved Rib replaces one crafted line') | {'node': 'd1'},
            K('영혼의 우물에서 공개', 'Reveal at the Well of Souls') | {'node': 'rv'},
            K('빗나가면 좌측 결정화의 징조 + 분광 합금으로 덮기', 'A miss: Omen of Sinistral Crystallisation + Prismatic Alloy to cover it') | {'node': 'rx'},
            K('원소 저항 관통이 남아 있으면 좌측 결정화의 징조 + 군왕의 합금으로 덮기', 'Penetration still there: Omen of Sinistral Crystallisation + Sovereign Alloy instead') | {'node': 'rx2'}],
  'item': [PO, RW, FA, CU, RS, RS, KAT, AST], 'itemBy': {'ess': [PO, RW, RD, CU, RS, RS, KAT, AST]}},
]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
