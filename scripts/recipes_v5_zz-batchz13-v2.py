# ---- 2026-11-10 batch 13 (사용자: 전문가부터는 2개씩): 전문가 → High-end (video) + Balance (reveal kept). Matches scripts/graphs/gen_batch13.py. ----
def _noble(r, t):
    _drop(r,'n8','n12','n13')   # optional radius reroll, the note step and the finishing catalyst quality (정책 23)
    # 사용자 확정 2026-11-10: Contempt takes a line first, so fill both prefixes (2/3; the video uses one)
    _node(r,'n3')['target']['count']=2; _node(r,'n4')['target']['chance']=2/3
    _node(r,'n5')['br']=K('실패: 소멸의 오브. 경멸 옵션이 지워지면 빗나간 접미까지 지우고 접두를 채워 경멸 다시','Miss: Annulment. If the Contempt line goes: remove the missed suffix too, refill prefixes and Contempt again')
    n10=_node(r,'n10'); n10['omens']=['Omen_of_Sinistral_Necromancy']
    n11=_node(r,'n11')
    if t=='bal': n11.pop('fail',None); n11['br']=KEEP
    else: n11['fail']={'goto':'n9','via':{'cur':'Chaos_Orb'}}
for _t in ('high','bal'): _grade8('noble-timelost-sapphire','noble-timelost-sapphire-v2',_t,_noble)
def _mzgloves(r, t):
    _drop(r,'g17')   # rune swap and Divine values are taste (정책 23)
    r['ilvl']=80   # 2026-11-12 영상 18:38 완성품 툴팁 '아이템 레벨 80'(분열에 성공한 네 번째 장갑)
    # 꿀팁 연결(2026-11-12): 플로우차트 읽기가 같은 id 단계의 tips를 이어받음 — 베이스(h1)와 카오스 상자(k11)
    _b=next(n for n in r['nodes'] if n.get('do')=='base'); _b['tips']=list(dict.fromkeys((_b.get('tips') or [])+['quality-30-optional']))
    r['nodes'].append({'id':'k11','do':'note','tips':['first-t1-side-order']})
    # 영상 재확인(2026-11-10, 10:56~): with the suffix done, a prefix junk + Sinistral Crystallisation pushes crit damage into the suffixes; the alloy the same way on a prefix
    ids=[n['id'] for n in r['nodes']]; g11,g12,g13,g14=(_node(r,x) for x in ('g11','g12','g13','g14'))
    g13.update({'omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'}}); g14['omens']=['Omen_of_Sinistral_Crystallisation']
    i=ids.index('g11'); r['nodes'][i:i+4]=[g13,g14,g11,g12]
    if t=='bal': g16=_node(r,'g16'); g16.pop('fail',None); g16['br']=KEEP
for _t in ('high','bal'): _grade8('mazbro-proj-gloves','mazbro-proj-gloves-v2',_t,_mzgloves)
