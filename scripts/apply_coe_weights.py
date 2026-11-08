"""raw/coe_weights_patch.json 의 가중치를 site/data/c/*.json 에 채워요(build_site_data.py 뒤에 실행).
채운 그룹에는 wsrc:'coe' 와 채운 티어 번호(wcoe)를 남겨 화면에 출처를 표시해요."""
import json, os
ROOT = '/home/claude/poe2data'
P = json.load(open(f'{ROOT}/raw/coe_weights_patch.json'))
n = 0
for cls, groups in P['fills'].items():
    fp = f'{ROOT}/site/data/c/{cls}.json'; D = json.load(open(fp))
    for gi, fills in groups.items():
        g = D['groups'][int(gi)]; done = []
        for ti, lvl, w in fills:
            if ti < len(g['t']) and g['t'][ti][0] == lvl and g['t'][ti][1] <= 1: g['t'][ti][1] = w; done.append(ti); n += 1
        if done: g['wsrc'] = 'coe'; g['wcoe'] = sorted(set(g.get('wcoe', []) + done))
    json.dump(D, open(fp, 'w'), ensure_ascii=False, separators=(',', ':'))
print('applied', n, 'tier weights from', P['source'])
