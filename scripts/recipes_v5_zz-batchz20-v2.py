# ---- 2026-11-10 batch 20 (사용자: 남은 2가지): 미러 활 · 주문 +6 부재 목걸이 → 미러 활 = High-end only (극한), 부재 목걸이 = High-end only (극한). Matches scripts/graphs/gen_batch20.py. Videos rechecked (transcripts). ----
def _mbow(r, t):
    # 재시도 구간(우측 결정화 + 심연의 에센스 → 징표 → 고대 턱뼈)은 훼손이 붙은 아이템엔 심연의 에센스를 못 써서 빛의 징조 + 고대 턱뼈 다시 훼손으로
    _drop(r,'b2','x1','x2','x3')
    r['title']=K('치명타 확률 분열 + 물리 피해 증가 1티어','fractured crit chance + T1 % physical damage')   # 줄임말 금지
    b4=_node(r,'b4'); b4['fail']={'goto':'self','via':LIGHT8}
    # 사용자 확정 2026-11-10: 정확도 1티어로 자리를 막으면 카오스 오브에 정확도가 안 나와, 물리 피해 %(레벨 82)보다 낮은 잡옵을 절사의 징조로 안전하게 지움
    acc=[x for x in b4['target']['reveal']['anyOf'] if x['gi']==16]
    if acc: b4['target']['reveal']['anyOf']=acc
    # 미러급이라 완벽한 카오스 오브(정책 23 ②)
    b6=_node(r,'b6'); b6['cur']='Perfect_Chaos_Orb'; b6['omens']=['Omen_of_Whittling']
    for nid in ('b7','b10'): _node(r,nid)['cur']='Perfect_Chaos_Orb'
    # 사용자 확정 2026-11-10: 세를의 승리는 접미 세 개를 끝낸 뒤, 네 번째 접미 작업 전에
    b10=_node(r,'b10'); third=_cp.deepcopy(b10); third['id']='b8w'; third.pop('ts',None)
    third['target']={'anyOf':[y for x in b10['target']['all'] for y in (x['anyOf'] if 'anyOf' in x else [x])],'replace':'s'}
    junk=_cp.deepcopy(_node(r,'b8')); junk['id']='b9x'; junk.pop('ts',None)
    ids=[n['id'] for n in r['nodes']]
    r['nodes'].insert(ids.index('b9'), third); ids=[n['id'] for n in r['nodes']]
    r['nodes'].insert(ids.index('b10'), junk)
for _t in ('high',): _grade8('mirror-bow-video','mirror-bow-video-v2',_t,_mbow)

def _spell6(r, t):
    # 2026-11-13 W12 영상 전체 화면 재대조: 단계는 플로우차트(scripts/graphs/gen_absent_amulet_spell6.py)를 그대로 읽음. 여기서는 같은 id 단계에 영상 시각만 붙임
    # 극한(난이도 5) = 하이엔드만(정책 10장). 성유·완벽한 유동체·신성한 오브·축성은 정책 14장대로 레시피에서 뺌
    _b=next(n for n in r['nodes'] if n.get('do')=='base'); _b['ts']='2:40'
    for _nid,_ts in [('b1','2:30'),('b2','3:35'),('b3','3:20'),('b4','7:25'),('b5','9:22'),('b6','9:40'),('b7','9:46'),('b8','9:57'),('b9','10:13'),
                     ('pf','19:00'),('b11','20:30'),('k1','20:58'),('q1','21:51'),('q2','21:55'),('q3','25:30'),('m1','27:20'),('m1e','27:28'),('m1d','28:08'),
                     ('c1','28:25'),('m2','29:15'),('m2l','29:20'),('m2e','29:25'),('m2d','29:50'),('m2r','30:00'),('m3','32:20'),('m3d','32:30'),('m3r','33:50'),('m3x','33:35')]:
        r['nodes'].append({'id':_nid,'do':'note','ts':_ts})
for _t in ('high',): _grade8('absent-amulet-spell6','absent-amulet-spell6-v2',_t,_spell6)
