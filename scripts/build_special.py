# Special bases guide data → site/data/special.json (the "특수 베이스" tab, site/bases.html).
# Only game data (class files' bases: implicits, slot changes, level) plus our recipes that use each base. Nothing hand-written about mechanics
# except what the data itself says (e.g. Perfect Flux's effect text from crafting.json).
import json, glob, re
D='/home/claude/poe2data/site/data/'
idx=json.load(open(D+'index.json'))
CLS={c['id']:c for g in idx['groups'] for c in g['classes']}
craft=json.load(open(D+'crafting.json'))
recs=json.load(open(D+'recipes.json'))['recipes']

def cname(cid):
    c=CLS.get(cid); return {'kr':c['kr'],'en':c['en']} if c else {'kr':cid,'en':cid.replace('_',' ')}

# recipes by (class, base index) — one card per tier group (the high-end id)
use={}
_lead={}
for r in recs:   # one link per item: its best kept grade
    g=r.get('tierGroup')
    if g and (g not in _lead or ['high','bal','ess'].index(r['tier'])<['high','bal','ess'].index(_lead[g]['tier'])): _lead[g]=r
for r in recs:
    if r.get('tierGroup') and _lead[r['tierGroup']] is not r: continue
    use.setdefault((r['cls'], r['base']), []).append({'id':r['id'], 'title':r['title']})

SKILL=re.compile(r'^스킬 부여: 레벨 (\d+) (.+)$'); SKILL_EN=re.compile(r'^Grants Skill: Level (\d+) (.+)$')
ASIF=re.compile(r'인 것처럼|속성 부여 가능')
out={'skill':[], 'slots':[], 'breach':[], 'asif':[], 'rune':{}}
for f in sorted(glob.glob(D+'c/*.json')):
    c=json.load(open(f)); cid=c['id']
    for bi,b in enumerate(c['bases']):
        sp=b.get('sp') or ''; imp=b.get('imp') or [[],[]]; en,kr=imp[0],imp[1]
        if sp=='unique': continue
        item={'cls':cid,'clsName':cname(cid),'id':b['id'],'kr':b['kr'],'en':b['en'],'lv':b.get('dl') or b.get('lv'),
              'p':3+(b.get('pd') or 0),'s':3+(b.get('sd') or 0),'imp':[{'kr':k,'en':e} for k,e in zip(kr,en)],'recipes':use.get((cid,bi),[])}
        if sp=='rune':
            kind='Runeforged' if b['en'].startswith('Runeforged') else 'Runemastered' if b['en'].startswith('Runemastered') else 'other'
            out['rune'].setdefault(cid,{'clsName':cname(cid),'items':[]})['items'].append({k:item[k] for k in ('id','kr','en','lv','imp','recipes')}|{'kind':kind})
            continue
        item['img']=b.get('img')
        if any(SKILL.match(x) for x in kr) and sp=='mod':
            sk=[]
            for k,e in zip(kr,en):
                m=SKILL.match(k); me=SKILL_EN.match(e)
                if m: sk.append({'kr':m.group(2),'en':me.group(2) if me else e,'lv':int(m.group(1))})
            item['skills']=sk; item['imp']=[x for x in item['imp'] if not SKILL.match(x['kr'])]
            out['skill'].append(item)
        elif sp=='mod': out['slots'].append(item)
        elif sp=='breach': out['breach'].append(item)
        elif any(ASIF.search(x) for x in kr): out['asif'].append(item)
# user-confirmed facts per base (shown on the card) — only what the user or data confirmed
NOTE={'Absent_Amulet':{'kr':'매직 상태 없음: 진화·확장의 오브가 안 먹고, 노멀에서 제왕의 오브로 바로 레어(랜덤 옵션 1개)','en':'No magic stage: Transmutation and Augmentation do not work; a Regal Orb turns it straight from normal to rare (one random line)'}}
for k in ('skill','slots','breach','asif'):
    for it in out[k]:
        if it['id'] in NOTE: it['note']=NOTE[it['id']]
flux=next((x for x in craft['extra'] if x['id']=='Perfect_Flux'), None)
out['flux']={'id':'Perfect_Flux','kr':flux['kr'],'en':flux['en'],'fx':flux.get('fx'),'fxen':flux.get('fxen'),'icon':flux.get('icon')} if flux else None
# helper classes (e.g. Grasping_Mail_ring = body armour that rolls ring modifiers) repeat a base: keep one card, merge recipes
for k in ('skill','slots','breach','asif'):
    seen={}
    for it in out[k]:
        if it['id'] in seen: seen[it['id']]['recipes']+=it['recipes']
        else: seen[it['id']]=it
    out[k]=list(seen.values())
out['rune'].pop('Grasping_Mail_ring', None)
out['rune']=[{'cls':k}|v for k,v in out['rune'].items()]
json.dump(out, open(D+'special.json','w'), ensure_ascii=False, separators=(',',':'))
print('special:', {k:len(v) for k,v in out.items() if isinstance(v,list)}, 'rune bases', sum(len(x['items']) for x in out['rune']))
