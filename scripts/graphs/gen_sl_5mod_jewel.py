# G4 2026-11-13: SL 5옵션 사파이어(VKMT7tuSIYk) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G4/sl-5mod-jewel-v2/timeline.md, frames/ (영상 0:00~13:10 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sl_5mod_jewel.py  → sl-5mod-jewel-v2.json (gen_batch10.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sl-5mod-jewel-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

AILn = L('s', '피해를 주는 상태 이상의 피해 (3—7)%만큼 가속', 'Damaging Ailments deal damage (3—7)% faster', 'n', ['ail'])
AIL = L('s', '피해를 주는 상태 이상의 피해 (3—7)%만큼 가속', 'Damaging Ailments deal damage (3—7)% faster', 'f', ['ail'])
MAG = L('p', '플레이어가 유발하는 상태 이상의 강도 (5—15)% 증가', '(5—15)% increased Magnitude of Ailments you inflict', 'n', ['p1'])
CHA = L('p', '카오스 피해 (7—13)% 증가', '(7—13)% increased Chaos Damage', 'n', ['p4'])
SPL = L('p', '주문 피해 (5—15)% 증가', '(5—15)% increased Spell Damage', 'd', ['p49'])
CP = L('s', '접두어 속성 부여의 최대 개수 +1개', '+1 Prefix Modifier allowed', 'c', ['contP'])
FER = L('s', '접두어 효과 (40—60)% 증가', '(40—60)% increased Effect of Prefixes', 'c', ['fer'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

PRE = ['p4', 'p49', 'p1', 'p29']   # 7:10~7:50 영상 카오스 목표: 카오스 피해·주문 피해·상태 이상의 강도·점화 강도(검은 화염 빌드)
PRE_LABEL = K('카오스 피해·주문 피해·상태 이상의 강도·점화 강도', 'Chaos Damage, Spell Damage, Magnitude of Ailments or Ignite Magnitude')

g = {
 'id': 'sl-5mod-jewel-v2', 'recipe': 'sl-5mod-jewel-v2', 'cls': 'Sapphire', 'base': 'Sapphire', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 5},   # 3:40 자막 '매물 400개, 5 div부터'(거래 화면 가격 글자는 화면으로 못 읽음)
 'note': ('2026-11-13 G4 영상 전체 화면 대조(근거 scratchpad review/G4/sl-5mod-jewel-v2/timeline.md). '
          '피해를 주는 상태 이상의 피해 가속 7% 사파이어 4개 구입(6:30, 옵션 4개) → 분열 1/4(6:58 상태 이상 가속 분열) → 소멸의 오브로 분열 + 옵션 1개(7:00) → '
          '카오스로 접두(8:02 상태 이상의 강도, 목표 카오스·주문·상태 이상 강도·점화 강도) → 좌측 찬미 + 엑잘, 빗나가면 소멸의 오브(8:05~8:21 카오스 피해) → 엑잘 접미 잡옵 → '
          '위력적인 액체 경멸 1/3(8:44 접미 잡옵이 지워지고 접두어 +1개) → 보존된 두개골(자막) + 심연의 메아리 공개(9:07 주문 피해) → 우측 소멸의 징조 + 소멸의 오브로 경멸 옵션 제거(9:35) → '
          '엑잘 접미 잡옵(9:48) → 위력적인 액체 흉포함(10:22 접두어 효과 43%). 흉포함 수치 다시 굴리기(카오스 → 흉포함, 10:20~10:40)·신성한 오브·카오스 기폭제 퀄리티(10:50)·바알 오브(11:30)는 뺌. '
          '내부 결정: 경멸 실패 처리(분열 + 옵션 1개로 되돌려 카오스부터)는 영상에 없음. '
          '11-13 오후 새 정책(P11): (B) 영상 공개는 9:07 한 번에 성공해 빛의 징조로 다시 하는 장면이 없어 빛의 징조 반복을 뺌, 공개 결과 그대로(카드 랜덤 옵션) '
          '(D) 그러면 밸런스·에센셜의 과정·완성품이 같아 밸런스 하나만(옛 시뮬 167.7/104.6).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상 그대로: 훼손 공개 한 번, 결과 그대로', 'As the video: one reveal, kept as it comes')}],
 'tags': {'ail': {'gi': 24}, 'p29': {'gi': 29}, 'p1': {'gi': 1}, 'p49': {'gi': 49}, 'p4': {'gi': 4},
          'pre': {'anyOf': PRE, 'shown': ['p1', 'p4'], 'label': PRE_LABEL},
          'contP': {'gi': 104, 'slot': {'p': 1}}, 'contS': {'gi': 103, 'slot': {'s': 1}}, 'fer': {'gi': 102}},
 'require': {'all': [{'has': 'ail'}, {'count': {'tag': 'pre', 'min': 2}}, {'has': 'fer'}, {'not': {'has': 'contP'}}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'pre'}, {'tag': 'pre'}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'ail', 'fr': True}, {'tag': 'fer'}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='pf', start={'rar': 'rare', 'mods': ['ail', {'junk': 'p'}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('피해를 주는 상태 이상의 피해 가속 + 옵션 3개 레어 사파이어 구입 (아이템 레벨 82)', 'Buy a rare Sapphire: faster damaging ailments + three options (item level 82)'),
  item=[J('p'), J('p'), AILn, J('s')])
A(id='pf', kind='act', group='prep', pos=[0, 1], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (옵션 4개 중 하나)', 'Fracture (one of the four options)'),
  showText=[K('상태 이상 가속이 분열되면 성공', 'Success when faster ailments fractures')],
  edges=[{'if': {'fractured': 'ail'}, 'to': 'pc', 'res': 'ok', 'label': K('상태 이상 가속 분열', 'Faster ailments fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), J('p'), AIL, J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 1], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('상태 이상 가속이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 2], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('x'), AIL])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='s2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('x'), AIL])
A(id='s2', kind='act', group='main', pos=[0, 4.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 상태 이상의 강도 — 아래 옵션 중 먼저 뜬 것', 'Magnitude of Ailments prefix: whichever listed option lands first'), show=PRE,
  edges=[{'if': {'has': 'pre'}, 'to': 's3', 'res': 'ok'}, {'to': 's2', 'res': 'fail', 'hide': True}], item=[MAG, AIL])
A(id='s3', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Exalted_Orb', omens=['Omen_of_Sinistral_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('접두 카오스 피해 — 남은 옵션 중 먼저 뜬 것', 'Chaos damage prefix: whichever remaining option lands first'), show=PRE,
  edges=[{'if': {'count': {'tag': 'pre', 'min': 2}}, 'to': 's4', 'res': 'ok'}, {'to': 's3x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[MAG, CHA, AIL])
A(id='s3x', kind='cleanup', group='main', pos=[1, 5.4], keep=['pre'], maxJunk=0, label=ANN, goal=ANN,
  target=K('빗나간 접두 지우기', 'Remove the missed prefix'),
  edges=[{'lost': 'pre', 'to': 's2', 'label': K('좋은 접두가 지워짐 — 다시 카오스', 'Good prefix gone: Chaos again')}, {'to': 's3', 'label': K('다시 엑잘', 'Exalt again')}])
A(id='s4', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접미 잡옵 1개', 'One junk suffix'), showText=[K('접미에 랜덤 옵션 1개', 'One random suffix')],
  edges=[{'to': 's5'}], item=[MAG, CHA, AIL, J('s')])
A(id='s5', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Potent_Liquid_Contempt', ess='contP', liquid=True, anyRemove=True,
  label=K('액체', 'Liquid'), goal=K('접두어 속성 부여의 최대 개수 +1개', '+1 Prefix Modifier allowed'),
  showText=[K('접미 잡옵이 지워지면 성공, 접두가 지워지면 실패', 'The junk suffix goes: success; a prefix goes: miss')],
  edges=[{'if': {'all': [{'has': 'contP'}, {'count': {'tag': 'pre', 'min': 2}}]}, 'to': 's6', 'res': 'ok'},
         {'to': 's5x', 'res': 'fail', 'label': K('접두가 지워짐', 'A prefix removed')}],
  item=[MAG, CHA, AIL, CP])
A(id='s5x', kind='cleanup', group='main', pos=[1, 7.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기고 카오스부터', 'Keep the fracture + one option, Chaos again'), edges=[{'to': 's2', 'label': K('다시 카오스', 'Chaos again')}])
A(id='s6', kind='act', group='main', pos=[0, 8.4], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 's7'}], item=[MAG, CHA, UN('p'), AIL, CP])
A(id='s7', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], label=K('공개', 'Reveal'),
  goal=K('접두 훼손 옵션 공개 — 나오는 대로', 'Reveal the prefix desecration: keep what comes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (훼손)', 'en': 'One random option (desecrated)'}],
  edges=[{'to': 's8'}],
  item=[MAG, CHA, SPL, AIL, CP])   # 2026-11-13 P11 새 정책 B: 영상 9:07 공개 한 번에 성공(주문 피해), 빛의 징조 반복 없음
A(id='s8', kind='act', group='main', pos=[0, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Dextral_Annulment'], label=K('소멸', 'Annul'),
  goal=K('접두어 속성 부여의 최대 개수 +1개 지우기', 'Remove +1 Prefix Modifier allowed'),
  showText=[K('접미에 분열 말고 이 옵션뿐이라 확정', 'The only non-fractured suffix: certain')], edges=[{'to': 's9'}], item=[MAG, CHA, SPL, AIL])
A(id='s9', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('흉포함이 지울 접미 잡옵', 'A junk suffix for Ferocity to remove'), showText=[K('접두가 한도를 넘어 접미로 랜덤 옵션 1개', 'Prefixes are over the limit: one random suffix')],
  edges=[{'to': 's11'}], item=[MAG, CHA, SPL, AIL, J('s')])
A(id='s11', kind='act', group='main', pos=[0, 12.4], act='essence', cur='Potent_Liquid_Ferocity', ess='fer', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접두어 효과 (40—60)% 증가', '(40—60)% increased Effect of Prefixes'),
  showText=[K('접미 잡옵이 지워지고 붙음', 'The junk suffix goes')], edges=[{'to': 'ok'}], item=[MAG, CHA, SPL, AIL, FER])
A(id='ok', kind='done', group='main', pos=[0, 13.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
