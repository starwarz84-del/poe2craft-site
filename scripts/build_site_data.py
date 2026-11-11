import json, re, base64, io, os
from PIL import Image
RAW='/home/claude/poe2data/raw/'; OUT='/home/claude/poe2data/site/data/'
os.makedirs(OUT+'c',exist_ok=True)
m=json.load(open(RAW+'poe2db_mods_raw.json'))
bi=json.load(open(RAW+'poe2db_bases_images_raw.json'))
labels=json.load(open(RAW+'class_labels_kr.json'))
import collections
rp=json.load(open(RAW+'repoe_base_items.json'))
rp_by=collections.defaultdict(list)
for key,v in rp.items():
    if v.get('domain')=='item': rp_by[v['name']].append((key.split('/')[-1],v))
SOCKET_IMPL={'Gloves':'gloves','Helmet':'helmet','Boots':'boots'}
RUNE_SRC={'gloves':'Gloves_str','helmet':'Helmets_str','boots':'Boots_str'}
def base_kind(name, implicit_en):
    ents=rp_by.get(name,[])
    keys=[k for k,_ in ents]; tags=set(t for _,v in ents for t in v['tags']); rs={v['release_state'] for _,v in ents}
    if 'runeforged' in tags: return 'rune'
    if any('Modifier allowed' in x or 'Modifiers allowed' in x for x in implicit_en): return 'mod'
    if any('Breach' in k for k in keys): return 'breach'
    if 'unique_only' in rs or 'demigods' in tags or any(k.startswith(('StormBlade','EtherealBlade')) for k in keys) or 'FourRingBase' in keys: return 'unique'
    return ''
def mod_delta(implicit_en):
    t=' '.join(implicit_en); d={'p':0,'s':0}
    for n,w in re.findall(r'([+-]\d+) (Prefix|Suffix) Modifiers? allowed',t): d['p' if w=='Prefix' else 's']+=int(n)
    return d
def jewel_socket(implicit_en):
    m=re.search(r'as though it was (?:a )?(Gloves|Helmet|Boots)',' '.join(implicit_en))
    return SOCKET_IMPL[m.group(1)] if m else None
# section -> (pool code, sub label kr, sub label en)
SEC={'normal':('n','일반','Base'),'desecrated':('d','훼손','Desecrated'),'essence':('e','에센스','Essence'),'perfect_essence':('e','완벽한 에센스','Perfect Essence'),
 'marksman':('x','콜르의 사냥',"Kolr's Hunt"),'decay':('x','카틀라의 순흑',"Katla's Gloom"),'soul':('x','메드베드의 보살핌',"Medved's Tending"),
 'destruction':('x','스루드의 완력',"Thrud's Might"),'berserking':('x','보라나의 학살',"Vorana's Carnage"),'chronomancy':('x','우트레드의 성좌',"Uhtred's Sidereus"),
 'breach_otherworldly':('x','이계','Otherworldly'),'breach_minion':('x','기원의 나무 소환수','Genesis Tree Minion'),'breach_caster':('x','기원의 나무 시전','Genesis Tree Caster'),
 'liquid':('x','액체 감정','Liquid Emotions'),
 'corrupted':('c','타락','Corrupted'),'corruption_upgrade':('u','희생','Orb of Sacrifice')}
TWO_HAND={'Bows','Staves','Two_Hand_Swords','Two_Hand_Axes','Two_Hand_Maces','Quarterstaves','Crossbows','Talismans'}
pat=lambda t: re.sub(r'\d+(\.\d+)?','#',t)
GROUPS=[('weapon','한손 무기',['Claws','Daggers','Wands','One_Hand_Swords','One_Hand_Axes','One_Hand_Maces','Sceptres','Spears','Flails','Traps']),
 ('weapon2','양손 무기',['Bows','Staves','Two_Hand_Swords','Two_Hand_Axes','Two_Hand_Maces','Quarterstaves','Crossbows','Talismans']),
 ('offhand','보조',['Quivers','Shields_str','Shields_str_dex','Shields_str_int','Bucklers','Foci']),
 ('helmet','투구',[k for k in m['classes'] if k.startswith('Helmets')]),
 ('body','갑옷',[k for k in m['classes'] if k.startswith('Body')]),
 ('gloves','장갑',[k for k in m['classes'] if k.startswith('Gloves')]),
 ('boots','장화',[k for k in m['classes'] if k.startswith('Boots')]),
 ('jewellery','장신구',['Amulets','Rings','Belts']),
 ('jewel','주얼',['Ruby','Emerald','Sapphire','Diamond','Time-Lost_Ruby','Time-Lost_Emerald','Time-Lost_Sapphire','Time-Lost_Diamond']),
 ('flask','플라스크',['Life_Flasks','Mana_Flasks','Charms'])]
assert sorted(sum((g[2] for g in GROUPS),[]))==sorted(m['classes'])
def short_kr(cid):
    l=labels[cid]; mm=re.match(r'.+\((.+)\)$',l)
    return mm.group(1) if mm else l
def sockets(cid,c):
    if 'socketable' not in c['sections']: return 0
    return 2 if (cid in TWO_HAND or cid.startswith('Body')) else 1
def shrink(b64):
    im=Image.open(io.BytesIO(base64.b64decode(b64))).convert('RGBA'); s=min(1,200/max(im.size))
    if s<1: im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    o=io.BytesIO(); im.save(o,'WEBP',quality=82,method=4); return 'data:image/webp;base64,'+base64.b64encode(o.getvalue()).decode()
imgcache={}
def build_runes(secs):
    bonded={r['n_us']:[r['t_kr'],r['t_us']] for r in secs.get('bonded',[])}
    runes=[]; ridx={}
    for r in secs.get('socketable',[]):
        f=r['fam'][0] if r['fam'] else r['n_us']
        if f not in ridx: ridx[f]=len(runes); runes.append({'f':f,'t':[]})
        runes[ridx[f]]['t'].append([r['n_kr'],r['n_us'],r['t_kr'],r['t_us'],*(bonded.get(r['n_us'],['',''] ))])
    for r in runes: r['t'].reverse()
    return runes
index={'collected_at':m['collected_at'],'patch':'0.5.5','groups':[]}
for gid,gkr,ids in GROUPS:
    index['groups'].append({'id':gid,'kr':gkr,'classes':[{'id':c,'en':m['classes'][c]['label'],'kr':labels[c],'short':short_kr(c),'sockets':sockets(c,m['classes'][c])} for c in ids]})
for cid,c in m['classes'].items():
    secs=c['sections']; groups=[]; gidx={}
    for s,(code,lk,le) in SEC.items():
        for i,r in enumerate(secs.get(s,[])):
            if r.get('lvl') is None: continue
            gen={'1':'p','2':'s'}.get(str(r['gen']),'i')   # i = implicit (corruption)
            key=(code,lk,gen,tuple(r['fam']),pat(r['t_us']))
            if key not in gidx: gidx[key]=len(groups); groups.append({'s':code,'sub':[lk,le],'g':gen,'f':list(key[3]),'m':[]})
            groups[gidx[key]]['m'].append(r)
    for g in groups:
        ms=sorted(g['m'],key=lambda r:-r['lvl'])
        g['t']=[[r['lvl'],r['w'],r['n_kr'],r['n_us'],r['t_kr'],r['t_us']] for r in ms]; g['tg']=sorted({t for r in ms for t in r.get('tags',[])}); del g['m']
    # runes: family groups, strongest first; bonded text by rune name
    runes=build_runes(secs)
    bases=[]; rune_extra=set()
    for a,k in zip(bi['bases'][cid]['us'],bi['bases'][cid]['kr']):
        req=' '.join(a['req']); mm=re.search(r'Level (\d+)',req); lv=int(mm.group(1)) if mm else 0
        sp=base_kind(a['name'],a['implicit']); md=mod_delta(a['implicit']); js=jewel_socket(a['implicit'])
        if js: rune_extra.add(js)
        if a['icon'] not in imgcache and bi['images'].get(a['icon']): imgcache[a['icon']]=shrink(bi['images'][a['icon']])
        bases.append({'id':a['key'],'en':a['name'],'kr':k['name'],'img':imgcache.get(a['icon'],''),'lv':lv,'sp':sp,'pd':md['p'],'sd':md['s'],'sock':(1 if js else sockets(cid,c)),'rk':js or '',
          'req':[a['req'],k['req']],'props':[a['props'],k['props']],'imp':[a['implicit'],k['implicit']]})
    data={'id':cid,'en':c['label'],'kr':labels[cid],'sockets':sockets(cid,c),'bases':bases,'groups':groups,'runes':runes,
          'runesBy':{k:build_runes(m['classes'][RUNE_SRC[k]]['sections']) for k in sorted(rune_extra)}}
    open(OUT+f'c/{cid}.json','w').write(json.dumps(data,ensure_ascii=False,separators=(',',':')))
json.dump(index,open(OUT+'index.json','w'),ensure_ascii=False,separators=(',',':'))
tot=sum(os.path.getsize(OUT+'c/'+f) for f in os.listdir(OUT+'c'))
print('MB',round(tot/1e6,1))
d=json.load(open(OUT+'c/Body_Armours_str.json'))
for cid in ['Rings','Amulets','Belts','Body_Armours_str','One_Hand_Swords']:
    d=json.load(open(OUT+f'c/{cid}.json'))
    print(cid, collections.Counter(b['sp'] for b in d['bases']), [ (b['en'],b['pd'],b['sd'],b['sock'],b['rk']) for b in d['bases'] if b['sp'] in('mod','breach','unique') or b['rk']], list(d['runesBy']))

# 알두르 룬 4종 = 모든 무기 (patch_aldur_runes.py, 사용자 확정 2026-11-11)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch_aldur_runes.py")).read())

# 무한의 에센스 문구를 능력치별로 (patch_essence_text.py, 2026-11-11)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch_essence_text.py")).read())

# SL 게임연구소 실험 가중치(주얼 6종·콜르의 사냥 장갑) (patch_sl_weights.py, 2026-11-11)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch_sl_weights.py")).read())

# poe2db 내부 능력치 줄 정리 (patch_raw_stats.py, 2026-11-11)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch_raw_stats.py")).read())
