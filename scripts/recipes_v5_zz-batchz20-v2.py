# ---- 2026-11-10 batch 20 (사용자: 남은 2가지): 미러 활 · 주문 +6 부재 목걸이 → High-end (video) + Balance. Matches scripts/graphs/gen_batch20.py. Videos rechecked (transcripts). ----
def _mbow(r, t):
    # 재시도 구간(우측 결정화 + 심연의 에센스 → 징표 → 고대 턱뼈)은 훼손이 붙은 아이템엔 심연의 에센스를 못 써서 빛의 징조 + 고대 턱뼈 다시 훼손으로
    _drop(r,'b2','x1','x2','x3')
    r['title']=K('치명타 확률 분열 + 물리 피해 증가 1티어','fractured crit chance + T1 % physical damage')   # 줄임말 금지
    b4=_node(r,'b4'); b4['fail']={'goto':'self','via':LIGHT8}
    # 미러급이라 완벽한 카오스 오브(정책 23 ②) — 절사는 좌측 말소의 징조와 같이 써서 접두 잡옵만
    b6=_node(r,'b6'); b6['cur']='Perfect_Chaos_Orb'; b6['omens']=['Omen_of_Whittling','Omen_of_Sinistral_Erasure']
    for nid in ('b7','b10'): _node(r,nid)['cur']='Perfect_Chaos_Orb'
    if t=='bal':   # 접두 엑잘이 빗나가면 잡옵을 두고 진행, 물리 접두 하나는 마지막 공개 · 화살·치명타 피해 1~2티어
        b5=_node(r,'b5'); b5.pop('fail',None); b5['br']=KEEP; _drop(r,'b6')
        for x in _node(r,'b7')['target']['anyOf']: x['tmax']=2
        for x in _node(r,'b10')['target']['all']:
            for y in (x['anyOf'] if 'anyOf' in x else [x]): y['tmax']=2
        _node(r,'e2')['target']['reveal']['tmax']=2
for _t in ('high','bal'): _grade8('mirror-bow-video','mirror-bow-video-v2',_t,_mbow)

def _spell6(r, t):
    if t=='bal':   # 유동체·성유·신성한 오브·축성 없이 판매
        _drop(r,'e1','e2','e3','e4')
        for x in _node(r,'m2')['target']['anyOf']: x['tmax']=2
        for x in _node(r,'c1')['target']['reveal']['anyOf']: x['tmax']=2
for _t in ('high','bal'): _grade8('absent-amulet-spell6','absent-amulet-spell6-v2',_t,_spell6)
