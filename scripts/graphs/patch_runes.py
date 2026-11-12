"""룬 상자에 rune 필드 채우기(2026-11-13): act:'rune' 상자에 rune이 없으면 goal 영문 'Socket <이름>'에서 읽어 넣음.
rune이 비면 완성 카드 R 줄이 비고, 룬 규칙 점검(tools/test/runerules.py)도 못 함. gen_*.py로 그래프를 다시 만든 뒤 build_recipes.py 앞에 실행."""
import json, glob, os, re
ROOT = '/home/claude/poe2data'
KR = {}
for f in glob.glob(f'{ROOT}/site/data/c/*.json'):
    try: C = json.load(open(f))
    except Exception: continue
    for x in C.get('runes') or []:
        for t in x.get('t') or []:
            if t and t[1]: KR[t[1].replace('’', "'")] = t[0]
n = 0
for f in sorted(glob.glob(f'{ROOT}/scripts/graphs/*.json')):
    g = json.load(open(f)); ch = False
    for nd in g.get('nodes', []):
        if nd.get('act') != 'rune' or (nd.get('rune') or {}).get('en'): continue
        m = re.match(r"Socket (.+?)(?: \(|$)", ((nd.get('goal') or {}).get('en') or '').replace('’', "'"))
        if m and m.group(1) in KR:
            nd['rune'] = {'kr': KR[m.group(1)], 'en': m.group(1)}; ch = True
    if ch: json.dump(g, open(f, 'w'), ensure_ascii=False, indent=1); n += 1
print('rune 필드 채운 그래프', n)
