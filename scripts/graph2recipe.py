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
            elif isinstance(x, dict) and x.get('gi') is not None: out.append((x['gi'], self.tmax(None, x['tmax']) if x.get('tmax') is not None else None))   # '$pT' 같은 등급 파라미터도 풂(2026-11-13 S3 1번: 레시피에 '$pT'가 남아 엔진 확률 0)   # 태그 안에 바로 적은 옵션 {gi} — 이름표 태그(label) 공개 목표가 비던 것(2026-11-13 S2: MazBro 시전자 목걸이 a8, Unstoppable q1)
        if T.get('tmax') is not None:
            t = self.tmax(tag); out = [(gi, t if tm is None else min(tm, t) if t else tm) for gi, tm in out]
        return out

    def spec(self, tags):
        xs = []
        for t in tags:
            for gi, tm in self.leaves(self.name(t)):
                if gi not in [x['gi'] for x in xs]: xs.append({'gi': gi, **({'tmax': tm} if tm else {})})
        if not xs: return None
        if len(xs) == 1: return xs[0]
        out = {'anyOf': xs}
        lb = [self.tags.get(self.name(t), {}).get('label') for t in tags]
        if len(tags) == 1 and isinstance(lb[0], dict) and lb[0].get('kr'): out['label'] = {'kr': lb[0]['kr'], 'en': lb[0].get('en') or lb[0]['kr']}   # 묶음 이름(티어 상관없는 긴 목록은 이름으로, 2026-11-13 S3 27번)
        return out


def _room(G_, prev):
    """앞 아이템 칸에서 아직 자리가 있는 쪽(그래프 cap, 없으면 3/3) — 한쪽이 꽉 차면 '접두·접미 무관'이 아니라 남은 쪽(2026-11-13 S3 2·13번)"""
    cap = G_.g.get('cap') or (G_.src or {}).get('cap') or {}
    n = {'p': 0, 's': 0}
    for l in prev or []:
        if l.get('s') in n: n[l['s']] += 1
    return [sd for sd in ('p', 's') if n[sd] < (cap.get(sd) or 3)]


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
    # 이 등급에선 늘 맞는 성공 선(param만, 예: 에센셜 '나오는 대로')이 있으면 목표 옵션 없이 '아무 옵션'(2026-11-13 S2, G5 보고)
    keep_any = any(e.get('res') == 'ok' and e.get('if') is not None and _simp(e['if'], G_.params) is True for e in sn.get('edges') or []) or getattr(G_, '_kall', False)
    if keep_any and act in ('chaos', 'exalt', 'transmute', 'augment', 'regal'):
        rm = _room(G_, prev)
        sd = next((l.get('s') for l in new), None) or _side_of_omens(om, 'Exaltation') or _side_of_omens(om, 'Coronation') or (rm[0] if len(rm) == 1 else 'p')
        k = 2 if act == 'exalt' and 'Omen_of_Greater_Exaltation' in om else 1   # 상위 찬미 = 옵션 2개(2026-11-13 S3 30번: '아무 옵션 1개'로 나오던 것)
        if k > 1:
            ns = [l.get('s') for l in new if l.get('s') in ('p', 's')]
            t = {'junk': ns if len(ns) == k else [sd] * k}
            if not (_side_of_omens(om, 'Exaltation') or _side_of_omens(om, 'Coronation')) and len(rm) > 1: t['anySide'] = True
        else:
            t = {'junk': sd} if act != 'chaos' else {'asIs': True, 'junk': sd}
        return act, om, t, last_bone
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
        elif junk and n['pos'][0] != 0 and [x for x in (n.get('show') or []) if isinstance(x, str)] and G_.spec([x for x in n['show'] if isinstance(x, str)]):
            t = dict(G_.spec([x for x in n['show'] if isinstance(x, str)]))   # 옆 상자가 잡옵 자리를 채우지만 플로우차트에 고르는 옵션(show)을 적었으면 그 옵션이 목표 — 시한 투구 밸런스 '빈 접미 엑잘'(2026-11-12)
        elif junk:
            sides = [l['s'] for l in junk]
            t = {'junk': sides if len(sides) > 1 else sides[0]}
            if len(sides) > 1 and not (_side_of_omens(om, 'Exaltation') or _side_of_omens(om, 'Coronation')) and len(_room(G_, prev)) > 1: t['anySide'] = True   # 징조 없이 여러 개: 앞 결과에 따라 쪽이 달라짐 — '(접두 2)'로 단정하지 않음(2026-11-13 S2, G10 보고)
        elif act == 'chaos':
            t = {'asIs': True, 'junk': next((l.get('s') for l in gone if l.get('s') in ('p', 's')), 'p')}
        else:
            rm = _room(G_, prev)
            # 쪽: 징조 → 새로 붙은 줄의 쪽(태그 없는 일반 줄 m='n'도) → 남은 쪽이 하나면 그쪽 → 접두 — 접미 엑잘이 '(접두)'로 나오던 것(2026-11-13 S3 12번)
            sd = _side_of_omens(om, 'Exaltation') or _side_of_omens(om, 'Coronation') or next((l.get('s') for l in new if l.get('s') in ('p', 's')), None) or (rm[0] if len(rm) == 1 else 'p')
            k = 2 if 'Omen_of_Greater_Exaltation' in om else 1
            if k > 1 and not (_side_of_omens(om, 'Exaltation') or _side_of_omens(om, 'Coronation')):
                ns = [l.get('s') for l in new if l.get('s') in ('p', 's')]
                t = {'junk': ns if len(ns) == k else [sd] * k}
                if len(rm) > 1: t['anySide'] = True
            else:
                t = {'junk': [sd] * k if k > 1 else sd}
    elif act == 'essence':
        nl = next((l for l in new if l.get('tags')), None)
        if nl: t = dict(G_.spec(nl['tags']) or {})
        elif okc: t = dict(G_.spec(okc) or {})
        mk = next((l for l in new if '징표' in (l.get('kr') or '')), None)
        if mk and not t:   # 징표 줄에 태그가 없으면 gi 0(엉뚱한 '힘 +…')이 되던 것 — 태그로 옵션을 알 때만 징표 목표, 아니면 줄 글을 목표 글로(2026-11-13 S2, G2 보고)
            mg = (G_.spec(mk.get('tags') or []) or {}).get('gi')
            if mg is not None: t = {'mark': {'gi': mg}}
            else: G_._marktx = {'kr': mk.get('kr') or '', 'en': mk.get('en') or mk.get('kr') or ''}
    elif act == 'desecrate':
        sd = _side_of_omens(om, 'Necromancy') or next((l.get('s') for l in new), None) or next((l.get('s') for l in n.get('showText') or [] if l.get('s') in ('p', 's')), None) or 'p'
        G_._lus = sd   # 다음 공개 상자의 쪽(접힌 상자는 아이템 칸이 없어 공개 쪽을 못 읽음, 2026-11-13 S1)
        t = {'unrev': sd}
        if sn.get('fromMark') or (sn.get('target') or {}).get('fromMark'): t['fromMark'] = True
        last_bone = n.get('cur') or last_bone
    elif act == 'reveal':
        want = sn.get('want') or n.get('want') or (n.get('show') or [None])[0]
        if isinstance(n.get('show'), list) and not n['show'] and 'show' in (sn or {}) and not sn['show']: want = None   # 등급이 show를 비움(over) = 공개 결과 그대로 — 에센셜에 want가 목표처럼 나오던 것(2026-11-13 S2, G1 보고)
        wl = want if isinstance(want, list) else [want] if want else []
        wl = [G_.name(w) for w in wl] or ([] if want is None and isinstance(n.get('show'), list) and not n['show'] else okc)
        nl = next((l for l in new if l.get('tags')), None)
        asis_v = (want is None and isinstance(n.get('show'), list) and not n['show']) or keep_any
        if keep_any: wl = []
        sp = G_.spec([w for w in wl if isinstance(w, str)]) or (None if asis_v else (nl and G_.spec(nl['tags'])))
        # 공개 쪽: 새로 공개된 줄 → 바로 앞 훼손 상자의 쪽 → 고르는 옵션의 쪽 → 지워진 줄 — 접힌 상자(아이템 칸 없음)가 늘 접두로 나오던 것(2026-11-13 S1: MazBro 시전자 목걸이 a8)
        ws = next((T.get('s') for w in wl if isinstance(w, str) for gi, _ in G_.leaves(w) for T in G_.tags.values() if isinstance(T, dict) and T.get('gi') == gi and T.get('s') in ('p', 's')), None)
        sd = (nl or {}).get('s') or getattr(G_, '_lus', None) or ws or next((l.get('s') for l in gone), None) or 'p'
        t = {'reveal': sp or {'anyOf': []}, 'side': sd}
        if last_bone: t['bone'] = last_bone
        if not sp:   # 고르는 옵션을 태그로 적지 않은 공개(가장 높은 레벨 옵션·아무거나): 상자 글을 목표 글로 — '선택지 3개 중:'으로 끝나던 것(2026-11-13 S2)
            t['asIs'] = True; t['anyReveal'] = True   # 엔진(engine.js)도 확정 공개로 셈 — 빈 목표로 멈추던 것
            tx_ = next((x for x in (n.get('showText') or sn.get('showText') or []) if isinstance(x, dict) and x.get('kr')), None) or n.get('goal') or sn.get('goal')
            # 결과 그대로 두는 공개(등급이 show를 비움·늘 맞는 성공 선)는 상자 글 대신 '공개: 결과 그대로' — '선택지 3개 중: 공개 결과 그대로/랜덤 옵션'·다른 등급 목표 글이 들어가던 것(2026-11-13 S3 23·29·32번)
            if asis_v: t['keepReveal'] = True
            elif tx_: t['revealTx'] = {'kr': tx_['kr'], 'en': tx_.get('en') or tx_['kr']}
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
        # q가 없으면 상자 글의 'n%' → 기폭제 개수(count ≈ %) → 20 (2026-11-13 S1: q 없는 기폭제 상자가 늘 20%로 읽히던 것)
        mq = re.search(r'(\d+)\s*%', ' '.join(((sn.get(k) or n.get(k) or {}).get('kr') or '') for k in ('goal', 'label')))
        t = {'quality': sn.get('q') or (int(mq.group(1)) if mq else None) or sn.get('count') or 20}
    elif act == 'rune':
        rn = n.get('rune') or sn.get('rune')
        t = {'rune': rn if isinstance(rn, dict) else {'kr': rn or '', 'en': rn or ''}}
        # 룬 교체 상자(swapAstrid: 아스트리드의 창의성을 빼고 이 룬) · 같은 룬 여러 개(count, fill = 빈 소켓 모두) — 2026-11-13 S1: SaVeQ 집중구 r2 철 룬 2개
        if sn.get('swapAstrid') or n.get('swapAstrid'): t['swapAstrid'] = True
        k = sn.get('count') or n.get('count')
        if isinstance(k, int) and k > 1: t['runeCount'] = k
        if sn.get('fill') or n.get('fill'): t['runeFill'] = True
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
        self.P = V['params']; self.res = S['res']; self.sim = sim; self.vid = V.get('id')
        self.nodes = [dict(n, goal=n['goalBy'][V.get('id')]) if isinstance(n.get('goalBy'), dict) and n['goalBy'].get(V.get('id')) else n for n in _over(sim['graph']['nodes'], self.P)]   # 상자 goalBy(등급별 목표 글, 2026-11-13 S3 44번)
        self.by = {n['id']: n for n in self.nodes}
        self.E = self.res.get('edges') or {}
        self.EI = self.res.get('edgesI') or {}   # 선마다 센 값(a#순번, 2026-11-11) — 같은 상자로 가는 성공·실패 선을 따로 셈

    def st(self, nid): return (self.res.get('nodes') or {}).get(nid)

    def seen(self, nid):
        t = self.st(nid); return bool(t) and (t.get('visits') or 0) > 0 and not self.skipall(nid)

    def skipall(self, nid):
        """이 등급에서 늘 건너뛰는 상자(지나간 횟수 = 건너뛴 횟수, 사용량 없음 — 시한 투구 밸런스의 유동체, 2026-11-12): 레시피 단계에서 뺌"""
        t = self.st(nid) or {}; v = t.get('visits') or 0
        return v > 0 and (t.get('skips') or 0) >= v * 0.999 and not (t.get('use') or {}) and bool((self.by.get(nid) or {}).get('skipTo'))

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
    # (16—24)~(28—42), +(4.41—5)% — 바로 뒤에 조사(의·만큼·로…)가 붙은 수치는 문장 일부라 남김('피해가 의 원소 저항 관통' 깨짐, 2026-11-13 S2 G1 보고)
    t = re.sub(r'[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\)(\s*~\s*[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\))?(?!%?[의만로을를에으])%?', '', t)
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


def _simp(c, P):
    """조건에서 이 등급 값(param)을 풀어 냄: 늘 참이면 True, 늘 거짓이면 False, 나머지는 남은 조건"""
    if not isinstance(c, dict): return c
    if 'param' in c: return all(str(P.get(k)) == str(v) for k, v in c['param'].items())
    if 'not' in c:
        x = _simp(c['not'], P); return (not x) if isinstance(x, bool) else {'not': x}
    for k in ('all', 'any'):
        if k in c:
            xs = [_simp(x, P) for x in c[k]]
            if k == 'all' and any(x is False for x in xs): return False
            if k == 'any' and any(x is True for x in xs): return True
            xs = [x for x in xs if not isinstance(x, bool)]
            return (k == 'all') if not xs else xs[0] if len(xs) == 1 else {k: xs}
    return c


def _routes(W, n, valid, G_=None, CD=None):
    """단계 칩: 상자에서 나가는 선을 끝까지 따라가 실제 단계 번호로(지우기 상자·표시 상자는 건너뜀), 비율은 시뮬에서 그 선을 지난 횟수.
    라우터 선(아이템 상태마다 다음 단계를 고르는 숨은 선)은 '아이템 상태에 맞는 단계'로 묶지 않고 조건 글 + 단계 번호로(2026-11-12)"""
    t = W.st(n['id']) or {}
    def dest(to, d=0):
        T = W.by.get(to) or {}
        if to == n['id']: return 'self'
        # 이어 가는 버림 상자(variant ok + swapFracture/simTo: '다른 옵션이 분열돼도 같은 흐름') = 그 다음 상자로 — '버리고 처음부터'로 나오던 것(2026-11-13 S2, G7 보고)
        Ts = {**((G_.srcn.get(to) or {}) if G_ else {}), **T}   # 시뮬 파일 그래프엔 simTo·swapFracture가 없음
        if T.get('kind') == 'exit' and Ts.get('simTo') and (Ts.get('variant') == 'ok' or Ts.get('swapFracture')) and d < 5: return dest(Ts['simTo'], d + 1)
        if T.get('kind') in ('base', 'exit'): return 'restart'
        if T.get('kind') == 'done': return 'done'
        return to
    def ok_dest(d): return d in ('self', 'done', 'restart') or d in valid
    def src_if(nid, i, to):
        se = ((G_.srcn.get(nid) or {}).get('edges') or []) if G_ else []
        if not (i < len(se) and se[i].get('to') == to): return '?'
        e = se[i]
        if e.get('if') is None and e.get('lost'): return {'removed': e['lost']}   # 정리 상자의 '그 옵션이 지워지면' 선
        return e.get('if')
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
            if W.via(to):
                vo = list(T.get('omens') or [])
                if T.get('kind') == 'cleanup': vo += [k for k in ('Omen_of_Sinistral_Annulment', 'Omen_of_Dextral_Annulment') if ((W.st(to) or {}).get('use') or {}).get(k) and k not in vo]
                nv.append({'cur': T.get('cur') or 'Orb_of_Annulment', **({'omens': vo} if vo else {})})
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
        r = {'cls': 'no' if no else 'ok', 'lab': lab, 'to': L['to'], 'share': L['share'], 'n': round(L['share'] * ntot, 3), 'res': cls0 or cls_post, '_i': e0[5] if e0[5] is not None and e0[5] >= 0 else 999}
        if needc: r['_c'] = True; r['_e0'] = e0[2]
        if L['vias']:
            v = dict(L['vias'][0])
            if len(L['vias']) > 1: v['then'] = L['vias'][1:]
            r['via'] = v; r['vo'] = True
        if post and not main: r['lost'] = True
        # 조건 글 재료: 이 단계 선의 조건, 지우기 뒤 선의 조건(지운 뒤 상태)
        if CD:
            c0 = src_if(L['first'][0], L['first'][1][5], L['first'][1][4]) if L['first'][1][5] >= 0 else '?'
            a0 = CD.atoms(c0) if c0 != '?' else []
            r['_a'] = a0 or []
            if c0 != '?' and L['first'][0] == n['id']: r['_if'] = c0
            if post:
                ap = CD.atoms(src_if(post[0], post[1][5], post[1][4])) if post[1][5] >= 0 else []
                ap = [a for a in (ap or []) if a[0] not in {b[0] for b in (a0 or [])}]
                # 같은 라우터 선 목록이고 지운 뒤 선이 앞 순번이면, 그 선이 지우기 전엔 맞지 않았음 = '없음'이 '지워짐'
                Pn = W.by.get(post[0]) or {}
                same = [e['to'] for e in n.get('edges') or []] == [e['to'] for e in Pn.get('edges') or []]
                if same and post[1][5] < L['first'][1][5]:
                    ap = [(a[0], a[1][:-3] + ' 지워짐', a[2].replace('no ', '', 1) + ' removed', 'x') if a[3] == 'nohas' else a for a in ap]
                r['_a'] = ap if needc else (a0 or [])
                # 같은 글로 보이는 갈래를 가를 때 쓰는 '지운 뒤 상태': 지우기 뒤 선 전부의 조건(마지막 선에 조건이 없을 때 앞 선 조건)
                apx = list(ap)
                for y in ch[:-1]:
                    for a in (CD.atoms(src_if(y[0], y[1][5], y[1][4])) if y[1][5] >= 0 else []) or []:
                        if a[0] not in {b[0] for b in apx} and a[0] not in {b[0] for b in (a0 or [])}: apx.append(a)
                r['_ap'] = apx
        out.append(r)
    # 같은 결과(종류·도착·지우기·글)는 합침 — 조건 재료는 많이 지난 쪽
    m = {}
    for r in sorted(out, key=lambda r: -r['share']):
        k = (r['cls'], r['to'], json.dumps(r.get('lab'), ensure_ascii=False), json.dumps(r.get('via'), sort_keys=True), r.get('lost'))
        if k in m:
            m[k]['share'] += r['share']; m[k]['n'] = (m[k].get('n') or 0) + (r.get('n') or 0); m[k]['_i'] = min(m[k].get('_i', 999), r.get('_i', 999))
            if m[k].get('_ap') is not None:   # 지운 뒤 갈래가 여럿 합쳐짐 — 모두에 맞는 조건만 남김
                ks = {a[0] for a in (r.get('_ap') or [])}; m[k]['_ap'] = [a for a in m[k]['_ap'] if a[0] in ks]
        else: m[k] = dict(r)
    rs = list(m.values())
    # 이 등급에선 늘 맞는 성공 선(예: '나오는 대로')이 있으면 같은 곳으로 가는 다른 성공 선은 그 줄에 합침 — '나오는 대로 →'와 '성공 →'이 같이 나오던 것(2026-11-13 S2, G5 보고)
    ka = next((r for r in rs if r['cls'] == 'ok' and r.get('lab') and r.get('_if') not in (None, '?') and G_ and _simp(r['_if'], G_.params) is True), None)
    if ka:
        for r in [x for x in rs if x is not ka and x['cls'] == 'ok' and x['to'] == ka['to'] and not x.get('via')]:
            ka['share'] += r['share']; ka['n'] = (ka.get('n') or 0) + (r.get('n') or 0); rs.remove(r)
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
        # 지우고 같은 단계를 다시 하는 선(먼저: 소멸)도 보이는 갈래 — '실패 → 다시'와 '실패 → 18번'이 조건 없이 같이 나오던 것(2026-11-13 S2: 바리케이드 p4)
        grp = [r for r in rs if r['cls'] == cl and not (r['to'] == 'self' and not r.get('via')) and not r.get('skip')]
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
        elif len(bare) == 1 and len(grp) == 2:   # 조건 없는 '나머지' 선: 다른 선 조건의 반대(이 등급 값을 푼 뒤) — 예: 가장 낮은 옵션이 잡옵 ↔ 지킬 옵션
            oth = next((r for r in grp if r is not bare[0] and not r.get('_c') and r.get('_if') not in (None, '?')), None)
            oc = _simp(oth['_if'], G_.params) if oth and G_ else None
            if isinstance(oc, dict):
                na = CD.atoms({'not': oc}) if CD else None
                if na: bare[0]['_a'] = na
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
    # 화면에서 같은 글로 보이는 갈래가 다른 단계로 가면(2026-11-13 S2: '빗나감 → 8-2번'과 '빗나감 → 다시', '원하는 옵션이 지워지면 → 4-1번으로'와 '→ 7-3번으로'):
    # 지운 뒤 조건(_ap)이 있으면 그 글로, 없으면 이 갈래에만 있는 조건으로 이름을 바꿈
    def shown(r):
        if r.get('vo') and r.get('alt') and (not r.get('lab') or r.get('plab')): return ('alt',)
        if r.get('lost') and not r.get('lab'): return ('lost',)
        return ('lab', r['cls'], (r.get('lab') or {}).get('kr'))
    byshow = {}
    for r in rs:
        if r.get('skip') or (r['to'] == 'self' and not r.get('via')) or (r.get('lab') or {}).get('kr') == '그 밖': continue
        byshow.setdefault(json.dumps(shown(r), ensure_ascii=False), []).append(r)
    for grp_ in byshow.values():
        if len({r['to'] for r in grp_}) < 2: continue
        for r in grp_:
            lb = _label(r.get('_ap') or [])
            if not lb:
                others = [set(a[0] for a in (o.get('_a') or [])) for o in grp_ if o is not r]
                own = [a for a in (r.get('_a') or []) if not any(a[0] in o for o in others)]
                lb = _label(own) if own else None
            if not lb: continue
            base = (r.get('lab') or {}) if shown(r)[0] == 'lab' and r.get('lab') else None
            if base and lb['kr'] not in base['kr']:
                r['lab'] = {'kr': base['kr'] + ', ' + lb['kr'], 'en': base['en'] + ', ' + lb['en']}
            elif not base:
                pre = ('실패, ', 'Miss, ') if r['cls'] == 'no' and shown(r)[0] == 'lab' else ('', '')
                r['lab'] = {'kr': pre[0] + lb['kr'], 'en': pre[1] + lb['en'][:1].upper() + lb['en'][1:]}
            r['plab'] = False
    # 그래도 같은 글로 남는 갈래(조건을 글로 못 푸는 라우터 선)는 한 줄로 합침: '다른 옵션이 지워지면 → 3·4-4번으로'
    byshow = {}
    for r in rs:
        if r.get('skip') or (r['to'] == 'self' and not r.get('via')) or (r.get('lab') or {}).get('kr') == '그 밖': continue
        byshow.setdefault(json.dumps(shown(r), ensure_ascii=False), []).append(r)
    for grp_ in byshow.values():
        if len({r['to'] for r in grp_}) < 2 or any(r['to'] == 'self' for r in grp_): continue
        grp_.sort(key=lambda r: -r['share']); h = grp_[0]
        h['toAlt'] = [r['to'] for r in grp_[1:] if r['to'] != h['to']]
        for r in grp_[1:]:
            h['share'] += r['share']; h['n'] = (h.get('n') or 0) + (r.get('n') or 0); rs.remove(r)
        if len({json.dumps(r.get('via'), sort_keys=True) for r in grp_}) > 1: h.pop('via', None)
    if n.get('skipTo') and (t.get('skips') or 0) > 0.001 and ok_dest(dest(n['skipTo'])) and t['skips'] / max(1e-9, t.get('visits') or 1) >= 0.005:
        sl = n.get('skipNote')
        sif = n.get('skipIf') or ((G_.srcn.get(n['id']) or {}).get('skipIf') if G_ else None)   # 시뮬 파일 그래프에는 skipIf가 없음
        if not sl and CD and isinstance(sif, dict):   # 건너뛰는 조건 글(예: 접미 꽉 참) — '이미 있으면 건너뜀 → 완성'이 무엇이 있는지 안 보이던 것(2026-11-13 S2: MazBro +5 목걸이 Z12)
            sc = _simp(sif, G_.params) if G_ else sif
            sl = _label(CD.atoms(sc) or []) if isinstance(sc, dict) else None
        rs.append({'cls': 'ok', 'lab': sl or {'kr': '건너뜀', 'en': 'Skip'}, 'to': dest(n['skipTo']),
                   'share': t['skips'] / max(1e-9, t.get('visits') or 1), 'skip': True})
    # 성공·빗나감이 모두 같은 단계로 가면(에센셜 '빗나감 — 그대로') 한 줄 '→ n번' — '성공 → 8번'과 '빗나감 — 그대로 → 8번'이 같이 나오던 것(2026-11-13 S3 40번)
    rn = [r for r in rs if not r.get('skip')]
    if len(rn) >= 2 and len({r['to'] for r in rn}) == 1 and rn[0]['to'] != 'self' and not any(r.get('via') or r.get('toAlt') for r in rn) and any(r['cls'] == 'ok' for r in rn):
        h = next(r for r in rn if r['cls'] == 'ok')
        h['share'] = sum(r['share'] or 0 for r in rn); h['n'] = sum(r.get('n') or 0 for r in rn) or h.get('n'); h['lab'] = None; h['keepAll'] = True
        for r in rn:
            if r is not h: rs.remove(r)
    # 순서: 성공(많은 것부터) → 실패(그래프 선 순서 = 플로우차트 흐름, 같으면 많은 것부터) → 그 밖 (2026-11-12: '1번째·2번째·3번째 빗나감'이 거꾸로 읽히던 것)
    rs.sort(key=lambda r: (r['cls'] != 'ok', r.get('skip', False), (r.get('lab') or {}).get('kr') == '그 밖', r.get('_i', 999) if r['cls'] != 'ok' else 0, r['to'] != 'self', -(r['share'] or 0)))
    for r in rs: r['share'] = round(r['share'], 5); r.pop('_a', None); r.pop('_c', None); r.pop('_e0', None); r.pop('_i', None); r.pop('_if', None); r.pop('_ap', None)
    return [{k: v for k, v in r.items() if v is not None and v is not False} for r in rs]


def _repeats(W, n):
    """상자가 다시 쓰이는지: 나가는 선을 따라 베이스·완성·버림을 거치지 않고 이 상자로 돌아올 수 있으면 반복(2026-11-12, recipes.html fcRepeats와 같은 규칙)"""
    def nx(N): return [e.get('to') for e in N.get('edges') or []] + [N.get('next'), N.get('skipTo')] + list((N.get('options') or {}).values())
    seen, q = set(), [x for x in nx(n) if x]
    while q:
        x = q.pop(0)
        if x == n['id']: return True
        if x in seen: continue
        seen.add(x); N = W.by.get(x)
        if not N or N.get('kind') in ('base', 'done', 'exit'): continue
        q += [y for y in nx(N) if y]
    return False


def _keep_all(W, n):
    """이 등급에서 성공·빗나감이 모두 같은 상자로 감(빗나감 — 그대로): 목표가 없는 '결과 그대로' 상자(2026-11-13 S3 40·44번)"""
    if getattr(W, 'vid', None) != 'ess': return False   # 에센셜(반복 없음, 랜덤 옵션 허용)만 — 밸런스의 '한 번 시도하고 그대로'는 목표가 있음
    outs = W.outs(n)
    used = [x for x in outs if W.ec(n['id'], x, outs) > 0]
    return bool(used) and len({x[1] for x in used}) == 1 and used[0][1] != n['id'] and any(x[3] == 'ok' for x in outs if x[1] == used[0][1]) and any(x[3] == 'fail' for x in used) and not W.via(used[0][1])


def _fcs(W, n, fold_ids=frozenset()):
    t = W.st(n['id']) or {}
    tries = (t.get('visits') or 0) - (0 if n.get('kind') == 'cleanup' else (t.get('skips') or 0))
    outs = W.outs(n)
    has_res = any(x[3] for x in outs)
    ok = [x for x in outs if x[3] == 'ok' and (n.get('pAll') or not x[0].get('dash') or (W.by.get(x[1]) or {}).get('kind') == 'assume' or ((W.by.get(x[1]) or {}).get('kind') == 'exit' and (W.by.get(x[1]) or {}).get('variant') == 'ok'))]   # '같은 흐름으로 가정'(assume) 갈래도 성공(2026-11-13 S2, G7 보고: Belton 분열 34%)
    if has_res and not any(x[3] == 'ok' for x in outs): ok = [x for x in outs if not x[3] and x[1] != n['id']]   # 실패선만 표시된 상자: 나머지 선이 성공
    okc = sum(W.ec(n['id'], x, outs) for x in ok)
    if has_res and okc <= 0 and tries > 0:   # 상태마다 다른 단계로 보내는 상자: 표시된 성공선을 안 거치고 숨은 선으로 나아감 → 실패·반복이 아닌 선 모두
        okc = sum(W.ec(n['id'], x, outs) for x in outs if x[3] != 'fail' and x[1] != n['id'])
    p = min(1.0, okc / tries) if has_res and tries > 0 else 1.0
    if n.get('act') == 'flux' or _keep_all(W, n): p = 1.0   # 유동체는 늘 바뀜(확정 변환) — 뒤 선은 변환 뒤 상태로 고르는 갈래라 성공 확률이 아님(2026-11-13 S1: 시한 장화 6.8%)
    rows = None
    if n.get('curRows') and t.get('byCur'):
        rows = []
        for rw in n['curRows']:
            b = t['byCur'].get(rw.get('key') or rw.get('cur'))
            ids = rw.get('ids') or [rw.get('cur')] + list(n.get('omens') or [])
            rows.append({'kr': rw['kr'], 'en': rw['en'], 'ids': ids, **({'p': round(b['ok'] / b['t'], 5)} if b and b.get('t') else {})})
    if not rows and n.get('trim') and len(t.get('byCur') or {}) >= 2:   # 절사/말소 상자: 경우마다 쓰는 징조와 그때 성공 확률(2026-11-13 S1)
        sd = (n['trim'].get('side') if isinstance(n['trim'], dict) else None) or 'p'
        er = 'Omen_of_Sinistral_Erasure' if sd == 'p' else 'Omen_of_Dextral_Erasure'
        sk, se = ('접두', 'prefix') if sd == 'p' else ('접미', 'suffix')
        LB = {'Omen_of_Whittling': (f'잡옵이 아이템에서 레벨이 가장 낮음', 'Junk is the lowest-level modifier'),
              f'{er}+Omen_of_Whittling': (f'잡옵이 {sk}에서만 레벨이 가장 낮음', f'Junk is the lowest-level {se} only'),
              er: (f'남길 {sk}가 잡옵보다 레벨이 낮음', f'A kept {se} is lower than the junk')}
        rows = []
        for k in sorted(t['byCur'], key=lambda k: -t['byCur'][k].get('t', 0)):
            b = t['byCur'][k]
            if k not in LB or not b.get('t'): continue
            rows.append({'kr': LB[k][0], 'en': LB[k][1], 'ids': [n.get('cur')] + k.split('+'), 'p': round(b['ok'] / b['t'], 5)})
        rows = rows or None
    if p <= 0 and tries > 0: p = None   # 이 상자에서 바로 성공하는 일은 없고 결과에 따라 다음 상자로 갈림
    return {'p': round(p, 6) if p is not None else None, 'tries': round(tries, 4), 'use': {k: round(v, 4) for k, v in (t.get('use') or {}).items() if v >= 0.0005},
            'div': round(t.get('div') or 0, 4), 'reach': round(t.get('reach') or 0, 4), **({'rows': rows} if rows else {}), **({'loop': True} if n['id'] in fold_ids else {}), **({'once': True} if n.get('once') or (n.get('kind') != 'cleanup' and n['id'] not in fold_ids and p is not None and p < 0.995 and (not _repeats(W, n) or (p > 0 and tries * p < 0.9 * (t.get('reach') or 1)))) else {})}   # 다시 하지 않는 상자: 레시피 글은 '1회 시도' — 접힌 반복 안 상자는 반복이 다시 부르니 빼고 시뮬 사용량 그대로(2026-11-13 S2: 화살통 엑잘 '1회 시도 0.3%')


def _miss(W, n):
    """등급을 가르는 갈래: 빗나갈 때 가는 선(1% 넘게 지나는 것)과 분기 상자를 거치는 선.
    성공 선은 빼고, 결과를 적지 않은 숨은 선은 같은 상자로 가는 보이는 선의 결과를 따름(2026-11-12: 숨은 성공 선을 빗나감으로 세던 것)"""
    outs = W.outs(n); tot = sum(W.ec(n['id'], x, outs) for x in outs) or 1
    vres = {}
    for x in outs:
        if not x[0].get('hide') and x[3]: vres.setdefault(x[4], x[3])
    def miss(x):
        eff = x[3] or (vres.get(x[4]) if x[0].get('hide') else None)   # 선에 적은 결과가 먼저, 결과 없는 숨은 선만 보이는 선을 따름
        return not (eff == 'ok' and x[4] == x[1])
    return [x for x in outs if miss(x) and W.ec(n['id'], x, outs) / tot >= 0.01]


_NT = {}
def _ntiers(cls, gi):
    """그 옵션 그룹의 티어 수(클래스 파일)"""
    if cls not in _NT:
        try: _NT[cls] = [len(g.get('t') or []) for g in json.load(open(f'/home/claude/poe2data/site/data/c/{cls}.json'))['groups']]
        except Exception: _NT[cls] = []
    a = _NT[cls]; return a[gi] if 0 <= gi < len(a) else None


_TL = {}
def _top_tier(cls, gi, ilvl):
    """그 아이템 레벨에서 나올 수 있는 가장 높은 티어 번호(1 = 1티어) — 등급 갈림 글 '2~3티어'(2026-11-13 S3 48번)"""
    if not ilvl: return 1
    if cls not in _TL:
        try: _TL[cls] = [[(t[0] if isinstance(t, list) else (t.get('l') or t.get('lvl') or 0)) for t in (g.get('t') or [])] for g in json.load(open(f'/home/claude/poe2data/site/data/c/{cls}.json'))['groups']]
        except Exception: _TL[cls] = []
    a = _TL[cls]
    if not (0 <= gi < len(a)): return 1
    return next((i + 1 for i, lv in enumerate(a[gi]) if isinstance(lv, (int, float)) and lv <= ilvl), 1)


def _sig(W, n, G_, cls=None):
    """등급 비교용: 이 상자를 이 등급은 어떻게 지나가나"""
    if not n or not W.seen(n['id']): return None
    tiers = []; tops = []
    for t in (n.get('show') or []):
        for gi, tm in G_.leaves(G_.name(t)):
            nt = _ntiers(cls, gi) if cls else None
            try: tm = int(tm) if tm is not None else None
            except Exception: tm = None
            tiers.append(99 if (tm and nt and tm >= nt) else (tm or 0))   # 티어 한도가 그 옵션의 최저 티어 이상 = 나오는 대로(2026-11-13 S2, G3 보고: '1~9티어')
            tops.append(_top_tier(cls, gi, W.sim['graph'].get('ilvl') or (G_.src or {}).get('ilvl')) if cls else 1)
    fails = sorted({(json.dumps(x[2], ensure_ascii=False, sort_keys=True) if x[2] else '', x[1] if not W.via(x[1]) else 'via')
                    for x in _miss(W, n)})
    return {'tiers': tiers, 'fails': fails, 'cur': n.get('cur'), 'top': min(tops) if tops else 1}


def _grade_note(sim, src, nid, tiers, cls=None):
    """같은 상자를 다른 등급이 다르게 지나면: [{tiers:[…], kr, en}, …]"""
    descs = []
    for tr in tiers:
        F, V, S = _version(sim, tr)
        if not S: continue
        W = Walk(sim, V, S); G_ = G(sim, src, V['params']); n = W.by.get(nid)
        descs.append((tr, W, G_, n, _sig(W, n, G_, cls)))
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
                tm = max(s['tiers'])
                if tm >= 99: kr.append('티어 상관없음'); en.append('any tier')
                else:
                    t0 = min(s.get('top') or 1, tm)   # 아이템 레벨로 못 붙는 위 티어는 빼고(1티어 레벨 81, 아이템 레벨 77 → '2~3티어')
                    kr.append(f'{tm}티어' if tm == t0 else f'{t0}~{tm}티어'); en.append(f'T{tm}' if tm == t0 else f'T{t0}–{tm}')
            if diff_c and n.get('cur'): kr.append('@' + n['cur']); en.append('@' + n['cur'])
            if diff_f:
                fl = _miss(W, n)
                if not fl: kr.append('결과 그대로 다음'); en.append('keep the result')
                else:
                    # 갈래가 여럿이면 플로우차트 읽는 순서(도착 상자 위치)로 첫 번째 — 선 순서의 첫 번째라 접힌 상자 순서와 다르던 것(2026-11-13 S3 24번: 시한 장갑 분광 먼저)
                    fl = sorted(fl, key=lambda x: tuple((W.by.get(x[1]) or {}).get('pos') or (0, 0))[::-1] if x[1] != n['id'] else (-1e9, 0))   # 같은 상자 다시는 맨 앞(예전처럼)
                    e, to, lab, cls, raw = fl[0][:5]; T = W.by.get(to) or {}
                    # 선 이름 앞의 '빗나감'·'실패'는 뗌 — '빗나가면 빗나감'(2026-11-13 S2: MazBro +5 목걸이·노블 오래된 사파이어)
                    lk = re.sub(r'^(빗나감|실패)\s*([—,:·-]\s*)?', '', (lab or {}).get('kr') or '').strip()
                    le = re.sub(r'^(miss(ed)?|fail(ed)?)\b\s*([—,:·-]\s*)?', '', (lab or {}).get('en') or '', flags=re.I).strip()
                    tg = (T.get('goal') or T.get('label')) if T.get('kind') in ('act', 'cleanup') else None
                    if not e.get('res') and not lk and to != n['id']:   # 결과 표시 없는 선 = 빗나감이 아니라 등급마다 다음 상자가 다름(2026-11-13 S2: Seek 장화 합금 '빗나가면 다른 작업')
                        if T.get('kind') == 'done': kr.append('바로 완성'); en.append('finish here')
                        elif tg: kr.append('이어서 ' + tg['kr']); en.append('then: ' + (tg.get('en') or tg['kr']).lower())
                        elif T.get('cur'): kr.append(f"이어서 @{T['cur']}"); en.append(f"then @{T['cur']}")
                        else: kr.append('이어서 다른 단계'); en.append('then another step')
                    elif lk: kr.append('빗나가면 ' + lk); en.append('on a miss: ' + (le or lk).lower())
                    elif to == n['id']: kr.append('빗나가면 다시'); en.append('retry on a miss')
                    elif T.get('kind') == 'done': kr.append('빗나가도 그대로 완성'); en.append('finish as it is on a miss')
                    elif W.via(to): kr.append('빗나가면 지우고 다시'); en.append('remove and retry on a miss')
                    elif T.get('kind') in ('base', 'exit'): kr.append('빗나가면 처음부터'); en.append('start over on a miss')
                    elif T.get('cur'): kr.append(f"빗나가면 @{T['cur']}로"); en.append(f"on a miss: @{T['cur']}")
                    elif tg: kr.append('빗나가면 ' + tg['kr']); en.append('on a miss: ' + (tg.get('en') or tg['kr']).lower())
                    else: kr.append('빗나가면 다른 작업'); en.append('another step on a miss')
        if s and not kr: kr.append('이 단계 씀'); en.append('uses this step')
        parts.append({'tier': tr, 'kr': ', '.join(kr), 'en': ', '.join(en)})
    grp = []
    for p in parts:
        g = next((x for x in grp if x['kr'] == p['kr']), None)
        if g: g['tiers'].append(p['tier'])
        else: grp.append({'tiers': [p['tier']], 'kr': p['kr'], 'en': p['en']})
    return grp if len(grp) >= 2 else None


def read_recipe(r, sim, src, tiers, inherit=True):
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
    fold_ids = frozenset(i for L in loops if L.get('fold') or any(x.get('fold') and x.get('id') == L.get('id') for x in (src or {}).get('loops') or []) for i in L.get('nodes') or [])
    def loop_of(nid): return next((L for L in loops if nid in L['nodes']), None)
    old = {n['id']: n for n in r.get('nodes') or []}
    # 옛 단계 레시피(recipes_v5·notes_short)의 갈래 글(br)은 붙이지 않음 — 같은 id라도 플로우차트와 다른 흐름의 글이 섞여 나옴(2026-11-13 S1: 시한 장화 p1, 바리케이드 p2).
    # 갈래는 플로우차트 선(routes)에서 읽음. 꿀팁 번호(tips)·영상 시각(ts)만 이어받음
    # 2026-11-13 S2(G3 보고): 옛 노드 id가 새 상자 id와 같다고 옛 영상 시각·꿀팁을 이어받으면 엉뚱한 값이 붙음(한손 둔기).
    # 영상으로 다시 대조한 그래프(build_recipes FC_TS가 있음, inherit=False)는 시각은 FC_TS, 꿀팁은 TIPREF(상자 id 기준)만 씀.
    # 아직 다시 대조하지 않은 그래프는 예전처럼 이어받음(이어받기를 끄면 시각·꿀팁이 모두 사라지는 레시피가 많음 — 목록은 S2 보고)
    keep = (lambda i: {k: old[i][k] for k in ('tips', 'ts') if i in old and old[i].get(k)}) if inherit else (lambda i: {})
    b0 = {'id': base['id'] if base else 'b0', 'phase': 'base', 'do': 'base', 'cost': 'base', **(keep(base['id']) if base else {})}
    ob = next((x for x in r.get('nodes') or [] if x.get('do') == 'base'), None)
    if ob:
        for k in (('note', 'tips', 'ts') if inherit else ('note',)):   # 다시 대조한 그래프는 베이스 설명만 — 시각·꿀팁은 FC_TS·TIPREF
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
    for oi, n in enumerate(order):
        cur = n.get('item') or prev
        pv = prev if n['pos'][0] == 0 or not parent.get(n['id']) else (W.by[parent[n['id']]].get('item') or prev)
        # 바로 앞 상자가 레시피 단계에서 빠진 상자면 그 상자의 아이템 칸이 이 상자의 시작 상태(2026-11-12 시한 투구):
        # 옆 상자 앞의 지우기 상자(k2 → k3 '빈 접미 엑잘'), 이 등급에서 늘 건너뛰는 상자(밸런스 유동체 → q1)
        vin = [m for m in W.nodes if m.get('item') and ((n['pos'][0] != 0 and W.via(m['id'])) or W.skipall(m['id'])) and any(e.get('to') == n['id'] for e in m.get('edges') or [])]
        if vin: pv = vin[0]['item']
        G_._kall = _keep_all(W, n)
        act, om, t, last_bone = _target(G_, n, pv, cur, last_bone)
        o = {'id': n['id'], 'do': ACT.get(act, act) or 'manual'}
        if n.get('cur'): o['cur'] = n['cur']
        elif o['do'] == 'remove': o['cur'] = 'Orb_of_Annulment'
        if n.get('curIf') and o.get('cur'):   # 상태에 따라 오브가 바뀌는 상자: 그 등급 시뮬에서 가장 많이 쓴 오브(2026-11-12, 예: 하이엔드는 늘 완벽한 엑잘티드 오브)
            u = (W.st(n['id']) or {}).get('use') or {}
            cs = [o['cur']] + [c if isinstance(c, str) else c.get('cur') for c in n['curIf'] if (c if isinstance(c, str) else c.get('cur'))]
            top = max(cs, key=lambda c: u.get(c) or 0)
            if (u.get(top) or 0) > (u.get(o['cur']) or 0): o['cur'] = top
        if n.get('kind') == 'cleanup':   # 좌측·우측 소멸의 징조를 같이 쓰는 정리 상자(그래프 side): 시뮬 사용량에 있는 징조를 커런시 줄에(2026-11-12, 활 14.A)
            u = (W.st(n['id']) or {}).get('use') or {}
            om = om + [k for k in ('Omen_of_Sinistral_Annulment', 'Omen_of_Dextral_Annulment') if (u.get(k) or 0) > 0 and k not in om]
        if n.get('trim'):   # 절사/말소 자동 선택 상자(sim trimOmens): 시뮬이 실제로 쓴 징조를 많이 쓴 순서로 — '절사의 징조'만 적던 것(2026-11-13 S1: SaVeQ 집중구 w1, 좌측 말소가 더 많음)
            u = (W.st(n['id']) or {}).get('use') or {}
            tu = sorted([k for k in u if re.search(r'Whittling|Erasure', k) and (u.get(k) or 0) > 0], key=lambda k: -(u.get(k) or 0))
            if tu: om = [x for x in om if not re.search(r'Whittling|Erasure', x)] + tu
        if om: o['omens'] = om
        if t: o['target'] = t
        if n.get('trim'): o['trimFc'] = n['trim'].get('side') if isinstance(n['trim'], dict) else 'p'
        o['fcs'] = _fcs(W, n, fold_ids)
        o['routes'] = _routes(W, n, placed, G_, CD)
        if not o.get('cur') and (n.get('goal') or n.get('label')): o['label'] = n.get('goal') or n.get('label')
        if not t and n.get('showText'): o['note'] = n['showText'][0]
        elif not t and getattr(G_, '_marktx', None): o['note'] = G_._marktx
        G_._marktx = None
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
        elif o['do'] == 'remove' and (n.get('goal') or {}).get('kr') and n['goal']['kr'] != '소멸의 오브 사용':
            _, gone_ = _diff(pv, cur)   # 잡옵이 아닌 옵션을 지우는 소멸(예: 경멸 액체 옵션): '접미 잡옵 제거' 대신 상자 목표 글(2026-11-13 S2: SL 5옵션 주얼 s8)
            if any(l.get('m') not in ('j', 'u', 'd') and l.get('tags') for l in gone_): o['fcTarget'] = n['goal']
        gn = _grade_note(sim, src, n['id'], tiers, r.get('cls'))
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
        # 접힌 루프(그래프 loops fold)의 머리 단계: 목표·최악의 경우 한 줄씩(2026-11-12)
        FL = next((x for x in (src or {}).get('loops') or [] if x.get('fold') and (x.get('nodes') or [None])[0] == n['id']), None)
        # 이 등급에서 반복이 없는 루프(에센셜: 한 번 지나감 = 소속 상자에서 같은·앞 소속 상자로 되돌아간 통과 0)면 '반복 목표'·'최악의 경우' 줄을 붙이지 않음(2026-11-13 S3 22·37번)
        if FL:
            mem = [x for x in FL.get('nodes') or []]
            back = sum(W.cnt(a, b) for i, a in enumerate(mem) for b in mem[:i + 1])
            via_back = sum(W.cnt(a, v['id']) * 1 for a in mem for v in W.nodes if W.via(v['id']) and any(e.get('to') in mem for e in v.get('edges') or []))
            wto = (FL.get('worst') or {}).get('to')
            if back + via_back <= 1e-6: FL = dict(FL, goal=None, goalBy=None, worst=FL.get('worst') if wto and sum(W.cnt(a, wto) for a in mem) > 1e-6 else None)
        if FL:
            ln = {'goal': (FL.get('goalBy') or {}).get(V['id']) or FL.get('goal'), 'worst': {'kr': FL['worst']['kr'], 'en': FL['worst']['en']} if FL.get('worst') else None}
            ln = {k: v for k, v in ln.items() if v}
            if ln: o['loopNote'] = ln
        out.append(o)
        if n['pos'][0] == 0: prev = cur
        # 접힌 루프를 빠져나갈 때: 다음 상자의 시작 상태 = 접힌 상자의 아이템 칸(등급별 itemBy) — 더 앞 상자 칸을 쓰던 것(2026-11-13 S2, G2 보고)
        FLp = next((x for x in (src or {}).get('loops') or [] if x.get('fold') and n['id'] in (x.get('nodes') or [])), None)
        if FLp and (oi + 1 >= len(order) or order[oi + 1]['id'] not in FLp['nodes']):
            li = (FLp.get('itemBy') or {}).get(V['id']) or FLp.get('item')
            if li: prev = li
    # 선택 상자(kind side: 신성한 오브 수치 올리기·축성·합금 도박 등)는 레시피에도 '선택' 단계로 — 비용 합계에는 넣지 않음(optional, 합계는 시뮬 값) (2026-11-13 S1)
    for sn_ in [x for x in (src or {}).get('nodes') or [] if x.get('kind') == 'side']:
        if isinstance(sn_.get('tiers'), list) and V['id'] not in sn_['tiers']: continue
        at = [a_ for a_ in (sn_.get('attach') or []) if a_]
        ids = [x['id'] for x in out]
        anchor = next((a_ for a_ in at if a_ in ids), None)
        if not anchor and not any(W.by.get(a_, {}).get('kind') == 'done' for a_ in at): continue   # 붙는 상자가 이 등급 레시피에 없음
        o = {'id': sn_['id'], 'do': ACT.get(sn_.get('act'), sn_.get('act')) or 'manual', 'optional': True}
        if sn_.get('cur'): o['cur'] = sn_['cur']
        if sn_.get('omens'): o['omens'] = list(sn_['omens'])
        if sn_.get('goal') or sn_.get('label'): o['label'] = sn_.get('goal') or sn_.get('label'); o['goal'] = o['label']
        o['note'] = (sn_.get('showText') or [None])[0] or sn_.get('goal') or sn_.get('label') or {'kr': '선택 단계', 'en': 'Optional step'}
        o.update(keep(sn_['id']))
        i = ids.index(anchor) + 1 if anchor else len(out)
        while i < len(out) and out[i].get('fallbackFor'): i += 1   # 붙는 단계의 옆 단계 묶음 뒤
        o['phase'] = out[i - 1]['phase'] if i > 0 else phases[-1]['id']
        pf = next((out[j].get('fst') for j in range(i - 1, -1, -1) if out[j].get('fst') is not None), None)
        if pf is not None: o['fst'] = copy.deepcopy(pf)   # 선택 단계는 옵션을 바꾸지 않음 — 앞 단계 아이템 상태 그대로(엔진이 추측한 상태가 완성으로 넘어가지 않게)
        out.insert(i, o)
    last = (r.get('nodes') or [None])[-1]
    # 옛 레시피의 마지막 '선택' 단계(optional, 예: 히네코라의 머리카락 + 바알 오브)는 플로우차트에 없는 단계라 완성 글로 쓰지 않음(2026-11-13 S1)
    done_note = last.get('note') if last and last.get('do') == 'note' and not last.get('optional') else None
    out.append({'id': 'done', 'phase': phases[-1]['id'], 'do': 'note', 'note': done_note or {'kr': '완성.', 'en': 'Done.'}})
    # 단계 번호 = 플로우차트 상자 번호(베이스·선택·완성은 번호 없음 — 화면이 '선택'·'완성'으로)
    fno = fc_numbers(W, sim, src, V['id'])
    for o in out:
        if o.get('do') == 'base' or o.get('optional') or o['id'] == 'done': continue
        if o['id'] in fno: o['fcNo'] = fno[o['id']]
    res = S['res']
    return {'nodes': out, 'phases': phases, 'start': start_of(r, sim, src, V['params']),
            'fcRead': {k: res.get(k) for k in ('mean', 'median', 'p90', 'bases', 'baseDiv', 'use', 'useDiv')} | {'version': V['id']}}


def fc_numbers(W, sim, src, vid):
    """플로우차트 상자 번호(recipes.html flowchartHTML의 no와 같은 규칙: fcPrune → fcFold → 작업 상자를 읽는 순서로 1, 2, … · 옆 열 2.A · 그 옆 2.A.a).
    접힌 루프 안 상자는 '머리 번호-순서'(루프 steps의 node 순서). 레시피 단계 번호를 플로우차트와 같게(2026-11-13 S2: R1 지적 — 레시피 번호가 1~2 큼)"""
    res = W.res; rn = res.get('nodes') or {}
    nodes = W.nodes; by = {n['id']: n for n in nodes}
    gone = {n['id'] for n in nodes if n.get('kind') in ('act', 'cleanup', 'mark') and not rn.get(n['id'])}
    for n in nodes:
        if n.get('kind') == 'side' and isinstance(n.get('tiers'), list) and vid and vid not in n['tiers']: gone.add(n['id'])
    for n in nodes:
        if n.get('kind') == 'side' and n.get('attach') and all(a in gone or a not in by for a in n['attach']): gone.add(n['id'])
    jump = {}
    for n in nodes:
        t = rn.get(n['id'])
        if n.get('kind') == 'act' and n.get('skipTo') and t and (t.get('visits') or 0) > 0 and (t.get('skips') or 0) >= t['visits'] * 0.999 and not (t.get('use') or {}):
            gone.add(n['id']); jump[n['id']] = n['skipTo']
    def to(i):
        k = i; c = 0
        while k in jump and c < 20: k = jump[k]; c += 1
        return k
    edges_of = {n['id']: [to(e.get('to')) for e in n.get('edges') or []] for n in nodes}
    loops = []
    for L in (sim['graph'].get('loops') or []):
        ln = [i for i in L.get('nodes') or [] if i not in gone and i in by]
        if gone and len(ln) < 2: continue
        # fcPrune은 빠지는 상자가 하나도 없으면 루프를 그대로 둠(되돌아가는 선 검사도 안 함)
        if gone and not any(any(0 <= (ln.index(e) if e in ln else -1) <= k for e in edges_of.get(i) or []) for k, i in enumerate(ln)): continue
        loops.append({**L, 'nodes': ln})
    srcL = {L.get('id'): L for L in (src or {}).get('loops') or []}
    member = {}; folded = set()
    for L in loops:
        if not (L.get('fold') or (srcL.get(L.get('id')) or {}).get('fold')): continue
        steps = (srcL.get(L.get('id')) or {}).get('steps') or L.get('steps') or []
        order = [s.get('node') for s in steps if s.get('node') and s.get('node') not in gone]   # 이 등급이 거치지 않는 순서 줄은 번호에서 뺌(플로우차트 fcFold와 같게)
        for j, i in enumerate(L['nodes']):
            k = order.index(i) + 1 if i in order else j + 1
            member[i] = (L['nodes'][0], k)
            if j: folded.add(i)
    steps = sorted([n for n in nodes if n['id'] not in gone and n['id'] not in folded and n.get('kind') in ('act', 'cleanup')], key=lambda n: (n['pos'][1], n['pos'][0]))
    no = {}; cnt = {}; m = 0
    for n in steps:
        if n['pos'][0] == 0: m += 1; no[n['id']] = str(m)
    def parent(n, col):
        xs = [x for x in steps if x['pos'][0] == col and x['pos'][1] <= n['pos'][1]]
        return max(xs, key=lambda x: (x['pos'][1], x['pos'][0])) if xs else None
    for n in steps:
        if n['pos'][0] == 1:
            P = parent(n, 0); k = no[P['id']] if P else '0'; cnt[k] = cnt.get(k, 0) + 1; no[n['id']] = f'{k}.{chr(64 + cnt[k])}'
    for n in steps:
        if n['pos'][0] >= 2:
            P0 = parent(n, 0); P = parent(n, 1)
            k = no[P['id']] if P and (not P0 or P['pos'][1] >= P0['pos'][1]) else (no[P0['id']] if P0 else '0')
            cnt[k] = cnt.get(k, 0) + 1; no[n['id']] = f"{k}.{chr((96 if '.' in k else 64) + cnt[k])}"
    out = dict(no)
    for i, (h, k) in member.items():
        if h in no: out[i] = f'{no[h]}-{k}'
    return out


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
