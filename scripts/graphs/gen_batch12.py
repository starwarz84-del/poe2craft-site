# Batch 12 (사용자 2026-11-10: 전문가부터는 2개씩) — 전문가(4) → High-end (video) + Balance (reveal kept as it comes).
#   mastert-timelost-emerald-v2 (GNNkhSENp6Q), chiba-timelost-emerald-v2 (O6Rp7JIxhrs)
# Finishing Divine Orb / catalyst quality are left out (정책 23, like the other jewels).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch10.py').read(); exec(_src[:_src.index('# ---------- 1. SL')])
PH={'high':{'v':1},'bal':{'v':2}}
DESC={'high':K('영상: 빛의 징조로 원하는 접미가 나올 때까지 다시 공개','Video: Light retries until the wanted suffix shows'),
      'bal':K('공개 결과 그대로, 나머지는 영상대로','Keep the reveal, the rest as in the video')}
FRC=it('s','공격 치명타 명중 확률 (분열)','Attack crit chance (fractured)',['cc']); CS2=it('p','+1 접미 허용','+1 suffix allowed',['contS'])
RD=it('p','범위 아주 큼','Very large radius',['rad'])
BASE_TAGS={'cc':{'gi':8},'contS':{'gi':101,'slot':{'s':1}},'contP':{'gi':102,'slot':{'p':1}},'rad':{'gi':99}}
def contempt(id,pos,ok,fail,item,keep=None):
    return LIQ(id,pos,'Ancient_Potent_Liquid_Contempt','contS',K('고대 위력적인 액체 경멸','Ancient Potent Liquid Contempt'),
        [st('p','+1 접미 허용','+1 suffix allowed')],
        [{'if':{'all':[{'has':'contS'},{'has':keep}]} if keep else {'has':'contS'},'to':ok,'res':'ok'},{'to':fail,'res':'fail','port':'right'}],item,alt='contP')
def resetx(id,pos,to):   # a failed contempt: Annulment down to the fracture + one line, then Chaos again (video)
    return cleanup(id,pos,[],[{'to':to,'port':'right'}],K('분열 + 옵션 1개만 남기기','Keep the fracture + one line'),maxJunk=1)
def erase(id,pos,nxt,item):
    return act(id,'main',pos,'chaos','Chaos_Orb',K('+1 접미 허용 옵션 지우기 (접두만 바뀜)','Reroll the +1 suffix line away (prefixes only)'),None,K('카오스','Chaos'),
        [{'if':{'has':'contS'},'to':id,'res':'fail'},{'to':nxt,'res':'ok'}],item,omens=['Omen_of_Sinistral_Erasure'])
def goodpre(id,pos,nxt,show,item):
    return act(id,'main',pos,'chaos','Chaos_Orb',K('좋은 접두 (접미가 한도를 넘어 접두만 바뀜)','A good prefix (only prefixes change)'),None,K('카오스','Chaos'),
        [{'if':{'has':'pre'},'to':nxt,'res':'ok'},{'to':id,'res':'fail'}],item,show=show)
def melan(id,pos,back,item):
    return LIQ(id,pos,'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 (접두 하나가 지워짐)','Ancient Potent Liquid Melancholy (one prefix goes)'),[st('p','범위 아주 큼','Very large radius')],
        [{'if':{'has':'pre'},'to':'ok','res':'ok'},{'to':back,'res':'fail','port':'right'}],item)

# ---------- 1. Master T 5옵션 오래된 에메랄드 (GNNkhSENp6Q) ----------
# 원본: 공격 치명타 확률 분열 + 잡옵 → 카오스 오브(공격 치명타 피해) → 엑잘(접두 잡옵) → 고대 위력적인 액체 경멸(실패 = 소멸의 오브로 분열 + 옵션 1개, 카오스부터)
# → 우측 강령술 + 보존된 두개골 → 공개(이동 속도, 빛의 징조로 다시) → 좌측 말소의 징조 + 카오스 오브(경멸 옵션 지우기) → 카오스 오브(상태 이상·감전 강도) → 고대 위력적인 액체 우울(1/2).
GP=[6,62]
tags={**BASE_TAGS,'cd':{'gi':9},'ms':{'gi':48},**{f'p{g}':{'gi':g} for g in GP},'pre':{'anyOf':[f'p{g}' for g in GP],'label':K('상태 이상·감전 강도','Ailment or shock magnitude')}}
CD=it('s','공격 치명타 피해 보너스','Attack crit damage bonus',['cd']); MS=it('s','이동 속도','Movement speed',['ms']); PR=it('p','상태 이상·감전 강도','Ailment or shock magnitude',['pre'])
I0=[FRC,J('p')]; I1=[FRC,CD]; I2=[FRC,CD,J('p'),J('p')]; I3=[FRC,CD,J('p'),CS2]; I4=I3+[UN('s')]; I5=[FRC,CD,MS,J('p'),CS2]; I6=[FRC,CD,MS,J('p'),J('p')]; I7=[FRC,CD,MS,PR,J('p')]; I8=[FRC,CD,MS,PR,RD]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'cc','fr':True},{'junk':'p'}]},K('공격 치명타 확률 분열 + 잡옵 1개 오래된 에메랄드','Time-Lost Emerald: fractured attack crit chance + one junk line'),I0),
 mark([0,0.6],'m2',I0),
 act('m2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'cd'},'to':'m3','res':'ok'},{'to':'m2','res':'fail'}],I1,show=['cd']),
 act('m3','main',[0,2],'exalt','Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 1개씩 (접미가 꽉 차 접두로)','One random line each (suffixes are full)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'m4'},{'to':'m3','hide':True}],I2),
 contempt('m4',[0,3],'m5','m4x',I3,keep='cd'), resetx('m4x',[1,3],'m2'),
 act('m5','main',[0,4],'desecrate','Preserved_Cranium',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'m6'}],I4,omens=['Omen_of_Dextral_Necromancy']),
 REVEAL('m6',[0,5],'ms',['ms'],'m7','m6x',I5), LIGHTX('m6x',[1,5],'m5'),
 erase('m7',[0,6],'m8',I6),
 goodpre('m8',[0,7],'m9',[f'p{g}' for g in GP],I7),
 melan('m9',[0,8],'m8',I8),
 done([0,9])]
graph10('mastert-timelost-emerald-v2','Time-Lost_Emerald','Time-Lost Emerald',81,
  'Master T 5옵션 오래된 에메랄드(원본 레시피 기록) — 공격 치명타 확률 분열 + 잡옵 → 카오스 오브(공격 치명타 피해) → 엑잘 2번(접두) → 고대 위력적인 액체 경멸(실패 = 소멸의 오브로 분열 + 옵션 1개) → 우측 강령술 + 보존된 두개골 → 공개(이동 속도, 하이엔드 = 빛의 징조로 다시) → 좌측 말소의 징조 + 카오스 오브(경멸 옵션) → 카오스 오브(상태 이상·감전 강도) → 고대 위력적인 액체 우울. 신성한 오브 마무리는 뺌.',
  ROUTE,PH,DESC,tags,nodes,
  [{'id':'L1','nodes':['m5','m6','m6x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['m8','m9'],'kr':'우울','en':'Melancholy'}],
  FIN(('high','bal'),lambda v:[{'side':'p','label':K('상태 이상·감전 강도','Ailment or shock magnitude')},{'tag':'rad','tmax':1},{'tag':'cc','tmax':1,'fr':True},{'tag':'cd','tmax':1},{'tag':'ms','tmax':1} if v=='high' else {'side':'s','random':True}]),
  {'quality':0,'sockets':0},{'all':[{'has':'cd'},{'has':'pre'},{'has':'rad'}]},('high','bal'),cap={'p':2,'s':2})

# ---------- 2. ChibaTTV 오래된 에메랄드 (O6Rp7JIxhrs) ----------
# 원본: 공격 치명타 확률 분열 + 잡옵 → 카오스 오브(창·공격 치명타 피해) → 엑잘 2번(접두 잡옵) → 고대 위력적인 액체 경멸(실패 = 소멸의 오브로 분열 + 옵션 1개, 카오스부터)
# → 보존된 두개골(접두가 꽉 차 접미로) → 공개(공격 속도·치명타 피해·창 공격 속도·주요 패시브 효과, 빛의 징조로 다시) → 좌측 소멸의 징조로 경멸 옵션(빗나가면 한 번 더)
# → 엑잘(접두) → 카오스 오브(투사체 속도·투사체 피해·공격 피해) → 고대 위력적인 액체 우울(1/2). 제련된 강탈자 기폭제(퀄리티)는 뺌.
SUF=[65,9]; REV=[11,9,64,3]; GP=[55,54,10]
tags={**BASE_TAGS,**{f's{g}':{'gi':g} for g in sorted(set(SUF+REV))},'suf':{'anyOf':[f's{g}' for g in SUF],'label':K('치명타 피해 (창 포함)','Crit damage (or with spears)')},
      'rev':{'anyOf':[f's{g}' for g in REV],'label':K('핵심 패시브 접미','Notable suffix')},**{f'p{g}':{'gi':g} for g in GP},'pre':{'anyOf':[f'p{g}' for g in GP],'label':K('투사체·공격 피해 접두','Projectile or attack damage prefix')}}
SU=it('s','치명타 피해 (창 포함)','Crit damage (or with spears)',['suf']); RV=it('s','공개 접미','Revealed suffix',['rev']); PR=it('p','투사체·공격 피해 접두','Projectile or attack damage prefix',['pre'])
I0=[FRC,J('p')]; I1=[FRC,SU]; I2=[FRC,SU,J('p'),J('p')]; I3=[FRC,SU,J('p'),CS2]; I4=I3+[UN('s')]; I5=[FRC,SU,RV,J('p'),CS2]; I6=[FRC,SU,RV,J('p')]; I7=[FRC,SU,RV,J('p'),J('p')]; I8=[FRC,SU,RV,PR,J('p')]; I9=[FRC,SU,RV,PR,RD]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'cc','fr':True},{'junk':'p'}]},K('공격 치명타 확률 분열 + 잡옵 1개 오래된 에메랄드','Time-Lost Emerald: fractured attack crit chance + one junk line'),I0),
 mark([0,0.6],'c2',I0),
 act('c2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'suf'},'to':'c3','res':'ok'},{'to':'c2','res':'fail'}],I1,show=[f's{g}' for g in SUF]),
 act('c3','main',[0,2],'exalt','Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 1개씩 (접미가 꽉 차 접두로)','One random line each (suffixes are full)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'c4'},{'to':'c3','hide':True}],I2),
 contempt('c4',[0,3],'c5','c4x',I3,keep='suf'), resetx('c4x',[1,3],'c2'),
 act('c5','main',[0,4],'desecrate','Preserved_Cranium',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개, 접두가 꽉 차 접미로)','Desecrated modifier (unrevealed; prefixes are full)')],K('훼손','Desecrate'),[{'to':'c6'}],I4),
 REVEAL('c6',[0,5],'rev',[f's{g}' for g in REV],'c7','c6x',I5), LIGHTX('c6x',[1,5],'c5'),
 act('c7','main',[0,6],'annul','Orb_of_Annulment',K('+1 접미 허용 옵션 제거 (접두 옵션 2개 중 하나)','Remove the +1 suffix line (one of the two prefixes)'),None,K('소멸','Annul'),
     [{'if':{'has':'contS'},'to':'c7','res':'fail'},{'to':'c8','res':'ok'}],I6,omens=['Omen_of_Sinistral_Annulment']),
 act('c8','main',[0,7],'exalt','Exalted_Orb',K('접두 채우기','Fill the prefixes'),[st('p','랜덤 옵션 (접미가 한도를 넘어 접두로만)','Random lines (suffixes are over the limit)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'c9'},{'to':'c8','hide':True}],I7),
 goodpre('c9',[0,8],'c10',[f'p{g}' for g in GP],I8),
 melan('c10',[0,9],'c9',I9),
 done([0,10])]
graph10('chiba-timelost-emerald-v2','Time-Lost_Emerald','Time-Lost Emerald',80,
  'ChibaTTV 오래된 에메랄드(원본 레시피 기록) — 공격 치명타 확률 분열 + 잡옵 → 카오스 오브(치명타 피해) → 엑잘 2번 → 고대 위력적인 액체 경멸(실패 = 소멸의 오브로 분열 + 옵션 1개) → 보존된 두개골 → 공개(하이엔드 = 빛의 징조로 다시) → 좌측 소멸의 징조(경멸 옵션) → 엑잘 → 카오스 오브(투사체·공격 피해) → 고대 위력적인 액체 우울. 기폭제 퀄리티는 뺌.',
  ROUTE,PH,DESC,tags,nodes,
  [{'id':'L1','nodes':['c5','c6','c6x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['c9','c10'],'kr':'우울','en':'Melancholy'}],
  FIN(('high','bal'),lambda v:[{'side':'p','label':K('투사체·공격 피해 접두','Projectile or attack damage prefix')},{'tag':'rad','tmax':1},{'tag':'cc','tmax':1,'fr':True},{'side':'s','label':K('치명타 피해 (창 포함)','Crit damage (or with spears)')},{'side':'s','label':K('핵심 패시브 접미','Notable suffix')} if v=='high' else {'side':'s','random':True}]),
  {'quality':0,'sockets':0},{'all':[{'has':'suf'},{'has':'pre'},{'has':'rad'}]},('high','bal'),cap={'p':2,'s':2})
