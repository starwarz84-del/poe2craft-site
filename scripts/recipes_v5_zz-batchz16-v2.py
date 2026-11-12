# ---- 2026-11-10 batch 16 (사용자: 나머지도 순차적으로): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch16.py. Videos rechecked (transcripts). ----
def _absent(r, t):
    # 2026-11-13 W29 영상 전체 화면 재대조: 단계는 플로우차트(scripts/graphs/gen_absent_amulet_video.py)를 그대로 읽음(graph2recipe).
    # 영상 시각은 build_recipes.py FC_TS로 붙임. 전문가(4) = 하이엔드·밸런스(정책 10장), 완벽한 유동체·쥬얼러·할당·축성은 정책 14장대로 뺌
    pass
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
