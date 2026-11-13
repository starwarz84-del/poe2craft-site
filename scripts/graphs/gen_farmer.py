# Writes the flowcharts of the two XTheFarmerX league-start recipes (policy 24/25 grades):
#   farmer-budget-armour-v2.json  (Flowing Raiment, three energy shield prefixes)
#   farmer-starter-staff-v2.json  (+5 lightning spells staff, extra damage gains)
# Base work uses Perfect Transmutation / Augmentation (사용자 확정 2026-11-10). Staff base = +6 roll (a +5 needs a Divine Orb later). Video steps kept; grades differ only in the tiers aimed for (and the bone that can roll them).
import json, os
H=os.path.dirname(os.path.abspath(__file__))
K=lambda kr,en: {'kr':kr,'en':en}
GRP=[{'id':'prep','kr':'베이스템 완성','en':'Finished base','cols':[0,1]},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers','cols':[0,1]}]
VER=[('ess','에센셜','Essential'),('bal','밸런스','Balance'),('high','하이엔드','High-end')]
def it(s,kr,en,tags=None,m='n'):
    d={'s':s,'kr':kr,'en':en,'m':m}
    if tags: d['tags']=tags
    return d
def annul(id,pos,back):
    return {'id':id,'kind':'act','group':'main','pos':pos,'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],
            'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
            'target':K('훼손 옵션 제거','Remove the desecrated modifier'),'edges':[{'to':back,'port':'right'}]}
def graph(id, cls, base, ilvl, note, params, P, desc, tags, nodes, loopNodes, loopName, finals, finalItem):
    return {'id':id,'recipe':id,'cls':cls,'base':base,'ilvl':ilvl,'note':note,'params':params,
            'strategies':[{'id':v,'params':P[v]} for v in ('high','bal','ess')],
            'versions':[{'id':v,'kr':kr,'en':en,'params':P[v],'desc':desc[v]} for v,kr,en in VER],
            'tags':tags,'require':{'all':[{'full':'p'},{'full':'s'}]},'groups':GRP,'start':'h1',
            'loops':[{'id':'L1','nodes':loopNodes,**loopName}],'finals':finals,'finalItem':finalItem,'nodes':nodes}

# ---------- armour ----------
P={'high':{'esT':1,'rvT':1,'bone':'a'},'bal':{'esT':2,'rvT':2,'bone':'a'},'ess':{'esT':3,'rvT':9,'bone':'p'}}
tags={'flat':{'gi':6,'tmax':'$esT'},'ess':{'gi':31},'hyb':{'gi':9,'tmax':'$rvT'},'eslife':{'gi':8,'tmax':'$rvT'},'spirit':{'gi':14,'tmax':'$rvT'},
      'want':{'anyOf':['hyb','eslife','spirit']}}
I0=[it('p','에너지 보호막 최대치','Max energy shield',['flat'])]
I1=I0+[it('s','잡옵','Junk',None,'j')]
I2=I1+[it('p','방어 % (제작 옵션)','Defences % (crafted)',['ess'])]
I3=I2+[it('p','훼손 옵션(미공개)','Desecrated (unrevealed)')]
I4=I2+[it('p','에너지 보호막 혼합 · 생명력 · 정신력 중 하나','Hybrid ES, ES + life or Spirit',['want'])]
I5=I4+[it('s','랜덤 옵션 2개','Two random lines',None,'j')]
nodes=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'a2','start':{'rar':'magic','mods':['flat']},
  'label':K('에너지 보호막 최대치 매직 흐르는 의복 구입','Buy a magic Flowing Raiment with max energy shield'),'item':I0},
 {'id':'a2','kind':'act','group':'prep','pos':[0,1],'act':'augment','cur':'Perfect_Orb_of_Augmentation','goal':K('접미 옵션 1개 추가','Add a suffix'),
  'showText':[K('잡옵 (아무 옵션)','Junk (any line)')|{'s':'s'}],'label':K('확장','Augment'),'edges':[{'to':'a3'}],'item':I1},
 {'id':'a3','kind':'act','group':'prep','pos':[0,2],'act':'essence','ess':'ess','cur':'Greater_Essence_of_Enhancement','goal':K('레어로 업그레이드 + 접두 방어 %','Upgrade to rare + defences % prefix'),
  'showText':[K('방어 % (제작 옵션)','Defences % (crafted)')|{'s':'p'}],'label':K('에센스','Essence'),'edges':[{'to':'ms'}],'item':I2},
 {'id':'ms','kind':'mark','group':'main','pos':[0,2.5],'next':'a4','label':K('아이템 제작 시작','Item crafting starts'),'item':I2},
 {'id':'a4','kind':'act','group':'main','pos':[0,3],'act':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],
  'over':[{'param':{'bone':'p'},'set':{'cur':'Preserved_Rib'}}],
  'goal':K('접두 세 번째 옵션(훼손)','Third prefix option (desecrated)'),'showText':[K('훼손 옵션(미공개)','Desecrated modifier (unrevealed)')|{'s':'p'}],
  'label':K('훼손','Desecrate'),'edges':[{'to':'a5'}],'item':I3},
 {'id':'a5','kind':'act','group':'main','pos':[0,4],'act':'reveal','want':'want','goal':K('훼손 옵션 확인','Reveal the desecrated modifier'),'show':['want'],
  'label':K('공개','Reveal'),'edges':[{'if':{'added':'want'},'to':'a6','res':'ok'},{'to':'a5x','res':'fail'}],'item':I4},
 annul('a5x',[1,4],'a4'),
 {'id':'a6','kind':'act','group':'main','pos':[0,5],'act':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],
  'goal':K('접미 두 번째·세 번째 옵션','Second and third suffix options'),'showText':[K('랜덤 옵션 2개 (저항이 뜨면 대박) — 결과 그대로','Two random lines (resistances are the jackpot) — keep whatever comes')|{'s':'s'}],
  'label':K('엑잘','Exalt'),'edges':[{'to':'ok'}],'item':I5},
 {'id':'ok','kind':'done','group':'main','pos':[0,6],'label':K('완성','Finished')}]
fin=lambda v,kr,en,e,r: {'id':v,'kr':kr,'en':en,'lines':[{'tag':'flat','tmax':e},{'tag':'ess','tmax':1},{'tag':'hyb','tmax':r},{'side':'s','random':True},{'side':'s','random':True},{'side':'s','random':True}]}
g=graph('farmer-budget-armour-v2','Body_Armours_int','Flowing Raiment',79,
  'XTheFarmerX 리그 초반 에너지 보호막 갑옷(영상 방식) — 에너지 보호막 최대치 매직 구입 → 상위 확장의 오브(접미 잡옵) → 상위 강화의 에센스(접두 방어 %) → 좌측 강령술 + 갈비뼈 → 공개(혼합·생명력·정신력) → 상위 찬미 + 상위 엑잘(접미 옵션 2개 결과 그대로). 상위 철 룬은 취향(정책 23)이라 뺌. 에센셜 = 영상(보존된 갈비뼈, 아무 티어), 밸런스·하이엔드는 고대 갈비뼈(레벨 40+ 티어만)로 1~2티어 / 1티어.',
  {'esT':{'kr':'에너지 보호막 최대치','en':'Max energy shield','values':{'1':K('1티어','T1'),'2':K('1~2티어','T1–2'),'3':K('1~3티어','T1–3')}},
   'rvT':{'kr':'훼손 공개 목표','en':'Reveal target','values':{'1':K('1티어','T1'),'2':K('1~2티어','T1–2'),'9':K('아무 티어','Any tier')}},
   'bone':{'kr':'갈비뼈','en':'Rib','values':{'a':K('고대 갈비뼈','Ancient Rib'),'p':K('보존된 갈비뼈','Preserved Rib')}}},
  P,{'ess':K('에너지 보호막 최대치 1~3티어, 훼손 아무 티어 (영상)','Max ES T1–3, any desecrated tier (as the video)'),
     'bal':K('에너지 보호막 최대치 1~2티어, 훼손 1~2티어 (고대 갈비뼈)','Max ES T1–2, desecrated T1–2 (Ancient Rib)'),
     'high':K('에너지 보호막 최대치 1티어, 훼손 1티어 (고대 갈비뼈)','Max ES T1, desecrated T1 (Ancient Rib)')},
  tags,nodes,['a4','a5','a5x'],K('접두 세 번째 옵션(훼손)','Third prefix (desecrated)'),
  [fin('high','하이엔드 옵션','High-end',1,1),fin('bal','밸런스 옵션','Balance',2,2),fin('ess','에센셜 옵션','Essential',3,6)],{'quality':20,'sockets':2})
json.dump(g,open(f'{H}/farmer-budget-armour-v2.json','w'),ensure_ascii=False,indent=1)

# ---------- staff ----------
P={'high':{'fT':1,'rvT':1,'bone':'a'},'bal':{'fT':2,'rvT':2,'bone':'a'},'ess':{'fT':2,'rvT':9,'bone':'p'}}
tags={'l5':{'gi':17,'tmax':1},'fire':{'gi':32,'tmax':'$fT'},'ess':{'gi':49},'cold':{'gi':33,'tmax':'$rvT'},'lit':{'gi':34,'tmax':'$rvT'},'chaos':{'gi':35},
      'want':{'anyOf':['cold','lit','chaos']}}
I0=[it('p','추가 화염 피해 획득','Extra fire damage',['fire']),it('s','모든 번개 주문 스킬 레벨 +6','+6 to all lightning spell skills',['l5'])]
I2=I0+[it('p','주문 피해 % (제작 옵션)','Spell damage % (crafted)',['ess'])]
I3=I2+[it('p','훼손 옵션(미공개)','Desecrated (unrevealed)')]
I4=I2+[it('p','추가 냉기·번개·카오스 피해 획득 중 하나','Extra cold, lightning or chaos damage',['want'])]
I5=I4+[it('s','랜덤 옵션 2개','Two random lines',None,'j')]
nodes=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'w2','start':{'rar':'magic','mods':['fire','l5']},
  'label':K('번개 주문 +6 + 추가 화염 피해 매직 지팡이 구입','Buy a magic staff with +6 lightning spells + extra fire'),'item':I0},
 {'id':'w2','kind':'act','group':'prep','pos':[0,1],'act':'essence','ess':'ess','cur':'Greater_Essence_of_Sorcery','goal':K('레어로 업그레이드 + 접두 주문 피해','Upgrade to rare + spell damage prefix'),
  'showText':[K('주문 피해 % (제작 옵션)','Spell damage % (crafted)')|{'s':'p'}],'label':K('에센스','Essence'),'edges':[{'to':'ms'}],'item':I2},
 {'id':'ms','kind':'mark','group':'main','pos':[0,1.5],'next':'w3','label':K('아이템 제작 시작','Item crafting starts'),'item':I2},
 {'id':'w3','kind':'act','group':'main','pos':[0,2],'act':'desecrate','cur':'Ancient_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],
  'over':[{'param':{'bone':'p'},'set':{'cur':'Preserved_Jawbone'}}],
  'goal':K('접두 세 번째 옵션(훼손)','Third prefix option (desecrated)'),'showText':[K('훼손 옵션(미공개)','Desecrated modifier (unrevealed)')|{'s':'p'}],
  'label':K('훼손','Desecrate'),'edges':[{'to':'w4'}],'item':I3},
 {'id':'w4','kind':'act','group':'main','pos':[0,3],'act':'reveal','omens':['Omen_of_Abyssal_Echoes'],'want':'want','goal':K('훼손 옵션 확인','Reveal the desecrated modifier'),'show':['want'],
  'label':K('공개','Reveal'),'edges':[{'if':{'added':'want'},'to':'w5','res':'ok'},{'to':'w4x','res':'fail'}],'item':I4},
 annul('w4x',[1,3],'w3'),
 {'id':'w5','kind':'act','group':'main','pos':[0,4],'act':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],
  'goal':K('접미 두 번째·세 번째 옵션','Second and third suffix options'),'showText':[K('랜덤 옵션 2개 (시전 속도·치명타가 뜨면 대박) — 결과 그대로','Two random lines (cast speed or crit is the jackpot) — keep whatever comes')|{'s':'s'}],
  'label':K('엑잘','Exalt'),'edges':[{'to':'ok'}],'item':I5},
 {'id':'ok','kind':'done','group':'main','pos':[0,5],'label':K('완성','Finished')}]
fin=lambda v,kr,en,f,r: {'id':v,'kr':kr,'en':en,'lines':[{'tag':'fire','tmax':f},{'tag':'ess','tmax':1},{'tag':'lit','tmax':r},{'tag':'l5','tmax':1},{'side':'s','random':True},{'side':'s','random':True}]}
g=graph('farmer-starter-staff-v2','Staves','Sanctified Staff',80,
  'XTheFarmerX 리그 초반 번개 지팡이(영상 방식) — 번개 주문 +5 + 추가 화염 피해 매직 구입 → 상위 마법의 에센스(접두 주문 피해) → 좌측 강령술 + 턱뼈 → 공개(추가 냉기·번개·카오스) → 상위 찬미 + 엑잘(접미 옵션 2개 결과 그대로). 영상 베이스는 아이템 레벨 73(추가 피해 1티어는 레벨 80) — 그래프는 80으로 두고 에센셜·밸런스는 2티어까지로 맞춤. 에센셜 = 영상(보존된 턱뼈, 아무 티어), 밸런스·하이엔드는 고대 턱뼈(레벨 40+)로 1~2티어 / 1티어.',
  {'fT':{'kr':'추가 화염 피해','en':'Extra fire damage','values':{'1':K('1티어','T1'),'2':K('1~2티어','T1–2')}},
   'rvT':{'kr':'훼손 공개 목표','en':'Reveal target','values':{'1':K('1티어','T1'),'2':K('1~2티어','T1–2'),'9':K('아무 티어','Any tier')}},
   'bone':{'kr':'턱뼈','en':'Jawbone','values':{'a':K('고대 턱뼈','Ancient Jawbone'),'p':K('보존된 턱뼈','Preserved Jawbone')}}},
  P,{'ess':K('추가 화염 피해 1~2티어, 훼손 아무 티어 (영상)','Extra fire T1–2, any desecrated tier (as the video)'),
     'bal':K('추가 화염 피해 1~2티어, 훼손 1~2티어 (고대 턱뼈)','Extra fire T1–2, desecrated T1–2 (Ancient Jawbone)'),
     'high':K('추가 화염 피해 1티어, 훼손 1티어 (고대 턱뼈, 아이템 레벨 80+)','Extra fire T1, desecrated T1 (Ancient Jawbone, item level 80+)')},
  tags,nodes,['w3','w4','w4x'],K('접두 세 번째 옵션(훼손)','Third prefix (desecrated)'),
  [fin('high','하이엔드 옵션','High-end',1,1),fin('bal','밸런스 옵션','Balance',2,2),fin('ess','에센셜 옵션','Essential',2,5)],{'quality':20,'sockets':0})
g['basePrice']={'Chaos_Orb':1}   # 사용자 2026-11-10 거래소: +6 매직 지팡이 카오스 오브 1개
json.dump(g,open(f'{H}/farmer-starter-staff-v2.json','w'),ensure_ascii=False,indent=1)
print('wrote 2 graphs')

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_farmer_budget_armour.py'): _sp.run([_sy.executable, f'{H}/gen_farmer_budget_armour.py'], check=True)   # 2026-11-13 G14: 새 기준 전용 생성기가 갑옷을 덮어씀

import subprocess as _sp, sys as _sy
if os.path.exists(f'{H}/gen_farmer_starter_staff.py'): _sp.run([_sy.executable, f'{H}/gen_farmer_starter_staff.py'], check=True)   # 2026-11-13 G13: 새 기준 전용 생성기가 덮어씀
