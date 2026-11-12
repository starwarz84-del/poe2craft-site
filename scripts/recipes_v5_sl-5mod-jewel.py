# ---- SL 게임연구소! "[POE2 0.5.5] #4 (5줄) 레어 주얼 제작 가이드" (youtu.be/VKMT7tuSIYk) ----
SL=K('SL 게임연구소! 영상 기반','Based on SL 게임연구소!')
c='Sapphire'
def textB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sj_dot=textB('Damaging Ailments deal damage','n','s')
sj_ail=textB('increased Magnitude of Ailments you inflict','n','p'); sj_ign=textB('increased Ignite Magnitude','n','p')
sj_spell=textB('increased Spell Damage','n','p'); sj_chaos=textB('increased Chaos Damage','n','p'); sj_with=textB('increased Withered Magnitude','n','p')
sj_plusP=textB('+1 Prefix Modifier allowed','x','s'); sj_effP=textB('increased Effect of Prefixes','x','s')
SJP=[{'gi':sj_ign},{'gi':sj_ail},{'gi':sj_spell},{'gi':sj_chaos},{'gi':sj_with}]
R.append({
 'id':'sl-5mod-jewel','cls':c,'base':0,'ilvl':82,'cap':{'p':2,'s':2},'difficulty':3,'budget':'medium','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('상태 이상','Ailments'),K('카오스','Chaos')],'patch':'0.5.5','created':'2026-11-09','author':SL,
 'source':{'url':'https://www.youtube.com/watch?v=VKMT7tuSIYk','title':'[POE2 0.5.5] #4 (5줄) 레어 주얼 제작 가이드 (맥롤까지 비교적 저렴하게 띄우기)','channel':'SL 게임연구소!'},
 'title':K('접두 옵션 3개 5옵션 · 상태 이상 가속 분열','five mods with three prefixes, fractured ailment speed'),
 'start':{'rar':'rare','mods':[{'gi':sj_dot,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'pre','kr':'접두 옵션 2개','en':'Two prefixes'},{'id':'con','kr':'경멸: 접두 +1','en':'Contempt: +1 prefix'},{'id':'des','kr':'3번째 접두 (훼손)','en':'Third prefix (desecrated)'},{'id':'fer','kr':'흉포함: 접두 효과','en':'Ferocity: prefix effect'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'s1','phase':'pre','do':'base','cost':'base','ts':'4:42','note':K('피해를 주는 상태 이상의 피해 7% 가속(최대치) 사파이어를 사서 분열의 오브로 그 옵션을 분열(옵션 4개이라 1/4, 보존된 두개골은 비싸서 생으로). 소멸의 오브로 분열 + 옵션 1개만 남긴 상태. 이 접미는 정말 안 떠서 분열부터 하는 게 결국 더 쌈.','Buy Sapphires with max 7% faster damaging ailments and fracture that line (1 in 4 with four mods; Preserved Cranium is too pricey). Annul down to the fracture plus one line. This suffix almost never rolls, so fracturing it first ends up cheaper.')},
  {'id':'s2','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':SJP},'fail':{'goto':'self'},'ts':'7:00','note':K('카오스 오브로 원하는 접두 하나: 점화 강도·상태 이상의 강도·주문 피해·카오스 피해·위축 강도(검은 화염 기준).','Chaos for a wanted prefix: Ignite magnitude, ailment magnitude, spell, chaos damage or Withered magnitude (for Dark Flame).')},
  {'id':'s3','phase':'pre','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':SJP},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'s2'},'ts':'8:01',
   'note':K('좌측 찬미의 징조 + 엑잘티드 오브로 두 번째 접두. 주얼 옵션은 모두 1티어라 상위·완벽한 엑잘티드 오브가 필요 없음. 쓸모없는 옵션이면 소멸의 오브(1/2로 첫 옵션이 지워지면 카오스 오브부터).','Sinistral Exaltation + Exalted Orb for a second prefix; jewel mods have a single tier, so no Greater or Perfect Exalt. On a miss, Annul (1 in 2 it takes the first prefix: chaos again).')},
  {'id':'s4','phase':'con','do':'exalt','cur':'Exalted_Orb','target':{'junk':'s'},'ts':'8:20','note':K('접미에 아무 옵션 하나.','Any suffix.')},
  {'id':'s5','phase':'con','do':'essence','cur':'Potent_Liquid_Contempt','knownP':True,'target':{'gi':sj_plusP,'chance':round(1/3,3),'slots':{'p':1}},'fail':{'goto':'s2','via':{'cur':'Orb_of_Annulment'}},'ts':'8:28',
   'note':K('위력적인 액체 경멸: 분열 옵션 빼고 옵션 세 개 중 하나를 지우고 "접두어 속성 부여의 최대 개수 +1개". 접미 잡옵이 지워져야 성공(1/3). 접두가 지워지면 소멸의 오브로 분열 + 옵션 1개로 되돌리고 카오스 오브부터.','Potent Liquid Contempt removes one of the three non-fractured lines and adds "+1 Prefix Modifier allowed". It must take the junk suffix (1 in 3); otherwise annul back to the fracture plus one line and chaos again.')},
  {'id':'s6','phase':'des','do':'desecrate','cur':'Preserved_Cranium','target':{'unrev':'p'},'ts':'8:50','note':K('보존된 두개골로 세 번째 접두 훼손.','Preserved Cranium desecrates the third prefix.')},
  {'id':'s7','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':SJP},'side':'p','bone':'Preserved_Cranium'},'fail':{'goto':'s6','via':LIGHT},'ts':'9:05','note':K('심연의 메아리의 징조로 공개해 남은 원하는 접두(영상은 주문 피해). 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손.','Reveal with Abyssal Echoes for the remaining wanted prefix (spell damage in the video); otherwise Light + Annulment and desecrate again.')},
  {'id':'s8','phase':'fer','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment'],'target':{'dropGi':sj_plusP},'ts':'9:21','note':K('우측 소멸의 징조 + 소멸의 오브로 "접두어 속성 부여의 최대 개수 +1개"를 지움(접미는 분열 옵션과 이 옵션뿐이라 확정). 접두 옵션 3개는 그대로 남음.','Dextral Annulment removes "+1 Prefix Modifier allowed" (the only other suffix is fractured, so it is certain). The three prefixes stay.')},
  {'id':'s9','phase':'fer','do':'exalt','cur':'Exalted_Orb','target':{'junk':'s'},'ts':'9:30','note':K('엑잘티드 오브로 접미 잡옵 하나를 꼭 채움(흉포함이 지울 옵션).','Exalted Orb to fill a junk suffix, which Ferocity will replace. Required.')},
  {'id':'s10','phase':'fer','do':'divine','cur':'Divine_Orb','optional':True,'ts':'9:40','note':K('신성한 오브로 접두 옵션 3개를 최대치 근처까지.','Divine the three prefixes close to max.')},
  {'id':'s11','phase':'fer','do':'essence','cur':'Potent_Liquid_Ferocity','knownP':True,'target':{'gi':sj_effP},'ts':'10:01',
   'note':K('위력적인 액체 흉포함: 접미 잡옵이 지워지고 "접두어 효과 (40~60)% 증가". 안 먹을 때가 있는데 먹을 때까지 바르면 됨. 수치가 낮으면 카오스 오브(이 옵션만 바뀜)로 잡옵으로 돌린 뒤 다시 흉포함, 55% 이상이면 마무리.','Potent Liquid Ferocity replaces the junk suffix with "(40–60)% increased Effect of Prefixes"; it sometimes fails to apply, keep using it. If the roll is low, Chaos (only this line changes) back to junk and Ferocity again; stop at 55% or more.')},
  {'id':'s12','phase':'fin','do':'quality','cur':'Chayulas_Catalyst','target':{'quality':20},'ts':'10:58','note':K('퀄리티 영향을 받는 옵션이 카오스 피해·주문 피해뿐. 시전 퀄리티 기폭제가 비싸서 싼 차율라의 기폭제(카오스)로 20%.','Only chaos and spell damage scale with quality; caster catalysts are pricey, so cheap Chayula\'s Catalysts (chaos) to 20%.')},
  {'id':'s13','phase':'fin','do':'note','ts':'11:30','note':K('타락 주얼 효과를 키우는 고유 주얼을 쓰면 바알 오브로 타락(영상 체감 약 1/3 실패, 2/3 성공 — 정확한 확률 아님). 완성.','If you use a unique jewel that boosts corrupted jewels, Vaal it (about 1/3 bad, 2/3 good by feel, not exact). Done.')},
 ]})
