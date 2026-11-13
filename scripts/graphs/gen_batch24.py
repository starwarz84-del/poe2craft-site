# Batch 24 (사용자 2026-11-11: "플로우차트가 아직 없는 레시피가 있어? 그럼 만들어야지")
#   breach-ring-phys-v2 — 균열 반지 물리 플랫 분열 + 원소 플랫(사이트 운영자 제작 방식, 영상 없음). 원본 레시피는 recipes_batch4.py.
# 원본에서 꼬였던 곳(최대 퀄리티·합금 순서)을 그래프로 풀었음:
#   절사의 징조 + 카오스 오브로 최대 퀄리티(레벨 1)를 지울 때 새 옵션이 접미로 가면 접미가 꽉 차 재빠른 합금(접미)이 접미 옵션을 지움
#   → 접미 잡옵을 절사·말소(정책 23 ④, trim — 말소 1/2 도박으로 모든 원소 저항·화염 저항이 지워지면 새 베이스) + 상위 카오스 오브로 돌려 접미 자리를 비운 뒤 → 좌측 찬미 + 완벽한 엑잘로 접두를 채우고
#   → 좌측 결정화 + 재빠른 합금(접두 둘 중 하나가 지워지고 공격 속도는 접미).
# 접두 마무리: 남은 접두가 공격 시 원소 피해면 빈자리에 고대 빗장뼈 훼손 → 공개, 아니면 완벽한 엑잘로 채우고 절사·말소 + 완벽한 카오스 오브로 원소 피해 하나를 찾은 뒤
#   좌측 강령술 + 고대 빗장뼈(꽉 찬 접두: 원소 피해와 잡옵 중 하나가 지워짐 1/2) → 공개. 원소 피해 2개가 아니면 빛의 징조 + 소멸의 오브로 훼손 옵션을 지우고 다시.
# 난이도 3 → 밸런스 + 에센셜(정책 30). 밸런스 = 원소 피해 2개 1~3티어 · 화염 저항 1~2티어 다시 도전,
# 에센셜 = 남은 접두가 무엇이든 빈자리에 훼손 한 번, 공개 결과 그대로 · 화염 저항 1~3티어 빗나가도 그대로(정책 32: 카오스 오브로 찾는 모든 원소 저항은 두 등급 모두 1티어).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch22.py').read(); exec(_src[:_src.index('# ---------- 1. 시한')])

c='Rings'; P={'bal':{'eT':3,'fT':2,'v':1},'ess':{'eT':4,'fT':3,'v':2}}
tags={'phys':{'gi':13,'tmax':1},'allres':{'gi':7,'tmax':1},'fres':{'gi':4,'tmax':'$fT'},'maxq':{'gi':71},'alloy':{'gi':73},
      'fire':{'gi':15,'tmax':'$eT'},'cold':{'gi':17,'tmax':'$eT'},'light':{'gi':19,'tmax':'$eT'},
      'ele':{'anyOf':['fire','cold','light']},'keepS':{'anyOf':['allres','fres','alloy']},'keepP':{'anyOf':['fire','cold','light']}}
V1={'param':{'v':1}}
PH=itg('p',c,13,['phys'],'f'); AR=itg('s',c,7,['allres']); FR=itg('s',c,4,['fres'],ti=1)
MQ=itg('p',c,71,['maxq'],'c',suffix=('균열의 에센스','Essence of the Breach')); AL=itg('s',c,73,['alloy'],'c',suffix=('재빠른 합금','Swift Alloy'))
FI=itg('p',c,15,['fire'],ti=2); CO=itg('p',c,17,['cold'],ti=2); FId=itg('p',c,15,['fire'],'d',ti=2)
I0=[PH,J('s')]; I1=[PH,AR]; I2=[PH,J('p'),AR]; I3=[PH,MQ,AR]; I4=I3+[FR]; I5=[PH,R1('p'),AR,FR]; I6=[PH,R1('p'),R1('p'),AR,FR]; I7=[PH,FI,AR,FR,AL]; I8=I7+[UN('p')]; I9=[PH,FI,CO,AR,FR,AL]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'phys','fr':True},{'junk':'s'}]},K('공격 시 물리 피해 1티어 분열 + 잡옵 1개 균열 반지 구입','Buy a Breach Ring with fractured T1 physical attack damage + one junk line'),I0),
 mark([0,0.6],'b2',I0),
 act('b2','main',[0,1],'chaos','Chaos_Orb',K('접미 첫 번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'allres'},'to':'b3','res':'ok'},{'to':'b2','res':'fail'}],I1,show=['allres']),
 act('b3','main',[0,2],'exalt','Exalted_Orb',K('에센스가 지울 접두','The prefix for the essence to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'b4'}],I2,omens=['Omen_of_Sinistral_Exaltation']),
 act('b4','main',[0,3],'essence','Essence_of_the_Breach',K('접두 잡옵을 최대 퀄리티로','Swap the junk prefix for maximum quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% maximum quality (crafted)')],K('에센스','Essence'),[{'to':'b5'}],I3,ess='maxq',omens=['Omen_of_Sinistral_Crystallisation']),
 act('b5','main',[0,4],'quality','Xophs_Catalyst',K('화염 퀄리티 60%','Fire quality 60%'),[st(None,'조프의 기폭제 60개','60 Xoph’s Catalysts')],K('퀄리티','Quality'),[{'to':'b6'}],I3,count=60),
 act('b6','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 두 번째 옵션','Second suffix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'fres'},'to':'b7','res':'ok'},{'if':V1,'to':'b6x','res':'fail'},{'to':'b7','res':'fail'}],I4,show=['fres'],omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],cat='fres'),
 {'id':'b6x','kind':'act','group':'main','pos':[1,5],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment'],
  'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('접미 하나 지우기','Remove one suffix'),
  'edges':[{'if':{'removed':'allres'},'to':'h1','res':'fail','lost':'allres','port':'right'},{'to':'b5','res':'ok','port':'right'}]},
 act('b7','main',[0,6],'quality','Reaver_Catalyst',K('공격 퀄리티 60%','Attack quality 60%'),[st(None,'강탈자 기폭제 60개','60 Reaver Catalysts')],K('퀄리티','Quality'),[{'to':'b8'}],I4,count=60),
 act('b8','main',[0,7],'chaos','Chaos_Orb',K('최대 퀄리티 지우기','Remove maximum quality'),[st(None,'최대 퀄리티(레벨이 가장 낮음)가 다른 옵션으로 바뀜','Maximum quality (lowest level) turns into another line')],K('카오스','Chaos'),
     [{'if':{'removed':'allres'},'to':'h1','res':'fail','lost':'allres','hide':True},{'if':{'all':[V1,{'removed':'fres'}]},'to':'h1','res':'fail','lost':'fres','hide':True},{'if':{'has':'maxq'},'to':'b8','res':'fail','hide':True},{'if':{'sideLt':{'side':'s','n':3}},'to':'b9a','res':'ok'},{'to':'b8s','res':'fail'}],I5,omens=['Omen_of_Whittling']),
 act('b8s','main',[1,7],'chaos','Greater_Chaos_Orb',K('접미 자리 비우기','Free a suffix slot'),[st('s','접미 잡옵을 다른 옵션으로 (접두로 가면 성공)','The junk suffix into another line (done when it goes to the prefixes)')],K('카오스','Chaos'),
     [{'if':{'removed':'allres'},'to':'h1','res':'fail','lost':'allres','hide':True},{'if':{'all':[V1,{'removed':'fres'}]},'to':'h1','res':'fail','lost':'fres','hide':True},{'if':{'sideLt':{'side':'s','n':3}},'to':'b9a','res':'ok'},{'to':'b8s','res':'fail'}],None,trim={'side':'s','keep':'keepS'}),
 act('b9a','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접두 두 번째·세 번째 옵션 채우기','Fill the second and third prefixes'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'b9'}],I6,omens=['Omen_of_Sinistral_Exaltation'],skipIf={'full':'p'},skipTo='b9'),
 act('b9','main',[0,9],'essence','Swift_Alloy',K('접미 세 번째 옵션','Third suffix'),[st('s','공격 속도 (7—9)% 증가 (제작 옵션) — 접두 둘 중 하나가 지워짐','(7—9)% increased Attack Speed (crafted) — one of the two prefixes goes')],K('합금','Alloy'),
     [{'if':{'has':'ele'},'to':'d1','res':'ok'},{'if':V1,'to':'e1','res':'fail'},{'to':'d1','res':'fail'}],I7,ess='alloy',omens=['Omen_of_Sinistral_Crystallisation']),
 act('e1','main',[1,9],'exalt','Perfect_Exalted_Orb',K('접두 세 번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'all':[V1,{'has':'ele'}]},'to':'d1','res':'ok'},{'if':V1,'to':'e2','res':'fail'},{'to':'ok','res':'fail'}],None,show=['fire','cold','light'],omens=['Omen_of_Sinistral_Exaltation']),
 act('e2','main',[2,9],'chaos','Perfect_Chaos_Orb',K('접두 원소 피해 찾기','Find an elemental attack prefix'),None,K('카오스','Chaos'),
     [{'if':{'has':'ele'},'to':'d1','res':'ok'},{'to':'e2','res':'fail'}],None,show=['fire','cold','light'],trim={'side':'p','keep':'keepP'}),
 act('d1','main',[0,10],'desecrate','Ancient_Collarbone',K('접두 원소 피해(훼손)','Elemental attack prefix (desecrated)'),[st('p','훼손 옵션(미공개) — 접두가 꽉 차 있으면 하나가 지워짐','Desecrated modifier (unrevealed) — a full prefix side loses one line')],K('훼손','Desecrate'),[{'to':'d2'}],I8,omens=['Omen_of_Sinistral_Necromancy']),
 act('d2','main',[0,11],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'count':{'tag':'ele','min':2}},'to':'ok','res':'ok'},{'if':V1,'to':'d2x','res':'fail'},{'to':'ok','res':'fail'}],I9,want='ele',show=['fire','cold','light'],omens=['Omen_of_Abyssal_Echoes']),
 {'id':'d2x','kind':'act','group':'main','pos':[1,11],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],
  'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('훼손 옵션 제거','Remove the desecrated modifier'),
  'edges':[{'if':{'has':'ele'},'to':'d1','res':'ok','port':'right'},{'to':'e1','res':'fail','port':'right'}]},
 done([0,12])]
g22('breach-ring-phys-v2',c,'Breach Ring',82,
  '균열 반지 물리 플랫 분열 + 원소 플랫(사이트 운영자 제작 방식) — 카오스 오브(모든 원소 저항) → 좌측 결정화 + 균열의 에센스 → 조프의 기폭제 60% → 촉진 + 우측 찬미 + 완벽한 엑잘(화염 저항) → 강탈자 기폭제 60% → 절사 + 카오스 오브(최대 퀄리티 지우기, 접미로 가면 접미 잡옵 절사·말소 카오스로 자리 비움) → 좌측 찬미 + 완벽한 엑잘 → 좌측 결정화 + 재빠른 합금 → 원소 피해 접두 훼손 공개.',
  {'eT':{'kr':'공격 시 원소 피해','en':'Elemental attack damage','values':TV({'3':('1~3티어','T1–3'),'4':('1~4티어','T1–4')})},
   'fT':{'kr':'화염 저항','en':'Fire res','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},
   'v':{'kr':'진행','en':'Route','values':TV({'1':('원소 피해 2개까지','Until two elemental lines'),'2':('결과 그대로','As it comes')})}},P,
  {'bal':K('공격 시 원소 피해 2개(1~3티어), 화염 저항 1~2티어','Two elemental attack lines (T1–3), fire res T1–2'),'ess':K('접두 훼손 한 번, 공개 결과 그대로, 화염 저항 빗나가도 그대로','One prefix desecration kept as revealed, fire res kept on a miss')},
  tags,nodes,[{'id':'L1','nodes':['d1','d2','d2x'],'kr':'원소 피해 훼손 공개','en':'Elemental reveal'}],
  FIN(VBE,lambda v:[{'tag':'phys','fr':True},{'tag':'fire','tmax':3,'alt':K('또는 냉기·번개','or cold / lightning')} if v=='bal' else {'side':'p','random':True},{'tag':'cold','tmax':3,'alt':K('또는 화염·번개','or fire / lightning')} if v=='bal' else {'side':'p','random':True},
                    {'tag':'allres','tmax':1},{'tag':'fres','tmax':2 if v=='bal' else 3},{'tag':'alloy'}]),
  {'quality':60,'sockets':0},{'all':[{'has':'phys'},{'has':'allres'},{'has':'alloy'},{'any':[{'count':{'tag':'ele','min':2}},{'param':{'v':2}}]},{'any':[{'has':'fres'},{'param':{'v':2}}]}]},VBE)

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_breach_ring_phys.py'): _sp.run([_sy.executable, f'{H}/gen_breach_ring_phys.py'], check=True)   # 2026-11-13 G6: 새 기준 전용 생성기가 덮어씀
