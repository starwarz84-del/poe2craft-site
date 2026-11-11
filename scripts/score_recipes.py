"""레시피 점수 → docs/recipe-notes.md 의 자동 점수표(마커 사이)만 다시 씀. 손으로 쓴 노트는 그대로 둠.

사용자 확정 2026-11-11: 레시피를 만들면 레시피 노트를 항상 업데이트하고, 점수를 매겨 낮으면 이유를 분석해 해결책을 찾는다.

실행 순서(테스트 서버 필요):
  bash tools/test/serve.sh start
  node tools/test/_score.js            # 엔진 값 → tools/test/score_eng.json
  node tools/test/skipcheck.js > tools/test/skipcheck.txt
  python3 scripts/score_recipes.py     # → docs/recipe-notes.md 점수표

점수(100점, docs/policies.md 15장 — 2026-11-11 배점 고침):
  A 완성 조건 20   플로우차트 시뮬에서 완성품이 완성 조건을 만족한 비율(reqOk). 플로우차트 없으면 10
  B 가중치 15      가중치를 모르는 단계 하나마다 -5, 추정값(실측 없는 증강물 옵션)으로 계산한 단계 하나마다 -2
  C 실패 처리 10   확률 단계인데 실패했을 때 할 일이 없는 단계 하나마다 -5
  D 계산 일치 15   레시피 엔진 비용 ÷ 시뮬 평균(둘 다 옵션 추가 작업 구간, 베이스 값·준비 비용 제외, 1 div 아래는 같은 값): 1.5배 안 15 · 2.5배 10 · 4배 5 · 그 밖 0. 플로우차트 없으면 8
  E 등급 차이 5    같은 그룹의 다른 등급과 비용이 5% 넘게 다름(정책 10장). 등급이 하나면 5
  F 근거 10        영상·글 주소가 있음
  G 과정 10        skipcheck 문제 하나마다 -5
  H 정책 준수 10   제작 옵션 한도 위반(tools/sim/c1check.json) 단계 하나마다 -5
  I 비용 효율 5    리버스 초안(tools/test/revscore.json)이 같은 완성품을 20% 넘게 싸게 만들면 0
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
    'H': '제작 옵션이 있을 때 에센스·합금은 아스트리드의 창의성이 있어야 함(정책 5장) — 영상 재확인 뒤 순서 수정',
    'I': '리버스 초안의 방법을 낮은 등급에 반영할지 사용자에게 보고(정책 0장 3번)',
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
    if not s: return None
    grp = {n['id']: n.get('group') for n in d['graph']['nodes']}
    res = dict(s['res']); res['main'] = sum(n.get('div', 0) for k, n in s['res']['nodes'].items() if grp.get(k) != 'prep'); res['sid'] = s['id']; res['gid'] = sid
    return res


C1 = json.load(open(f'{ROOT}/tools/sim/c1check.json')) if os.path.exists(f'{ROOT}/tools/sim/c1check.json') else {}
REV = {x['id']: x for x in json.load(open(f'{ROOT}/tools/test/revscore.json'))} if os.path.exists(f'{ROOT}/tools/test/revscore.json') else {}
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
    gs = e.get('guess', [])
    pts['B'] = max(0, 15 - 5 * len(unk) - 2 * len(gs))
    if unk: why.append(f'B 가중치 모름 {len(unk)}단계')
    if gs: why.append(f'B 가중치 추정 {len(gs)}단계')
    nodes = {n['id']: n for n in r['nodes']}
    nf = [i for i in e.get('noFail', []) if not (nodes.get(i, {}).get('br') or nodes.get(i, {}).get('knownP'))]
    pts['C'] = max(0, 10 - 5 * len(nf))
    if nf: why.append(f'C 실패 처리 없음 {",".join(nf)}')
    em = e.get('main') if e.get('main') is not None else e.get('all')
    if res is None or em is None:
        pts['D'] = 8
    else:
        k = max(em, 1) / max(res['main'], 1); k = max(k, 1 / k)
        pts['D'] = 15 if k <= 1.5 else 10 if k <= 2.5 else 5 if k <= 4 else 0
        if pts['D'] < 15: why.append(f'D 엔진 {em:.0f} vs 시뮬 {res["main"]:.0f} div')
    g = groups[r.get('tierGroup') or r['id']]
    if len(g) > 1 and e.get('all') is not None:
        others = [ENG.get(x['id'], {}).get('all') for x in g if x['id'] != r['id']]
        same = [o for o in others if o is not None and abs(o - e['all']) <= 0.05 * max(o, e['all'], 0.01)]
        pts['E'] = 0 if same else 5
        if same: why.append('E 다른 등급과 비용이 같음')
    else:
        pts['E'] = 5
    pts['F'] = 10 if (r.get('source') or {}).get('url') else 0
    if not pts['F']: why.append('F 근거 주소 없음')
    nsk = len(re.findall(rf'^{re.escape(r["id"])}\b', SKIP, re.M))
    pts['G'] = max(0, 10 - 5 * nsk)
    if nsk: why.append(f'G skipcheck {nsk}건')
    c1 = {x['node'] for x in C1.get(res['gid'], []) if x['v'] == res['sid']} if res else set()
    pts['H'] = max(0, 10 - 5 * len(c1))
    if c1: why.append(f'H 제작 옵션 한도 위반 {",".join(sorted(c1))}')
    rv = REV.get(r['id']) or {}
    # 등록 레시피가 '결과 그대로' 받는 옵션이 있으면 리버스가 그만큼 쉬운 목표라 비교하지 않음
    fbk = {n.get('fallbackFor') for n in r['nodes'] if n.get('fallbackFor') and n.get('do') != 'note'}
    loose = any((n.get('target') or {}).get('asIs') or (n.get('target') or {}).get('anyReveal') or n.get('optional') or
                (n.get('do') in ('exalt', 'reveal', 'regal', 'transmute', 'augment', 'chaos') and not n.get('fail') and n['id'] not in fbk and not n.get('expect')
                 and any(k in (n.get('target') or {}) for k in ('gi', 'anyOf', 'reveal'))) for n in r['nodes'])
    cheaper = not loose and rv.get('k') is not None and rv['k'] < 0.8 and not (rv.get('pts') or {}).get('sim', 20) < 20 and (rv.get('pts') or {}).get('ver')
    pts['I'] = 0 if cheaper else 5
    if cheaper: why.append(f'I 리버스 초안이 더 쌈({rv["div"]:.0f} vs {rv["orig"]:.0f} div)')
    rows.append({'id': r['id'], 'tier': r.get('tier'), 'score': sum(pts.values()), 'why': why,
                 'cost': em, 'sim': res and res['main'], 'title': (r.get('title') or {}).get('kr', '')})

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
