# ---- SaVeQ "ES·마나 장화" (youtu.be/5ngxdC6xY6Q, 2026-09-18, 0.5.5) — 조사 g89(docs/craft-guides.md 5차), RECIPE-B 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_saveq_es_mana_boots.py(saveq-es-mana-boots-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 3(어려움 — 분열 빗나감으로 베이스 약 3개) → 밸런스(영상 흐름, 1~2티어)·에센셜(1~4티어, 공개 결과 그대로). 축성은 선택 단계.
c='Boots_int'
def _seb(tier):
    R.append({
 'id':'saveq-es-mana-boots-v2-'+tier,'tierGroup':'saveq-es-mana-boots-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Luxurious Slippers'),'ilvl':82,'difficulty':3,'budget':'high' if tier=='bal' else 'medium','basePrice':1,
 'buildTags':[K('에너지 보호막','Energy shield'),K('마나','Mana'),K('이동 속도','Movement speed')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=5ngxdC6xY6Q','title':'ES·마나 장화 (완벽한 진화 → 제왕 → 분열 → 이동 속도 훼손 → 아스트리드 접미 2개 → 축성)','channel':'SaVeQ'},
 'title':K('저항 분열 + 마나·에너지 보호막 + 이동 속도 훼손 + 경악의 에센스·신비한 합금','fractured resistance + mana and energy shield + desecrated movement speed + Horror essence and Mystic Alloy'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'2:03','note':K('호화로운 슬리퍼(노멀, 아이템 레벨 82, 약 1 div).','Luxurious Slippers (normal, item level 82, about 1 div).')},
  {'id':'t1','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','ts':'2:03','target':{'anyOf':[{'gi':1,'tmax':1},{'gi':2,'tmax':1},{'gi':3,'tmax':1}]}},
  {'id':'r1','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','ts':'4:40','target':{'junk':'p'}},
  {'id':'d0','phase':'base','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'ts':'5:11','target':{'unrev':'p'}},
  {'id':'f0','phase':'base','do':'fracture','cur':'Fracturing_Orb','ts':'5:11','target':{'gi':3}},
  {'id':'p1','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'ts':'6:15','target':{'all':[{'gi':6},{'gi':8}]}},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'ts':'8:18','target':{'unrev':'p'}},
  {'id':'d2','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'ts':'15:29','target':{'reveal':{'gi':12},'side':'p','bone':'Ancient_Rib'}},
  {'id':'rn','phase':'main','do':'socket','ts':'8:48','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")}},
  {'id':'s1','phase':'main','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'ts':'8:48','target':{'junk':['s','s']}},
  {'id':'s2','phase':'main','do':'essence','cur':'Essence_of_Horror','ts':'8:48','target':{'gi':46}},
  {'id':'s3','phase':'main','do':'essence','cur':'Mystic_Alloy','ts':'8:48','target':{'gi':51}},
  {'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')}]})
for _t in ('bal','ess'): _seb(_t)
