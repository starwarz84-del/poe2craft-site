# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜투구 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/z_r1uAYIusk) ----
c='Helmets_dex_int'
SHH=K('시한 영상 기반','Based on 시한')
def textHH(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
ch_pct=textHH('% increased Evasion and Energy Shield','n','p')
ch_life=textHH('to maximum Life','n','p'); ch_hyb=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='n' and gr['g']=='p' and 'Evasion and Energy Shield' in gr['t'][0][5] and 'maximum Life' in gr['t'][0][5]][0]
ch_defl=textHH('Gain Deflection Rating','n','s'); ch_crit=textHH('increased Critical Hit Chance','n','s')
ch_flat=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='n' and gr['g']=='p' and gr['t'][0][5].startswith('+') and 'Evasion Rating' in gr['t'][0][5] and 'Energy Shield' in gr['t'][0][5]][0]
CH_PRE=[{'gi':ch_flat,'tmax':3},{'gi':ch_life,'tmax':3},{'gi':ch_hyb,'tmax':3}]
R.append({
 'id':'sihan-chayula-helmet','cls':c,'base':base(c,'Grinning Mask'),'ilvl':82,'difficulty':3,'budget':'medium',
 'buildTags':[K('회피','Evasion'),K('에너지 보호막','Energy Shield'),K('튕겨내기','Deflection'),K('차율라','Chayula')],'patch':'0.5.5','created':'2026-11-11','author':SHH,
 'source':{'url':'https://www.youtube.com/watch?v=z_r1uAYIusk','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜투구 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('회피·에너지 보호막 % 분열 + 튕겨내기 평점 + 방어 접두 3개','fractured evasion/ES % + deflection + three defence prefixes'),
 'start':{'rar':'rare','mods':[{'gi':ch_pct,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미','en':'Suffix'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'0:29','note':K('아이템 레벨 82 웃는 가면, 회피 및 에너지 보호막 % 1티어 분열 + 잡옵 1개. 다른 접두 분열도 가능.','Item level 82 Grinning Mask: fractured tier 1 evasion/ES % plus one junk line; another prefix fracture also works.')},
  {'id':'h2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':ch_defl,'tmax':2},'fail':{'goto':'self'},'ts':'0:58'},
  {'id':'h3','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'gi':ch_crit,'tmax':2},'optional':True,
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'h2'},'ts':'1:25','label':K('치명타 확률 (자금 여유가 있을 때)','Critical hit chance (when you can afford it)')},
  {'id':'h4','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':CH_PRE},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'h2'},'ts':'1:54'},
  {'id':'h5','phase':'pre','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'8:00'},
  {'id':'h6','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':CH_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'h5','via':LIGHT},'ts':'10:06'},
  {'id':'h7','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'asIs':True,'side':'s','anyOf':[{'gi':ch_crit,'tmax':3}]},'ts':'7:04',
   'br':K('남은 접미 2자리는 나오는 대로','The last two suffixes stay as rolled')},
  {'id':'h8','phase':'fin','do':'note','ts':'11:36','note':K('완성. 저항·능력치가 떠도 그대로 진행.','Done; resistances or attributes are fine as they come.')},
 ]})
