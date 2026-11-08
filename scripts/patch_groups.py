# Recompute only the modifier groups (fast; leaves base images untouched)
import json, re, os, sys
sys.argv=['x']
src=open('/home/claude/poe2data/scripts/build_site_data.py').read()
head=src[:src.index('imgcache={}')]          # constants + helpers
ns={}; exec(head, ns)
m=ns['m']; SEC=ns['SEC']; pat=ns['pat']; OUT=ns['OUT']
for cid,c in m['classes'].items():
    secs=c['sections']; groups=[]; gidx={}
    for s,(code,lk,le) in SEC.items():
        for r in secs.get(s,[]):
            if r.get('lvl') is None: continue
            gen={'1':'p','2':'s'}.get(str(r['gen']),'i')
            key=(code,lk,gen,tuple(r['fam']),pat(r['t_us']))
            if key not in gidx: gidx[key]=len(groups); groups.append({'s':code,'sub':[lk,le],'g':gen,'f':list(key[3]),'m':[],'src':s})
            groups[gidx[key]]['m'].append(r)
    for g in groups:
        ms=sorted(g['m'],key=lambda r:-r['lvl'])
        g['t']=[[r['lvl'],r['w'],r['n_kr'],r['n_us'],r['t_kr'],r['t_us']] for r in ms]
        g['tg']=sorted({t for r in ms for t in r.get('tags',[])})
        g['cr']=1 if (g['src'] in ('essence','perfect_essence','liquid')) else 0
        del g['m']; del g['src']
    p=OUT+f'c/{cid}.json'; d=json.load(open(p))
    assert len(d['groups'])==len(groups) and all(a['t'][0][5]==b['t'][0][5] for a,b in zip(d['groups'],groups)), cid
    d['groups']=groups
    open(p,'w').write(json.dumps(d,ensure_ascii=False,separators=(',',':')))
# catalysts into index
cur=json.load(open('/home/claude/poe2data/raw/poe2db_currency_raw.json'))
TAG={'Life':'life','Mana':'mana','Armour, Evasion and Energy Shield':'defences','Physical':'physical','Fire':'fire','Cold':'cold','Lightning':'lightning','Chaos':'chaos','Attack':'attack','Caster':'caster','Speed':'speed','Attribute':'attribute','Minion':'minion'}
cats=[]
for a,b in zip(cur['catalyst']['us'],cur['catalyst']['kr']):
    mm=re.search(r'enhances (.+) modifiers on a (ring or amulet|jewel)',a['mods'][0])
    if not mm: continue
    cats.append({'id':a['key'],'en':a['name'],'kr':b['name'],'tag':TAG[mm.group(1)],'on':'jewel' if mm.group(2)=='jewel' else 'jewellery','kr_fx':b['mods'][0].split('\n')[0]})
idx=json.load(open(OUT+'index.json')); idx['catalysts']=cats
json.dump(idx,open(OUT+'index.json','w'),ensure_ascii=False,separators=(',',':'))
print('ok', len(cats))
