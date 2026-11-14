# ---- Hax 마나 스태커 오래된 사파이어 (youtu.be/qATcKacI83o, 2026-09-09) — RECIPE-A 2026-11-14 등록(정책 13장 사용자 확정 11-14 19:55) ----
# 플로우차트 scripts/graphs/gen_hax_timelost_sapphire.py(hax-timelost-sapphire-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 2(보통) → 밸런스(영상, 최대 마나까지 빛의 징조로 다시) · 에센셜(공개 한 번, 결과 그대로).
def _hax_rec(tier):
    c='Time-Lost_Sapphire'
    TS={'b0':'1:32','m2':'2:02','m3':'2:32','m4':'3:35','m4x':'5:07','m5':'5:07'}
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','ts':TS['b0'],'note':K('접미 주문 치명타 피해 보너스 + 주문 치명타 명중 확률 레어 오래된 사파이어(타락·제작·훼손·분열 없음, 아이템 레벨 82).','A rare Time-Lost Sapphire with spell crit damage and spell crit chance suffixes (not corrupted, crafted, desecrated or fractured, item level 82).')}]
    for i,d in (('m2','essence'),('m3','desecrate'),('m4','reveal'),('m4x','annul'),('m5','desecrate')):
        nodes.append({'id':i,'phase':'main','do':d,'ts':TS[i]})
    nodes.append({'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')})
    R.append({
 'id':'hax-timelost-sapphire-v2-'+tier,'tierGroup':'hax-timelost-sapphire-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':0,'ilvl':82,'cap':{'p':2,'s':2},'difficulty':2,'budget':'mid','unknownW':True,'basePrice':11,
 'buildTags':[K('주얼','Jewel'),K('오래된 주얼','Time-Lost jewel'),K('주문 치명타','Spell crit'),K('마나','Mana')],'patch':'0.5.5','created':'2026-11-14','author':K('Hax 영상 기반','Based on Hax'),
 'source':{'url':'https://www.youtube.com/watch?v=qATcKacI83o','title':'Hax — Mana stacker Time-Lost Sapphire craft (0.5.5)','channel':'Hax'},
 'title':K('매우 넓은 반경 + 최대 마나 훼손 + 주문 치명타 접미 2개','Very Large radius + desecrated maximum mana + two spell crit suffixes'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'p'},{'gi':16},{'gi':50}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('bal','ess'): _hax_rec(_t)
