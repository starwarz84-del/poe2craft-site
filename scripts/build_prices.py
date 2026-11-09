# Builds site/data/prices.json from a poe2scout snapshot (raw/poe2scout_prices_<date>.json, prices in Exalted Orbs, English names).
# Matching: crafting.json items by their English name (en) -> currency id; runes / soul cores by the class rune data -> "rune:<en>"
# (the id the recipes use). Prints what did not match on either side. Names are never translated here (Korean comes from game data only).
# Policy 22 (user, 2026-11-09 15:19): an odd price (a lower tier dearer than the higher tier of the same family, or an entry in OVERRIDE)
# and a currency with no price at all (too cheap to trade) both count as 1 Exalted Orb. What was changed is kept in prices.json "adj".
import json, glob, os, re, sys
ROOT = '/home/claude/poe2data'
sys.path.insert(0, ROOT + '/scripts')
import add_extra_currency                      # POE2DB names for priced items we lacked -> crafting.json "extra"
add_extra_currency.main(verbose=False)
RAW = sorted(glob.glob(ROOT + '/raw/poe2scout_prices_*.json'))[-1]
src = json.load(open(RAW))
P = dict(src['prices'])
divine = float(P.get('Divine Orb') or 363)
FLOOR = 1.0                                     # 1 Exalted Orb
# explicit fixes (English poe2scout name -> ex), on top of the tier rule below
OVERRIDE = {'Lesser Essence of Seeking': FLOOR, 'Lesser Essence of Haste': FLOOR}
adj = {}                                        # en -> {"from": old price, "why": "tier"|"override"|"none"}

# tier rule: essences - a Lesser or normal essence dearer than the Greater one of the same family; runes - a Lesser rune dearer
# than the normal one. Perfect essences do a different job (rare items), so they are not compared. Only prices above 1 ex are lowered.
def family(n):
    m = re.match(r'^(Lesser |Greater |Perfect )?(Essence of .+|.+ Rune)$', n)
    return (m.group(2), (m.group(1) or 'normal').strip()) if m else (None, None)
fams = {}
for n, v in P.items():
    f, t = family(n)
    if f: fams.setdefault(f, {})[t] = (n, v)
for f, d in fams.items():
    if f.startswith('Essence of') and 'Greater' in d:
        g = d['Greater'][1]
        for t in ('Lesser', 'normal'):
            if t in d and d[t][1] > g and d[t][1] > FLOOR: adj[d[t][0]] = {'from': d[t][1], 'why': 'tier'}
    elif f.endswith(' Rune') and 'Lesser' in d and 'normal' in d:
        if d['Lesser'][1] > d['normal'][1] and d['Lesser'][1] > FLOOR: adj[d['Lesser'][0]] = {'from': d['Lesser'][1], 'why': 'tier'}
for n, v in OVERRIDE.items():
    if n in P and n not in adj and P[n] != v: adj[n] = {'from': P[n], 'why': 'override'}
for n in adj: P[n] = OVERRIDE.get(n, FLOOR)

craft = json.load(open(ROOT + '/site/data/crafting.json'))
items = [x for k in craft for x in craft[k]]
runes = set()
for f in glob.glob(ROOT + '/site/data/c/*.json'):
    for x in json.load(open(f)).get('runes', []):
        for t in x['t']:
            runes.add(t[1])
out, used, ids = {}, set(), {}
for x in items:
    ids[x['en']] = x['id']
    if x['en'] in P:
        out[x['id']] = P[x['en']]; used.add(x['en'])
for en in sorted(runes):
    if en in P:
        out['rune:' + en] = P[en]; used.add(en); ids[en] = 'rune:' + en
# no price at all: too cheap to show up in trades -> 1 ex (game currencies only; runes without data stay unpriced)
noprice = [x for x in items if x['en'] not in P and x['id'] != 'Exalted_Orb']
for x in noprice:
    out[x['id']] = FLOOR; adj[x['en']] = {'from': None, 'why': 'none'}
fetched = src.get('fetched') or re.search(r'(\d{4}-\d{2}-\d{2})', RAW).group(1)
json.dump({'fetched': fetched, 'source': 'poe2scout', 'unit': 'ex', 'divine': divine, 'p': out,
           'adj': {ids.get(n, n): a for n, a in adj.items()}},
          open(ROOT + '/site/data/prices.json', 'w'), ensure_ascii=False, separators=(',', ':'))
kr = {x['en']: x['kr'] for x in items}
print(f'prices.json: {len(out)} prices ({fetched}, 1 div = {divine:g} ex) from {os.path.basename(RAW)}')
print(f'set to 1 ex - odd price ({sum(1 for a in adj.values() if a["why"] != "none")}):')
for n, a in sorted(adj.items(), key=lambda x: -(x[1]['from'] or 0)):
    if a['why'] != 'none': print(f'   {n} / {kr.get(n, "(룬·데이터 밖)")}: {a["from"]:g} ex -> 1 ex ({a["why"]})')
print(f'set to 1 ex - no price ({len(noprice)}):')
for x in noprice: print('  ', x['id'], x['kr'])
miss_p = [n for n in P if n not in used]
print(f'price names not in our data ({len(miss_p)}):')
for n in miss_p: print('  ', n, P[n])
