"""알두르 룬 4종(열정·숨결·노여움·배신)을 모든 무기 클래스에 넣음.
poe2db 클래스 페이지에는 마법봉·지팡이·셉터에만 나오지만, 룬 설명은 '무기:'(무도 무기·'마법봉 또는 지팡이'와 구분)이고
아이템 설명도 '희귀 무기에 있는 빈 증강물 홈에 장착' → 모든 무기(사용자 확정 2026-11-11).
build_site_data.py를 다시 돌렸으면 그 뒤에 실행."""
import json, os
C = '/home/claude/poe2data/site/data/c/'
WEAPONS = ['Bows','Claws','Crossbows','Daggers','Flails','One_Hand_Axes','One_Hand_Maces','One_Hand_Swords','Quarterstaves',
           'Sceptres','Spears','Staves','Talismans','Two_Hand_Axes','Two_Hand_Maces','Two_Hand_Swords','Wands']
FAM = ['PassionofAldur','BreathofAldur','IreofAldur','BetrayalofAldur']
src = {r['f']: r for r in json.load(open(C+'Wands.json'))['runes'] if r['f'] in FAM}
assert len(src) == 4, src.keys()
def patch(runes):
    have = {r['f'] for r in runes}; add = [src[f] for f in FAM if f not in have]
    if not add: return 0
    at = next((i for i, r in enumerate(runes) if r['f'] == 'AldursLegacy' or r['f'].startswith('Legacyof')), len(runes))
    runes[at:at] = add; return len(add)
for cid in WEAPONS:
    p = C+cid+'.json'
    if not os.path.exists(p): continue
    d = json.load(open(p)); n = patch(d['runes']) + sum(patch(v) for v in (d.get('runesBy') or {}).values())
    if n: open(p, 'w').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print(cid, '+', n)
