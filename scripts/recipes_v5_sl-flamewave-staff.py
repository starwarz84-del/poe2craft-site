# ---- SL 게임연구소 "#1 화염파 종결급 지팡이 제작 가이드 | 검은 화염파" (youtu.be/6EzSVUItzsg) ----
c='Staves'
SL=K('SL 게임연구소 영상 기반','Based on SL 게임연구소')
def textS(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return max(hits, key=lambda gi: cd(c)['groups'][gi]['t'][0][0])   # the ladder with the highest tier
st_fire7=textS('Level of all Fire Spell Skills','n','s')
st_spell=textS('increased Spell Damage','n','p'); st_fireP=textS('increased Fire Damage','n','p'); st_coldP=textS('increased Cold Damage','n','p')
st_lightP=textS('increased Lightning Damage','n','p'); st_chaosP=textS('increased Chaos Damage','n','p')
st_xF=textS('Extra Fire Damage','n','p'); st_xC=textS('Extra Cold Damage','n','p'); st_xL=textS('Extra Lightning Damage','n','p')
st_mag=textS('increased Explicit Fire Modifier magnitudes','x','s')
st_alloy=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='e' and 'Transcendent Alloy' in [x[3] for x in gr['t']]][0]
ST_PRE=[{'gi':gi,'tmax':1} for gi in (st_spell,st_fireP,st_coldP,st_lightP,st_chaosP,st_xF,st_xC,st_xL)]
ST_DMG=[{'gi':gi,'tmax':1} for gi in (st_spell,st_fireP,st_coldP,st_lightP,st_chaosP)]
ST_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'sl-flamewave-staff','cls':c,'base':base(c,'Chiming Staff'),'ilvl':81,'sockets':3,'exceptional':{'sockets':1},'difficulty':4,'budget':'high',
 'buildTags':[K('검은 화염파','Black Flame Wave'),K('주문','Spell'),K('카오스','Chaos')],'patch':'0.5.5','created':'2026-11-09','author':SL,
 'source':{'url':'https://www.youtube.com/watch?v=6EzSVUItzsg','title':'[POE2 0.5.5] #1 화염파 종결급 지팡이 제작 가이드 | 검은 화염파','channel':'SL 게임연구소!'},
 'title':K('화염 주문 +7 분열 + 알두르의 배신 카오스 접두 + 스루드의 완력','fractured fire spell +7 + Betrayal of Aldur chaos prefixes + Thrud\'s Might'),
 'start':{'rar':'normal','mods':[]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fracture','kr':'화염 주문 +7 분열','en':'Fracture fire spell +7'},{'id':'pre','kr':'접두 3줄','en':'Three prefixes'},
           {'id':'rune','kr':'알두르의 배신 · 스루드의 완력','en':'Betrayal of Aldur and Thrud\'s Might'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'finish','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'t1','phase':'base','do':'base','cost':'base','ts':'0:25','note':K('아이템 레벨 81 이상, 룬 소켓 3개(특출난) 일반 차임벨 지팡이. 분열은 오래 걸리고 스트레스가 커서 화염 주문 +7 분열 지팡이가 적당한 값에 올라와 있으면 사서 5번부터 시작하는 것도 방법(영상도 분열 실패 후 구매).','A normal item level 81+ Chiming Staff with 3 rune sockets (exceptional). Fracturing is slow and painful: if a fractured fire spell +7 staff is listed at a fair price, buy it and start from step 5 (the video bought one after its fractures failed).')},
  {'id':'t2','phase':'fracture','do':'transmute','cur':'Orb_of_Transmutation','target':{'junk':'p'},'ts':'2:43','note':K('진화의 오브로 매직. 모든 화염 주문 스킬 레벨 +7은 접미라 진화의 오브는 접두에 붙어야 함 — 접미가 붙으면 소멸의 오브로 지우고 다시.','Transmute to magic. +7 fire spell skills is a suffix, so the Transmute must land a prefix; if it lands a suffix, annul and transmute again.')},
  {'id':'t3','phase':'fracture','do':'augment','cur':'Perfect_Orb_of_Augmentation','target':{'gi':st_fire7,'tmax':1},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'t2'},'ts':'2:46',
   'note':K('완벽한 확장의 오브로 남은 접미에 모든 화염 주문 스킬 레벨 +7. 안 뜨면 소멸의 오브: 접미가 지워지면 다시 확장, 접두가 지워지면(1/2) 남은 접미도 지우고 진화부터. 대략 120번에 한 번(영상은 소멸의 오브 약 70개). 레어 상태에서 카오스 오브로 띄워도 됨.','Perfect Augmentation for +7 to all fire spell skills in the open suffix. On a miss, annul: if the suffix goes, augment again; if the prefix goes (1/2), clear the suffix and transmute again. roughly 1 in 120 (about 70 Annulments in the video). Chaos on a rare works too.')},
  {'id':'t4','phase':'fracture','do':'regal','cur':'Perfect_Regal_Orb','target':{'junk':'p'},'ts':'3:47','note':K('매직 2줄을 채우고 완벽한 제왕의 오브로 레어(옵션은 상관없음).','Fill both magic slots, then a Perfect Regal to rare (any modifier).')},
  {'id':'t5','phase':'fracture','do':'desecrate','cur':'Preserved_Jawbone','target':{'unrev':'s'},'ts':'3:52','note':K('보존된 턱뼈로 4줄(훼손은 분열되지 않음).','A Preserved Jawbone makes four lines (the desecration cannot fracture).')},
  {'id':'t6','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':st_fire7}]},'fail':{'goto':'restart'},'ts':'4:48',
   'note':K('훼손 제외 3줄 중 1줄(1/3). 영상은 3개 동시에 분열해서 모두 실패 후 분열된 지팡이를 구매.','1 in 3 (the desecration cannot fracture). The video fractured three at once, all failed, and bought a fractured staff.')},
  {'id':'t7','phase':'fracture','do':'remove','cur':'Orb_of_Annulment','expect':2,'after':{'keepOnly':[st_fire7,'junk1']},'ts':'5:23',
   'note':K('소멸의 오브로 두 줄을 지워 분열 줄 + 한 줄만 남김.','Annul two lines, leaving the fracture plus one line.')},
  {'id':'p1','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':ST_DMG},'fail':{'goto':'self'},'ts':'5:29',
   'note':K('카오스 오브로 접두 피해 % 증가 1티어(주문·화염·냉기·번개·카오스). 알두르의 배신으로 원소가 카오스로 바뀌니 원소는 무관. 피해의 %를 추가 피해로 획득 1티어도 되지만 가중치가 낮은 피해 % 증가를 먼저(영상은 주문 피해 → 지워진 뒤 화염 피해 1티어).','Chaos for a T1 % damage prefix (spell, fire, cold, lightning or chaos); Betrayal of Aldur turns elements into chaos, so any element works. T1 gain-as-extra also works, but the rarer % damage comes first (the video hit spell damage, lost it, then T1 fire damage).')},
  {'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':ST_PRE},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'p1'},'ts':'6:55',
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 하나 더(피해 % 증가 또는 피해의 %를 추가 피해로 획득, 1티어). 접미엔 분열 줄뿐이라 실패하면 징조 없는 소멸의 오브(1/2로 앞 줄이 지워지면 카오스 오브부터).','Sinistral Exaltation + Perfect Exalt for a second T1 prefix (% damage or gain as extra). Suffixes hold only the fracture, so a miss takes a plain Annulment (half the time it takes the first line: chaos again).')},
  {'id':'p3','phase':'pre','do':'desecrate','cur':'Ancient_Jawbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'8:19','note':K('좌측 강령술의 징조 + 고대 턱뼈로 마지막 접두 훼손.','Sinistral Necromancy + Ancient Jawbone desecrates the last prefix.')},
  {'id':'p4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':ST_PRE},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'p3','via':ST_LIGHT},'ts':'8:25',
   'note':K('심연의 메아리의 징조로 공개해 남은 접두 1티어(영상은 피해의 %를 추가 피해로 획득 1티어). 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시.','Reveal with Abyssal Echoes for the last T1 prefix (gain as extra in the video); otherwise Light + Annulment and desecrate again.')},
  {'id':'r1','phase':'rune','do':'socket','cur':'rune:Betrayal of Aldur','ts':'8:54',
   'note':K('알두르의 배신 장착: 화염·냉기·번개 접두가 같은 티어의 카오스 옵션으로 바뀜(화염 주문 +7은 그대로).','Socket Betrayal of Aldur: the fire, cold and lightning prefixes become same-tier chaos ones (fire spell +7 stays).')},
  {'id':'r1b','phase':'rune','do':'note','label':K('가성비 마무리','Budget finish'),'ts':'9:13',
   'note':K('여기서 멈추는 것도 방법: 산울마녀 아산드라의 지혜의 룬 + 지콰니의 물결 영혼 핵을 끼우고, 접미는 엑잘티드 오브 두 줄 + 초월의 합금으로 마무리. 아래 방식보다 스킬 레벨이 1 낮지만(최종 피해 약 17% 차이) 비용이 몇 배 적음.','Stopping here is an option: socket Hedgewitch Assandra\'s Rune of Wisdom and Jiquani\'s Soul Core of Rippling, exalt two suffixes and finish with Transcendent Alloy. One skill level less than below (about 17% final damage) but several times cheaper.')},
  {'id':'r2','phase':'rune','do':'socket','cur':"rune:Thrud's Might",'ts':'11:05','note':K('스루드의 완력 장착: 파괴 속성(비고정 화염 속성 부여 규모 등)이 붙을 수 있게 됨.','Socket Thrud\'s Might so Destruction modifiers (explicit fire modifier magnitudes, etc.) can roll.')},
  {'id':'s1','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':'s','count':2},'ts':'11:11','note':K('접두가 꽉 차서 상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 2줄(잡옵).','Prefixes are full, so Greater Exaltation + Perfect Exalt adds two suffixes (junk).')},
  {'id':'s2','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'gi':st_mag,'replace':'s'},'fail':{'goto':'self'},'ts':'11:27',
   'note':K('절사의 징조 + 우측 말소의 징조 + 완벽한 카오스 오브로 접미의 잡옵을 돌려 비고정 화염 속성 부여 규모. 가중치가 공개되지 않음(영상 경험상 절사의 징조 20~30개).','Whittling + Dextral Erasure + Perfect Chaos rerolls a junk suffix into explicit fire modifier magnitudes. The weight is not published (20–30 Whittlings from the video author\'s experience).')},
  {'id':'s3','phase':'suf','do':'essence','cur':'Transcendent_Alloy','target':{'gi':st_alloy,'chance':0.5},'fail':{'goto':'s2'},'ts':'13:04',
   'note':K('초월의 합금으로 시전 속도 + 원소 피해의 %를 추가 냉기 피해로 획득. 접미가 꽉 차 있어 접미 한 줄이 지워짐(분열 제외 두 줄 중 잡옵이면 성공 1/2). 화염 속성 부여 규모가 지워지면 절사의 징조 단계부터. 시전 속도는 이 빌드에서 큰 옵션은 아니라 여기서 멈춰도 됨.','Transcendent Alloy adds cast speed + elemental damage as extra cold. Suffixes are full, so one of the two unfractured suffixes goes: 1/2 it is the junk. If it takes the fire magnitudes, go back to the Whittling step. Cast speed is not a big stat for this build, so stopping before this is fine.')},
  {'id':'f1','phase':'finish','do':'socket','cur':"rune:Hedgewitch Assandra's Rune of Wisdom",'ts':'2:07','note':K('세 번째 소켓에 산울마녀 아산드라의 지혜의 룬(모든 주문 스킬 레벨 +1).','Hedgewitch Assandra\'s Rune of Wisdom (+1 to all spell skills) in the third socket.')},
  {'id':'f2','phase':'finish','do':'note','ts':'14:17',
   'note':K('선택: 히네코라의 머리카락으로 미리 보거나 그냥 바알 오브로 타락시켜 소켓 하나 추가(1/4) → 지콰니의 물결 영혼 핵으로 스킬 레벨 +1. 실패하면 아이템이 망가질 수 있음(영상은 타락만 붙고 변화 없음).','Optional: preview with Hinekora\'s Lock or just corrupt with a Vaal Orb for a fourth socket (1 in 4), then Jiquani\'s Soul Core of Rippling for +1 skill level. It can brick the staff (the video only got the corruption).')},
 ],
})
