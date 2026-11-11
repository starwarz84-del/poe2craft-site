"""poe2db 원문에 남은 내부 능력치 줄 정리(2026-11-11, 사용자 지적: 한글 문구 뒤에 영문이 남아 있음).
'local jewel effect base radius [500]'처럼 게임 화면에 나오지 않는 내부 이름 줄을 지우고,
번역이 없는 실제 능력치 줄은 게임 문구 형식으로 바꿈(용어는 데이터의 다른 옵션 문구에서 확인: 반려수·흘려보내기·맹공·격노).
build_site_data.py 끝에서 자동 실행."""
import json, glob, re
C = '/home/claude/poe2data/site/data/c/'
RAW = re.compile(r'^[a-z][a-z0-9 _%+\-]*\[[-\d,]+\]$')
# 번역이 없는 실제 능력치(내부 이름 → 한글, 영문)
TR = {
  'minion area of effect +%': ('소환수 효과 범위 ({v})% 증가', 'Minions have ({v})% increased Area of Effect'),
  'rage effect +%': ('격노 효과 {v}% 증가', '{v}% increased effect of Rage'),
  'companions gain onslaught when you parry': ('흘려보내기 시 반려수가 맹공 획득', 'Companions gain Onslaught when you Parry'),
}
def fix(kr, en):
    if not isinstance(kr, str) or not isinstance(en, str): return kr, en
    ks, es = kr.split('\n'), en.split('\n')
    if not any(RAW.match(x.strip()) for x in ks + es): return kr, en
    def conv(lines, i):
        out = []
        for x in lines:
            s = x.strip(); m = RAW.match(s)
            if not m: out.append(x); continue
            name, vals = re.match(r'^(.*?)\s*\[([-\d,]+)\]$', s).groups(); name = name.strip()
            if name in TR:
                v = vals.split(','); v = v[0] if len(v) == 1 else f'{v[0]}—{v[1]}'
                out.append(TR[name][i].format(v=v))
            # 그 밖의 내부 이름 줄(반경·자리 수·우상 표시·숨은 피해 변환)은 앞줄과 같은 내용이거나 화면에 안 나와서 지움
        return '\n'.join(out)
    return conv(ks, 0), conv(es, 1)
n = 0
for p in sorted(glob.glob(C + '*.json')):
    d = json.load(open(p)); ch = False
    for g in d['groups']:
        for t in g['t']:
            a = fix(t[4], t[5])
            if a != (t[4], t[5]): t[4], t[5] = a; ch = True; n += 1
    for r in d.get('runes', []):
        for t in r['t']:
            for i in (2, 4):
                if len(t) > i + 1:
                    a = fix(t[i], t[i + 1])
                    if a != (t[i], t[i + 1]): t[i], t[i + 1] = a; ch = True; n += 1
    for b in d.get('bases', []):
        imp = b.get('imp')
        if imp and len(imp) == 2 and len(imp[0]) == len(imp[1]):
            for j in range(len(imp[0])):
                a = fix(imp[1][j], imp[0][j])
                if a != (imp[1][j], imp[0][j]): imp[1][j], imp[0][j] = a; ch = True; n += 1
            keep = [j for j in range(len(imp[0])) if imp[0][j] or imp[1][j]]
            if len(keep) != len(imp[0]): b['imp'] = [[imp[0][j] for j in keep], [imp[1][j] for j in keep]]; ch = True
    if ch: open(p, 'w').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
print('raw stat lines cleaned:', n)
