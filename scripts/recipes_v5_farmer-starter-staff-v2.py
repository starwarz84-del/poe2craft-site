# ---- XTheFarmerX league-start staff (youtu.be/ITBexsgq2NI) — grade recipes (policy 25) from scripts/graphs/farmer-starter-staff-v2.json ----
# Rewrites 'farmer-starter-staff' (REPLACES). Video steps. The video base is item level 73 (extra damage T1 needs 80): High-end buys an 80+ staff.
# Essential = video (Preserved Jawbone, any tier); Balance / High-end use an Ancient Jawbone (only level 40+ tiers) for T1–2 / T1.
c='Staves'
def _fw(t, sec, side=None):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]: return gi
    raise Exception(t)
fw2_l5=_fw('+(5—6) to Level of all Lightning Spell Skills','n','s')
fw2_xF=_fw('Extra Fire Damage','n','p'); fw2_xC=_fw('Extra Cold Damage','n','p'); fw2_xL=_fw('Extra Lightning Damage','n','p')
fw2_xCh=_fw('Extra Chaos Damage','d','p'); fw2_spellE=_fw('increased Spell Damage','e','p')
def fm_staff(tier):
    hi=tier=='high'; rid='farmer-starter-staff-v2'+('' if hi else '-'+tier)
    ft={'high':1,'bal':2,'ess':2}[tier]; rv={'high':1,'bal':2,'ess':9}[tier]; bone='Preserved_Jawbone' if tier=='ess' else 'Ancient_Jawbone'
    R.append({
 'id':rid,'tierGroup':'farmer-starter-staff-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Sanctified Staff'),'ilvl':80 if hi else 73,'difficulty':1,'budget':'low',
 'buildTags':[K('번개','Lightning'),K('주문','Spell'),K('리그 초반','League start'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':K('XTheFarmerX 영상 기반','Based on XTheFarmerX'),
 'source':{'url':'https://www.youtube.com/watch?v=ITBexsgq2NI','title':'How To Craft Your League Starter Weapon For CHEAP In POE2 0.5.5!','channel':'XTheFarmerX'},
 'title':K('번개 주문 +5 + 추가 피해 획득 2줄 + 주문 피해 (리그 초반 가성비)','+5 lightning spells + two extra-damage gains + spell damage (league-start budget)'),
 'start':{'rar':'magic','mods':[{'gi':fw2_xF,'tmax':ft},{'gi':fw2_l5,'tmax':1}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'},{'id':'suf','kr':'접미 두번째·세번째 옵션','en':'Suffix options 2–3'}],
 'nodes':[
  {'id':'w1','phase':'base','do':'base','cost':'base','ts':'11:03','note':K('모든 번개 주문 스킬 레벨 +5 + 추가 화염 피해 획득 매직 지팡이. 베이스 종류는 상관없음.','A magic staff with +5 to all lightning spell skills and extra fire damage gain. Any staff base.')},
  {'id':'w2','phase':'base','do':'essence','cur':'Greater_Essence_of_Sorcery','target':{'gi':fw2_spellE},'ts':'12:20'},
  {'id':'w3','phase':'pre','do':'desecrate','cur':bone,'omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'14:14'},
  {'id':'w4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[dict({'gi':g},**({'tmax':rv} if rv<9 else {})) for g in (fw2_xC,fw2_xL)]+[{'gi':fw2_xCh}]},'side':'p','bone':bone},'fail':{'goto':'w3','via':LIGHT},'ts':'14:30'},
  {'id':'w5','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'15:20',
   'br':K('시전 속도·치명타가 뜨면 대박. 꽝이어도 완성.','Cast speed or crit is the jackpot; a miss still finishes it.')},
 ]})
for _t in ('high','bal','ess'): fm_staff(_t)
