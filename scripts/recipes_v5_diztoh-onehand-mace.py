# ---- Diztoh "How to Craft a One-Handed Mace | Double Crafted Mod Tech Explained | PoE 2" (youtu.be/WDEkEIQFgT4) ----
DZM=K('Diztoh 영상 기반','Based on Diztoh')
c='One_Hand_Maces'
def textOM(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
om_crit=textOM('to Critical Hit Chance','n','s'); om_as=textOM('increased Attack Speed','e','s'); om_atk=textOM('+2 to Level of all Attack Skills','e','s')
om_hyb=textOM('increased Physical Damage\n+','n','p'); om_ppct=textOM('(170—179)% increased Physical Damage','n','p'); om_pflat=textOM('Physical Damage','n','p')
om_fire=textOM('Fire Damage','n','p'); om_cold=textOM('Cold Damage','n','p'); om_light=textOM('(202—234) Lightning Damage','n','p')
om_kpct=textOM('15% reduced Attack Speed','d','p')
OM_PHYS=[{'gi':om_hyb,'tmax':2},{'gi':om_ppct,'tmax':3},{'gi':om_pflat,'tmax':2}]
OM_FLAT=[{'gi':om_pflat,'tmax':2},{'gi':om_fire,'tmax':2},{'gi':om_cold,'tmax':2},{'gi':om_light,'tmax':2}]
OM_ASTRID=K('아스트리드의 창의성',"Astrid's Creativity")
R.append({
 'id':'diztoh-onehand-mace','cls':c,'base':base(c,'Marauding Mace'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('물리','Physical'),K('공격 속도','Attack speed'),K('치명타','Critical hit')],'patch':'0.5','created':'2026-11-09','author':DZM,
 'source':{'url':'https://www.youtube.com/watch?v=WDEkEIQFgT4','title':'How to Craft a One-Handed Mace | Double Crafted Mod Tech Explained | PoE 2','channel':'Diztoh'},
 'title':K('에센스 옵션 2개(공격 속도 + 공격 스킬 +2) + 쿠르갈 물리','two essence lines (attack speed + attack skills +2) + Kurgal physical'),
 'start':{'rar':'normal','quality':20,'mods':[]},
 'phases':[{'id':'base','kr':'매직 · 에센스','en':'Magic and essences'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'m1','phase':'base','do':'base','cost':'base','ts':'0:03','note':K('퀄리티 20% 노멀 베이스(영상 3디바인).','A 20% quality normal base (3 divines in the video).')},
  {'id':'m2','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':om_crit,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},'ts':'0:13'},
  {'id':'m3','phase':'base','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'p'},'ts':'1:40'},
  {'id':'m4','phase':'base','do':'essence','cur':'Greater_Essence_of_Haste','target':{'gi':om_as},'ts':'2:03'},
  {'id':'m5','phase':'base','do':'manual','target':{'rune':OM_ASTRID},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'2:20'},
  {'id':'m6','phase':'base','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':om_atk},'ts':'2:50'},
  {'id':'m7','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':OM_PHYS},'ts':'3:10',
   'br':K('실패: 좌측 말소의 징조 + 상위 카오스 오브','Miss: Sinistral Erasure + Greater Chaos')},
  {'id':'m7b','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':OM_PHYS,'replace':'p'},'fallbackFor':'m7','fail':{'goto':'self'},'ts':'3:31'},
  {'id':'m8','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_the_Blackblooded'],'target':{'unrev':'p'},'ts':'4:07'},
  {'id':'m9','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':OM_FLAT},'ts':'4:35',
   'br':K('실패: 절사의 징조 + 상위 카오스 오브','Miss: Whittling + Greater Chaos')},
  {'id':'m10','phase':'pre','do':'reveal','target':{'reveal':{'gi':om_kpct},'side':'p','lord':'kurgal','bone':'Preserved_Jawbone'},'fail':{'goto':'m8','via':LIGHT},'ts':'4:46'},
  {'id':'m11','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':OM_FLAT,'replace':'p'},'fallbackFor':'m9','fail':{'goto':'self'},'ts':'4:55',
   'br':K('버릴 옵션이 공격 속도 에센스(레벨 60)보다 낮을 때만','Only while the junk line is below the attack speed essence (level 60)')},
  {'id':'m12','phase':'fin','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':om_kpct}},'fail':{'goto':'self'},'ts':'5:12'},
  {'id':'m13','phase':'fin','do':'note','target':{'runeSwap':[OM_ASTRID,K('완벽한 철 룬','Perfect Iron Rune')]},'ts':'5:40'},
  {'id':'m14','phase':'fin','do':'note','ts':'6:17','note':K('선택: 타락(소켓 3개 노림). 건축가의 오브 2차 타락은 아이템이 바뀌거나 사라질 수 있음.','Optional: corrupt for a third socket. A second corruption with an Architect\'s Orb can transform or destroy the item.')},
 ]})
