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
  {'id':'b1','phase':'base','do':'base','cost':'base','note':K('공격 시 물리 피해 1티어 분열 + 잡옵 1줄 균열 반지(아이템 레벨 82).','A Breach Ring with fractured T1 physical attack damage plus one junk line (item level 82).')},
  {'id':'b2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':bp_allres,'tmax':1},'fail':{'goto':'self'},
   'note':K('카오스 오브로 모든 원소 저항 1티어. 가중치가 낮아 뒤에서 엑잘로 뽑기 어려우니 여기서 먼저 확보.','Chaos for T1 all elemental resistances: low weight, hard to slam later, so it comes first.')},
  {'id':'b3','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},'note':K('접두에 버릴 옵션 하나.','One throwaway prefix.')},
  {'id':'b4','phase':'suf','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':bp_maxQ},'note':K('좌측 결정화의 징조 + 균열의 에센스로 그 접두를 최대 퀄리티 +20%로 바꿈.','Sinistral Crystallisation + Essence of the Breach turns it into +20% maximum quality.')},
  {'id':'b5','phase':'suf','do':'quality','cur':'Xophs_Catalyst','target':{'quality':60},'note':K('조프의 기폭제로 화염 퀄리티 60%(기본 20% + 균열 반지 고정 20% + 최대 퀄리티 20%).','Xoph\'s Catalysts to 60% fire quality (20% base + 20% implicit + 20% from the Breach line).')},
  {'id':'b6','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'gi':bp_fres,'tmax':2},
   'fail':{'goto':'b5','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'b2'},
   'note':K('촉진하는 찬미의 징조 + 우측 찬미의 징조 + 완벽한 엑잘티드 오브로 화염 저항. 원소 무관 3종을 그냥 노리는 것보다 잘 뜸. 퀄리티는 0%가 됨. 쓸 수 없는 줄이면 우측 소멸의 징조 + 소멸의 오브로 1/2 도박(모든 원소 저항이 지워지면 처음부터) 후 기폭제부터 다시.','Catalysing + Dextral Exaltation + Perfect Exalt for fire resistance, likelier than any of three plain; quality drops to 0. On a useless line, Dextral Annulment is a 1/2 gamble (losing all-res means starting over), then refill and retry.')},
  {'id':'b6b','phase':'suf','do':'note','fallbackFor':'b6','label':K('갈림길 ②: 타협','Fork (2): settle'),'note':K('쓸 만한 접미면 그대로 두고 접두로 넘어감.','Keep a usable suffix and move on to the prefixes.')},
  {'id':'b7','phase':'pre','do':'quality','cur':'Reaver_Catalyst','target':{'quality':60},'note':K('접미가 끝났으니 강탈자 기폭제로 공격 퀄리티 60%. 완성품의 퀄리티 종류.','Suffixes done: Reaver Catalysts to 60% attack quality, the finished quality type.')},
  {'id':'b8','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'},
   'note':K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브로 접두 한 줄. 공격 시 원소 피해가 붙으면 베스트, 아니면 잡옵.','Sinistral Exaltation + Perfect Exalt one prefix: an elemental attack flat is best, otherwise junk.')},
  {'id':'b9','phase':'pre','do':'essence','cur':'Swift_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':bp_as,'removeGi':bp_maxQ,'chance':0.5},'fail':{'goto':'m1'},
   'note':K('좌측 결정화의 징조 + 재빠른 합금: 접두(최대 퀄리티 · 방금 붙은 줄) 중 하나가 지워지고 공격 속도는 접미에. 최대 퀄리티가 지워지면 좋음(1/2). 이 뒤로는 제작 옵션이 이미 있어서 심연의 에센스(제작 옵션)를 쓸 수 없음.','Sinistral Crystallisation + Swift Alloy: one prefix goes (maximum quality or the new line) and attack speed lands on a suffix; losing maximum quality is the good half. From here Essence of the Abyss (also crafted) cannot be used.')},
  {'id':'o1','phase':'pre','branch':OKA,'do':'desecrate','cur':'Ancient_Collarbone','target':{'unrev':'p'},
   'note':K('최대 퀄리티가 지워졌으면 남은 자리에 고대 빗장뼈로 훼손. 8번 줄이 잡옵이었다면 아래 "남았을 때"처럼 완벽한 엑잘티드 오브로 채운 뒤 1/2 훼손 도박.','Maximum quality gone: desecrate the free prefix with an Ancient Collarbone. If step 8 gave junk, fill it with a Perfect Exalt and use the 1/2 desecration gamble below instead.')},
  {'id':'o2','phase':'pre','branch':OKA,'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':FLATS},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'o1','via':LIGHT},
   'note':K('심연의 메아리의 징조로 공개해 공격 시 원소 피해. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 다시.','Reveal with Abyssal Echoes for an elemental attack flat; otherwise Light + Annulment and retry.')},
  {'id':'m1','phase':'pre','branch':MSA,'do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'p'},
   'note':K('최대 퀄리티가 남았으면 완벽한 엑잘티드 오브로 접두를 채움(접미는 꽉 차서 징조 불필요).','Maximum quality stayed: fill the prefixes with a Perfect Exalt (suffixes are full, no omen).')},
  {'id':'m2','phase':'pre','branch':MSA,'do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'anyOf':FLATS,'removeGi':bp_maxQ},
   'note':K('절사의 징조 + 완벽한 카오스 오브로 최대 퀄리티(레벨이 가장 낮음)를 돌려 공격 시 원소 피해 찾기(티어는 타협).','Whittling + Perfect Chaos rerolls maximum quality (the lowest level) into an elemental attack flat (settle on the tier).')},
  {'id':'m3','phase':'pre','branch':MSA,'do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Sinistral_Erasure'],'target':{'anyOf':FLATS,'replace':'p'},'fallbackFor':'m2','fail':{'goto':'self'},
   'label':K('안 뜨면: 접두 계속 돌리기','On a miss: keep rolling'),
   'note':K('안 뜬 줄이 낮은 레벨이면 다시 절사의 징조, 레벨이 높아 절사의 징조로는 좋은 줄이 바뀔 수 있으면 좌측 말소의 징조(보통 더 비쌈) + 완벽한 카오스 오브로 계속 돌림.','If the miss is low level, Whittling again; if it is high level (Whittling could hit a good line), Sinistral Erasure (usually pricier) + Perfect Chaos.')},
  {'id':'m4','phase':'pre','branch':MSA,'do':'desecrate','cur':'Ancient_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p','chance':0.5},'fail':{'goto':'m2'},
   'note':K('접두가 꽉 찬 채로 좌측 강령술의 징조 + 고대 빗장뼈: 분열 줄 빼고 두 줄 중 하나가 지워지고 그 자리에 훼손(1/2로 잡옵이 지워짐). 찾은 원소 피해가 1티어면 이 도박 대신 좌측 말소의 징조 + 절사의 징조 + 완벽한 카오스 오브로 마지막 줄을 찾음.','Full prefixes, Sinistral Necromancy + Ancient Collarbone: one of the two non-fractured prefixes goes and the desecration takes its place (1/2 it takes the junk). If the flat you found is tier 1, use Sinistral Erasure + Whittling + Perfect Chaos for the last line instead.')},
  {'id':'m5','phase':'pre','branch':MSA,'do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':FLATS},'side':'p','bone':'Ancient_Collarbone'},'fail':{'goto':'m4','via':LIGHT},
   'note':K('심연의 메아리의 징조로 공개해 공격 시 원소 피해. 안 나오면 빛의 징조 + 소멸의 오브로 지우고 빈자리에 다시 훼손.','Reveal with Abyssal Echoes for an elemental attack flat; otherwise Light + Annulment and desecrate the free slot again.')},
 ],
})
