# ---- ccs "오일 수류탄 정신력 석궁" (youtu.be/72ckN2hCgCU, 2026-09-12, 0.5.5) — 조사 g107(docs/craft-guides.md 6차), RECIPE-D 2026-11-14 등록 ----
# 플로우차트 scripts/graphs/gen_ccs_amanamu_crossbow.py(ccs-amanamu-crossbow-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 0(입문) → 에센셜만(10장 C11). 바알 오브 홈 4개·영혼 핵은 타락이라 뺌.
c='Crossbows'
R.append({
 'id':'ccs-amanamu-crossbow-v2-ess','tierGroup':'ccs-amanamu-crossbow-v2','tier':'ess','tierLabel':K('에센셜','Essential'),
 'cls':c,'base':base(c,'Cannonade Crossbow'),'ilvl':79,'sockets':2,'exceptional':{'sockets':1},'difficulty':0,'budget':'low','basePrice':0.004,
 'buildTags':[K('수류탄','Grenade'),K('정신력','Spirit'),K('아마나무','Amanamu')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('ccs 영상 기반','Based on ccs'),
 'source':{'url':'https://www.youtube.com/watch?v=72ckN2hCgCU','title':'오일 수류탄 젬링 석궁 (변화 → 에센스 → 아마나무 훼손 정신력 점유 효율)','channel':'ccs'},
 'title':K('상위 가속의 에센스 + 아마나무 훼손 정신력 점유 효율 석궁','Greater Essence of Haste + Amanamu desecrated spirit reservation efficiency crossbow'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'b0','phase':'base','do':'base','cost':'base','ts':'1:02','note':K('홈 3개 노멀 석궁(아무 종류, 1~2 엑잘). 피해·공격 속도·스킬 레벨은 상관없음.','A normal crossbow with three sockets (any type, 1–2 exalts). Damage, attack speed and skill levels do not matter.')},
  {'id':'t1','phase':'base','do':'transmute','cur':'Orb_of_Transmutation','ts':'1:33','target':{'junk':'p'}},
  {'id':'e1','phase':'base','do':'essence','cur':'Greater_Essence_of_Haste','ts':'2:03','target':{'gi':44}},
  {'id':'d1','phase':'main','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Liege'],'ts':'2:03','target':{'unrev':'s'}},
  {'id':'d2','phase':'main','do':'reveal','target':{'reveal':{'gi':29},'side':'s','lord':'amanamu','bone':'Preserved_Jawbone'}},
  {'id':'ok','phase':'main','do':'note','note':K('완성. 영상은 이어서 바알 오브로 홈 4개(실패면 새 베이스)를 노리고 영혼 핵 4개로 정신력을 채움.','Done. The video then aims for a fourth socket with a Vaal Orb (a new base on failure) and fills four soul cores for spirit.')}]})
