# ---- 2026-11-10 batch 18 (사용자: 나머지도 2개씩): 극한 → High-end (video) + Balance. Matches scripts/graphs/gen_batch18.py. Videos rechecked (transcripts). ----
def _proj7(r, t):
    if t=='bal':
        v7=_node(r,'v7'); v7.pop('fail',None); v7['br']=KEEP   # 관통 공개 결과 그대로
for _t in ('high','bal'): _grade8('sl-proj7-gloves','sl-proj7-gloves-v2',_t,_proj7)

def _iceshot(r, t):
    _drop(r,'w16')   # 신성한 오브·룬 교체·타락은 선택 (정책 23)
    # 꿀팁 연결(2026-11-12 마스터 지시): 플로우차트 읽기가 같은 id 단계의 tips를 이어받음. 신성한 오브 옆 상자(fd)는 레시피 단계가 아니라 분열 단계(f2)에 붙임
    for _id,_tp in (('f2','divine-before-fracture'),('al','aldur-breath-to-cold'),('d2','reveal-high-to-steer-whittle'),
                    ('l1','desecrate-reroll-no-light'),('l2','desecrate-reroll-no-light'),('l3','desecrate-reroll-no-light'),('x2','whittle-safe-top-level')):
        r['nodes'].append({'id':_id,'do':'note','tips':[_tp]})
# 2026-11-12 W3 영상 전체 재대조: 극한(난이도 5) → 하이엔드만(정책 10장). 단계는 플로우차트(gen_batch18.py)에서 읽음(fcRead), 영상 시각은 build_recipes.py FC_TS.
for _t in ('high','bal'): _grade8('diztoh-iceshot-bow','diztoh-iceshot-bow-v2',_t,_iceshot)   # 2026-11-13 D1: 난이도 표 4(전문가) → 하이엔드·밸런스(사용자 확정 15:42)
