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

# 2. Diztoh 가성비 석궁 — 2026-11-13 G14: 영상 전체 화면 대조(근거 scratchpad review/G14/diztoh-budget-crossbow-v2/timeline.md), 난이도 쉬움 → 에센셜만.
#    단계·확률은 플로우차트(scripts/graphs/gen_diztoh_budget_crossbow.py). 상자 id(b0·m1·m1x·m2·e1·k1~k6)는 옛 단계 id(c1~c16)와 겹치지 않게 새로 붙임.
def _xbow(r, t):
    r['start']={'rar':'normal','mods':[]}
    r['phases']=[{'id':'base','kr':'매직 · 에센스','en':'Magic and essences'},{'id':'des','kr':'훼손 · 엑잘','en':'Desecration and slam'}]
    r['nodes']=[
      {'id':'b0','phase':'base','do':'base','cost':'base','ts':'0:45','note':K('노멀 특출난 공성 쇠뇌(소켓 3), 아이템 레벨 82.','A normal exceptional Siege Crossbow (3 sockets), item level 82.')},
      {'id':'m1','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':xd_ppct},'ts':'0:50'},
      {'id':'m2','phase':'base','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'gi':xd_ppct},'ts':'1:05'},
      {'id':'e1','phase':'base','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':xd_flatE},'ts':'1:37'},
      {'id':'k1','phase':'des','do':'manual','target':{'rune':XD_ASTRID},'ts':'1:52'},
      {'id':'k2','phase':'des','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':xd_battle},'ts':'2:00'},
      {'id':'k3','phase':'des','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Liege'],'target':{'unrev':'s'},'ts':'2:16'},
      {'id':'k4','phase':'des','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},'ts':'2:40'},
      {'id':'k5','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':xd_gren},'side':'s','lord':'amanamu','bone':'Preserved_Jawbone'},'ts':'2:53'},
      {'id':'k6','phase':'des','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'junk':'p'},'ts':'3:32'},
    ]
_grade('diztoh-budget-crossbow','diztoh-budget-crossbow-v2','ess',_xbow)

# 3. Diztoh 한손 둔기 — bought magic crit base (정책 18), no Sinistral Erasure loop (about 470 div in the sim); Balance keeps the Whittling fix
def _mace1(r, t):
    r['start']={'rar':'magic','quality':20,'mods':[{'gi':om_crit,'tmax':2 if t=='bal' else 3}]}
    _node(r,'m1')['note']=K('노멀 특출난 약탈하는 철퇴 구입(영상 3 div, 퀄리티 26%).','Buy a normal exceptional Marauding Mace (3 div in the video, 26% quality).')   # G3 2026-11-13: 새 플로우차트는 노멀부터
    m7=_node(r,'m7'); m7['target']={'anyOf':OM_PHYS,'asIs':True,'side':'p'}; m7['br']=K('안 나와도 그대로, 좌측 말소의 징조 반복은 뺌','A miss stays (the Sinistral Erasure loop is left out)')
    _drop(r,'m2','m7b','m12','m13','m14')   # m14 타락은 정책 14장대로 뺌(G3 2026-11-13)
    if t=='ess':
        _drop(r,'m11'); m9=_node(r,'m9'); m9['target']={'anyOf':OM_FLAT,'asIs':True,'side':'p'}; m9['br']=KEEP
        for nid in ('m7','m9'): _node(r,nid)['cur']='Greater_Exalted_Orb'
for _t in ('bal','ess'): _grade('diztoh-onehand-mace','diztoh-onehand-mace-v2',_t,_mace1)

# 4. SaVeQ 합금 집중구 — Balance = video (Light until T1, Sinistral Annulment on a missed exalt), Essential = looser, results kept, Greater Exalts
def _focus(r, t):
    r['ilvl']=84   # 2026-11-13 G9: 영상 1번 집중구 아이템 레벨 84(0702 캡처) — 단계·확률은 플로우차트(gen_saveq_alloy_focus.py)에서 읽음
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
for _t in ('bal',): _grade('saveq-alloy-focus','saveq-alloy-focus-v2',_t,_focus)

# 5. 탱정 키타바 방패 — 난이도 4(사용자 확정 2026-11-12) = 하이엔드(영상) + 밸런스. 단계·확률·준비 과정은 플로우차트(graph2recipe)가 다시 쓰고, 여기서는 베이스 설명·분기 줄만 정함.
#    영상 시각은 build_recipes.py FC_TS(2026-11-12 W5 영상 전체 재대조, 근거 scratchpad review/W5-kitava-shield/timeline.md).
def _kitava(r, t):
    m={'high':1,'bal':2}[t]
    for x in _node(r,'t2')['target']['anyOf']: x['tmax']=1
    _node(r,'t4')['target']['reveal']={'anyOf':[dict(x,tmax=m) for x in TJ_MAXRES]}
    _drop(r,'t8','t9','t10','t11','t12')
    _node(r,'t1')['note']=K('특출난 타호아의 거대 방패(소켓 2개), 아이템 레벨 정확히 81, 일반 등급·미타락·미축성.',
        'Exceptional Tawhoan Tower Shield (two sockets), item level exactly 81, normal, not corrupted or sanctified.')
    _node(r,'t4')['br']=K('물리 피해 감소·화염 저항 최대치가 이미 있어 냉기·번개 저항 최대치를 고름. 빗나가면 빛의 징조 + 소멸의 오브 → {#t3}번','Damage reduction and fire maximum resistance are already there, so pick cold or lightning maximum resistance. Miss: Omen of Light + Annulment → step {#t3}')
    _node(r,'t7')['br']=K('절사의 징조는 요구 레벨이 가장 낮은 옵션을 바꿈. 방어도 최대치·% 1티어는 레벨 75, 복합 1티어와 가시 피해 1티어는 74라 마지막 칸은 복합이 나올 때까지 반복',
        'Whittling hits the lowest-level option: flat and % armour T1 are level 75, the hybrid T1 and thorns T1 are 74, so the last slot repeats until the hybrid lands')
    _node(r,'t2')['tips']=['chaos-after-fracture-families']   # 17:24 STEP 10 '이미 붙은 옵션은 중복 등장하지 않음'(마스터 지시 2026-11-12)
    r['start'].pop('quality',None); r.pop('prep',None)
    r['nodes'].insert([n['id'] for n in r['nodes']].index('t5'),{'id':'tf','phase':'pre','do':'note','br':K('영상에 없는 단계. 슬라이드 완성 문구 화염 저항 최대치 총 +6%와 거래소 실물에 맞춤','Not in the video: matches the slide goal of +6% total maximum fire resistance and a traded item')})   # 사용자 결정 2026-11-12
_grade('tankjung-kitava-shield','tankjung-kitava-shield-v2','bal',_kitava)
_r=_cp.deepcopy(_orig('tankjung-kitava-shield')); _r.update(id='tankjung-kitava-shield-v2',tierGroup='tankjung-kitava-shield-v2',tier='high',tierLabel=K('하이엔드','High-end')); _r.pop('note',None); _kitava(_r,'high'); R.append(_r)
