# ---- SL 게임연구소! "[POE2 0.5.5] #8 투사체 7줄 장갑 제작 가이드! 세를의 승리 (접미어 4줄)" (youtu.be/XMYJh3CnXuY) ----
SL=K('SL 게임연구소! 영상 기반','Based on SL 게임연구소!')
c='Gloves_int'
def textB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sg_proj=textB('+2 to Level of all Projectile Skills','x','s'); sg_pdmg=textB('increased Projectile Damage','x','p'); sg_pspd=textB('increased Projectile Speed','x','p')
sg_crit=textB('increased Critical Hit Chance','x','s'); sg_pierce=textB('chance to Pierce an Enemy','x','s')
sg_mana=textB('to maximum Mana','n','p'); sg_esp=textB('% increased Energy Shield','n','p'); sg_esf=textB('to maximum Energy Shield','n','p'); sg_phys=textB('to (22—32) Physical Damage to Attacks','n','p')
sg_rem=textB('Remnants can be collected','e','s')
KOLR=K('콜르의 사냥',"Kolr's Hunt"); SERLE=K('세를의 승리',"Serle's Triumph")
R.append({
 'id':'sl-proj7-gloves','cls':c,'base':base(c,'Sirenscale Gloves'),'ilvl':80,'cap':{'p':3,'s':4},'sockets':2,'exceptional':{'sockets':1},'difficulty':5,'budget':'high','unknownW':True,
 'buildTags':[K('투사체','Projectile'),K('치명타','Crit'),K('에너지 보호막','Energy Shield')],'patch':'0.5.5','created':'2026-11-09','author':SL,
 'source':{'url':'https://www.youtube.com/watch?v=XMYJh3CnXuY','title':'[POE2 0.5.5] #8 투사체 7줄 장갑 제작 가이드! 세를의 승리 (접미어 4줄)','channel':'SL 게임연구소!'},
 'title':K('7줄 · 투사체 +2 분열 + 세를의 승리 접미 4줄','seven mods: fractured +2 projectile, four suffixes with Serle\'s Triumph'),
 'start':{'rar':'rare','quality':25,'runes':[KOLR],'mods':[{'gi':sg_proj,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두 3줄','en':'Three prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'훼손 마무리','en':'Desecration finish'}],
 'nodes':[
  {'id':'v1','phase':'base','do':'base','cost':'base','ts':'1:41',
   'note':K('퀄리티 25% 이상. 콜르의 사냥을 장착한 상태로 모든 투사체 스킬 레벨 +2가 분열된 베이스 + 잡옵 1줄.',
            '25%+ quality, Kolr\'s Hunt socketed: fractured +2 projectile skills plus one junk line.')},
  {'id':'v1b','phase':'base','do':'manual','target':{'rune':SERLE},'label':K('세를의 승리 장착',"Socket Serle's Triumph"),
   'note':K('접미 4줄을 위해 세를의 승리 장착(분열 뒤에 끼움).',"Socket Serle's Triumph for a fourth suffix (after the fracture).")},
  {'id':'v2','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':sg_pspd,'tmax':1},{'gi':sg_pdmg,'tmax':1}]},'fail':{'goto':'self'},'ts':'3:02',
   'note':K('카오스 오브로 투사체 속도 또는 투사체 피해 1티어(둘 다 거의 필수).','Chaos for tier 1 projectile speed or projectile damage (both near-mandatory).')},
  {'id':'v3','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation','Omen_of_Sinistral_Exaltation'],
   'target':{'anyOf':[{'gi':sg_pdmg,'tmax':1},{'gi':sg_pspd,'tmax':1}]},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'v2'},'ts':'3:20',
   'note':K('(계산은 남은 투사체 1티어 기준) 상위 찬미의 징조 + 좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 2줄: 남은 투사체 1티어 + 마나 최대치·에너지 보호막·공격 시 물리 피해 1티어 중 하나. 잡옵 2줄이면 소멸의 오브(접미는 분열 줄뿐), 1줄이면 그 줄이 레벨이 가장 낮을 때만 절사의 징조 + 카오스 오브(영상은 안 돼서 소멸의 오브 반복). 가장 어려운 구간.',
            'Greater + Sinistral Exaltation + Perfect Exalt for two prefixes: the other tier 1 projectile line plus tier 1 mana, energy shield or flat physical. Two junk: Annul (the only suffix is fractured); one junk: Whittling + Chaos only if it is the lowest level (it was not in the video, so Annul again). The hardest part.')},
  {'id':'v4','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'gi':sg_crit,'tmax':1},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}},'ts':'4:01',
   'note':K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 2줄(접두가 꽉 차서 면 징조 없음): 치명타 확률 1티어 + 잡옵. 잡옵만 2줄이면 우측 소멸의 징조 대신 우측 결정화의 징조 + 심연의 에센스 → 뼈로 징표 훼손 → 빛의 징조 + 소멸의 오브로 지우는 게 더 쌈.',
            'Greater Exaltation + Perfect Exalt for two suffixes (prefixes are full, so no side omen): tier 1 crit chance plus junk. If both are junk, Dextral Crystallisation + Essence of the Abyss, desecrate the Mark with a bone, then Light + Annulment is cheaper than Dextral Annulment.')},
  {'id':'v5','phase':'suf','do':'essence','cur':'Expansive_Alloy','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':sg_rem,'chance':0.5},'fail':{'goto':'v4'},'ts':'15:42',
   'note':K('우측 결정화의 징조 + 팽창하는 합금: 접미 잡옵이 지워지면 성공(1/2, 치명타 확률이 지워지면 접미 작업 처음부터). 접두에 마나 최대치 1티어가 있을 때 매물들이 쓰는 합금(아니면 원하는 에센스).',
            'Dextral Crystallisation + Expansive Alloy: success when it takes the junk suffix (1 in 2; if crit goes, redo the suffixes). Listings with tier 1 mana use this alloy; otherwise the essence you want.')},
  {'id':'v6','phase':'fin','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'16:01','note':K('고대 갈비뼈로 마지막 접미 훼손.','Ancient Rib desecrates the last suffix.')},
  {'id':'v7','phase':'fin','do':'reveal','target':{'reveal':{'gi':sg_pierce,'tmax':1},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'v6','via':LIGHT},'ts':'16:05',
   'note':K('공개해서 관통 1티어(51% 이상). 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손. 영상은 관통이 정말 안 떠서 여러 번 반복.','Reveal for tier 1 pierce (51%+); otherwise Light + Annulment and desecrate again. Pierce took many tries in the video.')},
  {'id':'v8','phase':'fin','do':'note','ts':'17:50','note':K('완성(영상 시세 1,000디바인 이상). 변수가 많아 직접 만들기보다 거래소 구매를 추천.','Done (over 1,000 divines in the video). Lots of variance; buying is recommended over crafting.')},
 ]})
