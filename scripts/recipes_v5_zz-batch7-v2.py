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

# 5. 탱정 키타바 방패 — 난이도 4(사용자 확정 2026-11-12) = 하이엔드(영상) + 밸런스. 단계·확률·준비 과정은 플로우차트(graph2recipe)가 다시 쓰고, 여기서는 베이스 설명·분기 줄만 정함.
#    영상 시각은 build_recipes.py FC_TS(2026-11-12 W5 영상 전체 재대조, 근거 scratchpad review/W5-kitava-shield/timeline.md).
def _kitava(r, t):
    m={'high':1,'bal':2}[t]
    for x in _node(r,'t2')['target']['anyOf']: x['tmax']=1
    _node(r,'t4')['target']['reveal']={'anyOf':[dict(x,tmax=m) for x in TJ_MAXRES]}
    _drop(r,'t8','t9','t10','t11','t12')
    _node(r,'t1')['note']=K('특출난 타호아의 거대 방패(소켓 2개), 아이템 레벨 정확히 81, 일반 등급·미타락·미축성.',
        'Exceptional Tawhoan Tower Shield (two sockets), item level exactly 81, normal, not corrupted or sanctified.')
    _node(r,'t4')['br']=K('받는 물리 피해 감소가 없으면 물리 피해 감소, 있으면 저항 최대치를 고름. 빗나가면 빛의 징조 + 소멸의 오브 → {#t3}번','Pick physical damage reduction if the item lacks it, otherwise maximum resistance. Miss: Omen of Light + Annulment → step {#t3}')
    _node(r,'t7')['br']=K('절사의 징조는 요구 레벨이 가장 낮은 옵션을 바꿈. 방어도 최대치·% 1티어는 레벨 75, 복합 1티어와 가시 피해 1티어는 74라 마지막 칸은 복합이 나올 때까지 반복',
        'Whittling hits the lowest-level option: flat and % armour T1 are level 75, the hybrid T1 and thorns T1 are 74, so the last slot repeats until the hybrid lands')
    r['start'].pop('quality',None); r.pop('prep',None)
_grade('tankjung-kitava-shield','tankjung-kitava-shield-v2','bal',_kitava)
_r=_cp.deepcopy(_orig('tankjung-kitava-shield')); _r.update(id='tankjung-kitava-shield-v2',tierGroup='tankjung-kitava-shield-v2',tier='high',tierLabel=K('하이엔드','High-end')); _r.pop('note',None); _kitava(_r,'high'); R.append(_r)
