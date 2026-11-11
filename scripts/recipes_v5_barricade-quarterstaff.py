# ---- Barricade "How to Craft an Endgame Sinister Quarterstaff | PoE 2" (youtu.be/B4yShuKydt0) ----
BRC=K('Barricade 영상 기반','Based on Barricade')
c='Quarterstaves'
def textQ(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return max(hits, key=lambda gi: cd(c)['groups'][gi]['t'][0][0])   # the ladder with the highest tier
bq_crit=textQ('to Critical Hit Chance','n','s'); bq_melee=textQ('to Level of all Melee Skills','n','s')
bq_aspd=textQ('increased Attack Speed','n','s'); bq_cdmg=textQ('to Critical Damage Bonus','n','s')
bq_ele=textQ('increased Elemental Damage with Attacks','n','p'); bq_fire=textQ('Fire Damage','n','p'); bq_cold=textQ('Cold Damage','n','p'); bq_light=textQ('Lightning Damage','n','p')
BQ_PRE=[{'gi':gi,'tmax':1} for gi in (bq_ele,bq_fire,bq_cold,bq_light)]
BQ_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
BQ_WH=['Omen_of_Whittling']
R.append({
 'id':'barricade-quarterstaff','cls':c,'base':base(c,'Sinister Quarterstaff'),'ilvl':81,'sockets':3,'exceptional':{'sockets':1},'difficulty':5,'budget':'high',
 'buildTags':[K('원소','Elemental'),K('치명타','Critical'),K('근접','Melee')],'patch':'0.5.5','created':'2026-11-09','author':BRC,
 'source':{'url':'https://www.youtube.com/watch?v=B4yShuKydt0','title':'How to Craft an Endgame Sinister Quarterstaff | PoE 2','channel':'Barricade'},
 'title':K('치명타 확률 분열 + 근접 스킬 +5 + 원소 접두 1티어 옵션 3개','fractured crit chance + melee skills +5 + three T1 elemental prefixes'),
 'start':{'rar':'rare','quality':30,'mods':[{'gi':bq_crit,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'q1','phase':'suf','do':'base','cost':'base','ts':'10:20','note':K('퀄리티 30%. 치명타 확률 5% 분열 + 잡옵 1개.','30% quality. Fractured 5% critical hit chance plus one junk line.')},
  {'id':'q2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':bq_melee,'tmax':1},'fail':{'goto':'self'},'ts':'10:30'},
  {'id':'q3','phase':'suf','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'10:50'},
  {'id':'q4','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':bq_aspd,'tmax':1},{'gi':bq_cdmg,'tmax':1}]},'side':'s','bone':'Preserved_Jawbone'},'fail':{'goto':'q3','via':BQ_LIGHT},'ts':'12:20'},
  {'id':'p1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':'p','count':2},'ts':'14:20'},
  {'id':'p2','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':BQ_WH,'target':{'anyOf':BQ_PRE,'replace':'p'},'fail':{'goto':'self'},'ts':'15:00'},
  {'id':'p3','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':BQ_WH,'target':{'anyOf':BQ_PRE[1:],'replace':'p'},'fail':{'goto':'self'},'ts':'16:20'},
  {'id':'p4','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':BQ_PRE[2:]},'fail':{'goto':'p5'},'ts':'17:05',
   'br':K('1티어 → 완성, 실패 → 다음 단계','T1 → done; miss → next step')},
  {'id':'p5','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':BQ_WH,'target':{'anyOf':BQ_PRE[2:],'replace':'p'},'fallbackFor':'p4','fail':{'goto':'self'},'ts':'17:20',
   'br':K('물리 피해 + 정확도 1티어처럼 버릴 옵션이 레벨 77 이상이면 → 다음 갈림길','Junk at level 77+ (e.g. T1 physical + accuracy) → next fork')},
  {'id':'p6','phase':'pre','do':'note','fallbackFor':'p5','label':K('갈림길: 좌측 소멸의 징조 + 소멸의 오브','Fork: Sinistral Annulment + Annulment'),'ts':'18:00',
   'note':K('접두 옵션 3개 중 하나 제거(1/3로 버릴 옵션). 좋은 옵션이 지워지면 완벽한 엑잘티드 오브부터 다시.','Removes one of the three prefixes (1 in 3 it is the junk). If a good line goes, Perfect Exalt again.')},
  {'id':'f1','phase':'fin','do':'note','optional':True,'ts':'23:40','note':K('선택: 히네코라의 머리카락 + 바알 오브로 소켓 4개.',"Optional: Hinekora's Lock + Vaal Orb for a fourth socket.")},
 ]})
