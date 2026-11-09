# ---- Diztoh "I Crafted Gold Rings to Increase my Item Rarity | Path of Exile 2 0.5.5" (youtu.be/GDLDxn6yxEs) — grade recipes (policy 25) ----
# Rewrites 'diztoh-rarity-ring' (REPLACES) from the flowchart scripts/graphs/diztoh-rarity-ring-v2.json. Same steps as the video;
# the grades differ only in the all-resistance tier kept from the desecration (high T1–2, balance T1–3, essential any — the video kept T4).
c='Rings'
def _rr(t, sec, side=None, multi=False):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5] and (not multi or len(gr['t'])>1): return gi
    raise Exception(t)
rr_rarP=_rr('increased Rarity of Items found','n','p'); rr_cres=_rr('to Cold Resistance','n','s'); rr_rarE=_rr('increased Rarity of Items found','e','s')
rr_allres=_rr('to all Elemental Resistances','n','s'); rr_catk=_rr('Cold damage to Attacks','n','p',True); rr_cpct=_rr('increased Cold Damage','n','p'); rr_patk=_rr('Physical Damage to Attacks','n','p',True)
def dz_ring(tier):
    hi=tier=='high'; rid='diztoh-rarity-ring-v2'+('' if hi else '-'+tier); at={'high':2,'bal':3,'ess':5}[tier]
    R.append({
 'id':rid,'tierGroup':'diztoh-rarity-ring-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Gold Ring'),'ilvl':81,'difficulty':2,'budget':'low',
 'buildTags':[K('아이템 희귀도','Item rarity'),K('냉기','Cold'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':K('Diztoh 영상 기반','Based on Diztoh'),
 'source':{'url':'https://www.youtube.com/watch?v=GDLDxn6yxEs','title':'I Crafted Gold Rings to Increase my Item Rarity | Path of Exile 2 0.5.5','channel':'Diztoh'},
 'title':K('희귀도 2줄 + 냉기 저항 + 모든 원소 저항','double rarity + cold res + all resistances'),
 'start':{'rar':'magic','mods':[{'gi':rr_rarP,'tmax':3},{'gi':rr_cres,'tmax':2}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 세번째 옵션(훼손)','en':'Third suffix (desecrated)'},{'id':'pre','kr':'접두 두번째·세번째 옵션','en':'Prefix options 2–3'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'1:00','note':K('접두 희귀도 + 접미 냉기 저항 매직 황금 반지.','A magic Gold Ring with prefix rarity and suffix cold resistance.')},
  {'id':'g2','phase':'base','do':'essence','cur':'Greater_Essence_of_Opulence','target':{'gi':rr_rarE},'ts':'1:20'},
  {'id':'g3','phase':'suf','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'2:20'},
  {'id':'g4','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':rr_allres,'tmax':at},'side':'s','bone':'Preserved_Collarbone'},'fail':{'goto':'g3','via':LIGHT},'ts':'3:20'},
  {'id':'g5','phase':'pre','do':'quality','cur':'Tuls_Catalyst','target':{'quality':20},'ts':'4:20'},
  {'id':'g6','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Greater_Exaltation'],'target':{'anyOf':[{'gi':rr_catk},{'gi':rr_cpct},{'gi':rr_patk}]},'knownP':1,'ts':'4:40',
   'br':K('결과는 그대로 받아들임','Keep whatever comes')},
  {'id':'g7','phase':'pre','do':'note','ts':'5:40','note':K('완성.','Done.')}]})
for _t in ('high','bal','ess'): dz_ring(_t)
