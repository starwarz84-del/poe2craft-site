# ---- Belton "How to Craft an Early League End Game +8 Wand For Under 100d | PoE 2 0.5.5" (youtu.be/j0FeuX0NZQI) ----
BT5=K('Belton 영상 기반','Based on Belton')
c='Wands'
def textB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
bt_l4=textB('+4 to Level of all Spell Skills','n','s')
bt_spell=textB('(105—119)% increased Spell Damage','n','p'); bt_hyb=textB('increased Spell Damage\n+','n','p')
bt_xF=textB('Extra Fire Damage','n','p'); bt_xC=textB('Extra Cold Damage','n','p'); bt_xL=textB('Extra Lightning Damage','n','p')
bt_regen=textB('(60—69)% increased Mana Regeneration Rate','n','s'); bt_scrit=textB('increased Critical Hit Chance for Spells','n','s'); bt_cdmg=textB('increased Critical Spell Damage Bonus','n','s')
bt_ele=textB('increased Elemental Damage','d','p')
bt_trans=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Transcendent Alloy' in [x[3] for x in gr['t']]][0]
bt_cel=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Celestial Alloy' in [x[3] for x in gr['t']]][0]
BT_PRE=[{'gi':bt_xF,'tmax':2},{'gi':bt_xC,'tmax':2},{'gi':bt_xL,'tmax':2},{'gi':bt_spell,'tmax':3},{'gi':bt_hyb,'tmax':1}]
BT_SUF=[{'gi':bt_regen,'tmax':1},{'gi':bt_scrit,'tmax':2},{'gi':bt_cdmg,'tmax':2}]
BT_ANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}
BT_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
BT_ASTRID=K('아스트리드의 창의성',"Astrid's Creativity")
R.append({
 'id':'belton-plus8-wand','cls':c,'base':base(c,'Dueling Wand'),'ilvl':82,'difficulty':3,'budget':'medium',
 'buildTags':[K('주문','Spell'),K('시전 속도','Cast speed'),K('추가 피해','Extra damage')],'patch':'0.5.5','created':'2026-11-09','author':BT5,
 'source':{'url':'https://www.youtube.com/watch?v=j0FeuX0NZQI','title':'How to Craft an Early League End Game +8 Wand For Under 100d | PoE 2 0.5.5','channel':'Belton'},
 'title':K('초월의 합금 분열 + 모든 주문 +4 + 천공의 합금','fractured Transcendent Alloy + all spells +4 + Celestial Alloy'),
 'start':{'rar':'rare','quality':21,'runes':[BT_ASTRID],
          'mods':[{'gi':bt_l4,'tmax':1},{'gi':bt_trans,'fr':True,'crafted':True},{'gi':bt_cel,'crafted':True},{'unrev':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두 막기 · 추가 피해','en':'Block and extra damage'},{'id':'suf','kr':'접미 훼손','en':'Suffix desecration'},{'id':'fin','kr':'마지막 접두','en':'Last prefix'}],
 'nodes':[
  {'id':'b1','phase':'base','do':'base','cost':'base','ts':'1:54',
   'note':K('퀄리티 21%. 아스트리드의 창의성 장착 상태로 초월의 합금(시전 속도) 분열 + 모든 주문 +4 + 천공의 합금 + 미공개 훼손 접두(군왕의 징조).',"21% quality. Astrid's Creativity socketed: fractured Transcendent Alloy (cast speed), all spells +4, Celestial Alloy and an unrevealed desecrated prefix (Omen of the Liege).")},
  {'id':'b2','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':bt_ele},'side':'p','lord':'amanamu','bone':'Preserved_Jawbone'},'fail':{'goto':'self','via':BT_LIGHT},'ts':'2:49',
   'br':K('원소 피해 % 증가로 화염·냉기·번개 % 계열을 막아 둠(나중에 지움).','Elemental damage blocks the fire, cold and lightning % families (removed later).')},
  {'id':'b3','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':BT_PRE},'fail':{'goto':'self','via':BT_ANN},'ts':'3:49',
   'br':K('실패: 좌측 소멸의 징조 + 소멸의 오브. 천공의 합금이 지워지면 좌측 결정화의 징조 + 천공의 합금으로 다시.','Miss: Sinistral Annulment + Annulment; if the Celestial Alloy goes, Sinistral Crystallisation + Celestial Alloy again.')},
  {'id':'b4','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'4:45'},
  {'id':'b5','phase':'suf','do':'desecrate','cur':'Ancient_Jawbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'5:21'},
  {'id':'b6','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':BT_SUF},'side':'s','bone':'Ancient_Jawbone'},'fail':{'goto':'b5','via':BT_LIGHT},'ts':'5:39'},
  {'id':'b7','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':BT_PRE},'fail':{'goto':'self','via':BT_ANN,'lost':'b3'},'ts':'6:25',
   'br':K('카오스·물리 피해 % 등이 뜨면 타협 가능(영상: 카오스 피해 3티어로 마무리).','Chaos or physical % damage can be kept for now (the video settled on tier 3 chaos damage).')},
 ]})
