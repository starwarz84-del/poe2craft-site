# ---- Unstoppable BTW "How to Craft the Best Body Armours and Sell Them for Big Profit in Path of Exile 2" (youtu.be/swF5mwXmZ0k, 2026-10, 0.5.5 리그) ----
# 글 정리본 guides-factory.com/guides/poe2-body-armour-crafting-guide (영상 기반). 플로우차트 scripts/graphs/gen_batch27.py와 같은 단계 id(정책 31).
# 기록 tools/notes/web-unstoppable-chests.md. 원본 = 하이엔드(모두 1티어), 등급 레시피 recipes_v5_zz-batchz27-v2.py.
UNS=K('Unstoppable BTW 영상 기반','Based on Unstoppable BTW')
UNSRC={'url':'https://www.youtube.com/watch?v=swF5mwXmZ0k','title':'How to Craft the Best Body Armours and Sell Them for Big Profit in Path of Exile 2','channel':'Unstoppable BTW'}
LIGHTU={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
WH=['Omen_of_Whittling','Omen_of_Dextral_Erasure']
def _uns(id, c, bname, title, tags, start, nodes):
    R.append({'id':id,'cls':c,'base':base(c,bname),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high','buildTags':tags,
              'patch':'0.5.5','created':'2026-11-11','author':UNS,'source':UNSRC,'title':title,'start':start,
              'phases':[{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'}],'nodes':nodes})

# 1. Vile Robe — 에너지 보호막
_GP=[{'gi':6,'tmax':1},{'gi':9,'tmax':1},{'gi':14,'tmax':1}]
_R3=[{'gi':1,'tmax':1},{'gi':2,'tmax':1},{'gi':3,'tmax':1}]
_uns('unstoppable-vile-robe','Body_Armours_int','Vile Robe',K('에너지 보호막 증가 분열 + 에너지 보호막·정신력 접두 + 원소 저항 3개','fractured % energy shield + energy shield / spirit prefixes + three elemental resistances'),
  [K('에너지 보호막','Energy shield'),K('저항','Resistances'),K('판매용','For sale')],
  {'rar':'rare','mods':[{'gi':7,'tmax':1,'fr':True},{'junk':'s'}]},[
  {'id':'v0','phase':'pre','do':'base','cost':'base','note':K('에너지 보호막 증가 1티어 분열 + 잡옵 1개, 아이템 레벨 82 룬 소켓 3개.','Fractured T1 % energy shield + one junk line, item level 82, three rune sockets.')},
  {'id':'c1','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':_GP},'fail':{'goto':'self'}},
  {'id':'d1','phase':'pre','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'d2','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':_GP},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'d1','via':LIGHTU}},
  {'id':'e1','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'junk':['s','s']}},
  {'id':'e2','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'}},
  {'id':'t1','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':WH,'target':{'anyOf':_R3,'replace':'s'},'fail':{'goto':'self'},
   'br':K('원소 저항 1티어 3개가 될 때까지','Until three T1 elemental resistances')},
  {'id':'t2','phase':'suf','do':'note','note':K('완성.','Done.')}])

# 2. Slipstrike Vest — 회피
_GE=[{'gi':6,'tmax':1},{'gi':9,'tmax':1}]
_RD=[{'gi':1,'tmax':1},{'gi':2,'tmax':1},{'gi':3,'tmax':1},{'gi':18,'tmax':1}]
_uns('unstoppable-slipstrike-vest','Body_Armours_dex','Slipstrike Vest',K('회피 증가 분열 + 회피 접두 2개 + 저항 2개·굴절','fractured % evasion + two evasion prefixes + two resistances and deflection'),
  [K('회피','Evasion'),K('저항','Resistances'),K('판매용','For sale')],
  {'rar':'rare','mods':[{'gi':7,'tmax':1,'fr':True},{'junk':'s'}]},[
  {'id':'v0','phase':'suf','do':'base','cost':'base','note':K('회피 증가 1티어 분열 + 잡옵 1개, 아이템 레벨 82 룬 소켓 3개.','Fractured T1 % evasion + one junk line, item level 82, three rune sockets.')},
  {'id':'e1','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'junk':['s','s']}},
  {'id':'t1','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':WH,'target':{'anyOf':_RD,'replace':'s'},'fail':{'goto':'self'},
   'br':K('저항 2개 + 굴절이 될 때까지','Until two resistances and deflection')},
  {'id':'d1','phase':'pre','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'d2','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':5},{'gi':12}]},'side':'p','bone':'Ancient_Rib','asIs':True},
   'br':K('생명력·가시 같은 흔한 옵션으로 접두 한 자리를 막아 둠','A common line such as life or thorns blocks one prefix')},
  {'id':'e3','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':_GE},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}}},
  {'id':'w1','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True}},
  {'id':'d3','phase':'pre','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'d4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':_GE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'d3','via':LIGHTU}},
  {'id':'d5','phase':'pre','do':'note','note':K('완성.','Done.')}])
