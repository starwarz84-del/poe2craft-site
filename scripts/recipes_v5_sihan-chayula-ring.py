# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜반지 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/GgD_vxKgNsw) ----
c='Rings'
SHR=K('시한 영상 기반','Based on 시한')
def textRR(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
cr_far=textRR('Remnants can be collected from','x','s'); cr_res=textRR('to all Elemental Resistances','n','s'); cr_chaos=textRR('increased Chaos Damage','n','p')
cr_eff=textRR('Remnants you create have','d','p'); cr_maxq=textRR('to Maximum Quality','e','p')
R.append({
 'id':'sihan-chayula-ring','cls':c,'base':base(c,'Breach Ring'),'ilvl':81,'difficulty':4,'budget':'medium',
 'buildTags':[K('카오스','Chaos'),K('잔류물','Remnants'),K('저항','Resistances'),K('차율라','Chayula')],'patch':'0.5.5','created':'2026-11-11','author':SHR,
 'source':{'url':'https://www.youtube.com/watch?v=GgD_vxKgNsw','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜반지 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('잔류물 거리 분열 + 모든 원소 저항 + 카오스 피해 + 아마나무 잔류물 효과','fractured remnant range + all res + chaos damage + Amanamu remnant effect'),
 'start':{'rar':'rare','mods':[{'gi':cr_far,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'q','kr':'퀄리티','en':'Quality'},{'id':'core','kr':'옵션','en':'Lines'},{'id':'fin','kr':'훼손 마무리','en':'Desecration finish'}],
 'nodes':[
  {'id':'r1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('잔류물 더 먼 곳에서 획득 분열 + 잡옵 1개 균열 반지(카오스 오브로는 안 나오는 옵션).','Breach Ring with fractured remnant pickup range plus one junk line (that line cannot come from Chaos Orbs).')},
  {'id':'r2','phase':'q','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':cr_maxq},'ts':'1:30'},
  {'id':'r3','phase':'q','do':'quality','cur':'Chayulas_Catalyst','target':{'quality':60},'ts':'1:43'},
  {'id':'r4','phase':'core','do':'chaos','cur':'Chaos_Orb','target':{'gi':cr_res,'tmax':2},'fail':{'goto':'self'},'ts':'0:20'},
  {'id':'r5','phase':'core','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'gi':cr_chaos,'tmax':2},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'r4'},'ts':'3:27'},
  {'id':'r6','phase':'fin','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Sinistral_Necromancy','Omen_of_the_Liege'],'target':{'unrev':'p'},'ts':'3:40'},
  {'id':'r7','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':cr_eff},'side':'p','lord':'amanamu','bone':'Preserved_Collarbone'},'fail':{'goto':'r6','via':LIGHT},'ts':'4:20'},
  {'id':'r8','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'3:56','br':K('마지막 옵션은 나오는 대로','Last line stays as rolled')},
  {'id':'r9','phase':'fin','do':'note','ts':'4:28','note':K('완성. 모든 원소 저항 12% 이상(2티어 이상)이면 충분.','Done; all resistances at 12%+ (tier 2 or better) is enough.')},
 ]})
