# ---- XTheFarmerX "How To Craft Your League Starter Weapon For CHEAP In POE2 0.5.5!" (youtu.be/ITBexsgq2NI) ----
FW5=K('XTheFarmerX 영상 기반','Based on XTheFarmerX')
c='Staves'
def textW(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
fw_l5=textW('+(5—6) to Level of all Lightning Spell Skills','n','s')
fw_xF=textW('Extra Fire Damage','n','p'); fw_xC=textW('Extra Cold Damage','n','p'); fw_xL=textW('Extra Lightning Damage','n','p')
fw_xCh=textW('Extra Chaos Damage','d','p'); fw_spellE=textW('increased Spell Damage','e','p')
R.append({
 'id':'farmer-starter-staff','cls':c,'base':base(c,'Sanctified Staff'),'ilvl':73,'difficulty':1,'budget':'low',
 'buildTags':[K('번개','Lightning'),K('주문','Spell'),K('리그 초반','League start'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':FW5,
 'source':{'url':'https://www.youtube.com/watch?v=ITBexsgq2NI','title':'How To Craft Your League Starter Weapon For CHEAP In POE2 0.5.5!','channel':'XTheFarmerX'},
 'title':K('번개 주문 +5 + 추가 피해 획득 옵션 2개 + 주문 피해 (리그 초반 가성비)','+5 lightning spells + two extra-damage gains + spell damage (league-start budget)'),
 'start':{'rar':'magic','mods':[{'gi':fw_xF,'tmax':2},{'gi':fw_l5,'tmax':1}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'}],
 'nodes':[
  {'id':'w1','phase':'base','do':'base','cost':'base','ts':'11:03','note':K('모든 번개 주문 스킬 레벨 +5 + 좋은 피해 접두(영상은 추가 화염 피해 획득)가 붙은 매직 지팡이. 베이스 종류는 상관없음.','A magic staff with +5 to all lightning spell skills and a good damage prefix (extra fire damage gain in the video). Any staff base.')},
  {'id':'w2','phase':'pre','do':'essence','cur':'Greater_Essence_of_Sorcery','target':{'gi':fw_spellE},'ts':'12:20'},
  {'id':'w3','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'14:14'},
  {'id':'w4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':fw_xC},{'gi':fw_xL},{'gi':fw_xCh}]},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'w3','via':LIGHT},'ts':'14:30'},
  {'id':'w5','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'15:20',
   'br':K('시전 속도·치명타가 뜨면 대박. 꽝이어도 완성.','Cast speed or crit is the jackpot; a miss still finishes it.')},
 ]})
