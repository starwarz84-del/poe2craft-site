"""플로우차트 점검: 나가는 선은 있는데 들어오는 선이 화면에 보이지 않는 상자(사용자 지적 2026-11-11).
python3 tools/test/fc_noinput.py  → 마지막 줄 '들어오는 선 없는 상자 n'. 0이어야 함.
안내 상자(kind side)와 시작 상자는 뺌. 선택 상자(options)와 등급별 덮어쓰기(over)로 이어지는 것은 보이는 선으로 셈."""
import json, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
tot = 0
for f in sorted(glob.glob(f'{ROOT}/scripts/graphs/*.json')):
    g = json.load(open(f)); N = {n['id']: n for n in g['nodes']}; vis = dict.fromkeys(N, 0); hid = dict.fromkeys(N, 0)
    for n in g['nodes']:
        es = ([{'to': n['next']}] if n.get('next') else []) + list(n.get('edges', []))
        for o in n.get('over', []): es += o.get('set', {}).get('edges', [])
        for o in n.get('options', []): es.append({'to': o.get('to')} if isinstance(o, dict) else {'to': o})
        for k in ('options', 'over'):
            for t in N:
                if t != n['id'] and json.dumps(n.get(k, '')).find('"' + t + '"') >= 0: vis[t] += 1
        for e in es:
            t = e.get('to')
            if t in N and t != n['id']: (hid if e.get('hide') else vis)[t] += 1
    bad = [k for k, n in N.items() if k != g['nodes'][0]['id'] and n.get('kind') not in ('base', 'side') and vis[k] == 0]
    if bad: tot += len(bad); print(g['id'], ', '.join(f"{k}({(N[k].get('goal') or {}).get('kr', '')} · 숨긴 선 {hid[k]})" for k in bad))
print('들어오는 선 없는 상자', tot)
