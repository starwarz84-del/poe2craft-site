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
TS=TV({'1':('1티어','T1'),'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})
RES3=lambda c: [{'gi':1,'tmax':'$rT'},{'gi':2,'tmax':'$rT'},{'gi':3,'tmax':'$rT'}]

# ---------- 1. Vile Robe (에너지 보호막) ----------
# 영상 대조(2026-11-11, swF5mwXmZ0k 5:45~24:15): 분열 뒤 소멸로 옵션 2개만 → 카오스로 저항(11:15) → 우측 찬미 + 엑잘로 접미(12:00)
#   → 저항 2개 + 잡옵이면 비싼 징조 대신 소멸의 오브(12:30, "징조는 마지막 한 옵션에만") → 생명력·가시를 우물에서 막고 엑잘로 접두(14:45~15:45)
#   → 빛의 징조로 막기 제거(16:00) → 고대 갈비뼈 공개로 마지막 접두, 낮으면 빛의 징조 + 소멸로 다시(16:15~18:15)
#   → 마지막 접미 잡옵은 절사의 징조 + 카오스(레벨 82 저항이 접미를 잠가서 2~4번, 18:45~19:45). "저항 3티어라도 괜찮다"(22:00)
c='Body_Armours_int'
P={'high':{'pT':1,'rT':1,'last':'res'},'bal':{'pT':2,'rT':1,'last':'any'}}   # 2026-11-12 C17: 밸런스 접두(엑잘·훼손 반복으로 찾음) 1~2티어, 저항은 카오스·엑잘 + 소멸의 오브(싼 반복)라 모든 등급 1티어
tags={'pes':{'gi':7,'tmax':1},'esf':{'gi':6,'tmax':'$pT'},'hyb':{'gi':9,'tmax':'$pT'},'sp':{'gi':14,'tmax':'$pT'},
      'gp':{'anyOf':['esf','hyb','sp']},'fr':{'gi':1,'tmax':'$rT'},'cr':{'gi':2,'tmax':'$rT'},'lr':{'gi':3,'tmax':'$rT'},
      'goodS':{'anyOf':['fr','cr','lr']},'blk':{'anyOf':[{'gi':5},{'gi':12}]},'mkP':{'gi':44}}
PE=itg('p',c,7,['pes'],'f'); EF=itg('p',c,6,['esf']); EF2=itg('p',c,14,['sp'])
RF=itg('s',c,1,['fr']); RC=itg('s',c,2,['cr']); RL=itg('s',c,3,['lr'])
GSv=it('s','저항 1개','One resistance',['goodS'],'n')
I0=[PE,J('s')]; I1=[PE,GSv]; I2=[PE,RF,RC]; I3=I2+[EF]; I4=I3+[UN('p')]; I5=I3+[EF2]; I6=I5+[RL]
G2={'count':{'tag':'goodS','min':2}}; G3={'count':{'tag':'goodS','min':3}}; PJ={'not':{'sideLt':{'side':'p','n':2}}}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pes','fr':True},{'junk':'s'}]},K('에너지 보호막 증가 1티어 분열 Vile Robe (아이템 레벨 82, 분열 + 잡옵 1개만 남김)','Vile Robe with fractured T1 % energy shield (item level 82, fracture + one junk line)'),I0),
 mark([0,0.6],'c1',I0),
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'goodS'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],I1,show=['fr','cr','lr']),
 act('e1','main',[0,2],'exalt','Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),
     [{'if':{'all':[G2,PJ]},'to':'cx','res':'ok','label':K('접두 잡옵 있음','Junk prefix there')},{'if':G2,'to':'e3','res':'ok'},{'if':{'full':'s'},'to':'ax','res':'fail'},{'to':'e1','res':'fail'}],I2,show=['fr','cr','lr'],omens=['Omen_of_Dextral_Exaltation']),
 annul('ax',[1,2],[{'if':{'has':'goodS'},'to':'e1','res':'ok'},{'to':'c1','res':'fail','label':K('저항이 지워짐','Resistance removed')}],omens=(),target=K('잡옵 지우기 (저항이 지워질 수도 있음)','Remove a junk line (a resistance may go)')),
 act('e3','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'all':[{'added':'gp'},{'has':'blk'}]},'to':'w1','res':'ok'},{'if':{'added':'gp'},'to':'d3','res':'ok'},{'to':'cx','res':'fail'}],I3,show=['esf','hyb','sp'],omens=['Omen_of_Sinistral_Exaltation']),
 act('cx','main',[1,4],'essence','Essence_of_the_Abyss',K('빗나간 접두를 징표로','The missed prefix goes for the Mark'),[st('p','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),
     [{'if':{'has':'blk'},'to':'w0','label':K('막기가 남음','Blocker still there')},{'to':'db'}],None,ess='mkP',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 annul('w0',[2,4],[{'to':'db'}],target=K('남은 막기 훼손 옵션 제거 (훼손 옵션은 하나만)','Remove the old blocker (one desecrated line per item)')),
 act('db','main',[1,5],'desecrate','Ancient_Rib',K('징표 훼손','Desecrate the Mark'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'rb'}],None,fromMark=True),
 act('rb','main',[1,6],'reveal',None,K('생명력·가시로 자리 막기','Block with life or thorns'),None,K('공개','Reveal'),
     [{'if':{'full':'p'},'to':'cx','res':'fail','port':'right'},{'to':'e3','res':'ok'}],None,want='blk',show=['blk'],omens=['Omen_of_Abyssal_Echoes']),
 annul('w1',[0,5],[{'to':'d3'}],target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecrated line')),
 act('d3','main',[0,6],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d4'}],I4,omens=['Omen_of_Sinistral_Necromancy']),
 act('d4','main',[0,7],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'all':[{'count':{'tag':'gp','min':2}},{'any':[G3,{'all':[{'param':{'last':'any'}},{'full':'s'}]}]}]},'to':'ok','res':'ok'},{'if':{'count':{'tag':'gp','min':2}},'to':'f1','res':'ok'},{'to':'d4x','res':'fail'}],I5,want='gp',show=['esf','hyb','sp'],omens=['Omen_of_Abyssal_Echoes']),
 annul('d4x',[1,7],[{'to':'d3','port':'right'}]),
 act('f1','main',[0,8],'exalt','Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),[{'if':{'any':[G3,{'param':{'last':'any'}}]},'to':'ok','res':'ok'},{'to':'t1','res':'fail'}],I6,show=['fr','cr','lr'],omens=['Omen_of_Dextral_Exaltation'],skipIf={'full':'s'},skipTo='t1',skipHide=True),
 act('t1','main',[0,9],'chaos','Perfect_Chaos_Orb',K('마지막 접미 잡옵 바꾸기','Reroll the last junk suffix'),None,K('카오스','Chaos'),
     [{'if':G3,'to':'ok','res':'ok'},{'if':{'not':{'full':'s'}},'to':'f1','res':'fail','label':K('새 옵션이 접두로','New line went to a prefix')},{'to':'t1','res':'fail'}],I6,show=['fr','cr','lr'],omens=['Omen_of_Whittling','Omen_of_Dextral_Erasure']),
 done([0,10])]
g22('unstoppable-vile-robe-v2',c,'Vile Robe',82,
  'Unstoppable BTW 에너지 보호막 갑옷(swF5mwXmZ0k 5:45~24:15, 영상 대조 2026-11-11) — 에너지 보호막 증가 1티어 분열에 옵션 1개만 남김 → 카오스 오브로 저항 → 우측 찬미 + 엑잘티드 오브로 두번째 저항(꽉 차면 소멸의 오브, 영상 12:30 비싼 징조는 마지막 한 옵션에만) → 좌측 찬미 + 완벽한 엑잘로 접두, 빗나가면 좌측 결정화의 징조 + 심연의 에센스 → 고대 갈비뼈 → 생명력·가시로 자리 막기 → 빛의 징조로 막기 제거 → 고대 갈비뼈 공개로 마지막 접두(빛의 징조로 다시) → 우측 찬미 + 엑잘로 마지막 접미, 잡옵이면 절사의 징조 + 우측 말소의 징조 + 완벽한 카오스 오브(영상 21:00 “접미만 노리는 징조 두 개”, 레벨 82 저항이 접미를 잠금 18:45). 디바인·바알 오브는 뺌(정책 33).',
  {'pT':{'kr':'접두 에너지 보호막·정신력','en':'Energy shield / spirit prefixes','values':TS},'rT':{'kr':'저항','en':'Resistances','values':TS},'last':{'kr':'마지막 접미','en':'Last suffix','values':{'res':{'kr':'세번째 저항','en':'Third resistance'},'any':{'kr':'랜덤 옵션','en':'Random modifier'}}}},P,
  {'high':K('모든 옵션 1티어, 마지막 저항은 절사 + 우측 말소 카오스 반복 (영상: 저항 133%)','Every line tier 1, the last resistance by Whittling + Dextral Erasure Chaos (video: 133% total resistance)'),'bal':K('1티어 접두·저항 2개, 마지막 접미는 랜덤 옵션 (영상 비용 180~200 div와 비슷)','T1 prefixes and two T1 resistances, last suffix as it comes (close to the video’s 180–200 div)')},
  tags,nodes,[{'id':'L0','nodes':['e1','ax'],'kr':'접미 저항 2개','en':'Two resistances'},{'id':'L1','nodes':['e3','cx','w0','db','rb'],'kr':'접두 두번째 옵션','en':'Second prefix'},{'id':'L2','nodes':['d3','d4','d4x'],'kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'},{'id':'L3','nodes':['f1','t1'],'kr':'마지막 접미','en':'Last suffix'}],
  FIN(('high','bal'),lambda v:[{'tag':'pes','fr':True},{'tag':'esf','tmax':1},{'tag':'sp','tmax':1},{'tag':'fr','tmax':1},{'tag':'cr','tmax':1}]+([{'tag':'lr','tmax':1}] if v=='high' else [{'side':'s','random':True}])+[]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'pes'},{'count':{'tag':'gp','min':2}},{'any':[{'count':{'tag':'goodS','min':3}},{'all':[{'param':{'last':'any'}},{'count':{'tag':'goodS','min':2}},{'full':'s'}]}]}]},('high','bal'))

# ---------- 2. Slipstrike Vest (회피) ----------
# 영상 대조(2026-11-11, swF5mwXmZ0k 40:45~46:30, 사용자: 영상에 맞춰 플로우차트를 만들고 적정 가격 100~200 div):
#   41:16 소멸의 오브로 분열 + 옵션 1개만 → 41:19 카오스 오브로 그 잡옵을 저항으로 → 41:26 상위 찬미의 징조 + 완벽한 엑잘로 접미 2개
#   → 41:55 절사의 징조 + 완벽한 카오스 오브로 마지막 잡옵 접미
#   → 42:20 엑잘 한 번, 빗나가면 좌측 결정화의 징조 + 심연의 에센스(접두 하나 → 징표) → 갈비뼈 → 우물에서 공개해 생명력·가시로 자리 막기 → 다시 엑잘
#   → 45:30 막아 둔 옵션을 지우고 마지막 접두는 훼손 공개(생명력 없는 복합·정신력 1티어, 약한 건 넘김)
c='Body_Armours_dex'
P2={'high':{'pT':1,'rT':1,'dT':1,'g':1},'bal':{'pT':2,'rT':2,'dT':2,'g':0}}   # 2026-11-12 C17: 반복으로 찾는 옵션 하이엔드 1티어·밸런스 1~2티어, 밸런스는 마지막 접미가 잡옵이어도 랜덤 옵션으로 둠(g)
tags={'pev':{'gi':7,'tmax':1},'evf':{'gi':6,'tmax':'$pT'},'hyb':{'gi':9,'tmax':'$pT'},'gpE':{'anyOf':['evf','hyb']},
      'fr':{'gi':1,'tmax':'$rT'},'cr':{'gi':2,'tmax':'$rT'},'lr':{'gi':3,'tmax':'$rT'},'dfl':{'gi':18,'tmax':'$dT'},
      'goodS':{'anyOf':['fr','cr','lr','dfl']},'blk':{'anyOf':[{'gi':5},{'gi':12}]},'mkP':{'gi':45}}
PV=itg('p',c,7,['pev'],'f'); EV=itg('p',c,6,['evf']); HY=itg('p',c,9,['hyb'])
RF=itg('s',c,1,['fr']); RC=itg('s',c,2,['cr']); DF=itg('s',c,18,['dfl'])
GS=it('s','저항 또는 굴절 1개','One resistance or deflection',['goodS'],'n')
BL=it('p','생명력 최대치 또는 가시 피해 (훼손, 자리 막기)','Max life or thorns (desecrated, slot blocker)',['blk'],'d')
S0=[PV,J('s')]; S0b=[PV,GS]; S1=S0b+[it('s','랜덤 옵션 2개','Two random lines',None,'j')]; S2=[PV,RF,RC,DF]
S5=S2+[EV]; S7=S5+[UN('p')]; S8=S5+[HY]
G3={'any':[{'count':{'tag':'goodS','min':3}},{'all':[{'param':{'g':0}},{'count':{'tag':'goodS','min':2}},{'full':'s'}]}]}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pev','fr':True},{'junk':'s'}]},K('회피 증가 1티어 분열 Slipstrike Vest (아이템 레벨 82, 분열 + 잡옵 1개만 남김)','Slipstrike Vest with fractured T1 % evasion (item level 82, fracture + one junk line)'),S0),
 mark([0,0.6],'c0',S0),
 act('c0','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'goodS'},'to':'e1','res':'ok'},{'to':'c0','res':'fail'}],S0b,show=['fr','cr','lr','dfl']),
 act('e1','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 옵션 2개','Two suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),
     [{'if':{'all':[G3,{'not':{'sideLt':{'side':'p','n':2}}}]},'to':'cx','res':'ok','label':K('접두 잡옵 있음','Junk prefix there')},{'if':G3,'to':'e3','res':'ok'},{'to':'t1','res':'fail'}],S1,omens=['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation']),
 act('t1','main',[0,3],'chaos','Greater_Chaos_Orb',K('접미 잡옵 바꾸기','Reroll the junk suffix'),None,K('카오스','Chaos'),
     [{'if':{'all':[G3,{'not':{'sideLt':{'side':'p','n':2}}}]},'to':'cx','res':'ok','label':K('접두 잡옵 있음','Junk prefix there')},{'if':G3,'to':'e3','res':'ok'},{'if':{'not':{'full':'s'}},'to':'e2','label':K('새 옵션이 접두로','New line went to a prefix')},{'to':'t1','res':'fail'}],S2,show=['fr','cr','lr','dfl']),
 act('e2','main',[1,3],'exalt','Exalted_Orb',K('빈 접미 채우기','Fill the empty suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),
     [{'if':{'all':[G3,{'not':{'sideLt':{'side':'p','n':2}}}]},'to':'cx','res':'ok','label':K('접두 잡옵 있음','Junk prefix there')},{'if':G3,'to':'e3','res':'ok'},{'to':'t1','res':'fail','port':'right'}],None,omens=['Omen_of_Dextral_Exaltation']),
 act('e3','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'all':[{'added':'gpE'},{'has':'blk'}]},'to':'w1','res':'ok'},{'if':{'added':'gpE'},'to':'d3','res':'ok'},{'to':'cx','res':'fail'}],S5,show=['evf','hyb'],omens=['Omen_of_Sinistral_Exaltation']),
 act('cx','main',[1,5],'essence','Essence_of_the_Abyss',K('빗나간 접두를 징표로','The missed prefix goes for the Mark'),[st('p','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),
     [{'if':{'has':'blk'},'to':'w0','label':K('막기가 남음','Blocker still there')},{'to':'db'}],None,ess='mkP',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 annul('w0',[2,5],[{'to':'db'}],target=K('남은 막기 훼손 옵션 제거 (훼손 옵션은 하나만)','Remove the old blocker (one desecrated line per item)')),
 act('db','main',[1,6],'desecrate','Ancient_Rib',K('징표 훼손','Desecrate the Mark'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'rb'}],None,fromMark=True),
 act('rb','main',[1,7],'reveal',None,K('생명력·가시로 자리 막기','Block with life or thorns'),None,K('공개','Reveal'),
     [{'if':{'full':'p'},'to':'cx','res':'fail','port':'right'},{'to':'e3','res':'ok'}],None,want='blk',show=['blk'],omens=['Omen_of_Abyssal_Echoes']),
 annul('w1',[0,6],[{'to':'d3'}],target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecrated line')),
 act('d3','main',[0,7],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d4'}],S7,omens=['Omen_of_Sinistral_Necromancy']),
 act('d4','main',[0,8],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'count':{'tag':'gpE','min':2}},'to':'ok','res':'ok'},{'to':'d4x','res':'fail'}],S8,want='gpE',show=['evf','hyb'],omens=['Omen_of_Abyssal_Echoes']),
 annul('d4x',[1,8],[{'to':'d3','port':'right'}]),
 done([0,9])]
g22('unstoppable-slipstrike-vest-v2',c,'Slipstrike Vest',82,
  'Unstoppable BTW 회피 갑옷(swF5mwXmZ0k 40:45~46:30, 영상 대조 2026-11-11) — 회피 증가 1티어 분열에 옵션 1개만 남김 → 카오스 오브로 그 잡옵을 저항으로 → 상위 찬미 + 우측 찬미 + 완벽한 엑잘로 접미 2개 → 잡옵 접미는 상위 카오스 오브 반복(영상 41:50 “카오스로 막 돌리기” — 일반 카오스 오브보다 시뮬이 싸서 상위로 바꿈: 밸런스 224 → 176 div, 하이엔드 940 → 651 div, 정책 0장 3번. 영상 41:55의 절사의 징조 + 완벽한 카오스 오브 한 번은 운이 좋았던 경우. 새 옵션이 접두로 가면 우측 찬미 + 엑잘티드 오브) → 좌측 찬미 + 완벽한 엑잘로 접두, 빗나가면 좌측 결정화의 징조 + 심연의 에센스로 징표 → 고대 갈비뼈 → 공개해 생명력·가시로 자리 막기 → 다시 엑잘 → 빛의 징조로 막기 제거 → 고대 갈비뼈 → 마지막 접두 공개(빛의 징조로 다시). 디바인·바알 주입기·바알 오브는 뺌(정책 33).',
  {'pT':{'kr':'접두 회피','en':'Evasion prefixes','values':TS},'rT':{'kr':'저항','en':'Resistances','values':TS},'dT':{'kr':'굴절','en':'Deflection','values':TS},'g':{'kr':'마지막 접미가 잡옵일 때','en':'Junk last suffix','values':TV({'1':('바꾸는 도박','Gamble to replace'),'0':('랜덤 옵션으로 둠','Keep as a random line')})}},P2,
  {'high':K('모든 옵션 1티어 (영상: 회피 3,646)','Every line tier 1 (video: 3,646 evasion)'),'bal':K('접두·저항·굴절 1~2티어, 마지막 접미는 랜덤 옵션 (영상: 회피 복합 2티어도 괜찮음)','Prefixes, resistances and deflection at T1–2, the last suffix random (video: a T2 hybrid is fine)')},
  tags,nodes,[{'id':'L0','nodes':['t1','e2'],'kr':'접미 잡옵 바꾸기','en':'Junk suffix swap'},{'id':'L1','nodes':['e3','cx','w0','db','rb'],'kr':'접두 두번째 옵션','en':'Second prefix'},{'id':'L2','nodes':['d3','d4','d4x'],'kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'}],
  FIN(('high','bal'),lambda v:[{'tag':'pev','fr':True},{'tag':'evf','tmax':1},{'tag':'hyb','tmax':1},{'tag':'fr','tmax':1},{'tag':'cr','tmax':1},{'tag':'dfl','tmax':1}] if v=='high' else
      [{'tag':'pev','fr':True},{'tag':'evf','tmax':2},{'tag':'hyb','tmax':2},{'side':'s','label':K('저항 또는 굴절 1~2티어','Resistance or deflection T1–2')},{'side':'s','label':K('저항 또는 굴절 1~2티어','Resistance or deflection T1–2')},{'side':'s','random':True}]),
  {'quality':20,'sockets':3,'exceptional':True},{'all':[{'has':'pev'},{'count':{'tag':'gpE','min':2}},G3]},('high','bal'))

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_unstoppable_vile_robe.py'): _sp.run([_sy.executable, f'{H}/gen_unstoppable_vile_robe.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_unstoppable_slipstrike_vest.py'): _sp.run([_sy.executable, f'{H}/gen_unstoppable_slipstrike_vest.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 덮어씀
