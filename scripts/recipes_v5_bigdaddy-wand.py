# ---- BigDaddyGaming "0.5 Wand Crafting Guide" (mobalytics.gg/poe-2/profile/bigdaddygaming/guides/0-5-7-wand-crafting-guide, 2026-06-02) ----
# 가성비 길(번개 주문 +5 분열 → 주문 치명타 → 초월의 합금 → 마나 자리 막기 → 엑잘 → 막기 제거 → 마지막 접두 공개).
# 플로우차트 scripts/graphs/gen_batch26.py와 같은 단계 id(정책 31), 기록 tools/notes/web-bigdaddy-wand.md.
c='Wands'
_WPRE=[{'gi':3,'tmax':2},{'gi':7,'tmax':2},{'gi':4,'tmax':2},{'gi':28,'tmax':2}]
R.append({'id':'bigdaddy-lightning-wand','cls':c,'base':base(c,'Dueling Wand'),'ilvl':81,'difficulty':3,'budget':'mid',
 'buildTags':[K('번개','Lightning'),K('주문','Spell'),K('치명타','Critical')],'patch':'0.5.5','adaptedFrom':'0.5','created':'2026-11-11','author':K('BigDaddyGaming 글 기반','Based on BigDaddyGaming’s guide'),
 'source':{'url':'https://mobalytics.gg/poe-2/profile/bigdaddygaming/guides/0-5-7-wand-crafting-guide','title':'0.5 Wand Crafting Guide','channel':'BigDaddyGaming (Mobalytics)'},
 'title':K('번개 주문 +5 분열 + 주문 치명타 + 초월의 합금 + 주문·번개 피해 접두','fractured lightning spells +5 + spell crit + Transcendent Alloy + spell/lightning prefixes'),
 'start':{'rar':'rare','mods':[{'gi':13,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'w0','phase':'suf','do':'base','cost':'base','note':K('모든 번개 주문 스킬 레벨 +5 분열 + 잡옵 1개.','Fractured +5 lightning spells + one junk line.')},
  {'id':'w1','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':20,'tmax':1},'fail':{'goto':'self'}},
  {'id':'w2','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'}},
  {'id':'w3','phase':'suf','do':'essence','cur':'Transcendent_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':60}},
  {'id':'w4','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'p'}},
  {'id':'w5','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':1},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'w4','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}},
   'br':K('마나 최대치로 접두 한 자리를 막아 두면 다음 엑잘에 마나가 안 붙음','A mana line blocks one prefix, so the next exalts cannot roll mana')},
  {'id':'w6','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','p']}},
  {'id':'w7','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True}},
  {'id':'w8','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'p'}},
  {'id':'w9','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':_WPRE},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'w8','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}}},
  {'id':'w10','phase':'pre','do':'note','note':K('완성.','Done.')},
 ]})
