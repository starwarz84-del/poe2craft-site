# Recipes from the user's own crafting notes. Exec'd from build_recipes.py.
ME=K('사용자 제작 방식','From the site owner\'s method')
c='Rings'
bp_phys=textR('Physical Damage to Attacks','n','p'); bp_fire=textR('Fire damage to Attacks','n','p'); bp_cold=textR('Cold damage to Attacks','n','p'); bp_light=textR('Lightning damage to Attacks','n','p')
bp_allres=textR('to all Elemental Resistances','n','s'); bp_fres=textR('to Fire Resistance','n','s')
bp_maxQ=textR('to Maximum Quality','e','p'); bp_as=textR('increased Attack Speed','e','s')
FLATS=[{'gi':bp_fire,'tmax':4},{'gi':bp_cold,'tmax':4},{'gi':bp_light,'tmax':4}]
OKA={'of':'b9','when':'ok'}; MSA={'of':'b9','when':'miss'}
R.append({
 'id':'breach-ring-phys','cls':c,'base':base(c,'Breach Ring'),'ilvl':82,'difficulty':3,'budget':'medium',
 'buildTags':[K('공격','Attack'),K('원소','Elemental'),K('물리','Physical')],'patch':'0.5.5','created':'2026-11-09','author':ME,
 'title':K('물리 플랫 분열 + 원소 플랫 (공격 퀄리티 60%)','fractured physical flat + elemental flats (60% attack quality)'),
 'start':{'rar':'rare','mods':[{'gi':bp_phys,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'}],
 'nodes':[
  {'id':'b1','phase':'base','do':'base','cost':'base','note':K('공격 시 물리 피해 1티어 분열 + 잡옵 1개 균열 반지(아이템 레벨 82).','A Breach Ring with fractured T1 physical attack damage plus one junk line (item level 82).')},
  {'id':'b2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':bp_allres,'tmax':1},'fail':{'goto':'self'},
   'note':K('카오스 오브로 모든 원소 저항 1티어. 가중치가 낮아 뒤에서 엑잘로 뽑기 어려우니 여기서 먼저 확보.','Chaos for T1 all elemental resistances: low weight, hard to slam later, so it comes first.')},
  {'id':'b3','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'note':K('접두에 버릴 옵션 하나.','One throwaway prefix.')},
  {'id':'b4','phase':'suf','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':bp_maxQ},'note':K('좌측 결정화의 징조 + 균열의 에센스로 그 접두를 최대 퀄리티 +20%로 바꿈.','Sinistral Crystallisation + Essence of the Breach turns it into +20% maximum quality.')},
  {'id':'b5','phase':'suf','do':'quality','cur':'Xophs_Catalyst','target':{'quality':60},'note':K('조프의 기폭제로 화염 퀄리티 60%(기본 20% + 균열 반지 고정 20% + 최대 퀄리티 20%).','Xoph\'s Catalysts to 60% fire quality (20% base + 20% implicit + 20% from the Breach line).')},
  {'id':'b6','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'gi':bp_fres,'tmax':2},
   'fail':{'goto':'b5','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'b2'},
   'note':K('촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 화염 저항. 원소 무관 3종을 그냥 노리는 것보다 잘 뜸. 퀄리티는 0%가 됨. 쓸 수 없는 옵션이면 우측 소멸의 징조 + 소멸의 오브로 1/2 도박(모든 원소 저항이 지워지면 처음부터) 후 기폭제부터 다시.','Catalysing + Dextral Exaltation + Perfect Exalt for fire resistance, likelier than any of three plain; quality drops to 0. On a useless line, Dextral Annulment is a 1/2 gamble (losing all-res means starting over), then refill and retry.')},
  {'id':'b6b','phase':'suf','do':'note','fallbackFor':'b6','label':K('갈림길 ②: 타협','Fork (2): settle'),'note':K('쓸 만한 접미면 그대로 두고 접두로 넘어감.','Keep a usable suffix and move on to the prefixes.')},
  {'id':'b7','phase':'pre','do':'quality','cur':'Reaver_Catalyst','target':{'quality':60},'note':K('접미가 끝났으니 강탈자 기폭제로 공격 퀄리티 60%. 완성품의 퀄리티 종류.','Suffixes done: Reaver Catalysts to 60% attack quality, the finished quality type.')},
  {'id':'b8','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 옵션 하나. 공격 시 원소 피해가 붙으면 베스트, 아니면 잡옵.','Sinistral Exaltation + Perfect Exalt one prefix: an elemental attack flat is best, otherwise junk.')},
  {'id':'b8b','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'removeGi':bp_maxQ,'junk':'p'},
   'note':K('절사의 징조 + 카오스 오브로 최대 퀄리티(레벨이 가장 낮음)를 다른 옵션으로 바꿈. 에센스·합금은 옵션을 붙인 뒤 지우는 방식이라 제작 옵션인 최대 퀄리티가 남아 있으면 합금을 못 씀. 퀄리티는 그대로 남고, 여기서도 공격 시 원소 피해가 뜨면 이득.','Whittling + Chaos swaps maximum quality (the lowest level) for another line: an alloy adds before it removes, so it cannot go on while that crafted line is there. The quality stays, and an elemental attack flat here is a bonus.')},
  {'id':'b9','phase':'pre','do':'essence','cur':'Swift_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':bp_as,'chance':0.5},'fail':{'goto':'m1'},
   'note':K('좌측 결정화의 징조 + 재빠른 합금: 접두 옵션 두 개(8번·9번에서 붙은 옵션) 중 하나가 지워지고 공격 속도는 접미에. 남은 접두가 공격 시 원소 피해면 아래 "성공", 잡옵이면 "실패" 경로. 이 뒤로는 제작 옵션이 있어서 심연의 에센스를 쓸 수 없음.','Sinistral Crystallisation + Swift Alloy: one of the two new prefixes goes and attack speed lands on a suffix. If the prefix left is an elemental attack flat, follow "success" below; if it is junk, "miss". From here Essence of the Abyss (crafted) cannot be used.')},
  {'id':'o1','phase':'pre','branch':OKA,'do':'desecrate','cur':'Ancient_Collarbone','target':{'unrev':'p'},
   'note':K('남은 접두가 공격 시 원소 피해면 빈자리에 고대 빗장뼈로 훼손.','The prefix left is an elemental attack flat: desecrate the free slot with an Ancient Collarbone.')},
  {'id':'o2','phase':'pre','branch':OKA,'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':FLATS},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'o1','via':LIGHT},
   'note':K('심연의 메아리의 징조로 공개해 공격 시 원소 피해. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시.','Reveal with Abyssal Echoes for an elemental attack flat; otherwise Light + Annulment and retry.')},
  {'id':'m1','phase':'pre','branch':MSA,'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'p'},
   'note':K('남은 접두가 잡옵이면 완벽한 엑잘티드 오브로 빈자리를 채움(접미는 꽉 차서 징조 불필요). 공격 시 원소 피해면 이득.','The prefix left is junk: fill the free slot with a Perfect Exalt (suffixes are full, no omen); an elemental attack flat is a bonus.')},
  {'id':'m2','phase':'pre','branch':MSA,'do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':FLATS,'replace':'p'},
   'note':K('절사의 징조 + 완벽한 카오스 오브로 잡옵(레벨이 가장 낮을 때)을 돌려 공격 시 원소 피해 찾기(티어는 타협). 잡옵 레벨이 더 높으면 다음 단계처럼 좌측 말소의 징조.','Whittling + Perfect Chaos rerolls the junk prefix (when it is the lowest level) into an elemental attack flat (settle on the tier); if the junk is higher level, use Sinistral Erasure as below.')},
  {'id':'m3','phase':'pre','branch':MSA,'do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':FLATS,'replace':'p'},'fallbackFor':'m2','fail':{'goto':'self'},
   'label':K('안 뜨면: 접두 계속 돌리기','On a miss: keep rolling'),
   'note':K('안 뜬 옵션이 낮은 레벨이면 다시 절사의 징조, 레벨이 높아 절사의 징조로는 좋은 옵션이 바뀔 수 있으면 좌측 말소의 징조(보통 더 비쌈) + 완벽한 카오스 오브로 계속 돌림.','If the miss is low level, Whittling again; if it is high level (Whittling could hit a good line), Sinistral Erasure (usually pricier) + Perfect Chaos.')},
  {'id':'m4','phase':'pre','branch':MSA,'do':'desecrate','cur':'Ancient_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p','chance':0.5},'fail':{'goto':'m2'},
   'note':K('접두가 꽉 찬 채로 좌측 강령술의 징조 + 고대 빗장뼈: 분열 옵션 빼고 옵션 두 개 중 하나가 지워지고 그 자리에 훼손(1/2로 잡옵이 지워짐). 찾은 원소 피해가 1티어면 이 도박 대신 좌측 말소의 징조 + 절사의 징조 + 완벽한 카오스 오브로 마지막 옵션을 찾음.','Full prefixes, Sinistral Necromancy + Ancient Collarbone: one of the two non-fractured prefixes goes and the desecration takes its place (1/2 it takes the junk). If the flat you found is tier 1, use Sinistral Erasure + Whittling + Perfect Chaos for the last line instead.')},
  {'id':'m5','phase':'pre','branch':MSA,'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':FLATS},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'m4','via':LIGHT},
   'note':K('심연의 메아리의 징조로 공개해 공격 시 원소 피해. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 빈자리에 다시 훼손.','Reveal with Abyssal Echoes for an elemental attack flat; otherwise Light + Annulment and desecrate the free slot again.')},
 ],
})

# ---- 라그나게임채널 "라장간 #1 아샷활 초간단 제작 가이드" (youtu.be/m0eHw6nq24Q) ----
c='Bows'
def textB(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
bw_pct=textB('% increased Physical Damage','n','p'); bw_flatE=textB('Physical Damage','e','p')
bw_as=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']=='d' and 'CompanionAttackSpeed' in gr.get('f',[])][0]
R.append({
 'id':'ragna-ashot-bow','cls':c,'base':base(c,'Warmonger Bow'),'ilvl':82,'difficulty':1,'budget':'low',
 'buildTags':[K('활 공격','Bow attacks'),K('물리','Physical'),K('공격 속도','Attack speed')],'patch':'0.5','created':'2026-11-09','author':RG,
 'source':{'url':'https://www.youtube.com/watch?v=m0eHw6nq24Q','title':'【POE 2】라장간 #1 아샷활 초간단 제작 가이드 (엔드게임에서 제작 꼭 하세요)','channel':'라그나게임채널'},
 'title':K('물리 % 1티어 + 마모 플랫 + 아마나무 공격 속도','T1 % physical + Abrasion flat + Amanamu attack speed'),
 'start':{'rar':'magic','mods':[{'gi':bw_pct,'tmax':1},{'junk':'s'}]},
 'phases':[{'id':'base','kr':'베이스','en':'Base'},{'id':'pre','kr':'접두','en':'Prefixes'},{'id':'suf','kr':'접미 (훼손)','en':'Suffixes (desecration)'}],
 'nodes':[
  {'id':'w1','phase':'base','do':'base','cost':'base','ts':'0:40','note':K('물리 피해 % 증가 1티어가 붙은 매직 전쟁광 활(아이템 레벨 82). 자본에 맞춰 거래소에서 사거나 진화·확장으로 직접 띄움. 영상은 초반엔 깡딜이 높은 절멸자 활(공격 속도 1.1)을 추천, 전쟁광 활(1.2)은 사거리 감소 디버프가 없어 하이엔드용.','A magic Warmonger Bow with T1 % physical damage (item level 82); buy it to your budget or roll it with transmute/augment. The video recommends the Obliterator Bow (higher base damage, 1.1 attack speed) early; the Warmonger (1.2) avoids the range penalty for high end.')},
  {'id':'w2','phase':'pre','do':'essence','cur':'Greater_Essence_of_Abrasion','target':{'gi':bw_flatE},'ts':'2:07','note':K('상위 마모의 에센스로 희귀가 되며 공격 시 물리 피해 추가 확정. 이 옵션은 제작 속성이라 이후 심연의 에센스 같은 제작 속성은 못 씀.','Greater Essence of Abrasion makes it rare with a guaranteed flat physical line. That line counts as crafted, so another crafted line (e.g. Essence of the Abyss) cannot be added later.')},
  {'id':'w3','phase':'pre','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'ts':'2:31','note':K('좌측 찬미의 징조 + 엑잘티드 오브로 접두 마지막 자리. 원소 플랫이면 좋고 정확도는 아쉬움. 물리 % + 정확도 하이브리드가 뜨면 대박(영상).','Sinistral Exaltation + Exalted Orb for the last prefix: an elemental flat is good, accuracy is a letdown, the % physical + accuracy hybrid is the jackpot (as in the video).')},
  {'id':'w4','phase':'suf','do':'desecrate','cur':'Preserved_Jawbone','omens':['Omen_of_the_Liege'],'target':{'unrev':'s'},'ts':'3:42','note':K('보존된 턱뼈 + 군왕의 징조로 아마나무 훼손. 접두가 꽉 차 있어서 우측 강령술의 징조 없이도 접미에 들어감. 아마나무 접미에 공격 속도가 있음.','Preserved Jawbone + Omen of the Liege for an Amanamu desecration; with the prefixes full it lands on a suffix without Necromancy. Amanamu suffixes include attack speed.')},
  {'id':'w5','phase':'suf','do':'exalt','cur':'Greater_Exalted_Orb','target':{'junk':'s'},'ts':'4:18','note':K('공개 전에 상위 엑잘티드 오브로 남은 접미 하나. 레벨 35 미만 옵션이 안 나와서 공격 속도가 뜨면 1티어(레벨 35) 확정. 투사체 스킬 레벨·치명타·추가 화살·흡혈도 좋음(영상은 생명력 흡수).','Greater Exalted Orb for the last suffix before revealing: it skips modifiers below level 35, so attack speed lands at tier 1 (level 35). Projectile levels, crit, extra arrows or leech are good too (life leech in the video).')},
  {'id':'w6','phase':'suf','do':'reveal','target':{'reveal':{'gi':bw_as},'side':'s','lord':'amanamu','bone':'Preserved_Jawbone'},'fail':{'goto':'w4','via':LIGHT},'ts':'5:05','note':K('심연의 우물에서 공개해 공격 속도 + 반려수 공격 속도(영상 14%). 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시 훼손.','Reveal at the Well of Souls for attack speed + companion attack speed (14% in the video); otherwise Light + Annulment and desecrate again.')},
  {'id':'w7','phase':'suf','do':'note','ts':'5:43','note':K('주의: 마모의 에센스 옵션이 제작 속성이라 심연의 에센스 + 우측 결정화의 징조는 먹지 않음(우측 결정화의 징조를 살 필요 없음). 안 좋게 나온 활은 팔고 다시.','Note: the Abrasion line is crafted, so Essence of the Abyss with Dextral Crystallisation does not work (no need to buy the omen). Sell the misses and try again.')},
 ],
})
