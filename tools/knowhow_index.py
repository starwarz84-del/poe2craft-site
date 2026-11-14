"""제작 노하우 분류표 만들기 (사용자 확정 2026-11-14 19:02: 제작법을 분류법에 따라 분류해서 사용)
   python3 tools/knowhow_index.py
   docs/crafting-knowhow.md의 K 표를 읽어 docs/crafting-knowhow.json(분류 + 리버스 적용)을 만들고,
   md의 '분류별 찾기' 칸(<!-- 분류표: 시작/끝 -->)을 다시 씀. 분류는 아래 CLS에 적음 — 새 K를 넣으면 여기에도 한 줄."""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, 'docs', 'crafting-knowhow.md')
STAGE = {'1': '베이스·매직 → 레어', '2': '분열', '3': '분열 직후 두 번째 옵션', '4': '반대쪽 채우기·엑잘', '5': '절사', '6': '잡옵 지우기',
         '7': '훼손', '8': '제작 옵션(에센스·합금)', '9': '마무리(퀄리티·수치)', '10': '주얼', '10-1': '분열 없는 가성비 경로', '11': '사기·팔기 판단', '0': '지난 리그'}
EFFECT = {'확정': '옵션을 확정으로 붙임', '확률': '원하는 옵션이 뜰 확률을 올림', '정리': '잡옵·실패 정리 비용을 줄임', '자리': '자리 막기·순서로 다른 옵션을 지킴', '판단': '경로·구입·판매를 고름'}
# id: (구간, 부위, 효과)
CLS = {
 'K1': ('3', '전체', '정리'), 'K2': ('4', '전체', '정리'), 'K3': ('6', '전체', '정리'), 'K4': ('8', '전체', '확정'), 'K5': ('8', '전체', '확정'),
 'K5b': ('8', '무기', '확정'), 'K6': ('7', '전체', '확률'), 'K7': ('7', '전체', '자리'), 'K8': ('4', '장신구', '확률'), 'K9': ('6', '장신구', '정리'),
 'K10': ('4', '전체', '정리'), 'K11': ('4', '전체', '확률'), 'K12': ('7', '무기·장신구', '확률'), 'K13': ('11', '장신구·방어구', '판단'), 'K14': ('4', '전체', '확률'),
 'K15': ('5', '전체', '자리'), 'K16': ('3', '전체', '확률'), 'K17': ('1', '무기(지팡이)', '확률'), 'K18': ('7', '전체', '자리'), 'K19': ('1', '장신구', '자리'),
 'K20': ('5', '장신구', '정리'), 'K21': ('1', '장신구', '확정'), 'K22': ('2', '전체', '판단'), 'K23': ('8', '무기(마법봉)', '확정'), 'K24': ('0', '전체', '판단'),
 'K25': ('1', '전체', '자리'), 'K26': ('7', '전체', '자리'), 'K27': ('2', '장신구(목걸이)', '판단'), 'K28': ('11', '전체', '판단'), 'K29': ('8', '방어구(집중구)', '확정'),
 'K30': ('4', '전체', '자리'), 'K31': ('10-1', '전체', '판단'), 'K32': ('2', '장신구(목걸이)', '판단'), 'K33': ('2', '장신구(반지)', '판단'), 'K34': ('10-1', '장신구(반지)', '판단'),
 'K35': ('6', '장신구', '정리'), 'K36': ('5', '무기', '자리'), 'K37': ('4', '전체', '확률'), 'K38': ('8', '무기(활)', '확정'), 'K39': ('4', '전체', '확률'),
 'K40': ('5', '전체', '확률'), 'K41': ('4', '장신구', '확률'), 'K42': ('8', '전체', '정리'), 'K43': ('1', '장신구(반지)', '판단'), 'K44': ('10', '주얼', '자리'),
 'K45': ('8', '방어구(장화)', '확정'), 'K46': ('9', '전체', '정리'), 'K47': ('10-1', '장신구·방어구', '확정'), 'K48': ('10-1', '전체', '정리'), 'K49': ('11', '전체', '판단'),
 'K50': ('2', '장신구(반지)', '판단'), 'K51': ('3', '전체', '확률'), 'K52': ('4', '장신구', '확률'), 'K53': ('2', '전체', '판단'),
}
def rstate(t):
    t = t.strip()
    for k in ('자동', '선택', '제안', '미적용', '아직 없음'):
        if t.startswith(k): return k
    return '기타'
def main():
    s = open(MD, encoding='utf-8').read()
    rows = [l for l in s.split('\n') if re.match(r'^\| K\d+b? \|', l)]
    out, miss = [], []
    for l in rows:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        k = c[0]
        if k not in CLS: miss.append(k); continue
        st, part, eff = CLS[k]
        out.append({'id': k, 'when': c[1], 'how': c[2], 'stage': st, 'stageName': STAGE[st], 'part': part, 'effect': eff, 'reverse': rstate(c[5]), 'reverseNote': c[5]})
    if miss: raise SystemExit('분류 없는 노하우: ' + ', '.join(miss) + ' → tools/knowhow_index.py CLS에 추가')
    json.dump({'stages': STAGE, 'effects': EFFECT, 'items': out}, open(os.path.join(ROOT, 'docs', 'crafting-knowhow.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    order = list(STAGE)
    L = ['<!-- 분류표: 시작 (tools/knowhow_index.py가 씀) -->', '', '| 구간 | 노하우(부위 · 효과 · 리버스) |', '|---|---|']
    for st in order:
        xs = [x for x in out if x['stage'] == st]
        if xs: L.append(f"| {st}. {STAGE[st]} | " + '<br>'.join(f"{x['id']} {x['when']} ({x['part']} · {x['effect']} · {x['reverse']})" for x in xs) + ' |')
    L += ['', '| 효과 | 노하우 |', '|---|---|']
    for e in EFFECT:
        L.append(f"| {e}: {EFFECT[e]} | " + ', '.join(x['id'] for x in out if x['effect'] == e) + ' |')
    L += ['', '| 리버스 | 노하우 |', '|---|---|']
    for r in ('자동', '선택', '제안', '아직 없음', '미적용'):
        L.append(f"| {r} | " + ', '.join(x['id'] for x in out if x['reverse'] == r) + ' |')
    L += ['', '<!-- 분류표: 끝 -->']
    block = '\n'.join(L)
    if '<!-- 분류표: 시작' in s:
        s = re.sub(r'<!-- 분류표: 시작.*?<!-- 분류표: 끝 -->', lambda m: block, s, flags=re.S)
    else:
        s = s.replace('## 노하우\n', '## 분류별 찾기\n\n분류법(사용자 확정 2026-11-14 19:02): **구간**(제작 순서, `docs/crafting-stages.md` 장 번호와 같음) · **부위** · **효과**(확정·확률·정리·자리·판단) · **리버스 적용**(자동·선택·제안·아직 없음·미적용). 새 노하우는 아래 K 표에 한 줄 + `tools/knowhow_index.py` CLS에 분류 한 줄 → 스크립트를 돌리면 이 칸과 `docs/crafting-knowhow.json`이 다시 써짐. 리버스에 넣을 땐 같은 구간·효과의 노하우를 함께 봄.\n\n' + block + '\n\n## 노하우\n', 1)
    open(MD, 'w', encoding='utf-8').write(s)
    print(f'노하우 {len(out)}개 분류 → docs/crafting-knowhow.json')
main()
