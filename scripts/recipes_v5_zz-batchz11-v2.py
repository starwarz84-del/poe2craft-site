# ---- 2026-11-10 batch 11 (남은 레시피 쉬운 것부터): 어려움 → Balance (video) + Essential. Matches scripts/graphs/gen_batch11.py. ----
# diztoh-twister-spear and diztoh-as-spear are the same video: one group (REPLACES drops both).
def _spear(r, t):
    a10=_node(r,'a10')
    if t=='ess':
        a10['cur']='Greater_Exalted_Orb'; _asIs(a10, a10['target']['anyOf'], 'p'); _drop(r,'a11')
for _t in ('bal','ess'): _grade8('diztoh-as-spear','diztoh-as-spear-v2',_t,_spear)
def _sgloves(r, t):
    d11=_node(r,'d11'); _asIs(d11, d11['target']['anyOf'], 'p')
    d11['br']=K('결과 그대로 (좌측 소멸의 징조 반복은 평균 약 650 div라 뺌)','Keep it (the Sinistral Annulment loop averages about 650 div)')
    for nid in ('dm1','dm2'):
        n=_node(r,nid); _asIs(n, n['target']['anyOf'], 'p')
        if t=='ess': n['cur']='Greater_Exalted_Orb'
    if t=='ess': d11['cur']='Greater_Exalted_Orb'
for _t in ('bal','ess'): _grade8('diztoh-socket-gloves','diztoh-socket-gloves-v2',_t,_sgloves)
def _seek(r, t):
    if t=='ess':
        _drop(r,'k6','k7','k8','k9'); k10=_node(r,'k10'); _asIs(k10, k10['target']['anyOf'], 'p')
        k10['br']=K('영상의 가성비 마무리 — 결과 그대로','The video’s budget finish — keep it')
    else: _drop(r,'k6')
for _t in ('bal','ess'): _grade8('seek-cyclone-boots','seek-cyclone-boots-v2',_t,_seek)
