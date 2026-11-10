# Batch 17 (사용자 2026-11-10: 다음 작업) — 전문가(4) → High-end (video) + Balance. Videos rechecked 2026-11-10 (transcripts).
#   breach-ring-video-v2 (SL RiJixgqBnBY), saveq-focus-v2 (SaVeQ R43FVay8_XI)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch16.py').read(); exec(_src[:_src.index('# ---------- 1. SL 부재')])

# ---------- 1. SL 원소 3플랫 재련된 균열 반지 (RiJixgqBnBY) ----------
# 영상 권장 순서: 원소 플랫 1티어 분열(화염·냉기·번개 아무거나) + 잡옵 → 균열의 에센스 → 강탈자 기폭제 65% → 바알 촉진시키는 주입기 1번(처음 1번은 100% 성공)
# → 카오스 오브(접미 하나 — 모든 원소 저항·희귀도) → 우측 찬미 + 완벽한 엑잘(나머지 하나, 빗나가면 지우고 다시 카오스 — 본편 6번째 성공)
# → 좌측 찬미 + 엑잘(접두 잡옵) → 좌측 결정화 + 재빠른 합금(공격 속도) → 완벽한 엑잘 1번(상위 찬미 없이) → 빗나가면 좌측 소멸의 징조 + 완벽한 엑잘 반복(평균 약 50번, 영상 59번, "2티어 타협도 좋음")
# → 마지막 접두는 고대 빗장뼈 + 심연의 메아리(영상 17개). 75% 퀄리티 본편과 디바인·축성·타락은 뺌.
# 하이엔드 = 영상(원소 플랫 모두 1티어), 밸런스 = 원소 플랫 1~2티어(영상: 너무 안 뜨면 2티어로 타협).
FLS=[('ff',15),('cf',17),('lf',19)]
tags={**{n:{'gi':g,'tmax':'$pT'} for n,g in FLS},'fr':{'gi':15,'tmax':1},'mq':{'gi':71},'ar':{'gi':7,'tmax':1},'rs':{'gi':27,'tmax':1},'as':{'gi':73},
      'fl':{'anyOf':[n for n,_ in FLS]},'gs':{'anyOf':['ar','rs']}}
FF=it('p','공격 시 화염 피해 (25—29)~(37—45) 추가 (분열)','Adds (25—29) to (37—45) Fire damage to Attacks (fractured)',['fr'])
CF=it('p','공격 시 냉기 피해 (21—24)~(32—37) 추가','Adds (21—24) to (32—37) Cold damage to Attacks',['cf'])
LF=it('p','공격 시 번개 피해 (1—4)~(60—71) 추가','Adds (1—4) to (60—71) Lightning damage to Attacks',['lf'],'d')
BQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% to Maximum Quality (Essence of the Breach)',['mq'],'c')
AR=it('s','모든 원소 저항 +(15—16)%','+(15—16)% to all Elemental Resistances',['ar']); RR=it('s','발견하는 아이템 희귀도 (15—18)% 증가','(15—18)% increased Rarity of Items found',['rs'])
AS=it('s','공격 속도 (7—9)% 증가 (재빠른 합금)','(7—9)% increased Attack Speed (Swift Alloy)',['as'],'c')
FLN=[n for n,_ in FLS]
B0=[FF,J('s')]; B1=[FF,BQ]; B2=[FF,AR]; B3=[FF,AR,RR]; B4=[FF,J('p'),AR,RR]; B5=[FF,AR,RR,AS]; B6=[FF,CF,AR,RR,AS]; B7=B6+[UN('p')]; B8=[FF,CF,LF,AR,RR,AS]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'fr','fr':True},{'junk':'s'}]},K('공격 시 화염 피해 1티어 분열 + 잡옵 1개 (재련된 균열 반지, 아이템 레벨 80)','Fractured T1 fire damage to attacks + one junk line (Refined Breach Ring, item level 80)'),B0),
 mark([0,0.6],'q1',B0),
 act('q1','main',[0,1],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티','The junk goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% to Maximum Quality (crafted)')],K('에센스','Essence'),[{'to':'q2'}],B1,ess='mq'),
 act('q2','main',[0,2],'quality','Reaver_Catalyst',K('공격 퀄리티 65%','Attack quality 65%'),[st(None,'강탈자 기폭제 52개 (영상 평균)','52 Reaver Catalysts (video average)')],K('퀄리티','Quality'),[{'to':'q3'}],B1,count=52),
 act('q3','main',[0,3],'quality','Vaal_Catalysing_Infuser',K('퀄리티 66% 이상','Quality 66%+'),[st(None,'바알 촉진시키는 주입기 1개','One Vaal Catalysing Infuser')],K('퀄리티','Quality'),[{'to':'s1'}],B1,count=1),
 act('s1','main',[0,4],'chaos','Chaos_Orb',K('최대 퀄리티를 접미 첫번째 옵션으로','Max quality into the first suffix'),None,K('카오스','Chaos'),[{'if':{'has':'gs'},'to':'s2','res':'ok'},{'to':'s1','res':'fail'}],B2,show=['ar','rs']),
 act('s2','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),[{'if':{'all':[{'has':'ar'},{'has':'rs'}]},'to':'p0','res':'ok'},{'to':'s2x',**F}],B3,show=['ar','rs'],omens=['Omen_of_Dextral_Exaltation']),
 annul('s2x',[1,5],[{'if':{'has':'gs'},'to':'s2','res':'ok','port':'right'},{'to':'s1','res':'fail'}],omens=(),target=K('접미 옵션 하나 지우기','Remove one suffix')),
 act('p0','main',[0,6],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'p0b'}],B4,omens=['Omen_of_Sinistral_Exaltation']),
 act('p0b','main',[0,7],'essence','Swift_Alloy',K('잡옵을 지우고 공격 속도 (7—9)% 증가','The junk goes for (7—9)% increased Attack Speed'),[st('s','공격 속도 (7—9)% 증가 (제작 옵션)','(7—9)% increased Attack Speed (crafted)')],K('합금','Alloy'),[{'to':'p1'}],B5,ess='as',omens=['Omen_of_Sinistral_Crystallisation']),
 act('p1','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'fl','min':2}},'to':'d1','res':'ok'},{'to':'p1x',**F}],B6,show=['cf','lf']),
 annul('p1x',[1,8],[{'to':'p1'}],omens=('Omen_of_Sinistral_Annulment',),target=K('접두 잡옵 지우기','Remove the junk prefix')),
 act('d1','main',[0,9],'desecrate','Ancient_Collarbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],B7),
 act('d2','main',[0,10],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'count':{'tag':'fl','min':3}},'to':'ok','res':'ok'},{'to':'d2x',**F}],B8,want='fl',show=['cf','lf'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('d2x',[1,10],'d1'),
 done([0,11])]
graph11('breach-ring-video-v2','Rings','Refined Breach Ring',80,
  'SL 원소 3플랫 재련된 균열 반지(RiJixgqBnBY) — 원소 플랫 1티어 분열 + 잡옵 → 균열의 에센스 → 강탈자 기폭제 65% → 바알 촉진시키는 주입기 1번 → 카오스 오브(접미) → 우측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브 뒤 다시) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 재빠른 합금 → 완벽한 엑잘(빗나가면 좌측 소멸의 징조 + 완벽한 엑잘 반복) → 고대 빗장뼈 + 심연의 메아리(빛의 징조로 다시). 하이엔드 = 영상(원소 플랫 1티어), 밸런스 = 원소 플랫 1~2티어.',
  {**ROUTE,'pT':{'kr':'원소 플랫','en':'Elemental flats','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,
  {'high':K('영상: 원소 플랫 모두 1티어','Video: every elemental flat T1'),'bal':K('원소 플랫 1~2티어 (영상: 너무 안 뜨면 2티어로 타협)','T1–2 elemental flats (video: settle for T2 if it drags)')},tags,nodes,
  [{'id':'L1','nodes':['p1','p1x'],'kr':'접두 원소 플랫','en':'Prefix flat'},{'id':'L2','nodes':['d1','d2','d2x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'fr','tmax':1,'fr':True},{'tag':'cf','tmax':1 if v=='high' else 2},{'tag':'lf','tmax':1 if v=='high' else 2,'des':True},{'tag':'ar','tmax':1},{'tag':'rs','tmax':1},{'tag':'as','ess':True}]),
  {'quality':66,'sockets':0},{'all':[{'count':{'tag':'fl','min':3}},{'has':'ar'},{'has':'rs'},{'has':'as'}]},('high','bal'))

# ---------- 2. SaVeQ 집중구 (R43FVay8_XI) ----------
# 영상(첫 번째 집중구): 퀄리티 22% · 상위 마술의 에센스 주문 피해 분열 · 에너지 보호막 1티어 · 모든 주문 스킬 +2 · 접두 잡옵(훼손 공개 "아무거나")
# → 아스트리드의 창의성 장착 → 좌측 결정화 + 초월의 합금(시전 속도, 50/50으로 에너지 보호막 또는 잡옵이 지워짐) → 고대 갈비뼈로 접미 훼손(공개는 접두를 끝낸 뒤)
# → 완벽한 엑잘(에너지 보호막 1티어 기대, 혼합 에너지 보호막이 뜸) → 절사로 접두 → 에너지 보호막 2티어로 타협("완벽을 노리지 말 것")
# → 심연의 메아리 + 빛의 징조로 주문 치명타 명중 확률 1티어(2티어도 고민, 영상은 1티어까지). 완벽한 철 룬은 취향(정책 23).
# 하이엔드 = 영상(주문 치명타 1티어), 밸런스 = 주문 치명타 1~2티어.
tags={'sp':{'gi':43},'esp':{'gi':7,'tmax':1},'esf':{'gi':6,'tmax':2},'esh':{'gi':8,'tmax':2},'lvl':{'gi':16},'cs':{'gi':59},'cr':{'gi':19,'tmax':'$pT'},
      'ges':{'anyOf':['esp','esf','esh']},'keepF':{'anyOf':['ges','lvl','cs']}}
SPF=it('p','주문 피해 (75—89)% 증가 (분열)','(75—89)% increased Spell Damage (fractured)',['sp'],'c')
ESP=it('p','에너지 보호막 (92—100)% 증가','(92—100)% increased Energy Shield',['esp']); ESF=it('p','에너지 보호막 최대치 +(81—90)','+(81—90) to maximum Energy Shield',['esf'])
LV=it('s','모든 주문 스킬 레벨 +2','+2 to Level of all Spell Skills',['lvl']); CSA=it('s','시전 속도 (26—31)% 증가 (초월의 합금)','(26—31)% increased Cast Speed (Transcendent Alloy)',['cs'],'c')
CRT=it('s','주문 치명타 명중 확률 (54—59)% 증가','(54—59)% increased Critical Hit Chance for Spells',['cr'],'d')
RNA=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
GES=['esp','esf','esh']
def RF(vis):
    two={'count':{'tag':'ges','min':2}}
    return ROUTE_([{'if':{'all':[{'des':True},{'not':{'has':'cr'}}]},'to':'rvx'},
       {'if':{'all':[{'not':{'has':'cr'}},{'not':{'unrev':True}},{'sideLt':{'side':'s','n':3}}]},'to':'d1'},
       {'if':{'all':[{'not':two},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},{'if':{'not':two},'to':'w1'},{'if':{'unrevSide':'s'},'to':'rv'},{'to':'ok'}],vis)
RV=lambda vis: ROUTE_([{'if':{'not':{'count':{'tag':'ges','min':2}}},'to':'e1'},{'if':{'has':'cr'},'to':'ok'},{'to':'rvx'}],vis)
F0=[SPF,ESP,J('p'),LV]; F1=F0+[RNA]; F2=[SPF,ESP,LV,CSA,RNA]; F3=F2+[UN('s')]; F4=[SPF,ESP,ESF,LV,CSA,UN('s'),RNA]; F5=[SPF,ESP,ESF,LV,CSA,CRT,RNA]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'sp','fr':True,'ess':True},{'tag':'esp'},{'junk':'p'},{'tag':'lvl'}]},K('주문 피해 분열 + 에너지 보호막 1티어 + 모든 주문 스킬 +2 + 잡옵 1개 (퀄리티 22%, 특출난 베이스)','Fractured spell damage + T1 energy shield + all spell skills +2 + one junk line (22% quality, exceptional)'),F0),
 mark([0,0.6],'r1',F0),
 RUNE('r1',[0,1],'a1',F1),
 act('a1','main',[0,2],'essence','Transcendent_Alloy',K('잡옵을 지우고 시전 속도 (26—31)% 증가','The junk goes for (26—31)% increased Cast Speed'),[st('s','시전 속도 (26—31)% 증가 (제작 옵션)','(26—31)% increased Cast Speed (crafted)')],K('합금','Alloy'),RF({'d1':'ok','e1':F}),F2,ess='cs',omens=['Omen_of_Sinistral_Crystallisation']),
 act('d1','main',[0,3],'desecrate','Ancient_Rib',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RF({'e1':{}}),F3,omens=['Omen_of_Dextral_Necromancy']),
 act('e1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),RF({'rv':'ok','w1':F}),F4,show=GES),
 act('w1','main',[1,4],'chaos','Perfect_Chaos_Orb',K('접두 세번째 옵션','Third prefix'),None,K('카오스','Chaos'),RF({'rv':'ok'}),F4,show=GES,trim={'side':'p','keep':'keepF'}),
 act('rv','main',[0,5],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RV({'ok':'ok','rvx':F}),F5,want='cr',show=['cr'],omens=['Omen_of_Abyssal_Echoes']),
 annul('rvx',[1,5],[{'to':'d1','port':'right'}]),
 done([0,6])]
nodes[0]['start']['runes']=[]
graph11('saveq-focus-v2','Foci','Tasalian Focus',80,
  'SaVeQ 집중구(R43FVay8_XI) — 주문 피해 분열 + 에너지 보호막 1티어 + 모든 주문 스킬 +2 + 잡옵 → 아스트리드의 창의성 → 좌측 결정화 + 초월의 합금 → 고대 갈비뼈(접미 훼손) → 완벽한 엑잘(접두) → 절사로 에너지 보호막 1~2티어 → 공개(빛의 징조로 다시). 하이엔드 = 영상(주문 치명타 1티어), 밸런스 = 1~2티어.',
  {**ROUTE,'pT':{'kr':'주문 치명타 명중 확률','en':'Spell critical hit chance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,
  {'high':K('영상: 주문 치명타 명중 확률 1티어, 에너지 보호막은 2티어로 타협','Video: T1 spell crit chance, settle for T2 energy shield'),'bal':K('주문 치명타 명중 확률 1~2티어','T1–2 spell crit chance')},tags,nodes,
  [{'id':'L1','nodes':['d1','rv','rvx'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'sp','fr':True,'ess':True},{'tag':'esp','tmax':1},{'tag':'esf','tmax':2},{'tag':'lvl'},{'tag':'cs','ess':True},{'tag':'cr','tmax':1 if v=='high' else 2,'des':True}]),
  {'quality':22,'sockets':2},{'all':[{'has':'cr'},{'has':'cs'},{'count':{'tag':'ges','min':2}}]},('high','bal'))
