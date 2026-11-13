/* site/fcread.js(JS) = scripts/graph2recipe.py(파이썬) 점검 — 2026-11-13 W3
   등록 그래프(scripts/graphs/*.json) × 완성 카드 등급마다:
   ① 같은 입력으로 파이썬 read_recipe와 JS readRecipe 결과 전체(nodes·phases·start·fcRead)를 비교(inherit 켬·끔 둘 다)
   ② JS 결과를 recipes.json의 그 레시피(nodes·phases·fcRead)와 비교 — 옛 레시피에서 이어받거나 빌드가 뒤에 붙이는 칸
      (꿀팁 tips·영상 시각 ts, 시작 룬)은 빼고. recipes.json이 지금 그래프·시뮬보다 오래됐으면 여기서만 차이가 남
   차이 0이어야 함(끝 줄 '차이 0'). 테스트 서버 필요 없음.
     node tools/test/_fcparity.js [그래프 id…]      PY=<파일>이면 파이썬 결과 파일을 다시 만들지 않고 씀, V=1이면 차이를 모두 보임 */
const fs = require('fs'), path = require('path'), cp = require('child_process'), os = require('os');
const ROOT = path.resolve(__dirname, '../..');
const FcRead = require(path.join(ROOT, 'site/fcread.js'));
const only = process.argv.slice(2);
const V = !!process.env.V;

let pyFile = process.env.PY;
if (!pyFile) {
  pyFile = path.join(os.tmpdir(), `fcparity-${process.pid}.json`);
  const r = cp.spawnSync('python3', [path.join(__dirname, '_fcparity_py.py'), pyFile, ...only], { encoding: 'utf8', maxBuffer: 1 << 28 });
  if (r.status !== 0) { console.error(r.stdout, r.stderr); process.exit(2); }
}
const PY = JSON.parse(fs.readFileSync(pyFile, 'utf8'));
if (!process.env.PY) try { fs.unlinkSync(pyFile); } catch (e) {}

const R = JSON.parse(fs.readFileSync(path.join(ROOT, 'site/data/recipes.json'), 'utf8')).recipes;
const RB = Object.fromEntries(R.map(r => [r.id, r]));
const GC = {};
const groups = cls => {
  if (!(cls in GC)) { try { GC[cls] = JSON.parse(fs.readFileSync(path.join(ROOT, 'site/data/c', cls + '.json'), 'utf8')).groups; } catch (e) { GC[cls] = null; } }
  return GC[cls];
};
const J = {};
const load = f => J[f] || (J[f] = JSON.parse(fs.readFileSync(f, 'utf8')));

function diff(a, b, p, out) {
  if (out.length > 20) return;
  if (a === b) return;
  if (typeof a === 'number' && typeof b === 'number') { if (a !== b) out.push(`${p}: py ${a} · js ${b}`); return; }
  if (a === null || b === null || typeof a !== 'object' || typeof b !== 'object' || Array.isArray(a) !== Array.isArray(b)) {
    out.push(`${p}: py ${JSON.stringify(a)} · js ${JSON.stringify(b)}`.slice(0, 400)); return;
  }
  if (Array.isArray(a)) {
    if (a.length !== b.length) out.push(`${p}: 길이 py ${a.length} · js ${b.length}`);
    for (let i = 0; i < Math.min(a.length, b.length); i++) diff(a[i], b[i], `${p}[${i}]${a[i] && a[i].id ? '(' + a[i].id + ')' : ''}`, out);
    return;
  }
  const ka = Object.keys(a), kb = Object.keys(b);
  for (const k of ka) if (!(k in b)) out.push(`${p}.${k}: js에 없음 (py ${JSON.stringify(a[k])})`.slice(0, 400));
  for (const k of kb) if (!(k in a)) out.push(`${p}.${k}: py에 없음 (js ${JSON.stringify(b[k])})`.slice(0, 400));
  for (const k of ka) if (k in b) diff(a[k], b[k], `${p}.${k}`, out);
  if (ka.filter(k => k in b).join() !== kb.filter(k => k in a).join()) out.push(`${p}: 키 순서 py ${ka.join(',')} · js ${kb.join(',')}`);
}
const strip = x => JSON.parse(JSON.stringify(x, (k, v) => (k === 'tips' || k === 'ts') ? undefined : v));

let n1 = 0, bad1 = 0, n2 = 0, bad2 = 0, err = 0;
const t0 = Date.now();
const graphs = new Set(), byGraph = {};
for (const key of Object.keys(PY)) {
  const [gid, tier, inh] = key.split('|');
  const P = PY[key];
  graphs.add(gid);
  const sim = load(path.join(ROOT, 'site/data/sim', gid + '.json'));
  const src = load(path.join(ROOT, 'scripts/graphs', gid + '.json'));
  const rin = RB[P.r] || { id: P.r, tier, cls: sim.graph.cls || src.cls, nodes: [], start: {} };
  let js, je = null;
  try { js = FcRead.readRecipe(JSON.parse(JSON.stringify(rin)), sim, src, P.tiers, { inherit: inh === '1', groups }); js = JSON.parse(JSON.stringify(js)); }
  catch (e) { je = e; }
  n1++;
  const d = [];
  if (P.err || je) { if (!(P.err && je)) d.push(`오류: py ${P.err || '-'} · js ${je ? je.stack.split('\n').slice(0, 3).join(' | ') : '-'}`); }
  else diff(P.out, js, '', d);
  if (d.length) { bad1++; (byGraph[gid] = byGraph[gid] || []).push(`${tier}/inherit=${inh}: ${d.length}건 — ${d.slice(0, V ? 99 : 3).join(' ; ')}`); }
  if (P.err) err++;
  /* ② recipes.json과 비교(inherit 켠 결과로, 이어받는 칸 제외) */
  if (inh === '1' && RB[P.r] && RB[P.r].fcRead && js) {
    n2++;
    const rb = RB[P.r]; const d2 = [];
    diff(strip({ nodes: rb.nodes, phases: rb.phases, fcRead: rb.fcRead }), strip({ nodes: js.nodes, phases: js.phases, fcRead: js.fcRead }), '', d2);
    if (d2.length) { bad2++; (byGraph[gid] = byGraph[gid] || []).push(`${tier} recipes.json(${rb.id}) 대비: ${d2.length}건 — ${d2.slice(0, V ? 99 : 3).join(' ; ')}`); }
  }
}
for (const gid of Object.keys(byGraph).sort()) { console.log('■', gid); for (const l of byGraph[gid]) console.log('  ', l); }
console.log(`그래프 ${graphs.size}개 · 경우 ${n1}개(등급 × inherit 2) · 파이썬 = JS 다른 경우 ${bad1}` + (err ? ` · 파이썬 오류 ${err}` : ''));
console.log(`recipes.json 레시피 ${n2}개 대비 다른 레시피 ${bad2}`);
console.log(`${((Date.now() - t0) / 1000).toFixed(1)}초 · ${bad1 + bad2 === 0 ? '차이 0' : '차이 ' + (bad1 + bad2)}`);
process.exit(bad1 + bad2 ? 1 : 0);
