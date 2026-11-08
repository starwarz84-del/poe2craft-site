"""Craft of Exile 가중치와 우리 데이터(poedb) 대조.
사용: python3 -I tools/coe/compare.py <poec_data.json> [출력 json]
CoE 파일은 저장소에 넣지 않아요(외부 데이터). 결과(대조표)만 씀."""
import json, re, sys, collections
SRC = sys.argv[1]; OUT = sys.argv[2] if len(sys.argv)>2 else None
ROOT = '/home/claude/poe2craft-site/site/data'
t = open(SRC, encoding='utf-8').read()
if t.startswith('poecd='): t = t[6:]
d = json.loads(t.strip().rstrip(';'))
CLS2BASE = {'Claws':'11','Daggers':'12','Wands':'18','One_Hand_Swords':'13','One_Hand_Axes':'15','One_Hand_Maces':'16','Sceptres':'17','Spears':'216','Flails':'217',
 'Bows':'20','Staves':'21','Two_Hand_Swords':'22','Two_Hand_Axes':'24','Two_Hand_Maces':'23','Quarterstaves':'25','Crossbows':'228','Talismans':'244','Quivers':'4',
 'Shields_str':'5','Shields_str_dex':'8','Shields_str_int':'9','Bucklers':'6','Foci':'229',
 'Helmets_str':'52','Helmets_dex':'53','Helmets_int':'54','Helmets_str_dex':'55','Helmets_str_int':'56','Helmets_dex_int':'57',
 'Body_Armours_str':'45','Body_Armours_dex':'46','Body_Armours_int':'47','Body_Armours_str_dex':'48','Body_Armours_str_int':'49','Body_Armours_dex_int':'50',
 'Gloves_str':'33','Gloves_dex':'34','Gloves_int':'35','Gloves_str_dex':'36','Gloves_str_int':'37','Gloves_dex_int':'38',
 'Boots_str':'39','Boots_dex':'40','Boots_int':'41','Boots_str_dex':'42','Boots_str_int':'43','Boots_dex_int':'44',
 'Amulets':'2','Rings':'1','Belts':'3','Ruby':'26','Emerald':'27','Sapphire':'28','Life_Flasks':'60','Mana_Flasks':'61','Charms':'241'}
MG = {'n':'1','d':'10','e':'13'}
mods = {m['id_modifier']: m for m in d['modifiers']['seq']}
norm = lambda s: re.sub(r'\s+',' ', re.sub(r'\(?-?\d+(?:\.\d+)?(?:[—–-]-?\d+(?:\.\d+)?)?\)?', '#', s or '')).strip().lower()
res = {}; stats = collections.Counter()
for cls, bid in CLS2BASE.items():
    D = json.load(open(f'{ROOT}/c/{cls}.json'))
    avail = set(d['basemods'].get(bid, []))
    out = []
    for gi, g in enumerate(D['groups']):
        if g['s'] not in MG: continue
        side = 'prefix' if g['g']=='p' else 'suffix'
        fam = set(g['f']); txt = norm(g['t'][0][5].split('\n')[0])
        cands = [m for mid, m in mods.items() if mid in avail and m['affix']==side and m['id_mgroup']==MG[g['s']]
                 and fam & set(json.loads(m['modgroups'] or '[]'))]
        if len(cands) > 1: cands = [m for m in cands if norm(m['name_modifier'].split('\n')[0]) == txt] or cands
        if not cands: stats['no_match'] += 1; continue
        m = cands[0]; ct = sorted(d['tiers'].get(m['id_modifier'], {}).get(bid, []), key=lambda x: -int(x['ilvl']))
        ours = [(x[0], x[1]) for x in g['t']]; coe = [(int(x['ilvl']), int(x['weighting'])) for x in ct]
        same = ours == coe
        unknown = all(w <= 1 for _, w in ours)
        stats['matched'] += 1; stats['same' if same else 'diff'] += 1
        if unknown and coe and any(w > 1 for _, w in coe): stats['fills_unknown'] += 1
        out.append({'gi': gi, 's': g['s'], 'side': g['g'], 'name': g['t'][0][5].split('\n')[0], 'coe_id': m['id_modifier'], 'ours': ours, 'coe': coe, 'same': same, 'unknown': unknown})
    res[cls] = out
print(dict(stats))
if OUT: json.dump(res, open(OUT, 'w'), ensure_ascii=False)
