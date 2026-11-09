# ---- 시한 "[POE2 0.5.5] 하이엔드 장화 제작 방법｜범용 적용 가능｜실전 제작 포함" (youtu.be/dlrD21AcCUE) ----
c='Boots_str'
SH5=K('시한 영상 기반','Based on 시한')
def textH(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5] and '\n' not in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sh_arm=textH('% increased Armour','n','p'); sh_life=textH('to maximum Life','n','p'); sh_ms=textH('increased Movement Speed','n','p')
sh_ele=textH('of Armour also applies to Elemental Damage','n','s'); sh_str=textH('to Strength','n','s')
sh_mark=textH('Abyssal Lord','e','p')
SH_RES=[{'gi':textH(t,'n','s'),'tmax':2} for t in ('to Fire Resistance','to Cold Resistance','to Lightning Resistance','to Chaos Resistance')]
SH_PRE=[{'gi':sh_ms,'tmax':2},{'gi':sh_life,'tmax':2}]
SH_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'sihan-highend-boots','cls':c,'base':base(c,'Tasalian Greaves'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('방어도','Armour'),K('이동 속도','Movement speed'),K('생명력','Life')],'patch':'0.5.5','created':'2026-11-09','author':SH5,
 'source':{'url':'https://www.youtube.com/watch?v=dlrD21AcCUE','title':'[POE2 0.5.5] 하이엔드 장화 제작 방법｜범용 적용 가능｜실전 제작 포함','channel':'시한'},
 'title':K('방어도 % 분열 + 이동 속도·생명력 + 방어도 원소 적용','fractured % armour + movement speed, life, armour applies to elemental'),
 'start':{'rar':'rare','mods':[{'gi':sh_arm,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 먼저','en':'Suffixes first'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'9:40','note':K('방어도 % 증가 1티어 분열 + 잡옵 1줄.','Fractured T1 % increased armour plus one junk line.')},
  {'id':'s1','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':sh_ele,'tmax':1},'fail':{'goto':'self'},'ts':'9:59'},
  {'id':'s2','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'gi':sh_str,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'s1'},'ts':'11:57'},
  {'id':'s3','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':SH_RES},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'s2'},'ts':'10:17'},
  {'id':'s4','phase':'suf','do':'manual','optional':True,'label':K('공허 유동체로 카오스 저항 (선택)','Void liquid to chaos resistance (optional)'),'ts':'10:35',
   'note':K('화염·냉기·번개 저항이 뜨면 공허 유동체로 카오스 저항으로 바꿈.','A fire, cold or lightning resistance becomes chaos resistance with Void Flux.')},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':SH_PRE},'ts':'13:18','br':K('성공 → 훼손, 실패 → 심연의 에센스로 지우기','Hit → desecrate; miss → clear it with Essence of the Abyss')},
  {'id':'p2','phase':'pre','branch':{'of':'p1','when':'ok'},'do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'}},
  {'id':'p3','phase':'pre','branch':{'of':'p1','when':'ok'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SH_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'p2','via':SH_LIGHT}},
  {'id':'m1','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'mark':{'gi':sh_mark},'chance':1},'ts':'13:33'},
  {'id':'m2','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':SH_PRE},
   'fail':{'goto':'m1','via':{'cur':'Preserved_Rib','also':[SH_LIGHT]}},'ts':'13:50','br':K('실패: 보존된 갈비뼈로 징표 훼손 → 빛의 징조 + 소멸의 오브 → {#m1}번부터','Miss: desecrate the Mark with a Preserved Rib → Light + Annulment → back to step {#m1}')},
  {'id':'m3','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p','fromMark':True},'ts':'14:52'},
  {'id':'m4','phase':'pre','branch':{'of':'p1','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SH_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'m3','via':SH_LIGHT},'ts':'15:57'},
 ]})
