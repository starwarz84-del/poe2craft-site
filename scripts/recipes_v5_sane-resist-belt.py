# ---- TheSaneExile "PoE2 0.5.5 - Craft your resistance Belt/Rings for half price on leaguestart" (youtu.be/Zop328DR50Q) ----
SANE=K('TheSaneExile 영상 기반','Based on TheSaneExile')
c='Belts'
def textS(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sb_life=textS('to maximum Life','n','p'); sb_lres=textS('to Lightning Resistance','n','s')
sb_cresE=textS('to Chaos Resistance','e','s'); sb_ulaman=textS('to Lightning and Chaos Resistances','d','s')
R.append({
 'id':'sane-resist-belt','cls':c,'base':base(c,'Fine Belt'),'ilvl':81,'difficulty':1,'budget':'low',
 'buildTags':[K('저항','Resistances'),K('카오스 저항','Chaos resistance'),K('리그 초반','League start')],'patch':'0.5.5','created':'2026-11-09','author':SANE,
 'source':{'url':'https://www.youtube.com/watch?v=Zop328DR50Q','title':'PoE2 0.5.5 - Craft your resistance Belt/Rings for half price on leaguestart','channel':'TheSaneExile'},
 'title':K('생명력 + 번개 저항 + 카오스 저항 + 울라만 번개·카오스 저항','life + lightning res + chaos res + Ulaman lightning/chaos res'),
 'start':{'rar':'magic','mods':[{'gi':sb_life,'tmax':1},{'gi':sb_lres,'tmax':2}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 훼손','en':'Suffix desecration'}],
 'nodes':[
  {'id':'b1','phase':'base','do':'base','cost':'base','ts':'0:12',
   'note':K('생명력 + 저항이 붙은 매직 허리띠(부적 칸 2개 이상).','A magic belt with life and a resistance (two or more charm slots).')},
  {'id':'b2','phase':'base','do':'essence','cur':'Greater_Essence_of_Ruin','target':{'gi':sb_cresE},'ts':'1:18'},
  {'id':'b3','phase':'suf','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Sovereign'],'target':{'unrev':'s'},'ts':'1:37'},
  {'id':'b4','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':sb_ulaman},'side':'s','lord':'ulaman','bone':'Preserved_Collarbone'},'fail':{'goto':'b3','via':LIGHT},'ts':'2:25',
   'br':K('대박 → 완성, 실패: 빛의 징조 + 소멸의 오브로 지우고 다시 훼손','hit → done; miss: Omen of Light + Annulment and desecrate again')},
  {'id':'b5','phase':'suf','do':'note','ts':'2:58',
   'note':K('완성. 접두 2자리는 비어 있음.','Done; two prefix slots stay open.')},
 ],
})
