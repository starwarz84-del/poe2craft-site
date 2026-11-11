# 등급 완성품 비교(2026-11-12, 정책 10장 C17-4): 플로우차트 finals의 옵션 줄이 같은 등급 쌍 → 낮은 등급을 뺄 후보
import json,glob,sys
out=[]
for f in sorted(glob.glob('/home/claude/poe2data/scripts/graphs/*.json')):
    g=json.load(open(f))
    if not isinstance(g,dict) or 'finals' not in g: continue
    F={x['id']:json.dumps(x.get('lines'),ensure_ascii=False,sort_keys=True) for x in g['finals']}
    ids=[x['id'] for x in g['finals']]
    for i in range(len(ids)):
        for j in range(i+1,len(ids)):
            if F[ids[i]]==F[ids[j]]: out.append(f"{g['id']}: {ids[i]} = {ids[j]}")
print('완성품 줄이 같은 등급 쌍', len(out))
for x in out: print(' ',x)
