# ---- 2026-11-11 batch 23: EasyBabi 부적 · SL 딜용 장갑 (플로우차트 scripts/graphs/gen_batch23.py와 같은 단계 id, 정책 30·31) ----
# 1. EasyBabi 가시투성이 부적 — 하이엔드 = 영상(원소 피해 1~2티어, 다시 도전), 밸런스 = 1~3티어·엑잘과 공개 결과 그대로
def _tali(r, t):
    if t=='bal':
        for n in r['nodes']:
            for x in (n.get('target',{}).get('anyOf') or n.get('target',{}).get('reveal',{}).get('anyOf') or []): x['tmax']=3
        t5=_node(r,'t5'); t5.pop('fail',None); t5['br']=KEEP
        t6=_node(r,'t6'); _asIs(t6, t6['target']['anyOf'], 'p'); _drop(r,'t6b')
        t9=_node(r,'t9'); t9.pop('fail',None); t9['br']=KEEP
for _t in ('high','bal','ess'): _grade8('easybabi-spiny-talisman','easybabi-spiny-talisman-v2',_t,_tali)

# 2. SL 딜용 장갑 — 2026-11-13 W13: 영상 전체 화면 대조로 새 기준 재작성(scripts/graphs/gen_sl_blacksteel_gauntlets.py). 난이도 극한 → 하이엔드만(정책 10장 C11).
#    등급 레시피 단계는 플로우차트를 읽어 만듦(graph2recipe), 옛 단계 고치기는 쓰지 않음
def _sgl(r, t): return
for _t in ('high',): _grade8('sl-blacksteel-gauntlets','sl-blacksteel-gauntlets-v2',_t,_sgl)
