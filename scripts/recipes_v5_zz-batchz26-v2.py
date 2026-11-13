# ---- 2026-11-11 batch 26: 웹 글 기반 6개 (플로우차트 scripts/graphs/gen_batch26.py와 같은 단계 id, 정책 30·31·32) ----
# 밸런스 = 원본(공개는 빛의 징조로 다시, 엑잘은 완벽한 엑잘티드 오브), 에센셜 = 더 싼 베이스·공개 결과 그대로·상위 엑잘티드 오브.
def _keep(n): n.pop('fail',None); n['br']=KEEP
def _web26(start_t, reveals, exalts):
    def ed(r, t):
        if t!='ess': return
        for i,tm in start_t.items(): r['start']['mods'][i]['tmax']=tm
        for nid in reveals: _keep(_node(r,nid))
        for nid in exalts: _node(r,nid)['cur']='Greater_Exalted_Orb'
    return ed
for _id,_st,_rv,_ex in (('fubgun-quiver',{0:2},['q4'],['q5']),('fubgun-phys-bow',{0:4},['b4'],['b5']),('fubgun-crit-bow',{0:4},['b4'],['b5']),
                         ('fubgun-proj-amulet',{},['a9'],[]),('fubgun-es-helmet',{},['e4'],[]),('bigdaddy-lightning-wand',{},['w5','w9'],['w6'])):
    for _t in (('bal',) if _id=='fubgun-es-helmet' else ('bal','ess')): _grade8(_id,_id+'-v2',_t,_web26(_st,_rv,_ex))   # 2026-11-13 P2: ES 투구는 빛의 징조 반복을 빼니 밸런스 = 에센셜 비용(10% 이내) → 밸런스만(정책 D)
