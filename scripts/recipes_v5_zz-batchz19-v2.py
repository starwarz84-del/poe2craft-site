# ---- 2026-11-10 batch 19 (사용자: 다음 2개): 극한 → High-end (video) + Balance. Matches scripts/graphs/gen_batch19.py. Videos rechecked (transcripts). ----
def _nosideomen(r, *ids):   # the other side is full: side omens do nothing (REDUNDANT in build_recipes.py, for the copies)
    for nid in ids:
        n=_node(r,nid); n['omens']=[o for o in n.get('omens',[]) if not re.search(r'(Sinistral|Dextral)_(Exaltation|Necromancy)',o)]
        if not n['omens']: del n['omens']
import re
def _grasp(r, t):
    _drop(r,'m8')   # 룬 교체는 취향 (정책 23)
    _node(r,'p3')['cur']='Runic_Alloy'   # 영상: 룬 합금
    for nid in ('p4','p5'):
        n=_node(r,nid)
        if n.get('cur')=='Preserved_Collarbone': n['cur']='Ancient_Rib'
        if 'bone' in n.get('target',{}): n['target']['bone']='Ancient_Rib'
    p5=_node(r,'p5'); p5['omens']=['Omen_of_Abyssal_Echoes']
    _nosideomen(r,'p0','p2','p4')
    if t=='bal':
        for x in _node(r,'s1')['target']['all']: x['tmax']=2
        for x in p5['target']['reveal']['anyOf']: x['tmax']=2
for _t in ('high','bal'): _grade8('grasping-mail-spell1','grasping-mail-spell1-v2',_t,_grasp)

def _bis(r, t):
    _drop(r,'c17')   # 신성한 오브·축복받은 자의 징조·유동체는 선택 (정책 23)
    c8=_node(r,'c8'); c8.update({'do':'chaos','cur':'Chaos_Orb','fail':{'goto':'self'}}); c8.pop('omens',None)   # 영상: 카오스 오브 반복으로 첫 접두
    c9=_node(r,'c9'); c9['cur']='Perfect_Exalted_Orb'; c9['fail']={'goto':'c8','via':{'cur':'Orb_of_Annulment'}}   # 영상 뒷부분: 완벽한 엑잘 권장, 빗나가면 소멸의 오브(50/50)
    _nosideomen(r,'c12','c10','c13')
    if t=='bal':   # 영상 중간: 복합 저항 1개 + 원소 저항 1티어에서 끝내도 됨
        c13=_node(r,'c13'); c13['target']['anyOf']=c13['target']['anyOf']+[{'gi':g,'tmax':1} for g in (2,3,4)]
for _t in ('high',): _grade8('mazbro-bis-chest','mazbro-bis-chest-v2',_t,_bis)   # 2026-11-12 W7: 난이도 5(극한) → 하이엔드만(정책 10장), 단계는 플로우차트 읽기
