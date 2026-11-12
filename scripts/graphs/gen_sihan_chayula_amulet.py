# G2 2026-11-13: 시한 차율라 목걸이(2vyq26ZFgOk, 6:18) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G2/sihan-chayula-amulet-v2/timeline.md, frames/ (영상 0:00~6:18 화면 대조)
# 실행: cd scripts/graphs && python3 gen_sihan_chayula_amulet.py  → sihan-chayula-amulet-v2.json (gen_batch22.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/sihan-chayula-amulet-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

# 아이템 칸 — 영상 성공 회차(3:02 매물 → 4:04 완성)에 실제로 나온 옵션
ES = L('p', '에너지 보호막 최대치 +(71—79)', '+(71—79) to maximum Energy Shield', 'n', ['es'])
SP = L('p', '정신력 +(47—50)', '+(47—50) to Spirit', 'n', ['spirit'])
DX = L('s', '민첩 +(31—33) (분열)', '+(31—33) to Dexterity (fractured)', 'f', ['dex'])
STP = L('s', '힘 (7—10)% 증가 (완벽한 무한의 에센스)', '(7—10)% increased Strength (Perfect Essence of the Infinite)', 'c', ['strp'])
SK = L('s', '모든 스킬 레벨 +1 (훼손)', '+1 to Level of all Skills (desecrated)', 'd', ['skill'])
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')

g = {
 'id': 'sihan-chayula-amulet-v2', 'recipe': 'sihan-chayula-amulet-v2', 'cls': 'Amulets', 'base': 'Absent Amulet', 'ilvl': 80,
 'basePrice': {'Divine_Orb': 15},   # 3:02 거래소 '~b/o 15 divine'
 'note': ('2026-11-13 G2 영상 전체 화면 대조(0:00~6:18). 성공 회차 한 줄: 정신력 분열에 실패한 부재 목걸이 매물 구입'
          '(혼란 유발의 갑충석, 아이템 레벨 80, 에너지 보호막 최대치 +79 2티어·정신력 +50 1티어 / 민첩 +33 분열·미공개 훼손 접미, 15 div, 2:00~3:02 거래소) → '
          '완벽한 무한의 에센스(접미가 꽉 차 미공개 훼손이 지워지고 힘 9% 증가, 3:22~3:29) → '
          '우측 강령술 + 군주의 징조 + 보존된 빗장뼈(힘 %가 지워지고 울라만 훼손, 3:33~3:44) → 공개(모든 스킬 레벨 +1, 3:49 — 다시 굴림 버튼이 보여 심연의 메아리 사용으로 봄) → 완성(4:04). '
          '빗나가면(4:35~5:14 시연) 완벽한 무한의 에센스로 훼손 옵션을 지우고(분열 민첩 말고 지울 접미가 그것뿐) 다시 — 빛의 징조 없음. '
          '등급(정책 10장 C17-3·4): 빛의 징조 없이 다시 할 수 있는 반복이라 에센셜도 반복 → 밸런스와 같아져 밸런스만. 정신력·에너지 보호막은 매물에 있는 옵션(모든 등급 1티어, C15).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
  {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
   'desc': K('영상: 모든 스킬 레벨 +1이 나올 때까지 에센스·훼손 반복', 'Video: essence and desecration until +1 to all skills shows')}],
 'tags': {'spirit': {'gi': 28, 'tmax': 1}, 'es': {'gi': 13, 'tmax': 2}, 'dex': {'gi': 1, 'tmax': 1}, 'strp': {'gi': 75}, 'skill': {'gi': 56}},
 'require': {'all': [{'has': 'spirit'}, {'has': 'es'}, {'has': 'dex'}, {'has': 'skill'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'k0',
 'finals': [
  {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
   'lines': [{'tag': 'es'}, {'tag': 'spirit'}, {'tag': 'dex', 'fr': True}, {'tag': 'skill', 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = N.append
I0 = [ES, SP, DX, UN('s')]
A(dict(id='k0', kind='base', group='prep', pos=[0, 0], next='km',
  start={'rar': 'rare', 'mods': [{'tag': 'es'}, {'tag': 'spirit'}, {'tag': 'dex', 'fr': True}, {'unrev': 's'}]},
  label=K('부재 목걸이 매물 구입 (아이템 레벨 80, 에너지 보호막·정신력 / 민첩 분열 + 미공개 훼손 접미)',
          'Buy an Absent Amulet listing (item level 80: energy shield and Spirit / fractured Dexterity + an unrevealed desecrated suffix)'),
  item=I0))
A(dict(id='km', kind='mark', group='main', pos=[0, 1.4], next='a2', label=K('아이템 제작 시작', 'Item crafting starts'), item=I0))
A(dict(id='a2', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Perfect_Essence_of_the_Infinite', ess='strp', label=K('에센스', 'Essence'),
  goal=K('접미 두번째 옵션 — 훼손 옵션을 제작 옵션으로', 'Second suffix: the desecrated modifier becomes a crafted one'),
  showText=[{'s': 's', 'kr': '힘 (7—10)% 증가 (제작 옵션)', 'en': '(7—10)% increased Strength (crafted)'}],
  edges=[{'to': 'a3'}], item=[ES, SP, DX, STP]))
A(dict(id='a3', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Collarbone',
  omens=['Omen_of_Dextral_Necromancy', 'Omen_of_the_Sovereign'], label=K('훼손', 'Desecrate'),
  goal=K('접미 두번째 옵션 — 울라만 훼손', 'Second suffix: Ulaman desecration'),
  showText=[{'s': 's', 'kr': '울라만 훼손 옵션 (미공개)', 'en': 'Ulaman desecration (unrevealed)'}],
  edges=[{'to': 'a4'}], item=[ES, SP, DX, UN('s')]))
A(dict(id='a4', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='skill', label=K('공개', 'Reveal'),
  goal=K('접미 두번째 옵션(훼손) — 모든 스킬 레벨 +1', 'Second suffix (desecrated): +1 to Level of all Skills'), show=['skill'],
  edges=[{'if': {'added': 'skill'}, 'to': 'ok', 'res': 'ok'},
         {'to': 'a2', 'res': 'fail', 'label': K('빗나감 — 다시 에센스', 'Miss: essence again')}],
  item=[ES, SP, DX, SK]))
A(dict(id='ok', kind='done', group='main', pos=[0, 5.4], label=K('완성', 'Finished')))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['a2', 'a3', 'a4'], 'kr': '울라만 공개', 'en': 'Ulaman reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
