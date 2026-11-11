# ---- 2026-11-11 batch 23: EasyBabi 부적 · SL 딜용 장갑 (플로우차트 scripts/graphs/gen_batch23.py와 같은 단계 id, 정책 30·31) ----
# 1. EasyBabi 가시투성이 부적 — 하이엔드 = 영상(원소 피해 1~2티어, 다시 도전), 밸런스 = 1~3티어·엑잘과 공개 결과 그대로
def _tali(r, t):
    if t=='bal':
        for n in r['nodes']:
            for x in (n.get('target',{}).get('anyOf') or n.get('target',{}).get('reveal',{}).get('anyOf') or []): x['tmax']=3
        t5=_node(r,'t5'); t5.pop('fail',None); t5['br']=KEEP
        t6=_node(r,'t6'); _asIs(t6, t6['target']['anyOf'], 'p'); _drop(r,'t6b')
        t9=_node(r,'t9'); t9.pop('fail',None); t9['br']=KEEP
for _t in ('high','bal'): _grade8('easybabi-spiny-talisman','easybabi-spiny-talisman-v2',_t,_tali)

# 2. SL 딜용 장갑 — 하이엔드 = 영상(1티어), 밸런스 = 1~2티어·접두 엑잘·접미 카오스 한 번·공개 결과 그대로
def _sgl(r, t):
    if t=='bal':
        for n in r['nodes']:
            for x in (n.get('target',{}).get('anyOf') or n.get('target',{}).get('reveal',{}).get('anyOf') or []): x['tmax']=2
        k2=_node(r,'k2'); _asIs(k2, k2['target']['anyOf'], 'p')
        k4=_node(r,'k4'); k4['fail']={'goto':'k5'}; k4['br']=KEEP
        k6=_node(r,'k6'); k6.pop('fail',None); k6['br']=KEEP
for _t in ('high','bal'): _grade8('sl-blacksteel-gauntlets','sl-blacksteel-gauntlets-v2',_t,_sgl)
