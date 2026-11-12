# ---- SL 게임연구소 "[POE2 0.5.5] 검은 화염파 최종 완성형 세팅 | 제작 가이드 포함" (youtu.be/J7J8Jo7ibvE) 딜용 장갑 슬라이드(6:10) ----
# 플로우차트(scripts/graphs/gen_batch23.py)를 따라 작성(정책 31). 분열 전 준비는 시작 상태(정책 2), 준비 단계는 prep.
SLG=K('SL 게임연구소 영상 기반','Based on SL 게임연구소')
c='Gloves_str_dex'
sg_am,sg_ig,sg_fa,sg_cu,sg_wi,sg_fr=85,82,86,92,91,2
SG_KATLA=K('카틀라의 순흑',"Katla's Gloom")
R.append({
 'id':'sl-blacksteel-gauntlets','cls':c,'base':base(c,'Blacksteel Gauntlets'),'ilvl':82,'exceptional':{'sockets':1},'difficulty':5,'budget':'high',
 'buildTags':[K('상태 이상','Ailment'),K('점화','Ignite'),K('저주','Curse')],'patch':'0.5.5','created':'2026-11-11','author':SLG,
 'source':{'url':'https://www.youtube.com/watch?v=J7J8Jo7ibvE','title':'[POE2 0.5.5] 검은 화염파 최종 완성형 세팅 | 극 하이엔드 세팅 | 화염파 | 제작 가이드 포함','channel':'SL 게임연구소'},
 'title':K('저주 강도 분열 + 상태 이상 강도·점화 강도·피해 가속 + 위축·화염 저항','fractured curse magnitude + ailment magnitude, ignite and faster ailments + withered and fire resistance'),   # 2026-11-13 W13: 6:08 툴팁의 분열 색 = 저주 강도
 'start':{'rar':'rare','quality':29,'mods':[{'gi':sg_cu,'tmax':1,'fr':True},{'junk':'p'}]},   # 2026-11-13 W13: 분열 = 접미 저주 강도(플로우차트가 단계·시작 상태를 덮어씀), 카틀라의 순흑은 플로우차트 룬 단계에서 장착(시작에 두면 두 번 들어감)
 'phases':[{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'훼손 공개','en':'Reveal'}],
 'nodes':[
  {'id':'k0','phase':'pre','do':'base','cost':'base','ts':'6:10','note':K('퀄리티 25%. 카틀라의 순흑 장착 상태로 상태 이상 강도 1티어 분열 + 잡옵 1개.',"25% quality. Katla's Gloom socketed: fractured T1 ailment magnitude plus one junk line.")},
  {'id':'k1','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':sg_ig,'tmax':1},{'gi':sg_fa,'tmax':1}]},'fail':{'goto':'self'},'ts':'6:10'},
  {'id':'k2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':sg_ig,'tmax':1},{'gi':sg_fa,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'k1'},'ts':'6:10'},
  {'id':'k3','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':[{'gi':sg_cu,'tmax':1},{'gi':sg_wi,'tmax':1},{'gi':sg_fr,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment'],'n':2}},'ts':'6:10'},
  {'id':'k4','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'anyOf':[{'gi':sg_cu,'tmax':1},{'gi':sg_wi,'tmax':1},{'gi':sg_fr,'tmax':1}],'replace':'s'},'fail':{'goto':'self'},'ts':'6:10'},
  {'id':'k5','phase':'fin','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'6:10'},
  {'id':'k6','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':sg_fr,'tmax':1},{'gi':sg_cu,'tmax':1},{'gi':sg_wi,'tmax':1}]},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'k5','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}},'ts':'6:10'},
 ],
 'prep':{'start':{'rar':'normal','quality':0},'phases':[{'id':'prep','kr':'분열 준비','en':'Fracture prep'}],'nodes':[
  {'id':'x1','phase':'prep','do':'quality','cur':'Vaal_Armourers_Infuser','target':{'setQuality':25},'note':K('바알 방어구 장인의 주입기로 25% 이상(타락하면 새 베이스).',"Vaal Armourer's Infuser to 25%+ (a corruption means a new base).")},
  {'id':'x2','phase':'prep','do':'manual','target':{'rune':SG_KATLA},'label':K('카틀라의 순흑 장착',"Socket Katla's Gloom")},
  {'id':'x3','phase':'prep','do':'note','note':K('완벽한 진화의 오브 → 완벽한 확장의 오브 + 소멸의 오브 반복(원하는 1티어 2개) → 완벽한 제왕의 오브 → 보존된 갈비뼈 + 분열의 오브(1티어 분열).','Perfect Transmutation → Perfect Augmentation with Annulment until two wanted T1 lines → Perfect Regal → Preserved Rib + Fracturing Orb (a T1 line fractured).')}]},
 'quality':25})
