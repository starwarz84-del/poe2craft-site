# ---- 탱정-탱커의정석 "[POE2] 방패분쇄 키타바 2부 | 하이엔드 장비 제작 가이드 (워리어 방패·장갑·장화·철퇴)" (youtu.be/gQa51XOS98s) — 방패 부분(13:00~22:15)만 ----
c='Shields_str'
TJ5=K('탱정-탱커의정석 영상 기반','Based on 탱정-탱커의정석')
def textJ(t, sec, side=None):
    hits=[gi for gi,gr in enumerate(cd(c)['groups']) if gr['s']==sec and (side is None or gr['g']==side) and t in gr['t'][0][5]]
    if not hits: raise Exception(t)
    return hits[0]
tj_pdr=textJ('additional Physical Damage Reduction','n','s')
TJ_MAXRES=[{'gi':textJ('to Maximum %s Resistance'%e,'n','s'),'tmax':1} for e in ('Fire','Cold','Lightning')]
tj_flat=textJ('to Armour','n','p'); tj_pct=textJ('% increased Armour','n','p'); tj_hyb=textJ('increased Armour\n+','n','p')
TJ_ARM=[{'gi':tj_flat,'tmax':1},{'gi':tj_pct,'tmax':1}]
TJ_WH=['Omen_of_Whittling']
TJ_IRON=K('상위 철 룬 → 일품 룬으로 완벽한 철 룬','Greater Iron Rune → Masterwork Rune to a Perfect Iron Rune')
R.append({
 'id':'tankjung-kitava-shield','cls':c,'base':base(c,'Tawhoan Tower Shield'),'ilvl':81,'sockets':2,'exceptional':{'sockets':1},'difficulty':3,'budget':'high',
 'buildTags':[K('방어도','Armour'),K('방패 분쇄','Shield Crush'),K('최대 저항','Maximum resistance')],'patch':'0.5.5','created':'2026-11-09','author':TJ5,
 'source':{'url':'https://www.youtube.com/watch?v=gQa51XOS98s','title':'[POE2] 방패분쇄 키타바 2부 | 하이엔드 장비 제작 가이드 (워리어 방패·장갑·장화·철퇴)','channel':'탱정-탱커의정석'},
 'title':K('받는 물리 피해 감소 분열 + 최대 저항 옵션 2개 + 방어도 1티어 옵션 3개','fractured physical damage reduction + two max resistances + three T1 armour lines'),
 'start':{'rar':'rare','quality':20,'mods':[{'gi':tj_pdr,'tmax':1,'fr':True},{'junk':'s'}]},
 'phases':[{'id':'suf','kr':'접미 먼저','en':'Suffixes first'},{'id':'pre','kr':'접두 · 절사','en':'Prefixes and whittling'},{'id':'fin','kr':'마무리','en':'Finish'}],
 'nodes':[
  {'id':'t1','phase':'suf','do':'base','cost':'base','ts':'14:24',
   'note':K('받는 물리 피해 8% 감소(또는 화염 저항 최대치 +3%) 분열 + 잡옵 1개.','Fractured 8% physical damage reduction (or +3% maximum fire resistance) plus one junk line.')},
  {'id':'t2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'anyOf':TJ_MAXRES},'fail':{'goto':'self'},'ts':'17:21'},
  {'id':'t3','phase':'suf','do':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Dextral_Necromancy'],'target':{'unrev':'s'},'ts':'18:24'},
  {'id':'t4','phase':'suf','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':TJ_MAXRES},'side':'s','bone':'Ancient_Rib'},'fail':{'goto':'t3','via':LIGHT},'ts':'18:31',
   'br':K('대박 → 접두, 실패: 빛의 징조 + 소멸의 오브 → {#t3}번','hit → prefixes; miss: Omen of Light + Annulment → step {#t3}')},
  {'id':'t5','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Greater_Exaltation'],'target':{'junk':['p','p']},'ts':'19:03'},
  {'id':'t6','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','target':{'junk':'p'},'ts':'19:15'},
  {'id':'t7','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':TJ_WH,'target':{'anyOf':TJ_ARM,'replace':'p'},'fail':{'goto':'self'},'ts':'20:00',
   'br':K('방어도 1티어 레벨 75가 접두 최고 레벨이라 7~9번 절사는 늘 잡옵만 바꿈','T1 armour (75) is the top prefix level, so whittling in steps 7–9 only ever hits junk')},
  {'id':'t8','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':TJ_WH,'target':{'gi':tj_pct,'tmax':1,'replace':'p'},'fail':{'goto':'self'},'ts':'20:15'},
  {'id':'t9','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':TJ_WH,'target':{'gi':tj_hyb,'tmax':1,'replace':'p'},'fail':{'goto':'self'},'ts':'20:32',
   'br':K('복합 1티어가 뜰 때까지 반복, 매번 절사의 징조 확인','Repeat until the T1 hybrid lands (check the Omen of Whittling every time)')},
  {'id':'t10','phase':'fin','do':'manual','target':{'rune':K('완벽한 철 룬','Perfect Iron Rune')},'label':TJ_IRON,'ts':'21:25'},
  {'id':'t11','phase':'fin','do':'manual','target':{'rune':K('완벽한 철 룬','Perfect Iron Rune')},'label':TJ_IRON,'ts':'21:25'},
  {'id':'t12','phase':'fin','do':'manual','optional':True,'label':K('바알 방어구 장인의 주입기로 퀄리티 30% (선택)',"Vaal Armourer's Infuser to 30% quality (optional)"),'ts':'21:40',
   'note':K('타락하면 그 퀄리티로 완성.','If it corrupts, that quality is final.')},
 ]})
