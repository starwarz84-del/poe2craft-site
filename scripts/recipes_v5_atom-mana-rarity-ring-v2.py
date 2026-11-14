# ---- 사용자(Atom1q84) 직접 제작: 마나·희귀도·시전 속도 황금 반지 (2026-11-14, 영상 없음 — 운영자 레시피) ----
# 플로우차트 scripts/graphs/gen_atom_mana_rarity_ring.py(atom-mana-rarity-ring-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 표 2(보통) → 밸런스(공개 희귀도 1~2티어, 빛의 징조로 다시)·에센셜(공개 한 번, 결과 그대로).
c='Rings'
def _amr(tier):
    bal = tier=='bal'
    R.append({
 'id':'atom-mana-rarity-ring-v2-'+tier,'tierGroup':'atom-mana-rarity-ring-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Gold Ring'),'ilvl':82,'difficulty':2,'budget':'mid',
 'buildTags':[K('마나','Mana'),K('아이템 희귀도','Item rarity'),K('시전 속도','Cast speed')],'patch':'0.5.5','created':'2026-11-14','author':K('사용자 제작 방식','From the site owner\'s method'),
 'title':K('마나 최대치 + 최대 마나 % + 희귀도 옵션 2개 + 시전 속도','maximum mana + % maximum mana + double rarity + cast speed'),
 'start':{'rar':'magic','mods':[{'gi':10,'tmax':1},{'gi':34,'tmax':2}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':[
  {'id':'a0','phase':'base','do':'base','cost':'base','note':K('접두 마나 최대치 + 접미 시전 속도 매직 황금 반지(아이템 레벨 82).','A magic Gold Ring with prefix maximum mana and suffix cast speed (item level 82).')},
  {'id':'a1','phase':'base','do':'essence','cur':'Greater_Essence_of_Opulence','target':{'gi':66}},
  {'id':'a2','phase':'base','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
  {'id':'a3','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},
   'br':K('접미 세 번째 옵션은 나오는 대로 둠','The third suffix stays as it comes')},
  {'id':'a4','phase':'main','do':'essence','cur':'Perfect_Essence_of_the_Mind','target':{'gi':67}},
  {'id':'a6','phase':'main','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],
   'target':{'reveal':{'gi':28,'tmax':2},'side':'p','bone':'Preserved_Collarbone'} if bal else {'reveal':{'gi':28,'tmax':3},'side':'p','bone':'Preserved_Collarbone','anyReveal':True},
   **({'fail':{'goto':'self','via':LIGHT}} if bal else {'br':K('공개 결과 그대로, 다시 하지 않음','Keep whatever the reveal gives')})},
  {'id':'a7','phase':'main','do':'quality','cur':'Neural_Catalyst','target':{'quality':20}},
  {'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')}]})
for _t in ('bal','ess'): _amr(_t)
