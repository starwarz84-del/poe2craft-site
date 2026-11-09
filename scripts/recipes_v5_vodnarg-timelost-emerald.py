# ---- Vodnarg "[POE 2 0.5] Craft OP Time-Lost Jewels for Any Build! Step By Step Crafting Guide" (youtu.be/3tFs16SXkD8) ----
VD5=K('Vodnarg 영상 기반','Based on Vodnarg')
c='Time-Lost_Emerald'
def textV(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
vd_cc=textV('increased Critical Hit Chance for Attac','n','s'); vd_cdA=textV('Critical Damage Bonus for At','n','s'); vd_cdS=textV('Critical Damage Bonus with S','n','s')
vd_as=textV('(1—2)% increased Attack Speed','n','s'); vd_asS=textV('increased Attack Speed with Spears','n','s')
vd_pdmg=textV('(1—2)% increased Projectile Damage','n','p'); vd_spear=textV('increased Damage with Spears','n','p'); vd_pspd=textV('increased Projectile Speed','n','p'); vd_adm=textV('increased Attack Damage','n','p')
vd_plusS=textV('+1 Suffix Modifier allowed','x','p'); vd_mel=textV('Upgrades Radius to Very Large','x','p')
assert cd(c)['groups'][vd_as]['t'][0][5].strip().endswith('Attack Speed') and 'if' not in cd(c)['groups'][vd_pdmg]['t'][0][5]
VD_PRE=[{'gi':vd_pdmg},{'gi':vd_spear},{'gi':vd_pspd},{'gi':vd_adm}]
R.append({
 'id':'vodnarg-timelost-emerald','cls':c,'base':0,'ilvl':80,'cap':{'p':2,'s':2},'difficulty':3,'budget':'medium','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('오래된 주얼','Time-Lost jewel'),K('공격 치명타','Attack crit'),K('돌개바람','Twister')],'patch':'0.5','created':'2026-11-09','author':VD5,
 'source':{'url':'https://www.youtube.com/watch?v=3tFs16SXkD8','title':'[POE 2 0.5] Craft OP Time-Lost Jewels for Any Build! Step By Step Crafting Guide','channel':'Vodnarg'},
 'title':K('분열 없이 공격 속도·치명타 3접미 + 매우 넓은 반경','no fracture: three attack speed/crit suffixes + Very Large radius'),
 'start':{'rar':'rare','mods':[{'gi':vd_as},{'gi':vd_cdS},{'junk':'p'},{'junk':'p'}]},
 'phases':[{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'des','kr':'3번째 접미 (훼손)','en':'Third suffix (desecrated)'},{'id':'pre','kr':'접두 · 우울','en':'Prefixes and Melancholy'}],
 'nodes':[
  {'id':'v1','phase':'con','do':'base','cost':'base','ts':'2:50',
   'note':K('원하는 접미 2줄 + 접두 2줄 희귀 오래된 에메랄드(분열·타락·훼손·제작 옵션 없음).','Rare Time-Lost Emerald with two wanted suffixes and two prefixes (no fracture, corruption, desecration or crafted mod).')},
  {'id':'v2','phase':'con','do':'essence','cur':'Ancient_Potent_Liquid_Contempt','knownP':True,'target':{'gi':vd_plusS,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'restart'},'ts':'3:48',
   'br':K('접미 +1 → 다음, 접두 +1이 뜨면 → 새 주얼로','+1 suffix → next; +1 prefix → new jewel')},
  {'id':'v3','phase':'des','do':'desecrate','cur':'Preserved_Cranium','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'4:58'},
  {'id':'v4','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':vd_cc},{'gi':vd_asS},{'gi':vd_cdA}]},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'v3','via':LIGHT},'ts':'5:40'},
  {'id':'v5','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'removeGi':vd_plusS,'junk':'p'},'expect':2,'ts':'10:16',
   'br':K('1/2: 경멸 줄이 지워지면 다음, 아니면 다시','1 in 2: Contempt line gone → next; otherwise again')},
  {'id':'v6','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':VD_PRE},'fail':{'goto':'self'},'ts':'10:53'},
  {'id':'v7','phase':'pre','do':'essence','cur':'Ancient_Potent_Liquid_Melancholy','knownP':True,'target':{'gi':vd_mel,'chance':0.5,'missDrop':vd_pdmg},'fail':{'goto':'v6'},'ts':'12:34',
   'br':K('좋은 접두 유지 → 완성, 지워지면 카오스 오브부터','Good prefix kept → done; lost → chaos again')},
  {'id':'v8','phase':'pre','do':'note','optional':True,'label':K('신성한 오브로 수치 정리','Divine the rolls'),'ts':'14:19'},
 ]})
