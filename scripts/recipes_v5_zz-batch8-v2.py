# ---- 2026-11-10: five more grade recipes (policy 25/30), matching scripts/graphs/gen_batch8.py ----
# 어려움 이하 → 밸런스 + 에센셜, 전문가 이상 → 하이엔드 + 밸런스 (정책 30). High-end / Balance = the video record, the lower grade = looser targets, results kept.
# (_orig, _node from recipes_v5_zz-batch5-v2.py, _drop/KEEP from recipes_v5_zz-batch6-v2.py). Video re-check is planned later (사용자: 최종 확인은 나중에 한번에).
exec(open('/home/claude/poe2data/scripts/difficulty.py').read())
_TL={'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}
def _grade8(old, gid, tier, edit):
    r=_cp.deepcopy(_orig(old)); r['id']=gid if tier=='high' else gid+'-'+tier; r['tierGroup']=gid; r['tier']=tier
    r['tierLabel']=_TL[tier]; r.pop('note',None)
    if old in DIFFSET: r['difficulty']=DIFFSET[old]
    edit(r, tier); R.append(r)
LIGHT8={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
def _asIs(n, spec, side):
    n.pop('fail',None); n['target']=dict(spec, asIs=True, side=side) if 'gi' in spec else {'anyOf':spec, 'asIs':True, 'side':side}; n['br']=KEEP

# 1. 라그나 주문 +4 목걸이 — Balance = video (Dextral Annulment retry for cast speed, Light on the reveal), Essential = T1–3 Spirit base, results kept
def _ragna(r, t):
    r['start']['mods'][0]['tmax']=1   # G5 11-13: 베이스에 있는 옵션은 모든 등급 1티어(C15)
    g9=_node(r,'g9'); g9['target']['reveal']['tmax']=2 if t=='bal' else 4
    if t=='ess':
        g6=_node(r,'g6'); _asIs(g6, {'gi':g6['target']['gi'],'tmax':3}, 's'); _drop(r,'g6b')
        g9.pop('fail',None); g9['br']=KEEP
for _t in ('bal','ess'): _grade8('ragna-spell4-amulet','ragna-spell4-amulet-v2',_t,_ragna)

# 2. 노블이 본능적인 화살통 — High-end = video, Balance = T1–2 suffix targets, prefix exalts kept as they come
def _quiver(r, t):
    if t=='high': return
    for nid in ('q2','q3'):
        for x in _node(r,nid)['target']['anyOf']:
            if x['gi']==_node(r,'q2')['target']['anyOf'][0]['gi']: x['tmax']=2
            elif 'tmax' in x: x['tmax']=3
    for nid in ('q7','qm3'):
        for x in _node(r,nid)['target']['reveal']['anyOf']:
            if 'tmax' in x: x['tmax']=2 if x['tmax']==1 else 3
    for nid in ('q5','q6'):
        n=_node(r,nid); _asIs(n, [dict(x,tmax=2) for x in n['target']['anyOf']], 'p')
for _t in ('high','bal'): _grade8('noble-visceral-quiver','noble-visceral-quiver-v2',_t,_quiver)

# 3. 시한 하이엔드 투구 — 2026-11-12 W8: 등급 레시피 단계는 플로우차트(scripts/graphs/sihan-highend-helmet-v2.json)를 등급별로 읽어 만듦(graph2recipe). 옛 단계 고치기는 쓰지 않음
def _shelm(r, t): return
for _t in ('high','bal'): _grade8('sihan-highend-helmet','sihan-highend-helmet-v2',_t,_shelm)

# 4. Barricade 험악한 육척봉 — High-end = video (three T1 elemental prefixes), Balance = one T1–2 line with Whittling + Greater Chaos, the rest kept
def _barr(r, t):
    if t=='high': return
    q4=_node(r,'q4'); q4['target']['reveal']={'anyOf':[dict(x,tmax=2) for x in q4['target']['reveal']['anyOf']]}
    p2=_node(r,'p2'); p2['cur']='Greater_Chaos_Orb'; p2['target']['anyOf']=[dict(x,tmax=2) for x in p2['target']['anyOf']]
    p2['br']=K('원소 피해 접두 옵션 1개가 나오면 다음 단계','Move on once one elemental prefix shows')
    p4=_node(r,'p4'); _asIs(p4, p2['target']['anyOf'], 'p')
    _drop(r,'p3','p5','p6')
for _t in ('high','bal'): _grade8('barricade-quarterstaff','barricade-quarterstaff-v2',_t,_barr)

# 5. Diztoh 엔드게임 육척봉 — High-end = video (Light instead of Dextral Annulment on a missed reveal: Annulment can take the good suffix), Balance = Greater Exalts, misses kept
def _dzstaff(r, t):
    _drop(r,'s8','s9','s10')   # Perfect Iron Runes are taste (정책 23), the Divine Orb is for values
    s7=_node(r,'s7'); s7['fail']={'goto':'s6','via':LIGHT8}
    if t=='high': return
    s3=_node(r,'s3'); _asIs(s3, [dict(x,tmax=3) for x in s3['target']['anyOf']], 'p')
    s4=_node(r,'s4'); s4['cur']='Greater_Exalted_Orb'; _asIs(s4, s4['target']['anyOf'], 'p')
    s5=_node(r,'s5'); s5['cur']='Greater_Exalted_Orb'; _asIs(s5, s5['target']['anyOf'], 's')
    s7['target']['reveal']={'anyOf':[dict(x,tmax=3) for x in s7['target']['reveal']['anyOf']]}
    _drop(r,'s4b','s5b')
for _t in ('high','bal'): _grade8('diztoh-endgame-quarterstaff','diztoh-endgame-quarterstaff-v2',_t,_dzstaff)
