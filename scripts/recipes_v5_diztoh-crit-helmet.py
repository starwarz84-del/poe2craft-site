# ---- Diztoh "How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5" (youtu.be/QuW8BOSpPpo) ----
# Rewrites the older batch2 recipe 'diztoh-crit-helmet' (REPLACES in build_recipes.py) from the flow the user wrote out
# (사용자 확정 2026-11-09: the user's flow is the answer, no video re-check; ts reuse the old recipe's values).
# Prep (FRSTART cuts h2..h7 into the folded "base preparation"): exceptional Grinning Mask -> magic % eva/ES T1 + crit T1 or
# rarity T1 -> regal -> dextral desecration -> divine -> fracture (2/3) -> annul to fracture + one junk line.
# Main (policy 23 ③, prefix fractured): suffix crit (chaos) -> prefixes done -> suffix desecration -> last suffix as it comes.
# Runes: none affect the craft, so both sockets stay empty (policy 23 ①). No Raven's Touch, no Vaal infuser.
DZ5=K('Diztoh 영상 기반','Based on Diztoh')
c='Helmets_dex_int'
def textH(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
hc_pct=textH('(92—100)% increased Evasion and Energy Shield','n','p')                 # fractured T1 % evasion/ES (level 65)
hc_flat=textH('to Evasion Rating\n+(26—29) to maximum Energy Shield','n','p')         # flat evasion + ES
hc_life=textH('increased Evasion and Energy Shield\n+(42—49) to maximum Life','n','p')
hc_mana=textH('increased Evasion and Energy Shield\n+(33—39) to maximum Mana','n','p')
hc_crit=textH('increased Critical Hit Chance','n','s')
hc_rarS=textH('increased Rarity of Items found','n','s')
hc_cdmg=textH('Critical Damage Bonus','d','s')
HC_MAGIC=[{'gi':hc_pct,'tmax':1},{'gi':hc_crit,'tmax':1},{'gi':hc_rarS,'tmax':1}]
HC_P1=[{'gi':hc_flat,'tmax':1}]                                   # 사용자 확정 2026-11-09 17:36: 접두 1번째 = 회피·ES 최대치 1티어
HC_P2=[{'gi':hc_life,'tmax':3},{'gi':hc_mana,'tmax':3}]            # 접두 2번째 = %+생명력/마나 복합 1~3티어(타협)
HC_ANN={'cur':'Orb_of_Annulment','side':'any'}        # a plain annul: any non-fractured line on either side
HC_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
# 사용자 확정 2026-11-09 23:35: one recipe per grade, written from the flowchart (scripts/graphs/diztoh-crit-helmet-v2.json):
# high-end first, then balance and essential as the compromises. The recipe tab shows them as tabs (+ the flowchart tab).
#   high-end  = crit T1, flat T1, hybrid T1 (9 misses → 9.A rework), rarity T1 as the last suffix (estimated finish, see f1b)
#   balance   = crit T1–2, flat T1, hybrid T1–3 (9 misses → settle), last suffix random
#   essential = crit T1–2, flat T1–2, third prefix random, last suffix random
HC_WHITTLE=['Omen_of_Whittling']
def crit_helmet(tier):
    hi, ess = tier=='high', tier=='ess'
    rid = 'diztoh-crit-helmet-v2' + ('' if hi else '-'+tier)
    T={'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier]
    crit={'gi':hc_crit,'tmax':1 if hi else 2}
    flat={'gi':hc_flat,'tmax':2 if ess else 1}
    hyb=[{'gi':hc_life,'tmax':1 if hi else 3},{'gi':hc_mana,'tmax':1 if hi else 3}]
    nodes=[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('특출난 웃는 가면(소켓 2개), 약 8 카오스 오브. 퀄리티 20%.','An exceptional Grinning Mask (two sockets), about 8 Chaos Orbs. Quality 20%.')},
  {'id':'h2','phase':'mag','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN},'ts':'0:46'},
  {'id':'h3','phase':'mag','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN,'lost':'h2'},'ts':'1:30'},
  {'id':'h4','phase':'mag','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'1:30'},
  {'id':'h5','phase':'fr','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'1:30'},
  {'id':'h7','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':HC_MAGIC},'fail':{'goto':'restart'},'extra':{'Orb_of_Annulment':2},
   'after':{'keepOnly':[hc_pct,'junk1']},'ts':'2:15'},
  {'id':'c1','phase':'crit','do':'chaos','cur':'Chaos_Orb','target':crit,'fail':{'goto':'self'},'ts':'3:02'},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb' if hi else 'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':flat,
   'fail':{'goto':'self','via':HC_ANN,'lost':'c1'},'ts':'3:46'},
    ]
    if ess:
        nodes.append({'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'9:02'})
    else:
        nodes.append({'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':hyb},'ts':'9:02',
                      **({'fail':{'goto':'p3'}} if hi else {'compromise':{'fail':{'goto':'self'}}})})
        if hi:
            nodes.append({'id':'p3','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'p2','target':{'anyOf':hyb,'replace':'p','whittle':0.5},
                          'fail':{'goto':'self','lost':'p1'},'ts':'9:02'})
    nodes+=[
  {'id':'d1','phase':'des','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'9:46'},
  {'id':'d2','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':hc_cdmg},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'d1','via':HC_LIGHT},'ts':'10:31'},
    ]
    if hi:
        nodes+=[
  {'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'gi':hc_rarS,'tmax':1},'ts':'11:15'},
  {'id':'f1b','phase':'fin','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'f1','target':{'gi':hc_rarS,'tmax':1,'replace':'s','whittle':0.7},
   'fail':{'goto':'self','lost':'c1'},'ts':'11:15'}]
    else:
        nodes.append({'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'11:15'})
    nodes.append({'id':'f3','phase':'fin','do':'note','ts':'12:00','note':K('완성. 룬 소켓 2개는 비워 둠(취향껏).','Done. Both rune sockets are left empty (your choice).')})
    R.append({
 'id':rid,'tierGroup':'diztoh-crit-helmet-v2','tier':tier,'cls':c,'base':base(c,'Grinning Mask'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high',
 'buildTags':[K('치명타','Crit'),K('회피','Evasion'),K('에너지 보호막','Energy Shield'),K('몽크','Monk')],'patch':'0.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=QuW8BOSpPpo','title':'How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5','channel':'Diztoh'},
 'title':K('웃는 가면 | 회피·에너지 보호막 + 치명타 확률·치명타 피해 보너스','Grinning Mask | evasion/ES + crit chance and crit damage bonus'),
 'tierLabel':T,
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'mag','kr':'매직 만들기','en':'Make it magic'},{'id':'fr','kr':'분열','en':'Fracture'},
           {'id':'crit','kr':'접미 첫번째 옵션','en':'First suffix option'},{'id':'pre','kr':'접두 두번째·세번째 옵션','en':'Second and third prefix options'},
           {'id':'des','kr':'접미 두번째 옵션(훼손)','en':'Second suffix option (desecrated)'},{'id':'fin','kr':'접미 세번째 옵션','en':'Third suffix option'}],
 'nodes':nodes})
for _t in ('high','bal','ess'): crit_helmet(_t)
