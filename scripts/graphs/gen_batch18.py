# Batch 18 (사용자 2026-11-10: 나머지도 2개씩) — 극한(5) → High-end (video) + Balance. Videos rechecked 2026-11-10 (transcripts).
#   sl-proj7-gloves-v2 (SL XMYJh3CnXuY), diztoh-iceshot-bow-v2 (Diztoh 29vO0mMUoME)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch16.py').read(); exec(_src[:_src.index('# ---------- 1. SL 부재')])

# ---------- 1. SL 투사체 7옵션 장갑 (XMYJh3CnXuY) ----------
# 영상: 콜르의 사냥 장착 · 모든 투사체 스킬 레벨 +2 분열 + 잡옵(퀄리티 25%) → 세를의 승리(분열 뒤에 장착 — 영상의 교훈)
# → 카오스 오브(투사체 피해·속도 1티어) → 상위 찬미 + 좌측 찬미 + 완벽한 엑잘(남은 투사체 1티어 + 마나·에너지 보호막·공격 시 물리 피해 1티어),
#   잡옵 2개 = 소멸의 오브, 잡옵 1개 = 절사(가장 낮을 때만 — 영상은 안 돼서 소멸의 오브 반복), 투사체 옵션이 지워지면 카오스부터
# → 상위 찬미 + 완벽한 엑잘(접미 치명타 확률 1티어 + 잡옵, 둘 다 잡옵이면 우측 결정화 + 심연의 에센스 → 고대 갈비뼈 → 빛의 징조로 하나씩 지움)
# → 우측 결정화 + 팽창하는 합금(마나 1티어가 있을 때 매물 방식, 1/2 — 치명타가 지워지면 접미 처음부터) → 고대 갈비뼈 → 관통 51%+ 공개(빛의 징조로 다시).
# 하이엔드 = 영상, 밸런스 = 세 번째 접두 1~2티어 · 관통 공개 결과 그대로.
GP=[('mf',7),('esf',8),('esp',9),('esh',10),('ph',13)]
tags={'proj':{'gi':82},'pd':{'gi':71,'tmax':1},'ps':{'gi':73,'tmax':1},'cr':{'gi':74},'pie':{'gi':75},'rem':{'gi':65},'mkS':{'gi':61},
      **{n:{'gi':g,'tmax':'$pT'} for n,g in GP},'pp':{'anyOf':['pd','ps']},'third':{'anyOf':[n for n,_ in GP]},'gpre':{'anyOf':['pp','third']},'keepP':{'anyOf':['pp','third']}}
PR=it('s','모든 투사체 스킬 레벨 +2 (분열)','+2 to Level of all Projectile Skills (fractured)',['proj'])
KO=it('r','콜르의 사냥','Kolr’s Hunt',None,'r'); SE=it('r','세를의 승리','Serle’s Triumph',None,'r')
PS=it('p','투사체 속도 (31—40)% 증가','(31—40)% increased Projectile Speed',['ps']); PD=it('p','투사체 피해 (31—40)% 증가','(31—40)% increased Projectile Damage',['pd'])
MF=it('p','마나 최대치 +(105—124)','+(105—124) to maximum Mana',['mf'])
CR=it('s','치명타 확률 (28—34)% 증가','(28—34)% increased Critical Hit Chance',['cr']); RM=it('s','잔류물을 (35—50)% 더 먼 곳에서 획득 가능 (팽창하는 합금)','Remnants can be collected from (35—50)% further away (Expansive Alloy)',['rem'],'c')
PI=it('s','(51—100)%의 확률로 적 관통','(51—100)% chance to Pierce an Enemy',['pie'],'d'); MS=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mkS'],'c')
SHP=['pd','ps']; SHT=[n for n,_ in GP]
def RG(vis):   # every step re-checks the item
    p2={'count':{'tag':'pp','min':2}}; full={'all':[p2,{'has':'third'}]}
    return ROUTE_([{'if':{'not':{'has':'pp'}},'to':'c1'},{'if':{'unrevSide':'s'},'to':'mL'},{'if':{'has':'mkS'},'to':'mB'},
       {'if':{'all':[{'not':full},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},
       {'if':{'not':full},'to':'e1x'},
       {'if':{'all':[{'has':'cr'},{'has':'rem'},{'sideLt':{'side':'s','n':4}}]},'to':'d1'},{'if':{'has':'rem'},'to':'sR'},   # 합금이 치명타 확률을 지웠거나 접미가 꽉 참 → 영상 4:47 '실패하면 접미 작업 처음부터': 합금이 있는 동안은 심연의 에센스를 못 쓰니(제작 옵션 1개) 우측 소멸의 징조로 비움
       
       {'if':{'all':[{'has':'cr'},{'not':{'has':'rem'}},{'sideLt':{'side':'s','n':3}}]},'to':'s1'},
       {'if':{'all':[{'has':'cr'},{'not':{'has':'rem'}}]},'to':'a1'},
       {'if':{'sideLt':{'side':'s','n':2}},'to':'s1'},{'to':'mA'}],vis)
G0=[PR,J('p'),KO]; G1=[PR,J('p'),KO,SE]; G2=[PS,PR,KO,SE]; G3=[PS,PD,MF,PR,KO,SE]; G4=G3[:3]+[PR,CR,J('s'),KO,SE]; G5=G3[:3]+[PR,CR,RM,KO,SE]; G6=G5[:-2]+[UN('s'),KO,SE]; G7=G3[:3]+[PR,CR,RM,PI,KO,SE]
GM=G3[:3]+[PR,J('s'),MS,KO,SE]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'proj','fr':True},{'junk':'p'}]},K('콜르의 사냥 장착 · 모든 투사체 스킬 레벨 +2 분열 + 잡옵 1개 (퀄리티 25%)','Kolr’s Hunt socketed · fractured +2 projectile skills + one junk line (25% quality)'),G0),
 mark([0,0.6],'r1',G0),
 act('r1','main',[0,1],'rune',None,K('세를의 승리 장착 (접미 +1)','Socket Serle’s Triumph (+1 suffix)'),[st(None,'접미 옵션 4개','Four suffixes')],K('룬','Rune'),[{'to':'c1'}],G1,slots={'s':1},rune=K('세를의 승리','Serle’s Triumph')),
 act('c1','main',[0,2],'chaos','Chaos_Orb',K('접두 첫번째 옵션','First prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pp'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],G2,show=SHP),
 act('e1','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefixes'),None,K('엑잘','Exalt'),RG({'s1':'ok','e1x':F}),G3,show=SHP+SHT,omens=['Omen_of_Greater_Exaltation','Omen_of_Sinistral_Exaltation']),
 annul('e1x',[1,3],RG({'e1':{'res':'ok','port':'right'},'c1':{'res':'fail'}}),omens=(),target=K('접두 잡옵 지우기','Remove a junk prefix')),
 act('s1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),None,K('엑잘','Exalt'),RG({'a1':'ok','mA':F}),G4,show=['cr'],omens=['Omen_of_Greater_Exaltation']),
 act('mA','main',[1,4],'essence','Essence_of_the_Abyss',K('잡옵을 지우고 심연의 군주의 징표','The junk goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),RG({'mB':{}}),GM,ess='mkS',mark=True,omens=['Omen_of_Dextral_Crystallisation']),
 act('mB','main',[2,4],'desecrate','Ancient_Rib',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RG({'mL':{}}),GM,fromMark=True),
 annul('mL',[2,5],RG({'s1':{},'mA':{}})),
 act('a1','main',[0,6],'essence','Expansive_Alloy',K('잡옵을 지우고 잔류물을 (35—50)% 더 먼 곳에서 획득 가능','The junk goes for Remnants collected (35—50)% further away'),[st('s','잔류물을 (35—50)% 더 먼 곳에서 획득 가능 (제작 옵션)','Remnants can be collected from (35—50)% further away (crafted)')],K('합금','Alloy'),RG({'d1':'ok','sR':F}),G5,ess='rem',omens=['Omen_of_Dextral_Crystallisation']),
 annul('sR',[1,6],RG({'s1':{},'mA':{},'d1':{}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 옵션 지우기','Remove a suffix')),
 act('d1','main',[0,7],'desecrate','Ancient_Rib',K('접미 네번째 옵션(훼손)','Fourth suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],G6),
 act('d2','main',[0,8],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'pie'},'to':'ok','res':'ok'},{'if':V1,'to':'d2x',**F},{'to':'ok','res':'fail'}],G7,want='pie',show=['pie']),
 LIGHTX('d2x',[1,8],'d1'),
 done([0,9])]
graph11('sl-proj7-gloves-v2','Gloves_int','Sirenscale Gloves',80,
  'SL 투사체 7옵션 장갑(XMYJh3CnXuY) — 콜르의 사냥 · 투사체 +2 분열 + 잡옵 → 세를의 승리 → 카오스 오브(투사체 피해·속도) → 상위 찬미 + 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브) → 상위 찬미 + 완벽한 엑잘(치명타 확률, 잡옵 2개면 우측 결정화 + 심연의 에센스 → 고대 갈비뼈 → 빛의 징조) → 우측 결정화 + 팽창하는 합금(1/2) → 고대 갈비뼈 → 관통 공개. 하이엔드 = 영상, 밸런스 = 세 번째 접두 1~2티어 · 관통 공개 결과 그대로.',
  {**ROUTE,'pT':{'kr':'접두 세번째 옵션','en':'Third prefix','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,
  {'high':K('영상: 세 번째 접두 1티어, 관통은 빛의 징조로 다시','Video: T1 third prefix, Light retries pierce'),'bal':K('세 번째 접두 1~2티어, 관통 공개 결과 그대로','T1–2 third prefix, keep the reveal')},tags,nodes,
  [{'id':'L1','nodes':['d1','d2','d2x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['mA','mB','mL'],'kr':'잡옵 정리','en':'Clear junk'}],
  FIN(('high','bal'),lambda v:[{'tag':'ps','tmax':1},{'tag':'pd','tmax':1},{'tag':'mf','tmax':1 if v=='high' else 2},{'tag':'proj','fr':True},{'tag':'cr'},{'tag':'rem','ess':True},{'tag':'pie','des':True} if v=='high' else {'side':'s','random':True}]),
  {'quality':25,'sockets':2},{'all':[{'count':{'tag':'pp','min':2}},{'has':'third'},{'has':'cr'},{'has':'rem'}]},('high','bal'),xsub=["Kolr's Hunt"],xroll=True)

# ---------- 2. Diztoh 얼음 사격 데드아이 활 (29vO0mMUoME) ----------
# 영상: 물리 피해 % 분열 + 잡옵 → 카오스 오브(물리 피해 추가 1티어, 3티어 이상도 타협 가능) → 좌측 찬미 + 완벽한 엑잘(냉기 — 번개·화염·복합 물리도 받음,
# 공격 원소 피해 %·정확도는 절사의 징조 + 카오스 오브로 교체) → 번개·화염 1티어면 알두르의 숨결(냉기로 바뀜, 소켓 소모) → 아스트리드의 창의성
# → 우측 강령술 + 고대 턱뼈 → 메아리 공개(투사체 +4) → 안 나오면 '빛 없이 다시': 우측 결정화 + 완벽한 가속의 에센스(훼손 제거·맹공) → 우측 결정화 + 심연의 에센스(맹공 → 징표) → 징표 훼손
# → 우측 찬미 + 엑잘(접미 잡옵) → 절사의 징조(+ 우측 말소의 징조) + 카오스 오브(치명타 확률) → 완벽한 엑잘(마지막 접미, 운). 신성한 오브·타락은 뺌.
# 하이엔드 = 영상(투사체 +4, 물리 추가 1티어), 밸런스 = 투사체 +3~+4 · 물리 추가 1~3티어 · 냉기 등 1~2티어.
# 2026-11-12 영상 전체 대조(자동 번역 자막 0:00~22:20 + 화면 9:25, 메인 세션): 단계 일치. 화면 9:25 = 훼손할 때 접미가 훼손 하나뿐(접두 3개, 접미 비어 있음) — 그래야 우측 결정화 + 에센스가 훼손 옵션만 지움.
#   옛 그래프는 접두 단계 카오스가 접미 잡옵을 남겨(최대 3개) 결정화가 아무 접미나 지우고 제작 옵션이 쌓였음(c1check l1·l2) → 매 단계 아이템을 다시 보는 RB로 다시 만듦:
#   접두 단계 카오스가 접미 잡옵을 2개 이상 남기면 우측 소멸의 징조로 하나씩(내부 결정). 접두 잡옵은 가장 낮은 레벨일 때만 절사 + 좌측 말소 + 카오스(영상 4:30, 16:00), 아니면 좌측 소멸의 징조. 접미에 잡옵이 남아 있으면 훼손 대신 결정화 + 완벽한 가속의 에센스부터(빛 없이 다시 공개와 같은 길).
#   치명타 확률은 절사의 징조 + 카오스(영상 15:30~18:00 일반 카오스 오브, 가장 낮은 옵션이 접두면 우측 말소의 징조도). 등급 목표가 1~2티어라 절사 반복은 상위 카오스 오브(1,000회 시험: 일반 25,116 / 상위 12,476 / 완벽 14,080). 마지막 접미는 영상이 완벽한 엑잘 한 번(민첩, 그대로 둠).
#   등급 C17: 물리 피해 추가는 분열 뒤 카오스라 모든 등급 1티어. 원소·투사체·치명타 확률 = 하이엔드 1티어 / 밸런스 1~2티어, 마지막 접미는 하이엔드만 공격 속도·치명타 피해 1티어로 바꾸는 도박(절사 카오스).
tags={'pp':{'gi':7},'fl':{'gi':2,'tmax':1},'co':{'gi':4,'tmax':'$pT'},'li':{'gi':6,'tmax':'$pT'},'fi':{'gi':3,'tmax':'$pT'},'hy':{'gi':8,'tmax':'$pT'},
      'ele':{'anyOf':['co','li','fi','hy']},'conv':{'anyOf':['li','fi']},'proj':{'gi':9,'tmax':'$jT'},'cc':{'gi':17,'tmax':'$cT'},'ons':{'gi':55},'mk':{'gi':57},
      'as':{'gi':15,'tmax':1},'cd':{'gi':18,'tmax':1},'last':{'anyOf':['as','cd'],'label':K('공격 속도·치명타 피해 1티어','T1 attack speed or crit damage')},
      'keepP':{'anyOf':['pp','fl','ele']},'keepS':{'anyOf':['proj','cc']},'keepS3':{'anyOf':['proj','cc','last']}}
PP=it('p','물리 피해 (155—169)% 증가 (분열)','(155—169)% increased Physical Damage (fractured)',['pp'])   # 영상 완성품 = 2티어 분열(165%)
FL=it('p','물리 피해 (26—39)~(44—66) 추가','Adds (26—39) to (44—66) Physical Damage',['fl']); CO=it('p','냉기 피해 (72—81)~(110—123) 추가','Adds (72—81) to (110—123) Cold Damage',['co'])
PJ=it('s','모든 투사체 스킬 레벨 +4','+4 to Level of all Projectile Skills',['proj'],'d'); CC=it('s','치명타 확률 +(3.11—3.8)%','+(3.11—3.8)% to Critical Hit Chance',['cc'])   # 영상 완성품 = 3티어(+3.6%)
ON=it('s','이 무기로 명중시켜 처치 시 (20—25)%의 확률로 맹공 획득 (완벽한 가속의 에센스)','(20—25)% chance to gain Onslaught on Killing Hits with this Weapon (Perfect Essence of Haste)',['ons'],'c')
MKB=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mk'],'c')
AL=it('r','알두르의 숨결','Breath of Aldur',None,'r'); AS=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
def RB(vis):   # every step re-checks the item — prefixes (RB) → runes → suffixes (RS)
    return ROUTE_([{'if':{'not':{'has':'fl'}},'to':'c1'},
       {'if':{'all':[{'not':{'has':'ele'}},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},
       {'if':{'all':[{'not':{'has':'ele'}},{'whittleSafe':{'tag':'keepP','side':'p'}}]},'to':'e1w'},
       {'if':{'not':{'has':'ele'}},'to':'e1x'},{'if':{'has':'conv'},'to':'al'},{'to':'r2'}],vis)
def RS(vis):   # after the runes: suffixes only (nothing here touches a prefix)
    sN=lambda n:{'sideLt':{'side':'s','n':n}}
    return ROUTE_([{'if':{'unrevSide':'s'},'to':'d2'},{'if':{'has':'mk'},'to':'l3'},
       {'if':{'all':[{'has':'proj'},sN(2)]},'to':'x1'},
       {'if':{'all':[{'has':'proj'},{'not':{'has':'cc'}},{'whittleSafe':{'tag':'keepS','side':'s'}}]},'to':'x2'},
       {'if':{'all':[{'has':'proj'},{'not':{'has':'cc'}}]},'to':'x2x'},
       {'if':{'all':[{'has':'proj'},sN(3)]},'to':'x3'},
       {'if':{'all':[{'has':'proj'},{'any':[{'has':'last'},{'param':{'v':2}}]}]},'to':'ok'},
       {'if':{'all':[{'has':'proj'},{'whittleSafe':{'tag':'keepS3','side':'s'}}]},'to':'x3w'},
       {'if':{'has':'proj'},'to':'ok'},   # 마지막 접미가 가장 낮은 레벨이 아니면 도박을 멈춤(우측 소멸은 투사체를 지울 수 있음)
       {'if':{'not':sN(2)},'to':'sX'},{'if':{'has':'ons'},'to':'l2'},{'if':sN(1),'to':'d1'},{'to':'l1'}],vis)
W0=[PP,J('s')]; W1=[PP,FL]; W2=[PP,FL,CO]; W3=W2+[AL]; W4=W3+[AS]; W5=W4+[UN('s')]; W6=W4+[PJ]; W7=W4+[ON]; W8=W4+[MKB]; W9=W4+[PJ,J('s')]; W10=W4+[PJ,CC]; W11=W10+[R1('s')]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pp','fr':True},{'junk':'s'}]},K('물리 피해 % 2티어 분열 + 잡옵 1개 (특출난 절멸자 활, 룬 소켓 3, 아이템 레벨 82)','Fractured T2 % physical damage + one junk line (exceptional Obliterator Bow, 3 rune sockets, item level 82)'),W0),
 mark([0,0.6],'c1',W0),
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접두 두번째 옵션','Second prefix'),None,K('카오스','Chaos'),RB({'e1':'ok','c1':F}),W1,show=['fl']),
 act('e1','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     RB({'al':{'res':'ok','hide':True},'r2':'ok','e1w':F,'e1x':F}),W2,show=['co','li','fi','hy'],omens=['Omen_of_Sinistral_Exaltation']),
 act('e1w','main',[1,2],'chaos','Greater_Chaos_Orb',K('접두 잡옵을 다시 (가장 낮은 레벨일 때)','Reroll the junk prefix (while it is the lowest level)'),None,K('카오스','Chaos'),
     RB({'al':'ok','r2':'ok','e1':{'res':'fail','port':'left'},'e1w':F,'e1x':F}),W2,show=['co','li','fi','hy'],omens=['Omen_of_Whittling','Omen_of_Sinistral_Erasure']),
 annul('e1x',[2,2],RB({'e1':{'res':'ok','port':'top'},'c1':{'res':'fail'}}),omens=('Omen_of_Sinistral_Annulment',),target=K('접두 하나 지우기 (잡옵 또는 물리 피해 추가, 50:50)','Remove one prefix (the junk or the flat physical, 50:50)')),
 act('al','main',[1,3],'rune',None,K('알두르의 숨결 장착','Socket Breath of Aldur'),[st(None,'화염·번개 옵션 → 냉기','Fire and lightning mods → cold')],K('룬','Rune'),[{'to':'r2'}],W3,rune=K('알두르의 숨결','Breath of Aldur')),
 act('r2','main',[0,4],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),RS({'d1':{},'l1':{},'sX':{}}),W4,rune=K('아스트리드의 창의성','Astrid’s Creativity')),
 annul('sX',[1,4],RS({'l1':{},'d1':{},'sX':{}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 줄이기 (2개 이상일 때)','Cut the junk suffixes (two or more)')),
 act('d1','main',[0,5],'desecrate','Ancient_Jawbone',K('접미 첫번째 옵션(훼손)','First suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RS({'d2':{}}),W5,omens=['Omen_of_Dextral_Necromancy']),
 act('d2','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RS({'x1':'ok','l1':F}),W6,want='proj',show=['proj'],omens=['Omen_of_Abyssal_Echoes']),
 act('l1','main',[1,6],'essence','Perfect_Essence_of_Haste',K('접미 옵션을 지우고 맹공','A suffix goes for Onslaught'),[st('s','맹공 획득 (제작 옵션)','Onslaught (crafted)')],K('에센스','Essence'),RS({'l2':{}}),W7,ess='ons',omens=['Omen_of_Dextral_Crystallisation']),
 act('l2','main',[1,7],'essence','Essence_of_the_Abyss',K('맹공을 지우고 심연의 군주의 징표','Onslaught goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),RS({'l3':{}}),W8,ess='mk',mark=True,omens=['Omen_of_Dextral_Crystallisation']),
 act('l3','main',[1,8],'desecrate','Ancient_Jawbone',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RS({'d2':{'port':'right'}}),W5,fromMark=True),
 act('x1','main',[0,9],'exalt','Exalted_Orb',K('접미 잡옵','A junk suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),RS({'x2':{},'x2x':F}),W9,omens=['Omen_of_Dextral_Exaltation']),
 act('x2','main',[0,10],'chaos','Greater_Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),RS({'x3':'ok','x2':F,'x2x':F}),W10,show=['cc'],trim={'side':'s','keep':'keepS'}),
 annul('x2x',[1,10],RS({'x2':{'res':'ok'},'x1':{},'l1':{'res':'fail'}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 하나 지우기 (잡옵이 가장 낮은 레벨이 아닐 때)','Remove one suffix (when the junk is not the lowest level)')),
 act('x3','main',[0,11],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),RS({'ok':'ok','x3w':F,'x2x':F}),W11,show=['as','cd'],
     over=[{'param':{'v':2},'set':{'goal':K('접미 세번째 옵션 (나오는 대로)','Third suffix (keep what comes)')}}]),
 act('x3w','main',[1,11],'chaos','Greater_Chaos_Orb',K('마지막 접미를 다시 (가장 낮은 레벨일 때)','Reroll the last suffix (while it is the lowest level)'),None,K('카오스','Chaos'),RS({'ok':'ok','x3w':F,'x2x':F}),W11,show=['as','cd'],trim={'side':'s','keep':'keepS3'}),
 done([0,12])]
graph11('diztoh-iceshot-bow-v2','Bows','Obliterator Bow',82,
  'Diztoh 얼음 사격 활(29vO0mMUoME) — 물리 % 분열 + 잡옵 → 카오스 오브(물리 피해 추가 1티어) → 좌측 찬미 + 완벽한 엑잘(냉기·번개·화염·복합, 빗나가면 절사 + 좌측 말소 + 카오스 오브) → 번개·화염이면 알두르의 숨결 → 아스트리드의 창의성 → 우측 강령술 + 고대 턱뼈 → 공개(투사체 +4, 빗나가면 우측 결정화 + 완벽한 가속의 에센스 → 심연의 에센스 → 징표 훼손) → 우측 찬미 + 엑잘 → 절사(+ 우측 말소) + 카오스 오브(치명타 확률) → 완벽한 엑잘. 하이엔드 = 원소·투사체 +4·치명타 확률 1티어, 마지막 접미는 공격 속도·치명타 피해 1티어로 바꾸는 도박. 밸런스 = 원소·치명타 확률 1~2티어, 투사체 +3~+4, 마지막 접미 랜덤 옵션.',
  {**ROUTE,'pT':{'kr':'원소 피해 추가','en':'Elemental flat','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'cT':{'kr':'치명타 확률','en':'Critical hit chance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'jT':{'kr':'모든 투사체 스킬 레벨','en':'Projectile skills','values':TV({'1':('+4','+4'),'2':('+3~+4','+3–+4')})}},
  {'high':{'v':1,'pT':1,'jT':1,'cT':1},'bal':{'v':2,'pT':2,'jT':2,'cT':2}},
  {'high':K('원소·투사체 +4·치명타 확률 1티어, 마지막 접미 도박','T1 elemental, +4 projectiles, T1 crit chance, last suffix gambled'),'bal':K('원소·치명타 확률 1~2티어 · 투사체 +3~+4 · 마지막 접미 랜덤 옵션','T1–2 elemental and crit chance, +3–+4 projectiles, last suffix random')},tags,nodes,
  [{'id':'L1','nodes':['d2','l1','l2','l3'],'kr':'빛 없이 다시 공개','en':'Lightless reroll'}],
  FIN(('high','bal'),lambda v:[{'tag':'pp','fr':True,'tmax':2,'tmin':2},{'tag':'fl','tmax':1},{'tag':'co','tmax':1 if v=='high' else 2},{'tag':'proj','tmax':1 if v=='high' else 2,'des':True},{'tag':'cc','tmax':1 if v=='high' else 2},{'tag':'last'} if v=='high' else {'side':'s','random':True}]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'fl'},{'has':'ele'},{'has':'proj'},{'has':'cc'}]},('high','bal'))
