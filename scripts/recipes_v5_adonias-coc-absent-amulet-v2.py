# ---- AdoniasHope 치명타 시 시전 부재 목걸이 (youtu.be/SOddUyQPIxQ, 2026-10-02) — RECIPE-A 2026-11-14 등록(정책 13장 사용자 확정 11-14 19:55) ----
# 플로우차트 scripts/graphs/gen_adonias_coc_absent_amulet.py(adonias-coc-absent-amulet-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 4(카오스 약 2,000개) → 하이엔드(영상: 시전 속도 1티어) · 밸런스(시전 속도 1~2티어).
def _ado_rec(tier):
    c='Amulets'
    TS={'b0':'2:34','k1':'3:06','e1':'4:06','w1':'4:06','d1':'5:08','r1':'5:08','r1x':'5:08'}
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','ts':TS['b0'],'note':K('분열 정신력 + 잡옵 1개 부재 목걸이(치명타 시 시전, 아이템 레벨 82).','An Absent Amulet with fractured Spirit + one junk option (Cast on Critical, item level 82).')}]
    for i,d in (('k1','chaos'),('e1','exalt'),('w1','chaos'),('kx','remove'),('d1','desecrate'),('r1','reveal'),('r1x','annul')):
        n={'id':i,'phase':'main','do':d}
        if i in TS: n['ts']=TS[i]
        nodes.append(n)
    nodes.append({'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')})
    R.append({
 'id':'adonias-coc-absent-amulet-v2'+('' if tier=='high' else '-'+tier),'tierGroup':'adonias-coc-absent-amulet-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance')}[tier],
 'cls':c,'base':base(c,'Absent Amulet'),'ilvl':82,'difficulty':4,'budget':'high',
 'buildTags':[K('정신력','Spirit'),K('주문','Spell'),K('시전 속도','Cast speed'),K('치명타 시 시전','Cast on Critical')],'patch':'0.5.5','created':'2026-11-14','author':K('AdoniasHope 영상 기반','Based on AdoniasHope'),
 'source':{'url':'https://www.youtube.com/watch?v=SOddUyQPIxQ','title':'AdoniasHope — Cast on Crit Absent Amulet craft (0.5.5)','channel':'AdoniasHope'},
 'title':K('분열 정신력 + 주문 +3 + 시전 속도 훼손','fractured Spirit + +3 spell skills + desecrated cast speed'),
 'start':{'rar':'rare','mods':[{'gi':28,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('high','bal'): _ado_rec(_t)
