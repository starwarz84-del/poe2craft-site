# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜목걸이 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/2vyq26ZFgOk) ----
c='Amulets'
SHA=K('시한 영상 기반','Based on 시한')
def textAA(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
ca_spirit=textAA('to Spirit','n','p'); ca_dex=textAA('to Dexterity','n','s'); ca_life=textAA('to maximum Life','n','p')
ca_str=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and gr['g']=='s' and 'Strength, Dexterity or Intelligence' in gr['t'][0][5]][0]
ca_skill=textAA('+1 to Level of all Skills','d','s')
R.append({
 'id':'sihan-chayula-amulet','cls':c,'base':base(c,'Solar Amulet'),'ilvl':82,'difficulty':3,'budget':'low',
 'buildTags':[K('정신력','Spirit'),K('스킬 레벨','Skill level'),K('차율라','Chayula')],'patch':'0.5.5','created':'2026-11-11','author':SHA,
 'source':{'url':'https://www.youtube.com/watch?v=2vyq26ZFgOk','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜목걸이 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('정신력 + 능력치 분열 + 울라만 모든 스킬 레벨','spirit + fractured attribute + Ulaman all skills'),
 'start':{'rar':'rare','mods':[{'gi':ca_spirit,'tmax':1},{'gi':ca_life,'tmax':2},{'gi':ca_dex,'tmax':1,'fr':True},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fin','kr':'울라만 훼손','en':'Ulaman desecration'}],
 'nodes':[
  {'id':'a1','phase':'base','do':'base','cost':'base','ts':'0:59','note':K('정신력 분열에 실패한 목걸이 구입: 정신력 + 접미 능력치 분열(영상 약 15 div).','Buy a failed Spirit-fracture amulet: Spirit with a fractured attribute suffix (about 15 div in the video).')},
  {'id':'a2','phase':'fin','do':'essence','cur':'Perfect_Essence_of_the_Infinite','target':{'gi':ca_str},'ts':'3:17'},
  {'id':'a3','phase':'fin','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Sovereign'],'target':{'unrev':'s'},'fail':{'goto':'a2'},'ts':'3:30'},
  {'id':'a4','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':ca_skill},'side':'s','lord':'ulaman','bone':'Preserved_Collarbone'},'fail':{'goto':'a2'},'ts':'3:45',
   'br':K('실패: 완벽한 무한의 에센스로 훼손 옵션을 지우고 다시(빛의 징조 없이)','Miss: Perfect Essence of the Infinite clears the desecrated line, then again (no Omen of Light)')},
  {'id':'a5','phase':'fin','do':'note','ts':'5:35','note':K('완성. 접두 마지막 자리는 자유.','Done; the last prefix is free.')},
 ]})
