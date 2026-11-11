# Batch 27 (사용자 2026-11-11: "영문으로 레딧 등에서도 찾아보자") — 레딧은 접속이 막혀 영문 가이드 사이트에서.
#   Unstoppable BTW "How to Craft the Best Body Armours and Sell Them for Big Profit" (youtu.be/swF5mwXmZ0k, 2026-10, 0.5.5 리그)
#   글 정리본 guides-factory.com/guides/poe2-body-armour-crafting-guide — 기록 tools/notes/web-unstoppable-chests.md
#   unstoppable-vile-robe-v2 (에너지 보호막 갑옷) · unstoppable-slipstrike-vest-v2 (회피 갑옷)
# 공통 요령(영상): 아이템 레벨 82 = 저항 1티어(레벨 82)가 접미를 잠가서 절사의 징조가 남은 잡옵만 침, 징조는 마지막 옵션에만,
#   흔한 옵션(생명력·가시)을 훼손 공개로 막아 두고 엑잘, 마지막 접두는 고대 갈비뼈 공개(빛의 징조로 다시).
# 전문가(4) → 하이엔드(1티어) + 밸런스(1~2티어, 정책 30·32).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch22.py').read(); exec(_src[:_src.index('# ---------- 1. 시한')])
TS=TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})
RES3=lambda c: [{'gi':1,'tmax':'$rT'},{'gi':2,'tmax':'$rT'},{'gi':3,'tmax':'$rT'}]

# ---------- 1. Vile Robe (에너지 보호막) ----------
c='Body_Armours_int'
P={'high':{'pT':1,'rT':1},'bal':{'pT':2,'rT':2}}
tags={'pes':{'gi':7,'tmax':1},'esf':{'gi':6,'tmax':'$pT'},'hyb':{'gi':9,'tmax':'$pT'},'sp':{'gi':14,'tmax':'$pT'},
      'gp':{'anyOf':['esf','hyb','sp']},'fr':{'gi':1,'tmax':'$rT'},'cr':{'gi':2,'tmax':'$rT'},'lr':{'gi':3,'tmax':'$rT'},
      'goodS':{'anyOf':['fr','cr','lr']}}
PE=itg('p',c,7,['pes'],'f'); EF=itg('p',c,6,['esf']); EF2=itg('p',c,14,['sp'])
RF=itg('s',c,1,['fr']); RC=itg('s',c,2,['cr']); RL=itg('s',c,3,['lr'])
I0=[PE,J('s')]; I1=[PE,EF]; 
V2=I1+[UN('p')]; V3=I1+[EF2]; V4=V3+[it('s','랜덤 옵션 2개','Two random lines',None,'j')]; V5=V3+[RF,RC,RL]
L1={'if':{'removed':'gp'},'to':'c1','res':'fail','lost':'gp','hide':True}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pes','fr':True},{'junk':'s'}]},K('에너지 보호막 증가 1티어 분열 Vile Robe (아이템 레벨 82, 잡옵 1개)','Vile Robe with fractured T1 % energy shield (item level 82, one junk line)'),I0),
 mark([0,0.6],'c1',I0),
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접두 두번째 옵션','Second prefix'),None,K('카오스','Chaos'),[{'if':{'has':'gp'},'to':'d1','res':'ok'},{'to':'c1','res':'fail'}],I1,show=['esf','hyb','sp']),
 act('d1','main',[0,2],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],V2,omens=['Omen_of_Sinistral_Necromancy']),
 act('d2','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'count':{'tag':'gp','min':2}},'to':'e1','res':'ok'},{'to':'d2x','res':'fail'}],V3,want='gp',show=['esf','hyb','sp'],omens=['Omen_of_Abyssal_Echoes']),
 annul('d2x',[1,3],[{'to':'d1','port':'right'}]),
 act('e1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 옵션 2개','Two suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'e2'}],V4,omens=['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation'],skipIf={'full':'s'},skipTo='t1'),
 act('e2','main',[1,5],'exalt','Perfect_Exalted_Orb',K('빈 접미 채우기','Fill the empty suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'t1'}],None,omens=['Omen_of_Dextral_Exaltation'],skipIf={'full':'s'},skipTo='t1'),
 act('t1','main',[0,6],'chaos','Perfect_Chaos_Orb',K('접미 저항 3개','Three suffix resistances'),None,K('카오스','Chaos'),
     [{'if':{'removed':'gp'},'to':'d1','res':'fail','lost':'gp','hide':True},{'if':{'count':{'tag':'goodS','min':3}},'to':'ok','res':'ok'},{'if':{'not':{'full':'s'}},'to':'e2','res':'fail','hide':True},{'to':'t1','res':'fail'}],V5,show=['fr','cr','lr'],trim={'side':'s','keep':'goodS'},skipIf={'count':{'tag':'goodS','min':3}},skipTo='ok'),
 done([0,7])]
g22('unstoppable-vile-robe-v2',c,'Vile Robe',82,
  'Unstoppable BTW 에너지 보호막 갑옷(swF5mwXmZ0k, 0.5.5 리그) — 에너지 보호막 증가 1티어 분열(영상: 확장의 오브·소멸의 오브 반복 → 완벽한 제왕의 오브 → 훼손으로 4옵션 → 분열) → 카오스 오브로 두번째 접두(에너지 보호막 최대치·복합·정신력) → 좌측 강령술 + 고대 갈비뼈 → 세번째 접두 공개(빛의 징조로 다시, 영상: 접두를 먼저 끝냄) → 우측 찬미 + 상위 찬미 + 완벽한 엑잘로 접미 → 절사의 징조(말소) + 완벽한 카오스 오브로 저항 3개(저항 1티어는 레벨 82라 절사가 잡옵만 침). 영상의 유동체 수치 조정·디바인·바알 주입기는 뺌(정책 33).',
  {'pT':{'kr':'접두 에너지 보호막·정신력','en':'Energy shield / spirit prefixes','values':TS},'rT':{'kr':'저항','en':'Resistances','values':TS}},P,
  {'high':K('모든 옵션 1티어 (영상: 저항 133%)','Every line tier 1 (video: 133% total resistance)'),'bal':K('접두·저항 1~2티어','Prefixes and resistances at T1–2')},
  tags,nodes,[{'id':'L1','nodes':['d1','d2','d2x'],'kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'}],
  FIN(('high','bal'),lambda v:[{'tag':'pes','fr':True},{'tag':'esf','tmax':1 if v=='high' else 2},{'tag':'sp','tmax':1 if v=='high' else 2},{'tag':'fr','tmax':1 if v=='high' else 2},{'tag':'cr','tmax':1 if v=='high' else 2},{'tag':'lr','tmax':1 if v=='high' else 2}]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'pes'},{'count':{'tag':'gp','min':2}},{'count':{'tag':'goodS','min':3}}]},('high','bal'))

# ---------- 2. Slipstrike Vest (회피) ----------
c='Body_Armours_dex'
tags={'pev':{'gi':7,'tmax':1},'evf':{'gi':6,'tmax':'$pT'},'hyb':{'gi':9,'tmax':'$pT'},'gpE':{'anyOf':['evf','hyb']},
      'fr':{'gi':1,'tmax':'$rT'},'cr':{'gi':2,'tmax':'$rT'},'lr':{'gi':3,'tmax':'$rT'},'dfl':{'gi':18,'tmax':'$rT'},
      'goodS':{'anyOf':['fr','cr','lr','dfl']},'blk':{'anyOf':[{'gi':5},{'gi':12}]}}
PV=itg('p',c,7,['pev'],'f'); EV=itg('p',c,6,['evf']); HY=itg('p',c,9,['hyb'])
RF=itg('s',c,1,['fr']); RC=itg('s',c,2,['cr']); DF=itg('s',c,18,['dfl'])
BL=it('p','생명력 최대치 또는 가시 피해 (훼손, 자리 막기)','Max life or thorns (desecrated, slot blocker)',['blk'],'d')
S0=[PV,J('s')]; S1=S0+[it('s','랜덤 옵션 2개','Two random lines',None,'j')]; S2=[PV,RF,RC,DF]; S3=S2+[UN('p')]; S4=S2+[BL]; S5=S4+[EV]
S6=[x for x in S5 if x is not BL]; S7=S6+[UN('p')]; S8=S6+[HY]
LS={'if':{'removed':'pev'},'to':'ok','res':'fail','hide':True}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pev','fr':True},{'junk':'s'}]},K('회피 증가 1티어 분열 Slipstrike Vest (아이템 레벨 82, 잡옵 1개)','Slipstrike Vest with fractured T1 % evasion (item level 82, one junk line)'),S0),
 mark([0,0.6],'e1',S0),
 act('e1','main',[0,1],'exalt','Perfect_Exalted_Orb',K('접미 옵션 2개','Two suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'t1'}],S1,omens=['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation']),
 act('t1','main',[0,2],'chaos','Perfect_Chaos_Orb',K('접미 저항 2개 + 굴절','Two suffix resistances + deflection'),None,K('카오스','Chaos'),
     [{'if':{'all':[{'count':{'tag':'goodS','min':3}},{'junk':{'side':'p','tag':'gpE'}}]},'to':'pc','res':'ok','hide':True},{'if':{'count':{'tag':'goodS','min':3}},'to':'d1','res':'ok'},{'if':{'not':{'full':'s'}},'to':'e2','res':'fail','hide':True},{'to':'t1','res':'fail'}],S2,show=['fr','cr','lr','dfl'],trim={'side':'s','keep':'goodS'}),
 act('e2','main',[1,2],'exalt','Exalted_Orb',K('빈 접미 채우기','Fill the empty suffix'),[st('s','잡옵 (아무 옵션)','Junk (any line)')],K('엑잘','Exalt'),[{'to':'t1','port':'right'}],None,omens=['Omen_of_Dextral_Exaltation'],skipIf={'full':'s'},skipTo='t1'),
 annul('pc',[1,3],[{'if':{'junk':{'side':'p','tag':'gpE'}},'to':'pc','port':'right'},{'to':'d1','res':'ok'}],omens=('Omen_of_Sinistral_Annulment',),target=K('접두 잡옵 지우기','Remove the junk prefix')),
 act('d1','main',[0,3],'desecrate','Ancient_Rib',K('접두 자리 막기(훼손)','Block a prefix slot (desecrate)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],S3,omens=['Omen_of_Sinistral_Necromancy']),
 act('d2','main',[0,4],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'to':'e3'}],S4,want='blk',show=['blk'],omens=['Omen_of_Abyssal_Echoes']),
 act('e3','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'gpE','min':2}},'to':'ok','res':'ok','hide':True},{'if':{'added':'gpE'},'to':'w1','res':'ok'},{'to':'e3x','res':'fail','port':'right'}],S5,show=['evf','hyb'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('e3x',[1,5],[{'if':{'des':True},'to':'e3','port':'right'},{'to':'d1','res':'fail','hide':True}],omens=('Omen_of_Sinistral_Annulment',),target=K('빗나간 접두 지우기','Remove the missed prefix')),
 annul('w1',[0,6],[{'to':'d3'}],target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecrated line')),
 act('d3','main',[0,7],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d4'}],S7,omens=['Omen_of_Sinistral_Necromancy']),
 act('d4','main',[0,8],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'count':{'tag':'gpE','min':2}},'to':'ok','res':'ok'},{'to':'d4x','res':'fail'}],S8,want='gpE',show=['evf','hyb'],omens=['Omen_of_Abyssal_Echoes']),
 annul('d4x',[1,8],[{'to':'d3','port':'right'}]),
 done([0,9])]
g22('unstoppable-slipstrike-vest-v2',c,'Slipstrike Vest',82,
  'Unstoppable BTW 회피 갑옷(swF5mwXmZ0k, 0.5.5 리그) — 회피 증가 1티어 분열 → 우측 찬미 + 상위 찬미 + 완벽한 엑잘로 접미 → 절사의 징조(말소) + 완벽한 카오스 오브로 저항 2개 + 굴절(영상은 일찍 절사) → 좌측 강령술 + 고대 갈비뼈로 생명력·가시 같은 흔한 옵션을 공개해 접두 자리 막기 → 좌측 찬미 + 완벽한 엑잘(회피 최대치·회피 복합, 빗나가면 좌측 소멸의 징조 + 소멸의 오브) → 빛의 징조로 막기 제거 → 고대 갈비뼈 → 마지막 접두 공개(빛의 징조로 다시). 영상의 좌측 결정화 + 심연의 에센스로 접두를 뒤집는 반복은 좌측 소멸의 징조로 단순화(가정). 디바인·바알 주입기·바알 오브는 뺌(정책 33).',
  {'pT':{'kr':'접두 회피','en':'Evasion prefixes','values':TS},'rT':{'kr':'저항·굴절','en':'Resistances / deflection','values':TS}},P,
  {'high':K('모든 옵션 1티어 (영상: 회피 3,646)','Every line tier 1 (video: 3,646 evasion)'),'bal':K('접두·저항·굴절 1~2티어 (영상: 회피 복합 2티어도 괜찮음)','Prefixes, resistances and deflection at T1–2 (video: a T2 hybrid is fine)')},
  tags,nodes,[{'id':'L1','nodes':['e3','e3x'],'kr':'접두 두번째 옵션','en':'Second prefix'},{'id':'L2','nodes':['d3','d4','d4x'],'kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'}],
  FIN(('high','bal'),lambda v:[{'tag':'pev','fr':True},{'tag':'evf','tmax':1 if v=='high' else 2},{'tag':'hyb','tmax':1 if v=='high' else 2},{'tag':'fr','tmax':1 if v=='high' else 2},{'tag':'cr','tmax':1 if v=='high' else 2},{'tag':'dfl','tmax':1 if v=='high' else 2}]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'pev'},{'count':{'tag':'gpE','min':2}},{'count':{'tag':'goodS','min':3}}]},('high','bal'))
