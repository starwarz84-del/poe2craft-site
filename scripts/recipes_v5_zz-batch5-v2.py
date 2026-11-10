# ---- 2026-11-10: five easy recipes as grade recipes (policy 25/30, 어려움 이하 → 밸런스 + 에센셜) ----
# Built from the original recipe of each video (copied out of R, which is why this file sorts last), matching
# scripts/graphs/gen_batch5.py. The originals are dropped by REPLACES in build_recipes.py.
import copy as _cp
def _orig(rid): return next(r for r in R if r['id']==rid)
def _grade(old, gid, tier, edit):
    r=_cp.deepcopy(_orig(old)); r['id']=gid+'-'+tier; r['tierGroup']=gid; r['tier']=tier
    r['tierLabel']={'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier]; r.pop('note',None)
    edit(r, tier); R.append(r)
def _node(r, nid): return next(n for n in r['nodes'] if n['id']==nid)

# 1. 라그나 아샷 활 — Balance = video (T1 % physical bought), Essential = T1–3 % physical base
def _bow(r, t):
    r['start']['mods'][0]['tmax'] = 1 if t=='bal' else 3
    r['nodes']=[n for n in r['nodes'] if n['id']!='w7']
    _node(r,'w6')['br']=K('공격 속도 → 완성 (마지막 엑잘이 일반 공격 속도면 공개 결과 무관). 실패: 빛의 징조 + 소멸의 오브로 다시 훼손','Attack speed → done (a normal attack speed from the last exalt also does it); miss: Light + Annulment and desecrate again')
for _t in ('bal','ess'): _grade('ragna-ashot-bow','ragna-ashot-bow-v2',_t,_bow)

# 2. TheSaneExile 저항 벨트 — Balance = video (T1 life + T1–2 lightning res), Essential = both T1–3
def _belt(r, t):
    r['start']['mods'][0]['tmax'] = 1 if t=='bal' else 3; r['start']['mods'][1]['tmax'] = 2 if t=='bal' else 3
for _t in ('bal','ess'): _grade('sane-resist-belt','sane-resist-belt-v2',_t,_belt)

# 3. Diztoh 가성비 양손 둔기 — Balance = video (Perfect Transmutation for T1–2 hybrid), Essential = buy a T1–4 hybrid magic base (정책 18) + Greater Exalt
def _mace(r, t):
    hyb=_node(r,'d2')['target']['gi']
    if t=='ess':
        r['start']={'rar':'magic','mods':[{'gi':hyb,'tmax':4}]}; r['nodes']=[n for n in r['nodes'] if n['id']!='d2']
        _node(r,'d1')['note']=K('물리 % + 정확도 복합(1~4티어)이 붙은 매직 특출난 거대한 대망치(소켓 3), 아이템 레벨 82.','A magic exceptional Massive Greathammer (3 sockets) with T1–4 hybrid physical + accuracy, item level 82.')
        _node(r,'d9')['cur']='Greater_Exalted_Orb'
    else: _node(r,'d2')['target']['tmax']=2
    _node(r,'d8')['fail']={'goto':'d5','via':LIGHT}
    _node(r,'d8')['br']=K('쿠르갈 물리 % → 다음, 실패: 빛의 징조 + 소멸의 오브로 다시 훼손','Kurgal % physical → next; miss: Light + Annulment and desecrate again')
    r['nodes']=[n for n in r['nodes'] if n['id']!='d10']+[{'id':'d10','phase':'fin','do':'note','ts':'4:32','note':K('완성. 소켓의 아스트리드의 창의성은 빼고 원하는 룬으로.','Done. Swap Astrid’s Creativity for the runes you like.')}]
for _t in ('bal','ess'): _grade('diztoh-budget-mace','diztoh-budget-mace-v2',_t,_mace)

# 4. LilBotQ 가성비 장화 — Balance = video, Essential = T1–2 movement speed + T1–3 cold res bought, lightning res T1–4
def _boots(r, t):
    if t=='ess':
        r['start']['mods'][0]['tmax']=2; r['start']['mods'][1]['tmax']=3; _node(r,'b5')['target']['reveal']['tmax']=4
for _t in ('bal','ess'): _grade('lilbotq-budget-boots','lilbotq-budget-boots-v2',_t,_boots)

# 5. Icesly 가성비 완드 — Balance = video tiers, Essential = T1–2 +5 lightning, looser prefix targets
def _wand(r, t):
    if t=='ess':
        r['start']['mods'][0]['tmax']=2
        xs={id(x):x for nid in ('i4','i5') for x in _node(r,nid)['target']['anyOf']}
        xs.update({id(x):x for x in _node(r,'i9')['target']['reveal']['anyOf']})
        for x in xs.values(): x['tmax']=x['tmax']+2   # the same target list is shared by the three steps
for _t in ('bal','ess'): _grade('icesly-budget-wand','icesly-budget-wand-v2',_t,_wand)
