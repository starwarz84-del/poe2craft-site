# ---- Master T "How To Craft INSANE Endgame 5 Mod Jewels For ANY Build - Beginner Friendly Craft Guide - PoE 2" (youtu.be/GNNkhSENp6Q) ----
MT5=K('Master T 영상 기반','Based on Master T')
c='Time-Lost_Emerald'
def textT(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
mt_cc=textT('increased Critical Hit Chance for Attacks','n','s'); mt_cd=textT('increased Critical Damage Bonus for Attack Damage','n','s')
mt_ms=textT('1% increased Movement Speed','n','s')
mt_ail=textT('increased Magnitude of Ailments you inflict','n','p'); mt_shock=textT('increased Magnitude of Shock you inflict','n','p')
mt_plusS=textT('+1 Suffix Modifier allowed','x','p'); mt_vl=textT('Upgrades Radius to Very Large','x','p')
assert 'Spear' not in cd(c)['groups'][mt_cd]['t'][0][5] and 'Damaging' not in cd(c)['groups'][mt_ail]['t'][0][5]
MT_PRE=[{'gi':mt_ail},{'gi':mt_shock}]
R.append({
 'id':'mastert-timelost-emerald','cls':c,'base':0,'ilvl':81,'cap':{'p':2,'s':2},'difficulty':4,'budget':'high','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('오래된 주얼','Time-Lost jewel'),K('공격 치명타','Attack crit'),K('이동 속도','Movement speed')],'patch':'0.5','created':'2026-11-09','author':MT5,
 'source':{'url':'https://www.youtube.com/watch?v=GNNkhSENp6Q','title':'How To Craft INSANE Endgame 5 Mod Jewels For ANY Build - Beginner Friendly Craft Guide - PoE 2','channel':'Master T'},
 'title':K('공격 치명타 분열 + 접미 옵션 3개 + 매우 넓은 반경 5옵션','fractured attack crit, three suffixes + Very Large radius, five mods'),
 'start':{'rar':'rare','mods':[{'gi':mt_cc,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미 옵션 2개','en':'Two suffixes'},{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'des','kr':'3번째 접미 (훼손)','en':'Third suffix (desecrated)'},
           {'id':'pre','kr':'접두 · 우울','en':'Prefixes and Melancholy'}],
 'nodes':[
  {'id':'t1','phase':'suf','do':'base','cost':'base','ts':'4:38',
   'note':K('공격 치명타 확률 7%(최대치) 분열 오래된 에메랄드를 사서 소멸의 오브로 분열 + 옵션 1개만 남긴 상태.','A Time-Lost Emerald with fractured max 7% attack crit chance, annulled down to the fracture plus one line.')},
  {'id':'t2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':mt_cd},'fail':{'goto':'self'},'ts':'5:53'},
  {'id':'t3','phase':'con','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'7:46'},
  {'id':'t4','phase':'con','do':'essence','cur':'Ancient_Potent_Liquid_Contempt','knownP':True,'target':{'gi':mt_plusS,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'t2','via':{'cur':'Orb_of_Annulment'}},'ts':'8:06',
   'br':K('접두가 지워지면 다음, 치명타 피해가 지워지면 카오스 오브부터','Hit (the prefix goes) → next; miss (crit damage goes) → back to Chaos')},
  {'id':'t5','phase':'des','do':'desecrate','cur':'Preserved_Cranium','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'9:34'},
  {'id':'t6','phase':'des','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':mt_ms},'side':'s','bone':'Preserved_Cranium'},'fail':{'goto':'t5','via':LIGHT},'ts':'11:47'},
  {'id':'t7','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'removeGi':mt_plusS,'junk':'p'},'ts':'14:54'},
  {'id':'t8','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'15:21'},
  {'id':'t9','phase':'pre','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':MT_PRE,'replace':'p'},'fail':{'goto':'self'},'ts':'17:16'},
  {'id':'t10','phase':'pre','do':'essence','cur':'Ancient_Potent_Liquid_Melancholy','knownP':True,'target':{'gi':mt_vl,'chance':0.5},'fail':{'goto':'t9'},'ts':'21:04',
   'br':K('대박 → 완성, 좋은 접두가 지워지면 카오스 오브부터','Hit → done; miss (the good prefix goes) → back to Chaos')},
  {'id':'t11','phase':'pre','do':'divine','cur':'Divine_Orb','optional':True,'ts':'22:45','note':K('완성. 신성한 오브로 공격 치명타 피해 보너스 10%까지.','Done; divine attack crit damage to 10%.')},
 ]})
