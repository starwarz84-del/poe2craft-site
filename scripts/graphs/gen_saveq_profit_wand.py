# RECIPE-B 2026-11-14: SaVeQ 서리 기둥 수익 마법봉(youtu.be/qdyfBnzqBLo, 2026-09-09, 0.5.5) — 조사 g91(docs/craft-guides.md 5차)
# 영상 흐름 한 줄: 냉기 주문 스킬 레벨 매직 마법봉 구입 → 확장(빈 접두) → 상위 마술의 에센스로 레어(주문 피해) → 좌측 강령술 + 보존된 턱뼈 → 공개 → 상위 찬미 + 상위 엑잘로 접미 2개
# 실행: cd scripts/graphs && python3 gen_saveq_profit_wand.py  → saveq-profit-wand-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/saveq-profit-wand-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CL = L('s', '모든 냉기 주문 스킬 레벨 +4', '+4 to Level of all Cold Spell Skills', 'n', ['cold'])
XC = L('p', '피해의 (28—30)%를 추가 냉기 피해로 획득', 'Gain (28—30)% of Damage as Extra Cold Damage', 'n')
SD = L('p', '주문 피해 (75—89)% 증가 (상위 마술의 에센스)', '(75—89)% increased Spell Damage (Greater Essence of Sorcery)', 'c', ['sd'])
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
ED = L('p', '원소 피해 (74—89)% 증가', '(74—89)% increased Elemental Damage', 'd', ['ele'])
CS = L('s', '시전 속도 (29—32)% 증가', '(29—32)% increased Cast Speed', 'n')
CD = L('s', '주문 치명타 피해 보너스 (30—34)% 증가', '(30—34)% increased Critical Spell Damage Bonus', 'n')

g = {
 'id': 'saveq-profit-wand-v2', 'recipe': 'saveq-profit-wand-v2', 'cls': 'Wands', 'base': 'Twisted Wand', 'ilvl': 81,
 'note': ('2026-11-14 RECIPE-B: SaVeQ 수익용 마법봉(youtu.be/qdyfBnzqBLo, 조사 g91 — docs/craft-guides.md 5차). 영상 3:05 냉기 주문 스킬 레벨 매직 마법봉 구입(약 0.5 div) → '
          '빈 접두는 확장으로 채움(내부 결정: 자막 "상위·완벽한 엑잘"은 매직 아이템에 쓸 수 없어 상위 확장의 오브로 읽음, 마나가 안 뜨길 바람) → 상위 마술의 에센스로 레어(주문 피해 확정) → '
          '3:36 좌측 강령술의 징조 + 보존된 턱뼈로 접두 훼손 → 공개(심연의 메아리는 35~40 엑잘이라 쓰지 않음, 영상: 원소 피해 %) → 5:07 상위 찬미의 징조 + 상위 엑잘티드 오브로 남은 접미 2개. '
          '영상은 빗나감을 따로 처리하지 않고 결과 그대로 판매(하나당 1~1.5 div, 판매 2~30 div). 주문 피해가 이미 있는 베이스에 시전 속도 에센스를 쓰는 갈래는 꿀팁.'),
 'params': {},
 'strategies': [{'id': 'ess', 'params': {}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {}, 'tier': 'ess',
               'desc': K('영상 그대로: 한 번씩, 결과 그대로', 'As in the video: each step once, kept as it comes')}],
 'tags': {'cold': {'gi': 12, 'tmax': 2}, 'sd': {'gi': 44}, 'ele': {'gi': 30}},
 'require': {'all': [{'has': 'cold'}, {'has': 'sd'}, {'des': True}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'basePrice': {'Divine_Orb': 0.5},
 'finalItem': {'quality': 20, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)
A(id='b0', kind='base', group='prep', pos=[0, 0], next='a1', start={'rar': 'magic', 'mods': ['cold']},
  label=K('냉기 주문 스킬 레벨 매직 뒤틀린 마법봉 구입 (아이템 레벨 81)', 'Buy a magic Twisted Wand with cold spell skill levels (item level 81)'), item=[CL])
A(id='a1', kind='act', group='prep', pos=[0, 1], act='augment', cur='Greater_Orb_of_Augmentation', label=K('확장', 'Augment'),
  goal=K('빈 접두 채우기 — 나오는 대로 (영상: 추가 냉기 피해)', 'Fill the empty prefix: keep what comes (video: extra cold damage)'),
  showText=[K('랜덤 옵션 1개', 'One random option')], skipIf={'not': {'sideLt': {'side': 'p', 'n': 1}}}, skipTo='e1',
  skipNote=K('접두가 이미 있으면 건너뜀', 'Skipped when a prefix is already there'), edges=[{'to': 'e1'}], item=[XC, CL])
A(id='e1', kind='act', group='prep', pos=[0, 2], act='essence', cur='Greater_Essence_of_Sorcery', ess='sd', label=K('에센스', 'Essence'),
  goal=K('레어 + 접두 주문 피해', 'Rare + prefix spell damage'), showText=[{'s': 'p', 'kr': '주문 피해 (75—89)% 증가 (제작 옵션)', 'en': '(75—89)% increased Spell Damage (crafted)'}],
  edges=[{'to': 'ms'}], item=[XC, SD, CL])
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='d1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[XC, SD, CL])
A(id='d1', kind='act', group='main', pos=[0, 4.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=[XC, SD, UN, CL])
A(id='d2', kind='act', group='main', pos=[0, 5.4], act='reveal', want='ele', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 나오는 대로 (영상: 원소 피해)', 'Third prefix (desecrated): keep what comes (video: elemental damage)'), show=['ele'],
  edges=[{'to': 'x1'}], item=[XC, SD, ED, CL])
A(id='x1', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'], label=K('엑잘', 'Exalt'),
  goal=K('남은 접미 2개 — 나오는 대로 (영상: 시전 속도·주문 치명타 피해)', 'The last two suffixes: keep what comes (video: cast speed, critical spell damage)'),
  showText=[K('랜덤 옵션 2개', 'Two random options')], edges=[{'to': 'ok'}], item=[XC, SD, ED, CL, CS, CD])
A(id='ok', kind='done', group='main', pos=[0, 7.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'side': 'p', 'random': True}, {'tag': 'sd', 'ess': True}, {'side': 'p', 'random': True, 'des': True},
            {'tag': 'cold'}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
