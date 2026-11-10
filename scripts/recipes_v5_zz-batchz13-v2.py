# ---- 2026-11-10 batch 13 (사용자: 전문가부터는 2개씩): 전문가 → High-end (video) + Balance (reveal kept). Matches scripts/graphs/gen_batch13.py. ----
def _noble(r, t):
    _drop(r,'n8','n12','n13')   # optional radius reroll, the note step and the finishing catalyst quality (정책 23)
    _node(r,'n3')['target']['count']=2   # both prefixes filled before Contempt (사용자 확정 2026-11-10: it takes a line first — a prefix goes 2/3)
    _node(r,'n4')['target']['chance']=2/3
    n10=_node(r,'n10'); n10['omens']=['Omen_of_Sinistral_Necromancy']
    n11=_node(r,'n11')
    if t=='bal': n11.pop('fail',None); n11['br']=KEEP
    else: n11['fail']={'goto':'n9','via':{'cur':'Chaos_Orb'}}
for _t in ('high','bal'): _grade8('noble-timelost-sapphire','noble-timelost-sapphire-v2',_t,_noble)
def _mzgloves(r, t):
    _drop(r,'g17')   # rune swap and Divine values are taste (정책 23)
    if t=='bal': g16=_node(r,'g16'); g16.pop('fail',None); g16['br']=KEEP
for _t in ('high','bal'): _grade8('mazbro-proj-gloves','mazbro-proj-gloves-v2',_t,_mzgloves)
