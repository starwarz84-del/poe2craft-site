# ---- Fubgun "화염파 오일 수류탄 지팡이" 방법1 (youtu.be/WInrHPfAMd4, 2026-09-07, 0.5.5) — 조사 g100(docs/craft-guides.md 5차), RECIPE-B 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_fubgun_ulaman_staff.py(fubgun-ulaman-staff-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 0~1 → 에센셜만(10장 C11).
c='Staves'
R.append({
 'id':'fubgun-ulaman-staff-v2-ess','tierGroup':'fubgun-ulaman-staff-v2','tier':'ess','tierLabel':K('에센셜','Essential'),
 'cls':c,'base':base(c,'Ashen Staff'),'ilvl':82,'difficulty':1,'budget':'low','basePrice':1.5,
 'buildTags':[K('화염 주문','Fire spells'),K('상태 이상','Ailments'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('Fubgun 영상 기반','Based on Fubgun'),
 'source':{'url':'https://www.youtube.com/watch?v=WInrHPfAMd4','title':'화염파 오일 수류탄 지팡이 (울라만 훼손 → 마술의 에센스 +5)','channel':'Fubgun'},
 'title':K('주문 피해 + 추가 화염 피해 + 울라만 상태 이상 강도 + 주문 스킬 +5 지팡이','spell damage + extra fire + Ulaman ailment magnitude + +5 spell skills staff'),
 'start':{'rar':'rare','mods':[{'gi':3},{'gi':32},{'junk':'s'},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'3:14','note':K('주문 피해 + 추가 화염 피해 레어 잿빛 지팡이(아이템 레벨 82, 접미 3개, 1~2 div).','A rare Ashen Staff with spell damage + extra fire damage (item level 82, three suffixes, 1–2 div).')},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_the_Sovereign'],'ts':'3:14','target':{'unrev':'p'}},
  {'id':'d2','phase':'main','do':'reveal','target':{'reveal':{'gi':48},'side':'p','bone':'Preserved_Jawbone','lord':'ulaman'}},
  {'id':'e1','phase':'main','do':'essence','cur':'Perfect_Essence_of_Sorcery','ts':'4:35','target':{'gi':55}},
  {'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')}]})
