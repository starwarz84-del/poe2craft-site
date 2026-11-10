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
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티(레벨이 가장 낮음)를 날리고 접두 굴림. 좋은 옵션이면 끝. 안 뜨면 갈림길(절사의 징조를 다시 쓰면 엉뚱한 줄보다 레벨 낮은 모든 스킬의 퀄리티가 지워질 수 있음).','Whittling + Perfect Chaos removes Maximum Quality (the lowest level) and rolls a prefix; a good one ends the craft. On a miss, choose a fork (Whittling again could take the skill quality line).')},
  {'id':'a12','phase':'des','branch':OK,'do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':[{'gi':esFlat,'tmax':1},{'gi':esPct,'tmax':1}],'replace':'p'},'fallbackFor':'a11','fail':{'goto':'self'},
   'label':K('갈림길 ①: 계속 돌리기','Fork (1): keep rolling'),
   'note':K('좌측 말소의 징조 + 상위 카오스 오브로 접두를 계속 돌려 에너지 보호막 1티어 찾기. 좌측 말소의 징조는 접두만 바꾸고, 접두엔 엉뚱한 줄과 분열 줄뿐이라 좋은 줄이 안 지워짐.','Sinistral Erasure + Greater Chaos keeps rerolling the prefix for T1 Energy Shield; Erasure only touches prefixes, and the only removable prefix is the wrong one.')},
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
   'note':K('완벽한 엑잘티드 오브로 접두 한 줄(에너지 보호막 1티어, 접미는 꽉 차서 징조 불필요). 영상은 여기서 멈춤. 공개도 성공했고 이것만 안 뜨면 갈림길.','Perfect Exalt one prefix (T1 Energy Shield; suffixes are full, no omen); the video stopped here. If the reveal landed and only this missed, choose a fork.')},
  {'id':'a16b','phase':'des','branch':MISS,'do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':[{'gi':esFlat,'tmax':1},{'gi':esPct,'tmax':1}],'replace':'p'},'fallbackFor':'a16','fail':{'goto':'self'},
   'label':K('갈림길 ①: 계속 돌리기','Fork (1): keep rolling'),
   'note':K('좌측 말소의 징조 + 상위 카오스 오브로 접두를 계속 돌려 에너지 보호막 1티어 찾기. 좌측 말소의 징조는 접두만 바꾸고, 접두엔 엉뚱한 줄과 분열 줄뿐이라 좋은 줄이 안 지워짐.','Sinistral Erasure + Greater Chaos keeps rerolling the prefix for T1 Energy Shield; Erasure only touches prefixes, and the only removable prefix is the wrong one.')},
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
   {'id':'suffix','kr':'접미 3줄','en':'Three suffixes'},
   {'id':'prefix','kr':'접두 원소 플랫','en':'Prefix elemental flats'},
   {'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'c1','phase':'base','do':'base','cost':'base','ts':'1:27',
   'note':K('제련된 균열 반지(균열 나무에서만, 항상 레어). 아이템 레벨 75 이상이면 충분(목표 옵션 중 75 넘는 게 없음). 계산은 80 기준. 가성비면 일반 균열 반지도 가능.','Refined Breach Ring (Breach tree only, always rare). Item level 75+ is enough (no target mod is above 75); 80 assumed. A plain Breach Ring works for a budget build.')},
  {'id':'c2','phase':'fracture','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':FL,'replace':'p'},'fail':{'goto':'self'},'ts':'2:00',
   'note':K('카오스 오브로 화염·냉기·번개 플랫 중 아무거나 1티어. 물리 플랫은 수치가 낮아 비추. 영상 기준 약 250개에 한 번.','Chaos until any T1 fire/cold/lightning flat. Physical flat rolls too low. About 1 in 250 per the video.')},
  {'id':'c3','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'22:21',
   'note':K('빗장뼈로 훼손 자리를 채워 4줄(훼손은 분열 안 됨).','Fill a slot with a Collarbone desecration (it cannot fracture).')},
  {'id':'c4','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':FL},'fail':{'goto':'restart'},'ts':'25:53',
   'after':{'keepOnly':[fireF,coldF,lightF,'junk']},
   'note':K('훼손 제외 3줄 중 1줄(1/3). 이후 훼손 자리는 정리.','1 in 3 (the desecrated slot cannot fracture). The desecrated slot is cleared afterwards.')},
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
   'note':K('카오스 오브로 원하는 접미 하나(영상 완성품: 모든 원소 저항, 아이템 희귀도). 분열 줄 말고 지울 수 있는 줄이 최대 퀄리티뿐이라 첫 카오스 오브가 그 줄을 지움 — 제작 옵션인 최대 퀄리티가 없어져서 뒤에 재빠른 합금을 쓸 수 있음(퀄리티는 그대로). 영상 순서대로 희귀도를 카오스 오브 쪽에서 뽑는 걸로 계산.','Chaos for one wanted suffix (the finished ring has all resistances and item rarity). Following the video, rarity is counted on the Chaos side.')},
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
   'note':K('분열의 오브는 옵션 4개가 필요해서 보존된 갈비뼈로 한 줄 채움. 훼손(미공개)은 분열되지 않음.','The Fracturing Orb needs four modifiers, so a Preserved Rib fills one. Unrevealed desecrated mods cannot fracture.')},
  {'id':'f2','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':armEle},{'gi':armP},{'gi':rarE}]},'ts':'5:56',
   'note':K('남은 세 줄이 모두 유효 옵션이라 어느 쪽이 분열돼도 성공(100%). 영상은 방어도→원소 적용이 분열됨. 아래 단계는 그 경우 기준.','All three remaining lines are wanted, so any fracture works (100%). In the video Armour-applies-to-Elemental fractured; the steps below follow that case.')},
  {'id':'f3','phase':'fracture','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},'optional':True,'ts':'6:09',
   'exit':K('제작 종료 (그대로 쓰거나 판매)','stop here (use or sell it)'),
   'note':K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 한 번 도박(접두 1·접미 1). 1티어 두 줄처럼 괜찮은 옵션이 뜨면 여기서 제작 끝 — 그대로 쓰거나 팔면 됨. 꽝이면 다음 단계로. 영상은 2·3티어라 꽝.','One gamble with Greater Exaltation + Perfect Exalt (one prefix, one suffix). If it lands something good, such as two T1 lines, the craft ends here: use or sell it. Otherwise continue. The video got T2/T3.')},
  {'id':'f4','phase':'fracture','do':'remove','cur':'Orb_of_Annulment','expect':4,'after':{'keepOnly':[armEle,'junk1']},'ts':'6:57',
   'note':K('소멸의 오브로 정리해서 분열 옵션 + 아무 한 줄만 남김(어떤 옵션이든 상관없음). 다음 단계 카오스 오브가 그 한 줄을 원하는 옵션으로 바꿈.','Annul down to the fractured mod plus any one line (it does not matter which); the next Chaos turns that line into a wanted mod.')},
  {'id':'b1','phase':'prefix','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':P3},'fail':{'goto':'self'},'ts':'7:05',
   'note':K('카오스 오브로 접두 1티어 하나: 방어도 1티어, 방어도 % 1티어, 생명력 1티어 중 아무거나. 방어구는 가중치가 높아 금방 나옴.','Chaos for one T1 prefix: flat Armour, % Armour or Life, any of them. Armour weights are high, so it comes quickly.')},
  {'id':'b2','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':P3},'fail':{'goto':'b1','via':{'cur':'Orb_of_Annulment'}},'ts':'7:51',
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 하나 더. 원하지 않는 옵션이면 소멸의 오브로 지우고(유효 옵션이 같이 지워지면 카오스 오브부터 다시). 영상에서 가장 어려운 구간.','Sinistral Exaltation + Perfect Exalt for another prefix. On a miss, annul (if the good one goes too, chaos again). The hardest part of the craft.')},
  {'id':'b3','phase':'prefix','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'8:44',
   'note':K('남은 접두 한 자리는 훼손으로: 고대 갈비뼈 + 좌측 강령술의 징조. 접두 3종 중 아직 없는 옵션 하나만 찾으면 됨.','The last prefix slot goes to a desecration: Ancient Rib + Sinistral Necromancy. Only the one prefix still missing is needed.')},
  {'id':'b4','phase':'prefix','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':P3},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'b3','via':LIGHT},'ts':'8:54',
   'note':K('영혼의 우물에서 심연의 메아리의 징조로 공개해 남은 하나(이미 붙은 두 옵션과 같은 계열은 안 나오므로 사실상 그 하나)를 찾음. 영상은 한 번에 방어도 % 1티어. 실패하면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손.','Reveal at the Well with Abyssal Echoes; the video hit T1 % Armour first time. On a miss, Light + Annulment and desecrate again.')},
  {'id':'s1','phase':'suffix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':RES},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}},'ts':'9:12',
   'note':K('접두가 꽉 차서 상위 찬미의 징조 + 완벽한 엑잘티드 오브의 두 줄이 모두 접미로. 원소 저항 1티어 아무거나. 2·3티어로 타협해도 됨, 아니면 우측 소멸의 징조 + 소멸의 오브로 지우고 다시(영상은 3번째에 냉기 1티어).','Prefixes are full, so Greater Exaltation puts both lines on suffixes: any T1 elemental resistance. T2/T3 is acceptable; otherwise Dextral Annulment and retry (third try in the video).')},
  {'id':'s2','phase':'suffix','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'anyOf':[{'gi':rarS,'tmax':1}],'replace':'s'},'fail':{'goto':'self'},'ts':'10:15',
   'note':K('절사의 징조 + 완벽한 카오스 오브로 남은 접미 한 줄. 접두가 날아갈 수 있어 우측 말소의 징조도 켬. 영상은 희귀도 1티어로 마무리.','Whittling + Perfect Chaos for the last suffix, with Dextral Erasure so prefixes are safe. The video finished with T1 Rarity.')},
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
 'source':{'url':V5, 'title':'[POE2 0.5.5] #7 황금 목걸이 심연의 에센스 활용하여 졸업급으로 만들기! (태양의 목걸이, 6줄 목걸이)', 'channel':'SL 게임연구소!'},
 'title':K('정신력 분열 + 주문 +3 6줄','fractured Spirit + spell +3, six lines'),
 'note':K('목표 구조: 접두 = 정신력(분열) + 완벽한 강화의 에센스 방어 % + 적당한 접두 1줄, 접미 = 주문 스킬 +3 + 적당한 접미 1줄 + 훼손 1줄. 접두 2줄·접미 2줄까지만 노리고 나머지는 나오는 걸 씀. 영상 1트 기준 경로이고, 다른 경우는 각 단계 메모 참고.',
          'Target: prefixes = fractured Spirit + Perfect Essence of Enhancement defences + one acceptable prefix; suffixes = spell +3 + one acceptable suffix + one desecration. Aim for two lines on each side and take what comes for the rest. Main path from the first attempt; other cases are in the step notes.'),
 'start':{'rar':'rare','mods':[{'gi':spirit5,'tmax':1},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fracture','kr':'분열','en':'Fracture'},{'id':'skill','kr':'주문 스킬 +3','en':'Spell skills +3'},
           {'id':'quality','kr':'퀄리티 작업','en':'Quality'},{'id':'suffix','kr':'접미 한 줄 완성','en':'First suffix'},{'id':'prefix','kr':'접두 작업','en':'Prefixes'},
           {'id':'last','kr':'마지막 접미 (훼손)','en':'Last suffix (desecration)'},{'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'1:54',
   'note':K('황금 목걸이(또는 태양의 목걸이), 아이템 레벨 82 이상, 정신력 +50(1티어)이 붙은 3줄 이하 희귀 목걸이. 접미는 아무 옵션이나 상관없음.','A rare Gold (or Solar) Amulet, item level 82+, with +50 Spirit (T1) and three lines or fewer. Suffixes do not matter.')},
  {'id':'g2','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},
   'note':K('분열의 오브는 옵션 4개가 필요해서 보존된 빗장뼈로 한 줄 채움(훼손은 분열되지 않아 정신력 확률 1/3).','The Fracturing Orb needs four modifiers, so a Preserved Collarbone fills one (desecrations cannot fracture, so Spirit is 1 in 3).')},
  {'id':'g3','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':spirit5}]},'fail':{'goto':'restart'},'ts':'11:10',
   'after':{'keepOnly':[spirit5,'junk1']},
   'note':K('정신력 분열 1/3. 영상은 4개 중 1개 성공. 이후 분열 + 한 줄만 남기고 소멸의 오브.','Spirit fractures 1 in 3; 1 of 4 in the video. Then annul down to the fracture plus one line.')},
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
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티를 날리고 접미 한 줄부터 완성. 접미는 2티어 이상 적당한 옵션이면 멈춤. 옵션이 접두로 가면 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 접미를 노림. 영상은 희귀도 1티어.','Whittling + Perfect Chaos removes max quality; finish one suffix first. Stop at any decent T2+ suffix. If the roll goes to a prefix, use Dextral Exaltation + Perfect Exalt for the suffix. The video got T1 Rarity.')},
  {'id':'p1','phase':'prefix','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'target':{'anyOf':[{'gi':spelld5,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}},'ts':'15:06',
   'note':K('좌측 찬미의 징조 + 상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 두 자리를 채우며 주문 피해 % 1티어(27—30%)를 노림 — 주문 빌드 기준 베스트 접두이자 영상 1트 완성품의 옵션. 같이 붙은 나머지 한 줄은 다음 단계에서 정리. 안 뜨면 좌측 소멸의 징조 + 소멸의 오브로 지우고 다시. 주문 빌드가 아니면 에너지 보호막·생명력 최대치 1티어도 대안.','Sinistral + Greater Exaltation + Perfect Exalt fills both prefix slots, aiming for T1 % Spell Damage (27–30%): the best prefix for a spell build and what the video\'s first amulet got. The other line is dealt with next. On a miss, Sinistral Annulment and retry. For non-spell builds, T1 flat ES or Life work too.')},
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
  {'id':'f0','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'8:20',
   'note':K('분열의 오브는 옵션 4개가 필요. 훼손 한 줄은 분열되지 않으니 +1이 분열될 확률이 1/3이 됨.','The Fracturing Orb needs four modifiers. A desecrated line cannot fracture, so +1 fractures 1 time in 3.')},
  {'id':'f1','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':spell1}]},'extra':{'Hinekoras_Lock':4},
   'after':{'keepOnly':[spell1,'junk1']},
   'note':K('22만 카오스짜리 옵션이라 그냥 분열하지 않고, 히네코라의 머리카락으로 결과를 미리 봄. 미리 본 결과가 +1이 아니면 아이템을 살짝 바꾸고 다시 머리카락. 영상은 4개째에 +1 분열 확인 후 분열. 이후 분열 + 한 줄만 남기고 정리.','At 220,000 Chaos this is not left to chance: Hinekora\'s Lock previews the result. If the preview is not +1, change the item slightly and lock again. The video saw +1 on the fourth lock, then fractured. Afterwards keep the fracture plus one line.')},
  {'id':'s1','phase':'suffix','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'all':[{'gi':scd,'tmax':1},{'gi':cast,'tmax':1}]},'fail':{'goto':'self'},
   'note':K('절사의 징조 + 카오스 오브로 접미 두 자리를 주문 치명타 피해 보너스 1티어(26—29%)와 시전 속도 1티어(22—24%)로 채움. 접미부터 끝내 두면 접두 작업을 마음 편히 할 수 있음.','Whittling + Chaos fills the two suffixes with T1 spell crit damage bonus (26–29%) and T1 cast speed (22–24%). Finishing the suffixes first frees the prefixes.')},
  {'id':'p0','phase':'prefix','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},
   'note':K('에센스가 지울 자리를 만들기 위해 접두에 아무 옵션 하나.','Any prefix, as the slot the essence will remove.')},
  {'id':'p1','phase':'prefix','do':'essence','cur':'Essence_of_Delirium','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':notable},'knownP':True,
   'note':K('좌측 결정화의 징조 + 섬망의 에센스로 접두 잡옵을 지우고 "무작위 주요 패시브 할당". 영상은 지배가 나옴. 시전 빌드라면 자루크의 선물·모범·마학 같은 노드가 인기. 원하는 노드가 아니면 다시.','Sinistral Crystallisation + Essence of Delirium swaps the junk prefix for "Allocates a random Notable". The video got Dominion; for casters, notables like Zarokh\'s Gift, Exemplar or Arcane studies are popular. Redo it if the notable is not one you want.')},
  {'id':'p2','phase':'prefix','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},
   'note':K('합금이 지울 자리로 접두 하나 더.','One more prefix for the alloy to remove.')},
  {'id':'p2b','phase':'prefix','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 장착',"Socket Astrid's Creativity"),
   'note':K('섬망의 에센스 줄도 제작 옵션이라, 두 번째 제작 옵션(합금)을 붙이려면 아스트리드의 창의성이 필요. 제작이 끝나면 빼고 원하는 룬으로 교체.',"The Delirium line is crafted too, so the second crafted line (the alloy) needs Astrid's Creativity. Swap it for any rune once crafting is done.")},
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
 'title':K('축성 주문 스킬 +6 · 정신력 · 마나 · 시전 속도','sanctified +6 spell skills, Spirit, Mana, cast speed'),
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
   'note':K('히네코라의 머리카락으로 분열 결과를 미리 봄. 정신력이 아니면 아이템을 바꾸고(영상은 소멸의 오브로 한 줄 지우고 다시 채움) 다시 머리카락. 영상은 모든 원소 저항·최대 퀄리티를 거쳐 약 4개째에 정신력 분열. 이후 분열 + 한 줄만 남김.','Preview the fracture with Hinekora\'s Lock. If it is not Spirit, change the item (the video annulled a line and refilled it) and lock again. The video saw all resistances and Maximum Quality first and got Spirit on about the fourth lock. Then keep the fracture plus one line.')},
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
 'absent-amulet-video': _fb(('a2','a4'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1줄.', 'Fractured Spirit plus one junk line.'),
 'breach-ring-video': _fb(('c2','c4b'), [{'gi':15,'tmax':1,'fr':True},{'junk':'s'}], '공격 시 원소 피해 1티어 분열(화염·냉기·번개 아무거나) + 잡옵 1줄.', 'A fractured T1 elemental attack flat (any element) plus one junk line.'),
 'helmet-armour-sl': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1줄.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'sihan-highend-boots-v2': _fb(('h2','f4'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '방어도 % 증가 분열 + 잡옵 1줄.', 'Fractured % increased armour plus one junk line.', 26),
 'sihan-highend-boots-v2-bal': _fb(('h2','f4'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '방어도 % 증가 분열 + 잡옵 1줄.', 'Fractured % increased armour plus one junk line.', 26),
 'sihan-highend-boots-v2-ess': _fb(('h2','f4'), [{'gi':8,'tmax':1,'fr':True},{'junk':'s'}], '방어도 % 증가 분열 + 잡옵 1줄.', 'Fractured % increased armour plus one junk line.', 26),
 'saveq-absent-amulet-v2': _fb(('r0','f4'), [{'gi':25,'tmax':1,'fr':True},{'junk':'p'}], '치명타 피해 보너스 1티어 분열 + 잡옵 1줄.', 'Fractured T1 critical damage bonus plus one junk line.'),
 'saveq-absent-amulet-v2-bal': _fb(('r0','f4'), [{'gi':25,'tmax':1,'fr':True},{'junk':'p'}], '치명타 피해 보너스 1티어 분열 + 잡옵 1줄.', 'Fractured T1 critical damage bonus plus one junk line.'),
 'saveq-absent-amulet-v2-ess': _fb(('r0','f4'), [{'gi':25,'tmax':1,'fr':True},{'junk':'p'}], '치명타 피해 보너스 1티어 분열 + 잡옵 1줄.', 'Fractured T1 critical damage bonus plus one junk line.'),
 'helmet-armour-sl-v2': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1줄.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'helmet-armour-sl-v2-bal': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1줄.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'helmet-armour-sl-v2-ess': _fb(('h2','f4'), [{'gi':20,'tmax':1,'fr':True},{'junk':'p'}], '방어도의 원소 피해 적용 분열 + 잡옵 1줄.', 'Fractured armour applies to elemental damage plus one junk line.', 26),
 'gold-amulet-6line': _fb(('g2','g3'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1줄.', 'Fractured Spirit plus one junk line.'),
 'grasping-mail-spell1': _fb(('m2','f1'), [{'gi':140,'fr':True},{'junk':'s'}], '룬 아버지 단계까지 올린 베이스(갑옷·기폭제 퀄리티 30%). 모든 주문 스킬 레벨 +1 분열 + 잡옵 1줄.', "A Runefather base (armour and catalyst quality 30%) with fractured +1 spell skills plus one junk line.", 30),
 'absent-amulet-spell6': _fb(('b1b','f1'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '시전 퀄리티 48%. 정신력 분열 + 잡옵 1줄.', '48% caster quality, fractured Spirit plus one junk line.', 48),
 'mazbro-caster-ring': _fb(('r1b','r4'), [{'gi':34,'tmax':1,'fr':True},{'junk':'p'}], '시전 속도 분열 + 잡옵 1줄.', 'Fractured cast speed plus one junk line.'),
 'mazbro-caster-amulet': _fb(('a2','a3'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 분열 + 잡옵 1줄.', 'Fractured Spirit plus one junk line.'),
 'mazbro-bis-chest': _fb(('c2','c6'), [{'gi':15,'tmax':1,'fr':True}], '정신력 분열(나머지 줄은 정리한 상태).', 'Fractured Spirit, everything else cleared.'),
 'mazbro-proj-gloves': _fb(('g2','g7'), [{'gi':81,'fr':True},{'junk':'p'}], '콜르의 사냥을 장착한 상태로 모든 투사체 스킬 레벨 +2 분열 + 잡옵 1줄.', "Kolr's Hunt socketed: fractured +2 projectile skills plus one junk line.", 30, [KOLR_]),
 'diztoh-iceshot-bow': _fb(('w2','w6'), [{'gi':7,'tmax':1,'fr':True},{'junk':'p'}], '물리 피해 % 1티어 분열 + 잡옵 1줄.', 'Fractured T1 % physical damage plus one junk line.'),
 'diztoh-crit-helmet-v2': _fb(('h2','h7'), [{'gi':9,'tmax':1,'fr':True},{'junk':'s'}], '퀄리티 20%. 회피 및 에너지 보호막 % 1티어 분열 + 잡옵 1줄.', 'Quality 20%. Fractured T1 % evasion and energy shield plus one junk line.', 20),
 'diztoh-crit-helmet-v2-bal': _fb(('h2','h7'), [{'gi':9,'tmax':1,'fr':True},{'junk':'s'}], '퀄리티 20%. 회피 및 에너지 보호막 % 1티어 분열 + 잡옵 1줄.', 'Quality 20%. Fractured T1 % evasion and energy shield plus one junk line.', 20),
 'diztoh-crit-helmet-v2-ess': _fb(('h2','h7'), [{'gi':9,'tmax':1,'fr':True},{'junk':'s'}], '퀄리티 20%. 회피 및 에너지 보호막 % 1티어 분열 + 잡옵 1줄.', 'Quality 20%. Fractured T1 % evasion and energy shield plus one junk line.', 20),
 'diztoh-socket-gloves': _fb(('d2','d6'), [{'gi':82,'fr':True},{'gi':8,'tmax':2},{'gi':57,'crafted':True},{'unrev':'p'}], '콜르의 사냥을 장착한 상태로 모든 투사체 스킬 레벨 +2 분열 + 에너지 보호막 최대치 + 희귀도(상위 풍요의 에센스) + 미공개 훼손 접두.', "Kolr's Hunt socketed: fractured +2 projectile skills, flat energy shield, rarity (Greater Essence of Opulence) and an unrevealed desecrated prefix.", None, [KOLR_]),
 'mazbro-sceptre': _fb(('z2','z6'), [{'gi':10,'tmax':1,'fr':True},{'junk':'s'}], '동료 피해 1티어 분열 + 잡옵 1줄.', 'Fractured T1 ally damage plus one junk line.'),
 'mazbro-spell5-amulet': _fb(('z2','z6'), [{'gi':28,'tmax':1,'fr':True},{'junk':'s'}], '정신력 +50 분열 + 잡옵 1줄.', 'Fractured +50 Spirit plus one junk line.'),
 'sl-flamewave-ring': _fb(('g2','g4'), [{'gi':7,'tmax':1,'fr':True},{'junk':'p'}], '모든 원소 저항 1티어 분열 + 잡옵 1줄.', 'Fractured T1 all elemental resistances plus one junk line.'),
}
for _r in R:
    _c = FRSTART.get(_r['id']) or (FRSTART.get(_r['tierGroup'][:-3]) if _r.get('tierGroup','').endswith('-v2') and _r['tierGroup'] not in FRSTART else None)   # grade recipes copied from an original in this table
    if not _c: continue
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
exec(open('/home/claude/poe2data/scripts/notes_short.py').read())
# "{#id}" in a step's text becomes that step's number, so cutting steps never leaves stale references
import re as _re
for _r in R:
    _no = {n['id']:i+1 for i,n in enumerate(_r['nodes'])}
    def _fix(v):
        if isinstance(v, str): return _re.sub(r'\{#(\w+)\}', lambda m: str(_no[m.group(1)]), v)
        if isinstance(v, dict): return {k:_fix(x) for k,x in v.items()}
        if isinstance(v, list): return [_fix(x) for x in v]
        return v
    _r['nodes'] = _fix(_r['nodes'])
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
# grades by difficulty (사용자 확정 2026-11-10): 어려움(3) 이하 = no High-end, 전문가(4) 이상 = no Essential
_gd={x['id']:x.get('difficulty',0) for x in R if x.get('tierGroup')==x['id']}   # the group's difficulty = its High-end recipe's
R[:]=[x for x in R if not (x.get('tierGroup') and ((_gd.get(x['tierGroup'],0)<=3 and x.get('tier')=='high') or (_gd.get(x['tierGroup'],0)>=4 and x.get('tier')=='ess')))]
REPLACES={'diztoh-budget-crossbow':'diztoh-grenade-crossbow','diztoh-crit-helmet-v2':'diztoh-crit-helmet','helmet-armour-sl-v2':'helmet-armour-sl','sihan-highend-boots-v2':'sihan-highend-boots','diztoh-rarity-ring-v2':'diztoh-rarity-ring','saveq-absent-amulet-v2':'saveq-absent-amulet','farmer-budget-armour-v2':'farmer-budget-armour','farmer-starter-staff-v2':'farmer-starter-staff','ragna-ashot-bow-v2-bal':'ragna-ashot-bow','sane-resist-belt-v2-bal':'sane-resist-belt','diztoh-budget-mace-v2-bal':'diztoh-budget-mace','lilbotq-budget-boots-v2-bal':'lilbotq-budget-boots','icesly-budget-wand-v2-bal':'icesly-budget-wand','diztoh-budget-mace-v2-ess':'diztoh-budget-2h-mace','diztoh-es-helmet-v2-bal':'diztoh-es-helmet','belton-plus8-wand-v2-bal':'belton-plus8-wand','lilbotq-armour-shield-v2-bal':'lilbotq-armour-shield','diztoh-vile-robe-v2-bal':'diztoh-vile-robe','diztoh-talisman-v2-bal':'diztoh-talisman','sihan-chayula-sceptre-v2-bal':'sihan-chayula-sceptre','diztoh-budget-crossbow-v2-bal':'diztoh-budget-crossbow','diztoh-onehand-mace-v2-bal':'diztoh-onehand-mace','saveq-alloy-focus-v2-bal':'saveq-alloy-focus','tankjung-kitava-shield-v2-bal':'tankjung-kitava-shield','ragna-spell4-amulet-v2-bal':'ragna-spell4-amulet','noble-visceral-quiver-v2':'noble-visceral-quiver','sihan-highend-helmet-v2':'sihan-highend-helmet','barricade-quarterstaff-v2':'barricade-quarterstaff','diztoh-endgame-quarterstaff-v2':'diztoh-endgame-quarterstaff','lilbotq-emerald-v2-bal':'lilbotq-emerald','zenm-timelost-sapphire-v2-bal':'zenm-timelost-sapphire','diztoh-5mod-emerald-v2-bal':'diztoh-5mod-emerald','diztoh-5mod-sapphire-v2-bal':'diztoh-5mod-sapphire','sl-5mod-jewel-v2-bal':'sl-5mod-jewel','vodnarg-timelost-emerald-v2-bal':'vodnarg-timelost-emerald','lilbotq-boots-v2-bal':'lilbotq-boots','mazbro-caster-ring-v2-bal':'mazbro-caster-ring','diztoh-as-spear-v2-bal':'diztoh-as-spear','diztoh-socket-gloves-v2-bal':'diztoh-socket-gloves','seek-cyclone-boots-v2-bal':'seek-cyclone-boots','diztoh-as-spear-v2-ess':'diztoh-twister-spear'}
_ids={x['id'] for x in R}|{x['tierGroup'] for x in R if x.get('tierGroup')}   # a group whose High-end was dropped still replaces its old recipe
R[:]=[x for x in R if not any(o==x['id'] and n in _ids for n,o in REPLACES.items())]
# policy 22: base price (Divine Orbs) from scripts/base_prices.py; None = not known yet
exec(open('/home/claude/poe2data/scripts/base_prices.py').read())
for _r in R:
    if BASEPRICE.get(_r['id']): _r['basePrice'] = BASEPRICE[_r['id']]
print('base price missing:', sum(1 for _r in R if not _r.get('basePrice')), 'of', len(R))
# flowchart + simulation (tools/sim/run.js → site/data/sim/<id>.json): the recipe tab shows its button only when the file exists
for _r in R:
    _sid=_r.get('tierGroup') or _r['id']
    if os.path.exists(f"{D}sim/{_sid}.json"):
        _r['sim'] = 1
        if _sid!=_r['id']: _r['simId'] = _sid
json.dump({'v':2,'recipes':R},open(D+'recipes.json','w'),ensure_ascii=False)
print(len(R),'recipes')
