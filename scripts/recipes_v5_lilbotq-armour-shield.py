# ---- LilBotQ "How I Crafted a 2000 Armour Shield - Path of Exile 2 Crafting Guide" (youtu.be/4YOSSAa53UU) ----
LBQ=K('LilBotQ 영상 기반','Based on LilBotQ')
c='Shields_str'
def textL(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
lq_flat=textL('to Armour','n','p'); lq_pct=textL('increased Armour','n','p'); lq_hyb=textL('increased Armour\n+','n','p')
LQ_IRON=K('완벽한 철 룬','Perfect Iron Rune')
R.append({
 'id':'lilbotq-armour-shield','cls':c,'base':base(c,'Tawhoan Tower Shield'),'ilvl':81,'sockets':2,'exceptional':{'sockets':1},'difficulty':2,'budget':'medium',
 'buildTags':[K('방어도','Armour'),K('방패 벽','Shield Wall'),K('방패','Shield')],'patch':'0.5.5','created':'2026-11-09','author':LBQ,
 'source':{'url':'https://www.youtube.com/watch?v=4YOSSAa53UU','title':'How I Crafted a 2000 Armour Shield - Path of Exile 2 Crafting Guide','channel':'LilBotQ'},
 'title':K('방어도 분열 + 방어도 % + 훼손 방어도·기절 한계 (방어도 2000)','fractured flat armour + % armour + desecrated armour/stun hybrid (2000 armour)'),
 'start':{'rar':'rare','quality':28,'mods':[{'gi':lq_flat,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'rune','kr':'룬','en':'Runes'},{'id':'suf','kr':'접미','en':'Suffixes'}],
 'nodes':[
  {'id':'l1','phase':'pre','do':'base','cost':'base','ts':'0:59',
   'note':K('퀄리티 28%(바알 방어구 장인의 주입기). 방어도 1티어 분열 + 잡옵 1개.','28% quality (Vaal Armourer\'s Infuser). Fractured T1 flat armour plus one junk line.')},
  {'id':'l2','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'gi':lq_pct,'tmax':1},'fail':{'goto':'self'},'ts':'5:49'},
  {'id':'l3','phase':'pre','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'7:28'},
  {'id':'l4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':lq_hyb,'tmax':1},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'l3','via':LIGHT},'ts':'7:37',
   'br':K('대박 → 다음, 실패: 빛의 징조 + 소멸의 오브로 지우고 다시 훼손. 팔 용도면 낮은 티어로 타협','hit → next; miss: Omen of Light + Annulment and desecrate again (settle for a lower tier when selling)')},
  {'id':'l5','phase':'rune','do':'manual','target':{'rune':LQ_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'8:37'},
  {'id':'l6','phase':'rune','do':'manual','target':{'rune':LQ_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'8:43'},
  {'id':'l7','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'9:44',
   'note':K('접미는 아무거나(영상: 저항 옵션 2개).','Any suffixes (two resistances in the video).')},
  {'id':'l8','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'10:05',
   'note':K('완성. 신성한 오브로 방어도 수치 정리(영상 2015).','Done; Divine the armour rolls (2015 in the video).')},
 ],
})
