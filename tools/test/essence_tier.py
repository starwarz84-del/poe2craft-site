"""에센스 단계 점검 (2026-11-11, 사용자: 완벽한 무한의 에센스 옵션을 잘못 씀 — 에센스 옵션 다시 정리)
레시피(recipes.json)·그래프(scripts/graphs/*.json)의 에센스 단계가 노리는 옵션 그룹이
  ① 에센스 전용 그룹(s='e')이고 ② 완벽한 에센스면 'Perfect Essence' 그룹, 하위·일반·상위 에센스면 'Essence' 그룹인지 확인.
특수 에센스(심연·균열·히스테리아·섬망·공포·광기)는 'Perfect Essence' 그룹에 있어 예외, 합금·액체는 대상 아님.
실행: python3 tools/test/essence_tier.py  (문제 0이어야 함)"""
import json, glob, re, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
C = {}
def grp(cls, gi):
    if cls not in C: C[cls] = json.load(open(f'{B}/site/data/c/{cls}.json'))
    return C[cls]['groups'][gi]
SKIP = re.compile(r'Alloy|Liquid')
SPEC = re.compile(r'Abyss|Breach|Hysteria|Delirium|Horror|Insanity')
rows = []
for r in json.load(open(f'{B}/site/data/recipes.json'))['recipes']:
    for n in r.get('nodes', []) + (r.get('prep') or {}).get('nodes', []):
        t = n.get('target') or {}
        if n.get('do') == 'essence' and n.get('cur') and 'gi' in t and not SKIP.search(n['cur']):
            rows.append((r['id'], n['id'], n['cur'], grp(r['cls'], t['gi'])))
for f in glob.glob(f'{B}/scripts/graphs/*.json'):
    g = json.load(open(f))
    for n in g.get('nodes', []):
        if n.get('act') == 'essence' and n.get('cur') and n.get('ess') and not SKIP.search(n['cur']):
            t = g['tags'].get(n['ess'])
            if t and 'gi' in t: rows.append(('graph:' + g['id'], n['id'], n['cur'], grp(g['cls'], t['gi'])))
bad = [(a, b, c, g['sub'][1], g['t'][0][5].split('\n')[0]) for a, b, c, g in rows
       if g['s'] != 'e' or (not SPEC.search(c) and c.startswith('Perfect_') != ('Perfect' in g['sub'][1]))]
for x in bad: print(*x, sep=' | ')
print(f'{len(rows)} essence steps checked, {len(bad)} problem(s)')
