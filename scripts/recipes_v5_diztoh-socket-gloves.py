# ---- Diztoh "How to Craft 60% Socket Effect +2 Projectile Gloves | PoE 2 0.5 Guide" (youtu.be/CI7zQO_Ml_s) ----
DZ5=K('Diztoh 영상 기반','Based on Diztoh')
c='Gloves_int'
def textD(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
dz_proj=textD('+2 to Level of all Projectile Skills','x','s'); dz_pdmg=textD('increased Projectile Damage','x','p'); dz_pspd=textD('increased Projectile Speed','x','p')
dz_esf=textD('to maximum Energy Shield','n','p'); dz_esp=textD('% increased Energy Shield','n','p')
dz_rar=textD('increased Rarity of Items found','e','s'); dz_aug=textD('increased effect of Socketed Augment Items','e','s')
DZ_ANN={'cur':'Orb_of_Annulment'}
R.append({
 'id':'diztoh-socket-gloves','cls':c,'base':base(c,'Sirenscale Gloves'),'ilvl':81,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'medium','unknownW':True,
 'buildTags':[K('투사체','Projectile'),K('에너지 보호막','Energy Shield'),K('아이템 희귀도','Item rarity')],'patch':'0.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=CI7zQO_Ml_s','title':'How to Craft 60% Socket Effect +2 Projectile Gloves | PoE 2 0.5 Guide','channel':'Diztoh'},
 'title':K('투사체 +2 분열 + 장착 증강 효과 60%','fractured +2 projectile, 60% socketed augment effect'),
 'start':{'rar':'normal','quality':20,'runes':[K('콜르의 사냥',"Kolr's Hunt")],'mods':[]},
 'phases':[{'id':'base','kr':'매직 · 분열','en':'Magic and fracture'},{'id':'ess','kr':'에센스 2개','en':'Two essences'},{'id':'pre','kr':'접두 채우기','en':'Fill prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'d1','phase':'base','do':'base','cost':'base','ts':'0:17','note':K('특출난 사이렌비늘 장갑(룬 소켓 2개, 아이템 레벨 81), 퀄리티 20%. 매직으로 만들기 전에 콜르의 사냥 룬부터 장착해 투사체 옵션이 붙게 함.','Exceptional Sirenscale Gloves (two rune sockets, item level 81) at 20% quality. Socket Kolr\'s Hunt before making it magic so projectile mods can roll.')},
  {'id':'d2','phase':'base','do':'transmute','cur':'Orb_of_Transmutation','target':{'gi':dz_proj},'fail':{'goto':'self','via':DZ_ANN},'ts':'0:35',
   'note':K('진화의 오브로 투사체 스킬 +2. 다른 접미가 붙으면 소멸의 오브로 지우고 다시. 재화가 모자라면 희귀로 만들어 카오스 오브를 돌려도 됨.','Transmute for +2 projectile skills; annul any other suffix and retry. Short on currency, go rare and spam Chaos instead.')},
  {'id':'d3','phase':'base','do':'augment','cur':'Orb_of_Augmentation','target':{'gi':dz_esf,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}},'ts':'1:26',
   'note':K('확장의 오브로 접두에 에너지 보호막 최대치. 영상은 금방 1티어(+48)가 뜸.','Augment for flat maximum energy shield on the prefix; the video hit tier 1 (+48) quickly.')},
  {'id':'d4','phase':'base','do':'essence','cur':'Greater_Essence_of_Opulence','target':{'gi':dz_rar},'ts':'2:02',
   'note':K('상위 풍요의 에센스로 희귀 + 아이템 희귀도(1티어). 이 줄은 제작 옵션이라 다음 에센스엔 아스트리드의 창의성이 필요함.','Greater Essence of Opulence: rare plus tier 1 item rarity. That line is crafted, so the next essence needs Astrid\'s Creativity.')},
  {'id':'d5','phase':'base','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'2:38',
   'note':K('좌측 강령술의 징조 + 보존된 갈비뼈로 접두에 훼손해 4줄. 공개하지 않은 훼손 줄은 분열이 안 걸려서 분열 확률 1/3. 분열 전 신성한 오브로 에너지 보호막 수치를 올림(영상 +59).','Sinistral Necromancy + Preserved Rib desecrates a prefix for four lines; an unrevealed desecration cannot fracture, so the odds are 1 in 3. Divine the energy shield roll before fracturing (+59 in the video).')},
  {'id':'d6','phase':'base','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':dz_proj}]},'fail':{'goto':'restart'},'ts':'3:29',
   'note':K('투사체 스킬 +2 분열 1/3. 영상은 한 번에 성공.','+2 projectile skills fractures 1 in 3; the video hit first try.')},
  {'id':'d7','phase':'ess','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'3:46',
   'note':K('두 번째 소켓에. 제작 옵션을 하나 더 붙일 수 있게 함.','In the second socket: allows one more crafted modifier.')},
  {'id':'d8','phase':'ess','do':'essence','cur':'Essence_of_Horror','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':dz_aug,'chance':0.5},'ts':'4:03',
   'note':K('좌측 결정화의 징조 + 경악의 에센스: 접두 두 줄(에너지 보호막·훼손) 중 하나가 지워지고 접미에 장착 증강 효과 60% 증가. 훼손 줄이 지워지면 성공(1/2, 영상 성공). 에너지 보호막이 지워져도 망가지진 않고 그 자리도 아래에서 채움.','Sinistral Crystallisation + Essence of Horror: one of the two prefixes (energy shield or the desecration) goes and 60% socketed augment effect lands on a suffix. Losing the desecration is the hit (1 in 2; it hit in the video). Losing the energy shield does not brick it; that slot is filled below too.')},
  {'id':'d9','phase':'pre','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'},'ts':'4:53','note':K('접미가 꽉 차서 고대 갈비뼈 훼손은 빈 접두로.','Suffixes are full, so the Ancient Rib desecration lands on a free prefix.')},
  {'id':'d10','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':dz_esp},{'gi':dz_pdmg},{'gi':dz_pspd}]},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'d9','via':LIGHT},'ts':'5:12',
   'note':K('심연의 메아리의 징조로 공개해 에너지 보호막 % 증가(목표). 투사체 피해·속도도 타협 가능(영상은 투사체 피해 2티어로 마무리). 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시.','Reveal with Abyssal Echoes for % increased energy shield (the goal); projectile damage or speed are fine (the video settled on tier 2 projectile damage). Otherwise Omen of Light + Annulment and desecrate again.')},
  {'id':'d11','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':[{'gi':dz_pspd},{'gi':dz_pdmg},{'gi':dz_esp}]},'ts':'5:30',
   'note':K('남은 접두는 완벽한 엑잘티드 오브(접미가 꽉 차서 징조 불필요). 영상은 투사체 속도 2티어. 영상은 첫 공개가 빗나갔을 때 그 줄을 둔 채 이걸 먼저 하고, 그 뒤 빛의 징조 + 소멸의 오브로 훼손을 다시 돌림.','The last prefix takes a Perfect Exalt (suffixes full, no omen); tier 2 projectile speed in the video. The video did this after its first reveal missed, keeping that line, then cleared it with Light + Annulment and desecrated again.')},
  {'id':'d12','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('페누무스의 회전의 룬',"Fenumus' Rune of Spinning")]},'ts':'6:25',
   'note':K('아스트리드의 창의성을 페누무스의 회전의 룬으로 교체(제작 옵션은 그대로, 시전 속도 8% → 장착 증강 효과로 12%). 영상은 바알 방어구 장인의 주입기로 퀄리티 22% 후 바알 오브 타락으로 소켓 3개를 노림(선택, 망가질 수 있음).','Swap Astrid\'s Creativity for Fenumus\' Rune of Spinning (crafted lines stay; 8% cast speed becomes 12% with the augment effect). The video then pushed quality to 22% with a Vaal Armourer\'s Infuser and corrupted for a third socket (optional, can brick).')},
 ]})
