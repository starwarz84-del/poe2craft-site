# ---- SaVeQ "I made over 2 mirrors with that Craft poe2 0.5.5" (youtu.be/S4sflKbsA8A) — grade recipes (policy 25) ----
# Rewrites 'saveq-absent-amulet' (REPLACES) from scripts/graphs/saveq-absent-amulet-v2.json. Steps as the video (subtitles 6:11–17:50);
# the fracture prep (ilvl 79 one-line rare → chaos for T1 crit damage → divine → fill + desecrate → fracture 1/3) is cut into the base prep (FRSTART).
# G5 2026-11-13: grades by difficulty 3 (policy 10 C11) = Balance (Spirit T1–2, Light retries) + Essential (one reveal, no Light, C17-3). Steps are read from the flowchart (fcRead); ts below follow the video screen check.
c='Amulets'
def _sa(t, sec, side=None):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]: return gi
    raise Exception(t)
s2_crit=_sa('increased Critical Damage Bonus','n','s'); s2_melee=_sa('to Level of all Melee Skills','n','s'); s2_proj=_sa('to Level of all Projectile Skills','n','s')
s2_maxQ=_sa('to Maximum Quality','e','p'); s2_def=_sa('increased Global Armour, Evasion and Energy Shield','e','p'); s2_spirit=_sa('to Spirit','n','p')
def sv_amulet(tier):
    hi, ess = tier=='high', tier=='ess'; rid='saveq-absent-amulet-v2'+('' if hi else '-'+tier)
    LIGHT2={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
    rev = {'id':'v9','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'ts':'14:26'}
    bone='Ancient_Collarbone'
    rev.update({'target':{'reveal':{'gi':s2_spirit,'tmax':1 if hi else 2 if not ess else 4},'side':'p','bone':bone},'fail':{'goto':'v8','via':LIGHT2}})
    if ess: rev.pop('fail'); rev['target']['asIs']=True
    R.append({
 'id':rid,'tierGroup':'saveq-absent-amulet-v2','tier':tier,'tierLabel':{'high':K('하이엔드','High-end'),'bal':K('밸런스','Balance'),'ess':K('에센셜','Essential')}[tier],
 'cls':c,'base':base(c,'Absent Amulet'),'ilvl':79,'difficulty':3,'budget':'high',
 'imp':[K('스킬 부여: 레벨 17 영원한 격노','Grants Skill: Level 17 Eternal Rage'),   # 11-13 사용자 결정: 레벨 17로 시작(영상 완성품은 18 — 나중에 유동체로 맞출 수 있음, 유동체 단계는 정책 14장대로 뺌)
 K('접두어 속성 부여의 최대 개수 -1개\n접미어 속성 부여의 최대 개수 -1개','-1 Prefix Modifier allowed\n-1 Suffix Modifier allowed')],
 'buildTags':[K('영원한 격노','Eternal Rage'),K('근접','Melee'),K('정신력','Spirit')],'patch':'0.5.5','created':'2026-11-09','author':K('SaVeQ 영상 기반','Based on SaVeQ'),
 'source':{'url':'https://www.youtube.com/watch?v=S4sflKbsA8A','title':'I made over 2 mirrors with that Craft poe2 0.5.5','channel':'SaVeQ'},
 'title':K('치명타 피해 보너스 분열 + 근접 스킬 +4(공격 퀄리티) + 정신력','fractured crit damage bonus + melee skills +4 (attack quality) + Spirit'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fracture','kr':'분열 준비','en':'Fracture prep'},{'id':'suf','kr':'접미 두 번째 옵션','en':'Second suffix'},
           {'id':'quality','kr':'퀄리티 작업','en':'Quality'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'h0','phase':'base','do':'base','cost':'base','ts':'6:10'},
  {'id':'r0','phase':'fracture','do':'regal','cur':'Regal_Orb','target':{'junk':'any'},'knownP':1,'ts':'7:00'},
  {'id':'c1','phase':'fracture','do':'chaos','cur':'Chaos_Orb','target':{'gi':s2_crit,'tmax':1},'fail':{'goto':'self'},'ts':'7:32'},
  {'id':'e1','phase':'fracture','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':'p'},'ts':'9:08'},
  {'id':'f1','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'9:08'},
  {'id':'f2','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'gi':s2_crit},'fail':{'goto':'h0'},'ts':'9:29'},
  {'id':'f4','phase':'fracture','do':'remove','cur':'Orb_of_Annulment','expect':2,'after':{'keepOnly':[s2_crit,'junk1']},'ts':'9:58'},
  {'id':'v2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':s2_melee,'tmax':1},{'gi':s2_proj,'tmax':1}]},'fail':{'goto':'self'},'ts':'12:02'},
  {'id':'v3','phase':'quality','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'12:10'},
  {'id':'v4','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':s2_maxQ},'ts':'12:25'},
  {'id':'v5','phase':'quality','do':'quality','cur':'Reaver_Catalyst','target':{'quality':40},'ts':'12:33'},
  {'id':'v6','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'removeGi':s2_maxQ,'junk':'p'},'ts':'12:45'},
  {'id':'v7','phase':'pre','do':'essence','cur':'Perfect_Essence_of_Enhancement','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':s2_def},'ts':'12:48'},
  {'id':'v8','phase':'pre','do':'desecrate','cur':bone,'target':{'unrev':'p'},'ts':'14:00'},
  rev,
  {'id':'vs','phase':'fin','do':'note','optional':True,'label':K('축성 (선택)','Sanctify (optional)'),'ts':'19:30',
   'br':K('축성 성공 → 스킬 레벨 상승, 실패해도 판매 가능','Sanctify hit → higher skill level; misses still sell')},
 ]})
for _t in ('bal','ess'): sv_amulet(_t)
