# ---- MazBro "+5 Skill Amulet Craft Guide that PAYS FOR ITSELF" (youtu.be/kULlZJBSec4) ----
c='Amulets'
MZ5=K('MazBro 영상 기반','Based on MazBro')
def txA(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
z_spirit=txA('to Spirit','n','p'); z_spell=txA('Level of all Spell Skills','n','s'); z_maxQ=txA('to Maximum Quality','e','p')
z_ward=txA('increased maximum Runic Ward','e','p'); z_allq=txA('to Quality of all Skills','d','s')
z_cast=txA('increased Cast Speed','n','s'); z_crit=txA('increased Critical Hit Chance','n','s'); z_cdmg=txA('increased Critical Damage Bonus','n','s')
z_res=txA('to all Elemental Resistances','n','s'); z_rar=txA('increased Rarity of Items found','n','s')
IMP_Z=lambda lv:[K('스킬 부여: 레벨 %d 원소 상태 이상 시 시전'%lv,'Grants Skill: Level %d Cast on Elemental Ailment'%lv),K('접두어 속성 부여의 최대 개수 -1개\n접미어 속성 부여의 최대 개수 -1개','-1 Prefix Modifier allowed\n-1 Suffix Modifier allowed')]
R.append({
 'id':'mazbro-spell5-amulet','cls':c,'base':base(c,'Absent Amulet'),'ilvl':81,'imp':IMP_Z(12),'difficulty':4,'budget':'high',
 'buildTags':[K('주문','Spell'),K('정신력','Spirit'),K('룬 수호','Runic Ward')],'patch':'0.5.5','created':'2026-11-09','author':MZ5,
 'source':{'url':'https://www.youtube.com/watch?v=kULlZJBSec4','title':'+5 Skill Amulet Craft Guide that PAYS FOR ITSELF','channel':'MazBro'},
 'title':K('정신력 분열 + 주문 +3 + 룬 수호 (축성 +5 노리기)','fractured Spirit + spell +3 + Runic Ward (sanctify for +5)'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fr','kr':'정신력 분열','en':'Fracture Spirit'},{'id':'q','kr':'퀄리티 40%','en':'Quality to 40%'},
           {'id':'sk','kr':'주문 +3','en':'Spell +3'},{'id':'pre','kr':'접두 룬 수호','en':'Runic Ward prefix'},{'id':'suf','kr':'접미 훼손','en':'Suffix desecration'},
           {'id':'fin','kr':'성유 · 디바인 · 축성','en':'Anoint, Divine, sanctify'}],
 'nodes':[
  {'id':'z1','phase':'base','do':'base','cost':'base','ts':'8:40',
   'note':K('원하는 부여 스킬(원소 상태 이상 시 시전·치명타 시 시전·삼위일체 등)이 붙은 희귀 부재 목걸이. 타락·축성되지 않은 것, 아이템 레벨 75 이상(모든 원소 저항까지 보려면 82).','A rare Absent Amulet with the granted skill you want (Cast on Elemental Ailment, Cast on Critical, Trinity…), not corrupted or sanctified, item level 75+ (82 if you want all elemental resistances).')},
  {'id':'z2','phase':'base','do':'chaos','cur':'Chaos_Orb','target':{'gi':z_spirit,'tmax':1},'fail':{'goto':'self'},'after':{'keepOnly':[z_spirit]},'ts':'9:20',
   'note':K('카오스 오브로 정신력 1티어. 나온 뒤 소멸의 오브로 정신력만 남김. 도중에 주문 스킬 +3이 접두 하나와 뜨면 그대로 팔아도 이득(영상 140디바인).','Chaos for T1 Spirit, then annul down to Spirit alone. If +3 spell skills shows up with a single prefix on the way, selling it as is pays (140 divines in the video).')},
  {'id':'z3','phase':'base','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':z_spirit}},'fail':{'goto':'self'},'ts':'10:20',
   'note':K('신성한 오브로 정신력 +50까지.','Divine Spirit up to +50.')},
  {'id':'z4','phase':'fr','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},'ts':'11:15',
   'note':K('상위 찬미의 징조 + 상위 엑잘티드 오브로 두 줄(무엇이든 상관없음).','Greater Exaltation + Greater Exalted Orb for two lines (anything).')},
  {'id':'z5','phase':'fr','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'s'},'ts':'11:30',
   'note':K('남은 자리를 빗장뼈로 훼손(고대 빗장뼈 필요 없음)해 4줄. 훼손은 분열되지 않아서 정신력 분열이 1/3.','Fill the last slot with any Collarbone (no need for Ancient): four lines. Desecrations cannot fracture, so Spirit is 1 in 3.')},
  {'id':'z6','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':z_spirit}]},'fail':{'goto':'restart'},'after':{'keepOnly':[z_spirit,'junk1']},'ts':'11:40',
   'note':K('정신력 분열(1/3). 실패 대비로 목걸이 3개쯤 미리 준비(영상 3개 중 2개 성공). 이후 소멸의 오브로 분열 + 한 줄만 남김.','Fracture Spirit (1 in 3); prepare about three amulets (2 of 3 hit in the video). Then annul down to the fracture plus one line.')},
  {'id':'z7','phase':'q','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':z_maxQ},'ts':'12:10',
   'note':K('균열의 에센스: 남은 한 줄이 지워지고 최대 퀄리티 +20%.','Essence of the Breach: the one other line goes and +20% maximum quality comes on.')},
  {'id':'z8','phase':'q','do':'quality','cur':'Sibilant_Catalyst','target':{'quality':40},'ts':'12:40',
   'note':K('쇳소리 기폭제로 시전 퀄리티 40%. 34%면 주문 +3이 +4가 되고, 40%는 시전 속도 같은 다른 시전 옵션까지 챙기려는 것.','Sibilant Catalysts to 40% caster quality: 34% already turns +3 into +4; 40% also boosts other caster lines such as cast speed.')},
  {'id':'z9','phase':'sk','do':'chaos','cur':'Chaos_Orb','target':{'gi':z_spell,'tmax':1,'removeGi':z_maxQ},'fail':{'goto':'self'},'ts':'13:40',
   'note':K('카오스 오브로 주문 스킬 +3(약 1/1000, 카오스 오브 약 1,000개). 최대 퀄리티 줄은 첫 카오스에 바뀌어도 퀄리티 수치는 남음. 시전 속도·치명타·치명타 피해 1티어처럼 드문 접미가 뜨면 상위 엑잘티드 오브로 주문 +3을 한 번 노려 보고, 안 되면 소멸의 오브 후 다시 카오스.','Chaos for +3 spell skills (about 1 in 1,000, roughly 1,000 Chaos). Losing the maximum quality line on the first Chaos is fine; the quality value stays. If a rare suffix like T1 cast speed, crit or crit damage lands, try one Greater Exalted Orb for +3, otherwise annul and back to Chaos.')},
  {'id':'z9b','phase':'sk','do':'note','label':K('실험: 촉진 엑잘','Experiment: catalysing slams'),'ts':'17:40',
   'note':K('영상 실험: 정신력 분열 + 최대 퀄리티 상태에서 시전 퀄리티 40% → 촉진하는 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 주문 +3·시전 속도를 노림(한 번에 약 20디바인, 절반쯤 성공). 퀄리티가 0%가 되니 실패하면 기폭제를 40%로 다시 채운 뒤 소멸의 오브(최대 퀄리티가 지워지면 균열의 에센스로 다시). 이렇게 끝낸 목걸이는 퀄리티를 40%로 채우고 절사의 징조 + 상위 카오스 오브로 최대 퀄리티를 바꾼 뒤, 접미 잡옵은 우측 강령술의 징조 + 고대 빗장뼈로 1/2 도박(주문 +3이 지워지면 처음부터).','The video\'s experiment: with fractured Spirit and maximum quality, 40% caster quality → Catalysing Exaltation + Perfect Exalted Orb for +3 spell / cast speed on the suffixes (about 20 divines a try, roughly half hit). Quality drops to 0%, so refill to 40% before annulling a miss (re-add maximum quality with the Breach essence if it goes). Amulets finished this way refill to 40%, swap maximum quality with Whittling + Greater Chaos, then gamble Dextral Necromancy + Ancient Collarbone on the junk suffix (1/2; losing +3 means starting over).')},
  {'id':'z10','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'26:40',
   'note':K('좌측 찬미의 징조 + 상위(또는 완벽한) 엑잘티드 오브로 접두 한 줄. 좋은 줄이면 다음 단계를 건너뜀. 다른 징조가 켜져 있지 않은지 꼭 확인.','Sinistral Exaltation + Greater (or Perfect) Exalted Orb for one prefix; a good one skips the next step. Make sure no other omen is active.')},
  {'id':'z11','phase':'pre','do':'essence','cur':'Runic_Alloy','target':{'gi':z_ward},'ts':'25:40',
   'note':K('룬 합금으로 그 접두를 룬 수호 최대치 % 증가로 바꿈(접두가 꽉 차 있어 접두 줄이 지워짐, 영상은 좌측 결정화의 징조도 켬). 최대 퀄리티(제작 옵션)가 남아 있으면 합금을 못 씀. 룬 수호를 안 쓰면 완벽한 강화의 에센스(방어 % 증가).','Runic Alloy turns that prefix into increased maximum Runic Ward (prefixes are full, so a prefix goes; the video also uses Sinistral Crystallisation). It cannot go on while maximum quality (crafted) is still there. Without Runic Ward, a Perfect Essence of Enhancement (% global defences).')},
  {'id':'z12','phase':'suf','do':'desecrate','cur':'Ancient_Collarbone','target':{'unrev':'s'},'ts':'29:00',
   'note':K('남은 접미를 고대 빗장뼈로 훼손. 빛의 징조·심연의 메아리의 징조·소멸의 오브 개수를 늘 같게 맞춰 둠(소멸의 오브가 남으면 주문 +3이 지워질 수 있음).','Desecrate the last suffix with an Ancient Collarbone. Keep Omens of Light, Abyssal Echoes and Annulments in equal numbers (a spare Annulment can wipe the +3).')},
  {'id':'z13','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':z_allq},{'gi':z_cast,'tmax':1},{'gi':z_crit},{'gi':z_cdmg},{'gi':z_res},{'gi':z_rar}]},'side':'s','bone':'Ancient_Collarbone'},'fail':{'goto':'z12','via':LIGHT},'ts':'29:15',
   'note':K('심연의 메아리의 징조로 공개해 모든 스킬 퀄리티 / 시전 속도 / 치명타 / 치명타 피해 / 모든 원소 저항 / 희귀도. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시.','Reveal with Abyssal Echoes for quality of all skills, cast speed, crit, crit damage, all resistances or rarity; otherwise Light + Annulment and desecrate again.')},
  {'id':'z14','phase':'fin','do':'manual','label':K('성유: 자로크의 선물 할당','Anoint: Zarokh\'s Gift'),'target':{'anoint':K('자로크의 선물','Zarokh\'s Gift')},'ts':'30:00',
   'note':K('성유로 자로크의 선물(또는 지배 등 인기 노드). 실패해도 빨리 팔림.','Anoint Zarokh\'s Gift (or another popular notable such as Dominion) so even a miss sells fast.')},
  {'id':'z15','phase':'fin','do':'manual','label':K('부여 스킬 20레벨 · 5홈','Granted skill level 20, five sockets'),'target':{'imp':IMP_Z(20)},'ts':'30:20','extra':{'Perfect_Flux':1,'Perfect_Jewellers_Orb':1},
   'note':K('완벽한 유동체로 부여 스킬 20레벨, 완벽한 쥬얼러 오브로 5홈. 이걸 빼고 축성하면 쓸모없는 목걸이가 됨.','Perfect Flux for a level 20 granted skill and Perfect Jeweller\'s Orbs for five sockets. Sanctifying without them ruins the amulet.')},
  {'id':'z16','phase':'fin','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':z_ward}},'fail':{'goto':'self'},'ts':'31:00',
   'note':K('축성은 지금 수치 기준이라 신성한 오브로 모든 줄을 최대 수치로(평균 약 20번).','Sanctifying starts from the current values, so Divine every line to max (about 20 Divines on average).')},
  {'id':'z17','phase':'fin','do':'manual','label':K('축성 (주문 +4 → +5)','Sanctify (+4 → +5 spell)'),'target':{'sanctify':True,'vals':{str(z_spell):K('모든 주문 스킬 레벨 +5','+5 to Level of all Spell Skills')}},'ts':'31:50',
   'note':K('축성의 징조 + 신성한 오브. 체크: 성유, 5홈, 부여 스킬 20레벨, 퀄리티 34% 이상, 수치 최대. +5는 약 13%라 목걸이 여러 개로 시도(영상은 약 15번째에 +5). +3이 +2로 떨어지지만 않으면 실패작도 팔아서 본전 근처.','Omen of Sanctification + Divine Orb. Checklist: anointed, five sockets, level 20 skill, 34%+ quality, max values. +5 is about 13%, so sanctify several amulets (the video hit on about the fifteenth). Misses that do not drop to +2 still sell near cost.')},
  {'id':'z18','phase':'fin','do':'note','ts':'37:45',
   'note':K('완성. 영상 완성품: 부재 목걸이, 퀄리티(시전) 40%, 자로크의 선물 할당, 원소 상태 이상 시 시전 20레벨 / 정신력 +50 · 룬 수호 최대치 10% 증가 / 모든 주문 스킬 +5 · 모든 스킬 퀄리티 +4%, 축성.','Done. The video\'s amulet: Absent Amulet, 40% caster quality, Zarokh\'s Gift, level 20 Cast on Elemental Ailment / +50 Spirit, 10% increased maximum Runic Ward / +5 all spell skills, +4% quality of all skills, sanctified.')},
 ],
})
