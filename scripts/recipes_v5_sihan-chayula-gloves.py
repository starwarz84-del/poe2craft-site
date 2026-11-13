# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜장갑 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/Sf-2cvWhQY0) ----
c='Gloves_dex_int'
SHG=K('시한 영상 기반','Based on 시한')
def textGG(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
cg_pois=textGG('Magnitude of Poison you inflict','x','p'); cg_curse=textGG('faster Curse Activation','x','s')
cg_fast=textGG('Damaging Ailments deal damage','x','p'); cg_ail=textGG('increased Magnitude of Ailments you inflict','x','p')
cg_with=textGG('increased Withered Magnitude','x','s'); cg_cmag=textGG('increased Curse Magnitudes','x','s')
KATLA=K('카틀라의 순흑',"Katla's Gloom")
R.append({
 'id':'sihan-chayula-gloves','cls':c,'base':base(c,'Secured Wraps'),'ilvl':83,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('중독','Poison'),K('저주','Curse'),K('차율라','Chayula')],'patch':'0.5.5','created':'2026-11-11','author':SHG,
 'source':{'url':'https://www.youtube.com/watch?v=Sf-2cvWhQY0','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜장갑 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('카틀라의 순흑 · 중독 강도 분열 + 저주 활성화 속도 + 상태 이상 옵션','Katla\'s Gloom: fractured poison magnitude + curse activation + ailment lines'),
 'start':{'rar':'rare','runes':[KATLA],'mods':[{'gi':cg_pois,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'core','kr':'필수 옵션','en':'Must-have lines'},{'id':'rand','kr':'랜덤 옵션','en':'Random lines'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'0:01','note':K('아이템 레벨 83 고정된 싸개, 룬 소켓 2개. 카틀라의 순흑 장착, 중독의 강도 1티어 분열 + 잡옵 1개.','Item level 83 Secured Wraps with two sockets: Katla\'s Gloom socketed, fractured tier 1 poison magnitude plus one junk line.')},
  {'id':'g2','phase':'core','do':'chaos','cur':'Chaos_Orb','target':{'gi':cg_curse,'tmax':1},'fail':{'goto':'self'},'ts':'2:22'},
  {'id':'g3','phase':'rand','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation','Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':cg_fast},{'gi':cg_ail}],'asIs':True,'side':'p'},'ts':'3:19'},
  {'id':'g4','phase':'rand','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':cg_with},{'gi':cg_cmag}],'asIs':True,'side':'s'},'ts':'3:47'},
  {'id':'g5','phase':'rand','do':'note','ts':'9:29','note':K('완성. 필수 2개 + 쓸 만한 옵션 1개면 멈춤.','Done; stop at the two must-haves plus one useful line.')},
 ]})
