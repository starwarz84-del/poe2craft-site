# ---- 2026-11-10: the remaining recipes as grade recipes, easiest first (사용자: "플로우차트로 작성되지 않은 리스트를 쉬운 것부터 차례대로") ----
# Batch 9 = four 보통 jewels → Balance (video) + Essential (keep the reveal, leave the contempt line, Ferocity once). Matches scripts/graphs/gen_batch9.py.
# The finishing Refined catalyst quality step is left out (like taste runes, 정책 23). (_grade8 from recipes_v5_zz-batch8-v2.py)
def _jewel(rev, drop_ess, fer, reveal_any=None):
    def ed(r, t):
        _drop(r, *[n['id'] for n in r['nodes'] if n['do']=='quality' and r['nodes'].index(n)>len(r['nodes'])-4])
        rv=_node(r, rev)
        if reveal_any: rv['target']['reveal']={'anyOf':[{'gi':g} for g in reveal_any]}
        if t=='ess':
            rv.pop('fail',None); rv['br']=KEEP
            _drop(r, *drop_ess)
            f=_node(r, fer); f.pop('fail',None); f['target'].pop('chance',None); f['br']=K('접두 하나가 지워짐 — 결과 그대로','One prefix goes — keep whatever comes')
    return ed
def _then(f, g):
    def h(r, t): f(r, t); g(r)
    return h
def _lbBudget(r, t):
    _node(r,'l3')['omens']=['Omen_of_Dextral_Necromancy']
    if t!='ess': return
    # 영상 3:35~ 가성비: 좋은 옵션 3개(접두 2 + 공격 속도) + 잡옵 접미 주얼을 싸게 사서 농축된 액체 두려움 50/50
    r['start']={'rar':'rare','mods':[{'gi':7},{'junk':'s'},{'gi':6},{'junk':'p'}]}
    l1=_node(r,'l1'); l1['note']=K('좋은 접두 2개 + 공격 속도 + 잡옵 접미 희귀 에메랄드 구입(약 1 카오스).','Buy a rare Emerald with two good prefixes, attack speed and a junk suffix (about 1 Chaos).')
    r['nodes']=[l1,{'id':'b1','phase':'con','do':'essence','cur':'Concentrated_Liquid_Fear','target':{'gi':113,'chance':0.5},'fail':{'goto':'restart'},
        'br':K('접미 2개 중 잡옵이 지워지면 성공, 공격 속도가 지워지면 새 주얼','The junk suffix goes → done; attack speed goes → a new jewel')},_node(r,'l9')]
_lbE=_then(_jewel('l4',('l5','l5b','l6','l7'),'l8'),lambda r: _lbBudget(r,'bal'))
for _t in ('bal','ess'): _grade8('lilbotq-emerald','lilbotq-emerald-v2',_t,lambda r,t: _lbE(r,'bal'))   # F2b 11-13: 난이도 표 2 → 밸런스·에센셜(15:42), 단계는 플로우차트(graph2recipe) — 옛 에센셜 가성비 길(_lbBudget ess)은 쓰지 않음
def _contFail(nid, back, first, kr, en):
    # 사용자 확정 2026-11-10: a failed contempt took a suffix — the first one → start again, the second → Dextral Annulment on the +1 prefix line, then that suffix step again
    def f(r):
        n=_node(r,nid); n['fail']={'goto':back,'via':{'cur':'Orb_of_Annulment'},'lost':first}; n['br']=K(kr,en)
    return f
_emF=_contFail('e4','e2','e1','실패: 공격 치명타 피해가 지워지면 새 베이스, 공격 속도가 지워지면 접두가 잡옵뿐이라 소멸의 오브로 +1 접두 허용 제거 → 2번부터','Miss: crit damage gone → new base; attack speed gone → plain Annulment until +1 prefix allowed goes (prefixes are junk), then step 2')
_saF=_contFail('j4','j1','j1','실패: 영상처럼 소멸의 오브로 모두 지우고 1번 카오스 오브부터 다시','Miss: annul everything and start again at step 1 (Chaos), as the video')
for _t in ('bal','ess'): _grade8('diztoh-5mod-emerald','diztoh-5mod-emerald-v2',_t,_then(_jewel('e6',('e7','e8','e9'),'e10',reveal_any=[7,55]),_emF))
for _t in ('bal','ess'): _grade8('diztoh-5mod-sapphire','diztoh-5mod-sapphire-v2',_t,_then(_jewel('j6',('j7','j8','j9'),'j10'),_saF))
def _zenm(r, t):
    z5=_node(r,'z5')
    if t=='ess': z5.pop('fail',None); z5['br']=KEEP
    else:   # Zen_M 영상 6:17: 빛의 징조 없이 징조 없는 소멸의 오브 — 1/2로 훼손 옵션, 좋은 접미가 지워지면 카오스 오브부터
        z5['fail']={'goto':'z4','via':{'cur':'Orb_of_Annulment'},'lost':'z3'}
        z5['br']=K('빗나가면 징조 없는 소멸의 오브. 1/2로 훼손 옵션이 지워지고, 좋은 접미가 지워지면 카오스 오브부터','Miss: a plain Annulment (1/2 the desecrated line; the good suffix gone: Chaos again)')
for _t in ('bal','ess'): _grade8('zenm-timelost-sapphire','zenm-timelost-sapphire-v2',_t,_zenm)
