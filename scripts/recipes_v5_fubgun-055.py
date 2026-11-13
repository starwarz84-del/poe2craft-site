# ---- Fubgun "0.5.5 Fubgun Ice Shot Deadeye" 빌드 글의 Crafting Guide (mobalytics.gg/poe-2/builds/ice-shot-deadeye, 2026-06-18 갱신) ----
# 글 하나에 제작법이 여러 개라 이 파일에 같이 둠. 플로우차트 scripts/graphs/gen_batch26.py와 같은 단계 id(정책 31).
# 기록 tools/notes/web-fubgun-iceshot.md. 원본 = 밸런스 기준(공개는 빛의 징조로 다시), 등급 레시피는 recipes_v5_zz-batchz26-v2.py.
FUB=K('Fubgun 빌드 글 기반','Based on Fubgun’s build guide')
FUBSRC={'url':'https://mobalytics.gg/poe-2/builds/ice-shot-deadeye','title':'0.5.5 Fubgun Ice Shot Deadeye — Crafting Guide','channel':'Fubgun (Mobalytics)'}
LIGHTF={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
def _fub(id, c, bname, ilvl, diff, title, tags, start, phases, nodes):
    R.append({'id':id,'cls':c,'base':base(c,bname),'ilvl':ilvl,'difficulty':diff,'budget':'low','buildTags':tags,'patch':'0.5.5','created':'2026-11-11','author':FUB,
              'source':FUBSRC,'title':title,'start':start,'phases':phases,'nodes':nodes})
PH=[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가','en':'Adding modifiers'}]

# 1. 가성비 화살통
c='Quivers'
_fub('fubgun-quiver',c,'Visceral Quiver',75,2,K('물리 피해 추가 + 투사체 +1 + 공격 속도 + 치명타 훼손','flat physical + projectile skills +1 + attack speed + crit desecration'),
  [K('활','Bow'),K('투사체','Projectile'),K('리그 초반','League start')],
  {'rar':'magic','mods':[{'gi':2,'tmax':1},{'gi':9,'tmax':1}]},PH,[
  {'id':'q1','phase':'base','do':'base','cost':'base','note':K('노멀 본능적인 화살통(아이템 레벨 75).','A normal Visceral Quiver (item level 75).')},   # 2026-11-13 G10: 플로우차트는 노멀부터 진화·확장(글 1단계)
  {'id':'q2','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','omens':['Omen_of_Sinistral_Coronation'],'target':{'anyOf':[{'gi':4},{'gi':6},{'gi':8},{'gi':19}],'asIs':True,'side':'p'},
   'br':K('원소 피해 추가·활 스킬 피해면 좋음, 아니면 그대로','Flat elemental or bow damage is good; otherwise keep it')},
  {'id':'q3','phase':'main','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'}},
  {'id':'q4','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':14,'tmax':2},{'gi':12,'tmax':2},{'gi':24},{'gi':25}]},'side':'s','bone':'Preserved_Jawbone'},'fail':{'goto':'q3','via':LIGHTF}},
  {'id':'q5','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']}},
  {'id':'q6','phase':'main','do':'note','note':K('완성.','Done.')}])

# 2. 가성비 물리 활 (비치명타)
c='Bows'
_PHYS_ELE=[{'gi':3,'tmax':3},{'gi':4,'tmax':3},{'gi':6,'tmax':3}]
_fub('fubgun-phys-bow',c,'Warmonger Bow',75,2,K('물리 피해 % + 물리 피해 추가 + 원소 피해 추가 훼손','% physical + flat physical + flat elemental desecration'),
  [K('활','Bow'),K('물리','Physical'),K('리그 초반','League start')],
  {'rar':'magic','mods':[{'gi':7,'tmax':2},{'junk':'s'}]},PH,[
  {'id':'b1','phase':'base','do':'base','cost':'base','note':K('물리 피해 % 매직 활(확장의 오브까지 쓴 상태).','A magic bow with % physical (already augmented).')},
  {'id':'b2','phase':'base','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':39}},
  {'id':'b3','phase':'main','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'b4','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':_PHYS_ELE},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'b3','via':LIGHTF}},
  {'id':'b5','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']}},
  {'id':'b6','phase':'main','do':'note','note':K('완성.','Done.')}])

# 3. 가성비 치명타 활
_CRIT_FL=[{'gi':2,'tmax':2},{'gi':3,'tmax':2},{'gi':4,'tmax':2},{'gi':6,'tmax':2}]
_fub('fubgun-crit-bow',c,'Warmonger Bow',75,2,K('물리 피해 % + 치명타 확률 + 피해 추가 훼손','% physical + crit chance + flat damage desecration'),
  [K('활','Bow'),K('치명타','Critical'),K('리그 초반','League start')],
  {'rar':'magic','mods':[{'gi':7,'tmax':2},{'junk':'s'}]},PH,[
  {'id':'b1','phase':'base','do':'base','cost':'base','note':K('물리 피해 % 매직 활(확장의 오브까지 쓴 상태).','A magic bow with % physical (already augmented).')},
  {'id':'b2','phase':'base','do':'essence','cur':'Greater_Essence_of_Seeking','target':{'gi':49}},
  {'id':'b3','phase':'main','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'b4','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':_CRIT_FL},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'b3','via':LIGHTF}},
  {'id':'b5','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']}},
  {'id':'b6','phase':'main','do':'note','note':K('완성.','Done.')}])

# 5. 투사체 +3 목걸이
c='Amulets'
_RES=[{'gi':4},{'gi':5},{'gi':6},{'gi':7},{'gi':8},{'gi':24},{'gi':26}]
_fub('fubgun-proj-amulet',c,'Gold Amulet',82,3,K('투사체 +3 분열 + 정신력 + 강화의 에센스 + 저항 2개 + 생명력·에너지 보호막 훼손','fractured projectile +3 + spirit + Enhancement essence + two resistances + life or ES desecration'),
  [K('투사체','Projectile'),K('정신력','Spirit'),K('저항','Resistances')],
  {'rar':'rare','mods':[{'gi':20,'tmax':1,'fr':True},{'junk':'p'}]},PH,[
  {'id':'a0','phase':'base','do':'base','cost':'base','note':K('모든 투사체 스킬 레벨 +3 분열 + 잡옵 1개.','Fractured +3 projectile skills + one junk line.')},
  {'id':'a1','phase':'main','do':'chaos','cur':'Chaos_Orb','target':{'gi':28,'tmax':2},'fail':{'goto':'self'}},
  {'id':'a2','phase':'main','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'}},
  {'id':'a3','phase':'main','do':'essence','cur':'Perfect_Essence_of_Enhancement','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':74}},
  {'id':'a4','phase':'main','do':'quality','cur':'Xophs_Catalyst','target':{'quality':20}},
  {'id':'a5','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'anyOf':_RES},
   'fail':{'goto':'a4','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}}},
  {'id':'a6','phase':'main','do':'quality','cur':'Xophs_Catalyst','target':{'quality':20}},
  {'id':'a7','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'anyOf':_RES},
   'fail':{'goto':'a6','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'a5'}},
  {'id':'a8','phase':'main','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'}},
  {'id':'a9','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':9,'tmax':2},{'gi':13,'tmax':2},{'gi':16,'tmax':2}]},'side':'p','bone':'Preserved_Collarbone'},'fail':{'goto':'a8','via':LIGHTF}},
  {'id':'a10','phase':'main','do':'note','note':K('완성.','Done.')}])

# 6. 가성비 에너지 보호막 투구
c='Helmets_int'
_fub('fubgun-es-helmet',c,'Kamasan Tiara',78,2,K('에너지 보호막 최대치 + 강화의 에센스 + 에너지 보호막 % 복합 훼손','flat energy shield + Enhancement essence + hybrid % energy shield desecration'),
  [K('에너지 보호막','Energy shield'),K('리그 초반','League start')],
  {'rar':'magic','mods':[{'gi':7,'tmax':1},{'junk':'s'}]},PH,[
  {'id':'e1','phase':'base','do':'base','cost':'base','note':K('에너지 보호막 최대치 1티어 매직 투구.','A magic helmet with T1 flat energy shield.')},
  {'id':'e2','phase':'base','do':'essence','cur':'Greater_Essence_of_Enhancement','target':{'gi':34}},
  {'id':'e3','phase':'main','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'e4','phase':'main','do':'reveal','target':{'reveal':{'anyOf':[{'gi':9,'tmax':2},{'gi':10,'tmax':2}]},'side':'p','bone':'Preserved_Rib'},'fail':{'goto':'e3','via':LIGHTF}},
  {'id':'e5','phase':'main','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']}},
  {'id':'e6','phase':'main','do':'note','note':K('완성.','Done.')}])
