# ---- 2026-11-11 batch 25: 반지깎는노인 미러 지팡이 (플로우차트 scripts/graphs/gen_batch25.py와 같은 단계 id, 정책 30·31·32) ----
# 하이엔드 = 영상(모두 1티어), 밸런스 = 주문 치명타·접두 2개 1~2티어(시전 속도는 1티어 — 2티어면 다음 절사에서 번개 주문 +7을 잃기 쉬움, 시뮬 확인)
def _bzstaff(r, t):
    if t!='bal': return
    _node(r,'s3')['target']['tmax']=2
    for nid in ('p3','p5','pT'):
        n=_node(r,nid); lst=n['target']['reveal']['anyOf'] if nid=='p3' else n['target']['anyOf']
        for x in lst: x['tmax']=2
for _t in ('high','bal'): _grade8('banzino-mirror-staff','banzino-mirror-staff-v2',_t,_bzstaff)
