# RECIPE-B 2026-11-14: Fubgun 화염파 오일 수류탄 지팡이 방법1(youtu.be/WInrHPfAMd4, 2026-09-07, 0.5.5) — 조사 g100(docs/craft-guides.md 5차)
# 영상 흐름 한 줄(3:14~5:35): 주문 피해 + 추가 화염 피해 레어 구입 → 군주의 징조 + 보존된 턱뼈(빈 접두) → 공개(울라만 상태 이상 강도) → 완벽한 마술의 에센스(접미 꽉 참) = 주문 스킬 +5
# 방법2(화염 +7 베이스 → 상위 에센스 → 상위 찬미)는 첫 에센스 이름이 불확실해 넣지 않음(꿀팁 후보)
# 실행: cd scripts/graphs && python3 gen_fubgun_ulaman_staff.py  → fubgun-ulaman-staff-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-ulaman-staff-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SD = L('p', '주문 피해 증가', 'Increased Spell Damage', 'n', ['sd'])
XF = L('p', '피해의 일부를 추가 화염 피해로 획득', 'Gain a part of Damage as Extra Fire Damage', 'n', ['xf'])
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
MG = L('p', '피해를 주는 상태 이상의 강도 (40—64)% 증가', '(40—64)% increased Magnitude of Damaging Ailments you inflict', 'd', ['mag'])
P5 = L('s', '모든 주문 스킬 레벨 +5 (완벽한 마술의 에센스)', '+5 to Level of all Spell Skills (Perfect Essence of Sorcery)', 'c', ['sp5'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')

g = {
 'id': 'fubgun-ulaman-staff-v2', 'recipe': 'fubgun-ulaman-staff-v2', 'cls': 'Staves', 'base': 'Ashen Staff', 'ilvl': 82,
 'note': ('2026-11-14 RECIPE-B: Fubgun 화염파 오일 수류탄 지팡이 방법1(youtu.be/WInrHPfAMd4 3:14~5:35, 조사 g100 — docs/craft-guides.md 5차). '
          '주문 피해 + 피해의 일부를 추가 화염 피해로 레어 지팡이 구입(1~2 div) → 접두가 하나만 비어 있어 강령술의 징조 없이 군주의 징조 + 보존된 턱뼈 → '
          '공개(지팡이 접두 울라만 옵션은 2개뿐이라 늘 상태 이상 강도가 보임, 단일 티어라 심연의 메아리 필요 없음) → 4:35 접미 3개가 꽉 찬 상태에서 완벽한 마술의 에센스 = 모든 주문 스킬 +5(접미 하나가 지워짐). '
          '내부 결정: 영상은 "접미 개수는 상관없이" 사라고 하지만 접미가 2개면 에센스가 접두를 지울 수 있다고 설명하므로 시작 베이스를 접미 3개 레어로 정함. '
          '주문 피해·추가 화염 피해 티어는 영상에서 정하지 않아 티어 제한 없이 둠. 5:35 아스트리드의 창의성 + 초월의 합금(시전 속도)은 선택 단계(비용 미포함). '
          '7:40 방법2(화염 주문 +7 베이스 → 상위 에센스 → 상위 찬미)는 첫 에센스 이름을 확인하지 못해 넣지 않음. 신성한 오브·룬은 정책 9장대로 뺌.'),
 'params': {},
 'strategies': [{'id': 'ess', 'params': {}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {}, 'tier': 'ess',
               'desc': K('영상 방법1: 한 번씩, 반복 없음', 'Video method 1: each step once, no loop')}],
 'tags': {'sd': {'gi': 3}, 'xf': {'gi': 32}, 'mag': {'gi': 48}, 'sp5': {'gi': 55}},
 'require': {'all': [{'has': 'sd'}, {'has': 'xf'}, {'has': 'mag'}, {'has': 'sp5'}, {'unrev': False}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'basePrice': {'Divine_Orb': 1.5},
 'finalItem': {'quality': 20, 'sockets': 2},
}

N = []
A = lambda **kw: N.append(kw)
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'rare', 'mods': ['sd', 'xf', {'junk': 's'}, {'junk': 's'}, {'junk': 's'}]},
  label=K('주문 피해 + 추가 화염 피해 레어 잿빛 지팡이 구입 (아이템 레벨 82, 접미 3개)', 'Buy a rare Ashen Staff with spell damage + extra fire damage (item level 82, three suffixes)'),
  item=[SD, XF, J('s'), J('s'), J('s')])
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='d1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[SD, XF, J('s'), J('s'), J('s')])
A(id='d1', kind='act', group='main', pos=[0, 2.4], act='desecrate', cur='Preserved_Jawbone', omens=['Omen_of_the_Sovereign'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션 — 울라만 훼손', 'Third prefix: Ulaman desecration'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'd2'}], item=[SD, XF, UN, J('s'), J('s'), J('s')])
A(id='d2', kind='act', group='main', pos=[0, 3.4], act='reveal', want='mag', label=K('공개', 'Reveal'),
  goal=K('접두 세 번째 옵션(훼손) — 피해를 주는 상태 이상의 강도', 'Third prefix (desecrated): magnitude of damaging ailments'), show=['mag'],
  edges=[{'if': {'added': 'mag'}, 'to': 'e1', 'res': 'ok'}, {'to': 'e1', 'res': 'fail', 'hide': True}], item=[SD, XF, MG, J('s'), J('s'), J('s')])
A(id='e1', kind='act', group='main', pos=[0, 4.4], act='essence', cur='Perfect_Essence_of_Sorcery', ess='sp5', label=K('에센스', 'Essence'),
  goal=K('접미 모든 주문 스킬 레벨 +5 — 꽉 찬 접미 하나가 지워짐', 'Suffix +5 to all spell skills: one of the full suffixes goes'),
  showText=[{'s': 's', 'kr': '모든 주문 스킬 레벨 +5 (제작 옵션)', 'en': '+5 to Level of all Spell Skills (crafted)'}],
  edges=[{'to': 'ok'}], item=[SD, XF, MG, P5, J('s'), J('s')])
A(id='ok', kind='done', group='main', pos=[0, 5.4], label=K('완성', 'Finished'))
A(id='hs', kind='side', group='main', pos=[1, 5.4], attach=['ok', 'ok'], cur='Transcendent_Alloy',
  goal=K('아스트리드의 창의성 + 초월의 합금으로 시전 속도, 선택·비용 미포함', "Astrid's Creativity + Transcendent Alloy for cast speed, optional, not costed"),
  label=K('합금', 'Alloy'))
g['nodes'] = N
g['loops'] = []
g['finals'] = [
 {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
  'lines': [{'tag': 'sd'}, {'tag': 'xf'}, {'tag': 'mag', 'des': True},
            {'tag': 'sp5', 'ess': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
]
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
