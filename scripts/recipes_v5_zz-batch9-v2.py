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
for _t in ('bal','ess'): _grade8('lilbotq-emerald','lilbotq-emerald-v2',_t,_jewel('l4',('l5','l5b','l6','l7'),'l8'))
def _contFail(nid, back, first, kr, en):
    # 사용자 확정 2026-11-10: a failed contempt took a suffix — the first one → start again, the second → Dextral Annulment on the +1 prefix line, then that suffix step again
    def f(r):
        n=_node(r,nid); n['fail']={'goto':back,'via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':first}; n['br']=K(kr,en)
    return f
_emF=_contFail('e4','e2','e1','실패: 공격 치명타 피해가 지워지면 새 베이스, 공격 속도가 지워지면 우측 소멸의 징조 + 소멸의 오브로 +1 접두 허용 제거 → 2번부터','Miss: crit damage gone → new base; attack speed gone → Dextral Annulment on +1 prefix allowed, then step 2')
_saF=_contFail('j4','j2','j1','실패: 지워진 치명타 옵션은 우측 소멸의 징조 + 소멸의 오브로 +1 접두 허용 제거 → 2번부터 (남은 치명타까지 지워지면 1번부터)','Miss: Dextral Annulment on +1 prefix allowed, then step 2 (step 1 if the other crit goes too)')
def _then(f, g):
    def h(r, t): f(r, t); g(r)
    return h
for _t in ('bal','ess'): _grade8('diztoh-5mod-emerald','diztoh-5mod-emerald-v2',_t,_then(_jewel('e6',('e7','e8','e9'),'e10',reveal_any=[7,55]),_emF))
for _t in ('bal','ess'): _grade8('diztoh-5mod-sapphire','diztoh-5mod-sapphire-v2',_t,_then(_jewel('j6',('j7','j8','j9'),'j10'),_saF))
def _zenm(r, t):
    if t=='ess': z5=_node(r,'z5'); z5.pop('fail',None); z5['br']=KEEP
for _t in ('bal','ess'): _grade8('zenm-timelost-sapphire','zenm-timelost-sapphire-v2',_t,_zenm)
