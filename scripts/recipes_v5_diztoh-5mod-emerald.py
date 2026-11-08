# Diztoh: 5-mod Emerald for Monk (Potent Liquid Contempt + Ferocity) — youtu.be/s70CV_nvjXg
DZE=K('Diztoh 영상 기반','Based on Diztoh')
c='Emerald'
def textB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
em_cdmg=textB('Critical Damage Bonus for Attack Damage','n','s'); em_as=textB('% increased Attack Speed','n','s'); em_qas=textB('Attack Speed with Quarterstaves','n','s')
em_adm=textB('increased Attack Damage','n','p'); em_qdm=textB('Damage with Quarterstaves','n','p')
em_plus=textB('+1 Suffix Modifier allowed','x','p'); em_eff=textB('Effect of Suffixes','x','p')
assert cd(c)['groups'][em_as]['t'][0][5].startswith('(2—4)% increased Attack Speed') and 'with' not in cd(c)['groups'][em_as]['t'][0][5]
R.append({
 'id':'diztoh-5mod-emerald','cls':c,'base':0,'ilvl':80,'cap':{'p':2,'s':2},'difficulty':3,'budget':'high','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('몽크','Monk'),K('육척봉','Quarterstaff'),K('공격 속도','Attack speed')],'patch':'0.5','created':'2026-11-09','author':DZE,
 'source':{'url':'https://www.youtube.com/watch?v=s70CV_nvjXg','title':'Crafting 5 Mod Emeralds For my Monk | POE 2 0.5','channel':'Diztoh'},
 'title':K('공격 속도 접미 3줄 + 접미 효과 5옵션','three attack speed/crit suffixes + suffix effect, five mods'),
 'start':{'rar':'rare','mods':[{'gi':em_cdmg},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미 2줄','en':'Two suffixes'},{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'des','kr':'3번째 접미 (훼손)','en':'Third suffix (desecrated)'},{'id':'pre','kr':'접두 · 흉포함','en':'Prefixes and Ferocity'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'e1','phase':'suf','do':'base','cost':'base','ts':'0:41','note':K('공격 치명타 피해 보너스 접미가 붙은 희귀 에메랄드(아이템 레벨 80). 영상은 원소 피해 접두가 같이 붙은 것을 구매. 거래소에서 "제작됨"으로 속인 매물 주의.','A rare Emerald (item level 80) with an attack crit damage bonus suffix; the video bought one with an elemental damage prefix. Watch for listings faking a "crafted" line.')},
  {'id':'e2','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'anyOf':[{'gi':em_qas},{'gi':em_as}]},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'e1'},'ts':'1:24',
   'note':K('우측 찬미의 징조 + 엑잘티드 오브로 공격 속도 접미(영상은 육척봉 공격 속도). 아니면 소멸의 오브.','Dextral Exaltation + Exalt for an attack speed suffix (quarterstaff attack speed in the video); annul on a miss.')},
  {'id':'e3','phase':'con','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'2:27','note':K('접두를 2줄로 채움(아무 옵션).','Fill the prefixes to two (anything).')},
  {'id':'e4','phase':'con','do':'essence','cur':'Potent_Liquid_Contempt','knownP':True,'target':{'gi':em_plus,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'restart'},'ts':'2:53',
   'note':K('위력적인 액체 경멸: 옵션 하나를 지우고 "+1 접미 허용" 또는 "+1 접두 허용"(50/50). 접미 쪽이 나와야 성공.','Potent Liquid Contempt removes a mod and adds "+1 suffix allowed" or "+1 prefix allowed" (50/50); you need the suffix one.')},
  {'id':'e5','phase':'des','do':'desecrate','cur':'Preserved_Cranium','target':{'unrev':'s'},'ts':'3:14','note':K('보존된 두개골로 훼손: 3번째 접미로 들어감.','Desecrate with a Preserved Cranium; it lands on the third suffix.')},
  {'id':'e6','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':em_as},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'e5','via':LIGHT},'ts':'3:35',
   'note':K('심연의 메아리의 징조를 켜고 공격 속도 공개(공격 치명타 피해·육척봉 공격 속도도 OK). 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손.','Reveal attack speed with Abyssal Echoes (attack crit damage or quarterstaff attack speed also fine). Otherwise Light + Annulment and desecrate again.')},
  {'id':'e7','phase':'pre','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment'],'target':{'dropGi':em_plus},'extra':{'Orb_of_Annulment':0.5,'Omen_of_Sinistral_Annulment':0.5},'ts':'5:19','note':K('좌측 소멸의 징조 + 소멸의 오브로 "+1 접미 허용"을 지움(접두 50/50). 접미 3줄은 그대로 남음.','Sinistral Annulment removes "+1 suffix allowed" (a prefix 50/50); the three suffixes stay.')},
  {'id':'e8','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'5:41','note':K('아무 접두 하나(영상은 위험 피해).','Any prefix (hazard damage in the video).')},
  {'id':'e9','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':[{'gi':em_adm},{'gi':em_qdm}],'replace':'p'},'fail':{'goto':'self'},'ts':'6:03',
   'note':K('접미가 상한보다 많은 상태라 카오스 오브가 접두만 바꿈(그 사이에 소멸의 오브를 쓰면 안 됨). 공격 피해 증가 또는 육척봉 피해 증가.','With suffixes over the cap, Chaos only rerolls prefixes (do not annul in between). Aim for increased attack damage or quarterstaff damage.')},
  {'id':'e10','phase':'pre','do':'essence','cur':'Potent_Liquid_Ferocity','knownP':True,'target':{'gi':em_eff,'chance':0.5},'fail':{'goto':'e9'},'ts':'7:52',
   'note':K('위력적인 액체 흉포함: 접두 하나를 지우고 "접미 효과 증가". 잡옵 접두가 지워지면 성공(50/50), 좋은 접두가 지워지면 카오스 오브부터 다시. 영상 첫 번째는 원소 피해가 지워져 성공, 두 번째는 여러 번 실패.','Potent Liquid Ferocity removes a prefix and adds "increased effect of suffixes". Success when the junk prefix goes (50/50); otherwise chaos again. The first emerald hit; the second missed several times.')},
  {'id':'e11','phase':'fin','do':'quality','cur':'Refined_Reaver_Catalyst','target':{'quality':20},'ts':'11:23','note':K('제련된 강탈자 기폭제로 공격 퀄리티 20%. 신성한 오브로 수치 정리(접미 효과 덕에 최대치를 넘음).','Refined Reaver Catalysts to 20% attack quality; divine the rolls (they exceed their max thanks to suffix effect).')},
  {'id':'e12','phase':'fin','do':'note','ts':'26:14','note':K('완성. 영상은 두 개를 만들어 타락시켰는데 하나는 6번째 옵션(마나 흡수)이 붙었다가 두 번째 타락에서 둘 다 망가짐: 타락은 선택.','Done. The video corrupted both: one gained a sixth mod (mana leech), then a second corruption bricked both. Corrupting is optional.')},
 ]})
