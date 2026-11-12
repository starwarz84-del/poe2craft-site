# ---- 2026-11-10 batch 12 (사용자: 전문가부터는 2개씩): 전문가 → High-end (video) + Balance (reveal kept). Matches scripts/graphs/gen_batch12.py. ----
def _mastert(r, t):
    _drop(r,'t8','t11')   # prefixes are already full after the Erasure Chaos; the Divine Orb is for values (정책 23)
    _node(r,'t3')['target']['count']=2   # both prefixes filled: contempt takes a random line first (사용자 확정 2026-11-10) — a prefix (2 of the 3 removable) → +1 suffix allowed
    _node(r,'t4')['target']['chance']=2/3
    if t=='bal': t6=_node(r,'t6'); t6.pop('fail',None); t6['br']=KEEP
for _t in ('high','bal'): _grade8('mastert-timelost-emerald','mastert-timelost-emerald-v2',_t,_mastert)
def _chiba(r, t):
    _drop(r,'c11')   # finishing catalyst quality is left out (정책 23)
    _node(r,'c4')['target']['chance']=2/3   # 2 junk prefixes + 1 removable suffix: a prefix goes 2/3 → +1 suffix allowed
    # W24 2026-11-13: 밸런스도 빛의 징조로 다시 공개(정책 10장 C17-3) — 플로우차트 그대로 읽음
for _t in ('high','bal'): _grade8('chiba-timelost-emerald','chiba-timelost-emerald-v2',_t,_chiba)
