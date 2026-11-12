# ---- 2026-11-10 batch 17 (사용자: 다음 작업): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch17.py. Videos rechecked (transcripts). ----
def _breach(r, t):
    _drop(r,'c16')   # 디바인·축성·타락은 선택 (정책 23)
    # 2026-11-12 W9 영상 전체 재대조: 단계는 플로우차트(scripts/graphs/gen_batch17.py)를 그대로 읽음. 여기서는 같은 id 단계에 영상 시각·꿀팁만 붙임
    _b=next(n for n in r['nodes'] if n.get('do')=='base'); _b['ts']='5:35'
    for _nid,_ts,_tp in [('pc','24:55',None),('pe','25:05',None),('pb','25:35',None),('pf','26:25',['breach-ring-fracture-first']),('p8','26:43',None),
                         ('q1','7:35',None),('q2','7:00',None),('q3','7:50',None),('s1','27:48',None),('s2','28:05',None),('p0','28:17',None),('p0b','28:21',None),
                         ('p1','29:00',None),('d1','29:20',None),('d2','29:25',None)]:
        _x={'id':_nid,'do':'note','ts':_ts}
        if _tp: _x['tips']=_tp
        r['nodes'].append(_x)
for _t in ('high','bal'): _grade8('breach-ring-video','breach-ring-video-v2',_t,_breach)

def _sqfocus(r, t):
    _drop(r,'q8')   # 완벽한 철 룬은 취향 (정책 23)
    if t=='bal': _node(r,'q7')['target']['reveal']['tmax']=2
for _t in ('high','bal'): _grade8('saveq-focus','saveq-focus-v2',_t,_sqfocus)
