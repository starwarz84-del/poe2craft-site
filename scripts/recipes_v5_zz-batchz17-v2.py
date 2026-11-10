# ---- 2026-11-10 batch 17 (사용자: 다음 작업): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch17.py. Videos rechecked (transcripts). ----
def _breach(r, t):
    _drop(r,'c16')   # 디바인·축성·타락은 선택 (정책 23)
    c7=_node(r,'c7'); c7['target']={'setQuality':66}; c7['label']=K('바알 촉진시키는 주입기 1개','One Vaal Catalysing Infuser')   # 영상: 처음 1번은 100% 성공, 그 뒤는 타락 위험
    # 영상: 엑잘이 빗나가면 소멸의 오브로 지우고 다시 (희귀도·저항이 지워지면 카오스 오브부터)
    _node(r,'c9')['fail']={'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'c8'}
    if t=='bal':
        for nid in ('c12','c13'):
            for x in _node(r,nid)['target']['anyOf']: x['tmax']=2
        for x in _node(r,'c15')['target']['reveal']['anyOf']: x['tmax']=2
for _t in ('high','bal'): _grade8('breach-ring-video','breach-ring-video-v2',_t,_breach)

def _sqfocus(r, t):
    _drop(r,'q8')   # 완벽한 철 룬은 취향 (정책 23)
    if t=='bal': _node(r,'q7')['target']['reveal']['tmax']=2
for _t in ('high','bal'): _grade8('saveq-focus','saveq-focus-v2',_t,_sqfocus)
