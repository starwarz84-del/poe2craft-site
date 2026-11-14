# RECIPE-A 2026-11-14: Hax 마나 스태커 오래된 사파이어(qATcKacI83o, 2026-09-09) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: docs/craft-guides.md '5차 조사' g95(영어 자막 + 설명란 단계 요약, 완성품 3개 화면) + docs/craft-guides.json register(ok)
# 실행: cd scripts/graphs && python3 gen_hax_timelost_sapphire.py  → hax-timelost-sapphire-v2.json
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/hax-timelost-sapphire-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SCD = L('s', '반경 내 주요 패시브 스킬이 주문 치명타 피해 보너스 (5—10)% 증가도 부여', 'Notable Passive Skills in Radius also grant (5—10)% increased Critical Spell Damage Bonus', 'n', ['scd'])
SCC = L('s', '반경 내 주요 패시브 스킬이 주문 치명타 명중 확률 (3—7)% 증가도 부여', 'Notable Passive Skills in Radius also grant (3—7)% increased Critical Hit Chance for Spells', 'n', ['scc'])
RAD = L('p', '반경이 매우 넓은 반경으로 업그레이드 (고대 위력적인 액체 우울)', 'Upgrades Radius to Very Large (Ancient Potent Liquid Melancholy)', 'n', ['rad'])
MANA = L('p', '반경 내 주요 패시브 스킬이 최대 마나 1% 증가도 부여 (훼손)', 'Notable Passive Skills in Radius also grant 1% increased maximum Mana (desecrated)', 'd', ['mana'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = L('p', '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
LIGHT = K('소멸의 오브 + 빛의 징조', 'Orb of Annulment + Omen of Light')

g = {
 'id': 'hax-timelost-sapphire-v2', 'recipe': 'hax-timelost-sapphire-v2', 'cls': 'Time-Lost_Sapphire', 'base': 'Time-Lost Sapphire', 'ilvl': 82,
 'basePrice': {'Divine_Orb': 11},   # 1:32 자막 '10~12 div'(접미 주문 치명타 피해 보너스 + 주문 치명타 명중 확률 오래된 사파이어) — 가운데 11 div
 'note': ('2026-11-14 RECIPE-A: Hax 마나 스태커 오래된 사파이어(2026-09-09, 0.5.5) 성공 회차 한 줄(근거 docs/craft-guides.md 5차 g95, 영어 자막 + 설명란 요약 + 완성품 화면). '
          '접미 주문 치명타 피해 보너스 + 주문 치명타 명중 확률 오래된 사파이어 구입(1:32, 10~12 div, 타락·제작·훼손·분열 없음) → 고대 위력적인 액체 우울로 매우 넓은 반경(2:02, 꽉 찬 아이템이면 접두 하나를 지우고 붙음) → '
          '좌측 강령술의 징조 + 보존된 두개골(2:32, 접두가 꽉 차서 둘 중 하나가 지워짐 — 우울 옵션이 지워지면 우울을 다시, 좌측 소멸의 징조보다 쌈) → '
          '심연의 메아리의 징조로 공개(3:35) → 최대 마나 1%가 아니면 빛의 징조 + 소멸의 오브로 훼손 옵션만 지우고 보존된 두개골(빈자리가 접두뿐이라 강령술 필요 없음) → 5:07 여덟 번째에 성공. '
          '내부 결정: 산 베이스의 접두 2개는 잡옵(자막: 꽉 차 있으면 우울이 접두만 지움), 우울을 다시 쓸 때 미공개 훼손 옵션이 지워지면 다시 두개골(자막에 없음, 같은 핑퐁의 반대 경우). '
          '등급: 난이도 2 → 밸런스(영상, 최대 마나가 나올 때까지 빛의 징조) · 에센셜(공개 한 번, 결과 그대로).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('빛의 징조로 다시', 'Retry with Light'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('공개 한 번, 결과 그대로', 'One reveal, kept as it comes')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 최대 마나가 나올 때까지 빛의 징조로 다시', 'Video: retry with Omen of Light until maximum mana')}],
 'tags': {'scd': {'gi': 16}, 'scc': {'gi': 50}, 'rad': {'gi': 82}, 'mana': {'gi': 69}},
 'require': {'all': [{'has': 'scd'}, {'has': 'scc'}, {'has': 'rad'}, {'unrev': False}, {'full': 'p'},
                     {'any': [{'has': 'mana'}, {'param': {'v': 2}}]}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},   # 주얼: 접두 2 · 접미 2(정책 8장)
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'rad'}, {'tag': 'mana', 'des': True}, {'tag': 'scd'}, {'tag': 'scc'}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'tag': 'rad'}, {'side': 'p', 'random': True, 'des': True}, {'tag': 'scd'}, {'tag': 'scc'}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)
# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'rare', 'mods': [{'junk': 'p'}, {'junk': 'p'}, {'tag': 'scd'}, {'tag': 'scc'}]},
  label=K('접미 주문 치명타 피해 보너스 + 주문 치명타 명중 확률 레어 오래된 사파이어 구입 (아이템 레벨 82)', 'Buy a rare Time-Lost Sapphire with spell crit damage + spell crit chance suffixes (item level 82)'),
  item=[J('p'), J('p'), SCD, SCC])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='m2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), J('p'), SCD, SCC])
A(id='m2', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('고대 위력적인 액체 우울 (접두 하나가 지워짐)', 'Ancient Potent Liquid Melancholy (one prefix goes)'),
  showText=[{'s': 'p', 'kr': '반경이 매우 넓은 반경으로 업그레이드', 'en': 'Upgrades Radius to Very Large'}],
  edges=[{'if': {'unrev': True}, 'to': 'm4', 'res': 'ok', 'label': K('잡옵이 지워짐 — 공개', 'The junk went: reveal')},
         {'to': 'm3', 'res': 'ok'}],
  item=[J('p'), RAD, SCD, SCC])
A(id='m3', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Cranium', omens=['Omen_of_Sinistral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접두 훼손 (접두 둘 중 하나가 지워짐)', 'Prefix desecration (one of the two prefixes goes)'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'if': {'has': 'rad'}, 'to': 'm4', 'res': 'ok', 'label': K('잡옵이 지워짐', 'The junk went')},
         {'to': 'm2', 'res': 'fail', 'label': K('우울 옵션이 지워짐 — 우울 다시', 'The Melancholy line went: Melancholy again')}],
  item=[UN, RAD, SCD, SCC])
A(id='m4', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='mana',
  label=K('공개', 'Reveal'), goal=K('접두 최대 마나 % 증가', 'Maximum mana % prefix'), show=['mana'],
  goalBy={'ess': K('접두 훼손 옵션 공개 — 나오는 대로 (영상: 최대 마나 % 증가)', 'Reveal the prefix desecration: keep what comes (video: maximum mana %)')},
  edges=[{'if': {'added': 'mana'}, 'to': 'ok', 'res': 'ok'},
         {'to': 'm4x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  over=[{'param': {'v': 2}, 'set': {'edges': [{'to': 'ok', 'res': 'ok'}]}}],
  item=[MANA, RAD, SCD, SCC])
A(id='m4x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=LIGHT, goal=LIGHT,
  target=K('훼손 옵션 제거', 'Remove the desecrated modifier'), edges=[{'to': 'm5'}])
A(id='m5', kind='act', group='main', pos=[1, 3.4], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('접두 훼손 — 빈자리가 접두뿐', 'Prefix desecration: the only free slot'),
  showText=[{'s': 'p', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'm4', 'label': K('다시 공개', 'Reveal again')}])
A(id='ok', kind='done', group='main', pos=[0, 5.6], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['m2', 'm3'], 'kr': '우울·두개골', 'en': 'Melancholy and Cranium'},
              {'id': 'L2', 'nodes': ['m4', 'm4x', 'm5'], 'kr': '훼손 공개', 'en': 'Reveal'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
