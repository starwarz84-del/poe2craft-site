# ---- 시한 "[POE2 0.5.5] 하이엔드 장화 제작 방법" (youtu.be/dlrD21AcCUE) — grade recipes (policy 25) ----
# Rewrites 'sihan-highend-boots' (REPLACES in build_recipes.py) as high-end / balance / essential from the flowchart
# scripts/graphs/sihan-highend-boots-v2.json (1차 초안 2026-11-10, 사용자 검토 전).
#   high-end  = resist T1, desecrated prefix T1
#   balance   = resist T1–2, desecrated prefix T1–2
#   essential = third suffix as it comes, desecrated prefix T1–3
# 2차 (2026-11-10 user feedback): rare by Perfect Regal (policy 26), suffixes as the video (armour-to-elemental by Chaos, then strength, then resist by Dextral exalt + Annulment),
# a missed prefix exalt becomes the Abyssal Lord's Mark (Sinistral Crystallisation + Essence of the Abyss) → desecrate the Mark → reveal.
# The fracture prep is not in the video (it starts from a fractured base).
c='Boots_str'; VSB='https://www.youtube.com/watch?v=dlrD21AcCUE'
sb_armP=g(c,'% increased Armour',side='p'); sb_ele=g(c,'Armour also applies to Elemental'); sb_str=g(c,'to Strength',side='s')
sb_life=g(c,'to maximum Life',side='p'); sb_ms=g(c,'increased Movement Speed',side='p'); sb_lifeE=g(c,'to maximum Life','e','p')
sb_mark=g(c,'Abyssal Lord','e','p'); sb_fire=g(c,'to Fire Resistance'); sb_cold=g(c,'to Cold Resistance'); sb_light=g(c,'to Lightning Resistance')
def sh_boots(tier):
    hi, ess = tier=='high', tier=='ess'
    rid='sihan-highend-boots-v2'+('' if hi else '-'+tier)
    rt=1 if hi else 2; dt={'high':1,'bal':2,'ess':3}[tier]
    PRE=[{'gi':sb_ms,'tmax':1},{'gi':sb_life,'tmax':1}]
    PRED=[{'gi':sb_ms,'tmax':dt},{'gi':sb_life,'tmax':dt}]
    RES=[{'gi':sb_fire,'tmax':rt},{'gi':sb_cold,'tmax':rt},{'gi':sb_light,'tmax':rt}]
    X=[{'gi':sb_str,'tmax':1},{'gi':sb_ele,'tmax':1}]
    GOOD=PRE+X+[{'gi':sb_fire,'tmax':1},{'gi':sb_cold,'tmax':1},{'gi':sb_light,'tmax':1}]
    DEX={'cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation']}
    nodes=[
  {'id':'h1','phase':'base','do':'base','cost':'base','note':K('특출난 타살리오의 각반(소켓 2개), 아이템 레벨 82.','Exceptional Tasalian Greaves (two sockets), item level 82.')},
  {'id':'h2','phase':'base','do':'manual','cost':'quality','optional':True,'target':{'setQuality':26},'label':K('퀄리티 25% 이상 (선택)','Quality 25%+ (optional)')},
  {'id':'m1','phase':'magic','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':[{'gi':sb_armP,'tmax':1},{'gi':sb_ele,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}}},
  {'id':'m2','phase':'magic','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':[{'gi':sb_armP,'tmax':1},{'gi':sb_ele,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'m1'}},
  {'id':'r1','phase':'rare','do':'regal','cur':'Perfect_Regal_Orb','target':{'anyOf':GOOD},'fail':{'goto':'h1'},'br':K('잡옵이 붙어도 분열 진행 — 잡옵이 분열되면 새 베이스','Junk is fine too — fracture anyway; a fractured junk line means a new base')},
  {'id':'r2','phase':'rare','do':'divine','cur':'Divine_Orb','optional':True},
  {'id':'f1','phase':'fracture','do':'desecrate','cur':'Preserved_Rib','target':{'unrev':'s'}},
  {'id':'f2','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':sb_armP},{'gi':sb_ele}]+GOOD}},
  {'id':'f4','phase':'fracture','do':'remove','cur':'Orb_of_Annulment','expect':2,'after':{'keepOnly':[sb_armP,'junk1']}},
  {'id':'s1','phase':'suffix','do':'chaos','cur':'Chaos_Orb','target':{'gi':sb_ele,'tmax':1},'fail':{'goto':'self'},'ts':'9:59'},
  {'id':'s2','phase':'suffix','do':'exalt',**DEX,'target':{'gi':sb_str,'tmax':1},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'s1'},'ts':'11:57'},
    ]
    if ess:
        nodes.append({'id':'s3','phase':'suffix','do':'exalt',**DEX,'target':{'junk':'s'},'label':K('접미 세번째 옵션 (나오는 대로)','Third suffix (whatever comes)'),'ts':'10:17'})
    else:
        nodes.append({'id':'s3','phase':'suffix','do':'exalt',**DEX,'target':{'anyOf':RES},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'s2'},'ts':'10:17'})
    nodes+=[
  {'id':'p1','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':PRE},'br':K('성공 → 훼손 / 실패 → 심연의 에센스로 징표','Hit → desecrate; miss → the Abyssal Mark')},
  {'id':'p2','phase':'prefix','branch':{'of':'p1','when':'ok'},'do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'}},
  {'id':'p3','phase':'prefix','branch':{'of':'p1','when':'ok'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':PRED},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'p2','via':LIGHT}},
  {'id':'q1','phase':'prefix','branch':{'of':'p1','when':'miss'},'do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'mark':{'gi':sb_mark},'chance':1}},
  {'id':'q2','phase':'prefix','branch':{'of':'p1','when':'miss'},'do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p','fromMark':True}},
  {'id':'q3','phase':'prefix','branch':{'of':'p1','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':PRED},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'p1','via':LIGHT},
   'br':K('실패: 빛의 징조 + 소멸의 오브 → {#p1}번부터','Miss: Light + Annulment → back to step {#p1}')},
  {'id':'q4','phase':'prefix','branch':{'of':'p1','when':'miss'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':PRE},'fail':{'goto':'q1','via':LIGHT},
   'br':K('실패: 빛의 징조 + 소멸의 오브로 훼손 줄 제거 → {#q1}번부터','Miss: remove the desecrated line with Light + Annulment → back to step {#q1}')},
  {'id':'fz','phase':'prefix','do':'note','note':K('완성. 룬 소켓 2개는 비워 둠(취향껏).','Done. Both rune sockets are left empty (your choice).')}]
    R.append({
 'id':rid,'tierGroup':'sihan-highend-boots-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Tasalian Greaves'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('방어도','Armour'),K('이동 속도','Movement speed'),K('생명력','Life')],'patch':'0.5.5','created':'2026-11-09','author':K('시한 영상 기반','Based on 시한'),
 'source':{'url':VSB,'title':'[POE2 0.5.5] 하이엔드 장화 제작 방법｜범용 적용 가능｜실전 제작 포함','channel':'시한'},
 'title':K('방어도 % 분열 + 이동 속도·생명력 + 방어도 원소 적용','fractured % armour + movement speed, life, armour applies to elemental'),
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'magic','kr':'매직 만들기','en':'Make it magic'},{'id':'rare','kr':'레어 전환','en':'To rare'},
           {'id':'fracture','kr':'분열','en':'Fracture'},{'id':'suffix','kr':'접미 첫번째~세번째 옵션','en':'Suffix options 1–3'},{'id':'prefix','kr':'접두 두번째·세번째 옵션','en':'Prefix options 2–3'}],
 'nodes':nodes})
for _t in ('high','bal','ess'): sh_boots(_t)
