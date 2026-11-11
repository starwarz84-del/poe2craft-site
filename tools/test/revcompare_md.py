"""등록 레시피 vs 리버스 초안 비교 결과(tools/test/revcompare.json, `node tools/test/_revcompare.js <id…>`) → docs/reverse-compare.md"""
import json, datetime
ROOT = '/home/claude/poe2data'
d = json.load(open(f'{ROOT}/tools/test/revcompare.json'))
f = lambda v: '-' if v is None else f'{v:,.0f}' if v >= 10 else f'{v:.1f}'
pc = lambda v: '-' if v is None else f'{round(v * 100)}%'
out = ['# 등록 레시피와 리버스 초안 비교', '',
       f'{datetime.date.today()} 기준. 난이도마다 등록 레시피 2개를 골라 같은 아이템을 리버스 크래프팅으로 만들어 비교했어요. 다시 만들기: `node tools/test/_revcompare.js <레시피 id…>` → `python3 tools/test/revcompare_md.py`(테스트 서버 필요).', '',
       '읽는 법', '',
       '- 목표는 등록 레시피의 완성품 카드예요. 카드에 적힌 옵션을 리버스의 필수로 넣었고, 등록 레시피가 베이스에 붙여 사는 옵션은 "베이스에 포함"으로 넣었어요.',
       '- 비용은 플로우차트 시뮬의 완성 1개당 평균이고 베이스 값과 분열 준비는 뺐어요.',
       '- 카드 일치율은 시뮬 완성품이 카드 옵션을 모두 가진 비율이에요. 등록 레시피는 카드에 대표 옵션 하나를 적고 실제로는 여러 옵션 중 하나를 받는 자리가 있어 100%가 안 되는 것이 많아요.',
       '- 환산 비용은 등록 레시피 비용 ÷ 카드 일치율이에요. 카드와 똑같은 아이템 하나를 얻는 데 드는 값의 어림이에요.', '',
       '## 한눈에', '',
       '| 난이도 | 레시피 | 등록 비용 | 등록 카드 일치 | 등록 환산 | 리버스 비용 | 리버스 카드 일치 | 리버스 ÷ 환산 | 비싼 징조(등록 / 리버스) |', '|---|---|---|---|---|---|---|---|---|']
for o in d:
    r, dr = o['reg'], o['draft']
    if dr.get('err'):
        out.append(f"| {o['diff']} | `{o['id']}` | {f(r['div'])} | {pc(r['match'])} | - | {dr['err']} | - | - | - |"); continue
    adj = r['div'] / max(r['match'], 0.05)
    k = max(dr['div'], 1) / max(adj, 1) if dr['div'] is not None else None
    out.append(f"| {o['diff']} | `{o['id']}` ({o['tier']}) | {f(r['div'])} | {pc(r['match'])} | {f(adj)} | {f(dr['div'])} | {pc(dr['match'])} | {'-' if k is None else f'{k:.1f}배'} | {f(r['om'])} / {f(dr['om'])} |")
out += ['', '비용 단위는 div.', '']
for o in d:
    r, dr = o['reg'], o['draft']
    out += [f"## {o['diff']} · {o['title']}", '', f"`{o['id']}` · {o['tier']} · {o['cls']} · 근거 {o['src']}", '', '완성품 카드와 등록 레시피의 옵션별 일치율', '']
    out += [f"- {c} — {pc(p)}" for c, p in zip(r['card'], r['per'])]
    if r['rnd']: out.append(f"- 랜덤 옵션 {r['rnd']}개")
    out += ['', '등록 레시피 단계', ''] + [f"{i + 1}. {s}" for i, s in enumerate(r['steps'])]
    out += ['', f"비용이 큰 것: {' · '.join(r['top'][:3])}", '']
    if dr.get('err'):
        out += [f"리버스: {dr['err']}", '']; continue
    out += ['리버스 초안 단계', ''] + [f"{i + 1}. {s}" for i, s in enumerate(dr['steps'])]
    extra = []
    if dr.get('pick'): extra.append(f"고른 후보 {dr['pick']['k']}({f(dr['pick'].get('from'))} → {f(dr['pick'].get('to'))} div)")
    if dr.get('knowhow'): extra.append('노하우 ' + '·'.join(dr['knowhow']))
    if dr.get('tried'): extra.append(f"후보 {dr['tried']['n']}개 · 시뮬 {dr['tried']['runs']:,}회")
    if dr.get('miss'): extra.append('완성품 글에 없는 카드 옵션: ' + ', '.join(dr['miss']))
    if dr.get('verr'): extra.append('검산 오류: ' + dr['verr'][0])
    if dr.get('vwarn'): extra.append('검산 경고: ' + dr['vwarn'][0][:80])
    if dr.get('run'): extra.append('시뮬이 끝나지 않음: ' + str(dr['run']))
    out += ['', f"비용이 큰 것: {' · '.join(dr['top'][:3])}", ''] + ([' / '.join(extra), ''] if extra else [])
    out += ['<!-- 메모:' + o['id'] + ' -->', '']
p = f'{ROOT}/docs/reverse-compare.md'
# 손으로 쓴 메모(<!-- 메모:id --> 다음 문단)는 다시 만들 때 유지
old = open(p).read() if __import__('os').path.exists(p) else ''
txt = '\n'.join(out)
for o in d:
    mk = '<!-- 메모:' + o['id'] + ' -->'
    if mk in old:
        seg = old.split(mk, 1)[1].split('\n## ', 1)[0].strip('\n')
        if seg: txt = txt.replace(mk + '\n', mk + '\n' + seg + '\n', 1)
if '## 정리' in old: txt += '\n' + old[old.index('## 정리'):]
open(p, 'w').write(txt); print('wrote', p, len(d))
