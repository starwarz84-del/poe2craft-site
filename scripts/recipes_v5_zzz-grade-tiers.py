# ---- 정책 32 (사용자 확정 2026-11-11 12:06): 등급끼리 같은 옵션·같은 티어로 끝나던 레시피를 티어로 나눔 ----
# 싸게 돌리는 옵션(분열 뒤 카오스 오브, 매직 단계, 베이스 옵션)은 그대로 1티어, 비싼 징조·루프로 찾는 옵션만 낮은 등급에서 티어를 넓힘.
# 티어가 하나뿐인 옵션(주얼)은 낮은 등급에서 공개 결과를 그대로 받음(anyReveal — 카드엔 안 보임).
import json as _j32
_C32={}
def _tiers32(cls, gi):
    if cls not in _C32: _C32[cls]=_j32.load(open(f'/home/claude/poe2data/site/data/c/{cls}.json'))['groups']
    return len(_C32[cls][gi]['t'])
def _rid32(rid): return next(x for x in R if x['id']==rid)
def _tm32(r, nid, tm, gis=None):
    n=next(x for x in r['nodes'] if x['id']==nid); t=n['target']; specs=t['reveal'] if 'reveal' in t else t
    lst=specs.get('anyOf') or [specs]
    for x in lst:
        if 'gi' in x and (gis is None or x['gi'] in gis): x['tmax']=min(tm, _tiers32(r['cls'], x['gi']))
def _any32(r, nid):
    n=next(x for x in r['nodes'] if x['id']==nid); n['target']['anyReveal']=True; n.pop('fail',None)
    n['br']={'kr':'공개 결과 그대로 (다시 하지 않음)','en':'Keep whatever the reveal gives'}
for _id,_n in [('chiba-timelost-emerald-v2-bal','c6'),('mastert-timelost-emerald-v2-bal','t6'),('noble-timelost-sapphire-v2-bal','n11'),
               ('sl-5mod-jewel-v2-ess','s7'),('vodnarg-timelost-emerald-v2-ess','v4'),('zenm-timelost-sapphire-v2-ess','z5'),('mazbro-spell5-amulet-v2-bal','z13')]:
    _any32(_rid32(_id),_n)
for _t,_tm in (('bal',2),('ess',3)):
    _r=_rid32('diztoh-socket-gloves-v2-'+_t); _tm32(_r,'d10',_tm); _tm32(_r,'dm3',_tm)
    _r=_rid32('sihan-chayula-gloves-v2-'+_t); _tm32(_r,'g3',_tm-1); _tm32(_r,'g4',_tm-1)   # 카틀라 옵션은 2티어뿐: 밸런스(완벽한 엑잘) 1티어 · 에센셜(상위 엑잘) 1~2티어
_r=_rid32('gold-amulet-6line-v2-bal'); _tm32(_r,'s1',3); _tm32(_r,'d2',3)
_r=_rid32('mazbro-caster-amulet-v2-bal')
for _n in ('a10','a12','a14','a17'): _tm32(_r,_n,2)
_r=_rid32('mazbro-proj-gloves-v2-bal'); _tm32(_r,'g10',2,{73}); _tm32(_r,'g16',2)
