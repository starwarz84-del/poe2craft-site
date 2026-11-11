# Batch 20 (사용자 2026-11-10: 남은 2가지) — 미러 활 · 주문 +6 부재 목걸이 → High-end (video) + Balance. Videos rechecked 2026-11-10 (transcripts).
#   mirror-bow-video-v2 (반지깎는노인 J0LF3MRssh0), absent-amulet-spell6-v2 (반지깎는노인 Yi1u0LhJztI)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch19.py').read(); exec(_src[:_src.index('# ---------- 1. 반지깎는노인')])

# ---------- 1. 미러 활 (J0LF3MRssh0, 사용자 단계 목록 기반) ----------
# 영상 대조 2026-11-11(사용자: 영상과 다시 확인): 물리 피해 % 1티어는 분열 뒤 카오스 오브로 찾음(15:00~16:00, 빈자리 3개, 약 4,000개 예상) → 시작에서 빼고 단계로.
#   타협(공격 원소 피해로 막기, 영상이 실제로 쓴 길 19:15~21:30)은 정확도가 절사로 들어오면 물리 % 를 잃는 위험이 커 시뮬 평균이 높음 → 숨긴 비교용 전략.
# 시작: 치명타 확률 1티어 분열(퀄리티 30%) → 카오스 오브(물리 피해 % 1티어) → 보존된 턱뼈 + 좌측 강령술(미공개 접두 훼손)
# → 접두 훼손 공개(자리 막기: 공격 원소 피해 1티어 또는 정확도 1티어, 빛의 징조 + 소멸의 오브 → 고대 턱뼈 + 좌측 강령술로 다시)
# → 좌측 찬미 + 완벽한 엑잘(물리 % + 정확도 1티어 또는 물리 피해 추가 1티어, 빗나가면 절사 카오스)
# → 완벽한 엑잘(접미 잡옵) → 우측 말소의 징조 + 카오스 오브(투사체 +4 또는 화살 초과 1티어) → 완벽한 엑잘 → 세를의 승리(접미 +1) → 완벽한 엑잘
# → 절사의 징조 + 상위 카오스 오브(남은 투사체/화살 + 치명타 피해 보너스 1티어) → 빛의 징조로 막기 제거 → 고대 턱뼈 → 공개(남은 물리 접두 1티어, 빛의 징조로 다시).
# 영상의 우측 결정화 + 심연의 에센스로 징표를 만드는 재시도 구간은 훼손이 붙은 아이템엔 심연의 에센스를 못 써서(MazBro 갑옷 영상) 고대 턱뼈 다시 훼손으로 바꿈.
tags={'crit':{'gi':17,'tmax':1},'pp':{'gi':7,'tmax':1},'hyb':{'gi':8,'tmax':1},'flat':{'gi':2,'tmax':1},'eatk':{'gi':21,'tmax':1},'acc':{'gi':16,'tmax':1},
      'proj':{'gi':9,'tmax':1},'arr':{'gi':20,'tmax':1},'cdm':{'gi':18,'tmax':1},
      'blk':{'anyOf':['eatk','acc']},'p3':{'anyOf':['hyb','flat']},'sx':{'anyOf':['proj','arr']},'sg':{'anyOf':['proj','arr','cdm']},
      'keepP':{'anyOf':['pp','p3']},'keepT':{'anyOf':['pp','p3','blk']},'keepS':{'anyOf':['sx','cdm']}}
CR=it('s','치명타 확률 +(4.41—5)% (분열)','+(4.41—5)% to Critical Hit Chance (fractured)',['crit']); PP=it('p','물리 피해 (170—179)% 증가','(170—179)% increased Physical Damage',['pp'])
BK=it('p','정확도 +(551—650) (훼손, 자리 막기)','+(551—650) to Accuracy Rating (desecrated, blocker)',['acc'],'d')
HY=it('p','물리 피해 (75—79)% 증가 + 정확도 +(175—200)','(75—79)% increased Physical Damage + (175—200) to Accuracy Rating',['hyb'])
FL=it('p','물리 피해 (26—39)~(44—66) 추가','Adds (26—39) to (44—66) Physical Damage',['flat'],'d')
PJ=it('s','모든 투사체 스킬 레벨 +4','+4 to Level of all Projectile Skills',['proj']); AR=it('s','화살 하나를 추가로 발사할 초과 확률 +(175—200)%','+(175—200)% Surpassing chance to fire an additional Arrow',['arr'])
CD=it('s','치명타 피해 보너스 +(23—25)%','+(23—25)% to Critical Damage Bonus',['cdm']); SE=it('r','세를의 승리','Serle’s Triumph',None,'r')
def RB(vis):   # every step re-checks the item
    fs={'all':[{'has':'cdm'},{'count':{'tag':'sx','min':2}}]}; s3={'count':{'tag':'sg','min':2}}
    return ROUTE_([{'if':{'not':{'has':'pp'}},'to':'c0'},{'if':JK('p','keepP'),'to':'w1'},{'if':{'all':[fs,{'has':'p3'},{'not':{'des':True}},{'unrevSide':'p'}]},'to':'f3'},{'if':{'unrevSide':'p'},'to':'rv'},
       {'if':{'all':[{'not':{'des':True}},{'not':{'has':'p3'}},{'sideLt':{'side':'p','n':3}}]},'to':'d1'},
       {'if':{'all':[{'not':{'has':'p3'}},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},{'if':{'not':{'has':'p3'}},'to':'w1'},
       {'if':{'all':[{'not':{'has':'sx'}},{'sideLt':{'side':'s','n':2}}]},'to':'s1'},{'if':{'not':{'has':'sx'}},'to':'s2'},
       {'if':{'all':[{'not':s3},{'sideLt':{'side':'s','n':3}}]},'to':'s3'},{'if':{'not':s3},'to':'w2'},
       {'if':{'all':[{'full':'s'},{'sideLt':{'side':'s','n':4}}]},'to':'r1'},
       {'if':{'all':[{'not':fs},{'sideLt':{'side':'s','n':4}}]},'to':'s4'},{'if':{'not':fs},'to':'w3'},
       {'if':JK('p','keepP'),'to':'w1'},{'if':{'des':True},'to':'f1'},{'if':{'count':{'tag':'p3','min':2}},'to':'ok'},{'to':'f2'}],vis)
I0=[PP,UN('p'),CR]; I1=[PP,BK,CR]; I2=[PP,BK,HY,CR]; I3=I2+[J('s')]; I4=I2+[PJ]; I5=I4+[J('s')]; I6=I4+[AR]; I7=I6+[SE]; I8=I6+[J('s'),SE]; I9=I6+[CD,SE]
I10=[PP,HY,UN('p'),CR,PJ,AR,CD,SE]; I11=[PP,HY,FL,CR,PJ,AR,CD,SE]
IS=[J('p'),J('p'),CR]; IP=[PP,J('p'),CR]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'crit','fr':True},{'junk':'p'},{'junk':'p'}]},K('치명타 확률 1티어 분열 활 (퀄리티 30%, 옵션 2개 + 빈자리 3개)','Bow with fractured T1 crit chance (30% quality, two lines and three open slots)'),IS),
 mark([0,0.4],'c00',IS),
 act('c00','main',[0,0.6],'chaos','Chaos_Orb',K('접두 첫번째 옵션','First prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pp'},'to':'d0','res':'ok'},{'to':'c00','res':'fail'}],IP,show=['pp']),
 act('d0','main',[0,0.8],'desecrate','Preserved_Jawbone',K('자리 막기 훼손','Desecrate for a blocker'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'rv'}],I0,omens=['Omen_of_Sinistral_Necromancy']),
 act('rv','main',[0,1],'reveal',None,K('자리 막기 옵션 확인','Reveal the blocker'),None,K('공개','Reveal'),
     [{'if':{'added':'$bw'},'to':'e1','res':'ok'},{'to':'rvx',**F}],I1,want='$bw',show=['acc','eatk'],omens=['Omen_of_Abyssal_Echoes'],showIf=[{'param':{'bw':'acc'},'show':['acc']}]),
 annul('rvx',[1,1],RB({'d1':{'port':'right'}})),
 act('d1','main',[2,1],'desecrate','Ancient_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RB({'rv':{}}),I0,omens=['Omen_of_Sinistral_Necromancy']),
 act('e1','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),RB({'s1':'ok','w1':F}),I2,show=['hyb','flat'],omens=['Omen_of_Sinistral_Exaltation']),
 act('w1','main',[1,2],'chaos','Perfect_Chaos_Orb',K('접두 세번째 옵션','Third prefix'),None,K('카오스','Chaos'),RB({'s1':'ok','e1':{'res':'fail'},'c0':F}),I2,show=['hyb','flat'],trim={'side':'p','keep':'keepP','keepDes':True}),
 act('c0','main',[2,2],'chaos','Perfect_Chaos_Orb',K('접두 첫번째 옵션','First prefix'),None,K('카오스','Chaos'),[e if e.get('res') or e['to']=='c0' else dict(e,res='ok') for e in RB({'e1':{'res':'ok'}})],I2,show=['pp'],omens=['Omen_of_Sinistral_Erasure']),
 act('s1','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접미 잡옵','A junk suffix'),[st('s','잡옵','Junk')],K('엑잘','Exalt'),RB({'s2':{}}),I3),
 act('s2','main',[0,4],'chaos','Perfect_Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),RB({'s3':'ok'}),I4,show=['proj','arr'],omens=['Omen_of_Dextral_Erasure']),
 act('s3','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 잡옵','A junk suffix'),[st('s','잡옵','Junk')],K('엑잘','Exalt'),RB({'w2':{}}),I5),
 act('w2','main',[0,6],'chaos','Perfect_Chaos_Orb',K('접미 세번째 옵션','Third suffix'),None,K('카오스','Chaos'),RB({'r1':'ok'}),I6,show=['proj','arr','cdm'],trim={'side':'s','keep':'keepS'}),
 act('r1','main',[0,7],'rune',None,K('세를의 승리 장착 (접미 +1)','Socket Serle’s Triumph (+1 suffix)'),[st(None,'접미 옵션 4개','Four suffixes')],K('룬','Rune'),[{'to':'s4'}],I7,slots={'s':1},rune=K('세를의 승리','Serle’s Triumph')),
 act('s4','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접미 잡옵','A junk suffix'),[st('s','잡옵','Junk')],K('엑잘','Exalt'),RB({'w3':{}}),I8),
 act('w3','main',[0,9],'chaos','Perfect_Chaos_Orb',K('접미 네번째 옵션','Fourth suffix'),None,K('카오스','Chaos'),RB({'f1':'ok'}),I9,show=['proj','arr','cdm'],trim={'side':'s','keep':'keepS'}),
 annul('f1',[0,10],RB({'f2':{}}),target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),
 act('f2','main',[0,11],'desecrate','Ancient_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f3'}],I10),
 act('f3','main',[0,12],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'p3'},'to':'ok','res':'ok'},{'to':'f3x',**F}],I11,want='p3',show=['flat','hyb'],omens=['Omen_of_Abyssal_Echoes']),
 annul('f3x',[1,12],RB({'f2':{'port':'right'}})),
 done([0,13])]
nodes[0]['start']['quality']=30
graph11('mirror-bow-video-v2','Bows','Warmonger Bow',82,
  '반지깎는노인 미러 활(J0LF3MRssh0, 사용자 단계 목록) — 치명타 확률 분열 + 물리 피해 % 1티어 + 미공개 접두 훼손 → 자리 막기 공개(정확도 1티어 — 막아 두면 카오스 오브에 정확도가 안 나와 물리 피해 %보다 낮은 잡옵을 절사로 안전하게 지움, 타협 = 정확도 또는 공격 원소 피해 1티어) → 좌측 찬미 + 완벽한 엑잘(물리 % + 정확도 또는 물리 피해 추가 1티어, 빗나가면 절사 카오스) → 접미 잡옵 + 우측 말소 + 완벽한 카오스 오브(투사체 +4 또는 화살 초과) → 접미 잡옵 + 절사 카오스(세 번째 접미) → 세를의 승리 → 접미 잡옵 + 절사 카오스(네 번째 접미) → 빛의 징조로 막기 제거 → 고대 턱뼈 → 남은 물리 접두 공개.',
  {'pT':{'kr':'목표 티어','en':'Target tier','values':TV({'1':('1티어','T1')})},'bw':{'kr':'자리 막기','en':'Blocker','values':TV({'acc':('정확도 1티어','T1 accuracy'),'blk':('정확도 또는 공격 원소 피해 1티어 (타협)','T1 accuracy or attack elemental (settle)')})}},
  {'high':{'pT':1,'bw':'acc'}},
  {'high':K('영상·사용자 방식: 정확도 1티어로 자리 막기 → 절사로 확정 제작','Video/user method: block with T1 accuracy, then whittle safely')},tags,nodes,
  [{'id':'L1','nodes':['f2','f3','f3x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['rv','rvx','d1'],'kr':'자리 막기','en':'Block'}],
  FIN(('high',),lambda v:[{'tag':'pp'},{'tag':'hyb'},{'tag':'flat','des':True},{'tag':'crit','fr':True},{'tag':'proj'},{'tag':'arr'},{'tag':'cdm'}]),
  {'quality':30,'sockets':3},{'all':[{'has':'pp'},{'count':{'tag':'p3','min':2}},{'count':{'tag':'sx','min':2}},{'has':'cdm'}]},('high',))
_g=json.load(open(f'{H}/mirror-bow-video-v2.json')); _g['strategies'].append({'id':'high-settle','params':{'pT':1,'bw':'blk'},'hidden':True}); json.dump(_g,open(f'{H}/mirror-bow-video-v2.json','w'),ensure_ascii=False,indent=1)

# ---------- 2. 반지깎는노인 주문 +6 부재 목걸이 (Yi1u0LhJztI) ----------
# 시작: 정신력 +50 분열 + 잡옵(시전 퀄리티 48%) → 카오스 오브(모든 주문 스킬 +3) → 좌측 찬미 + 엑잘(접두 잡옵) → 균열의 에센스(최대 퀄리티, 접두가 꽉 차 있어 징조 없음)
# → 히네코라의 머리카락 + 바알 촉진시키는 주입기로 50% → 좌측 강령술 + 보존된 빗장뼈(최대 퀄리티 자리를 날림) → 빛의 징조 + 소멸의 오브 → 우측 강령술 + 보존된 빗장뼈(훼손을 접미로)
# → 좌측 찬미 + 상위 엑잘(마나 최대치 1티어, 빗나가면 좌측 소멸의 징조 + 소멸의 오브) → 시전 속도 공개(빛의 징조로 다시). 성유·유동체·신성한 오브·축성은 레시피 하이엔드에만.
tags={'spirit':{'gi':28,'tmax':1},'spell':{'gi':17,'tmax':1},'mq':{'gi':81},'mana':{'gi':11,'tmax':'$pT'},'cs':{'gi':32,'tmax':'$pT'}}
SP=it('p','정신력 +(47—50) (분열)','+(47—50) to Spirit (fractured)',['spirit']); SL=it('s','모든 주문 스킬 레벨 +3','+3 to Level of all Spell Skills',['spell'])
MQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% to Maximum Quality (Essence of the Breach)',['mq'],'c'); MA=it('p','마나 최대치 +(180—189)','+(180—189) to maximum Mana',['mana'])
CS=it('s','시전 속도 (25—28)% 증가','(25—28)% increased Cast Speed',['cs'],'d')
def RA(vis):
    return ROUTE_([{'if':{'not':{'has':'spell'}},'to':'k1'},{'if':{'has':'mq'},'to':'m1'},{'if':{'unrevSide':'p'},'to':'m1x'},
       {'if':{'all':[{'not':{'des':True}},{'not':{'unrev':True}},{'sideLt':{'side':'s','n':2}}]},'to':'m1b'},
       {'if':{'all':[{'not':{'has':'mana'}},{'sideLt':{'side':'p','n':2}}]},'to':'m2'},{'if':{'not':{'has':'mana'}},'to':'m2x'},
       {'if':{'all':[{'not':{'des':True}},{'not':{'unrev':True}}]},'to':'m1b'},{'if':{'unrevSide':'s'},'to':'c1'},{'if':{'has':'cs'},'to':'ok'},{'to':'c1x'}],vis)
A0=[SP,J('s')]; A1=[SP,SL]; A2=[SP,J('p'),SL]; A3=[SP,MQ,SL]; A4=[SP,UN('p'),SL]; A5=[SP,SL]; A6=[SP,SL,UN('s')]; A7=[SP,MA,SL,UN('s')]; A8=[SP,MA,SL,CS]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'s'}]},K('정신력 +50 분열 + 잡옵 1개 (시전 퀄리티 48%)','Fractured +50 Spirit + one junk line (48% caster quality)'),A0),
 mark([0,0.6],'k1',A0),
 act('k1','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'spell'},'to':'q1','res':'ok'},{'to':'k1','res':'fail'}],A1,show=['spell']),
 act('q1','main',[0,2],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','잡옵','Junk')],K('엑잘','Exalt'),[{'to':'q2'}],A2,omens=['Omen_of_Sinistral_Exaltation']),
 act('q2','main',[0,3],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티 +20%','The junk goes for +20% Maximum Quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% to Maximum Quality (crafted)')],K('에센스','Essence'),[{'to':'q3'}],A3,ess='mq'),
 act('q3','main',[0,4],'quality','Vaal_Catalysing_Infuser',K('퀄리티 50%','Quality to 50%'),[st(None,'히네코라의 머리카락으로 미리 보고 50%','Preview with Hinekora’s Lock, then 50%')],K('퀄리티','Quality'),[{'to':'m1'}],A3,count=2),
 act('m1','main',[0,5],'desecrate','Preserved_Collarbone',K('접두 두번째 옵션(훼손)','Second prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RA({'m1x':{}}),A4,omens=['Omen_of_Sinistral_Necromancy']),
 annul('m1x',[0,6],RA({'m1b':{}}),target=K('접두 훼손 옵션 제거','Remove the prefix desecration')),
 act('m1b','main',[0,7],'desecrate','Preserved_Collarbone',K('접미 두번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RA({'m2':{}}),A6,omens=['Omen_of_Dextral_Necromancy']),
 act('m2','main',[0,8],'exalt','Greater_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),RA({'c1':'ok','m2x':F}),A7,show=['mana'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('m2x',[1,8],RA({'m2':{'res':'ok','port':'right'}}),omens=('Omen_of_Sinistral_Annulment',),target=K('접두 잡옵 지우기','Remove the junk prefix')),
 act('c1','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RA({'ok':'ok','c1x':F}),A8,want='cs',show=['cs']),
 annul('c1x',[1,9],RA({'m1b':{'port':'right'}})),
 done([0,10])]
nodes[0]['start']['quality']=48
graph11('absent-amulet-spell6-v2','Amulets','Absent Amulet',82,
  '반지깎는노인 주문 +6 부재 목걸이(Yi1u0LhJztI) — 정신력 +50 분열 + 잡옵(시전 퀄리티 48%) → 카오스 오브(모든 주문 스킬 +3) → 좌측 찬미 + 엑잘(접두 잡옵) → 균열의 에센스 → 히네코라의 머리카락 + 바알 촉진시키는 주입기로 50% → 좌측 강령술 + 보존된 빗장뼈(최대 퀄리티 자리) → 빛의 징조로 지우고 우측 강령술 + 보존된 빗장뼈(접미) → 좌측 찬미 + 상위 엑잘(마나 최대치, 빗나가면 좌측 소멸의 징조) → 시전 속도 공개(빛의 징조로 다시). 성유·유동체·신성한 오브·축성은 레시피 하이엔드에만.',
  {'pT':{'kr':'목표 티어','en':'Target tier','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,
  {'high':K('영상: 마나 최대치·시전 속도 1티어','Video: T1 maximum Mana and cast speed'),'bal':K('마나 최대치·시전 속도 1~2티어','T1–2 maximum Mana and cast speed')},tags,nodes,
  [{'id':'L1','nodes':['m1b','c1','c1x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','fr':True},{'tag':'mana','tmax':1 if v=='high' else 2},{'tag':'spell'},{'tag':'cs','tmax':1 if v=='high' else 2,'des':True}]),
  {'quality':50,'sockets':0},{'all':[{'has':'spell'},{'has':'mana'},{'has':'cs'}]},('high','bal'))
