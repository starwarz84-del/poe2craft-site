# Trade search links (사용자 확정 2026-11-11: 베이스템 구입 버튼 → 거래소에 조건 자동 입력)
# raw/trade2_stats_explicit_*.json  = [statnum, has_fractured(0/1), en text]  (pathofexile.com /api/trade2/data/stats, explicit block)
# raw/trade2_types_*.json           = {en:[base type names], kr:[...]}       (/api/trade2/data/items, en + Kakao)
# → site/data/trade.json {league, cat:{cls:id}, noType:{cls:[base idx]}, st:{cls:{gi:[[statnum, neg, fr], ...per line]}}}
import json, glob, re, collections, os
R='/home/claude/poe2data/'
LEAGUE='Forbidden Rites'   # trade league id (same on pathofexile.com and poe.kakaogames.com) — change when the league changes
rows=json.load(open(sorted(glob.glob(R+'raw/trade2_stats_explicit_*.json'))[-1]))
types=json.load(open(sorted(glob.glob(R+'raw/trade2_types_*.json'))[-1])); TE, TK = set(types['en']), set(types['kr'])
idx=collections.defaultdict(list)
for i,fr,t in rows:
    if '|' not in i: idx[t].append((i,fr))
CAT={'Claws':'weapon.claw','Daggers':'weapon.dagger','Wands':'weapon.wand','One_Hand_Swords':'weapon.onesword','One_Hand_Axes':'weapon.oneaxe','One_Hand_Maces':'weapon.onemace',
 'Sceptres':'weapon.sceptre','Spears':'weapon.spear','Flails':'weapon.flail','Bows':'weapon.bow','Staves':'weapon.staff','Two_Hand_Swords':'weapon.twosword','Two_Hand_Axes':'weapon.twoaxe',
 'Two_Hand_Maces':'weapon.twomace','Quarterstaves':'weapon.warstaff','Crossbows':'weapon.crossbow','Talismans':'weapon.talisman','Quivers':'armour.quiver','Bucklers':'armour.buckler','Foci':'armour.focus',
 'Amulets':'accessory.amulet','Rings':'accessory.ring','Belts':'accessory.belt','Life_Flasks':'flask.life','Mana_Flasks':'flask.mana','Charms':'flask.charm'}
def cat(c):
    if c in CAT: return CAT[c]
    for p,v in (('Shields','armour.shield'),('Helmets','armour.helmet'),('Body_Armours','armour.chest'),('Gloves','armour.gloves'),('Boots','armour.boots')):
        if c.startswith(p): return v
    if c in ('Ruby','Emerald','Sapphire','Diamond') or c.startswith('Time-Lost'): return 'jewel'
    return None
def norm(s):
    s=re.sub(r'\(([\d.]+)[—–-]([\d.]+)\)','#',s); s=re.sub(r'(?<![\w#])[+-]?\d+(\.\d+)?','#',s); return s.replace('+#','#').strip()
def find(l, local):
    n=norm(l); neg=0
    if n not in idx and n+' (Local)' not in idx and 'reduced' in n: n=n.replace('reduced','increased'); neg=1
    c = idx.get(n+' (Local)') if local and n+' (Local)' in idx else idx.get(n) or idx.get(n+' (Local)')
    return [c[0][0], neg, c[0][1]] if c else None
out={'league':LEAGUE,'cat':{},'noType':{},'st':{}}; tot=ok=0
for f in sorted(glob.glob(R+'site/data/c/*.json')):
    d=json.load(open(f)); c=d['id']; out['cat'][c]=cat(c)
    nt=[i for i,b in enumerate(d.get('bases',[])) if b['en'] not in TE or b['kr'] not in TK]
    if nt: out['noType'][c]=nt
    m={}
    for gi,g in enumerate(d['groups']):
        if g['s'] not in ('n','e','x'): continue
        lines=g['t'][0][5].split('\n'); loc=any('Local' in x for x in g.get('f',[]))
        got=[find(l,loc) for l in lines]; tot+=1
        if all(got): m[gi]=got; ok+=1
    out['st'][c]=m
json.dump(out,open(R+'site/data/trade.json','w'),ensure_ascii=False,separators=(',',':'))
print(f'trade.json: {ok}/{tot} groups mapped, base types missing on trade: {sum(len(v) for v in out["noType"].values())}, size {os.path.getsize(R+"site/data/trade.json")//1024} KB')
