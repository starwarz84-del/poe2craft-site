# ---- SaVeQ 수익용 주문 +3 목걸이 (youtu.be/QJIhgSMS_ls, 2026-09-11) — RECIPE-A 2026-11-14 등록(정책 13장 사용자 확정 11-14 19:55) ----
# 플로우차트 scripts/graphs/gen_saveq_quality_spell_amulet.py(saveq-quality-spell-amulet-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 2(보통) → 밸런스(빗나가면 팔고 새 베이스) · 에센셜(공개 한 번, 결과 그대로).
def _sq3_rec(tier):
    c='Amulets'
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','note':K('모든 주문 스킬 레벨 +3 레어 별의 목걸이(훼손 없음, 접미 빈자리, 아이템 레벨 82).','A rare Stellar Amulet with +3 Spell Skills (no desecration, a free suffix, item level 82).')}]
    for i,d in (('d1','desecrate'),('r1','reveal'),('e1','exalt')):
        nodes.append({'id':i,'phase':'main','do':d})
    nodes.append({'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')})
    R.append({
 'id':'saveq-quality-spell-amulet-v2-'+tier,'tierGroup':'saveq-quality-spell-amulet-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Stellar Amulet'),'ilvl':82,'difficulty':2,'budget':'low','basePrice':4.5,
 'buildTags':[K('주문','Spell'),K('스킬 퀄리티','Skill quality'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-14','author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=QJIhgSMS_ls','title':'SaVeQ — profit craft: +3 spell amulet with skill quality (0.5.5)','channel':'SaVeQ'},
 'title':K('주문 +3 + 모든 스킬의 퀄리티 훼손','+3 spell skills + desecrated skill quality'),
 'start':{'rar':'rare','mods':[{'gi':17,'tmax':1},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('bal','ess'): _sq3_rec(_t)
