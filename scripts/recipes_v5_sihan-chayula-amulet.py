# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜목걸이 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/2vyq26ZFgOk) ----
c='Amulets'
SHA=K('시한 영상 기반','Based on 시한')
def textAA(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
ca_spirit=textAA('to Spirit','n','p'); ca_dex=textAA('to Dexterity','n','s')
ca_es=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='n' and gr['g']=='p' and gr['t'][0][5].endswith('to maximum Energy Shield')][0]
# 완벽한 무한의 에센스(목걸이) = 접미 '힘·민첩·지능 (7—10)% 증가' — 힘 +(25—27)은 상위 무한의 에센스(사용자 지적 2026-11-11)
ca_strp=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and gr['g']=='s' and gr['t'][0][5].endswith('increased Strength')][0]
ca_skill=textAA('+1 to Level of all Skills','d','s')
R.append({
 'id':'sihan-chayula-amulet','cls':c,'base':base(c,'Absent Amulet'),'ilvl':80,'difficulty':3,'budget':'low',
 'buildTags':[K('정신력','Spirit'),K('스킬 레벨','Skill level'),K('차율라','Chayula')],'patch':'0.5.5','created':'2026-11-11','author':SHA,
 'source':{'url':'https://www.youtube.com/watch?v=2vyq26ZFgOk','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜목걸이 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('정신력 + 에너지 보호막 + 민첩 분열 + 울라만 모든 스킬 레벨','spirit + energy shield + fractured dexterity + Ulaman all skills'),
 'start':{'rar':'rare','mods':[{'gi':ca_es,'tmax':2},{'gi':ca_spirit,'tmax':1},{'gi':ca_dex,'tmax':1,'fr':True},{'unrev':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fin','kr':'울라만 훼손','en':'Ulaman desecration'}],
 'nodes':[
  {'id':'a1','phase':'base','do':'base','cost':'base','ts':'3:08','note':K('정신력 분열에 실패한 부재 목걸이 구입: 에너지 보호막 + 정신력 / 민첩 분열 + 미공개 훼손 접미(영상 약 15 div).','Buy a failed Spirit-fracture Absent Amulet: energy shield + Spirit / fractured Dexterity + an unrevealed desecrated suffix (about 15 div in the video).')},
  {'id':'a2','phase':'fin','do':'essence','cur':'Perfect_Essence_of_the_Infinite','target':{'gi':ca_strp},'ts':'3:20'},
  {'id':'a3','phase':'fin','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Sovereign'],'target':{'unrev':'s','dropGi':ca_strp},'ts':'3:35'},
  {'id':'a4','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':ca_skill},'side':'s','lord':'ulaman','bone':'Preserved_Collarbone'},'fail':{'goto':'a2'},'ts':'3:47',
   'br':K('실패: 완벽한 무한의 에센스로 훼손 옵션을 지우고 빛의 징조 없이 다시','Miss: Perfect Essence of the Infinite clears the desecrated line, then again (no Omen of Light)')},
  {'id':'a5','phase':'fin','do':'note','ts':'5:52','note':K('완성.','Done.')},
 ]})
