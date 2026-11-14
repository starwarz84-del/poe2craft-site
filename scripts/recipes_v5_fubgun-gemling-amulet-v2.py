# ---- Fubgun 젬링 +4 목걸이 (youtu.be/bz5DJ0csq58, 2026-09-09) — RECIPE-A 2026-11-14 등록(정책 13장 사용자 확정 11-14 19:55) ----
# 플로우차트 scripts/graphs/gen_fubgun_gemling_amulet.py(fubgun-gemling-amulet-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 3(어려움) → 밸런스(영상: 저항 2~3티어, 퀄리티까지 빛의 징조) · 에센셜(저항 엑잘·공개 한 번씩 결과 그대로).
def _fgm_rec(tier):
    c='Amulets'
    TS={'h0':'6:03','k1':'6:35','w1':'1:09','r1':'9:48'}
    nodes=[{'id':'h0','phase':'base','do':'base','cost':'base','ts':TS['h0'],'note':K('모든 주문 스킬 레벨 +3 분열 황금 목걸이(아이템 레벨 80) — 직접 분열하면 베이스 8~9 div, 1/3, 평균 30 div.','A Gold Amulet with fractured +3 Spell Skills (item level 80): fracturing it yourself costs 8–9 div per base at 1 in 3, about 30 div on average.')}]
    for i,d in (('a0','remove'),('k1','chaos'),('e1','exalt'),('q1','essence'),('q2','quality'),('e2','exalt'),('e2x','annul'),('kc','remove'),('q3','quality'),('w1','chaos'),('q4','essence'),('e3','exalt'),('k2','chaos'),('d1','desecrate'),('r1','reveal'),('r1x','annul')):
        n={'id':i,'phase':'main','do':d}
        if i in TS and i!='w1': n['ts']=TS[i]
        nodes.append(n)
    nodes.append({'id':'ok','phase':'main','do':'note','ts':'9:52','note':K('완성.','Done.')})
    R.append({
 'id':'fubgun-gemling-amulet-v2-'+tier,'tierGroup':'fubgun-gemling-amulet-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Gold Amulet'),'ilvl':80,'difficulty':3,'budget':'mid','basePrice':30,
 'buildTags':[K('주문','Spell'),K('정신력','Spirit'),K('스킬 퀄리티','Skill quality'),K('촉진','Catalysing')],'patch':'0.5.5','created':'2026-11-14','author':K('Fubgun 영상 기반','Based on Fubgun'),
 'source':{'url':'https://www.youtube.com/watch?v=bz5DJ0csq58','title':'Fubgun — Gemling +4 spell amulet craft (0.5.5)','channel':'Fubgun'},
 'title':K('주문 +3 분열 + 시전 퀄리티 34%(+4) + 정신력·생명력·전역 방어 + 스킬 퀄리티 훼손','fractured +3 spells + 34% caster quality (+4) + spirit, life, global defences + desecrated skill quality'),
 'start':{'rar':'rare','mods':[{'gi':17,'tmax':1,'fr':True},{'junk':'p'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('bal','ess'): _fgm_rec(_t)
