# ---- 2026-11-10 batch 12 (사용자: 전문가부터는 2개씩): 전문가 → High-end (video) + Balance (reveal kept). Matches scripts/graphs/gen_batch12.py. ----
def _mastert(r, t):
    _drop(r,'t8','t11')   # prefixes are already full after the Erasure Chaos; the Divine Orb is for values (정책 23)
    _node(r,'t3')['target']['count']=2   # both prefixes filled so the contempt line replaces a prefix (50%)
    if t=='bal': t6=_node(r,'t6'); t6.pop('fail',None); t6['br']=KEEP
for _t in ('high','bal'): _grade8('mastert-timelost-emerald','mastert-timelost-emerald-v2',_t,_mastert)
def _chiba(r, t):
    _drop(r,'c11')   # finishing catalyst quality is left out (정책 23)
    if t=='bal': c6=_node(r,'c6'); c6.pop('fail',None); c6['br']=KEEP
for _t in ('high','bal'): _grade8('chiba-timelost-emerald','chiba-timelost-emerald-v2',_t,_chiba)
