# ---- Diztoh "How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5" (youtu.be/QuW8BOSpPpo) ----
# Rewrites the older batch2 recipe 'diztoh-crit-helmet' (REPLACES in build_recipes.py).
# 2026-11-12 W6 whole-video screen check (scratchpad review/W6-crit-helmet/timeline.md). Success run 7:23-12:03:
# prep: exceptional Grinning Mask (8 chaos, quality 20%) -> Perfect Transmutation (0:55) + Perfect Augmentation / Annulment until
# magic T1 flat evasion/ES (1:29) + T1 rarity (1:41) -> Perfect Regal (1:47) -> Preserved Rib + Dextral Necromancy (2:07) -> divines
# -> fracture = the flat line (2:59) -> two annuls down to the fracture + the unrevealed desecration (3:08).
# main: chaos for T1 crit chance (7:23) -> Perfect Exalt + Sinistral Exaltation: accuracy (junk, 7:29) and % T1 (7:32)
# -> Sinistral Erasure + Greater Chaos (9:09, took the % and put cold res on the suffix) -> annul cold res and accuracy (9:17-9:26)
# -> Perfect Exalt % T2 (9:32, accepted) and %+mana T1 (9:41) -> Ancient Rib + Abyssal Echoes, Light + annul twice -> crit damage (11:25)
# -> Perfect Exalt, last suffix as it comes (fire res, 12:03). The flowchart (scripts/graphs/diztoh-crit-helmet-v2.json) is the source;
# these engine nodes follow the same ids and step order.
# Runes: the video sockets runes only after the craft (17:42+), no crafting effect, so both sockets stay empty (policy 9).
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
HC_MAGIC=[{'gi':hc_flat,'tmax':1},{'gi':hc_rarS,'tmax':1}]   # video: flat T1 (1:29) + rarity T1 (1:41)
hc_fire=textH('to Fire Resistance','n','s')
hc_chaosR=textH('to Chaos Resistance','n','s')
HC_LAST=[{'gi':hc_rarS,'tmax':1},{'gi':hc_fire,'tmax':1},{'gi':hc_chaosR,'tmax':1}]   # graph tag lastS
HC_ANN={'cur':'Orb_of_Annulment','side':'any'}        # a plain annul: any non-fractured line on either side
HC_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
# One recipe per grade, read from the flowchart at build time (policies C17, difficulty 4 -> high + bal):
#   high-end  = % and %+mana T1, a miss -> Sinistral Erasure + Greater Chaos, annul the junk
#   balance   = % and %+mana T1-2 -- the video's own finished item (% T2 at 9:32)
#   both      = crit chance T1 (chaos after the fracture, policy C15)
#   last suffix: high-end T1 rarity / fire / chaos res, rerolled with Whittling + Greater Chaos only while it is the lowest level; balance random (user 2026-11-13)
#   essential = kept for the data, not shown (difficulty 4)
def crit_helmet(tier):
    hi, ess = tier=='high', tier=='ess'
    rid = 'diztoh-crit-helmet-v2' + ('' if hi else '-'+tier)
    T={'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier]
    bT=1 if hi else 2 if tier=='bal' else 4
    PCT={'gi':hc_pct,'tmax':bT}; HYB={'gi':hc_mana,'tmax':bT}
    nodes=[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'0:30','note':K('소켓 2개짜리 특출난 웃는 가면, 약 8 카오스 오브. 퀄리티 20%.','An exceptional Grinning Mask with two sockets, about 8 Chaos Orbs. Quality 20%.')},
  {'id':'h2','phase':'mag','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN},'ts':'0:55'},
  {'id':'h3','phase':'mag','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN,'lost':'h2'},'ts':'0:58'},
  {'id':'h4','phase':'mag','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'1:47'},
  {'id':'h5','phase':'fr','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'2:07'},
  {'id':'h7','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'gi':hc_flat,'tmax':1},'fail':{'goto':'restart'},'extra':{'Orb_of_Annulment':2},
   'after':{'keepOnly':[hc_flat,'junk1']},'ts':'2:51'},
  {'id':'c1','phase':'crit','do':'chaos','cur':'Chaos_Orb','target':{'gi':hc_crit,'tmax':1},'fail':{'goto':'self'},'ts':'7:23'},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':PCT,
   'fail':{'goto':'self','via':HC_ANN,'lost':'c1'},'ts':'7:29'},
  {'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':HYB,'fail':{'goto':'p3'},'ts':'9:41'},
  {'id':'p3','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'fallbackFor':'p2','target':{**HYB,'replace':'p'},
   'fail':{'goto':'self','lost':'p1'},'ts':'9:09'},
  {'id':'d1','phase':'des','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'10:03'},
  {'id':'d2','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':hc_cdmg},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'d1','via':HC_LIGHT},'ts':'10:30'},
    ]
    if hi:   # 사용자 결정 2026-11-13 00:05: 배포판처럼 하이엔드 마지막 접미 = 희귀도·화염·카오스 저항 1티어, 빗나가면 가장 낮은 레벨일 때만 절사 + 상위 카오스
        nodes.append({'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':HC_LAST},'fail':{'goto':'f2'},'ts':'12:00'})
        nodes.append({'id':'f2','phase':'fin','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'f1','target':{'anyOf':HC_LAST,'replace':'s'},'fail':{'goto':'self'}})
    else:
        nodes.append({'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'12:00'})
    nodes+=[
  {'id':'f3','phase':'fin','do':'note','ts':'12:03','note':K('완성. 영상은 제작이 끝난 뒤 공허 유동체·룬으로 저항을 손보지만 제작에는 영향이 없어 비워 둠.',
        'Done. After the craft the video adjusts resistances with a Void Flux and runes; that does not affect crafting, so both sockets stay empty here.')},
    ]
    R.append({
 'id':rid,'tierGroup':'diztoh-crit-helmet-v2','tier':tier,'cls':c,'base':base(c,'Grinning Mask'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high',
 'buildTags':[K('치명타','Crit'),K('회피','Evasion'),K('에너지 보호막','Energy Shield'),K('몽크','Monk')],'patch':'0.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=QuW8BOSpPpo','title':'How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5','channel':'Diztoh'},
 'title':K('회피·에너지 보호막 + 치명타 확률·치명타 피해 보너스','evasion/ES + crit chance and crit damage bonus'),
 'tierLabel':T,
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'mag','kr':'매직 만들기','en':'Make it magic'},{'id':'fr','kr':'분열','en':'Fracture'},
           {'id':'crit','kr':'접미 첫 번째 옵션','en':'First suffix option'},{'id':'pre','kr':'접두 두 번째·세 번째 옵션','en':'Second and third prefix options'},
           {'id':'des','kr':'접미 두 번째 옵션(훼손)','en':'Second suffix option (desecrated)'},{'id':'fin','kr':'접미 세 번째 옵션','en':'Third suffix option'}],
 'nodes':nodes})
for _t in ('high','bal','ess'): crit_helmet(_t)
