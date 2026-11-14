# ---- SaVeQ "황혼 반지 공격 플랫 4개" (youtu.be/CZepweLtKwA, 2026-09-23, 0.5.5) — 조사 g109(docs/craft-guides.md 6차), RECIPE-D 2026-11-14 등록(정책 13장 C18) ----
# 플로우차트 scripts/graphs/gen_saveq_dusk_flat_ring.py(saveq-dusk-flat-ring-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 4(분열 1/3로 베이스 약 3개, 분열 준비 카오스 수백 개) → 하이엔드(번개·냉기 1티어)·밸런스(영상: 냉기 2티어 타협, 1~2티어).
def _sdr_rec(tier):
    c='Rings'
    TS={'b0':'3:04','p0':'4:35','p1':'4:35','p2':'6:13','p3':'6:13','p4':'6:13','p5':'8:30','m1':'8:30','m2':'10:49','m3':'10:49','m4':'10:49','m5':'10:49',
        'm6':'12:22','m7':'12:22','m8':'13:07','m9':'13:07','m9x':'13:07','m10':'16:15','m11':'16:15'}
    DO={'p0':'remove','p1':'chaos','p2':'exalt','p3':'desecrate','p4':'fracture','p5':'remove','m1':'chaos','m2':'exalt','m3':'essence','m4':'quality','m5':'exalt',
        'm6':'quality','m7':'chaos','m8':'desecrate','m9':'reveal','m9x':'annul','m10':'essence','m11':'exalt'}
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','ts':TS['b0'],'note':K('레어 황혼 반지(접두 4개·접미 2개, 아이템 레벨 79, 1 엑잘). 아이템 레벨 75면 풀이 좁아 더 좋고, 글룸 링은 사지 않음.','A rare Dusk Ring (four prefixes and two suffixes, item level 79, 1 exalt). Item level 75 narrows the pool further; do not buy a Gloam Ring.')}]
    for i,d in DO.items():
        nodes.append({'id':i,'phase':'base' if i.startswith('p') else 'main','do':d,'ts':TS[i]})
    nodes.append({'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')})
    R.append({
 'id':'saveq-dusk-flat-ring-v2-'+tier,'tierGroup':'saveq-dusk-flat-ring-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance')}[tier],
 'cls':c,'base':base(c,'Dusk Ring'),'ilvl':79,'difficulty':4,'budget':'high','basePrice':0.003,
 'buildTags':[K('공격','Attack'),K('원소 플랫','Elemental flat'),K('균열·촉진','Breach and catalysts')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=CZepweLtKwA','title':'황혼 반지 공격 플랫 4개 (원소 플랫 분열 → 균열·촉진 → 절사 옮김 → 훼손 냉기 플랫 → 재빠른 합금)','channel':'SaVeQ'},
 'title':K('원소 공격 플랫 분열 + 플랫 4개 + 재빠른 합금 황혼 반지','fractured elemental attack flat + four flats + Swift Alloy Dusk Ring'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'p'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('high','bal'): _sdr_rec(_t)
