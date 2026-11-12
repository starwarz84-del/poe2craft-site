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
# 2026-11-12 영상 전체 화면 대조(작업자, 증거 scratchpad/evidence/diztoh-iceshot-bow-v2/timeline.md). 영상 순서:
#   0:00~0:45 절멸자 활 매직 굴리기(진화·확장·소멸, 0:58 완벽한 확장의 오브) → 0:35 물리 피해 % 2티어(159%) 매직
#   → 0:50 상위 마모의 에센스(레어 + 물리 피해 추가) → 1:10 무작위 훼손(미공개) → 1:13~1:18 신성한 오브로 165% → 분열(셋 중 하나) → 1:28 소멸의 오브로 모두 지움
#   → 1:30~3:52 카오스 오브 반복(물리 피해 추가 1티어) → 4:34 좌측 찬미 + 완벽한 엑잘(공격 원소 피해 %) → 4:44 상위 카오스 오브 + 절사의 징조(말소 없음, 4:48 채팅) → 번개 1티어
#   → 5:05 알두르의 숨결(번개 → 냉기) → 6:05 아스트리드의 창의성 → 7:01 고대 턱뼈(강령술 없음 — 접두가 꽉 차 있음) → 8:20 심연의 메아리 공개
#   → 빗나가면 우측 결정화 + 완벽한 가속의 에센스(9:12) → 우측 결정화 + 심연의 에센스(12:38 징표) → 징표 훼손 → 공개 … 15:05 투사체 +4
#   → 15:12 완벽한 엑잘(징조 없음, 능력치 요구 감소) → 15:30~18:18 절사의 징조(+ 우측 말소) + 상위 카오스 오브로 치명타 확률(3티어 +3.78%)
#     (15:43 인벤토리 상위 카오스 오브 'II' 10+20개, 18:06 12개, 창고 카오스 오브 307개는 5:30과 18:32에 같음 — 일반 카오스는 안 씀)
#   → 18:30 완벽한 엑잘 한 번(민첩, 그대로 둠) → 19:00 물리 룬·신성·타락(벽돌) — 레시피에서 뺌.
# 난이도 5(극한) → 하이엔드만(정책 10장). 하이엔드 = 영상 흐름 + C17(반복 목표 1티어, 마지막 접미가 잡옵이면 공격 속도·치명타 피해·추가 화살 1티어로 바꾸는 도박).
tags={'pp':{'gi':7,'tmax':2},'ppm':{'gi':7,'tmax':2},'fle':{'gi':2},'fl':{'gi':2,'tmax':1},'co':{'gi':4,'tmax':'$pT'},'li':{'gi':6,'tmax':'$pT'},'fi':{'gi':3,'tmax':'$pT'},'hy':{'gi':8,'tmax':'$pT'},
      'ele':{'anyOf':['co','li','fi','hy']},'conv':{'anyOf':['li','fi']},'proj':{'gi':9,'tmax':'$jT'},'cc':{'gi':17,'tmax':'$cT'},'ons':{'gi':55},'mk':{'gi':57},
      'as':{'gi':15,'tmax':1},'cd':{'gi':18,'tmax':1},'sur':{'gi':20,'tmax':1},'last':{'anyOf':['as','cd','sur'],'label':K('공격 속도·치명타 피해 보너스·추가 화살 1티어','T1 attack speed, crit damage bonus or additional arrow')},
      'keepP':{'anyOf':['pp','fl','ele']},'keepS':{'anyOf':['proj','cc']},'keepS3':{'anyOf':['proj','cc','last']}}
PP=it('p','물리 피해 (155—169)% 증가 (분열)','(155—169)% increased Physical Damage (fractured)',['pp'])   # 영상 완성품 = 2티어 분열(165%)
PPM=lambda m='n': it('p','물리 피해 (155—169)% 증가','(155—169)% increased Physical Damage',['ppm'],m)
FLE=it('p','물리 피해 (16—24)~(28—42) 추가 (상위 마모의 에센스)','Adds (16—24) to (28—42) Physical Damage (Greater Essence of Abrasion)',['fle'],'c')
FL=it('p','물리 피해 (26—39)~(44—66) 추가','Adds (26—39) to (44—66) Physical Damage',['fl']); CO=it('p','냉기 피해 (72—81)~(110—123) 추가','Adds (72—81) to (110—123) Cold Damage',['co'])
PJ=it('s','모든 투사체 스킬 레벨 +4','+4 to Level of all Projectile Skills',['proj'],'d'); CC=it('s','치명타 확률 +(4.41—5)%','+(4.41—5)% to Critical Hit Chance',['cc'])
ON=it('s','이 무기로 명중시켜 처치 시 (20—25)%의 확률로 맹공 획득 (완벽한 가속의 에센스)','(20—25)% chance to gain Onslaught on Killing Hits with this Weapon (Perfect Essence of Haste)',['ons'],'c')
MKB=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mk'],'c')
AL=it('r','알두르의 숨결','Breath of Aldur',None,'r'); AS=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
def RB(vis):   # every step re-checks the item — prefixes (RB) → runes → suffixes (RS)
    return ROUTE_([{'if':{'not':{'has':'fl'}},'to':'c1'},
       {'if':{'all':[{'not':{'has':'ele'}},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},
       {'if':{'all':[{'not':{'has':'ele'}},{'whittleSafe':{'tag':'keepP'}}]},'to':'e1w'},   # 영상 4:44: 절사의 징조만(말소 없음) — 가장 낮은 옵션이 지킬 옵션이 아니면
       {'if':{'not':{'has':'ele'}},'to':'e1x'},{'if':{'has':'conv'},'to':'al'},{'to':'r2'}],vis)
def RS(vis):   # after the runes: suffixes only (nothing here touches a prefix)
    sN=lambda n:{'sideLt':{'side':'s','n':n}}
    return ROUTE_([{'if':{'unrevSide':'s'},'to':'d2'},{'if':{'has':'mk'},'to':'l3'},
       {'if':{'all':[{'has':'proj'},sN(2)]},'to':'x1'},
       {'if':{'all':[{'has':'proj'},{'not':{'has':'cc'}},{'whittleSafe':{'tag':'keepS','side':'s'}}]},'to':'x2'},
       {'if':{'all':[{'has':'proj'},{'not':{'has':'cc'}}]},'to':'x2x'},
       {'if':{'all':[{'has':'proj'},sN(3)]},'to':'x3'},
       {'if':{'all':[{'has':'proj'},{'has':'last'}]},'to':'ok'},
       {'if':{'all':[{'has':'proj'},{'whittleSafe':{'tag':'keepS3','side':'s'}}]},'to':'x3w'},
       {'if':{'has':'proj'},'to':'ok'},   # 마지막 접미가 가장 낮은 레벨이 아니면 도박을 멈춤(우측 소멸은 투사체를 지울 수 있음)
       {'if':{'not':sN(2)},'to':'sX'},{'if':{'has':'ons'},'to':'l2'},{'if':sN(1),'to':'d1'},{'to':'l1'}],vis)
M0=[PPM()]; M1=[PPM(),J('s')]; M2=[PPM(),FLE,J('s')]; M3=M2+[UN('x')]; M4=[PP]
W0=[PP,J('x')]; W1=[PP,FL]; W2=[PP,FL,CO]; W3=W2+[AL]; W4=W3+[AS]; W5=W4+[UN('s')]; W6=W4+[PJ]; W7=W4+[ON]; W8=W4+[MKB]; W9=W4+[PJ,J('s')]; W10=W4+[PJ,CC]; W11=W10+[R1('s')]
b0=base('m1',None,K('특출난 절멸자 활 구입 (룬 소켓 3, 아이템 레벨 82)','Buy an exceptional Obliterator Bow (three rune sockets, item level 82)'),[]); b0['id']='b0'; b0.pop('start',None)
nodes=[b0,
 act('m1','prep',[0,1],'transmute','Perfect_Orb_of_Transmutation',K('매직 첫 옵션','First magic option'),None,K('진화','Transmute'),
     [{'if':{'all':[{'has':'ppm'},{'full':'s'}]},'to':'e0','res':'ok'},{'if':{'has':'ppm'},'to':'m3','res':'ok'},{'if':{'full':'p'},'to':'m1x','res':'fail'},{'to':'m2','res':'fail'}],M0,show=['ppm']),
 act('m2','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('매직 접두 옵션','Magic prefix option'),None,K('확장','Augment'),
     [{'if':{'all':[{'has':'ppm'},{'full':'s'}]},'to':'e0','res':'ok'},{'if':{'has':'ppm'},'to':'m3','res':'ok'},{'if':{'full':'p'},'to':'m1x','res':'fail'},{'to':'m2','res':'fail'}],M0,show=['ppm']),
 act('m3','prep',[0,3],'augment','Perfect_Orb_of_Augmentation',K('매직 접미 옵션','Magic suffix option'),[st('s','랜덤 옵션 1개','One random line')],K('확장','Augment'),[{'to':'e0'}],M1),
 {'id':'m1x','kind':'act','group':'prep','pos':[1,2],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('빗나간 접두 지우기','Remove the missed prefix'),'edges':[{'if':{'all':[{'full':'p'},{'not':{'has':'ppm'}}]},'to':'m1x'},{'to':'m2'}]},
 act('e0','prep',[0,4],'essence','Greater_Essence_of_Abrasion',K('레어로 업그레이드 + 물리 피해 추가','Upgrade to rare + flat physical damage'),[st('p','물리 피해 추가 (제작 옵션)','Flat physical damage (crafted)')],K('에센스','Essence'),[{'to':'f1'}],M2,ess='fle'),
 act('f1','prep',[0,5],'desecrate','Preserved_Jawbone',K('분열 확률을 높이기 위해 훼손','Desecrate to raise the fracture odds'),[st(None,'훼손 옵션 1개 (미공개)','One desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f2'}],M3),
 {'id':'fd','kind':'side','group':'prep','pos':[1,5.5],'attach':['f1','f2'],'cur':'Divine_Orb','goal':K('물리 피해 % 165 이상 (선택)','Physical damage % 165 or more (optional)'),'label':K('신성','Divine')},
 act('f2','prep',[0,6],'fracture','Fracturing_Orb',K('분열 (셋 중 하나)','Fracture (one of three)'),[st(None,'물리 피해 % 증가가 분열되면 성공','Success when % physical damage fractures')],K('분열','Fracture'),
     [{'if':{'fractured':'ppm'},'to':'f4','res':'ok'},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another option fractured')}],[PPM('f'),FLE,J('s'),UN('x')],pAll=True),
 {'id':'xj','kind':'exit','group':'prep','pos':[1,6],'simTo':'b0','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another option fractured — new base')},
 {'id':'f4','kind':'cleanup','group':'prep','pos':[0,7],'keep':[],'maxJunk':0,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('분열 옵션만 남기기','Keep only the fractured modifier'),'edges':[{'to':'ms'}],'item':M4},
 mark([0,7.6],'c1',M4),
 act('c1','main',[0,8],'chaos','Chaos_Orb',K('접두 두번째 옵션','Second prefix'),None,K('카오스','Chaos'),RB({'e1':'ok','c1':F}),W1,show=['fl']),
 act('e1','main',[0,9],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     RB({'al':{'res':'ok','hide':True},'r2':'ok','e1w':F,'e1x':F}),W2,show=['co','li','fi','hy'],omens=['Omen_of_Sinistral_Exaltation']),
 act('e1w','main',[1,9],'chaos','Greater_Chaos_Orb',K('접두 잡옵을 다시 (가장 낮은 레벨일 때)','Reroll the junk prefix (while it is the lowest level)'),None,K('카오스','Chaos'),
     RB({'al':'ok','r2':'ok','e1':{'res':'fail','port':'left'},'e1w':F,'e1x':F}),W2,show=['co','li','fi','hy'],omens=['Omen_of_Whittling']),
 annul('e1x',[2,9],RB({'e1':{'res':'ok','port':'top'},'c1':{'res':'fail'}}),omens=('Omen_of_Sinistral_Annulment',),target=K('접두 하나 지우기 (잡옵 또는 물리 피해 추가, 50:50)','Remove one prefix (the junk or the flat physical, 50:50)')),
 act('al','main',[1,10],'rune',None,K('알두르의 숨결 장착','Socket Breath of Aldur'),[st(None,'화염·번개 옵션 → 냉기','Fire and lightning mods → cold')],K('룬','Rune'),[{'to':'r2'}],W3,rune=K('알두르의 숨결','Breath of Aldur')),
 act('r2','main',[0,11],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),RS({'d1':{},'l1':{},'sX':{}}),W4,rune=K('아스트리드의 창의성','Astrid’s Creativity')),
 annul('sX',[1,11],RS({'l1':{},'d1':{},'sX':{}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 줄이기 (2개 이상일 때)','Cut the junk suffixes (two or more)')),
 act('d1','main',[0,12],'desecrate','Ancient_Jawbone',K('접미 첫번째 옵션(훼손)','First suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RS({'d2':{}}),W5),
 act('d2','main',[0,13],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RS({'x1':'ok','l1':F}),W6,want='proj',show=['proj'],omens=['Omen_of_Abyssal_Echoes']),
 act('l1','main',[1,13],'essence','Perfect_Essence_of_Haste',K('접미 옵션을 지우고 맹공','A suffix goes for Onslaught'),[st('s','맹공 획득 (제작 옵션)','Onslaught (crafted)')],K('에센스','Essence'),RS({'l2':{}}),W7,ess='ons',omens=['Omen_of_Dextral_Crystallisation']),
 act('l2','main',[1,14],'essence','Essence_of_the_Abyss',K('맹공을 지우고 심연의 군주의 징표','Onslaught goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),RS({'l3':{}}),W8,ess='mk',mark=True,omens=['Omen_of_Dextral_Crystallisation']),
 act('l3','main',[1,15],'desecrate','Ancient_Jawbone',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RS({'d2':{'port':'right'}}),W5,fromMark=True),
 act('x1','main',[0,16],'exalt','Perfect_Exalted_Orb',K('접미 잡옵','A junk suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'if':{'not':{'whittleSafe':{'tag':'keepS','side':'s'}}},'to':'x2x',**F},{'to':'x2','res':'ok'}],W9),   # 접두가 꽉 차 있어 엑잘은 접미로만
 act('x2','main',[0,17.4],'chaos','Greater_Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),RS({'x3':'ok','x2':F,'x2x':F}),W10,show=['cc'],trim={'side':'s','keep':'keepS'}),
 annul('x2x',[1,17.4],RS({'x2':{'res':'ok'},'x1':{'res':'ok'},'l1':{'res':'fail'}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 하나 지우기 (잡옵이 가장 낮은 레벨이 아닐 때)','Remove one suffix (when the junk is not the lowest level)')),
 act('x3','main',[0,18.8],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),RS({'ok':'ok','x3w':F,'x2x':F}),W11,show=['as','cd','sur']),
 act('x3w','main',[1,18.8],'chaos','Greater_Chaos_Orb',K('마지막 접미를 다시 (가장 낮은 레벨일 때)','Reroll the last suffix (while it is the lowest level)'),None,K('카오스','Chaos'),RS({'ok':'ok','x3w':F,'x2x':F}),W11,show=['as','cd','sur'],trim={'side':'s','keep':'keepS3'}),
 done([0,19.8])]
graph11('diztoh-iceshot-bow-v2','Bows','Obliterator Bow',82,
  'Diztoh 얼음 사격 활(29vO0mMUoME) — 매직 물리 피해 % 2티어 → 상위 마모의 에센스 → 보존된 턱뼈 훼손 → 분열(셋 중 하나) → 소멸의 오브 → 카오스 오브(물리 피해 추가 1티어) → 좌측 찬미 + 완벽한 엑잘(냉기·번개·화염·복합, 빗나가면 절사의 징조 + 상위 카오스 오브) → 번개·화염이면 알두르의 숨결 → 아스트리드의 창의성 → 고대 턱뼈 → 공개(투사체 +4, 빗나가면 우측 결정화 + 완벽한 가속의 에센스 → 심연의 에센스 → 징표 훼손) → 완벽한 엑잘(접미 잡옵) → 절사(+ 우측 말소) + 카오스 오브(치명타 확률) → 완벽한 엑잘. 극한 → 하이엔드만: 원소·투사체 +4·치명타 확률 1티어, 마지막 접미는 공격 속도·치명타 피해·추가 화살 1티어로 바꾸는 도박.',
  {**ROUTE,'pT':{'kr':'원소 피해 추가','en':'Elemental flat','values':TV({'1':('1티어','T1')})},
   'cT':{'kr':'치명타 확률','en':'Critical hit chance','values':TV({'1':('1티어','T1')})},'jT':{'kr':'모든 투사체 스킬 레벨','en':'Projectile skills','values':TV({'1':('+4','+4')})}},
  {'high':{'v':1,'pT':1,'jT':1,'cT':1}},
  {'high':K('원소·투사체 +4·치명타 확률 1티어, 마지막 접미 도박','T1 elemental, +4 projectiles, T1 crit chance, last suffix gambled')},tags,nodes,
  [{'id':'L0','nodes':['m1','m2','m1x'],'kr':'매직 물리 피해 %','en':'Magic % physical'},{'id':'L1','nodes':['d2','l1','l2','l3'],'kr':'빛 없이 다시 공개','en':'Lightless reroll'}],
  FIN(('high',),lambda v:[{'tag':'pp','fr':True,'tmax':2,'tmin':2},{'tag':'fl','tmax':1},{'tag':'co','tmax':1},{'tag':'proj','tmax':1,'des':True},{'tag':'cc','tmax':1},{'tag':'last'}]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'fl'},{'has':'ele'},{'has':'proj'},{'has':'cc'}]},('high',))
_p=f'{H}/diztoh-iceshot-bow-v2.json'; _g=json.load(open(_p))   # 분열 준비를 플로우차트 안에(prep 묶음) — 비용에 베이스·준비가 들어감
_g['start']='b0'
_g['groups']=[{'id':'prep','kr':'베이스템 완성','en':'Finished base','cols':[0,1]},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers','cols':[0,2]}]
json.dump(_g,open(_p,'w'),ensure_ascii=False,indent=1)
