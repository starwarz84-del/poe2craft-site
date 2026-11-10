# ---- 2026-11-10 batch 16 (사용자: 나머지도 순차적으로): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch16.py. Videos rechecked (transcripts). ----
def _absent(r, t):
    tm=1 if t=='high' else 2
    GPA=[{'gi':g,'tmax':tm} for g in (13,16,31,9)]   # 에너지 보호막 최대치 · 에너지 보호막 % · 주문 피해 · 생명력 최대치 (영상: 1티어가 뜨면 멈춤)
    _node(r,'a7')['omens']=['Omen_of_Sinistral_Crystallisation']   # 영상 2:14 / 14:37: 좌측 결정화의 징조 + 균열의 에센스
    for nid in ('a11','a12','a16','a16b'): _node(r,nid)['target']['anyOf']=GPA
    for nid in ('a12','a16b'):   # 영상: "죽어도 그 옵션" = 절사 돌리기 — 좌측 말소의 징조와 같이 써서 잡옵 접두만
        n=_node(r,nid); n['cur']='Perfect_Chaos_Orb'; n['omens']=['Omen_of_Whittling','Omen_of_Sinistral_Erasure']
    # 영상 순서: 심연의 에센스(징표) → 접두 엑잘 → 징표 훼손 → 공개
    ids=[n['id'] for n in r['nodes']]; a16=r['nodes'].pop(ids.index('a16')); r['nodes'].insert([n['id'] for n in r['nodes']].index('a17'),a16)
    a15=_node(r,'a15'); a15['fail']={'goto':'a16','via':{'cur':'Preserved_Collarbone','omens':['Omen_of_Light']}}
    a15['br']=K('징표가 접두면 보존된 빗장뼈 + 빛의 징조로 지우고 좌측 찬미의 징조 + 완벽한 엑잘티드 오브','Mark on a prefix: Preserved Collarbone + Light, then Sinistral Exaltation + Perfect Exalt')
    _node(r,'a18')['fail']={'goto':'a17','via':LIGHT8}
    if t=='high':
        _drop(r,'a12b','a16c')
    else:
        _drop(r,'a12','a16b')   # 밸런스: 공개 뒤 잡옵 접두는 영상의 가성비 마무리
        for nid in ('a12b','a16c'): _node(r,nid)['label']=K('가성비 마무리','Budget finish')
for _t in ('high','bal'): _grade8('absent-amulet-video','absent-amulet-video-v2',_t,_absent)

def _ring(r, t):
    _drop(r,'q3')   # 바알 촉진시키는 주입기는 선택 (정책 23)
    s1=_node(r,'s1'); s2=_node(r,'s2')
    # 영상: 빗나가면 우측 소멸의 징조 + 소멸의 오브 → 완벽한 엑잘티드 오브
    s2.update({'do':'exalt','cur':'Perfect_Exalted_Orb','omens':[],'target':{'anyOf':s1['target']['anyOf']},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}}})
    if t=='bal':
        for n in (s1,s2):
            for x in n['target']['anyOf']: x['tmax']=2
        p2=_node(r,'p2'); p2['target']['anyOf']=p2['target']['anyOf']+[{'gi':9,'tmax':1}]   # 영상: 생명력 1티어도 좋음
        _drop(r,'s3')   # 마지막 접미는 나오는 대로 (영상도 비용 때문에 멈춤)
for _t in ('high','bal'): _grade8('sl-flamewave-ring','sl-flamewave-ring-v2',_t,_ring)
