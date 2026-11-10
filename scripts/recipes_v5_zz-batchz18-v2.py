# ---- 2026-11-10 batch 18 (사용자: 나머지도 2개씩): 극한 → High-end (video) + Balance. Matches scripts/graphs/gen_batch18.py. Videos rechecked (transcripts). ----
def _proj7(r, t):
    if t=='bal':
        v7=_node(r,'v7'); v7.pop('fail',None); v7['br']=KEEP   # 관통 공개 결과 그대로
for _t in ('high','bal'): _grade8('sl-proj7-gloves','sl-proj7-gloves-v2',_t,_proj7)

def _iceshot(r, t):
    _drop(r,'w16')   # 신성한 오브·룬 교체·타락은 선택 (정책 23)
    w8=_node(r,'w8'); el=w8['target']['anyOf']
    tm=2 if t=='high' else 3   # 영상: 냉기가 좋지만 다른 원소·복합 물리도 받음
    for x in el: x['tmax']=tm
    if t=='bal':
        _node(r,'w7')['target']['tmax']=3
        _node(r,'w12')['target']['reveal']['tmax']=2   # 투사체 +3도 받음
        _node(r,'w14')['target']['tmax']=3
for _t in ('high','bal'): _grade8('diztoh-iceshot-bow','diztoh-iceshot-bow-v2',_t,_iceshot)
