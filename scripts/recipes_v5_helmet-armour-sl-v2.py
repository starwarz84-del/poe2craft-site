# ---- SL 게임연구소 "#2 종결급 투구 제작 가이드 | 화염파용" (youtu.be/p0fChSu91uI) — grade recipes (policy 25) ----
# Rewrites 'helmet-armour-sl' (REPLACES in build_recipes.py) as high-end / balance / essential from the flowchart
# scripts/graphs/helmet-armour-sl-v2.json (1차 초안 2026-11-10, 사용자 검토 전).
#   high-end  = prefixes T1, resist T1, rarity T1 (Whittling + Dextral Erasure + Perfect Chaos, as the video)
#   balance   = prefixes T1, resist T1–3, rarity T1–2 (Greater Chaos)
#   essential = prefixes T1–2, resist T1–3, the second Greater-Exaltation suffix stays as it comes
c='Helmets_str'; V4SL='https://www.youtube.com/watch?v=p0fChSu91uI'
sl_life=g(c,'to maximum Life',side='p'); sl_armF=g(c,'to Armour',side='p'); sl_armP=g(c,'increased Armour',side='p')
sl_armEle=g(c,'Armour also applies to Elemental'); sl_fire=g(c,'to Fire Resistance'); sl_cold=g(c,'to Cold Resistance'); sl_light=g(c,'to Lightning Resistance')
sl_rarS=g(c,'Rarity of Items found',side='s'); sl_rarE=g(c,'Rarity of Items found','e','s')
def sl_helmet(tier):
    hi, ess = tier=='high', tier=='ess'
    rid='helmet-armour-sl-v2'+('' if hi else '-'+tier)
    pt=2 if ess else 1; rt=1 if hi else 3
    P3=[{'gi':sl_life,'tmax':pt},{'gi':sl_armF,'tmax':pt},{'gi':sl_armP,'tmax':pt}]
    RES=[{'gi':sl_fire,'tmax':rt},{'gi':sl_cold,'tmax':rt},{'gi':sl_light,'tmax':rt}]
    nodes=[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'1:04','note':K('특출난 제국의 대헬름(소켓 2개), 아이템 레벨 82.','An exceptional Imperial Greathelm (two sockets), item level 82.')},
  {'id':'h2','phase':'base','do':'manual','cost':'quality','optional':True,'target':{'setQuality':26},'label':K('퀄리티 25% 이상 (선택)','Quality 25%+ (optional)'),'ts':'3:03'},
  {'id':'m1','phase':'magic','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':[{'gi':sl_armP,'tmax':1},{'gi':sl_armEle,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},'ts':'4:00'},
  {'id':'m2','phase':'magic','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':[{'gi':sl_armP,'tmax':1},{'gi':sl_armEle,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'m1'},'ts':'4:08'},
  {'id':'r1','phase':'rare','do':'essence','cur':'Greater_Essence_of_Opulence','target':{'gi':sl_rarE,'ti':0},'ts':'4:31'},
  {'id':'r2','phase':'rare','do':'divine','cur':'Divine_Orb','optional':True,'ts':'4:40'},
  {'id':'f1','phase':'fracture','do':'desecrate','cur':'Preserved_Rib','target':{'unrev':'p'},'ts':'5:47'},
  {'id':'f2','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':sl_armEle},{'gi':sl_armP},{'gi':sl_rarE}]},'ts':'5:56'},
  {'id':'f4','phase':'fracture','do':'remove','cur':'Orb_of_Annulment','expect':4,'after':{'keepOnly':[sl_armEle,'junk1']},'ts':'6:57'},
  {'id':'b1','phase':'prefix','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':P3},'fail':{'goto':'self'},'ts':'7:05'},
  {'id':'b2','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':P3},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'b1'},'ts':'7:51'},
  {'id':'b3','phase':'prefix','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'8:44'},
  {'id':'b4','phase':'prefix','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':P3},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'b3','via':LIGHT},'ts':'8:54'},
  {'id':'s1','phase':'suffix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':RES},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}},'ts':'9:12'},
    ]
    if not ess:
        nodes.append({'id':'s2','phase':'suffix','do':'chaos','cur':'Perfect_Chaos_Orb' if hi else 'Greater_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],
                      'target':{'anyOf':[{'gi':sl_rarS,'tmax':1 if hi else 2}],'replace':'s'},'fail':{'goto':'self'},'ts':'10:15'})
    nodes.append({'id':'fz','phase':'suffix','do':'note','ts':'10:30','note':K('완성. 룬 소켓 2개는 비워 둠(취향껏).','Done. Both rune sockets are left empty (your choice).')})
    R.append({
 'id':rid,'tierGroup':'helmet-armour-sl-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Imperial Greathelm'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('방어도','Armour'),K('생명력','Life'),K('원소 저항','Elemental res')],'patch':'0.5.5','created':'2026-11-08',
 'author':K('SL 게임연구소 영상 기반','Based on SL 게임연구소'),
 'source':{'url':V4SL,'title':'[POE2 0.5.5] #2 종결급 투구 제작 가이드 | 화염파용','channel':'SL 게임연구소!'},
 'title':K('방어도·생명력 + 원소 저항 (화염파용)','armour/life + elemental resistance (Fireball)'),
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'magic','kr':'매직 만들기','en':'Make it magic'},{'id':'rare','kr':'레어 전환','en':'To rare'},
           {'id':'fracture','kr':'분열','en':'Fracture'},{'id':'prefix','kr':'접두 첫 번째~세 번째 옵션','en':'Prefix options 1–3'},{'id':'suffix','kr':'접미 두 번째·세 번째 옵션','en':'Suffix options 2–3'}],
 'nodes':nodes})
for _t in ('high','bal','ess'): sl_helmet(_t)
