#!/usr/bin/env python3
"""플로우차트 완성품의 '고르는 줄'(label)이 DB 옵션(gi/anyOf 태그)에 연결됐는지 점검 — 정책 12장(사용자 확정 2026-11-12: 임의 명칭 금지).
build_recipes.py 뒤에 실행. 연결 안 된 줄을 레시피별로 보여 주고, 마지막 줄 '연결 안 된 줄 N'(0이어야 함)."""
import json, sys
R = json.load(open('/home/claude/poe2data/site/data/recipes.json'))['recipes']
bad = {}; tot = 0
for r in R:
    fc = r.get('fc')
    if not fc: continue
    for l in fc['lines']:
        if l.get('label') and not l.get('random'):
            tot += 1
            if not l.get('any'): bad.setdefault(r.get('tierGroup') or r['id'], set()).add(l['label']['kr'])
n = sum(len(v) for v in bad.values())
if '-q' not in sys.argv:
    for k, v in sorted(bad.items()): print(k, ' | '.join(sorted(v)))
print(f'고르는 줄 {tot} · 연결 안 된 줄 {n} (레시피 {len(bad)}개)')
