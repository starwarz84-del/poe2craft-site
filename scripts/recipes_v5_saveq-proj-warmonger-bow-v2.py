# ---- SaVeQ 투사체 물리 활 (youtu.be/35uKJrlkZuo, 2026-10-26, 0.5.5, A-Z #3) — 조사 g105(docs/craft-guides.md 6차), RECIPE-C 2026-11-14 등록(정책 13장 C18) ----
# 플로우차트 scripts/graphs/gen_saveq_proj_warmonger_bow.py(saveq-proj-warmonger-bow-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 3(어려움 — 분열 빗나감으로 베이스 약 3개, 완벽한 확장 약 290개) → 밸런스(영상: 치명타 확률 2티어)·에센셜(1~4티어).
def _sqb_rec(tier):
    c='Bows'
    TS={'pb':'0:30','pt':'2:34','pa':'2:34','px':'2:34','pr':'6:08','pd':'6:08','pf':'6:08','pc':'7:09','p1':'7:09','p1x':'7:09','p2':'7:09','rn':'9:13','k2':'9:13','k3':'9:13','k4':'9:13','k4x':'9:13','u1':'19:47'}
    nodes=[{'id':'pb','phase':'base','do':'base','cost':'base','ts':TS['pb'],'note':K('노멀 전쟁광 활(아이템 레벨 81, 3 카오스, 퀄리티 30%).','A normal Warmonger Bow (item level 81, 3 Chaos, 30% quality).')}]
    for i,d,ph in (('pt','transmute','base'),('pa','augment','base'),('px','remove','base'),('pr','regal','base'),('pd','desecrate','base'),('pf','fracture','base'),
                   ('p1','exalt','main'),('p2','exalt','main'),('rn','socket','main'),('k2','essence','main'),('k3','desecrate','main'),('k4','reveal','main'),('k4x','essence','main'),('u1','exalt','main')):
        n={'id':i,'phase':ph,'do':d}
        if i in TS: n['ts']=TS[i]
        nodes.append(n)
    nodes.append({'id':'ok','phase':'main','do':'note','ts':'21:02','note':K('완성.','Done.')})
    R.append({
 'id':'saveq-proj-warmonger-bow-v2-'+tier,'tierGroup':'saveq-proj-warmonger-bow-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Warmonger Bow'),'ilvl':81,'difficulty':3,'budget':'high','basePrice':0.33,
 'buildTags':[K('물리','Physical'),K('투사체','Projectile'),K('치명타','Critical')],'patch':'0.5.5','created':'2026-11-14','author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=35uKJrlkZuo','title':'투사체 물리 활 (퀄리티 30 → 투사체 +4 분열 → 접두 엑잘 → 아스트리드 결정화 루프로 치명타 확률 훼손)','channel':'SaVeQ'},
 'title':K('투사체 +4 분열 + 물리 피해 % + 치명타 확률 훼손 활','fractured +4 projectiles + % physical + desecrated crit chance bow'),
 'start':{'rar':'normal','mods':[],'quality':30},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('bal','ess'): _sqb_rec(_t)
