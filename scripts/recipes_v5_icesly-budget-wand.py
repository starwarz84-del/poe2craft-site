# ---- Icesly "How to Craft a Budget-Friendly +7 Level Wand | League 0.5.5" (youtu.be/gtxAqZfCxxI, Thai) ----
IC5=K('Icesly 영상 기반','Based on Icesly')
c='Wands'
def textI(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
ic_l5=textI('+5 to Level of all Lightning Spell Skills','n','s')
ic_lin=textI('increased Lightning Damage','n','p'); ic_spell=textI('(105—119)% increased Spell Damage','n','p')
ic_xL=textI('Extra Lightning Damage','n','p'); ic_xC=textI('Extra Cold Damage','n','p'); ic_xF=textI('Extra Fire Damage','n','p')
ic_trans=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Transcendent Alloy' in [x[3] for x in gr['t']]][0]
ic_cel=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Celestial Alloy' in [x[3] for x in gr['t']]][0]
IC_PRE=[{'gi':ic_lin,'tmax':3},{'gi':ic_xL,'tmax':2},{'gi':ic_xC,'tmax':2},{'gi':ic_xF,'tmax':2},{'gi':ic_spell,'tmax':3}]
IC_ANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}
IC_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'icesly-budget-wand','cls':c,'base':base(c,'Dueling Wand'),'ilvl':81,'difficulty':2,'budget':'low',
 'buildTags':[K('번개','Lightning'),K('주문','Spell'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':IC5,
 'source':{'url':'https://www.youtube.com/watch?v=gtxAqZfCxxI','title':'How to Craft a Budget-Friendly +7 Level Wand | League 0.5.5','channel':'Icesly'},
 'title':K('번개 주문 +5 + 천공의 합금·초월의 합금 (가성비)','+5 lightning spells + Celestial and Transcendent Alloys (budget)'),
 'start':{'rar':'magic','mods':[{'gi':ic_l5,'tmax':1},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 합금','en':'Suffix alloy'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'천공의 합금','en':'Celestial Alloy'}],
 'nodes':[
  {'id':'i1','phase':'base','do':'base','cost':'base','ts':'0:59','note':K('모든 번개 주문 스킬 레벨 +5 매직 지팡이(아이템 레벨 81). 화염·냉기 등 다른 원소 +5도 같은 방법.','A magic wand with +5 to all lightning spell skills (item level 81). Other elements work the same way.')},
  {'id':'i2','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'s'},'ts':'1:41'},
  {'id':'i3','phase':'suf','do':'essence','cur':'Transcendent_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':ic_trans},'ts':'2:42'},
  {'id':'i4','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':IC_PRE},'fail':{'goto':'self','via':IC_ANN},'ts':'3:09',
   'br':K('나쁜 줄이면 그대로 두고 훼손 생략 → 천공의 합금이 지울 후보로.','A bad roll can stay: skip the desecration and let the Celestial Alloy take it.')},
  {'id':'i5','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':IC_PRE},'fail':{'goto':'self','via':IC_ANN,'lost':'i4'},'ts':'3:29'},
  {'id':'i6','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'p'},'ts':'3:46'},
  {'id':'i7','phase':'fin','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'4:20'},
  {'id':'i8','phase':'fin','do':'essence','cur':'Celestial_Alloy','target':{'gi':ic_cel,'chance':1/3,'missDrop':ic_xL},'ts':'4:38',
   'br':K('미공개 훼손이 지워지면 → 완성. 좋은 접두가 지워지면 → 남은 훼손을 공개.','Takes the unrevealed desecration → done; takes a good prefix → reveal the desecration.')},
  {'id':'i9','phase':'fin','branch':{'of':'i8','when':'miss'},'do':'reveal','target':{'reveal':{'anyOf':IC_PRE},'side':'p','bone':'Preserved_Jawbone'},'fail':{'goto':'self','via':IC_LIGHT},'ts':'5:40'},
 ]})
