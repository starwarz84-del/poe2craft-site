# ---- Kite_xdd "싼 ES 티아라 대량 제작" (youtu.be/GQAf_p5GeiQ, 2026-09-13, 0.5.5, 러시아어) — 조사 g114(docs/craft-guides.md 6차), RECIPE-D 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_kite_budget_es_tiara.py(kite-budget-es-tiara-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 1(쉬움, 반복 없음) → 에센셜만. 영상은 빗나간 것을 그대로 판매.
c='Helmets_int'
R.append({
 'id':'kite-budget-es-tiara-v2-ess','tierGroup':'kite-budget-es-tiara-v2','tier':'ess','tierLabel':K('에센셜','Essential'),
 'cls':c,'base':base(c,'Ancestral Tiara'),'ilvl':81,'difficulty':1,'budget':'low',
 'buildTags':[K('에너지 보호막','Energy shield'),K('가성비','Budget'),K('판매용','For sale')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('Kite_xdd 영상 기반','Based on Kite_xdd'),
 'source':{'url':'https://www.youtube.com/watch?v=GQAf_p5GeiQ','title':'싼 ES 티아라 대량 제작 (매직 → 완벽한 확장·제왕 → 좌측 찬미 + 상위 엑잘 → 좌측 강령술 훼손 → 메아리 공개)','channel':'Kite_xdd'},
 'title':K('분열 없는 에너지 보호막 접두 3개 티아라','three energy shield prefixes on a tiara without fracturing'),
 'start':{'rar':'magic','mods':[{'gi':8}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'0:01','note':K('에너지 보호막 % 매직 선대의 티아라(아이템 레벨 81, 1 카오스~20 엑잘). 여러 개를 사서 1 div어치 한 번에 돌림.','A magic Ancestral Tiara with % energy shield (item level 81, 1 chaos to 20 exalts). Buy several, about 1 div worth, and craft them in one go.')},
  {'id':'a1','phase':'base','do':'augment','cur':'Perfect_Orb_of_Augmentation','ts':'0:52','target':{'junk':'s'}},
  {'id':'r1','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','ts':'1:39','target':{'junk':'s'}},
  {'id':'x1','phase':'main','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'ts':'2:25','target':{'junk':'p'}},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'ts':'3:55','target':{'unrev':'p'}},
  {'id':'x2','phase':'main','do':'exalt','cur':'Greater_Exalted_Orb','ts':'3:55','target':{'junk':'s'}},
  {'id':'d2','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'ts':'4:40','target':{'reveal':{'gi':9},'side':'p','bone':'Preserved_Rib','anyReveal':True}},
  {'id':'ok','phase':'main','do':'note','note':K('완성. 영상은 철의 룬을 끼우고 그대로 판매(550 ES 하나 80 div, 나머지 7~18 div).','Done. The video sockets an Iron Rune and sells as is (one 550 ES piece at 80 div, the rest 7–18 div).')}]})
