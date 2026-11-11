# ---- 시크의 Seek "[POE2]0.5.5 돌개바람 장화 제작 가이드" (youtu.be/cj9o8_LuFQs) ----
c='Boots_str_int'
SK5=K('시크의 Seek 영상 기반','Based on 시크의 Seek')
def textK(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
sk_ele=textK('of Armour also applies to Elemental Damage','n','s'); sk_chg=textK('chance to not remove Charges','x','s')
sk_spirit=textK('to Spirit','e','s'); sk_dur=textK('increased Skill Effect Duration','x','s')
sk_aes=textK('% increased Armour and Energy Shield','n','p'); sk_flat=textK('to Armour\n','n','p'); sk_life=textK('to maximum Life','n','p')
SK_RES=[{'gi':textK(t,'n','s'),'tmax':2} for t in ('to Fire Resistance','to Cold Resistance','to Lightning Resistance')]
SK_PRE=[{'gi':sk_aes,'tmax':2},{'gi':sk_flat,'tmax':1},{'gi':sk_life,'tmax':2}]
UHTRED=K('우트레드의 성좌',"Uhtred's Sidereus"); SERLE=K('세를의 승리',"Serle's Triumph")
SK_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
R.append({
 'id':'seek-cyclone-boots','cls':c,'base':base(c,'Faithful Leggings'),'ilvl':81,'sockets':2,'exceptional':{'sockets':1},'difficulty':2,'budget':'low',
 'buildTags':[K('돌개바람','Cyclone'),K('충전','Charges'),K('정신력','Spirit')],'patch':'0.5.5','created':'2026-11-09','author':SK5,
 'source':{'url':'https://www.youtube.com/watch?v=cj9o8_LuFQs','title':'[POE2]0.5.5 돌개바람 장화 제작 가이드','channel':'시크의 Seek'},
 'title':K('방어도 원소 적용 분열 + 충전 미소모 + 정신력','fractured armour applies to elemental + charges not removed + Spirit'),
 'start':{'rar':'rare','mods':[{'gi':sk_ele,'tmax':1,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'k1','phase':'base','do':'base','cost':'base','ts':'3:57','note':K('방어도의 원소 피해 적용 분열 + 잡옵 1개.','Fractured armour applies to elemental damage plus one junk line.')},
  {'id':'k2','phase':'suf','do':'manual','target':{'rune':UHTRED},'label':K('우트레드의 성좌 장착',"Socket Uhtred's Sidereus"),'ts':'4:31'},
  {'id':'k3','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':sk_chg,'tmax':2},'fail':{'goto':'self'},'ts':'5:03'},
  {'id':'k4','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'target':{'junk':['p','p']},'ts':'6:21'},
  {'id':'k5','phase':'suf','do':'essence','cur':'Mystic_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':sk_spirit},'ts':'6:53',
   'br':K('지속시간이 더 필요하면 회오리바람 합금','For more duration: Cyclonic Alloy')},
  {'id':'k6','phase':'suf','do':'note','label':K('가성비 마무리','Budget finish'),'ts':'7:42',
   'note':K('여기서 끝내도 됨: 좌측 찬미의 징조 + 상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접두를 채우고, 좌측 강령술의 징조 + 보존된 갈비뼈 → 심연의 메아리의 징조로 방어도·에너지 보호막 공개.','Stopping here works: Sinistral + Greater Exaltation with a Perfect Exalt fills the prefixes, then Sinistral Necromancy + Preserved Rib and an Abyssal Echoes reveal for armour and energy shield.')},
  {'id':'k7','phase':'suf','do':'manual','target':{'rune':SERLE,'slots':{'s':1}},'label':K('세를의 승리 장착',"Socket Serle's Triumph"),'ts':'8:46'},
  {'id':'k8','phase':'suf','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'9:03'},
  {'id':'k9','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[{'gi':sk_dur,'tmax':2}]+SK_RES},'side':'s','bone':'Preserved_Rib'},'fail':{'goto':'k8','via':SK_LIGHT},'ts':'9:20'},
  {'id':'k10','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'target':{'anyOf':SK_PRE},
   'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}},'ts':'10:58',
   'br':K('실패: 그대로 마무리가 추천 / 좌측 소멸의 징조 + 소멸의 오브로 지우고 다시','Miss: keep it (recommended) / Sinistral Annulment + Annulment and again')},
 ]})
