# ---- XTheFarmerX "INSANELY Cheap Way To Craft Your League Start ALL Of Your Armor For POE2 0.5.5" (youtu.be/UWrIgHklsPg) ----
FM5=K('XTheFarmerX 영상 기반','Based on XTheFarmerX')
c='Body_Armours_int'
def textF(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
fa_flat=textF('to maximum Energy Shield','n','p'); fa_hyb=textF('to maximum Energy Shield\n','n','p'); fa_life=textF('% increased Energy Shield\n+','n','p')
fa_spirit=textF('to Spirit','n','p'); fa_ess=textF('increased Armour, Evasion and Energy Shield','e','p')
R.append({
 'id':'farmer-budget-armour','cls':c,'base':base(c,'Flowing Raiment'),'ilvl':79,'difficulty':1,'budget':'low',
 'buildTags':[K('에너지 보호막','Energy Shield'),K('리그 초반','League start'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':FM5,
 'source':{'url':'https://www.youtube.com/watch?v=UWrIgHklsPg','title':'INSANELY Cheap Way To Craft Your League Start ALL Of Your Armor For POE2 0.5.5','channel':'XTheFarmerX'},
 'title':K('에너지 보호막 접두 옵션 3개 (리그 초반 가성비)','three energy shield prefixes (league-start budget)'),
 'start':{'rar':'magic','mods':[{'gi':fa_flat,'tmax':3}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'}],
 'nodes':[
  {'id':'f1','phase':'base','do':'base','cost':'base','ts':'3:03','note':K('에너지 보호막 최대치 3티어 이상(접두)만 붙은 매직 흐르는 의복. 다른 에너지 보호막 베이스도 가능.','A magic Flowing Raiment with only a T3+ flat energy shield prefix. Any energy shield base works.')},
  {'id':'f2','phase':'base','do':'augment','cur':'Greater_Orb_of_Augmentation','target':{'junk':'s'},'ts':'3:23'},
  {'id':'f3','phase':'pre','do':'essence','cur':'Greater_Essence_of_Enhancement','target':{'gi':fa_ess},'ts':'3:31'},
  {'id':'f4','phase':'pre','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'3:55'},
  {'id':'f5','phase':'pre','do':'reveal','target':{'reveal':{'anyOf':[{'gi':fa_hyb},{'gi':fa_life},{'gi':fa_spirit}]},'side':'p','bone':'Preserved_Rib'},'fail':{'goto':'f4','via':LIGHT},'ts':'4:13'},
  {'id':'f6','phase':'suf','do':'manual','target':{'rune':K('상위 철 룬','Greater Iron Rune')},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'4:24'},
  {'id':'f7','phase':'suf','do':'manual','target':{'rune':K('상위 철 룬','Greater Iron Rune')},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'4:24'},
  {'id':'f8','phase':'suf','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'4:38',
   'br':K('저항이 뜨면 대박. 꽝이어도 완성(저항은 장갑·장화에서).','Resistances are the jackpot; a miss still finishes it (get resistances on gloves and boots).')},
 ]})
