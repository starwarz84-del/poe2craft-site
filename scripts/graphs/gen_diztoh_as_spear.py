# G3 2026-11-13: Diztoh 트위스터 공격 속도 창(cTjgn7NnHR8) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G3/diztoh-as-spear-v2/timeline.md, frames/ (영상 0:00~9:18 화면 대조)
# 실행: cd scripts/graphs && python3 gen_diztoh_as_spear.py  → diztoh-as-spear-v2.json (gen_batch11.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/diztoh-as-spear-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 줄 — 영상 성공 회차에 나온 옵션
PJ = L('s', '모든 투사체 스킬 레벨 +4', '+4 to Level of all Projectile Skills', 'f', ['proj'])
LPK = L('s', '처치한 적 하나당 생명력 획득', 'Gain Life per enemy killed', 'j')
AS = L('s', '공격 속도 (20—22)% 증가', '(20—22)% increased Attack Speed', 'n', ['as3'])
PHj = L('p', '물리 피해 추가 (낮은 티어)', 'Adds Physical Damage (low tier)', 'j')
SOV = L('s', '장착된 증강물 효과 (20—30)% 증가 (군주의 합금)', '(20—30)% increased effect of Socketed Augment Items (Sovereign Alloy)', 'c', ['sov'])
CEL = L('p', '정확도 +(327—427), 공격 속도 (5—8)% 증가 (천상의 합금)', '+(327—427) to Accuracy Rating, (5—8)% increased Attack Speed (Celestial Alloy)', 'c', ['cel'])
UN = L('p', '접두 훼손 옵션 (미공개)', 'Prefix desecration (unrevealed)', 'n')
PH5 = L('p', '물리 피해 (10—15)~(18—26) 추가', 'Adds (10—15) to (18—26) Physical Damage', 'n')   # 태그 없음: 엑잘은 나오는 대로
TH = L('p', '명시된 속도 옵션 효과 (25—30)% 증가 (훼손)', '(25—30)% increased Explicit Speed Modifier magnitudes (desecrated)', 'd', ['thrud'])
AST = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')
THR = L('r', '스루드의 완력', 'Thrud’s Might', 'r')
J = lambda s: L(s, '잡옵', 'Junk', 'j')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'diztoh-as-spear-v2', 'recipe': 'diztoh-as-spear-v2', 'cls': 'Spears', 'base': 'Akoyan Spear', 'ilvl': 82,
 'xsub': ["Thrud's Might"], 'astrid': True,
 'note': ('2026-11-13 G3 영상 전체 화면 대조(근거 scratchpad review/G3/diztoh-as-spear-v2/timeline.md). 성공 회차 한 줄(영상은 창 하나): '
          '투사체 +4 분열 + 처치당 생명력 아코야의 창(아이템 레벨 82, 아스트리드의 창의성 장착, 0:02) → 카오스 오브 반복 → 공격 속도 3티어 20%(0:16 툴팁, 1:28) → '
          '좌측 찬미 + 상위 엑잘로 접두 잡옵(1:34~1:36) → 좌측 결정화 + 군주의 합금, 접두 잡옵이 지워지고 장착 증강 효과 28%(2:16~2:22) → 상위 엑잘(징조 없음) 접두 잡옵(2:46) → '
          '좌측 결정화 + 천상의 합금, 정확도 + 공격 속도(2:36·2:54) → 아스트리드를 스루드의 완력으로 교체(3:12~3:20) → 고대 턱뼈 접두 훼손(3:30) → 상위 엑잘 세 번째 접두(물리 피해 추가 5티어, 3:52) → '
          '심연의 메아리 공개, 다시 뽑기로 명시된 속도 옵션 효과 29%(4:06~4:12, 빛의 징조로 다시 하는 장면 없음). 신성한 오브(5:26~5:40), 절사 + 좌측 말소 + 상위 카오스로 세 번째 접두 다시(5:52~6:17, 번개 6티어로 나빠짐 — 마지막 옵션 도박이라 뺌, 꿀팁 후보), 바알·타락(6:20~9:18)은 뺌. '
          '내부 결정: 공격 속도는 영상대로 1~3티어(\'최소 16%\'), 마지막 접두 다시 굴리기는 등급 기준(10장 2번)대로 랜덤 옵션 — 영상도 한 번 굴리고 나빠진 결과를 받음. '
          '11-13 오후 새 정책(P8): (B) 영상은 공개를 메아리 다시 뽑기 한 번으로 끝내고 빛의 징조로 다시 하지 않아 빛의 징조 반복을 뺌, 공개 결과 그대로(카드 랜덤 옵션) '
          '(D) 그러면 밸런스·에센셜의 과정·완성품이 같아 밸런스 하나만(옛 시뮬 55.5/27.6).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상 그대로: 훼손 공개 한 번(메아리로 다시 뽑기), 결과 그대로', 'As the video: one reveal (Abyssal Echoes reroll), kept as it comes')}],
 'tags': {
   'proj': {'gi': 11, 'tmax': 1}, 'as3': {'gi': 17, 'tmax': 3}, 'sov': {'gi': 63}, 'cel': {'gi': 64}, 'thrud': {'gi': 74}},
 'require': {'all': [{'has': 'proj'}, {'has': 'as3'}, {'has': 'sov'}, {'has': 'cel'}, {'full': 'p'}, {'desSide': 'p'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h1',
 'finalItem': {'quality': 20, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='h1', kind='base', group='prep', pos=[0, 0], next='ms',
  start={'rar': 'rare', 'mods': [{'tag': 'proj', 'fr': True}, {'junk': 's'}], 'runes': [K('아스트리드의 창의성', 'Astrid’s Creativity')]},
  label=K('투사체 스킬 +4 분열 아코야의 창 구입 (아이템 레벨 82, 아스트리드의 창의성 장착)', 'Buy an Akoyan Spear with fractured +4 projectile skills (item level 82, Astrid’s Creativity socketed)'),
  item=[PJ, LPK, AST])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[PJ, LPK, AST])
A(id='c1', kind='act', group='main', pos=[0, 2.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 공격 속도 3티어 (1~3티어)', 'T3 attack speed suffix (T1–3)'), show=['as3'],
  edges=[{'if': {'has': 'as3'}, 'to': 'e1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}],
  item=[PJ, AS, AST])
A(id='e1', kind='act', group='main', pos=[0, 3.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('합금이 지울 접두', 'The prefix for the alloy to remove'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'y1'}], item=[PHj, PJ, AS, AST])
A(id='y1', kind='act', group='main', pos=[0, 4.4], act='essence', cur='Sovereign_Alloy', ess='sov', omens=['Omen_of_Sinistral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('접두 잡옵을 지우고 접미 장착된 증강물 효과', 'Clear the junk prefix for the socketed augment effect suffix'),
  showText=[{'s': 's', 'kr': '장착된 증강물 효과 (20—30)% 증가 (제작 옵션)', 'en': '(20—30)% increased effect of Socketed Augment Items (crafted)'}],
  edges=[{'to': 'e2'}], item=[PJ, AS, SOV, AST])
A(id='e2', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('합금이 지울 접두', 'The prefix for the alloy to remove'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개', 'en': 'One random option'}],
  edges=[{'to': 'y2'}], item=[PHj, PJ, AS, SOV, AST])
A(id='y2', kind='act', group='main', pos=[0, 6.4], act='essence', cur='Celestial_Alloy', ess='cel', omens=['Omen_of_Sinistral_Crystallisation'], label=K('합금', 'Alloy'),
  goal=K('접두 잡옵을 정확도 + 공격 속도로', 'Swap the junk prefix for accuracy + attack speed'),
  showText=[{'s': 'p', 'kr': '정확도 + 공격 속도 (제작 옵션)', 'en': 'Accuracy + attack speed (crafted)'}],
  edges=[{'to': 'r1'}], item=[CEL, PJ, AS, SOV, AST])
A(id='r1', kind='act', group='main', pos=[0, 7.4], act='rune', label=K('룬', 'Rune'), goal=K('아스트리드의 창의성을 스루드의 완력으로 교체', 'Swap Astrid’s Creativity for Thrud’s Might'),
  showText=[K('제작 옵션 2개는 그대로, 스루드 옵션이 훼손 공개에 나옴', 'Both crafted options stay; Thrud options join the reveal')],
  rune=K('스루드의 완력', 'Thrud’s Might'), swapAstrid=True,
  edges=[{'to': 'd1'}], item=[CEL, PJ, AS, SOV, THR])
A(id='d1', kind='act', group='main', pos=[0, 8.4], act='desecrate', cur='Ancient_Jawbone', label=K('훼손', 'Desecrate'),
  goal=K('접두 두 번째 옵션(훼손)', 'Second prefix option (desecrated)'),
  showText=[{'s': 'p', 'kr': '접두 훼손 옵션 (미공개)', 'en': 'Prefix desecration (unrevealed)'}],
  edges=[{'to': 'e3'}], item=[CEL, UN, PJ, AS, SOV, THR])
A(id='e3', kind='act', group='main', pos=[0, 9.4], act='exalt', cur='Greater_Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 세 번째 옵션', 'Third prefix option'), showText=[{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}],
  edges=[{'to': 'v1'}], item=[CEL, UN, PH5, PJ, AS, SOV, THR])
A(id='v1', kind='act', group='main', pos=[0, 10.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], label=K('공개', 'Reveal'),
  goal=K('접두 훼손 옵션 공개 — 나오는 대로', 'Reveal the prefix desecration: keep what comes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}],
  edges=[{'to': 'ok'}],
  item=[CEL, TH, PH5, PJ, AS, SOV, THR])   # 2026-11-13 P8 새 정책 B: 영상 4:06~4:12 메아리 다시 뽑기 한 번, 빛의 징조 반복 없음
# 영상 5:52~6:17 절사 + 좌측 말소 + 상위 카오스(세 번째 접두 다시, 번개 6티어로 나빠짐)는 마지막 옵션 도박이라 등급 기준(10장 2번)대로 뺌 — 꿀팁 후보
A(id='ok', kind='done', group='main', pos=[0, 12.4], label=K('완성', 'Finished'))
g['nodes'] = N

g['loops'] = []
g['finals'] = [
 {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
  'lines': [{'tag': 'cel', 'ess': True}, {'side': 'p', 'random': True}, {'side': 'p', 'random': True}, {'tag': 'proj', 'fr': True}, {'tag': 'as3'}, {'tag': 'sov', 'ess': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
