# ---- 2026-11-10 batch 14 (사용자: 전문가부터는 2개씩, 영상 확인 후 바로잡기): 전문가 → High-end (video) + Balance. Matches scripts/graphs/gen_batch14.py. ----
def _slstaff(r, t):
    # 알두르의 배신·아산드라 룬·영혼 핵·바알 오브는 취향 (정책 23)
    _drop(r,'r1','r1b','f1','f2')
    if t=='high':
        for nid in ('s2','s3m'): _node(r,nid)['omens']=['Omen_of_Whittling']   # 영상: 절사의 징조 + 완벽한 카오스 오브 (두 접미 잡옵이 가장 낮음)
        return
    # 밸런스 = 영상의 가성비 마무리: 엑잘 접미 2개 + 초월의 합금, 공개 결과 그대로
    p4=_node(r,'p4'); p4.pop('fail',None); p4['br']=KEEP
    _drop(r,'r2','s2','s3m')
    s1=_node(r,'s1'); s1['cur']='Exalted_Orb'
    s3=_node(r,'s3'); s3['target']={'gi':s3['target']['gi']}; s3['br']=K('접미 잡옵 하나가 지워짐','One junk suffix goes')   # 접미 잡옵 2개 중 하나가 지워짐 — 잃을 옵션 없음
def _sltitle(r,t):
    _slstaff(r,t); r['title']=K('화염 주문 +7 분열 + 피해 접두 1티어','Fractured +7 fire spells + T1 damage prefixes')
for _t in ('high','bal'): _grade8('sl-flamewave-staff','sl-flamewave-staff-v2',_t,_sltitle)

def _mzamu(r, t):
    _drop(r,'a18')   # 신성한 오브 + 축복받은 자의 징조는 수치 맞추기 (정책 23)
    a5=_node(r,'a5'); a5['cur']='Greater_Exalted_Orb'; a5['target']={'junk':'p','count':2}   # 영상: 상위 엑잘 2번으로 접두를 채워 균열의 에센스가 잡옵을 지우게
    a8=_node(r,'a8'); a8['target']['reveal']={'anyOf':[{'gi':g} for g in (21,0,1,2,3,4,5,6,7)]}   # 자리 막기: 생명력 재생 → 능력치 → 저항
    a10=_node(r,'a10'); a10['br']=K('빗나가면 소멸의 오브: 주문 +3이 지워지면 카오스부터, 막아 둔 옵션이 지워지면 훼손부터','Miss: Annulment — +3 spells gone: Chaos again; blocker gone: desecrate again')
    # 영상: 접두가 꽉 차 있어 좌측 소멸의 징조로 잡옵 접두를 지움(최대 퀄리티가 지워지면 좌측 결정화 + 균열의 에센스)
    ids=[n['id'] for n in r['nodes']]
    r['nodes'].insert(ids.index('a11'),{'id':'a10b','phase':_node(r,'a11').get('phase'),'do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment'],
        'target':{'removeJunk':'p','chance':0.5},'fail':{'goto':'a11','via':{'cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation']}},'ts':'17:25',
        'note':K('좌측 소멸의 징조 + 소멸의 오브로 잡옵 접두 제거.','Sinistral Annulment + Annulment removes the junk prefix.'),
        'br':K('최대 퀄리티가 지워지면 좌측 결정화 + 균열의 에센스','Max quality gone: Sinistral Crystallisation + Essence of the Breach')})
    _node(r,'a12')['fail']={'goto':'a10b'}
    a14=_node(r,'a14'); a14['target']['anyOf']=[{'gi':g,'tmax':1} for g in (11,31)]   # 엔진은 12번 단계를 마나 % 로 셈 → 남은 접두는 마나 최대치·주문 피해; a14['omens']=['Omen_of_Whittling','Omen_of_Sinistral_Erasure']
    if t=='bal':
        a14.pop('fail',None); a14['omens']=['Omen_of_Whittling']; a14['br']=KEEP   # 절사 카오스 한 번(최대 퀄리티만 지움)
        a17=_node(r,'a17'); a17.pop('fail',None); a17['br']=KEEP
for _t in ('high','bal'): _grade8('mazbro-caster-amulet','mazbro-caster-amulet-v2',_t,_mzamu)
