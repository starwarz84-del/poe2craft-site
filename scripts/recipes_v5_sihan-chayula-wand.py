# ---- 시한 "[POE2 0.5.5] 차율라 부패운반자 장비 제작｜마법봉 제작 가이드｜매물이 없다면 직접 만들자!" (youtu.be/rSs4fumlHo4) ----
c='Wands'
SHW=K('시한 영상 기반','Based on 시한')
def textW(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
cw_chaos=textW('increased Chaos Damage','n','p'); cw_scrit=textW('increased Critical Hit Chance for Spells','n','s')
cw_int=textW('to Intelligence','n','s'); cw_mreg=textW('increased Mana Regeneration Rate','n','s'); cw_cast=textW('increased Cast Speed','n','s')
cw_spell3=textW('+3 to Level of all Spell Skills','e','s'); cw_cel=textW('to Level of all Spell Skills','e','p'); cw_ula=textW('of Damage as Extra Physical Damage','d','p')
R.append({
 'id':'sihan-chayula-wand','cls':c,'base':base(c,'Attuned Wand'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('카오스','Chaos'),K('주문','Spell'),K('차율라','Chayula')],'patch':'0.5.5','created':'2026-11-11','author':SHW,
 'source':{'url':'https://www.youtube.com/watch?v=rSs4fumlHo4','title':'[POE2 0.5.5] 차율라 부패운반자 장비 제작｜마법봉 제작 가이드｜매물이 없다면 직접 만들자!','channel':'시한'},
 'title':K('카오스 피해 분열 + 주문 +3 에센스 + 천공의 합금 + 울라만 추가 물리 피해','fractured chaos damage + spell +3 essence + Celestial Alloy + Ulaman extra physical'),
 'start':{'rar':'rare','mods':[{'gi':cw_chaos,'tmax':2,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fix','kr':'확정 제작','en':'Deterministic finish'}],
 'nodes':[
  {'id':'w1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('룬 소켓 2개(특출난) 마법봉, 카오스 피해 분열 + 잡옵 1개. 베이스 이름은 상관없음.','Two-socket (exceptional) wand with fractured chaos damage plus one junk line; the base type does not matter.')},
  {'id':'w2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':cw_scrit,'tmax':2},'fail':{'goto':'self'},'ts':'0:42'},
  {'id':'w3','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':cw_int,'tmax':2},{'gi':cw_mreg,'tmax':2},{'gi':cw_cast,'tmax':2}]},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'w2'},'ts':'4:43'},
  {'id':'w4','phase':'fix','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'5:40'},
  {'id':'w5','phase':'fix','do':'essence','cur':'Perfect_Essence_of_Sorcery','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':cw_spell3,'chance':1},'ts':'6:07'},
  {'id':'w6','phase':'fix','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'6:28'},
  {'id':'w7','phase':'fix','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'p'},'ts':'6:34'},
  {'id':'w8','phase':'fix','do':'essence','cur':'Celestial_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':cw_cel,'chance':1},'ts':'6:55'},
  {'id':'w9','phase':'fix','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_the_Sovereign'],'target':{'unrev':'p'},'ts':'7:21'},
  {'id':'w10','phase':'fix','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':cw_ula},'side':'p','lord':'ulaman','bone':'Preserved_Jawbone'},'fail':{'goto':'w9','via':LIGHT},'ts':'7:40'},
  {'id':'w11','phase':'fix','do':'note','ts':'8:00','note':K('완성. 무기 세트 2의 능력치가 모자라 접미 두 번째 옵션은 지능이 가장 좋음.','Done; weapon set 2 runs short on attributes, so intelligence is the best second suffix.')},
 ]})
