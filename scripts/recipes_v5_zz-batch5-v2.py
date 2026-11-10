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
    w6=_node(r,'w6'); w6.pop('fail',None)   # the Liege shows all three Amanamu suffixes (영상 5:06): attack speed is sure
    am=[gi for gi,gr in enumerate(cd(r['cls'])['groups']) if gr['s']=='d' and gr['g']=='s' and 'amanamu_mod' in gr['tg']]
    w6['target']['reveal']={'anyOf':[{'gi':g} for g in am]}
    w6['br']=K('아마나무 3개가 전부 나와서 공격 속도 확정. 마지막 엑잘에서 일반 공격 속도가 떴으면 관통·정신력 효율 중 하나.','All three Amanamu lines show, so attack speed is sure; with a normal attack speed from the last exalt, take pierce or spirit efficiency.')
for _t in ('bal','ess'): _grade('ragna-ashot-bow','ragna-ashot-bow-v2',_t,_bow)

# 2. TheSaneExile 저항 벨트 — Balance = video (T1 life + T1–2 lightning res), Essential = both T1–3
def _belt(r, t):
    r['start']['mods'][0]['tmax'] = 1 if t=='bal' else 3; r['start']['mods'][1]['tmax'] = 2 if t=='bal' else 3
    # 사용자 확정 2026-11-10: finish the two empty prefixes with Greater Exaltation + Greater Exalted Orb (keep whatever comes)
    _node(r,'b4')['br']=K('울라만 저항 → 접두 마무리, 실패: 빛의 징조 + 소멸의 오브로 지우고 다시 훼손','Ulaman resist → finish the prefixes; miss: Light + Annulment and desecrate again')
    r['nodes']=[n for n in r['nodes'] if n['id']!='b5']+[
      {'id':'b5','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','p']},
       'note':K('접두 2자리 랜덤 옵션 — 결과 그대로.','The two empty prefixes: random lines, keep whatever comes.')},
      {'id':'b6','phase':'fin','do':'note','note':K('완성.','Done.')}]
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
    lt=2
    if t=='ess':
        r['start']['mods'][0]['tmax']=2; r['start']['mods'][1]['tmax']=3; lt=4
    # 사용자 확정 2026-11-10: the reveal also stops on a chaos dual resist (3 kinds) or T1–3 chaos res — far likelier, cheaper
    b5=_node(r,'b5'); b5['target']['reveal']={'anyOf':[{'gi':3,'tmax':lt},{'gi':23},{'gi':24},{'gi':33},{'gi':4,'tmax':3}]}
    b5['br']=K('번개 저항·카오스 듀얼 저항·카오스 저항(1~3티어) 중 하나 → 완성, 실패: 빛의 징조 + 소멸의 오브로 다시 훼손','Lightning res, a chaos dual res or T1–3 chaos res → done; miss: Light + Annulment and desecrate again')
for _t in ('bal','ess'): _grade('lilbotq-budget-boots','lilbotq-budget-boots-v2',_t,_boots)

# 5. Icesly 가성비 완드 — 2026-11-10 다시 작성(영상 다시 확인, 사용자: 가성비엔 비싼 오브 없이). 그래프 scripts/graphs/gen_batch5.py와 같은 흐름.
#    소멸의 오브 없음: 빗나간 엑잘은 천공의 합금이 지우게 함(영상 캡션). 제왕의 오브는 우측 대관식의 징조로 접미에. 엑잘은 상위 엑잘티드 오브.
#    밸런스 = 영상 티어 + 남은 훼손이 빗나가면 빛의 징조, 에센셜 = 번개 +5 1~2티어·접두 목표 넓힘·결과 그대로.
def _wand(r, t):
    xT,yT=(2,3) if t=='bal' else (4,5)
    r['start']['mods'][0]['tmax']=1 if t=='bal' else 2
    pre=[{'gi':ic_lin,'tmax':yT},{'gi':ic_spell,'tmax':yT},{'gi':ic_xL,'tmax':xT},{'gi':ic_xC,'tmax':xT},{'gi':ic_xF,'tmax':xT}]
    i1=_node(r,'i1'); i3=_node(r,'i3'); i7=_node(r,'i7')
    i1['note']=K('모든 번개 주문 스킬 레벨 +5 매직 완드(접두 잡옵 1개, 아이템 레벨 81). 화염·냉기 등 다른 원소 +5도 같은 방법.','A magic wand with +5 to all lightning spell skills (one junk prefix, item level 81). Other elements work the same way.')
    miss=K('번개·주문·추가 피해 획득이면 다음, 빗나가면 그대로 두고 {#i8}에서 좌측 결정화의 징조 + 천공의 합금으로 그 옵션을 지움(소멸의 오브 안 씀)',
           'Lightning, spell or extra damage → next; a miss stays and the Celestial Alloy eats it at {#i8} (Sinistral Crystallisation) — no Annulment')
    nodes=[i1,
      {'id':'i2','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','omens':['Omen_of_Dextral_Coronation'],'target':{'junk':'s'},'ts':'1:41'},
      i3,
      {'id':'i4','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','target':{'anyOf':pre,'asIs':True,'side':'p'},'ts':'3:09','br':miss},
      {'id':'i5','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','target':{'anyOf':pre,'asIs':True,'side':'p'},'ts':'3:29','br':miss},
      {'id':'i6','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'p'},'ts':'3:46',
       'br':K('엑잘 옵션 2개가 모두 좋을 때만. 하나가 빗나갔으면 {#i8} 다음에 훼손.','Only when both exalts hit; with a miss, desecrate after {#i8}.')},
      i7,
      {'id':'i8','phase':'fin','do':'essence','cur':'Celestial_Alloy','target':{'gi':ic_cel,'chance':1/3,'missDrop':ic_lin},'ts':'4:38',
       'br':K('미공개 훼손이 지워지면 → 완성. 좋은 접두가 지워지면 → 남은 훼손 공개.','Takes the unrevealed desecration → done; takes a good prefix → reveal the desecration.')},
      {'id':'i9','phase':'fin','branch':{'of':'i8','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],
       'target':{'reveal':{'anyOf':pre},'side':'p','bone':'Preserved_Jawbone'},'ts':'5:40'}]
    if t=='bal':
        nodes[-1]['fail']={'goto':'self','via':dict(IC_LIGHT, also=[{'cur':'Preserved_Jawbone'},{'cur':'Omen_of_Abyssal_Echoes'}])}
        nodes[-1]['br']=K('좋은 옵션 → 완성, 빗나감: 빛의 징조 + 소멸의 오브 → 보존된 턱뼈로 다시 훼손','Hit → done; miss: Light + Annulment, desecrate again with a Preserved Jawbone')
    else:
        nodes[-1]['br']=K('결과 그대로 완성(빛의 징조 안 씀)','Keep whatever comes (no Light)')
    r['nodes']=nodes
for _t in ('bal','ess'): _grade('icesly-budget-wand','icesly-budget-wand-v2',_t,_wand)
