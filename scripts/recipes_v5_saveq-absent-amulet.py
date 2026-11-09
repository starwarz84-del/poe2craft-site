# ---- SaVeQ "I made over 2 mirrors with that Craft poe2 0.5.5" (youtu.be/S4sflKbsA8A) ----
SVA=K('SaVeQ 영상 기반','Based on SaVeQ')
c='Amulets'
def textSA(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sa_crit=textSA('increased Critical Damage Bonus','n','s'); sa_melee=textSA('to Level of all Melee Skills','n','s'); sa_proj=textSA('to Level of all Projectile Skills','n','s')
sa_maxQ=textSA('to Maximum Quality','e','p'); sa_def=textSA('increased Global Armour, Evasion and Energy Shield','e','p'); sa_spirit=textSA('to Spirit','n','p')
SA_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'saveq-absent-amulet','cls':c,'base':base(c,'Absent Amulet'),'ilvl':79,'difficulty':3,'budget':'high',
 'imp':[K('스킬 부여: 레벨 18 영원한 격노','Grants Skill: Level 18 Eternal Rage'),K('접두어 속성 부여의 최대 개수 -1개\n접미어 속성 부여의 최대 개수 -1개','-1 Prefix Modifier allowed\n-1 Suffix Modifier allowed')],
 'buildTags':[K('영원한 격노','Eternal Rage'),K('근접','Melee'),K('정신력','Spirit')],'patch':'0.5.5','created':'2026-11-09','author':SVA,
 'source':{'url':'https://www.youtube.com/watch?v=S4sflKbsA8A','title':'I made over 2 mirrors with that Craft poe2 0.5.5','channel':'SaVeQ'},
 'title':K('치명타 피해 보너스 분열 + 근접 스킬 +4(공격 퀄리티) + 정신력','fractured crit damage bonus + melee skills +4 (attack quality) + Spirit'),
 'start':{'rar':'rare','mods':[{'gi':sa_crit,'tmax':1,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffix'},{'id':'quality','kr':'퀄리티 작업','en':'Quality'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'v1','phase':'suf','do':'base','cost':'base','ts':'8:59','note':K('치명타 피해 보너스 1티어 분열 + 잡옵 1줄.','Fractured T1 critical damage bonus plus one junk line.')},
  {'id':'v2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':sa_melee,'tmax':1},{'gi':sa_proj,'tmax':1}]},'fail':{'goto':'self'},'ts':'9:55'},
  {'id':'v3','phase':'quality','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'12:15'},
  {'id':'v4','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sa_maxQ},'ts':'12:19'},
  {'id':'v5','phase':'quality','do':'quality','cur':'Reaver_Catalyst','target':{'quality':40},'ts':'12:25',
   'br':K('투사체 +3이면 갑각 기폭제(영상)','Projectile +3: Carapace Catalysts (as in the video)')},
  {'id':'v6','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'removeGi':sa_maxQ,'junk':'p'},'ts':'12:30'},
  {'id':'v7','phase':'pre','do':'essence','cur':'Perfect_Essence_of_Enhancement','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sa_def},'ts':'12:40'},
  {'id':'v8','phase':'pre','do':'desecrate','cur':'Ancient_Collarbone','target':{'unrev':'p'},'ts':'13:40'},
  {'id':'v9','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':sa_spirit,'tmax':1},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'v8','via':SA_LIGHT},'ts':'14:17',
   'br':K('대박 → 완성, 실패: 빛의 징조 + 소멸의 오브로 다시 훼손','hit → done; miss: Omen of Light + Annulment and desecrate again')},
  {'id':'v10','phase':'fin','do':'note','optional':True,'label':K('신성한 오브 · 축성 (선택)','Divine and sanctify (optional)'),'ts':'19:11',
   'br':K('축성 성공 → 스킬 레벨 상승, 실패해도 판매 가능(영상 2개 실패)','Sanctify hit → higher skill level; misses still sell (both missed in the video)')},
 ]})
