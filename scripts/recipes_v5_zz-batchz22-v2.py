# ---- 2026-11-11 batch 22: 시한 0.5.5 영상 7개를 플로우차트 기준 등급 레시피로 (사용자: "플로우차트 작성 후 > 플로우차트 기반으로 일반 레시피") ----
# Matches scripts/graphs/gen_batch22.py step for step (same step ids). 어려움 → 밸런스 + 에센셜, 전문가 → 하이엔드 + 밸런스 (정책 30).
# (_orig/_node from recipes_v5_zz-batch5-v2.py, _drop/KEEP from batch6, _grade8/LIGHT8/_asIs from batch8)

# 1. 차율라 목걸이(부재 목걸이) — 밸런스 = 영상(빗나가면 완벽한 무한의 에센스로 훼손 옵션을 지우고 다시), 에센셜 = 정신력 1~2티어 매물·공개 결과 그대로 (2026-11-11 영상 화면 재확인: 베이스·에센스 옵션 바로잡음)
def _amu(r, t):
    a4=_node(r,'a4')
    if t=='ess': a4.pop('fail',None); a4['br']=KEEP; r['start']['mods'][1]['tmax']=2   # 정신력 1~2티어 매물
for _t in ('bal','ess'): _grade8('sihan-chayula-amulet','sihan-chayula-amulet-v2',_t,_amu)

# 2. 차율라 장갑 — 밸런스 = 영상(완벽한 엑잘티드 오브), 에센셜 = 상위 엑잘티드 오브
def _cglv(r, t):
    if t=='ess':
        for nid in ('g3','g4'): _node(r,nid)['cur']='Greater_Exalted_Orb'
for _t in ('bal','ess'): _grade8('sihan-chayula-gloves','sihan-chayula-gloves-v2',_t,_cglv)

# 3. 차율라 투구 — 치명타 확률(선택)은 그래프에 없어 뺌. 밸런스 = 영상, 에센셜 = 튕겨내기 1~3티어·접두와 공개 결과 그대로
def _chel(r, t):
    _drop(r,'h3')
    if t=='ess':
        _node(r,'h2')['target']['tmax']=3
        h4=_node(r,'h4'); _asIs(h4, h4['target']['anyOf'], 'p')
        h6=_node(r,'h6'); h6.pop('fail',None); h6['br']=KEEP
for _t in ('bal','ess'): _grade8('sihan-chayula-helmet','sihan-chayula-helmet-v2',_t,_chel)

# 4. 차율라 마법봉 — 밸런스 = 영상(주문 치명타 1~2티어, 접미 빗나가면 다시), 에센셜 = 1~3티어·접미 결과 그대로
def _cwand(r, t):
    if t=='ess':
        _node(r,'w2')['target']['tmax']=3
        w3=_node(r,'w3'); _asIs(w3, w3['target']['anyOf'], 's')
for _t in ('bal','ess'): _grade8('sihan-chayula-wand','sihan-chayula-wand-v2',_t,_cwand)

# 5. 공격 플랫 3줄 반지 — 밸런스 = 영상(플랫 1~2티어, 공개는 빛의 징조로 다시), 에센셜 = 1~3티어·공개 결과 그대로
def _flat(r, t):
    if t=='ess':
        for nid in ('f4',):
            for x in _node(r,nid)['target']['anyOf']: x['tmax']=3
        f9=_node(r,'f9'); f9.pop('fail',None); f9['br']=KEEP
        for x in f9['target']['reveal']['anyOf']: x['tmax']=3
for _t in ('bal','ess'): _grade8('sihan-attack-flat-ring','sihan-attack-flat-ring-v2',_t,_flat)

# 6. 차율라 반지 — 하이엔드 = 저항·카오스 피해 1티어(영상 완성품), 밸런스 = 1~2티어
def _cring(r, t):
    tm=1 if t=='high' else 2
    _node(r,'r4')['target']['tmax']=tm; _node(r,'r5')['target']['tmax']=tm
    if t=='high': _node(r,'r9')['note']=K('완성. 카오스 피해·모든 원소 저항 모두 1티어.','Done; chaos damage and all resistances both at tier 1.')   # 사용자 결정 2026-11-13(C17), 영상 기준(저항 2티어 이상)은 밸런스
for _t in ('high','bal'): _grade8('sihan-chayula-ring','sihan-chayula-ring-v2',_t,_cring)

# 7. 하이엔드 투사체 장갑 — 하이엔드 = 1티어(영상), 밸런스 = 1~2티어(영상: 2티어는 금방). 마지막 훼손은 좌측 강령술의 징조로 접두에.
def _pglv(r, t):
    tm=1 if t=='high' else 2
    _node(r,'p2')['target']['tmax']=tm
    for nid in ('p6','p7'):
        for x in _node(r,nid)['target']['anyOf']: x['tmax']=tm
        if t=='bal': _node(r,nid)['expect']=8
    for x in _node(r,'p9')['target']['reveal']['anyOf']: x['tmax']=tm
    _node(r,'p8')['omens']=['Omen_of_Sinistral_Necromancy']
    r['start'].pop('runes',None)   # 2026-11-12 W10: 플로우차트 준비 구역이 콜르의 사냥을 단계로 장착 — 시작 룬으로 두면 카드에 콜르가 두 번 나옴
for _t in ('high','bal'): _grade8('sihan-proj-gloves','sihan-proj-gloves-v2',_t,_pglv)
