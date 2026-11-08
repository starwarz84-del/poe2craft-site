# ---- MazBro "How to Craft ANY Best-in-Slot Sceptre (and Profit) | PoE2 Crafting Guide" (youtu.be/UwzsARlgaFM) ----
MZ5=K('MazBro 영상 기반','Based on MazBro')
c='Sceptres'
def textM(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
mz_dmg=textM('increased Damage','n','p'); mz_mana=textM('to maximum Mana','n','p'); mz_spirit=textM('(61—65)% increased Spirit','n','p'); mz_hyb=textM('increased Spirit\n+','n','p')
mz_regen=textM('increased Mana Regeneration Rate','n','s'); mz_aoe=textM('increased Presence Area of Effect','n','s'); mz_cast=textM('increased Cast Speed','n','s')
mz_crit=textM('increased Critical Hit Chance','n','s'); mz_cdmg=textM('increased Critical Damage Bonus','n','s'); mz_aug=textM('increased effect of Socketed Augment Items','e','s')
MZ_ANN={'cur':'Orb_of_Annulment'}
MZ_SUF=[{'gi':mz_regen,'tmax':1},{'gi':mz_aoe,'tmax':1},{'gi':mz_cast,'tmax':1},{'gi':mz_crit,'tmax':1},{'gi':mz_cdmg,'tmax':1}]
R.append({
 'id':'mazbro-sceptre','cls':c,'base':base(c,'Stoic Sceptre'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':5,'budget':'high',
 'buildTags':[K('정신력','Spirit'),K('마나','Mana'),K('아군 피해','Ally damage')],'patch':'0.5.5','created':'2026-11-09','author':MZ5,
 'source':{'url':'https://www.youtube.com/watch?v=UwzsARlgaFM','title':'How to Craft ANY Best-in-Slot Sceptre (and Profit) | PoE2 Crafting Guide','channel':'MazBro'},
 'title':K('아군 피해 분열 + 정신력·마나 1티어','fractured ally damage + T1 spirit and mana'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'매직 · 분열','en':'Magic and fracture'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'z1','phase':'base','do':'base','cost':'base','ts':'1:48','note':K('특출난 엄숙한 셉터(룬 소켓 2개, 아이템 레벨 82) 노멀을 여러 개. 분열이 1/3이라 예비가 필요함.','Several normal Exceptional Stoic Sceptres (two rune sockets, item level 82); the fracture is 1 in 3, so keep spares.')},
  {'id':'z2','phase':'base','do':'transmute','cur':'Perfect_Orb_of_Transmutation','target':{'gi':mz_dmg,'tmax':1},'fail':{'goto':'self','via':MZ_ANN},'ts':'2:10',
   'note':K('완벽한 진화의 오브로 존재 범위 내 아군 피해 증가 1티어(가중치가 매우 낮아 분열로 확보). 접미가 붙으면 완벽한 확장의 오브로 접두를 노리고, 빗나가면 소멸의 오브. 1티어 정신력·소환수 스킬 +4 같은 비싼 줄이 뜨면 바로 팔아 비용 회수(영상 10~39디바인).','Perfect Transmute for tier 1 ally damage in your presence (very low weight, so it is the line to fracture). If a suffix lands, Perfect Augment for the prefix; annul misses. Sell pricey hits like T1 spirit or +4 minion skills on the spot (10–39 divines in the video).')},
  {'id':'z3','phase':'base','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'s'},'ts':'8:24','note':K('완벽한 제왕의 오브로 희귀.','Perfect Regal to rare.')},
  {'id':'z4','phase':'base','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':mz_dmg}},'ts':'8:40','note':K('분열 전에 신성한 오브로 아군 피해를 최대(119%)까지.','Divine the ally damage to its maximum (119%) before fracturing.')},
  {'id':'z5','phase':'base','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'9:56',
   'note':K('좌측 강령술의 징조 + 보존된 턱뼈로 접두에 훼손해 4줄(공개 전 훼손 줄은 분열 안 됨 → 1/3).','Sinistral Necromancy + Preserved Jawbone desecrates a prefix for four lines (an unrevealed desecration cannot fracture, so 1 in 3).')},
  {'id':'z6','phase':'base','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':mz_dmg}]},'fail':{'goto':'restart'},'ts':'11:25','after':{'keepOnly':[mz_dmg,'junk1']},
   'note':K('아군 피해 분열 1/3. 영상은 셉터 4개 중 세 번째에서 성공. 이후 소멸의 오브로 분열 + 잡옵 1줄만 남김(영상 23:38).','Ally damage fractures 1 in 3; the third of four sceptres hit. Then annul down to the fracture plus one junk line (23:38).')},
  {'id':'z7','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'gi':mz_mana,'tmax':1},'fail':{'goto':'self'},'ts':'23:59',
   'note':K('카오스 오브로 마나 최대치 1티어. 마나 재생·존재 범위 1티어 같은 필수 접미가 먼저 뜨면 그쪽부터 진행해도 됨.','Chaos for tier 1 maximum mana. If a must-have suffix (T1 mana regen or presence area) lands first, you can work from that instead.')},
  {'id':'z8','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':[{'gi':mz_spirit,'tmax':1},{'gi':mz_hyb,'tmax':1}]},'fail':{'goto':'self','via':MZ_ANN,'lost':'z7'},'ts':'29:49',
   'note':K('좌측 찬미의 징조 + 상위 엑잘티드 오브로 정신력 증가 1티어(또는 정신력·마나 하이브리드 1티어). 가중치가 매우 낮아 가장 오래 걸림(영상 약 2시간 반 만에 성공). 빗나가면 소멸의 오브(마나가 지워지면 카오스 오브부터).','Sinistral Exaltation + Greater Exalt for tier 1 increased spirit (or tier 1 spirit/mana hybrid). Very low weight, the longest part (about two and a half hours in the video). Annul misses; if the mana goes, back to the Chaos step.')},
  {'id':'z9','phase':'suf','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'22:11',
   'note':K('제작 옵션을 하나 더(합금 + 심연의 에센스를 같이 쓰기 위함). 빼낼 수 있어서 마지막에 교체.','One more crafted modifier, so the alloy and Essence of the Abyss can sit together; removable, swapped at the end.')},
  {'id':'z10','phase':'suf','do':'exalt','cur':'Exalted_Orb','target':{'junk':'s'},'ts':'47:58','note':K('합금이 바꿀 접미 하나(접두가 꽉 차서 징조 불필요).','A suffix for the alloy to replace (prefixes are full, no omen).')},
  {'id':'z11','phase':'suf','do':'essence','cur':'Sovereign_Alloy','omens':['Omen_of_Dextral_Crystallisation'],'target':{'gi':mz_aug},'ts':'47:58',
   'note':K('우측 결정화의 징조 + 군왕의 합금: 그 줄을 장착 증강 효과 30% 증가로. 깎기(절사의 징조)를 쓰면 레벨 70인 마나 1티어가 지워져서, 접미는 합금·훼손·엑잘로 채움. 증강 효과 덕에 존재 범위 소울 코어 효과가 커져 존재 범위 접미를 대신함.','Dextral Crystallisation + Sovereign Alloy turns it into 30% socketed augment effect. Whittling would remove the level 70 T1 mana, so suffixes come from the alloy, desecration and exalts. The augment boost to a presence-area core stands in for the presence area suffix.')},
  {'id':'z12','phase':'suf','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'s'},'ts':'57:29','note':K('접두가 꽉 차서 보존된 턱뼈 훼손은 접미로.','Prefixes are full, so the Preserved Jawbone desecration lands on a suffix.')},
  {'id':'z13','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':mz_regen,'tmax':1},{'gi':mz_aoe,'tmax':1},{'gi':mz_cast,'tmax':1}]},'side':'s','bone':'Preserved_Jawbone'},'ts':'57:29',
   'note':K('심연의 메아리의 징조로 공개해 마나 재생 1티어(영상 63%)나 존재 범위·시전 속도. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시.','Reveal with Abyssal Echoes for tier 1 mana regeneration (63% in the video), presence area or cast speed; otherwise Omen of Light + Annulment and desecrate again.')},
  {'id':'z14','phase':'suf','branch':{'of':'z13','when':'ok'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':MZ_SUF},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'z11'},'ts':'57:29',
   'note':K('완벽한 엑잘티드 오브로 마지막 접미(레벨 50 미만 옵션 제외). 영상은 아군 시전 속도 1티어로 완성. 빗나가면 우측 소멸의 징조 + 소멸의 오브(좋은 줄이 지워지면 그 단계부터).','Perfect Exalt the last suffix (no modifiers below level 50); the video finished on tier 1 ally cast speed. On a miss, Dextral Annulment (if a good line goes, redo its step).')},
  {'id':'z14b','phase':'suf','branch':{'of':'z13','when':'ok'},'do':'note','fallbackFor':'z14','label':K('갈림길: 막아 두고 다시','Fork: block and retry'),'ts':'45:01',
   'note':K('빗나간 접미를 우측 결정화의 징조 + 심연의 에센스로 징표로 바꾸고, 보존된 턱뼈 훼손 → 심연의 메아리 공개에서 가중치가 가장 큰 아군 생명력 재생(10000)을 골라 그 계열을 막아 둔 채 완벽한 엑잘티드 오브. 그 줄은 나중에 군왕의 합금(우측 결정화)으로 바꿀 수 있음(영상 57:07에서 확인).','Turn the missed suffix into the Mark with Dextral Crystallisation + Essence of the Abyss, desecrate with a Preserved Jawbone and pick ally life regeneration (weight 10000, the biggest) on reveal to block that family, then Perfect Exalt. That line can later be swapped out with a Sovereign Alloy (Dextral Crystallisation), as the video found at 57:07.')},
  # reveal missed (사용자 확정 2026-11-09): leave the miss, finish the last suffix first, redo the desecration last
  {'id':'zm1','phase':'suf','branch':{'of':'z13','when':'miss'},'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':MZ_SUF},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'z11'},
   'note':K('공개가 빗나가면 그대로 두고 마지막 접미부터.','On a reveal miss, leave it and do the last suffix first.')},
  {'id':'zm2','phase':'suf','branch':{'of':'z13','when':'miss'},'do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True}},
  {'id':'zm3','phase':'suf','branch':{'of':'z13','when':'miss'},'do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'s'}},
  {'id':'zm4','phase':'suf','branch':{'of':'z13','when':'miss'},'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':mz_regen,'tmax':1},{'gi':mz_aoe,'tmax':1},{'gi':mz_cast,'tmax':1}]},'side':'s','bone':'Preserved_Jawbone'},'fail':{'goto':'zm3','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}}},
  {'id':'z15','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('존재 범위 증강물','presence area augment')]},'ts':'57:50',
   'note':K('신성한 오브로 마나 재생·시전 속도 수치 정리. 아스트리드의 창의성은 존재 범위 증가 증강물로 교체(증강 효과로 63%). 바알 신비학자의 주입기로 퀄리티 21%(영상: 첫 번째는 타락하지 않음), 스킬 레벨 20, 젬 소켓 5개.','Divine mana regeneration and cast speed. Swap Astrid\'s Creativity for a presence area augment (63% with the augment effect). Vaal Arcanist\'s Infuser to 21% quality (the video says the first one never corrupts), skill level 20 and five gem sockets.')},
 ]})
