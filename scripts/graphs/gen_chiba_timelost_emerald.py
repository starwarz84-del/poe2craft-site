# W24 2026-11-13: ChibaTTV 오래된 에메랄드(O6Rp7JIxhrs) 플로우차트 생성기 — 영상 성공 회차 한 줄
# 근거: scratchpad review/W24-chiba-emerald/timeline.md, frames/ (영상 0:00~14:57 화면 대조)
# 실행: cd scripts/graphs && python3 gen_chiba_timelost_emerald.py  → chiba-timelost-emerald-v2.json (gen_batch12.py 끝에서 자동 호출)
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/chiba-timelost-emerald-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

CCn = L('s', '반경 내 주요 패시브 스킬이 공격 치명타 명중 확률 (3—7)% 증가도 부여', 'Notable Passive Skills in Radius also grant (3—7)% increased Critical Hit Chance for Attacks', 'n', ['cc'])
CC = L('s', '반경 내 주요 패시브 스킬이 공격 치명타 명중 확률 (3—7)% 증가도 부여', 'Notable Passive Skills in Radius also grant (3—7)% increased Critical Hit Chance for Attacks', 'f', ['cc'])
CDS = L('s', '반경 내 주요 패시브 스킬이 창 사용 시 치명타 피해 보너스 (5—10)% 증가도 부여', 'Notable Passive Skills in Radius also grant (5—10)% increased Critical Damage Bonus with Spears', 'n', ['suf'])
CONT = L('p', '접미어 속성 부여의 최대 개수 +1개', '+1 Suffix Modifier allowed', 'c', ['contS'])
AS = L('s', '반경 내 주요 패시브 스킬이 공격 속도 (1—2)% 증가도 부여', 'Notable Passive Skills in Radius also grant (1—2)% increased Attack Speed', 'd', ['rev'])
PS = L('p', '반경 내 주요 패시브 스킬이 투사체 속도 (2—3)% 증가도 부여', 'Notable Passive Skills in Radius also grant (2—3)% increased Projectile Speed', 'n', ['pre'])
RAD = L('p', '반경이 매우 넓은 반경으로 업그레이드', 'Upgrades Radius to Very Large', 'c', ['rad'])
J = lambda s: L(s, '잡옵', 'Junk', 'j')
UN = lambda s: L(s, '훼손 옵션 (미공개)', 'Desecrated (unrevealed)', 'n')
ANN = K('소멸의 오브 사용', 'Use an Orb of Annulment')

g = {
 'id': 'chiba-timelost-emerald-v2', 'recipe': 'chiba-timelost-emerald-v2', 'cls': 'Time-Lost_Emerald', 'base': 'Time-Lost Emerald', 'ilvl': 80,
 'basePrice': {'Divine_Orb': 14},   # 4:05 자막 '14 divines'(거래 화면 4:10 같은 조건 13~14 div)
 'note': ('2026-11-13 W24 영상 전체 화면 대조(근거 scratchpad review/W24-chiba-emerald/timeline.md). 성공 회차(두 번째 베이스 Chimeric Curio) 한 줄: '
          '공격 치명타 확률 7% + 옵션 2개 레어 오래된 에메랄드 구입(4:05, 14 div) → 보존된 두개골로 네 번째 옵션(4:30) → 분열 = 공격 치명타 확률(4:46, 첫 베이스는 전령 분열로 실패 3:59) → '
          '소멸의 오브로 분열 + 옵션 1개(5:13) → 카오스로 창 치명타 피해 보너스(5:34) → 엑잘 2번(5:44) → 고대 위력적인 액체 경멸, 투사체 피해가 지워지고 +1 접미 허용(6:08) → '
          '두개골 훼손 + 심연의 메아리 공개, 빗나감(6:24) → 빛의 징조 + 소멸의 오브(9:13) → 다시 훼손·공개, 메아리로 다시 굴려 공격 속도(9:26) → 좌측 소멸의 징조 + 소멸의 오브 2번(10:22~10:34, 첫 번은 잡옵) → '
          '엑잘 2번(10:34) → 카오스로 투사체 속도(11:00, 접미가 한도를 넘어 접두만 바뀜) → 고대 위력적인 액체 우울, 잡옵이 지워지고 매우 넓은 반경(11:26). '
          '신성한 오브 수치 올리기(11:30~11:55)와 정제된 약탈자 기폭제 퀄리티(12:00)는 정책 14장·7장대로 뺌. 첫 베이스의 완벽한 확장·완벽한 제왕·신성한 오브(2:00~3:40)는 실패 회차라 꿀팁 후보. '
          '내부 결정: 두 번째 훼손의 뼈 종류는 화면으로 못 봐 보존된 두개골(정책 6장, 주얼 옵션 레벨 1). 경멸이 창 치명타 피해를 지우면 분열 + 옵션 1개까지 소멸 후 카오스부터(영상에 없음). '
          '공개는 빛의 징조로 다시(C17-3). 밸런스(마지막 접두 랜덤)는 하이엔드와 비용 차이가 약 2%라 뺌(사용자 결정 2026-11-13). '
          'D4 2026-11-13: 난이도 표 3(어려움) → 옛 하이엔드(영상 길)는 이름만 밸런스. '
          'E1 2026-11-13: D4가 만든 에센셜(공개·마지막 접두 결과 그대로)은 밸런스 159.5 / 에센셜 144.9 div로 차이 9.2% — 정책 D(등급별 비용 차이 10% 이내면 높은 등급 하나)로 지우고 밸런스 하나.'),
 'params': {'v': {'kr': '공개·마지막 접두', 'en': 'Reveal and last prefix', 'values': {
   '1': K('빛의 징조로 다시 공개, 투사체 속도·투사체 피해·공격 피해까지 카오스', 'Reveal again with Omen of Light, Chaos for projectile speed, projectile damage or attack damage')}}},
 'strategies': [{'id': 'bal', 'params': {'v': 1}}],
 'versions': [
   {'id': 'bal', 'kr': '밸런스', 'en': 'Balance', 'params': {'v': 1}, 'tier': 'bal',
    'desc': K('영상: 접두 투사체 속도까지 카오스, 우울이 지우면 다시', 'Video: Chaos until projectile speed, again if Melancholy takes it')}],
 'tags': {'cc': {'gi': 8}, 'contS': {'gi': 101, 'slot': {'s': 1}}, 'contP': {'gi': 102, 'slot': {'p': 1}}, 'rad': {'gi': 99},
          's3': {'gi': 3}, 's9': {'gi': 9}, 's11': {'gi': 11}, 's64': {'gi': 64}, 's65': {'gi': 65},
          'suf': {'anyOf': ['s65', 's9'], 'shown': 's65', 'label': K('창 치명타 피해 보너스·공격 치명타 피해 보너스', 'Critical Damage Bonus with Spears or for Attack Damage')},
          'rev': {'anyOf': ['s11', 's9', 's64', 's3'], 'shown': 's11', 'label': K('공격 속도·공격 치명타 피해 보너스·창 공격 속도·주요 패시브 스킬 효과', 'Attack Speed, Critical Damage Bonus for Attack Damage, Attack Speed with Spears or Notable Passive effect')},
          'p55': {'gi': 55}, 'p54': {'gi': 54}, 'p10': {'gi': 10},
          'pre': {'anyOf': ['p55', 'p54', 'p10'], 'shown': 'p55', 'label': K('투사체 속도·투사체 피해·공격 피해', 'Projectile Speed, Projectile Damage or Attack Damage')}},   # 5:00·6:30·10:40 영상 계획대로, 먼저 뜬 것
 'require': {'all': [{'has': 'cc'}, {'has': 'suf'}, {'has': 'rev'}, {'has': 'rad'}, {'has': 'pre'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]},
            {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'b0',
 'finals': [
   {'id': 'bal', 'tier': 'bal', 'kr': '밸런스 옵션', 'en': 'Balance',
    'lines': [{'tag': 'pre'}, {'tag': 'rad'}, {'tag': 'cc', 'fr': True}, {'tag': 'suf'}, {'tag': 'rev', 'des': True}]}],
 'finalItem': {'quality': 0, 'sockets': 0},
 'cap': {'p': 2, 's': 2},
}

N = []
A = lambda **kw: N.append(kw)

# ---------------- 베이스템 완성 ----------------
A(id='b0', kind='base', group='prep', pos=[0, 0], next='p1', start={'rar': 'rare', 'mods': [{'tag': 'cc'}, {'junk': 'p'}, {'junk': 's'}]},
  label=K('공격 치명타 확률 + 옵션 2개 레어 오래된 에메랄드 구입 (아이템 레벨 80)', 'Buy a rare Time-Lost Emerald: attack crit chance + two options (item level 80)'),
  item=[J('p'), CCn, J('s')])
A(id='p1', kind='act', group='prep', pos=[0, 1], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('네 번째 옵션(훼손) — 분열 조건 옵션 4개', 'Fourth option (desecrated): the fracture needs four'),
  showText=[K('훼손 옵션 (미공개, 분열되지 않음)', 'Desecrated (unrevealed, cannot fracture)')], edges=[{'to': 'pf'}],
  item=[J('p'), UN('p'), CCn, J('s')])
A(id='pf', kind='act', group='prep', pos=[0, 2], act='fracture', cur='Fracturing_Orb', label=K('분열', 'Fracture'),
  goal=K('분열 (공개된 옵션 3개 중 하나)', 'Fracture (one of the three revealed options)'),
  showText=[K('공격 치명타 확률이 분열되면 성공', 'Success when attack crit chance fractures')],
  edges=[{'if': {'fractured': 'cc'}, 'to': 'pc', 'res': 'ok', 'label': K('공격 치명타 확률 분열', 'Attack crit chance fractured')},
         {'to': 'xj', 'res': 'fail', 'dash': True, 'label': K('다른 옵션 분열', 'Another option fractured')}],
  item=[J('p'), UN('p'), CC, J('s')])
A(id='xj', kind='exit', group='prep', pos=[1, 2], simTo='b0', variant='fail', label=K('다른 옵션 분열 — 새 베이스', 'Another option fractured: new base'),
  note=K('공격 치명타 확률이 아닌 옵션이 분열되면 새 베이스로 처음부터', 'Another option fractured: start over on a new base'))
A(id='pc', kind='cleanup', group='prep', pos=[0, 3], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기기', 'Keep only the fracture + one option'), edges=[{'to': 'ms'}], item=[J('p'), CC])
# ---------------- 옵션 추가 작업 ----------------
A(id='ms', kind='mark', group='main', pos=[0, 4.4], next='c2', label=K('아이템 제작 시작', 'Item crafting starts'), item=[J('p'), CC])
A(id='c2', kind='act', group='main', pos=[0, 5.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접미 두 번째 옵션', 'Second suffix'), show=['suf'],
  edges=[{'if': {'has': 'suf'}, 'to': 'c3', 'res': 'ok'}, {'to': 'c2', 'res': 'fail', 'hide': True}], item=[CC, CDS])
A(id='c3', kind='act', group='main', pos=[0, 6.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 옵션 2개', 'Two prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개씩', 'en': 'One random option each'}],
  edges=[{'if': {'full': 'p'}, 'to': 'c4'}, {'to': 'c3', 'hide': True}], item=[J('p'), J('p'), CC, CDS])
A(id='c4', kind='act', group='main', pos=[0, 7.4], act='essence', cur='Ancient_Potent_Liquid_Contempt', ess='contS', liquid=True, alt='contP',
  label=K('액체', 'Liquid'), goal=K('고대 위력적인 액체 경멸', 'Ancient Potent Liquid Contempt'),
  showText=[{'s': 'p', 'kr': '접미어 속성 부여의 최대 개수 +1개', 'en': '+1 Suffix Modifier allowed'}],
  edges=[{'if': {'all': [{'has': 'contS'}, {'has': 'suf'}]}, 'to': 'c5', 'res': 'ok'},
         {'to': 'c4x', 'res': 'fail', 'label': K('치명타 피해가 지워짐', 'Crit damage removed')}],
  item=[J('p'), CONT, CC, CDS])
A(id='c4x', kind='cleanup', group='main', pos=[1, 7.4], keep=[], maxJunk=1, label=ANN, goal=ANN,
  target=K('분열 + 옵션 1개만 남기고 카오스부터', 'Keep the fracture + one option, Chaos again'), edges=[{'to': 'c2'}])
A(id='c5', kind='act', group='main', pos=[0, 8.4], act='desecrate', cur='Preserved_Cranium', label=K('훼손', 'Desecrate'),
  goal=K('접미 세 번째 옵션(훼손)', 'Third suffix (desecrated)'), showText=[{'s': 's', 'kr': '훼손 옵션 (미공개)', 'en': 'Desecrated (unrevealed)'}],
  edges=[{'to': 'c6'}], item=[J('p'), CONT, CC, CDS, UN('s')])
A(id='c6', kind='act', group='main', pos=[0, 9.4], act='reveal', omens=['Omen_of_Abyssal_Echoes'], want='rev', label=K('공개', 'Reveal'),
  goal=K('접미 공격 속도', 'Attack speed suffix'),
  show=['rev'],
  edges=[{'if': {'added': 'rev'}, 'to': 'c7', 'res': 'ok'}, {'to': 'c6x', 'res': 'fail', 'label': K('빗나감', 'Miss')}],
  item=[J('p'), CONT, CC, CDS, AS])
A(id='c6x', kind='act', group='main', pos=[1, 9.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Light'], label=ANN, goal=ANN,
  target=K('훼손 옵션 지우고 다시 훼손', 'Remove the desecrated option, desecrate again'), edges=[{'to': 'c5'}])
A(id='c7', kind='act', group='main', pos=[0, 10.4], act='annul', cur='Orb_of_Annulment', omens=['Omen_of_Sinistral_Annulment'], label=K('소멸', 'Annul'),
  goal=K('접두 +1 접미 허용 옵션 지우기 — 잡옵이 지워지면 한 번 더', 'Remove the +1 suffix line: once more if the junk goes'),
  edges=[{'if': {'has': 'contS'}, 'to': 'c7', 'res': 'fail'}, {'to': 'c8', 'res': 'ok'}], item=[CC, CDS, AS])
A(id='c8', kind='act', group='main', pos=[0, 11.4], act='exalt', cur='Exalted_Orb', label=K('엑잘', 'Exalt'),
  goal=K('접두 채우기', 'Fill the prefixes'), showText=[{'s': 'p', 'kr': '랜덤 옵션 1개씩', 'en': 'One random option each'}],
  edges=[{'if': {'full': 'p'}, 'to': 'c9'}, {'to': 'c8', 'hide': True}], item=[J('p'), J('p'), CC, CDS, AS])
A(id='c9', kind='act', group='main', pos=[0, 12.4], act='chaos', cur='Chaos_Orb', label=K('카오스', 'Chaos'),
  goal=K('접두 투사체 속도', 'Projectile speed prefix'), show=['pre'],
  edges=[{'if': {'has': 'pre'}, 'to': 'c10', 'res': 'ok'}, {'to': 'c9', 'res': 'fail', 'hide': True}], item=[PS, J('p'), CC, CDS, AS])
A(id='c10', kind='act', group='main', pos=[0, 13.4], act='essence', cur='Ancient_Potent_Liquid_Melancholy', ess='rad', liquid=True,
  label=K('액체', 'Liquid'), goal=K('고대 위력적인 액체 우울', 'Ancient Potent Liquid Melancholy'),
  showText=[{'s': 'p', 'kr': '반경이 매우 넓은 반경으로 업그레이드', 'en': 'Upgrades Radius to Very Large'}],
  edges=[{'if': {'has': 'pre'}, 'to': 'ok', 'res': 'ok'}, {'to': 'c9', 'res': 'fail', 'label': K('투사체 속도가 지워짐', 'Projectile speed removed')}],
  item=[PS, RAD, CC, CDS, AS])
A(id='ok', kind='done', group='main', pos=[0, 14.4], label=K('완성', 'Finished'))
g['nodes'] = N
g['loops'] = [{'id': 'L1', 'nodes': ['c5', 'c6', 'c6x'], 'kr': '훼손 공개', 'en': 'Reveal'},
              {'id': 'L2', 'nodes': ['c9', 'c10'], 'kr': '우울', 'en': 'Melancholy'}]

json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(N), 'nodes')
