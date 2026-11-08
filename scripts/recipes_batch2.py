# Ten recipes from MazBro and Diztoh videos (built 2026-11-08). Exec'd from build_recipes.py, so g/base/K/LIGHT/R are in scope.
MZ=K('MazBro 영상 기반','Based on MazBro'); DZ=K('Diztoh 영상 기반','Based on Diztoh')
def src(vid,title,ch): return {'url':'https://www.youtube.com/watch?v='+vid,'title':title,'channel':ch}
ANNUL={'cur':'Orb_of_Annulment'}
SANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}
DANN={'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']}

# ---------- 1. MazBro: BiS caster ring (Mnemonic Ring) ----------
c='Rings'
r_cast=g(c,'increased Cast Speed','n','s'); r_mana=g(c,'to maximum Mana','n','p'); r_regen=g(c,'(60—69)% increased Mana Regeneration','n','s')
r_rar=g(c,'Rarity of Items found','n','s'); r_res=g(c,'to all Elemental Resistances','n','s'); r_maxQ=g(c,'to Maximum Quality','e','p')
r_pmana=g(c,'increased maximum Mana','e','p'); r_mbl=g(c,'Mana before Life','x','p')
R.append({
 'id':'mazbro-caster-ring','cls':c,'base':base(c,'Mnemonic Ring'),'ilvl':82,'difficulty':2,'budget':'medium',
 'buildTags':[K('마나','Mana'),K('주문','Spell'),K('토템','Totem')],'patch':'0.5.5','created':'2026-11-08','author':MZ,
 'source':src('o3Fh1DJmxBA','Crafting caster rings the cheap way (PoE2)','MazBro'),
 'title':K('시전 속도 분열 + 마나 1티어 캐스터 반지','fractured cast speed + T1 mana caster ring'),
 'note':K('평균 약 100신성한 오브로 만들어 300~800디바인에 팔리는 반지. 필수 옵션은 마나 최대치 1티어와 마나 최대치 % 8%(마나 퀄리티 반영), 시전 속도는 분열로 고정. 나머지 줄은 욕심내지 말고 적당한 데서 멈추고 새 반지를 시작하는 게 이득. 황금 반지로도 같은 방법이 됨.',
          'A ring that costs about 100 divines to make and sells for 300–800. Must-haves: T1 flat mana and 8% increased maximum mana (with mana quality); cast speed is locked by the fracture. Do not force the other lines: settle and start a new ring. Works on Gold Rings too.'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fr','kr':'시전 속도 분열','en':'Fracture cast speed'},{'id':'q','kr':'퀄리티 41%','en':'Quality to 41%'},
           {'id':'roll','kr':'카오스 · 마나','en':'Chaos and mana'},{'id':'fill','kr':'나머지 · 훼손','en':'Fill and desecrate'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'r1','phase':'base','do':'base','cost':'base','ts':'3:33',
   'note':K('아이템 레벨 82 희귀 기억 반지. 제작·훼손 옵션이 없는 것만, 옵션 4줄 이하에 접두 하나가 있으면 가장 좋음. 시전 속도 22~24%(1티어)가 이미 붙은 반지를 사면 다음 단계는 건너뜀.','An item level 82 rare Mnemonic Ring with no crafted or desecrated mods, four lines or fewer, ideally one prefix. Buying one that already has 22–24% cast speed (T1) skips the next step.')},
  {'id':'r1b','phase':'base','do':'chaos','cur':'Chaos_Orb','target':{'gi':r_cast,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'3:33',
   'note':K('카오스 오브(재련)로 시전 속도 1티어(22~24%). 24가 아니면 나중에 신성한 오브로 맞춤.','Chaos (reroll) for T1 cast speed (22–24%). Divine it to 24 later if needed.')},
  {'id':'r2','phase':'fr','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'4:26',
   'note':K('소멸의 오브로 4줄 이하로 맞추고 훼손 한 줄로 4줄 채움. 훼손은 분열되지 않음.','Annul down to four lines or fewer and fill with one desecration, which cannot fracture.')},
  {'id':'r3','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':r_cast}]},'fail':{'goto':'restart'},'ts':'7:15',
   'after':{'keepOnly':[r_cast]},
   'note':K('시전 속도 분열 1/3. 실패하면 다음 반지로(베이스가 싸서 여러 개를 한꺼번에 작업). 이후 분열만 남김.','Cast speed fractures 1 in 3; on a miss move to the next ring (bases are cheap, craft in batches). Keep only the fracture.')},
  {'id':'r4','phase':'q','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'11:51',
   'note':K('다른 옵션이 없으면 접두에 아무 옵션 하나.','If nothing else is left, any prefix.')},
  {'id':'r5','phase':'q','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':r_maxQ},'ts':'11:51',
   'note':K('좌측 결정화의 징조 + 균열의 에센스로 최대 퀄리티 +20%.','Sinistral Crystallisation + Essence of the Breach: +20% maximum quality.')},
  {'id':'r6','phase':'q','do':'quality','cur':'Neural_Catalyst','target':{'quality':40},'ts':'12:30',
   'note':K('신경 기폭제(마나 퀄리티)로 40%.','Neural Catalysts (mana quality) to 40%.')},
  {'id':'r7','phase':'q','do':'manual','cost':'vaal','target':{'setQuality':41},'label':K('주입기 1회로 41%','One infuser to 41%'),
   'note':K('촉진시키는 주입기를 딱 한 번만. 첫 번째 주입기는 타락 확률이 0%라서 안전.','Exactly one infuser: the first one has no corruption chance.')},
  {'id':'r8','phase':'roll','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':r_regen,'tmax':1},{'gi':r_rar,'tmax':1},{'gi':r_res,'tmax':1}],'removeGi':r_maxQ},'fail':{'goto':'self'},'ts':'13:34',
   'note':K('카오스 오브로 마나 재생 1티어 / 희귀도 1티어 / 모든 원소 저항 1티어(마나 최대치 1티어가 먼저 떠도 좋음). 최대 퀄리티 줄은 여기서 날아가도 퀄리티 수치는 유지.','Chaos for T1 mana regeneration, T1 rarity or T1 all resistances (T1 flat mana first is also great). Losing the maximum quality line is fine; the quality value stays.')},
  {'id':'r9','phase':'roll','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':r_mana,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Essence_of_the_Mind','omens':['Omen_of_Sinistral_Crystallisation']}},'ts':'13:34',
   'note':K('상위 엑잘티드 오브(좌측 찬미의 징조)로 접두에 마나 최대치 1티어. 빗나가면 좌측 결정화의 징조 + 정신의 에센스로 그 접두를 마나 % 증가로 바꾸고 한 번 더. 그래도 없으면 마지막에 고대 빗장뼈로 노림.','Greater Exalt (Sinistral) for T1 flat mana. On a miss, Sinistral Crystallisation + Essence of the Mind turns that prefix into % maximum mana for one more try; otherwise go for it with an Ancient Collarbone at the end.')},
  {'id':'r10','phase':'roll','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'13:34','note':K('접두 하나(에센스가 바꿀 자리).','One prefix for the essence to replace.')},
  {'id':'r10b','phase':'roll','do':'essence','cur':'Essence_of_the_Mind','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':r_pmana},'ts':'13:34',
   'note':K('좌측 결정화의 징조 + 정신의 에센스: 마나 최대치 % 증가(퀄리티 반영 8%가 필수).','Sinistral Crystallisation + Essence of the Mind: % increased maximum mana (8% with quality is a must).')},
  {'id':'r11','phase':'fill','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'20:00',
   'note':K('남은 접미를 채움. 이 단계는 운: 나쁜 게 붙으면 욕심내지 말고 소멸의 오브 후 다시 하거나 새 반지로.','Fill the last suffix. Pure luck: on bad rolls annul and redo or start a new ring.')},
  {'id':'r12','phase':'fill','do':'desecrate','cur':'Altered_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'29:15',
   'note':K('마나 최대치 1티어가 있으면 뒤바뀐 빗장뼈로 접두에 "받는 피해를 생명력 대신 마나로 소모" 노림(토템 빌드 최고 옵션). 1티어 마나가 없으면 고대 빗장뼈로 마나 최대치를 노림.','With T1 flat mana, an Altered Collarbone on the prefix aims for Mana before Life (best for totems). Without it, an Ancient Collarbone aims for flat mana.')},
  {'id':'r13','phase':'fill','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':r_mbl}]},'side':'p','bone':'Altered_Collarbone'},'unknownW':True,'fail':{'goto':'r12','via':LIGHT},'ts':'29:15',
   'note':K('공개해서 받는 피해를 생명력 대신 마나로 소모. 아니면 빛의 징조 + 소멸의 오브로 지우고 다시. 소멸의 오브는 빛의 징조보다 많이 들고 다니지 말 것.','Reveal for Mana before Life; otherwise Light + Annulment and retry. Never carry more Annulments than Omens of Light.')},
  {'id':'r14','phase':'fin','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':r_pmana}},'fail':{'goto':'self'},'ts':'37:30',
   'note':K('신성한 오브로 마나 최대치 %를 8%(퀄리티 반영)까지. 이후 축복받은 자의 징조 + 신성한 오브로 고정 옵션도 8%. 저항은 유동체로 원소를 바꿔 수치를 맞출 수 있음.','Divine increased maximum mana to 8% (with quality), then Omen of the Blessed + Divine for the implicit at 8%. Resistances can be fluxed to another element to fix rolls.')},
  {'id':'r15','phase':'fin','do':'note','ts':'41:00',
   'note':K('완성. 영상 판매가 300~800디바인. 빨리 팔려면 살짝 싸게.','Done. The video\'s rings sold for 300–800 divines; undercut a little to sell fast.')},
 ]})

# ---------- 2. MazBro: BiS caster amulet (Solar Amulet) ----------
c='Amulets'
m_spirit=g(c,'to Spirit','n','p'); m_spell=g(c,'Level of all Spell Skills','n','s'); m_maxQ=g(c,'to Maximum Quality','e','p')
m_cast=g(c,'increased Cast Speed','n','s'); m_crit=g(c,'increased Critical Hit Chance','n','s'); m_cdmg=g(c,'increased Critical Damage Bonus','n','s')
m_pmana=g(c,'increased maximum Mana','n','p'); m_mana=g(c,'to maximum Mana','n','p'); m_sdmg=g(c,'increased Spell Damage','n','p'); m_rar=g(c,'Rarity of Items found','n','p')
m_regen=g(c,'Life Regeneration per second','n','s'); m_int=g(c,'to Intelligence','n','s'); m_allq=g(c,'Quality of all Skills','d','s')
R.append({
 'id':'mazbro-caster-amulet','cls':c,'base':base(c,'Solar Amulet'),'ilvl':82,'difficulty':4,'budget':'high',
 'buildTags':[K('주문','Spell'),K('정신력','Spirit'),K('마나','Mana')],'patch':'0.5.5','created':'2026-11-08','author':MZ,
 'source':src('4PazhuHwdL8','How to Craft a Best-in-Slot Caster Amulet (One Sold for 3000 Div)','MazBro'),
 'title':K('정신력 분열 + 주문 +3 BiS 캐스터 목걸이','fractured Spirit + spell +3 BiS caster amulet'),
 'note':K('접두 = 정신력 +50(분열) + 마나 % / 마나 최대치 / 주문 피해 / 희귀도 1티어 중 2개(제작자 선호: 마나 최대치 + 마나 %), 접미 = 주문 스킬 +3 + 시전 속도·치명타·치명타 피해 중 1개 + 모든 스킬 퀄리티 +5%(훼손). 영상 목걸이 하나가 약 3,000디바인, 전부 1티어면 미러 1~2개. 퀄리티 종류를 단계마다 바꿔 촉진하는 찬미의 징조로 원하는 쪽을 노리는 게 핵심.',
          'Prefixes: fractured +50 Spirit plus two of T1 % mana, flat mana, spell damage or rarity (the author prefers flat mana + % mana). Suffixes: +3 spell skills, one of cast speed / crit chance / crit damage, and a desecrated +5% quality of all skills. One sold for about 3,000 divines; full T1 goes for 1–2 mirrors. The trick is switching quality type per step so Catalysing Exaltation favours the side you want.'),
 'start':{'rar':'rare','mods':[{'gi':m_spirit,'tmax':1},{'junk':'s'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fr','kr':'정신력 분열','en':'Fracture Spirit'},{'id':'sk','kr':'주문 +3','en':'Spell +3'},{'id':'block','kr':'훼손 막기 · 접미','en':'Block and suffix'},
           {'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'a1','phase':'base','do':'base','cost':'base','ts':'1:34',
   'note':K('아이템 레벨 82 태양의 목걸이(또는 황금 목걸이), 정신력 +50(1티어). 50 근처면 신성한 오브로 맞춤.','An item level 82 Solar (or Gold) Amulet with +50 Spirit (T1); divine it to 50 if close.')},
  {'id':'a2','phase':'fr','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'2:33',
   'note':K('소멸의 오브로 4줄 이하로 맞추고 훼손으로 4줄. 정신력 분열 1/3.','Annul to four lines or fewer and desecrate to four; Spirit fractures 1 in 3.')},
  {'id':'a3','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':m_spirit}]},'fail':{'goto':'restart'},'ts':'2:33','after':{'keepOnly':[m_spirit,'junk1']},
   'note':K('정신력 분열 후 분열 + 한 줄만 남김.','Fracture Spirit, then keep the fracture plus one line.')},
  {'id':'a4','phase':'sk','do':'chaos','cur':'Chaos_Orb','target':{'gi':m_spell,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'5:07','after':{'keepOnly':[m_spirit,m_spell]},
   'note':K('카오스 오브로 주문 스킬 +3. 근접·소환수·투사체 +3이 뜨면 그 상태로 판매(80~90디바인) 후 새로 시작.','Chaos for +3 spell skills. If +3 melee, minion or projectile lands instead, sell it as is (80–90 divines) and start a new one.')},
  {'id':'a5','phase':'sk','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'12:01','note':K('접두에 엑잘티드 오브 하나.','Exalt one prefix.')},
  {'id':'a6','phase':'sk','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':m_maxQ},'ts':'12:01',
   'note':K('좌측 결정화의 징조 + 균열의 에센스로 그 접두를 최대 퀄리티 +20%로 교체.','Sinistral Crystallisation + Essence of the Breach turns that prefix into +20% maximum quality.')},
  {'id':'a7','phase':'block','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'13:16',
   'note':K('우측 강령술의 징조 + 보존된 빗장뼈로 접미 훼손.','Dextral Necromancy + Preserved Collarbone desecrates a suffix.')},
  {'id':'a8','phase':'block','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':m_regen},{'gi':m_int}]},'side':'s','bone':'Preserved_Collarbone'},'fail':{'goto':'a7','via':LIGHT},'ts':'13:16',
   'note':K('가중치 높은 옵션으로 자리를 막음: 생명력 재생 → 힘·지능·민첩·원소 저항 → 모든 능력치 순. 이렇게 막아 두면 다음 엑잘티드 오브가 원하는 옵션에 붙을 확률이 오름. 없으면 빛의 징조로 지우고 다시.','Block with a high-weight mod: life regeneration, then a single attribute or resistance, then all attributes. That raises the next slam\'s odds. If none show, Omen of Light and redo.')},
  {'id':'a9','phase':'block','do':'quality','cur':'Skittering_Catalyst','target':{'quality':40},'ts':'13:16',
   'note':K('달리는 기폭제로 속도 퀄리티 40%(쇳소리 기폭제보다 싸면). 촉진하는 찬미의 징조가 속도 옵션(시전 속도)을 밀어 줌.','40% speed quality (if cheaper than caster). Catalysing Exaltation then favours speed mods (cast speed).')},
  {'id':'a10','phase':'block','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':m_cast,'tmax':1},{'gi':m_crit,'tmax':1},{'gi':m_cdmg,'tmax':1}]},'unknownW':True,'fail':{'goto':'self','via':ANNUL},'ts':'13:16',
   'note':K('촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 접미에 시전 속도 / 치명타 / 치명타 피해. 마음에 안 들면 퀄리티를 다시 올리고 소멸의 오브: 주문 +3이 지워지면 4번부터, 훼손이 지워지면 7번부터.','Catalysing + Dextral Exaltation + Perfect Exalt for cast speed, crit chance or crit damage. On a bad hit, re-add quality and annul: if +3 goes, back to step 4; if the desecration goes, back to step 7.')},
  {'id':'a11','phase':'pre','do':'quality','cur':'Neural_Catalyst','target':{'quality':40},'ts':'17:03',
   'note':K('신경 기폭제로 마나 퀄리티 40%로 바꿔서 접두 마나 옵션을 밀어 줌.','Switch to 40% mana quality to favour mana prefixes.')},
  {'id':'a12','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':m_pmana,'tmax':1},{'gi':m_mana,'tmax':1},{'gi':m_sdmg,'tmax':1}]},'fail':{'goto':'self','via':SANN},'ts':'17:03',
   'note':K('촉진하는 찬미의 징조 + 완벽한 엑잘티드 오브. 가장 좋은 건 마나 % 1티어(가중치 300, 절사의 징조로 노리기 가장 어려움). 마나 최대치·주문 피해 1티어도 OK. 둘 다 아니면 좌측 소멸의 징조(최대 퀄리티가 지워지면 균열의 에센스로 다시 붙이고 반복).','Catalysing Exaltation + Perfect Exalt. Best is T1 % mana (weight 300, hardest to whittle into); T1 flat mana or spell damage are fine. Otherwise Sinistral Annul (if max quality goes, re-add it with the Breach essence and repeat).')},
  {'id':'a13','phase':'pre','do':'quality','cur':'Sibilant_Catalyst','target':{'quality':40},'ts':'17:03',
   'note':K('아주 중요: 쇳소리 기폭제로 시전 퀄리티 34% 또는 40%로 바꿈. 주문 +3이 +4가 됨.','Very important: switch to 34% or 40% caster quality; +3 becomes +4.')},
  {'id':'a14','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':[{'gi':m_mana,'tmax':1},{'gi':m_sdmg,'tmax':1},{'gi':m_rar,'tmax':1}],'removeGi':m_maxQ},'fail':{'goto':'self'},'ts':'17:03',
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티 줄을 날리고 남은 접두 노림. 필요하면 좌측 말소의 징조(아주 비쌈). 훼손 옵션 레벨이 가장 낮은 접미보다 낮으면 먼저 빛의 징조로 더 높은 레벨 훼손으로 바꿔 둠(시전 62·치명타 72·치명타 피해 74). 마나 최대치 1티어(레벨 82)는 절사의 징조에 안 지워짐. 적당한 조합이면 멈춤.','Whittling + Perfect Chaos replaces the max-quality line and hunts the last prefix; Sinistral Erasure if needed (very expensive). If the desecration is lower level than your lowest suffix, swap it for a higher-level one first (cast speed 62, crit 72, crit damage 74). T1 flat mana (level 82) never gets whittled. Settle for any good combo.')},
  {'id':'a15','phase':'fin','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'26:45','note':K('막아 둔 훼손 옵션을 빛의 징조 + 소멸의 오브로 제거.','Remove the blocking desecration with Light + Annulment.')},
  {'id':'a16','phase':'fin','do':'desecrate','cur':'Ancient_Collarbone','omens':['Omen_of_the_Blackblooded'],'target':{'unrev':'s'},'ts':'26:45','note':K('고대 빗장뼈 + 검은 피의 징조로 쿠르갈 옵션.','Ancient Collarbone + Omen of the Blackblooded for a Kurgal mod.')},
  {'id':'a17','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':m_allq},'side':'s','lord':'kurgal','bone':'Ancient_Collarbone'},'fail':{'goto':'a16','via':LIGHT},'ts':'26:45',
   'note':K('모든 스킬 퀄리티 +5% 노림(다른 좋은 옵션도 OK).','Aim for +5% quality of all skills (anything good is fine).')},
  {'id':'a18','phase':'fin','do':'note','ts':'29:10',
   'note':K('신성한 오브로 수치를 올리고 축복받은 자의 징조로 고정 옵션 정신력 15. 완성.','Divine the rolls and use Omen of the Blessed for 15 Spirit on the implicit. Done.')},
 ]})

# ---------- 3. MazBro: BiS chest (Conjurer Mantle) ----------
c='Body_Armours_str_int'
b_spirit=g(c,'to Spirit','n','p'); b_ispirit=g(c,'increased Spirit','x','p'); b_imana=g(c,'increased maximum Mana','x','p')
b_hfire=g(c,'to Fire and Chaos Resistances','x','s'); b_hcold=g(c,'to Cold and Chaos Resistances','x','s'); b_hlight=g(c,'to Lightning and Chaos Resistances','x','s')
b_regen=g(c,'Life Regeneration per second','n','s'); b_mbl=g(c,'Mana before Life','d','s'); b_sre=g(c,'Spirit Reservation Efficiency','d','s')
R.append({
 'id':'mazbro-bis-chest','cls':c,'base':base(c,'Conjurer Mantle'),'ilvl':82,'difficulty':5,'budget':'high','unknownW':True,
 'buildTags':[K('정신력','Spirit'),K('마나','Mana'),K('토템','Totem')],'patch':'0.5.5','created':'2026-11-08','author':MZ,
 'source':src('LUB59xlkNtk','I Made 3 MIRRORS Crafting This BiS Chest','MazBro'),
 'title':K('정신력 분열 + 복합 저항 2줄 BiS 갑옷','fractured Spirit + double hybrid res BiS chest'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fr','kr':'정신력 분열','en':'Fracture Spirit'},{'id':'pre','kr':'접두 2줄','en':'Two prefixes'},{'id':'suf','kr':'복합 저항 접미','en':'Hybrid res suffixes'},{'id':'fin','kr':'훼손 · 마무리','en':'Desecration and finish'}],
 'nodes':[
  {'id':'c1','phase':'base','do':'base','cost':'base','ts':'1:39',
   'note':K('요술사 외투(고정 옵션 정신력 +30, 가장 추천), 깃털 의복(받는 피해를 생명력 대신 마나로 소모 고정 옵션), 끔찍한 로브(에너지 보호막 최고) 중 하나.','Conjurer Mantle (+30 Spirit implicit, the author\'s favourite), Feathered Raiment (Mana before Life implicit) or Vile Robe (highest ES).')},
  {'id':'c2','phase':'fr','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':b_spirit,'tmax':1},'knownP':True,'fail':{'goto':'self','via':ANNUL},'ts':'3:33',
   'note':K('완벽한 진화·확장의 오브 + 소멸의 오브 반복으로 정신력 1티어.','Perfect Transmute, Perfect Augment and annul for T1 Spirit.')},
  {'id':'c3','phase':'fr','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'s'},'ts':'3:33','note':K('완벽한 제왕의 오브로 희귀.','Regal to rare.')},
  {'id':'c4','phase':'fr','do':'exalt','cur':'Exalted_Orb','target':{'junk':'s'},'ts':'3:33','note':K('분열에 필요한 줄 수를 맞춤.','Bring the line count up for the fracture.')},
  {'id':'c5','phase':'fr','do':'desecrate','cur':'Preserved_Rib','target':{'unrev':'p'},'ts':'3:33','note':K('보존된 갈비뼈로 훼손: 4줄, 정신력 분열 1/3.','Desecrate with a Preserved Rib: four lines, Spirit fractures 1 in 3.')},
  {'id':'c6','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':b_spirit}]},'fail':{'goto':'restart'},'ts':'3:33','after':{'keepOnly':[b_spirit]},
   'note':K('정신력 분열 후 분열만 남기고 소멸의 오브.','Fracture Spirit, then annul down to just the fracture.')},
  {'id':'c7','phase':'pre','do':'manual','target':{'rune':K('영혼 핵: 메드베드의 보살핌','Soul core: Medved\'s Tending')},'label':K('영혼 핵 장착','Socket the soul core'),'ts':'5:55',
   'note':K('마나 %·정신력 %·복합 저항 옵션을 여는 영혼 핵을 소켓에 장착(소켓에 묶임, poe2db에서 확인).','Socket the soul core that unlocks the % mana, % Spirit and hybrid resistance mods (socket-bound; check poe2db).')},
  {'id':'c8','phase':'pre','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':b_ispirit},{'gi':b_imana}]},'fail':{'goto':'self','via':SANN},'ts':'5:55',
   'note':K('카오스 오브나 좌측 찬미의 징조 + 엑잘티드 오브로 정신력 % 또는 마나 %. 실패하면 소멸의 오브. 엑잘티드 오브·소멸의 오브·카오스 오브 반복.','Chaos, or Sinistral Exaltation + Exalt, for % Spirit or % mana. On a miss annul. Slam, annul, chaos.')},
  {'id':'c9','phase':'pre','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':b_imana},{'gi':b_ispirit}]},'fail':{'goto':'self','via':SANN},'ts':'5:55',
   'note':K('남은 하나. 제작자는 접두 2줄에만 3일이 걸림.','The other one. The prefixes alone took the author three days.')},
  {'id':'c12','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':b_hfire},{'gi':b_hcold},{'gi':b_hlight}]},'fail':{'goto':'self','via':{'cur':'Essence_of_the_Abyss','omens':['Omen_of_Dextral_Crystallisation']}},'ts':'12:23',
   'note':K('완벽한 엑잘티드 오브(영상은 상위 찬미의 징조로 두 줄씩)로 접미에 복합 저항 첫 줄. 완벽한 엑잘티드 오브는 레벨 50 이상만 굴러서 접미 가중치가 약 7만 → 약 2.8만으로 줄어듦. 잡옵 제거는 싼 순서: 심연의 에센스 + 우측 결정화의 징조(약 1디바인) → 우측 소멸의 징조 → 절사의 징조는 맞는 줄을 고를 때만. 심연의 에센스는 훼손 옵션이 있는 아이템엔 안 먹히니, 막기 훼손을 붙이기 전인 지금 단계에서 씀.','Perfect Exalt (the video doubles up with Greater Exaltation) for the first hybrid. Perfect Exalts only roll level 50+ mods, cutting the suffix pool from about 70.5k weight to about 28k. Remove junk the cheapest way: Essence of the Abyss + Dextral Crystallisation (~1 div), then Dextral Annul; Whittling only when it hits the right line. Essence of the Abyss does not work on an item with a desecrated mod, so use it now, before the blocking desecration.')},
  {'id':'c10','phase':'suf','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'8:49',
   'note':K('접미 준비물: 우측 소멸의 징조 + 빛의 징조를 함께 켜 두는 안전장치(소멸의 오브가 엉뚱한 줄을 못 지움), 우측 결정화의 징조, 심연의 에센스, 절사의 징조 + 완벽한 카오스 오브, 보존된 갈비뼈, 심연의 메아리의 징조.','Suffix kit: Dextral Annulment and Omen of Light active together as a guard rail (the annul cannot hit the wrong line), Dextral Crystallisation, Essences of the Abyss, Whittling + Perfect Chaos, Preserved Ribs and Abyssal Echoes.')},
  {'id':'c11','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':b_regen},'side':'s','bone':'Preserved_Rib'},'knownP':True,'fail':{'goto':'c10','via':LIGHT},'ts':'8:49',
   'note':K('가중치 높은 잡옵으로 자리를 막음: 생명력 재생 → 능력치·저항 → 출혈·중독·점화 감소 → 방어도의 원소 피해 적용 순.','Block the highest-weight junk: life regeneration first, then attributes/resistances, then reduced bleed/poison/ignite, then armour applies to elemental damage.')},
  {'id':'c13','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':b_hcold},{'gi':b_hlight},{'gi':b_hfire}]},'fail':{'goto':'self','via':DANN},'ts':'12:23',
   'note':K('막기 훼손을 붙인 뒤 두 번째 복합 저항. 이제 훼손이 있어서 심연의 에센스는 못 쓰니 잡옵은 우측 소멸의 징조(빛의 징조와 함께 켜 두면 훼손은 안 지워짐)이나 절사의 징조로 제거. 훼손 전용 옵션은 레벨 65로 복합 저항과 같아서 막아 둔 채로 절사의 징조를 써도 됨.','The second hybrid, with the block on. With a desecration present Essence of the Abyss no longer works, so remove junk with Dextral Annul (keep Omen of Light active too so the desecration is safe) or Whittling. Desecration-only mods are level 65 like the hybrids, so whittling with the block on is fine.')},
  {'id':'c14','phase':'fin','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'24:58','note':K('막아 둔 훼손 제거.','Remove the blocking desecration.')},
  {'id':'c15','phase':'fin','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'24:58','note':K('고대 갈비뼈로 마지막 훼손.','Final desecration with an Ancient Rib.')},
  {'id':'c16','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':b_mbl},{'gi':b_sre}]},'side':'s','bone':'Ancient_Rib'},'knownP':True,'fail':{'goto':'c15','via':LIGHT},'ts':'24:58',
   'note':K('받는 피해를 생명력 대신 마나로 소모(10~20%) 또는 정신력 점유 효율(6~12%).','Mana before Life (10–20%) or Spirit Reservation Efficiency (6–12%).')},
  {'id':'c17','phase':'fin','do':'note','ts':'30:44',
   'note':K('신성한 오브로 마나 %·정신력 %를 올림(평균 약 400디바인). 훼손 수치는 디바인보다 다시 훼손하는 게 쌈. 축복받은 자의 징조로 고정 옵션 정신력 30. 유동체로 저항 두 줄을 같은 원소로 맞춰 수치를 올리는 방법도 있음. 내 빌드용이면 룬벼림으로 방어도 대신 룬 수호.','Divine % mana and % Spirit (about 400 divines on average). Re-desecrating is cheaper than divining the desecration. Omen of the Blessed for 30 Spirit on the implicit. A flux can make both resistances the same element to max them. For your own build, runeforge it to trade armour for Runic Ward.')},
 ]})

# ---------- 4. MazBro: +2 projectile gloves, 30% quality (Blacksteel Gauntlets) ----------
c='Gloves_str_dex'
gl_proj=g(c,'+2 to Level of all Projectile','x','s'); gl_pspd=g(c,'increased Projectile Speed','x','p'); gl_pdmg=g(c,'increased Projectile Damage','x','p')
gl_crit=g(c,'increased Critical Hit Chance','x','s'); gl_pierce=g(c,'chance to Pierce','x','s'); gl_ward=g(c,'increased Runic Ward','e','p'); gl_cdmg=g(c,'increased Critical Damage Bonus','e','s')
R.append({
 'id':'mazbro-proj-gloves','cls':c,'base':base(c,'Blacksteel Gauntlets'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':4,'budget':'high','unknownW':True,
 'buildTags':[K('투사체','Projectile'),K('치명타','Crit'),K('룬 수호','Runic Ward')],'patch':'0.5','created':'2026-11-08','author':MZ,
 'source':src('BIxlixCKPO0','POE 2 Glove Crafting Guide: 30% Quality +2 Projectile Gloves','MazBro'),
 'title':K('퀄리티 30% · 투사체 +2 분열 장갑','30% quality, fractured +2 projectile gloves'),
 'note':K('캐스터(스파크)와 트위스터·데드아이 모두 쓰는 장갑. 접두 = 투사체 속도·투사체 피해 1티어 + 룬 수호 %(트위스터는 공격 추가 피해), 접미 = 투사체 스킬 +2(분열) + 치명타 1티어 + 치명타 피해(캐스터는 관통 100%도 좋음). 검은강철 건틀릿이 룬 수호가 가장 높은 베이스. 퀄리티 30%는 선택(20%면 훨씬 쌈). 분열 이후로는 망가지지 않는 제작. 콜르의 사냥 룬으로 여는 옵션들이라 가중치 데이터가 없음.',
          'For casters (Spark) and Twister/Deadeye alike. Prefixes: T1 projectile speed and damage + % Runic Ward (Twister: flat attack damage). Suffixes: fractured +2 projectile skills, T1 crit chance, crit damage (casters may prefer 100% pierce). Blacksteel Gauntlets give the most Runic Ward. 30% quality is optional (20% is far cheaper). After the fracture the craft cannot brick. These mods come from the Kolr\'s Hunt rune, so we have no weights.'),
 'start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스 · 퀄리티','en':'Base and quality'},{'id':'fr','kr':'투사체 +2 분열','en':'Fracture +2 projectile'},{'id':'main','kr':'접두·접미 채우기','en':'Fill prefixes and suffixes'},{'id':'fin','kr':'마지막 훼손 · 마무리','en':'Desecration and finish'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'1:30','note':K('특출난 검은강철 건틀릿(룬 소켓 +1로 소켓 2개, 룬 수호 최고 베이스), 장당 9~16디바인. 퀄리티 20%까지.','Exceptional Blacksteel Gauntlets (+1 rune socket for two, highest Runic Ward), 9–16 divines each. Quality to 20%.')},
  {'id':'g2','phase':'base','do':'manual','cost':'vaal','target':{'setQuality':30},'label':K('바알 방어구 장인의 주입기로 30%','Vaal Armourer\'s Infuser to 30%'),'ts':'2:16',
   'note':K('20%를 넘겨 30%까지. 첫 번째 주입기는 실패 확률 0%, 이후 한 번마다 약 5%씩 늘어남. 영상은 약 10개 중 1개만 살아남아 300~400디바인이 듦. 30%는 선택.','Push past 20% to 30%. The first infuser cannot fail; each one after adds about 5% failure. Only about 1 in 10 survived in the video (300–400 divines). 30% is optional.')},
  {'id':'g3','phase':'base','do':'manual','target':{'rune':K('콜르의 사냥','Kolr\'s Hunt')},'label':K('콜르의 사냥 룬 장착','Socket Kolr\'s Hunt'),'ts':'3:45','note':K('투사체 옵션을 굴릴 수 있게 하는 룬. 한 번 끼우면 뺄 수 없음.','The rune that lets projectile mods roll; it cannot be removed.')},
  {'id':'g4','phase':'fr','do':'chaos','cur':'Chaos_Orb','target':{'gi':gl_proj,'replace':'s'},'fail':{'goto':'self'},'ts':'4:31',
   'note':K('완벽한 진화·확장·제왕의 오브으로 희귀를 만든 뒤 카오스 오브로 투사체 스킬 +2. 치명타 1티어처럼 좋은 줄이 먼저 뜨면 우측 찬미의 징조 + 상위 엑잘티드 오브로 +2를 노림(실패하면 소멸의 오브).','Transmute, augment and regal to rare, then Chaos for +2 projectile skills. If a good line like T1 crit lands first, Dextral Exaltation + Greater Exalt for the +2 (annul on a miss).')},
  {'id':'g5','phase':'fr','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':gl_pspd,'tmax':1},{'gi':gl_pdmg,'tmax':1}]},'fail':{'goto':'self','via':SANN},'ts':'5:17',
   'note':K('분열 전에 좋은 줄을 2~3개 만들어 두면 분열이 무엇에 걸려도 손해가 적음(30% 베이스는 거의 필수).','Get two or three good lines before fracturing so any outcome is useful (near-mandatory on a 30% base).')},
  {'id':'g6','phase':'fr','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'6:45','note':K('훼손 한 줄로 4줄: 분열 1/3.','One desecration for four lines: 1 in 3.')},
  {'id':'g7','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':gl_proj}]},'fail':{'goto':'restart'},'ts':'6:45','after':{'keepOnly':[gl_proj]},
   'note':K('투사체 +2 분열 1/3. 영상은 네 번째에 성공(빗나가도 다른 장갑으로는 쓸 수 있음). 이후 분열만 남김.','+2 projectile fractures 1 in 3; the video hit on the fourth try (a miss still makes usable gloves). Keep only the fracture.')},
  {'id':'g8','phase':'main','do':'manual','target':{'rune':K('아스트리드의 창의성','Astrid\'s Creativity')},'label':K('아스트리드의 창의성 룬 장착','Socket Astrid\'s Creativity'),'ts':'7:32','note':K('제작 옵션을 2개까지 붙일 수 있게 하는 룬. 마지막에 다른 룬으로 교체.','Allows two crafted mods; swapped for another rune at the end.')},
  {'id':'g9','phase':'main','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':gl_pspd,'tmax':1},{'gi':gl_pdmg,'tmax':1},{'gi':gl_crit,'tmax':1},{'gi':gl_pierce}]},'fail':{'goto':'self'},'ts':'9:00',
   'note':K('카오스 오브로 좋은 1티어 하나. 접두가 뜨면(투사체 속도·피해) 다음은 접미를 먼저, 접미가 뜨면(치명타·관통) 접두를 먼저 채움.','Chaos for one good T1. If it is a prefix (projectile speed/damage) do the suffixes next; if a suffix (crit, pierce), the prefixes first.')},
  {'id':'g10','phase':'main','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':gl_crit,'tmax':1},{'gi':gl_pierce}]},'fail':{'goto':'self','via':{'cur':'Sovereign_Alloy','omens':['Omen_of_Dextral_Crystallisation']}},'ts':'9:45',
   'note':K('우측 찬미의 징조 + 상위 엑잘티드 오브로 치명타 1티어(또는 관통). 실패하면 우측 결정화의 징조 + 군왕의 합금·발작의 에센스로 잡옵을 바꿔 두 번 더 시도. 다 실패하면 하나씩 소멸의 오브.','Dextral Exaltation + Greater Exalt for T1 crit (or pierce). On a miss, Dextral Crystallisation + Sovereign Alloy or Essence of Hysteria swaps the junk for two more tries. If all fail, annul one at a time.')},
  {'id':'g11','phase':'main','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'11:16','note':K('합금이 바꿀 접두 하나.','A prefix for the alloy to replace.')},
  {'id':'g12','phase':'main','do':'essence','cur':'Sovereign_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':gl_ward},'ts':'14:15','note':K('좌측 결정화의 징조 + 군왕의 합금: 룬 수호 % 증가.','Sinistral Crystallisation + Sovereign Alloy: increased Runic Ward.')},
  {'id':'g13','phase':'main','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'15:46','note':K('발작의 에센스가 바꿀 접미 하나.','A suffix for the Hysteria essence to replace.')},
  {'id':'g14','phase':'main','do':'essence','cur':'Essence_of_Hysteria','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':gl_cdmg},'ts':'15:46','note':K('우측 결정화의 징조 + 발작의 에센스: 치명타 피해(제작 옵션 2번째).','Dextral Crystallisation + Essence of Hysteria: crit damage (second crafted mod).')},
  {'id':'g15','phase':'fin','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'},'ts':'16:30','note':K('남은 접두를 고대 갈비뼈로 훼손. 원하면 그 전에 룬 모루로 룬벼림(룬 수호 대폭 증가).','Desecrate the last prefix with an Ancient Rib. Optionally runeforge at the anvil first (much more Runic Ward).')},
  {'id':'g16','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':gl_pdmg,'tmax':1}]},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'g15','via':LIGHT},'ts':'17:16',
   'note':K('투사체 피해 1티어 하나만 노림. 빛의 징조 개수만큼만 소멸의 오브를 챙김. 영상은 약 8번.','Only T1 projectile damage counts. Carry exactly as many Annulments as Omens of Light. About 8 tries in the video.')},
  {'id':'g17','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성','Astrid\'s Creativity'),K('시전 속도 룬','cast speed rune')]},'ts':'18:00',
   'note':K('신성한 오브로 수치 정리(전부 최대는 수천 디바인이라 적당히). 아스트리드의 창의성 룬은 시전 속도 룬 등으로 교체. 완성.','Divine the rolls (maxing everything costs thousands, so settle). Swap Astrid\'s Creativity for a cast speed rune or similar. Done.')},
 ]})

# ---------- 5. Diztoh: Twister attack speed spear (Akoyan Spear) ----------
c='Spears'
sp_proj=g(c,'Level of all Projectile Skills','n','s'); sp_as=g(c,'(26—28)% increased Attack Speed','n','s'); sp_aug=g(c,'Socketed Augment','e','s')
sp_cel=g(c,'to Accuracy Rating\n(5—8)% increased Attack Speed','e','p'); sp_mag=g(c,'Explicit Speed Modifier','x','p')
R.append({
 'id':'diztoh-twister-spear','cls':c,'base':base(c,'Akoyan Spear'),'ilvl':82,'difficulty':3,'budget':'high','unknownW':True,
 'buildTags':[K('트위스터','Twister'),K('공격 속도','Attack speed'),K('창','Spear')],'patch':'0.5.5','created':'2026-11-08','author':DZ,
 'source':src('cTjgn7NnHR8','How to Craft an Attack Speed Spear for Twister | PoE 2 0.5.5','Diztoh'),
 'title':K('공격 속도 · 속도 옵션 강화 트위스터 창','attack speed Twister spear with speed magnitudes'),
 'note':K('트위스터용 공격 속도 창. 군왕의 합금(장착 증강 효과)과 천공의 합금(공격 속도·정확도) 두 제작 옵션을 아스트리드의 창의성 룬으로 동시에 붙이고, 스레드의 힘 룬으로 "명시 속도 옵션 강화" 훼손을 노림. 제작자도 처음 시도한 실험 제작이라 순서 위주로 참고.',
          'An attack speed spear for Twister. Astrid\'s Creativity lets two alloys sit together (Sovereign: socketed augment effect; Celestial: attack speed + accuracy), then a Thread\'s Might rune opens the "explicit speed modifier magnitudes" desecration. The author\'s first try at this craft, so use it for the order of steps.'),
 'start':{'rar':'rare','mods':[{'gi':sp_proj,'tmax':1,'fr':True}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'as','kr':'공격 속도','en':'Attack speed'},{'id':'alloy','kr':'합금 2개','en':'Two alloys'},{'id':'des','kr':'속도 강화 훼손','en':'Speed magnitude desecration'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'s1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('아이템 레벨 82 아코야의 창, 투사체 스킬 +4가 분열된 희귀 베이스(영상은 이미 분열된 창으로 시작).','An item level 82 Akoyan Spear with fractured +4 projectile skills (the video starts from an already-fractured spear).')},
  {'id':'s1b','phase':'as','do':'exalt','cur':'Exalted_Orb','target':{'junk':'s'},'ts':'0:00','note':K('카오스 오브가 바꿀 옵션 하나를 엑잘티드 오브로 추가.','Exalt one mod for the Chaos Orb to replace.')},
  {'id':'s2','phase':'as','do':'chaos','cur':'Chaos_Orb','target':{'gi':sp_as,'tmax':2,'replace':'s'},'fail':{'goto':'self'},'ts':'0:47','note':K('카오스 오브로 공격 속도 2티어 이상(23~28%).','Chaos for tier 2+ attack speed (23–28%).')},
  {'id':'s3','phase':'alloy','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'1:31','note':K('접두에 하나 추가(합금이 지울 자리).','Add a prefix for the alloy to remove.')},
  {'id':'s4','phase':'alloy','do':'essence','cur':'Sovereign_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sp_aug},'ts':'1:31','note':K('좌측 결정화의 징조 + 군왕의 합금: 접두를 지우고 접미에 장착 증강 효과 증가.','Sinistral Crystallisation + Sovereign Alloy removes a prefix and adds increased socketed augment effect.')},
  {'id':'s5','phase':'alloy','do':'manual','target':{'rune':K('아스트리드의 창의성','Astrid\'s Creativity')},'label':K('아스트리드의 창의성 룬 장착','Socket Astrid\'s Creativity'),'ts':'2:15','note':K('제작 옵션을 하나 더 붙일 수 있게 함.','Allows one more crafted mod.')},
  {'id':'s6','phase':'alloy','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'2:15','note':K('접두 하나 추가.','Add a prefix.')},
  {'id':'s7','phase':'alloy','do':'essence','cur':'Celestial_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sp_cel},'ts':'2:15','note':K('좌측 결정화의 징조 + 천공의 합금: 물리 잡옵을 지우고 정확도 + 공격 속도.','Sinistral Crystallisation + Celestial Alloy swaps the flat physical line for accuracy + attack speed.')},
  {'id':'s8','phase':'des','do':'manual','target':{'runeSwap':[K('아스트리드의 창의성','Astrid\'s Creativity'),K('스레드의 힘','Thread\'s Might')]},'label':K('스레드의 힘 룬으로 교체','Swap to Thread\'s Might'),'ts':'3:01','note':K('창의성 룬을 빼도 제작 옵션 두 개는 유지됨. 이 룬이 있어야 속도 강화 훼손이 나옴.','Both crafted mods stay when Astrid\'s Creativity comes out; this rune is what opens the speed magnitude desecration.')},
  {'id':'s9','phase':'des','do':'desecrate','cur':'Ancient_Jawbone','target':{'unrev':'p'},'ts':'3:01','note':K('고대 턱뼈로 훼손.','Desecrate with an Ancient Jawbone.')},
  {'id':'s10','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':sp_mag},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'s9','via':LIGHT},'ts':'3:45','note':K('명시 속도 옵션 강화(25~30%) 공개. 영상은 다시 굴림 한 번에 나옴.','Reveal explicit speed modifier magnitudes (25–30%); it showed after one reroll.')},
  {'id':'s11','phase':'fin','do':'note','ts':'5:16',
   'note':K('디바인·퀄리티로 마무리. 장착 증강 효과는 두 번째 소켓이 있어야 의미가 있어서 영상은 히네코라의 머리카락으로 보고 타락(2소켓) 후 키바와의 영혼(공격 속도) 증강을 끼움. 타락은 선택이고 아이템이 망가질 수 있음.','Finish with Divines and quality. Socketed augment effect only matters with a second socket, so the video previewed with Hinekora, corrupted for a second socket and added the Soul of Kibawa (attack speed) augment. Corrupting is optional and can brick the item.')},
 ]})

# ---------- 6. Diztoh: Iceshot Deadeye bow (Obliterator Bow) ----------
c='Bows'
bw_ppct=g(c,'(170—179)% increased Physical Damage','n','p'); bw_flat=g(c,'Adds (26—39) to (44—66) Physical Damage','n','p')
bw_cold=g(c,'Adds (72—81) to (110—123) Cold Damage','n','p'); bw_light=g(c,'Adds (1—12) to (202—234) Lightning','n','p')
bw_proj=g(c,'Level of all Projectile Skills','n','s'); bw_crit=g(c,'to Critical Hit Chance','n','s'); bw_flatE=g(c,'Adds (16—24) to (28—42) Physical','e','p')
R.append({
 'id':'diztoh-iceshot-bow','cls':c,'base':base(c,'Obliterator Bow'),'ilvl':82,'difficulty':4,'budget':'high',
 'buildTags':[K('얼음 사격','Ice Shot'),K('데드아이','Deadeye'),K('냉기','Cold')],'patch':'0.5.5','created':'2026-11-08','author':DZ,
 'source':src('29vO0mMUoME','How to craft an Endgame Iceshot Deadeye Bow','Diztoh'),
 'title':K('물리 % 분열 + 냉기 1티어 + 투사체 +4 활','fractured % phys + T1 cold + projectile +4 bow'),
 'note':K('접두 = 물리 피해 %(분열) + 물리 추가 1티어 + 냉기 추가 1티어, 접미 = 투사체 스킬 +4(훼손 공개) + 치명타 확률 + 마지막 1줄은 운. 번개가 붙으면 알두르의 숨결 룬으로 냉기로 바꿈(소켓 소모). 아스트리드의 창의성 룬으로 훼손을 빛의 징조 없이 다시 굴리는 방법이 핵심. 영상은 마지막 타락에서 망가짐.',
          'Prefixes: fractured % physical, T1 flat physical, T1 flat cold. Suffixes: +4 projectile skills (revealed desecration), crit chance, and a luck-of-the-draw last line. Lightning is converted to cold with a Breath of Aldur rune (it uses up the socket). The key trick is Astrid\'s Creativity letting you reroll the desecration without Omens of Light. The video\'s bow bricked on the final corruption.'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fr','kr':'물리 % 분열','en':'Fracture % phys'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'투사체 +4 · 접미','en':'Projectile +4 and suffixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'w1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('아이템 레벨 82 절멸자 활(투사체 +4는 82부터).','An item level 82 Obliterator Bow (+4 projectiles needs 82).')},
  {'id':'w2','phase':'fr','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':bw_ppct,'tmax':2},'fail':{'goto':'self','via':ANNUL},'ts':'0:00','note':K('완벽한 진화의 오브 + 소멸의 오브로 물리 피해 % 2티어 이상.','Perfect Transmute and annul for tier 2+ % physical damage.')},
  {'id':'w3','phase':'fr','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'0:00','note':K('완벽한 확장의 오브로 접미 하나.','Augment a suffix.')},
  {'id':'w4','phase':'fr','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':bw_flatE},'ts':'0:45','note':K('상위 마모의 에센스로 희귀 + 물리 추가.','Greater Essence of Abrasion: rare plus flat physical.')},
  {'id':'w5','phase':'fr','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'s'},'ts':'0:45','note':K('훼손 하나로 4줄. 분열 전에 물리 %를 신성한 오브로 165% 이상.','One desecration for four lines; divine % physical to 165%+ before fracturing.')},
  {'id':'w6','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':bw_ppct}]},'fail':{'goto':'restart'},'ts':'1:00','after':{'keepOnly':[bw_ppct,'junk1']},
   'note':K('물리 % 분열 1/3. 실패하면 예비 활로. 이후 분열 + 한 줄만 남기고 카오스 오브.','% physical fractures 1 in 3; use a backup bow on a miss. Keep the fracture plus one line and chaos.')},
  {'id':'w7','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'gi':bw_flat,'tmax':1,'replace':'p'},'fail':{'goto':'self'},'ts':'1:30','note':K('카오스 오브로 물리 추가 1티어(3티어 이상이면 타협 가능).','Chaos for T1 flat physical (tier 3+ is acceptable).')},
  {'id':'w8','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':bw_cold,'tmax':1},{'gi':bw_light,'tmax':1}]},'fail':{'goto':'self','via':{'cur':'Chaos_Orb','omens':['Omen_of_Whittling']}},'ts':'3:47',
   'note':K('완벽한 엑잘티드 오브로 냉기 추가(복합 물리나 다른 원소도 OK). 공격 원소 피해 %·정확도는 꽝이라 절사의 징조 + 카오스 오브로 교체.','Perfect Exalt for flat cold (hybrid phys or another element is fine). Elemental damage with attacks or accuracy are misses: replace with Whittling + Chaos.')},
  {'id':'w9','phase':'pre','do':'manual','target':{'rune':K('알두르의 숨결 (소켓 소모)','Breath of Aldur (socket used up)')},'label':K('알두르의 숨결 룬 (번개 → 냉기)','Breath of Aldur (lightning → cold)'),'ts':'4:32','note':K('번개 1티어가 붙었으면 알두르의 숨결로 화염·번개 옵션을 같은 티어 냉기로 바꿈. 소켓이 소모되어 이후 룬 교체 불가.','With T1 lightning, Breath of Aldur turns fire and lightning mods into same-tier cold. It uses up the socket.')},
  {'id':'w10','phase':'suf','do':'manual','target':{'rune':K('아스트리드의 창의성','Astrid\'s Creativity')},'label':K('아스트리드의 창의성 룬 장착','Socket Astrid\'s Creativity'),'ts':'5:15','note':K('제작 옵션 하나 더. 훼손을 다시 굴릴 때 에센스 두 개를 번갈아 쓰기 위함.','One more crafted mod, so two essences can alternate while rerolling the desecration.')},
  {'id':'w11','phase':'suf','do':'desecrate','cur':'Ancient_Jawbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'6:45','note':K('고대 턱뼈로 접미 훼손.','An Ancient Jawbone desecrates the suffix.')},
  {'id':'w12','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':bw_proj,'tmax':1},'side':'s','bone':'Ancient_Jawbone'},'fail':{'goto':'w11','via':{'cur':'Perfect_Essence_of_Haste','omens':['Omen_of_Dextral_Crystallisation']}},'ts':'8:17',
   'note':K('투사체 스킬 +4를 공개. 아니면 "빛 없이 다시 굴리기": 우측 결정화의 징조 + 완벽한 가속의 에센스로 훼손을 지우고(맹공 생김), 심연의 에센스로 맹공을 심연 군주의 징표로 바꾼 뒤 다시 훼손. 에센스·징조가 매번 소모되니 개수 확인. +3이 떠도 이후 치명타 굴리기가 불편해져서 +4를 노림.','Reveal +4 projectile skills. Otherwise the lightless reroll: Dextral Crystallisation + Perfect Essence of Haste removes the desecration (adds Onslaught), an Essence of the Abyss turns that into the Mark, then desecrate again. Essences and omens go fast; keep count. A +3 makes the later crit rolls awkward, so hold out for +4.')},
  {'id':'w13','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'15:01','note':K('접미에 아무 옵션 하나.','Any suffix.')},
  {'id':'w14','phase':'suf','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'gi':bw_crit,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'15:45',
   'note':K('절사의 징조 + 카오스 오브로 치명타 확률. 레벨이 낮은 접두가 걸릴 땐 우측 말소의 징조를 같이 켜서 접미만 바꿈. 초과 화살 확률이 뜨면 거기서 멈춰도 좋음.','Whittling Chaos for crit chance. When a low-level prefix would be hit, add Omen of Dextral Erasure to touch suffixes only. Surpassing is also a fine stop.')},
  {'id':'w15','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'18:00','note':K('마지막 접미는 운(공격 속도·치명타 피해·초과 화살이면 대박).','The last suffix is luck (attack speed, crit damage or surpassing is a jackpot).')},
  {'id':'w16','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성','Astrid\'s Creativity'),K('물리 룬','physical rune')]},'ts':'18:45',
   'note':K('창의성 룬은 물리 룬으로 교체 가능(알두르의 숨결 소켓은 고정). 신성한 오브로 수치 정리. 영상은 히네코라의 머리카락 확인 후 4소켓 타락을 시도했다가 망가짐: 타락은 선택.','Astrid\'s Creativity can be swapped for physical runes (the Breath of Aldur socket is fixed). Divine the rolls. The video tried a corruption for a fourth socket and bricked it: corrupting is optional.')},
 ]})

# ---------- 7. Diztoh: budget two-handed mace (exceptional Massive Greathammer) ----------
c='Two_Hand_Maces'
mc_hyb=g(c,'(75—79)% increased Physical Damage\n+(175—200) to Accuracy','n','p'); mc_flatE=g(c,'Adds (23—35) to (39—59) Physical','e','p'); mc_kpct=g(c,'(110—154)% increased Physical Damage','d','p')
mc_battle=g(c,'Level of all Attack Skills','e','s'); mc_as=g(c,'(26—28)% increased Attack Speed','n','s'); mc_attr=g(c,'reduced Attribute Requirements','n','s')
R.append({
 'id':'diztoh-budget-mace','cls':c,'base':base(c,'Massive Greathammer'),'ilvl':82,'sockets':3,'exceptional':{'sockets':1},'difficulty':1,'budget':'low',
 'buildTags':[K('물리','Physical'),K('근접','Melee'),K('가성비','Budget')],'patch':'0.5','created':'2026-11-08','author':DZ,
 'source':src('ITbefGq6V18','How to Craft a Budget Two-Handed Mace in PoE 2 - 0.5','Diztoh'),
 'title':K('물리 700 DPS 가성비 양손 둔기','budget 700 phys DPS two-handed mace'),
 'note':K('약 10디바인짜리 결정론적 제작. 접두 = 복합 물리 + 물리 추가(에센스) + 쿠르갈 물리 %(공격 속도 감소 붙음), 접미 = 공격 스킬 +3(전투의 에센스) + 운 2줄. 특출난 베이스라 소켓 3개에 완벽한 철 룬.',
          'A deterministic craft worth about 10 divines. Prefixes: hybrid physical, flat physical (essence), Kurgal % physical (with reduced attack speed). Suffixes: +3 attack skills (Essence of Battle) and two lucky lines. The exceptional base has three sockets for Perfect Iron Runes.'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'d1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('특출난 거대한 대망치(소켓 3), 일반 등급, 아이템 레벨 82.','An exceptional Massive Greathammer (3 sockets), normal rarity, item level 82.')},
  {'id':'d2','phase':'pre','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':mc_hyb,'tmax':2},'knownP':True,'fail':{'goto':'self','via':ANNUL},'ts':'0:00','note':K('완벽한 진화의 오브로 물리 % + 정확도 복합 2티어 이상. 물리 추가와 물리 %는 나중에 직접 붙일 수 있어서 복합을 노림.','Transmute for tier 2+ hybrid physical + accuracy. Flat and % physical can be added later, so aim for the hybrid.')},
  {'id':'d3','phase':'pre','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'0:46','note':K('접미 하나(나중에 에센스가 교체).','A suffix (an essence replaces it later).')},
  {'id':'d4','phase':'pre','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':mc_flatE},'ts':'0:46','note':K('상위 마모의 에센스로 희귀 + 물리 추가.','Greater Essence of Abrasion: rare plus flat physical.')},
  {'id':'d5','phase':'pre','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy','Omen_of_the_Blackblooded'],'target':{'unrev':'p'},'ts':'0:46','note':K('좌측 강령술의 징조 + 검은 피의 징조로 접두에 쿠르갈 훼손.','Sinistral Necromancy + Blackblooded for a Kurgal prefix desecration.')},
  {'id':'d6','phase':'suf','do':'manual','target':{'rune':K('아스트리드의 창의성','Astrid\'s Creativity')},'label':K('아스트리드의 창의성 룬 장착','Socket Astrid\'s Creativity'),'ts':'1:30','note':K('제작 옵션 하나 더(에센스 옵션 두 개).','One more crafted mod (two essence mods).')},
  {'id':'d7','phase':'suf','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':mc_battle},'ts':'1:30','note':K('우측 결정화의 징조 + 완벽한 전투의 에센스: 정확도 접미를 지우고 공격 스킬 +3.','Dextral Crystallisation + Perfect Essence of Battle replaces the accuracy suffix with +3 attack skills.')},
  {'id':'d8','phase':'suf','do':'reveal','target':{'reveal':{'gi':mc_kpct},'side':'p','lord':'kurgal','bone':'Preserved_Jawbone'},'ts':'2:16','note':K('우물에서 공개: 물리 피해 % (최대 154%, 공격 속도 15% 감소). 심연의 메아리의 징조는 필요 없음.','Reveal at the Well: % physical (up to 154%, with 15% reduced attack speed). Abyssal Echoes is not needed.')},
  {'id':'d9','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':[{'gi':mc_as},{'gi':mc_attr}]},'knownP':True,'ts':'3:00',
   'note':K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 두 줄. 최선은 공격 속도·능력치 요구 감소, 치명타도 괜찮음. 마음에 안 들면 우측 소멸의 징조 + 소멸의 오브로 하나씩 지우고(전투의 에센스가 지워지면 다시) 반복.','Greater Exaltation + Perfect Exalt adds two suffixes. Best: attack speed and reduced attribute requirements; crit is fine. If unhappy, Dextral Annul one at a time (redo Battle if it goes) and repeat.')},
  {'id':'d10','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성','Astrid\'s Creativity'),K('완벽한 철 룬','Perfect Iron Rune')]},'ts':'4:32','note':K('상위 철 룬 3개 → 숙련 룬으로 완벽한 철 룬. 물리 DPS 약 700, 시세 약 10디바인. 완성.','Three Greater Iron Runes upgraded to Perfect with a master rune. About 700 physical DPS, worth roughly 10 divines. Done.')},
 ]})

# ---------- 8. Diztoh: budget grenade crossbow (Siege Crossbow) ----------
c='Crossbows'
xb_ppct=g(c,'(170—179)% increased Physical Damage','n','p'); xb_flatE=g(c,'Adds (23—35) to (39—59) Physical','e','p'); xb_battle=g(c,'Level of all Attack Skills','e','s')
xb_gren=g(c,'Grenades have','d','s'); xb_as=g(c,'(17—19)% increased Attack Speed','n','s'); xb_hyb=g(c,'(75—79)% increased Physical Damage\n+(175—200) to Accuracy','n','p')
R.append({
 'id':'diztoh-grenade-crossbow','cls':c,'base':base(c,'Siege Crossbow'),'ilvl':82,'difficulty':1,'budget':'low',
 'buildTags':[K('수류탄','Grenade'),K('물리','Physical'),K('가성비','Budget')],'patch':'0.5','created':'2026-11-08','author':DZ,
 'source':src('vk3pLFUov8U','Easy Budget Endgame Crossbow Crafting Guide | PoE 2 0.5','Diztoh'),
 'title':K('수류탄 2회 발동 가성비 공성 석궁','budget Siege Crossbow with grenade double-fire'),
 'note':K('비싼 징조로 옵션을 쫓지 않는 가성비 석궁. 일반 → 마법 → 에센스로 희귀 → 접미 아마나무 훼손(수류탄 2회 발동) → 마지막 두 줄은 운.',
          'A budget crossbow that skips expensive omen chasing: normal to magic, an essence to rare, an Amanamu suffix desecration (grenades activate a second time), then two luck slams.'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'rare','kr':'희귀 만들기','en':'Make it rare'},{'id':'des','kr':'수류탄 훼손 · 운','en':'Grenade desecration and slams'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'x1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('아이템 레벨 82 공성 석궁(높을수록 좋음).','An item level 82 Siege Crossbow (higher is better).')},
  {'id':'x2','phase':'rare','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':xb_ppct,'tmax':2},'knownP':True,'fail':{'goto':'self','via':ANNUL},'ts':'0:45','note':K('완벽한 진화의 오브로 물리 % 2티어 이상(투사체 레벨이 뜨면 그것도 OK).','Perfect Transmute for tier 2+ % physical (projectile levels are fine too).')},
  {'id':'x3','phase':'rare','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'0:45','note':K('완벽한 확장의 오브 한 번.','One augment.')},
  {'id':'x4','phase':'rare','do':'essence','cur':'Essence_of_Abrasion','target':{'gi':xb_flatE},'ts':'1:30','note':K('마모의 에센스로 희귀 + 물리 추가.','Essence of Abrasion: rare plus flat physical.')},
  {'id':'x5','phase':'rare','do':'manual','target':{'rune':K('아스트리드의 창의성','Astrid\'s Creativity')},'label':K('아스트리드의 창의성 룬 장착','Socket Astrid\'s Creativity'),'ts':'1:30','note':K('제작 옵션 하나 더.','One more crafted mod.')},
  {'id':'x6','phase':'rare','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':xb_battle},'ts':'1:30','note':K('우측 결정화의 징조 + 완벽한 전투의 에센스: 흡혈 접미를 지우고 공격 스킬 +3.','Dextral Crystallisation + Perfect Essence of Battle swaps the leech suffix for +3 attack skills.')},
  {'id':'x7','phase':'des','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Liege'],'target':{'unrev':'s'},'ts':'2:15','note':K('우측 강령술의 징조 + 군왕의 징조(아마나무 확정) + 보존된 턱뼈.','Dextral Necromancy + Omen of the Liege (guaranteed Amanamu) + Preserved Jawbone.')},
  {'id':'x8','phase':'des','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','s']},'ts':'2:15','note':K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 두 줄. 원하는 건 접미 공격 속도·접두 복합 물리지만 순수 운.','Greater Exaltation + Perfect Exalt adds two lines. Ideal: attack speed and hybrid physical, but it is pure luck.')},
  {'id':'x9','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':xb_gren},'side':'s','lord':'amanamu','bone':'Preserved_Jawbone'},'fail':{'goto':'x7','via':LIGHT},'ts':'2:45','note':K('공개: 수류탄 2회 발동 확률(15~25%).','Reveal: grenades have a chance to activate a second time (15–25%).')},
  {'id':'x10','phase':'fin','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'reroll':True,'runeSwap':[K('아스트리드의 창의성','Astrid\'s Creativity'),K('완벽한 철 룬','Perfect Iron Rune')]},'ts':'3:01','note':K('창의성 룬을 일반 룬으로 바꾼 뒤, 4티어 정확도처럼 레벨 낮은 줄은 절사의 징조 + 완벽한 카오스 오브로 교체(약 5디바인).','Swap Astrid\'s Creativity for a normal rune, then replace a low line like T4 accuracy with Whittling + Perfect Chaos (about 5 divines).')},
  {'id':'x11','phase':'fin','do':'note','target':{'setQuality':20},'ts':'3:45','note':K('퀄리티 20%, 완벽한 철 룬. 타락은 선택(영상은 망가짐). 완성.','Quality to 20% and Perfect Iron Runes. Corrupting is optional (the video bricked). Done.')},
 ]})

# ---------- 9. Diztoh: crit helmet (exceptional Grinning Mask) ----------
c='Helmets_dex_int'
hm_eva=g(c,'(92—100)% increased Evasion and Energy Shield','n','p'); hm_hl=g(c,'increased Evasion and Energy Shield\n+(42—49) to maximum Life','n','p')
hm_hm=g(c,'increased Evasion and Energy Shield\n+(33—39) to maximum Mana','n','p'); hm_crit=g(c,'increased Critical Hit Chance','n','s'); hm_cdmg=g(c,'Critical Damage Bonus','d','s'); hm_rar=g(c,'Rarity of Items found','n','s')
R.append({
 'id':'diztoh-crit-helmet','cls':c,'base':base(c,'Grinning Mask'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium',
 'buildTags':[K('치명타','Crit'),K('회피','Evasion'),K('몽크','Monk')],'patch':'0.5','created':'2026-11-08','author':DZ,
 'source':src('QuW8BOSpPpo','How to Craft an Endgame Crit Helmet | Step-by-Step Guide | PoE 2 0.5','Diztoh'),
 'title':K('회피·에너지 보호막 분열 + 치명타·치명타 피해 투구','fractured eva/ES + crit and crit damage helmet'),
 'note':K('치명타 몽크 등 민첩·지능 치명타 빌드용. 접두 = 회피·에너지 보호막 % 1티어(분열) + 복합, 접미 = 치명타 확률 + 치명타 피해(울라만 훼손) + 1줄. 웃는 가면에서 되는 조합. 타락하면 레이븐의 손길(주입) 옵션을 못 붙이니 바로 타락하지 않음. 시세 약 700디바인.',
          'For crit Monk and other Dex/Int crit builds. Prefixes: fractured T1 % evasion/ES plus a hybrid; suffixes: crit chance, crit damage (Ulaman desecration) and one more. Works on Grinning Mask. Corrupting blocks the Raven\'s Touch instillation, so do not corrupt right away. Worth about 700 divines.'),
 'start':{'rar':'normal','mods':[],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fr','kr':'회피·보호막 분열','en':'Fracture eva/ES'},{'id':'main','kr':'치명타 · 접두','en':'Crit and prefixes'},{'id':'des','kr':'치명타 피해 훼손','en':'Crit damage desecration'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'h1','phase':'base','do':'base','cost':'base','ts':'0:00','note':K('특출난 웃는 가면(소켓 +1), 아이템 레벨 82. 몇 카오스 오브면 삼. 퀄리티 20%.','An exceptional Grinning Mask (+1 socket), item level 82, a few chaos. Quality to 20%.')},
  {'id':'h2','phase':'fr','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':hm_eva,'tmax':1},'knownP':True,'fail':{'goto':'self','via':ANNUL},'ts':'0:46','note':K('완벽한 진화·확장의 오브 + 소멸의 오브로 회피·에너지 보호막 % 1티어.','Perfect Transmute, Perfect Augment and annul for T1 % evasion and ES.')},
  {'id':'h3','phase':'fr','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'junk':'s'},'ts':'1:30','note':K('같이 쓸 만한 접미(영상은 희귀도).','A useful partner suffix (rarity in the video).')},
  {'id':'h4','phase':'fr','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'1:30','note':K('완벽한 제왕의 오브.','Perfect Regal Orb.')},
  {'id':'h5','phase':'fr','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'1:30','note':K('우측 강령술의 징조로 접미 훼손: 4줄, 분열 1/3. 분열 전에 신성한 오브로 수치 정리.','Dextral Necromancy desecrates a suffix: four lines, 1 in 3. Divine the rolls before fracturing.')},
  {'id':'h6','phase':'fr','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':hm_eva}]},'fail':{'goto':'restart'},'ts':'2:15','after':{'keepOnly':[hm_eva,'junk1']},'note':K('회피·에너지 보호막 % 분열 후 나머지 소멸의 오브.','Fracture % evasion/ES and annul the rest.')},
  {'id':'h7','phase':'main','do':'chaos','cur':'Chaos_Orb','target':{'gi':hm_crit,'tmax':2,'replace':'s'},'fail':{'goto':'self'},'ts':'3:02','note':K('카오스 오브로 치명타 확률 2티어 이상. 지나쳐 굴리지 않게 천천히.','Chaos for tier 2+ crit chance; go slowly so you do not roll past it.')},
  {'id':'h8','phase':'main','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':hm_hl,'tmax':2},{'gi':hm_hm,'tmax':2}]},'fail':{'goto':'self','via':{'cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Sinistral_Erasure']}},'ts':'3:46',
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 회피·에너지 보호막 % 복합. 정확도는 꽝: 절사의 징조 + 좌측 말소의 징조 + 상위 카오스 오브로 접두의 레벨 낮은 줄만 교체하거나 50/50 소멸의 오브. 치명타가 지워지면 7번부터.','Sinistral Exaltation + Perfect Exalt for a % evasion/ES hybrid. Accuracy is a miss: Whittling + Sinistral Erasure + Greater Chaos replaces the lowest prefix, or take the 50/50 annul. If crit goes, back to step 7.')},
  {'id':'h9','phase':'main','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'9:02','note':K('남은 접두(영상은 마나).','The last prefix (mana in the video).')},
  {'id':'h10','phase':'des','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'s'},'ts':'9:46','note':K('빛의 징조를 켜 두고 고대 갈비뼈로 훼손.','Desecrate with an Ancient Rib, Omen of Light ready.')},
  {'id':'h11','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':hm_cdmg},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'h10','via':LIGHT},'ts':'10:31','note':K('치명타 피해 보너스 공개. 영상은 약 4번.','Reveal crit damage bonus; about four tries in the video.')},
  {'id':'h12','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'s'},'ts':'11:15','note':K('마지막 접미는 운(희귀도·저항이면 좋음, 영상은 화염 저항).','The last suffix is luck (rarity or resistance is good; fire res in the video).')},
  {'id':'h13','phase':'fin','do':'note','ts':'12:00','note':K('신성한 오브로 수치 정리. 레이븐의 손길(약 95디바인)을 쓸 거면 타락하지 말 것. 바알 방어구 장인의 주입기로 퀄리티 +1~2%. 완성.','Divine the rolls. Do not corrupt if you want Raven\'s Touch (about 95 divines). A Vaal infuser adds 1–2% quality. Done.')},
 ]})

# ---------- 10. Diztoh: 5-mod Sapphire jewel ----------
c='Sapphire'
jw_crit=g(c,'increased Critical Hit Chance$','n','s') if False else g(c,'(5—15)% increased Critical Hit Chance','n','s')
jw_scrit=g(c,'Critical Hit Chance for Spells','n','s'); jw_cdmg=g(c,'(10—20)% increased Critical Damage Bonus','n','s'); jw_cast=g(c,'increased Cast Speed','n','s')
jw_cold=g(c,'increased Cold Damage','n','p'); jw_spell=g(c,'(5—15)% increased Spell Damage','n','p'); jw_ele=g(c,'increased Elemental Damage','n','p')
jw_plus=g(c,'+1 Suffix Modifier allowed','x','p'); jw_eff=g(c,'Effect of Suffixes','x','p')
R.append({
 'id':'diztoh-5mod-sapphire','cls':c,'base':0,'ilvl':82,'cap':{'p':2,'s':2},'difficulty':3,'budget':'medium','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('치명타','Crit'),K('주문','Spell')],'patch':'0.5','created':'2026-11-08','author':DZ,
 'source':src('-YZm55-QuoQ','New 5-Mod Jewel Crafting Tech Explained | PoE 2 0.5','Diztoh'),
 'title':K('접미 3줄 5옵션 사파이어','five-mod sapphire with three suffixes'),
 'note':K('위력적인 액체 경멸로 "+1 접미 허용"을 얻어 접미 3줄을 만들고, 위력적인 액체 흉포함으로 "접미 효과 증가" 접두를 붙여 5옵션 주얼을 만드는 방법. 루비·에메랄드도 같은 방법. 50/50 구간이 두 번 있음. 주얼 옵션 가중치 데이터가 없어 확률은 표시하지 않음.',
          'Potent Liquid Contempt grants "+1 suffix allowed" for three suffixes, then Potent Liquid Ferocity adds "increased effect of suffixes" for a five-mod jewel. Works on Ruby and Emerald too. There are two 50/50 checkpoints. We have no jewel weights, so no odds are shown.'),
 'start':{'rar':'rare','mods':[{'junk':'s'}]},
 'phases':[{'id':'suf','kr':'접미 2줄','en':'Two suffixes'},{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'des','kr':'3번째 접미 (훼손)','en':'Third suffix (desecrated)'},{'id':'fer','kr':'흉포함: 접미 효과','en':'Ferocity: suffix effect'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'j1','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':jw_scrit},{'gi':jw_crit},{'gi':jw_cdmg}],'replace':'s'},'fail':{'goto':'self'},'ts':'0:00','note':K('희귀 사파이어를 소멸의 오브로 비우고 카오스 오브로 치명타 계열 접미(주문 치명타·치명타·치명타 피해). 반대로 접두 2줄(주문 피해·원소 피해)로 가도 같은 방법.','Annul a rare Sapphire clean and chaos for a crit suffix (spell crit, crit, crit damage). The same works the other way with two prefixes (spell/elemental damage).')},
  {'id':'j2','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':jw_cdmg},{'gi':jw_crit},{'gi':jw_scrit}]},'fail':{'goto':'self','via':ANNUL},'ts':'0:47','note':K('우측 찬미의 징조로 두 번째 치명타 접미. 아니면 소멸의 오브(우측 찬미의 징조를 넉넉히).','Dextral Exaltation for a second crit suffix; annul on a miss (bring plenty of Dextral Exaltations).')},
  {'id':'j3','phase':'con','do':'exalt','cur':'Exalted_Orb','target':{'junk':['p','p']},'ts':'1:30','note':K('접두에 아무 옵션 2개.','Any two prefixes.')},
  {'id':'j4','phase':'con','do':'essence','cur':'Potent_Liquid_Contempt','knownP':True,'target':{'gi':jw_plus,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'restart'},'ts':'1:30','note':K('위력적인 액체 경멸: 옵션 하나를 지우고 "+1 접미 허용" 또는 "+1 접두 허용"(50/50). 접미 쪽이 나와야 성공, 아니면 소멸의 오브로 비우고 처음부터.','Potent Liquid Contempt removes a mod and adds "+1 suffix allowed" or "+1 prefix allowed" (50/50). You need the suffix one; otherwise annul and start over.')},
  {'id':'j5','phase':'des','do':'desecrate','cur':'Preserved_Cranium','target':{'unrev':'s'},'ts':'3:00','note':K('보존된 두개골로 훼손: 3번째 접미로 들어감.','Desecrate with a Preserved Cranium; it goes to the third suffix.')},
  {'id':'j6','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':jw_cast},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'j5','via':LIGHT},'ts':'3:00','note':K('시전 속도(또는 치명타 피해·주문 치명타 피해) 공개. 영상은 약 5번.','Reveal cast speed (or crit damage / spell crit damage); about five tries in the video.')},
  {'id':'j7','phase':'fer','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment'],'target':{'dropGi':jw_plus},'ts':'4:33','note':K('좌측 소멸의 징조로 "+1 접미 허용" 접두를 지움(접두 50/50). 접미 3줄은 그대로 고정됨.','Sinistral Annul the "+1 suffix allowed" prefix (a prefix 50/50). The three suffixes stay locked in.')},
  {'id':'j8','phase':'fer','do':'exalt','cur':'Greater_Exalted_Orb','target':{'junk':'p'},'ts':'5:16','note':K('상위 엑잘티드 오브로 접두 두 자리를 채움.','A Greater Exalt fills the second prefix.')},
  {'id':'j9','phase':'fer','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':jw_cold},{'gi':jw_spell},{'gi':jw_ele}],'replace':'p'},'fail':{'goto':'self'},'ts':'6:00','note':K('이 상태에선 카오스 오브가 접두만 바꿈(소멸의 오브 단계를 건너뛰어야 함). 쓸 만한 접두를 만듦(영상은 냉기 피해).','In this state Chaos only rerolls prefixes (skip the annul step). Roll a useful prefix (cold damage in the video).')},
  {'id':'j10','phase':'fer','do':'essence','cur':'Potent_Liquid_Ferocity','knownP':True,'target':{'gi':jw_eff,'chance':0.5},'fail':{'goto':'j9'},'ts':'6:47','note':K('위력적인 액체 흉포함: 접두 하나를 지우고 "접미 효과 증가(40~60%)". 접미가 3줄이라 접두 쪽에만 붙음. 잡옵이 지워지면 성공(50/50), 좋은 접두가 지워지면 카오스 오브부터 다시.','Potent Liquid Ferocity removes a prefix and adds "increased effect of suffixes (40–60%)"; with three suffixes it can only land on the prefix side. Success when the junk goes (50/50); if the good prefix goes, chaos again.')},
  {'id':'j11','phase':'fin','do':'quality','cur':'Refined_Skittering_Catalyst','target':{'quality':20},'ts':'7:31','note':K('신성한 오브로 수치를 올리고(접미 효과 증가 덕에 최대치를 넘음), 제련된 달리는 기폭제로 속도 퀄리티 20%,  시전 속도 7%까지.','Divine the rolls (they exceed their max thanks to suffix effect) and a Refined Skittering Catalyst to 20% pushes cast speed to 7%.')},
  {'id':'j12','phase':'fin','do':'note','ts':'8:16','note':K('완성. 타락으로 한 줄 더 노릴 수도 있지만 영상은 판매.','Done. You could corrupt for another mod; the video sold it instead.')},
 ]})
