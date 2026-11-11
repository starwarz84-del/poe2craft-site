# ---- Zen_M "[PoE 2] How To Profit Craft Time-Lost Jewels In Path Of Exile 2" (youtu.be/IKC9DquM7GM) ----
ZM5=K('Zen_M 영상 기반','Based on Zen_M')
c='Time-Lost_Sapphire'
def textZ(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
zm_cc=textZ('(3—7)% increased Critical Hit Chance','n','s'); zm_cd=textZ('(5—10)% increased Critical Damage Bonus','n','s')
zm_scc=textZ('increased Critical Hit Chance for Spell','n','s'); zm_scd=textZ('increased Critical Spell Damage Bonus','n','s')
zm_mcc=textZ('Minions have (5—10)% increased Critical Hit Ch','n','s'); zm_mcd=textZ('Minions have (6—12)% increased Critical Damage','n','s')
zm_mel=textZ('Upgrades Radius to Very Large','x','p')
assert 'Spell' not in cd(c)['groups'][zm_cc]['t'][0][5] and 'Minion' not in cd(c)['groups'][zm_cc]['t'][0][5]
ZM_SUF=[{'gi':zm_scd},{'gi':zm_cd},{'gi':zm_scc},{'gi':zm_cc},{'gi':zm_mcc},{'gi':zm_mcd}]
R.append({
 'id':'zenm-timelost-sapphire','cls':c,'base':0,'ilvl':41,'cap':{'p':2,'s':2},'difficulty':2,'budget':'low','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('오래된 주얼','Time-Lost jewel'),K('치명타','Crit'),K('수익 제작','Profit craft')],'patch':'0.5','created':'2026-11-09','author':ZM5,
 'source':{'url':'https://www.youtube.com/watch?v=IKC9DquM7GM','title':'[PoE 2] How To Profit Craft Time-Lost Jewels In Path Of Exile 2','channel':'Zen_M'},
 'title':K('치명타 접미 옵션 2개 + 매우 넓은 반경 (수익 제작)','two crit suffixes + Very Large radius (profit craft)'),
 'start':{'rar':'magic','mods':[{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'치명타 접미 옵션 2개','en':'Two crit suffixes'},{'id':'pre','kr':'접두 · 우울','en':'Prefixes and Melancholy'}],
 'nodes':[
  {'id':'z1','phase':'base','do':'base','cost':'base','ts':'1:57',
   'note':K('옵션 1개짜리 싼 매직 오래된 사파이어(영상 아이템 레벨 41). 여러 개를 한꺼번에.','Cheap one-mod magic Time-Lost Sapphires (item level 41 in the video), several at once.')},
  {'id':'z2','phase':'base','do':'regal','cur':'Regal_Orb','target':{'junk':'p'},'after':{'keepOnly':['junk1']},'ts':'2:20',
   'note':K('레어로 만든 뒤 소멸의 오브로 옵션 1개만 남김.','Regal, then annul down to one line.')},
  {'id':'z3','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':ZM_SUF},'fail':{'goto':'self'},'ts':'2:40',
   'br':K('수치가 최소치면 다시 굴림','Reroll a minimum roll')},
  {'id':'z4','phase':'suf','do':'desecrate','cur':'Preserved_Cranium','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'4:20'},
  {'id':'z5','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':ZM_SUF},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'z4','via':{'cur':'Orb_of_Annulment'},'lost':'z3'},'ts':'4:42',
   'br':K('실패: 소멸의 오브(1/2로 훼손 옵션), 치명타 옵션이 지워지면 카오스 오브부터','Miss: Annulment (1 in 2 takes the desecrated line); if the crit line goes, chaos again')},
  {'id':'z6','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p','count':2},'ts':'9:15',
   'br':K('중형 반경이 뜨면 소멸의 오브, 치명타 옵션이 지워지면 카오스 오브부터 / 대형 반경은 그대로 판매','Medium radius → Annulment (if a crit line goes, chaos again) / Large radius: sell as is')},
  {'id':'z7','phase':'pre','do':'essence','cur':'Ancient_Potent_Liquid_Melancholy','knownP':True,'target':{'gi':zm_mel},'ts':'9:43',
   'note':K('접두가 꽉 차 있어 접두 하나가 지워짐. 완성.','Prefixes are full, so a prefix is replaced. Done.')},
 ]})
