# 시험용(2026-11-11): 아직 빌드에 연결하지 않음 — 136개 중 카드 일치가 절반 정도라 레시피를 바꾸지 않음
"""플로우차트(그래프) → 등급 레시피 단계 (사용자 확정 2026-11-11: 플로우차트 → 등급 카드 3장 → 그 등급 흐름을 따른 레시피)

build_recipes.py 끝에서 실행. 레시피마다 그 등급(버전)의 시뮬 결과에서 실제로 지나간 메인 단계를 위→아래로 따라가며
단계의 아이템 칸(item, 플로우차트 왼쪽 옵션 칸) 변화로 목표를 정하고, 실패선은 fail(goto·via)로 옮긴다.
레시피의 이름·출처·시작 퀄리티·룬·특출난 같은 정보는 원래 레시피 것을 그대로 둠. 단계 설명(br)은 같은 id 단계에만 옮김.

    gen(recipe, simfile, srcgraph) -> nodes 또는 None(만들 수 없음)
"""
import json, copy

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
    """성공 간선 조건에서 노리는 태그 모으기(added·has·count)"""
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


class G:
    def __init__(self, sim, src, params):
        self.g = sim['graph']; self.src = src or {}; self.params = params
        self.tags = self.g.get('tags') or {}
        self.srcn = {n['id']: n for n in (self.src.get('nodes') or [])}

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
        # 묶음 태그에 걸린 티어 제한은 하위 옵션에도
        if T.get('tmax') is not None:
            t = self.tmax(tag); out = [(gi, t if tm is None else min(tm, t) if t else tm) for gi, tm in out]
        return out

    def spec(self, tags):
        """여러 태그 → {gi,tmax} 또는 {anyOf:[...]}"""
        xs = []
        for t in tags:
            for gi, tm in self.leaves(self.name(t)):
                if gi not in [x['gi'] for x in xs]: xs.append({'gi': gi, **({'tmax': tm} if tm else {})})
        if not xs: return None
        return xs[0] if len(xs) == 1 else {'anyOf': xs}


def gen(r, sim, src):
    g = sim['graph']; tier = r.get('tier') or 'high'
    F = next((f for f in g.get('finals') or [] if (f.get('tier') or f['id']) == tier), None)
    V = F and next((v for v in g.get('versions') or [] if v['id'] == F['id']), None)
    S = next((x for x in sim.get('strategies', []) if not x.get('hidden') and V and all(str(x['params'].get(k)) == str(v) for k, v in V['params'].items())), None)
    if not S: return None
    G_ = G(sim, src, V['params']); res = S['res']; nodes = g['nodes']; byid = {n['id']: n for n in nodes}
    seen = lambda nid: (res['nodes'].get(nid) or {}).get('reach', 0) > 0
    base = next((n for n in nodes if n.get('kind') == 'base'), None)
    main = [n for n in nodes if n.get('kind') in ('act', 'cleanup') and n['pos'][0] == 0 and seen(n['id']) and n.get('group') != 'prep']
    mark = next((n for n in nodes if n.get('kind') == 'mark'), None)
    main.sort(key=lambda n: n['pos'][1])
    if not main: return None
    # 같은 id 단계의 분기 줄은 이어받음
    old = {n['id']: n for n in r.get('nodes') or []}
    out = [{'id': base['id'] if base else 'b0', 'phase': 'main', 'do': 'base', 'cost': 'base',
            **({'br': old[base['id']]['br']} if base and base['id'] in old and old[base['id']].get('br') else {})}]
    prev = (mark or base or {}).get('item') or []
    mainIds = [n['id'] for n in main]
    last_bone = None
    for n in main:
        sn = G_.srcn.get(n['id'], {})
        act = n.get('act') or ('remove' if n.get('kind') == 'cleanup' else None)
        cur = n.get('item') or prev
        new, gone = _diff(prev, cur)
        o = {'id': n['id'], 'phase': 'main', 'do': ACT.get(act, act)}
        if n.get('cur'): o['cur'] = n['cur']
        om = list(n.get('omens') or [])
        t = {}
        okc = []
        for e in sn.get('edges') or []:
            if e.get('res') == 'ok' and e.get('if'): okc = _cond_tags(e['if'], []); break
        okc = [G_.name(x) for x in okc if G_.name(x) in G_.tags]
        new = [l for l in new if l.get('s') in ('p', 's')]
        if act in ('chaos', 'exalt', 'transmute', 'augment', 'regal'):
            tagged = [l for l in new if l.get('tags')]
            if okc and not tagged:
                sp = G_.spec(okc)
                if sp: tagged = [{'tags': okc, 's': None}]
            junk = [l for l in new if l.get('m') == 'j' and not l.get('tags')]
            if tagged:
                tg = []
                for l in tagged: tg += l['tags']
                # 상자에 보이는 목표(show)가 더 넓으면 그쪽(여러 옵션 중 하나)
                show = [x for x in (n.get('show') or []) if isinstance(x, str)]
                sp = G_.spec(show) if show and len(tagged) == 1 else None
                sp = sp or G_.spec(tg)
                if len(tagged) > 1 and act == 'exalt':
                    parts = [G_.spec(l['tags']) for l in tagged]; t = {'all': [p for p in parts if p]}
                elif sp: t = dict(sp)
                if act == 'chaos':
                    rep = next((l.get('s') for l in gone if l.get('m') == 'j'), None)
                    if rep: t['replace'] = rep
                    if n.get('trim'):
                        sd = n['trim'].get('side') if isinstance(n['trim'], dict) else None
                        om = om or ['Omen_of_Whittling']
                    # 한 번에 여러 옵션이 생긴 반복 카오스 → 옵션마다 단계 하나
                    if len(tagged) > 1:
                        for k, l in enumerate(tagged):
                            sp1 = G_.spec(l['tags']) or {}
                            o2 = {**o, 'id': n['id'] if k == 0 else f"{n['id']}_{k+1}", 'target': {**sp1, **({'replace': rep} if rep else {})}, 'fail': {'goto': 'self'}}
                            if om: o2['omens'] = om
                            out.append(o2)
                        prev = cur; continue
            elif junk:
                sides = [l['s'] for l in junk]
                t = {'junk': sides if len(sides) > 1 else sides[0]}
            elif act == 'chaos':
                t = {'asIs': True, 'junk': next((l.get('s') for l in gone if l.get('s') in ('p','s')), 'p')}
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
            if sn.get('chance'): t['chance'] = sn['chance']
        elif act == 'desecrate':
            sd = _side_of_omens(om, 'Necromancy') or next((l.get('s') for l in new), None) or 'p'
            t = {'unrev': sd}
            if sn.get('fromMark') or (sn.get('target') or {}).get('fromMark'): t['fromMark'] = True
            last_bone = n.get('cur')
        elif act == 'reveal':
            want = sn.get('want') or (n.get('show') or [None])[0]
            wl = want if isinstance(want, list) else [want] if want else []
            wl = [G_.name(w) for w in wl] or okc
            nl = next((l for l in new if l.get('tags')), None)
            sp = G_.spec([w for w in wl if isinstance(w, str)]) or (nl and G_.spec(nl['tags']))
            sd = (nl or {}).get('s') or next((l.get('s') for l in gone), None) or 'p'
            t = {'reveal': sp or {'anyOf': []}, 'side': sd}
            if last_bone: t['bone'] = last_bone
            if not sp: t['asIs'] = True
        elif act in ('annul', 'cleanup'):
            if any(l.get('m') == 'd' or '훼손' in (l.get('kr') or '') for l in gone): t = {'removeDes': True}
            else:
                sd = _side_of_omens(om, 'Annulment') or (gone[0].get('s') if gone else None) or 'any'
                t = {'removeJunk': sd}
        elif act == 'quality':
            q = sn.get('q') or (r.get('start') or {}).get('quality') or 20
            t = {'quality': q}
        elif act == 'rune':
            rn = n.get('rune') or sn.get('rune')
            t = {'rune': rn if isinstance(rn, dict) else {'kr': rn or '', 'en': rn or ''}}
        if om: o['omens'] = om
        if t: o['target'] = t
        # 실패선: 자기 자신 / 옆 상자(소멸의 오브 등) 거쳐 메인 단계로
        fails = [e for e in n.get('edges') or [] if e.get('res') == 'fail' and (not e.get('when') or all(str(V['params'].get(k)) == str(v) for k, v in e['when'].items()))]
        for e in fails:
            to = e['to']
            if to == n['id']: o['fail'] = {'goto': 'self'}; break
            if to in mainIds: o['fail'] = {'goto': to}; break
            s1 = byid.get(to)
            if s1 and seen(to):
                back = next((x['to'] for x in s1.get('edges') or [] if x['to'] in mainIds), None)
                via = {'cur': s1['cur'], **({'omens': s1['omens']} if s1.get('omens') else {})} if s1.get('cur') else None
                if back:
                    o['fail'] = {'goto': 'self' if back == n['id'] else back, **({'via': via} if via else {})}; break
        if n['id'] in old and old[n['id']].get('br'): o['br'] = old[n['id']]['br']
        out.append(o); prev = cur
    out.append({'id': 'done', 'phase': 'main', 'do': 'note', 'note': {'kr': '완성.', 'en': 'Done.'}})
    return out


def start_of(r, sim, src):
    """시작 아이템 = 플로우차트 베이스 상자의 아이템(분열·잡옵·미공개 훼손)"""
    st = copy.deepcopy(r.get('start') or {})
    s0 = next((n for n in (src or {}).get('nodes') or [] if n.get('kind') == 'base'), None)
    if not s0 or not s0.get('start'): return st
    G_ = G(sim, src, {})
    mods = []
    for m in s0['start'].get('mods') or []:
        if 'tag' in m:
            sp = G_.spec([m['tag']]) or {}
            if 'gi' in sp: mods.append({'gi': sp['gi'], **({'tmax': sp['tmax']} if sp.get('tmax') else {}), **({'fr': True} if m.get('fr') else {}), **({'ess': True} if m.get('ess') else {})})
        elif 'junk' in m: mods.append({'junk': m['junk']})
        elif 'unrev' in m: mods.append({'unrev': m['unrev']})
    if mods: st['mods'] = mods
    if s0['start'].get('rar'): st['rar'] = s0['start']['rar']
    return st
