# ---- XenoARPG "[EN] PoE2 0.5 | Crafting Multi-Mirror Physical Damage Crossbow | Step-by-Step" (youtu.be/1TP4aGqxU7Q) ----
# 자막이 없는 영상이라 화면(아이템 툴팁·징조 툴팁)만 보고 작성.
XNO=K('XenoARPG 영상 기반','Based on XenoARPG')
c='Crossbows'
def textXN(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
xn_crit=textXN('to Critical Hit Chance','n','s'); xn_proj=textXN('Level of all Projectile Skills','n','s'); xn_as=textXN('increased Attack Speed','n','s')
xn_ppct=textXN('(170—179)% increased Physical Damage','n','p'); xn_hyb=textXN('increased Physical Damage\n+','n','p')
xn_flat=textXN('Physical Damage','n','p'); xn_eatk=textXN('increased Elemental Damage with Attacks','n','p')
XN_IRON=K('상위 철 룬','Greater Iron Rune')
R.append({
 'id':'xeno-phys-crossbow','cls':c,'base':base(c,'Desolate Crossbow'),'ilvl':82,'sockets':3,'exceptional':{'sockets':1},'difficulty':5,'budget':'high',
 'buildTags':[K('물리','Physical'),K('투사체','Projectile'),K('치명타','Crit')],'patch':'0.5','created':'2026-11-09','author':XNO,
 'source':{'url':'https://www.youtube.com/watch?v=1TP4aGqxU7Q','title':'[EN] PoE2 0.5 | Crafting Multi-Mirror Physical Damage Crossbow | Step-by-Step','channel':'XenoARPG'},
 'title':K('치명타 확률 분열 + 물리 접두 3줄(1티어) + 투사체 +5 · 공격 속도','fractured crit chance + three T1 physical prefixes + projectile +5 and attack speed'),
 'start':{'rar':'rare','mods':[{'gi':xn_crit,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'pre','kr':'접두 · 막기','en':'Prefixes and block'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'물리 추가 · 마무리','en':'Flat physical and finish'}],
 'nodes':[
  {'id':'x1','phase':'pre','do':'base','cost':'base','ts':'2:51','note':K('치명타 확률 1티어 분열 + 잡옵 1줄.','Fractured tier 1 crit chance plus one junk line.')},
  {'id':'x2','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'gi':xn_ppct,'tmax':1},'fail':{'goto':'self'},'ts':'3:05'},
  {'id':'x3','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'gi':xn_hyb,'tmax':1},'ts':'5:42',
   'br':K('실패: 절사의 징조 + 완벽한 카오스 오브(영상)','Miss: Whittling + Perfect Chaos (video)')},
  {'id':'x3b','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'x3','target':{'gi':xn_hyb,'tmax':1},'fail':{'goto':'self'},'ts':'5:50'},
  {'id':'x4','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'4:47'},
  {'id':'x5','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':xn_eatk,'tmax':1},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'x4','via':LIGHT},'ts':'5:29',
   'note':K('막기용 접두(뒤에서 지움).','A blocking prefix (removed later).')},
  {'id':'x6','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'gi':xn_proj,'tmax':1},'ts':'6:17',
   'br':K('실패: 절사의 징조 + 완벽한 카오스 오브(영상)','Miss: Whittling + Perfect Chaos (video)')},
  {'id':'x6b','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'x6','target':{'gi':xn_proj,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'6:37'},
  {'id':'x7','phase':'fin','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'8:10'},
  {'id':'x8','phase':'fin','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'p'},'ts':'8:20'},
  {'id':'x9','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':xn_flat,'tmax':1},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'x8','via':LIGHT},'ts':'8:27'},
  {'id':'x10','phase':'fin','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'gi':xn_as,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'10:03',
   'br':K('버릴 접미가 레벨 75 미만일 때만. 레벨 높은 잡옵(영상: 볼트 2개 장전, 82)은 갈림길로','Only while the junk suffix is below level 75. A high-level junk line (video: loads 2 additional bolts, 82) goes to the fork')},
  {'id':'x10b','phase':'fin','do':'note','fallbackFor':'x10','label':K('갈림길: 높은 잡옵 바꾸기','Fork: reroll a high-level junk line'),'ts':'9:50',
   'note':K('우측 말소의 징조 + 카오스 오브로 그 접미를 레벨 75 미만 줄로 바꾼 뒤 절사로 돌아감(영상은 히네코라의 머리카락으로 결과를 미리 봄).','Dextral Erasure + Chaos turns that suffix into a line below level 75, then back to Whittling (the video previewed each result with Hinekora\'s Lock).')},
  {'id':'x11','phase':'fin','do':'quality','cur':'Blacksmiths_Whetstone','target':{'quality':20},'ts':'10:03'},
  {'id':'x12','phase':'fin','do':'manual','target':{'rune':XN_IRON},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'10:03'},
  {'id':'x13','phase':'fin','do':'manual','target':{'rune':XN_IRON},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'10:03'},
  {'id':'x14','phase':'fin','do':'manual','target':{'rune':XN_IRON},'label':K('상위 철 룬 장착','Socket a Greater Iron Rune'),'ts':'10:03'},
  {'id':'x15','phase':'fin','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':xn_ppct}},'fail':{'goto':'self'},'ts':'9:43'},
 ]})
