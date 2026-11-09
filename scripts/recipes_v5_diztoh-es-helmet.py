# ---- Diztoh "How to Craft an Endgame Energy Shield Helmet | Temple of Corruption | PoE 2" (youtu.be/yegMdBTuEtY) ----
DZ5=K('Diztoh 영상 기반','Based on Diztoh')
c='Helmets_int'
def textE(t, sec, side=None, f=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5] and '\n' not in gr['t'][0][5] and (f is None or f in gr.get('f',[]))]
    if not hits: raise Exception(t)
    return hits[0]
de_esf=textE('to maximum Energy Shield','n','p'); de_esp=textE('% increased Energy Shield','n','p'); de_rarP=textE('increased Rarity of Items found','n','p')
de_rarS=textE('increased Rarity of Items found','n','s'); de_int=textE('Strength, Dexterity or Intelligence','e','s','Intelligence')
DE_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
DE_PRE=[{'gi':de_esp,'tmax':3},{'gi':de_rarP,'tmax':1}]
R.append({
 'id':'diztoh-es-helmet','cls':c,'base':base(c,'Kamasan Tiara'),'ilvl':81,'sockets':2,'exceptional':{'sockets':1},'difficulty':2,'budget':'low',
 'buildTags':[K('에너지 보호막','Energy Shield'),K('아이템 희귀도','Item rarity')],'patch':'0.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=yegMdBTuEtY','title':'How to Craft an Endgame Energy Shield Helmet | Temple of Corruption | PoE 2','channel':'Diztoh'},
 'title':K('에너지 보호막 분열 + 희귀도 2줄 + 에너지 보호막 %','fractured flat energy shield + two rarity lines + % energy shield'),
 'start':{'rar':'rare','quality':20,'mods':[{'gi':de_esf,'tmax':1,'fr':True},{'unrev':'p'},{'gi':de_rarS,'tmax':1},{'gi':de_int,'crafted':True}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'fill','kr':'채우기','en':'Fill'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'e1','phase':'base','do':'base','cost':'base','ts':'0:51','note':K('에너지 보호막 최대치 1티어 분열 + 희귀도(접미) + 지능(상위 무한의 에센스) + 미공개 훼손 접두.','Fractured T1 flat energy shield, suffix rarity, intelligence (Greater Essence of the Infinite) and an unrevealed desecrated prefix.')},
  {'id':'e2','phase':'fill','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'junk':'s'},'ts':'2:35'},
  {'id':'e3','phase':'fill','do':'exalt','cur':'Greater_Exalted_Orb','target':{'anyOf':DE_PRE},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Sinistral_Annulment']}},'ts':'2:50'},
  {'id':'e4','phase':'fill','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':DE_PRE},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'self','via':{'cur':'Ancient_Rib','also':[DE_LIGHT]}},'ts':'3:22'},
  {'id':'e5','phase':'fin','do':'manual','target':{'rune':K('곰 우상','Bear Idol')},'label':K('곰 우상 장착','Socket a Bear Idol'),'ts':'4:26'},
  {'id':'e6','phase':'fin','do':'manual','optional':True,'target':{'rune':K('완벽한 사막 룬','Perfect Desert Rune')},'label':K('완벽한 사막 룬 장착 (선택)','Socket a Perfect Desert Rune (optional)'),'ts':'5:00'},
  {'id':'e7','phase':'fin','do':'note','optional':True,'cost':'vaal','label':K('타락으로 소켓 추가 (선택)','Corrupt for an extra socket (optional)'),'ts':'6:25',
   'note':K('타락으로 소켓을 하나 더 노림. 아이템이 망가질 수 있음.','Corrupt for one more socket; the item can be ruined.')},
 ]})
