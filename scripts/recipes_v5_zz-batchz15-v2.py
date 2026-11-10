# ---- 2026-11-10 batch 15 (사용자: 두 개 더, 영상 확인 후 바로잡기): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch15.py. ----
def _mz5(r, t):
    _drop(r,'z9b')   # 촉진 + 완벽한 엑잘로 주문 +3·시전 속도를 같이 노리는 방법은 영상에서 20번에 1번 — 뺌
    _node(r,'z11')['omens']=['Omen_of_Sinistral_Crystallisation']   # 영상: 좌측 결정화 + 룬 합금
    if t=='bal':
        _drop(r,'z14','z15','z16','z17')   # 밸런스: 축성 없이 판매 (영상: 축성 전 시세 약 450~600 div)
        z13=_node(r,'z13'); z13.pop('fail',None); z13['br']=KEEP
for _t in ('high','bal'): _grade8('mazbro-spell5-amulet','mazbro-spell5-amulet-v2',_t,_mz5)

def _gold(r, t):
    p1=_node(r,'p1'); p1.pop('fail',None)
    p1['omens']=['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation']
    p1['target']={'anyOf':[{'gi':g,'tmax':2} for g in (31,12,11,13,16,14,27)]}
    p1['br']=K('잡옵 1개: 완벽한 강화의 에센스, 2개: 심연의 에센스','One junk: Perfect Essence of Enhancement; two: Essence of the Abyss')
    _node(r,'p2')['omens']=['Omen_of_Sinistral_Crystallisation']   # 영상 16:20
    if t=='bal': d2=_node(r,'d2'); d2.pop('fail',None); d2['br']=KEEP
for _t in ('high','bal'): _grade8('gold-amulet-6line','gold-amulet-6line-v2',_t,_gold)
