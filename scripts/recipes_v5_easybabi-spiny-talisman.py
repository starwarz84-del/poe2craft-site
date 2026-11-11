# ---- EasyBabi "[PoE 2] 새로운 제작법으로 엔드게임 무도무기를 제작해보자 | 아스트리드의 창의성" (youtu.be/fabBIuR6yhw, 0.5) ----
# 플로우차트(scripts/graphs/gen_batch23.py)를 따라 작성(정책 31). 같은 단계 id.
EZB=K('EasyBabi 영상 기반','Based on EasyBabi')
c='Talismans'
eb_crit,eb_as,eb_bat,eb_acc,eb_eatk,eb_cold,eb_light,eb_fire=18,47,56,17,23,5,7,4
EB_PRE=[{'gi':eb_eatk,'tmax':2},{'gi':eb_cold,'tmax':2},{'gi':eb_light,'tmax':2},{'gi':eb_fire,'tmax':2}]
R.append({
 'id':'easybabi-spiny-talisman','cls':c,'base':base(c,'Spiny Talisman'),'ilvl':82,'difficulty':4,'budget':'high',
 'buildTags':[K('원소','Elemental'),K('치명타','Critical'),K('무도 무기','Martial weapon')],'patch':'0.5.5','adaptedFrom':'0.5','created':'2026-11-11','author':EZB,
 'source':{'url':'https://www.youtube.com/watch?v=fabBIuR6yhw','title':'[PoE 2] 새로운 제작법으로 엔드게임 무도무기를 제작해보자 | 아스트리드의 창의성','channel':'EasyBabi'},
 'title':K('치명타 확률 + 공격 속도 + 공격 스킬 +3 + 원소 피해 접두 3개','crit chance + attack speed + attack skills +3 + three elemental prefixes'),
 'start':{'rar':'magic','mods':[{'gi':eb_crit,'tmax':1},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'훼손 공개','en':'Reveal'}],
 'nodes':[
  {'id':'t0','phase':'suf','do':'base','cost':'base','ts':'0:59','note':K('치명타 확률 1티어 매직 가시투성이 부적(아이템 레벨 82).','A magic Spiny Talisman with T1 crit chance (item level 82).')},
  {'id':'t1','phase':'suf','do':'manual','target':{'rune':K('아스트리드의 창의성',"Astrid's Creativity")},'label':K('아스트리드의 창의성 장착',"Socket Astrid's Creativity"),'ts':'1:46'},
  {'id':'t2','phase':'suf','do':'essence','cur':'Greater_Essence_of_Haste','target':{'gi':eb_as},'ts':'2:06'},
  {'id':'t3','phase':'suf','do':'essence','cur':'Perfect_Essence_of_Battle','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':eb_bat},'ts':'2:14'},
  {'id':'t4','phase':'pre','do':'desecrate','cur':'Ancient_Jawbone','target':{'unrev':'p'},'ts':'2:59'},
  {'id':'t5','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':eb_acc},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'t4','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}},'ts':'3:20'},
  {'id':'t6','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'anyOf':EB_PRE},'fail':{'goto':'t6b'},'ts':'3:40'},
  {'id':'t6b','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':EB_PRE,'replace':'p'},'fallbackFor':'t6','fail':{'goto':'self'},'ts':'4:09'},
  {'id':'t7','phase':'fin','do':'remove','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'target':{'removeDes':True},'ts':'3:49'},
  {'id':'t8','phase':'fin','do':'desecrate','cur':'Ancient_Jawbone','target':{'unrev':'p'},'ts':'3:52'},
  {'id':'t9','phase':'fin','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':EB_PRE},'side':'p','bone':'Ancient_Jawbone'},'fail':{'goto':'t8','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}},'ts':'3:56'},
 ]})
