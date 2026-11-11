"""플로우차트 전수 검사(2026-11-11, 사용자: 등록된 플로우차트를 모두 검사해서 레시피가 제대로 뽑히는지).
python3 tools/test/fcaudit.py  → tools/test/fcaudit.txt
검사: ① 들어오는 선이 없는(모두 숨김) 상자 ② 숨긴 선으로 많이 가는 흐름 ③ 완성 조건(reqOk) ④ 등급별 비용·비싼 징조 반복이 비용 대부분인 상자
⑤ 등급 레시피가 플로우차트로 만들어졌는지(fcRead)·단계 수 ⑥ 그래프 설명에 '가정·단순화·정리본' 같은 말(영상과 다를 수 있음)"""
import json, glob, os, re
R = '/home/claude/poe2data'
pr = json.load(open(f'{R}/site/data/prices.json')); D = pr['divine']; P = pr['p']
price = lambda k: 0 if k == 'Exalted_Orb' else (P.get(k) or 0) / D
recipes = json.load(open(f'{R}/site/data/recipes.json'))['recipes']
out = []; summary = {}
for f in sorted(glob.glob(f'{R}/site/data/sim/*.json')):
    d = json.load(open(f)); gid = d['id']; g = d['graph']; nodes = {n['id']: n for n in g['nodes']}
    src = f'{R}/scripts/graphs/{gid}.json'; sg = json.load(open(src)) if os.path.exists(src) else {}
    vis = [s for s in d['strategies'] if not s.get('hidden')]
    probs = []
    inc = {}
    for n in g['nodes']:
        if n.get('next'): inc.setdefault(n['next'], []).append((n['id'], False))
        for e in n.get('edges') or []: inc.setdefault(e['to'], []).append((n['id'], bool(e.get('hide'))))
        for v, to in (n.get('options') or {}).items(): inc.setdefault(to, []).append((n['id'], False))
        if n.get('skipTo'): inc.setdefault(n['skipTo'], []).append((n['id'], True))
    reached = lambda nid: any((s['res']['nodes'].get(nid) or {}).get('visits', 0) > 0 for s in vis)
    for n in g['nodes']:
        if n['kind'] not in ('act', 'cleanup') or not reached(n['id']): continue
        ins = [x for x in inc.get(n['id'], []) if x[0] != n['id']]
        if ins and all(h for _, h in ins): probs.append(f"① 들어오는 선 없음: {n['id']} ({(n.get('goal') or n.get('label') or {}).get('kr','')}) ← 숨긴 선만 {','.join(sorted({a for a,_ in ins}))}")
        if not ins: probs.append(f"① 들어오는 선 없음: {n['id']} (아무 상자도 이리로 안 옴)")
    for s in vis:
        E = s['res'].get('edges') or {}
        for n in g['nodes']:
            outs = n.get('edges') or []; tot = sum(E.get(f"{n['id']}>{e['to']}", 0) for e in outs)
            if tot <= 0: continue
            for e in outs:
                c = E.get(f"{n['id']}>{e['to']}", 0)
                if e.get('hide') and e['to'] != n['id'] and c / tot >= 0.10 and nodes.get(e['to'], {}).get('kind') not in ('done',):
                    probs.append(f"② [{s['id']}] 숨긴 선으로 {c/tot:.0%}: {n['id']} → {e['to']}")
    costs = {}
    for s in vis:
        r = s['res']; m = r['mean']; costs[s['id']] = m
        if r.get('reqOk', 1) < 0.999: probs.append(f"③ [{s['id']}] 완성 조건 만족 {r['reqOk']:.1%}")
        for nid, t in (r.get('nodes') or {}).items():
            if m > 0 and t.get('div', 0) / m >= 0.4 and t.get('visits', 0) >= 3:
                ex = [k for k in (t.get('use') or {}) if price(k) >= 5]
                if ex: probs.append(f"④ [{s['id']}] {nid}이(가) 비용의 {t['div']/m:.0%} ({t['div']:.0f} div, {t['visits']:.0f}번, 비싼 커런시 {', '.join(ex)})")
    vers = {v['id']: v for v in g.get('versions') or []}
    gc = []
    for F in g.get('finals') or []:
        V = vers.get(F['id']); S = V and next((x for x in vis if all(str(x['params'].get(k)) == str(v) for k, v in V['params'].items())), None)
        gc.append((F.get('tier') or F['id'], round(S['res']['mean']) if S else None))
    for tr, c in gc:
        if c and c > 500: probs.append(f"④ [{tr}] 완성 1개당 평균 {c:,} div")
    note = sg.get('note') or ''
    kw = [w for w in ('가정', '단순화', '정리본', '요약판', '추정', '글 정리', '슬라이드만', '화면만') if w in note]
    if kw: probs.append(f"⑥ 그래프 설명에 '{', '.join(kw)}' — 영상과 맞춰 볼 것")
    rs = [r for r in recipes if (r.get('tierGroup') or r['id']) == gid]
    for r in rs:
        if not r.get('fcRead'): probs.append(f"⑤ {r['id']}: 플로우차트로 만든 레시피가 아님")
        elif len([n for n in r['nodes'] if n.get('do') not in ('base', 'note')]) < 1: probs.append(f"⑤ {r['id']}: 단계 없음")
    summary[gid] = {'grades': gc, 'n': len(probs)}
    out.append(f"## {gid}  등급 비용 {', '.join(f'{t} {c:,}' if c else f'{t} ?' for t,c in gc)}  문제 {len(probs)}")
    out += ['  ' + p for p in probs]
cnt = {}
for line in out:
    m = re.match(r'\s+([①②③④⑤⑥])', line)
    if m: cnt[m.group(1)] = cnt.get(m.group(1), 0) + 1
head = [f"플로우차트 {len(summary)}개 · 문제 있는 플로우차트 {sum(1 for v in summary.values() if v['n'])}개 · " + ' '.join(f'{k} {v}' for k, v in sorted(cnt.items()))]
open(f'{R}/tools/test/fcaudit.txt', 'w').write('\n'.join(head + out) + '\n')
print(head[0])
