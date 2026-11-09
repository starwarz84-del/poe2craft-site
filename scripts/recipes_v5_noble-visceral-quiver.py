# ---- 노블이-NoblE "[패스오브엑자일2] 1미러에 팔린 본능적인 화살통 제작 풀 영상" (youtu.be/2PUEwoePtRs) ----
# Old-patch video (published 2026-02-07, 0.4 era, no captions: read from burned-in subtitles and screen).
# Policy 15: keep the finished mod set, rewrite the steps for 0.5.5 data. The video's desecrated "+2 to Level of all
# Projectile Skills" no longer exists on quivers; the closest current mod is the normal "+1 to Level of all Projectile Skills".
NQ5=K('노블이-NoblE 영상 기반','Based on 노블이-NoblE')
c='Quivers'
def textQ(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return max(hits, key=lambda gi: cd(c)['groups'][gi]['t'][0][0])   # the ladder with the highest tier
nq_lt=textQ('Lightning damage to Attacks','n','p'); nq_pspd=textQ('increased Projectile Speed','n','p'); nq_bow=textQ('increased Damage with Bow Skills','n','p')
nq_cc=textQ('increased Critical Hit Chance for Attacks','n','s'); nq_cd=textQ('increased Critical Damage Bonus for Attack Damage','n','s')
nq_proj=textQ('to Level of all Projectile Skills','n','s')
NQ_SUF=[{'gi':nq_cc,'tmax':1},{'gi':nq_cd,'tmax':2},{'gi':nq_proj}]
NQ_PRE=[{'gi':nq_pspd,'tmax':1},{'gi':nq_bow,'tmax':1}]
NQ_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
NQ_SANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}
R.append({
 'id':'noble-visceral-quiver','cls':c,'base':base(c,'Visceral Quiver'),'ilvl':82,'difficulty':4,'budget':'high',
 'buildTags':[K('활','Bow'),K('번개','Lightning'),K('공격 치명타','Attack crit'),K('투사체','Projectile')],
 'patch':'0.5.5','adaptedFrom':'0.4','created':'2026-11-09','author':NQ5,
 'source':{'url':'https://www.youtube.com/watch?v=2PUEwoePtRs','title':'[패스오브엑자일2] 1미러에 팔린 본능적인 화살통 제작 풀 영상','channel':'노블이-NoblE'},
 'title':K('번개 피해 분열 + 공격 치명타 2종 · 투사체 스킬 +1','fractured lightning damage + attack crit chance and damage, +1 projectile skills'),
 'start':{'rar':'rare','mods':[{'gi':nq_lt,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'suf','kr':'접미: 치명타','en':'Suffixes: crit'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'훼손 공개','en':'Reveal'}],
 'nodes':[
  {'id':'q1','phase':'suf','do':'base','cost':'base','ts':'0:24',
   'note':K('번개 피해 추가 1티어 분열 + 잡옵 1줄.','Fractured T1 added lightning damage plus one junk line.')},
  {'id':'q2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':NQ_SUF},'fail':{'goto':'self'},'ts':'5:15'},
  {'id':'q3','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':NQ_SUF},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'q2'},'ts':'6:00',
   'br':K('실패: 소멸의 오브. 치명타 줄이 지워지면 카오스 오브부터','Miss: Annulment; if the crit line goes, chaos again')},
  {'id':'q4','phase':'suf','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'8:00'},
  {'id':'q5','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':NQ_PRE},'fail':{'goto':'self','via':NQ_SANN},'ts':'8:16'},
  {'id':'q6','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':NQ_PRE},'fail':{'goto':'self','via':NQ_SANN,'lost':'q5'},'ts':'10:39',
   'br':K('실패: 좌측 소멸의 징조 + 소멸의 오브. 앞 접두가 지워지면 그 단계부터','Miss: Sinistral Annulment; if the first prefix goes, redo that step')},
  {'id':'q7','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':NQ_SUF},'side':'s','bone':'Preserved_Jawbone'},'ts':'10:51',
   'br':K('대박 → 완성, 실패: 빛의 징조 + 소멸의 오브 → 다시 훼손','Hit → done; miss: Omen of Light + Annulment, desecrate again')},
  {'id':'qm1','phase':'fin','branch':{'of':'q7','when':'miss'},'do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True}},
  {'id':'qm2','phase':'fin','branch':{'of':'q7','when':'miss'},'do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'s'}},
  {'id':'qm3','phase':'fin','branch':{'of':'q7','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':NQ_SUF},'side':'s','bone':'Preserved_Jawbone'},'fail':{'goto':'qm2','via':NQ_LIGHT}},
 ]})
