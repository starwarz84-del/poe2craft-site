# ---- SaVeQ "Focus Crafting Is TOO PROFITABLE Right Now Poe2 - 0.5" (youtu.be/uCbyTF-LJ5I) ----
# 같은 채널의 recipes_v5_saveq-focus.py(주문 피해 분열 + 접미 훼손)와 다른 판: 매직 베이스 → 상위 추구의 에센스 → 접두 훼손 → 분열 → 초월의 합금
SVA=K('SaVeQ 영상 기반','Based on SaVeQ')
c='Foci'
def textA(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sa_lvl=textA('to Level of all Spell Skills','n','s'); sa_spell=textA('increased Spell Damage','n','p')
sa_critE=textA('Critical Hit Chance for Spells','e','s')
sa_esp=textA('% increased Energy Shield','n','p'); sa_esf=textA('to maximum Energy Shield','n','p'); sa_hyb=textA('increased Energy Shield\n+','n','p'); sa_mana=textA('to maximum Mana','n','p')
sa_alloy=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Transcendent Alloy' in [x[3] for x in gr['t']]][0]
SA_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
SA_REV=[{'gi':sa_esp,'tmax':1},{'gi':sa_hyb,'tmax':1},{'gi':sa_mana,'tmax':1}]
SA_PRE=[{'gi':sa_esp,'tmax':2},{'gi':sa_hyb,'tmax':2},{'gi':sa_esf,'tmax':3},{'gi':sa_mana,'tmax':2}]
SA_ANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}
R.append({
 'id':'saveq-alloy-focus','cls':c,'base':base(c,'Tasalian Focus'),'ilvl':81,'sockets':1,'difficulty':2,'budget':'medium',
 'buildTags':[K('주문','Spell'),K('에너지 보호막','Energy Shield'),K('치명타','Critical')],'patch':'0.5','created':'2026-11-09','author':SVA,
 'source':{'url':'https://www.youtube.com/watch?v=uCbyTF-LJ5I','title':'Focus Crafting Is TOO PROFITABLE Right Now Poe2 - 0.5','channel':'SaVeQ'},
 'title':K('모든 주문 스킬 +2 분열 + 주문 치명타 에센스 + 초월의 합금','fractured +2 spell skills + spell crit essence + Transcendent Alloy'),
 'start':{'rar':'rare','mods':[{'gi':sa_lvl,'fr':True},{'gi':sa_spell,'tmax':1},{'gi':sa_critE,'crafted':True},{'unrev':'p'}]},
 'phases':[{'id':'rev','kr':'접두 훼손 공개','en':'Prefix reveal'},{'id':'alloy','kr':'초월의 합금','en':'Transcendent Alloy'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'v1','phase':'rev','do':'base','cost':'base','ts':'8:40',
   'note':K('모든 주문 스킬 +2 분열 + 주문 피해 1티어 + 주문 치명타(상위 추구의 에센스) + 미공개 훼손 접두.','Fractured +2 spell skills + T1 spell damage + spell crit (Greater Essence of Seeking) + an unrevealed desecrated prefix.')},
  {'id':'v2','phase':'rev','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SA_REV},'side':'p','bone':'Ancient_Rib'},'ts':'9:35',
   'br':K('1티어 → 계속, 실패 → 빛의 징조 + 소멸의 오브로 지우고 다시 훼손','T1 → continue; miss → Omen of Light + Annulment and desecrate again')},
  {'id':'vr1','phase':'rev','branch':{'of':'v2','when':'miss'},'do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'7:58'},
  {'id':'vr2','phase':'rev','branch':{'of':'v2','when':'miss'},'do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'7:58'},
  {'id':'vr3','phase':'rev','branch':{'of':'v2','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SA_REV},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'vr2','via':SA_LIGHT},'ts':'8:05'},
  {'id':'v4','phase':'alloy','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'9:45',
   'br':K('합금이 지울 접두 (에너지 보호막·마나가 뜨면 그대로 써도 됨)','The prefix for the alloy to remove (keep it if energy shield or mana lands)')},
  {'id':'v3','phase':'alloy','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'9:50'},
  {'id':'v5','phase':'alloy','do':'essence','cur':'Transcendent_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sa_alloy,'chance':1/3,'missDrop':sa_spell},'ts':'10:05',
   'br':K('방금 엑잘한 줄이 지워지면 → 계속, 주문 피해·공개 줄이 지워지면 → 그 자리 엑잘','The exalted line goes → continue; spell damage or the revealed line goes → exalt that slot')},
  {'id':'v6','phase':'fin','branch':{'of':'v5','when':'ok'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':SA_PRE},'fail':{'goto':'self','via':SA_ANN,'lost':'v2'},'ts':'10:20'},
  {'id':'vm1','phase':'fin','branch':{'of':'v5','when':'miss'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':[{'gi':sa_spell,'tmax':2}]+SA_PRE},'fail':{'goto':'self','via':SA_ANN,'lost':'v2'},'ts':'10:20'},
  {'id':'v7','phase':'fin','do':'note','optional':True,'target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('완벽한 철 룬','Perfect Iron Rune')]},'ts':'14:30',
   'note':K('선택: 완벽한 철 룬·신성한 오브로 에너지 보호막 400·450 같은 기준선 넘기기.','Optional: Perfect Iron Rune or Divine to push energy shield past round marks like 400 or 450.')},
 ]})
