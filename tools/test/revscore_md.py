"""리버스 점수(tools/test/revscore.json, `node tools/test/_revscore.js`가 만듦) → docs/recipe-notes.md 의 리버스 점수표(마커 사이)만 다시 씀.
점수 기준은 docs/policies.md 15장."""
import json
ROOT = '/home/claude/poe2data'
d = json.load(open(f'{ROOT}/tools/test/revscore.json'))
d = [r for r in d if r.get('score') is not None]
rows = sorted(d, key=lambda r: (r['score'], r['id']))
f = lambda v: '-' if v is None else f'{v:,.0f}' if v >= 10 else f'{v:.1f}'
ks = sorted(r['k'] for r in d if r.get('k') is not None)
out = [f"초안 {len(d)}개 · 평균 {sum(r['score'] for r in d) / len(d):.1f}점 · 70점 미만 {sum(r['score'] < 70 for r in d)}개 · 비용 배수 중앙값 {ks[len(ks) // 2]} · 1.5배 안 {sum(k <= 1.5 for k in ks)}개 · 5배 넘음 {sum(k > 5 for k in ks)}개 · 시뮬 문제 {sum(r['pts']['sim'] < 20 for r in d)}개",
       '', '| 점수 | 등록 레시피 | 초안 / 등록(div) | 고른 후보 | 감점 이유 |', '|---|---|---|---|---|']
for r in rows:
    if r['score'] >= 90: continue
    out.append(f"| {r['score']} | `{r['id']}` | {f(r.get('div'))} / {f(r.get('orig'))} | {(r.get('pick') or {}).get('k', '-')} | {'; '.join(r['why']) or '-'} |")
out += ['', f"90점 이상 {sum(r['score'] >= 90 for r in d)}개는 표에서 뺐어요. 고른 후보: plain = 징조 없는 소멸의 오브, noloop = 절사·말소 반복 생략, flip = 면 순서 바꿈, gex = 상위 엑잘티드 오브."]
A, B = '<!-- 리버스 점수표: 시작 -->', '<!-- 리버스 점수표: 끝 -->'
p = f'{ROOT}/docs/recipe-notes.md'; s = open(p).read()
if A not in s:
    k = s.index('## 점수표'); s = s[:k] + f'## 리버스 점수표\n\n{A}\n{B}\n\n' + s[k:]
s = s[:s.index(A) + len(A)] + '\n' + '\n'.join(out) + '\n' + s[s.index(B):]
open(p, 'w').write(s); print(out[0])
