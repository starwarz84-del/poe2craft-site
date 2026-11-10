# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜셉터 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/-F7pV0Y7BMA) ----
c='Sceptres'
SHS=K('시한 영상 기반','Based on 시한')
def textS(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
ss_spirit=textS('(61—65)% increased Spirit','n','p'); ss_hyb=textS('increased Spirit\n+','n','p')
ss_aoe=textS('increased Presence Area of Effect','n','s')
ss_ward=textS('maximum Runic Ward','e','s'); ss_aura=textS('Aura Skills have','e','s')
R.append({
 'id':'sihan-chayula-sceptre','cls':c,'base':base(c,'Stoic Sceptre'),'ilvl':82,'difficulty':2,'budget':'low',
 'buildTags':[K('정신력','Spirit'),K('오라','Aura'),K('룬 수호','Runic Ward')],'patch':'0.5.5','created':'2026-11-09','author':SHS,
 'source':{'url':'https://www.youtube.com/watch?v=-F7pV0Y7BMA','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜셉터 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('정신력 분열 + 접근 효과 범위 1티어 + 제작 옵션 2개','fractured Spirit + T1 presence area + two crafted lines'),
 'start':{'rar':'rare','quality':20,'mods':[{'gi':ss_spirit,'tmax':2,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'s1','phase':'suf','do':'base','cost':'base','ts':'1:10','note':K('정신력 % 2티어 이상 분열 + 잡옵 1개.','Fractured T2+ % Spirit plus one junk line.')},
  {'id':'s2','phase':'suf','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'1:13'},
  {'id':'s3','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':ss_aoe,'tmax':1},'fail':{'goto':'self'},'ts':'1:18'},
  {'id':'s4','phase':'suf','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'1:40'},
  {'id':'s5','phase':'suf','do':'essence','cur':'Protective_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':ss_ward},'ts':'1:53'},
  {'id':'s6','phase':'suf','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'2:07'},
  {'id':'s7','phase':'suf','do':'essence','cur':'Perfect_Essence_of_Command','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':ss_aura},'ts':'2:20'},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'5:43'},
  {'id':'p2','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'5:47'},
  {'id':'p3','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'5:53'},
  {'id':'p4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':ss_hyb,'tmax':4},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'p3','via':LIGHT},'ts':'6:03',
   'br':K('대박 → 완성, 실패: 빛의 징조 + 소멸의 오브 → {#p3}번','hit → done; miss: Omen of Light + Annulment → step {#p3}')},
 ]})
