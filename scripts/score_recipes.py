"""레시피 점수 → docs/recipe-notes.md 의 자동 점수표(마커 사이)만 다시 씀. 손으로 쓴 노트는 그대로 둠.

사용자 확정 2026-11-11: 레시피를 만들면 레시피 노트를 항상 업데이트하고, 점수를 매겨 낮으면 이유를 분석해 해결책을 찾는다.

실행 순서(테스트 서버 필요):
  bash tools/test/serve.sh start
  node tools/test/_score.js            # 엔진 값 → tools/test/score_eng.json
  node tools/test/skipcheck.js > tools/test/skipcheck.txt
  python3 scripts/score_recipes.py     # → docs/recipe-notes.md 점수표

점수(100점):
  A 완성 조건 20   플로우차트 시뮬에서 완성품이 완성 조건을 만족한 비율(reqOk). 플로우차트 없으면 10
  B 가중치 15      가중치를 모르는 단계 하나마다 -5
  C 실패 처리 15   확률 단계인데 실패했을 때 할 일이 없는 단계 하나마다 -5
  D 비용 일치 15   레시피 엔진 비용 ÷ 시뮬 평균: 1.5배 안 15 · 2.5배 10 · 4배 5 · 그 밖 0. 플로우차트 없으면 8
  E 등급 차이 10   같은 그룹의 다른 등급과 비용이 5% 넘게 다름(정책 32). 등급이 하나면 10
  F 근거 10        영상·글 주소가 있음
  G 과정 15        skipcheck 문제 하나마다 -5
"""
import json, os, re

ROOT = '/home/claude/poe2data'
R = json.load(open(f'{ROOT}/site/data/recipes.json'))
R = R['recipes'] if isinstance(R, dict) else R
ENG = json.load(open(f'{ROOT}/tools/test/score_eng.json'))
SKIP = open(f'{ROOT}/tools/test/skipcheck.txt').read() if os.path.exists(f'{ROOT}/tools/test/skipcheck.txt') else ''
NOTES = f'{ROOT}/docs/recipe-notes.md'
TIERK = {'high': '하이엔드', 'bal': '밸런스', 'ess': '에센셜', None: '-'}
FIX = {  # 감점 이유 → 먼저 해 볼 해결책
    'A': '시뮬 dbg.js로 완성 조건을 못 맞춘 아이템을 보고 그래프 간선(되돌아갈 곳)을 고침',
    'B': '가중치 근거 찾기(Craft of Exile·SL 실험·영상 시도 횟수) → patch 스크립트로 채움, 없으면 화면에 추정 표시',
    'C': '그 단계에 fail(다시)·compromise(타협)·br(분기 줄) 중 하나를 넣음',
    'D': '엔진과 시뮬 단계별 사용량 비교(engine.js·sim 파일 nodes) → 되돌아가기·손실 계산이 다른 단계 확인',
    'E': '정책 32: 루프로 찾는 옵션의 티어를 등급마다 넓힘(zzz-grade-tiers)',
    'F': '레시피 source에 영상·글 주소 넣기',
    'G': 'skipcheck.txt의 그 레시피 줄을 보고 빠진 단계 추가',
}


def sim_of(r):
    sid = r.get('simId') or (r.get('tierGroup') or r['id'])
    f = f'{ROOT}/site/data/sim/{sid}.json'
    if not os.path.exists(f):
        return None
    d = json.load(open(f))
    KT = {'하이엔드': 'high', '밸런스': 'bal', '에센셜': 'ess'}
    v = next((v for v in (d['graph'].get('versions') or []) if (v.get('tier') or KT.get(v.get('kr'))) == (r.get('tier') or 'high')), None)
    if not v:
        return None
    s = next((s for s in d['strategies'] if all(s['params'].get(k) == x for k, x in v['params'].items())), None)
    return s and s['res']


groups = {}
for r in R:
    groups.setdefault(r.get('tierGroup') or r['id'], []).append(r)

rows = []
for r in R:
    e = ENG.get(r['id'], {})
    pts, why = {}, []
    res = sim_of(r)
    if res is None:
        pts['A'] = 10; why.append('A 플로우차트 없음')
    else:
        ok = res.get('reqOk', 1)
        pts['A'] = round(20 * ok)
        if ok < 0.999: why.append(f'A 완성 조건 {ok:.0%}')
    unk = e.get('unk', [])
    pts['B'] = max(0, 15 - 5 * len(unk))
    if unk: why.append(f'B 가중치 모름 {len(unk)}단계')
    nodes = {n['id']: n for n in r['nodes']}
    nf = [i for i in e.get('noFail', []) if not (nodes.get(i, {}).get('br') or nodes.get(i, {}).get('knownP'))]
    pts['C'] = max(0, 15 - 5 * len(nf))
    if nf: why.append(f'C 실패 처리 없음 {",".join(nf)}')
    if res is None or not e.get('all'):
        pts['D'] = 8
    else:
        k = max(e['all'], 0.01) / max(res['mean'], 0.01); k = max(k, 1 / k)
        pts['D'] = 15 if k <= 1.5 else 10 if k <= 2.5 else 5 if k <= 4 else 0
        if pts['D'] < 15: why.append(f'D 엔진 {e["all"]:.0f} vs 시뮬 {res["mean"]:.0f} div')
    g = groups[r.get('tierGroup') or r['id']]
    if len(g) > 1 and e.get('all') is not None:
        others = [ENG.get(x['id'], {}).get('all') for x in g if x['id'] != r['id']]
        same = [o for o in others if o is not None and abs(o - e['all']) <= 0.05 * max(o, e['all'], 0.01)]
        pts['E'] = 0 if same else 10
        if same: why.append('E 다른 등급과 비용이 같음')
    else:
        pts['E'] = 10
    pts['F'] = 10 if (r.get('source') or {}).get('url') else 0
    if not pts['F']: why.append('F 근거 주소 없음')
    nsk = len(re.findall(rf'^{re.escape(r["id"])}\b', SKIP, re.M))
    pts['G'] = max(0, 15 - 5 * nsk)
    if nsk: why.append(f'G skipcheck {nsk}건')
    rows.append({'id': r['id'], 'tier': r.get('tier'), 'score': sum(pts.values()), 'why': why,
                 'cost': e.get('all'), 'sim': res and res['mean'], 'title': (r.get('title') or {}).get('kr', '')})

rows.sort(key=lambda x: (x['score'], x['id']))
avg = sum(x['score'] for x in rows) / len(rows)
low = [x for x in rows if x['score'] < 70]
out = [f'레시피 {len(rows)}개 · 평균 {avg:.1f}점 · 70점 미만 {len(low)}개 (갱신: `python3 scripts/score_recipes.py`)', '',
       '| 점수 | 레시피 | 등급 | 엔진 / 시뮬(div) | 감점 이유 |', '|---|---|---|---|---|']
fmt = lambda v: '-' if v is None else f'{v:,.0f}' if v >= 10 else f'{v:.1f}'
for x in rows:
    out.append(f'| {x["score"]} | `{x["id"]}` {x["title"]} | {TIERK.get(x["tier"], "-")} | {fmt(x["cost"])} / {fmt(x["sim"])} | {"; ".join(x["why"]) or "-"} |')
cnt = {}
for x in rows:
    for w in x['why']:
        cnt[w[0]] = cnt.get(w[0], 0) + 1
out += ['', '감점 종류별 레시피 수와 먼저 해 볼 해결책:', '']
out += [f'- **{k}** {v}개 — {FIX[k]}' for k, v in sorted(cnt.items(), key=lambda z: -z[1])]
auto = '\n'.join(out)

A, B = '<!-- 자동 점수표: 시작 -->', '<!-- 자동 점수표: 끝 -->'
doc = open(NOTES).read() if os.path.exists(NOTES) else f'# 레시피 노트\n\n## 점수표\n\n{A}\n{B}\n'
doc = doc[:doc.index(A) + len(A)] + '\n' + auto + '\n' + doc[doc.index(B):]
open(NOTES, 'w').write(doc)
print(f'{len(rows)} recipes, avg {avg:.1f}, <70: {len(low)}')
for k, v in sorted(cnt.items(), key=lambda z: -z[1]):
    print(' ', k, v)
