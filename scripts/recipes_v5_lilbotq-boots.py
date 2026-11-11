# ---- LilBotQ "Stop Buying Boots! Craft Them Yourself - PoE2 Guide" (youtu.be/S-7YHuq3-P4) ----
LBB=K('LilBotQ 영상 기반','Based on LilBotQ')
LBB_SRC={'url':'https://www.youtube.com/watch?v=S-7YHuq3-P4','title':'Stop Buying Boots! Craft Them Yourself - PoE2 Guide','channel':'LilBotQ'}
def textLB(c, t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
LBB_LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}

# budget: magic movement speed + resistance base, greater essence, suffix desecration, two prefixes
c='Boots_int'
lb_ms=textLB(c,'35% increased Movement Speed','n','p'); lb_cold=textLB(c,'to Cold Resistance','n','s'); lb_light=textLB(c,'to Lightning Resistance','n','s')
lb_fireE=textLB(c,'to Fire Resistance','e','s')
R.append({
 'id':'lilbotq-budget-boots','cls':c,'base':base(c,'Sandsworn Sandals'),'ilvl':82,'difficulty':1,'budget':'low',
 'buildTags':[K('이동 속도','Movement speed'),K('저항','Resistances'),K('에너지 보호막','Energy Shield')],'patch':'0.5.5','created':'2026-11-09','author':LBB,
 'source':LBB_SRC,
 'title':K('이동 속도 + 저항 옵션 3개 가성비','budget movement speed + three resistances'),
 'start':{'rar':'magic','mods':[{'gi':lb_ms,'tmax':1},{'gi':lb_cold,'tmax':1}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'b1','phase':'suf','do':'base','cost':'base','ts':'0:12','note':K('이동 속도 + 저항이 붙은 매직 장화(낮은 티어도 됨).','A magic pair with movement speed and a resistance (lower tiers are fine).')},
  {'id':'b2','phase':'suf','do':'essence','cur':'Greater_Essence_of_Insulation','target':{'gi':lb_fireE},'ts':'1:50',
   'br':K('없는 원소의 상위 에센스, 또는 상위 풍요의 에센스로 희귀도','The greater essence of the missing element (or Greater Essence of Opulence for rarity)')},
  {'id':'b3','phase':'suf','do':'desecrate','cur':'Preserved_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'2:16'},
  {'id':'b4','phase':'pre','do':'exalt','cur':'Greater_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','p']},'ts':'2:35',
   'note':K('접두 아무거나(영상: 에너지 보호막 % + 최대 생명력).','Any prefixes (% energy shield and maximum life in the video).')},
  {'id':'b5','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':lb_light,'tmax':2},'side':'s','bone':'Preserved_Rib'},'fail':{'goto':'b3','via':LBB_LIGHT},'ts':'3:14',
   'br':K('대박 → 완성, 실패: 빛의 징조 + 소멸의 오브로 다시 훼손 (접두가 별로면 처음부터)','hit → done; miss: Omen of Light + Annulment and desecrate again (poor prefixes: start over)')},
  {'id':'b6','phase':'fin','do':'note','label':K('방어구 장인의 고철 · 숙련공의 오브',"Armourer's Scrap and Artificer's Orb"),'ts':'3:39',
   'note':K('퀄리티 20%, 소켓 추가.','20% quality and a socket.')},
 ]})

# high end: exceptional base, Uhtred's Sidereus, fractured movement speed / slow hybrid
c='Boots_str'
lh_ms=textLB(c,'increased Movement Speed\n(21','x','p'); lh_dodge=textLB(c,'metres to Dodge Roll distance','x','p')
lh_light=textLB(c,'to Lightning Resistance','n','s'); lh_rarE=textLB(c,'increased Rarity of Items found','e','s'); lh_spirit=textLB(c,'to Spirit','e','s')
lh_flat=textLB(c,'to Armour','n','p'); lh_pct=textLB(c,'increased Armour','n','p'); lh_life=textLB(c,'to maximum Life','n','p')
LH_PRE=[{'gi':lh_flat,'tmax':1},{'gi':lh_pct,'tmax':2},{'gi':lh_life,'tmax':2}]
LH_UHTRED=K('우트레드의 성좌',"Uhtred's Sidereus"); LH_ASTRID=K('아스트리드의 창의성',"Astrid's Creativity")
R.append({
 'id':'lilbotq-boots','cls':c,'base':base(c,'Tasalian Greaves'),'ilvl':82,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'high',
 'buildTags':[K('이동 속도','Movement speed'),K('회피 구르기','Dodge roll'),K('정신력','Spirit')],'patch':'0.5.5','created':'2026-11-09','author':LBB,
 'source':LBB_SRC,
 'title':K('이동 속도·둔화 감소 분열 + 회피 구르기 거리 + 정신력','fractured movement speed/slow + dodge roll distance + Spirit'),
 'start':{'rar':'rare','quality':26,'runes':[LH_UHTRED],
          'mods':[{'gi':lh_ms,'tmax':1,'fr':True},{'gi':lh_light,'tmax':1},{'gi':lh_rarE,'crafted':True},{'unrev':'p'}]},
 'phases':[{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'h1','phase':'suf','do':'base','cost':'base','ts':'9:42',
   'note':K('퀄리티 26%. 우트레드의 성좌 장착 상태로 이동 속도·둔화 감소 분열 + 번개 저항 + 희귀도(상위 풍요의 에센스) + 미공개 훼손 접두.',"26% quality. Uhtred's Sidereus socketed: fractured movement speed/slow, lightning resistance, rarity (Greater Essence of Opulence) and an unrevealed desecrated prefix.")},
  {'id':'h2','phase':'suf','do':'manual','target':{'rune':LH_ASTRID},'label':K('아스트리드의 창의성 장착',"Socket Astrid's Creativity"),'ts':'10:52'},
  {'id':'h3','phase':'suf','do':'essence','cur':'Mystic_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':lh_spirit},'ts':'11:09'},
  {'id':'h4','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'anyOf':LH_PRE},'fail':{'goto':'h4b'},'ts':'11:39',
   'br':K('실패: 영상 추천대로 그대로 진행 / 좌측 말소의 징조 + 카오스 오브','Miss: keep it (the video\'s pick) / Sinistral Erasure + Chaos')},
  {'id':'h4b','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':LH_PRE,'replace':'p'},'fallbackFor':'h4','fail':{'goto':'self'},'ts':'11:58'},
  {'id':'h5','phase':'pre','do':'desecrate','cur':'Ancient_Rib','target':{'unrev':'p'},'ts':'12:16'},
  {'id':'h6','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'gi':lh_dodge,'tmax':2},'side':'p','bone':'Ancient_Rib'},'fail':{'goto':'h5','via':LBB_LIGHT},'ts':'12:20',
   'br':K('대박 → 완성, 실패: 빛의 징조 + 소멸의 오브로 다시 훼손','hit → done; miss: Omen of Light + Annulment and desecrate again')},
  {'id':'h7','phase':'fin','do':'note','optional':True,'label':K('아스트리드의 창의성 교체 (선택)',"Swap Astrid's Creativity (optional)"),'ts':'12:50',
   'note':K('제작 옵션은 남음. 원하는 룬으로 교체.','Crafted lines stay; swap in any rune.')},
 ]})
