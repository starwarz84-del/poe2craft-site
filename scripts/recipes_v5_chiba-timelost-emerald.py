# ---- ChibaTTV "COMO CRAFTAR TIME-LOST EMERALD PERFEITA para TWISTER | Path of Exile 2" (youtu.be/O6Rp7JIxhrs) ----
CB5=K('ChibaTTV 영상 기반','Based on ChibaTTV')
c='Time-Lost_Emerald'
def textC(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
cb_cc=textC('increased Critical Hit Chance for Attac','n','s'); cb_cdA=textC('Critical Damage Bonus for At','n','s'); cb_cdS=textC('Critical Damage Bonus with S','n','s')
cb_as=textC('(1—2)% increased Attack Speed','n','s'); cb_asS=textC('increased Attack Speed with Spears','n','s'); cb_nef=textC('increased Effect of Notable Passive Skills','n','s')
cb_pspd=textC('increased Projectile Speed','n','p'); cb_pdmg=textC('(1—2)% increased Projectile Damage','n','p'); cb_adm=textC('increased Attack Damage','n','p')
cb_plusS=textC('+1 Suffix Modifier allowed','x','p'); cb_mel=textC('Upgrades Radius to Very Large','x','p')
assert cd(c)['groups'][cb_as]['t'][0][5].strip().endswith('Attack Speed') and 'if' not in cd(c)['groups'][cb_pdmg]['t'][0][5]
CB_PRE=[{'gi':cb_pspd},{'gi':cb_pdmg},{'gi':cb_adm}]
R.append({
 'id':'chiba-timelost-emerald','cls':c,'base':0,'ilvl':80,'cap':{'p':2,'s':2},'difficulty':4,'budget':'high','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('오래된 주얼','Time-Lost jewel'),K('공격 치명타','Attack crit'),K('돌개바람','Twister')],'patch':'0.5.5','created':'2026-11-09','author':CB5,
 'source':{'url':'https://www.youtube.com/watch?v=O6Rp7JIxhrs','title':'COMO CRAFTAR TIME-LOST EMERALD PERFEITA para TWISTER | Path of Exile 2','channel':'ChibaTTV'},
 'title':K('공격 치명타 분열 + 치명타·공격 속도 3접미 + 매우 넓은 반경','fractured attack crit + three crit/speed suffixes, Very Large radius'),
 'start':{'rar':'rare','mods':[{'gi':cb_cc,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미 옵션 2개','en':'Two suffixes'},{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'des','kr':'3번째 접미 (훼손)','en':'Third suffix (desecrated)'},{'id':'pre','kr':'접두 · 우울','en':'Prefixes and Melancholy'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'c1','phase':'suf','do':'base','cost':'base','ts':'0:23',
   'note':K('공격 치명타 확률 7%(최대) 분열 + 잡옵 1개.','Fractured 7% attack crit chance (max) plus one junk line.')},
  {'id':'c2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':cb_cdS},{'gi':cb_cdA}]},'fail':{'goto':'self'},'ts':'5:02'},
  {'id':'c3','phase':'con','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p','count':2},'ts':'5:42'},
  {'id':'c4','phase':'con','do':'essence','cur':'Ancient_Potent_Liquid_Contempt','knownP':True,'target':{'gi':cb_plusS,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'c2','via':{'cur':'Orb_of_Annulment'}},'ts':'5:53'},   # W24 11-13: 분기 줄은 플로우차트 갈래 칩과 겹쳐 뺌
  {'id':'c5','phase':'des','do':'desecrate','cur':'Preserved_Cranium','target':{'unrev':'s'},'ts':'6:11'},
  {'id':'c6','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':cb_as},{'gi':cb_cdA},{'gi':cb_asS},{'gi':cb_nef}]},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'c5','via':LIGHT},'ts':'6:15'},
  {'id':'c7','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment'],'target':{'dropGi':cb_plusS},'ts':'10:02',
   'br':K('경멸 옵션이 지워지면 다음, 잡옵이 지워지면 남은 접두가 경멸 옵션뿐이니 한 번 더','Contempt line gone → next; junk gone → once more (only the Contempt line is left)')},
  {'id':'c8','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'10:30',
   'br':K('접두 옵션 2개까지, 두 번 지웠으면 2번','Up to two prefixes (twice if both were annulled)')},
  {'id':'c9','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':CB_PRE},'fail':{'goto':'self'},'ts':'10:40'},
  {'id':'c10','phase':'pre','do':'essence','cur':'Ancient_Potent_Liquid_Melancholy','knownP':True,'target':{'gi':cb_mel,'chance':0.5,'missDrop':cb_pspd},'fail':{'goto':'c9'},'ts':'11:08'},   # W24 11-13: 분기 줄은 플로우차트 갈래 칩과 겹쳐 뺌(밸런스는 결과 그대로)
  {'id':'c11','phase':'fin','do':'quality','cur':'Refined_Reaver_Catalyst','target':{'quality':20},'ts':'11:57'},
 ]})
