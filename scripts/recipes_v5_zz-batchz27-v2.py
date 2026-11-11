# ---- 2026-11-11 batch 27: Unstoppable BTW 갑옷 2개 (플로우차트 scripts/graphs/gen_batch27.py와 같은 단계 id, 정책 30·31·32) ----
# 하이엔드 = 영상(모두 1티어), 밸런스 = 루프로 찾는 접두·저항·굴절 1~2티어.
def _uns2(r, t):
    if t!='bal': return
    for n in r['nodes']:
        tg=n.get('target') or {}
        lst=(tg.get('reveal') or {}).get('anyOf') if 'reveal' in tg else tg.get('anyOf')
        if lst and not tg.get('asIs') and not (tg.get('reveal') or {}).get('asIs'):
            for x in lst:
                if x.get('tmax')==1: x['tmax']=2
for _id in ('unstoppable-vile-robe','unstoppable-slipstrike-vest'):
    for _t in ('high','bal'): _grade8(_id,_id+'-v2',_t,_uns2)
