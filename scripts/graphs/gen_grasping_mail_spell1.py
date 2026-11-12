# W11 2026-11-13: 반지깎는노인 룬 아버지의 탐욕스러운 사슬옷 플로우차트(새 기준) 생성기 — 영상 y5Ch3AJpl5c 성공 회차 한 줄
# (gen_batch19.py의 1번 그래프를 대신함. scripts/graphs/에서 python3 gen_grasping_mail_spell1.py)
# 출력: scripts/graphs/grasping-mail-spell1-v2.json (이 파일만 씀)
# 근거: scratchpad review/W11-grasping-mail/timeline.md (영상 0:00~12:41 자막 전체 + 화면 캡처 50장)
#   0:00~7:00 베이스 설명(균열 반지 60개 → 룬벼림 → 룬숙련 → 룬 아버지, 퀄리티·기폭제 퀄리티 30%), 7:01 목표 슬라이드
#   7:35~7:58 카오스 오브 약 22만 개로 모든 주문 스킬 +1 → 8:38~9:58 미공개 훼손으로 후보를 셋으로 줄이고 히네코라의 머리카락 4개로 분열 = 베이스(basePrice, 사용자 확정 11-12)
#   10:09 주문 치명타 피해 보너스(먼저) → 10:12 절사의 징조 2개 → 10:15 시전 속도(접미 완성). 접미를 붙인 커런시는 편집으로 빠짐(엑잘 단계는 가정)
#   10:11 아스트리드의 창의성 이미 장착 → 10:28~11:04 좌측 결정화 + 섬망의 에센스(할당, 영상은 '지배'가 나올 때까지 완벽한 육신의 에센스와 번갈아)
#   11:25 접두 잡옵(방어도·회피·에너지 보호막 %) → 11:28 좌측 결정화 + 룬 수호 합금 50:50 한 번에 성공 → 11:40 훼손 → 11:43·11:58 공개 + 메아리, 빛의 징조로 다시 → 주문 피해 38%(1티어)
# 내부 결정: 합금 = 군왕의 합금(POE2DB 'Armour: (24—30)% increased Runic Ward', 룬 합금은 반지·목걸이·벨트용), 훼손 뼈 = 고대 갈비뼈(주문 피해 1티어 레벨 82, 화면 확인 못 함),
#   강령술의 징조 없음(접미가 꽉 차고 접두 한 자리만 비어 뼈가 그 자리로 감 — 영상 채팅에도 빛·메아리만), 아스트리드는 영상처럼 접두 작업 전(10:11).
# 등급: 난이도 5(극한) → 하이엔드만(정책 10장).
import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else f'{H}/grasping-mail-spell1-v2.json'
K = lambda kr, en: {'kr': kr, 'en': en}

def L(s, kr, en, m='n', tags=None):
    d = {'s': s, 'kr': kr, 'en': en, 'm': m}
    if tags: d['tags'] = tags
    return d

SPL = L('s', '모든 주문 스킬 레벨 +1 (분열)', '+1 to Level of all Spell Skills (fractured)', 'f', ['spell'])
CSD = L('s', '주문 치명타 피해 보너스 (26—29)% 증가', '(26—29)% increased Critical Spell Damage Bonus', 'n', ['csd'])
CS = L('s', '시전 속도 (22—24)% 증가', '(22—24)% increased Cast Speed', 'n', ['cs'])
NT = L('p', '무작위 주요 패시브 스킬 할당 (섬망의 에센스)', 'Allocates a random Notable Passive Skill (Essence of Delirium)', 'c', ['nt'])
RW = L('p', '룬 수호 (24—30)% 증가 (군왕의 합금)', '(24—30)% increased Runic Ward (Sovereign Alloy)', 'c', ['rw'])
SD = L('p', '주문 피해 (35—39)% 증가', '(35—39)% increased Spell Damage', 'd', ['sd'])
UNR = L('p', '훼손 옵션(미공개)', 'Desecrated modifier (unrevealed)', 'u')
JP = L('p', '잡옵', 'Junk', 'j')
AS = L('r', '아스트리드의 창의성', 'Astrid’s Creativity', 'r')

I0 = [JP, SPL]
I1 = [SPL, CSD]
I2 = [SPL, CSD, CS]
I3 = [JP, SPL, CSD, CS, AS]
I4 = [NT, SPL, CSD, CS, AS]
I5 = [NT, JP, SPL, CSD, CS, AS]
I6 = [NT, RW, SPL, CSD, CS, AS]
I7 = [NT, RW, UNR, SPL, CSD, CS, AS]
I8 = [NT, RW, SD, SPL, CSD, CS, AS]

TWO = {'count': {'tag': 'suf', 'min': 2}}
JUNKP = {'junk': {'side': 'p', 'tag': 'keepP'}}
RULES = [
    ({'all': [{'not': TWO}, {'not': {'has': 'suf'}}]}, 'c1'),
    ({'all': [{'not': TWO}, {'sideLt': {'side': 's', 'n': 3}}]}, 's1'),
    ({'not': TWO}, 'w1'),
    ({'not': {'rune': 'Astrid'}}, 'r1'),
    ({'unrevSide': 'p'}, 'rv'),
    ({'all': [{'has': 'nt'}, {'has': 'rw'}, {'has': 'sd'}]}, 'ok'),
    ({'des': True}, 'rvx'),
    ({'all': [{'not': {'has': 'nt'}}, {'not': {'has': 'rw'}}, {'not': {'sideLt': {'side': 'p', 'n': 2}}}]}, 'pc'),
    ({'all': [{'not': {'has': 'nt'}}, JUNKP]}, 'p1'),
    ({'not': {'has': 'nt'}}, 'p0'),
    ({'all': [{'not': {'has': 'rw'}}, JUNKP]}, 'p3'),
    ({'not': {'has': 'rw'}}, 'p2'),
    (None, 'd1'),
]

def R(vis):
    """Every step re-checks the item; only the targets in vis are drawn (first rule with that target)."""
    out, seen = [], set()
    for c, to in RULES:
        e = {'to': to}
        if c is not None: e['if'] = c
        v = vis.get(to)
        if v is not None and to not in seen:
            e.update(v if isinstance(v, dict) else {'res': v}); seen.add(to)
        else:
            e['hide'] = True
        out.append(e)
    return out

OKV = lambda **k: dict({'res': 'ok'}, **k)
FV = lambda **k: dict({'res': 'fail'}, **k)

def act(id, pos, a, cur, goal, label, item, edges, **k):
    n = {'id': id, 'kind': 'act', 'group': 'main', 'pos': pos, 'act': a}
    if cur: n['cur'] = cur
    n.update({'goal': goal, 'label': label, 'edges': edges, 'item': item})
    n.update(k)
    return n

nodes = [
 {'id': 'h1', 'kind': 'base', 'group': 'prep', 'pos': [0, 0], 'next': 'ms',
  'start': {'rar': 'rare', 'mods': [{'tag': 'spell', 'fr': True}, {'junk': 'p'}], 'quality': 30},
  'label': K('모든 주문 스킬 레벨 +1 분열 + 잡옵 1개 (퀄리티 30% · 기폭제 퀄리티 30%)', 'Fractured +1 to all spell skills + one junk line (30% quality, 30% catalyst quality)'),
  'item': I0},
 {'id': 'ms', 'kind': 'mark', 'group': 'main', 'pos': [0, 0.6], 'next': 'c1', 'label': K('아이템 제작 시작', 'Item crafting starts'), 'item': I0},
 act('c1', [0, 1], 'chaos', 'Chaos_Orb', K('접미 두번째 옵션', 'Second suffix'), K('카오스', 'Chaos'), I1,
     [{'if': {'has': 'suf'}, 'to': 's1', 'res': 'ok'}, {'to': 'c1', 'res': 'fail'}], show=['csd'],
     showText=[K('주문 치명타 피해 보너스·시전 속도 중 먼저 뜬 것', 'Whichever of spell crit damage or cast speed lands first')]),
 act('s1', [0, 2], 'exalt', 'Perfect_Exalted_Orb', K('접미 세번째 옵션', 'Third suffix'), K('엑잘', 'Exalt'), I2,
     R({'r1': OKV(), 'w1': FV(port='right')}), show=['cs'], omens=['Omen_of_Dextral_Exaltation'],
     showText=[K('남은 옵션 중 먼저 뜬 것', 'Whichever of the rest lands first')]),
 act('w1', [1, 2], 'chaos', 'Perfect_Chaos_Orb', K('접미 세번째 옵션', 'Third suffix'), K('카오스', 'Chaos'), I2,
     R({'r1': OKV(), 's1': FV(), 'c1': FV()}), show=['cs'], trim={'side': 's', 'keep': 'keepS'}),
 act('r1', [0, 3], 'rune', None, K('아스트리드의 창의성 장착', 'Socket Astrid’s Creativity'), K('룬', 'Rune'), I3,
     [{'to': 'pc'}], showText=[K('제작 옵션 하나 더', 'One more crafted modifier')], rune=K('아스트리드의 창의성', 'Astrid’s Creativity'),
     skipIf={'rune': 'Astrid'}, skipTo='pc', skipHide=True),
 act('pc', [0, 4], 'annul', 'Orb_of_Annulment', K('접두 잡옵 하나만 남기기', 'Leave one junk prefix'), K('소멸', 'Annul'), I3,
     [{'if': {'not': {'sideLt': {'side': 'p', 'n': 2}}}, 'to': 'pc', 'res': 'fail'}, {'to': 'p0', 'res': 'ok'}], omens=['Omen_of_Sinistral_Annulment'],
     skipIf={'any': [{'has': 'nt'}, {'has': 'rw'}, {'sideLt': {'side': 'p', 'n': 2}}]}, skipTo='p0', skipNote=K('접두가 하나 이하면 건너뜀', 'Skipped with one prefix or none')),
 act('p0', [0, 5], 'exalt', 'Exalted_Orb', K('에센스가 지울 접두 잡옵', 'A junk prefix for the essence to remove'), K('엑잘', 'Exalt'), I3,
     [{'to': 'p1', 'res': 'ok'}], showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}],
     skipIf={'any': [JUNKP, {'has': 'nt'}]}, skipTo='p1', skipNote=K('접두 잡옵이 있으면 건너뜀', 'Skipped while a junk prefix is there')),
 act('p1', [0, 6], 'essence', 'Essence_of_Delirium', K('잡옵을 지우고 무작위 주요 패시브 스킬 할당', 'The junk goes for Allocates a random Notable Passive Skill'), K('에센스', 'Essence'), I4,
     R({'p2': OKV()}), showText=[{'s': 'p', 'kr': '무작위 주요 패시브 스킬 할당 (제작 옵션)', 'en': 'Allocates a random Notable Passive Skill (crafted)'}],
     ess='nt', omens=['Omen_of_Sinistral_Crystallisation'], skipIf={'has': 'nt'}, skipTo='p2', skipHide=True),
 act('p2', [0, 7], 'exalt', 'Exalted_Orb', K('합금이 지울 접두 잡옵', 'A junk prefix for the alloy to remove'), K('엑잘', 'Exalt'), I5,
     R({'p3': OKV()}), showText=[{'s': 'p', 'kr': '잡옵', 'en': 'Junk'}],
     skipIf={'any': [{'has': 'rw'}, {'all': [{'has': 'nt'}, JUNKP]}]}, skipTo='p3', skipNote=K('접두 잡옵이 남아 있으면 건너뜀', 'Skipped while a junk prefix is left')),
 act('p3', [0, 8], 'essence', 'Sovereign_Alloy', K('잡옵을 지우고 룬 수호 (24—30)% 증가', 'The junk goes for (24—30)% increased Runic Ward'), K('합금', 'Alloy'), I6,
     R({'d1': OKV(), 'p1': FV(port='right', label=K('할당이 지워짐 — 에센스부터', 'Allocation gone: back to the essence'))}),
     showText=[{'s': 'p', 'kr': '룬 수호 (24—30)% 증가 (제작 옵션)', 'en': '(24—30)% increased Runic Ward (crafted)'}],
     ess='rw', omens=['Omen_of_Sinistral_Crystallisation']),
 act('d1', [0, 9], 'desecrate', 'Ancient_Rib', K('접두 세번째 옵션(훼손)', 'Third prefix (desecrated)'), K('훼손', 'Desecrate'), I7,
     R({'rv': {}}), showText=[{'s': 'p', 'kr': '훼손 옵션(미공개)', 'en': 'Desecrated modifier (unrevealed)'}], **({'omens': ['Omen_of_Sinistral_Necromancy']} if os.environ.get('GM_NECRO') else {})),
 act('rv', [0, 10], 'reveal', None, K('훼손 옵션 확인', 'Reveal the desecrated modifier'), K('공개', 'Reveal'), I8,
     R({'ok': OKV(), 'rvx': FV(port='right')}), want='sd', show=['sd'], omens=['Omen_of_Abyssal_Echoes']),
 {'id': 'rvx', 'kind': 'act', 'group': 'main', 'pos': [1, 10], 'act': 'annul', 'cur': 'Orb_of_Annulment', 'omens': ['Omen_of_Light'],
  'label': K('소멸의 오브 사용', 'Use an Orb of Annulment'), 'goal': K('소멸의 오브 사용', 'Use an Orb of Annulment'),
  'target': K('훼손 옵션 제거', 'Remove the desecrated modifier'), 'edges': R({'d1': {}})},
 {'id': 'ok', 'kind': 'done', 'group': 'main', 'pos': [0, 11], 'label': K('완성', 'Finished')},
]

g = {
 'id': 'grasping-mail-spell1-v2', 'recipe': 'grasping-mail-spell1-v2', 'cls': 'Grasping_Mail_ring', 'base': "Runefather's Grasping Mail", 'ilvl': 82,
 'note': ('반지깎는노인 탐욕스러운 사슬옷(y5Ch3AJpl5c, 2026-11-13 W11 영상 전체 재대조, 새 플로우차트 기준) — 모든 주문 스킬 +1 분열 + 잡옵(카오스 오브 약 22만 개, 베이스) '
          '→ 카오스 오브(주문 치명타 피해 보너스) → 우측 찬미 + 완벽한 엑잘·절사의 징조 + 완벽한 카오스 오브(시전 속도, 영상 10:12 절사 2개) → 아스트리드의 창의성 '
          '→ 좌측 결정화 + 섬망의 에센스(할당) → 접두 잡옵 → 좌측 결정화 + 군왕의 합금(룬 수호, 1/2) → 고대 갈비뼈 → 주문 피해 1티어 공개(빛의 징조로 다시). '
          '기원의 나무 옵션 가중치는 추정. 히네코라의 머리카락·신성한 오브는 비용에서 뺌.'),
 'params': {}, 'strategies': [{'id': 'high', 'params': {}}],
 'versions': [{'id': 'high', 'kr': '하이엔드', 'en': 'High-end', 'params': {},
               'desc': K('영상: 주문 치명타 피해 보너스 · 시전 속도 · 주문 피해 1티어', 'Video: T1 spell crit damage, cast speed and spell damage')}],
 'tags': {'spell': {'gi': 140}, 'csd': {'gi': 138, 'tmax': 1}, 'cs': {'gi': 126, 'tmax': 1}, 'sd': {'gi': 134, 'tmax': 1}, 'nt': {'gi': 51}, 'rw': {'gi': 57},
          'suf': {'anyOf': ['csd', 'cs'], 'label': K('주문 치명타 피해 보너스·시전 속도 1티어', 'T1 spell crit damage or cast speed')},
          'keepS': {'anyOf': ['csd', 'cs', 'spell']}, 'keepP': {'anyOf': ['nt', 'rw', 'sd']}},
 'require': {'all': [{'has': 'nt'}, {'has': 'rw'}, {'has': 'sd'}, {'has': 'csd'}, {'has': 'cs'}, {'has': 'spell'}]},
 'groups': [{'id': 'prep', 'kr': '베이스템 완성', 'en': 'Finished base', 'cols': [0, 1]}, {'id': 'main', 'kr': '옵션 추가 작업', 'en': 'Adding modifiers', 'cols': [0, 1]}],
 'start': 'h1',
 'loops': [
   {'id': 'L0', 'nodes': ['s1', 'w1'], 'kr': '접미 시전 속도', 'en': 'Cast speed suffix', 'fold': True,
    'goal': K('접미 시전 속도 1티어', 'T1 cast speed suffix'),
    'steps': [{'kr': '우측 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 세번째 옵션', 'en': 'Omen of Dextral Exaltation + Perfect Exalted Orb for the third suffix', 'node': 's1'},
              {'kr': '빗나간 옵션이 가장 낮으면 절사의 징조 + 완벽한 카오스 오브로 다시', 'en': 'Miss and it is the lowest line: Omen of Whittling + Perfect Chaos Orb', 'node': 'w1'},
              {'kr': '접미 자리가 비면 1번부터', 'en': 'A suffix slot opens: back to step 1', 'node': 's1'}],
    'worst': {'kr': '주문 치명타 피해 보너스가 지워지면 카오스 단계부터', 'en': 'Spell crit damage gone: back to the Chaos step', 'to': 'c1'},
    'item': I2},
   {'id': 'L1', 'nodes': ['d1', 'rv', 'rvx'], 'kr': '훼손 공개', 'en': 'Reveal'}],
 'finals': [{'id': 'high', 'kr': '하이엔드 옵션', 'en': 'High-end',
             'lines': [{'tag': 'nt', 'ess': True}, {'tag': 'rw', 'ess': True}, {'tag': 'sd', 'tmax': 1, 'des': True},
                       {'tag': 'spell', 'fr': True}, {'tag': 'csd', 'tmax': 1}, {'tag': 'cs', 'tmax': 1}]}],
 'finalItem': {'quality': 30, 'sockets': 2},
 'xsub': ['Genesis Tree Caster', 'Genesis Tree Minion'], 'xroll': True,
 'basePrice': {'Chaos_Orb': 220000, 'Hinekoras_Lock': 4},   # 마스터 11-13: 6행 노트대로 히네코라 4개도 베이스(W11이 빠뜨림)
 'nodes': nodes,
}
json.dump(g, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('wrote', OUT, len(nodes), 'nodes')
