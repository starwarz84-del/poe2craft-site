# ---- Diztoh "Easy Budget Endgame Crossbow Crafting Guide | PoE 2 0.5" (youtu.be/vk3pLFUov8U) ----
# 같은 영상의 옛 레시피(recipes_batch2.py #8 'diztoh-grenade-crossbow')를 현재 정책으로 다시 쓴 판.
DZX=K('Diztoh 영상 기반','Based on Diztoh')
c='Crossbows'
def textXB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
xd_ppct=textXB('(170—179)% increased Physical Damage','n','p'); xd_hyb=textXB('increased Physical Damage\n+','n','p')
xd_flatE=textXB('Physical Damage','e','p'); xd_battle=textXB('Level of all Attack Skills','e','s')
xd_gren=textXB('Grenades have','d','s')
xd_fire=textXB('Fire Damage','n','p'); xd_cold=textXB('Cold Damage','n','p'); xd_light=textXB('(310—358) Lightning Damage','n','p'); xd_eatk=textXB('increased Elemental Damage with Attacks','n','p')
XD_PRE=[{'gi':xd_hyb,'tmax':3},{'gi':xd_fire,'tmax':4},{'gi':xd_cold,'tmax':4},{'gi':xd_light,'tmax':4},{'gi':xd_eatk,'tmax':2}]
XD_ASTRID=K('아스트리드의 창의성',"Astrid's Creativity"); XD_IRON=K('완벽한 철 룬','Perfect Iron Rune')
R.append({
 'id':'diztoh-budget-crossbow','cls':c,'base':base(c,'Siege Crossbow'),'ilvl':82,'sockets':3,'exceptional':{'sockets':1},'difficulty':1,'budget':'low',
 'buildTags':[K('수류탄','Grenade'),K('물리','Physical'),K('가성비','Budget')],'patch':'0.5','created':'2026-11-09','author':DZX,
 'source':{'url':'https://www.youtube.com/watch?v=vk3pLFUov8U','title':'Easy Budget Endgame Crossbow Crafting Guide | PoE 2 0.5','channel':'Diztoh'},
 'title':K('에센스 옵션 2개(물리 추가 + 공격 스킬 +3) + 아마나무 수류탄 2회 발동','two essence lines (flat physical + attack skills +3) + Amanamu grenade double activation'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'매직 · 에센스','en':'Magic and essences'},{'id':'des','kr':'훼손 · 엑잘','en':'Desecration and slam'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'c1','phase':'base','do':'base','cost':'base','ts':'0:02','note':K('노멀 베이스(룬 소켓 3개).','A normal base (three rune sockets).')},
  {'id':'c2','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':xd_ppct,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},'ts':'0:50'},
  {'id':'c3','phase':'base','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'1:20'},
  {'id':'c4','phase':'base','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':xd_flatE},'ts':'1:28'},
  {'id':'c5','phase':'base','do':'manual','target':{'rune':XD_ASTRID},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'1:35'},
  {'id':'c6','phase':'base','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':xd_battle},'ts':'1:56'},
  {'id':'c7','phase':'des','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Liege'],'target':{'unrev':'s'},'ts':'2:16'},
  {'id':'c8','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':xd_gren},'side':'s','lord':'amanamu','bone':'Preserved_Jawbone'},'fail':{'goto':'c7','via':LIGHT},'ts':'2:53'},
  {'id':'c9','phase':'des','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},'ts':'2:35',
   'br':K('대박(복합 물리·공격 속도) → 완성, 아니면 절사로 접두 바꾸기','Hit (hybrid physical, attack speed) → done; otherwise Whittling on the prefix')},
  {'id':'c10','phase':'fin','do':'note','target':{'runeSwap':[XD_ASTRID,XD_IRON]},'ts':'3:15'},
  {'id':'c11','phase':'fin','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'optional':True,'target':{'anyOf':XD_PRE,'replace':'p'},'fail':{'goto':'self'},'ts':'3:33',
   'br':K('버릴 옵션이 레벨 60 미만(영상: 정확도 4티어)일 때만. 레벨 60 이상 옵션이 뜨면 멈춤(다음 절사가 에센스 옵션을 지움)','Only while the junk line is below level 60 (video: tier 4 accuracy). Stop once a level 60+ line lands (the next Whittling would take the essence line)')},
  {'id':'c12','phase':'fin','do':'quality','cur':'Blacksmiths_Whetstone','target':{'quality':20},'ts':'4:00'},
  {'id':'c13','phase':'fin','do':'manual','target':{'rune':XD_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'4:05'},
  {'id':'c14','phase':'fin','do':'manual','target':{'rune':XD_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'4:05'},
  {'id':'c15','phase':'fin','do':'manual','cost':'vaal','optional':True,'target':{'setQuality':22},'label':K('바알 대장장이의 주입기 (선택)',"Vaal Blacksmith's Infuser (optional)"),'ts':'4:17'},
  {'id':'c16','phase':'fin','do':'note','ts':'4:59','note':K('완성. 타락은 선택(영상은 소켓 4개를 노렸다가 망가짐).','Done. Corrupting is optional (the video went for a fourth socket and bricked it).')},
 ]})
