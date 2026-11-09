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
R.append({
 'id':'diztoh-crit-helmet-v2','cls':c,'base':base(c,'Grinning Mask'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high',
 'buildTags':[K('치명타','Crit'),K('회피','Evasion'),K('에너지 보호막','Energy Shield'),K('몽크','Monk')],'patch':'0.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=QuW8BOSpPpo','title':'How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5','channel':'Diztoh'},
 'title':K('웃는 가면 | 회피·에너지 보호막 + 치명타 확률·치명타 피해 보너스','Grinning Mask | evasion/ES + crit chance and crit damage bonus'),
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'mag','kr':'매직 만들기','en':'Make it magic'},{'id':'fr','kr':'분열','en':'Fracture'},
           {'id':'crit','kr':'접미 치명타 확률','en':'Crit chance suffix'},{'id':'pre','kr':'접두 완성','en':'Finish the prefixes'},
           {'id':'des','kr':'치명타 피해 훼손','en':'Crit damage desecration'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  # --- base preparation (cut into r.prep by FRSTART) ---
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('특출난 웃는 가면(소켓 2개), 약 8 카오스 오브. 퀄리티 20%.','An exceptional Grinning Mask (two sockets), about 8 Chaos Orbs. Quality 20%.')},
  {'id':'h2','phase':'mag','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN},'ts':'0:46',
   'br':K('접두 회피·에너지 보호막 % 또는 접미 치명타 확률·아이템 희귀도 1티어 → 확장','% evasion/ES prefix, or T1 crit chance / rarity suffix → augment')},
  {'id':'h3','phase':'mag','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':HC_MAGIC},'fail':{'goto':'self','via':HC_ANN,'lost':'h2'},'ts':'1:30',
   'br':K('실패: 소멸의 오브 → 잡옵이 지워지면 다시 확장, 필수 줄이 지워지면 소멸의 오브 한 번 더 → 진화부터','Miss: Annulment → junk gone: augment again; wanted line gone: one more Annulment, back to transmute')},
  {'id':'h4','phase':'mag','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'1:30'},
  {'id':'h5','phase':'fr','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'1:30'},
  {'id':'h6','phase':'fr','do':'divine','cur':'Divine_Orb','label':K('신성한 오브로 수치 올리기','Divine the rolls up'),'ts':'1:30'},
  {'id':'h7','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':HC_MAGIC},'fail':{'goto':'restart'},'extra':{'Orb_of_Annulment':2},
   'after':{'keepOnly':[hc_pct,'junk1']},'ts':'2:15',
   'br':K('필수 줄 분열 → 소멸의 오브 2개로 분열 줄 + 잡옵 1줄 / 잡옵 분열 → 베이스 구입부터','Wanted line fractured → two Annulments to the fracture + one junk / junk fractured → buy a new base')},
  # --- main path: fractured % evasion/ES + one junk line ---
  {'id':'c1','phase':'crit','do':'chaos','cur':'Chaos_Orb','target':{'gi':hc_crit,'tmax':2},'fail':{'goto':'self'},'ts':'3:02'},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':HC_P1[0],
   'fail':{'goto':'self','via':HC_ANN,'lost':'c1'},'ts':'3:46',
   'br':K('치명타 확률 1티어면 완벽한 엑잘티드 오브. 접두 아이템 희귀도 1~2티어 → 두고 한 번 더. 실패: 소멸의 오브(치명타 확률이 지워지면 {#c1}번부터)',
          'T1 crit chance: use a Perfect Exalt. T1–2 prefix rarity → keep it and slam once more. Miss: Annulment (crit chance gone: back to step {#c1})')},
  {'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':HC_P2},'ts':'9:02',
   'br':K('필수 → {#d1}번 / 실패 → 타협: 그대로 {#d1}번 (더 노리려면 {#p3}번, 선택)','Wanted → step {#d1} / miss → settle: go on to step {#d1} (step {#p3} is optional)')},
  {'id':'p3','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'fallbackFor':'p2','optional':True,'target':{'anyOf':HC_P2,'replace':'p','whittle':0.5},
   'fail':{'goto':'self','lost':'p1'},'ts':'9:02',
   'br':K('회피·ES 최대치 1티어(레벨 54)가 잡옵보다 낮은 경우가 대부분이라 좌측 말소의 징조(1/2). 잡옵이 더 낮으면 절사의 징조. 최대치 줄이 지워지면 소멸의 오브 → {#p1}번부터',
          'T1 flat evasion/ES (level 54) is usually lower than the junk, so Sinistral Erasure (1/2); if the junk is lower, Whittling. Flat line gone → Annulment, back to step {#p1}')},
  {'id':'d1','phase':'des','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'9:46'},
  {'id':'d2','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':hc_cdmg},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'d1','via':HC_LIGHT},'ts':'10:31'},
  {'id':'f1','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'11:15',
   'br':K('마지막 접미는 나오는 대로(저항·아이템 희귀도면 최고)','Last suffix as it comes (resistance or rarity is best)')},
  {'id':'f2','phase':'fin','do':'divine','cur':'Divine_Orb','label':K('신성한 오브로 수치 조정','Divine the rolls'),'ts':'12:00'},
  {'id':'f3','phase':'fin','do':'note','ts':'12:00','note':K('완성. 룬 소켓 2개는 비워 둠(취향껏).','Done. Both rune sockets are left empty (your choice).')},
 ]})
