# ---- SaVeQ "서리 기둥 수익 마법봉" (youtu.be/qdyfBnzqBLo, 2026-09-09, 0.5.5) — 조사 g91(docs/craft-guides.md 5차), RECIPE-B 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_saveq_profit_wand.py(saveq-profit-wand-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 0(입문) → 에센셜만(10장 C11). 영상은 빗나감을 처리하지 않고 결과 그대로 판매.
c='Wands'
R.append({
 'id':'saveq-profit-wand-v2-ess','tierGroup':'saveq-profit-wand-v2','tier':'ess','tierLabel':K('에센셜','Essential'),
 'cls':c,'base':base(c,'Twisted Wand'),'ilvl':81,'difficulty':0,'budget':'low','basePrice':0.5,
 'buildTags':[K('냉기 주문','Cold spells'),K('주문 피해','Spell damage'),K('판매용','For sale')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=qdyfBnzqBLo','title':'서리 기둥 수익 마법봉 (냉기 주문 레벨 매직 → 마술의 에센스 → 강령술 원소 피해 훼손 → 상위 찬미 엑잘)','channel':'SaVeQ'},
 'title':K('냉기 주문 스킬 레벨 + 주문 피해 에센스 + 원소 피해 훼손 수익용 마법봉','cold spell levels + spell damage essence + desecrated elemental damage wand for profit'),
 'start':{'rar':'magic','mods':[{'gi':12,'tmax':2}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'3:05','note':K('냉기 주문 스킬 레벨 매직 뒤틀린 마법봉(아이템 레벨 81, 약 0.5 div).','A magic Twisted Wand with cold spell skill levels (item level 81, about 0.5 div).')},
  {'id':'a1','phase':'base','do':'augment','cur':'Greater_Orb_of_Augmentation','ts':'3:05','target':{'junk':'p'}},
  {'id':'e1','phase':'base','do':'essence','cur':'Greater_Essence_of_Sorcery','target':{'gi':44}},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'ts':'3:36','target':{'unrev':'p'}},
  {'id':'d2','phase':'main','do':'reveal','target':{'reveal':{'gi':30},'side':'p','bone':'Preserved_Jawbone','anyReveal':True}},
  {'id':'x1','phase':'main','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'ts':'5:07','target':{'junk':['s','s']}},
  {'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')}]})
