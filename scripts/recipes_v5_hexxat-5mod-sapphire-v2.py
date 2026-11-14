# ---- Hexxat Gaming 5옵션 사파이어 (youtu.be/0yK4eN3KpBo, 2026-09-30) — RECIPE-A 2026-11-14 등록(정책 13장 사용자 확정 11-14 19:55) ----
# 플로우차트 scripts/graphs/gen_hexxat_5mod_sapphire.py(hexxat-5mod-sapphire-v2.json)와 같은 단계 id(정책 31). 단계 글·확률은 build_recipes가 플로우차트에서 읽음.
# 등급: 난이도 3(분열 빗나감으로 베이스 약 4개) → 밸런스·에센셜, 비용 차이 10% 이내라 밸런스 하나만(10장 ①).
def _hx_rec(tier):
    c='Sapphire'
    TS={'b0':'0:02','pf':'1:04','a1':'1:34','k1':'2:36','d1':'3:07','r1':'3:07','n1':'3:38','g1':'4:40','c1':'5:11','f1':'4:40'}
    nodes=[{'id':'b0','phase':'base','do':'base','cost':'base','ts':TS['b0'],'note':K('치명타 피해 보너스가 최대 수치 근처인 레어 사파이어(옵션 4개, 아이템 레벨 82).','A rare Sapphire with near-max Critical Damage Bonus (four options, item level 82).')}]
    for i,d in (('pf','fracture'),('a1','chaos'),('k1','essence'),('d1','desecrate'),('r1','reveal'),('n1','annul'),('g1','exalt'),('c1','chaos'),('f1','essence')):
        nodes.append({'id':i,'phase':'main','do':d,'ts':TS[i]})
    nodes.append({'id':'ok','phase':'main','do':'note','note':K('완성.','Done.')})
    R.append({
 'id':'hexxat-5mod-sapphire-v2-'+tier,'tierGroup':'hexxat-5mod-sapphire-v2','tier':tier,'tierLabel':{'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':0,'ilvl':82,'cap':{'p':2,'s':2},'difficulty':3,'budget':'mid','unknownW':True,'basePrice':4,
 'buildTags':[K('주얼','Jewel'),K('주문 치명타','Spell crit'),K('접미어 효과','Suffix effect')],'patch':'0.5.5','created':'2026-11-14','author':K('Hexxat Gaming 영상 기반','Based on Hexxat Gaming'),
 'source':{'url':'https://www.youtube.com/watch?v=0yK4eN3KpBo','title':'Hexxat Gaming — 5 mod Sapphire craft (0.5.5)','channel':'Hexxat Gaming'},
 'title':K('치명타 피해 분열 + 주문 치명타 훼손 + 접미어 효과 5옵션','fractured crit damage + desecrated spell crit + suffix effect, five mods'),
 'start':{'rar':'rare','mods':[{'gi':11},{'junk':'s'},{'junk':'p'},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers'}],
 'nodes':nodes})
for _t in ('bal',): _hx_rec(_t)
