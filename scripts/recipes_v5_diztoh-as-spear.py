# ---- Diztoh "How to Craft an Attack Speed Spear for Twister | PoE 2 0.5.5" (youtu.be/cTjgn7NnHR8) ----
DZS=K('Diztoh 영상 기반','Based on Diztoh')
c='Spears'
def textP(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sp_proj=textP('to Level of all Projectile Skills','n','s'); sp_as=textP('increased Attack Speed','n','s')
sp_aug=textP('increased effect of Socketed Augment Items','e','s'); sp_cel=textP('to Accuracy Rating\n','e','p')
sp_spd=textP('increased Explicit Speed Modifier magnitudes','x','p')
sp_pphys=textP('% increased Physical Damage','n','p'); sp_hyb=textP('increased Physical Damage\n+','n','p'); sp_fphys=textP('Physical Damage','n','p')
SP_PRE=[{'gi':sp_pphys,'tmax':2},{'gi':sp_hyb,'tmax':2},{'gi':sp_fphys,'tmax':2}]
SP_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'diztoh-as-spear','cls':c,'base':base(c,'Akoyan Spear'),'ilvl':82,'difficulty':3,'budget':'medium','unknownW':True,
 'buildTags':[K('돌개바람','Twister'),K('공격 속도','Attack speed'),K('투사체','Projectile')],'patch':'0.5.5','created':'2026-11-09','author':DZS,
 'source':{'url':'https://www.youtube.com/watch?v=cTjgn7NnHR8','title':'How to Craft an Attack Speed Spear for Twister | PoE 2 0.5.5','channel':'Diztoh'},
 'title':K('투사체 +4 분열 + 공격 속도 · 장착 효과 + 스루드의 완력 속도 규모','fractured +4 projectile + attack speed, augment effect, Thrud\'s speed magnitudes'),
 'start':{'rar':'rare','runes':[K('아스트리드의 창의성',"Astrid's Creativity")],'mods':[{'gi':sp_proj,'tmax':1,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'alloy','kr':'합금 2개','en':'Two alloys'},{'id':'pre','kr':'스루드의 완력 · 접두','en':'Thrud\'s Might and prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'a1','phase':'suf','do':'base','cost':'base','ts':'0:20','note':K('투사체 +4 분열 + 잡옵 1개, 아스트리드의 창의성 장착.','Fractured +4 projectile plus one junk line, Astrid\'s Creativity socketed.')},
  {'id':'a2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':sp_as,'tmax':3},'fail':{'goto':'self'},'ts':'0:40'},
  {'id':'a3','phase':'alloy','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'1:36'},
  {'id':'a4','phase':'alloy','do':'essence','cur':'Sovereign_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sp_aug},'ts':'1:54'},
  {'id':'a5','phase':'alloy','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'2:35'},
  {'id':'a6','phase':'alloy','do':'essence','cur':'Celestial_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sp_cel},'ts':'2:40'},
  {'id':'a7','phase':'pre','do':'note','target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('스루드의 완력',"Thrud's Might")]},'ts':'3:08'},
  {'id':'a8','phase':'pre','do':'desecrate','cur':'Ancient_Jawbone','target':{'unrev':'p'},'ts':'3:28'},
  {'id':'a9','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':sp_spd},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'a8','via':SP_LIGHT},'ts':'4:04'},
  {'id':'a10','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':SP_PRE},'ts':'4:20',
   'br':K('대박 → 완성, 실패: 영상처럼 그대로 완성 / 절사의 징조 + 카오스 오브','Hit → done; miss: keep it (video) or Whittling + Chaos')},
  {'id':'a11','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'fallbackFor':'a10','optional':True,'target':{'anyOf':SP_PRE,'replace':'p'},'fail':{'goto':'self'},'ts':'5:47',
   'br':K('새 옵션이 레벨 65 이상인데 목표가 아니면 다시 쓰지 않음. 합금·훼손 옵션이 지워지기 때문','A new non-target line of level 65+ ends it (the alloy or desecrated line would go next)')},
  {'id':'a12','phase':'fin','do':'note','optional':True,'ts':'6:34','label':K('타락으로 소켓 추가 (선택)','Corrupt for a socket (optional)'),
   'note':K('퀄리티 20% · 신성한 오브 후 바알 오브로 두 번째 소켓 노림(망가질 수 있음).','20% quality and Divine, then a Vaal Orb for a second socket (can brick).')},
 ]})
