# 라그나게임채널 recipes. Exec'd from build_recipes.py.
RG=K('라그나게임채널 영상 기반','Based on 라그나게임채널')
c='Amulets'
rg_spirit=textA('to Spirit','n','p'); rg_spell=textA('Level of all Spell Skills','n','s'); rg_maxQ=textA('to Maximum Quality','e','p')
rg_cast=textA('increased Cast Speed','n','s'); rg_sdmg=textA('increased Spell Damage','n','p'); rg_es=textA('increased maximum Energy Shield','n','p')
R.append({
 'id':'ragna-spell4-amulet','cls':c,'base':base(c,'Solar Amulet'),'ilvl':81,'difficulty':2,'budget':'medium',
 'buildTags':[K('주문','Spell'),K('정신력','Spirit'),K('시전 속도','Cast speed')],'patch':'0.5','created':'2026-11-08','author':RG,
 'source':{'url':'https://www.youtube.com/watch?v=Tzpdm8M-Pkk','title':'【POE 2】라장간 #8 4렙 목걸이 해보면 정말 간단합니다','channel':'라그나게임채널'},
 'title':K('정신력 분열 + 주문 +4(퀄리티) 목걸이','fractured Spirit + spell +4 (quality) amulet'),
 'start':{'rar':'rare','mods':[{'gi':rg_spirit,'tmax':1,'fr':True},{'gi':rg_spell,'tmax':1}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'q','kr':'최대 퀄리티','en':'Maximum quality'},{'id':'suf','kr':'시전 속도','en':'Cast speed'},{'id':'pre','kr':'접두 · 주문 +4','en':'Prefixes and spell +4'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('정신력 +50 분열 + 카오스 오브로 모든 주문 스킬 +3까지 뽑아 둔 태양의 목걸이.','A Solar Amulet with fractured +50 Spirit and +3 to all spell skills from Chaos Orbs.')},
  {'id':'g2','phase':'q','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'0:00','note':K('접두에 하나(영상은 회피).','One prefix (evasion in the video).')},
  {'id':'g3','phase':'q','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':rg_maxQ},'ts':'0:30','note':K('좌측 결정화의 징조 + 균열의 에센스로 그 접두를 최대 퀄리티 +20%로 바꿈.','Sinistral Crystallisation + Essence of the Breach turns that prefix into +20% maximum quality.')},
  {'id':'g4','phase':'suf','do':'quality','cur':'Skittering_Catalyst','target':{'quality':40},'ts':'0:45','note':K('달리는 기폭제(속도)로 40%. 쇳소리 기폭제보다 훨씬 싸고, 다음 단계에서 시전 속도를 밀어 줌.','Skittering Catalysts (speed) to 40%: much cheaper than Sibilant, and they push cast speed on the next slam.')},
  {'id':'g5','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'0:55','note':K('촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브. 영상은 첫 번째에 지능.','Catalysing + Dextral Exaltation + Perfect Exalt. Intelligence on the first one in the video.')},
  {'id':'g6','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'gi':rg_cast,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}},'ts':'1:31','note':K('같은 방법으로 마지막 접미에 시전 속도 2티어 이상. 영상은 두 번째에 성공(23%).','Same again for tier 2+ cast speed on the last suffix; it landed on the second try (23%).')},
  {'id':'g7','phase':'pre','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'2:16','note':K('남은 접두에 훼손(장막).','Desecrate the last prefix.')},
  {'id':'g8','phase':'pre','do':'quality','cur':'Sibilant_Catalyst','target':{'quality':40},'ts':'2:16','note':K('쇳소리 기폭제로 시전 퀄리티 40%. 34%부터 주문 +3이 +4가 되고 시전 속도도 같이 오름.','Sibilant Catalysts to 40% caster quality. From 34% the +3 becomes +4, and cast speed goes up too.')},
  {'id':'g9','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':rg_sdmg,'tmax':2},'side':'p','bone':'Preserved_Collarbone'},'fail':{'goto':'g7','via':LIGHT},'ts':'2:45','note':K('심연의 메아리의 징조로 공개해 주문 피해. 영상은 3티어(19%).','Reveal with Abyssal Echoes for spell damage; tier 3 (19%) in the video.')},
  {'id':'g10','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'removeGi':rg_maxQ,'junk':'p'},'ts':'3:03','note':K('퀄리티를 다 올렸으니 최대 퀄리티 줄은 필요 없음. 절사의 징조 + 상위 카오스 오브로 그 줄을 바꿈(영상은 에너지 보호막 % 증가).','With quality done, the maximum quality line is no longer needed. Whittling + Greater Chaos replaces it (increased energy shield in the video).')},
 ]})
