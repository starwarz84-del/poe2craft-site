# ---- D3lebronjames "아크 토템 마나 기억 반지" (youtube JeA3cg79qZY, 2026-09-12, 0.5.5) — 조사 g126(docs/craft-guides.md 7차), RECIPE-E 2026-11-14 등록(정책 13장 C18) ----
# 플로우차트 scripts/graphs/gen_d3lebron_mnemonic_ring.py(d3lebron-mnemonic-ring-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 4(시뮬 하이엔드 평균 약 760 div, 비싼 징조 50개 넘게) → 하이엔드(최대 마나 1티어, 유효 접미 1~2티어)·밸런스(최대 마나 1~2티어, 유효 접미 1~4티어).
def _d3m_rec(tier):
    c='Rings'
    TS={'b0':'1:21','p1':'3:24','p2':'3:24','p3':'4:55','p4':'5:15','p5':'5:35','p6':'5:35','m1':'6:00','m2':'9:44','m3':'10:05','m4':'12:10',
        'm5':'13:13','m6':'13:13','m6x':'14:35','s1':'15:41','s2':'15:41','s3':'15:41'}
    DO={'p1':'essence','p2':'desecrate','p3':'fracture','p4':'remove','p5':'essence','p6':'quality','m1':'chaos','m2':'exalt','m3':'essence','m4':'exalt',
        'm5':'desecrate','m6':'reveal','m6x':'annul','s1':'remove','s2':'exalt','s3':'chaos'}
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','ts':TS['b0'],'note':K('시전 속도 1티어(22~24%) 레어 기억 반지, 옵션 4개에 분열·타락·성소화 없음(아이템 레벨 79, 1~2 div). 마나 소모 효율 기억 반지는 분열 전에도 30~35 div라 피함.','A rare Mnemonic Ring with T1 cast speed (22–24%), four options and no fracture, corruption or sanctification (item level 79, 1–2 div). Mana cost efficiency rings already cost 30–35 div before the fracture, so the video avoids them.')}]
    for i,d in DO.items():
        nodes.append({'id':i,'phase':'base' if i.startswith('p') else 'main','do':d,'ts':TS[i]})
    nodes.append({'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')})
    R.append({
 'id':'d3lebron-mnemonic-ring-v2-'+tier,'tierGroup':'d3lebron-mnemonic-ring-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance')}[tier],
 'cls':c,'base':base(c,'Mnemonic Ring'),'ilvl':79,'difficulty':4,'budget':'high','basePrice':1.5,
 'buildTags':[K('주문','Spell'),K('마나','Mana'),K('아크 토템','Arc totem')],'patch':'0.5.5','created':'2026-11-14',
 'author':K('D3lebronjames 영상 기반','Based on D3lebronjames'),
 'source':{'url':'https://www.youtube.com/watch?v=JeA3cg79qZY','title':'아크 토템 마나 기억 반지 (징표 훼손으로 분열 1/3 → 균열의 에센스 + 신경 기폭제 → 카오스 마나 → 결정화 + 완벽한 정신의 에센스 → 뒤바뀐 빗장뼈 카오스 획득)','channel':'D3lebronjames'},
 'title':K('시전 속도 분열 + 마나 3개 + 주문 카오스 획득 기억 반지','fractured cast speed + three mana options + spell chaos gain Mnemonic Ring'),
 'start':{'rar':'rare','mods':[{'gi':34,'tmax':1},{'junk':'p'},{'junk':'p'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('high','bal'): _d3m_rec(_t)
