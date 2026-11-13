# ---- XTheFarmerX league-start armour (youtu.be/UWrIgHklsPg) — grade recipes (policy 25) from scripts/graphs/farmer-budget-armour-v2.json ----
# Rewrites 'farmer-budget-armour' (REPLACES). Video steps; the Greater Iron Runes are taste (policy 23), so the sockets stay empty.
# 2026-11-13 G14: easy (difficulty 1) → Essential only = the video (Greater Augmentation, Preserved Rib, reveal and exalt kept as they come).
c='Body_Armours_int'
def _fa(t, sec, side=None):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]: return gi
    raise Exception(t)
fa2_flat=_fa('to maximum Energy Shield','n','p'); fa2_hyb=_fa('to maximum Energy Shield\n','n','p'); fa2_life=_fa('% increased Energy Shield\n+','n','p')
fa2_spirit=_fa('to Spirit','n','p'); fa2_ess=_fa('increased Armour, Evasion and Energy Shield','e','p')
def fm_armour(tier):
    # 2026-11-13 G14: 영상 전체 화면 대조(근거 scratchpad review/G14/farmer-budget-armour-v2/timeline.md). 난이도 쉬움 → 에센셜만(정책 10장).
    # 단계·확률은 플로우차트(scripts/graphs/gen_farmer_budget_armour.py)에서 읽음. 상자 id(b0·g1~g5)는 옛 단계 id(f1~f8)와 겹치지 않게 새로 붙임.
    rid='farmer-budget-armour-v2-'+tier
    R.append({
 'id':rid,'tierGroup':'farmer-budget-armour-v2','tier':tier,'tierLabel':K('에센셜','Essential'),
 'cls':c,'base':base(c,'Flowing Raiment'),'ilvl':79,'difficulty':1,'budget':'low',
 'buildTags':[K('에너지 보호막','Energy Shield'),K('리그 초반','League start'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':K('XTheFarmerX 영상 기반','Based on XTheFarmerX'),
 'source':{'url':'https://www.youtube.com/watch?v=UWrIgHklsPg','title':'INSANELY Cheap Way To Craft Your League Start ALL Of Your Armor For POE2 0.5.5','channel':'XTheFarmerX'},
 'title':K('에너지 보호막 접두 옵션 3개 (리그 초반 가성비)','three energy shield prefixes (league-start budget)'),
 'start':{'rar':'magic','mods':[{'gi':fa2_flat,'tmax':3}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'},{'id':'suf','kr':'접미 두번째·세번째 옵션','en':'Suffix options 2–3'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'3:16','note':K('에너지 보호막 최대치 3티어 매직 흐르는 의복(아이템 레벨 79), 1 엑잘티드 오브.','A magic Flowing Raiment with T3 maximum energy shield (item level 79), 1 Exalted Orb.')},
  {'id':'g1','phase':'base','do':'augment','cur':'Greater_Orb_of_Augmentation','target':{'junk':'s'},'ts':'3:26'},
  {'id':'g2','phase':'base','do':'essence','cur':'Greater_Essence_of_Enhancement','target':{'gi':fa2_ess},'ts':'3:45'},
  {'id':'g3','phase':'pre','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'4:00'},
  {'id':'g4','phase':'pre','do':'reveal','target':{'reveal':{'gi':fa2_hyb},'side':'p','bone':'Preserved_Rib'},'ts':'4:14'},
  {'id':'g5','phase':'suf','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'4:57'},
 ]})
fm_armour('ess')
