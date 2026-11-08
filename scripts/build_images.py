import json, base64, os, io, zipfile
from PIL import Image
RAW='/home/claude/poe2data/raw/'; OUT='/home/claude/poe2data/out/'
d=json.load(open(RAW+'poe2db_bases_images_raw.json'))
cur=json.load(open(RAW+'poe2db_currency_raw.json'))
labels=json.load(open(RAW+'class_labels_kr.json'))
mods=json.load(open(RAW+'poe2db_mods_raw.json'))
PFX='https://cdn.poe2db.tw/image/Art/2DItems/'
def rel(u): return 'images/'+u[len(PFX):] if u.startswith(PFX) else 'images/other/'+u.split('/')[-1]
zf=zipfile.ZipFile(OUT+'poe2_item_images.zip','w',zipfile.ZIP_DEFLATED)
sizes={}
for u,b in d['images'].items():
    raw=base64.b64decode(b); p=rel(u)
    zf.writestr(p,raw); sizes[p]=Image.open(io.BytesIO(raw)).size
zf.close()
bases=[]
for cid,v in d['bases'].items():
    for a,k in zip(v['us'],v['kr']):
        assert a['key']==k['key']
        p=rel(a['icon']) if a['icon'] else None
        bases.append({'class_id':cid,'class_en':mods['classes'][cid]['label'],'class_kr':labels[cid],'id':a['key'],
          'name_en':a['name'],'name_kr':k['name'],'image':p,'image_size':sizes.get(p),
          'requires_en':' '.join(a['req']),'requires_kr':' '.join(k['req']),
          'properties_en':a['props'],'properties_kr':k['props'],'implicit_en':a['implicit'],'implicit_kr':k['implicit']})
cimg={}
for kind in ('currency','essence','catalyst','omen'):
    cimg[kind]=[{'id':a['key'],'name_en':a['name'],'name_kr':b['name'],'image':rel(a['icon']) if a.get('icon') else None} for a,b in zip(cur[kind]['us'],cur[kind]['kr'])]
json.dump({'meta':{'source':'poe2db.tw','collected_at':d['collected_at'],'note':'image 경로는 poe2_item_images.zip 안의 경로. 이미지 권리는 Grinding Gear Games'},
  'base_items':bases,**{k+'_images':v for k,v in cimg.items()}},open(OUT+'poe2_base_items.json','w'),ensure_ascii=False,indent=1)
missing=[b['id'] for b in bases if not b['image'] or b['image'] not in sizes]
print('bases',len(bases),'images',len(sizes),'missing',missing[:5],len(missing))
print(bases[0]); print(sorted(set(sizes.values()))[:12])
