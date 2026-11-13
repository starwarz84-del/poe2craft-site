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
 act('c1','main',[0,2],'chaos','Chaos_Orb',K('접두 첫 번째 옵션','First prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pp'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],G2,show=SHP),
 act('e1','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 두 번째·세 번째 옵션','Second and third prefixes'),None,K('엑잘','Exalt'),RG({'s1':'ok','e1x':F}),G3,show=SHP+SHT,omens=['Omen_of_Greater_Exaltation','Omen_of_Sinistral_Exaltation']),
 annul('e1x',[1,3],RG({'e1':{'res':'ok','port':'right'},'c1':{'res':'fail'}}),omens=(),target=K('접두 잡옵 지우기','Remove a junk prefix')),
 act('s1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두 번째·세 번째 옵션','Second and third suffixes'),None,K('엑잘','Exalt'),RG({'a1':'ok','mA':F}),G4,show=['cr'],omens=['Omen_of_Greater_Exaltation']),
 act('mA','main',[1,4],'essence','Essence_of_the_Abyss',K('잡옵을 지우고 심연의 군주의 징표','The junk goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),RG({'mB':{}}),GM,ess='mkS',mark=True,omens=['Omen_of_Dextral_Crystallisation']),
 act('mB','main',[2,4],'desecrate','Ancient_Rib',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RG({'mL':{}}),GM,fromMark=True),
 annul('mL',[2,5],RG({'s1':{},'mA':{}})),
 act('a1','main',[0,6],'essence','Expansive_Alloy',K('잡옵을 지우고 잔류물을 (35—50)% 더 먼 곳에서 획득 가능','The junk goes for Remnants collected (35—50)% further away'),[st('s','잔류물을 (35—50)% 더 먼 곳에서 획득 가능 (제작 옵션)','Remnants can be collected from (35—50)% further away (crafted)')],K('합금','Alloy'),RG({'d1':'ok','sR':F}),G5,ess='rem',omens=['Omen_of_Dextral_Crystallisation']),
 annul('sR',[1,6],RG({'s1':{},'mA':{},'d1':{}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 옵션 지우기','Remove a suffix')),
 act('d1','main',[0,7],'desecrate','Ancient_Rib',K('접미 네 번째 옵션(훼손)','Fourth suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],G6),
 act('d2','main',[0,8],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'pie'},'to':'ok','res':'ok'},{'if':V1,'to':'d2x',**F},{'to':'ok','res':'fail'}],G7,want='pie',show=['pie']),
 LIGHTX('d2x',[1,8],'d1'),
 done([0,9])]
graph11('sl-proj7-gloves-v2','Gloves_int','Sirenscale Gloves',80,
  'SL 투사체 7옵션 장갑(XMYJh3CnXuY) — 콜르의 사냥 · 투사체 +2 분열 + 잡옵 → 세를의 승리 → 카오스 오브(투사체 피해·속도) → 상위 찬미 + 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브) → 상위 찬미 + 완벽한 엑잘(치명타 확률, 잡옵 2개면 우측 결정화 + 심연의 에센스 → 고대 갈비뼈 → 빛의 징조) → 우측 결정화 + 팽창하는 합금(1/2) → 고대 갈비뼈 → 관통 공개. 하이엔드 = 영상, 밸런스 = 세 번째 접두 1~2티어 · 관통 공개 결과 그대로.',
  {**ROUTE,'pT':{'kr':'접두 세 번째 옵션','en':'Third prefix','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,
  {'high':K('영상: 세 번째 접두 1티어, 관통은 빛의 징조로 다시','Video: T1 third prefix, Light retries pierce'),'bal':K('세 번째 접두 1~2티어, 관통 공개 결과 그대로','T1–2 third prefix, keep the reveal')},tags,nodes,
  [{'id':'L1','nodes':['d1','d2','d2x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['mA','mB','mL'],'kr':'잡옵 정리','en':'Clear junk'}],
  FIN(('high','bal'),lambda v:[{'tag':'ps','tmax':1},{'tag':'pd','tmax':1},{'tag':'mf','tmax':1 if v=='high' else 2},{'tag':'proj','fr':True},{'tag':'cr'},{'tag':'rem','ess':True},{'tag':'pie','des':True} if v=='high' else {'side':'s','random':True}]),
  {'quality':25,'sockets':2},{'all':[{'count':{'tag':'pp','min':2}},{'has':'third'},{'has':'cr'},{'has':'rem'}]},('high','bal'),xsub=["Kolr's Hunt"],xroll=True)

# ---------- 2. Diztoh 얼음 사격 데드아이 활 (29vO0mMUoME) ----------
# 2026-11-13 D1: 전용 생성기 gen_diztoh_iceshot_bow.py로 옮김(하이엔드·밸런스)
import subprocess as _sp0, sys as _sy0; _sp0.run([_sy0.executable, f'{H}/gen_diztoh_iceshot_bow.py'], check=True)

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_sl_proj7_gloves.py'): _sp.run([_sy.executable, f'{H}/gen_sl_proj7_gloves.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 이 파일의 결과를 덮어씀
