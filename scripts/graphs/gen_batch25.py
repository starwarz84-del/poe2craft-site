# Batch 25 (사용자 2026-11-11: "반지노 작업영상 최신부터 10개, 레시피 등록 + 제작 노하우 흡수")
#   banzino-mirror-staff-v2 — 반지깎는노인 '미러 지팡이 제작 방법'(vT482uJFESs, 0.4 무렵 영상 → 0.5.5 데이터로 응용, 정책 15)
# 영상: 주문 피해 % 1티어 분열 → 빈자리를 모두 채운 채로(이미 붙은 계열은 안 나와 확률이 오름) 카오스 오브로 모든 번개 주문 +7
#   → 절사로 시전 속도 1티어 → 절사로 주문 치명타 1티어(번개 주문 +7 레벨 81·시전 속도 80이라 절사에 안 지워짐)
#   → 접두: 좌측 결정화 + 심연의 에센스(접두 둘 중 하나) → 징표 훼손 → 공개(번개 피해 % 1티어 / 추가 번개 1티어)
#   → 빗나가면 빛의 징조 + 소멸의 오브 → 완벽한 엑잘로 남은 접두 → 하나만 맞으면 절사·말소 카오스로 나머지.
# 2026-11-12 등급 기준 C17(정책 10장): 밸런스는 시전 속도 1~2티어, 훼손 공개(빛의 징조 사용)로 접두 하나 1~2티어, 접미·접두 마지막 옵션은 도박 없이 랜덤 옵션(주문 치명타 절사·남은 접두 절사는 하이엔드만).
# 2026-11-11 영상 대조: 접미 두·세 번째 옵션은 영상대로 절사의 징조만(말소 없이) — 번개 주문 +7(81)·시전 속도(80)·분열·접두 잡옵(80 이상)보다 낮은 접미 잡옵을 절사가 지움. 하이엔드 7,754 → 5,415, 밸런스 4,686 → 3,325 div(pT는 말소 포함 절사 유지 — 치명타 1티어가 레벨 76이라 절사만으로는 접두 잡옵(80)을 못 지워 끝나지 않음).
# 바꾼 점(정책 15): 영상의 지팡이 베이스 제한(전도성 지팡이 = 번개 계열만)은 우리 데이터(클래스 단위 가중치)에 없어 비용이 실제보다 큼(추정).
#   영상의 '마나 최대치를 먼저 공개해 두고 엑잘' 요령은 꿀팁으로만(시뮬은 공개 실패 = 빛의 징조).
# 미러급이라 카오스는 완벽한 카오스 오브(정책 23 ②). 하이엔드 = 모두 1티어, 밸런스 = 주문 치명타·접두 2개 1~2티어(정책 32 — 카오스 오브로 찾는 번개 주문 +7은 1티어, 시전 속도도 1티어: 2티어(레벨 70)면 다음 절사에서 말소의 징조 1/3로 번개 주문 +7이 지워져 오히려 비쌈 — 시뮬 확인).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch22.py').read(); exec(_src[:_src.index('# ---------- 1. 시한')])

c='Staves'; P={'high':{'sT':1,'pT':1,'cT':1,'g':1},'bal':{'sT':2,'pT':2,'cT':2,'g':0}}   # g: 접두·접미 마지막 옵션이 잡옵이면 바꾸는 도박(하이엔드만, 정책 10장 C17)
tags={'spd':{'gi':3,'tmax':1},'l7':{'gi':16,'tmax':1},'cast':{'gi':25,'tmax':'$cT'},'crit':{'gi':26,'tmax':'$sT'},
      'light':{'gi':7,'tmax':'$pT'},'xl':{'gi':34,'tmax':'$pT'},'markP':{'gi':56},
      'pg':{'anyOf':['light','xl']},'keepS':{'anyOf':['l7','cast','crit']}}
SP=itg('p',c,3,['spd'],'f'); L7=itg('s',c,16,['l7']); CA=itg('s',c,25,['cast']); CR=itg('s',c,26,['crit'])
LI=itg('p',c,7,['light']); XL=itg('p',c,34,['xl']); MK=it('p','심연의 군주의 징표','Mark of the Abyssal Lord',['markP'],'c')
I0=[SP,J('p'),J('p'),J('s'),J('s'),J('s')]; I1=[SP,J('p'),J('p'),L7,J('s'),J('s')]; I2=[SP,J('p'),J('p'),L7,CA,J('s')]; I3=[SP,J('p'),J('p'),L7,CA,CR]
I4=[SP,J('p'),MK,L7,CA,CR]; I5=[SP,J('p'),UN('p'),L7,CA,CR]; I6=[SP,J('p'),LI,L7,CA,CR]; I7=[SP,XL,LI,L7,CA,CR]
L1={'if':{'removed':'l7'},'to':'s1','res':'fail','lost':'l7','hide':True}
L2={'if':{'removed':'cast'},'to':'s2','res':'fail','lost':'cast','hide':True}
TWO={'count':{'tag':'pg','min':2}}; ONE={'count':{'tag':'pg','min':1}}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spd','fr':True},{'junk':'p'},{'junk':'p'},{'junk':'s'},{'junk':'s'},{'junk':'s'}]},
            K('주문 피해 % 1티어 분열 전도성 지팡이 (옵션 6개 모두 찬 상태)','Voltaic Staff with fractured T1 spell damage (all six slots filled)'),I0),
 mark([0,0.6],'s1',I0),
 act('s1','main',[0,1],'chaos','Chaos_Orb',K('접미 첫 번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'l7'},'to':'s2','res':'ok'},{'to':'s1','res':'fail'}],I1,show=['l7']),
 act('s2','main',[0,2],'chaos','Perfect_Chaos_Orb',K('접미 두 번째 옵션','Second suffix'),None,K('카오스','Chaos'),
     [L1,{'if':{'all':[{'has':'cast'},{'param':{'g':0}}]},'to':'p1','res':'ok'},{'if':{'has':'cast'},'to':'s3','res':'ok'},{'to':'s2','res':'fail'}],I2,show=['cast'],omens=['Omen_of_Whittling'],skipIf={'has':'cast'},skipTo='s3',over=[{'param':{'g':0},'set':{'skipTo':'p1'}}]),
 act('s3','main',[0,3],'chaos','Perfect_Chaos_Orb',K('접미 세 번째 옵션','Third suffix'),None,K('카오스','Chaos'),
     [L1,L2,{'if':{'all':[{'has':'crit'},TWO]},'to':'ok','res':'ok','hide':True},{'if':{'all':[{'has':'crit'},ONE,{'full':'p'}]},'to':'pT','res':'ok','hide':True},{'if':{'has':'crit'},'to':'p1','res':'ok'},{'to':'s3','res':'fail'}],
     I3,show=['crit'],omens=['Omen_of_Whittling']),
 act('p1','main',[0,4],'essence','Essence_of_the_Abyss',K('접두 잡옵 하나를 징표로','Turn one junk prefix into a mark'),[st('p','심연의 군주의 징표 (제작 옵션)','Mark of the Abyssal Lord (crafted)')],K('에센스','Essence'),
     [L1,L2,{'to':'p2'}],I4,ess='markP',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 act('p2','main',[0,5],'desecrate','Ancient_Jawbone',K('접두 두 번째 옵션(징표 훼손)','Second prefix (desecrate the mark)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p3'}],I5,fromMark=True),
 act('p3','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':TWO,'to':'ok','res':'ok','hide':True},{'if':{'all':[ONE,{'param':{'g':0}}]},'to':'ok','res':'ok'},{'if':ONE,'to':'p5','res':'ok'},{'to':'p4','res':'fail'}],I6,want='pg',show=['light','xl'],omens=['Omen_of_Abyssal_Echoes']),
 {'id':'p4','kind':'act','group':'main','pos':[1,6],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],
  'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('훼손 옵션 제거','Remove the desecrated modifier'),
  'edges':[{'to':'p5','res':'ok','port':'right'}]},
 act('p5','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접두 세 번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':TWO,'to':'ok','res':'ok'},{'if':{'all':[ONE,{'param':{'g':0}}]},'to':'ok','res':'ok'},{'if':ONE,'to':'pT','res':'fail'},{'to':'p1','res':'fail'}],I7,show=['light','xl'],omens=['Omen_of_Sinistral_Exaltation'],skipIf={'full':'p'},skipTo='pT'),
 act('pT','main',[1,7],'chaos','Perfect_Chaos_Orb',K('접두 남은 옵션 찾기','Find the remaining prefix'),None,K('카오스','Chaos'),
     [L1,L2,{'if':{'removed':'crit'},'to':'s3','res':'fail','lost':'crit','hide':True},{'if':TWO,'to':'ok','res':'ok'},{'if':{'not':ONE},'to':'p1','res':'fail','hide':True},{'to':'pT','res':'fail'}],
     None,show=['light','xl'],trim={'side':'p','keep':'pg','keepDes':True}),
 done([0,8])]
g22('banzino-mirror-staff-v2',c,'Voltaic Staff',82,
  '반지깎는노인 미러 지팡이(vT482uJFESs, 0.4 영상 → 0.5.5 응용) — 주문 피해 % 분열(옵션 6개 찬 상태) → 카오스 오브 모든 번개 주문 +7 → 절사 카오스 시전 속도·주문 치명타 → 좌측 결정화 + 심연의 에센스 → 징표 훼손 공개 → 완벽한 엑잘·절사 카오스로 접두 2개.',
  {'sT':{'kr':'주문 치명타','en':'Spell crit','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'pT':{'kr':'번개 피해 %·추가 번개','en':'Lightning % / extra lightning','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'cT':{'kr':'시전 속도','en':'Cast speed','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'g':{'kr':'마지막 옵션이 잡옵일 때','en':'Junk last line','values':TV({'1':('바꾸는 도박','Gamble to replace'),'0':('랜덤 옵션으로 둠','Keep as a random line')})}},P,
  {'high':K('모든 옵션 1티어 (영상)','Every line tier 1 (video)'),'bal':K('시전 속도·훼손 접두 1~2티어, 접미·접두 마지막 옵션은 랜덤 옵션','Cast speed and the desecrated prefix at T1–2; the last suffix and prefix are random lines')},
  tags,nodes,[{'id':'L1','nodes':['p1','p2','p3','p4','p5'],'kr':'접두 징표 훼손','en':'Prefix mark desecration'}],
  FIN(VHB,lambda v:[{'tag':'spd','fr':True},{'tag':'light','tmax':1},{'tag':'xl','tmax':1},{'tag':'l7','tmax':1},{'tag':'cast','tmax':1},{'tag':'crit','tmax':1}] if v=='high' else
      [{'tag':'spd','fr':True},{'side':'p','label':K('번개 피해 % 또는 추가 번개 1~2티어 (훼손)','Lightning % or extra lightning T1–2 (desecrated)')},{'side':'p','random':True},{'tag':'l7','tmax':1},{'tag':'cast','tmax':2},{'side':'s','random':True}]),
  {'quality':20,'sockets':0},{'any':[{'all':[{'param':{'g':1}},{'has':'spd'},{'has':'l7'},{'has':'cast'},{'has':'crit'},TWO]},{'all':[{'param':{'g':0}},{'has':'spd'},{'has':'l7'},{'has':'cast'},ONE]}]},VHB)

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_banzino_mirror_staff.py'): _sp.run([_sy.executable, f'{H}/gen_banzino_mirror_staff.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 이 파일의 결과를 덮어씀
