// poe2craft.xyz Worker: 정적 파일(web/) + 영상·제작글 분석 요청 API.
// 요청 저장 = KV(REQ), 처리 결과 = 저장소의 web/data/reqdone.json(예약 작업이 커밋).
// 접근 코드는 해시만 여기 둠(코드 자체는 저장소에 없음).
const CODE_HASHES = {
  'ee16fc5bc22bc1bb89923faef65bb12fd368f5b33eae279cfd40ac07318990db': { name: 'owner', perDay: 3 },
};
const MAX_URL = 400, MAX_MEMO = 300;

const json = (o, s = 200) => new Response(JSON.stringify(o), {
  status: s, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', 'x-robots-tag': 'noindex' },
});

async function sha256(t) {
  const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t));
  return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('');
}

// 같은 영상·글인지 비교하는 열쇠: 유튜브는 영상 id, 그 밖은 주소(쿼리·#·끝 / 제외)
function urlKey(u) {
  try {
    const x = new URL(u);
    const h = x.hostname.replace(/^www\.|^m\./, '');
    if (h === 'youtu.be') return 'yt:' + x.pathname.slice(1, 12);
    if (h.endsWith('youtube.com')) {
      const v = x.searchParams.get('v') || (x.pathname.match(/\/(?:shorts|live|embed)\/([\w-]{11})/) || [])[1];
      if (v) return 'yt:' + v;
    }
    return h + x.pathname.replace(/\/+$/, '');
  } catch { return null; }
}

async function doneMap(env, req) {
  try {
    const r = await env.ASSETS.fetch(new URL('/data/reqdone.json', req.url));
    return r.ok ? await r.json() : {};
  } catch { return {}; }
}

async function knownSources(env, req) {
  try {
    const r = await env.ASSETS.fetch(new URL('/data/recipes.json', req.url));
    if (!r.ok) return {};
    const d = await r.json();
    const list = Array.isArray(d) ? d : (d.recipes || Object.values(d));
    const m = {};
    for (const x of list) {
      const k = x && x.source && x.source.url && urlKey(x.source.url);
      if (k && !m[k]) m[k] = x.tierGroup || x.id;
    }
    return m;
  } catch { return {}; }
}

function view(it, done) {
  const d = done[it.id];
  return { id: it.id, url: it.url, memo: it.memo || '', at: it.at, st: d ? d.st : 'queued', recipe: d && d.recipe || null, why: d && d.why || null, doneAt: d && d.at || null };
}

async function create(req, env) {
  let b;
  try { b = await req.json(); } catch { return json({ error: 'bad_json' }, 400); }
  const url = String(b.url || '').trim(), memo = String(b.memo || '').trim().slice(0, MAX_MEMO), code = String(b.code || '').trim();
  if (!/^https?:\/\//i.test(url) || url.length > MAX_URL) return json({ error: 'bad_url' }, 400);
  const key = urlKey(url);
  if (!key) return json({ error: 'bad_url' }, 400);
  const h = await sha256(code);
  const who = CODE_HASHES[h];
  if (!who) return json({ error: 'bad_code' }, 403);

  // 이미 레시피가 있는 영상·글
  const known = await knownSources(env, req);
  if (known[key]) return json({ error: 'exists', recipe: known[key] }, 409);

  // 이미 대기 중인 같은 주소
  const ex = await env.REQ.get('url:' + key);
  if (ex) {
    const it = await env.REQ.get('req:' + ex, 'json');
    if (it) return json({ ok: true, dup: true, req: view(it, await doneMap(env, req)) });
  }

  const day = new Date(Date.now() + 9 * 3600e3).toISOString().slice(0, 10); // 한국 날짜
  const rk = `rate:${h.slice(0, 12)}:${day}`;
  const used = +(await env.REQ.get(rk) || 0);
  if (used >= who.perDay) return json({ error: 'limit', perDay: who.perDay }, 429);

  const id = Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
  const it = { id, url, key, memo, at: new Date().toISOString(), by: who.name };
  await env.REQ.put('req:' + id, JSON.stringify(it));
  await env.REQ.put('url:' + key, id);
  await env.REQ.put(rk, String(used + 1), { expirationTtl: 3 * 86400 });
  return json({ ok: true, req: view(it, {}), left: who.perDay - used - 1 });
}

async function status(req, env) {
  const ids = (new URL(req.url).searchParams.get('ids') || '').split(',').filter(x => /^[a-z0-9]{6,20}$/.test(x)).slice(0, 30);
  const done = await doneMap(env, req);
  const out = [];
  for (const id of ids) {
    const it = await env.REQ.get('req:' + id, 'json');
    if (it) out.push(view(it, done));
  }
  return json({ reqs: out });
}

// 예약 작업이 읽는 대기열: 아직 처리 결과가 없는 요청(오래된 것부터)
async function queue(req, env) {
  const done = await doneMap(env, req);
  const all = [];
  let cursor;
  do {
    const r = await env.REQ.list({ prefix: 'req:', cursor });
    for (const k of r.keys) {
      const id = k.name.slice(4);
      if (done[id]) continue;
      const it = await env.REQ.get(k.name, 'json');
      if (it) all.push({ id: it.id, url: it.url, memo: it.memo || '', at: it.at });
    }
    cursor = r.list_complete ? null : r.cursor;
  } while (cursor);
  all.sort((a, b) => a.at < b.at ? -1 : 1);
  return json({ queue: all });
}

export default {
  async fetch(req, env) {
    const u = new URL(req.url);
    if (u.pathname.startsWith('/api/')) {
      if (!env.REQ) return json({ error: 'unavailable' }, 503);
      if (u.pathname === '/api/req' && req.method === 'POST') return create(req, env);
      if (u.pathname === '/api/req' && req.method === 'GET') return status(req, env);
      if (u.pathname === '/api/queue' && req.method === 'GET') return queue(req, env);
      return json({ error: 'not_found' }, 404);
    }
    return env.ASSETS.fetch(req);
  },
};
