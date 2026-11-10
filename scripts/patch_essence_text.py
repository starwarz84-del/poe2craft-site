"""무한의 에센스 옵션 문구 정리(2026-11-11, 사용자 지적): 게임 데이터는 힘·민첩·지능 그룹이 따로 있는데
문구가 모두 '힘, 민첩 또는 지능'으로 같아 아이템 카드·플로우차트에 어떤 능력치인지 안 보임 → 그룹(계열)별로 실제 능력치 문구로 바꿈.
(에센스 설명 자체는 '힘, 민첩 또는 지능' — 셋 중 하나가 붙음. poe2db 확인: 하위·일반·상위 = 장비 +9—12/+17—20/+25—27, 완벽한 = 목걸이 (7—10)% 증가)
build_site_data.py 끝에서 자동 실행."""
import json, glob, re
C = '/home/claude/poe2data/site/data/c/'
ST = {'Strength':('힘','Strength'), 'Dexterity':('민첩','Dexterity'), 'Intelligence':('지능','Intelligence')}
n = 0
for p in sorted(glob.glob(C+'*.json')):
    d = json.load(open(p)); ch = False
    for g in d['groups']:
        if g['s'] != 'e' or len(g['f']) != 1: continue
        fam = g['f'][0]; pct = fam.startswith('Percentage'); key = fam.replace('Percentage', '')
        if key not in ST: continue
        kr, en = ST[key]
        for t in g['t']:
            if 'Dexterity or Intelligence' not in t[5]: continue
            rng = re.search(r'\(?[\d.]+—[\d.]+\)?|\d+', t[5]).group(0)
            t[4] = f'{kr} {rng}% 증가' if pct else f'{kr} +{rng}'
            t[5] = f'{rng}% increased {en}' if pct else f'+{rng} to {en}'
            ch = True; n += 1
    if ch: open(p, 'w').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
print('essence attribute lines renamed:', n)
