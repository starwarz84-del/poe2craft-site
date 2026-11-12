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
# 2026-11-12 W3 영상 전체 재대조(새 플로우차트 기준: 성공 회차 한 줄, 실패는 짧은 되돌림만). 근거 scratchpad review/W3-iceshot-bow/timeline.md · frames/.
# 화면 순서: 0:00 완벽한 진화의 오브 → 0:30 소멸·확장으로 매직 굴리기 → 0:38 물리 피해 % 2티어(159%) 매직 → 0:46 확장(처치 시 생명력) → 0:50~0:54 상위 마모의 에센스(레어 + 물리 피해 추가)
#   → 1:05 보존된 턱뼈(툴팁) → 1:08 미공개 훼손(옵션 4개) → 1:14~1:17 신성한 오브 158 → 165% → 1:21 분열의 오브(툴팁) → 1:22 165% 분열 → 1:26~1:31 소멸로 분열 + 옵션 1개
#   → 1:30~3:53 카오스 오브(창고 일반 카오스 578 → 510 → 433 → 307개) → 물리 피해 추가 1티어 → 4:34 좌측 찬미 + 완벽한 엑잘(공격 원소 피해 % — 빗나감)
#   → 4:46 절사의 징조 + 상위 카오스 오브(창고 'II' 2 → 1개, 일반 307 그대로, 4:48 '절사의 징조 소모') → 번개 1티어 → 5:26 알두르의 숨결 → 5:33 냉기 1티어
#   → 6:10 아스트리드의 창의성 → 7:00 고대 턱뼈 훼손(접미, 강령술 없음) → 8:20 공개 + 심연의 메아리(8:32 소모 메시지) → 빗나가면 우측 결정화 + 완벽한 가속의 에센스(9:12 맹공)
#   → 우측 결정화 + 심연의 에센스(10:05 징표) → 징표 훼손 → 공개 … 14:50 투사체 +4 → 15:12 완벽한 엑잘(징조 없음) → 15:18 능력치 요구 35% 감소
#   → 15:43~18:15 절사의 징조(+ 가장 낮은 옵션이 접두면 우측 말소의 징조, 16:40 소모 메시지) + 상위 카오스 오브(인벤토리 'II' 10·20개) → 치명타 확률 3티어(+3.78%)
#   → 18:28 완벽한 엑잘 한 번(민첩, 그대로 둠) → 19:25 완벽한 철의 룬·신성한 오브·타락(망가짐) — 레시피에서 뺌.
# 난이도 5(극한, difficulty.py) → 하이엔드만(정책 10장). 하이엔드 = 반복 목표 1티어(C17①). 마지막 접미 도박(C17②)은 넣지 않음: 치명타 확률 1티어(레벨 73)가 접미에서 가장 낮아
#   절사로 마지막 접미만 다시 굴릴 수 없고, 말소 단독은 투사체 +4·치명타 확률을 1/3씩 지움(시뮬 확인) — 영상처럼 랜덤으로 둠.
tags={'pp':{'gi':7,'tmax':2},'fle':{'gi':39},'fl':{'gi':2,'tmax':1},
      'co':{'gi':4,'tmax':1},'li':{'gi':6,'tmax':1},'fi':{'gi':3,'tmax':1},
      'ele':{'anyOf':['co','li','fi'],'label':K('냉기 피해 추가 1티어 (알두르의 숨결)','T1 added cold damage (Breath of Aldur)')},
      'proj':{'gi':9,'tmax':1},'cc':{'gi':17,'tmax':1},'ons':{'gi':55},'mk':{'gi':57},
      'as':{'gi':15,'tmax':1},'cd':{'gi':18,'tmax':1},'sur':{'gi':20,'tmax':1},
      'last':{'anyOf':['as','cd','sur'],'label':K('공격 속도·치명타 피해 보너스·추가 화살 1티어','T1 attack speed, crit damage bonus or additional arrow')},
      'keepP':{'anyOf':['pp','fl']},'keepS':{'anyOf':['proj','cc']}}
PPM=lambda m='n': it('p','물리 피해 (155—179)% 증가','(155—179)% increased Physical Damage',['pp'],m)
PP=PPM('f')
FLE=it('p','물리 피해 (16—24)~(28—42) 추가 (상위 마모의 에센스)','Adds (16—24) to (28—42) Physical Damage (Greater Essence of Abrasion)',['fle'],'c')
FL=it('p','물리 피해 (26—39)~(44—66) 추가','Adds (26—39) to (44—66) Physical Damage',['fl'])
LI=it('p','번개 피해 (1—12)~(202—234) 추가','Adds (1—12) to (202—234) Lightning Damage',['li'])
CO=it('p','냉기 피해 (72—81)~(110—123) 추가','Adds (72—81) to (110—123) Cold Damage',['co'])
PJ=it('s','모든 투사체 스킬 레벨 +4','+4 to Level of all Projectile Skills',['proj'],'d')
CC=it('s','치명타 확률 +(4.41—5)%','+(4.41—5)% to Critical Hit Chance',['cc'])
ON=it('s','이 무기로 명중시켜 처치 시 (20—25)%의 확률로 맹공 획득 (완벽한 가속의 에센스)','(20—25)% chance to gain Onslaught on Killing Hits with this Weapon (Perfect Essence of Haste)',['ons'],'c')
MKB=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mk'],'c')
AL=it('r','알두르의 숨결','Breath of Aldur',None,'r'); AS=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
M0=[PPM()]; M1=[PPM(),J('s')]; M2=[PPM(),FLE,J('s')]; M3=M2+[UN('s')]; M4=[PP,J('x')]
W1=[PP,FL]; W1j=[PP,FL,J('p')]; W2=[PP,FL,LI]; W3=[PP,FL,CO,AL]; W4=W3+[AS]; W5=W4+[UN('s')]; W6=W4+[PJ]; W7=W4+[ON]; W8=W4+[MKB]; W9=W4+[PJ,J('s')]; W10=W4+[PJ,CC]; W11=W10+[R1('s')]
L_=lambda kr,en: {'label':K(kr,en)}
F={'res':'fail'}
b0=base('m1',None,K('특출난 절멸자 활 구입 (아이템 레벨 82, 룬 소켓 3)','Buy an exceptional Obliterator Bow (item level 82, three rune sockets)'),[]); b0['id']='b0'; b0.pop('start',None)
nodes=[b0,
 # 매직 굴리기(0:00~0:38): 완벽한 진화 → 접두가 물리 피해 %가 아니면 소멸 → 완벽한 확장 … (L0으로 접음)
 act('m1','prep',[0,1],'transmute','Perfect_Orb_of_Transmutation',K('매직 물리 피해 % 1~2티어','Magic % physical damage T1–2'),None,K('진화','Transmute'),
     [{'if':{'all':[{'has':'pp'},{'full':'s'}]},'to':'e0','res':'ok'},{'if':{'has':'pp'},'to':'m3','res':'ok'},{'if':{'full':'p'},'to':'m1x','res':'fail'},{'to':'m2','res':'fail'}],M0,show=['pp']),
 act('m2','prep',[1,1],'augment','Perfect_Orb_of_Augmentation',K('매직 접두 옵션','Magic prefix option'),None,K('확장','Augment'),
     [{'if':{'all':[{'has':'pp'},{'full':'s'}]},'to':'e0','res':'ok'},{'if':{'has':'pp'},'to':'m3','res':'ok'},{'if':{'full':'p'},'to':'m1x','res':'fail'},{'to':'m2','res':'fail'}],M0,show=['pp']),
 {'id':'m1x','kind':'act','group':'prep','pos':[1,2],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('빗나간 접두 지우기','Remove the missed prefix'),'edges':[{'if':{'all':[{'full':'p'},{'not':{'has':'pp'}}]},'to':'m1x'},{'to':'m2'}]},
 act('m3','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('매직 접미 옵션','Magic suffix option'),[st('s','잡옵 1개','One junk line')],K('확장','Augment'),[{'to':'e0'}],M1),   # 0:46 처치 시 생명력
 act('e0','prep',[0,3],'essence','Greater_Essence_of_Abrasion',K('레어로 업그레이드 + 물리 피해 추가','Upgrade to rare + flat physical damage'),[st('p','물리 피해 추가 (제작 옵션)','Flat physical damage (crafted)')],K('에센스','Essence'),[{'to':'f1'}],M2,ess='fle'),   # 0:50 툴팁, 0:54 레어
 act('f1','prep',[0,4],'desecrate','Preserved_Jawbone',K('네번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),[st(None,'훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],K('훼손','Desecrate'),[{'to':'f2'}],M3),   # 1:05 툴팁, 1:08 옵션 4개
 {'id':'fd','kind':'side','group':'prep','pos':[1,4.5],'attach':['f1','f2'],'cur':'Divine_Orb','goal':K('물리 피해 % 165 이상, 선택·비용 미포함','Physical damage % 165+, optional, not costed'),'label':K('신성','Divine')},   # 1:14 158 → 1:17 165
 act('f2','prep',[0,5],'fracture','Fracturing_Orb',K('분열 (셋 중 하나)','Fracture (one of three)'),[st(None,'물리 피해 % 증가가 분열되면 성공','Success when % physical damage fractures')],K('분열','Fracture'),
     [{'if':{'fractured':'pp'},'to':'f4','res':'ok',**L_('물리 피해 % 분열','% physical fractured')},{'to':'xj','res':'fail','dash':True,**L_('다른 옵션 분열','Another line fractured')}],[PPM('f'),FLE,J('s'),UN('s')],pAll=True),   # 1:21 툴팁, 1:22 분열 색
 {'id':'xj','kind':'exit','group':'prep','pos':[1,5],'simTo':'b0','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),
  'note':K('물리 피해 %가 아닌 옵션이 분열되면 이 활은 다른 용도로 두고 새 베이스로 처음부터','Another line fractured: set this bow aside and start on a new base')},
 {'id':'f4','kind':'cleanup','group':'prep','pos':[0,6],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':M4},   # 1:26 툴팁, 1:27 훼손 지워짐, 1:31 분열 + 민첩
 mark([0,6.6],'c1',M4),
 act('c1','main',[0,7],'chaos','Chaos_Orb',K('접두 물리 피해 추가 1티어','T1 flat physical prefix'),None,K('카오스','Chaos'),
     [{'if':{'all':[{'has':'fl'},{'has':'ele'},{'full':'p'}]},'to':'al','res':'ok','hide':True},
      {'if':{'all':[{'has':'fl'},{'sideLt':{'side':'p','n':3}},{'sideLt':{'side':'s','n':1}}]},'to':'e1','res':'ok'},
      {'if':{'all':[{'has':'fl'},{'full':'p'}]},'to':'e1w','res':'ok','hide':True},
      {'if':{'has':'fl'},'to':'e1s','res':'ok','hide':True},
      {'to':'c1','res':'fail'}],W1,show=['fl']),   # 3:53 물리 피해 추가 1티어(37~44), 창고 일반 카오스 오브 578 → 307개
 act('e1','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접두 원소 피해 추가 1티어','T1 added elemental damage prefix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'ele'},'to':'al','res':'ok'},{'to':'e1w',**F,**L_('빗나감 — 절사','Miss: Whittling')}],W1j,show=['co','li','fi'],omens=['Omen_of_Sinistral_Exaltation']),   # 4:34 공격 원소 피해 %(빗나감), 4:35 좌측 찬미 소모
 act('e1w','main',[1,8],'chaos','Greater_Chaos_Orb',K('접두 잡옵을 다시','Reroll the junk prefix'),None,K('카오스','Chaos'),
     [{'if':{'all':[{'has':'ele'},{'has':'fl'}]},'to':'al','res':'ok',**L_('원소 피해 추가 1티어','T1 added elemental')},
      {'if':{'not':{'has':'fl'}},'to':'c1',**F,**L_('물리 피해 추가가 지워짐 — 카오스부터','Flat physical gone: back to Chaos')},
      {'if':{'sideLt':{'side':'p','n':3}},'to':'e1s',**F,**L_('새 옵션이 접미로','The new line went to a suffix')},
      {'to':'e1w',**F}],W2,show=['co','li','fi'],trim={'side':'p','keep':'keepP'}),
 annul('e1s',[1,8.5],[{'if':{'not':{'sideLt':{'side':'s','n':1}}},'to':'e1s'},{'to':'e1',**L_('다시 엑잘','Exalt again')}],omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 지우기','Remove the junk suffix')),   # 4:46 상위 카오스(II) 2 → 1개, 4:48 절사의 징조 소모 → 번개 1티어
 act('al','main',[0,9],'rune',None,K('알두르의 숨결 장착','Socket Breath of Aldur'),[st(None,'화염·번개 옵션 → 같은 티어 냉기','Fire and lightning mods → same-tier cold')],K('룬','Rune'),[{'to':'r2'}],W3,rune=K('알두르의 숨결','Breath of Aldur')),   # 5:14 툴팁, 5:26 장착, 5:33 냉기 1티어
 act('r2','main',[0,10],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':'d1'}],W4,rune=K('아스트리드의 창의성','Astrid’s Creativity')),   # 6:02 툴팁, 6:10 '제작 옵션 1개 추가'
 act('d1','main',[0,11],'desecrate','Ancient_Jawbone',K('접미 첫번째 옵션(훼손)','First suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],W5),   # 7:00 미공개 접미(접두가 꽉 차 강령술 없음)
 act('d2','main',[0,12],'reveal',None,K('접미 모든 투사체 스킬 레벨 +4','+4 projectile skills suffix'),None,K('공개','Reveal'),
     [{'if':{'has':'proj'},'to':'x1','res':'ok'},{'to':'l1',**F,**L_('빗나감 — 빛 없이 다시','Miss: lightless reroll')}],W6,want='proj',show=['proj'],omens=['Omen_of_Abyssal_Echoes']),   # 8:20 빗나감, 12:43 +3 넘김, 14:50 +4
 act('l1','main',[1,12],'essence','Perfect_Essence_of_Haste',K('공개된 접미를 지우고 맹공','The revealed suffix goes, Onslaught comes'),[st('s','맹공 획득 (제작 옵션)','Onslaught (crafted)')],K('에센스','Essence'),[{'to':'l2'}],W7,ess='ons',omens=['Omen_of_Dextral_Crystallisation']),   # 9:12
 act('l2','main',[1,13],'essence','Essence_of_the_Abyss',K('맹공을 지우고 심연의 군주의 징표','Onslaught goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),[{'to':'l3'}],W8,ess='mk',mark=True,omens=['Omen_of_Dextral_Crystallisation']),   # 10:05
 act('l3','main',[1,14],'desecrate','Ancient_Jawbone',K('징표 자리 훼손','Desecrate the Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2',**L_('다시 공개','Reveal again')}],W5,fromMark=True),
 act('x1','main',[0,15],'exalt','Perfect_Exalted_Orb',K('접미 잡옵','A junk suffix'),[st('s','랜덤 옵션 1개 (접두가 꽉 차 접미로)','One random line (prefixes are full)')],K('엑잘','Exalt'),
     [{'to':'x2'}],W9,skipIf={'not':{'sideLt':{'side':'s','n':2}}},skipTo='x2',skipHide=True),   # 15:12 툴팁, 15:18 능력치 요구 감소
 act('x2','main',[0,16],'chaos','Greater_Chaos_Orb',K('접미 치명타 확률 1티어','T1 critical hit chance suffix'),None,K('카오스','Chaos'),
     [{'if':{'all':[{'has':'proj'},{'has':'cc'}]},'to':'x3','res':'ok'},{'if':{'not':{'has':'proj'}},'to':'xz',**F,**L_('투사체 +4가 지워짐','+4 projectiles gone')},{'to':'x2',**F}],
     W10,show=['cc'],trim={'side':'s','keep':'keepS'},skipIf={'all':[{'has':'proj'},{'has':'cc'}]},skipTo='x3',skipHide=True),   # 15:43 상위 카오스(II) 10·20개, 16:40 우측 말소 + 절사 소모, 18:15 치명타 확률
 cleanup('xz',[1,16],[],[{'to':'d1',**L_('접미를 비우고 훼손부터','Suffixes cleared: desecrate again')}],K('우측 소멸의 징조로 접미 옵션 모두 지우기','Clear every suffix with Omen of Dextral Annulment'),side='s'),
 act('x3','main',[0,17],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'ok'}],W11,skipIf={'full':'s'},skipTo='ok',skipHide=True),   # 18:28 툴팁, 18:38 민첩(영상은 그대로 둠)
 done([0,18])]
graph11('diztoh-iceshot-bow-v2','Bows','Obliterator Bow',82,
  'Diztoh 얼음 사격 활(29vO0mMUoME, 2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 특출난 절멸자 활 → 완벽한 진화·확장·소멸로 매직 물리 피해 % → 상위 마모의 에센스 → 보존된 턱뼈 훼손 → 분열(1/3, 빗나가면 새 베이스) → 소멸로 분열 + 옵션 1개 → 카오스 오브(물리 피해 추가 1티어) → 좌측 찬미 + 완벽한 엑잘(빗나가면 절사의 징조 + 상위 카오스 오브) → 알두르의 숨결 → 아스트리드의 창의성 → 고대 턱뼈 → 공개(투사체 +4, 빗나가면 우측 결정화 + 완벽한 가속의 에센스 → 심연의 에센스 → 징표 훼손) → 완벽한 엑잘(접미 잡옵) → 절사(+ 우측 말소) + 상위 카오스 오브(치명타 확률) → 완벽한 엑잘. 극한 → 하이엔드만: 반복 목표 1티어, 마지막 접미는 영상처럼 랜덤. 신성한 오브·룬 교체·타락은 뺌.',
  {'t':{'kr':'반복 목표','en':'Loop target','values':TV({'1':('1티어','T1')})}},
  {'high':{'t':1}},
  {'high':K('원소·투사체 +4·치명타 확률 1티어, 마지막 접미 랜덤','T1 elemental, +4 projectiles, T1 crit chance, random last suffix')},tags,nodes,
  [{'id':'L0','nodes':['m1','m2','m1x'],'kr':'매직 물리 피해 %','en':'Magic % physical',
    'fold':True,'goal':K('매직 물리 피해 % 1~2티어','Magic % physical damage T1–2'),
    'steps':[{**K('완벽한 진화의 오브로 매직','Perfect Orb of Transmutation'),'node':'m1'},
             {**K('접두가 빗나가면 소멸의 오브','Missed prefix: Orb of Annulment'),'node':'m1x'},
             {**K('접두가 비면 완벽한 확장의 오브','Empty prefix: Perfect Orb of Augmentation'),'node':'m2'}],
    'item':M0},
   {'id':'L2','nodes':['e1','e1w','e1s'],'kr':'접두 원소 피해 추가','en':'Elemental prefix',
    'fold':True,'goal':K('접두 원소 피해 추가 1티어 (냉기·번개·화염)','T1 added elemental damage prefix (cold, lightning or fire)'),
    'steps':[{**K('좌측 찬미의 징조 + 완벽한 엑잘티드 오브','Omen of Sinistral Exaltation + Perfect Exalted Orb'),'node':'e1'},
             {**K('빗나가면 절사의 징조 + 상위 카오스 오브, 가장 낮은 접두가 물리 피해 추가면 좌측 말소의 징조도','Miss: Omen of Whittling + Greater Chaos Orb, plus Omen of Sinistral Erasure when flat physical is the lowest prefix'),'node':'e1w'},
             {**K('새 옵션이 접미로 가면 우측 소멸의 징조 + 소멸의 오브 뒤 다시 엑잘','New line on a suffix: Omen of Dextral Annulment + Orb of Annulment, then exalt again'),'node':'e1s'}],
    'worst':{**K('물리 피해 추가가 지워지면 카오스 단계부터','Flat physical gone: back to the Chaos step'),'to':'c1'},
    'item':W2},
   {'id':'L1','nodes':['d2','l1','l2','l3'],'kr':'빛 없이 다시 공개','en':'Lightless reroll'}],
  FIN(('high',),lambda v:[{'tag':'pp','fr':True},{'tag':'fl'},{'tag':'ele'},{'tag':'proj','des':True},{'tag':'cc'},{'side':'s','random':True}]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'fl'},{'has':'ele'},{'has':'proj'},{'has':'cc'}]},('high',))
_p=f'{H}/diztoh-iceshot-bow-v2.json'; _g=json.load(open(_p))   # 분열 준비를 플로우차트 안에(prep 묶음) — 비용에 베이스·준비가 들어감
_g['start']='b0'
_g['groups']=[{'id':'prep','kr':'베이스템 완성','en':'Finished base','cols':[0,1]},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers','cols':[0,1]}]
json.dump(_g,open(_p,'w'),ensure_ascii=False,indent=1)
