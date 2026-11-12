# ---- Diztoh "How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5" (youtu.be/QuW8BOSpPpo) ----
# Rewrites the older batch2 recipe 'diztoh-crit-helmet' (REPLACES in build_recipes.py).
# 2026-11-12 whole-video screen check (W5 + W8, evidence/diztoh-crit-helmet-v2), user confirmed the same day:
# the fractured line is the FLAT evasion + flat ES prefix (T1, +79-94 / +26-29), not the % line.
# Prep (FRSTART cuts h2..h7 into the folded "base preparation"): exceptional Grinning Mask -> Perfect Transmutation (0:49 tooltip)
# + Perfect Augmentation / Annulment until magic flat T1 + rarity (or crit) T1 -> Perfect Regal -> Preserved Rib (2:07 tooltip)
# + Dextral Necromancy -> divines -> fracture (flat line) -> annul down to the fracture + one junk line.
# Main: A crit suffix (chaos) -> B = % evasion/ES or the %+life/mana hybrid, whichever lands first (7:28 % T1)
# -> C = the other one (9:40 hybrid mana T1). High-end reworks a C miss with Sinistral Erasure + Greater Chaos (8:26-9:27).
# -> Ancient Rib desecration + Abyssal Echoes reveal, Light + annul to redo (10:03-11:25) -> last suffix Perfect Exalt as it comes (11:57).
# Runes: the video sockets a chaos resistance rune only after the craft (17:44), no crafting effect, so both sockets stay empty (policy 9).
DZ5=K('Diztoh 영상 기반','Based on Diztoh')
c='Helmets_dex_int'
def textH(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
hc_pct=textH('(92—100)% increased Evasion and Energy Shield','n','p')                 # B or C: % evasion/ES
hc_flat=textH('to Evasion Rating\n+(26—29) to maximum Energy Shield','n','p')         # fractured T1 flat evasion + ES (video 1:29, 2:51)
hc_life=textH('increased Evasion and Energy Shield\n+(42—49) to maximum Life','n','p')
hc_mana=textH('increased Evasion and Energy Shield\n+(33—39) to maximum Mana','n','p')
hc_crit=textH('increased Critical Hit Chance','n','s')
hc_rarS=textH('increased Rarity of Items found','n','s')
hc_cdmg=textH('Critical Damage Bonus','d','s')
HC_MAGIC=[{'gi':hc_flat,'tmax':1},{'gi':hc_crit,'tmax':1},{'gi':hc_rarS,'tmax':1}]   # video: flat T1 (1:29) + rarity T1 (1:41)
# B = whichever of % / hybrid lands first, C = the other one. The step text follows the video order (B % at 7:28, C hybrid mana at 9:40);
# the engine pushes the first listed line, so C is listed as the hybrid.
def hc_B(t): return [{'gi':hc_pct,'tmax':t},{'gi':hc_life,'tmax':t},{'gi':hc_mana,'tmax':t}]
def hc_C(t): return [{'gi':hc_life,'tmax':t},{'gi':hc_mana,'tmax':t}]
hc_fire=textH('to Fire Resistance','n','s')
hc_chaosR=textH('to Chaos Resistance','n','s')
HC_LAST=[{'gi':hc_rarS,'tmax':1},{'gi':hc_fire,'tmax':1},{'gi':hc_chaosR,'tmax':1}]   # graph tag lastS
HC_ANN={'cur':'Orb_of_Annulment','side':'any'}        # a plain annul: any non-fractured line on either side
HC_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
# One recipe per grade, written from the flowchart (scripts/graphs/diztoh-crit-helmet-v2.json, policies C17, difficulty 4 -> high + bal):
#   high-end  = crit T1, B and C T1, a C miss -> Sinistral Erasure + Greater Chaos loop
#   balance   = crit T1-2, B T1-2, C aimed once then settled (random option) -- the video's own finished item (B % T2 at 9:30)
#   essential = kept for the data, not shown (difficulty 4)
def crit_helmet(tier):
    hi, ess = tier=='high', tier=='ess'
    rid = 'diztoh-crit-helmet-v2' + ('' if hi else '-'+tier)
    T={'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier]
    crit={'gi':hc_crit,'tmax':1 if hi else 2}
    bT=1 if hi else 2 if tier=='bal' else 4
    nodes=[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('소켓 2개짜리 특출난 웃는 가면, 약 8 카오스 오브. 퀄리티 20%.','An exceptional Grinning Mask with two sockets, about 8 Chaos Orbs. Quality 20%.')},
  {'id':'h2','phase':'mag','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN},'ts':'0:50'},
  {'id':'h3','phase':'mag','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN,'lost':'h2'},'ts':'0:58'},
  {'id':'h4','phase':'mag','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'1:47'},
  {'id':'h5','phase':'fr','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'2:07'},
  {'id':'h7','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':HC_MAGIC},'fail':{'goto':'restart'},'extra':{'Orb_of_Annulment':2},
   'after':{'keepOnly':[hc_flat,'junk1']},'ts':'2:51'},
  {'id':'c1','phase':'crit','do':'chaos','cur':'Chaos_Orb','target':crit,'fail':{'goto':'self'},'ts':'3:10'},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb' if hi else 'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':hc_B(bT)},
   'fail':{'goto':'self','via':HC_ANN,'lost':'c1'},'ts':'7:28'},
    ]
    if ess:
        nodes.append({'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'9:37'})
    else:
        nodes.append({'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':hc_C(bT)},'ts':'9:37',
                      **({'fail':{'goto':'p3'}} if hi else {'compromise':{'fail':{'goto':'self'}}})})
        if hi:   # video 8:26-9:27: Sinistral Erasure + Greater Chaos; the % line was hit, so annul the new line and exalt B again
            nodes.append({'id':'p3','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'fallbackFor':'p2','target':{'anyOf':hc_C(1),'replace':'p'},
                          'fail':{'goto':'self','lost':'p1'},'ts':'9:09'})
    nodes+=[
  {'id':'d1','phase':'des','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'9:49'},
  {'id':'d2','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':hc_cdmg},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'d1','via':HC_LIGHT},'ts':'10:28'},
    ]
    if hi:   # policies C17: only the high-end gambles a junk last suffix (graph f2); the video keeps what comes (fire resistance T2)
        nodes.append({'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':HC_LAST},'fail':{'goto':'f2'},'ts':'11:57'})
        nodes.append({'id':'f2','phase':'fin','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'f1','target':{'anyOf':HC_LAST,'replace':'s'},'fail':{'goto':'self'},'ts':'11:57'})
    else:
        nodes.append({'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'11:57'})
    nodes.append({'id':'f3','phase':'fin','do':'note','ts':'12:05','note':K('완성. 영상은 제작이 끝난 뒤 룬 소켓에 카오스 저항 룬을 박지만 제작에는 영향이 없어 비워 둠.',
        'Done. The video socketed a chaos resistance rune after the craft; it does not affect crafting, so both sockets stay empty here.')})
    R.append({
 'id':rid,'tierGroup':'diztoh-crit-helmet-v2','tier':tier,'cls':c,'base':base(c,'Grinning Mask'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high',
 'buildTags':[K('치명타','Crit'),K('회피','Evasion'),K('에너지 보호막','Energy Shield'),K('몽크','Monk')],'patch':'0.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=QuW8BOSpPpo','title':'How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5','channel':'Diztoh'},
 'title':K('회피·에너지 보호막 + 치명타 확률·치명타 피해 보너스','evasion/ES + crit chance and crit damage bonus'),
 'tierLabel':T,
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'mag','kr':'매직 만들기','en':'Make it magic'},{'id':'fr','kr':'분열','en':'Fracture'},
           {'id':'crit','kr':'접미 첫번째 옵션','en':'First suffix option'},{'id':'pre','kr':'접두 두번째·세번째 옵션','en':'Second and third prefix options'},
           {'id':'des','kr':'접미 두번째 옵션(훼손)','en':'Second suffix option (desecrated)'},{'id':'fin','kr':'접미 세번째 옵션','en':'Third suffix option'}],
 'nodes':nodes})
for _t in ('high','bal','ess'): crit_helmet(_t)
