# ---- Diztoh "I Crafted Gold Rings to Increase my Item Rarity | Path of Exile 2 0.5.5" (youtu.be/GDLDxn6yxEs) ----
c='Rings'
DZ5=K('Diztoh 영상 기반','Based on Diztoh')
def txR(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
gr_rarP=txR('increased Rarity of Items found','n','p'); gr_cres=txR('to Cold Resistance','n','s'); gr_rarE=txR('increased Rarity of Items found','e','s')
gr_allres=txR('to all Elemental Resistances','n','s')
gr_catk=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='n' and gr['g']=='p' and 'Cold damage to Attacks' in gr['t'][0][5] and len(gr['t'])>1][0]
gr_ppct=txR('increased Cold Damage','n','p')
gr_patk=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='n' and gr['g']=='p' and 'Physical Damage to Attacks' in gr['t'][0][5] and len(gr['t'])>1][0]
R.append({
 'id':'diztoh-rarity-ring','cls':c,'base':base(c,'Gold Ring'),'ilvl':81,'difficulty':1,'budget':'low',
 'buildTags':[K('아이템 희귀도','Item rarity'),K('냉기','Cold'),K('가성비','Budget')],'patch':'0.5.5','created':'2026-11-09','author':DZ5,
 'source':{'url':'https://www.youtube.com/watch?v=GDLDxn6yxEs','title':'I Crafted Gold Rings to Increase my Item Rarity | Path of Exile 2 0.5.5','channel':'Diztoh'},
 'title':K('희귀도 2줄 + 냉기 저항 + 모든 원소 저항','double rarity + cold res + all resistances'),
 'start':{'rar':'magic','mods':[{'gi':gr_rarP,'tmax':3},{'gi':gr_cres,'tmax':2}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미 훼손','en':'Suffix desecration'},{'id':'pre','kr':'접두 촉진 엑잘','en':'Catalysed prefixes'}],
 'nodes':[
  {'id':'g1','phase':'base','do':'base','cost':'base','ts':'1:00',
   'note':K('접두 희귀도 + 접미 냉기 저항(영상 40%)이 붙은 매직 황금 반지(1디바인 안팎). 희귀도는 꼭 접두여야 함: 에센스의 희귀도가 접미라 접미 희귀도 반지엔 안 붙음.','A magic Gold Ring with prefix rarity and suffix cold resistance (40% in the video), about 1 divine. The rarity must be the prefix: the essence\'s rarity is a suffix and will not go on a ring that already has suffix rarity.')},
  {'id':'g2','phase':'base','do':'essence','cur':'Greater_Essence_of_Opulence','target':{'gi':gr_rarE},'ts':'1:20',
   'note':K('상위 풍요의 에센스로 희귀가 되며 접미 희귀도 확정(영상 15%). 이 줄은 제작 옵션.','Greater Essence of Opulence makes it rare with guaranteed suffix rarity (15% in the video). This line counts as crafted.')},
  {'id':'g3','phase':'suf','do':'desecrate','cur':'Preserved_Collarbone','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'2:20',
   'note':K('우측 강령술의 징조 + 보존된 빗장뼈로 마지막 접미를 훼손.','Dextral Necromancy + Preserved Collarbone desecrates the last suffix.')},
  {'id':'g4','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':gr_allres},'side':'s','bone':'Preserved_Collarbone'},'fail':{'goto':'g3','via':LIGHT},'ts':'3:20',
   'note':K('심연의 메아리의 징조로 공개해 모든 원소 저항(번개 저항도 OK). 영상은 첫 화면에 4티어가 떠서 그대로 확정.','Reveal with Abyssal Echoes for all elemental resistances (lightning resistance also works). The video took a tier 4 from the first page.')},
  {'id':'g5','phase':'pre','do':'quality','cur':'Tuls_Catalyst','target':{'quality':20},'ts':'4:20',
   'note':K('툴의 기폭제로 냉기 퀄리티 20%.','Tul\'s Catalysts to 20% cold quality.')},
  {'id':'g6','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Greater_Exaltation'],'target':{'anyOf':[{'gi':gr_catk},{'gi':gr_ppct},{'gi':gr_patk}]},'ts':'4:40',
   'note':K('촉진하는 찬미의 징조 + 상위 찬미의 징조 + 상위 엑잘티드 오브로 빈 접두 두 줄. 냉기 퀄리티가 공격 시 냉기 피해·냉기 피해 % 확률을 올림(물리 추가도 OK). 영상은 공격 시 냉기 피해 + 회피. 결과는 그대로 받아들임.','Catalysing + Greater Exaltation + Greater Exalted Orb fills both empty prefixes; cold quality favours flat cold attack damage or % cold damage (flat physical also fine). The video got flat cold + evasion and kept it.')},
  {'id':'g7','phase':'pre','do':'note','ts':'5:40',
   'note':K('완성. 영상 완성품: 황금 반지(고정 희귀도 14%) / 공격 시 냉기 피해 10~17 · 회피 +122 · 희귀도 11% / 냉기 저항 40% · 모든 원소 저항 8% · 희귀도 16%. 희귀도 68 → 93. 더 싸게 하려면 모든 원소 저항 베이스로 좌측 강령술의 징조 훼손, 번개 저항이 붙으면 유동체로 냉기 저항으로 바꿈(영상 후반).','Done. The video\'s ring: Gold Ring (14% rarity implicit) / 10–17 cold attack damage, +122 evasion, 11% rarity / 40% cold res, 8% all resistances, 16% rarity. Rarity went from 68 to 93. Cheaper: start from an all-resistances base, desecrate a prefix with Sinistral Necromancy, and turn a lightning resistance into cold with a flux (end of the video).')},
 ],
})
