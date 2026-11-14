# ---- 시한 젬링 저격용 힘 투구 (youtu.be/iXL71H94AdM, 2026-10-10, 0.5.5) — 조사 g101(docs/craft-guides.md 6차), RECIPE-C 2026-11-14 등록(정책 13장 C18) ----
# 플로우차트 scripts/graphs/gen_sihan_gemling_greathelm.py(sihan-gemling-greathelm-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 4(전문가 — 밸런스도 우측 소멸의 징조 약 59개·평균 약 720 div) → 하이엔드(1티어)·밸런스(영상: 치명타 확률·방어도 원소 적용 2티어 이상).
def _shg_rec(tier):
    c='Helmets_str'
    TS={'b0':'6:33','c1':'10:03','s1':'10:52','s2':'10:52','e1':'22:54','x1':'23:10','d1':'24:07','d2':'24:07','d2x':'28:00','d3':'28:00'}
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','ts':TS['b0'],'note':K('방어도 % 분열 제국의 대헬름(아이템 레벨 80, 퀄리티 20%).','An Imperial Greathelm with fractured % armour (item level 80, 20% quality).')}]
    for i,d in (('c1','chaos'),('s1','remove'),('s2','exalt'),('e1','essence'),('x1','exalt'),('d1','desecrate'),('d2','reveal'),('d2x','annul'),('d3','desecrate')):
        n={'id':i,'phase':'main','do':d}
        if i in TS: n['ts']=TS[i]
        nodes.append(n)
    nodes.append({'id':'ok','phase':'main','do':'note','ts':'32:47','note':K('완성.','Done.')})
    R.append({
 'id':'sihan-gemling-greathelm-v2'+('' if tier=='high' else '-'+tier),'tierGroup':'sihan-gemling-greathelm-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance')}[tier],
 'cls':c,'base':base(c,'Imperial Greathelm'),'ilvl':80,'difficulty':4,'budget':'high',
 'buildTags':[K('방어도','Armour'),K('치명타','Critical'),K('젬링','Gemling')],'patch':'0.5.5','created':'2026-11-14','author':K('시한 영상 기반','Based on 시한'),
 'source':{'url':'https://www.youtube.com/watch?v=iXL71H94AdM','title':'젬링 저격용 힘 투구 (방어도 % 분열 → 카오스 치명타 → 우측 소멸 + 엑잘 → 심연 징표 → 고대 갈비뼈 방어도 플랫)','channel':'시한'},
 'title':K('방어도 % 분열 + 치명타 확률·방어도 원소 적용 + 방어도 플랫 훼손 힘 투구','fractured % armour + crit chance and armour to elemental + desecrated flat armour helmet'),
 'start':{'rar':'rare','quality':20,'mods':[{'gi':9,'tmax':1,'fr':True},{'junk':'p'},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('high','bal'): _shg_rec(_t)
