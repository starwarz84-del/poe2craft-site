# Builds site/data/prices.json from a poe2scout snapshot (raw/poe2scout_prices_<date>.json, prices in Exalted Orbs, English names).
# Matching: crafting.json items by their English name (en) -> currency id; runes / soul cores by the class rune data -> "rune:<en>"
# (the id the recipes use). Prints what did not match on either side. Names are never translated here (Korean comes from game data only).
import json, glob, os, re, sys
ROOT = '/home/claude/poe2data'
RAW = sorted(glob.glob(ROOT + '/raw/poe2scout_prices_*.json'))[-1]
src = json.load(open(RAW))
P = src['prices']
divine = float(P.get('Divine Orb') or 363)
craft = json.load(open(ROOT + '/site/data/crafting.json'))
items = [x for k in craft for x in craft[k]]
byen = {x['en']: x['id'] for x in items}
runes = set()
for f in glob.glob(ROOT + '/site/data/c/*.json'):
    for x in json.load(open(f)).get('runes', []):
        for t in x['t']:
            runes.add(t[1])
out, used = {}, set()
for x in items:
    if x['en'] in P:
        out[x['id']] = P[x['en']]; used.add(x['en'])
for en in sorted(runes):
    if en in P:
        out['rune:' + en] = P[en]; used.add(en)
fetched = src.get('fetched') or re.search(r'(\d{4}-\d{2}-\d{2})', RAW).group(1)
json.dump({'fetched': fetched, 'source': 'poe2scout', 'unit': 'ex', 'divine': divine, 'p': out},
          open(ROOT + '/site/data/prices.json', 'w'), ensure_ascii=False, separators=(',', ':'))
miss_c = [(x['id'], x['kr']) for x in items if x['en'] not in P]
miss_p = [n for n in P if n not in used]
print(f'prices.json: {len(out)} prices ({fetched}, 1 div = {divine:g} ex) from {os.path.basename(RAW)}')
print(f'crafting.json items without a price ({len(miss_c)}):')
for i, kr in miss_c: print('  ', i, kr)
print(f'price names not in our data ({len(miss_p)}):')
for n in miss_p: print('  ', n, P[n])
