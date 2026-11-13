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
HYB = L('p', '에너지 보호막 % 증가 · 생명력 최대치 1~2티어 (훼손)', 'T1–2 % energy shield · maximum life (desecrated)', 'd', ['hyb2'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'u')
RS = L('s', '랜덤 옵션', 'Random option', 'n')
RP = L('p', '랜덤 옵션', 'Random option', 'd')
RJ = L('s', '랜덤 옵션', 'Random option', 'j')   # m 'j': graph2recipe가 엑잘 자리(접미 2개)를 이 줄에서 읽음
LIGHT = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'fubgun-es-helmet-v2', 'recipe': 'fubgun-es-helmet-v2', 'cls': 'Helmets_int', 'base': 'Kamasan Tiara', 'ilvl': 78,
 'note': ('2026-11-13 G11 글 전체 다시 대조(mobalytics Fubgun 0.5.5 Ice Shot Deadeye, Crafting Guide의 Helmet - ilvl 78 - Cheap method 1~6단계, 화면 캡처 guide-helmet-cheap-1-6). '
          '글: ① 에너지 보호막 최대치 1티어 매직 베이스 구입(또는 완벽한 진화·확장) ② 상위 강화의 에센스 ③ 좌측 강령술 + 보존된 갈비뼈 ④ 공개, 에너지 보호막 % 복합(생명력·마나)이면 아무 티어나 '
          '⑤ 복합이 1티어면 완벽한 엑잘 + 상위 찬미, 아니면 상위 엑잘(+ 상위 찬미)로 접미 마무리 ⑥ 좋으면 바알 주입기(타락 — 정책상 뺌, 소켓 추가 조언도 뺌). '
          '내부 결정(글에 없음): 베이스 = 카마사의 티아라(아이템 레벨 78에서 나오는 가장 높은 지능 투구 — 장비 미리보기의 선대의 티아라는 베이스 레벨 80이라 아이템 레벨 78엔 없음), '
          '구입 매직 베이스의 접미는 잡옵 1개, 복합 목표 = 에너지 보호막 % + 생명력(확정 옵션 규칙 11-12 — 같은 글 장비 미리보기 투구의 복합 옵션, 생명력·마나 둘 다 받으면 더 쌈), 공개는 심연의 메아리 없이(글 그대로), 공개가 복합이 아니면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손(밸런스만, 정책 4장). '
          '등급(난이도 보통 → 밸런스·에센셜): 밸런스 = 복합 1~2티어까지 다시(C17 — 글은 아무 티어), 에센셜 = 공개 결과 그대로. 다음 단계 오브는 복합 1티어일 때만 완벽한 엑잘(글 5단계).'),
 'params': {'L': {'kr': '훼손 공개', 'en': 'Desecration reveal', 'values': {'1': K('빛의 징조로 다시', 'Retry with Omen of Light'), '0': K('결과 그대로', 'Keep what comes')}}},
 'strategies': [{'id': 'bal', 'params': {'L': 1}}, {'id': 'ess', 'params': {'L': 0}}],
 'versions': [{'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'L': 0}, 'tier': 'ess',
               'desc': K('훼손 공개 결과 그대로, 접미 두 개는 나오는 대로', 'Keep the reveal; the two suffixes come as they come')},
              {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'L': 1}, 'tier': 'bal',
               'desc': K('에너지 보호막 % 복합 1~2티어까지 빛의 징조로 다시', 'Retry with Light until a T1–2 hybrid % energy shield')}],
 'tags': {'esf': {'gi': 7, 'tmax': 1}, 'enh': {'gi': 34},
          'hyb2': {'gi': 9, 'tmax': 2}, 'hyb1': {'gi': 9, 'tmax': 1}},
 'require': {'all': [{'has': 'esf'}, {'has': 'enh'}, {'full': 'p'}, {'full': 's'}, {'any': [{'param': {'L': 0}}, {'has': 'hyb2'}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [{'id': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
             'lines': [{'tag': 'esf'}, {'tag': 'enh'}, {'tag': 'hyb2', 'des': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}, {'side': 's', 'random': True}]},
            {'id': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
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
  goal=K('레어로 + 접두 두번째 옵션', 'Make it rare + second prefix'),
  showText=[{'s': 'p', 'kr': T(34)[0] + ' (제작 옵션)', 'en': T(34)[1] + ' (crafted)'}], edges=[{'to': 'k2'}], item=[ESF, ENH, J('s')])
A(id='k2', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Rib', omens=['Omen_of_Sinistral_Necromancy'], label=K('훼손', 'Desecrate'),
  goal=K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'), showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'k3'}], item=[ESF, ENH, UN, J('s')])
A(id='k3', kind='act', group='main', pos=[0, 4.4], act='reveal', want='hyb2', label=K('공개', 'Reveal'),
  goal=K('접두 에너지 보호막 % 증가 · 생명력 최대치 1~2티어', 'T1–2 % energy shield · maximum life prefix'), show=['hyb2'],
  edges=[{'if': {'added': 'hyb2'}, 'to': 'k4', 'res': 'ok'}, {'if': {'param': {'L': 0}}, 'to': 'k4', 'res': 'ok', 'label': K('나오는 대로', 'Keep what comes')},
         {'to': 'k3x', 'res': 'fail'}], item=[ESF, ENH, HYB, J('s')],
  over=[{'param': {'L': 0}, 'set': {'goal': K('접두 훼손 옵션 공개 — 나오는 대로', 'Reveal the prefix desecration: keep what comes'), 'show': [],
                                    'showText': [{'s': 'p', 'kr': '랜덤 옵션', 'en': 'Random option'}], 'item': [ESF, ENH, RP, J('s')]}}])
A(id='k3x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated option'), edges=[{'to': 'k2', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='k4', kind='act', group='main', pos=[0, 5.4], act='exalt', cur='Greater_Exalted_Orb', omens=['Omen_of_Greater_Exaltation'],
  curIf=[{'if': {'has': 'hyb1'}, 'cur': 'Perfect_Exalted_Orb'}], label=K('엑잘', 'Exalt'),
  goal=K('접미 두번째·세번째 옵션 — 복합 옵션이 1티어면 완벽한 엑잘티드 오브', 'Second and third suffixes: Perfect Exalted Orb if the hybrid is T1'),
  showText=[{'s': 's', 'kr': '랜덤 옵션 2개', 'en': 'Two random options'}], edges=[{'to': 'ok'}], item=[ESF, ENH, HYB, J('s'), RJ, RJ],
  over=[{'param': {'L': 0}, 'set': {'item': [ESF, ENH, RP, J('s'), RJ, RJ]}}])
A(id='ok', kind='done', group='main', pos=[0, 6.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['k2', 'k3', 'k3x'], 'kr': '접두 세번째 옵션(훼손)', 'en': 'Third prefix (desecrated)'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
