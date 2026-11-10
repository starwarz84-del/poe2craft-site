# ---- 시한 "[POE2 0.5.5] 하이엔드 투사체 장갑 제작 방법｜범용 적용 가능｜실전 제작 포함" (youtu.be/DH4jiORLg10) ----
c='Gloves_str'
SHP=K('시한 영상 기반','Based on 시한')
def textPP(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sp_lvl=textPP('+2 to Level of all Projectile Skills','x','s'); sp_add=textPP('chance to fire an additional Projectile','x','s')
sp_pdmg=textPP('increased Projectile Damage','x','p'); sp_pspd=textPP('increased Projectile Speed','x','p')
sp_phys=textPP('to (22—32) Physical Damage to Attacks','n','p'); sp_cdb=textPP('increased Critical Damage Bonus','e','s')
SP_PRE=[{'gi':sp_phys,'tmax':1},{'gi':sp_pdmg,'tmax':1},{'gi':sp_pspd,'tmax':1}]
KOLR2=K('콜르의 사냥',"Kolr's Hunt")
R.append({
 'id':'sihan-proj-gloves','cls':c,'base':base(c,'Massive Mitts'),'ilvl':80,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high',
 'buildTags':[K('투사체','Projectile'),K('공격','Attack'),K('방어도','Armour')],'patch':'0.5.5','created':'2026-11-11','author':SHP,
 'source':{'url':'https://www.youtube.com/watch?v=DH4jiORLg10','title':'[POE2 0.5.5] 하이엔드 투사체 장갑 제작 방법｜범용 적용 가능｜실전 제작 포함','channel':'시한'},
 'title':K('콜르의 사냥 · 투사체 +2 분열 + 추가 발사 + 발작의 에센스 + 접두 3개','Kolr\'s Hunt: fractured +2 projectiles + extra projectile + Hysteria + three prefixes'),
 'start':{'rar':'rare','runes':[KOLR2],'mods':[{'gi':sp_lvl,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 완성','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'훼손 마무리','en':'Desecration finish'}],
 'nodes':[
  {'id':'p1','phase':'base','do':'base','cost':'base','ts':'1:36','note':K('거대한 미트(룬 소켓 2개), 콜르의 사냥 장착 상태로 모든 투사체 스킬 레벨 +2 분열 + 잡옵 1개.','Massive Mitts (two sockets) with Kolr\'s Hunt socketed: fractured +2 to all projectile skills plus one junk line.')},
  {'id':'p2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':sp_add,'tmax':2},'fail':{'goto':'self'},'ts':'4:52'},
  {'id':'p3','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'5:05'},
  {'id':'p4','phase':'suf','do':'essence','cur':'Essence_of_Hysteria','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sp_cdb,'chance':1},'ts':'5:25'},
  {'id':'p5','phase':'pre','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'16:09'},
  {'id':'p6','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':SP_PRE},'expect':20,
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'p2'},'ts':'7:16',
   'br':K('실패: 접두가 하나뿐이면 소멸의 오브, 접미가 지워지면 카오스 오브부터','Miss: with one prefix use a plain Annulment; if a suffix goes, back to the Chaos step')},
  {'id':'p7','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':SP_PRE},'expect':20,
   'fail':{'goto':'self','via':{'cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'also':[{'cur':'Preserved_Rib'},LIGHT]},'lost':'p6'},'ts':'7:56',
   'br':K('실패: 좌측 결정화의 징조 + 심연의 에센스 → 보존된 갈비뼈 → 빛의 징조 + 소멸의 오브로 그 옵션만 지우기','Miss: Sinistral Crystallisation + Essence of the Abyss → Preserved Rib → Light + Annulment removes just that line')},
  {'id':'p8','phase':'fin','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'},'ts':'23:30'},
  {'id':'p9','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SP_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'p8','via':LIGHT},'ts':'25:30'},
  {'id':'p10','phase':'fin','do':'note','ts':'26:30','note':K('완성. 자금이 모자라면 접두 2티어로 마무리하고 나중에 다시 쌓아도 됨.','Done; short on currency, settle for tier 2 prefixes and rebuild later.')},
 ]})
