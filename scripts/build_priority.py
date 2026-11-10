# Builds site/data/priority.json: per item class (and per base where the base matters) the "core" modifiers
# a draft buys on its magic base first (policy 18). Ranked by (1) what our recipes actually make first on that
# class/base, then (2) the IGGM 0.5.0 crafting guide summary for the item type. Families that do not exist in the
# class data are dropped; classes/bases with neither source stay "미정" (unknown) and the draft starts from a
# normal base there. Sources are kept in the data only (not shown on screen).
import json, re
D = '/home/claude/poe2data/site/data/'
R = json.load(open(D + 'recipes.json'))['recipes']
I = json.load(open(D + 'index.json'))
C = {}
def cls(c):
    if c not in C:
        try: C[c] = json.load(open(D + 'c/' + c + '.json'))
        except FileNotFoundError: C[c] = None
    return C[c]

ELEM = ['FireResistance', 'ColdResistance', 'LightningResistance']
def key(fams):   # single elemental resistances count as one entry (policy 6: any element)
    return 'ELEM' if len(fams) == 1 and fams[0] in ELEM else '+'.join(fams)
def fams_of(k): return ELEM if k == 'ELEM' else k.split('+')

# ---- (1) recipe evidence: the lines each recipe makes first ----
def first_lines(r):
    c = cls(r['cls']); G = c['groups']; out = []
    def add(gi, how):
        g = G[gi]; f = g['f']
        if g['s'] != 'n' and not any(x['s'] == 'n' and x['f'] == f for x in G): return   # mechanics (max quality, liquids, soul cores) are no core lines
        out.append((key(f), g['g'], how))
    start = r.get('start') or {}
    for m in start.get('mods', []):
        sp = m.get('anyOf') or [m]
        if 'gi' in sp[0]: add(sp[0]['gi'], 'fr' if m.get('fr') else 'start')
    fr = any(m.get('fr') for m in start.get('mods', []))
    chaos_seen = False
    for n in r['nodes']:
        t = n.get('target') or {}; sp = t.get('anyOf') or ([t] if 'gi' in t else [])
        if n['do'] in ('exalt', 'desecrate', 'reveal'): break   # past the magic / fractured-base stage
        if not sp: continue
        if n['do'] in ('transmute', 'augment', 'regal'): add(sp[0]['gi'], n['do'])
        elif n['do'] == 'essence' and not fr: add(sp[0]['gi'], 'essence')
        elif n['do'] == 'chaos' and fr and not chaos_seen: add(sp[0]['gi'], 'chaos'); chaos_seen = True
    return out

ev_cls, ev_base = {}, {}
for r in R:
    c = cls(r['cls'])
    if not c: continue
    base = c['bases'][r['base']]['en']
    for k, side, how in first_lines(r):
        for tbl, kk in ((ev_cls, r['cls']), (ev_base, (r['cls'], base))):
            e = tbl.setdefault(kk, {}).setdefault(k, {'side': side, 'n': 0, 'recipes': []})
            e['n'] += 1
            if r['id'] not in e['recipes']: e['recipes'].append(r['id'])

# ---- (2) IGGM 0.5.0 guide summary (item type level), defence families by attribute ----
DEF = ['BaseLocalDefences', 'DefencesPercent']   # flat / % of the class's own defence (armour, evasion or energy shield)
ATTACK_W = ['Bows', 'Crossbows', 'Spears', 'Quarterstaves', 'Two_Hand_Maces', 'One_Hand_Maces', 'Two_Hand_Swords', 'Two_Hand_Axes',
            'One_Hand_Swords', 'One_Hand_Axes', 'Claws', 'Daggers', 'Flails', 'Talismans']
CASTER_W = ['Wands', 'Staves']
def iggm(c):
    if c.startswith('Boots_'): return ['MovementVelocity', 'ELEM', 'IncreasedLife'] + (DEF if 'int' in c else [])
    if c.startswith('Gloves_'): return ['ProjectileDamage', 'IncreaseSocketedGemLevel', 'IncreasedAttackSpeed']
    if c.startswith('Helmets_'): return ['ELEM'] + (DEF if 'int' in c else []) + ['CriticalStrikeChanceIncrease', 'IncreaseSocketedGemLevel']
    if c.startswith('Body_Armours_'):
        a = []
        if 'dex' in c: a += ['EvasionAppliesToDeflection']
        if 'str' in c: a += DEF + ['IncreasedLife']
        if 'int' in c: a += DEF + ['BaseSpirit']
        return list(dict.fromkeys(a))
    if c == 'Amulets': return ['BaseSpirit', 'IncreaseSocketedGemLevel']
    if c == 'Rings': return ['PhysicalDamage', 'FireDamage', 'ColdDamage', 'LightningDamage', 'ELEM', 'ItemFoundRarityIncrease', 'ItemFoundRarityIncreasePrefix']
    if c == 'Belts': return ['IncreasedLife', 'ELEM']
    if c in ATTACK_W: return ['LocalPhysicalDamagePercent', 'PhysicalDamage', 'LocalIncreasedPhysicalDamagePercentAndAccuracyRating']
    if c in CASTER_W: return ['IncreaseSocketedGemLevel', 'IncreasedCastSpeed', 'SpellCriticalStrikeChanceIncrease', 'CriticalStrikeChanceIncrease']
    if c in ('Ruby', 'Emerald', 'Sapphire', 'Time-Lost_Ruby', 'Time-Lost_Emerald', 'Time-Lost_Sapphire'):
        return ['CriticalStrikeChanceIncrease', 'CriticalStrikeMultiplier', 'EnergyShieldPercent']
    return []

def exists(c, k):   # the family has a regular-pool group in this class
    g = cls(c)
    return g and any(x['s'] == 'n' and (x['f'] == fams_of(k) or (k == 'ELEM' and len(x['f']) == 1 and x['f'][0] in ELEM)) for x in g['groups'])
def side_of(c, k):
    for x in cls(c)['groups']:
        if x['s'] == 'n' and (x['f'] == fams_of(k) or (k == 'ELEM' and x['f'][0] in ELEM and len(x['f']) == 1)): return x['g']

def core(c, ev, guide):
    out = []
    for k, e in sorted((ev or {}).items(), key=lambda kv: -kv[1]['n']):
        if exists(c, k): out.append({'f': fams_of(k), 'side': e['side'], 'src': 'recipes', 'n': e['n'], 'recipes': e['recipes']})
    for k in guide:
        if exists(c, k) and not any(fams_of(k) == x['f'] for x in out):
            out.append({'f': fams_of(k), 'side': side_of(c, k), 'src': 'iggm'})
    for i, x in enumerate(out): x['rank'] = i + 1
    return out

classes = {}
for grp in I['groups']:
    if grp['id'] == 'flask': continue
    for ci in grp['classes']:
        c = ci['id']
        if c in ('Diamond', 'Time-Lost_Diamond', 'Traps') or not cls(c): continue
        lst = core(c, ev_cls.get(c), iggm(c))
        e = {'kr': ci['kr'], 'status': 'ok' if lst else '미정', 'core': lst}
        # bases where the implicit changes what to buy first: rings and amulets, body armour with an implicit
        if c in ('Rings', 'Amulets') or c.startswith('Body_Armours_'):
            bs = {}
            for b in cls(c)['bases']:
                en = re.sub(r'^Rune(forged|mastered) ', '', b['en'])
                if en in bs: continue
                if c.startswith('Body_Armours_') and not any(x for x in (b.get('imp') or []) if x) and (c, b['en']) not in ev_base: continue
                ev = ev_base.get((c, b['en']))
                bl = core(c, ev, []) if ev else []
                bs[en] = {'kr': b['kr'], 'imp': ' / '.join(x if isinstance(x,str) else ' / '.join(x) for x in (b.get('imp') or []))[:80], 'status': 'ok' if bl else '미정', 'core': bl}
            e['bases'] = bs
        classes[c] = e

out = {'v': 1,
       'note': {'kr': '부위(클래스)·베이스별로 매직 단계에서 먼저 맞추는 핵심 옵션. 순위 = 우리 레시피에서 실제로 먼저 만든 옵션(횟수 순) → IGGM 0.5.0 제작 가이드 요약. 베이스 항목이 미정이면 클래스 항목을 씀. 화면에는 표시하지 않음.',
                'en': 'Core modifiers bought on the magic base first, per class and base. Rank: lines our recipes make first (by count), then the IGGM 0.5.0 crafting guide summary. A base marked 미정 falls back to its class. Not shown on screen.'},
       'sources': {'recipes': 'site/data/recipes.json (start mods, fractured line, magic-stage orbs/essence, first Chaos on a fractured base)',
                   'iggm': 'IGGM POE2 0.5.0 crafting guide (summary given by the user 2026-11-09)'},
       'classes': classes}
json.dump(out, open(D + 'priority.json', 'w'), ensure_ascii=False, indent=1)
und = [c for c, e in classes.items() if e['status'] == '미정']
print('classes', len(classes), 'unknown', und)
for c in ('Rings', 'Amulets'):
    print(c, 'bases with data', [b for b, x in classes[c]['bases'].items() if x['status'] == 'ok'])
