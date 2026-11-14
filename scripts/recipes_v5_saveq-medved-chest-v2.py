# ---- SaVeQ "메드베드 정신력 갑옷" (youtu.be/5puSqTO0AKM, 2026-10-11, 0.5.5) — 조사 g87(docs/craft-guides.md 5차), RECIPE-B 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_saveq_medved_chest.py(saveq-medved-chest-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 4(전문가) → 하이엔드(영상: 접미 저항·지능 1티어)·밸런스(1~2티어). 메드베드 옵션 가중치는 추정.
c='Body_Armours_int'
def _smc(tier):
    R.append({
 'id':'saveq-medved-chest-v2-'+tier,'tierGroup':'saveq-medved-chest-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance')}[tier],
 'cls':c,'base':base(c,'Flowing Raiment'),'ilvl':82,'difficulty':4,'budget':'high','basePrice':4,
 'buildTags':[K('정신력','Spirit'),K('메드베드의 보살핌','Medved’s Tending'),K('토템','Totems')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=5puSqTO0AKM','title':'메드베드 정신력 갑옷 (정신력 분열 → 메드베드 정신력·마나 % → 정신력 점유 효율 훼손)','channel':'SaVeQ'},
 'title':K('정신력 분열 + 메드베드 정신력 %·최대 마나 % + 정신력 점유 효율 훼손','fractured Spirit + Medved % Spirit and % maximum Mana + desecrated Spirit reservation efficiency'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'0:32','note':K('흐르는 의복(노멀, 아이템 레벨 82, 약 4 div).','A Flowing Raiment (normal, item level 82, about 4 div).')},
  {'id':'c0','phase':'base','do':'chaos','cur':'Chaos_Orb','ts':'6:14','target':{'gi':14,'tmax':1}},
  {'id':'d0','phase':'base','do':'desecrate','cur':'Preserved_Rib','ts':'8:26','target':{'unrev':'s'}},
  {'id':'f0','phase':'base','do':'fracture','cur':'Fracturing_Orb','ts':'8:26','target':{'gi':14}},
  {'id':'rn','phase':'main','do':'socket','ts':'9:30','target':{'rune':K('메드베드의 보살핌','Medved’s Tending')}},
  {'id':'c1','phase':'main','do':'chaos','cur':'Chaos_Orb','ts':'9:30','target':{'anyOf':[{'gi':51},{'gi':50}]}},
  {'id':'e1','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'ts':'23:59','target':{'gi':50}},
  {'id':'s1','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'ts':'24:30','target':{'junk':['s','s']}},
  {'id':'s2','phase':'main','do':'chaos','cur':'Chaos_Orb','ts':'24:30','target':{'gi':0}},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Preserved_Rib','ts':'25:34','target':{'unrev':'s'}},
  {'id':'d2','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'ts':'26:53','target':{'reveal':{'gi':21},'side':'s','bone':'Preserved_Rib'}},
  {'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')}]})
for _t in ('high','bal'): _smc(_t)
