# ---- SaVeQ "How I made 2000 Divines From simple Focus Craft Poe 2 0.5.5" (youtu.be/R43FVay8_XI, 요약판 youtu.be/80sCtea0XZQ) ----
SVQ=K('SaVeQ 영상 기반','Based on SaVeQ')
c='Foci'
def textF(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sq_spellE=textF('increased Spell Damage','e','p'); sq_esp=textF('% increased Energy Shield','n','p'); sq_esf=textF('to maximum Energy Shield','n','p')
sq_lvl=textF('to Level of all Spell Skills','n','s'); sq_crit=textF('Critical Hit Chance for Spells','n','s')
sq_alloy=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Transcendent Alloy' in [x[3] for x in gr['t']]][0]
SQ_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'saveq-focus','cls':c,'base':base(c,'Tasalian Focus'),'ilvl':80,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('주문','Spell'),K('에너지 보호막','Energy Shield'),K('치명타','Critical')],'patch':'0.5.5','created':'2026-11-09','author':SVQ,
 'source':{'url':'https://www.youtube.com/watch?v=R43FVay8_XI','title':'How I made 2000 Divines From simple Focus Craft Poe 2 0.5.5','channel':'SaVeQ'},
 'title':K('주문 피해 분열 + 모든 주문 스킬 +2 + 초월의 합금','fractured spell damage + all spell skills +2 + Transcendent Alloy'),
 'start':{'rar':'rare','quality':22,'mods':[{'gi':sq_spellE,'fr':True,'crafted':True},{'gi':sq_esp,'tmax':1},{'gi':sq_lvl},{'junk':'p'}]},
 'phases':[{'id':'alloy','kr':'초월의 합금','en':'Transcendent Alloy'},{'id':'pre','kr':'접두','en':'Prefix'},{'id':'suf','kr':'접미 훼손','en':'Suffix desecration'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'q1','phase':'alloy','do':'base','cost':'base','ts':'18:20',
   'note':K('퀄리티 22%. 상위 마술의 에센스 주문 피해 분열 + 에너지 보호막 % 1티어 + 모든 주문 스킬 +2 + 잡옵 접두 옵션 1개.','22% quality. Fractured Greater Essence of Sorcery spell damage + T1 % energy shield + all spell skills +2 + one junk prefix.')},
  {'id':'q2','phase':'alloy','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'20:40'},
  {'id':'q3','phase':'alloy','do':'essence','cur':'Transcendent_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sq_alloy,'chance':0.5,'missDrop':sq_esp},'ts':'21:20',
   'br':K('잡옵이 지워지면 → 계속, 에너지 보호막이 지워지면 → 그 자리 엑잘','Junk removed → continue; energy shield removed → exalt that slot')},
  {'id':'qm1','phase':'alloy','branch':{'of':'q3','when':'miss'},'do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':sq_esp,'tmax':2},{'gi':sq_esf,'tmax':2}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}}},
  {'id':'q4','phase':'pre','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'21:50'},
  {'id':'q5','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'gi':sq_esf,'tmax':2},'fail':{'goto':'q6'},'ts':'22:40',
   'br':K('1~2티어 → 계속, 실패 → 다음 단계','T1–T2 → continue; miss → next step')},
  {'id':'q6','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Sinistral_Erasure'],'target':{'gi':sq_esf,'tmax':2,'replace':'p'},'fallbackFor':'q5','fail':{'goto':'self'},'ts':'23:05'},
  {'id':'q7','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':sq_crit,'tmax':1},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'q4','via':SQ_LIGHT},'ts':'24:00'},
  {'id':'q8','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('완벽한 철 룬','Perfect Iron Rune')]},'ts':'26:15',
   'note':K('룬 소켓 2개 모두 완벽한 철 룬.','Perfect Iron Runes in both sockets.')},
 ]})
