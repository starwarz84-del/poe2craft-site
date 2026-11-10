# ---- XTheFarmerX league-start armour (youtu.be/UWrIgHklsPg) — grade recipes (policy 25) from scripts/graphs/farmer-budget-armour-v2.json ----
# Rewrites 'farmer-budget-armour' (REPLACES). Video steps; the Greater Iron Runes are taste (policy 23), so the sockets stay empty.
# Essential = video (Preserved Rib, any tier); Balance / High-end use an Ancient Rib (only level 40+ tiers) for T1–2 / T1.
c='Body_Armours_int'
def _fa(t, sec, side=None):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]: return gi
    raise Exception(t)
fa2_flat=_fa('to maximum Energy Shield','n','p'); fa2_hyb=_fa('to maximum Energy Shield\n','n','p'); fa2_life=_fa('% increased Energy Shield\n+','n','p')
fa2_spirit=_fa('to Spirit','n','p'); fa2_ess=_fa('increased Armour, Evasion and Energy Shield','e','p')
def fm_armour(tier):
    hi=tier=='high'; rid='farmer-budget-armour-v2'+('' if hi else '-'+tier)
    es={'high':1,'bal':2,'ess':3}[tier]; rv={'high':1,'bal':2,'ess':9}[tier]; bone='Preserved_Rib' if tier=='ess' else 'Ancient_Rib'
    R.append({
 'id':rid,'tierGroup':'farmer-budget-armour-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Flowing Raiment'),'ilvl':79,'difficulty':1,'budget':'low',
 'buildTags':[K('에너지 보호막','Energy Shield'),K('리그 초반','League start'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':K('XTheFarmerX 영상 기반','Based on XTheFarmerX'),
 'source':{'url':'https://www.youtube.com/watch?v=UWrIgHklsPg','title':'INSANELY Cheap Way To Craft Your League Start ALL Of Your Armor For POE2 0.5.5','channel':'XTheFarmerX'},
 'title':K('에너지 보호막 접두 옵션 3개 (리그 초반 가성비)','three energy shield prefixes (league-start budget)'),
 'start':{'rar':'magic','mods':[{'gi':fa2_flat,'tmax':es}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'},{'id':'suf','kr':'접미 두번째·세번째 옵션','en':'Suffix options 2–3'}],
 'nodes':[
  {'id':'f1','phase':'base','do':'base','cost':'base','ts':'3:03','note':K('에너지 보호막 최대치(접두)만 붙은 매직 흐르는 의복.','A magic Flowing Raiment with only a flat energy shield prefix.')},
  {'id':'f2','phase':'base','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'3:23'},
  {'id':'f3','phase':'base','do':'essence','cur':'Greater_Essence_of_Enhancement','target':{'gi':fa2_ess},'ts':'3:31'},
  {'id':'f4','phase':'pre','do':'desecrate','cur':bone,'omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'3:55'},
  {'id':'f5','phase':'pre','do':'reveal','target':{'reveal':{'anyOf':[dict({'gi':g},**({'tmax':rv} if rv<9 else {})) for g in (fa2_hyb,fa2_life,fa2_spirit)]},'side':'p','bone':bone},'fail':{'goto':'f4','via':LIGHT},'ts':'4:13'},
  {'id':'f8','phase':'suf','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'4:38',
   'br':K('저항이 뜨면 대박. 꽝이어도 완성.','Resistances are the jackpot; a miss still finishes it.')},
 ]})
for _t in ('high','bal','ess'): fm_armour(_t)
