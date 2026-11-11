"""플로우차트(그래프) → 등급 레시피 (사용자 확정 2026-11-11)

레시피 = 플로우차트를 그 등급 흐름대로 위에서 아래로 읽어 준 것. build_recipes.py가 플로우차트가 있는 등급 레시피마다 부름.

- 단계 = 그 등급(버전) 시뮬에서 실제로 지나간 작업 상자(준비 구역 제외). 오른쪽 열의 소멸 상자는 앞 단계의 '지우기'로 붙이고,
  오른쪽 열의 다른 작업(절사 반복, 대체 에센스 등)은 그 상자로 가는 단계 바로 아래 '실패 시' 묶음으로 둠.
- 확률·평균 개수·사용량·비용 = 그 등급 시뮬 값(fcs). 레시피 엔진은 목표 글과 시작 상태만 씀.
- 갈래(routes) = 상자에서 나가는 선(등급 조건 when·분기 choice를 그 등급 값으로 풀어서), 비율 = 시뮬에서 그 선을 지난 횟수.
- 등급이 갈리는 단계(grade) = 같은 상자를 다른 등급이 다르게 지나는 곳(목표 티어·갈래·커런시·안 거침).
- 단계 뒤 아이템(fst) = 상자의 아이템 칸(플로우차트 왼쪽 옵션 칸)을 그대로 옮김.

    read_recipe(recipe, simfile, srcgraph, tiers) -> {'nodes','phases','start','fcRead'} 또는 None
"""
import json, copy, re

ACT = {'annul': 'remove', 'rune': 'manual', 'cleanup': 'remove'}
SIDE_OMEN = {'Sinistral': 'p', 'Dextral': 's'}


def _key(l):
    return (l.get('s'), tuple(l.get('tags') or []) or l.get('kr'), l.get('m'))


def _diff(prev, cur):
    rest = list(cur); gone = []
    for l in prev:
        k = _key(l)
        j = next((i for i, x in enumerate(rest) if _key(x) == k), None)
        if j is None: gone.append(l)
        else: rest.pop(j)
    return rest, gone


def _side_of_omens(omens, word):
    for o in omens or []:
        for k, sd in SIDE_OMEN.items():
            if o.startswith(f'Omen_of_{k}_{word}'): return sd
    return None


def _cond_tags(c, out):
    if isinstance(c, dict):
        for k, v in c.items():
            if k == 'not': continue
            if k in ('added', 'has') and isinstance(v, str): out.append(v)
            elif k in ('added', 'has') and isinstance(v, dict) and isinstance(v.get('tag'), str): out.append(v['tag'])
            elif k == 'count' and isinstance(v, dict) and isinstance(v.get('tag'), str): out.append(v['tag'])
            else: _cond_tags(v, out)
    elif isinstance(c, list):
        for x in c: _cond_tags(x, out)
    return out


def _over(nodes, P):
    out = []
    for n in nodes:
        o = next((o for o in n.get('over') or [] if all(str(P.get(k)) == str(v) for k, v in (o.get('param') or {}).items())), None)
        out.append({**n, **o['set']} if o else n)
    return out


def _when(e, P):
    return all(str(P.get(k)) == str(v) for k, v in (e.get('when') or {}).items())


def _strip(lab):
    """플로우차트 선 이름의 상자 번호(→ 7) 떼기"""
    if not lab: return None
    return {k: re.sub(r'\s*→\s*[\dA-Z.]+$', '', v) for k, v in lab.items()}


class G:
    def __init__(self, sim, src, params):
        self.g = sim['graph']; self.src = src or {}; self.params = params
        self.tags = self.g.get('tags') or {}
        self.srcn = {n['id']: n for n in _over(self.src.get('nodes') or [], params)}

    def name(self, t):
        if isinstance(t, str) and t.startswith('$'): return self.params.get(t[1:], t)
        return t

    def tmax(self, tag, line_tmax=None):
        T = self.tags.get(tag) or {}
        v = line_tmax if line_tmax is not None else T.get('tmax')
        if isinstance(v, str) and v.startswith('$'): v = self.params.get(v[1:])
        try: return int(v) if v is not None else None
        except Exception: return None

    def leaves(self, tag, seen=()):
        tag = self.name(tag); T = self.tags.get(tag)
        if not T: return []
        if T.get('gi') is not None: return [(T['gi'], self.tmax(tag))]
        out = []
        for x in T.get('anyOf') or []:
            if isinstance(x, str) and x not in seen: out += self.leaves(x, seen + (tag,))
        if T.get('tmax') is not None:
            t = self.tmax(tag); out = [(gi, t if tm is None else min(tm, t) if t else tm) for gi, tm in out]
        return out

    def spec(self, tags):
        xs = []
        for t in tags:
            for gi, tm in self.leaves(self.name(t)):
                if gi not in [x['gi'] for x in xs]: xs.append({'gi': gi, **({'tmax': tm} if tm else {})})
        if not xs: return None
        return xs[0] if len(xs) == 1 else {'anyOf': xs}


def _target(G_, n, prev, cur, last_bone):
    """상자 하나 → 엔진 목표(목표 글에만 씀, 확률은 시뮬 값)"""
    sn = G_.srcn.get(n['id'], {})
    act = n.get('act') or ('remove' if n.get('kind') == 'cleanup' else None)
    new, gone = _diff(prev, cur)
    om = list(n.get('omens') or [])
    t = {}
    okc = []
    for e in sn.get('edges') or []:
        if e.get('res') == 'ok' and e.get('if'): okc = _cond_tags(e['if'], []); break
    okc = [G_.name(x) for x in okc if G_.name(x) in G_.tags]
    new = [l for l in new if l.get('s') in ('p', 's')]
    if act in ('chaos', 'exalt', 'transmute', 'augment', 'regal'):
        tagged = [l for l in new if l.get('tags')]
        if okc and not tagged and G_.spec(okc): tagged = [{'tags': okc, 's': None}]
        junk = [l for l in new if l.get('m') == 'j' and not l.get('tags')]
        if tagged:
            show = [x for x in (n.get('show') or []) if isinstance(x, str)]
            if len(tagged) > 1:
                parts = [G_.spec(l['tags']) for l in tagged]; t = {'all': [p for p in parts if p]}
            else:
                sp = (G_.spec(show) if show else None) or G_.spec(tagged[0]['tags'])
                if sp: t = dict(sp)
            if act == 'chaos':
                rep = next((l.get('s') for l in gone if l.get('m') == 'j'), None)
                if rep in ('p', 's') and 'all' not in t: t['replace'] = rep
                if n.get('trim') and not om: om = ['Omen_of_Whittling']
        elif junk:
            sides = [l['s'] for l in junk]
            t = {'junk': sides if len(sides) > 1 else sides[0]}
        elif act == 'chaos':
            t = {'asIs': True, 'junk': next((l.get('s') for l in gone if l.get('s') in ('p', 's')), 'p')}
        else:
            sd = _side_of_omens(om, 'Exaltation') or _side_of_omens(om, 'Coronation') or 'p'
            k = 2 if 'Omen_of_Greater_Exaltation' in om else 1
            t = {'junk': [sd] * k if k > 1 else sd}
    elif act == 'essence':
        nl = next((l for l in new if l.get('tags')), None)
        if nl: t = dict(G_.spec(nl['tags']) or {})
        elif okc: t = dict(G_.spec(okc) or {})
        mk = next((l for l in new if '징표' in (l.get('kr') or '')), None)
        if mk and not t: t = {'mark': {'gi': (G_.spec(mk.get('tags') or []) or {}).get('gi', 0)}}
    elif act == 'desecrate':
        sd = _side_of_omens(om, 'Necromancy') or next((l.get('s') for l in new), None) or 'p'
        t = {'unrev': sd}
        if sn.get('fromMark') or (sn.get('target') or {}).get('fromMark'): t['fromMark'] = True
        last_bone = n.get('cur') or last_bone
    elif act == 'reveal':
        want = sn.get('want') or n.get('want') or (n.get('show') or [None])[0]
        wl = want if isinstance(want, list) else [want] if want else []
        wl = [G_.name(w) for w in wl] or okc
        nl = next((l for l in new if l.get('tags')), None)
        sp = G_.spec([w for w in wl if isinstance(w, str)]) or (nl and G_.spec(nl['tags']))
        sd = (nl or {}).get('s') or next((l.get('s') for l in gone), None) or 'p'
        t = {'reveal': sp or {'anyOf': []}, 'side': sd}
        if last_bone: t['bone'] = last_bone
        if not sp: t['asIs'] = True
    elif act in ('annul', 'remove'):
        if any(l.get('m') in ('d', 'u') or '훼손' in (l.get('kr') or '') for l in gone): t = {'removeDes': True}
        else:
            sd = _side_of_omens(om, 'Annulment') or (gone[0].get('s') if gone and gone[0].get('s') in ('p', 's') else None) or 'any'
            t = {'removeJunk': sd}
    elif act == 'quality':
        t = {'quality': sn.get('q') or 20}
    elif act == 'rune':
        rn = n.get('rune') or sn.get('rune')
        t = {'rune': rn if isinstance(rn, dict) else {'kr': rn or '', 'en': rn or ''}}
    return act, om, t, last_bone


def _state(G_, lines, final_tags):
    """아이템 칸 → 엔진 상태(오른쪽 아이템 카드)"""
    out = []; cnt = {'p': 0, 's': 0}
    for l in lines:
        if l.get('s') == 'r': continue
        sd = l.get('s')
        if sd == 'x': sd = 'p' if cnt['p'] <= cnt['s'] else 's'
        if sd not in ('p', 's'): continue
        m = l.get('m'); tags = [G_.name(x) for x in (l.get('tags') or [])]
        if m == 'u': out.append({'unrev': True, 'junk': True, 'side': sd}); cnt[sd] += 1; continue
        tag = next((x for x in tags if x in final_tags), tags[0] if tags else None)
        lv = G_.leaves(tag) if tag else []
        if m == 'j' or not lv:
            out.append({'junk': True, 'side': sd, **({'des': True} if m == 'd' else {})}); cnt[sd] += 1; continue
        gi, tm = lv[0]
        e = {'gi': gi, 'side': sd}
        if tm: e['tmax'] = tm
        if m == 'f': e['fr'] = True
        if m == 'd': e['des'] = True
        if m == 'c': e['ess'] = True
        out.append(e); cnt[sd] += 1
    return out


def _version(sim, tier):
    g = sim['graph']
    F = next((f for f in g.get('finals') or [] if (f.get('tier') or f['id']) == tier), None)
    V = F and next((v for v in g.get('versions') or [] if v['id'] == F['id']), None)
    S = V and next((x for x in sim.get('strategies', []) if not x.get('hidden') and all(str(x['params'].get(k)) == str(v) for k, v in V['params'].items())), None)
    return F, V, S


class Walk:
    """한 등급(버전)으로 본 플로우차트: 상자, 나가는 선, 시뮬 값"""
    def __init__(self, sim, V, S):
        self.P = V['params']; self.res = S['res']
        self.nodes = _over(sim['graph']['nodes'], self.P)
        self.by = {n['id']: n for n in self.nodes}
        self.E = self.res.get('edges') or {}
        self.EI = self.res.get('edgesI') or {}   # 선마다 센 값(a#순번, 2026-11-11) — 같은 상자로 가는 성공·실패 선을 따로 셈

    def st(self, nid): return (self.res.get('nodes') or {}).get(nid)

    def seen(self, nid):
        t = self.st(nid); return bool(t) and (t.get('visits') or 0) > 0

    def via(self, nid):
        n = self.by.get(nid) or {}
        return n.get('pos', [0])[0] != 0 and (n.get('kind') == 'cleanup' or n.get('act') == 'annul')

    def outs(self, n):
        """나가는 선(등급 조건을 푼 것) → [(선, 도착 id, 선 이름, 결과, 시뮬 집계용 도착 id)]"""
        res = []
        for i, e in enumerate(n.get('edges') or []):
            if not _when(e, self.P): continue
            to = e['to']; lab = _strip(e.get('label')); cls = e.get('res')
            T = self.by.get(to)
            if T and T.get('kind') == 'choice':
                opt = str(self.P.get(T['param'])); to2 = (T.get('options') or {}).get(opt)
                if not to2: continue
                res.append((e, to2, (T.get('edgeLabels') or {}).get(opt) or lab, ((T.get('optStyle') or {}).get(opt) or {}).get('res') or cls, to, i))
                continue
            res.append((e, to, lab, cls, to, i))
        return res

    def cnt(self, a, b): return self.E.get(f'{a}>{b}', 0) or 0

    def ec(self, nid, x, outs):
        """선 하나(outs의 한 줄)를 지난 횟수. 선마다 센 값이 있으면 그것, 없으면 도착 상자 기준(같은 상자로 가는 선이 여럿이면 첫 선에만 — 두 번 세지 않음)"""
        if any(k.startswith(nid + '#') for k in self.EI): return self.EI.get(f'{nid}#{x[5]}', 0) or 0
        first = next(y for y in outs if y[4] == x[4])
        return self.cnt(nid, x[4]) if first is x else 0


def _routes(W, n, valid):
    """단계 칩: 성공·실패·되돌아감, 비율은 시뮬에서 그 선을 지난 횟수"""
    t = W.st(n['id']) or {}
    outs = W.outs(n); tot = sum(W.ec(n['id'], x, outs) for x in outs) or 1
    out = []
    def dest(to):
        T = W.by.get(to) or {}
        if to == n['id']: return 'self'
        if T.get('kind') in ('base', 'exit'): return 'restart'
        if T.get('kind') == 'done': return 'done'
        return to
    other = {'n': 0, 'share': 0}
    def ok_dest(d): return d in ('self', 'done', 'restart') or d in valid
    def hidden_many(es, frm):
        return len({x[1] for x in es if x[0].get('hide') and W.ec(frm, x, es) > 0 and x[1] != frm}) >= 2
    hm = hidden_many(outs, n['id'])
    for x0 in outs:
        e, to, lab, cls, raw = x0[:5]
        c = W.ec(n['id'], x0, outs)
        if c <= 0 and (e.get('hide') or len(outs) > 1): continue
        share = c / tot
        if hm and e.get('hide') and to != n['id']: other['n'] += c; other['share'] += share; continue
        if W.via(to):
            V = W.by[to]; vo = W.outs(V); vt = sum(W.ec(to, x, vo) for x in vo) or 1
            via = {'cur': V.get('cur') or 'Orb_of_Annulment', **({'omens': V['omens']} if V.get('omens') else {})}
            vhm = hidden_many(vo, to); vother = 0; k0 = len(out)
            for y0 in vo:
                e2, to2, lab2, cls2, raw2 = y0[:5]
                c2 = W.ec(to, y0, vo)
                if c2 <= 0 and len(vo) > 1: continue
                d2 = dest(to2)
                if (vhm and e2.get('hide')) or not ok_dest(d2): vother += c2; continue
                main = d2 == 'self' or cls2 != 'fail' or len(vo) == 1
                out.append({'cls': 'no' if (cls == 'fail' or not main) else 'ok', 'lab': lab2 or (lab if main else {'kr': '다른 옵션이 지워지면', 'en': 'Another mod removed'}),
                            'plab': bool(main and not lab2), 'vo': True,
                            'to': d2, 'via': via if main else None, 'share': share * (c2 / vt), 'n': round(c2, 3), 'lost': not main, 'res': cls})
            if vother > 0: out.append({'cls': 'no' if cls == 'fail' else 'ok', 'lab': lab, 'to': 'state', 'via': via, 'share': share * (vother / vt), 'res': cls})
            mine = out[k0:]
            if len(mine) > 1:
                top = max(mine, key=lambda x: x.get('n') or 0)
                for x in mine:
                    if x is not top: x['alt'] = True
            continue
        if not ok_dest(dest(to)): other['n'] += c; other['share'] += share; continue
        out.append({'cls': 'no' if cls == 'fail' else 'ok', 'lab': lab, 'to': dest(to), 'share': share, 'n': round(c, 3), 'res': cls})
    if other['share'] > 0: out.append({'cls': 'ok', 'lab': {'kr': '그 밖', 'en': 'Otherwise'}, 'to': 'state', 'share': other['share']})
    if n.get('skipTo') and (t.get('skips') or 0) > 0.001 and ok_dest(dest(n['skipTo'])):
        out.append({'cls': 'ok', 'lab': n.get('skipNote') or {'kr': '이미 있으면 건너뜀', 'en': 'Skip if already there'}, 'to': dest(n['skipTo']),
                    'share': t['skips'] / max(1e-9, t.get('visits') or 1), 'skip': True})
    m = {}
    for r in out:
        k = (r['cls'], r['to'], json.dumps(r.get('lab'), ensure_ascii=False), json.dumps(r.get('via')), r.get('lost'))
        if k in m: m[k]['share'] = (m[k]['share'] or 0) + (r['share'] or 0); m[k]['n'] = (m[k].get('n') or 0) + (r.get('n') or 0)
        else: m[k] = dict(r)
    rs = [r for r in m.values() if not ((r.get('lost') or r.get('skip') or r['cls'] == 'no' or r['to'] == 'state') and r['to'] != 'self' and (r['share'] or 0) < 0.005)]
    for r in rs: r['share'] = round(r['share'], 5)
    return [{k: v for k, v in r.items() if v not in (None, False)} for r in rs]


def _fcs(W, n):
    t = W.st(n['id']) or {}
    tries = (t.get('visits') or 0) - (0 if n.get('kind') == 'cleanup' else (t.get('skips') or 0))
    outs = W.outs(n)
    has_res = any(x[3] for x in outs)
    ok = [x for x in outs if x[3] == 'ok' and (n.get('pAll') or not x[0].get('dash'))]
    if has_res and not any(x[3] == 'ok' for x in outs): ok = [x for x in outs if not x[3] and x[1] != n['id']]   # 실패선만 표시된 상자: 나머지 선이 성공
    okc = sum(W.ec(n['id'], x, outs) for x in ok)
    if has_res and okc <= 0 and tries > 0:   # 상태마다 다른 단계로 보내는 상자: 표시된 성공선을 안 거치고 숨은 선으로 나아감 → 실패·반복이 아닌 선 모두
        okc = sum(W.ec(n['id'], x, outs) for x in outs if x[3] != 'fail' and x[1] != n['id'])
    p = min(1.0, okc / tries) if has_res and tries > 0 else 1.0
    rows = None
    if n.get('curRows') and t.get('byCur'):
        rows = []
        for rw in n['curRows']:
            b = t['byCur'].get(rw.get('key') or rw.get('cur'))
            ids = rw.get('ids') or [rw.get('cur')] + list(n.get('omens') or [])
            rows.append({'kr': rw['kr'], 'en': rw['en'], 'ids': ids, **({'p': round(b['ok'] / b['t'], 5)} if b and b.get('t') else {})})
    if p <= 0 and tries > 0: p = None   # 이 상자에서 바로 성공하는 일은 없고 결과에 따라 다음 상자로 갈림
    return {'p': round(p, 6) if p is not None else None, 'tries': round(tries, 4), 'use': {k: round(v, 4) for k, v in (t.get('use') or {}).items() if v >= 0.0005},
            'div': round(t.get('div') or 0, 4), 'reach': round(t.get('reach') or 0, 4), **({'rows': rows} if rows else {}), **({'once': True} if n.get('once') else {})}


def _miss(W, n):
    """등급을 가르는 갈래: 빗나갈 때 가는 선(1% 넘게 지나는 것)과 분기 상자를 거치는 선"""
    outs = W.outs(n); tot = sum(W.ec(n['id'], x, outs) for x in outs) or 1
    return [x for x in outs if (x[3] != 'ok' or x[4] != x[1]) and W.ec(n['id'], x, outs) / tot >= 0.01]


def _sig(W, n, G_):
    """등급 비교용: 이 상자를 이 등급은 어떻게 지나가나"""
    if not n or not W.seen(n['id']): return None
    tiers = []
    for t in (n.get('show') or []):
        for gi, tm in G_.leaves(G_.name(t)): tiers.append(tm or 0)
    fails = sorted({(json.dumps(x[2], ensure_ascii=False, sort_keys=True) if x[2] else '', x[1] if not W.via(x[1]) else 'via')
                    for x in _miss(W, n)})
    return {'tiers': tiers, 'fails': fails, 'cur': n.get('cur')}


def _grade_note(sim, src, nid, tiers):
    """같은 상자를 다른 등급이 다르게 지나면: [{tiers:[…], kr, en}, …]"""
    descs = []
    for tr in tiers:
        F, V, S = _version(sim, tr)
        if not S: continue
        W = Walk(sim, V, S); G_ = G(sim, src, V['params']); n = W.by.get(nid)
        descs.append((tr, W, G_, n, _sig(W, n, G_)))
    if len(descs) < 2: return None
    sigs = [json.dumps(d[4], sort_keys=True) for d in descs]
    if len(set(sigs)) < 2: return None
    live = [d for d in descs if d[4]]
    diff_t = len({json.dumps(d[4]['tiers']) for d in live}) > 1
    diff_f = len({json.dumps(d[4]['fails']) for d in live}) > 1
    diff_c = len({json.dumps(d[4]['cur']) for d in live}) > 1
    parts = []
    for tr, W, G_, n, s in descs:
        kr, en = [], []
        if not s: kr.append('이 단계 없음'); en.append('not used')
        else:
            if diff_t and s['tiers'] and max(s['tiers']):
                tm = max(s['tiers']); kr.append('1티어' if tm == 1 else f'1~{tm}티어'); en.append('T1' if tm == 1 else f'T1–{tm}')
            if diff_c and n.get('cur'): kr.append('@' + n['cur']); en.append('@' + n['cur'])
            if diff_f:
                fl = _miss(W, n)
                if not fl: kr.append('결과 그대로 다음'); en.append('keep the result')
                else:
                    e, to, lab, cls, raw = fl[0][:5]; T = W.by.get(to) or {}
                    if lab: kr.append('빗나가면 ' + lab['kr']); en.append('on a miss: ' + lab['en'].lower())
                    elif to == n['id']: kr.append('빗나가면 다시'); en.append('retry on a miss')
                    elif T.get('kind') == 'done': kr.append('빗나가도 그대로 완성'); en.append('finish as it is on a miss')
                    elif W.via(to): kr.append('빗나가면 지우고 다시'); en.append('remove and retry on a miss')
                    elif T.get('kind') in ('base', 'exit'): kr.append('빗나가면 처음부터'); en.append('start over on a miss')
                    elif T.get('cur'): kr.append(f"빗나가면 @{T['cur']}로"); en.append(f"on a miss: @{T['cur']}")
                    else: kr.append('빗나가면 다른 작업'); en.append('another step on a miss')
        if s and not kr: kr.append('이 단계 씀'); en.append('uses this step')
        parts.append({'tier': tr, 'kr': ', '.join(kr), 'en': ', '.join(en)})
    grp = []
    for p in parts:
        g = next((x for x in grp if x['kr'] == p['kr']), None)
        if g: g['tiers'].append(p['tier'])
        else: grp.append({'tiers': [p['tier']], 'kr': p['kr'], 'en': p['en']})
    return grp if len(grp) >= 2 else None


def read_recipe(r, sim, src, tiers):
    tier = r.get('tier') or 'high'
    F, V, S = _version(sim, tier)
    if not S: return None
    W = Walk(sim, V, S); G_ = G(sim, src, V['params'])
    final_tags = {G_.name(l['tag']) for l in F.get('lines') or [] if l.get('tag')}
    nodes = W.nodes
    base = next((n for n in nodes if n.get('kind') == 'base'), None)
    mark = next((n for n in nodes if n.get('kind') == 'mark'), None)
    work = [n for n in nodes if n.get('kind') in ('act', 'cleanup') and n.get('group') != 'prep' and W.seen(n['id']) and not W.via(n['id'])]
    main = sorted([n for n in work if n['pos'][0] == 0], key=lambda n: n['pos'][1])
    if not main: return None
    side = [n for n in work if n['pos'][0] != 0]
    parent = {}
    for s in side:
        for a in sorted(work, key=lambda n: (n['pos'][1], n['pos'][0])):
            if a is s: continue
            dests = set()
            for x in W.outs(a):
                dests.add(x[1])
                if W.via(x[1]): dests |= {y[1] for y in W.outs(W.by[x[1]])}
            if s['id'] in dests: parent[s['id']] = a['id']; break
    order = []; placed = set()
    def put(n):
        if n['id'] in placed: return
        order.append(n); placed.add(n['id'])
        for c in sorted([x for x in side if parent.get(x['id']) == n['id']], key=lambda x: (x['pos'][1], x['pos'][0])): put(c)
    for n in main: put(n)
    for s in sorted(side, key=lambda x: x['pos'][1]):
        if s['id'] not in placed:
            k = max([i for i, x in enumerate(order) if x['pos'][1] <= s['pos'][1]] or [len(order) - 1]); order.insert(k + 1, s); placed.add(s['id'])
            parent.setdefault(s['id'], order[k]['id'])
    loops = sim['graph'].get('loops') or []
    def loop_of(nid): return next((L for L in loops if nid in L['nodes']), None)
    old = {n['id']: n for n in r.get('nodes') or []}
    keep = lambda i: {k: old[i][k] for k in ('br', 'tips', 'ts') if i in old and old[i].get(k)}
    b0 = {'id': base['id'] if base else 'b0', 'phase': 'base', 'do': 'base', 'cost': 'base', **(keep(base['id']) if base else {})}
    ob = next((x for x in r.get('nodes') or [] if x.get('do') == 'base'), None)
    if ob:
        for k in ('note', 'br', 'tips', 'ts'):
            if ob.get(k): b0[k] = ob[k]
    out = [b0]
    phases = [{'id': 'base', 'kr': '베이스', 'en': 'Base'}]
    prev = (mark or base or {}).get('item') or []
    last_bone = None; cur_ph = None; ph_of = {}
    for n in order:
        cur = n.get('item') or prev
        pv = prev if n['pos'][0] == 0 or not parent.get(n['id']) else (W.by[parent[n['id']]].get('item') or prev)
        act, om, t, last_bone = _target(G_, n, pv, cur, last_bone)
        o = {'id': n['id'], 'do': ACT.get(act, act) or 'manual'}
        if n.get('cur'): o['cur'] = n['cur']
        elif o['do'] == 'remove': o['cur'] = 'Orb_of_Annulment'
        if om: o['omens'] = om
        if t: o['target'] = t
        if n.get('trim'): o['trimFc'] = n['trim'].get('side') if isinstance(n['trim'], dict) else 'p'
        o['fcs'] = _fcs(W, n)
        o['routes'] = _routes(W, n, placed)
        if not o.get('cur') and (n.get('goal') or n.get('label')): o['label'] = n.get('goal') or n.get('label')
        if not t and n.get('showText'): o['note'] = n['showText'][0]
        back = max([x for x in o['routes'] if x['cls'] == 'no' and x['to'] not in ('done', 'self', 'restart', 'state')], key=lambda x: x.get('share') or 0, default=None)
        back = back and back['to']
        if back: o['fail'] = {'goto': back}
        if parent.get(n['id']) and n['pos'][0] != 0: o['fallbackFor'] = parent[n['id']]
        o['fst'] = _state(G_, cur, final_tags)
        if n.get('goal') or n.get('label'): o['goal'] = n.get('goal') or n.get('label')
        if n.get('target') and isinstance(n['target'], dict) and 'kr' in n['target']: o['fcTarget'] = n['target']
        gn = _grade_note(sim, src, n['id'], tiers)
        if gn: o['grade'] = gn
        o.update(keep(n['id']))
        if o.get('fallbackFor'): o['phase'] = ph_of[o['fallbackFor']]
        else:
            L = loop_of(n['id'])
            key = ('L', L['id']) if L else ('g', json.dumps(n.get('goal') or n.get('label'), ensure_ascii=False))
            if key != cur_ph:
                cur_ph = key
                tl = L or n.get('goal') or n.get('label') or {'kr': '', 'en': ''}
                phases.append({'id': f'f{len(phases)}', 'kr': tl['kr'], 'en': tl['en']})
            o['phase'] = phases[-1]['id']
        ph_of[n['id']] = o['phase']
        out.append(o)
        if n['pos'][0] == 0: prev = cur
    last = (r.get('nodes') or [None])[-1]
    done_note = last.get('note') if last and last.get('do') == 'note' else None
    out.append({'id': 'done', 'phase': phases[-1]['id'], 'do': 'note', 'note': done_note or {'kr': '완성.', 'en': 'Done.'}})
    res = S['res']
    return {'nodes': out, 'phases': phases, 'start': start_of(r, sim, src),
            'fcRead': {k: res.get(k) for k in ('mean', 'median', 'p90', 'bases', 'baseDiv', 'use', 'useDiv')} | {'version': V['id']}}


def start_of(r, sim, src):
    """시작 아이템 = 플로우차트 베이스 상자의 아이템(분열·잡옵·미공개 훼손)"""
    st = copy.deepcopy(r.get('start') or {})
    s0 = next((n for n in (src or {}).get('nodes') or [] if n.get('kind') == 'base'), None)
    if not s0 or not s0.get('start'): return st
    G_ = G(sim, src, {})
    mods = []
    for m in s0['start'].get('mods') or []:
        if isinstance(m, str): m = {'tag': m}
        if 'tag' in m:
            sp = G_.spec([m['tag']]) or {}
            if 'gi' in sp: mods.append({'gi': sp['gi'], **({'tmax': sp['tmax']} if sp.get('tmax') else {}), **({'fr': True} if m.get('fr') else {}), **({'ess': True} if m.get('ess') else {})})
        elif 'junk' in m: mods.append({'junk': m['junk']})
        elif 'unrev' in m: mods.append({'unrev': m['unrev']})
    if mods: st['mods'] = mods
    if s0['start'].get('rar'): st['rar'] = s0['start']['rar']
    return st
