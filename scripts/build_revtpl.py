"""리버스 틀(W9, docs/reverse-pipeline.md 2-1): 등록 플로우차트를 리버스 초안 후보의 틀로 쓰게 사이트에 올림.

    python3 scripts/build_revtpl.py      (build_recipes.py 뒤 — recipes.json·site/data/sim/*.json을 읽음)

- site/data/revtpl.json : 그래프마다 클래스·베이스·등급별 시뮬 비용·완성 조건의 '꼭 있어야 하는 옵션 자리'(core)
- site/data/graphs/<id>.json : 그래프 본문(scripts/graphs/<id>.json 그대로). 화면은 틀로 쓸 때만 그 파일 하나를 받음

core = 완성 조건(require) 맨 위 all의 has·count 자리(등급 매개변수로 갈리는 any·full·desSide 등은 뺌).
자리마다 잎 옵션(gi), 쪽(p/s), 분류(n·d·e·x), 분열(fr)·훼손(des) 표시. 리버스(reverse.html tplMatch)가 붙여 넣은 필수 옵션과 짝지음.
"""
import json, os, glob

ROOT = '/home/claude/poe2data'
SITE = os.path.join(ROOT, 'site')
R = json.load(open(os.path.join(SITE, 'data', 'recipes.json'), encoding='utf-8'))
R = R.get('recipes', R) if isinstance(R, dict) else R
CLS = {}


def cls_groups(c):
    if c not in CLS:
        CLS[c] = json.load(open(os.path.join(SITE, 'data', 'c', c + '.json'), encoding='utf-8'))['groups']
    return CLS[c]


def leaves(g, G, name, seen=()):
    t = g['tags'].get(name)
    if t is None or name in seen:
        return []
    if 'anyOf' in t:
        out = []
        for x in t['anyOf']:
            if isinstance(x, str):
                out += leaves(g, G, x, seen + (name,))
            elif isinstance(x, dict) and x.get('gi') is not None:
                out.append(x['gi'])
        return out
    if t.get('gi') is not None:
        return [t['gi']]
    if t.get('fam'):
        for i, x in enumerate(G):
            if '+'.join(x['f']) == t['fam'] and (not t.get('sec') or x['s'] == t['sec']) and (not t.get('side') or x['g'] == t['side']):
                return [i]
    return []


def cond_true(c, P, conds):
    """등급 매개변수만으로 참인지(옵션 조건은 모름 → None)"""
    if 'param' in c:
        return all(str(P.get(k)) == str(v) for k, v in c['param'].items())
    if 'ref' in c:
        return cond_true(conds.get(c['ref'], {}), P, conds)
    if 'all' in c:
        r = [cond_true(x, P, conds) for x in c['all']]
        return False if False in r else (True if all(x is True for x in r) else None)
    if 'any' in c:
        r = [cond_true(x, P, conds) for x in c['any']]
        return True if True in r else (False if all(x is False for x in r) else None)
    return None


def slots_of(c, P, conds):
    """꼭 있어야 하는 옵션 자리 [(태그, 개수)]: all 안의 has·count, any는 등급 매개변수로 참인 갈래가 없을 때 옵션 갈래 하나(has·count·all)만"""
    out = []
    if 'ref' in c:
        return slots_of(conds.get(c['ref'], {}), P, conds)
    if 'has' in c:
        return [(c['has'], 1)]
    if 'count' in c:
        return [(c['count']['tag'], c['count'].get('min', 1))]
    if 'all' in c:
        for x in c['all']:
            out += slots_of(x, P, conds)
        return out
    if 'any' in c:
        if any(cond_true(x, P, conds) is True for x in c['any']):
            return []
        live = [x for x in c['any'] if cond_true(x, P, conds) is not False and 'param' not in x]
        if len(live) == 1:
            return slots_of(live[0], P, conds)
    return out


def merge_slots(core):
    """같은 옵션 자리를 두 번 세지 않게: 잎 옵션이 같은 자리는 개수 큰 쪽 하나, 한 자리의 잎이 다른 자리 잎에 다 들어가면 큰 자리 개수에서 작은 자리 개수를 뺌
    (예: has 16|18 + count 16|18|19 최소 2 → 16|18 하나 + 16|18|19 하나)"""
    by = {}
    for c in core:
        k = tuple(c['gis'])
        if k in by:
            by[k] = {**by[k], 'n': max(by[k]['n'], c['n']), **({'fr': 1} if c.get('fr') or by[k].get('fr') else {}), **({'des': 1} if c.get('des') and by[k].get('des') else {})}
            if not (c.get('des') and by[k].get('des')):
                by[k].pop('des', None)
        else:
            by[k] = dict(c)
    out = sorted(by.values(), key=lambda c: len(c['gis']))
    for i, a in enumerate(out):
        for b in out[i + 1:]:
            if set(a['gis']) < set(b['gis']):
                b['n'] = max(0, b['n'] - a['n'])
    return [c for c in out if c['n'] > 0]


def main():
    out_dir = os.path.join(SITE, 'data', 'graphs')
    os.makedirs(out_dir, exist_ok=True)
    for f in glob.glob(os.path.join(out_dir, '*.json')):
        os.remove(f)
    idx = {}
    skipped = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'scripts', 'graphs', '*.json'))):
        g = json.load(open(f, encoding='utf-8'))
        gid = g['id']
        simf = os.path.join(SITE, 'data', 'sim', gid + '.json')
        recs = [r for r in R if (r.get('simId') or r.get('tierGroup') or r['id']) == gid]
        if not os.path.exists(simf) or not recs:
            skipped.append(gid + ' (시뮬·레시피 없음)')
            continue
        try:
            G = cls_groups(g['cls'])
        except FileNotFoundError:
            skipped.append(gid + ' (클래스 파일 없음)')
            continue
        sim = json.load(open(simf, encoding='utf-8'))
        use = {s['id']: round(s['res'].get('useDiv', s['res'].get('mean', 0)), 3) for s in sim['strategies'] if s.get('res') and not s.get('hidden')}
        if not use:
            skipped.append(gid + ' (시뮬 결과 없음)')
            continue
        # 완성 카드 줄의 분열·훼손 표시(등급마다 같은 태그면 같음)
        fr, des = set(), set()
        for fin in g.get('finals') or []:
            for l in fin.get('lines', []):
                if l.get('tag') and l.get('fr'):
                    fr.add(l['tag'])
                if l.get('tag') and l.get('des'):
                    des.add(l['tag'])
        start = next((n for n in g['nodes'] if n['id'] == g.get('start')), None) or {}
        for m in (start.get('start') or {}).get('mods', []):
            if isinstance(m, dict) and m.get('fr') and m.get('tag'):
                fr.add(m['tag'])
        cores, extra, bad = {}, {}, None
        for st in g['strategies']:
            core = []
            for c in slots_of(g.get('require') or {}, st.get('params') or {}, g.get('conds') or {}):
                tag, n = c
                if isinstance(tag, str) and tag.startswith('$'):
                    tag = st['params'].get(tag[1:], tag)
                L = sorted(set(leaves(g, G, tag)))
                if not L:
                    bad = '잎 옵션 없는 태그 ' + str(tag)
                    break
                sides = sorted(set(G[i]['g'] for i in L))
                secs = sorted(set(G[i]['s'] for i in L))
                core.append({'t': tag, 'n': n, 'gis': L, 'side': sides[0] if len(sides) == 1 else 'x', 'sec': ''.join(secs),
                             **({'fr': 1} if tag in fr else {}), **({'des': 1} if tag in des or secs == ['d'] else {})})
            if bad:
                break
            core = merge_slots(core)
            if core:
                cores[st['id']] = core
                # 완성 카드에 늘 나오는 옵션 줄(완성 조건 밖): 붙여 넣은 필수 옵션이 core보다 많을 때 같은 옵션이면 짝지음(옵션은 못 바꿈)
                fin = next((f for f in g.get('finals') or [] if f.get('id') == st['id']), None)
                inc = {c['t'] for c in core}
                ex = []
                for l in (fin or {}).get('lines', []):
                    t = l.get('tag')
                    if not t or l.get('random') or t in inc:
                        continue
                    L = sorted(set(leaves(g, G, t)))
                    if L:
                        ex.append({'t': t, 'gis': L, **({'fr': 1} if l.get('fr') or t in fr else {}), **({'des': 1} if t in des or l.get('des') else {})})
                if ex:
                    extra[st['id']] = ex
        if bad or not cores:
            skipped.append(gid + ' (' + (bad or '완성 조건에 옵션 자리 없음') + ')')
            continue
        tiers = [r.get('tier') or 'high' for r in recs]
        lead = next((r for r in recs if r['id'] == g.get('recipe')), None) or recs[0]
        idx[gid] = {
            'g': gid, 'rid': lead['id'], 'recs': {(r.get('tier') or 'high'): r['id'] for r in recs},
            'cls': g['cls'], 'base': g.get('base'), 'ilvl': g.get('ilvl'),
            'diff': max(int(r.get('difficulty') or 0) for r in recs), 'ti': lead.get('title'),
            'use': use, 'grades': [s['id'] for s in g['strategies']], 'cores': cores, **({'extra': extra} if extra else {}),
            **({'astrid': 1} if g.get('astrid') is not None else {}), 'frg': sorted(set(i for t in fr for i in leaves(g, G, t))),
        }
        json.dump(g, open(os.path.join(out_dir, gid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump({'v': 1, 'g': idx}, open(os.path.join(SITE, 'data', 'revtpl.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('revtpl: 틀', len(idx), '개 · 뺀 것', len(skipped))
    for s in skipped:
        print('  -', s)


if __name__ == '__main__':
    main()
