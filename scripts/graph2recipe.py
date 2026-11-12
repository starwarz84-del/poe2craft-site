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
            if k in ('added', 'has', 'fractured') and isinstance(v, str): out.append(v)
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
    elif act == 'fracture':   # 분열 목표 = 이 단계 뒤 아이템 칸에서 새로 분열된 줄(없으면 성공 선 조건의 태그) — 준비 단계를 레시피에 넣으며 추가(2026-11-12)
        fl = [l for l in cur if l.get('m') == 'f' and l.get('tags')]
        nf = [l for l in fl if not any(_key(x) == _key(l) for x in prev)] or fl
        sp = (G_.spec(nf[0]['tags']) if nf else None) or (G_.spec(okc) if okc else None)
        if sp: t = dict(sp)
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


SIDE_W = {'p': ('접두', 'prefix'), 's': ('접미', 'suffix')}


def _clean_name(t):
    """아이템 칸 글 → 짧은 옵션 이름: 끝의 설명 괄호·수치 범위를 뗌"""
    t = re.sub(r'\s*\([^)]*[가-힣A-Za-z][^)]*\)\s*$', '', t or '')          # 끝의 '(분열)'·'(군왕의 합금)'
    t = re.sub(r'[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\)(\s*~\s*[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\))?%?', '', t)   # (16—24)~(28—42), +(4.41—5)%
    t = re.sub(r'\s+', ' ', t).strip(' +~')
    return t or None


class Cond:
    """갈래 조건 → 짧은 명사구(화면 문구 명사형). 라우터 선(상태마다 다음 단계를 고르는 선)을 사람이 읽을 수 있게(2026-11-12)"""
    def __init__(self, G_, sim, src, cls=None):
        self.G = G_; self.cls = cls; self._grp = None; self.conds = (src or {}).get('conds') or sim['graph'].get('conds') or {}
        self.nm = {}
        for n in sim['graph'].get('nodes') or []:
            for l in n.get('item') or []:
                tg = l.get('tags') or []
                if len(tg) == 1 and tg[0] not in self.nm:
                    k = _clean_name(l.get('kr')); e = _clean_name(l.get('en'))
                    if k: self.nm[G_.name(tg[0])] = (k, e or k)

    def name(self, tag):
        tag = self.G.name(tag) if isinstance(tag, str) else tag
        if isinstance(tag, dict):   # 조건 안에 바로 적은 옵션 {gi…}
            return None
        T = self.G.tags.get(tag) or {}
        if T.get('label'): return (T['label']['kr'], T['label']['en'])
        if tag in self.nm: return self.nm[tag]
        if T.get('gi') is not None and self.cls:   # 클래스 파일의 옵션 글(수치 뺀 것)
            if self._grp is None:
                try: self._grp = json.load(open(f'/home/claude/poe2data/site/data/c/{self.cls}.json'))['groups']
                except Exception: self._grp = []
            g = self._grp[T['gi']] if 0 <= T['gi'] < len(self._grp) else None
            if g and g.get('t'):
                k = _clean_name(g['t'][0][4]); e = _clean_name(g['t'][0][5])
                if k: return (k, e or k)
        subs = [x for x in T.get('anyOf') or [] if isinstance(x, str)]
        if 1 < len(subs) <= 2:
            ns = [self.name(x) for x in subs]
            if all(ns): return ('·'.join(x[0] for x in ns), ' or '.join(x[1] for x in ns))
        return None

    def atoms(self, c, neg=False):
        """[(키, kr, en, 종류)] — all은 펼침, 등급 param은 뺌. 모르는 조건은 빼고(None이면 이 선은 이 등급에서 안 지남)"""
        if c is None: return []
        if not isinstance(c, dict): return []
        if 'ref' in c: return self.atoms(self.conds.get(c['ref']), neg)
        if 'param' in c:
            ok = all(str(self.G.params.get(k)) == str(v) for k, v in c['param'].items())
            return [] if ok != neg else None
        if 'not' in c: return self.atoms(c['not'], not neg)
        if 'all' in c and not neg:
            out = []
            for x in c['all']:
                a = self.atoms(x)
                if a is None: return None
                out += a
            return out
        if 'any' in c and not neg:
            parts = []
            for x in c['any']:
                a = self.atoms(x)
                if a is None: continue
                if not a: return []
                parts.append(a)
            if not parts: return None
            if len(parts) > 3 or any(len(p) > 1 for p in parts): return []
            return [(('any',) + tuple(p[0][0] for p in parts), ' 또는 '.join(p[0][1] for p in parts), ' or '.join(p[0][2] for p in parts), 'any')]
        if ('all' in c or 'any' in c) and neg: return []
        k = next(iter(c)); v = c[k]
        S = lambda sd: SIDE_W.get(sd, ('', ''))
        def N(t):
            return self.name(t if not isinstance(t, dict) or 'tag' not in t else t['tag'])
        key = (k, json.dumps(v, sort_keys=True), neg)
        a = None
        if k == 'has':
            n_ = N(v); a = n_ and ((f'{n_[0]} 없음', f'no {n_[1]}', 'nohas') if neg else (f'{n_[0]} 있음', f'has {n_[1]}', 'has'))
        elif k == 'added':
            n_ = N(v); a = n_ and ((f'{n_[0]} 안 붙음', f'{n_[1]} not added', 'x') if neg else (f'{n_[0]} 붙음', f'{n_[1]} added', 'added'))
        elif k == 'removed':
            n_ = N(v); a = n_ and ((f'{n_[0]} 남음', f'{n_[1]} kept', 'x') if neg else (f'{n_[0]} 지워짐', f'{n_[1]} removed', 'x'))
        elif k == 'fractured':
            n_ = N(v); a = n_ and (('다른 옵션 분열', 'another mod fractured', 'x') if neg else (f'{n_[0]} 분열', f'{n_[1]} fractured', 'x'))
        elif k == 'full':
            s_ = S(v); a = (f'{s_[0]} 빈자리 있음', f'open {s_[1]}', 'x') if neg else (f'{s_[0]} 꽉 참', f'{s_[1]}es full', 'x')
        elif k == 'sideLt':
            s_ = S(v.get('side')); m = int(v.get('n') or 1)
            if neg: a = (f'{s_[0]} {m}개 이상', f'{m}+ {s_[1]}es', 'x')
            else: a = (f'{s_[0]} 없음', f'no {s_[1]}', 'x') if m <= 1 else (f'{s_[0]} {m - 1}개 이하', f'≤{m - 1} {s_[1]}es', 'x')
        elif k == 'count':
            n_ = N(v.get('tag')); m = v.get('min')
            if n_ and re.search(r' 1개$', n_[0]): n_ = (n_[0][:-3], re.sub(r'^(one|1) ', '', n_[1]))   # '저항 1개' 2개 → 저항 2개
            a = n_ and ((f'{n_[0]} {m}개 미만', f'fewer than {m} {n_[1]}', 'x') if neg else (f'{n_[0]} {m}개', f'{m}× {n_[1]}', 'has'))
        elif k == 'unrevSide':
            s_ = S(v); a = None if neg else (f'{s_[0]} 미공개 훼손', f'unrevealed {s_[1]}', 'x')
        elif k == 'unrev':
            yes = bool(v) != neg; a = ('미공개 훼손 있음', 'unrevealed desecration', 'x') if yes else ('미공개 훼손 없음', 'no unrevealed desecration', 'x')
        elif k == 'des':
            yes = bool(v) != neg; a = ('훼손 옵션 있음', 'desecrated mod', 'x') if yes else ('훼손 옵션 없음', 'no desecrated mod', 'x')
        elif k == 'desSide':
            s_ = S(v); a = (f'{s_[0]} 훼손 옵션 없음', f'no desecrated {s_[1]}', 'x') if neg else (f'{s_[0]} 훼손 옵션', f'desecrated {s_[1]}', 'x')
        elif k == 'sideAll':
            s_ = S(v.get('side')); n_ = N(v.get('tag'))
            if neg: a = (f'{s_[0]}에 잡옵', f'junk {s_[1]}', 'x')
            else: a = n_ and (f'{s_[0]} 모두 {n_[0]}', f'all {s_[1]}es {n_[1]}', 'x')
        elif k == 'junk':
            s_ = S(v.get('side')); a = (f'{s_[0]} 잡옵 없음', f'no junk {s_[1]}', 'x') if neg else (f'{s_[0]}에 잡옵', f'junk {s_[1]}', 'x')
        elif k == 'whittleSafe':
            a = ('가장 낮은 옵션이 지킬 옵션', 'lowest mod is a keeper', 'x') if neg else ('가장 낮은 옵션이 잡옵', 'lowest mod is junk', 'x')
        elif k == 'allMods':
            n_ = N(v); a = None if neg else n_ and (f'모두 {n_[0]}', f'all {n_[1]}', 'x')
        elif k == 'famBlock':
            a = None if neg else ('같은 계열 옵션이 막음', 'blocked by the same family', 'x')
        return [(key,) + a] if a else []


def _label(atoms, drop=()):
    """조건 조각 → 한 줄(최대 둘). 있음이 셋 이상이면 '목표 옵션 모두'"""
    if not atoms: return None
    xs = [a for a in atoms if a[0] not in drop] or list(atoms)
    hs = [a for a in atoms if a[3] == 'has']
    if len(hs) >= 3: return {'kr': '목표 옵션 모두 있음', 'en': 'all target mods'}
    seen = []; out = []
    for a in xs:
        if a[1] in seen: continue
        seen.append(a[1]); out.append(a)
    fullS = {a[1].split(' ')[0] for a in out if a[1].endswith(' 꽉 참')}
    out = [a for a in out if not (a[0][0] == 'sideLt' and a[1].split(' ')[0] in fullS)]   # '접미 꽉 참, 접미 3개 이하' → 꽉 참만
    out = out[:2]
    if len(out) == 2 and len(out[0][1]) + len(out[1][1]) > 26: out = out[:1]   # 길면 첫 조건만
    return {'kr': ', '.join(a[1] for a in out), 'en': ', '.join(a[2] for a in out)}


def _routes(W, n, valid, G_=None, CD=None):
    """단계 칩: 상자에서 나가는 선을 끝까지 따라가 실제 단계 번호로(지우기 상자·표시 상자는 건너뜀), 비율은 시뮬에서 그 선을 지난 횟수.
    라우터 선(아이템 상태마다 다음 단계를 고르는 숨은 선)은 '아이템 상태에 맞는 단계'로 묶지 않고 조건 글 + 단계 번호로(2026-11-12)"""
    t = W.st(n['id']) or {}
    def dest(to):
        T = W.by.get(to) or {}
        if to == n['id']: return 'self'
        if T.get('kind') in ('base', 'exit'): return 'restart'
        if T.get('kind') == 'done': return 'done'
        return to
    def ok_dest(d): return d in ('self', 'done', 'restart') or d in valid
    def src_if(nid, i, to):
        se = ((G_.srcn.get(nid) or {}).get('edges') or []) if G_ else []
        return se[i].get('if') if i < len(se) and se[i].get('to') == to else '?'
    def outs_of(N_):
        o = W.outs(N_)
        if o: return [(x, W.ec(N_['id'], x, o)) for x in o]
        nx = [(k.split('>', 1)[1], v) for k, v in W.E.items() if k.startswith(N_['id'] + '>')]
        if not nx and N_.get('next'): nx = [(N_['next'], 1)]
        return [(({'to': to}, to, None, None, to, -1), c) for to, c in nx]
    leaves = []
    def walk(N_, frac, first, chain, vias, depth, seen):
        os_ = outs_of(N_); tot = sum(c for _, c in os_)
        loop = sum(c for x, c in os_ if x[1] == N_['id'] and N_ is not n)   # 지우기 상자가 자기에게 돌아감 = 같은 오브를 한 번 더
        vis = [(x, c) for x, c in os_ if not (x[1] == N_['id'] and N_ is not n)]
        tv = sum(c for _, c in vis)
        if N_ is not n and loop > 0 and vias and tot / max(1e-9, tv) >= 1.05: vias[-1] = {**vias[-1], 'n': round(tot / max(1e-9, tv), 2)}
        for x, c in vis:
            if tv > 0 and c <= 0: continue
            if tv <= 0 and (x[0].get('hide') or len(vis) > 1): continue
            sh = frac * (c / tv if tv > 0 else 1.0)
            fx = first or (N_['id'], x); px = chain if N_ is n else chain + [(N_['id'], x)]
            to = x[1]; d = dest(to); T = W.by.get(to)
            if ok_dest(d) or not T or depth >= 5 or to in seen:
                leaves.append({'first': fx, 'chain': px, 'to': d if ok_dest(d) else 'state', 'share': sh,
                               'n': round(c, 3) if N_ is n else None, 'vias': list(vias), 'lab': x[2], 'cls': x[3]})
                continue
            nv = list(vias)
            if W.via(to): nv.append({'cur': T.get('cur') or 'Orb_of_Annulment', **({'omens': T['omens']} if T.get('omens') else {})})
            walk(T, sh, fx, px, nv, depth + 1, seen | {to})
    walk(n, 1.0, None, [], [], 0, {n['id']})
    multi = {}
    for L in leaves:
        if L['chain']: multi.setdefault(L['first'][1][5], set()).add(L['to'])
    # 숨은 선(라우터)은 결과 표시가 없거나 확률 계산용 'ok'라서, 같은 상자로 가는 보이는 선의 결과(성공·실패)를 따름
    vres = {}
    for x in W.outs(n):
        if not x[0].get('hide') and x[3]: vres.setdefault(x[4], x[3])
    ntot = sum(c for _, c in outs_of(n))
    out = []
    for L in leaves:
        e0 = L['first'][1]; cls0 = (vres.get(e0[4]) or e0[3]) if e0[0].get('hide') else e0[3]
        ch = L['chain']; post = ch[-1] if ch else None
        cls_post = post[1][3] if post else None
        lab_ch = next((y[1][2] for y in reversed(ch) if y[1][2]), None)
        main = L['to'] == 'self' or not post or cls_post != 'fail'
        needc = False
        if not post: lab = e0[2]
        elif L['to'] == 'self': lab = (e0[2] or lab_ch) if any(v.get('n') for v in L['vias']) else (lab_ch or e0[2])   # 지우기를 되풀이하는 상자: 이 단계 선 이름
        elif len(multi.get(e0[5]) or ()) >= 2: lab = lab_ch; needc = not lab   # 지운 뒤 갈 곳이 여럿: 무엇이 지워졌는지(지운 뒤 선의 조건)로 씀
        else: lab = (e0[2] or lab_ch) if any(v.get('n') for v in L['vias']) else (lab_ch or e0[2])
        no = cls0 == 'fail' or (post and not main) or L['to'] == 'self' or bool(lab and re.match(r'(빗나감|실패)', lab.get('kr') or ''))
        r = {'cls': 'no' if no else 'ok', 'lab': lab, 'to': L['to'], 'share': L['share'], 'n': round(L['share'] * ntot, 3), 'res': cls0 or cls_post}
        if needc: r['_c'] = True; r['_e0'] = e0[2]
        if L['vias']:
            v = dict(L['vias'][0])
            if len(L['vias']) > 1: v['then'] = L['vias'][1:]
            r['via'] = v; r['vo'] = True
        if post and not main: r['lost'] = True
        # 조건 글 재료: 이 단계 선의 조건, 지우기 뒤 선의 조건(지운 뒤 상태)
        if CD:
            a0 = CD.atoms(src_if(L['first'][0], L['first'][1][5], L['first'][1][4])) if L['first'][1][5] >= 0 else []
            r['_a'] = a0 or []
            if post:
                ap = CD.atoms(src_if(post[0], post[1][5], post[1][4])) if post[1][5] >= 0 else []
                ap = [a for a in (ap or []) if a[0] not in {b[0] for b in (a0 or [])}]
                # 같은 라우터 선 목록이고 지운 뒤 선이 앞 순번이면, 그 선이 지우기 전엔 맞지 않았음 = '없음'이 '지워짐'
                Pn = W.by.get(post[0]) or {}
                same = [e['to'] for e in n.get('edges') or []] == [e['to'] for e in Pn.get('edges') or []]
                if same and post[1][5] < L['first'][1][5]:
                    ap = [(a[0], a[1][:-3] + ' 지워짐', a[2].replace('no ', '', 1) + ' removed', 'x') if a[3] == 'nohas' else a for a in ap]
                r['_a'] = ap if needc else (a0 or [])
        out.append(r)
    # 같은 결과(종류·도착·지우기·글)는 합침 — 조건 재료는 많이 지난 쪽
    m = {}
    for r in sorted(out, key=lambda r: -r['share']):
        k = (r['cls'], r['to'], json.dumps(r.get('lab'), ensure_ascii=False), json.dumps(r.get('via'), sort_keys=True), r.get('lost'))
        if k in m: m[k]['share'] += r['share']; m[k]['n'] = (m[k].get('n') or 0) + (r.get('n') or 0)
        else: m[k] = dict(r)
    rs = list(m.values())
    # 아주 작은 갈래: 이 단계 반복(1% 미만)·실패(0.3% 미만)는 뺌, 1% 미만 실패가 둘 이상이면 '그 밖' 하나로.
    # 성공은 가장 큰 성공의 2% 미만이면 빼고 10% 미만은 같은 도착에 합치거나 '그 밖'으로
    rs = [r for r in rs if not (r['to'] == 'self' and r['share'] < 0.01 and len(rs) > 1)]
    rs = [r for r in rs if not (r['cls'] == 'no' and r['to'] != 'self' and r['share'] < 0.003)]
    def fold(tiny, cl):
        tiny.sort(key=lambda r: -r['share']); ds = []
        for r in tiny:
            if r['to'] not in ds: ds.append(r['to'])
        return {'cls': cl, 'lab': {'kr': '그 밖', 'en': 'Otherwise'}, 'to': ds[0], **({'toAlt': ds[1:4]} if len(ds) > 1 else {}), 'share': sum(r['share'] for r in tiny)}
    tiny = [r for r in rs if r['cls'] == 'no' and r['to'] != 'self' and r['share'] < 0.01]
    if len(tiny) >= 2: rs = [r for r in rs if r not in tiny] + [fold(tiny, 'no')]
    oks = [r for r in rs if r['cls'] == 'ok']
    mx = max([r['share'] for r in oks] or [0])
    if len(oks) > 1 and mx > 0:
        rs = [r for r in rs if not (r['cls'] == 'ok' and r['share'] < 0.02 * mx)]
        small = [r for r in rs if r['cls'] == 'ok' and r['share'] < 0.1 * mx]
        big = [r for r in rs if r['cls'] == 'ok' and r not in small]
        rest = []
        for r in small:
            same = next((b for b in big if b['to'] == r['to'] and json.dumps(b.get('via')) == json.dumps(r.get('via'))), None)
            if same: same['share'] += r['share']; same['n'] = (same.get('n') or 0) + (r.get('n') or 0)
            else: rest.append(r)
        rs = [r for r in rs if r not in small]
        if len(rest) == 1: rs.append(rest[0])
        elif rest: rs.append(fold(rest, 'ok'))
    # 같은 종류(성공·실패) 안에서 도착이 둘 이상이면 이름 없는 선에 조건 글, 지운 뒤 다른 단계로 가는 선은 늘 조건 글
    for cl in ('ok', 'no'):
        grp = [r for r in rs if r['cls'] == cl and r['to'] != 'self' and not r.get('skip')]
        many = len({(r['to'], bool(r.get('via'))) for r in grp}) >= 2
        need = [r for r in grp if not r.get('lab') and (many or r.get('_c'))]
        if not need: continue
        al = [set(a[0] for a in r.get('_a') or []) for r in grp if r.get('_a') and not r.get('_c')]
        common = set.intersection(*al) if len(al) >= 2 else set()
        hasres = any(r.get('res') for r in grp)
        # 조건 없는 선(마지막 '나머지' 선) 하나 + 조건 하나짜리 선 하나: 그 반대 글
        bare = [r for r in need if not r.get('_a') and not r.get('_c')]
        one = [r for r in grp if r not in bare and len(r.get('_a') or []) == 1 and r['_a'][0][3] in ('has', 'nohas')]
        if len(bare) == 1 and len(grp) == 2 and len(one) == 1:
            a = one[0]['_a'][0]
            bare[0]['_a'] = [(('neg',) + a[0], a[1][:-3] + (' 없음' if a[3] == 'has' else ' 있음'), ('no ' + a[2][4:]) if a[3] == 'has' else a[2][3:], 'x')]
        for r in need:
            lb = _label(r.get('_a'), () if r.get('_c') else common)
            if lb:
                pre = ('성공, ', 'Hit, ') if cl == 'ok' and hasres else ('실패, ', 'Miss, ') if cl == 'no' and hasres and not r.get('_c') else ('', '')
                r['lab'] = {'kr': pre[0] + lb['kr'], 'en': pre[1] + (lb['en'][:1].upper() + lb['en'][1:] if not pre[1] else lb['en'])}
            r['plab'] = False
    for r in rs:
        if r.get('lost') and not r.get('lab'): r['lab'] = {'kr': '다른 옵션이 지워지면', 'en': 'Another mod removed'}
        elif r.get('_c') and not r.get('lab'):
            if r.get('_e0') and r['to'] != 'self': r['lab'] = r['_e0']
            r['alt'] = True; r['plab'] = True   # 지운 뒤 앞 단계로: 화면이 '원하는 옵션이 지워지면 → n번으로'
    if n.get('skipTo') and (t.get('skips') or 0) > 0.001 and ok_dest(dest(n['skipTo'])) and t['skips'] / max(1e-9, t.get('visits') or 1) >= 0.005:
        rs.append({'cls': 'ok', 'lab': n.get('skipNote') or {'kr': '이미 있으면 건너뜀', 'en': 'Skip if already there'}, 'to': dest(n['skipTo']),
                   'share': t['skips'] / max(1e-9, t.get('visits') or 1), 'skip': True})
    # 순서: 성공(많은 것부터) → 실패(이 단계 반복 먼저) → 그 밖
    rs.sort(key=lambda r: (r['cls'] != 'ok', r.get('skip', False), (r.get('lab') or {}).get('kr') == '그 밖', r['to'] != 'self', -(r['share'] or 0)))
    for r in rs: r['share'] = round(r['share'], 5); r.pop('_a', None); r.pop('_c', None); r.pop('_e0', None)
    return [{k: v for k, v in r.items() if v is not None and v is not False} for r in rs]


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
    W = Walk(sim, V, S); G_ = G(sim, src, V['params']); CD = Cond(G_, sim, src, r.get('cls'))
    final_tags = {G_.name(l['tag']) for l in F.get('lines') or [] if l.get('tag')}
    nodes = W.nodes
    base = next((n for n in nodes if n.get('kind') == 'base'), None)
    mark = next((n for n in nodes if n.get('kind') == 'mark'), None)
    # 준비 구역에 작업 상자가 있는 그래프(노멀 베이스부터 분열까지 그림, 2026-11-12)는 그 단계도 레시피에 넣음 — 시뮬 합계가 이미 준비 비용을 셈
    own_prep = has_prep(sim)
    work = [n for n in nodes if n.get('kind') in ('act', 'cleanup') and (own_prep or n.get('group') != 'prep') and W.seen(n['id']) and not W.via(n['id'])]
    main = sorted([n for n in work if n['pos'][0] == 0], key=lambda n: n['pos'][1])
    if not main: return None
    side = [n for n in work if n['pos'][0] != 0]
    parent = {}
    def flow(a, sid):
        """a에서 sid로 가는 시뮬 통과 수(지우기 상자를 거치는 것 포함), 선이 있으면 최소 1e-9"""
        outs = W.outs(a); f = 0; hit = False; vis = False
        for x in outs:
            if x[1] == sid: hit = True; vis = vis or not x[0].get('hide'); f += W.ec(a['id'], x, outs)
            elif W.via(x[1]):
                V = W.by[x[1]]; vo = W.outs(V); vt = sum(W.ec(V['id'], y, vo) for y in vo) or 1
                for y in vo:
                    if y[1] == sid: hit = True; vis = vis or not (x[0].get('hide') or y[0].get('hide')); f += W.ec(a['id'], x, outs) * W.ec(V['id'], y, vo) / vt
        return (1 if vis else 0, f + 1e-9) if hit else 0
    for s in side:
        # 옆 단계의 부모 = 플로우차트에 그린 선(숨은 선 아님)으로 그 상자에 들어가는 작업 상자, 여럿이면 시뮬 통과 수가 많은 것 — 숨은 선 하나로 엉뚱한 단계 밑에 붙지 않게(2026-11-12)
        best = None; ks = (s['pos'][1], s['pos'][0])
        for early in (True, False):   # 위·왼쪽 상자 중에서 먼저 찾고(순서가 거꾸로 되지 않게), 없을 때만 나머지
            for a in sorted(work, key=lambda n: (n['pos'][1], n['pos'][0])):
                if a is s or (early and (a['pos'][1], a['pos'][0]) >= ks): continue
                f = flow(a, s['id'])
                if f and (best is None or f[0] > best[0][0] or (f[0] == best[0][0] and f[1] > best[0][1] * 1.000001)): best = (f, a['id'])
            if best: break
        if best: parent[s['id']] = best[1]
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
    # 준비 과정을 그린 그래프인데 옛 베이스 설명이 '분열해 둔 상태에서 시작'이면 플로우차트 베이스 상자 이름으로(2026-11-12)
    bst = ((base or {}).get('start') or {}) if own_prep else {}
    if own_prep and base and base.get('label') and '분열' in ((b0.get('note') or {}).get('kr') or '') and not any(isinstance(m, dict) and m.get('fr') for m in bst.get('mods') or []):
        b0['note'] = {'kr': base['label']['kr'] + '.', 'en': base['label']['en'] + '.'}
    out = [b0]
    phases = [{'id': 'base', 'kr': '베이스', 'en': 'Base'}]
    prev = ((base if own_prep else mark or base) or {}).get('item') or []
    groups = {x['id']: x for x in sim['graph'].get('groups') or []}
    last_bone = None; cur_ph = None; ph_of = {}
    for n in order:
        cur = n.get('item') or prev
        pv = prev if n['pos'][0] == 0 or not parent.get(n['id']) else (W.by[parent[n['id']]].get('item') or prev)
        act, om, t, last_bone = _target(G_, n, pv, cur, last_bone)
        o = {'id': n['id'], 'do': ACT.get(act, act) or 'manual'}
        if n.get('cur'): o['cur'] = n['cur']
        elif o['do'] == 'remove': o['cur'] = 'Orb_of_Annulment'
        if n.get('curIf') and o.get('cur'):   # 상태에 따라 오브가 바뀌는 상자: 그 등급 시뮬에서 가장 많이 쓴 오브(2026-11-12, 예: 하이엔드는 늘 완벽한 엑잘티드 오브)
            u = (W.st(n['id']) or {}).get('use') or {}
            cs = [o['cur']] + [c if isinstance(c, str) else c.get('cur') for c in n['curIf'] if (c if isinstance(c, str) else c.get('cur'))]
            top = max(cs, key=lambda c: u.get(c) or 0)
            if (u.get(top) or 0) > (u.get(o['cur']) or 0): o['cur'] = top
        if om: o['omens'] = om
        if t: o['target'] = t
        if n.get('trim'): o['trimFc'] = n['trim'].get('side') if isinstance(n['trim'], dict) else 'p'
        o['fcs'] = _fcs(W, n)
        o['routes'] = _routes(W, n, placed, G_, CD)
        if not o.get('cur') and (n.get('goal') or n.get('label')): o['label'] = n.get('goal') or n.get('label')
        if not t and n.get('showText'): o['note'] = n['showText'][0]
        back = max([x for x in o['routes'] if x['cls'] == 'no' and x['to'] not in ('done', 'self', 'restart', 'state')], key=lambda x: x.get('share') or 0, default=None)
        back = back and back['to']
        if back: o['fail'] = {'goto': back}
        if parent.get(n['id']) and n['pos'][0] != 0:
            pa = parent[n['id']]; po = next((x for x in out if x['id'] == pa), None)
            into = [x for x in (po or {}).get('routes') or [] if x.get('to') == n['id'] and not x.get('skip')]
            if po and po.get('fallbackFor') and into and all(x['cls'] == 'ok' for x in into):
                o['fallbackFor'] = po['fallbackFor']; o['chain'] = pa   # 옆 열 단계가 이어지는 것(앞 단계 성공 다음) — 앞 단계의 실패 묶음이 아님
                if po.get('alt'): o['alt'] = po['alt']
            else:
                o['fallbackFor'] = pa
                if into and all(x['cls'] == 'ok' for x in into):   # 실패가 아닌 다른 결과로 가는 옆 단계(예: 물리 피해 감소 없음 → 다른 공개)
                    o['alt'] = {'kr': (into[0].get('lab') or {}).get('kr') or '', 'en': (into[0].get('lab') or {}).get('en') or '', 'share': round(sum(x.get('share') or 0 for x in into), 5)}
        o['fst'] = _state(G_, cur, final_tags)
        if n.get('goal') or n.get('label'): o['goal'] = n.get('goal') or n.get('label')
        if n.get('target') and isinstance(n['target'], dict) and 'kr' in n['target']: o['fcTarget'] = n['target']
        gn = _grade_note(sim, src, n['id'], tiers)
        if gn: o['grade'] = gn
        o.update(keep(n['id']))
        if o.get('fallbackFor') and o['fallbackFor'] in ph_of: o['phase'] = ph_of[o['fallbackFor']]
        else:
            if o.get('fallbackFor'): o.pop('fallbackFor'); o.pop('chain', None); o.pop('alt', None)   # 부모가 아직 안 나온 옆 단계: 따로 단계로
            L = loop_of(n['id'])
            gp = own_prep and n.get('group') == 'prep'
            key = ('G', 'prep') if gp else ('L', L['id']) if L else ('g', json.dumps(n.get('goal') or n.get('label'), ensure_ascii=False))
            if key != cur_ph:
                cur_ph = key
                tl = (groups.get('prep') or {'kr': '베이스 준비', 'en': 'Base preparation'}) if gp else L or n.get('goal') or n.get('label') or {'kr': '', 'en': ''}
                phases.append({'id': f'f{len(phases)}', 'kr': tl['kr'], 'en': tl['en']})
            o['phase'] = phases[-1]['id']
        ph_of[n['id']] = o['phase']
        out.append(o)
        if n['pos'][0] == 0: prev = cur
    last = (r.get('nodes') or [None])[-1]
    done_note = last.get('note') if last and last.get('do') == 'note' else None
    out.append({'id': 'done', 'phase': phases[-1]['id'], 'do': 'note', 'note': done_note or {'kr': '완성.', 'en': 'Done.'}})
    res = S['res']
    return {'nodes': out, 'phases': phases, 'start': start_of(r, sim, src, V['params']),
            'fcRead': {k: res.get(k) for k in ('mean', 'median', 'p90', 'bases', 'baseDiv', 'use', 'useDiv')} | {'version': V['id']}}


def has_prep(sim):
    """준비 구역(group prep)에 작업 상자(act·cleanup)가 있는 그래프 — 노멀 베이스부터 준비 과정을 그림"""
    return any(n.get('group') == 'prep' and n.get('kind') in ('act', 'cleanup') for n in (sim.get('graph') or sim).get('nodes') or [])


def start_of(r, sim, src, params=None):
    """시작 아이템 = 플로우차트 베이스 상자의 아이템(분열·잡옵·미공개 훼손)"""
    st = copy.deepcopy(r.get('start') or {})
    s0 = next((n for n in (src or {}).get('nodes') or [] if n.get('kind') == 'base'), None)
    if has_prep(sim):   # 준비 과정을 그린 그래프: 레시피도 그 베이스(노멀)부터 — 옛 분열 시작 상태를 쓰지 않음
        b = (s0 or {}).get('start') or {}
        st = {'rar': b.get('rar') or 'normal', 'mods': []}
        q = b.get('quality') if b.get('quality') is not None else None
        if q: st['quality'] = q
        rn = b.get('runes') or (r.get('start') or {}).get('runes')
        if rn: st['runes'] = copy.deepcopy(rn)
        if not b.get('mods'): return st
    if not s0 or not s0.get('start'): return st
    G_ = G(sim, src, params or {})
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
