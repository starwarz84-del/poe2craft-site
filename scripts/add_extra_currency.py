# Adds the currencies / omens that have a market price (raw/poe2scout_prices_*.json) but are missing from site/data/crafting.json,
# under crafting.json "extra". Names and effects come only from POE2DB: raw/poe2db_currency_raw.json (the poe2db.tw scrape) and
# raw/poe2db_extra_currency.json (single pages read from poe2db.tw/kr for items the scrape lacks). Nothing is translated here.
# Runs from build_prices.py (after build_crafting_items.py has rewritten crafting.json). Idempotent.
import json, glob, base64, io, re, urllib.parse
ROOT = '/home/claude/poe2data'
RAW = ROOT + '/raw/'; OUT = ROOT + '/site/data/crafting.json'
# what each crafting-related extra does (used by the recipe notes / tooltips; the rest are map / league omens)
ACT = {'Architects_Orb': 'architect', 'Vaal_Cultivation_Orb': 'cultivate', 'Vaal_Siphoner': 'siphon', 'Orb_of_Chance': 'chance',
       'Orb_of_Extraction': 'extract', 'Perfect_Flux': 'flux', 'Blazing_Flux': 'flux', 'Chilling_Flux': 'flux', 'Crackling_Flux': 'flux',
       'Void_Flux': 'flux', 'Omen_of_Chance': 'chance_omen', 'Omen_of_the_Ancients': 'chance_omen', 'Artificers_Shard': 'shard',
       'Perfect_Jewellers_Orb': 'jeweller', 'Greater_Jewellers_Orb': 'jeweller', 'Lesser_Jewellers_Orb': 'jeweller', 'Gemcutters_Prism': 'gem_quality'}

def icon(imgs, u, size=48):
    b = imgs.get(u or '')
    if not b: return ''
    from PIL import Image
    im = Image.open(io.BytesIO(base64.b64decode(b))).convert('RGBA'); im.thumbnail((size, size), Image.LANCZOS)
    o = io.BytesIO(); im.save(o, 'WEBP', quality=85); return 'data:image/webp;base64,' + base64.b64encode(o.getvalue()).decode()

def lines(txt, active):
    xs = [x.strip() for x in (txt or '').split('\n') if x.strip()]
    if len(xs) > 1 and active(xs[0]): xs = xs[1:]
    return ' '.join(xs)

def main(verbose=True):
    prices = json.load(open(sorted(glob.glob(RAW + 'poe2scout_prices_*.json'))[-1]))['prices']
    craft = json.load(open(OUT)); craft.pop('extra', None)
    have = {x['en'] for k in craft for x in craft[k]}
    runes = set()
    for f in glob.glob(ROOT + '/site/data/c/*.json'):
        for x in json.load(open(f)).get('runes', []):
            for t in x['t']: runes.add(t[1])
    cur = json.load(open(RAW + 'poe2db_currency_raw.json'))
    imgs = json.load(open(RAW + 'poe2db_bases_images_raw.json'))['images']
    src = {}
    for kind in ['currency', 'essence', 'catalyst', 'omen']:
        for a, b in zip(cur[kind]['us'], cur[kind]['kr']):
            src[a['name']] = (a, b)
    extra_pages = {x['en']: x for x in json.load(open(RAW + 'poe2db_extra_currency.json'))['items']}
    out, notfound = [], []
    for en in prices:
        if en in have or en in runes: continue
        if en in src:
            a, b = src[en]
            key = re.sub(r'[^A-Za-z0-9_]', '', urllib.parse.unquote(a['key']).replace('(', '').replace(')', '').replace(' ', '_'))
            it = {'id': key, 'en': a['name'], 'kr': b['name'],
                  'fx': lines(b['mods'][0] if b.get('mods') else '', lambda s: '활성화되어' in s),
                  'fxen': lines(a['mods'][0] if a.get('mods') else '', lambda s: 'is in your inventory' in s.lower()),
                  'icon': icon(imgs, a.get('icon')), 'src': 'poe2db'}
        elif en in extra_pages:
            x = extra_pages[en]
            it = {'id': x['key'], 'en': en, 'kr': x['kr'], 'fx': x['fx'], 'fxen': x['fxen'], 'icon': '', 'src': 'poe2db-page'}
        else:
            notfound.append(en); continue
        if it['id'] in ACT: it['act'] = ACT[it['id']]
        out.append(it)
    craft['extra'] = out
    json.dump(craft, open(OUT, 'w'), ensure_ascii=False, separators=(',', ':'))
    if verbose:
        print(f'crafting.json extra: {len(out)} items from POE2DB')
        for it in out: print('  ', it['id'], it['kr'], '(' + it.get('act', '-') + ')')
        if notfound: print('not found on POE2DB data (left out):', notfound)
    return out, notfound

if __name__ == '__main__':
    main()
