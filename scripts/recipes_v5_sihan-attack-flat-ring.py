# ---- 시한 "[POE2 0.5.5] 공격 플랫 3줄 반지 제작 방법｜공격 빌드 필수 반지｜실전 제작 포함" (youtu.be/bpXgZGw4WQo) ----
c='Rings'
SHF=K('시한 영상 기반','Based on 시한')
def textFF(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sf_phys=textFF('to (22—32) Physical Damage to Attacks','n','p'); sf_fire=textFF('to (37—45) Fire damage to Attacks','n','p')
sf_cold=textFF('to (32—37) Cold damage to Attacks','n','p'); sf_lgt=textFF('to (60—71) Lightning damage to Attacks','n','p')
sf_maxq=textFF('to Maximum Quality','e','p'); sf_as=textFF('increased Attack Speed','e','s')
SF_FLAT=[{'gi':g,'tmax':2} for g in (sf_fire,sf_cold,sf_lgt)]   # 분열 플랫(물리) 말고 다른 원소 플랫
R.append({
 'id':'sihan-attack-flat-ring','cls':c,'base':base(c,'Unset Ring'),'ilvl':75,'difficulty':3,'budget':'medium',
 'buildTags':[K('공격','Attack'),K('추가 피해','Flat damage'),K('공격 속도','Attack speed')],'patch':'0.5.5','created':'2026-11-11','author':SHF,
 'source':{'url':'https://www.youtube.com/watch?v=bpXgZGw4WQo','title':'[POE2 0.5.5] 공격 플랫 3줄 반지 제작 방법｜공격 빌드 필수 반지｜실전 제작 포함','channel':'시한'},
 'title':K('공격 추가 피해 1티어 분열 + 플랫 2개 + 재빠른 합금 공격 속도','fractured tier 1 attack flat + two more flats + Swift Alloy attack speed'),
 'start':{'rar':'rare','mods':[{'gi':sf_phys,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'q','kr':'퀄리티','en':'Quality'},{'id':'pre','kr':'접두','en':'Prefix'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'훼손 마무리','en':'Desecration finish'}],
 'nodes':[
  {'id':'f1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('아이템 레벨 75 이상 무보석 반지, 공격 추가 피해 1티어 분열 + 잡옵 1개(분열된 매물이 60 div 아래면 구입).','Item level 75+ Unset Ring: fractured tier 1 attack flat plus one junk line (buy one if a fractured listing costs under ~60 div).')},
  {'id':'f2','phase':'q','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':sf_maxq},'ts':'1:50'},
  {'id':'f3','phase':'q','do':'quality','cur':'Reaver_Catalyst','target':{'quality':40},'ts':'2:08'},
  {'id':'f4','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':SF_FLAT},'br':K('카오스 오브가 최대 퀄리티 옵션을 바꿈(퀄리티는 유지)','Chaos replaces the max-quality line (quality stays)'),'fail':{'goto':'self'},'ts':'2:20'},
  {'id':'f5','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'2:52'},
  {'id':'f6','phase':'suf','do':'essence','cur':'Swift_Alloy','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':sf_as,'chance':1},'ts':'3:10'},
  {'id':'f7','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'junk':'s','count':2},'ts':'4:19',
   'br':K('마음에 드는 2개가 나올 때까지 소멸의 오브 + 다시(플랫이 지워지면 카오스 오브부터)','Repeat with Annulment until both are good (lost a flat → back to the Chaos step)')},
  {'id':'f8','phase':'fin','do':'desecrate','cur':'Ancient_Collarbone','target':{'unrev':'p'},'ts':'16:45'},
  {'id':'f9','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SF_FLAT},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'f8','via':LIGHT},'ts':'17:28'},
  {'id':'f10','phase':'fin','do':'note','ts':'18:30','note':K('완성. 공격 추가 피해 3개 + 공격 속도.','Done: three attack flats plus attack speed.')},
 ]})
