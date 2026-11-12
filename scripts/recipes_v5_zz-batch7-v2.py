# ---- 2026-11-10: five more grade recipes (policy 25/30, 어려움 이하 → 밸런스 + 에센셜), matching scripts/graphs/gen_batch7.py ----
# (_orig, _grade, _node from recipes_v5_zz-batch5-v2.py, _drop/KEEP from recipes_v5_zz-batch6-v2.py)
# Runes that are only taste (Iron Runes) and Divine/Vaal value steps are dropped (정책 23). Video re-check is planned later (사용자: 최종 확인은 나중에 한번에).

# 1. 시한 차율라 셉터 — Balance = video (Light on a missed reveal), Essential = cheaper fractured base, reveal kept
def _scep(r, t):
    r['start']['mods'][0]['tmax']=2 if t=='bal' else 4
    _node(r,'s3')['target']['tmax']=1 if t=='bal' else 2
    p4=_node(r,'p4'); p4['target']['reveal']['tmax']=4 if t=='bal' else 6
    if t=='ess': p4.pop('fail',None); p4['br']=KEEP
for _t in ('bal','ess'): _grade('sihan-chayula-sceptre','sihan-chayula-sceptre-v2',_t,_scep)

# 2. Diztoh 가성비 석궁 — both start from a bought magic % physical base (정책 18; the video's Perfect Transmutation loop is ~86 div in the sim)
def _xbow(r, t):
    r['start']={'rar':'magic','mods':[{'gi':xd_ppct,'tmax':2 if t=='bal' else 3}]}
    _node(r,'c1')['note']=K('물리 피해 % 매직 석궁 구입(특출난 베이스, 룬 소켓 3).','Buy a magic exceptional crossbow with % physical (3 rune sockets).')
    _drop(r,'c2','c10','c13','c14','c15')
    if t=='ess':
        _drop(r,'c11'); c9=_node(r,'c9'); c9['cur']='Greater_Exalted_Orb'; c9['br']=KEEP
for _t in ('bal','ess'): _grade('diztoh-budget-crossbow','diztoh-budget-crossbow-v2',_t,_xbow)

# 3. Diztoh 한손 둔기 — bought magic crit base (정책 18), no Sinistral Erasure loop (about 470 div in the sim); Balance keeps the Whittling fix
def _mace1(r, t):
    r['start']={'rar':'magic','quality':20,'mods':[{'gi':om_crit,'tmax':2 if t=='bal' else 3}]}
    _node(r,'m1')['note']=K('치명타 확률 매직 둔기 구입(특출난 베이스, 퀄리티 20%).','Buy a magic exceptional mace with crit chance (20% quality).')
    m7=_node(r,'m7'); m7['target']={'anyOf':OM_PHYS,'asIs':True,'side':'p'}; m7['br']=K('안 나와도 그대로, 좌측 말소의 징조 반복은 뺌','A miss stays (the Sinistral Erasure loop is left out)')
    _drop(r,'m2','m7b','m12','m13')
    if t=='ess':
        _drop(r,'m11'); m9=_node(r,'m9'); m9['target']={'anyOf':OM_FLAT,'asIs':True,'side':'p'}; m9['br']=KEEP
        for nid in ('m7','m9'): _node(r,nid)['cur']='Greater_Exalted_Orb'
for _t in ('bal','ess'): _grade('diztoh-onehand-mace','diztoh-onehand-mace-v2',_t,_mace1)

# 4. SaVeQ 합금 집중구 — Balance = video (Light until T1, Sinistral Annulment on a missed exalt), Essential = looser, results kept, Greater Exalts
def _focus(r, t):
    rT=1 if t=='bal' else 3
    rev=[{'gi':sa_esp,'tmax':rT},{'gi':sa_hyb,'tmax':rT},{'gi':sa_mana,'tmax':rT}]
    _node(r,'v2')['target']['reveal']={'anyOf':rev}
    if t=='ess':
        _drop(r,'vr1','vr2','vr3'); _node(r,'v2')['br']=KEEP
        for nid in ('v4','v6','vm1'):
            n=_node(r,nid); n['cur']='Greater_Exalted_Orb'; n.pop('fail',None)
        _node(r,'v6')['br']=KEEP
    else:
        _node(r,'vr3')['target']['reveal']={'anyOf':rev}
for _t in ('bal','ess'): _grade('saveq-alloy-focus','saveq-alloy-focus-v2',_t,_focus)

# 5. 탱정 키타바 방패 — 난이도 4(사용자 확정 2026-11-12) = 하이엔드(영상) + 밸런스. 단계·확률은 플로우차트(graph2recipe)가 다시 쓰고, 여기서는 영상 시간·분기 줄·베이스 설명만 정함.
#    영상 시간은 2026-11-12 W6 화면 확인(evidence/tankjung-kitava-shield-v2/timeline.md).
def _kitava(r, t):
    m={'high':1,'bal':2}[t]
    for x in _node(r,'t2')['target']['anyOf']: x['tmax']=1
    _node(r,'t4')['target']['reveal']={'anyOf':[dict(x,tmax=m) for x in TJ_MAXRES]}
    _drop(r,'t10','t11','t12')
    _node(r,'t1').update(ts='14:30',note=K('특출난 타호아의 거대 방패(소켓 2개), 아이템 레벨 정확히 81, 일반 등급·미타락. 접미 4종 중 하나를 분열해 둔 상태에서 시작.',
        'Exceptional Tawhoan Tower Shield (two sockets), item level exactly 81, normal and not corrupted. Starts once one of the four suffixes is fractured.'))
    for nid,ts in (('t2','17:25'),('t3','17:55'),('t4','17:55'),('t5','19:04'),('t6','19:04'),('t7','19:08')): _node(r,nid)['ts']=ts
    _node(r,'t4')['br']=K('빗나가면 빛의 징조 + 소멸의 오브 → {#t3}번','Miss: Omen of Light + Annulment → step {#t3}')
    _node(r,'t7')['br']=K('절사의 징조는 요구 레벨이 가장 낮은 옵션을 바꿈. 방어도 최대치·% 1티어는 레벨 75, 복합 1티어는 74라 복합이 다시 바뀔 수 있음','Whittling hits the lowest-level option: flat and % armour T1 are level 75, the hybrid T1 is 74, so the hybrid can be rolled again')
    for nid in ('t8','t9'): _node(r,nid).pop('br',None)
    r['start'].pop('quality',None)
    r['prep']={'start':{'rar':'normal','quality':0},'phases':[{'id':'prep','kr':'분열 준비','en':'Fracture prep'}],'nodes':[
     {'id':'x1','phase':'prep','do':'note','ts':'15:25','note':K('완벽한 진화의 오브로 시작해 접두가 붙으면 완벽한 확장의 오브, 빗나간 접미는 소멸의 오브로 지우고 다시. 목표는 접미 4종(받는 물리 피해 8% 감소, 화염·냉기·번개 저항 최대치 +3%) 중 하나. 냉기·번개가 나오면 맹렬한 유동체로 화염으로 바꿈.',
       'Start with a Perfect Orb of Transmutation; on a prefix add a Perfect Orb of Augmentation, annul a missed suffix and retry, until one of the four suffixes (8% physical damage reduction, +3% maximum fire, cold or lightning resistance). Turn cold or lightning into fire with Blazing Flux.')},
     {'id':'x2','phase':'prep','do':'note','ts':'16:55','note':K('옵션이 1개면 완벽한 확장의 오브를 먼저 쓰고 완벽한 제왕의 오브로 옵션 3개. 보존된 갈비뼈로 훼손 옵션을 붙이고 공개하지 않은 채 분열의 오브. 다른 옵션이 분열되면 새 베이스.',
       'With one option add a Perfect Orb of Augmentation first, then a Perfect Regal Orb for three options. Add a Preserved Rib desecration, leave it unrevealed and use a Fracturing Orb. Another option fractured means a new base.')}]}
_grade('tankjung-kitava-shield','tankjung-kitava-shield-v2','bal',_kitava)
_r=_cp.deepcopy(_orig('tankjung-kitava-shield')); _r.update(id='tankjung-kitava-shield-v2',tierGroup='tankjung-kitava-shield-v2',tier='high',tierLabel=K('하이엔드','High-end')); _r.pop('note',None); _kitava(_r,'high'); R.append(_r)
