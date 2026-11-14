/* 플로우차트(그래프) → 등급 레시피 — scripts/graph2recipe.py를 그대로 옮긴 것(node·브라우저 공용, 2026-11-13 W3)
   레시피 = 플로우차트를 그 등급 흐름대로 위에서 아래로 읽어 준 것. 파이썬 쪽을 고치면 여기도 같이 고치고
   node tools/test/_fcparity.js 로 차이 0을 확인함(docs/graph-model.md 'fcread.js').

   FcRead.readRecipe(recipe, sim, srcGraph, tiers, {inherit, groups}) -> {nodes, phases, start, fcRead} 또는 null
     sim      = site/data/sim/<id>.json, srcGraph = scripts/graphs/<id>.json, tiers = 같은 그래프 등급 레시피의 tier 목록
     groups   = 클래스 이름 → 클래스 파일 groups 배열(site/data/c/<cls>.json의 groups)을 돌려주는 함수 또는 {cls: groups}
   파이썬과 같은 결과를 내려고 파이썬 규칙을 흉내 냄: 참·거짓(빈 목록·빈 객체 = 거짓), None = null, round(반올림 = 가장 가까운 짝수),
   list.remove(값이 같은 첫 원소). 리버스(발굴 탭 reverse.html runFlow)가 등급 레시피를 읽을 때 씀(2026-11-13 W4). */
(function (root) {
  'use strict';
  const HAS = Object.prototype.hasOwnProperty;

  /* ---------- 파이썬 흉내 ---------- */
  function isObj(x) { return x !== null && typeof x === 'object' && !Array.isArray(x) && !(x instanceof Set); }
  function T(x) {   /* 파이썬 참·거짓 */
    if (x === null || x === undefined || x === false || x === 0 || x === '') return false;
    if (typeof x === 'number' && Number.isNaN(x)) return false;
    if (Array.isArray(x)) return x.length > 0;
    if (x instanceof Set) return x.size > 0;
    if (typeof x === 'object') return Object.keys(x).length > 0;
    return true;
  }
  function or_() { for (let i = 0; i < arguments.length - 1; i++) if (T(arguments[i])) return arguments[i]; return arguments[arguments.length - 1]; }
  function own(o, k) { return (o !== null && typeof o === 'object' && HAS.call(o, k)) ? o[k] : undefined; }
  function g(o, k) { const v = own(o, k); return v === undefined ? null : v; }   /* dict.get(k) */
  function gd(o, k, d) { return (o !== null && typeof o === 'object' && HAS.call(o, k)) ? o[k] : d; }   /* dict.get(k, d) */
  function nz(v) { return v === undefined ? null : v; }
  function isStr(x) { return typeof x === 'string'; }
  function isInt(x) { return typeof x === 'number' && Number.isInteger(x); }
  function pyStr(v) {
    if (v === null || v === undefined) return 'None';
    if (v === true) return 'True'; if (v === false) return 'False';
    return String(v);
  }
  function pyInt(v) {   /* int(v) — 안 되면 예외 */
    if (v === true) return 1; if (v === false) return 0;
    if (typeof v === 'number') { if (!isFinite(v)) throw new Error('int'); return Math.trunc(v); }
    if (typeof v === 'string') { const s = v.trim(); if (/^[+-]?\d+$/.test(s)) return parseInt(s, 10); throw new Error('int'); }
    throw new Error('int');
  }
  /* round(x, nd): 실제 값을 소수 nd자리로, 딱 반이면 짝수 쪽(파이썬과 같음) */
  const _dv = new DataView(new ArrayBuffer(8));
  function pyRound(x, nd) {
    if (typeof x !== 'number') x = Number(x);
    if (!isFinite(x) || x === 0) return x;
    const neg = x < 0; const ax = Math.abs(x);
    _dv.setFloat64(0, ax); const bits = _dv.getBigUint64(0);
    const ex = Number((bits >> 52n) & 0x7ffn); const mant = bits & ((1n << 52n) - 1n);
    let m, e;
    if (ex === 0) { m = mant; e = -1074; } else { m = mant | (1n << 52n); e = ex - 1075; }
    if (e >= 0) return x;
    const k = BigInt(-e); const num = m * (10n ** BigInt(nd)); const den = 1n << k;
    let q = num / den; const rem = num - q * den; const r2 = rem * 2n;
    if (r2 > den || (r2 === den && (q & 1n) === 1n)) q += 1n;
    let s = q.toString();
    if (nd > 0) { s = s.padStart(nd + 1, '0'); s = s.slice(0, s.length - nd) + '.' + s.slice(s.length - nd); }
    const v = Number(s);
    return neg ? -v : v;
  }
  function cmpStr(a, b) {   /* 코드 포인트 순서 */
    if (a === b) return 0;
    const n = Math.min(a.length, b.length);
    for (let i = 0; i < n; i++) {
      const x = a.codePointAt(i), y = b.codePointAt(i);
      if (x !== y) return x < y ? -1 : 1;
      if (x > 0xffff) i++;
    }
    return a.length < b.length ? -1 : a.length > b.length ? 1 : 0;
  }
  function cmp(a, b) {   /* 튜플 비교 */
    if (Array.isArray(a) && Array.isArray(b)) {
      for (let i = 0; i < Math.min(a.length, b.length); i++) { const c = cmp(a[i], b[i]); if (c) return c; }
      return a.length - b.length;
    }
    if (typeof a === 'string' && typeof b === 'string') return cmpStr(a, b);
    const x = typeof a === 'boolean' ? +a : a, y = typeof b === 'boolean' ? +b : b;
    return x < y ? -1 : x > y ? 1 : 0;
  }
  function sortBy(arr, key) {   /* sorted(arr, key=…) — 안정 정렬 */
    return arr.map((v, i) => [key(v), i, v]).sort((p, q) => cmp(p[0], q[0]) || p[1] - q[1]).map(p => p[2]);
  }
  function sortInPlace(arr, key) { const s = sortBy(arr, key); for (let i = 0; i < s.length; i++) arr[i] = s[i]; return arr; }
  function maxBy(arr, key) { let best, bk, f = false; for (const v of arr) { const k = key(v); if (!f || cmp(k, bk) > 0) { best = v; bk = k; f = true; } } return f ? best : undefined; }
  function sum(arr) { let s = 0; for (const v of arr) s += v; return s; }
  function dumps(v, sk) {   /* json.dumps(…) — 같은지 비교·정렬용 */
    if (v === null || v === undefined) return 'null';
    if (v === true) return 'true'; if (v === false) return 'false';
    if (typeof v === 'number') return String(v);
    if (typeof v === 'string') return JSON.stringify(v);
    if (v instanceof Set) v = [...v];
    if (Array.isArray(v)) return '[' + v.map(x => dumps(x, sk)).join(', ') + ']';
    let ks = Object.keys(v).filter(k => v[k] !== undefined);
    if (sk) ks = ks.slice().sort(cmpStr);
    return '{' + ks.map(k => JSON.stringify(k) + ': ' + dumps(v[k], sk)).join(', ') + '}';
  }
  function deq(a, b) {   /* 파이썬 == */
    if (a === b) return true;
    if (a === null || a === undefined || b === null || b === undefined) return (a == null) && (b == null);
    if (typeof a === 'boolean' || typeof b === 'boolean') return (typeof a === 'boolean' ? +a : a) === (typeof b === 'boolean' ? +b : b);
    if (typeof a !== 'object' || typeof b !== 'object') return false;
    if (Array.isArray(a) !== Array.isArray(b)) return false;
    if (Array.isArray(a)) { if (a.length !== b.length) return false; for (let i = 0; i < a.length; i++) if (!deq(a[i], b[i])) return false; return true; }
    const ka = Object.keys(a).filter(k => a[k] !== undefined), kb = Object.keys(b).filter(k => b[k] !== undefined);
    if (ka.length !== kb.length) return false;
    for (const k of ka) { if (!HAS.call(b, k) || b[k] === undefined || !deq(a[k], b[k])) return false; }
    return true;
  }
  function pyRemove(arr, x) { const i = arr.findIndex(y => deq(y, x)); if (i < 0) throw new Error('list.remove(x): x not in list'); arr.splice(i, 1); }
  function pyIn(arr, x) { return arr.some(y => deq(y, x)); }
  function clone(x) { return x === undefined ? undefined : JSON.parse(JSON.stringify(x)); }
  function kstr(k) { return JSON.stringify(k); }
  function cap1(s) { return s.slice(0, 1).toUpperCase() + s.slice(1); }

  const ACT = { annul: 'remove', rune: 'manual', cleanup: 'remove' };
  const SIDE_OMEN = [['Sinistral', 'p'], ['Dextral', 's']];

  function _key(l) {
    const tg = l.tags || [];
    return kstr([nz(l.s), tg.length ? tg : nz(l.kr), nz(l.m)]);
  }
  function _diff(prev, cur) {
    const rest = cur.slice(); const gone = [];
    for (const l of prev) {
      const k = _key(l);
      const j = rest.findIndex(x => _key(x) === k);
      if (j < 0) gone.push(l); else rest.splice(j, 1);
    }
    return [rest, gone];
  }
  function _side_of_omens(omens, word) {
    for (const o of omens || []) for (const [k, sd] of SIDE_OMEN) if (o.startsWith(`Omen_of_${k}_${word}`)) return sd;
    return null;
  }
  function _cond_tags(c, out) {
    if (isObj(c)) {
      for (const k of Object.keys(c)) {
        const v = c[k];
        if (k === 'not') continue;
        if ((k === 'added' || k === 'has' || k === 'fractured') && isStr(v)) out.push(v);
        else if ((k === 'added' || k === 'has') && isObj(v) && isStr(v.tag)) out.push(v.tag);
        else if (k === 'count' && isObj(v) && isStr(v.tag)) out.push(v.tag);
        else _cond_tags(v, out);
      }
    } else if (Array.isArray(c)) for (const x of c) _cond_tags(x, out);
    return out;
  }
  function _pmatch(par, P) { return Object.keys(par || {}).every(k => pyStr(g(P, k)) === pyStr(par[k])); }
  function _over(nodes, P) {
    return nodes.map(n => {
      const o = (n.over || []).find(o => _pmatch(o.param, P));
      return o ? Object.assign({}, n, o.set) : n;
    });
  }
  function _when(e, P) { return _pmatch(e.when, P); }
  function _strip(lab) {
    if (!T(lab)) return null;
    const o = {}; for (const k of Object.keys(lab)) o[k] = lab[k].replace(/\s*→\s*[\dA-Z.]+$/, ''); return o;
  }
  function vid_of(gr, params) {
    const v = (gr.versions || []).find(v => _pmatch(v.params, params || {}));
    return v ? nz(v.id) : null;
  }
  function _is_tip(x) { return isObj(x) && String(or_(g(x, 'kr'), '')).replace(/^\s+/, '').startsWith('💡'); }

  function shown_leaves(tags, tag, vid, params) {
    const Tg = own(tags || {}, tag);
    if (!isObj(Tg) || Tg.gi != null || !T(Tg.anyOf)) return null;
    let s = isObj(Tg.shownBy) ? g(Tg.shownBy, vid) : null;
    if (s == null) s = nz(Tg.shown);
    if (s == null) return null;
    const P = params || {};
    const tm = v => {
      if (isStr(v) && v.startsWith('$')) v = g(P, v.slice(1));
      try { return (v !== null && v !== undefined && v !== '') ? pyInt(v) : null; } catch (e) { return null; }
    };
    const out = [];
    for (const x of (Array.isArray(s) ? s : [s])) {
      if (typeof x === 'boolean') continue;
      if (isInt(x)) out.push({ gi: x, tmax: null });
      else if (isStr(x)) {
        const L = own(tags, x);
        if (isObj(L) && L.gi != null) out.push({ gi: L.gi, tmax: tm(g(L, 'tmax')), tag: x });
      } else if (isObj(x) && x.gi != null) {
        const o = { gi: x.gi, tmax: tm(g(x, 'tmax')) };
        if (T(x.tmin)) o.tmin = tm(x.tmin);
        out.push(o);
      }
    }
    return out.length ? out : null;
  }

  function leaf_gis(tags, tag, seen) {
    seen = seen || [];
    const Tg = isStr(tag) ? own(tags || {}, tag) : tag;
    if (isStr(tag) && seen.includes(tag)) return [];
    if (!isObj(Tg)) return [];
    if (Tg.gi != null) return [Tg.gi];
    const out = [];
    for (const x of Tg.anyOf || []) for (const gi of leaf_gis(tags, x, seen.concat(isStr(tag) ? [tag] : []))) if (!out.includes(gi)) out.push(gi);
    return out;
  }

  /* ---------- G: 태그·등급 값 ---------- */
  class G {
    constructor(sim, src, params) {
      this.g = sim.graph; this.src = T(src) ? src : {}; this.params = params;
      this.tags = this.g.tags || {};
      this.srcn = {}; for (const n of _over(this.src.nodes || [], params)) this.srcn[n.id] = n;
      this.vid = vid_of(this.g, params); this._cur = null;
      this._kall = false; this._lus = null; this._lord = null; this._marktx = null;
    }
    sn(id) { return own(this.srcn, id); }
    shown(tag, k) {
      k = k || 0;
      const sl = shown_leaves(this.tags, this.name(tag), this.vid, this.params);
      return sl ? sl[Math.min(k, sl.length - 1)] : null;
    }
    on_gis(lines, skip) {
      const out = new Set(), k = {};
      const ls = (lines || []).filter(l => l.m !== 'j' && T(l.tags));
      let last = null;
      if (T(skip)) { const ix = ls.map((l, i) => this.name(l.tags[0]) === skip ? i : -1).filter(i => i >= 0); last = ix.length ? Math.max(...ix) : null; }
      ls.forEach((l, i) => {
        const tg = this.name(l.tags[0]); const j = gd(k, tg, 0); k[tg] = j + 1;
        if (i === last) return;
        const lv = this.leaves(tg);
        if (lv.length === 1) out.add(lv[0][0]);
        else { const sh = this.shown(tg, j); if (T(sh)) out.add(sh.gi); }
      });
      return out;
    }
    nth(tag, lines) {
      return Math.max(0, (lines || []).filter(l => (l.tags || []).map(x => this.name(x)).includes(tag)).length - 1);
    }
    name(t) {
      if (isStr(t) && t.startsWith('$')) { const k = t.slice(1); return HAS.call(this.params, k) ? nz(this.params[k]) : t; }
      return t;
    }
    tmax(tag, line_tmax) {
      const Tg = (tag == null ? null : own(this.tags, tag)) || {};
      let v = line_tmax != null ? line_tmax : g(Tg, 'tmax');
      if (isStr(v) && v.startsWith('$')) v = g(this.params, v.slice(1));
      try { return v != null ? pyInt(v) : null; } catch (e) { return null; }
    }
    leaves(tag, seen) {
      seen = seen || [];
      tag = this.name(tag); const Tg = (isStr(tag) || typeof tag === 'number') ? own(this.tags, tag) : undefined;
      if (!T(Tg)) return [];
      if (Tg.gi != null) return [[Tg.gi, this.tmax(tag)]];
      let out = [];
      for (const x of Tg.anyOf || []) {
        if (isStr(x) && !seen.includes(x)) out = out.concat(this.leaves(x, seen.concat([tag])));
        else if (isObj(x) && x.gi != null) out.push([x.gi, x.tmax != null ? this.tmax(null, x.tmax) : null]);
      }
      if (Tg.tmax != null) {
        const t = this.tmax(tag);
        out = out.map(([gi, tm]) => [gi, tm == null ? t : (T(t) ? Math.min(tm, t) : tm)]);
      }
      return out;
    }
    spec(tags) {
      if (tags.length > 1) {
        const nm_ = new Set(tags.map(t => this.name(t)));
        const bt = Object.keys(this.tags).find(k => {
          const Tg = this.tags[k];
          return isObj(Tg) && Tg.gi == null && (Tg.shown != null || T(Tg.shownBy)) && Array.isArray(Tg.anyOf) && Tg.anyOf.every(isStr)
            && new Set(Tg.anyOf).size === nm_.size && [...new Set(Tg.anyOf)].every(x => nm_.has(x)) && T(shown_leaves(this.tags, k, this.vid, this.params));
        });
        if (bt !== undefined) tags = [bt];
      }
      const xs = [];
      for (const t of tags) for (const [gi, tm] of this.leaves(this.name(t))) {
        if (!xs.map(x => x.gi).includes(gi)) { const o = { gi }; if (T(tm)) o.tmax = tm; xs.push(o); }
      }
      if (!xs.length) return null;
      if (xs.length === 1) return xs[0];
      const out = { anyOf: xs };
      const lb = tags.map(t => g(gd(this.tags, this.name(t), {}) || {}, 'label'));
      if (tags.length === 1 && isObj(lb[0]) && T(lb[0].kr)) out.label = { kr: lb[0].kr, en: or_(g(lb[0], 'en'), lb[0].kr) };
      if (tags.length === 1) {
        let sh = this.shown(tags[0], this.nth(this.name(tags[0]), this._cur));
        const T0 = own(this.tags, this.name(tags[0])) || {};
        const lf = (T0.anyOf || []).filter(isStr);
        const hit = [];
        for (const l of this._cur || []) {
          if (l.m === 'j') continue;
          for (const t_ of (l.tags || []).slice(0, 1)) if (lf.includes(t_) && this.leaves(t_).length === 1) hit.push(this.leaves(t_)[0][0]);
        }
        if (T(sh) && hit.length && hit[hit.length - 1] !== sh.gi) {
          const f = this.leaves(tags[0]).find(([gi_]) => gi_ === hit[hit.length - 1]);
          const tm_ = f ? f[1] : null;
          sh = { gi: hit[hit.length - 1] }; if (T(tm_)) sh.tmax = tm_;
        }
        if (T(sh) && xs.map(x => x.gi).includes(sh.gi)) {
          const x0 = xs.find(x => x.gi === sh.gi);
          const s = { gi: sh.gi };
          if (T(g(sh, 'tmax'))) s.tmax = sh.tmax; else if (T(g(x0, 'tmax'))) s.tmax = x0.tmax;
          if (T(g(sh, 'tmin'))) s.tmin = sh.tmin;
          out.shown = s;
          const on = this.on_gis(this._cur, tags[0]);
          out.alt = xs.filter(x => x.gi !== sh.gi && !on.has(x.gi)).map(x => x.gi);
        }
      }
      return out;
    }
  }

  function _room(G_, prev) {
    const cap = or_(g(G_.g, 'cap'), g(G_.src || {}, 'cap'), {});
    const n = { p: 0, s: 0 };
    for (const l of prev || []) if (l.s === 'p' || l.s === 's') n[l.s] += 1;
    return ['p', 's'].filter(sd => n[sd] < or_(g(cap, sd), 3));
  }

  const _strs = a => (a || []).filter(isStr);

  function _target(G_, n, prev, cur, last_bone) {
    const sn = G_.sn(n.id) || {};
    G_._cur = cur;
    const act = or_(g(n, 'act'), n.kind === 'cleanup' ? 'remove' : null);
    let [nw, gone] = _diff(prev, cur);
    let om = (n.omens || []).slice();
    let t = {};
    let okc = [];
    for (const e of sn.edges || []) { if (e.res === 'ok' && T(e.if)) { okc = _cond_tags(e.if, []); break; } }
    okc = okc.filter(x => own(G_.tags, G_.name(x)) !== undefined).map(x => G_.name(x));
    nw = nw.filter(l => l.s === 'p' || l.s === 's');
    const keep_any = (sn.edges || []).some(e => e.res === 'ok' && e.if != null && _simp(e.if, G_.params) === true) || T(G_._kall);
    const CHX = ['chaos', 'exalt', 'transmute', 'augment', 'regal'];
    const omSide = () => _side_of_omens(om, 'Exaltation') || _side_of_omens(om, 'Coronation');
    if (keep_any && CHX.includes(act)) {
      const rm = _room(G_, prev);
      const sd = or_(nw.length ? nz(nw[0].s) : null, _side_of_omens(om, 'Exaltation'), _side_of_omens(om, 'Coronation'), rm.length === 1 ? rm[0] : 'p');
      const k = (act === 'exalt' && om.includes('Omen_of_Greater_Exaltation')) ? 2 : 1;
      if (k > 1) {
        const ns = nw.map(l => l.s).filter(s => s === 'p' || s === 's');
        t = { junk: ns.length === k ? ns : Array(k).fill(sd) };
        if (!T(omSide()) && rm.length > 1) t.anySide = true;
      } else t = act !== 'chaos' ? { junk: sd } : { asIs: true, junk: sd };
      return [act, om, t, last_bone];
    }
    if (CHX.includes(act)) {
      let tagged = nw.filter(l => T(l.tags));
      if (T(okc) && !tagged.length && T(G_.spec(okc))) tagged = [{ tags: okc, s: null }];
      const junk = nw.filter(l => (l.m == null || l.m === 'j' || l.m === 'n') && !T(l.tags));
      const showS = _strs(n.show);
      if (tagged.length) {
        const show = showS;
        const srcShow = ((G_.src || {}).nodes || []).find(x => x.id === n.id);
        if (tagged.length > 1 && act === 'chaos' && show.length && T(G_.spec(show))) t = Object.assign({}, G_.spec(show));
        else if (tagged.length > 1 && act === 'exalt' && show.length && show.length < tagged.length && show.every(x => T(G_.spec([x]))) && dumps(srcShow ? nz(srcShow.show) : null) !== dumps(nz(n.show))) {
          const parts = show.map(x => G_.spec([x])); t = parts.length === 1 ? Object.assign({}, parts[0]) : { all: parts };
          t.plusJunk = tagged.length - show.length;
        } else if (tagged.length > 1) {
          const parts = tagged.map(l => G_.spec(l.tags)); t = { all: parts.filter(p => T(p)) };
        } else {
          const sp = or_(show.length ? G_.spec(show) : null, G_.spec(tagged[0].tags));
          if (T(sp)) t = Object.assign({}, sp);
        }
        if (act === 'chaos') {
          const gj = gone.find(l => l.m === 'j'); const rep = gj ? nz(gj.s) : null;
          if ((rep === 'p' || rep === 's') && !HAS.call(t, 'all')) t.replace = rep;
          if (T(n.trim) && !T(om)) om = ['Omen_of_Whittling'];
        }
      } else if (junk.length && n.pos[0] !== 0 && showS.length && T(G_.spec(showS))) {
        t = Object.assign({}, G_.spec(showS));
      } else if (junk.length) {
        const sides = junk.map(l => l.s);
        t = { junk: sides.length > 1 ? sides : sides[0] };
        if (act === 'chaos') t.asIs = true;
        if (sides.length > 1 && !T(omSide()) && _room(G_, prev).length > 1) t.anySide = true;
      } else if (act === 'chaos' && showS.length && T(G_.spec(showS))) {
        t = Object.assign({}, G_.spec(showS));
        const er = om.includes('Omen_of_Dextral_Erasure') ? 's' : om.includes('Omen_of_Sinistral_Erasure') ? 'p' : null;
        if (er) t.replace = er;
      } else if (act === 'chaos') {
        const er = om.includes('Omen_of_Dextral_Erasure') ? 's' : om.includes('Omen_of_Sinistral_Erasure') ? 'p' : null;
        const gs = gone.find(l => l.s === 'p' || l.s === 's');
        t = { asIs: true, junk: or_(er, gs ? gs.s : 'p') };
      } else {
        const rm = _room(G_, prev);
        const ns0 = nw.find(l => l.s === 'p' || l.s === 's');
        const sd = or_(_side_of_omens(om, 'Exaltation'), _side_of_omens(om, 'Coronation'), ns0 ? ns0.s : null, rm.length === 1 ? rm[0] : 'p');
        const k = om.includes('Omen_of_Greater_Exaltation') ? 2 : 1;
        if (k > 1 && !T(omSide())) {
          const ns = nw.map(l => l.s).filter(s => s === 'p' || s === 's');
          t = { junk: ns.length === k ? ns : Array(k).fill(sd) };
          if (rm.length > 1) t.anySide = true;
        } else t = { junk: k > 1 ? Array(k).fill(sd) : sd };
      }
    } else if (act === 'essence') {
      const nl = nw.find(l => T(l.tags));
      if (nl) t = Object.assign({}, G_.spec(nl.tags) || {});
      else if (T(okc)) t = Object.assign({}, G_.spec(okc) || {});
      if (nl && T(okc)) {
        const ks = G_.spec(okc);
        const kg = new Set(or_(g(ks || {}, 'anyOf'), [ks || {}]).map(x => g(x, 'gi')));
        if (T(ks) && !kg.has(g(t, 'gi')) && !(t.anyOf || []).some(x => kg.has(g(x, 'gi')))) t.keep = ks;
      }
      const mk = nw.find(l => String(or_(g(l, 'kr'), '')).includes('징표'));
      if (mk && !T(t)) {
        const mg = g(G_.spec(mk.tags || []) || {}, 'gi');
        if (mg != null) t = { mark: { gi: mg } };
        else G_._marktx = { kr: or_(g(mk, 'kr'), ''), en: or_(g(mk, 'en'), g(mk, 'kr'), '') };
      }
    } else if (act === 'desecrate') {
      const st0 = (n.showText || []).find(l => l.s === 'p' || l.s === 's');
      const sd = or_(_side_of_omens(om, 'Necromancy'), nw.length ? nz(nw[0].s) : null, st0 ? nz(st0.s) : null, 'p');
      G_._lord = om.includes('Omen_of_the_Liege') ? 'amanamu' : om.includes('Omen_of_the_Sovereign') ? 'ulaman' : om.includes('Omen_of_the_Blackblooded') ? 'kurgal' : null;
      G_._lus = sd;
      t = { unrev: sd };
      if (T(sn.fromMark) || T(g(sn.target || {}, 'fromMark'))) t.fromMark = true;
      last_bone = or_(g(n, 'cur'), last_bone);
    } else if (act === 'reveal') {
      let want = or_(g(sn, 'want'), g(n, 'want'), nz((T(n.show) ? n.show : [null])[0]));
      const showEmpty = Array.isArray(n.show) && !n.show.length;
      if (showEmpty && HAS.call(sn || {}, 'show') && !T(sn.show)) want = null;
      let wl = Array.isArray(want) ? want : T(want) ? [want] : [];
      wl = or_(wl.map(w => G_.name(w)), (want == null && showEmpty) ? [] : okc);
      const nl = nw.find(l => T(l.tags));
      const asis_v = (want == null && showEmpty) || keep_any;
      if (keep_any) wl = [];
      let sp = or_(G_.spec(wl.filter(isStr)), asis_v ? null : (nl ? G_.spec(nl.tags) : null));
      let ws = null;
      outer: for (const w of wl) {
        if (!isStr(w)) continue;
        for (const [gi] of G_.leaves(w)) for (const Tg of Object.values(G_.tags)) if (isObj(Tg) && Tg.gi === gi && (Tg.s === 'p' || Tg.s === 's')) { ws = Tg.s; break outer; }
      }
      const sd = or_(g(nl || {}, 's'), G_._lus, ws, gone.length ? nz(gone[0].s) : null, 'p');
      if (T(sp) && T(sp.anyOf)) {
        const have = new Set();
        for (const l of prev || []) {
          if (l.m === 'j' || l.m === 'u') continue;
          for (const tg of l.tags || []) { const lv = G_.leaves(G_.name(tg)); for (const [gi] of lv) if (lv.length === 1) have.add(gi); }
        }
        const xs = sp.anyOf.filter(x => !have.has(g(x, 'gi')));
        if (xs.length && xs.length < sp.anyOf.length) {
          sp = xs.length === 1 ? Object.assign({}, xs[0]) : Object.assign({}, sp, { anyOf: xs });
          if (T(sp.alt)) sp.alt = sp.alt.filter(x => !have.has(x));
          if (T(sp.shown) && have.has(sp.shown.gi)) { delete sp.shown; delete sp.alt; }
        }
      }
      t = { reveal: or_(sp, { anyOf: [] }), side: sd };
      if (T(last_bone)) t.bone = last_bone;
      if (T(G_._lord)) t.lord = G_._lord;
      if (!T(sp)) {
        t.asIs = true; t.anyReveal = true;
        const tx_ = or_((or_(n.showText, sn.showText, [])).find(x => isObj(x) && T(x.kr) && !_is_tip(x)) || null, g(n, 'goal'), g(sn, 'goal'));
        if (asis_v) t.keepReveal = true;
        else if (T(tx_)) t.revealTx = { kr: tx_.kr, en: or_(g(tx_, 'en'), tx_.kr) };
      }
    } else if (act === 'annul' || act === 'remove') {
      if (gone.some(l => l.m === 'd' || l.m === 'u' || String(or_(g(l, 'kr'), '')).includes('훼손'))) t = { removeDes: true };
      else {
        const sd = or_(_side_of_omens(om, 'Annulment'), (gone.length && (gone[0].s === 'p' || gone[0].s === 's')) ? gone[0].s : null, 'any');
        t = { removeJunk: sd };
      }
    } else if (act === 'fracture') {
      const fl = cur.filter(l => l.m === 'f' && T(l.tags));
      const nf0 = fl.filter(l => !prev.some(x => _key(x) === _key(l)));
      const nf = nf0.length ? nf0 : fl;
      const sp = or_(nf.length ? G_.spec(nf[0].tags) : null, T(okc) ? G_.spec(okc) : null);
      if (T(sp)) t = Object.assign({}, sp);
    } else if (act === 'quality') {
      const txt = ['goal', 'label'].map(k => or_(g(or_(g(sn, k), g(n, k), {}), 'kr'), '')).join(' ');
      const mq = /(\d+)\s*%/.exec(txt);
      t = { quality: or_(g(sn, 'q'), mq ? parseInt(mq[1], 10) : null, g(sn, 'count'), 20) };
    } else if (act === 'rune') {
      const rn = or_(g(n, 'rune'), g(sn, 'rune'));
      t = { rune: isObj(rn) ? rn : { kr: or_(rn, ''), en: or_(rn, '') } };
      if (T(sn.swapAstrid) || T(n.swapAstrid)) t.swapAstrid = true;
      const k = or_(g(sn, 'count'), g(n, 'count'));
      if (typeof k === 'number' && Number.isInteger(k) && k > 1) t.runeCount = k;
      if (T(sn.fill) || T(n.fill)) t.runeFill = true;
    }
    return [act, om, t, last_bone];
  }

  function _state(G_, lines, final_tags) {
    const out = []; const cnt = { p: 0, s: 0 }; const seen_ = {};
    for (const l of lines) {
      if (l.s === 'r') continue;
      let sd = nz(l.s);
      if (sd === 'x') sd = cnt.p <= cnt.s ? 'p' : 's';
      if (sd !== 'p' && sd !== 's') continue;
      const m = nz(l.m); const tags = (l.tags || []).map(x => G_.name(x));
      if (m === 'u') { out.push({ unrev: true, junk: true, side: sd }); cnt[sd] += 1; continue; }
      const tg0 = tags.find(x => final_tags.has(x));
      const tag = tg0 !== undefined ? tg0 : (tags.length ? tags[0] : null);
      let lv = T(tag) ? G_.leaves(tag) : [];
      if (T(tag) && m !== 'j') {
        const k = gd(seen_, tag, 0); seen_[tag] = k + 1;
        const sh = G_.shown(tag, k);
        if (T(sh)) { const f = lv.find(([gi]) => gi === sh.gi); lv = [[sh.gi, or_(g(sh, 'tmax'), f ? f[1] : null)]]; }
      }
      if (m === 'j' || !lv.length) {
        const o = { junk: true, side: sd }; if (m === 'd') o.des = true;
        out.push(o); cnt[sd] += 1; continue;
      }
      const [gi, tm] = lv[0];
      const e = { gi, side: sd };
      if (T(tm)) e.tmax = tm;
      if (m === 'f') e.fr = true;
      if (m === 'd') e.des = true;
      if (m === 'c' || g(own(G_.tags, tag) || {}, 'sec') === 'e' || /(에센스|합금|Essence[^)]*|Alloy)\)/.test(or_(g(l, 'kr'), ''))) e.ess = true;
      out.push(e); cnt[sd] += 1;
    }
    return out;
  }

  function _version(sim, tier) {
    const gr = sim.graph;
    const F = (gr.finals || []).find(f => or_(g(f, 'tier'), f.id) === tier) || null;
    const V = F ? ((gr.versions || []).find(v => v.id === F.id) || null) : null;
    const S = V ? ((sim.strategies || []).find(x => !T(x.hidden) && Object.keys(V.params).every(k => pyStr(g(x.params, k)) === pyStr(V.params[k]))) || null) : null;
    return [F, V, S];
  }

  /* ---------- Walk: 한 등급으로 본 플로우차트 ---------- */
  class Walk {
    constructor(sim, V, S) {
      this.P = V.params; this.res = S.res; this.sim = sim; this.vid = nz(V.id);
      this.nodes = _over(sim.graph.nodes, this.P).map(n => (isObj(n.goalBy) && T(g(n.goalBy, V.id))) ? Object.assign({}, n, { goal: n.goalBy[V.id] }) : n);
      this.by = {}; for (const n of this.nodes) this.by[n.id] = n;
      this.E = this.res.edges || {};
      this.EI = this.res.edgesI || {};
      this._eik = {};
    }
    B(id) { return own(this.by, id); }
    st(nid) { return nz(own(this.res.nodes || {}, nid)); }
    seen(nid) { const t = this.st(nid); return T(t) && (t.visits || 0) > 0 && !this.skipall(nid); }
    skipall(nid) {
      const t = this.st(nid) || {}; const v = t.visits || 0;
      return v > 0 && (t.skips || 0) >= v * 0.999 && !T(t.use || {}) && T(g(this.B(nid) || {}, 'skipTo'));
    }
    via(nid) {
      const n = this.B(nid) || {};
      return gd(n, 'pos', [0])[0] !== 0 && (n.kind === 'cleanup' || n.act === 'annul');
    }
    outs(n) {
      const res = [];
      (n.edges || []).forEach((e, i) => {
        if (!_when(e, this.P)) return;
        const to = e.to; const lab = _strip(g(e, 'label')); const cls = nz(e.res);
        const Tn = this.B(to);
        if (T(Tn) && Tn.kind === 'choice') {
          const opt = pyStr(g(this.P, Tn.param)); const to2 = g(Tn.options || {}, opt);
          if (!T(to2)) return;
          res.push([e, to2, or_(g(Tn.edgeLabels || {}, opt), lab), or_(g(g(Tn.optStyle || {}, opt) || {}, 'res'), cls), to, i]);
          return;
        }
        res.push([e, to, lab, cls, to, i]);
      });
      return res;
    }
    cnt(a, b) { return or_(gd(this.E, `${pyStr(a)}>${pyStr(b)}`, 0), 0); }
    exits(n, outs) {
      outs = outs == null ? this.outs(n) : outs;
      const sx = outs.find(x => x[1] === n.id && x[3] !== 'ok');
      const si = sx ? sx[5] : null;
      if (si === null) return new Set();
      if (!outs.some(x => x[3] === 'ok' && x[5] < si)) return new Set();
      return new Set(outs.filter(x => x[3] === 'ok' && x[1] !== n.id && (T(x[0].exit) || (x[5] > si && T(x[0].hide)))).map(x => x[5]));
    }
    ec(nid, x, outs) {
      if (!HAS.call(this._eik, nid)) { const p = nid + '#'; this._eik[nid] = Object.keys(this.EI).some(k => k.startsWith(p)); }
      if (this._eik[nid]) return or_(gd(this.EI, `${nid}#${x[5]}`, 0), 0);
      const first = outs.find(y => y[4] === x[4]);
      return first === x ? this.cnt(nid, x[4]) : 0;
    }
  }

  const SIDE_W = { p: ['접두', 'prefix'], s: ['접미', 'suffix'] };

  function _clean_name(t) {
    t = (t || '').replace(/\s*\([^)]*[가-힣A-Za-z][^)]*\)\s*$/, '');
    t = t.replace(/[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\)(\s*~\s*[+\-]?\(\s*[\d.]+\s*[—–-]\s*[\d.]+\s*\))?(?!%?[의만로을를에으])%?/g, '');
    t = t.replace(/\s+/g, ' ').replace(/^[ +~]+|[ +~]+$/g, '');
    return t || null;
  }

  /* ---------- Cond: 갈래 조건 → 짧은 명사구 ---------- */
  class Cond {
    constructor(G_, sim, src, cls, grp) {
      this.G = G_; this.cls = cls; this._grpf = grp; this._grp = null;
      this.conds = or_(g(src || {}, 'conds'), g(sim.graph, 'conds'), {});
      this.nm = {};
      for (const n of sim.graph.nodes || []) for (const l of n.item || []) {
        const tg = l.tags || [];
        if (tg.length === 1 && !HAS.call(this.nm, tg[0])) {
          const k = _clean_name(nz(l.kr)); const e = _clean_name(nz(l.en));
          if (k) this.nm[G_.name(tg[0])] = [k, e || k];
        }
      }
    }
    name(tag) {
      tag = isStr(tag) ? this.G.name(tag) : tag;
      if (isObj(tag)) return null;
      const Tg = own(this.G.tags, tag) || {};
      if (T(Tg.label)) return [Tg.label.kr, Tg.label.en];
      if (HAS.call(this.nm, tag)) return this.nm[tag];
      if (Tg.gi != null && T(this.cls)) {
        if (this._grp === null) this._grp = this._grpf(this.cls) || [];
        const gr = (Tg.gi >= 0 && Tg.gi < this._grp.length) ? this._grp[Tg.gi] : null;
        if (T(gr) && T(gr.t)) {
          const k = _clean_name(gr.t[0][4]); const e = _clean_name(gr.t[0][5]);
          if (k) return [k, e || k];
        }
      }
      const subs = (Tg.anyOf || []).filter(isStr);
      if (subs.length > 1 && subs.length <= 2) {
        const ns = subs.map(x => this.name(x));
        if (ns.every(x => T(x))) return [ns.map(x => x[0]).join('·'), ns.map(x => x[1]).join(' or ')];
      }
      return null;
    }
    atoms(c, neg) {
      neg = !!neg;
      if (c == null) return [];
      if (!isObj(c)) return [];
      if (HAS.call(c, 'ref')) return this.atoms(nz(own(this.conds, c.ref)), neg);
      if (HAS.call(c, 'param')) { const ok = _pmatch(c.param, this.G.params); return ok !== neg ? [] : null; }
      if (HAS.call(c, 'not')) return this.atoms(c.not, !neg);
      if (HAS.call(c, 'all') && !neg) {
        let out = [];
        for (const x of c.all) { const a = this.atoms(x); if (a === null) return null; out = out.concat(a); }
        return out;
      }
      if (HAS.call(c, 'any') && !neg) {
        const parts = [];
        for (const x of c.any) { const a = this.atoms(x); if (a === null) continue; if (!a.length) return []; parts.push(a); }
        if (!parts.length) return null;
        if (parts.length > 3 || parts.some(p => p.length > 1)) return [];
        return [[['any'].concat(parts.map(p => p[0][0])), parts.map(p => p[0][1]).join(' 또는 '), parts.map(p => p[0][2]).join(' or '), 'any']];
      }
      if ((HAS.call(c, 'all') || HAS.call(c, 'any')) && neg) return [];
      const k = Object.keys(c)[0]; const v = c[k];
      const S = sd => gd(SIDE_W, sd, ['', '']);
      const N = t => this.name(!isObj(t) || !HAS.call(t, 'tag') ? t : t.tag);
      const key = [k, dumps(v, true), neg];
      let a = null, n_;
      const and = (x, y) => T(x) ? y : x;
      if (k === 'has') { n_ = N(v); a = and(n_, neg ? [`${n_ && n_[0]} 없음`, `no ${n_ && n_[1]}`, 'nohas'] : [`${n_ && n_[0]} 있음`, `has ${n_ && n_[1]}`, 'has']); }
      else if (k === 'added') { n_ = N(v); a = and(n_, neg ? [`${n_ && n_[0]} 안 붙음`, `${n_ && n_[1]} not added`, 'x'] : [`${n_ && n_[0]} 붙음`, `${n_ && n_[1]} added`, 'added']); }
      else if (k === 'removed') { n_ = N(v); a = and(n_, neg ? [`${n_ && n_[0]} 남음`, `${n_ && n_[1]} kept`, 'x'] : [`${n_ && n_[0]} 지워짐`, `${n_ && n_[1]} removed`, 'x']); }
      else if (k === 'fractured') { n_ = N(v); a = and(n_, neg ? ['다른 옵션 분열', 'another mod fractured', 'x'] : [`${n_ && n_[0]} 분열`, `${n_ && n_[1]} fractured`, 'x']); }
      else if (k === 'full') { const s_ = S(v); a = neg ? [`${s_[0]} 빈자리 있음`, `open ${s_[1]}`, 'x'] : [`${s_[0]} 꽉 참`, `${s_[1]}es full`, 'x']; }
      else if (k === 'sideLt') {
        const s_ = S(g(v, 'side')); const m = pyInt(or_(g(v, 'n'), 1));
        if (neg) a = [`${s_[0]} ${m}개 이상`, `${m}+ ${s_[1]}es`, 'x'];
        else a = m <= 1 ? [`${s_[0]} 없음`, `no ${s_[1]}`, 'x'] : [`${s_[0]} ${m - 1}개 이하`, `≤${m - 1} ${s_[1]}es`, 'x'];
      } else if (k === 'count') {
        n_ = N(g(v, 'tag')); const m = pyStr(g(v, 'min'));
        if (T(n_) && / 1개$/.test(n_[0])) n_ = [n_[0].slice(0, -3), n_[1].replace(/^(one|1) /, '')];
        a = and(n_, neg ? [`${n_ && n_[0]} ${m}개 미만`, `fewer than ${m} ${n_ && n_[1]}`, 'x'] : [`${n_ && n_[0]} ${m}개`, `${m}× ${n_ && n_[1]}`, 'has']);
      } else if (k === 'unrevSide') { const s_ = S(v); a = neg ? null : [`${s_[0]} 미공개 훼손`, `unrevealed ${s_[1]}`, 'x']; }
      else if (k === 'unrev') { const yes = T(v) !== neg; a = yes ? ['미공개 훼손 있음', 'unrevealed desecration', 'x'] : ['미공개 훼손 없음', 'no unrevealed desecration', 'x']; }
      else if (k === 'des') { const yes = T(v) !== neg; a = yes ? ['훼손 옵션 있음', 'desecrated mod', 'x'] : ['훼손 옵션 없음', 'no desecrated mod', 'x']; }
      else if (k === 'desSide') { const s_ = S(v); a = neg ? [`${s_[0]} 훼손 옵션 없음`, `no desecrated ${s_[1]}`, 'x'] : [`${s_[0]} 훼손 옵션`, `desecrated ${s_[1]}`, 'x']; }
      else if (k === 'sideAll') {
        const s_ = S(g(v, 'side')); n_ = N(g(v, 'tag'));
        if (neg) a = [`${s_[0]}에 잡옵`, `junk ${s_[1]}`, 'x'];
        else a = and(n_, [`${s_[0]} 모두 ${n_ && n_[0]}`, `all ${s_[1]}es ${n_ && n_[1]}`, 'x']);
      } else if (k === 'junk') { const s_ = S(g(v, 'side')); a = neg ? [`${s_[0]} 잡옵 없음`, `no junk ${s_[1]}`, 'x'] : [`${s_[0]}에 잡옵`, `junk ${s_[1]}`, 'x']; }
      else if (k === 'whittleSafe') a = neg ? ['가장 낮은 옵션이 지킬 옵션', 'lowest mod is a keeper', 'x'] : ['가장 낮은 옵션이 잡옵', 'lowest mod is junk', 'x'];
      else if (k === 'allMods') { n_ = N(v); a = neg ? null : and(n_, [`모두 ${n_ && n_[0]}`, `all ${n_ && n_[1]}`, 'x']); }
      else if (k === 'famBlock') a = neg ? null : ['같은 계열 옵션이 막음', 'blocked by the same family', 'x'];
      return T(a) ? [[key].concat(a)] : [];
    }
  }

  function _label(atoms, drop) {
    if (!T(atoms)) return null;
    const ds = new Set([...(drop || [])].map(kstr));
    let xs = atoms.filter(a => !ds.has(kstr(a[0])));
    if (!xs.length) xs = atoms.slice();
    const hs = atoms.filter(a => a[3] === 'has');
    if (hs.length >= 3) return { kr: '목표 옵션 모두 있음', en: 'all target mods' };
    const seen = []; let out = [];
    for (const a of xs) { if (seen.includes(a[1])) continue; seen.push(a[1]); out.push(a); }
    const fullS = new Set(out.filter(a => a[1].endsWith(' 꽉 참')).map(a => a[1].split(' ')[0]));
    out = out.filter(a => !(a[0][0] === 'sideLt' && fullS.has(a[1].split(' ')[0])));
    out = out.slice(0, 2);
    if (out.length === 2 && out[0][1].length + out[1][1].length > 26) out = out.slice(0, 1);
    return { kr: out.map(a => a[1]).join(', '), en: out.map(a => a[2]).join(', ') };
  }

  function _simp(c, P) {
    if (!isObj(c)) return c;
    if (HAS.call(c, 'param')) return _pmatch(c.param, P);
    if (HAS.call(c, 'not')) { const x = _simp(c.not, P); return typeof x === 'boolean' ? !x : { not: x }; }
    for (const k of ['all', 'any']) {
      if (HAS.call(c, k)) {
        let xs = c[k].map(x => _simp(x, P));
        if (k === 'all' && xs.some(x => x === false)) return false;
        if (k === 'any' && xs.some(x => x === true)) return true;
        xs = xs.filter(x => typeof x !== 'boolean');
        return !xs.length ? (k === 'all') : xs.length === 1 ? xs[0] : { [k]: xs };
      }
    }
    return c;
  }

  function _neg_atoms(c, CD) {
    if (!isObj(c)) return null;
    if (HAS.call(c, 'not')) { const a = CD.atoms(c.not); return T(a) ? a : null; }
    if (HAS.call(c, 'all')) return null;
    if (HAS.call(c, 'any')) {
      let out = [];
      for (const x of c.any) { const a = _neg_atoms(x, CD); if (a === null) return null; out = out.concat(a); }
      return out;
    }
    const a = CD.atoms({ not: c }); return T(a) ? a : null;
  }

  function _rest_atoms(W, n, r, G_, CD) {
    const se = (G_.sn(n.id) || {}).edges || [];
    const i = gd(r, '_i', 999);
    if (!(0 <= i && i < se.length) || se[i].if != null) return null;
    const out = []; const ks = new Set();
    for (const e of se.slice(0, i).reverse()) {
      const c = _simp(nz(e.if), G_.params);
      if (c === false || c == null) continue;
      if (c === true) return null;
      if (!((or_(g(W.E, n.id + '>' + pyStr(nz(e.to))), 0)) > 0)) continue;
      for (const a of _neg_atoms(c, CD) || []) { const kk = kstr(a[0]); if (!ks.has(kk)) { ks.add(kk); out.push(a); } }
    }
    return out.length ? out : null;
  }

  /* ---------- 갈래(routes) ---------- */
  function _routes(W, n, valid, G_, CD) {
    const t = W.st(n.id) || {};
    function dest(to, d) {
      d = d || 0;
      const Tn = W.B(to) || {};
      if (to === n.id) return 'self';
      const Ts = Object.assign({}, G_ ? (G_.sn(to) || {}) : {}, Tn);
      if (Tn.kind === 'exit' && T(Ts.simTo) && (Ts.variant === 'ok' || T(Ts.swapFracture)) && d < 5) return dest(Ts.simTo, d + 1);
      if (Tn.kind === 'base' || Tn.kind === 'exit') return 'restart';
      if (Tn.kind === 'done') return 'done';
      return to;
    }
    const ok_dest = d => d === 'self' || d === 'done' || d === 'restart' || valid.has(d);
    function src_if(nid, i, to) {
      const se = G_ ? ((G_.sn(nid) || {}).edges || []) : [];
      const ii = i < 0 ? se.length + i : i;
      if (!(i < se.length && ii >= 0 && se[ii].to === to)) return '?';
      const e = se[ii];
      if (e.if == null && T(e.lost)) return { removed: e.lost };
      return nz(e.if);
    }
    function outs_of(N_) {
      const o = W.outs(N_);
      if (o.length) return o.map(x => [x, W.ec(N_.id, x, o)]);
      let nx = Object.keys(W.E).filter(k => k.startsWith(N_.id + '>')).map(k => [k.slice(k.indexOf('>') + 1), W.E[k]]);
      if (!nx.length && T(N_.next)) nx = [[N_.next, 1]];
      return nx.map(([to, c]) => [[{ to }, to, null, null, to, -1], c]);
    }
    const leaves = [];
    function walk(N_, frac, first, chain, vias, depth, seen) {
      const os_ = outs_of(N_); const tot = sum(os_.map(p => p[1]));
      const loop = sum(os_.filter(([x]) => x[1] === N_.id && N_ !== n).map(p => p[1]));
      const vis = os_.filter(([x]) => !(x[1] === N_.id && N_ !== n));
      const tv = sum(vis.map(p => p[1]));
      if (N_ !== n && loop > 0 && vias.length && tot / Math.max(1e-9, tv) >= 1.05) vias[vias.length - 1] = Object.assign({}, vias[vias.length - 1], { n: pyRound(tot / Math.max(1e-9, tv), 2) });
      for (const [x, c] of vis) {
        if (tv > 0 && c <= 0) continue;
        if (tv <= 0 && (T(x[0].hide) || vis.length > 1)) continue;
        const sh = frac * (tv > 0 ? c / tv : 1.0);
        const fx = first || [N_.id, x]; const px = N_ === n ? chain : chain.concat([[N_.id, x]]);
        const to = x[1]; const d = dest(to); const Tn = W.B(to);
        if (ok_dest(d) || !T(Tn) || depth >= 5 || seen.has(to)) {
          leaves.push({ first: fx, chain: px, to: ok_dest(d) ? d : 'state', share: sh, n: N_ === n ? pyRound(c, 3) : null, vias: vias.slice(), lab: x[2], cls: x[3] });
          continue;
        }
        const nv = vias.slice();
        if (W.via(to)) {
          let vo = (Tn.omens || []).slice();
          if (Tn.kind === 'cleanup') vo = vo.concat(['Omen_of_Sinistral_Annulment', 'Omen_of_Dextral_Annulment'].filter(k => T(g((W.st(to) || {}).use || {}, k)) && !vo.includes(k)));
          const v = { cur: or_(g(Tn, 'cur'), 'Orb_of_Annulment') }; if (vo.length) v.omens = vo; v.vid = to;
          nv.push(v);
        }
        walk(Tn, sh, fx, px, nv, depth + 1, new Set([...seen, to]));
      }
    }
    walk(n, 1.0, null, [], [], 0, new Set([n.id]));
    const multi = {};
    for (const L of leaves) if (L.chain.length) { const k = L.first[1][5]; (multi[k] = multi[k] || new Set()).add(L.to); }
    const vres = {};
    for (const x of W.outs(n)) if (!T(x[0].hide) && T(x[3]) && !HAS.call(vres, x[4])) vres[x[4]] = x[3];
    const ntot = sum(outs_of(n).map(p => p[1]));
    const XS = W.exits(n);
    let out = [];
    for (const L of leaves) {
      const e0 = L.first[1];
      const cls0 = T(e0[0].hide) ? or_(nz(own(vres, e0[4])), e0[3]) : e0[3];
      const isx = L.first[0] === n.id && XS.has(e0[5]);
      const ch = L.chain; const post = ch.length ? ch[ch.length - 1] : null;
      const cls_post = post ? post[1][3] : null;
      const lc = ch.slice().reverse().find(y => T(y[1][2])); const lab_ch = lc ? lc[1][2] : null;
      const main = L.to === 'self' || !post || cls_post !== 'fail';
      let needc = false; let lab;
      const anyN = L.vias.some(v => T(v.n));
      if (!post) lab = e0[2];
      else if (L.to === 'self') lab = anyN ? or_(e0[2], lab_ch) : or_(lab_ch, e0[2]);
      else if ((multi[e0[5]] ? multi[e0[5]].size : 0) >= 2) { lab = lab_ch; needc = !T(lab); }
      else lab = anyN ? or_(e0[2], lab_ch) : or_(lab_ch, e0[2]);
      const no = cls0 === 'fail' || (post && !main) || L.to === 'self' || !!(T(lab) && /^(빗나감|실패)/.test(or_(g(lab, 'kr'), '')));
      const r = { cls: no ? 'no' : 'ok', lab: nz(lab), to: L.to, share: L.share, n: pyRound(L.share * ntot, 3), res: or_(cls0, cls_post), _i: (e0[5] != null && e0[5] >= 0) ? e0[5] : 999 };
      if (isx) {
        r.exit = true;
        if (!T(lab)) {
          const sx = W.outs(n).find(x => x[1] === n.id && x[3] !== 'ok'); const si = sx ? sx[5] : -1;
          let c = si >= 0 ? src_if(n.id, si, n.id) : '?';
          c = (G_ && isObj(c)) ? _simp(c, G_.params) : c;
          const lb = (CD && isObj(c)) ? _label(CD.atoms({ not: c }) || []) : null;
          lab = { kr: (lb ? lb.kr : '더 다시 할 수 없음') + ' — 목표 없이', en: (lb ? cap1(lb.en) : 'No more retries') + ': without the goal' };
        }
        r.lab = lab;
      }
      if (needc) { r._c = true; r._e0 = e0[2]; r._pr = cls_post; }
      if (L.vias.length) {
        const v = Object.assign({}, L.vias[0]);
        if (L.vias.length > 1) v.then = L.vias.slice(1);
        r.via = v; r.vo = true;
      }
      if (post && !main) r.lost = true;
      if (CD) {
        const c0 = L.first[1][5] >= 0 ? src_if(L.first[0], L.first[1][5], L.first[1][4]) : '?';
        const a0 = c0 !== '?' ? CD.atoms(c0) : [];
        r._a = a0 || [];
        if (c0 !== '?' && L.first[0] === n.id) r._if = c0;
        if (post) {
          let ap = post[1][5] >= 0 ? CD.atoms(src_if(post[0], post[1][5], post[1][4])) : [];
          const a0k = new Set((a0 || []).map(b => kstr(b[0])));
          ap = (ap || []).filter(a => !a0k.has(kstr(a[0])));
          const Pn = W.B(post[0]) || {};
          const same = deq((n.edges || []).map(e => nz(e.to)), (Pn.edges || []).map(e => nz(e.to)));
          if (same && post[1][5] < L.first[1][5]) ap = ap.map(a => a[3] === 'nohas' ? [a[0], a[1].slice(0, -3) + ' 지워짐', a[2].replace('no ', '') + ' removed', 'x'] : a);
          r._a = needc ? ap : (a0 || []);
          const apx = ap.slice();
          for (const y of ch.slice(0, -1)) {
            for (const a of (y[1][5] >= 0 ? CD.atoms(src_if(y[0], y[1][5], y[1][4])) : []) || []) {
              const kk = kstr(a[0]);
              if (!apx.some(b => kstr(b[0]) === kk) && !a0k.has(kk)) apx.push(a);
            }
          }
          r._ap = apx;
        }
      }
      out.push(r);
    }
    /* 같은 결과는 합침 */
    const m = new Map();
    for (const r of sortBy(out, r => -r.share)) {
      const k = kstr([r.cls, r.to, dumps(nz(r.lab)), dumps(nz(r.via), true), nz(r.lost), nz(r.exit)]);
      if (m.has(k)) {
        const h = m.get(k);
        h.share += r.share; h.n = or_(nz(h.n), 0) + or_(nz(r.n), 0); h._i = Math.min(gd(h, '_i', 999), gd(r, '_i', 999));
        if (h._ap != null) { const ks = new Set((r._ap || []).map(a => kstr(a[0]))); h._ap = h._ap.filter(a => ks.has(kstr(a[0]))); }
      } else m.set(k, Object.assign({}, r));
    }
    let rs = [...m.values()];
    const ka = rs.find(r => r.cls === 'ok' && !T(r.exit) && T(r.lab) && r._if != null && r._if !== '?' && G_ && _simp(r._if, G_.params) === true);
    if (ka) {
      for (const r of rs.filter(x => x !== ka && x.cls === 'ok' && x.to === ka.to && !T(x.via) && !T(x.exit))) {
        ka.share += r.share; ka.n = or_(nz(ka.n), 0) + or_(nz(r.n), 0); pyRemove(rs, r);
      }
    }
    { const L0 = rs.length; rs = rs.filter(r => !(r.to === 'self' && r.share < 0.01 && L0 > 1)); }
    rs = rs.filter(r => !(r.cls === 'no' && r.to !== 'self' && r.share < 0.003));
    function fold(tiny, cl) {
      sortInPlace(tiny, r => -r.share); const ds = [];
      for (const r of tiny) if (!ds.includes(r.to)) ds.push(r.to);
      const o = { cls: cl, lab: { kr: '그 밖', en: 'Otherwise' }, to: ds[0] };
      if (ds.length > 1) o.toAlt = ds.slice(1, 4);
      o.share = sum(tiny.map(r => r.share));
      return o;
    }
    const tiny = rs.filter(r => r.cls === 'no' && r.to !== 'self' && r.share < 0.01);
    if (tiny.length >= 2) { const a = rs.filter(r => !pyIn(tiny, r)); rs = a.concat([fold(tiny, 'no')]); }
    const oks = rs.filter(r => r.cls === 'ok' && !T(r.exit));
    const mx = Math.max(...(oks.length ? oks.map(r => r.share) : [0]));
    if (oks.length > 1 && mx > 0) {
      rs = rs.filter(r => !(r.cls === 'ok' && !T(r.exit) && r.share < 0.02 * mx));
      const small = rs.filter(r => r.cls === 'ok' && !T(r.exit) && r.share < 0.1 * mx);
      const big = rs.filter(r => r.cls === 'ok' && !T(r.exit) && !pyIn(small, r));
      const rest = [];
      for (const r of small) {
        const same = big.find(b => b.to === r.to && dumps(nz(b.via)) === dumps(nz(r.via)));
        if (same) { same.share += r.share; same.n = or_(nz(same.n), 0) + or_(nz(r.n), 0); }
        else rest.push(r);
      }
      rs = rs.filter(r => !pyIn(small, r));
      if (rest.length === 1) rs.push(rest[0]);
      else if (rest.length) rs.push(fold(rest, 'ok'));
    }
    for (const cl of ['ok', 'no']) {
      const grp = rs.filter(r => r.cls === cl && !(r.to === 'self' && !T(r.via)) && !T(r.skip));
      const many = new Set(grp.map(r => kstr([r.to, T(r.via)]))).size >= 2;
      const need = grp.filter(r => !T(r.lab) && (many || T(r._c)));
      if (!need.length) continue;
      const al = grp.filter(r => T(r._a) && !T(r._c)).map(r => new Set(r._a.map(a => kstr(a[0]))));
      const common = new Set();
      if (al.length >= 2) for (const k of al[0]) if (al.every(s => s.has(k))) common.add(k);
      const hasres = grp.some(r => T(r.res));
      const bare = need.filter(r => !T(r._a) && !T(r._c));
      const one = grp.filter(r => !pyIn(bare, r) && (r._a || []).length === 1 && (r._a[0][3] === 'has' || r._a[0][3] === 'nohas'));
      if (bare.length === 1 && grp.length === 2 && one.length === 1) {
        const a = one[0]._a[0];
        bare[0]._a = [[['neg'].concat(a[0]), a[1].slice(0, -3) + (a[3] === 'has' ? ' 없음' : ' 있음'), a[3] === 'has' ? ('no ' + a[2].slice(4)) : a[2].slice(3), 'x']];
      } else if (bare.length === 1 && grp.length === 2) {
        const oth = grp.find(r => r !== bare[0] && !T(r._c) && r._if != null && r._if !== '?') || null;
        const oc = (oth && G_) ? _simp(oth._if, G_.params) : null;
        if (isObj(oc)) { const na = CD ? CD.atoms({ not: oc }) : null; if (T(na)) bare[0]._a = na; }
        if (!T(g(bare[0], '_a')) && cl === 'ok' && CD && G_) bare[0]._a = _rest_atoms(W, n, bare[0], G_, CD);
      } else if (bare.length === 1 && cl === 'ok' && CD && G_) {
        const na = _rest_atoms(W, n, bare[0], G_, CD);
        if (T(na)) bare[0]._a = na;
      }
      for (const r of need) {
        const lb = _label(nz(r._a), T(r._c) ? [] : [...common].map(s => JSON.parse(s)));
        if (lb) {
          const pre = (cl === 'ok' && hasres) ? ['성공, ', 'Hit, '] : (cl === 'no' && hasres && !T(r._c)) ? ['실패, ', 'Miss, '] : ['', ''];
          r.lab = { kr: pre[0] + lb.kr, en: pre[1] + (!pre[1] ? cap1(lb.en) : lb.en) };
        }
        r.plab = false;
      }
    }
    for (const r of rs) {
      if (T(r.lost) && !T(r.lab)) r.lab = { kr: '다른 옵션이 지워지면', en: 'Another mod removed' };
      else if (T(r._c) && !T(r.lab) && r._pr === 'ok') r.lab = or_((T(r._e0) && r.to !== 'self') ? r._e0 : null, { kr: '빗나간 옵션이 지워지면', en: 'Missed mod removed' });
      else if (T(r._c) && !T(r.lab)) {
        if (T(r._e0) && r.to !== 'self') r.lab = r._e0;
        r.alt = true; r.plab = true;
      }
    }
    function shown(r) {
      if (T(r.vo) && T(r.alt) && (!T(r.lab) || T(r.plab))) return ['alt'];
      if (T(r.lost) && !T(r.lab)) return ['lost'];
      return ['lab', r.cls, nz(g(r.lab || {}, 'kr'))];
    }
    const skipr = r => T(r.skip) || (r.to === 'self' && !T(r.via)) || g(r.lab || {}, 'kr') === '그 밖';
    let byshow = new Map();
    for (const r of rs) { if (skipr(r)) continue; const k = kstr(shown(r)); if (!byshow.has(k)) byshow.set(k, []); byshow.get(k).push(r); }
    for (const grp_ of byshow.values()) {
      if (new Set(grp_.map(r => r.to)).size < 2) continue;
      for (const r of grp_) {
        let lb = _label(r._ap || []);
        if (!lb) {
          const others = grp_.filter(o => o !== r).map(o => new Set((o._a || []).map(a => kstr(a[0]))));
          const ownA = (r._a || []).filter(a => !others.some(o => o.has(kstr(a[0]))));
          lb = ownA.length ? _label(ownA) : null;
        }
        if (!lb) continue;
        const base = (shown(r)[0] === 'lab' && T(r.lab)) ? (r.lab || {}) : null;
        if (T(base) && !base.kr.includes(lb.kr)) r.lab = { kr: base.kr + ', ' + lb.kr, en: base.en + ', ' + lb.en };
        else if (!T(base)) {
          const pre = (r.cls === 'no' && shown(r)[0] === 'lab') ? ['실패, ', 'Miss, '] : ['', ''];
          r.lab = { kr: pre[0] + lb.kr, en: pre[1] + cap1(lb.en) };
        }
        r.plab = false;
      }
    }
    byshow = new Map();
    for (const r of rs) { if (skipr(r)) continue; const k = kstr(shown(r)); if (!byshow.has(k)) byshow.set(k, []); byshow.get(k).push(r); }
    for (const grp_ of byshow.values()) {
      if (new Set(grp_.map(r => r.to)).size < 2 || grp_.some(r => r.to === 'self')) continue;
      sortInPlace(grp_, r => -r.share); const h = grp_[0];
      h.toAlt = grp_.slice(1).filter(r => r.to !== h.to).map(r => r.to);
      for (const r of grp_.slice(1)) { h.share += r.share; h.n = or_(nz(h.n), 0) + or_(nz(r.n), 0); pyRemove(rs, r); }
      if (new Set(grp_.map(r => dumps(nz(r.via), true))).size > 1) delete h.via;
    }
    if (T(n.skipTo) && or_(g(t, 'skips'), 0) > 0.001 && ok_dest(dest(n.skipTo)) && t.skips / Math.max(1e-9, or_(g(t, 'visits'), 1)) >= 0.005) {
      let sl = nz(n.skipNote);
      const sif = or_(g(n, 'skipIf'), G_ ? g(G_.sn(n.id) || {}, 'skipIf') : null);
      if (!T(sl) && CD && isObj(sif)) {
        const sc = G_ ? _simp(sif, G_.params) : sif;
        sl = isObj(sc) ? _label(CD.atoms(sc) || []) : null;
      }
      if (T(sl) && /있음$/.test(or_(g(sl, 'kr'), '')) && !or_(g(sl, 'kr'), '').startsWith('이미')) {
        const se = or_(g(sl, 'en'), sl.kr);
        sl = { kr: '이미 ' + sl.kr, en: 'Already ' + se.slice(0, 1).toLowerCase() + se.slice(1) };
      }
      rs.push({ cls: 'ok', lab: or_(sl, { kr: '건너뜀', en: 'Skip' }), to: dest(n.skipTo), share: t.skips / Math.max(1e-9, or_(g(t, 'visits'), 1)), skip: true });
      const nk = rs.slice(0, -1).filter(r => !(r.to === 'self' && !T(r.via)));
      const nko = nk.filter(r => r.cls === 'ok' && r.to === rs[rs.length - 1].to && !T(r.lab) && !T(r.via));
      if (rs.length === 2 && nko.length) pyRemove(rs, nk[0]);
      else if (nko.length === 1 && nk.filter(r => r.cls === 'ok').length === 1 && !T(n.skipNote)) {
        const sk = rs[rs.length - 1]; const ks0 = 1 - sk.share; const ok_ = nko[0];
        sk.lab = { kr: '성공 또는 ' + sk.lab.kr, en: 'Hit or ' + sk.lab.en.slice(0, 1).toLowerCase() + sk.lab.en.slice(1) };
        sk.share = sk.share + or_(nz(ok_.share), 0) * ks0; sk.n = nz(ok_.n); delete sk.skip; sk._merged = true;
        pyRemove(rs, ok_);
        for (const r of rs) if (r !== sk && r.share != null) r.share *= ks0;
        const ix = rs.findIndex(y => deq(y, sk)); const [x] = rs.splice(ix, 1); rs.push(x);
      }
      const ks = !T(rs[rs.length - 1]._merged) ? 1 - rs[rs.length - 1].share : 1;
      for (const r of rs.slice(0, -1)) if (r.share != null) r.share *= ks;
    }
    for (const r of rs) if (r.to === 'restart' && r.cls === 'ok' && !T(r.skip)) r.cls = 'no';
    const rn = rs.filter(r => !T(r.skip));
    const hasf = rn.some(r => r.cls !== 'ok');
    if (rn.length >= 2 && new Set(rn.map(r => r.to)).size === 1 && rn[0].to !== 'self' && !rn.some(r => T(r.via) || T(r.toAlt) || T(r.exit)) && rn.some(r => r.cls === 'ok') && (!hasf || W.vid === 'ess')) {
      const h = rn.find(r => r.cls === 'ok');
      h.share = sum(rn.map(r => or_(nz(r.share), 0))); h.n = or_(sum(rn.map(r => or_(nz(r.n), 0))), nz(h.n)); h.lab = null;
      if (hasf) h.keepAll = true;
      for (const r of rn) if (r !== h) pyRemove(rs, r);
    }
    const rk = rs.filter(r => !T(r.skip) && !(r.to === 'self' && !T(r.via)));
    if (rk.length && rs.every(r => r.cls === 'ok') && new Set(rk.map(r => r.to)).size >= 2 && rk.some(r => T(r.lab) || T(r.keepAll))) {
      for (const r of rk) {
        const lb = r.lab || {};
        if (or_(g(lb, 'kr'), '').startsWith('성공, ')) { r.lab = { kr: lb.kr.slice(4), en: or_(g(lb, 'en'), '').replace(/^Hit, /, '') }; r.lab.en = cap1(r.lab.en); }
      }
      for (const r of rk) if (!T(r.lab) && !T(r.keepAll)) r.lab = { kr: '그 밖', en: 'Otherwise' };
      const ot = sortBy(rk.filter(r => g(r.lab || {}, 'kr') === '그 밖'), r => -or_(nz(r.share), 0));
      if (ot.length >= 2) {
        const h = ot[0]; const ds = [h.to].concat(h.toAlt || []);
        for (const r of ot.slice(1)) {
          for (const d of [r.to].concat(r.toAlt || [])) if (!ds.includes(d)) ds.push(d);
          h.share += or_(nz(r.share), 0); h.n = or_(or_(nz(h.n), 0) + or_(nz(r.n), 0), null); pyRemove(rs, r);
        }
        h.to = ds[0]; h.toAlt = or_(ds.slice(1, 4), null);
        if (new Set(ot.map(r => dumps(nz(r.via), true))).size > 1) { delete h.via; delete h.vo; }
      }
    }
    const _mk = r => dumps([r.cls, nz(g(r.lab || {}, 'kr')), r.to, nz(r.toAlt), T(r.via), T(r.skip), T(r.exit), T(r.lost)], true);
    const _seen = new Map();
    for (const r of rs.slice()) {
      if (r.to === 'self' && !T(r.via)) continue;
      const k = _mk(r);
      if (_seen.has(k)) {
        const h = _seen.get(k);
        if (or_(nz(r.share), 0) > or_(nz(h.share), 0) && T(r.via)) h.via = r.via;
        h.share = or_(nz(h.share), 0) + or_(nz(r.share), 0);
        if (T(r.n) || T(h.n)) h.n = or_(nz(h.n), 0) + or_(nz(r.n), 0);
        pyRemove(rs, r);
      } else _seen.set(k, r);
    }
    sortInPlace(rs, r => [r.cls !== 'ok', gd(r, 'skip', false), gd(r, 'exit', false), g(r.lab || {}, 'kr') === '그 밖', r.cls !== 'ok' ? gd(r, '_i', 999) : 0, r.to !== 'self', -or_(nz(r.share), 0)]);
    for (const r of rs) { r.share = pyRound(r.share, 5); for (const k of ['_a', '_c', '_e0', '_pr', '_i', '_if', '_ap', '_merged']) delete r[k]; }
    return rs.map(r => { const o = {}; for (const k of Object.keys(r)) { const v = r[k]; if (v !== null && v !== undefined && v !== false) o[k] = v; } return o; });
  }

  function _repeats(W, n) {
    const nx = N => (N.edges || []).map(e => nz(e.to)).concat([nz(N.next), nz(N.skipTo)]).concat(Object.values(N.options || {}));
    const seen = new Set(); const q = nx(n).filter(x => T(x));
    while (q.length) {
      const x = q.shift();
      if (x === n.id) return true;
      if (seen.has(x)) continue;
      seen.add(x); const N = W.B(x);
      if (!T(N) || ['base', 'done', 'exit'].includes(N.kind)) continue;
      for (const y of nx(N)) if (T(y)) q.push(y);
    }
    return false;
  }

  function _via_use(W, nid) {
    if (!W._vu) {
      const acc = {};
      let nid0 = null;
      const addTo = (d, use, k) => { for (const cur_ of Object.keys(use)) d[cur_] = gd(d, cur_, 0) + use[cur_] * k; };
      function give(src, use, k, depth) {
        depth = depth || 0;
        if (depth > 6) return;
        if (W.via(src) && src !== nid0) {
          const ins = W.nodes.filter(a => W.cnt(a.id, src) > 0 && a.id !== src).map(a => [a.id, W.cnt(a.id, src)]);
          const tot = sum(ins.map(p => p[1]));
          for (const [a, c] of ins) give(a, use, k * c / tot, depth + 1);
          return;
        }
        if (!HAS.call(acc, src)) acc[src] = {};
        addTo(acc[src], use, k);
      }
      for (const V of W.nodes) {
        if (!W.via(V.id)) continue;
        const u = (W.st(V.id) || {}).use || {};
        if (!T(u)) continue;
        nid0 = null;
        const ins = W.nodes.filter(a => a.id !== V.id && W.cnt(a.id, V.id) > 0).map(a => [a.id, W.cnt(a.id, V.id)]);
        const tot = sum(ins.map(p => p[1]));
        for (const [a, c] of ins) {
          if (W.via(a)) give(a, u, c / tot, 1);
          else { if (!HAS.call(acc, a)) acc[a] = {}; addTo(acc[a], u, c / tot); }
        }
      }
      W._vu = acc;
    }
    const o = {}; const d = own(W._vu, nid) || {};
    for (const k of Object.keys(d)) if (d[k] >= 0.0005) o[k] = pyRound(d[k], 4);
    return o;
  }

  function _keep_all(W, n) {
    if (W.vid !== 'ess') return false;
    const outs = W.outs(n);
    const used = outs.filter(x => W.ec(n.id, x, outs) > 0);
    return used.length > 0 && new Set(used.map(x => x[1])).size === 1 && used[0][1] !== n.id && outs.some(x => x[1] === used[0][1] && x[3] === 'ok') && used.some(x => x[3] === 'fail') && !W.via(used[0][1]);
  }

  const _STRUCT = ['sideLt', 'count', 'full', 'sideGe', 'empty'];
  function _structural(c) {
    if (!isObj(c)) return false;
    if (HAS.call(c, 'all') || HAS.call(c, 'any')) return (or_(g(c, 'all'), g(c, 'any'), [])).every(y => _structural(y));
    if (HAS.call(c, 'not')) return _structural(c.not);
    return _STRUCT.some(k => HAS.call(c, k));
  }

  function _fcs(W, n, fold_ids, srcn) {
    fold_ids = fold_ids || new Set();
    const t = W.st(n.id) || {};
    const tries = (t.visits || 0) - (n.kind === 'cleanup' ? 0 : (t.skips || 0));
    const outs = W.outs(n);
    const has_res = outs.some(x => T(x[3]));
    const goes_on = Tn => Tn.kind === 'exit' && Tn.variant === 'ok' && (T(Tn.swapFracture) || (T(Tn.simTo) && g(W.B(Tn.simTo) || {}, 'kind') !== 'base'));
    let ok = outs.filter(x => x[3] === 'ok' && (T(n.pAll) || !T(x[0].dash) || g(W.B(x[1]) || {}, 'kind') === 'assume' || goes_on(W.B(x[1]) || {})));
    if (has_res && !outs.some(x => x[3] === 'ok')) ok = outs.filter(x => !T(x[3]) && x[1] !== n.id);
    const xs = has_res ? W.exits(n, outs) : new Set();
    const xc = sum(ok.filter(x => xs.has(x[5])).map(x => W.ec(n.id, x, outs)));
    if (xc > 0) ok = ok.filter(x => !xs.has(x[5]));
    let okc = sum(ok.map(x => W.ec(n.id, x, outs)));
    if (has_res && okc <= 0 && tries > 0) okc = sum(outs.filter(x => x[3] !== 'fail' && x[1] !== n.id).map(x => W.ec(n.id, x, outs)));
    let p = (has_res && tries > 0) ? Math.min(1.0, okc / tries) : 1.0;
    if (!has_res && tries > 0) {
      const bad = sum(outs.filter(x => x[1] === n.id || T(x[0].lost)).map(x => W.ec(n.id, x, outs)));
      if (bad > 0) p = Math.max(0.0, (tries - bad) / tries);
    }
    let fixed_n = null;
    if (!has_res && tries > 0 && p < 0.995 && !outs.some(x => T(x[0].lost))) {
      const se = (srcn || {}).edges || [];
      const cond = x => { if (x[0].if != null) return x[0].if; const e = se.find(e => e.to === x[0].to); return e ? nz(e.if) : null; };
      const selfs = outs.filter(x => x[1] === n.id);
      const others = outs.filter(x => x[1] !== n.id);
      if (selfs.length && selfs.every(x => _structural(cond(x)) || (!T(cond(x)) && others.length && others.every(y => _structural(cond(y)))))) {
        const ent = Math.max(1e-9, tries - sum(selfs.map(x => W.ec(n.id, x, outs))));
        fixed_n = tries / ent; p = 1.0;
      }
    }
    if (n.act === 'flux' || _keep_all(W, n)) p = 1.0;
    let rows = null;
    if (T(n.curRows) && T(t.byCur)) {
      rows = [];
      for (const rw of n.curRows) {
        const b = own(t.byCur, or_(g(rw, 'key'), g(rw, 'cur')));
        const ids = or_(g(rw, 'ids'), [nz(rw.cur)].concat(n.omens || []));
        const o = { kr: rw.kr, en: rw.en, ids }; if (T(b) && T(b.t)) o.p = pyRound(b.ok / b.t, 5);
        rows.push(o);
      }
    }
    if (!T(rows) && T(n.trim) && Object.keys(t.byCur || {}).length >= 2) {
      const sd = or_(isObj(n.trim) ? g(n.trim, 'side') : null, 'p');
      const er = sd === 'p' ? 'Omen_of_Sinistral_Erasure' : 'Omen_of_Dextral_Erasure';
      const [sk, se] = sd === 'p' ? ['접두', 'prefix'] : ['접미', 'suffix'];
      const LB = {};
      LB['Omen_of_Whittling'] = ['잡옵이 아이템에서 레벨이 가장 낮음', 'Junk is the lowest-level modifier'];
      LB[`${er}+Omen_of_Whittling`] = [`잡옵이 ${sk}에서만 레벨이 가장 낮음`, `Junk is the lowest-level ${se} only`];
      LB[er] = [`남길 ${sk}가 잡옵보다 레벨이 낮음`, `A kept ${se} is lower than the junk`];
      rows = [];
      for (const k of sortBy(Object.keys(t.byCur), k => -gd(t.byCur[k], 't', 0))) {
        const b = t.byCur[k];
        if (!HAS.call(LB, k) || !T(b.t)) continue;
        rows.push({ kr: LB[k][0], en: LB[k][1], ids: [nz(n.cur)].concat(k.split('+')), p: pyRound(b.ok / b.t, 5) });
      }
      rows = rows.length ? rows : null;
    }
    const px = (xc > 0 && tries > 0) ? pyRound(xc / tries, 6) : null;
    const selfc = sum(outs.filter(x => x[1] === n.id).map(x => W.ec(n.id, x, outs)));
    if (p <= 0 && tries > 0 && !T(px)) p = null;
    const uv = _via_use(W, n.id);
    const o = { p: p != null ? pyRound(p, 6) : null };
    if (T(fixed_n)) o.fixedN = pyRound(fixed_n, 3);
    o.tries = pyRound(tries, 4);
    const use = {}; for (const k of Object.keys(t.use || {})) if (t.use[k] >= 0.0005) use[k] = pyRound(t.use[k], 4);
    o.use = use;
    if (T(uv)) o.useVia = uv;
    o.div = pyRound(t.div || 0, 4); o.reach = pyRound(t.reach || 0, 4);
    if (T(rows)) o.rows = rows;
    if (fold_ids.has(n.id)) o.loop = true;
    if (T(px)) o.pX = px;
    if (T(n.once) || (!(T(px) && selfc > 0) && n.kind !== 'cleanup' && !fold_ids.has(n.id) && p != null && p < 0.995 && (!_repeats(W, n) || (p > 0 && tries * p < 0.9 * (t.reach || 1))))) o.once = true;
    return o;
  }

  function _miss(W, n) {
    const outs = W.outs(n); const tot = or_(sum(outs.map(x => W.ec(n.id, x, outs))), 1);
    const vres = {};
    for (const x of outs) if (!T(x[0].hide) && T(x[3]) && !HAS.call(vres, x[4])) vres[x[4]] = x[3];
    const miss = x => { const eff = or_(x[3], T(x[0].hide) ? nz(own(vres, x[4])) : null); return !(eff === 'ok' && x[4] === x[1]); };
    return outs.filter(x => miss(x) && W.ec(n.id, x, outs) / tot >= 0.01);
  }

  function _ntiers(GR, cls, gi) {
    const a = GR.nt(cls); return (gi >= 0 && gi < a.length) ? a[gi] : null;
  }
  function _top_tier(GR, cls, gi, ilvl) {
    if (!T(ilvl)) return 1;
    const a = GR.tl(cls);
    if (!(gi >= 0 && gi < a.length)) return 1;
    const i = a[gi].findIndex(lv => typeof lv === 'number' && lv <= ilvl);
    return i >= 0 ? i + 1 : 1;
  }

  function _sig(W, n, G_, cls, GR) {
    if (!T(n) || !W.seen(n.id)) return null;
    const tiers = [], tops = [];
    const wt = or_(g(n, 'want'), g(G_.sn(n.id) || {}, 'want'));
    const shown_empty = Array.isArray(n.show) && !n.show.length;
    const lst = shown_empty ? [] : or_(isStr(wt) ? [wt] : (Array.isArray(wt) && wt.length) ? wt : null, n.show || []);
    for (const t of lst) {
      for (let [gi, tm] of G_.leaves(G_.name(t))) {
        const nt = T(cls) ? _ntiers(GR, cls, gi) : null;
        try { tm = tm != null ? pyInt(tm) : null; } catch (e) { tm = null; }
        tiers.push((T(tm) && T(nt) && tm >= nt && nt > 2) ? 99 : or_(tm, 0));
        tops.push(T(cls) ? _top_tier(GR, cls, gi, or_(g(W.sim.graph, 'ilvl'), g(G_.src || {}, 'ilvl'))) : 1);
      }
    }
    if (_keep_all(W, n)) return { tiers: [], fails: ['keep'], cur: nz(n.cur), top: 1, keep: true };
    const fs = new Map();
    for (const x of _miss(W, n)) { const tp = [T(x[2]) ? dumps(x[2], true) : '', !W.via(x[1]) ? x[1] : 'via']; fs.set(kstr(tp), tp); }
    const fails = sortBy([...fs.values()], v => v);
    return { tiers, fails, cur: nz(n.cur), top: tops.length ? Math.min(...tops) : 1 };
  }

  function _grade_note(sim, src, nid, tiers, cls, GR) {
    const descs = [];
    for (const tr of tiers) {
      const [F, V, S] = _version(sim, tr);
      if (!S) continue;
      const W = new Walk(sim, V, S); const G_ = new G(sim, src, V.params); const n = W.B(nid);
      descs.push([tr, W, G_, n, _sig(W, n, G_, cls, GR)]);
    }
    if (descs.length < 2) return null;
    const sigs = descs.map(d => dumps(d[4], true));
    if (new Set(sigs).size < 2) return null;
    const live = descs.filter(d => T(d[4]));
    const diff_t = new Set(live.map(d => dumps(d[4].tiers))).size > 1;
    const diff_f = new Set(live.map(d => dumps(d[4].fails))).size > 1;
    const diff_c = new Set(live.map(d => dumps(d[4].cur))).size > 1;
    const parts = [];
    for (const [tr, W, G_, n, s] of descs) {
      const kr = [], en = [];
      if (!T(s)) { kr.push('이 단계 없음'); en.push('not used'); }
      else {
        if (diff_t && !s.tiers.length && !T(s.keep)) { kr.push('나오는 대로'); en.push('keep what comes'); }
        if (diff_t && s.tiers.length && Math.max(...s.tiers)) {
          const lt = s.tiers.filter(x => x < 99); const tm = lt.length ? Math.max(...lt) : 99;
          if (tm >= 99) { kr.push('티어 상관없음'); en.push('any tier'); }
          else {
            const t0 = Math.min(or_(g(s, 'top'), 1), tm);
            kr.push(tm === t0 ? `${tm}티어` : `${t0}~${tm}티어`); en.push(tm === t0 ? `T${tm}` : `T${t0}–${tm}`);
          }
        }
        if (diff_c && T(n.cur)) { kr.push('@' + n.cur); en.push('@' + n.cur); }
        if (diff_f) {
          let fl = T(s.keep) ? [] : _miss(W, n);
          if (!fl.length) { kr.push('결과 그대로 다음'); en.push('keep the result'); }
          else {
            fl = sortBy(fl, x => x[1] !== n.id ? (or_(g(W.B(x[1]) || {}, 'pos'), [0, 0])).slice().reverse() : [-1e9, 0]);
            const [e, to, lab] = fl[0]; const Tn = W.B(to) || {};
            const lk = (or_(g(lab || {}, 'kr'), '')).replace(/^(빗나감|실패)\s*([—,:·-]\s*)?/, '').trim();
            const le = (or_(g(lab || {}, 'en'), '')).replace(/^(miss(ed)?|fail(ed)?)\b\s*([—,:·-]\s*)?/i, '').trim();
            const tg = (Tn.kind === 'act' || Tn.kind === 'cleanup') ? or_(g(Tn, 'goal'), g(Tn, 'label')) : null;
            if (!T(e.res) && !lk && to !== n.id) {
              if (Tn.kind === 'done') { kr.push('바로 완성'); en.push('finish here'); }
              else if (T(tg)) { kr.push('이어서 ' + tg.kr); en.push('then: ' + or_(g(tg, 'en'), tg.kr).toLowerCase()); }
              else if (T(Tn.cur)) { kr.push(`이어서 @${Tn.cur}`); en.push(`then @${Tn.cur}`); }
              else { kr.push('이어서 다른 단계'); en.push('then another step'); }
            } else if (lk) { kr.push('빗나가면 ' + lk); en.push('on a miss: ' + (le || lk).toLowerCase()); }
            else if (to === n.id) { kr.push('빗나가면 다시'); en.push('retry on a miss'); }
            else if (Tn.kind === 'done') { kr.push('빗나가도 그대로 완성'); en.push('finish as it is on a miss'); }
            else if (W.via(to)) { kr.push('빗나가면 지우고 다시'); en.push('remove and retry on a miss'); }
            else if (Tn.kind === 'base' || Tn.kind === 'exit') { kr.push('빗나가면 처음부터'); en.push('start over on a miss'); }
            else if (T(Tn.cur)) { kr.push(`빗나가면 @${Tn.cur}로`); en.push(`on a miss: @${Tn.cur}`); }
            else if (T(tg)) { kr.push('빗나가면 ' + tg.kr); en.push('on a miss: ' + or_(g(tg, 'en'), tg.kr).toLowerCase()); }
            else { kr.push('빗나가면 다른 작업'); en.push('another step on a miss'); }
          }
        }
      }
      if (kr.includes('결과 그대로 다음') && kr.includes('나오는 대로')) { kr.splice(kr.indexOf('나오는 대로'), 1); en.splice(en.indexOf('keep what comes'), 1); }
      if (kr.includes('결과 그대로 다음')) {
        const ix = kr.map((x, i) => /티어( 상관없음)?$/.test(x) ? i : -1).filter(i => i >= 0);
        for (const i of ix.reverse()) { kr.splice(i, 1); en.splice(i, 1); }
      }
      if (T(s) && !kr.length) { kr.push('이 단계 씀'); en.push('uses this step'); }
      parts.push({ tier: tr, kr: kr.join(', '), en: en.join(', ') });
    }
    const grp = [];
    for (const p of parts) {
      const x = grp.find(x => x.kr === p.kr);
      if (x) x.tiers.push(p.tier); else grp.push({ tiers: [p.tier], kr: p.kr, en: p.en });
    }
    return grp.length >= 2 ? grp : null;
  }

  /* 클래스 파일 groups 읽기(Cond 옵션 이름·티어 수·최고 티어) */
  function _groups(opt) {
    const src = opt && opt.groups;
    const cache = {}, NT = {}, TL = {};
    const get = cls => {
      if (HAS.call(cache, cls)) return cache[cls];
      let v = null;
      try { v = typeof src === 'function' ? src(cls) : (src ? own(src, cls) : null); } catch (e) { v = null; }
      cache[cls] = Array.isArray(v) ? v : (v && Array.isArray(v.groups) ? v.groups : null);
      return cache[cls];
    };
    return {
      get,
      nt(cls) { if (!HAS.call(NT, cls)) { const gs = get(cls); NT[cls] = gs ? gs.map(x => (x.t || []).length) : []; } return NT[cls]; },
      tl(cls) {
        if (!HAS.call(TL, cls)) {
          const gs = get(cls);
          TL[cls] = gs ? gs.map(x => (x.t || []).map(t => Array.isArray(t) ? t[0] : or_(g(t, 'l'), g(t, 'lvl'), 0))) : [];
        }
        return TL[cls];
      }
    };
  }

  function readRecipe(r, sim, src, tiers, opt) {
    opt = opt || {};
    const inherit = opt.inherit !== false;
    const GR = opt._GR || _groups(opt);
    const tier = or_(g(r, 'tier'), 'high');
    const [F, V, S] = _version(sim, tier);
    if (!S) return null;
    const W = new Walk(sim, V, S); const G_ = new G(sim, src, V.params); const CD = new Cond(G_, sim, src, nz(r.cls), GR.get);
    const final_tags = new Set((F.lines || []).filter(l => T(l.tag)).map(l => G_.name(l.tag)));
    const nodes = W.nodes;
    const base = nodes.find(n => n.kind === 'base') || null;
    const mark = nodes.find(n => n.kind === 'mark') || null;
    const own_prep = has_prep(sim);
    const work = nodes.filter(n => (n.kind === 'act' || n.kind === 'cleanup') && (own_prep || n.group !== 'prep') && W.seen(n.id) && !W.via(n.id));
    const main = sortBy(work.filter(n => n.pos[0] === 0), n => n.pos[1]);
    if (!main.length) return null;
    const side = work.filter(n => n.pos[0] !== 0);
    const parent = {};
    function flow(a, sid) {
      const outs = W.outs(a); let f = 0, hit = false, vis = false;
      for (const x of outs) {
        if (x[1] === sid) { hit = true; vis = vis || !T(x[0].hide); f += W.ec(a.id, x, outs); }
        else if (W.via(x[1])) {
          const Vn = W.by[x[1]]; const vo = W.outs(Vn); const vt = or_(sum(vo.map(y => W.ec(Vn.id, y, vo))), 1);
          for (const y of vo) if (y[1] === sid) { hit = true; vis = vis || !(T(x[0].hide) || T(y[0].hide)); f += W.ec(a.id, x, outs) * W.ec(Vn.id, y, vo) / vt; }
        }
      }
      return hit ? [vis ? 1 : 0, f + 1e-9] : 0;
    }
    const workSorted = sortBy(work, n => [n.pos[1], n.pos[0]]);
    for (const s of side) {
      let best = null; const ks = [s.pos[1], s.pos[0]];
      for (const early of [true, false]) {
        for (const a of workSorted) {
          if (a === s || (early && cmp([a.pos[1], a.pos[0]], ks) >= 0)) continue;
          const f = flow(a, s.id);
          if (T(f) && (best === null || f[0] > best[0][0] || (f[0] === best[0][0] && f[1] > best[0][1] * 1.000001))) best = [f, a.id];
        }
        if (best) break;
      }
      if (best) parent[s.id] = best[1];
    }
    const order = []; const placed = new Set();
    function put(n) {
      if (placed.has(n.id)) return;
      order.push(n); placed.add(n.id);
      for (const c of sortBy(side.filter(x => own(parent, x.id) === n.id), x => [x.pos[1], x.pos[0]])) put(c);
    }
    for (const n of main) put(n);
    for (const s of sortBy(side, x => x.pos[1])) {
      if (!placed.has(s.id)) {
        const ix = order.map((x, i) => x.pos[1] <= s.pos[1] ? i : -1).filter(i => i >= 0);
        const k = ix.length ? Math.max(...ix) : order.length - 1;
        order.splice(k + 1, 0, s); placed.add(s.id);
        if (!HAS.call(parent, s.id)) parent[s.id] = order[k].id;
      }
    }
    const loops = sim.graph.loops || [];
    const srcLoops = (src || {}).loops || [];
    const fold_ids = new Set();
    for (const L of loops) if (T(L.fold) || srcLoops.some(x => T(x.fold) && x.id === L.id)) for (const i of L.nodes || []) fold_ids.add(i);
    const loop_of = nid => loops.find(L => L.nodes.includes(nid)) || null;
    const old = {}; for (const n of r.nodes || []) old[n.id] = n;
    const keep = inherit ? (i => { const o = {}; for (const k of ['tips', 'ts']) if (HAS.call(old, i) && T(old[i][k])) o[k] = old[i][k]; return o; }) : (() => ({}));
    const b0 = Object.assign({ id: base ? base.id : 'b0', phase: 'base', do: 'base', cost: 'base' }, base ? keep(base.id) : {});
    const ob = (r.nodes || []).find(x => x.do === 'base');
    if (ob) for (const k of (inherit ? ['note', 'tips', 'ts'] : ['note'])) if (T(ob[k])) b0[k] = ob[k];
    const bst = own_prep ? (or_(g(base || {}, 'start'), {})) : {};
    if (own_prep && base && T(base.label) && or_(g(b0.note || {}, 'kr'), '').includes('분열') && !(bst.mods || []).some(m => isObj(m) && T(m.fr))) b0.note = { kr: base.label.kr + '.', en: base.label.en + '.' };
    const out = [b0];
    const phases = [{ id: 'base', kr: '베이스', en: 'Base' }];
    let prev = or_(g((own_prep ? base : or_(mark, base)) || {}, 'item'), []);
    const groups = {}; for (const x of sim.graph.groups || []) groups[x.id] = x;
    let last_bone = null, cur_ph = null; const ph_of = {};
    order.forEach((n, oi) => {
      const cur = or_(g(n, 'item'), prev);
      let pv = (n.pos[0] === 0 || !T(own(parent, n.id))) ? prev : or_(g(W.by[parent[n.id]], 'item'), prev);
      const vin = W.nodes.filter(m => T(m.item) && ((n.pos[0] !== 0 && W.via(m.id)) || W.skipall(m.id)) && (m.edges || []).some(e => e.to === n.id));
      if (vin.length) pv = vin[0].item;
      G_._kall = _keep_all(W, n);
      let act, om, t;
      [act, om, t, last_bone] = _target(G_, n, pv, cur, last_bone);
      const o = { id: n.id, do: or_(nz(own(ACT, act) !== undefined ? ACT[act] : act), 'manual') };
      if (T(n.cur)) o.cur = n.cur;
      else if (o.do === 'remove') o.cur = 'Orb_of_Annulment';
      if (T(n.curIf) && T(o.cur)) {
        const u = (W.st(n.id) || {}).use || {};
        const cs = [o.cur].concat(n.curIf.filter(c => T(isStr(c) ? c : g(c, 'cur'))).map(c => isStr(c) ? c : g(c, 'cur')));
        const top = maxBy(cs, c => or_(gd(u, c, null), 0));
        if (or_(gd(u, top, null), 0) > or_(gd(u, o.cur, null), 0)) o.cur = top;
        const ucs = [...new Set(cs)];
        const tot_ = sum(ucs.map(c => or_(gd(u, c, null), 0)));
        const mix = sortBy(ucs.filter(c => T(tot_) && or_(gd(u, c, null), 0) / tot_ >= 0.02).map(c => [c, or_(gd(u, c, null), 0) / tot_]), x => -x[1]);
        if (mix.length > 1) o.curMix = mix.map(([c, v]) => ({ cur: c, share: pyRound(v, 3) }));
      }
      if (n.kind === 'cleanup') {
        const u = (W.st(n.id) || {}).use || {};
        om = om.concat(['Omen_of_Sinistral_Annulment', 'Omen_of_Dextral_Annulment'].filter(k => or_(gd(u, k, null), 0) > 0 && !om.includes(k)));
      }
      if (T(n.trim)) {
        const u = (W.st(n.id) || {}).use || {};
        const tu = sortBy(Object.keys(u).filter(k => /Whittling|Erasure/.test(k) && or_(u[k], 0) > 0), k => -or_(u[k], 0));
        if (tu.length) om = om.filter(x => !/Whittling|Erasure/.test(x)).concat(tu);
      }
      if (T(om)) o.omens = om;
      if (T(t)) o.target = t;
      if (T(n.trim)) o.trimFc = isObj(n.trim) ? nz(n.trim.side) : 'p';
      o.fcs = _fcs(W, n, fold_ids, G_ ? G_.sn(n.id) || null : null);
      o.routes = _routes(W, n, placed, G_, CD);
      const _sn = G_ ? (((G_.src || {}).nodes || []).find(x => x.id === n.id) || {}) : {};
      if (T(t) && (act === 'chaos' || act === 'exalt') && (t.gi != null || T(t.anyOf)) && G_) {
        const shw = new Set((n.show || []).filter(isStr).map(x => G_.name(x)));
        const ex = [];
        for (const e of or_(g(G_.sn(n.id) || {}, 'edges'), g(n, 'edges'), [])) {
          const c = or_(g(e, 'if'), {});
          const tg = (e.res === 'ok' && !['done', n.id].includes(e.to) && isObj(c) && Object.keys(c).length === 1) ? or_(g(c, 'has'), g(c, 'added')) : null;
          if (isStr(tg) && !shw.has(G_.name(tg)) && !ex.includes(G_.name(tg))) ex.push(G_.name(tg));
        }
        const tg_ = new Set((t.gi != null ? [t] : (t.anyOf || [])).map(x => g(x, 'gi')));
        const ex2 = ex.filter(x => !G_.leaves(x).some(([gi]) => tg_.has(gi)));
        const sx = (ex2.length && shw.size) ? G_.spec(ex2) : null;
        if (T(sx)) t.orAlso = sx;
      }
      const _one = T(n.edges) && !n.edges.some(e => e.res === 'fail' || e.to === n.id || T(e.lost)) && new Set(n.edges.map(e => nz(e.to))).size === 1;
      if (T(t) && ['exalt', 'chaos', 'reveal'].includes(act) && _one && ((_sn.edges || []).some(e => e.res === 'fail') || act === 'reveal' || (!T(t.asIs) && !T(t.junk) && (t.gi != null || T(t.anyOf) || T(t.all))))) t.noMiss = true;
      if (!T(o.cur) && T(or_(g(n, 'goal'), g(n, 'label')))) o.label = or_(g(n, 'goal'), g(n, 'label'));
      const st_ = (n.showText || []).filter(x => !_is_tip(x));
      const tp_ = (n.showText || []).filter(x => _is_tip(x)).map(x => ({ kr: x.kr, en: or_(g(x, 'en'), x.kr) }));
      if (tp_.length) o.tipTx = tp_;
      if (!T(t) && st_.length) o.note = st_[0];
      else if (!T(t) && T(G_._marktx)) o.note = G_._marktx;
      G_._marktx = null;
      let back = maxBy(o.routes.filter(x => x.cls === 'no' && !['done', 'self', 'restart', 'state'].includes(x.to)), x => or_(nz(x.share), 0));
      back = back ? back.to : back;
      if (T(back)) o.fail = { goto: back };
      if (T(own(parent, n.id)) && n.pos[0] !== 0) {
        const pa = parent[n.id]; const po = out.find(x => x.id === pa) || null;
        const into = ((po || {}).routes || []).filter(x => x.to === n.id && !T(x.skip));
        if (po && T(po.fallbackFor) && into.length && into.every(x => x.cls === 'ok')) {
          o.fallbackFor = po.fallbackFor; o.chain = pa;
          if (T(po.alt)) o.alt = po.alt;
        } else {
          o.fallbackFor = pa;
          if (into.length && into.every(x => x.cls === 'ok')) o.alt = { kr: or_(g(into[0].lab || {}, 'kr'), ''), en: or_(g(into[0].lab || {}, 'en'), ''), share: pyRound(sum(into.map(x => or_(nz(x.share), 0))), 5) };
        }
      }
      o.fst = _state(G_, cur, final_tags);
      if (T(or_(g(n, 'goal'), g(n, 'label')))) o.goal = or_(g(n, 'goal'), g(n, 'label'));
      if (T(n.target) && isObj(n.target) && HAS.call(n.target, 'kr')) o.fcTarget = n.target;
      else if (o.do === 'remove' && T(g(n.goal || {}, 'kr')) && n.goal.kr !== '소멸의 오브 사용') {
        const gone_ = _diff(pv, cur)[1];
        if (gone_.some(l => !['j', 'u', 'd'].includes(nz(l.m)) && T(l.tags))) o.fcTarget = n.goal;
      }
      const gn = _grade_note(sim, src, n.id, tiers, nz(r.cls), GR);
      if (gn) o.grade = gn;
      Object.assign(o, keep(n.id));
      if (T(o.fallbackFor) && HAS.call(ph_of, o.fallbackFor)) o.phase = ph_of[o.fallbackFor];
      else {
        if (T(o.fallbackFor)) { delete o.fallbackFor; delete o.chain; delete o.alt; }
        const L = loop_of(n.id);
        const gp = own_prep && n.group === 'prep';
        const key = gp ? kstr(['G', 'prep']) : L ? kstr(['L', L.id]) : kstr(['g', dumps(or_(g(n, 'goal'), g(n, 'label')))]);
        if (key !== cur_ph) {
          cur_ph = key;
          const tl = gp ? or_(own(groups, 'prep'), { kr: '베이스 준비', en: 'Base preparation' }) : or_(L, g(n, 'goal'), g(n, 'label'), { kr: '', en: '' });
          const ph = { id: `f${phases.length}`, kr: tl.kr, en: tl.en }; if (gp) ph.prep = true;
          phases.push(ph);
        }
        o.phase = phases[phases.length - 1].id;
      }
      ph_of[n.id] = o.phase;
      let FL = srcLoops.find(x => T(x.fold) && (T(x.nodes) ? x.nodes : [null])[0] === n.id) || null;
      if (FL) {
        const mem = (FL.nodes || []).slice();
        let bk = 0; mem.forEach((a, i) => { for (const b of mem.slice(0, i + 1)) bk += W.cnt(a, b); });
        let via_back = 0;
        for (const a of mem) for (const v of W.nodes) if (W.via(v.id) && (v.edges || []).some(e => mem.includes(e.to))) via_back += W.cnt(a, v.id) * 1;
        const wto = g(FL.worst || {}, 'to');
        if (bk + via_back <= 1e-6) FL = Object.assign({}, FL, { goal: null, goalBy: null, worst: (T(wto) && sum(mem.map(a => W.cnt(a, wto))) > 1e-6) ? nz(FL.worst) : null });
      }
      if (FL) {
        const ln = { goal: or_(g(FL.goalBy || {}, V.id), g(FL, 'goal')), worst: T(FL.worst) ? { kr: FL.worst.kr, en: FL.worst.en } : null };
        const ln2 = {}; for (const k of Object.keys(ln)) if (T(ln[k])) ln2[k] = ln[k];
        if (T(ln2)) o.loopNote = ln2;
      }
      out.push(o);
      if (n.pos[0] === 0) prev = cur;
      const FLp = srcLoops.find(x => T(x.fold) && (x.nodes || []).includes(n.id)) || null;
      if (FLp && (oi + 1 >= order.length || !FLp.nodes.includes(order[oi + 1].id))) {
        const li = or_(g(FLp.itemBy || {}, V.id), g(FLp, 'item'));
        if (T(li)) prev = li;
      }
    });
    for (const sn_ of ((src || {}).nodes || []).filter(x => x.kind === 'side')) {
      if (Array.isArray(sn_.tiers) && !sn_.tiers.includes(V.id)) continue;
      const at = (sn_.attach || []).filter(a_ => T(a_));
      const ids = out.map(x => x.id);
      const anchor = at.find(a_ => ids.includes(a_));
      if (!T(anchor) && !at.some(a_ => g(gd(W.by, a_, {}) || {}, 'kind') === 'done')) continue;
      const o = { id: sn_.id, do: or_(nz(own(ACT, sn_.act) !== undefined ? ACT[sn_.act] : nz(sn_.act)), 'manual'), optional: true };
      if (T(sn_.cur)) o.cur = sn_.cur;
      if (T(sn_.omens)) o.omens = sn_.omens.slice();
      if (T(or_(g(sn_, 'goal'), g(sn_, 'label')))) { o.label = or_(g(sn_, 'goal'), g(sn_, 'label')); o.goal = o.label; }
      o.note = or_(nz((T(sn_.showText) ? sn_.showText : [null])[0]), g(sn_, 'goal'), g(sn_, 'label'), { kr: '선택 단계', en: 'Optional step' });
      Object.assign(o, keep(sn_.id));
      let i = T(anchor) ? ids.indexOf(anchor) + 1 : out.length;
      while (i < out.length && T(out[i].fallbackFor)) i += 1;
      o.phase = i > 0 ? out[i - 1].phase : phases[phases.length - 1].id;
      let pf = null; for (let j = i - 1; j >= 0; j--) if (out[j].fst != null) { pf = out[j].fst; break; }
      if (pf !== null) o.fst = clone(pf);
      out.splice(i, 0, o);
    }
    const last = (T(r.nodes) ? r.nodes : [null])[(T(r.nodes) ? r.nodes.length : 1) - 1];
    const done_note = (T(last) && last.do === 'note' && !T(last.optional)) ? nz(last.note) : null;
    out.push({ id: 'done', phase: phases[phases.length - 1].id, do: 'note', note: or_(done_note, { kr: '완성.', en: 'Done.' }) });
    const fno = fc_numbers(W, sim, src, V.id);
    for (const o of out) {
      if (o.do === 'base' || T(o.optional) || o.id === 'done') continue;
      if (HAS.call(fno, o.id)) o.fcNo = fno[o.id];
    }
    for (const o of out) for (const x of o.routes || []) {
      for (const v of [nz(x.via)].concat((x.via || {}).then || [])) {
        if (isObj(v) && HAS.call(v, 'vid')) { const k = v.vid; delete v.vid; if (T(own(fno, k))) v.no = fno[k]; }
      }
    }
    const res = S.res;
    const fr = {}; for (const k of ['mean', 'median', 'p90', 'bases', 'baseDiv', 'use', 'useDiv', 'est']) fr[k] = g(res, k);
    fr.version = V.id;
    return { nodes: out, phases, start: start_of(r, sim, src, V.params), fcRead: fr };
  }

  function fc_numbers(W, sim, src, vid) {
    const res = W.res; const rn = res.nodes || {};
    const nodes = W.nodes; const by = {}; for (const n of nodes) by[n.id] = n;
    const gone = new Set(nodes.filter(n => ['act', 'cleanup', 'mark'].includes(n.kind) && !T(own(rn, n.id))).map(n => n.id));
    for (const n of nodes) if (n.kind === 'side' && Array.isArray(n.tiers) && T(vid) && !n.tiers.includes(vid)) gone.add(n.id);
    for (const n of nodes) if (n.kind === 'side' && T(n.attach) && n.attach.every(a => gone.has(a) || !HAS.call(by, a))) gone.add(n.id);
    const jump = {};
    for (const n of nodes) {
      const t = own(rn, n.id);
      if (n.kind === 'act' && T(n.skipTo) && T(t) && (t.visits || 0) > 0 && (t.skips || 0) >= t.visits * 0.999 && !T(t.use || {})) { gone.add(n.id); jump[n.id] = n.skipTo; }
    }
    const to = i => { let k = i, c = 0; while (HAS.call(jump, k) && c < 20) { k = jump[k]; c += 1; } return k; };
    const edges_of = {}; for (const n of nodes) edges_of[n.id] = (n.edges || []).map(e => to(nz(e.to)));
    const loops = [];
    for (const L of (sim.graph.loops || [])) {
      const ln = (L.nodes || []).filter(i => !gone.has(i) && HAS.call(by, i));
      if (gone.size && ln.length < 2) continue;
      if (gone.size && !ln.some((i, k) => (own(edges_of, i) || []).some(e => { const ix = ln.indexOf(e); return 0 <= ix && ix <= k; }))) continue;
      loops.push(Object.assign({}, L, { nodes: ln }));
    }
    const srcL = {}; for (const L of (src || {}).loops || []) srcL[nz(L.id)] = L;
    const member = {}; const folded = new Set();
    for (const L of loops) {
      if (!(T(L.fold) || T(g(own(srcL, nz(L.id)) || {}, 'fold')))) continue;
      const SL = own(srcL, nz(L.id)) || {};
      const steps = or_(g(SL.stepsBy || {}, vid), g(L.stepsBy || {}, vid), g(SL, 'steps'), g(L, 'steps'), []);
      const ord = steps.filter(s => T(s.node) && !gone.has(s.node)).map(s => s.node);
      let extra = ord.length;
      L.nodes.forEach((i, j) => {
        let k = ord.includes(i) ? ord.indexOf(i) + 1 : (ord.length ? null : j + 1);
        if (k === null && ord.length && j && (own(by, i) || {}).kind === 'act' && (own(by, i) || {}).act !== 'annul') {   /* graph2recipe fc_numbers와 같음(W11): 같은 행동 상자 번호, 없으면 순서 줄 뒤 */
          const q = ord.findIndex(x => (own(by, x) || {}).act === by[i].act && (own(by, x) || {}).cur === by[i].cur);
          if (q >= 0) k = q + 1; else { extra += 1; k = extra; } }
        if (k !== null) member[i] = [L.nodes[0], k];
        if (j) folded.add(i);
      });
    }
    const steps = sortBy(nodes.filter(n => !gone.has(n.id) && !folded.has(n.id) && (n.kind === 'act' || n.kind === 'cleanup')), n => [n.pos[1], n.pos[0]]);
    const no = {}; const cnt = {}; let m = 0;
    for (const n of steps) if (n.pos[0] === 0) { m += 1; no[n.id] = String(m); }
    const parent = (n, col) => { const xs = steps.filter(x => x.pos[0] === col && x.pos[1] <= n.pos[1]); return xs.length ? maxBy(xs, x => [x.pos[1], x.pos[0]]) : null; };
    for (const n of steps) if (n.pos[0] === 1) {
      const P = parent(n, 0); const k = P ? no[P.id] : '0'; cnt[k] = gd(cnt, k, 0) + 1; no[n.id] = `${k}.${String.fromCharCode(64 + cnt[k])}`;
    }
    for (const n of steps) if (n.pos[0] >= 2) {
      const P0 = parent(n, 0); const P = parent(n, 1);
      const k = (P && (!P0 || P.pos[1] >= P0.pos[1])) ? no[P.id] : (P0 ? no[P0.id] : '0');
      cnt[k] = gd(cnt, k, 0) + 1; no[n.id] = `${k}.${String.fromCharCode((k.includes('.') ? 96 : 64) + cnt[k])}`;
    }
    const out = Object.assign({}, no);
    for (const i of Object.keys(member)) { const [h, k] = member[i]; if (HAS.call(no, h)) out[i] = `${no[h]}-${k}`; }
    return out;
  }

  function has_prep(sim) {
    return ((or_(g(sim, 'graph'), sim)).nodes || []).some(n => n.group === 'prep' && (n.kind === 'act' || n.kind === 'cleanup'));
  }

  function start_of(r, sim, src, params) {
    let st = clone(or_(g(r, 'start'), {}));
    const s0 = ((src || {}).nodes || []).find(n => n.kind === 'base') || null;
    if (has_prep(sim)) {
      const b = or_(g(s0 || {}, 'start'), {});
      st = { rar: or_(g(b, 'rar'), 'normal'), mods: [] };
      const q = b.quality != null ? b.quality : null;
      if (T(q)) st.quality = q;
      const rn = or_(g(b, 'runes'), g(r.start || {}, 'runes'));
      if (T(rn)) st.runes = clone(rn);
      if (!T(b.mods)) return st;
    }
    if (!T(s0) || !T(s0.start)) return st;
    const G_ = new G(sim, src, params || {});
    const mods = [];
    for (let m of s0.start.mods || []) {
      if (isStr(m)) m = { tag: m };
      if (HAS.call(m, 'tag')) {
        const sp = G_.spec([m.tag]) || {};
        const tmn = or_(g(m, 'tmin'), g(own(G_.tags, G_.name(m.tag)) || {}, 'tmin'), g(own((G_.src || {}).tags || {}, G_.name(m.tag)) || {}, 'tmin'));
        if (HAS.call(sp, 'gi')) {
          const o = { gi: sp.gi };
          if (T(sp.tmax)) o.tmax = sp.tmax;
          if (T(tmn)) o.tmin = tmn;
          if (T(m.fr)) o.fr = true;
          if (T(m.ess)) o.ess = true;
          mods.push(o);
        }
      } else if (HAS.call(m, 'junk')) mods.push({ junk: m.junk });
      else if (HAS.call(m, 'unrev')) mods.push({ unrev: m.unrev });
    }
    if (mods.length) st.mods = mods;
    if (T(s0.start.rar)) st.rar = s0.start.rar;
    return st;
  }

  const FcRead = { readRecipe, read_recipe: readRecipe, fc_numbers, has_prep, start_of, shown_leaves, leaf_gis, vid_of,
    _py: { T, pyRound, dumps, deq, cmp } };
  if (typeof module === 'object' && module.exports) module.exports = FcRead;
  else root.FcRead = FcRead;
})(typeof self !== 'undefined' ? self : this);
