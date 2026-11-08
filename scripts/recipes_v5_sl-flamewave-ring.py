# ---- SL 게임연구소 "#3 검은 화염파 반지 제작 가이드" (youtu.be/UAF91gEFRkM) ----
c='Rings'
SL=K('SL 게임연구소 영상 기반','Based on SL 게임연구소')
def textG(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return max(hits, key=lambda gi: cd(c)['groups'][gi]['t'][0][0])   # the ladder with the highest tier
gr_all=textG('to all Elemental Resistances','n','s'); gr_maxQ=textG('to Maximum Quality','e','p')
gr_rarP=textG('increased Rarity of Items found','n','p'); gr_rarS=textG('increased Rarity of Items found','n','s'); gr_chaosD=textG('increased Chaos Damage','n','p')
gr_spellC=textG('Spells Gain','x','p')
GR_PRE=[{'gi':gr_rarP,'tmax':1},{'gi':gr_chaosD,'tmax':1}]
GR_RES=[{'gi':textG(t,'n','s'),'tmax':1} for t in ('to Fire Resistance','to Cold Resistance','to Lightning Resistance','to Chaos Resistance')]
GR_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'sl-flamewave-ring','cls':c,'base':base(c,'Gold Ring'),'ilvl':82,'difficulty':3,'budget':'medium',
 'buildTags':[K('검은 화염파','Black Flame Wave'),K('카오스','Chaos'),K('희귀도','Rarity')],'patch':'0.5.5','created':'2026-11-09','author':SL,
 'source':{'url':'https://www.youtube.com/watch?v=UAF91gEFRkM','title':'[POE2 0.5.5] #3 검은 화염파 반지 제작 가이드','channel':'SL 게임연구소!'},
 'title':K('모든 원소 저항 분열 + 카오스 피해 + 별세계 주문 카오스 획득 (카오스 퀄리티)','fractured all res + chaos damage + Otherworldly spell chaos gain (chaos quality)'),
 'start':{'rar':'magic','mods':[{'gi':gr_all,'tmax':1},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fracture','kr':'모든 원소 저항 분열','en':'Fracture all res'},{'id':'quality','kr':'퀄리티 작업','en':'Quality'},
           {'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미','en':'Suffixes'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'0:47',
   'note':K('모든 원소 저항 +16%(1티어)가 붙은 매직 황금 반지, 아이템 레벨 82. 목표 옵션 중 82레벨은 없지만 단일 원소 저항 1티어(레벨 82)를 카오스 저항으로 바꾸려면 82가 필요. 다른 베이스도 가능.','A magic Gold Ring with +16% all elemental resistances (T1), item level 82. No target needs 82, but turning a T1 single resistance (level 82) into chaos resistance does. Other bases work too.')},
  {'id':'g2','phase':'fracture','do':'regal','cur':'Regal_Orb','target':{'junk':'s'},'ts':'3:13','note':K('제왕의 오브로 레어(옵션은 상관없음).','Regal to rare (any modifier).')},
  {'id':'g3','phase':'fracture','do':'desecrate','cur':'Preserved_Collarbone','target':{'unrev':'p'},'ts':'3:17','note':K('보존된 빗장뼈로 4줄(훼손은 분열되지 않음).','A Preserved Collarbone makes four lines (the desecration cannot fracture).')},
  {'id':'g4','phase':'fracture','do':'fracture','cur':'Fracturing_Orb','target':{'anyOf':[{'gi':gr_all}]},'fail':{'goto':'restart'},'after':{'keepOnly':[gr_all,'junk']},'ts':'3:20',
   'note':K('훼손 제외 3줄 중 1줄(1/3). 카오스 저항이 가중치는 더 낮지만 단일 원소 저항을 카오스 저항으로 바꿀 수 있어 모든 원소 저항을 분열. 영상은 3개 모두 실패 후 분열된 반지를 구매.','1 in 3 (the desecration cannot fracture). Chaos resistance is rarer, but a single resistance can be turned into it, so all res is the one to fracture. The video failed all three and bought a fractured ring.')},
  {'id':'q1','phase':'quality','do':'essence','cur':'Essence_of_the_Breach','target':{'gi':gr_maxQ},'ts':'3:46','note':K('균열의 에센스로 최대 퀄리티 +20%.','Essence of the Breach: +20% Maximum Quality.')},
  {'id':'q2','phase':'quality','do':'quality','cur':'Chayulas_Catalyst','target':{'quality':40},'ts':'3:49','note':K('차율라의 기폭제로 카오스 퀄리티 40%(기본 20% + 최대 퀄리티 20%).','Chayula\'s Catalysts to 40% chaos quality (20% base + 20% from the Breach line).')},
  {'id':'q3','phase':'quality','do':'manual','cost':'vaal','optional':True,'target':{'setQuality':45},'label':K('바알 촉진시키는 주입기 (선택)','Vaal Catalysing Infuser (optional)'),'ts':'3:52',
   'note':K('자본이 있으면 바알 촉진시키는 주입기로 더 올림. 두 번까지는 거의 성공, 세 번째부터 타락 위험(실패하면 처음부터). 영상은 한 번 더 발라 45%.','With spare currency, push higher with Vaal Catalysing Infusers: two almost always work, from the third it can corrupt (then start over). The video stopped at 45%.')},
  {'id':'p0','phase':'pre','do':'remove','cur':'Orb_of_Annulment','expect':2,'after':{'keepOnly':[gr_all,'junk1']},'ts':'4:26',
   'note':K('소멸의 오브로 두 줄을 지워 분열 줄 + 한 줄만 남김. 퀄리티는 그대로 남음.','Annul two lines, leaving the fracture plus one line. The quality stays.')},
  {'id':'p1','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':GR_PRE},'fail':{'goto':'self'},'ts':'4:31',
   'note':K('카오스 오브로 접두 희귀도 1티어 또는 카오스 피해 1티어. 남은 한 줄이 최대 퀄리티여도 여기서 바뀜. 장신구는 좋은 옵션 가중치가 낮지만 원소 플랫 반지보다는 훨씬 쉬움.','Chaos for T1 prefix rarity or T1 chaos damage; if the line left is maximum quality, this replaces it. Jewellery weights are low, but far easier than an elemental flat ring.')},
  {'id':'p2','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':GR_PRE},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'p1'},'ts':'5:41',
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 나머지 하나. 접미엔 분열 줄뿐이라 실패하면 징조 없는 소멸의 오브(1/2로 앞 줄이 지워지면 카오스 오브부터). 생명력 1티어가 뜨면 그대로 써도 좋음(영상은 8번째에 카오스 피해 1티어).','Sinistral Exaltation + Perfect Exalt for the other one. Suffixes hold only the fracture, so a miss takes a plain Annulment (half the time it takes the first line: chaos again). A T1 life roll is fine to keep (the video hit T1 chaos damage on try 8).')},
  {'id':'p3','phase':'pre','do':'desecrate','cur':'Altered_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'},'ts':'7:17','note':K('좌측 강령술의 징조 + 뒤바뀐 빗장뼈로 마지막 접두 훼손. 주문이 피해의 %를 카오스 피해로 획득은 뒤바뀐 빗장뼈에서만 나오는 별세계 옵션.','Sinistral Necromancy + Altered Collarbone desecrates the last prefix; spells gaining damage as chaos is an Otherworldly modifier only this bone gives.')},
  {'id':'p4','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':gr_spellC},'side':'p','bone':'Altered_Collarbone'},'fail':{'goto':'p3','via':GR_LIGHT},'ts':'7:28',
   'note':K('심연의 메아리의 징조로 공개해 주문이 피해의 %를 카오스 피해로 획득. 별세계 옵션은 가중치가 공개되지 않음. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시(영상은 세 번째).','Reveal with Abyssal Echoes for spells gaining damage as chaos; Otherworldly weights are not published. Otherwise Light + Annulment and again (third try in the video).')},
  {'id':'s1','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':GR_RES},'fail':{'goto':'s2'},'ts':'8:35',
   'note':K('접두가 꽉 차서 상위 찬미의 징조 + 완벽한 엑잘티드 오브의 두 줄이 모두 접미로. 저항 1티어 아무거나: 단일 원소 저항 1티어는 공허 유동체로 카오스 저항 1티어로 바꿈(카오스 퀄리티가 적용됨). 2티어로 만족해도 됨.','Prefixes are full, so Greater Exaltation puts both lines on suffixes: any T1 resistance. A T1 single elemental resistance is turned into T1 chaos resistance with a void liquid (chaos quality applies). T2 is acceptable.')},
  {'id':'s2','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','withEach':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'target':{'anyOf':GR_RES,'replace':'s'},'fallbackFor':'s1','fail':{'goto':'self'},'ts':'8:43',
   'note':K('안 뜨면 우측 소멸의 징조 + 소멸의 오브로 접미 하나를 지우고 완벽한 엑잘티드 오브 반복(영상은 여러 번 끝에 번개 저항 1티어). 우측 소멸의 징조가 비싸니 자본에 맞게.','On a miss, Dextral Annulment removes a suffix and a Perfect Exalt tries again (the video needed many tries for T1 lightning resistance). Dextral Annulment is pricey, so mind your budget.')},
  {'id':'s3','phase':'suf','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'target':{'gi':gr_rarS,'tmax':1,'replace':'s'},'fail':{'goto':'self'},'ts':'10:19',
   'note':K('절사의 징조 + 우측 말소의 징조 + 완벽한 카오스 오브로 마지막 접미 줄을 희귀도 1티어로. 접두 희귀도(레벨 47)가 레벨이 가장 낮아서 말소 징조로 접미만 바뀌게 함. 영상은 비용 때문에 시전 속도 등에서 멈춤.','Whittling + Dextral Erasure + Perfect Chaos turns the last suffix into T1 rarity. Prefix rarity (level 47) is the lowest level, so the Erasure keeps the change on suffixes. The video stopped early (cast speed etc.) to save currency.')},
 ],
})
