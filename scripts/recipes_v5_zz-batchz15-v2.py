# ---- 2026-11-10 batch 15 (사용자: 두 개 더, 영상 확인 후 바로잡기): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch15.py. ----
def _mz5(r, t):
    _drop(r,'z9b')   # 촉진 + 완벽한 엑잘로 주문 +3·시전 속도를 같이 노리는 방법은 영상에서 20번에 1번 — 뺌
    _node(r,'z11')['omens']=['Omen_of_Sinistral_Crystallisation']   # 영상: 좌측 결정화 + 룬 합금
for _t in ('high',): _grade8('mazbro-spell5-amulet','mazbro-spell5-amulet-v2',_t,_mz5)   # 2026-11-13 P13 새 정책 D: 하이엔드 404.2 / 밸런스 369.4 div(8.6%) → 하이엔드만

def _gold(r, t):
    p1=_node(r,'p1'); p1.pop('fail',None)
    p1['omens']=['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation']
    p1['target']={'anyOf':[{'gi':g,'tmax':2} for g in (31,12,11,13,16,14,27)]}
    p1['br']=K('잡옵 1개: 완벽한 강화의 에센스, 2개: 심연의 에센스','One junk: Perfect Essence of Enhancement; two: Essence of the Abyss')
    _node(r,'p2')['omens']=['Omen_of_Sinistral_Crystallisation']   # 영상 16:20
    if t=='bal': d2=_node(r,'d2'); d2.pop('fail',None); d2['br']=KEEP
for _t in ('high','bal'): _grade8('gold-amulet-6line','gold-amulet-6line-v2',_t,_gold)
