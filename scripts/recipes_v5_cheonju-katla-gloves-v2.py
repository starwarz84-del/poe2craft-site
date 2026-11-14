# ---- 천주 "화염파 젬링 장갑" (youtu.be/UwlQO3Qf6ZI, 2026-09-28, 0.5.5) — 조사 g83(docs/craft-guides.md 5차), RECIPE-B 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_cheonju_katla_gloves.py(cheonju-katla-gloves-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 3(어려움 — 분열 빗나감으로 베이스 약 3개) → 밸런스(영상 흐름)·에센셜(공개 결과 그대로).
c='Gloves_dex_int'
def _ckg(tier):
    R.append({
 'id':'cheonju-katla-gloves-v2-'+tier,'tierGroup':'cheonju-katla-gloves-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Secured Wraps'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'high' if tier=='bal' else 'medium',
 'buildTags':[K('상태 이상','Ailments'),K('카틀라의 순흑','Katla’s Gloom'),K('화염파','Flameblast')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('천주 영상 기반','Based on 천주'),
 'source':{'url':'https://www.youtube.com/watch?v=UwlQO3Qf6ZI','title':'화염파 젬링 장갑 (카틀라의 순흑 접두 3개)','channel':'천주'},
 'title':K('상태 이상 강도 분열 + 카틀라 접두 2개 + 경악의 에센스·신비한 합금','fractured ailment magnitude + two Katla prefixes + Horror essence and Mystic Alloy'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'1:12','note':K('특출난 고정된 싸개(노멀, 아이템 레벨 82, 증강 홈 2개).','Exceptional Secured Wraps (normal, item level 82, two augment sockets).')},
  {'id':'rk','phase':'base','do':'socket','ts':'2:04','target':{'rune':K('카틀라의 순흑','Katla’s Gloom')}},
  {'id':'t1','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','ts':'2:04','target':{'junk':'p'}},
  {'id':'d0','phase':'base','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'ts':'3:05','target':{'unrev':'p'}},
  {'id':'f0','phase':'base','do':'fracture','cur':'Fracturing_Orb','ts':'8:19','target':{'gi':89}},
  {'id':'c1','phase':'main','do':'chaos','cur':'Chaos_Orb','ts':'8:49','target':{'gi':90,'tmax':1}},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'ts':'11:02','target':{'unrev':'p'}},
  {'id':'d2','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'ts':'17:11','target':{'reveal':{'gi':86},'side':'p','bone':'Preserved_Rib'}},
  {'id':'s1','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'ts':'19:10','target':{'junk':['s','s']}},
  {'id':'rn','phase':'main','do':'socket','ts':'20:18','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")}},
  {'id':'s2','phase':'main','do':'essence','cur':'Essence_of_Horror','omens':['Omen_of_Dextral_Crystallisation'],'ts':'21:20','target':{'gi':62}},
  {'id':'s3','phase':'main','do':'essence','cur':'Mystic_Alloy','omens':['Omen_of_Dextral_Crystallisation'],'ts':'21:20','target':{'gi':72}},
  {'id':'s4','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','ts':'22:22','target':{'junk':'s'}},
  {'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')}]})
for _t in ('bal','ess'): _ckg(_t)
