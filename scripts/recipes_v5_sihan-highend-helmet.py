# ---- 시한 "[POE2 0.5.5] 하이엔드 투구 제작 방법｜범용 적용 가능｜실전 제작 포함" (youtu.be/CTrIbhQVU8U) ----
c='Helmets_str'
SH5=K('시한 영상 기반','Based on 시한')
def textT(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5] and '\n' not in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
ht_life=textT('to maximum Life','n','p'); ht_armF=textT('to Armour','n','p'); ht_armP=textT('% increased Armour','n','p')
ht_ele=textT('of Armour also applies to Elemental Damage','n','s'); ht_crit=textT('increased Critical Hit Chance','n','s')
ht_mark=textT('Abyssal Lord','e','p')
HT_RES=[{'gi':textT(t,'n','s'),'tmax':3} for t in ('to Fire Resistance','to Cold Resistance','to Lightning Resistance')]+[{'gi':textT('to Chaos Resistance','n','s'),'tmax':2}]
HT_SUF=[{'gi':ht_ele,'tmax':1},{'gi':ht_crit,'tmax':2}]
HT_PRE=[{'gi':ht_armF,'tmax':1},{'gi':ht_armP,'tmax':1}]
HT_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'sihan-highend-helmet','cls':c,'base':base(c,'Imperial Greathelm'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('방어도','Armour'),K('생명력','Life'),K('치명타','Critical')],'patch':'0.5.5','created':'2026-11-09','author':SH5,
 'source':{'url':'https://www.youtube.com/watch?v=CTrIbhQVU8U','title':'[POE2 0.5.5] 하이엔드 투구 제작 방법｜범용 적용 가능｜실전 제작 포함','channel':'시한'},
 'title':K('생명력 분열 + 방어도 1티어 2줄 + 치명타·방어도 원소 적용','fractured life + two T1 armour lines + crit, armour applies to elemental'),
 'start':{'rar':'rare','mods':[{'gi':ht_life,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 먼저','en':'Suffixes first'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'13:58','note':K('생명력 최대치 1티어 분열 + 잡옵 1줄.','Fractured T1 maximum life plus one junk line.')},
  {'id':'s1','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':HT_SUF},'fail':{'goto':'self'},'ts':'14:21'},
  {'id':'s2','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation','Omen_of_Greater_Exaltation'],'target':{'anyOf':HT_SUF},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'s1'},'ts':'14:50'},
  {'id':'s3','phase':'suf','do':'chaos','cur':'Greater_Chaos_Orb','target':{'anyOf':HT_RES,'replace':'s'},'fail':{'goto':'self','lost':'s2'},'ts':'15:21'},
  {'id':'s4','phase':'suf','do':'manual','optional':True,'label':K('카오스 저항으로 변환 (선택)','Convert to chaos resistance (optional)'),'ts':'18:21',
   'note':K('화염·냉기·번개 저항을 저항 유동체로 카오스 저항으로.','Turn the fire, cold or lightning resistance into chaos resistance with a resistance liquid.')},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':HT_PRE},'ts':'18:51','br':K('성공 → 훼손, 실패 → 심연의 에센스로 지우기','Hit → desecrate; miss → clear it with Essence of the Abyss')},
  {'id':'p2','phase':'pre','branch':{'of':'p1','when':'ok'},'do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'}},
  {'id':'p3','phase':'pre','branch':{'of':'p1','when':'ok'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':HT_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'p2','via':HT_LIGHT}},
  {'id':'m1','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'mark':{'gi':ht_mark},'chance':1},'ts':'19:00'},
  {'id':'m2','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':HT_PRE},
   'fail':{'goto':'m1','via':{'cur':'Preserved_Rib','also':[HT_LIGHT]}},'ts':'19:09','br':K('실패: 보존된 갈비뼈로 징표 훼손 → 빛의 징조 + 소멸의 오브 → {#m1}번부터','Miss: desecrate the Mark with a Preserved Rib → Light + Annulment → back to step {#m1}')},
  {'id':'m3','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p','fromMark':True},'ts':'20:16'},
  {'id':'m4','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':HT_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'m3','via':HT_LIGHT},'ts':'21:50'},
 ]})
