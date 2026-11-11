"""그래프에 아스트리드의 창의성 장착 표시(`astrid: true`)를 넣음 — 정책 5장 C1 점검(tools/sim/c1check.js)용.
등급 레시피에 아스트리드의 창의성 단계가 있는데 그래프엔 룬 상자가 없는 경우, 시뮬이 제작 옵션 2개를 위반으로 세지 않게 함.
gen_batch*.py로 그래프를 다시 만든 뒤, build_recipes.py 다음에 실행: python3 scripts/graphs/patch_astrid.py"""
import json, glob, os
ROOT = '/home/claude/poe2data'
R = json.load(open(f'{ROOT}/site/data/recipes.json')); R = R['recipes'] if isinstance(R, dict) else R
has = set()
for r in R:
    if any('Astrid' in json.dumps(n.get('target', {})) for n in r['nodes']) or any('Astrid' in json.dumps(x) for x in (r.get('start') or {}).get('runes', [])):
        has.add(r.get('simId') or r.get('tierGroup') or r['id'])
n = 0
for f in sorted(glob.glob(f'{ROOT}/scripts/graphs/*.json')):
    g = json.load(open(f)); gid = os.path.basename(f)[:-5]
    node = any('Astrid' in json.dumps(x.get('rune', {})) for x in g['nodes'])
    want = gid in has and not node
    if bool(g.get('astrid')) != want:
        if want: g['astrid'] = True
        else: g.pop('astrid', None)
        json.dump(g, open(f, 'w'), ensure_ascii=False, indent=1); n += 1
print('astrid 표시 바뀐 그래프', n)
