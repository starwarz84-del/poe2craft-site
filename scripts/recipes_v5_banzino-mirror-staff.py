# ---- 반지깎는노인 "[패스 오브 엑자일 2] 미러 지팡이 제작 방법" (youtu.be/vT482uJFESs, 0.4 무렵 → 0.5.5 응용, 정책 15) ----
# 플로우차트(scripts/graphs/gen_batch25.py)를 따라 작성(정책 31). 같은 단계 id. 영상 기록 tools/notes/banzino-vT482uJFESs.md
BZN=K('반지깎는노인 영상 기반','Based on 반지깎는노인')
c='Staves'
bz_spd,bz_l7,bz_cast,bz_crit,bz_light,bz_xl,bz_mark=3,16,25,26,7,34,56
BZ_PRE=[{'gi':bz_light,'tmax':1},{'gi':bz_xl,'tmax':1}]
LIGHT_BZ={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'banzino-mirror-staff','cls':c,'base':base(c,'Voltaic Staff'),'ilvl':82,'difficulty':5,'budget':'mirror',
 'buildTags':[K('번개','Lightning'),K('주문','Spell'),K('치명타','Critical')],'patch':'0.5.5','adaptedFrom':'0.4','created':'2026-11-11','author':BZN,
 'source':{'url':'https://www.youtube.com/watch?v=vT482uJFESs','title':'[패스 오브 엑자일 2] 미러 지팡이 제작 방법','channel':'반지깎는노인'},
 'title':K('주문 피해 분열 + 번개 주문 +7 + 시전 속도 + 주문 치명타 + 번개 피해 접두 2개','fractured spell damage + lightning spells +7 + cast speed + spell crit + two lightning prefixes'),
 'start':{'rar':'rare','mods':[{'gi':bz_spd,'tmax':1,'fr':True},{'junk':'p'},{'junk':'p'},{'junk':'s'},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'m0','phase':'suf','do':'base','cost':'base','ts':'5:38','note':K('주문 피해 % 1티어 분열 전도성 지팡이, 옵션 6개가 모두 찬 상태.','A Voltaic Staff with fractured T1 spell damage and all six slots filled.')},
  {'id':'s1','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':bz_l7,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'5:50'},
  {'id':'s2','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'gi':bz_cast,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'6:20'},
  {'id':'s3','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'gi':bz_crit,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'6:25'},
  {'id':'p1','phase':'pre','do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'mark':{'gi':bz_mark}},'ts':'7:11'},
  {'id':'p2','phase':'pre','do':'desecrate','cur':'Ancient_Jawbone','target':{'unrev':'p','fromMark':True},'ts':'7:20'},
  {'id':'p3','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':BZ_PRE},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'p4'},'ts':'7:25'},
  {'id':'pT','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Sinistral_Erasure'],'branch':{'of':'p3','when':'ok'},'target':{'anyOf':BZ_PRE,'replace':'p'},'fail':{'goto':'self'},'ts':'9:14'},
  {'id':'p4','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'branch':{'of':'p3','when':'miss'},'target':{'removeDes':True},'ts':'7:41'},
  {'id':'p5','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'branch':{'of':'p3','when':'miss'},'target':{'anyOf':BZ_PRE},'fail':{'goto':'pT'},'ts':'8:11'},
 ]})
