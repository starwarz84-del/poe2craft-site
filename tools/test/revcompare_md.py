"""등록 레시피 vs 리버스 초안 비교 결과(tools/test/revcompare.json, `node tools/test/_revcompare.js <id…>`) → docs/reverse-compare.md"""
import json, datetime
ROOT = '/home/claude/poe2data'
d = json.load(open(f'{ROOT}/tools/test/revcompare.json'))
f = lambda v: '-' if v is None else f'{v:,.0f}' if v >= 10 else f'{v:.1f}'
pc = lambda v: '-' if v is None else f'{round(v * 100)}%'
out = ['# 등록 레시피와 리버스 초안 비교', '',
       f'{datetime.date.today()} 기준. 난이도마다 등록 레시피 2개를 골라 같은 아이템을 리버스 크래프팅으로 만들어 비교했어요. 다시 만들기: `node tools/test/_revcompare.js <레시피 id…>` → `python3 tools/test/revcompare_md.py`(테스트 서버 필요).', '',
       '읽는 법', '',
       '- 기준은 등록 레시피의 플로우차트가 정한 완성 조건이에요. 등록 레시피는 이 조건을 항상 채워요. 리버스에는 그 조건이 요구하는 옵션을 필수로 넣었고(티어 범위와 "○○ 또는 ○○" 포함), 등록 레시피가 베이스에 붙여 사는 옵션은 "베이스에 포함"으로 넣었어요.',
       '- 비용은 플로우차트 시뮬의 완성 1개당 평균이고 베이스 값과 분열 준비는 뺐어요.',
       '- 조건 충족은 시뮬 완성품이 그 완성 조건을 채운 비율이에요.', '',
       '## 한눈에', '',
       '| 난이도 | 레시피 | 등록 비용 | 리버스 비용 | 리버스 ÷ 등록 | 조건 충족(등록 / 리버스) | 비싼 징조(등록 / 리버스) |', '|---|---|---|---|---|---|---|']
for o in d:
    r, dr = o['reg'], o['draft']
    if dr.get('err'):
        out.append(f"| {o['diff']} | `{o['id']}` | {f(r['div'])} | {dr['err']} | - | - | - |"); continue
    k = max(dr['div'], 1) / max(r['div'], 1) if dr['div'] is not None else None
    out.append(f"| {o['diff']} | `{o['id']}` ({o['tier']}) | {f(r['div'])} | {f(dr['div'])} | {'-' if k is None else f'{k:.1f}배'} | {pc(r['match'])} / {pc(dr['match'])} | {f(r['om'])} / {f(dr['om'])} |")
out += ['', '비용 단위는 div.', '']
for o in d:
    r, dr = o['reg'], o['draft']
    out += [f"## {o['diff']} · {o['title']}", '', f"`{o['id']}` · {o['tier']} · {o['cls']} · 근거 {o['src']}", '', '완성 조건이 요구하는 옵션', '']
    out += [f"- {c}" for c in r['card']]
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
    if dr.get('miss'): extra.append('완성품 글에 없는 목표 옵션: ' + ', '.join(dr['miss']))
    if dr.get('verr'): extra.append('검산 오류: ' + dr['verr'][0])
    if dr.get('vwarn'): extra.append('검산 경고: ' + dr['vwarn'][0][:80])
    if dr.get('run'): extra.append('시뮬이 끝나지 않음: ' + str(dr['run']))
    out += ['', f"비용이 큰 것: {' · '.join(dr['top'][:3])}", ''] + ([' / '.join(extra), ''] if extra else [])
p = f'{ROOT}/docs/reverse-compare.md'
txt = '\n'.join(out)
old = open(p).read() if __import__('os').path.exists(p) else ''
if '## 정리' in old: txt += '\n' + old[old.index('## 정리'):]
open(p, 'w').write(txt); print('wrote', p, len(d))
