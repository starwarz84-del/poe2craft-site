# G8 2026-11-13: Zen_M 오래된 사파이어(IKC9DquM7GM) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G8/zenm-timelost-sapphire-v2/timeline.md, frames/ (영상 0:00~21:07 화면 대조)
# 성공 회차 = 1번 주얼 Hypnotic Spark(2:00 매직 → 3:02 카오스 치명타 피해 보너스 → 4:26~4:42 우측 강령술 + 보존된 두개골 → 5:05 주문 치명타 명중 확률 → 9:20~9:30 엑잘 2번 → 9:50 우울 → 15:18 완성, 아이템 레벨 61)
# 실행: cd scripts/graphs && python3 gen_zenm_timelost_sapphire.py  → zenm-timelost-sapphire-v2.json (gen_batch9.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/zenm-timelost-sapphire-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

NP = '반경 내 주요 패시브 스킬이 '
NE = 'Notable Passive Skills in Radius also grant '
CD = L('s', NP + '치명타 피해 보너스 (5—10)% 증가도 부여', NE + '(5—10)% increased Critical Damage Bonus', 'n', ['cd'])
SCC = L('s', NP + '주문 치명타 명중 확률 (3—7)% 증가도 부여', NE + '(3—7)% increased Critical Hit Chance for Spells', 'd', ['scc'])
RAD = L('p', '반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large', 'n', ['rad'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'zenm-timelost-sapphire-v2', 'recipe': 'zenm-timelost-sapphire-v2', 'cls': 'Time-Lost_Sapphire', 'base': 'Time-Lost Sapphire', 'ilvl': 61,
 'basePrice': {'Chaos_Orb': 5},   # 18:08 메모장 '5 bases 5c'(매직 주얼 하나에 카오스 오브 5개), 2:00 자막 '이건 5 카오스, 이건 1 카오스'
 'note': ('2026-11-13 G8 영상 전체 화면 대조(근거 scratchpad review/G8/zenm-timelost-sapphire-v2/timeline.md). 주얼 5개를 같이 만들고 레시피는 1번 주얼(Hypnotic Spark) 한 줄: '
          '옵션 1개 매직 오래된 사파이어(2:00 감전의 강도, 5 카오스) → 제왕의 오브(2:28) → 소멸의 오브로 옵션 1개(2:30) → 카오스로 치명타 피해 보너스(3:02) → '
          '우측 강령술의 징조 + 보존된 두개골(4:26~4:42) → 심연의 메아리 공개(5:05 주문 치명타 명중 확률, 빗나가면 징조 없는 소멸의 오브 1/2 — 6:17·6:40, 좋은 접미가 지워지면 카오스부터 6:50) → '
          '엑잘 2번(9:20~9:30, 중형 반경이 뜨면 소멸의 오브 9:35·10:30·14:00) → 고대 위력적인 액체 우울(9:50) → 완성(15:18, 아이템 레벨 61). '
          '영상은 치명타 계열 6종(치명타 확률·치명타 피해·주문 치명타 확률·주문 치명타 피해·소환수 치명타 확률·소환수 치명타 피해) 중 아무거나 받았지만 확정 옵션 규칙(11장)대로 성공 회차의 두 옵션으로 적음.'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('공개 결과 그대로', 'Keep the reveal')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 공개가 빗나가면 징조 없는 소멸의 오브로 다시', 'Video: a plain Orb of Annulment on a missed reveal')}],
 'tags': {'cd': {'gi': 15}, 'scc': {'gi': 50}, 'rad': {'gi': 82}, 'radM': {'gi': 0}, 'radL': {'gi': 1},
          'radLo': {'anyOf': ['radM', 'radL'], 'label': K('반경 중형·대형 업그레이드', 'Radius to Medium or Large')}},
 'require': {'all': [{'has': 'cd'}, {'has': 'rad'}, {'full': 's'}, {'any': [{'has': 'scc'}, {'param': {'v': 2}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},   # 주얼: 접두 2 · 접미 2(정책 8장)
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'side': 'p', 'random': True}, {'tag': 'rad'}, {'tag': 'cd'}, {'tag': 'scc', 'des': True}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'side': 'p', 'random': True}, {'tag': 'rad'}, {'tag': 'cd'}, {'side': 's', 'random': True, 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='p1', start={'rar': 'magic', 'mods': [{'junk': 'p'}]},
  label=K('옵션 1개 매직 오래된 사파이어 구입', 'Buy a magic Time-Lost Sapphire with one option'), item=[J('p')])
A(id='p1', kind='act', group='prep', pos=[0, 1], act='regal', cur='Regal_Orb', label=K('제왕', 'Regal'),
  goal=K('레어', 'Rare'), showText=[K('랜덤 옵션 1개', 'One random option')], edges=[{'to': 'pc'}], item=[J('p'), J('x')])
A(id='pc', kind='cleanup', group='prep', pos=[0, 2], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('옵션 1개만 남기기', 'Keep only one option'), edges=[{'to': 'ms'}], item=[J('x')])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 3.4], next='c1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('x')])
A(id='c1', kind='act', group='main', pos=[0, 4.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 치명타 피해 보너스', 'Critical Damage Bonus suffix'), show=['cd'],
  edges=[{'if': {'has': 'cd'}, 'to': 'd1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail', 'hide': True}], item=[CD])
A(id='d1', kind='act', group='main', pos=[0, 5.4], act='desecrate', cur='Preserved_Cranium', omens=['Omen_of_Dextral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접미 두 번째 옵션(훼손)', 'Second suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'r1'}], item=[CD, UN('s')])
A(id='r1', kind='act', group='main', pos=[0, 6.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='scc', label=K('공개', 'Reveal'),
  goal=K('접미 주문 치명타 명중 확률', 'Spell Critical Hit Chance suffix'), show=['scc'],
  edges=[{'if': {'added': 'scc'}, 'to': 'x1', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접미 두 번째 옵션 — 공개 결과 그대로', 'Second suffix: keep the reveal'), 'show': [],
         'edges': [{'if': {'added': 'scc'}, 'to': 'x1', 'res': 'ok'}, {'to': 'x1', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')}]}}],
  item=[CD, SCC])
A(id='r1x', kind='act', group='main', pos=[1, 6.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('둘 중 하나 지우기 — 훼손 옵션이면 다시 훼손', 'One of two goes: the desecrated one means desecrate again'),
  edges=[{'if': {'has': 'cd'}, 'to': 'd1', 'res': 'ok', 'label': K('훼손 옵션이 지워짐 — 다시 훼손', 'Desecrated option gone: desecrate again')},
         {'to': 'c1', 'res': 'fail', 'label': K('치명타 피해 보너스가 지워짐 — 다시 카오스', 'Critical Damage Bonus gone: Chaos again')}])
A(id='x1', kind='act', group='main', pos=[0, 7.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 첫 번째 옵션', 'First prefix'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 꽉 차 접두로)', 'en': 'One random option (suffixes are full)'}],
  edges=[{'to': 'x2'}], item=[J('p'), CD, SCC])
A(id='x2', kind='act', group='main', pos=[0, 8.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 두 번째 옵션 — 우울이 지울 자리', 'Second prefix: the slot Melancholy takes'),
  showText=[{'s': 'p', 'kr': '랜덤 옵션 1개 (접미가 꽉 차 접두로)', 'en': 'One random option (suffixes are full)'}],
  edges=[{'if': {'has': 'radLo'}, 'to': 'xr', 'res': 'fail', 'label': K('반경 중형·대형 업그레이드', 'Radius to Medium or Large')},
         {'if': {'sideLt': {'side': 'p', 'n': 2}}, 'to': 'x2', 'hide': True}, {'to': 'm1', 'res': 'ok'}],
  item=[J('p'), J('p'), CD, SCC])
A(id='xr', kind='act', group='main', pos=[1, 8.4], act='annul', cur='Orb_of_Annulment', omens=[], label=ANN, goal=ANN,
  target=K('반경 업그레이드 옵션 지우기 (옵션 4개 중 하나)', 'Remove the radius upgrade (one of four options)'),
  edges=[{'if': {'not': {'all': [{'has': 'cd'}, {'has': 'scc'}]}}, 'to': 'xz', 'res': 'fail', 'label': K('좋은 접미가 지워짐', 'A good suffix gone')},
         {'if': {'has': 'radLo'}, 'to': 'xr', 'res': 'fail', 'hide': True},
         {'to': 'x2', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')}],
  over=[{'param': {'v': 2}, 'set': {'edges': [{'if': {'not': {'has': 'cd'}}, 'to': 'xz', 'res': 'fail', 'label': K('좋은 접미가 지워짐', 'A good suffix gone')},
         {'if': {'has': 'radLo'}, 'to': 'xr', 'res': 'fail', 'hide': True},
         {'if': {'full': 's'}, 'to': 'x2', 'res': 'ok', 'label': K('다시 엑잘', 'Exalt again')},
         {'to': 'xz', 'res': 'fail', 'hide': True}]}}])
A(id='xz', kind='cleanup', group='main', pos=[1, 7.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('옵션 1개만 남기고 카오스부터', 'Keep one option, Chaos again'), edges=[{'to': 'c1', 'label': K('다시 카오스', 'Chaos again')}])
A(id='m1', kind='act', group='main', pos=[0, 9.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large'),
  showText=[K('접두가 꽉 차 접두 하나가 지워짐', 'Prefixes are full: one prefix goes')], edges=[{'to': 'ok'}],
  item=[J('p'), RAD, CD, SCC])
A(id='ok', kind='done', group='main', pos=[0, 10.4], label=K('완성', 'Finished'))
# 에센셜: 공개 결과 그대로 → 왼쪽 아이템 칸의 두 번째 접미는 랜덤 옵션
RS = L('s', '랜덤 옵션', 'Random option', 'j')
for n in N:
    if n['id'] in ('r1', 'x1', 'x2', 'm1'):
        ess_item = [RS if x is SCC else x for x in n['item']]
        o = next((x for x in n.get('over', []) if x['param'] == {'v': 2}), None)
        if o: o['set']['item'] = ess_item
        else: n.setdefault('over', []).append({'param': {'v': 2}, 'set': {'item': ess_item}})
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
