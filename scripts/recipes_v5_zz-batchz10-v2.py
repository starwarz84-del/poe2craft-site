# (file name sorts after zz-batch9: z10)
# ---- 2026-11-10 batch 10 (남은 레시피 쉬운 것부터): 어려움 → Balance (video) + Essential (results kept). Matches scripts/graphs/gen_batch10.py. ----
def _sl5(r, t):
    _drop(r,'s10','s12')   # Divine values and the finishing catalyst quality are left out (정책 23)
    if t=='ess': s7=_node(r,'s7'); s7.pop('fail',None); s7['br']=KEEP
for _t in ('bal','ess'): _grade8('sl-5mod-jewel','sl-5mod-jewel-v2',_t,_sl5)
def _vod(r, t):
    if t=='ess':
        v4=_node(r,'v4'); v4.pop('fail',None); v4['br']=KEEP
        v6=_node(r,'v6'); v6.pop('fail',None); v6['br']=K('한 번만 — 결과 그대로','Once — keep whatever comes')
        v7=_node(r,'v7'); v7.pop('fail',None); v7['target'].pop('chance',None); v7['target'].pop('missDrop',None); v7['br']=K('접두 하나가 지워짐 — 결과 그대로','One prefix goes — keep whatever comes')
for _t in ('bal','ess'): _grade8('vodnarg-timelost-emerald','vodnarg-timelost-emerald-v2',_t,_vod)
def _lbboots(r, t):
    if t=='ess':
        h4=_node(r,'h4'); _asIs(h4, h4['target']['anyOf'], 'p'); _drop(r,'h4b')
        h6=_node(r,'h6'); h6.pop('fail',None); h6['br']=KEEP
for _t in ('bal','ess'): _grade8('lilbotq-boots','lilbotq-boots-v2',_t,_lbboots)
def _mzring(r, t):
    # 순서: 정신의 에센스(마나 %)를 먼저 — 영상 순서대로면 에센스가 엑잘로 붙인 마나 1티어를 1/2로 지움
    ids=[n['id'] for n in r['nodes']]; r9=_node(r,'r9'); r['nodes'].remove(r9); r['nodes'].insert([n['id'] for n in r['nodes']].index('r10b')+1, r9)
    r9['note']=K('좌측 찬미의 징조 + 상위 엑잘티드 오브로 접두에 마나 최대치 1티어.','Sinistral Exaltation + Greater Exalted Orb for T1 flat mana.')
    r9.pop('fail',None); r9['br']=K('안 나오면 마지막에 고대 빗장뼈로 마나 최대치','A miss: go for flat mana with an Ancient Collarbone at the end')
    _drop(r,'r14')
    if t=='ess': r13=_node(r,'r13'); r13.pop('fail',None); r13['br']=KEEP
for _t in ('bal','ess'): _grade8('mazbro-caster-ring','mazbro-caster-ring-v2',_t,_mzring)
