# Builds site/data/recipes.json (format v2: a recipe is a flow of nodes; each node can loop on itself or jump back on failure).
# Group indices are looked up by modifier text so the file survives data refreshes.
import json, os
D='/home/claude/poe2data/site/data/'
cache={}
def cd(cls):
    if cls not in cache: cache[cls]=json.load(open(f'{D}c/{cls}.json'))
    return cache[cls]
def g(cls, text, sec='n', side=None):
    for gi,gr in enumerate(cd(cls)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and text.lower() in gr['t'][0][5].lower(): return gi
    raise Exception((cls,text))
def base(cls,name): return [b['en'] for b in cd(cls)['bases']].index(name)
R=[]

# ---- Mirror bow: the user's step list, built on 반지깎는노인's video "미러 활 제작법" (youtu.be/J0LF3MRssh0) ----
c='Bows'
def fam(f, sec='n'):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and gr['f']==[f]: return gi
    raise Exception(f)
flat=fam('PhysicalDamage'); pphys=fam('LocalPhysicalDamagePercent'); hybrid=fam('LocalIncreasedPhysicalDamagePercentAndAccuracyRating')
acc=fam('IncreasedAccuracy'); mark_p=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and gr['g']=='p' and 'Abyssal Lord' in gr['t'][0][5]][0]; mark_s=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and gr['g']=='s' and 'Abyssal Lord' in gr['t'][0][5]][0]; crit=fam('CriticalStrikeChanceIncrease'); cdmg=fam('CriticalStrikeMultiplier')
proj=fam('IncreaseSocketedGemLevel'); arrow=fam('AdditionalArrows'); eleatk=fam('IncreasedWeaponElementalDamagePercent')
V='https://www.youtube.com/watch?v=J0LF3MRssh0'
def K(kr,en): return {'kr':kr,'en':en}
LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'mirror-bow-video', 'cls':c, 'base':base(c,'Warmonger Bow'), 'ilvl':82, 'quality':30, 'sockets':3, 'exceptional':{'sockets':1}, 'difficulty':4, 'budget':'high', 'buildTags':[K('치명타','Crit'),K('물리','Physical'),K('활 공격','Bow attacks')], 'patch':'0.5', 'created':'2026-11-08',
 'author':K('반지깎는노인 영상 기반','Based on 반지깎는노인'),
 'source':{'url':V, 'title':'미러 활 제작법 [POE2] Mirror crafting "Bow"', 'channel':'반지깎는노인'},
 'title':K('치확 분열 + 물피증 1티어','fractured crit + T1 % phys'),
 'phases':[
   {'id':'base','kr':'베이스 작업','en':'Base'},
   {'id':'magic','kr':'매직 단계','en':'Magic stage'},
   {'id':'rare','kr':'레어 전환','en':'Into rare'},
   {'id':'fracture','kr':'분열','en':'Fracture'},
   {'id':'build','kr':'본 작업 — 치확 분열 상태','en':'Main craft — crit fractured'},
   {'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'s1','phase':'base','do':'base','cost':'base',
   'note':K('전쟁광 활, 특출난 베이스(소켓 3개), 아이템 레벨 82.','Warmonger Bow, exceptional base (3 sockets), item level 82.')},
  {'id':'s2','phase':'base','do':'manual','cost':'quality','target':{'setQuality':30},'label':K('퀄리티 30% 작업','Quality to 30%'),'ts':'5:54',
   'note':K('20% 이후 바알 대장장이의 주입기. 운 요소가 커서 비용은 직접 입력.','Vaal infusers after 20%. Mostly luck, so enter the cost yourself.')},
  {'id':'m1','phase':'magic','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':[{'gi':pphys,'tmax':1},{'gi':crit,'tmax':1}]},'ts':'8:26',
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},
   'note':K('물피증 1티어 또는 치확 1티어 중 먼저 나오는 것.','T1 % phys or T1 crit, whichever comes first.')},
  {'id':'m2','phase':'magic','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':[{'gi':pphys,'tmax':1},{'gi':crit,'tmax':1}]},'ts':'9:31',
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}},
   'note':K('나머지 하나. 실패한 옵션은 우측(접미) 또는 좌측(접두) 소멸의 징조로 지움.','The other one. Remove a miss with Dextral (suffix) or Sinistral (prefix) Annulment.')},
  {'id':'r1','phase':'rare','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'s'},'ts':'10:04'},
  {'id':'r2','phase':'rare','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'reroll':'junk'},'ts':'10:09','optional':True,
   'note':K('추가 유효 옵션 노리기. 영상에선 잡옵이 떠서 그대로 진행.','Fish for another useful mod. The video kept a junk mod.')},
  {'id':'r3','phase':'rare','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':crit}},'fail':{'goto':'self'},'ts':'10:39',
   'note':K('치확 5.00% 만들기.','Roll crit to exactly 5.00%.')},
  {'id':'f1','phase':'fracture','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'11:49',
   'note':K('접두에 훼손 추가(공개 안 함). 아이템 레벨 82라 갉힌 턱뼈 대신 보존된 턱뼈.','Desecrate a prefix (left unrevealed); Preserved Jawbone, since this is item level 82.')},
  {'id':'f2','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':crit}]},'alsoUseful':[{'gi':pphys}],'ts':'12:04',
   'fail':{'goto':'restart'}, 'after':{'keepOnly':[pphys,crit,'unrev']},
   'note':K('훼손 옵션은 분열되지 않아 3개 중 1개: 1/3 치확(이 레시피), 1/3 물피증(다른 레시피에서 사용), 1/3 실패. 기회비용은 2/3로 계산. 분열 뒤 잡옵은 절사의 징조로 정리, 8번의 접두 훼손은 그대로 남아 바로 공개로 넘어감.','Desecrated mods cannot fracture, so 1 of 3: crit (this recipe), % phys (another recipe) or a miss. Restart cost uses 2/3.')},
  {'id':'b4','phase':'build','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':eleatk,'tmax':1},{'gi':acc,'tmax':1}]},'side':'p','bone':'Preserved_Jawbone','retryBone':'Ancient_Jawbone'},'ts':'21:59',
   'fail':{'goto':'b2','via':LIGHT},
   'note':K('시작 상태의 미공개 접두 훼손을 심연의 메아리의 징조로 두 번 보고 공원피 1티어 또는 정확도 1티어. 없으면 빛의 징조 + 소멸의 오브로 지우고 아래 재시도 구간(접미 추가 → 심연의 에센스 → 고대 턱뼈)을 거쳐 다시 공개.','Reveal the unrevealed prefix from the start, with Abyssal Echoes for a second look: T1 Attack Elemental or T1 Accuracy. Otherwise remove it with Light + Annulment and run the retry block below (suffix → Essence of the Abyss → Ancient Jawbone), then reveal again.')},
  {'id':'b2','phase':'build','retryFor':'b4','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},
   'note':K('접미 한 자리 추가 (다음 단계에서 심연의 에센스가 지울 자리).','Adds one suffix (the slot the Essence of the Abyss removes next).')},
  {'id':'x1','phase':'build','retryFor':'b4','do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Dextral_Crystallisation'],'target':{'mark':{'gi':mark_p,'alt':mark_s},'chance':0.5},'fail':{'goto':'x2'},
   'note':K('우측 결정화의 징조로 접미 하나를 지우고 심연 군주의 징표를 붙임. 접두·접미 중 어디에 붙을지는 반반으로 계산.','Dextral Crystallisation removes a suffix and the essence adds the Mark of the Abyssal Lord; prefix or suffix counted as 50/50.')},
  {'id':'x2','phase':'build','retryFor':'b4','do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Dextral_Crystallisation'],'withEach':{'cur':'Preserved_Jawbone'},'target':{'mark':{'gi':mark_p,'alt':mark_s},'chance':0.5},'fallbackFor':'x1','fail':{'goto':'self'},
   'note':K('징표가 접미에 붙으면 싼 뼈로 훼손을 붙인 뒤 다시 우측 결정화의 징조 + 심연의 에센스. 싼 뼈 = 보존된 턱뼈.','If the Mark lands on a suffix, desecrate with a cheap bone (Preserved Jawbone), then Dextral Crystallisation + Essence of the Abyss again.')},
  {'id':'x3','phase':'build','retryFor':'b4','do':'desecrate','cur':'Ancient_Jawbone','target':{'unrev':'p','fromMark':True},'fail':{'goto':'b4','label':'reveal'},
   'note':K('고대 턱뼈로 접두 자리(징표)에 훼손 옵션 추가.','Ancient Jawbone turns the prefix Mark into a desecrated modifier.')},
  {'id':'b5','phase':'build','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':hybrid,'tmax':1},{'gi':flat,'tmax':1}]},'fail':{'goto':'b6'},
   'note':K('접두에 하이브리드 1티어(물피증 + 정확도, 베스트) 또는 물피추 1티어.','Prefix: T1 hybrid % phys + accuracy (best) or T1 flat phys.')},
  {'id':'b6','phase':'build','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':[{'gi':hybrid,'tmax':1},{'gi':flat,'tmax':1}]},'fallbackFor':'b5','fail':{'goto':'self'},
   'note':K('바로 안 나오면 절사의 징조로 접두의 하이브리드·물피추 1티어를 찾음.','If it misses, use Whittling to fish the prefix.')},
  {'id':'b6x','phase':'build','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},
   'note':K('접두가 꽉 차 있어 완벽한 엑잘티드 오브는 접미에 붙음. 다음 단계에서 우측 말소의 징조 + 카오스 오브로 굴릴 접미 자리.','Prefixes are full, so the Perfect Exalt lands on a suffix: the slot the Dextral Erasure Chaos rerolls next.')},
  {'id':'b7','phase':'build','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Dextral_Erasure'],'target':{'anyOf':[{'gi':proj,'tmax':1},{'gi':arrow,'tmax':1}],'replace':'s'},'fail':{'goto':'self'},'ts':'24:35',
   'note':K('카오스 오브 + 우측 말소의 징조로 그 접미 자리를 굴려 투사체 +4 또는 화살 초과 확률 1티어.','Dextral Erasure or Whittling for +4 projectile levels or T1 additional arrow.')},
  {'id':'b8','phase':'build','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},
   'note':K('남은 한 자리에 엑잘티드 오브로 6자리 채움.','Fill the last slot (6 modifiers).')},
  {'id':'b9','phase':'build','do':'socket','cur':"rune:Serle's Triumph",'target':{'slots':{'s':1}},'ts':'27:39',
   'note':K('룬 세를의 승리를 소켓에 끼워 접미 한 자리 추가.',"Socket the rune Serle's Triumph to add a suffix slot.")},
  {'id':'b10','phase':'build','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'all':[{'anyOf':[{'gi':proj,'tmax':1},{'gi':arrow,'tmax':1}]},{'gi':cdmg,'tmax':1}],'replace':'s'},'fail':{'goto':'self'},'ts':'28:21',
   'note':K('절사의 징조 + 상위 카오스 오브로 남은 투사체 +4 / 화살 1티어와 치명타 피해 보너스 1티어를 모두 찾음.','Whittling + Greater Chaos until both the remaining projectile/arrow mod and T1 crit damage land.')},
  {'id':'e1','phase':'finish','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},
   'note':K('빛의 징조 + 소멸의 오브로 훼손 옵션(공원피·정확도 자리)을 지움. 항상 성공.','Light + Annulment removes the desecrated modifier (the placeholder). Always works.')},
  {'id':'e2','phase':'finish','do':'reveal','cur':'Ancient_Jawbone','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':flat,'tmax':1},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'e1'},'ts':'31:27',
   'note':K('고대 턱뼈 + 심연의 메아리의 징조로 물리 피해 추가 1티어. 강령술의 징조는 필요 없음(접미가 꽉 참). 실패하면 {#e1}번(제거)으로 돌아감.','Ancient Jawbone + Abyssal Echoes for T1 flat phys. No Necromancy omen needed (suffixes are full). On a miss go back to step {#e1} (removal).')},
  {'id':'e3','phase':'finish','do':'note','note':K('미러 활 완성. 남은 룬 2자리는 취향껏.','Mirror bow done. Fill the other 2 sockets to taste.')},
 ],
})

# ---- Absent Amulet, from SL 게임연구소's video "부재 목걸이 '심연의 에센스' 사용하여 저렴하게 띄우기" (youtu.be/jr6-YLMJsC8) ----
c='Amulets'
def famA(f, sec='n'):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and gr['f']==[f]: return gi
    raise Exception(f)
def textA(t, sec, side=None):
    for gi,gr in enumerate(cd(c)['groups']):
        if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]: return gi
    raise Exception(t)
spirit=textA('to Spirit','n','p'); spell=textA('Level of all Spell Skills','n','s')
esFlat=textA('to maximum Energy Shield','n','p'); esPct=textA('increased maximum Energy Shield','n','p')
maxQ=textA('to Maximum Quality','e','p'); globalDef=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Perfect Essence of Enhancement' in [x[3] for x in gr['t']]][0]
allQ=textA('Quality of all Skills','d','s')
markA_p=textA('Abyssal Lord','e','p'); markA_s=textA('Abyssal Lord','e','s')
V2='https://www.youtube.com/watch?v=jr6-YLMJsC8'
LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
MISS={'of':'a10','when':'miss'}; OK={'of':'a10','when':'ok'}
R.append({
 'id':'absent-amulet-video', 'cls':c, 'base':base(c,'Absent Amulet'), 'ilvl':82, 'difficulty':2, 'budget':'medium', 'buildTags':[K('주문','Spell'),K('에너지 보호막','Energy Shield'),K('정신력','Spirit')], 'patch':'0.5.5', 'created':'2026-11-08',
 'author':K('SL 게임연구소 영상 기반','Based on SL 게임연구소'),
 'source':{'url':V2, 'title':"[POE2 0.5.5] #5 부재 목걸이 '심연의 에센스' 사용하여 저렴하게 띄우기!", 'channel':'SL 게임연구소!'},
 'title':K('정신력 분열 + 주문 +3 + 모든 스킬 퀄리티','fractured Spirit + spell +3 + all skill quality'),
 'start':{'rar':'rare','mods':[{'gi':spirit,'tmax':1}]},
 'phases':[
   {'id':'base','kr':'베이스','en':'Base'},
   {'id':'fracture','kr':'분열','en':'Fracture'},
   {'id':'suffix','kr':'주문 스킬 레벨 +3','en':'Spell skill level +3'},
   {'id':'quality','kr':'퀄리티 작업','en':'Quality'},
   {'id':'des','kr':'모든 스킬 퀄리티 (훼손)','en':'All skill quality (desecrated)'},
   {'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'a1','phase':'base','do':'base','cost':'base','ts':'1:53',
   'note':K('정신력 +50(1티어)이 붙은 부재 목걸이를 거래소에서 구매. 아이템 레벨 75 이상(계산은 82 기준), 원하는 부여 스킬 확인.','Buy an Absent Amulet with +50 Spirit (T1). Item level 75+ (82 assumed), check the granted skill.')},
  {'id':'a2','phase':'fracture','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation','Omen_of_Greater_Exaltation'],'target':{'junk':'s','count':2},'ts':'11:35',
   'note':K('분열 전에 접미 2자리 채우기. 여기서 주문 +3이 뜨면 이득.','Fill both suffixes before fracturing; a spell +3 here is a bonus.')},
  {'id':'a3','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'12:01',
   'note':K('남은 접두 자리에 훼손(공개 안 함)으로 4자리 채움.','Desecrate the last prefix (unrevealed) to reach 4 modifiers.')},
  {'id':'a4','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':spirit}]},'fail':{'goto':'restart'},'ts':'12:07',
   'after':{'keepOnly':[spirit,'junk1']},
   'note':K('훼손은 분열되지 않아 3개 중 1개(1/3)로 정신력. 이후 훼손 자리는 정리하고 카오스 오브로 1자리를 굴림.','Desecrated slots cannot fracture: 1 in 3 for Spirit. Afterwards the desecrated slot is cleared and Chaos spins one slot.')},
  {'id':'a5','phase':'suffix','do':'chaos','cur':'Chaos_Orb','target':{'gi':spell,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'12:32',
   'after':{'keepOnly':[spirit,spell]},
   'note':K('영상 기준 약 1,700개(실제 약 2,000개).','About 1,700 in the video (≈2,000 actually used).')},
  {'id':'a6','phase':'quality','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'14:27',
   'note':K('접두에 아무 옵션 하나. 어차피 지울 자리라 일반 엑잘티드 오브.','Any prefix; it gets replaced, so a regular Exalted Orb.')},
  {'id':'a7','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':maxQ},'ts':'14:34',
   'note':K('균열의 에센스로 그 접두를 지우고 최대 퀄리티 +20%. 부재 목걸이는 접두 2자리가 꽉 차 있어서 결정화의 징조 없이도 접두(잡옵)가 지워짐.','Essence of the Breach replaces that prefix with +20% Maximum Quality; the two prefixes are full, so no omen is needed.')},
  {'id':'a8','phase':'quality','do':'quality','cur':'Sibilant_Catalyst','target':{'quality':40},'ts':'14:43',
   'note':K('쇳소리 기폭제로 최소 34%, 영상은 40%까지.','Sibilant Catalysts to at least 34% (40% in the video).')},
  {'id':'a9','phase':'des','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_the_Blackblooded'],'target':{'unrev':'s'},'ts':'15:00',
   'note':K('검은 피의 징조로 쿠르갈 옵션 확정.','Omen of the Blackblooded guarantees a Kurgal option.')},
  {'id':'a10','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':allQ},'side':'s','lord':'kurgal','bone':'Preserved_Collarbone'},'fail':{'goto':'a13'},'ts':'15:06',
   'note':K('모든 스킬 퀄리티는 열 번에 한 번 수준. 안 떠도 빛의 징조는 바로 쓰지 않음.','All skill quality is roughly 1 in 10. If it misses, do not use Omen of Light yet.')},
  {'id':'a11','phase':'des','branch':OK,'do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':[{'gi':esFlat,'tmax':1},{'gi':esPct,'tmax':1}],'removeGi':maxQ},'ts':'4:11',
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티(레벨이 가장 낮음)를 날리고 접두 굴림. 좋은 옵션이면 끝. 안 뜨면 갈림길(절사의 징조를 다시 쓰면 엉뚱한 옵션보다 레벨 낮은 모든 스킬의 퀄리티가 지워질 수 있음).','Whittling + Perfect Chaos removes Maximum Quality (the lowest level) and rolls a prefix; a good one ends the craft. On a miss, choose a fork (Whittling again could take the skill quality line).')},
  {'id':'a12','phase':'des','branch':OK,'do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':[{'gi':esFlat,'tmax':1},{'gi':esPct,'tmax':1}],'replace':'p'},'fallbackFor':'a11','fail':{'goto':'self'},
   'label':K('갈림길 ①: 계속 돌리기','Fork (1): keep rolling'),
   'note':K('좌측 말소의 징조 + 상위 카오스 오브로 접두를 계속 돌려 에너지 보호막 1티어 찾기. 좌측 말소의 징조는 접두만 바꾸고, 접두엔 엉뚱한 옵션과 분열 옵션뿐이라 좋은 옵션이 안 지워짐.','Sinistral Erasure + Greater Chaos keeps rerolling the prefix for T1 Energy Shield; Erasure only touches prefixes, and the only removable prefix is the wrong one.')},
  {'id':'a12b','phase':'des','branch':OK,'do':'note','fallbackFor':'a11','label':K('갈림길 ②: 타협','Fork (2): settle'),
   'note':K('좌측 결정화의 징조 + 완벽한 강화의 에센스로 엉뚱한 접두를 바꿔 가성비 마무리.','Sinistral Crystallisation + Perfect Essence of Enhancement swaps the wrong prefix for a cheap finish.')},
  {'id':'a13','phase':'des','branch':MISS,'do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'removeGi':maxQ,'junk':'p'},'ts':'15:20',
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티(레벨이 가장 낮음)를 날림. 심연의 에센스도 제작 옵션이라 최대 퀄리티가 남아 있으면 못 씀. 에너지 보호막 1티어가 뜨면 이득 — 그 경우 심연의 에센스 단계는 건너뛰고 바로 훼손.','Whittling + Perfect Chaos removes Maximum Quality (the lowest level): Essence of the Abyss is crafted too and cannot go on while it is there. A T1 Energy Shield here is a bonus (then skip the Essence of the Abyss step and desecrate right away).')},
  {'id':'a14','phase':'des','branch':MISS,'do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'15:31',
   'note':K('빛의 징조 + 소멸의 오브로 훼손 옵션 제거.','Light + Annulment removes the desecrated modifier.')},
  {'id':'a15','phase':'des','branch':MISS,'do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'mark':{'gi':markA_s,'alt':markA_p},'chance':0.5},'fail':{'goto':'self','via':{'cur':'Preserved_Collarbone'}},'ts':'15:36',
   'note':K('좌측 결정화의 징조 + 심연의 에센스로 엉뚱한 접두를 지우고 심연 군주의 징표(접두·접미 반반). 징표가 접두에 붙으면 보존된 빗장뼈로 훼손한 뒤 다시 이 단계(그 접두가 지워짐). 접미에 붙을 때까지. 앞 바퀴 엑잘에서 에너지 보호막이 이미 떴으면 이 단계는 건너뛰고 바로 훼손.','Sinistral Crystallisation + Essence of the Abyss removes the wrong prefix and adds the Mark (50/50 side). On a prefix, desecrate it with a Preserved Collarbone and repeat this step (it removes that prefix) until the Mark is a suffix. If an earlier exalt already landed Energy Shield, skip this and desecrate right away.')},
  {'id':'a17','phase':'des','branch':MISS,'do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_the_Blackblooded'],'target':{'unrev':'s','fromMark':True},'ts':'18:21',
   'note':K('검은 피의 징조 + 보존된 빗장뼈로 접미(징표 자리) 훼손.','Blackblooded + Collarbone desecrates the suffix (the Mark slot).')},
  {'id':'a18','phase':'des','branch':MISS,'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':allQ},'side':'s','lord':'kurgal','bone':'Preserved_Collarbone'},'fail':{'goto':'a14','via':LIGHT},'ts':'18:32',
   'note':K('심연의 메아리의 징조로 공개. 안 나와도 다음 단계(접두 엑잘)를 먼저 던져 에너지 보호막을 본 뒤 {#a14}번(빛의 징조)부터 다시. 적은 비용으로 훼손 기회와 접두 기회를 한 번에 봄.','Reveal with Abyssal Echoes. On a miss, still throw the next prefix exalt for Energy Shield, then go back to step {#a14} (Light): one reveal and one prefix chance per loop.')},
  {'id':'a16','phase':'des','branch':MISS,'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':[{'gi':esFlat,'tmax':1},{'gi':esPct,'tmax':1}]},'ts':'16:03',
   'note':K('완벽한 엑잘티드 오브로 접두 옵션 하나(에너지 보호막 1티어, 접미는 꽉 차서 징조 불필요). 영상은 여기서 멈춤. 공개도 성공했고 이것만 안 뜨면 갈림길.','Perfect Exalt one prefix (T1 Energy Shield; suffixes are full, no omen); the video stopped here. If the reveal landed and only this missed, choose a fork.')},
  {'id':'a16b','phase':'des','branch':MISS,'do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':[{'gi':esFlat,'tmax':1},{'gi':esPct,'tmax':1}],'replace':'p'},'fallbackFor':'a16','fail':{'goto':'self'},
   'label':K('갈림길 ①: 계속 돌리기','Fork (1): keep rolling'),
   'note':K('좌측 말소의 징조 + 상위 카오스 오브로 접두를 계속 돌려 에너지 보호막 1티어 찾기. 좌측 말소의 징조는 접두만 바꾸고, 접두엔 엉뚱한 옵션과 분열 옵션뿐이라 좋은 옵션이 안 지워짐.','Sinistral Erasure + Greater Chaos keeps rerolling the prefix for T1 Energy Shield; Erasure only touches prefixes, and the only removable prefix is the wrong one.')},
  {'id':'a16c','phase':'des','branch':MISS,'do':'note','fallbackFor':'a16','label':K('갈림길 ②: 타협','Fork (2): settle'),
   'note':K('좌측 결정화의 징조 + 완벽한 강화의 에센스로 엉뚱한 접두를 바꿔 가성비 마무리.','Sinistral Crystallisation + Perfect Essence of Enhancement swaps the wrong prefix for a cheap finish.')},
  {'id':'a19','phase':'finish','do':'note','ts':'19:13','extra':{'Perfect_Flux':1,'Perfect_Jewellers_Orb':1},
   'note':K('완벽한 유동체로 부여 스킬 20레벨, 완벽한 쥬얼러 오브로 5홈. 축성은 선택(퀄리티 34 이상 5레벨, 성공 시 6레벨).','Perfect Flux to raise the granted skill to 20, Perfect Jeweller\'s Orb for 5 sockets. Sanctifying is optional.')},
 ],
})

# ---- Refined Breach Ring, the recommended route from SL 게임연구소's video "원소 3플랫 ALL 1티어 재련된 균열 반지" (youtu.be/RiJixgqBnBY) ----
c='Rings'
def textR(t, sec, side=None, first=False):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return max(hits, key=lambda gi: cd(c)['groups'][gi]['t'][0][0])   # the ladder with the highest tier, not the low-level roll
fireF=textR('Fire damage to Attacks','n','p'); coldF=textR('Cold damage to Attacks','n','p'); lightF=textR('Lightning damage to Attacks','n','p')
allRes=textR('to all Elemental Resistances','n','s'); rarS=textR('increased Rarity of Items found','n','s')
maxQR=textR('to Maximum Quality','e','p'); swift=textR('increased Attack Speed','e','s')
FL=[{'gi':fireF,'tmax':1},{'gi':coldF,'tmax':1},{'gi':lightF,'tmax':1}]
V3='https://www.youtube.com/watch?v=RiJixgqBnBY'
R.append({
 'id':'breach-ring-video', 'cls':c, 'base':base(c,'Refined Breach Ring'), 'ilvl':80, 'difficulty':4, 'budget':'high', 'buildTags':[K('원소','Elemental'),K('공격','Attack'),K('희귀도','Rarity')], 'patch':'0.5.5', 'created':'2026-11-08',
 'author':K('SL 게임연구소 영상 기반','Based on SL 게임연구소'),
 'source':{'url':V3, 'title':'[POE2 0.5.5] #6 원소 3플랫 ALL 1티어 재련된 균열 반지. 끝까지 간다! 제작 멸망전!', 'channel':'SL 게임연구소!'},
 'title':K('원소 3플랫 1티어','three T1 elemental flats'),
 'note':K('영상 앞부분의 권장 순서(분열 먼저 → 퀄리티)로 구성. 영상 본편은 75퀄을 먼저 한 "따라하지 말라"는 실험이라 제외.','Built from the recommended order at the start of the video (fracture first, then quality). The main run (75% quality first) is the "do not copy" experiment and is left out.'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'s'},{'junk':'s'}]},
 'phases':[
   {'id':'base','kr':'베이스','en':'Base'},
   {'id':'fracture','kr':'원소 플랫 분열','en':'Fracture an elemental flat'},
   {'id':'quality','kr':'퀄리티 작업','en':'Quality'},
   {'id':'suffix','kr':'접미 옵션 3개','en':'Three suffixes'},
   {'id':'prefix','kr':'접두 원소 플랫','en':'Prefix elemental flats'},
   {'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'c1','phase':'base','do':'base','cost':'base','ts':'1:27',
   'note':K('제련된 균열 반지(균열 나무에서만, 항상 레어). 아이템 레벨 75 이상이면 충분(목표 옵션 중 75 넘는 게 없음). 계산은 80 기준. 가성비면 일반 균열 반지도 가능.','Refined Breach Ring (Breach tree only, always rare). Item level 75+ is enough (no target mod is above 75); 80 assumed. A plain Breach Ring works for a budget build.')},
  {'id':'c2','phase':'fracture','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':FL,'replace':'p'},'fail':{'goto':'self'},'ts':'2:00',
   'note':K('카오스 오브로 화염·냉기·번개 플랫 중 아무거나 1티어. 물리 플랫은 수치가 낮아 비추. 영상 기준 약 250개에 한 번.','Chaos until any T1 fire/cold/lightning flat. Physical flat rolls too low. About 1 in 250 per the video.')},
  {'id':'c3','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'22:21',
   'note':K('빗장뼈로 훼손 자리를 채워 옵션 4개(훼손은 분열 안 됨).','Fill a slot with a Collarbone desecration (it cannot fracture).')},
  {'id':'c4','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':FL},'fail':{'goto':'restart'},'ts':'25:53',
   'after':{'keepOnly':[fireF,coldF,lightF,'junk']},
   'note':K('훼손 제외 옵션 3개 중 옵션 1개(1/3). 이후 훼손 자리는 정리.','1 in 3 (the desecrated slot cannot fracture). The desecrated slot is cleared afterwards.')},
  {'id':'c4b','phase':'quality','do':'remove','cur':'Orb_of_Annulment','target':{'removeJunk':'s'},
   'note':K('에센스를 바르기 전에 잡옵 하나를 소멸의 오브로 미리 지워 깔끔하게 정리.','Clear one junk modifier with an Annulment before the essence.')},
  {'id':'c5','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':maxQR},'ts':'2:23',
   'note':K('균열의 에센스로 최대 퀄리티 +20%.','Essence of the Breach: +20% Maximum Quality.')},
  {'id':'c6','phase':'quality','do':'quality','cur':'Reaver_Catalyst','target':{'quality':65},'ts':'6:55',
   'note':K('강탈자 기폭제로 65%까지(기본 20% + 제련된 균열 반지 고정 옵션 25% + 균열의 에센스 20%). 영상은 반지 9개에 466개.','Reaver Catalysts to 65% (20% base + 25% from the Refined Breach Ring implicit + 20% from the Breach line). The video used 466 for nine rings.')},
  {'id':'c7','phase':'quality','do':'manual','cost':'vaal','target':{'setQuality':70},'label':K('바알 촉진시키는 주입기','Vaal Catalysing Infuser'),'ts':'2:31',
   'after':{'junk':[maxQR]},
   'note':K('첫 1회는 100% 성공이라 최소 한 번은 바름. 그다음부터는 타락 위험이 있어 감당 가능한 선까지(70% 권장, 75%는 돈 낭비). 운 요소가 커서 비용은 직접 입력. 퀄리티가 끝나면 최대 퀄리티 옵션은 지워져도 됨.','The first one always succeeds, so use at least one; after that it can corrupt, so stop where you are comfortable (70% suggested). Mostly luck, so enter the cost. Once quality is done the Maximum Quality mod can be removed.')},
  {'id':'c8','phase':'suffix','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':rarS,'tmax':1},{'gi':allRes,'tmax':1}],'replace':'p'},'fail':{'goto':'self'},'ts':'3:10',
   'note':K('카오스 오브로 원하는 접미 하나(영상 완성품: 모든 원소 저항, 아이템 희귀도). 분열 옵션 말고 지울 수 있는 옵션이 최대 퀄리티뿐이라 첫 카오스 오브가 그 옵션을 지움 — 제작 옵션인 최대 퀄리티가 없어져서 뒤에 재빠른 합금을 쓸 수 있음(퀄리티는 그대로). 영상 순서대로 희귀도를 카오스 오브 쪽에서 뽑는 걸로 계산.','Chaos for one wanted suffix (the finished ring has all resistances and item rarity). Following the video, rarity is counted on the Chaos side.')},
  {'id':'c9','phase':'suffix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':allRes,'tmax':1},{'gi':rarS,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'c8'},'ts':'3:17',
   'note':K('완벽한 엑잘티드 오브 + 우측 찬미의 징조로 나머지 하나. 영상은 안 뜨면 지우고 다시 카오스 오브(6번째 성공). 계산은 우측 소멸의 징조 + 소멸의 오브로 지우되, 희귀도가 대신 지워지면 {#c8}번으로 돌아가 다시 뽑는 것까지 포함.','Perfect Exalt + Dextral Exaltation for the other one. The video removed misses and went back to Chaos (success on try 6); the math removes with Dextral Annulment and, when it takes the rarity instead, goes back to step {#c8} to roll it again.')},
  {'id':'c10','phase':'suffix','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'3:24',
   'note':K('접두에 아무 잡옵 하나(일반 엑잘티드 오브).','Any junk prefix (a regular Exalted Orb).')},
  {'id':'c11','phase':'suffix','do':'essence','cur':'Swift_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':swift},'ts':'3:32',
   'note':K('좌측 결정화의 징조로 그 잡옵을 지우고 재빠른 합금으로 접미에 공격 속도.','Sinistral Crystallisation removes that junk prefix; Swift Alloy adds Attack Speed as a suffix.')},
  {'id':'c12','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':FL},'fail':{'goto':'c13'},'ts':'3:39',
   'note':K('완벽한 엑잘티드 오브 한 번(상위 찬미의 징조는 켜지 않음). 원소 플랫 1티어가 뜨면 훼손으로 마무리.','One Perfect Exalt (no Greater Exaltation). If a T1 elemental flat lands, finish with a desecration.')},
  {'id':'c13','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','withEach':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']},'target':{'anyOf':FL,'replace':'p'},'fallbackFor':'c12','fail':{'goto':'self'},'ts':'3:54',
   'note':K('좌측 소멸의 징조 + 완벽한 엑잘티드 오브 반복. 가중치 200짜리라 평균 50번 정도(영상은 59번). 너무 안 나오면 2티어로 타협.','Repeat Sinistral Annulment + Perfect Exalt. Weight 200, so about 50 tries on average (59 in the video). Settle for T2 if it drags on.')},
  {'id':'c15','phase':'prefix','do':'reveal','cur':'Ancient_Collarbone','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':FL},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'self','via':LIGHT},'ts':'29:27',
   'note':K('마지막 원소 플랫 1티어는 고대 빗장뼈 + 심연의 메아리의 징조로. 영상은 17개.','The last T1 elemental flat via Ancient Collarbone + Abyssal Echoes; 17 in the video.')},
  {'id':'c16','phase':'finish','do':'note','ts':'4:26',
   'note':K('자본이 많으면 디바인 후 축성 또는 타락.','With a big budget: divine, then sanctify or corrupt.')},
 ],
})

# ---- Helmet: SL 게임연구소 "#2 종결급 투구 제작 가이드 | 화염파용" (youtu.be/p0fChSu91uI) ----
c='Helmets_str'; V4='https://www.youtube.com/watch?v=p0fChSu91uI'
life=g(c,'to maximum Life',side='p'); armF=g(c,'to Armour',side='p'); armP=g(c,'increased Armour',side='p')
armEle=g(c,'Armour also applies to Elemental'); fireR=g(c,'to Fire Resistance'); coldR=g(c,'to Cold Resistance'); lightR=g(c,'to Lightning Resistance')
rarS=g(c,'Rarity of Items found',side='s'); rarE=g(c,'Rarity of Items found','e','s')
P3=[{'gi':life,'tmax':1},{'gi':armF,'tmax':1},{'gi':armP,'tmax':1}]; RES=[{'gi':fireR,'tmax':1},{'gi':coldR,'tmax':1},{'gi':lightR,'tmax':1}]
R.append({
 'id':'helmet-armour-sl', 'cls':c, 'base':base(c,'Imperial Greathelm'), 'ilvl':82, 'sockets':2, 'exceptional':{'sockets':1},
 'difficulty':2, 'budget':'medium', 'buildTags':[K('방어도','Armour'),K('생명력','Life'),K('원소 저항','Elemental res')],
 'patch':'0.5.5', 'created':'2026-11-08',
 'author':K('SL 게임연구소 영상 기반','Based on SL 게임연구소'),
 'source':{'url':V4, 'title':'[POE2 0.5.5] #2 종결급 투구 제작 가이드 | 화염파용', 'channel':'SL 게임연구소!'},
 'title':K('방어도·생명력 올 1티어 (화염파용)','all-T1 armour + life (Fireball)'),
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'magic','kr':'매직 단계','en':'Magic stage'},{'id':'rare','kr':'레어 전환','en':'To rare'},
           {'id':'fracture','kr':'분열','en':'Fracture'},{'id':'prefix','kr':'접두 작업','en':'Prefixes'},{'id':'suffix','kr':'접미 작업','en':'Suffixes'},{'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'1:04',
   'note':K('제국의 대헬름, 아이템 레벨 82, 소켓 2개(특출난) 일반 아이템을 구매. 영상은 4개 준비.','Buy a normal ilvl 82 Imperial Greathelm with 2 sockets (exceptional). The video prepares four.')},
  {'id':'h2','phase':'base','do':'manual','cost':'quality','optional':True,'target':{'setQuality':26},'label':K('퀄리티 25% 이상 (선택)','Quality 25%+ (optional)'),'ts':'3:03',
   'note':K('바알 방어구 장인의 주입기로 20% 이상. 퀄리티가 오를수록 성공 확률이 낮고 타락할 수 있어 3~4개 발라서 하나 건지는 방식. 영상은 26%.','Vaal infusers past 20%; the higher it goes, the lower the odds and it can corrupt, so try 3–4 bases and keep one. 26% in the video.')},
  {'id':'m1','phase':'magic','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'anyOf':[{'gi':armP,'tmax':1},{'gi':armEle,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},'ts':'4:00',
   'note':K('방어도 % 증가 1티어 또는 방어도→원소 적용 1티어. 필요 없는 옵션은 소멸의 오브로 지우고 다시.','T1 % Armour or T1 Armour-applies-to-Elemental. Annul anything else and retry.')},
  {'id':'m2','phase':'magic','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'anyOf':[{'gi':armP,'tmax':1},{'gi':armEle,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'}},'ts':'4:08',
   'note':K('나머지 하나. 방어구는 1티어가 잘 떠서 몇 번이면 됨.','The other one. Armour bases roll T1 often, so a few tries.')},
  {'id':'r1','phase':'rare','do':'essence','cur':'Greater_Essence_of_Opulence','target':{'gi':rarE,'ti':0},'ts':'4:31',
   'note':K('상위 풍요의 에센스로 희귀 전환 + 접미 희귀도. 이제 세 옵션 모두 유효 옵션.','Greater Essence of Opulence: rare + a Rarity suffix. All three modifiers are now useful.')},
  {'id':'r2','phase':'rare','do':'divine','cur':'Divine_Orb','optional':True,'ts':'4:40',
   'note':K('분열 전에 수치를 조금 다듬음(선택). 분열된 옵션은 이후 수치를 바꾸기 어려움.','Tidy the rolls before fracturing (optional).')},
  {'id':'f1','phase':'fracture','do':'desecrate','cur':'Preserved_Rib','target':{'unrev':'p'},'ts':'5:47',
   'note':K('분열의 오브는 옵션 4개가 필요해서 보존된 갈비뼈로 옵션 하나 채움. 훼손(미공개)은 분열되지 않음.','The Fracturing Orb needs four modifiers, so a Preserved Rib fills one. Unrevealed desecrated mods cannot fracture.')},
  {'id':'f2','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':armEle},{'gi':armP},{'gi':rarE}]},'ts':'5:56',
   'note':K('남은 옵션 세 개가 모두 유효 옵션이라 어느 쪽이 분열돼도 성공(100%). 영상은 방어도→원소 적용이 분열됨. 아래 단계는 그 경우 기준.','All three remaining lines are wanted, so any fracture works (100%). In the video Armour-applies-to-Elemental fractured; the steps below follow that case.')},
  {'id':'f3','phase':'fracture','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},'optional':True,'ts':'6:09',
   'exit':K('제작 종료 (그대로 쓰거나 판매)','stop here (use or sell it)'),
   'note':K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 한 번 도박(접두 1·접미 1). 1티어 옵션 두 개처럼 괜찮은 옵션이 뜨면 여기서 제작 끝 — 그대로 쓰거나 팔면 됨. 꽝이면 다음 단계로. 영상은 2·3티어라 꽝.','One gamble with Greater Exaltation + Perfect Exalt (one prefix, one suffix). If it lands something good, such as two T1 lines, the craft ends here: use or sell it. Otherwise continue. The video got T2/T3.')},
  {'id':'f4','phase':'fracture','do':'remove','cur':'Orb_of_Annulment','expect':4,'after':{'keepOnly':[armEle,'junk1']},'ts':'6:57',
   'note':K('소멸의 오브로 정리해서 분열 옵션 + 아무 옵션 하나만 남김(어떤 옵션이든 상관없음). 다음 단계 카오스 오브가 그 옵션 하나를 원하는 옵션으로 바꿈.','Annul down to the fractured mod plus any one line (it does not matter which); the next Chaos turns that line into a wanted mod.')},
  {'id':'b1','phase':'prefix','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':P3},'fail':{'goto':'self'},'ts':'7:05',
   'note':K('카오스 오브로 접두 1티어 하나: 방어도 1티어, 방어도 % 1티어, 생명력 1티어 중 아무거나. 방어구는 가중치가 높아 금방 나옴.','Chaos for one T1 prefix: flat Armour, % Armour or Life, any of them. Armour weights are high, so it comes quickly.')},
  {'id':'b2','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':P3},'fail':{'goto':'b1','via':{'cur':'Orb_of_Annulment'}},'ts':'7:51',
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 하나 더. 원하지 않는 옵션이면 소멸의 오브로 지우고(유효 옵션이 같이 지워지면 카오스 오브부터 다시). 영상에서 가장 어려운 구간.','Sinistral Exaltation + Perfect Exalt for another prefix. On a miss, annul (if the good one goes too, chaos again). The hardest part of the craft.')},
  {'id':'b3','phase':'prefix','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'8:44',
   'note':K('남은 접두 한 자리는 훼손으로: 고대 갈비뼈 + 좌측 강령술의 징조. 접두 3종 중 아직 없는 옵션 하나만 찾으면 됨.','The last prefix slot goes to a desecration: Ancient Rib + Sinistral Necromancy. Only the one prefix still missing is needed.')},
  {'id':'b4','phase':'prefix','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':P3},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'b3','via':LIGHT},'ts':'8:54',
   'note':K('영혼의 우물에서 심연의 메아리의 징조로 공개해 남은 하나(이미 붙은 두 옵션과 같은 계열은 안 나오므로 사실상 그 하나)를 찾음. 영상은 한 번에 방어도 % 1티어. 실패하면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손.','Reveal at the Well with Abyssal Echoes; the video hit T1 % Armour first time. On a miss, Light + Annulment and desecrate again.')},
  {'id':'s1','phase':'suffix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':RES},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}},'ts':'9:12',
   'note':K('접두가 꽉 차서 상위 찬미의 징조 + 완벽한 엑잘티드 오브의 옵션 두 개가 모두 접미로. 원소 저항 1티어 아무거나. 2·3티어로 타협해도 됨, 아니면 우측 소멸의 징조 + 소멸의 오브로 지우고 다시(영상은 3번째에 냉기 1티어).','Prefixes are full, so Greater Exaltation puts both lines on suffixes: any T1 elemental resistance. T2/T3 is acceptable; otherwise Dextral Annulment and retry (third try in the video).')},
  {'id':'s2','phase':'suffix','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'anyOf':[{'gi':rarS,'tmax':1}],'replace':'s'},'fail':{'goto':'self'},'ts':'10:15',
   'note':K('절사의 징조 + 완벽한 카오스 오브로 남은 접미 옵션 하나. 접두가 날아갈 수 있어 우측 말소의 징조도 켬. 영상은 희귀도 1티어로 마무리.','Whittling + Perfect Chaos for the last suffix, with Dextral Erasure so prefixes are safe. The video finished with T1 Rarity.')},
 ],
})

# ---- 6-line Gold Amulet: SL 게임연구소 "#7 황금 목걸이 심연의 에센스 활용하여 졸업급으로 만들기" (youtu.be/cb36jD9pqsw) ----
c='Amulets'; V5='https://www.youtube.com/watch?v=cb36jD9pqsw'
spirit5=textA('to Spirit','n','p'); spelld5=textA('increased Spell Damage','n','p'); spell5=textA('Level of all Spell Skills','n','s'); maxQ5=textA('to Maximum Quality','e','p')
gdef5=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Perfect Essence of Enhancement' in [x[3] for x in gr['t']]][0]
mark5_p=textA('Abyssal Lord','e','p'); mark5_s=textA('Abyssal Lord','e','s')
SUF5=[{'gi':textA('Rarity of Items found','n','s'),'tmax':2},{'gi':textA('to all Elemental Resistances','n','s'),'tmax':2},
      {'gi':textA('to Fire Resistance','n','s'),'tmax':2},{'gi':textA('to Cold Resistance','n','s'),'tmax':2},{'gi':textA('to Lightning Resistance','n','s'),'tmax':2}]
MISS5={'of':'p2','when':'miss'}
R.append({
 'id':'gold-amulet-6line', 'cls':c, 'base':base(c,'Gold Amulet'), 'ilvl':82, 'difficulty':3, 'budget':'high',
 'buildTags':[K('주문','Spell'),K('정신력','Spirit'),K('희귀도','Rarity')], 'patch':'0.5.5', 'created':'2026-11-08',
 'author':K('SL 게임연구소 영상 기반','Based on SL 게임연구소'),
 'source':{'url':V5, 'title':'[POE2 0.5.5] #7 황금 목걸이 심연의 에센스 활용하여 졸업급으로 만들기! (태양의 목걸이, 옵션 6개 목걸이)', 'channel':'SL 게임연구소!'},
 'title':K('정신력 분열 + 주문 +3 옵션 6개','fractured Spirit + spell +3, six lines'),
 'note':K('목표 구조: 접두 = 정신력(분열) + 완벽한 강화의 에센스 방어 % + 적당한 접두 옵션 1개, 접미 = 주문 스킬 +3 + 적당한 접미 옵션 1개 + 훼손 옵션 1개. 접두 옵션 2개·접미 옵션 2개까지만 노리고 나머지는 나오는 걸 씀. 영상 1트 기준 경로이고, 다른 경우는 각 단계 메모 참고.',
          'Target: prefixes = fractured Spirit + Perfect Essence of Enhancement defences + one acceptable prefix; suffixes = spell +3 + one acceptable suffix + one desecration. Aim for two lines on each side and take what comes for the rest. Main path from the first attempt; other cases are in the step notes.'),
 'start':{'rar':'rare','mods':[{'gi':spirit5,'tmax':1},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fracture','kr':'분열','en':'Fracture'},{'id':'skill','kr':'주문 스킬 +3','en':'Spell skills +3'},
           {'id':'quality','kr':'퀄리티 작업','en':'Quality'},{'id':'suffix','kr':'접미 옵션 하나 완성','en':'First suffix'},{'id':'prefix','kr':'접두 작업','en':'Prefixes'},
           {'id':'last','kr':'마지막 접미 (훼손)','en':'Last suffix (desecration)'},{'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'1:54',
   'note':K('황금 목걸이(또는 태양의 목걸이), 아이템 레벨 82 이상, 정신력 +50(1티어)이 붙은 옵션 3개 이하 희귀 목걸이. 접미는 아무 옵션이나 상관없음.','A rare Gold (or Solar) Amulet, item level 82+, with +50 Spirit (T1) and three lines or fewer. Suffixes do not matter.')},
  {'id':'g2','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},
   'note':K('분열의 오브는 옵션 4개가 필요해서 보존된 빗장뼈로 옵션 하나 채움(훼손은 분열되지 않아 정신력 확률 1/3).','The Fracturing Orb needs four modifiers, so a Preserved Collarbone fills one (desecrations cannot fracture, so Spirit is 1 in 3).')},
  {'id':'g3','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':spirit5}]},'fail':{'goto':'restart'},'ts':'11:10',
   'after':{'keepOnly':[spirit5,'junk1']},
   'note':K('정신력 분열 1/3. 영상은 4개 중 1개 성공. 이후 분열 + 옵션 하나만 남기고 소멸의 오브.','Spirit fractures 1 in 3; 1 of 4 in the video. Then annul down to the fracture plus one line.')},
  {'id':'k1','phase':'skill','do':'chaos','cur':'Chaos_Orb','target':{'gi':spell5,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'11:35',
   'after':{'keepOnly':[spirit5,spell5]},
   'note':K('카오스 오브로 주문 스킬 +3. 아무 스킬 +3은 약 425번, 원하는 주문 +3은 약 1,700번에 한 번. 이미 띄워 놓은 매물이 싸면 구매.','Chaos for +3 spell skills: any +3 about 1 in 425, spell +3 about 1 in 1,700. Buy one already rolled if it is cheap.')},
  {'id':'q1','phase':'quality','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'12:22',
   'note':K('접두에 아무 잡옵 하나(지울 자리라 일반 엑잘티드 오브). 어떤 스킬 레벨이 뜰지 몰라서 퀄리티는 이 시점에 함.','Any junk prefix (a regular Exalt, it gets removed). Quality comes now because the skill type is only known now.')},
  {'id':'q2','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':maxQ5},'ts':'12:30',
   'note':K('좌측 결정화의 징조로 잡옵을 지우고 균열의 에센스로 최대 퀄리티 +20%.','Sinistral Crystallisation removes the junk; Essence of the Breach adds +20% maximum quality.')},
  {'id':'q3','phase':'quality','do':'quality','cur':'Sibilant_Catalyst','target':{'quality':40},'ts':'12:30',
   'note':K('쇳소리 기폭제로 퀄리티 40%. 주문 스킬 +3이 +4가 됨.','Sibilant Catalyst to 40% quality; spell +3 becomes +4.')},
  {'id':'s1','phase':'suffix','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':SUF5,'removeGi':maxQ5},'fail':{'goto':'self'},'ts':'12:55',
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티를 날리고 접미 옵션 하나부터 완성. 접미는 2티어 이상 적당한 옵션이면 멈춤. 옵션이 접두로 가면 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 접미를 노림. 영상은 희귀도 1티어.','Whittling + Perfect Chaos removes max quality; finish one suffix first. Stop at any decent T2+ suffix. If the roll goes to a prefix, use Dextral Exaltation + Perfect Exalt for the suffix. The video got T1 Rarity.')},
  {'id':'p1','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'target':{'anyOf':[{'gi':spelld5,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}},'ts':'15:06',
   'note':K('좌측 찬미의 징조 + 상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 두 자리를 채우며 주문 피해 % 1티어(27—30%)를 노림 — 주문 빌드 기준 베스트 접두이자 영상 1트 완성품의 옵션. 같이 붙은 나머지 옵션 하나는 다음 단계에서 정리. 안 뜨면 좌측 소멸의 징조 + 소멸의 오브로 지우고 다시. 주문 빌드가 아니면 에너지 보호막·생명력 최대치 1티어도 대안.','Sinistral + Greater Exaltation + Perfect Exalt fills both prefix slots, aiming for T1 % Spell Damage (27–30%): the best prefix for a spell build and what the video\'s first amulet got. The other line is dealt with next. On a miss, Sinistral Annulment and retry. For non-spell builds, T1 flat ES or Life work too.')},
  {'id':'p2','phase':'prefix','do':'essence','cur':'Perfect_Essence_of_Enhancement','target':{'gi':gdef5,'chance':0.5},'fail':{'goto':'p3'},'ts':'16:18',
   'note':K('완벽한 강화의 에센스(접두가 꽉 차 있어서 결정화의 징조 없이도 접두 중 하나가 지워짐): 50% 확률로 주문 피해 대신 나머지 잡옵이 지워지고 방어 % 옵션이 붙으면 접두 완성. 둘 다 별로면 먼저 심연의 에센스로 하나를 지움.','One bad prefix: Perfect Essence of Enhancement (prefixes are full, so no omen) removes it half the time and adds defences, finishing the prefixes. If both are bad, clear one with an Essence of the Abyss first.')},
  {'id':'p3','phase':'prefix','retryFor':'p2','do':'essence','cur':'Essence_of_the_Abyss','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'mark':{'gi':mark5_s,'alt':mark5_p},'chance':0.5},'fail':{'goto':'p3b'},'ts':'6:42',
   'note':K('잡옵이 살아남으면 심연의 에센스 차례: 좌측 결정화의 징조로 접두 잡옵을 지우고 심연 군주의 징표. 징표가 접미로 가면 성공.','If the junk survives, use the Essence of the Abyss: Sinistral Crystallisation clears the junk prefix and adds the Mark. Success when the Mark lands on a suffix.')},
  {'id':'p3b','phase':'prefix','retryFor':'p2','do':'remove','cur':'Preserved_Collarbone','withEach':LIGHT,'target':{'removeMark':True},'fallbackFor':'p3','ts':'7:47',
   'note':K('징표가 접두에 찍히면 빗장뼈로 훼손 → 빛의 징조 + 소멸의 오브로 지우고 다시 심연의 에센스. 징표가 접미로 내려올 때까지.','If the Mark lands on a prefix, desecrate it with a Collarbone, remove it with Light + Annulment, and use the Essence of the Abyss again until the Mark goes to a suffix.')},
  {'id':'p4','phase':'prefix','retryFor':'p2','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'fail':{'goto':'p2','label':'reveal'},'ts':'8:02',
   'note':K('비운 접두 자리에 다시 완벽한 엑잘티드 오브. 다시 잡옵이면 {#p2}번(완벽한 강화의 에센스)부터 반복. 접미의 징표는 다음에 심연의 에센스를 써야 할 때 지움.','Perfect Exalt the freed prefix again; if it is junk, repeat from the Perfect Essence of Enhancement. Clear the suffix Mark only when the next Essence of the Abyss is needed.')},
  {'id':'d1','phase':'last','do':'desecrate','cur':'Ancient_Collarbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'15:22',
   'note':K('마지막 접미 자리는 고대 빗장뼈 훼손(보존된 빗장뼈는 1티어가 잘 안 나옴).','The last suffix slot: an Ancient Collarbone desecration (a Preserved one rarely gives T1).')},
  {'id':'d2','phase':'last','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SUF5},'side':'s','bone':'Ancient_Collarbone'},'fail':{'goto':'d1','via':LIGHT},'ts':'15:43',
   'note':K('심연의 메아리의 징조로 공개. 적당한 옵션이면 마무리.','Reveal with Abyssal Echoes and stop at anything decent.')},
  {'id':'g9','phase':'finish','do':'note','ts':'16:34',
   'note':K('완성. 영상 1트 완성품: 정신력 +50(분열) · 주문 피해 30%(1티어) · 방어 % 21%(완벽한 강화의 에센스) / 투사체 스킬 +3 · 희귀도 15%(1티어) · 모든 능력치 +21(훼손 2티어), 퀄리티 40%.','Done. The video\'s first amulet: Spirit +50 (fractured), 30% Spell Damage (T1), 21% defences (Enhancement) / +3 projectile skills, 15% Rarity (T1), +21 all attributes (desecrated T2), 40% quality.')},
 ],
})

# ---- Hard one: Runefather's Grasping Mail, +1 all spell skills (반지깎는노인, youtu.be/y5Ch3AJpl5c) ----
# Grasping Mail can roll ring modifiers, which our body-armour data lacks: build a recipe-only class = body armour + ring pool.
import copy
_ba=json.load(open(f'{D}c/Body_Armours_str_dex_int.json')); _ri=json.load(open(f'{D}c/Rings.json'))
gm=copy.deepcopy(_ba); gm['id']='Grasping_Mail_ring'; gm['en']='Grasping Mail (ring modifiers)'; gm['kr']='탐욕스러운 사슬옷 (반지 속성)'
gm['bases']=[b for b in gm['bases'] if 'Grasping' in b['en']]
rf=copy.deepcopy(gm['bases'][-1]); rf['id']='Runefathers_Grasping_Mail'; rf['en']="Runefather's Grasping Mail"; rf['kr']='룬 아버지의 탐욕스러운 사슬옷'
rf['props']=[['Armour: 136','Evasion Rating: 124','Energy Shield: 38','Base Movement Speed: -0.04'],['방어도: 136','회피: 124','에너지 보호막: 38','Base Movement Speed: -0.04']]
rf['imp']=[["Can roll Ring Modifiers","Catalysts can be applied to this item","Bonded: +5% to Quality of all Skills"],['반지 속성 부여 가능','이 아이템에 기폭제 적용 가능','결속: 모든 스킬 퀄리티 +5%']]
gm['bases'].append(rf)
_have={tuple(g['f']) for g in gm['groups'] if g['s']=='n'}
for _g in _ri['groups']:
    if (_g['s']=='n' and tuple(_g['f']) not in _have) or (_g['s']=='x' and _g['sub'][1].startswith('Genesis Tree')): gm['groups'].append(copy.deepcopy(_g))
json.dump(gm,open(f'{D}c/Grasping_Mail_ring.json','w'),ensure_ascii=False); cache.pop('Grasping_Mail_ring',None)
c='Grasping_Mail_ring'
spell1=g(c,'+1 to Level of all Spell Skills','x'); scd=g(c,'Critical Spell Damage Bonus','x'); cast=g(c,'increased Cast Speed','n','s')
sdmg=g(c,'increased Spell Damage','x'); notable=g(c,'Allocates a random Notable','e'); ward=g(c,'increased Runic Ward','e')
V6='https://www.youtube.com/watch?v=y5Ch3AJpl5c'
R.append({
 'id':'grasping-mail-spell1', 'cls':c, 'clsAs':'Body_Armours_str_dex_int', 'base':base(c,"Runefather's Grasping Mail"), 'ilvl':82, 'difficulty':5, 'budget':'high', 'unknownW':True,
 'buildTags':[K('주문','Spell'),K('룬 수호','Runic Ward'),K('반지 속성','Ring modifiers')], 'patch':'0.5', 'created':'2026-11-08',
 'author':K('반지깎는노인 영상 기반','Based on 반지깎는노인'),
 'source':{'url':V6, 'title':'POE2 역사상 가장 만들기 힘든 갑옷', 'channel':'반지깎는노인'},
 'title':K('모든 주문 스킬 +1 시전자 갑옷','+1 all spell skills caster armour'),
 'note':K('반지 속성이 붙는 갑옷이라 기원의 나무 시전 옵션(모든 주문 스킬 +1, 주문 피해, 주문 치명타 피해)을 갑옷에 올림. 이 베이스의 반지 옵션 가중치는 아직 확인된 데이터가 없어서 확률 대신 제작자가 실제로 쓴 횟수로 표시. 영상 제작자 본인도 카오스 약 22만 개, 4일이 들었다며 따라 하지 말라고 할 만큼 극한 제작.',
          'Ring modifiers can roll on this armour, so Genesis Tree caster mods (+1 spell skills, spell damage, spell crit damage) go on a body armour. We have no confirmed weights for ring mods on this base, so steps show the author\'s actual counts instead of odds. The author spent about 220,000 Chaos Orbs over four days and says not to try it: an extreme craft.'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'rune','kr':'룬 아버지 승급','en':'Runefather upgrade'},{'id':'quality','kr':'퀄리티 30/30','en':'Quality 30/30'},
           {'id':'skill','kr':'주문 스킬 +1','en':'Spell skills +1'},{'id':'fracture','kr':'분열','en':'Fracture'},{'id':'suffix','kr':'접미 완성','en':'Suffixes'},
           {'id':'prefix','kr':'접두 작업','en':'Prefixes'},{'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'m1','phase':'base','do':'base','cost':'base',
   'note':K('탐욕스러운 사슬옷(아이템 레벨 82). 균열 반지 60개를 수도원에서 교환해서 얻음. "반지 속성 부여 가능" 베이스라 반지 옵션이 굴러감.','Grasping Mail, item level 82, from trading 60 Breach Rings at the monastery. It can roll ring modifiers.')},
  {'id':'m2','phase':'rune','do':'manual','label':K('룬 벼림 → 룬 숙련 → 룬 아버지','Runeforged → Runemastered → Runefather'),
   'note':K('룬 단계를 올려 룬 아버지 베이스로 만듦. 룬 숙련 단계에서 방어도·회피·에너지 보호막 세 방어 속성이 모두 남아 있어야 룬 아버지로 올라감. 룬 아버지는 결속 효과로 모든 스킬 퀄리티 +5%와 룬 수호를 가짐.','Raise the rune stage to Runefather. At the Runemastered stage all three defences (armour, evasion, energy shield) must still be there to reach Runefather. Runefather adds a bonded +5% quality to all skills and Runic Ward.')},
  {'id':'m3','phase':'quality','do':'manual','cost':'vaal','target':{'setQuality':30},'label':K('갑옷 퀄리티 30% + 기폭제 퀄리티 30%','Armour quality 30% + catalyst quality 30%'),
   'note':K('바알 방어구 장인의 주입기로 갑옷 퀄리티, 쇳소리 기폭제 + 바알 촉진시키는 주입기로 기폭제 퀄리티를 각각 30%까지. 주입기는 일정 확률로 아이템을 타락시키니 비싼 옵션이 붙기 전, 가장 먼저 해 두는 게 안전.','Vaal Armourer\'s Infuser for armour quality and a caster catalyst plus Vaal infusers for catalyst quality, both to 30%. Infusers can corrupt the item, so do this first, before anything expensive is on it.')},
  {'id':'k1','phase':'skill','do':'chaos','cur':'Chaos_Orb','target':{'gi':spell1,'replace':'s'},'fail':{'goto':'self'},'expect':220000,
   'note':K('카오스 오브로 모든 주문 스킬 +1(기원의 나무 시전 옵션, 레벨 45). 제작자는 약 22만 개, 4일 걸림. 시세가 맞으면 이미 붙어 있는 베이스를 사는 쪽이 현실적.','Chaos for +1 to all spell skills (a level 45 Genesis Tree caster mod). The author needed about 220,000 over four days. Buying a base that already has it is the realistic route.')},
  {'id':'f0','phase':'fracture','do':'desecrate','cur':'Preserved_Rib','target':{'unrev':'p'},'ts':'8:20',
   'note':K('분열의 오브는 옵션 4개가 필요. 훼손 옵션 하나는 분열되지 않으니 +1이 분열될 확률이 1/3이 됨.','The Fracturing Orb needs four modifiers. A desecrated line cannot fracture, so +1 fractures 1 time in 3.')},
  {'id':'f1','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':spell1}]},'extra':{'Hinekoras_Lock':4},
   'after':{'keepOnly':[spell1,'junk1']},
   'note':K('22만 카오스짜리 옵션이라 그냥 분열하지 않고, 히네코라의 머리카락으로 결과를 미리 봄. 미리 본 결과가 +1이 아니면 아이템을 살짝 바꾸고 다시 머리카락. 영상은 4개째에 +1 분열 확인 후 분열. 이후 분열 + 옵션 하나만 남기고 정리.','At 220,000 Chaos this is not left to chance: Hinekora\'s Lock previews the result. If the preview is not +1, change the item slightly and lock again. The video saw +1 on the fourth lock, then fractured. Afterwards keep the fracture plus one line.')},
  {'id':'s1','phase':'suffix','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'all':[{'gi':scd,'tmax':1},{'gi':cast,'tmax':1}]},'fail':{'goto':'self'},
   'note':K('절사의 징조 + 카오스 오브로 접미 두 자리를 주문 치명타 피해 보너스 1티어(26—29%)와 시전 속도 1티어(22—24%)로 채움. 접미부터 끝내 두면 접두 작업을 마음 편히 할 수 있음.','Whittling + Chaos fills the two suffixes with T1 spell crit damage bonus (26–29%) and T1 cast speed (22–24%). Finishing the suffixes first frees the prefixes.')},
  {'id':'p0','phase':'prefix','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},
   'note':K('에센스가 지울 자리를 만들기 위해 접두에 아무 옵션 하나.','Any prefix, as the slot the essence will remove.')},
  {'id':'p1','phase':'prefix','do':'essence','cur':'Essence_of_Delirium','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':notable},'knownP':True,
   'note':K('좌측 결정화의 징조 + 섬망의 에센스로 접두 잡옵을 지우고 "무작위 주요 패시브 할당". 영상은 지배가 나옴. 시전 빌드라면 자루크의 선물·모범·마학 같은 노드가 인기. 원하는 노드가 아니면 다시.','Sinistral Crystallisation + Essence of Delirium swaps the junk prefix for "Allocates a random Notable". The video got Dominion; for casters, notables like Zarokh\'s Gift, Exemplar or Arcane studies are popular. Redo it if the notable is not one you want.')},
  {'id':'p2','phase':'prefix','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},
   'note':K('합금이 지울 자리로 접두 하나 더.','One more prefix for the alloy to remove.')},
  {'id':'p2b','phase':'prefix','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 장착',"Socket Astrid's Creativity"),
   'note':K('섬망의 에센스 옵션도 제작 옵션이라, 두 번째 제작 옵션(합금)을 붙이려면 아스트리드의 창의성이 필요. 제작이 끝나면 빼고 원하는 룬으로 교체.',"The Delirium line is crafted too, so the second crafted line (the alloy) needs Astrid's Creativity. Swap it for any rune once crafting is done.")},
  {'id':'p3','phase':'prefix','do':'essence','cur':'Sovereign_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':ward,'chance':0.5},'knownP':True,'fail':{'goto':'p1'},
   'note':K('좌측 결정화의 징조 + 군왕의 합금: 접두 둘 중 하나를 지우고 룬 수호 % 증가(24—30%). 잡옵이 지워지면 성공, 노드가 지워지면 섬망의 에센스부터 다시(반반). 좋은 노드를 뽑았다면 히네코라의 머리카락으로 결과를 먼저 보고 쓰는 걸 추천. 영상은 한 번에 성공.','Sinistral Crystallisation + Sovereign Alloy removes one of the two prefixes and adds increased Runic Ward (24–30%). Success when the junk goes; if the notable goes, redo from the Essence of Delirium (50/50). With a good notable, preview with Hinekora\'s Lock first. The video landed it first try.')},
  {'id':'p4','phase':'prefix','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},
   'note':K('마지막 접두는 훼손으로.','The last prefix is a desecration.')},
  {'id':'p5','phase':'prefix','do':'reveal','target':{'reveal':{'anyOf':[{'gi':sdmg,'tmax':1}]},'side':'p','bone':'Preserved_Collarbone'},'fail':{'goto':'p4','via':LIGHT},'ts':'11:40',
   'note':K('영혼의 우물에서 공개해 주문 피해 % 1티어(35—39%)를 고름. 아니면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손.','Reveal at the Well of Souls and take T1 % spell damage (35–39%). Otherwise Light + Annulment and desecrate again.')},
  {'id':'m8','phase':'finish','do':'manual','target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('원하는 룬','a rune of your choice')]},'label':K('룬 교체','Swap the rune'),
   'note':K('아스트리드의 창의성은 제작용이라 원하는 룬으로 교체.',"Astrid's Creativity was only for crafting; swap in the rune you want.")},
  {'id':'m9','phase':'finish','do':'note','ts':'12:20',
   'note':K('완성. 영상 완성품: 룬 아버지의 탐욕스러운 사슬옷, 퀄리티 30% · 기폭제 퀄리티 30%, 룬 수호 929 / 주문 피해 39% · 지배 할당 · 룬 수호 30% / 모든 주문 스킬 +1(분열) · 주문 치명타 피해 29% · 시전 속도 24%.','Done. The video\'s armour: Runefather\'s Grasping Mail, 30% quality and 30% catalyst quality, 929 Runic Ward / 39% spell damage, Dominion allocated, 30% Runic Ward / +1 all spell skills (fractured), 29% spell crit damage, 24% cast speed.')},
 ],
})

# ---- Absent Amulet, sanctified spell +6 (반지깎는노인, youtu.be/Yi1u0LhJztI) ----
c='Amulets'
aspirit=textA('to Spirit','n','p'); aspell=textA('Level of all Spell Skills','n','s'); amaxQ=textA('to Maximum Quality','e','p')
amana=textA('to maximum Mana','n','p'); acast=textA('increased Cast Speed','n','s')
V7='https://www.youtube.com/watch?v=Yi1u0LhJztI'
R.append({
 'id':'absent-amulet-spell6', 'cls':c, 'base':base(c,'Absent Amulet'), 'ilvl':82, 'imp':[K('스킬 부여: 레벨 12 대마법사','Grants Skill: Level 12 Archmage'),K('접두어 속성 부여의 최대 개수 -1개\n접미어 속성 부여의 최대 개수 -1개','-1 Prefix Modifier allowed\n-1 Suffix Modifier allowed')], 'difficulty':5, 'budget':'high',
 'buildTags':[K('주문','Spell'),K('정신력','Spirit'),K('마나','Mana')], 'patch':'0.5', 'created':'2026-11-08',
 'author':K('반지깎는노인 영상 기반','Based on 반지깎는노인'),
 'source':{'url':V7, 'title':'주문 스킬레벨 +6 목걸이 만들기 [POE2] How to make +6 skill level amulet', 'channel':'반지깎는노인'},
 'title':K('주문 스킬 +3 · 정신력 · 마나 · 시전 속도','+3 spell skills, Spirit, Mana, cast speed'),   # 사용자 결정 11-13: 퀄리티 50%·축성 뺌
 'note':K('목표: 접두 = 정신력 +50(분열) + 마나 최대치 1티어, 접미 = 주문 스킬 +3 + 시전 속도 1티어, 쇳소리 기폭제 퀄리티 50%. 퀄리티 50%로 주문 +3이 +4가 되고, 축성이 1.5배로 붙으면 +6. 부재 목걸이는 접두·접미가 한 자리씩 적고(2/2) 매직 상태에서는 제작이 안 돼서 희귀에서 시작. 마나 1티어(레벨 82) 때문에 아이템 레벨 82 베이스. 히네코라의 머리카락으로 결과를 미리 보며 비싼 단계를 넘기는 게 핵심.',
          'Target: prefixes = fractured +50 Spirit + T1 maximum Mana; suffixes = +3 spell skills + T1 cast speed; 50% caster catalyst quality. At 50% quality +3 becomes +4, and a 1.5× sanctify makes it +6. Absent Amulets have one fewer prefix and suffix (2/2) and cannot be crafted while magic, so start from a rare. Item level 82 for T1 Mana (level 82). The key is previewing expensive steps with Hinekora\'s Lock.'),
 'start':{'rar':'magic','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'quality','kr':'퀄리티 48%','en':'Quality to 48%'},{'id':'spirit','kr':'정신력','en':'Spirit'},
           {'id':'fracture','kr':'정신력 분열','en':'Fracture Spirit'},{'id':'skill','kr':'주문 스킬 +3','en':'Spell skills +3'},{'id':'q50','kr':'퀄리티 50%','en':'Quality to 50%'},
           {'id':'prefix','kr':'마나 최대치','en':'Maximum Mana'},{'id':'suffix','kr':'시전 속도 (훼손)','en':'Cast speed (desecrated)'},{'id':'finish','kr':'성유 · 디바인 · 축성','en':'Anoint, Divine, sanctify'}],
 'nodes':[
  {'id':'b1','phase':'base','do':'base','cost':'base','ts':'2:20',
   'note':K('아이템 레벨 82 부재 목걸이.','An item level 82 Absent Amulet.')},
  {'id':'b1b','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'2:20','note':K('완벽한 제왕의 오브로 희귀. 부재 목걸이는 매직 상태에서 다른 화폐가 안 먹혀서 바로 희귀로 만듦.','Perfect Regal to rare; nothing else works on an Absent Amulet while magic.')},
  {'id':'b2','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':amaxQ},'ts':'3:00',
   'note':K('균열의 에센스로 최대 퀄리티 +20% (접두).','Essence of the Breach adds +20% Maximum Quality (prefix).')},
  {'id':'b3','phase':'quality','do':'quality','cur':'Sibilant_Catalyst','target':{'quality':40},'ts':'3:20',
   'note':K('쇳소리 기폭제로 40%까지.','Caster (Sibilant) catalysts to 40%.')},
  {'id':'b4','phase':'quality','do':'manual','cost':'vaal','target':{'setQuality':48},'label':K('바알 촉진시키는 주입기로 48%','Vaal Catalysing Infuser to 48%'),'ts':'3:30',
   'note':K('바알 촉진시키는 주입기로 한 번에 몇 %씩 올림. 영상 기준 46% 근처부터 타락할 확률이 커져서, 아무 옵션도 없는 지금 최대한 올려 둠(영상 48%). 남은 2%는 나중에 히네코라의 머리카락으로 미리 보고 올림.','Vaal Catalysing Infusers add a few % at a time. Corruption gets likely from about 46%, so push it now while nothing is on the item (48% in the video). The last 2% comes later with a Hinekora preview.')},
  {'id':'s1','phase':'spirit','do':'chaos','cur':'Chaos_Orb','target':{'gi':aspirit,'tmax':1,'removeGi':amaxQ},'fail':{'goto':'self'},'ts':'8:30',
   'note':K('카오스 오브로 정신력 +50(1티어). 최대 퀄리티는 이때 날아가도 됨(퀄리티 수치는 유지). 영상은 300개 안쪽.','Chaos for +50 Spirit (T1). Losing Maximum Quality here is fine; the quality value stays. Under 300 in the video.')},
  {'id':'s2','phase':'fracture','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'9:31',
   'note':K('접미에 아무 옵션 하나(에센스가 지울 자리).','Any suffix, for the essence to remove.')},
  {'id':'s3','phase':'fracture','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':amaxQ},'ts':'9:40',
   'note':K('우측 결정화의 징조 + 균열의 에센스: 접미 잡옵을 지우고 접두에 최대 퀄리티 +20%를 다시 붙임. 분열 후보를 늘리는 자리이기도 함.','Dextral Crystallisation + Essence of the Breach removes the junk suffix and puts +20% Maximum Quality back on a prefix.')},
  {'id':'s4','phase':'fracture','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'9:50',
   'note':K('접미에 아무 옵션 하나 더(영상은 모든 원소 저항).','One more suffix (all elemental resistances in the video).')},
  {'id':'s5','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'s'},'ts':'10:05',
   'note':K('남은 접미를 훼손(공개 안 함)으로 채워 옵션 4개. 훼손은 분열되지 않아 정신력 분열이 1/3.','Fill the last suffix with an unrevealed desecration: four modifiers. Desecrations cannot fracture, so Spirit is 1 in 3.')},
  {'id':'f1','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':aspirit}]},'extra':{'Hinekoras_Lock':4},'ts':'10:30',
   'after':{'keepOnly':[aspirit,'junk1']},
   'note':K('히네코라의 머리카락으로 분열 결과를 미리 봄. 정신력이 아니면 아이템을 바꾸고(영상은 소멸의 오브로 옵션 하나 지우고 다시 채움) 다시 머리카락. 영상은 모든 원소 저항·최대 퀄리티를 거쳐 약 4개째에 정신력 분열. 이후 분열 + 옵션 하나만 남김.','Preview the fracture with Hinekora\'s Lock. If it is not Spirit, change the item (the video annulled a line and refilled it) and lock again. The video saw all resistances and Maximum Quality first and got Spirit on about the fourth lock. Then keep the fracture plus one line.')},
  {'id':'k1','phase':'skill','do':'chaos','cur':'Chaos_Orb','target':{'gi':aspell,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'20:01',
   'after':{'keepOnly':[aspirit,aspell]},
   'note':K('카오스 오브로 주문 스킬 +3. 영상은 아주 빨리 나옴.','Chaos for +3 spell skills; it came very quickly in the video.')},
  {'id':'q1','phase':'q50','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'21:20',
   'note':K('접두에 아무 옵션 하나.','Any prefix.')},
  {'id':'q2','phase':'q50','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':amaxQ},'ts':'21:35',
   'note':K('균열의 에센스로 최대 퀄리티를 다시 붙여 50%까지 올릴 여유를 만듦(접두가 꽉 차 있어서 결정화의 징조 없이도 접두가 지워짐).','Essence of the Breach (prefixes full, no omen) brings Maximum Quality back so quality can reach 50%.')},
  {'id':'e1','phase':'q50','do':'manual','label':K('완벽한 유동체로 대마법사 20레벨','Perfect Flux: Archmage to level 20'),'ts':'22:32','extra':{'Perfect_Flux':1},
   'target':{'imp':[K('스킬 부여: 레벨 20 대마법사','Grants Skill: Level 20 Archmage'),K('접두어 속성 부여의 최대 개수 -1개\n접미어 속성 부여의 최대 개수 -1개','-1 Prefix Modifier allowed\n-1 Suffix Modifier allowed')]},
   'note':K('완벽한 유동체로 부여 스킬(대마법사)을 20레벨로. 영상은 히네코라의 머리카락 단계 전에 미리 해 둠(아이템이 바뀌면 예측이 사라지니까).','A perfect liquid raises the granted skill (Archmage) to level 20. The video does it before the Hinekora steps, since any change wipes the preview.')},
  {'id':'q3','phase':'q50','do':'manual','cost':'vaal','target':{'setQuality':50},'extra':{'Hinekoras_Lock':1},'label':K('히네코라의 머리카락 + 바알 촉진시키는 주입기로 50%','Hinekora + Vaal Catalysing Infuser to 50%'),'ts':'25:30',
   'note':K('타락 위험 구간이라 히네코라의 머리카락으로 결과를 보고 주입기. 50%가 되면 더는 머리카락을 안 써도 됨. 머리카락은 소켓·유동체처럼 아이템을 바꾸는 작업을 다 끝낸 뒤에 써야 예측이 유지됨.','This is corruption territory, so preview with Hinekora before the infuser. Once at 50% no more locks are needed. Use the lock only after sockets, liquids and anything else that changes the item, or the preview is lost.')},
  {'id':'m1','phase':'prefix','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'s','dropGi':amaxQ},'ts':'27:01',
   'note':K('최대 퀄리티는 에센스로 붙은 제작 옵션이라 결정화로는 안 지워짐. 좌측 강령술의 징조 + 빗장뼈로 최대 퀄리티 자리를 날리고, 접두 제거와 반복해 훼손(장막)을 접미로 내려 둠. 이 과정에서 영상이 미리 붙였던 시전 속도도 정리됨.','Maximum Quality is a crafted essence mod, so Crystallisation will not remove it. Sinistral Necromancy + a Collarbone knocks it off; repeat with prefix removal until the desecration (the veil) sits on a suffix. The cast speed the video added earlier goes in this process.')},
  {'id':'m2','phase':'prefix','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':amana,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}},'ts':'28:31',
   'note':K('상위 엑잘티드 오브로 접두에 마나 최대치 1티어(180—189, 레벨 82). 아니면 좌측 소멸의 징조 + 소멸의 오브로 지우고 다시. 영상은 금방 나옴.','A Greater Exalted Orb on the prefix for T1 maximum Mana (180–189, level 82). On a miss, Sinistral Annulment and retry. It came quickly in the video.')},
  {'id':'c1','phase':'suffix','do':'reveal','target':{'reveal':{'anyOf':[{'gi':acast,'tmax':1}]},'side':'s','bone':'Preserved_Collarbone'},'unknownW':True,'fail':{'goto':'self','via':LIGHT},'ts':'34:05',
   'note':K('접미 훼손을 영혼의 우물에서 공개해 시전 속도 1티어(25—28%). 아니면 빛의 징조 + 소멸의 오브로 지우고 우측 강령술의 징조 + 빗장뼈로 다시 훼손 후 공개. 목걸이 시전 속도 가중치는 아직 확인된 데이터가 없어서 확률은 표시하지 않음.','Reveal the suffix desecration at the Well of Souls for T1 cast speed (25–28%). On a miss, Light + Annulment, desecrate again with Dextral Necromancy + a Collarbone, and reveal again. We have no confirmed weight for cast speed on amulets, so no odds are shown.')},
  {'id':'e2','phase':'finish','do':'manual','label':K('성유: 자로크의 선물 할당','Anoint: Zarokh\'s Gift'),'ts':'37:45',
   'target':{'anoint':K('자로크의 선물','Zarokh\'s Gift')},
   'note':K('성유로 자로크의 선물을 붙임(희귀 주얼 홈 하나 추가). 축성 전에 할 것.','Anoint Zarokh\'s Gift (adds a rare jewel socket). Do it before sanctifying.')},
  {'id':'e3','phase':'finish','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':acast}},'fail':{'goto':'self'},'extra':{'Hinekoras_Lock':1},'ts':'38:31',
   'note':K('축성은 지금 수치의 ±20%라 먼저 신성한 오브로 수치를 올려 둠. 히네코라의 머리카락으로 결과를 보고 시전 속도 28(최대)·마나 최대 근처일 때 확정. 영상은 시전 42%(퀄리티 반영)·마나 185로 둘 다 최대.','Sanctifying moves values ±20% from where they are, so Divine first. Preview with Hinekora and commit at 28 cast speed (max) with Mana near max. The video got 42% cast speed (with quality) and 185 Mana.')},
  {'id':'e4','phase':'finish','do':'manual','label':K('축성 (주문 +4 → +6)','Sanctify (+4 → +6 spell)'),'ts':'41:06',
   'target':{'sanctify':True,'vals':{str(aspell):K('모든 주문 스킬 레벨 +6','+6 to Level of all Spell Skills'),str(acast):K('시전 속도 48% 증가','48% increased Cast Speed')}},
   'note':K('축성할지 여부: 축성하면 수치가 한 번 더 바뀌지만 미러를 뜰 수 없고 이후 수정 불가. 축성한다면 순서는 퀄리티 50% → 성유 → 디바인 → 축성. 퀄리티 50%로 주문 +4인 상태에서 1.5배가 붙으면 +6. 영상은 바알 오브(변화 없음) 뒤 축성 한 번에 +6, 시전 속도 48%.','Whether to sanctify: it rerolls values once more but the item can no longer be mirrored or changed. If you do: quality 50% → anoint → Divine → sanctify. At +4 (from 50% quality), a 1.5× roll makes +6. The video used a Vaal Orb (no change), then hit +6 and 48% cast speed on the first sanctify.')},
  {'id':'e9','phase':'finish','do':'note','ts':'42:01',
   'note':K('완성. 영상 완성품: 부재 목걸이, 퀄리티(시전) 50%, 자로크의 선물 할당, 대마법사 20레벨 / 정신력 +50(분열) · 마나 최대치 +172(1티어) / 모든 주문 스킬 +6 · 시전 속도 48%, 축성.','Done. The video\'s amulet: Absent Amulet, 50% caster quality, Zarokh\'s Gift anointed, Archmage level 20 / +50 Spirit (fractured), +172 maximum Mana (T1) / +6 all spell skills, 48% cast speed, sanctified.')},
 ],
})
exec(open('/home/claude/poe2data/scripts/recipes_batch2.py').read())
exec(open('/home/claude/poe2data/scripts/recipes_batch3.py').read())
exec(open('/home/claude/poe2data/scripts/recipes_batch4.py').read())
import glob as _glob
for _f in sorted(_glob.glob('/home/claude/poe2data/scripts/recipes_v5_*.py')): exec(open(_f).read())   # one file per video recipe
# A finished item with a fractured line starts from the bought fractured base (fracture + one junk line); the steps up to the
# fracture and its clean-up become the starting state (사용자 확정 2026-11-09).
def _fb(cut, mods, kr, en, quality=None, runes=None):
    return {'cut':cut, 'mods':mods, 'note':K(kr,en), 'quality':quality, 'runes':runes}
KOLR_=K('콜르의 사냥',"Kolr's Hunt")
FRSTART = {
 'mirror-bow-video': _fb(('s2','f2'), [{'gi':17,'tmax':1,'fr':True},{'gi':7,'tmax':1},{'unrev':'p'}], '치명타 확률 분열 + 물리 피해 % 1티어 + 미공개 훼손 접두.', 'Fractured crit chance + T1 % physical + an unrevealed desecrated prefix.', 30),
 'absent-amulet-video': _fb(('a2','a4'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1개.', 'Fractured Spirit plus one junk line.'),
 'breach-ring-video': _fb(('c2','c4b'), [{'gi':15,'tmax':1,'fr':True},{'junk':'s'}], '공격 시 원소 피해 1티어 분열(화염·냉기·번개 아무거나) + 잡옵 1개.', 'A fractured T1 elemental attack flat (any element) plus one junk line.'),
 'helmet-armour-sl': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1개.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'sihan-highend-boots-v2': _fb(('h2','f4'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '방어도 % 증가 분열 + 잡옵 1개.', 'Fractured % increased armour plus one junk line.', 26),
 'sihan-highend-boots-v2-bal': _fb(('h2','f4'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '방어도 % 증가 분열 + 잡옵 1개.', 'Fractured % increased armour plus one junk line.', 26),
 'sihan-highend-boots-v2-ess': _fb(('h2','f4'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '방어도 % 증가 분열 + 잡옵 1개.', 'Fractured % increased armour plus one junk line.', 26),
 'saveq-absent-amulet-v2': _fb(('r0','f4'), [{'gi':25,'tmax':1,'fr':True},{'junk':'p'}], '치명타 피해 보너스 1티어 분열 + 잡옵 1개.', 'Fractured T1 critical damage bonus plus one junk line.'),
 'saveq-absent-amulet-v2-bal': _fb(('r0','f4'), [{'gi':25,'tmax':1,'fr':True},{'junk':'p'}], '치명타 피해 보너스 1티어 분열 + 잡옵 1개.', 'Fractured T1 critical damage bonus plus one junk line.'),
 'saveq-absent-amulet-v2-ess': _fb(('r0','f4'), [{'gi':25,'tmax':1,'fr':True},{'junk':'p'}], '치명타 피해 보너스 1티어 분열 + 잡옵 1개.', 'Fractured T1 critical damage bonus plus one junk line.'),
 'helmet-armour-sl-v2': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1개.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'helmet-armour-sl-v2-bal': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1개.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'helmet-armour-sl-v2-ess': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1개.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'gold-amulet-6line': _fb(('g2','g3'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1개.', 'Fractured Spirit plus one junk line.'),
 'grasping-mail-spell1': _fb(('m2','f1'), [{'gi':140,'fr':True},{'junk':'s'}], '룬 아버지 단계까지 올린 베이스(갑옷·기폭제 퀄리티 30%). 모든 주문 스킬 레벨 +1 분열 + 잡옵 1개.', "A Runefather base (armour and catalyst quality 30%) with fractured +1 spell skills plus one junk line.", 30),
 'absent-amulet-spell6': _fb(('b1b','f1'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1개.', 'Fractured Spirit plus one junk line.'),
 'mazbro-caster-ring': _fb(('r1b','r4'), [{'gi':34,'tmax':1,'fr':True},{'junk':'p'}], '시전 속도 분열 + 잡옵 1개.', 'Fractured cast speed plus one junk line.'),
 'mazbro-caster-amulet': _fb(('a2','a3'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1개.', 'Fractured Spirit plus one junk line.'),
 'mazbro-bis-chest': _fb(('c2','c6'), [{'gi':15,'tmax':1,'fr':True}], '정신력 분열(나머지 옵션은 정리한 상태).', 'Fractured Spirit, everything else cleared.'),
 'mazbro-proj-gloves': _fb(('g2','g7'), [{'gi':81,'fr':True},{'junk':'p'}], '콜르의 사냥을 장착한 상태로 모든 투사체 스킬 레벨 +2 분열 + 잡옵 1개.', "Kolr's Hunt socketed: fractured +2 projectile skills plus one junk line.", 30, [KOLR_]),
 'diztoh-iceshot-bow': _fb(('w2','w6'), [{'gi':7,'tmax':2,'tmin':2,'fr':True},{'junk':'p'}], '물리 피해 % 2티어 분열 + 잡옵 1개.', 'Fractured T2 % physical damage plus one junk line.'),   # 영상 완성품 = 165%(2티어) 분열
 'diztoh-crit-helmet-v2': _fb(('h2','h7'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '퀄리티 20%. 회피·에너지 보호막 최대치 1티어 분열(회피 +(79—94), 에너지 보호막 최대치 +(26—29)) + 잡옵 1개.', 'Quality 20%. Fractured T1 flat evasion and energy shield (+(79—94) evasion, +(26—29) maximum energy shield) plus one junk line.', 20),
 'diztoh-crit-helmet-v2-bal': _fb(('h2','h7'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '퀄리티 20%. 회피·에너지 보호막 최대치 1티어 분열(회피 +(79—94), 에너지 보호막 최대치 +(26—29)) + 잡옵 1개.', 'Quality 20%. Fractured T1 flat evasion and energy shield (+(79—94) evasion, +(26—29) maximum energy shield) plus one junk line.', 20),
 'diztoh-crit-helmet-v2-ess': _fb(('h2','h7'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '퀄리티 20%. 회피·에너지 보호막 최대치 1티어 분열(회피 +(79—94), 에너지 보호막 최대치 +(26—29)) + 잡옵 1개.', 'Quality 20%. Fractured T1 flat evasion and energy shield (+(79—94) evasion, +(26—29) maximum energy shield) plus one junk line.', 20),
 'diztoh-socket-gloves': _fb(('d2','d6'), [{'gi':82,'fr':True},{'gi':8,'tmax':2},{'gi':57,'crafted':True},{'unrev':'p'}], '콜르의 사냥을 장착한 상태로 모든 투사체 스킬 레벨 +2 분열 + 에너지 보호막 최대치 + 희귀도(상위 풍요의 에센스) + 미공개 훼손 접두.', "Kolr's Hunt socketed: fractured +2 projectile skills, flat energy shield, rarity (Greater Essence of Opulence) and an unrevealed desecrated prefix.", None, [KOLR_]),
 'mazbro-sceptre': _fb(('z2','z6'), [{'gi':10,'tmax':1,'fr':True},{'junk':'s'}], '동료 피해 1티어 분열 + 잡옵 1개.', 'Fractured T1 ally damage plus one junk line.'),
 'mazbro-spell5-amulet': _fb(('z2','z6'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 +50 분열 + 잡옵 1개.', 'Fractured +50 Spirit plus one junk line.'),
 'sl-flamewave-ring': _fb(('g2','g4'), [{'gi':7,'tmax':1,'fr':True},{'junk':'p'}], '모든 원소 저항 1티어 분열 + 잡옵 1개.', 'Fractured T1 all elemental resistances plus one junk line.'),
}
def _own_prep(_r):
    # 플로우차트가 준비 구역에 작업 상자를 가진 레시피(노멀 베이스 → 분열까지 그림)는 옛 준비 과정을 자르지도 더하지도 않음(2026-11-12) —
    # 시뮬 합계에 준비 비용이 이미 들어 있어 r.prep을 두면 엔진 합계가 두 번 셈. 단계는 graph2recipe가 플로우차트에서 읽음
    _f = f"{D}sim/{_r.get('tierGroup') or _r['id']}.json"
    if not os.path.exists(_f): return False
    import sys as _s0; _s0.path.insert(0,'/home/claude/poe2data/scripts'); import graph2recipe as _g0
    return _g0.has_prep(json.load(open(_f)))
FRSTART_SKIP=[]
for _r in R:
    _c = FRSTART.get(_r['id']) or (FRSTART.get(_r['tierGroup'][:-3]) if _r.get('tierGroup','').endswith('-v2') and _r['tierGroup'] not in FRSTART else None)   # grade recipes copied from an original in this table
    if not _c: continue
    if _own_prep(_r): FRSTART_SKIP.append(_r['id']); continue
    _ids = [n['id'] for n in _r['nodes']]; _a, _b = _ids.index(_c['cut'][0]), _ids.index(_c['cut'][1])
    _gone = set(_ids[_a:_b+1])
    # keep the cut steps as the folded "base preparation" (shown under the base step, not counted in the totals)
    import copy as _copy
    _pn = _copy.deepcopy(_r['nodes'][:_b+1]); _pu = {n.get('phase') for n in _pn}
    _r['prep'] = {'start': _copy.deepcopy(_r.get('start') or {'rar':'normal','mods':[]}), 'nodes': _pn,
                  'phases': [ph for ph in _copy.deepcopy(_r.get('phases') or []) if ph['id'] in _pu]}
    if _r.get('quality'): _r['prep']['quality'] = _r['quality']
    _r['nodes'] = _r['nodes'][:_a] + _r['nodes'][_b+1:]
    _st = {'rar':'rare', 'mods':_c['mods']}
    if _c['quality']: _st['quality'] = _c['quality']
    _runes = _c['runes'] or (_r.get('start') or {}).get('runes')
    if _runes: _st['runes'] = _runes
    _r['start'] = _st; _r.pop('quality', None)
    _b0 = _r['nodes'][0]; _b0['note'] = _c['note']
    for _n in _r['nodes']:
        _f = _n.get('fail') or {}
        if _f.get('goto') in _gone: _f['goto'] = 'restart'
        if _f.get('lost') in _gone: _f.pop('lost')
        if _n.get('fallbackFor') in _gone or (_n.get('branch') or {}).get('of') in _gone: raise Exception((_r['id'], _n['id']))
    _used = {n.get('phase') for n in _r['nodes']}
    if _r.get('phases'): _r['phases'] = [ph for ph in _r['phases'] if ph['id'] in _used]
print('FRSTART skipped (flowchart has its own prep):', FRSTART_SKIP)
exec(open('/home/claude/poe2data/scripts/notes_short.py').read())
# "{#id}" in a step's text becomes that step's number, so cutting steps never leaves stale references
import re as _re
def _fcread_later(_r):   # 플로우차트에서 단계를 다시 읽을 레시피: 단계 번호가 바뀌니 {#id}는 읽은 뒤에 채움(2026-11-12)
    _sid=_r.get('tierGroup') or _r['id']
    return os.path.exists(f"{D}sim/{_sid}.json") and os.path.exists(f"/home/claude/poe2data/scripts/graphs/{_sid}.json")
for _r in R:
    _no = {n['id']:i+1 for i,n in enumerate(_r['nodes'])}
    def _fix(v):
        if isinstance(v, str): return _re.sub(r'\{#(\w+)\}', lambda m: str(_no[m.group(1)]), v)
        if isinstance(v, dict): return {k:_fix(x) for k,x in v.items()}
        if isinstance(v, list): return [_fix(x) for x in v]
        return v
    if _fcread_later(_r): _r['_no0'] = _no
    else: _r['nodes'] = _fix(_r['nodes'])
    if _r.get('prep'):
        _no = {n['id']:i+1 for i,n in enumerate(_r['prep']['nodes'])}
        _r['prep']['nodes'] = _fix(_r['prep']['nodes'])
# side omens that do nothing: the other side is already full, so the slam/desecration can only land on this side anyway
REDUNDANT={('gold-amulet-6line','p4'),('gold-amulet-6line','d1'),('grasping-mail-spell1','p0'),('grasping-mail-spell1','p2'),('grasping-mail-spell1','p4'),
 ('absent-amulet-spell6','s4'),('absent-amulet-spell6','m2'),('mazbro-caster-ring','r12'),('mazbro-caster-amulet','a12'),('mazbro-bis-chest','c12'),('mazbro-bis-chest','c10'),('mazbro-bis-chest','c13'),
 ('diztoh-iceshot-bow','w11'),('diztoh-iceshot-bow','w13')}
import re as _re
for _r in R:
    for _n in _r['nodes']:
        if (_r['id'],_n['id']) in REDUNDANT and _n.get('omens'):
            _n['omens']=[o for o in _n['omens'] if not _re.search(r'(Sinistral|Dextral)_(Exaltation|Necromancy)',o)]
            if not _n['omens']: del _n['omens']
# A v5 file that rewrites an older recipe of the same video replaces it (REPLACES = {new id: old id}).
exec(open('/home/claude/poe2data/scripts/difficulty.py').read())   # 난이도 재산정 표(시도량 기준)
for _r in R:
    if _r['id'] in DIFFSET: _r['difficulty']=DIFFSET[_r['id']]
# DIFFSET 키는 옛 id라 새 등급 레시피(-v2·-v2-bal·-v2-ess)에는 붙지 않음 — 값은 생성기(작업자)가 정한 그대로 두고 다른 것만 알림(2026-11-13 S3 3·15번: 사용자 결정 대기)
_dm = [(_r['id'], _r.get('difficulty'), DIFFSET[_k]) for _r in R for _k in [_re.sub(r'-v2(-bal|-ess)?$', '', _r['id'])] if _k != _r['id'] and _k in DIFFSET and DIFFSET[_k] != _r.get('difficulty')]
if _dm: print('difficulty differs from DIFFSET (kept):', ', '.join(f'{a} {b}≠{c}' for a, b, c in _dm))
# grades by difficulty (사용자 확정 2026-11-10): 극한(5) = High-end only, 전문가(4) = High-end + Balance, 보통·어려움(2~3) = Balance + Essential, 쉬움 이하(≤1) = Essential only
_gd={}
for x in R:   # the group's difficulty: its High-end recipe's, else its other grades'
    if x.get('tierGroup'): _gd[x['tierGroup']] = x.get('difficulty',0) if x.get('tier')=='high' else max(_gd.get(x['tierGroup'],0), x.get('difficulty',0)) if x['tierGroup'] not in _gd or not any(y.get('tier')=='high' and y.get('tierGroup')==x['tierGroup'] for y in R) else _gd[x['tierGroup']]
def _gkeep(d): return ('high',) if d>=5 else ('high','bal') if d==4 else ('bal','ess') if d>=2 else ('ess',)
R[:]=[x for x in R if not (x.get('tierGroup') and x.get('tier') not in _gkeep(_gd.get(x['tierGroup'],0)))]
REPLACES={'sihan-chayula-amulet-v2-bal':'sihan-chayula-amulet','sihan-chayula-gloves-v2-bal':'sihan-chayula-gloves','sihan-chayula-helmet-v2-bal':'sihan-chayula-helmet','sihan-chayula-wand-v2-bal':'sihan-chayula-wand','sihan-attack-flat-ring-v2-bal':'sihan-attack-flat-ring','sihan-chayula-ring-v2':'sihan-chayula-ring','sihan-proj-gloves-v2':'sihan-proj-gloves','diztoh-budget-crossbow':'diztoh-grenade-crossbow','diztoh-crit-helmet-v2':'diztoh-crit-helmet','helmet-armour-sl-v2':'helmet-armour-sl','sihan-highend-boots-v2':'sihan-highend-boots','diztoh-rarity-ring-v2':'diztoh-rarity-ring','saveq-absent-amulet-v2':'saveq-absent-amulet','farmer-budget-armour-v2':'farmer-budget-armour','farmer-starter-staff-v2':'farmer-starter-staff','ragna-ashot-bow-v2-bal':'ragna-ashot-bow','sane-resist-belt-v2-bal':'sane-resist-belt','diztoh-budget-mace-v2-bal':'diztoh-budget-mace','lilbotq-budget-boots-v2-bal':'lilbotq-budget-boots','icesly-budget-wand-v2-bal':'icesly-budget-wand','diztoh-budget-mace-v2-ess':'diztoh-budget-2h-mace','diztoh-es-helmet-v2-bal':'diztoh-es-helmet','belton-plus8-wand-v2-bal':'belton-plus8-wand','lilbotq-armour-shield-v2-bal':'lilbotq-armour-shield','diztoh-vile-robe-v2-bal':'diztoh-vile-robe','diztoh-talisman-v2-bal':'diztoh-talisman','sihan-chayula-sceptre-v2-bal':'sihan-chayula-sceptre','diztoh-budget-crossbow-v2-bal':'diztoh-budget-crossbow','diztoh-onehand-mace-v2-bal':'diztoh-onehand-mace','saveq-alloy-focus-v2-bal':'saveq-alloy-focus','tankjung-kitava-shield-v2-bal':'tankjung-kitava-shield','ragna-spell4-amulet-v2-bal':'ragna-spell4-amulet','noble-visceral-quiver-v2':'noble-visceral-quiver','sihan-highend-helmet-v2':'sihan-highend-helmet','barricade-quarterstaff-v2':'barricade-quarterstaff','diztoh-endgame-quarterstaff-v2':'diztoh-endgame-quarterstaff','lilbotq-emerald-v2-bal':'lilbotq-emerald','zenm-timelost-sapphire-v2-bal':'zenm-timelost-sapphire','diztoh-5mod-emerald-v2-bal':'diztoh-5mod-emerald','diztoh-5mod-sapphire-v2-bal':'diztoh-5mod-sapphire','sl-5mod-jewel-v2-bal':'sl-5mod-jewel','vodnarg-timelost-emerald-v2-bal':'vodnarg-timelost-emerald','lilbotq-boots-v2-bal':'lilbotq-boots','mazbro-caster-ring-v2-bal':'mazbro-caster-ring','diztoh-as-spear-v2-bal':'diztoh-as-spear','diztoh-socket-gloves-v2-bal':'diztoh-socket-gloves','seek-cyclone-boots-v2-bal':'seek-cyclone-boots','diztoh-as-spear-v2-ess':'diztoh-twister-spear','mastert-timelost-emerald-v2':'mastert-timelost-emerald','chiba-timelost-emerald-v2':'chiba-timelost-emerald','noble-timelost-sapphire-v2':'noble-timelost-sapphire','mazbro-proj-gloves-v2':'mazbro-proj-gloves','sl-flamewave-staff-v2':'sl-flamewave-staff','mazbro-caster-amulet-v2':'mazbro-caster-amulet','mazbro-spell5-amulet-v2':'mazbro-spell5-amulet','gold-amulet-6line-v2':'gold-amulet-6line','absent-amulet-video-v2':'absent-amulet-video','sl-flamewave-ring-v2':'sl-flamewave-ring','breach-ring-video-v2':'breach-ring-video','saveq-focus-v2':'saveq-focus','sl-proj7-gloves-v2':'sl-proj7-gloves','diztoh-iceshot-bow-v2':'diztoh-iceshot-bow','grasping-mail-spell1-v2':'grasping-mail-spell1','mazbro-bis-chest-v2':'mazbro-bis-chest','mirror-bow-video-v2':'mirror-bow-video','absent-amulet-spell6-v2':'absent-amulet-spell6','mazbro-sceptre-v2':'mazbro-sceptre','xeno-phys-crossbow-v2':'xeno-phys-crossbow','easybabi-spiny-talisman-v2':'easybabi-spiny-talisman','sl-blacksteel-gauntlets-v2':'sl-blacksteel-gauntlets','breach-ring-phys-v2-bal':'breach-ring-phys','banzino-mirror-staff-v2':'banzino-mirror-staff','fubgun-quiver-v2-bal':'fubgun-quiver','fubgun-phys-bow-v2-bal':'fubgun-phys-bow','fubgun-crit-bow-v2-bal':'fubgun-crit-bow','fubgun-proj-amulet-v2-bal':'fubgun-proj-amulet','fubgun-es-helmet-v2-bal':'fubgun-es-helmet','bigdaddy-lightning-wand-v2-bal':'bigdaddy-lightning-wand','unstoppable-vile-robe-v2':'unstoppable-vile-robe','unstoppable-slipstrike-vest-v2':'unstoppable-slipstrike-vest'}
_ids={x['id'] for x in R}|{x['tierGroup'] for x in R if x.get('tierGroup')}   # a group whose High-end was dropped still replaces its old recipe
R[:]=[x for x in R if not any(o==x['id'] and (n in _ids or _re.sub(r'-(bal|ess)$','',n) in _ids) for n,o in REPLACES.items())]   # 2026-11-11: a grade dropped by policy 30 (e.g. -bal of an easy item) still replaces the old recipe
# policy 22: base price (Divine Orbs) from scripts/base_prices.py; None = not known yet
exec(open('/home/claude/poe2data/scripts/base_prices.py').read())
for _r in R:
    if BASEPRICE.get(_r['id']): _r['basePrice'] = BASEPRICE[_r['id']]
print('base price missing:', sum(1 for _r in R if not _r.get('basePrice')), 'of', len(R))
import sys as _sys; _sys.path.insert(0,'/home/claude/poe2data/scripts'); import graph2recipe as _g2r
FCREAD_OFF=set()
PREP_DROPPED=[]
# 플로우차트 읽기 레시피의 단계 시각은 옛 단계 레시피(같은 id 상자, 베이스는 옛 베이스 단계)에서 옴 — 틀린 곳만 여기서 고침(그래프 id → {상자 id 또는 'base': 시각})
FC_TS={'mazbro-proj-gloves-v2': {'base':'2:00','pk':'4:22','p1':'4:36','p2':'4:50','p3':'5:02','p3x':'5:05','p4':'5:15','p5':'6:55','p6':'7:03','p7':'8:45','xj':'7:10','p8':'12:15','pA':'8:06','k11':'15:56','kz':'13:40','k12':'15:58','ka':'16:00','kb':'16:03','kc':'13:30','kx1':'10:58','kx2':'10:58','kx3':'11:30','kx4':'11:30','k13':'17:35','k14':'17:50','k14x':'17:56'}}   # 2026-11-12 W1 영상 전체 재대조(화면 캡처 근거 scratchpad review/W1-mazbro-gloves/timeline.md) — 새 플로우차트 상자 id별 영상 시각   # 플로우차트 읽기를 끈 레시피(문제가 있을 때만)
FC_TS['diztoh-vile-robe-v2']={'base':'2:05','p1':'2:23','v2':'3:19','v3':'3:35','v3x':'4:20','v4':'6:10','v5':'4:55','v6':'8:56','v6a':'9:34','v6b':'9:58','v6c':'10:27','v7':'11:30','v8a':'12:29','v8':'13:20','v8b':'14:36'}   # 2026-11-12 W4 영상 전체 재대조(화면 캡처 근거 scratchpad review/W4-vile-robe/timeline.md) — v8c·v8x는 영상에 없음
FC_TS['tankjung-kitava-shield-v2']={'base':'14:28','m1':'15:52','m2':'15:52','m2x':'15:52','r1':'16:44','r2':'16:44','f1':'16:44','f2':'17:14','xj':'17:14','f4':'17:24','t2':'17:24','t3':'17:54','t4':'17:54','t4x':'17:54','t5':'19:04','t6':'19:04','t7':'19:08'}   # 2026-11-12 W5 영상 전체 재대조(슬라이드가 바뀌는 시각, 근거 scratchpad review/W5-kitava-shield/timeline.md)
FC_TS['diztoh-iceshot-bow-v2']={'base':'0:00','m1':'0:00','m2':'0:30','m1x':'0:30','m3':'0:46','e0':'0:50','f1':'1:05','f2':'1:21','xj':'1:05','f4':'1:26','c1':'1:30','e1':'4:34','e1w':'4:46','al':'5:26','r2':'6:10','d1':'7:00','d2':'8:20','l1':'9:12','l2':'10:05','l3':'10:10','x1':'15:12','x2':'15:43','x3':'18:28'}   # 2026-11-12 W3 영상 전체 재대조(근거 scratchpad review/W3-iceshot-bow/timeline.md), e1s는 영상에 없음
FC_TS['sihan-proj-gloves-v2']={'base':'11:45','pk':'11:58','q1':'11:58','q1x':'12:08','q2':'12:40','q3':'13:01','q4':'13:06','q5':'13:16','q6':'13:30','xj':'13:35','q7':'14:24','c1':'15:24','kz':'18:54','c2':'15:34','c3':'15:44','c4':'16:54','e1':'22:31','ec':'18:00','e2':'22:31','e2m':'23:12','e2e':'23:36','e2b':'22:58','e2l':'23:03','d1':'23:58','d2':'25:42'}   # 2026-11-12 W10 영상 전체 재대조(근거 scratchpad review/W10-sihan-gloves/timeline.md) — 성공 회차 22:26~26:42, d1n·d2x는 영상에 없음
FC_TS['sihan-highend-helmet-v2']={'base':'10:40','p1':'11:28','p1x':'11:35','p2':'11:40','p3':'12:15','p4':'12:32','p5':'13:46','xj':'14:00','p6':'14:02','s1':'17:01','kz':'16:40','k1':'17:34','k2':'17:38','k3':'17:48','fx':'18:35','q1':'18:52','q2':'19:02','q3':'19:14','q3x':'19:30','q3y':'19:40','q4':'20:18','q5':'22:00','q5x':'23:56','q6':'24:02'}   # 2026-11-12 W8 영상 전체 재대조(근거 scratchpad review/W8-sihan-helmet/timeline.md) — q3x·q3y는 영상 설명(19:30~20:00)만, 성공 회차에는 없음
FC_TS['grasping-mail-spell1-v2']={'base':'7:58','c1':'10:09','s1':'10:12','w1':'10:12','r1':'10:11','pc':'10:28','p1':'10:31','p2':'11:25','p3':'11:28','d1':'11:40','rv':'11:43','rvx':'11:52'}   # 2026-11-13 W11 영상 전체 재대조
FC_TS['sl-blacksteel-gauntlets-v2']={'base':'6:12','pk':'6:12','m1':'6:12','m1x':'6:12','m2':'6:12','m2x':'6:12','m2y':'6:12','m3':'6:12','m4':'6:12','m5':'6:12','xs':'6:13','xj':'6:12','m6':'6:13','k1':'6:13','k2':'6:13','k2x':'6:13','k5':'6:13','k6':'6:13','k6x':'6:13','k3':'6:13','k3x':'6:13','k4':'6:13'}   # 2026-11-13 W13 슬라이드(6:10~6:22) 재대조
FC_TS['mazbro-sceptre-v2']={'base':'2:00','p1':'2:10','p2':'2:25','p2x':'4:05','p3':'8:24','p4':'10:40','pf':'11:35','xj':'11:35','pc':'23:30','r1':'25:50','c1':'41:49','e1':'41:51','e1x':'30:00','s1':'57:52','aL':'57:40','mA':'57:20','b2':'57:45','b3':'57:45','da':'51:22'}   # 2026-11-13 W16 영상 전체 재대조 — e1x는 실패 회차 시각
FC_TS['sl-proj7-gloves-v2']={'base':'5:00','pk':'5:46','m1':'5:55','m2':'6:25','m2x':'6:30','m3':'6:55','m4':'9:45','m5':'9:15','xj':'9:30','m6':'9:50','r1':'5:46','c1':'9:50','e1':'10:20','e1x':'10:45','e2':'12:18','kz':'11:41','s1':'12:33','mA':'12:44','mB':'12:50','mL':'13:04','a1':'15:53','sR':'4:47','d1':'16:11','d2':'16:32','d2x':'17:20'}   # 2026-11-13 W14 — r1은 영상에서 분열 전 장착, sR은 영상에 없음
FC_TS['xeno-phys-crossbow-v2']={'base':'1:20','t1':'1:23','t2x':'1:26','t2':'1:40','r1':'1:50','d0':'1:59','sd':'2:04','f0':'2:54','xj':'2:54','hc':'2:58','c1':'3:04','e1':'4:24','b1':'4:50','rv':'5:32','rvx':'5:02','w1':'5:44','w1p':'5:50','s2':'6:20','w2':'6:28','s3':'7:38','w3':'9:54','f1':'8:06','f2':'8:50','f3':'9:08','f3x':'8:22'}   # 2026-11-13 W17 자막 없음 — f1~f3은 사용자 확정 순서라 영상 시각이 앞섬
FC_TS['mirror-bow-video-v2']={'base':'8:00','pt':'8:20','pa':'9:30','px':'9:30','pr':'10:18','pv':'10:55','pd':'11:52','pf':'13:32','xj':'13:00','pc':'15:00','k1':'15:45','k2':'19:01','k3':'21:55','k4':'20:58','k4w':'21:35','q1':'23:30','q1w':'23:42','u1':'25:05','u2':'25:25','u3':'26:15','u4':'28:02','u5':'28:20','u6':'28:24','z1':'31:20','z2':'31:27','z3':'31:35','z3x':'32:20'}   # 2026-11-13 W15 — 성공 회차 = 독사의 비, k4x는 영상에 없음
FC_TS['chiba-timelost-emerald-v2']={'base':'4:05','b0':'4:05','p1':'4:30','pf':'4:46','pc':'5:13','c2':'5:34','c3':'5:44','c4':'6:08','c5':'6:09','c6':'9:26','c6x':'9:13','c7':'10:25','c8':'10:34','c9':'11:00','c10':'11:26'}   # 2026-11-13 W24 영상 전체 재대조
FC_TS['mastert-timelost-emerald-v2']={'base':'5:00','pc':'5:47','c1':'7:50','e1':'8:05','l1':'8:52','d1':'10:05','r1':'13:52','r1x':'12:50','x1':'15:21','e2':'15:26','c2':'21:58','l2':'22:13'}   # 2026-11-13 W23 — l1x는 영상에 없음
FC_TS['sihan-highend-boots-v2']={'base':'7:20','m1':'8:13','m1x':'8:38','m2':'8:19','r1':'8:50','f1':'9:03','rd':'9:39','f2':'9:49','xj':'9:49','f4':'10:00','s1':'10:20','s2':'10:27','sf':'10:54','s2x':'11:24','s0':'11:24','p1':'13:38','q1':'13:42','q4':'13:50','q4b':'14:20','q4l':'14:20','p8m':'15:30','p3':'16:00','p3x':'16:24','p2':'16:30'}   # 2026-11-13 W19 — q4b·q4l은 14:00~14:45 설명 시각
FC_TS['sihan-highend-boots-v2-bal']=FC_TS['sihan-highend-boots-v2']
FC_TS['barricade-quarterstaff-v2']={'base':'4:52','q1':'5:45','q2':'6:28','t1':'7:36','r1':'7:42','a1':'7:50','c0':'8:02','e0':'9:35','e0b':'9:35','d0':'9:35','f0':'10:00','xj':'10:02','hc':'10:36','c1':'10:36','b1':'12:02','rv':'13:06','rvx':'12:50','p1':'14:50','p2':'15:42','p4':'17:28','p5':'17:39','p5x':'19:32'}   # 2026-11-13 W21 — 10:05~10:36 편집
FC_TS['barricade-quarterstaff-v2-bal']=FC_TS['barricade-quarterstaff-v2']
FC_TS['noble-timelost-sapphire-v2']={'base':'1:38','p1':'2:00','p2':'2:02','pf':'2:08','xj':'2:08','pc':'2:40','c1':'2:52','e1':'3:30','k4':'3:58','k4x':'5:52','k5':'4:39','k5x':'5:18','k5c':'5:30','k6':'8:20','k7':'9:08','m1':'9:16','m2':'9:23','m3':'9:44','m4':'10:03','m5':'11:58'}   # 2026-11-13 W25
FC_TS['noble-timelost-sapphire-v2-bal']=FC_TS['noble-timelost-sapphire-v2']
FC_TS['diztoh-endgame-quarterstaff-v2']={'base':'1:58','h0':'1:58','hc':'2:10','c1':'7:31','e1':'7:40','e1x':'7:38','e2':'8:32','e2b':'8:38','s1':'9:59','d1':'11:28','r1':'11:58','lx':'12:05'}   # 2026-11-13 W22 — sz·s0은 영상에 없음
FC_TS['diztoh-endgame-quarterstaff-v2-bal']=FC_TS['diztoh-endgame-quarterstaff-v2']
FC_TS['sl-flamewave-staff-v2']={'base':'2:22','t1':'2:30','a1':'2:40','x1':'3:21','a2':'3:46','rg':'3:50','ds':'3:53','fr':'5:00','xj':'5:12','pc':'6:35','c1':'6:50','e1':'7:50','e1x':'7:14','d1':'8:20','d2':'8:32','dx':'8:05','r1':'11:20','s1':'11:20','s2':'12:20','s3':'13:18','b1':'9:30','b1b':'9:30','b2':'9:30'}   # 2026-11-13 W26 — s3m은 영상에 없음
FC_TS['sl-flamewave-staff-v2-bal']=FC_TS['sl-flamewave-staff-v2']
FC_TS['mazbro-caster-amulet-v2']={'base':'2:30','a1':'2:30','a2':'4:30','a3':'4:40','pc':'5:05','a4':'5:30','c2':'6:25','c3':'7:10','c4':'7:45','a5':'12:30','a6':'13:00','a7':'13:30','a8':'14:05','a9':'15:00','a10':'16:30','a10x':'18:00','a11':'19:20','a11x':'19:40','a11e':'20:00','a12':'20:15','a13':'21:30','a14':'24:20','a15':'26:40','a16':'27:00','a17':'27:30'}   # 2026-11-13 W27
FC_TS['mazbro-caster-amulet-v2-bal']=FC_TS['mazbro-caster-amulet-v2']
FC_TS['sl-flamewave-ring-v2']={'base':'3:05','rg':'3:10','bn':'3:16','fr':'3:20','es':'3:46','ct':'3:49','cl':'4:30','ca':'4:52','ex':'5:41','dn':'7:17','rv':'7:33','sx':'8:36','wc':'10:22'}   # 2026-11-13 W30
FC_TS['sl-flamewave-ring-v2-bal']=FC_TS['sl-flamewave-ring-v2']
FC_TS['noble-visceral-quiver-v2']={'base':'0:35','h0':'0:35','p1':'0:35','p2':'0:35','p2x':'1:05','hd':'2:15','p3':'2:55','p4':'2:55','pf':'3:15','xj':'3:25','pc':'5:20','s1':'7:20','s2':'7:36','s2x':'7:40','d1':'8:02','e1':'8:11','d1r':'8:32','w1':'8:50','r1':'9:22','r2':'9:30','r3':'10:22','f1':'10:57','f2':'10:59','f3':'11:20'}   # 2026-11-13 W20 자막 없음
FC_TS['noble-visceral-quiver-v2-bal']=FC_TS['noble-visceral-quiver-v2']
FC_TS['mazbro-spell5-amulet-v2']={'base':'9:20','z1':'9:20','z1r':'9:27','z2':'9:32','z3':'10:33','z4':'11:20','z5':'11:35','z6':'11:44','z6c':'12:10','z7':'12:17','z8':'12:50','z9':'13:40','c2':'14:24','c3':'14:30','z10':'26:42','z11':'27:17','z12':'29:06','z13':'29:31','z13x':'28:42'}   # 2026-11-13 W28
FC_TS['mazbro-spell5-amulet-v2-bal']=FC_TS['mazbro-spell5-amulet-v2']
FC_TS['absent-amulet-video-v2']={'base':'11:32','b1':'11:53','b2':'12:02','pf':'12:18','xj':'12:18','b11':'12:40','k1':'14:12','q1':'14:34','q2':'14:44','q3':'14:56','d1':'15:05','r1':'15:15','w1':'15:25','m0':'15:35','m1':'15:45','m2':'15:55','m3':'16:00','m3e':'16:15','m4':'16:40','m5':'16:45','m6':'17:05','s1m':'18:26','s1':'18:50','s2':'19:05','s2x':'18:44'}   # 2026-11-13 W29 성공 회차 11:12~19:12
FC_TS['absent-amulet-video-v2-bal']=FC_TS['absent-amulet-video-v2']
FC_TS['sihan-chayula-ring-v2']={'base':'1:38','k1':'1:43','k2':'1:56','k3':'2:08','k4':'3:26','k4d':'2:32','k4g':'2:51','k5':'3:03','k5c':'3:15','k6':'3:37','k7':'4:01','k8':'4:27'}   # 2026-11-13 W32
FC_TS['sihan-chayula-ring-v2-bal']=FC_TS['sihan-chayula-ring-v2']
FC_TS['easybabi-spiny-talisman-v2']={'base':'1:18','b0':'1:18','es1':'2:11','ru1':'1:51','es2':'2:26','bd1':'2:58','bv1':'3:24','bl1':'4:00','ex1':'3:50','bl2':'4:00','bd2':'4:00','bv2':'4:00','bl3':'4:00','wc1':'4:20'}   # 2026-11-13 W33
FC_TS['easybabi-spiny-talisman-v2-bal']=FC_TS['easybabi-spiny-talisman-v2']
FC_TS['saveq-focus-v2']={'base':'6:02','f1':'6:30','f2':'7:00','f2x':'6:55','f3':'18:20','f3d':'18:40','f4':'19:33','f5':'19:46','f6':'20:58','r1':'20:40','a1':'21:40','d1':'22:18','v1':'22:23','e1':'22:58','w1':'23:16','vx':'24:20','d2':'24:12','v2':'26:10','r2':'26:15'}   # 2026-11-13 W31
FC_TS['saveq-focus-v2-bal']=FC_TS['saveq-focus-v2']
FC_TS['unstoppable-vile-robe-v2']={'base':'5:57','ut':'7:20','ua':'8:50','uax':'8:35','ur':'9:20','ud':'10:46','uf':'10:49','ux':'10:49','uc':'11:15','k1':'13:25','k2':'13:40','k2x':'12:50','q0':'14:10','q1':'15:00','q2':'15:55','q3':'42:30','q5':'42:55','r0':'16:18','r1':'16:21','r2':'18:25','w9':'21:51'}   # 2026-11-13 W34
FC_TS['unstoppable-vile-robe-v2-bal']=FC_TS['unstoppable-vile-robe-v2']
FC_TS['unstoppable-slipstrike-vest-v2']={'base': '40:58', 'ud': '41:12', 'uf': '41:13', 'ux': '41:20', 'uc': '41:15', 'k1': '41:23', 'k2': '41:29', 'k3': '41:45', 'q2': '42:25', 'q3': '42:32', 'q5': '42:46', 'q1': '43:20', 'q4': '43:36', 'r0': '45:32', 'r1': '45:55', 'r2': '46:05', 'ut': '40:58', 'uax': '40:58', 'ua': '41:00', 'ur': '41:12'}   # 2026-11-13 W34
FC_TS['unstoppable-slipstrike-vest-v2-bal']=FC_TS['unstoppable-slipstrike-vest-v2']
FC_TS['vodnarg-timelost-emerald-v2']={'base':'2:55','l1':'4:28','d1':'5:14','r1':'6:02','r1x':'6:58','x1':'10:33','c2':'12:26','l2':'12:58'}   # 2026-11-13 G4
FC_TS['sl-5mod-jewel-v2']={'base':'6:30','pf':'6:58','pc':'7:00','s2':'8:02','s3x':'8:13','s3':'8:21','s4':'8:22','s5':'8:44','s6':'8:55','s7':'9:07','s8':'9:35','s9':'9:48','s11':'10:22'}   # 2026-11-13 G4
FC_TS['seek-cyclone-boots-v2']={'base':'1:10','p1':'3:45','pf':'4:03','pc':'4:15','u1':'4:30','c1':'6:03','e1':'6:45','a1':'7:55','x1':'7:40','x2':'8:15','x3':'8:50','r1':'8:50','d1':'9:35','d2':'10:45','d2x':'9:55','e2':'11:12'}   # 2026-11-13 G4
FC_TS['sihan-chayula-amulet-v2']={'base':'3:02','a2':'3:22','a3':'3:40','a4':'3:49'}   # 2026-11-13 G2
FC_TS['sihan-attack-flat-ring-v2']={'base':'9:55','k1':'14:02','k2':'14:15','k3':'14:30','k4':'15:31','k5':'15:42','k6':'16:10','k7':'17:06','k8':'17:59','k8x':'18:35'}   # 2026-11-13 G2
FC_TS['mazbro-caster-ring-v2']={'base':'3:35','k1':'7:25','k2':'9:00','k3':'9:20','k4':'11:05','k5':'11:15','k6':'11:40','m1':'21:40','m2':'21:45','m3':'22:00','m4':'22:32','m5':'22:46','m5x':'22:20','m6':'23:30','m7':'30:00','m8':'30:40','m8x':'30:50'}   # 2026-11-13 G2
FC_TS['diztoh-socket-gloves-v2']={'base':'0:17','h1':'0:17','h2':'0:40','h2x':'1:34','h3':'1:46','h3x':'1:40','h4':'2:08','h5':'2:52','h6':'3:05','h7':'3:43','m1':'4:05','m2':'4:47','m3':'5:04','m4':'5:17','m5':'5:45','m6':'5:52','m7':'6:16','m8':'6:20','m9':'6:12'}   # 2026-11-13 G3
FC_TS['diztoh-onehand-mace-v2']={'base':'0:03','h1':'0:03','h2':'0:13','h2x':'0:40','h2b':'1:43','h3':'1:52','h4':'2:08','k1':'2:35','k2':'2:45','k3':'3:17','k4':'3:42','k5':'4:26','k6':'4:41','k7':'4:50','k8':'5:00'}   # 2026-11-13 G3
FC_TS['diztoh-as-spear-v2']={'base':'0:02','h1':'0:02','c1':'0:16','e1':'1:34','y1':'2:16','e2':'2:44','y2':'2:54','r1':'3:12','d1':'3:30','e3':'3:52','v1':'4:06'}   # 2026-11-13 G3
FC_TS['sihan-chayula-wand-v2']={'base':'2:45','b0':'2:45','w2':'3:24','w3':'5:01','w3x':'3:37','w4':'5:52','w5':'6:10','w6':'6:35','w7':'6:44','w8':'7:00','w9':'7:32','w10':'7:44'}   # 2026-11-13 G1
FC_TS['sihan-chayula-helmet-v2']={'base':'0:40','b0':'0:40','h2':'1:00','h7':'5:16','h4':'7:32','h4x':'9:00','h5':'8:06','h6':'8:16','h6x':'9:45'}   # 2026-11-13 G1
FC_TS['sihan-chayula-gloves-v2']={'base':'2:35','b0':'2:35','pk':'2:35','g2':'4:00','g4':'4:14','g3':'4:22','r1':'6:22','a1':'6:26','a2':'6:50','d1':'7:10','rv':'7:30','rx':'7:20','rx2':'6:26'}   # 2026-11-13 G1
FC_TS['saveq-absent-amulet-v2']={'base':'6:10','r0':'7:00','c1':'7:32','e1':'9:08','f1':'9:08','f2':'9:29','xs':'9:36','f4':'9:58','v2':'12:02','v3':'12:10','v4':'12:25','v5':'12:33','v6':'12:45','v7':'12:48','v8':'14:00','v9':'14:26','v9x':'15:18','vs':'19:30'}   # 2026-11-13 G5
FC_TS['ragna-spell4-amulet-v2']={'base':'0:00','g2':'0:16','g3':'0:26','g4':'0:58','g5':'1:30','g5b':'1:54','g6':'2:01','g7':'2:16','g8':'2:32','g9':'2:58','g10':'3:15'}   # 2026-11-13 G5
FC_TS['lilbotq-boots-v2']={'base':'4:22','q1':'5:56','q2':'6:20','u1':'6:45','m1':'6:52','m1x':'7:35','m2':'7:58','m2x':'7:42','e1':'8:27','d1':'9:51','f1':'10:02','xj':'10:02','a1':'11:08','a2':'11:20','p1':'11:56','p2':'12:26','p3':'12:34','p3x':'12:34'}   # 2026-11-13 G6
FC_TS['helmet-armour-sl-v2']={'base':'3:00','hq':'3:15','m1':'4:00','m1x':'4:18','m2':'4:26','m2x':'4:18','r1':'4:31','rd':'4:40','f1':'5:53','f2':'5:56','xs':'6:06','fg':'6:20','f4':'6:57','b1':'7:05','b2':'8:00','b2x':'8:04','b3':'8:48','b4':'9:04','b4x':'9:04','s1':'9:12','s1x':'9:44','sf':'10:03','sw':'10:11'}   # 2026-11-13 G6
FC_TS['bigdaddy-lightning-wand-v2']={'base':'1:30','a1':'1:30','rg':'1:30','ds':'1:30','fr':'1:30','xj':'1:30','pc':'1:50','c1':'2:20','e1':'2:41','al':'2:48','d1':'3:28','d2':'3:30','d2x':'3:30','e2':'3:35','lx':'3:40','d3':'3:45','d4':'3:50','d4x':'3:50'}   # 2026-11-13 G7
FC_TS['belton-plus8-wand-v2']={'base':'0:40','z1':'0:44','zr':'0:48','z2':'0:56','z3':'1:06','z4':'1:16','z5':'1:24','z6':'2:13','zs':'25:30','n1':'2:58','n1d':'2:58','n2':'3:52','n2x':'3:52','n2c':'1:16','n3':'5:12','n4':'5:25','n5':'5:45','n5x':'5:45','n6':'6:25'}   # 2026-11-13 G7
FC_TS['sihan-chayula-sceptre-v2']={'base':'1:04','qr':'1:14','q1':'4:28','q2':'5:10','q3':'5:13','q4':'5:16','q5':'5:19','q6':'5:27','q7':'5:33','q8':'5:43','q9':'6:06','x1':'3:35','x2':'3:52','x3':'3:52','xc':'4:10'}   # 2026-11-13 G7
FC_TS['zenm-timelost-sapphire-v2']={'base':'2:00','p1':'2:28','pc':'2:30','c1':'3:02','d1':'4:26','r1':'5:05','r1x':'6:17','x1':'9:20','x2':'9:30','xr':'10:30','xz':'13:30','m1':'9:50'}   # 2026-11-13 G8
FC_TS['diztoh-5mod-sapphire-v2']={'base':'0:08','pc':'0:14','a1':'0:20','a2':'0:47','a2x':'0:50','a3':'2:50','a4':'2:50','k1':'3:03','k1x':'2:35','d1':'3:16','r1':'3:30','r1x':'3:50','n1':'5:12','g1':'5:16','c1':'6:05','f1':'7:05'}   # 2026-11-13 G8
FC_TS['diztoh-5mod-emerald-v2']={'base': '0:36', 'a2': '1:19', 'a3': '2:49', 'a4': '2:49', 'k1': '2:48', 'd1': '3:23', 'r1': '3:50', 'r1x': '4:30', 'n1': '6:02', 'g1': '6:02', 'c1': '9:35', 'f1': '9:48', 'k1x': '16:05'}   # 2026-11-13 G8
FC_TS['saveq-alloy-focus-v2']={'base':'5:26','s1':'5:29','s2':'5:38','s3':'6:00','s4':'6:46','s5':'7:16','s6':'7:30','s7':'7:48','s8':'8:05','s9':'8:24','s10':'10:20'}   # 2026-11-13 G9
FC_TS['lilbotq-emerald-v2']={'base':'15:00','j1':'15:26','j2':'15:34','j3':'16:00','j3x':'17:20','j4':'19:15','j4e':'19:25','j5':'19:35','j6':'20:00','j7':'20:45'}   # 2026-11-13 G9
FC_TS['lilbotq-armour-shield-v2']={'base':'1:02','k1':'1:28','k2':'1:36','k2x':'2:30','k2a':'2:30','k3':'4:05','k4':'4:32','k5':'4:48','k6':'5:00','k7':'5:14','k8':'5:40','k9':'7:36','k10':'7:40','k11':'7:50','k11x':'8:00','k12':'9:44','k13':'10:05'}   # 2026-11-13 G9
FC_TS['diztoh-es-helmet-v2']={'base':'0:20','b0':'0:20','m1':'0:29','m2':'0:33','s1':'0:55','d0':'1:20','dv':'1:22','f1':'1:45','xs':'1:52','xj':'1:52','x1':'2:42','x2':'3:03','r1':'3:45','q1':'3:54'}   # 2026-11-13 G11
FC_TS['diztoh-talisman-v2']={'base':'0:20','b0':'0:20','e1':'1:04','d1':'1:23','r1':'1:36','x1':'2:32','q1':'3:10','dv':'3:23','a1':'3:44','x2':'3:56','x3':'4:28','rn':'4:44','x4':'5:16'}   # 2026-11-13 G11
FC_TS['ragna-ashot-bow-v2']={'base':'2:12','b0':'2:12','e1':'2:13','x1':'2:32','d1':'4:10','x2':'4:52','v1':'5:08'}   # 2026-11-13 G13
FC_TS['lilbotq-budget-boots-v2']={'base':'0:25','k0':'0:25','k1':'2:01','k2':'2:21','k3':'2:36','k4':'3:16','q1':'3:45'}   # 2026-11-13 G13
FC_TS['farmer-starter-staff-v2']={'base':'11:45','f0':'11:45','f1':'12:08','f2':'14:20','f3':'14:40','f4':'15:32','f5':'15:32'}   # 2026-11-13 G13
FC_TS['icesly-budget-wand-v2']={'base':'1:42','c1':'1:52','c2':'3:06','c3':'3:18','c4':'3:32','c5':'3:54','c6':'4:59','c7':'5:15','c8':'5:52'}   # 2026-11-13 G12
FC_TS['diztoh-rarity-ring-v2']={'base':'1:35','q1':'1:46','q2':'2:40','q3':'3:35','q4':'4:32','q5':'5:30'}   # 2026-11-13 G12
FC_TS['sane-resist-belt-v2']={'base':'0:14','t1':'1:40','t2':'1:40','t3':'2:40','t4':'4:15'}   # 2026-11-13 G12
FC_TS['farmer-budget-armour-v2']={'base':'3:16','g1':'3:26','g2':'3:45','g3':'4:00','g4':'4:14','g5':'4:57'}   # 2026-11-13 G14
FC_TS['diztoh-budget-mace-v2']={'base':'0:12','m1':'0:25','m1x':'0:33','m2':'0:45','e1':'0:57','k1':'1:04','k2':'1:41','k3':'1:54','k4':'2:33','k5':'2:52'}   # 2026-11-13 G14
FC_TS['diztoh-budget-crossbow-v2']={'base':'0:45','m1':'0:50','m1x':'1:19','m2':'1:05','e1':'1:37','k1':'1:52','k2':'2:00','k3':'2:16','k4':'2:40','k5':'2:53','k6':'3:32'}   # 2026-11-13 G14
FC_TS['mazbro-bis-chest-v2']={'base':'2:30','p1':'3:35','p2':'3:40','p2x':'3:50','hd':'3:23','p3':'4:15','p4':'4:20','p5':'4:40','xj':'4:40','p6':'5:10','r1':'5:40','c1':'6:00','e1':'6:32','e1x':'6:44','s0':'12:40','mA':'12:55','b2':'13:30','b2n':'31:00','b3':'13:38','s1':'23:47','w1':'24:36','da':'15:00','f1':'26:40','f2':'26:45','f3':'27:30','f3x':'27:05'}   # 2026-11-12 W7 영상 전체 재대조(근거 scratchpad review/W7-bis-chest/timeline.md) — 성공 회차 = 첫 번째 흉갑, 분열 준비(p1~p6)는 3:23 노트·3:36~5:27 시연
FC_TS['diztoh-crit-helmet-v2']={'base':'0:30','h2':'0:55','h2x':'1:20','h3':'0:58','h3x':'1:10','h3y':'1:27','h4':'1:47','h5':'2:07','h7':'2:51','xs':'2:51','xj':'2:51','h8':'3:01','c1':'7:23','cz':'5:47','p1':'7:29','p2':'9:41','p3':'9:09','p3x':'9:17','d1':'10:03','d2':'10:30','dx':'10:58','f1':'12:00'}   # 2026-11-12 W6 영상 전체 재대조(근거 scratchpad review/W6-crit-helmet/timeline.md) — 성공 회차 7:23~12:03, cz는 데모 회차(5:39~5:47)
# 성공 회차 옵션(S4, 2026-11-13): 완성 카드의 묶음 태그(anyOf) 줄에 태그 shown·shownBy가 있으면 그 옵션 줄로 바꾸고(of = 원래 태그, alt = 다른 유효 옵션 gi)
# 화면(recipes.html fcShowLines)과 같은 규칙 — 같은 묶음 줄이 여러 개면 shown 목록 순서대로
_CLSG = {}
def _shownlines(F, V, GT, tags, cls):
    if cls not in _CLSG:
        try: _CLSG[cls] = json.load(open(f"{D}c/{cls}.json"))['groups']
        except Exception: _CLSG[cls] = []
    gs = _CLSG[cls]; out = []; k = {}; vid = (V or {}).get('id') or F.get('id'); P = (V or {}).get('params') or {}
    allsh = {}
    for l in F['lines']:
        t = l.get('tag'); sl = _g2r.shown_leaves(GT, t, vid, P) if t and not l.get('label') and not l.get('random') else None
        if sl: i = k.get(t, 0); k[t] = i + 1; allsh.setdefault(t, []).append(sl[i]['gi'] if i < len(sl) else None)
    k = {}
    for l in F['lines']:
        t = l.get('tag'); sl = _g2r.shown_leaves(GT, t, vid, P) if t and not l.get('label') and not l.get('random') else None
        if not sl: out.append(l); continue
        i = k.get(t, 0); k[t] = i + 1
        if i >= len(sl): out.append(l); continue
        x = sl[i]; G0 = gs[x['gi']] if 0 <= x['gi'] < len(gs) else {}
        pt = f"{t}~{i}"
        tags[pt] = {'gi': x['gi'], 's': G0.get('g'), 'sec': G0.get('s'), 'tmax': x.get('tmax') or l.get('tmax')}
        if tags[pt]['tmax'] is None:
            lt = (GT.get(t) or {}).get('tmax') if isinstance(GT.get(t), dict) else None
            tags[pt]['tmax'] = lt if isinstance(lt, int) else None
        out.append({**{a: b for a, b in l.items() if a not in ('tag', 'label', 'any')}, 'tag': pt, 'of': t, 'sh': True,
                    'alt': [g for g in _g2r.leaf_gis(GT, t) if g not in [y for y in allsh.get(t, []) if y is not None]]})
    return out

# flowchart + simulation (tools/sim/run.js → site/data/sim/<id>.json): the recipe tab shows its button only when the file exists
for _r in R:
    _sid=_r.get('tierGroup') or _r['id']
    if os.path.exists(f"{D}sim/{_sid}.json"):
        _r['sim'] = 1
        if _sid!=_r['id']: _r['simId'] = _sid
        # 완성품 = 플로우차트의 그 등급 완성품 카드(사용자 확정 2026-11-11: 플로우차트 → 등급별 카드 3장 → 그 흐름을 따른 레시피, 같은 등급은 같은 카드)
        _sd=json.load(open(f"{D}sim/{_sid}.json")); _g=_sd.get('graph',{}); _tier=_r.get('tier') or 'high'
        _F=next((f for f in (_g.get('finals') or []) if (f.get('tier') or f['id'])==_tier), None)
        if _F:
            _V=next((v for v in (_g.get('versions') or []) if v['id']==_F['id']), None)
            _S=_V and next((x for x in _sd.get('strategies',[]) if not x.get('hidden') and all(str(x['params'].get(k))==str(v) for k,v in _V['params'].items())), None)
            _tags={l['tag']:{k:_g['tags'][l['tag']].get(k) for k in ('gi','s','sec','tmax')} for l in _F['lines'] if l.get('tag') in (_g.get('tags') or {})}
            for _T in _tags.values():   # 등급 파라미터 티어('$gT')를 그 등급 값으로 — 완성 카드가 1티어 범위만 보이던 것(2026-11-13 S3 8번)
                if isinstance(_T.get('tmax'), str) and _T['tmax'].startswith('$') and _V:
                    try: _T['tmax'] = int(_V['params'].get(_T['tmax'][1:]))
                    except Exception: _T['tmax'] = None
            # 고르는 줄(label)은 같은 이름의 anyOf 태그로 게임 데이터 옵션(gi)을 붙임 — 글자만 있는 줄은 정책 12장 위반(사용자 확정 2026-11-12)
            _GT=_g.get('tags') or {}
            def _gis(t, seen=()):
                if isinstance(t, str): return [] if t in seen else _gis(_GT.get(t), seen+(t,))
                if not isinstance(t, dict): return []
                if t.get('gi') is not None: return [t['gi']]
                return [g for x in (t.get('anyOf') or []) for g in _gis(x, seen)]
            def _anyline(l):
                # 묶음 태그만 적은 줄 → 그 태그 이름 + 옵션 목록(2026-11-12: 화면에서 줄이 빠지던 문제)
                T0=_GT.get(l.get('tag')) if l.get('tag') else None
                if not l.get('label') and not l.get('random') and isinstance(T0,dict) and T0.get('gi') is None and T0.get('anyOf'):
                    g=_gis(T0); return {**{k:v for k,v in l.items() if k!='tag'}, 'label':T0.get('label') or {'kr':'랜덤 옵션','en':'Random modifier'}, 'any':g}
                if not l.get('label') or l.get('random'): return l
                T=_GT.get(l.get('tag')) if l.get('tag') else next((t for t in _GT.values() if isinstance(t,dict) and t.get('anyOf') and (t.get('label') or {}).get('kr')==l['label'].get('kr')), None)
                g=_gis(T) if T else []
                return {**l, 'any':g} if g else l
            _r['fc']={'lines':[_anyline(l) for l in _shownlines(_F, _V, _GT, _tags, _r.get('cls'))],'tags':_tags,'ds':(_S or {}).get('res',{}).get('desStat')}
            if _g.get('finalItem'): _r['fc']['fi']={k:v for k,v in _g['finalItem'].items() if k in ('quality','sockets')}   # 완성 카드 퀄리티·소켓(두 완성 카드가 같은 값을 쓰게, 2026-11-12)
            # 레시피 = 그 등급 플로우차트를 순서대로 읽은 것(사용자 확정 2026-11-11, scripts/graph2recipe.py): 단계·확률·사용량·갈래 모두 플로우차트·시뮬 값
            if _S and _r['id'] not in FCREAD_OFF and os.path.exists(f"/home/claude/poe2data/scripts/graphs/{_sid}.json"):
                _tiers=[x.get('tier') or 'high' for x in R if (x.get('tierGroup') or x['id'])==_sid]
                try: _rd=_g2r.read_recipe(_r, _sd, json.load(open(f"/home/claude/poe2data/scripts/graphs/{_sid}.json")), _tiers, inherit=not FC_TS.get(_sid))   # 영상 재대조(FC_TS) 그래프는 옛 노드 시각·꿀팁을 이어받지 않음(2026-11-13 S2)
                except Exception as _e: print('flowchart read failed', _r['id'], _e); _rd=None
                if _rd:
                    _r['nodes']=_rd['nodes']; _r['phases']=_rd['phases']; _r['start']=_rd['start']; _r['fcRead']=_rd['fcRead']
                    for _n in _r['nodes']:   # 꿀팁 연결(notes_short TIPREF)을 플로우차트 상자 id로도 — 옛 단계 id와 다른 새 그래프(SaVeQ 집중구 f0·d1, 2026-11-13 S1)
                        _k=(_r['id'],_n['id'])
                        if _k not in TIPREF: _k=(_old(_r),_n['id'])
                        if _k in TIPREF: _n['tips']=list(dict.fromkeys((_n.get('tips') or [])+TIPREF[_k]))
                    if _g2r.has_prep(_sd) and _r.pop('prep', None) is not None: PREP_DROPPED.append(_r['id'])   # 준비 단계는 플로우차트에서 읽음 — 옛 접힌 준비(r.prep)를 두면 엔진 합계가 두 번 셈
                    for _k,_v in (FC_TS.get(_sid) or {}).items():   # 플로우차트 상자 → 영상 시각(옛 단계 레시피에서 온 시각이 틀린 곳만)
                        for _n in _r['nodes']:
                            if _n['id']==_k or (_k=='base' and _n.get('do')=='base'): _n['ts']=_v
print('old prep dropped (flowchart reads its own prep):', PREP_DROPPED)
for _r in R:   # {#id} → 플로우차트에서 읽은 단계 번호(그 id가 없으면 옛 번호)
    _no0 = _r.pop('_no0', None)
    if _no0 is None: continue
    _no1 = {n['id']:(n.get('fcNo') or i+1) for i,n in enumerate(_r['nodes'])}   # 플로우차트에서 읽은 레시피는 화면 번호(fcNo)와 같게(2026-11-13 S2)
    def _fix2(v):
        if isinstance(v, str): return _re.sub(r'\{#(\w+)\}', lambda m: str(_no1.get(m.group(1)) or _no0[m.group(1)]), v)
        if isinstance(v, dict): return {k:_fix2(x) for k,x in v.items()}
        if isinstance(v, list): return [_fix2(x) for x in v]
        return v
    _r['nodes'] = _fix2(_r['nodes'])
# 사용자 요청으로 내린 레시피(2026-11-11 22:21: 금 목걸이 6옵션 — 플로우차트 옵션이 영상이 만든 목걸이와 다름. 영상 전체 기준으로 다시 만들 때까지 등록하지 않음)
REMOVED={'gold-amulet-6line'}
R[:]=[x for x in R if _re.sub(r'-(bal|ess)$','',_re.sub(r'-v2(?=$|-)','',x['id'])) not in REMOVED and _re.sub(r'-v2$','',x.get('simId') or x.get('tierGroup') or '') not in REMOVED]
# 룬 규칙(2026-11-13): 시작 룬과 같은 룬을 단계에서 장착하면 시작 룬에서 뺌 — 'Limited to 1' 룬이 두 번 들어가 소켓이 넘치던 문제(SL 장갑 콜르)
_rn=lambda x:(x.get('en') if isinstance(x,dict) else str(x).replace('rune:','')).replace('’',"'").strip()
for _r in R:
    _st=(_r.get('start') or {}).get('runes')
    if not _st: continue
    _put={_rn(n['target']['rune']) for n in _r['nodes'] if (n.get('target') or {}).get('rune')}
    _r['start']['runes']=[x for x in _st if _rn(x) not in _put]
EXCLUDED={'banzino-mirror-staff'}   # 사용자 결정 2026-11-13: 미러 지팡이는 가중치 문제(전도성 지팡이 베이스별 옵션 제한이 데이터에 없음)로 사이트에서 뺌
R[:]=[x for x in R if _re.sub(r'-v2(-(bal|ess))?$','',x['id']) not in EXCLUDED]
json.dump({'v':2,'recipes':R},open(D+'recipes.json','w'),ensure_ascii=False)
print(len(R),'recipes')
