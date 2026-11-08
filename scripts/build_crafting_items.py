import json, base64, io, re
from PIL import Image
RAW='/home/claude/poe2data/raw/'; OUT='/home/claude/poe2data/site/data/'
cur=json.load(open(RAW+'poe2db_currency_raw.json')); imgs=json.load(open(RAW+'poe2db_bases_images_raw.json'))['images']
def icon(u, size=48):
    b=imgs.get(u)
    if not b: return ''
    im=Image.open(io.BytesIO(base64.b64decode(b))).convert('RGBA'); im.thumbnail((size,size), Image.LANCZOS)
    o=io.BytesIO(); im.save(o,'WEBP',quality=85); return 'data:image/webp;base64,'+base64.b64encode(o.getvalue()).decode()
def pair(kind):
    return {a['key']:(a,b) for a,b in zip(cur[kind]['us'],cur[kind]['kr'])}
C=pair('currency'); E=pair('essence'); O=pair('omen')
def item(src,key,**extra):
    a,b=src[key]; lines=[x.strip() for x in (b['mods'][0] if b['mods'] else '').split('\n') if x.strip()]
    if lines and '활성화되어 있을 때' in lines[0] and len(lines)>1: lines=lines[1:]
    le=[x.strip() for x in (a['mods'][0] if a['mods'] else '').split('\n') if x.strip()]
    if le and 'is in your inventory' in le[0].lower() and len(le)>1: le=le[1:]
    return {'id':key,'en':a['name'],'kr':b['name'],'fx':' '.join(lines),'fxen':' '.join(le),'icon':icon(a.get('icon','')),**extra}
orbs=[]
for base,act in [('Orb_of_Transmutation','transmute'),('Orb_of_Augmentation','augment'),('Regal_Orb','regal'),('Exalted_Orb','exalt'),('Chaos_Orb','chaos')]:
    tiers=[('',0)]+([('Greater_',55),('Perfect_',70)] if act in('transmute','augment') else [('Greater_',35),('Perfect_',50)])
    for pre,minl in tiers:
        k=(pre+base) if pre else base
        orbs.append(item(C,k,act=act,min=minl,tier=pre.strip('_').lower() or 'normal'))
for k,act in [('Orb_of_Alchemy','alchemy'),('Orb_of_Annulment','annul'),('Divine_Orb','divine'),('Fracturing_Orb','fracture'),('Vaal_Orb','vaal'),('Artificers_Orb','artificer')]:
    orbs.append(item(C,k,act=act,min=0,tier='normal'))
bones=[]
for k in ['Altered_Collarbone','Gnawed_Jawbone','Preserved_Jawbone','Ancient_Jawbone','Gnawed_Rib','Preserved_Rib','Ancient_Rib','Gnawed_Collarbone','Preserved_Collarbone','Ancient_Collarbone','Preserved_Cranium']:
    part = 'jaw' if 'Jaw' in k else 'rib' if 'Rib' in k else 'collar' if 'Collar' in k else 'cranium'
    bones.append(item(C,k,act='desecrate',part=part,min=40 if k.startswith('Ancient') else 0,maxilvl=64 if k.startswith('Gnawed') else 0))
ess=[]
for k,(a,b) in E.items():
    n=a['name']; tier='alloy' if 'Alloy' in n else 'perfect' if n.startswith('Perfect') else 'greater' if n.startswith('Greater') else 'lesser' if n.startswith('Lesser') else 'normal'
    it=item(E,k,act='essence',tier=tier, size=40)
    it['mode']='rare' if '제거' in it['fx'] else 'magic'
    if tier=='normal' and it['mode']=='rare': it['tier']='special'
    ess.append(it)
OMEN_ACT={'Omen_of_Whittling':'whittling','Omen_of_Sinistral_Erasure':'sin_erasure','Omen_of_Dextral_Erasure':'dex_erasure','Omen_of_Sinistral_Alchemy':'sin_alchemy','Omen_of_Dextral_Alchemy':'dex_alchemy',
 'Omen_of_Sinistral_Coronation':'sin_coronation','Omen_of_Dextral_Coronation':'dex_coronation','Omen_of_Corruption':'corruption','Omen_of_Greater_Exaltation':'greater_exaltation',
 'Omen_of_Sinistral_Exaltation':'sin_exaltation','Omen_of_Dextral_Exaltation':'dex_exaltation','Omen_of_Greater_Annulment':'greater_annulment','Omen_of_Sinistral_Annulment':'sin_annulment',
 'Omen_of_Dextral_Annulment':'dex_annulment','Omen_of_Homogenising_Exaltation':'homo_exaltation','Omen_of_Homogenising_Coronation':'homo_coronation','Omen_of_the_Blessed':'blessed',
 'Omen_of_Dextral_Crystallisation':'dex_crystal','Omen_of_Sinistral_Crystallisation':'sin_crystal','Omen_of_Catalysing_Exaltation':'catalysing','Omen_of_Abyssal_Echoes':'echoes',
 'Omen_of_the_Sovereign':'sovereign','Omen_of_the_Liege':'liege','Omen_of_the_Blackblooded':'blackblooded','Omen_of_Light':'light','Omen_of_Sinistral_Necromancy':'sin_necro','Omen_of_Dextral_Necromancy':'dex_necro','Omen_of_Sanctification':'sanctify','Omen_of_Putrefaction':'putrefaction'}
qual=[item(C,'Blacksmiths_Whetstone',act='quality',qk='weapon'),item(C,'Armourers_Scrap',act='quality',qk='armour'),item(C,'Arcanists_Etcher',act='quality',qk='caster'),
      item(C,'Vaal_Blacksmiths_Infuser',act='infuse',qk='weapon'),item(C,'Vaal_Armourers_Infuser',act='infuse',qk='armour'),item(C,'Vaal_Arcanists_Infuser',act='infuse',qk='caster'),item(C,'Vaal_Catalysing_Infuser',act='infuse',qk='jewellery')]
sac=[item(C,'Yaomacs_Orb_of_Sacrifice',act='sacrifice',part='weapon'),item(C,'Kopecs_Orb_of_Sacrifice',act='sacrifice',part='armour'),item(C,'Kamasas_Orb_of_Sacrifice',act='sacrifice',part='jewellery'),item(C,'Yuguls_Orb_of_Sacrifice',act='sacrifice',part='jewel')]
qual.append(item(C,'Glassblowers_Bauble',act='quality',qk='flask'))
special=[item(C,'Hinekoras_Lock',act='hinekora'),item(C,'Mirror_of_Kalandra',act='mirror')]
CAT=pair('catalyst'); idx=json.load(open(OUT+'index.json')); ctag={c['id']:c for c in idx['catalysts']}
cats=[item(CAT,k,act='catalyst',tag=ctag[k]['tag'],on=ctag[k]['on']) for k in CAT if k in ctag]
liquids=[item(C,k,act='liquid',mode='rare') for k in C if 'Liquid' in k and 'Verisium' not in k]
omens=[item(O,k,omen=v) for k,v in OMEN_ACT.items()]
json.dump({'special':special,'cats':cats,'liquids':liquids,'qual':qual,'sac':sac,'orbs':orbs,'bones':bones,'essences':ess,'omens':omens},open(OUT+'crafting.json','w'),ensure_ascii=False,separators=(',',':'))
import os; print(len(qual),len(sac),len(orbs),len(bones),len(ess),len(omens), os.path.getsize(OUT+'crafting.json')//1000,'KB', sum(1 for x in special+cats+liquids+qual+sac+orbs+bones+ess+omens if not x['icon']),'no icon')
