# ---- 2026-11-10: five more recipes as grade recipes (policy 25/30, 어려움 이하 → 밸런스 + 에센셜) ----
# Built from each original recipe (copied out of R), matching scripts/graphs/gen_batch6.py. The originals are dropped by REPLACES in build_recipes.py.
# Video transcripts re-read 2026-11-10: expensive retries (side Annulment omens) only where the video does them; Essential keeps results.
# (_orig, _grade, _node come from recipes_v5_zz-batch5-v2.py, which runs first)
def _drop(r, *ids): r['nodes']=[n for n in r['nodes'] if n['id'] not in ids]
KEEP=K('결과 그대로 진행','Keep whatever comes')

# 1. Diztoh 에너지 보호막 투구 — Balance = video targets (+ Light when it completes two good prefixes), Essential = looser, results kept
def _esh(r, t):
    pT,rT=(3,1) if t=='bal' else (4,2)
    pre=[{'gi':de_esp,'tmax':pT},{'gi':de_rarP,'tmax':rT}]
    e3=_node(r,'e3'); e3.pop('fail',None); e3['target']={'anyOf':pre,'asIs':True,'side':'p'}
    e3['br']=K('에너지 보호막 % 또는 희귀도. 안 나와도 그대로(소멸의 오브 반복 없음).','% energy shield or rarity; a miss stays (no Annulment loop).')
    e4=_node(r,'e4'); e4['target']['reveal']={'anyOf':pre}
    if t=='bal': e4['br']=K('좋은 줄 → 완성, 빗나감: 빛의 징조 + 소멸의 오브 → 고대 갈비뼈로 다시 (엑잘이 맞았을 때만)','Hit → done; miss: Light + Annulment, Ancient Rib again (only when the exalt hit)')
    else: e4.pop('fail',None); e4['br']=KEEP
    _drop(r,'e5','e6','e7')   # idols and runes are taste (정책 23); the corruption is optional
    r['nodes'].append({'id':'e8','phase':'fin','do':'note','ts':'4:00','note':K('완성. 퀄리티 20%, 소켓은 취향대로.','Done. 20% quality; sockets to taste.')})
for _t in ('bal','ess'): _grade('diztoh-es-helmet','diztoh-es-helmet-v2',_t,_esh)

# 2. Belton +8 완드 — Balance = video (Sinistral Annulment retry on the first prefix exalt, Light on the suffix reveal), Essential = results kept, Greater Exalt last
def _belton(r, t):
    xT,yT,sT,cT=(2,3,1,2) if t=='bal' else (4,5,3,4)
    pre=[{'gi':bt_xF,'tmax':xT},{'gi':bt_xC,'tmax':xT},{'gi':bt_xL,'tmax':xT},{'gi':bt_spell,'tmax':yT},{'gi':bt_hyb,'tmax':1}]
    suf=[{'gi':bt_regen,'tmax':sT},{'gi':bt_scrit,'tmax':cT},{'gi':bt_cdmg,'tmax':cT}]
    b3=_node(r,'b3'); b6=_node(r,'b6'); b7=_node(r,'b7')
    b3['target']['anyOf']=pre; b6['target']['reveal']={'anyOf':suf}
    b7.pop('fail',None); b7['target']={'anyOf':pre,'asIs':True,'side':'p'}
    b7['br']=K('안 나와도 그대로(영상: 카오스 피해 3티어로 타협)','A miss stays (the video kept tier 3 chaos damage)')
    if t=='ess':
        b3.pop('fail',None); b3['target']['asIs']=True; b3['br']=KEEP
        b6.pop('fail',None); b6['br']=KEEP; b7['cur']='Greater_Exalted_Orb'
for _t in ('bal','ess'): _grade('belton-plus8-wand','belton-plus8-wand-v2',_t,_belton)

# 3. LilBotQ 방어도 방패 — Balance = video (own build: Light until T1), Essential = the selling route (settle the reveal), Greater Exalts for suffixes
def _shield(r, t):
    pT,hT=(1,1) if t=='bal' else (2,3)
    _node(r,'l2')['target']['tmax']=pT
    l4=_node(r,'l4'); l4['target']['reveal']['tmax']=hT
    _drop(r,'l5','l6')   # Perfect Iron Runes are taste (정책 23)
    if t=='ess':
        l4.pop('fail',None); l4['br']=K('나온 티어로 타협(판매용)','Settle for the tier you get (to sell)')
        for nid in ('l7','l8'): _node(r,nid)['cur']='Greater_Exalted_Orb'
for _t in ('bal','ess'): _grade('lilbotq-armour-shield','lilbotq-armour-shield-v2',_t,_shield)

# 4. Diztoh 정신력 로브 — Chaos Orb for flat ES (정책 16, cheaper than the video's Greater Chaos in the sim); Balance = Perfect Exalt + Whittling for a resistance,
#    Essential = lower tiers, Greater Exalts, resistances as they come
def _robe(r, t):
    r['start']['mods'][0]['tmax']=4 if t=='bal' else 6
    v2=_node(r,'v2'); v2['cur']='Chaos_Orb'; v2['target']['tmax']=1 if t=='bal' else 2
    v3=_node(r,'v3'); v3['target']['tmax']=2 if t=='bal' else 3; v3['cur']='Perfect_Exalted_Orb' if t=='bal' else 'Greater_Exalted_Orb'
    if t=='bal':
        _node(r,'v8')['br']=K('가장 낮은 줄이 버릴 줄일 때만. 정신력 점유 효율(레벨 65)이 가장 낮아지면 그대로 타협.','Only while the lowest line is junk; once the reservation line (level 65) is lowest, settle.')
    else:
        _drop(r,'v8'); _node(r,'v7')['cur']='Greater_Exalted_Orb'; _node(r,'v7')['br']=KEEP
for _t in ('bal','ess'): _grade('diztoh-vile-robe','diztoh-vile-robe-v2',_t,_robe)

# 5. Diztoh +5 부적 — results kept (the video settled too), no side-Annulment fork; Essential = cheaper fire base + Greater Exalts
def _tal(r, t):
    r['start']['mods'][1]['tmax']=3 if t=='bal' else 5
    t5=_node(r,'t5'); t5['target']={'anyOf':TL_PRE,'asIs':True,'side':'p'}; t5['br']=KEEP
    t9=_node(r,'t9'); t9.pop('fail',None); t9['target']={'gi':tl_cdmg,'tmax':2,'asIs':True,'side':'s'}
    t9['br']=K('안 나와도 그대로(영상: 정확도 + 빛 반경)','A miss stays (accuracy + light radius in the video)')
    _drop(r,'t5b','t7','t10')   # t10 = Divine for values (not crafting); the Sinistral Annulment fork (expensive) and the Iron Rune (taste, 정책 23)
    if t=='ess': t5['cur']='Greater_Exalted_Orb'; t9['cur']='Greater_Exalted_Orb'
    _node(r,'t4')['br']=K('아마나무 접미 3개가 전부 나와서 공격 속도 확정.','All three Amanamu suffixes show, so attack speed is sure.')
    _node(r,'t4').pop('fail',None)
for _t in ('bal','ess'): _grade('diztoh-talisman','diztoh-talisman-v2',_t,_tal)
