# ---- Diztoh "How to Craft a +5 Talisman for Early Endgame | PoE 2 0.5" (youtu.be/p6HIFmJ9mRU) ----
DZT=K('Diztoh 영상 기반','Based on Diztoh')
c='Talismans'
def textT(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
tl_melee=textT('+5 to Level of all Melee Skills','n','s'); tl_fire=textT('Fire Damage','n','p'); tl_crit=textT('to Critical Hit Chance','e','s')
tl_as=textT('Companions have','d','s'); tl_cdmg=textT('to Critical Damage Bonus','n','s')
tl_phys=textT('Physical Damage','n','p'); tl_cold=textT('Cold Damage','n','p'); tl_light=textT('(310—358) Lightning Damage','n','p')
tl_ppct=textT('(170—179)% increased Physical Damage','n','p'); tl_hyb=textT('increased Physical Damage\n+','n','p'); tl_eatk=textT('increased Elemental Damage with Attacks','n','p')
TL_PRE=[{'gi':tl_phys,'tmax':3},{'gi':tl_cold,'tmax':3},{'gi':tl_light,'tmax':3},{'gi':tl_ppct,'tmax':4},{'gi':tl_hyb,'tmax':3},{'gi':tl_eatk,'tmax':2}]
TL_IRON=K('완벽한 철 룬','Perfect Iron Rune'); TL_SERLE=K('세를의 승리',"Serle's Triumph")
R.append({
 'id':'diztoh-talisman','cls':c,'base':base(c,'Maji Talisman'),'ilvl':81,'difficulty':2,'budget':'low',
 'buildTags':[K('근접','Melee'),K('공격 속도','Attack speed'),K('치명타','Critical hit')],'patch':'0.5','created':'2026-11-09','author':DZT,
 'source':{'url':'https://www.youtube.com/watch?v=p6HIFmJ9mRU','title':'How to Craft a +5 Talisman for Early Endgame | PoE 2 0.5','channel':'Diztoh'},
 'title':K('근접 스킬 +5 + 아마나무 공격 속도','+5 melee skills + Amanamu attack speed'),
 'start':{'rar':'magic','mods':[{'gi':tl_melee,'tmax':1},{'gi':tl_fire,'tmax':3}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'7번째 옵션 · 마무리','en':'Seventh line and finish'}],
 'nodes':[
  {'id':'t1','phase':'suf','do':'base','cost':'base','ts':'0:31','note':K('모든 근접 스킬 +5 + 화염 피해 추가가 붙은 매직 부적 구매.','Buy a magic talisman with +5 melee skills and flat fire damage.')},
  {'id':'t2','phase':'suf','do':'essence','cur':'Greater_Essence_of_Seeking','target':{'gi':tl_crit},'ts':'0:50'},
  {'id':'t3','phase':'suf','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_Dextral_Necromancy','Omen_of_the_Liege'],'target':{'unrev':'s'},'ts':'1:05'},
  {'id':'t4','phase':'suf','do':'reveal','target':{'reveal':{'gi':tl_as},'side':'s','lord':'amanamu','bone':'Preserved_Jawbone'},'fail':{'goto':'t3','via':LIGHT},'ts':'1:25'},
  {'id':'t5','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':TL_PRE},'ts':'2:14',
   'br':K('만족 → 다음 단계, 아니면 갈림길(접두 다시)','Happy → next step; otherwise the fork (redo prefixes)')},
  {'id':'t5b','phase':'pre','do':'note','fallbackFor':'t5','label':K('갈림길: 접두 다시','Fork: redo prefixes'),'ts':'3:25',
   'note':K('좌측 소멸의 징조 + 소멸의 오브로 접두를 비움 → 완벽한 엑잘티드 오브 옵션 1개(별로면 좌측 말소의 징조 + 카오스 오브) → 상위 찬미의 징조 + 완벽한 엑잘티드 오브로 옵션 2개.','Clear the prefixes with Sinistral Annulment + Annulment → Perfect Exalt one line (reroll a bad one with Sinistral Erasure + Chaos) → Greater Exaltation + Perfect Exalt for two.')},
  {'id':'t6','phase':'fin','do':'quality','cur':'Blacksmiths_Whetstone','target':{'quality':20},'ts':'2:50'},
  {'id':'t7','phase':'fin','do':'manual','target':{'rune':TL_IRON},'label':K('완벽한 철 룬 장착','Socket a Perfect Iron Rune'),'ts':'4:28'},
  {'id':'t8','phase':'fin','do':'manual','target':{'rune':TL_SERLE,'slots':{'s':1}},'label':K('세를의 승리 장착',"Socket Serle's Triumph"),'ts':'4:36'},
  {'id':'t9','phase':'fin','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'gi':tl_cdmg,'tmax':2},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'t3'},'ts':'5:00',
   'br':K('영상은 정확도 + 빛 반경으로 타협','The video settled for accuracy + light radius')},
  {'id':'t10','phase':'fin','do':'divine','cur':'Divine_Orb','target':{'roll':{'gi':tl_as}},'fail':{'goto':'self'},'ts':'3:05'},
  {'id':'t11','phase':'fin','do':'note','ts':'5:20','note':K('선택: 타락(소켓 3개 노림). 건축가의 오브 2차 타락은 아이템이 바뀌거나 사라질 수 있음.','Optional: corrupt for a third socket. A second corruption with an Architect\'s Orb can transform or destroy the item.')},
 ]})
