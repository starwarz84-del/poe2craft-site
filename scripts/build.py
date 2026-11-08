import json, re, collections, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

RAW='/home/claude/poe2data/raw/'
OUT='/home/claude/poe2data/out/'
m=json.load(open(RAW+'poe2db_mods_raw.json'))
cur=json.load(open(RAW+'poe2db_currency_raw.json'))
kr_labels=json.load(open(RAW+'class_labels_kr.json'))

GEN={'1':'prefix','2':'suffix','3':'corrupted','5':'corrupted','0':'socket'}
GEN_KR={'prefix':'접두','suffix':'접미','corrupted':'타락','socket':'소켓'}
SEC_KR={'normal':'일반','desecrated':'신성모독','corrupted':'타락(바알)','corruption_upgrade':'타락 강화',
 'essence':'에센스','perfect_essence':'완벽한 에센스','socketable':'룬·소켓','bonded':'결속 소켓',
 'breach_otherworldly':'균열(이계)','breach_minion':'균열(소환수)','breach_caster':'균열(시전자)',
 'destruction':'파괴 룬','soul':'영혼 룬','marksman':'명사수 룬','decay':'부패 룬','chronomancy':'시간술 룬',
 'berserking':'광전사 룬','liquid':'액체 감정'}
ILVL=82
pat=lambda t: re.sub(r'\d+(\.\d+)?','#',t)

classes=[]; rows_all=[]
for cid,c in m['classes'].items():
    secs={}
    for s,rows in c['sections'].items():
        if s=='ids': continue
        rows=[r for r in rows if r.get('lvl') is not None]
        if not rows: continue
        out=[]
        # tier within (gen, family, text pattern); T1 = highest level
        groups=collections.defaultdict(list)
        for r in rows: groups[(str(r['gen']),tuple(r['fam']),pat(r['t_us']),r['type'])].append(r)
        for (g,fam,_,_),lst in groups.items():
            lst=sorted(lst,key=lambda r:-r['lvl'])
            for i,r in enumerate(lst):
                gen=GEN.get(g, 'prefix' if g=='1' else g)
                out.append({'section':s,'gen':gen,'family':list(fam),'tier':i+1,'tiers':len(lst),
                 'ilvl':r['lvl'],'weight':r['w'],'tags':r['tags'],
                 'name_en':r['n_us'],'name_kr':r['n_kr'],'text_en':r['t_us'],'text_kr':r['t_kr'],
                 **({'essence_mod':r['code'],'req_level':r['reqlvl'],'perfect':r['perfect']=='1'} if s in('essence','perfect_essence') else {})})
        # naive share among normal mods of same gen at ilvl 82
        if s=='normal':
            tot=collections.Counter()
            for r in out:
                if r['ilvl']<=ILVL: tot[r['gen']]+=r['weight']
            for r in out:
                r['share_ilvl82']=round(r['weight']/tot[r['gen']],6) if r['ilvl']<=ILVL and tot[r['gen']] else 0
        out.sort(key=lambda r:(r['gen'],r['family'],r['tier']))
        secs[s]=out
        for r in out: rows_all.append((cid,r))
    classes.append({'id':cid,'name_en':c['label'],'name_kr':kr_labels.get(cid,c['label']),'sections':secs})

# currency-like items
def pair(kind):
    us=cur[kind]['us']; kr=cur[kind]['kr']
    assert [a['key'] for a in us]==[b['key'] for b in kr]
    return [{'id':a['key'],'art':a['art'],'icon':a.get('icon',''),'name_en':a['name'],'name_kr':b['name'],
             'effect_en':'\n'.join(a['mods']),'effect_kr':'\n'.join(b['mods']),
             'stack':(a['props'][0].split(':')[-1].strip() if a['props'] else '')} for a,b in zip(us,kr)]
items={k:pair(k) for k in ('currency','essence','catalyst','omen')}

meta={'source':'poe2db.tw (us / kr)','collected_at':m['collected_at'],
 'game_patch':'0.5.5 (The Forbidden Rites) — poe2db 기준',
 'notes':['weight = poe2db 표기 가중치(커뮤니티 측정값, Prohibited Library/Krakenbul 기반)',
          'tier = 같은 옵션 계열 안에서 요구 아이템 레벨 높은 순 (T1이 최상위)',
          'share_ilvl82 = 아이템 레벨 82 기준 같은 접두/접미 안에서의 단순 가중치 비율. 같은 계열 중복 제외·화폐 최소 티어 등은 반영 안 됨']}
json.dump({'meta':meta,'item_classes':classes,**items},open(OUT+'poe2_crafting_data.json','w'),ensure_ascii=False,separators=(',',':'))

# ---------- xlsx ----------
F=Font(name='Arial',size=10); HF=Font(name='Arial',size=10,bold=True,color='FFFFFF')
HFILL=PatternFill('solid',start_color='2F3640'); TF=Font(name='Arial',size=14,bold=True)
wb=Workbook()
def sheet(title,headers,rows,widths):
    ws=wb.create_sheet(title)
    ws.append(headers)
    for c in ws[1]: c.font=HF; c.fill=HFILL; c.alignment=Alignment(vertical='center')
    for r in rows: ws.append(r)
    for row in ws.iter_rows(min_row=2):
        for c in row: c.font=F
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
    return ws

# guide
ws=wb.active; ws.title='안내'
lines=[('POE2 크래프팅 데이터셋 (영문/한글)',TF),('',F),
 ('출처: poe2db.tw 영문(us)·한글(kr) 페이지 — 한글은 게임 공식 한글 문구',F),
 (f'수집 시각: {m["collected_at"][:16].replace("T"," ")} UTC · 패치 0.5.5 기준',F),('',F),
 ('시트 구성',Font(name='Arial',size=11,bold=True)),
 ('· 아이템종류: 옵션 데이터가 있는 아이템 종류 63개 (영문/한글명, 옵션 수)',F),
 ('· 일반옵션: 화폐로 붙는 일반 접두/접미 옵션 (티어, 요구 레벨, 가중치, 비율)',F),
 ('· 특수옵션: 신성모독·타락·에센스·룬·균열 등 일반 외 옵션',F),
 ('· 화폐 / 에센스 / 징조 / 기폭제: 이름·효과 영문/한글',F),('',F),
 ('열 설명',Font(name='Arial',size=11,bold=True)),
 ('· 티어: 같은 옵션 계열 안에서 요구 아이템 레벨이 높은 순으로 T1부터 번호 (T1 = 최상위)',F),
 ('· 가중치: poe2db 표기값. 게임 파일에 없는 값이라 커뮤니티(Prohibited Library / Krakenbul) 측정 기반 추정치',F),
 ('· 비율(ilvl82): 아이템 레벨 82에서 같은 접두/접미 옵션 전체 가중치 대비 비율. 파이썬으로 미리 계산한 참고값이며,',F),
 ('   같은 계열 중복 제외, 그레이터/퍼펙트 화폐의 최소 티어 제한 등은 반영하지 않음',F),
 ('· 가중치 0: 에센스·룬 등 직접 굴려서는 나오지 않는 옵션',F)]
for t,f in lines:
    ws.append([t]); ws.cell(ws.max_row,1).font=f
ws.column_dimensions['A'].width=110

sheet('아이템종류',['ID','영문명','한글명','일반 접두','일반 접미','특수 옵션 수'],
 [[c['id'],c['name_en'],c['name_kr'],
   sum(1 for r in c['sections'].get('normal',[]) if r['gen']=='prefix'),
   sum(1 for r in c['sections'].get('normal',[]) if r['gen']=='suffix'),
   sum(len(v) for k,v in c['sections'].items() if k!='normal')] for c in classes],[24,24,18,11,11,13])

cname={c['id']:(c['name_en'],c['name_kr']) for c in classes}
normal=[[cid,cname[cid][1],GEN_KR.get(r['gen'],r['gen']),', '.join(r['family']),f"T{r['tier']}",r['tiers'],r['ilvl'],r['weight'],r['share_ilvl82'],
  r['name_en'],r['name_kr'],r['text_en'],r['text_kr'],', '.join(r['tags'])] for cid,r in rows_all if r['section']=='normal']
ws=sheet('일반옵션',['아이템ID','아이템','구분','옵션 계열','티어','티어 수','요구 ilvl','가중치','비율(ilvl82)','옵션명(영문)','옵션명(한글)','효과(영문)','효과(한글)','태그'],
 normal,[18,12,7,24,6,7,8,8,11,22,16,42,36,28])
for c in ws['I'][1:]: c.number_format='0.00%'

special=[[cid,cname[cid][1],SEC_KR.get(r['section'],r['section']),GEN_KR.get(r['gen'],r['gen']),', '.join(r['family']),f"T{r['tier']}",r['ilvl'],r['weight'],
  r['name_en'],r['name_kr'],r['text_en'],r['text_kr']] for cid,r in rows_all if r['section']!='normal']
sheet('특수옵션',['아이템ID','아이템','종류','구분','옵션 계열','티어','요구 ilvl','가중치','이름(영문)','이름(한글)','효과(영문)','효과(한글)'],
 special,[18,12,13,7,24,6,8,8,26,20,42,36])

for k,t in (('currency','화폐'),('essence','에센스'),('omen','징조'),('catalyst','기폭제')):
    sheet(t,['ID','영문명','한글명','중첩','효과(영문)','효과(한글)'],
      [[x['id'],x['name_en'],x['name_kr'],x['stack'],x['effect_en'],x['effect_kr']] for x in items[k]],[28,30,24,8,70,60])
wb.save(OUT+'poe2_crafting_data.xlsx')
print('classes',len(classes),'normal',len(normal),'special',len(special),{k:len(v) for k,v in items.items()})
