# ---- 2026-11-10 batch 11 (남은 레시피 쉬운 것부터): 어려움 → Balance (video) + Essential. Matches scripts/graphs/gen_batch11.py. ----
# diztoh-twister-spear and diztoh-as-spear are the same video: one group (REPLACES drops both).
def _spear(r, t):
    # 2026-11-13 P8 새 정책 B: 영상 공개는 메아리 다시 뽑기 한 번(4:06~4:12), 빛의 징조 반복 없음 → 밸런스도 옛 에센셜처럼 결과 그대로
    a9=_node(r,'a9'); a9.pop('fail',None); a9['target']['anyReveal']=True; a9['br']={'kr':'공개 결과 그대로, 다시 하지 않음','en':'Keep whatever the reveal gives'}
    a10=_node(r,'a10'); a10['cur']='Greater_Exalted_Orb'; _asIs(a10, a10['target']['anyOf'], 'p'); a10['target']['rand']=True; _drop(r,'a11')
for _t in ('bal',): _grade8('diztoh-as-spear','diztoh-as-spear-v2',_t,_spear)   # 2026-11-13 P8 새 정책 B·D: 빛의 징조 반복을 빼니 밸런스 = 에센셜 → 밸런스만
def _sgloves(r, t):
    d11=_node(r,'d11'); _asIs(d11, d11['target']['anyOf'], 'p')
    d11['br']=K('결과 그대로. 좌측 소멸의 징조 반복은 평균 약 650 div라 뺌','Keep it (the Sinistral Annulment loop averages about 650 div)')
    for nid in ('dm1','dm2'):
        n=_node(r,nid); _asIs(n, n['target']['anyOf'], 'p')
        if t=='ess': n['cur']='Greater_Exalted_Orb'
    if t=='ess': d11['cur']='Greater_Exalted_Orb'
for _t in ('bal',): _grade8('diztoh-socket-gloves','diztoh-socket-gloves-v2',_t,_sgloves)   # 2026-11-13 P8 새 정책 D: 에센셜 241.4 vs 밸런스 255.4 div(6%) → 밸런스만
def _seek(r, t):
    if t=='ess':
        _drop(r,'k6','k7','k8','k9'); k10=_node(r,'k10'); _asIs(k10, k10['target']['anyOf'], 'p')
        k10['br']=K('영상의 가성비 마무리 — 결과 그대로','The video’s budget finish — keep it')
    else: _drop(r,'k6')
for _t in ('bal','ess'): _grade8('seek-cyclone-boots','seek-cyclone-boots-v2',_t,_seek)
