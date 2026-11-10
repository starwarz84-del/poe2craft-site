# ---- 2026-11-10 batch 21 (사용자: 나머지 2개): MazBro BiS 셉터 · XenoARPG 물리 석궁 → 둘 다 극한 = High-end only. Matches scripts/graphs/gen_batch21.py. ----
def _sceptre(r, t):
    _drop(r,'z15')   # 신성한 오브·룬 교체는 취향(정책 23)
for _t in ('high',): _grade8('mazbro-sceptre','mazbro-sceptre-v2',_t,_sceptre)

def _xeno(r, t):
    # 상위 철 룬·숫돌·신성한 오브는 취향(정책 23)
    _drop(r,'x11','x12','x13','x14','x15')
    # 사용자 확정 2026-11-10: 활·양손 무기 하이엔드는 확정 제작 — 먼저 훼손으로 정확도 1티어를 막아 두면 카오스 오브에 정확도가 안 나와
    # 물리 피해 %(레벨 82)보다 낮은 잡옵을 절사의 징조로 안전하게 지움 → 막기를 물리 피해 % 바로 뒤로
    ids=[n['id'] for n in r['nodes']]
    blk=[n for n in r['nodes'] if n['id'] in ('x4','x5')]
    r['nodes']=[n for n in r['nodes'] if n['id'] not in ('x4','x5')]
    i=[n['id'] for n in r['nodes']].index('x3')
    r['nodes'][i:i]=blk
    x5=_node(r,'x5'); x5['target']['reveal']={'gi':17,'tmax':1}; x5['target']['bone']='Ancient_Jawbone'
    x4=_node(r,'x4'); x4['cur']='Ancient_Jawbone'
    x5['fail']={'goto':'x4','via':LIGHT8}
    _node(r,'x8')['cur']='Ancient_Jawbone'
    _node(r,'x10')['cur']='Greater_Chaos_Orb'   # 영상(9:45): 공격 속도 1티어는 레벨 37이라 상위 카오스 오브(최소 레벨 35)로 돌림; _node(r,'x9')['target']['bone']='Ancient_Jawbone'
for _t in ('high',): _grade8('xeno-phys-crossbow','xeno-phys-crossbow-v2',_t,_xeno)
