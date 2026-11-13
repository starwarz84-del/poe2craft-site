# 난이도 표(docs/policies.md 10장, 사용자 확정 2026-11-13 14:43 '난이도는 표로 통일') 점검·계산
# 시뮬 결과(site/data/sim/<그래프 id>.json)에서 그 레시피의 가장 높은 등급(레시피가 있는 등급 중) 한 가지로 잼:
#   ① 가장 많이 한 단계의 시도 수(완성 1개당, 베이스를 다시 사는 회차 포함)  ② 비싼 징조 수(완성 1개당, site/data/budget.json expensive)
#   ③ 평균 비용(완성 1개당, div, 베이스 포함) — 셋 중 가장 높은 단계
#   ④ 분열 빗나감으로 베이스를 버림(분열 상자 + 시뮬 평균 베이스 2개 이상) → 최소 어려움(3) (사용자 확정 2026-11-13 15:21)
# 사용: python3 tools/test/_difftable.py         → 그래프마다 잰 값·표 난이도·DIFFSET 값, 다른 것에 '*'
#       python3 tools/test/_difftable.py --set   → DIFFSET에 넣을 줄(파이썬 dict)만 출력
import json, glob, os, sys
H = '/home/claude/poe2craft-site'
STEPS = [5, 10, 150, 1500, 20000]        # 쉬움·보통·어려움·전문가·극한이 되는 시도 수
OMENS = [0.5, 1, 15, 25, 300]            # 같은 순서, 비싼 징조 수
COST = [1, 5, 100, 500, None]            # 같은 순서, div — 극한 = 칼란드라의 거울 1개 시세
NAMES = ['입문', '쉬움', '보통', '어려움', '전문가', '극한']
B = json.load(open(f'{H}/site/data/budget.json')); EXP = set(B['expensive'])
P = json.load(open(f'{H}/site/data/prices.json')); MIRROR = P['p']['Mirror_of_Kalandra'] / P['divine']
COST[4] = MIRROR
R = json.load(open(f'{H}/site/data/recipes.json')); R = R['recipes'] if isinstance(R, dict) else R
exec(open(f'{H}/scripts/difficulty.py').read())
ORDER = ['high', 'bal', 'ess']
FRAC_BASES = 2   # 이 이상이면 '베이스를 계속 버림'

def measure(res, kinds):
    mx, mn = 0, ''
    for nid, nv in res['nodes'].items():
        if kinds.get(nid) in ('act', 'side') and nv['visits'] > mx: mx, mn = nv['visits'], nid
    om = sum(v for k, v in res['use'].items() if k in EXP)
    return mx, mn, om, res['mean']

def level(mx, om, cost):
    l = 0
    for i in range(5):
        if mx >= STEPS[i] or om >= OMENS[i] or cost >= COST[i]: l = i + 1
    return l

rows = []
for f in sorted(glob.glob(f'{H}/site/data/sim/*.json')):
    d = json.load(open(f)); gid = d['id']
    kinds = {n['id']: n.get('kind') for n in d['graph']['nodes']}
    frac = any(n.get('act') == 'fracture' for n in d['graph']['nodes'])
    have = {r.get('tier') for r in R if (r.get('tierGroup') or r['id']) == gid}
    S = {s['id']: s for s in d['strategies']}
    pick = next((t for t in ORDER if t in S and (t in have or not have)), None) or next(iter(S))
    mx, mn, om, cost = measure(S[pick]['res'], kinds)
    bases = S[pick]['res'].get('bases', 1)
    lv = level(mx, om, cost)
    if frac and bases >= FRAC_BASES: lv = max(lv, 3)
    rows.append((gid, pick, mx, mn, om, cost, bases, lv, DIFFSET.get(gid), sorted(have, key=ORDER.index) if have and None not in have else []))

if '--set' in sys.argv:
    print('{' + ', '.join(f"'{g}': {lv}" for g, _, _, _, _, _, _, lv, _, _ in rows) + '}')
else:
    for g, pick, mx, mn, om, cost, bases, lv, ds, have in rows:
        print(f"{'*' if ds != lv else ' '} {g[:34]:34} {pick:4} 시도 {mx:8.0f} ({mn}) 징조 {om:6.1f} 비용 {cost:8.1f} 베이스 {bases:5.2f} → {lv} {NAMES[lv]:3} 표 {ds} 등급 {'/'.join(have)}")
    print('다른 것', sum(1 for r in rows if r[8] != r[7]))
