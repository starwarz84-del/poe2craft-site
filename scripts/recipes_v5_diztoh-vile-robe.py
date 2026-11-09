# Diztoh: exceptional Vile Robe (fractured Spirit, Spirit reservation efficiency) — youtu.be/n97yEuKSWyM
DZV=K('Diztoh 영상 기반','Based on Diztoh')
c='Body_Armours_int'
def textB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
vr_spirit=textB('to Spirit','n','p'); vr_flat=textB('to maximum Energy Shield','n','p'); vr_pct=textB('% increased Energy Shield','n','p')
vr_res=textB('Spirit Reservation Efficiency of Skills','d','s')
vr_fire=textB('to Fire Resistance','n','s'); vr_cold=textB('to Cold Resistance','n','s'); vr_light=textB('to Lightning Resistance','n','s')
R.append({
 'id':'diztoh-vile-robe','cls':c,'base':base(c,'Vile Robe'),'ilvl':81,'sockets':3,'exceptional':{'sockets':1},'difficulty':3,'budget':'high',
 'buildTags':[K('정신력','Spirit'),K('에너지 보호막','Energy Shield'),K('젬링','Gemling')],'patch':'0.5.5','created':'2026-11-09','author':DZV,
 'source':{'url':'https://www.youtube.com/watch?v=n97yEuKSWyM','title':'I Crafted an Excpetional Spirit Vile Robe for my Gemling Spark Build | POE 2 0.5.5','channel':'Diztoh'},
 'title':K('정신력 분열 + 에너지 보호막 1티어 2줄 + 정신력 점유 효율','fractured Spirit + two T1 energy shield lines + Spirit reservation efficiency'),
 'start':{'rar':'rare','mods':[{'gi':vr_spirit,'tmax':4,'fr':True},{'junk':'p'}],'quality':20},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'des','kr':'정신력 점유 효율 (훼손)','en':'Reservation efficiency (desecration)'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'v1','phase':'base','do':'base','cost':'base','ts':'0:21','note':K('정신력 분열 특출난 끔찍한 로브(룬 소켓 3), 퀄리티 20%, 타락 안 됨. 거래소에서 정신력 분열(최소 45) + 소켓 3 + 타락 아님으로 검색, 약 30~45카오스.','An exceptional Vile Robe (3 rune sockets) with fractured Spirit, 20% quality, not corrupted. Search fractured Spirit (min 45), 3 sockets, not corrupted: about 30–45 chaos.')},
  {'id':'v2','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','target':{'gi':vr_flat,'tmax':1},'fail':{'goto':'self'},'ts':'3:06',
   'note':K('상위 카오스 오브로 에너지 보호막 최대치 1티어. 영상은 좌측 찬미의 징조 + 상위 엑잘티드 오브 + 소멸의 오브를 섞어 돌리다 6티어를 상위 카오스 오브로 바꿔 1티어.','Greater Chaos for T1 flat energy shield. The video mixed Sinistral Exaltation + Greater Exalts with annuls, then turned a T6 into T1 with a Greater Chaos.')},
  {'id':'v3','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'gi':vr_pct,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'v2'},'ts':'3:28',
   'note':K('좌측 찬미의 징조 + 상위 엑잘티드 오브로 에너지 보호막 % 증가(복합 말고 단일). 아니면 소멸의 오브(접미가 비어 있어 접두만 지워짐, 에너지 보호막 최대치가 지워지면 앞 단계부터). 영상은 1티어 101%.','Sinistral Exaltation + Greater Exalt for single % energy shield (not the hybrid). Otherwise annul (no suffixes, so it hits a prefix; if flat ES goes, back a step). T1 101% in the video.')},
  {'id':'v4','phase':'des','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 룬 장착',"Socket Astrid's Creativity"),'ts':'5:31',
   'note':K('제작 옵션 하나 더. 훼손을 빛의 징조 없이 다시 굴릴 때 에센스 두 개를 이어서 쓰기 위함.','One more crafted mod, so two essences can chain while rerolling the desecration without Omen of Light.')},
  {'id':'v5','phase':'des','do':'desecrate','cur':'Preserved_Rib','target':{'unrev':'s'},'ts':'8:17','note':K('보존된 갈비뼈로 훼손. 접두가 꽉 차 있어 접미로 들어감. 목표 옵션이 1티어뿐이라 고대 갈비뼈는 필요 없음.','Desecrate with a Preserved Rib; prefixes are full so it lands on a suffix. The target has a single tier, so no Ancient Rib needed.')},
  {'id':'v6','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':vr_res},'side':'s','bone':'Preserved_Rib'},'fail':{'goto':'self','via':{'cur':'Perfect_Essence_of_Seeking','omens':['Omen_of_Dextral_Crystallisation'],'also':[{'cur':'Essence_of_the_Abyss','omens':['Omen_of_Dextral_Crystallisation']},{'cur':'Preserved_Rib'}]}},'ts':'8:38',
   'note':K('심연의 메아리의 징조를 켜고 스킬의 정신력 점유 효율 증가(아마나무) 공개. 아니면 "빛 없이 다시 굴리기": 우측 결정화의 징조 + 완벽한 추구의 에센스로 훼손 줄을 지우고(유일한 접미), 우측 결정화의 징조 + 심연의 에센스로 그 줄을 심연 군주의 징표로 바꾼 뒤 다시 공개. 훼손 줄이 있는 채로는 심연의 에센스를 못 써서 추구의 에센스를 먼저 씀. 접미가 2줄이면 이 방법을 못 씀.',
            'Reveal with Abyssal Echoes for increased Spirit reservation efficiency of skills (Amanamu). Otherwise the lightless reroll: Dextral Crystallisation + Perfect Essence of Seeking removes the desecrated line (the only suffix), then Dextral Crystallisation + Essence of the Abyss turns it into the Mark; reveal again. The Abyss essence cannot go on while the desecrated line is there, hence Seeking first. Needs exactly one suffix.')},
  {'id':'v7','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['s','s']},'ts':'11:03',
   'note':K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 2줄. 저항 하나면 충분. 영상은 능력치 요구사항 감소 + 중독 지속시간 감소(꽝).','Omen of Greater Exaltation + Perfect Exalt adds two suffixes; one resistance is all you need. The video got reduced attribute requirements + reduced poison duration (a miss).')},
  {'id':'v8','phase':'suf','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':[{'gi':vr_fire,'tmax':3},{'gi':vr_cold,'tmax':3},{'gi':vr_light,'tmax':3}],'replace':'s'},'fail':{'goto':'self'},'ts':'12:49',
   'note':K('절사의 징조 + 상위 카오스 오브로 레벨이 가장 낮은 줄(영상은 중독 지속시간 3티어)을 저항으로 바꿈. 정신력 점유 효율(레벨 65)보다 낮은 줄이 남아 있는지 먼저 확인. 우측 소멸의 징조 + 소멸의 오브는 정신력 점유 효율이 지워질 수 있어 쓰지 않음. 영상은 냉기 저항 3티어.',
            'Whittling + Greater Chaos replaces the lowest-level line (T3 poison duration in the video) with a resistance. First check that a line below the reservation efficiency (level 65) is there. Dextral Annulment was skipped since it could hit the reservation line. T3 cold resistance in the video.')},
  {'id':'v9','phase':'fin','do':'note','target':{'runeSwap':[K('아스트리드의 창의성',"Astrid's Creativity"),K('여우 우상','Fox Idol')]},'ts':'15:39',
   'note':K('신성한 오브로 정신력 점유 효율 12%를 노림. 룬은 상위 철 룬 2개 + 아스트리드의 창의성 자리에 여우 우상. 저항은 치직대는 유동체로 번개 저항으로 바꿀 수 있음. 영상 시세 약 360디바인. 완성.',
            "Divine for 12% reservation efficiency. Runes: two Greater Iron Runes, and a Fox Idol replaces Astrid's Creativity. A Crackling Flux can turn the resistance into lightning. About 360 divines in the video. Done.")},
 ]})
