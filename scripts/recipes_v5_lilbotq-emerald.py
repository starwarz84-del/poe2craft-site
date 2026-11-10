# ---- LilBotQ "How I Make 100s Of Divines Selling Jewels - Crafting Guide for Path of Exile 2" (youtu.be/Hcb_HcWDUOA) ----
LBQ=K('LilBotQ 영상 기반','Based on LilBotQ')
c='Emerald'
def textL(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
lq_cdmg=textL('Critical Damage Bonus for Attack Damage','n','s'); lq_ms=textL('increased Movement Speed','n','s')
lq_cc=textL('Critical Hit Chance for Attacks','n','s'); lq_as=textL('% increased Attack Speed','n','s')
lq_adm=textL('increased Attack Damage','n','p')
lq_plus=textL('+1 Suffix Modifier allowed','x','p'); lq_eff=textL('Effect of Suffixes','x','p')
assert 'with' not in cd(c)['groups'][lq_as]['t'][0][5]
R.append({
 'id':'lilbotq-emerald','cls':c,'base':0,'ilvl':82,'cap':{'p':2,'s':2},'difficulty':3,'budget':'high','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('치명타','Critical'),K('이동 속도','Movement speed')],'patch':'0.5','created':'2026-11-09','author':LBQ,
 'source':{'url':'https://www.youtube.com/watch?v=Hcb_HcWDUOA','title':'How I Make 100s Of Divines Selling Jewels - Crafting Guide for Path of Exile 2','channel':'LilBotQ'},
 'title':K('공격 치명타 접미 옵션 3개 + 접미 효과 5옵션','three attack crit/speed suffixes + suffix effect, five mods'),
 'start':{'rar':'rare','mods':[{'gi':lq_cdmg},{'gi':lq_ms},{'junk':'p'},{'junk':'p'}]},
 'phases':[{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'des','kr':'3번째 접미 (훼손)','en':'Third suffix (desecrated)'},{'id':'pre','kr':'접두 · 흉포함','en':'Prefixes and Ferocity'}],
 'nodes':[
  {'id':'l1','phase':'con','do':'base','cost':'base','ts':'10:38','note':K('공격 치명타 피해 보너스 + 이동 속도 접미, 접두 옵션 2개가 붙은 희귀 에메랄드를 구매.','Buy a rare Emerald with attack crit damage bonus and movement speed suffixes plus two prefixes.')},
  {'id':'l2','phase':'con','do':'essence','cur':'Potent_Liquid_Contempt','knownP':True,'target':{'gi':lq_plus,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'restart'},'ts':'14:58'},
  {'id':'l3','phase':'des','do':'desecrate','cur':'Preserved_Cranium','target':{'unrev':'s'},'ts':'15:20'},
  {'id':'l4','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':lq_cc},{'gi':lq_as}]},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'l3','via':LIGHT},'ts':'15:31'},
  {'id':'l5','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment'],'target':{'dropGi':lq_plus},'ts':'19:03',
   'br':K('성공 → 다음, 실패(잡옵이 지워짐) → 좌측 말소의 징조 + 카오스 오브','Hit → next; miss (junk went) → Sinistral Erasure + Chaos')},
  {'id':'l5b','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'fallbackFor':'l5','target':{'removeGi':lq_plus,'junk':'p'},'ts':'19:20'},
  {'id':'l6','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'19:28'},
  {'id':'l7','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'gi':lq_adm,'replace':'p'},'fail':{'goto':'self'},'ts':'19:50'},
  {'id':'l8','phase':'pre','do':'essence','cur':'Potent_Liquid_Ferocity','knownP':True,'target':{'gi':lq_eff,'chance':0.5},'fail':{'goto':'l7'},'ts':'20:19'},
  {'id':'l9','phase':'pre','do':'note','ts':'21:14','note':K('완성. 신성한 오브로 수치 정리.','Done; divine the rolls.')},
 ]})
