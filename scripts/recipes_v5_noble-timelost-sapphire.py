# ---- 노블이-NoblE "[POE2] 제작의 신이 말아주는 가장 비싼 오래된 사파이어 주얼 5줄 제작 방법" (youtu.be/zEV8kWwveYQ) ----
NB5=K('노블이-NoblE 영상 기반','Based on 노블이-NoblE')
c='Time-Lost_Sapphire'
def textN(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
nb_scc=textN('increased Critical Hit Chance for Spells','n','s'); nb_scd=textN('increased Critical Spell Damage Bonus','n','s')
nb_cd=textN('(5—10)% increased Critical Damage Bonus','n','s')
nb_plusS=textN('+1 Suffix Modifier allowed','x','p'); nb_mel=textN('Upgrades Radius to Very Large','x','p')
nb_mana=textN('1% increased maximum Mana','d','p')
assert 'Spell' not in cd(c)['groups'][nb_cd]['t'][0][5]
R.append({
 'id':'noble-timelost-sapphire','cls':c,'base':0,'ilvl':79,'cap':{'p':2,'s':2},'difficulty':4,'budget':'high','unknownW':True,
 'buildTags':[K('주얼','Jewel'),K('오래된 주얼','Time-Lost jewel'),K('주문 치명타','Spell crit'),K('마나','Mana')],'patch':'0.5.5','created':'2026-11-09','author':NB5,
 'source':{'url':'https://www.youtube.com/watch?v=zEV8kWwveYQ','title':'[POE2] 제작의 신이 말아주는 가장 비싼 오래된 사파이어 주얼 5줄 제작 방법','channel':'노블이-NoblE'},
 'title':K('주문 치명타 3접미 + 매우 넓은 반경 · 최대 마나 5옵션','three crit suffixes + Very Large radius and max mana, five mods'),
 'start':{'rar':'rare','mods':[{'gi':nb_scc,'fr':True},{'junk':'p'}]},
 'phases':[{'id':'suf','kr':'접미 옵션 2개','en':'Two suffixes'},{'id':'con','kr':'경멸: 접미 +1','en':'Contempt: +1 suffix'},{'id':'pre','kr':'접두: 반경 · 훼손','en':'Prefixes: radius and desecration'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'n1','phase':'suf','do':'base','cost':'base','ts':'0:47',
   'note':K('주문 치명타 명중 확률 7%(최대) 분열 + 잡옵 1개.','Fractured 7% spell crit chance (max) plus one junk line.')},
  {'id':'n2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':nb_scd},'fail':{'goto':'self'},'ts':'2:37'},
  {'id':'n3','phase':'con','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'3:30'},
  {'id':'n4','phase':'con','do':'essence','cur':'Ancient_Potent_Liquid_Contempt','knownP':True,'target':{'gi':nb_plusS,'chance':0.5,'slots':{'s':1}},'fail':{'goto':'n2','via':{'cur':'Orb_of_Annulment'}},'ts':'3:41',
   'br':K('접미 +1 → 다음, 실패: 소멸의 오브로 분열 + 옵션 1개 → 카오스 오브부터','+1 suffix → next; miss: annul to fracture + one line, chaos again')},
  {'id':'n5','phase':'con','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'target':{'gi':nb_cd},'fail':{'goto':'self','via':{'cur':'Orb_of_Annulment'},'lost':'n2'},'ts':'4:13',
   'br':K('실패: 소멸의 오브. 경멸·주문 치명타 피해가 지워지면 카오스 오브부터','Miss: Annulment; if Contempt or spell crit damage goes, chaos again')},
  {'id':'n6','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'junk':'p','removeGi':nb_plusS},'ts':'8:15'},
  {'id':'n7','phase':'pre','do':'exalt','cur':'Exalted_Orb','target':{'junk':'p'},'ts':'8:56'},
  {'id':'n8','phase':'pre','do':'chaos','cur':'Chaos_Orb','optional':True,'target':{'reroll':True},'ts':'9:16',
   'note':K('반경 옵션(중형·대형)이 있을 때만.','Only while a radius line (Medium/Large) is there.')},
  {'id':'n9','phase':'pre','do':'essence','cur':'Ancient_Potent_Liquid_Melancholy','knownP':True,'target':{'gi':nb_mel},'ts':'9:20'},
  {'id':'n10','phase':'pre','do':'desecrate','cur':'Preserved_Cranium','target':{'unrev':'p','chance':1},'ts':'9:24',
   'br':K('우울 옵션이 지워져도 공개 먼저 → 최대 마나가 뜨면 액체 우울 다시, 1/2','If the Melancholy line goes, reveal first; on max mana, Melancholy again (1 in 2)')},
  {'id':'n11','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':nb_mana},'side':'p','bone':'Preserved_Cranium'},'fail':{'goto':'n8','via':{'cur':'Chaos_Orb'}},'ts':'9:57',
   'br':K('실패: 카오스 오브로 훼손 옵션 교체 → 반경 정리부터','Miss: Chaos Orb off the desecrated line, then from the radius step')},
  {'id':'n12','phase':'pre','do':'note','optional':True,'label':K('우울 옵션이 지워졌을 때: 액체 우울 다시','If Melancholy went: Melancholy again'),'ts':'11:53',
   'br':K('최대 마나 유지 → 완성, 실패 → 카오스 오브로 지우고 반경 정리부터','Max mana kept → done; miss → Chaos it off, from the radius step')},
  {'id':'n13','phase':'fin','do':'quality','cur':'Refined_Sibilant_Catalyst','target':{'quality':20},'ts':'12:11'},
 ]})
