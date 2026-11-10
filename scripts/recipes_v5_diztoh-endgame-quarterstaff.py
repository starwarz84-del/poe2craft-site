# ---- Diztoh "How to Craft an INSANE Endgame Quarterstaff | PoE 2 0.5" (youtu.be/YfGJyBrObxI) ----
DZQ=K('Diztoh 영상 기반','Based on Diztoh')
c='Quarterstaves'
def textDQ(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
dq_melee=textDQ('+5 to Level of all Melee Skills','n','s')
dq_flat=textDQ('Adds (37—55) to (63—94) Physical Damage','n','p'); dq_ppct=textDQ('(170—179)% increased Physical Damage','n','p')
dq_hyb=textDQ('increased Physical Damage\n+','n','p'); dq_fire=textDQ('Adds (135—156) to (205—236) Fire Damage','n','p')
dq_as=textDQ('increased Attack Speed','n','s'); dq_crit=textDQ('to Critical Hit Chance','n','s'); dq_cdmg=textDQ('to Critical Damage Bonus','n','s')
DQ_PCT=[{'gi':dq_ppct,'tmax':2},{'gi':dq_hyb,'tmax':2}]
DQ_LAST=[{'gi':dq_hyb,'tmax':2},{'gi':dq_fire,'tmax':4}]
DQ_SUF=[{'gi':dq_as,'tmax':4},{'gi':dq_crit,'tmax':2},{'gi':dq_cdmg,'tmax':2}]
DQ_CRIT=[{'gi':dq_crit,'tmax':2},{'gi':dq_cdmg,'tmax':2}]
DQ_IRON=K('완벽한 철 룬','Perfect Iron Rune')
DQ_DANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}
R.append({
 'id':'diztoh-endgame-quarterstaff','cls':c,'base':base(c,'Sinister Quarterstaff'),'ilvl':82,'sockets':2,'difficulty':4,'budget':'high',
 'buildTags':[K('물리','Physical'),K('근접','Melee'),K('치명타','Critical')],'patch':'0.5','created':'2026-11-09','author':DZQ,
 'source':{'url':'https://www.youtube.com/watch?v=YfGJyBrObxI','title':'How to Craft an INSANE Endgame Quarterstaff | PoE 2 0.5','channel':'Diztoh'},
 'title':K('근접 스킬 +5 분열 + 물리 접두 + 공격 속도 · 치명타 피해','fractured +5 melee skills + physical prefixes + attack speed and crit damage'),
 'start':{'rar':'rare','quality':20,'mods':[{'gi':dq_melee,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'s1','phase':'pre','do':'base','cost':'base','ts':'1:44','note':K('퀄리티 20%. 근접 스킬 +5 분열 + 잡옵 1개.','20% quality. Fractured +5 melee skills plus one junk line.')},
  {'id':'s2','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','target':{'anyOf':[{'gi':dq_flat,'tmax':3},{'gi':dq_ppct,'tmax':2},{'gi':dq_hyb,'tmax':2}]},'fail':{'goto':'self'},'ts':'3:19'},
  {'id':'s3','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':DQ_PCT},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']},'lost':'s2'},'ts':'6:00'},
  {'id':'s4','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':DQ_LAST},'ts':'8:13',
   'br':K('실패: 절사의 징조 + 좌측 말소의 징조 + 완벽한 카오스 오브','Miss: Whittling + Sinistral Erasure + Perfect Chaos')},
  {'id':'s4b','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Sinistral_Erasure'],'target':{'anyOf':DQ_LAST,'replace':'p'},'fallbackFor':'s4','fail':{'goto':'self'},'ts':'8:50',
   'br':K('버릴 옵션이 물리 피해 추가 3티어(레벨 60)보다 낮을 때만','Only while the junk line is below the tier 3 flat physical (level 60)')},
  {'id':'s5','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':DQ_SUF},'ts':'9:56',
   'br':K('실패: 우측 말소의 징조 + 카오스 오브로 그 옵션을 계속 바꿈','Miss: keep rerolling that line with Dextral Erasure + Chaos')},
  {'id':'s5b','phase':'suf','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Dextral_Erasure'],'target':{'anyOf':DQ_SUF,'replace':'s'},'fallbackFor':'s5','fail':{'goto':'self'},'ts':'9:56'},
  {'id':'s6','phase':'suf','do':'desecrate','cur':'Ancient_Jawbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'11:10'},
  {'id':'s7','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':DQ_CRIT},'side':'s','bone':'Ancient_Jawbone'},
   'fail':{'goto':'s6','via':DQ_DANN,'lost':'s5'},'ts':'12:20',
   'br':K('실패: 우측 소멸의 징조 + 소멸의 오브(빛의 징조보다 쌈, 1/2로 공격 속도가 지워짐)','Miss: Dextral Annulment + Annulment (cheaper than Omen of Light; 1 in 2 it takes attack speed)')},
  {'id':'s8','phase':'fin','do':'manual','target':{'rune':DQ_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'13:50'},
  {'id':'s9','phase':'fin','do':'manual','target':{'rune':DQ_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'14:25'},
  {'id':'s10','phase':'fin','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':dq_ppct}},'fail':{'goto':'self'},'ts':'14:04'},
  {'id':'s11','phase':'fin','do':'note','optional':True,'ts':'16:50','note':K('선택: 바알 대장장이의 주입기로 퀄리티 20% 초과(타락 위험).',"Optional: a Vaal Blacksmith's Infuser for quality above 20% (can corrupt).")},
 ]})
