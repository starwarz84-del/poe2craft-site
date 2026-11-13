# G11 2026-11-13: Fubgun 가성비 에너지 보호막 투구(mobalytics 0.5.5 Ice Shot Deadeye 빌드 글의 Crafting Guide 'Helmet - ilvl 78 - Cheap method' 1~6단계) 플로우차트 생성기
# 근거: scratchpad review/G11/fubgun-es-helmet-v2/timeline.md, frames/guide-helmet-cheap-1-6.jpg (글 전체 다시 읽음)
# 실행: cd scripts/graphs && python3 gen_fubgun_es_helmet.py  → fubgun-es-helmet-v2.json (gen_batch26.py 끝에서 자동 호출)
# 상자 id는 옛 단계 레시피(e1~e6)와 겹치지 않게 k로 시작(옛 꿀팁·시각이 이어붙지 않게).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/fubgun-es-helmet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}
C = json.load(open(f'{H}/../../site/data/c/Helmets_int.json'))

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

def T(gi, tier=1):   # 클래스 파일의 게임 문구(티어 번호 1부터)
    t = C['groups'][gi]['t'][tier - 1]
    return t[4].replace('\n', ' · '), t[5].replace('\n', ' · ')

ESF = L('p', *T(7), 'n', ['esf'])
ENH = L('p', T(34)[0] + ' (제작 옵션)', T(34)[1] + ' (crafted)', 'c', ['enh'])
HYB = L('p', '에너지 보호막 % 증가 · 생명력 최대치 (훼손)', '% energy shield · maximum life (desecrated)', 'd', ['hybL'])   # 상자·왼쪽 칸 = 글 장비 미리보기의 복합(성공 회차 옵션, 11-13 오후 새 정책 A)
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
RS = L('s', '랜덤 옵션', 'Random option', 'n')
RP = L('p', '랜덤 옵션', 'Random option', 'd')
RJ = L('s', '랜덤 옵션', 'Random option', 'j')   # m 'j': graph2recipe가 엑잘 자리(접미 2개)를 이 줄에서 읽음

g = {
 'id': 'fubgun-es-helmet-v2', 'recipe': 'fubgun-es-helmet-v2', 'cls': 'Helmets_int', 'base': 'Kamasan Tiara', 'ilvl': 78,
 'note': ('2026-11-13 G11 글 전체 다시 대조(mobalytics Fubgun 0.5.5 Ice Shot Deadeye, Crafting Guide의 Helmet - ilvl 78 - Cheap method 1~6단계, 화면 캡처 guide-helmet-cheap-1-6). '
          '글: ① 에너지 보호막 최대치 1티어 매직 베이스 구입(또는 완벽한 진화·확장) ② 상위 강화의 에센스 ③ 좌측 강령술 + 보존된 갈비뼈 ④ 공개, 에너지 보호막 % 복합(생명력·마나)이면 아무 티어나 '
          '⑤ 복합이 1티어면 완벽한 엑잘 + 상위 찬미, 아니면 상위 엑잘(+ 상위 찬미)로 접미 마무리 ⑥ 좋으면 바알 주입기(타락 — 정책상 뺌, 소켓 추가 조언도 뺌). '
          '내부 결정(글에 없음): 베이스 = 카마사의 티아라(아이템 레벨 78에서 나오는 가장 높은 지능 투구 — 장비 미리보기의 선대의 티아라는 베이스 레벨 80이라 아이템 레벨 78엔 없음), '
          '구입 매직 베이스의 접미는 잡옵 1개, 복합 목표 = 에너지 보호막 % + 생명력(확정 옵션 규칙 11-12 — 같은 글 장비 미리보기 투구의 복합 옵션, 생명력·마나 둘 다 받으면 더 쌈), 공개는 심연의 메아리 없이(글 그대로). '
          '11-13 오후 새 정책: (A) 공개 목표 = 에너지 보호막 % 복합(생명력·마나) 아무 티어 중 하나 — 공개 선택지 3개에 있으면 고름, 상자·카드는 글 장비 미리보기의 생명력 복합 (B) 글에 빗나감 처리가 없어 빛의 징조 반복 없음, 공개 결과 그대로 '
          '(D) 그러면 밸런스·에센셜 비용이 같아(10% 이내) 밸런스 하나만. 다음 단계 오브는 복합 1티어일 때만 완벽한 엑잘(글 5단계).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('글', 'Guide')}}},
 'strategies': [{'id': 'ess', 'params': {'v': 1}}],   # D4 2026-11-13: 난이도 표 0(입문) → 에센셜만(C11·15:42 ④), 내용은 그대로 이름만
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 1}, 'tier': 'ess',
               'desc': K('글: 공개 선택지에 에너지 보호막 % 복합이 있으면 고르고, 없으면 결과 그대로', 'Guide: take a hybrid % energy shield if the reveal offers one, otherwise keep what comes')}],
 'tags': {'esf': {'gi': 7, 'tmax': 1}, 'enh': {'gi': 34},
          'hybL': {'gi': 9}, 'hybM': {'gi': 10},
          'hyb': {'anyOf': ['hybL', 'hybM'], 'shown': 'hybL', 'label': K('에너지 보호막 % 복합(생명력·마나)', 'Hybrid % energy shield (life or mana)')},
          'hybL1': {'gi': 9, 'tmax': 1}, 'hybM1': {'gi': 10, 'tmax': 1}, 'hyb1': {'anyOf': ['hybL1', 'hybM1']}},
 'require': {'all': [{'has': 'esf'}, {'has': 'enh'}, {'full': 'p'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [{'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
             'lines': [{'tag': 'esf'}, {'tag': 'enh'}, {'side': 'p', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]}],
 'finalItem': {'quality': 0, 'sockets': 1},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 (글 1단계) ----------------
A(id='k0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'magic', 'mods': [{'tag': 'esf'}, {'junk': 's'}]},
  label=K('에너지 보호막 최대치 1티어 매직 카마사의 티아라 구입 (아이템 레벨 78)', 'Buy a magic Kamasan Tiara with T1 flat energy shield (item level 78)'), item=[ESF, J('s')])
# ---------------- 옵션 추가 작업 (글 2~5단계) ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='k1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[ESF, J('s')])
A(id='k1', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Greater_Essence_of_Enhancement', ess='enh', label=K('에센스', 'Essence'),
  goal=K('레어로 + 접두 두 번째 옵션', 'Make it rare + second prefix'),
  showText=[{'s': 'p', 'kr': T(34)[0] + ' (제작 옵션)', 'en': T(34)[1] + ' (crafted)'}], edges=[{'to': 'k2'}], item=[ESF, ENH, J('s')])
A(id='k2', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세 번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'k3'}], item=[ESF, ENH, UN, J('s')])
A(id='k3', kind='act', group='main', pos=[0, 4.4], act='reveal', want='hyb', label=K('공개', 'Reveal'),
  goal=K('접두 에너지 보호막 % 복합 — 선택지에 없으면 결과 그대로', 'Hybrid % energy shield prefix; keep what comes if it is not offered'), show=['hyb'],
  edges=[{'to': 'k4'}], item=[ESF, ENH, HYB, J('s')])
A(id='k4', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  curIf=[{'if': {'has': 'hyb1'}, 'cur': 'Perfect_Exalted_Orb'}], label=K('엑잘', 'Exalt'),
  goal=K('접미 두 번째·세 번째 옵션 — 복합 옵션이 1티어면 완벽한 엑잘티드 오브', 'Second and third suffixes: Perfect Exalted Orb if the hybrid is T1'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'ok'}], item=[ESF, ENH, HYB, J('s'), RJ, RJ])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = []

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
