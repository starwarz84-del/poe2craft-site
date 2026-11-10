# ---- Diztoh "How to Craft a Budget Two-Handed Mace in PoE 2 - 0.5 | Step-by-Step" (youtu.be/ITbefGq6V18) ----
DZB=K('Diztoh 영상 기반','Based on Diztoh')
c='Two_Hand_Maces'
def textTM(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
tm_hyb=textTM('increased Physical Damage\n+','n','p'); tm_flat=textTM('Adds (23—35) to (39—59) Physical Damage','e','p')
tm_kpct=textTM('15% reduced Attack Speed','d','p'); tm_atk=textTM('+3 to Level of all Attack Skills','e','s')
tm_as=textTM('increased Attack Speed','n','s'); tm_attr=textTM('reduced Attribute Requirements','n','s'); tm_crit=textTM('to Critical Hit Chance','n','s')
TM_SUF=[{'gi':tm_as,'tmax':3},{'gi':tm_attr,'tmax':1},{'gi':tm_crit,'tmax':2}]
TM_ASTRID=K('아스트리드의 창의성',"Astrid's Creativity"); TM_IRON=K('상위 철 룬','Greater Iron Rune')
R.append({
 'id':'diztoh-budget-2h-mace','cls':c,'base':base(c,'Massive Greathammer'),'ilvl':84,'sockets':3,'exceptional':{'sockets':1},'difficulty':2,'budget':'low',
 'buildTags':[K('물리','Physical'),K('공격 스킬','Attack skills'),K('가성비','Budget')],'patch':'0.5','created':'2026-11-09','author':DZB,
 'source':{'url':'https://www.youtube.com/watch?v=ITbefGq6V18','title':'How to Craft a Budget Two-Handed Mace in PoE 2 - 0.5 | Step-by-Step','channel':'Diztoh'},
 'title':K('에센스 옵션 2개(물리 피해 추가 + 공격 스킬 +3) + 쿠르갈 물리','two essence lines (flat physical + attack skills +3) + Kurgal physical'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'매직 · 에센스','en':'Magic and essence'},{'id':'des','kr':'훼손 · 공격 스킬','en':'Desecration and attack skills'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('특출난 노멀 베이스 구매.','Buy an exceptional normal base.')},
  {'id':'g2','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':tm_hyb,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},'ts':'0:20'},
  {'id':'g3','phase':'base','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'0:50'},
  {'id':'g4','phase':'base','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':tm_flat},'ts':'0:52'},
  {'id':'g5','phase':'des','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy','Omen_of_the_Blackblooded'],'target':{'unrev':'p'},'ts':'1:05'},
  {'id':'g6','phase':'des','do':'manual','target':{'rune':TM_ASTRID},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'1:19'},
  {'id':'g7','phase':'des','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':tm_atk},'ts':'1:48'},
  {'id':'g8','phase':'des','do':'reveal','target':{'reveal':{'gi':tm_kpct},'side':'p','lord':'kurgal','bone':'Preserved_Jawbone'},'fail':{'goto':'g5','via':LIGHT},'ts':'2:13'},
  {'id':'g9','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':TM_SUF},'ts':'2:45',
   'br':K('대박 → 완성, 실패: 그대로 완성(영상) / 접미 다시','Hit → done; miss: keep it (video) or redo the suffixes')},
  {'id':'g9b','phase':'suf','do':'note','fallbackFor':'g9','optional':True,'label':K('갈림길: 접미 다시','Fork: redo the suffixes'),'ts':'3:20',
   'note':K('우측 소멸의 징조 + 소멸의 오브로 접미를 하나씩 제거(공격 스킬 +3이 지워지면 우측 결정화의 징조 + 완벽한 전투의 에센스로 다시) → 상위 찬미의 징조 + 엑잘티드 오브로 옵션 2개.',
            'Remove suffixes one at a time with Dextral Annulment + Annulment (if +3 attack skills goes, Dextral Crystallisation + Perfect Essence of Battle again) → Greater Exaltation + Exalted Orb for two lines.')},
  {'id':'g10','phase':'fin','do':'manual','target':{'rune':TM_IRON},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'4:12'},
  {'id':'g11','phase':'fin','do':'manual','target':{'rune':TM_IRON},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'4:12'},
  {'id':'g12','phase':'fin','do':'note','target':{'runeSwap':[TM_ASTRID,TM_IRON]},'ts':'4:12'},
 ]})
