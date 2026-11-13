# G4 2026-11-13: Vodnarg 오래된 에메랄드(3tFs16SXkD8) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/G4/vodnarg-timelost-emerald-v2/timeline.md, frames/ (영상 0:00~16:40 화면 대조)
# 실행: cd scripts/graphs && python3 gen_vodnarg_timelost_emerald.py  → vodnarg-timelost-emerald-v2.json (gen_batch10.py 끝에서도 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/vodnarg-timelost-emerald-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

N_ = '반경 내 주요 패시브 스킬이 '
S_ = '반경 내 소형 패시브 스킬이 '
NE = 'Notable Passive Skills in Radius also grant '
SE = 'Small Passive Skills in Radius also grant '
AS = L('s', N_ + '공격 속도 (1—2)% 증가도 부여', NE + '(1—2)% increased Attack Speed', 'n', ['s11'])
CDS = L('s', N_ + '창 사용 시 치명타 피해 보너스 (5—10)% 증가도 부여', NE + '(5—10)% increased Critical Damage Bonus with Spears', 'n', ['s65'])
CC = L('s', N_ + '공격 치명타 명중 확률 (3—7)% 증가도 부여', NE + '(3—7)% increased Critical Hit Chance for Attacks', 'd', ['s8'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
PD = L('p', S_ + '투사체 피해 (1—2)% 증가도 부여', SE + '(1—2)% increased Projectile Damage', 'n', ['p54'])
RAD = L('p', '반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large', 'c', ['rad'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

REV = ['s8', 's64', 's9']   # 5:40 자막: 공격 속도·치명타 피해·치명타 확률 계열 중 하나 — 화면에서 고른 것 = 공격 치명타 확률(6:02, 7:45), 창 공격 속도(9:28)
REV_LABEL = K('공격 치명타 확률·창 공격 속도·공격 치명타 피해 보너스', 'Critical Hit Chance for Attacks, Attack Speed with Spears or Critical Damage Bonus for Attack Damage')
PRE = ['p54', 'p66']        # 12:26 투사체 피해(1·2번 주얼), 13:35 창 사용 시 피해(3번 주얼) — 영상이 받아들인 접두
PRE_LABEL = K('투사체 피해·창 사용 시 피해', 'Projectile Damage or Damage with Spears')

g = {
 'id': 'vodnarg-timelost-emerald-v2', 'recipe': 'vodnarg-timelost-emerald-v2', 'cls': 'Time-Lost_Emerald', 'base': 'Time-Lost Emerald', 'ilvl': 80,
 'basePrice': {'Divine_Orb': 3},   # 4:50 자막 '주얼 베이스는 하나에 약 3 div' (거래 화면은 영상에 없음)
 'note': ('2026-11-13 G4 영상 전체 화면 대조(근거 scratchpad review/G4/vodnarg-timelost-emerald-v2/timeline.md). 주얼 3개를 같이 만들고 셋 다 완성 — 레시피는 1번 주얼(Blight Desire) 한 줄: '
          '공격 속도 + 창 치명타 피해 보너스 접미 2개, 접두 잡옵 2개(실명 효과·소형 회피) 오래된 에메랄드 구입(2:55, 약 3 div) → 고대 위력적인 액체 경멸 50:50(4:28 실명 효과가 지워지고 접미어 +1개, 실패면 버리고 새 주얼) → '
          '우측 강령술의 징조 + 보존된 두개골(5:10~5:14) → 심연의 메아리 공개(6:02 공격 치명타 확률, 2·3번 주얼은 빛의 징조로 다시 6:35~9:28) → 좌측 말소의 징조 + 카오스(10:33 접미어 +1개가 지워지고 정확도 접두, 50:50 빗나가면 다시) → '
          '카오스 반복으로 접두만 바뀜(11:00~12:20, 투사체 피해) → 고대 위력적인 액체 우울(12:58 정확도가 지워지고 매우 넓은 반경, 50:50 빗나가면 카오스부터). 신성한 오브(14:10 말로만)는 뺌. '
          '밸런스 = 영상, 에센셜 = 공개 결과 그대로·접두 카오스 없이 우울 한 번(C17-3).'),
 'params': {'v': {'kr': '진행', 'en': 'Route', 'values': {'1': K('영상', 'Video'), '2': K('결과 그대로', 'As it comes')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}, {'id': 'ess', 'params': {'v': 2}}],
 'versions': [
   {'id': 'ess', 'kr': '에센셜', 'en': 'Essential', 'params': {'v': 2}, 'tier': 'ess',
    'desc': K('공개 결과 그대로, 우울 한 번', 'Keep the reveal, one Melancholy')},
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 빛의 징조로 다시 공개, 좋은 접두까지 카오스', 'Video: Omen of Light on a missed reveal, Chaos until a good prefix')}],
 'tags': {'s11': {'gi': 11}, 's65': {'gi': 65}, 's8': {'gi': 8}, 's64': {'gi': 64}, 's9': {'gi': 9},
          'p54': {'gi': 54}, 'p66': {'gi': 66}, 'rad': {'gi': 99},
          'contS': {'gi': 101, 'slot': {'s': 1}}, 'contP': {'gi': 102, 'slot': {'p': 1}},
          'rev': {'anyOf': REV, 'shown': 's8', 'label': REV_LABEL},
          'pre': {'anyOf': PRE, 'shown': 'p54', 'label': PRE_LABEL}},
 'require': {'all': [{'has': 's11'}, {'has': 's65'}, {'has': 'rad'}, {'full': 's'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'cap': {'p': 2, 's': 2},
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'pre'}, {'tag': 'rad'}, {'tag': 's11'}, {'tag': 's65'}, {'tag': 'rev', 'des': True}]},
   {'id': 'ess', 'tier': 'ess', 'kr': '에센셜 옵션', 'en': 'Essential',
    'lines': [{'side': 'p', 'random': True}, {'tag': 'rad'}, {'tag': 's11'}, {'tag': 's65'}, {'side': 's', 'random': True, 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='ms', start={'rar': 'rare', 'mods': ['s11', 's65', {'junk': 'p'}, {'junk': 'p'}]},
  label=K('공격 속도 + 창 치명타 피해 보너스 접미, 접두 2개 레어 오래된 에메랄드 구입', 'Buy a rare Time-Lost Emerald: attack speed + spear crit damage suffixes, two prefixes'),
  item=[J('p'), J('p'), AS, CDS])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 1.4], next='l1', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), J('p'), AS, CDS])
A(id='l1', kind='act', group='main', pos=[0, 2.4], act='essence', cur='Ancient_Potent_Liquid_Contempt', ess='contS', alt='contP', liquid=True,
  label=K('액체', 'Liquid'), goal=K('접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed'),
  showText=[K('접두 잡옵이 지워지면 성공, 접미가 지워지면 실패', 'A junk prefix goes: success; a suffix goes: miss')],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 's11'}, {'has': 's65'}]}, 'to': 'd1', 'res': 'ok'},
         {'to': 'l1x', 'res': 'fail', 'label': K('접미가 지워짐', 'A suffix removed')}],
  item=[J('p'), CONT, AS, CDS])
A(id='l1x', kind='exit', group='main', pos=[1, 2.4], simTo='b0', variant='fail', label=K('새 주얼', 'New jewel'),
  note=K('접미어 +1개가 붙지 않으면 그 주얼은 버리고 새 주얼로', 'No +1 suffix: set the jewel aside and buy a new one'))
A(id='d1', kind='act', group='main', pos=[0, 3.4], act='desecrate', cur='Preserved_Cranium', omens=['Omen_of_Dextral_Necromancy'],
  label=K('훼손', 'Desecrate'), goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'),
  showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}], edges=[{'to': 'r1'}],
  item=[J('p'), CONT, AS, CDS, UN('s')])
A(id='r1', kind='act', group='main', pos=[0, 4.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev', label=K('공개', 'Reveal'),
  goal=K('접미 공격 치명타 확률', 'Attack crit chance suffix'), show=['rev'],   # R3-8: 상자는 성공 회차 옵션(shown), 다른 유효 옵션은 자동 꿀팁(정책 A)
  edges=[{'if': {'added': 'rev'}, 'to': 'x1', 'res': 'ok'}, {'to': 'r1x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  over=[{'param': {'v': 2}, 'set': {'goal': K('접미 세 번째 옵션 — 공개 결과 그대로', 'Third suffix: keep the reveal'),
         'edges': [{'if': {'added': 'rev'}, 'to': 'x1', 'res': 'ok'}, {'to': 'x1', 'res': 'fail', 'label': K('빗나감 — 그대로', 'Miss: keep it')}]}}],
  item=[J('p'), CONT, AS, CDS, CC])
A(id='r1x', kind='act', group='main', pos=[1, 4.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'd1', 'label': K('다시 훼손', 'Desecrate again')}])
A(id='x1', kind='act', group='main', pos=[0, 5.4], act='chaos', cur='Chaos_Orb', omens=['Omen_of_Sinistral_Erasure'], label=K('카오스', 'Chaos'),
  goal=K('접미어 속성 부여의 최대 개수 +1개 지우기', 'Remove +1 Suffix Modifier allowed'),
  showText=[K('접미가 한도를 넘어 새 옵션은 접두로', 'Suffixes are over the limit: the new option is a prefix')],
  edges=[{'if': {'has': 'contS'}, 'to': 'x1', 'res': 'fail', 'hide': True}, {'to': 'c2', 'res': 'ok'}], item=[J('p'), J('p'), AS, CDS, CC])
A(id='c2', kind='act', group='main', pos=[0, 6.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 투사체 피해', 'Projectile damage prefix'),
  showText=[K('접미가 한도를 넘어 접두만 바뀜', 'Suffixes are over the limit: only prefixes change')], show=['pre'],
  skipIf={'any': [{'has': 'pre'}, {'param': {'v': 2}}]}, skipTo='l2',
  edges=[{'if': {'has': 'pre'}, 'to': 'l2', 'res': 'ok'}, {'to': 'c2', 'res': 'fail', 'hide': True}], item=[PD, J('p'), AS, CDS, CC])
A(id='l2', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large'),
  showText=[K('접두 잡옵이 지워지면 성공, 좋은 접두가 지워지면 실패', 'The junk prefix goes: success; the good prefix goes: miss')],
  edges=[{'if': {'has': 'pre'}, 'to': 'ok', 'res': 'ok'}, {'to': 'c2', 'res': 'fail', 'label': K('좋은 접두가 지워짐 — 다시 카오스', 'Good prefix gone: Chaos again')}],
  over=[{'param': {'v': 2}, 'set': {'showText': [K('접두 하나가 지워짐 — 결과 그대로', 'One prefix goes: keep the result')], 'edges': [{'to': 'ok', 'res': 'ok'}]}}],
  item=[PD, RAD, AS, CDS, CC])
A(id='ok', kind='done', group='main', pos=[0, 8.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['d1', 'r1', 'r1x'], 'kr': '훼손 공개', 'en': 'Reveal'},
              {'id': 'L2', 'nodes': ['c2', 'l2'], 'kr': '우울', 'en': 'Melancholy'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
