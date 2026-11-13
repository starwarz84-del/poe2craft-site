# Flowcharts for five easy recipes converted 2026-11-10 (사용자: 기존 등록 레시피를 쉬운 것부터 차례로).
# All are 어려움 이하 → Balance + Essential only (정책 30). Balance = the video, Essential = cheaper bought tiers / looser targets.
#   ragna-ashot-bow-v2, sane-resist-belt-v2, diztoh-budget-mace-v2, lilbotq-budget-boots-v2, icesly-budget-wand-v2
import json, os
H=os.path.dirname(os.path.abspath(__file__))
K=lambda kr,en: {'kr':kr,'en':en}
GRP=[{'id':'prep','kr':'베이스템 완성','en':'Finished base','cols':[0,1]},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers','cols':[0,1]}]
def it(s,kr,en,tags=None,m='n'):
    d={'s':s,'kr':kr,'en':en,'m':m}
    if tags: d['tags']=tags
    return d
J=lambda s: it(s,'잡옵','Junk',None,'j')
UN=lambda s: it(s,'훼손 옵션(미공개)','Desecrated (unrevealed)')
def st(s,kr,en): return {'s':s,'kr':kr,'en':en} if s else {'kr':kr,'en':en}
def act(id,grp,pos,a,cur,goal,shw,label,edges,item,**kw):
    d={'id':id,'kind':'act','group':grp,'pos':pos,'act':a,'goal':goal,'label':label,'edges':edges,'item':item}
    if cur: d['cur']=cur
    if shw: d['showText']=shw
    d.update(kw); return d
def annul(id,pos,edges,omens=('Omen_of_Light',),target=K('훼손 옵션 제거','Remove the desecrated modifier')):
    return {'id':id,'kind':'act','group':'main','pos':pos,'act':'annul','cur':'Orb_of_Annulment','omens':list(omens),
            'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':target,'edges':edges}
def base(next,start,label,item): return {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':next,'start':start,'label':label,'item':item}
def mark(pos,next,item): return {'id':'ms','kind':'mark','group':'main','pos':pos,'next':next,'label':K('아이템 제작 시작','Item crafting starts'),'item':item}
def done(pos): return {'id':'ok','kind':'done','group':'main','pos':pos,'label':K('완성','Finished')}
def graph(id,cls,bse,ilvl,note,params,P,desc,tags,nodes,loops,finals,finalItem,require,basePrice=None):
    VER=[('ess','에센셜','Essential'),('bal','밸런스','Balance')]
    g={'id':id,'recipe':id,'cls':cls,'base':bse,'ilvl':ilvl,'note':note,'params':params,
       'strategies':[{'id':v,'params':P[v]} for v in ('bal','ess')],
       'versions':[{'id':v,'kr':kr,'en':en,'params':P[v],'desc':desc[v]} for v,kr,en in VER],
       'tags':tags,'require':require,'groups':GRP,'start':'h1','loops':loops,'finals':finals,'finalItem':finalItem,'nodes':nodes}
    if basePrice: g['basePrice']=basePrice
    json.dump(g,open(f'{H}/{id}.json','w'),ensure_ascii=False,indent=1)
LIGHT_LOOP=lambda ids,kr,en: [{'id':'L1','nodes':ids,'kr':kr,'en':en}]
TV=lambda d: {k:K(*v) for k,v in d.items()}

# ---------- 1. 라그나 아샷 활 ----------
P={'bal':{'pT':1},'ess':{'pT':3}}
tags={'pct':{'gi':7,'tmax':'$pT'},'flat':{'gi':39},'as':{'gi':29},'asn':{'gi':15},'anyas':{'anyOf':['as','asn']},'anyam':{'anyOf':['as',{'gi':28},{'gi':30}]}}
I0=[it('p','물리 피해 % 증가','% physical damage',['pct']),J('s')]
I1=I0+[it('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)',['flat'])]
I2=I1+[it('p','랜덤 옵션 1개','One random line',None,'j')]
I3=I2+[UN('s')]
I4=I3+[it('s','랜덤 옵션 1개','One random line',None,'j')]
I5=I2+[it('s','랜덤 옵션 1개','One random line',None,'j'),it('s','공격 속도 + 반려수 공격 속도 (아마나무)','Attack speed + companion attack speed (Amanamu)',['as'])]
nodes=[base('w2',{'rar':'magic','mods':['pct'],'random':1},K('물리 피해 % 증가 매직 전쟁광 활 구입','Buy a magic Warmonger Bow with % physical'),I0),
 act('w2','prep',[0,1],'essence','Greater_Essence_of_Abrasion',K('레어로 업그레이드 + 접두 물리 피해 추가','Upgrade to rare + flat physical prefix'),[st('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='flat'),
 mark([0,1.5],'w3',I1),
 act('w3','main',[0,2],'exalt','Exalted_Orb',K('접두 세번째 옵션','Third prefix option'),[st('p','랜덤 옵션 1개 (원소 플랫이면 좋음) — 결과 그대로','One random line (an elemental flat is good) — keep whatever comes')],K('엑잘','Exalt'),[{'to':'w4'}],I2,omens=['Omen_of_Sinistral_Exaltation']),
 act('w4','main',[0,3],'desecrate','Preserved_Jawbone',K('접미 두번째 옵션(훼손)','Second suffix option (desecrated)'),[st('s','아마나무 훼손 옵션(미공개)','Amanamu desecration (unrevealed)')],K('훼손','Desecrate'),[{'if':{'unrev':True},'to':'w5'}],I3,omens=['Omen_of_the_Liege']),
 act('w5','main',[0,4],'exalt','Greater_Exalted_Orb',K('접미 세번째 옵션 (일반 공격 속도 먼저 노림)','Third suffix (a normal attack speed first)'),[st('s','랜덤 옵션 1개 (레벨 35+) — 공격 속도가 뜨면 훼손은 다른 아마나무 옵션으로','One random line (level 35+) — attack speed here frees the desecration for another Amanamu line')],K('엑잘','Exalt'),[{'to':'w6'}],I4,skipIf={'full':'s'},skipTo='w6'),
 act('w6','main',[0,5],'reveal',None,K('훼손 옵션 확인 (아마나무 3개 전부 나옴)','Reveal (all three Amanamu lines show)'),[st('s','공격 속도 + 반려수 공격 속도 (일반 공격 속도가 있으면 관통·정신력 효율 중 하나)','Attack speed + companion attack speed (with a normal attack speed: pierce or spirit efficiency)')],K('공개','Reveal'),[{'to':'ok'}],I5,want='as'),
 done([0,6])]
graph('ragna-ashot-bow-v2','Bows','Warmonger Bow',82,
  '라그나 아샷 활(영상 방식) — 물리 % 매직 구입 → 상위 마모의 에센스 → 좌측 찬미 + 엑잘(접두 결과 그대로) → 보존된 턱뼈 + 군왕의 징조(아마나무) → 상위 엑잘(접미 결과 그대로) → 공개: 군왕의 징조라 아마나무 접미 3개(공격 속도·관통·정신력 효율)가 전부 나와서 공격 속도 확정(영상 5:06 확인). 마지막 엑잘에서 일반 공격 속도가 뜨면 같은 계열이라 훼손은 관통·정신력 효율 중 하나. 밸런스 = 영상(물리 % 1티어), 에센셜 = 물리 % 1~3티어 베이스.',
  {'pT':{'kr':'물리 피해 %','en':'% physical','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})}},P,
  {'bal':K('물리 % 1티어 매직 구입 (영상)','Buy a T1 % physical magic bow (as the video)'),'ess':K('물리 % 1~3티어 매직 구입','Buy a T1–3 % physical magic bow')},
  tags,nodes,[],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'pct','tmax':t},{'tag':'flat','tmax':1},{'side':'p','random':True},{'tag':'as','tmax':1},{'side':'s','random':True},{'side':'s','random':True}]} for v,kr,en,t in (('bal','밸런스 옵션','Balance',1),('ess','에센셜 옵션','Essential',3))],
  {'quality':20,'sockets':0},{'all':[{'has':'anyas'},{'full':'p'},{'full':'s'}]})

# ---------- 2. TheSaneExile 저항 벨트 ----------
P={'bal':{'lT':1,'rT':2},'ess':{'lT':3,'rT':3}}
tags={'life':{'gi':5,'tmax':'$lT'},'lres':{'gi':3,'tmax':'$rT'},'cres':{'gi':40},'ul':{'gi':35}}
I0=[it('p','생명력 최대치','Max life',['life']),it('s','번개 저항','Lightning res',['lres'])]
I1=I0+[it('s','카오스 저항 (제작 옵션)','Chaos res (crafted)',['cres'])]
I2=I1+[UN('s')]; I3=I1+[it('s','번개 및 카오스 저항 (울라만)','Lightning and chaos res (Ulaman)',['ul'])]
I4=I3+[it('p','랜덤 옵션 2개','Two random lines',None,'j')]
nodes=[base('b2',{'rar':'magic','mods':['life','lres']},K('생명력 + 번개 저항 매직 허리띠 구입','Buy a magic belt with life + lightning res'),I0),
 act('b2','prep',[0,1],'essence','Greater_Essence_of_Ruin',K('레어로 업그레이드 + 접미 카오스 저항','Upgrade to rare + chaos res suffix'),[st('s','카오스 저항 (제작 옵션)','Chaos res (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='cres'),
 mark([0,1.5],'b3',I1),
 act('b3','main',[0,2],'desecrate','Preserved_Collarbone',K('접미 세번째 옵션(훼손)','Third suffix option (desecrated)'),[st('s','울라만 훼손 옵션(미공개)','Ulaman desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'b4'}],I2,omens=['Omen_of_Dextral_Necromancy','Omen_of_the_Sovereign']),
 act('b4','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'ul'},'to':'b5','res':'ok'},{'to':'b4x','res':'fail'}],I3,want='ul',show=['ul'],omens=['Omen_of_Abyssal_Echoes']),
 annul('b4x',[1,3],[{'to':'b3','port':'right'}]),
 act('b5','main',[0,4],'exalt','Greater_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefix options'),[st('p','랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I4,omens=['Omen_of_Greater_Exaltation']),
 done([0,5])]
graph('sane-resist-belt-v2','Belts','Fine Belt',81,
  'TheSaneExile 저항 벨트(영상 방식) — 생명력 + 번개 저항 매직 구입 → 상위 폐허의 에센스(카오스 저항) → 우측 강령술 + 군주의 징조(울라만) + 보존된 빗장뼈 → 공개(번개 및 카오스 저항, 심연의 메아리), 실패 시 빛의 징조 + 소멸의 오브 → 상위 찬미의 징조 + 상위 엑잘로 접두 2자리 랜덤 마무리(사용자 확정 2026-11-10). 밸런스 = 영상(생명력 1티어·번개 저항 1~2티어), 에센셜 = 둘 다 1~3티어 베이스.',
  {'lT':{'kr':'생명력','en':'Life','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})},'rT':{'kr':'번개 저항','en':'Lightning res','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})}},P,
  {'bal':K('생명력 1티어 + 번개 저항 1~2티어 매직 구입 (영상)','Buy T1 life + T1–2 lightning res (as the video)'),'ess':K('생명력·번개 저항 1~3티어 매직 구입','Buy T1–3 life and lightning res')},
  tags,nodes,LIGHT_LOOP(['b3','b4','b4x'],'접미 세번째 옵션(훼손)','Third suffix (desecrated)'),
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'life','tmax':a},{'side':'p','random':True},{'side':'p','random':True},{'tag':'lres','tmax':b},{'tag':'cres','tmax':1},{'tag':'ul','tmax':1}]} for v,kr,en,a,b in (('bal','밸런스 옵션','Balance',1,2),('ess','에센셜 옵션','Essential',3,3))],
  {'quality':20,'sockets':0},{'all':[{'has':'ul'},{'full':'p'},{'full':'s'}]})

# ---------- 3. Diztoh 가성비 양손 둔기 ----------
P={'bal':{'hT':2},'ess':{'hT':4}}
tags={'hyb':{'gi':8,'tmax':'$hT'},'flat':{'gi':39},'kp':{'gi':26},'battle':{'gi':53},'as':{'gi':15},'attr':{'gi':1}}
I0=[]; I1=[it('p','물리 % + 정확도 복합','Hybrid % physical + accuracy',['hyb'])]
I2=I1+[J('s')]; I3=I2+[it('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)',['flat'])]
I4=I3+[UN('p')]
I5=[x for x in I4 if x['m']!='j']+[it('s','모든 공격 스킬 레벨 +3 (제작 옵션)','+3 attack skills (crafted)',['battle'])]
I6=[x for x in I5 if x['kr']!='훼손 옵션(미공개)']+[it('p','물리 피해 % (쿠르갈, 공격 속도 감소)','% physical (Kurgal, reduced attack speed)',['kp'])]
I7=I6+[it('s','랜덤 옵션 2개 (공격 속도·능력치 요구 감소면 최선)','Two random lines (attack speed or attribute requirements is best)',None,'j')]
nodes=[dict(base('d2',{'rar':'normal'},K('특출난 거대한 대망치 (소켓 3) 노멀 구입','Buy a normal exceptional Massive Greathammer (3 sockets)'),I0),
   over=[{'param':{'hT':4},'set':{'start':{'rar':'magic','mods':['hyb']},'next':'d3','label':K('물리 복합 매직 특출난 거대한 대망치 구입','Buy a magic exceptional Massive Greathammer with hybrid physical'),'item':I1}}]),
 act('d2','prep',[0,1],'transmute','Perfect_Orb_of_Transmutation',K('매직으로 업그레이드 + 접두 물리 복합','Upgrade to magic + hybrid physical prefix'),None,K('진화','Transmute'),[{'if':{'added':'hyb'},'to':'d3','res':'ok'},{'to':'d2x','res':'fail'}],I1,show=['hyb']),
 annul('d2x',[1,1],[{'to':'d2','port':'right'}],omens=(),target=K('빗나간 옵션 제거','Remove the missed line')),
 act('d3','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('접미 옵션 1개 추가','Add a suffix'),[st('s','잡옵 (아무 옵션)','Junk (any line)')],K('확장','Augment'),[{'to':'d4'}],I2),
 act('d4','prep',[0,3],'essence','Greater_Essence_of_Abrasion',K('레어로 업그레이드 + 접두 물리 피해 추가','Upgrade to rare + flat physical prefix'),[st('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I3,ess='flat'),
 mark([0,3.5],'d5',I3),
 act('d5','main',[0,4],'desecrate','Preserved_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix option (desecrated)'),[st('p','쿠르갈 훼손 옵션(미공개)','Kurgal desecration (unrevealed)')],K('훼손','Desecrate'),[{'if':{'has':'battle'},'to':'d8'},{'to':'d7'}],I4,omens=['Omen_of_Sinistral_Necromancy','Omen_of_the_Blackblooded']),
 act('d7','main',[0,5],'essence','Perfect_Essence_of_Battle',K('아스트리드의 창의성 장착 후 접미 공격 스킬 +3','Socket Astrid’s Creativity, then +3 attack skills suffix'),[st('s','잡옵 → 모든 공격 스킬 레벨 +3 (제작 옵션)','Junk → +3 attack skills (crafted)')],K('에센스','Essence'),[{'to':'d8'}],I5,ess='battle',omens=['Omen_of_Dextral_Crystallisation']),
 act('d8','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'kp'},'to':'d9','res':'ok'},{'to':'d8x','res':'fail'}],I6,want='kp',show=['kp']),
 annul('d8x',[1,6],[{'to':'d5','port':'right'}]),
 act('d9','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffix options'),[st('s','랜덤 옵션 2개 (공격 속도·능력치 요구 감소면 최선) — 결과 그대로','Two random lines (attack speed or attribute requirements is best) — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I7,omens=['Omen_of_Greater_Exaltation'],over=[{'param':{'hT':4},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,8])]
graph('diztoh-budget-mace-v2','Two_Hand_Maces','Massive Greathammer',82,
  'Diztoh 가성비 양손 둔기(영상 방식) — 특출난 노멀 → 완벽한 진화의 오브(물리 복합, 실패 시 소멸의 오브) → 완벽한 확장의 오브 → 상위 마모의 에센스 → 좌측 강령술 + 검은 피의 징조(쿠르갈) + 보존된 턱뼈 → 아스트리드의 창의성 + 우측 결정화 + 완벽한 전투의 에센스 → 공개(쿠르갈 물리 %) → 상위 찬미 + 완벽한 엑잘(접미 옵션 2개 결과 그대로). 영상은 공개 실패 처리가 없어 빛의 징조 + 소멸의 오브로 다시 훼손하는 걸로 넣음. 철 룬은 취향(정책 23). 밸런스 = 영상(복합 1~2티어), 에센셜 = 복합 1~4티어 매직 베이스 구입(정책 18) + 마지막은 상위 엑잘티드 오브.',
  {'hT':{'kr':'물리 복합','en':'Hybrid physical','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('노멀에서 완벽한 진화의 오브로 물리 복합 1~2티어 (영상)','Transmute hybrid physical T1–2 from normal (as the video)'),'ess':K('물리 복합 1~4티어 매직 구입, 마지막 엑잘은 상위','Buy a T1–4 hybrid magic base, greater exalt to finish')},
  tags,nodes,[{'id':'L0','nodes':['d2','d2x'],'kr':'접두 첫번째 옵션','en':'First prefix'},{'id':'L1','nodes':['d5','d8','d8x'],'kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'hyb','tmax':t},{'tag':'flat','tmax':1},{'tag':'kp','tmax':1},{'tag':'battle','tmax':1},{'side':'s','random':True},{'side':'s','random':True}]} for v,kr,en,t in (('bal','밸런스 옵션','Balance',2),('ess','에센셜 옵션','Essential',4))],
  {'quality':20,'sockets':3},{'all':[{'has':'kp'},{'full':'p'},{'full':'s'}]})

# ---------- 4. LilBotQ 가성비 장화 ----------
P={'bal':{'mT':1,'cT':1,'rT':2},'ess':{'mT':2,'cT':3,'rT':4}}
tags={'ms':{'gi':12,'tmax':'$mT'},'cold':{'gi':2,'tmax':'$cT'},'fireE':{'gi':41},'lres':{'gi':3,'tmax':'$rT'},
      'goodS':{'anyOf':['lres',{'gi':23},{'gi':24},{'gi':33},{'gi':4,'tmax':3}],'label':K('번개 저항 / 카오스 듀얼 저항 / 카오스 저항','Lightning res / chaos dual res / chaos res')}}
I0=[it('p','이동 속도','Movement speed',['ms']),it('s','냉기 저항','Cold res',['cold'])]
I1=I0+[it('s','화염 저항 (제작 옵션)','Fire res (crafted)',['fireE'])]
I2=I1+[UN('s')]; I3=I2+[it('p','랜덤 옵션 2개','Two random lines',None,'j')]
I4=[x for x in I3 if x['kr']!='훼손 옵션(미공개)']+[it('s','번개 저항 / 카오스 듀얼 저항 / 카오스 저항','Lightning / chaos dual / chaos res',['goodS'])]
nodes=[base('b2',{'rar':'magic','mods':['ms','cold']},K('이동 속도 + 냉기 저항 매직 모래맹세 샌들 구입','Buy magic Sandsworn Sandals with movement speed + cold res'),I0),
 act('b2','prep',[0,1],'essence','Greater_Essence_of_Insulation',K('레어로 업그레이드 + 접미 화염 저항','Upgrade to rare + fire res suffix'),[st('s','화염 저항 (제작 옵션)','Fire res (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='fireE'),
 mark([0,1.5],'b3',I1),
 act('b3','main',[0,2],'desecrate','Preserved_Rib',K('접미 세번째 옵션(훼손)','Third suffix option (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'if':{'full':'p'},'to':'b5'},{'to':'b4'}],I2,omens=['Omen_of_Dextral_Necromancy']),
 act('b4','main',[0,3],'exalt','Greater_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefix options'),[st('p','랜덤 옵션 2개 (에너지 보호막 %·생명력이면 좋음) — 결과 그대로','Two random lines (% energy shield or life is good) — keep whatever comes')],K('엑잘','Exalt'),[{'to':'b5'}],I3,omens=['Omen_of_Greater_Exaltation']),
 act('b5','main',[0,4],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'goodS'},'to':'ok','res':'ok'},{'to':'b5x','res':'fail'}],I4,want='goodS',omens=['Omen_of_Abyssal_Echoes'],showIf=[{'param':{'rT':t},'show':[],'showText':[st('s',f'번개 저항 (T1~T{t}) / 카오스 듀얼 저항 3종 / 카오스 저항 (T1~T3)',f'Lightning res (T1–T{t}) / any chaos dual res / chaos res (T1–T3)')]} for t in (2,4)]),
 annul('b5x',[1,4],[{'to':'b3','port':'right'}]),
 done([0,5])]
graph('lilbotq-budget-boots-v2','Boots_int','Sandsworn Sandals',82,
  'LilBotQ 가성비 장화(영상 방식) — 이동 속도 + 냉기 저항 매직 구입 → 상위 절연의 에센스(화염 저항) → 우측 강령술 + 보존된 갈비뼈 → 상위 찬미 + 상위 엑잘(접두 옵션 2개 결과 그대로) → 공개(번개 저항 또는 카오스 듀얼 저항 3종·카오스 저항 1~3티어도 성공 — 사용자 확정 2026-11-10, 심연의 메아리), 실패 시 빛의 징조 + 소멸의 오브로 다시 훼손(접두는 그대로). 밸런스 = 영상(이동 속도·냉기 저항 1티어, 번개 저항 1~2티어), 에센셜 = 이동 속도 1~2티어·냉기 1~3티어·번개 1~4티어.',
  {'mT':{'kr':'이동 속도','en':'Movement speed','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'cT':{'kr':'냉기 저항','en':'Cold res','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})},'rT':{'kr':'번개 저항','en':'Lightning res','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('이동 속도·냉기 저항 1티어 구입, 번개 저항 1~2티어 (영상)','Buy T1 movement speed + cold res, lightning res T1–2 (as the video)'),'ess':K('이동 속도 1~2티어·냉기 저항 1~3티어 구입, 번개 저항 1~4티어','Buy T1–2 movement speed + T1–3 cold res, lightning res T1–4')},
  tags,nodes,LIGHT_LOOP(['b3','b5','b5x'],'접미 세번째 옵션(훼손)','Third suffix (desecrated)'),
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'ms','tmax':a},{'side':'p','random':True},{'side':'p','random':True},{'tag':'cold','tmax':b},{'tag':'fireE','tmax':1},{'side':'s','label':K('번개 저항 / 카오스 듀얼 저항 / 카오스 저항','Lightning / chaos dual / chaos res')}]} for v,kr,en,a,b,c in (('bal','밸런스 옵션','Balance',1,1,2),('ess','에센셜 옵션','Essential',2,3,4))],
  {'quality':20,'sockets':1},{'all':[{'has':'goodS'},{'full':'p'},{'full':'s'}]})

# ---------- 5. Icesly 가성비 완드 ----------
# 2026-11-10 다시 작성(사용자: 가성비엔 비싼 오브 없이, 영상 다시 확인). 영상(자막 + 화면): 번개 +5 매직(접두 마나 잡옵) 구입 → 완벽한 제왕의 오브 →
# 좌측 결정화 + 초월의 합금(접두 마나 삭제) → 엑잘 2번(접두) → 보존된 턱뼈 훼손 → 아스트리드 + 천공의 합금 → 남은 훼손 공개.
# 캡션 3:2x "옵션이 나쁘면 +1 레벨(천공의 합금)로 먹어 버려라", 3:52 "엑잘이 나쁘면 훼손 50/50 없이 먹게 둬라" → 소멸의 오브를 쓰지 않음.
# 사용자 확정: 제왕의 오브는 우측 대관식의 징조로 접미에 → 접두 잡옵 정리 단계 없음. 엑잘은 상위 엑잘티드 오브(가성비).
# 빗나간 접두를 천공의 합금이 지우게 할 땐 좌측 결정화의 징조(번개 +5가 지워지지 않게 — 영상엔 안 보임, 싼 징조).
# 빛의 징조(약 7 div)는 밸런스에서만, 접두 좋은 옵션 2개를 완성할 수 있을 때만(남은 훼손이 빗나간 경우).
P={'bal':{'lT':1,'xT':2,'yT':3},'ess':{'lT':2,'xT':4,'yT':5}}
tags={'l5':{'gi':13,'tmax':'$lT'},'trans':{'gi':60},'cel':{'gi':59},
      'lin':{'gi':7,'tmax':'$yT'},'spell':{'gi':3,'tmax':'$yT'},'xL':{'gi':28,'tmax':'$xT'},'xC':{'gi':27,'tmax':'$xT'},'xF':{'gi':26,'tmax':'$xT'},
      'pre':{'anyOf':['lin','spell','xL','xC','xF'],'label':K('번개 피해·주문 피해·추가 피해 획득','Lightning, spell or extra damage')}}
L5=it('s','모든 번개 주문 스킬 레벨 +5','+5 lightning spell skills',['l5']); TR=it('s','초월의 합금 (제작 옵션)','Transcendent Alloy (crafted)',['trans'])
CEL=it('p','천공의 합금 (제작 옵션)','Celestial Alloy (crafted)',['cel']); PRE=lambda: it('p','번개 피해·주문 피해·추가 피해 획득 중 하나','Lightning, spell or extra damage',['pre'])
RND=lambda: it('p','랜덤 옵션 1개','One random line',None,'j')
I0=[L5,J('p')]; I1=I0+[J('s')]; I2=[L5,J('s'),TR]
I3=I2+[PRE()]; I4=I3+[PRE()]; I5=I4+[UN('p')]; I6=I2+[PRE(),UN('p'),CEL]; I7=I2+[PRE(),CEL,PRE()]
IA=I2+[CEL]; IB=IA+[RND()]; IC=I2+[RND(),CEL]; ID=IC+[UN('p')]
GOOD2={'count':{'tag':'pre','min':2}}
nodes=[base('i2',{'rar':'magic','mods':['l5'],'random':1},K('번개 주문 +5 매직 결투 완드 구입','Buy a magic Dueling Wand with +5 lightning spells'),I0),
 act('i2','prep',[0,1],'regal','Perfect_Regal_Orb',K('레어로 업그레이드 + 접미 옵션 1개','Upgrade to rare + one suffix'),[st('s','랜덤 옵션 1개','One random line')],K('제왕','Regal'),[{'to':'i3'}],I1,omens=['Omen_of_Dextral_Coronation']),
 act('i3','prep',[0,2],'essence','Transcendent_Alloy',K('접두 잡옵을 지우고 접미 초월의 합금','Replace the junk prefix with the Transcendent Alloy suffix'),[st('s','초월의 합금 (제작 옵션)','Transcendent Alloy (crafted)')],K('합금','Alloy'),[{'to':'ms'}],I2,ess='trans',omens=['Omen_of_Sinistral_Crystallisation']),
 mark([0,2.5],'i4',I2),
 act('i4','main',[0,3],'exalt','Greater_Exalted_Orb',K('접두 첫번째 옵션','First prefix option'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'pre','min':1}},'to':'i5','res':'ok'},{'to':'i4a','res':'fail'}],I3,show=['pre'],once=True),
 act('i5','main',[0,4],'exalt','Greater_Exalted_Orb',K('접두 두번째 옵션','Second prefix option'),None,K('엑잘','Exalt'),[{'if':GOOD2,'to':'i6','res':'ok'},{'to':'i5a','res':'fail'}],I4,show=['pre'],once=True),
 act('i6','main',[0,5],'desecrate','Preserved_Jawbone',K('접두 세번째 옵션(훼손, 공개 안 함)','Third prefix (desecrated, left unrevealed)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'i8'}],I5),
 act('i8','main',[0,6],'essence','Celestial_Alloy',K('아스트리드의 창의성 장착 후 천공의 합금','Socket Astrid’s Creativity, then the Celestial Alloy'),[st('p','천공의 합금 (접두 하나가 지워짐 — 미공개 훼손이면 완성)','Celestial Alloy (a prefix makes way — the unrevealed desecration is the hit)')],K('합금','Alloy'),[{'if':{'unrev':False},'to':'ok','res':'ok'},{'to':'i9','res':'fail'}],I6,ess='cel',once=True),
 act('i9','main',[0,7],'reveal',None,K('남은 훼손 옵션 확인','Reveal the remaining desecration'),None,K('공개','Reveal'),
     [{'if':GOOD2,'to':'ok','res':'ok'},{'if':{'all':[{'param':{'lT':1}},{'not':{'added':'pre'}},{'count':{'tag':'pre','min':1}}]},'to':'i9x','res':'fail'},{'to':'ok','res':'fail'}],I7,want='pre',show=['pre'],omens=['Omen_of_Abyssal_Echoes']),
 annul('i9x',[1,7],[{'to':'i9d','port':'right'}]),
 act('i9d','main',[1,7.6],'desecrate','Preserved_Jawbone',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'i9','port':'right'}],I6),
 # a missed exalt: the Celestial Alloy eats it (영상 캡션)
 act('i4a','main',[1,3],'essence','Celestial_Alloy',K('빗나간 접두를 천공의 합금으로 지움','The Celestial Alloy eats the missed prefix'),[st('p','천공의 합금 (접두가 옵션 1개뿐이라 그 옵션이 지워짐)','Celestial Alloy (the only prefix makes way)')],K('합금','Alloy'),[{'to':'i4b'}],IA,ess='cel',omens=['Omen_of_Sinistral_Crystallisation']),
 act('i4b','main',[1,4],'exalt','Greater_Exalted_Orb',K('접두 두번째 옵션','Second prefix option'),[st('p','번개 피해·주문 피해·추가 피해 획득 (안 나와도 그대로)','Lightning, spell or extra damage (keep whatever comes)')],K('엑잘','Exalt'),[{'to':'i6b'}],IB),
 act('i5a','main',[2,4],'essence','Celestial_Alloy',K('빗나간 접두를 천공의 합금으로 지움 (1/2)','The Celestial Alloy eats a prefix (1/2 the missed one)'),[st('p','천공의 합금 (접두 옵션 2개 중 하나가 지워짐)','Celestial Alloy (one of the two prefixes makes way)')],K('합금','Alloy'),[{'to':'i6b'}],IC,ess='cel',omens=['Omen_of_Sinistral_Crystallisation']),
 act('i6b','main',[1,5],'desecrate','Preserved_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'i9'}],ID),
 done([0,8])]
graph('icesly-budget-wand-v2','Wands','Dueling Wand',81,
  'Icesly 가성비 완드(영상 다시 확인 2026-11-10) — 번개 주문 +5 매직 구입 → 완벽한 제왕의 오브 + 우측 대관식의 징조(접미 잡옵) → 좌측 결정화 + 초월의 합금(접두 잡옵 삭제) → 상위 엑잘 2번(접두) → 보존된 턱뼈 훼손 → 아스트리드의 창의성 + 천공의 합금(접두 3개 중 하나 삭제, 미공개 훼손이면 완성) → 좋은 옵션이 지워지면 남은 훼손 공개(심연의 메아리). 엑잘이 빗나가면 소멸의 오브 대신 천공의 합금이 그 옵션을 지우게 함(영상 캡션, 좌측 결정화의 징조). 빛의 징조는 밸런스에서 좋은 접두 옵션 2개를 완성할 수 있을 때만. 밸런스 = 영상 티어, 에센셜 = 번개 +5 1~2티어·접두 목표 넓힘, 빛의 징조 없음.',
  {'lT':{'kr':'번개 주문 레벨','en':'Lightning spell levels','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'xT':{'kr':'추가 피해 획득','en':'Extra damage','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})},'yT':{'kr':'번개·주문 피해','en':'Lightning / spell damage','values':TV({'3':('1~3티어','T1–3'),'5':('1~5티어','T1–5')})}},P,
  {'bal':K('번개 +5 1티어, 접두 목표 영상대로, 남은 훼손이 빗나가면 빛의 징조로 다시','T1 +5 lightning, prefix targets as the video, Light on a missed last desecration'),'ess':K('번개 +5 1~2티어, 접두 목표 넓힘, 결과 그대로','T1–2 +5 lightning, looser prefix targets, keep whatever comes')},
  tags,nodes,[{'id':'L2','nodes':['i9','i9x','i9d'],'kr':'남은 훼손 공개','en':'Remaining desecration'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'l5','tmax':a},{'tag':'trans','tmax':1},{'side':'s','random':True},{'side':'p','label':K('번개 피해·주문 피해·추가 피해 획득','Lightning, spell or extra damage')},{'side':'p','label':K('번개 피해·주문 피해·추가 피해 획득','Lightning, spell or extra damage')},{'tag':'cel','tmax':1}]} for v,kr,en,a in (('bal','밸런스 옵션','Balance',1),('ess','에센셜 옵션','Essential',2))],
  {'quality':20,'sockets':1},{'all':[{'has':'cel'},{'has':'trans'},{'has':'l5'},{'full':'p'}]})
print('wrote 5 graphs')

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_ragna_ashot_bow.py'): _sp.run([_sy.executable, f'{H}/gen_ragna_ashot_bow.py'], check=True)   # 2026-11-13 G13: 새 기준 전용 생성기가 덮어씀

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_icesly_budget_wand.py'): _sp.run([_sy.executable, f'{H}/gen_icesly_budget_wand.py'], check=True)   # 2026-11-13 G12: 새 기준 전용 생성기가 덮어씀
