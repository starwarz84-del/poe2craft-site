"""_fcparity.js용 파이썬 기준값: 등록 그래프(scripts/graphs/*.json) × 완성 카드 등급마다 graph2recipe.read_recipe 결과를 JSON으로.
입력 레시피 = recipes.json의 그 등급 레시피(없으면 클래스·등급만 있는 빈 레시피). inherit는 True·False 둘 다.
    python3 tools/test/_fcparity_py.py <출력 파일> [그래프 id…]
"""
import json, os, sys, glob
ROOT = '/home/claude/poe2data'
sys.path.insert(0, ROOT + '/scripts')
import graph2recipe as g2r

def cases(only=None):
    R = json.load(open(ROOT + '/site/data/recipes.json'))['recipes']
    gids = sorted(os.path.basename(f)[:-5] for f in glob.glob(ROOT + '/scripts/graphs/*.json'))
    for gid in gids:
        if only and gid not in only: continue
        sf = f'{ROOT}/site/data/sim/{gid}.json'
        if not os.path.exists(sf): continue
        sim = json.load(open(sf)); src = json.load(open(f'{ROOT}/scripts/graphs/{gid}.json'))
        mine = [r for r in R if (r.get('tierGroup') or r.get('simId') or r['id']) == gid or r.get('simId') == gid]
        fin = [f.get('tier') or f['id'] for f in (sim['graph'].get('finals') or [])]
        tiers = [r.get('tier') or 'high' for r in mine] or fin
        for tr in fin:
            r = next((x for x in mine if (x.get('tier') or 'high') == tr), None)
            if r is None: r = {'id': f'{gid}-{tr}', 'tier': tr, 'cls': sim['graph'].get('cls') or src.get('cls'), 'nodes': [], 'start': {}}
            yield gid, tr, r, sim, src, tiers

def main():
    out = sys.argv[1]; only = set(sys.argv[2:]) or None
    res = {}
    for gid, tr, r, sim, src, tiers in cases(only):
        for inh in (True, False):
            k = f'{gid}|{tr}|{int(inh)}'
            try: res[k] = {'r': r['id'], 'tiers': tiers, 'out': g2r.read_recipe(json.loads(json.dumps(r)), sim, src, tiers, inherit=inh)}
            except Exception as e: res[k] = {'r': r['id'], 'tiers': tiers, 'err': f'{type(e).__name__}: {e}'}
    json.dump(res, open(out, 'w'), ensure_ascii=False)
    print(len(res), 'cases →', out)

if __name__ == '__main__': main()
