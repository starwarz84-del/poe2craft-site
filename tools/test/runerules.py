"""룬 규칙 점검(사용자 지시 2026-11-13: 룬 특성에 맞게) — 근거 poe2db Socket-bound Augments·각 룬 페이지(docs/game-rules.md '룬 규칙').
① 'Limited to 1' 룬은 아이템당 하나 ② 소켓 고정(Socket-bound) 룬은 한 번 넣으면 빼거나 다른 룬으로 바꿀 수 없음
   (아스트리드의 창의성은 꺼낼 수 없지만 다른 증강물로 바꿀 수는 있음) ③ 넣은 룬 수 ≤ 소켓 수.
실행: python3 tools/test/runerules.py  (문제 0이어야 함)"""
import json, glob, os, collections
ROOT = '/home/claude/poe2data'
WARP = {"Serle's Triumph", "Cadigan's Epiphany", "Uhtred's Sidereus", "Kolr's Hunt", "Vorana's Carnage", "Thrud's Might", "Medved's Tending", "Katla's Gloom"}
ALDUR = {"Passion of Aldur", "Breath of Aldur", "Ire of Aldur", "Betrayal of Aldur"}
CORES = {"Atziri's Devotion", "Atziri's Vitality", "Atziri's Alacrity", "Atziri's Inoculation", "Raven-Touched Shard"}
LIMIT1 = WARP | CORES | {"Astrid's Creativity"}
NOSWAP = WARP | ALDUR | CORES          # 꺼낼 수도, 바꿀 수도 없음
nm = lambda x: (x.get('en') if isinstance(x, dict) else str(x).replace('rune:', '')).replace('’', "'").strip()
bad = []
R = json.load(open(f'{ROOT}/site/data/recipes.json'))['recipes']
for r in R:
    rs = [nm(x) for x in (r.get('start') or {}).get('runes') or []]
    for n in r['nodes']:
        t = n.get('target') or {}
        if t.get('rune'): rs.append(nm(t['rune']))
        if n.get('do') == 'socket' and str(n.get('cur', '')).startswith('rune:'): rs.append(nm(n['cur']))
        if t.get('runeSwap'):
            a, b = nm(t['runeSwap'][0]), nm(t['runeSwap'][1])
            if a in NOSWAP: bad.append(f"{r['id']} {n['id']}: {a}는 소켓 고정이라 {b}로 바꿀 수 없음")
            rs.append(b)
    if '' in rs: bad.append(f"{r['id']}: 이름 없는 룬 단계")
    for k, v in collections.Counter(x for x in rs if x).items():
        if v > 1 and k in LIMIT1: bad.append(f"{r['id']}: {k} {v}번 — 아이템당 하나")
    so = r.get('sockets')
    if isinstance(so, int) and len([x for x in rs if x]) > so: bad.append(f"{r['id']}: 룬 {len(rs)}개 > 소켓 {so}개")
for f in sorted(glob.glob(f'{ROOT}/scripts/graphs/*.json')):
    g = json.load(open(f)); gid = os.path.basename(f)[:-5]
    rs = [nm(x) for n in g['nodes'] if n.get('kind') == 'base' for x in (n.get('start') or {}).get('runes') or []]
    acts = [n for n in g['nodes'] if n.get('act') == 'rune']
    for n in acts:
        if not (n.get('rune') or {}).get('en'): bad.append(f"graph {gid} {n['id']}: 룬 상자에 rune 없음")
    names = rs + [nm(n['rune']) for n in acts if n.get('rune')]
    for k, v in collections.Counter(names).items():
        if v > 1 and k in LIMIT1: bad.append(f"graph {gid}: {k} {v}번 — 아이템당 하나(시작 룬과 장착 상자가 겹치면 하나만)")
for b in bad: print(b)
print('룬 규칙 문제', len(bad))
