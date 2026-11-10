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
for _t in ('bal','ess'): _grade8('diztoh-5mod-emerald','diztoh-5mod-emerald-v2',_t,_jewel('e6',('e7','e8','e9'),'e10',reveal_any=[7,55]))
for _t in ('bal','ess'): _grade8('diztoh-5mod-sapphire','diztoh-5mod-sapphire-v2',_t,_jewel('j6',('j7','j8','j9'),'j10'))
def _zenm(r, t):
    if t=='ess': z5=_node(r,'z5'); z5.pop('fail',None); z5['br']=KEEP
for _t in ('bal','ess'): _grade8('zenm-timelost-sapphire','zenm-timelost-sapphire-v2',_t,_zenm)
