# Batch 13 (사용자 2026-11-10: 전문가부터는 2개씩) — 전문가(4) → High-end (video) + Balance.
#   noble-timelost-sapphire-v2, mazbro-proj-gloves-v2
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch12.py').read(); exec(_src[:_src.index('# ---------- 1. Master T')])
_s11=open(f'{H}/gen_batch11.py').read(); exec(_s11[_s11.index('def graph11'):_s11.index('def WHIT')])

# ---------- 1. 노블이 5옵션 오래된 사파이어 ----------
# 원본: 주문 치명타 확률 분열 + 잡옵 → 카오스 오브(주문 치명타 피해) → 엑잘(접두) → 고대 위력적인 액체 경멸 → 우측 찬미 + 엑잘(치명타 피해, 빗나가면 소멸의 오브)
# → 좌측 말소의 징조 + 카오스 오브(경멸 옵션) → 엑잘(접두) → 고대 위력적인 액체 우울 → 보존된 두개골(접두가 꽉 차 접두 하나를 지우고 붙음) → 공개(최대 마나, 실패는 카오스 오브로 바꾸고 다시)
# 영상 재확인(2026-11-10) 뒤 사용자 확정: 경멸은 '지우고 붙음'이라 접두 2개를 채워서(성공 2/3, 영상은 1개). 세 번째 접미 엑잘 실패는 소멸의 오브 — 경멸 옵션이 지워지면 빗나간 접미까지 지우고 접두를 채워 경멸 다시. 기폭제 퀄리티는 뺌.
FRS=it('s','주문 치명타 명중 확률 (분열)','Spell crit chance (fractured)',['cc'])
tags={'cc':{'gi':50},'scd':{'gi':16},'cd':{'gi':15},'contS':{'gi':84,'slot':{'s':1}},'contP':{'gi':85,'slot':{'p':1}},'rad':{'gi':82},'mana':{'gi':69}}
SCD=it('s','주문 치명타 피해 보너스','Spell crit damage bonus',['scd']); CD=it('s','치명타 피해 보너스','Crit damage bonus',['cd']); MN=it('p','최대 마나','Maximum mana',['mana'])
RDs=it('p','범위 아주 큼','Very large radius',['rad'])
I0=[FRS,J('p')]; I1=[FRS,SCD]; I2=[FRS,SCD,J('p'),J('p')]; I3=[FRS,SCD,J('p'),CS2]; I4=I3+[CD]; I5=[FRS,SCD,CD,J('p'),J('p')]; I5b=I5; I6=[FRS,SCD,CD,J('p'),RDs]
I7=[FRS,SCD,CD,J('p'),UN('p')]; I8=[FRS,SCD,CD,MN,RDs]
def contempt_s(id,pos,ok,fail,item,keep):
    return LIQ(id,pos,'Ancient_Potent_Liquid_Contempt','contS',K('고대 위력적인 액체 경멸','Ancient Potent Liquid Contempt'),
        [st('p','+1 접미 허용','+1 suffix allowed')],
        [{'if':{'all':[{'has':'contS'},{'has':keep}]},'to':ok,'res':'ok'},{'to':fail,'res':'fail','port':'right'}],item,alt='contP')
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'cc','fr':True},{'junk':'p'}]},K('주문 치명타 확률 분열 + 잡옵 1개 오래된 사파이어','Time-Lost Sapphire: fractured spell crit chance + one junk line'),I0),
 mark([0,0.6],'n2',I0),
 act('n2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'scd'},'to':'n3','res':'ok'},{'to':'n2','res':'fail'}],I1,show=['scd']),
 act('n3','main',[0,2],'exalt','Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 1개씩 (접미가 꽉 차 접두로)','One random line each (suffixes are full)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'n4'},{'to':'n3','hide':True}],I2),
 contempt_s('n4',[0,3],'n5','n4x',I3,'scd'), resetx('n4x',[1,3],'n2'),
 act('n5','main',[0,4],'exalt','Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),[{'if':{'all':[{'has':'cd'},{'has':'scd'}]},'to':'n6','res':'ok'},{'if':{'full':'s'},'to':'n5x','res':'fail','port':'right'},{'to':'n5','res':'fail'}],I4,show=['cd','scd'],omens=['Omen_of_Dextral_Exaltation']),
 annul('n5x',[1,4],[{'if':{'not':{'has':'contS'}},'to':'n5c','port':'right'},{'if':{'full':'s'},'to':'n5x'},{'to':'n5','port':'bottom'}],omens=(),
       target=K('빗나간 접미 지우기','Remove the missed suffix')),
 annul('n5c',[2,4],[{'if':{'not':{'has':'scd'}},'to':'n4x','port':'right'},{'if':{'not':{'sideLt':{'side':'s','n':3}}},'to':'n5c'},{'to':'n3','port':'right'}],omens=(),
       target=K('빗나간 접미 지우기','Remove the missed suffix')),
 erase('n6',[0,5],'n7',I5),
 act('n7','main',[0,6],'exalt','Exalted_Orb',K('접두 채우기','Fill the prefixes'),[st('p','랜덤 옵션 (접미가 한도를 넘어 접두로만)','Random lines (suffixes are over the limit)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'n9'},{'to':'n7','hide':True}],I5b),
 LIQ('n9',[0,7],'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 (접두 하나가 지워짐)','Ancient Potent Liquid Melancholy (one prefix goes)'),[st('p','범위 아주 큼','Very large radius')],
     [{'if':{'all':[{'has':'mana'},{'has':'rad'}]},'to':'ok','res':'ok'},{'to':'n10'}],I6),
 act('n10','main',[0,8],'desecrate','Preserved_Cranium',K('접두 훼손','Prefix desecration'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'n11'}],I7,omens=['Omen_of_Sinistral_Necromancy']),
 act('n11','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'all':[{'added':'mana'},{'has':'rad'}]},'to':'ok','res':'ok'},{'if':{'added':'mana'},'to':'n9','res':'ok','port':'right'},{'to':'n11x','res':'fail','port':'right'}],I8,want='mana',show=['mana'],omens=['Omen_of_Abyssal_Echoes'],
     over=[{'param':{'v':2},'set':{'edges':[{'if':{'has':'rad'},'to':'ok','res':'ok'},{'to':'n9k','res':'fail','port':'right'}]}}]),
 act('n11x','main',[1,9],'chaos','Chaos_Orb',K('훼손 옵션 바꾸기','Replace the desecrated line'),None,K('카오스','Chaos'),
     [{'if':{'has':'rad'},'to':'n10','port':'right'},{'to':'n9','port':'right'}],I6),
 LIQ('n9k',[1,9.8],'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 다시','Ancient Potent Liquid Melancholy again'),[st('p','범위 아주 큼','Very large radius')],[{'to':'ok'}],I6),
 done([0,10.6])]
graph10('noble-timelost-sapphire-v2','Time-Lost_Sapphire','Time-Lost Sapphire',79,
  '노블이 5옵션 오래된 사파이어(원본 레시피 기록, 영상 재확인) — 주문 치명타 확률 분열 + 잡옵 → 카오스 오브(주문 치명타 피해) → 엑잘 2번(접두, 사용자 확정) → 고대 위력적인 액체 경멸(실패 = 분열 + 옵션 1개) → 우측 찬미 + 엑잘(치명타 피해, 빗나가면 소멸의 오브) → 좌측 말소의 징조 + 카오스 오브(경멸 옵션) → 엑잘 → 고대 위력적인 액체 우울 → 보존된 두개골 → 공개(최대 마나, 하이엔드 = 카오스 오브로 바꾸고 다시).',
  ROUTE,PH,{'high':K('영상: 최대 마나가 나올 때까지 카오스 오브로 바꾸고 다시','Video: Chaos the line away and retry until maximum mana'),'bal':K('공개 결과 그대로, 나머지는 영상대로','Keep the reveal, the rest as in the video')},tags,nodes,
  [{'id':'L1','nodes':['n9','n10','n11','n11x'],'kr':'최대 마나','en':'Maximum mana'}],
  FIN(('high','bal'),lambda v:[{'tag':'mana','tmax':1} if v=='high' else {'side':'p','random':True},{'tag':'rad','tmax':1},{'tag':'cc','tmax':1,'fr':True},{'tag':'scd','tmax':1},{'tag':'cd','tmax':1}]),
  {'quality':0,'sockets':0},{'all':[{'has':'scd'},{'has':'cd'},{'has':'rad'}]},('high','bal'),cap={'p':2,'s':2})

# ---------- 2. MazBro 투사체 +2 분열 장갑 (BIxlixCKPO0) ----------
# 2026-11-12 W1 영상 전체 재대조(자막 0:00~21:25 + 화면 캡처, 근거 scratchpad review/W1-mazbro-gloves/timeline.md) + 새 플로우차트 기준(사용자 확정 2026-11-12 15:02, 정책 11장 맨 위):
#   영상 흐름 한 줄. 11 카오스 → 영상에서 나온 접두 투사체 피해 1티어(15:20)로 정해진 상태 → 12 접미 치명타 확률·관통(4A, 12:52~13:40·15:25~16:10)
#   → 13·14 접두 투사체 속도를 훼손 공개로(17:35~18:24). 실패는 그 단계 옆의 짧은 되돌림만(라우터 없음).
# 베이스 준비(영상 화면): 2:05 특출난 검은강철 건틀릿(노트 '24 Gloves x 12 Divs') → 3:00~4:05 바알 방어구 장인의 주입기 30%(선택, 비용 미포함 — 다른 그래프와 같은 옆 상자)
#   → 4:22 콜르의 사냥(룬 툴팁) → 4:42 완벽한 진화(투사체 피해) → 4:56 완벽한 확장(덱스터리티) → 5:02 완벽한 제왕 → 5:12 소멸로 옵션 1개
#   → 6:34 카오스 오브로 투사체 +2(카오스 1073 → 503개) → 7:01 '좌측 찬미·상위 찬미 소모' 메시지 + 7:51 완벽한 엑잘티드 오브 → 7:04 훼손(미공개)
#   → 분열 1/3: 장갑 1·2·3 실패(7:20 투사체 피해가 분열되어 맨 위로), 장갑 4에서 성공(8:48 투사체 +2가 맨 위) → 12:15~12:27 소멸로 분열 + 옵션 1개.
#   아스트리드의 창의성은 8:06에 장착(화면 툴팁), 12:27부터 아이템에 '제작 옵션 1개 추가' 표시.
P2={'high':{'t':1},'bal':{'t':2}}
PT={'t':{'kr':'반복 목표','en':'Loop target','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}}
tags={'proj':{'gi':81,'tmax':1},
      'pspd1':{'gi':72,'tmax':1},
      'pdmg':{'gi':70,'tmax':'$t'},'pdmg1':{'gi':70,'tmax':1},'pdmg2':{'gi':70,'tmax':2},
      'crit':{'gi':73,'tmax':'$t'},'pierce':{'gi':74,'tmax':'$t'},
      'crit1':{'gi':73,'tmax':1},'pierce1':{'gi':74,'tmax':1},'crit2':{'gi':73,'tmax':2},'pierce2':{'gi':74,'tmax':2},
      'ss':{'anyOf':['crit','pierce'],'label':K('치명타 확률·관통','Crit chance or pierce')},
      'ss1':{'anyOf':['crit1','pierce1'],'label':K('치명타 확률·관통 1티어','T1 crit chance or pierce')},
      'ss2':{'anyOf':['crit2','pierce2'],'label':K('치명타 확률·관통 1~2티어','T1–2 crit chance or pierce')},
      'cdAny':{'gi':28},   # 일반 치명타 피해(같은 계열이라 발작의 에센스가 붙지 않음)
      'ward':{'gi':69},'hyst':{'gi':57}}
PJ=it('s','모든 투사체 스킬 레벨 +2 (콜르)','+2 projectile skills (Kolr)',['proj'],'f')
PS=it('p','투사체 속도 1티어 (콜르)','T1 projectile speed (Kolr)',['pspd1'])
PD=it('p','투사체 피해 (훼손, 콜르)','Projectile damage (desecrated, Kolr)',['pdmg'],'d')
SS=it('s','치명타 확률·관통 (콜르)','Crit chance or pierce (Kolr)',['ss'])
WD=it('p','룬 수호 (군왕의 합금)','Runic ward (Sovereign Alloy)',['ward'])
HY=it('s','치명타 피해 (발작의 에센스)','Crit damage (Essence of Hysteria)',['hyst'])
MISS=lambda: it('s','빗나간 접미 (잡옵)','Missed suffix (junk)',None,'j')
G0=[PJ,J('p')]; G1=[PJ,PS]; G2=[PS,PJ,SS]; G3=[PS,WD,PJ,SS,HY]; G4=[PS,WD,UN('p'),PJ,SS,HY]; G5=[PS,WD,PD,PJ,SS,HY]
ALL=[{'has':'pspd1'},{'has':'ss'},{'has':'ward'},{'has':'hyst'}]
L_=lambda kr,en: {'label':K(kr,en)}
F={'res':'fail','port':'right'}
# 12번(상위 엑잘) 뒤: 성공이면 13, 빗나가면 영상 순서대로 합금(12.A) → 발작의 에센스(12.B) → 소멸(12.C). 영상 노트 4A 마지막 줄 '맞으면 남은 접미를 치명타 에센스로'(12.D~F)는 첫 엑잘에 맞았을 때만
# 12번 엑잘 뒤 상태로 다음 상자: 합금·발작 옵션보다 먼저 맞으면 그 상자에서 엑잘을 한 번 더(세 번째 접미) 하고 빗나간 접미를 합금·발작의 에센스로 바꿈 — 따로 상자를 그리지 않음
E12=[{'if':{'all':ALL},'to':'k13','res':'ok',**L_('치명타 확률·관통 성공','Crit chance or pierce hit')},
     {'if':{'all':[{'has':'ss'},{'not':{'full':'s'}}]},'to':'k12','res':'ok','hide':True,**L_('합금·발작 전에 맞음, 접미 자리 남음 — 한 번 더 엑잘','Hit before the alloy and essence, a suffix slot left: exalt once more')},
     {'if':{'not':{'has':'ward'}},'to':'ka',**F,**L_('1번째 빗나감 — 합금','1st miss: alloy')},
     {'if':{'not':{'any':[{'has':'hyst'},{'has':'cdAny'}]}},'to':'kb',**F,**L_('2번째 빗나감 — 발작의 에센스','2nd miss: Essence of Hysteria')},
     {'to':'kc',**F,**L_('3번째 빗나감 — 소멸','3rd miss: annul')}]
nodes=[
 mark([0,0.6],'k11',G0),
 act('k11','main',[0,2],'chaos','Chaos_Orb',K('접두 투사체 속도 1티어','T1 projectile speed prefix'),None,K('카오스','Chaos'),
     [{'if':{'has':'pspd1'},'to':'k12','res':'ok'},{'to':'k11','res':'fail'}],G1,show=['pspd1']),   # 15:56 성공 회차(사용자 확정 2026-11-12)
 cleanup('kz',[1,1.5],[],[{'to':'k11','port':'right'}],K('분열 + 옵션 1개만 남기기','Keep the fracture + one line'),maxJunk=1),   # 13:40 '투사체 속도가 지워짐 — 처음부터 카오스'
 act('k12','main',[0,3],'exalt','Greater_Exalted_Orb',K('접미 치명타 확률·관통','Crit chance or pierce suffix'),None,K('엑잘','Exalt'),E12,G3,show=['crit','pierce'],showText=[K('합금·발작 전에 맞으면 한 번 더 엑잘','A hit before the alloy and essence: exalt once more')],omens=['Omen_of_Dextral_Exaltation'],skipIf={'all':ALL},skipTo='k13',skipHide=True),   # 소멸 뒤 이미 완성된 상태면 엑잘 없이 13으로(영상 경로에는 없음, 그림에 안 보임)
 act('ka','main',[1,3],'essence','Sovereign_Alloy',K('빗나간 접미를 지우고 룬 수호','The missed suffix goes, runic ward comes'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],K('합금','Alloy'),[{'to':'k12','port':'left',**L_('다시 엑잘','Exalt again')}],[PS,WD,PJ],ess='ward',omens=['Omen_of_Dextral_Crystallisation']),
 act('kb','main',[1,4],'essence','Essence_of_Hysteria',K('빗나간 접미를 지우고 치명타 피해','The missed suffix goes, crit damage comes'),[st('s','치명타 피해 (제작 옵션)','Crit damage (crafted)')],K('에센스','Essence'),[{'to':'k12','port':'left',**L_('다시 엑잘','Exalt again')}],[PS,PJ,HY,WD],ess='hyst',omens=['Omen_of_Dextral_Crystallisation']),
 cleanup('kc',[1,5],['pspd1','ward','hyst','ss'],[{'lost':'pspd1','to':'kz','port':'right',**L_('투사체 속도가 지워짐 — 카오스부터','Projectile speed gone: back to Chaos')},
     {'lost':'ward','to':'kc',**L_('룬 수호가 지워짐 — 하나 더','Runic ward gone: one more')},{'lost':'hyst','to':'kc',**L_('치명타 피해가 지워짐 — 하나 더','Crit damage gone: one more')},{'lost':'ss','to':'kc','hide':True},
     {'to':'k12','port':'left',**L_('빗나간 접미가 지워짐 — 다시 엑잘','Missed suffix gone: exalt again')}],K('빗나간 접미가 지워질 때까지 한 개씩, 룬 수호·치명타 피해가 지워져도 계속','One at a time until the missed suffix goes, even if runic ward or crit damage goes first')),
 act('k13','main',[0,6],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'k14'}],G4),   # 17:35 '남은 자리가 접두뿐이라 징조 필요 없음'
 act('k14','main',[0,7],'reveal',None,K('접두 투사체 피해','Projectile damage prefix'),None,K('공개','Reveal'),
     [{'if':{'added':'pdmg'},'to':'ok','res':'ok'},{'to':'k14x','res':'fail','port':'right'}],G5,want='pdmg',show=['pdmg'],omens=['Omen_of_Abyssal_Echoes']),
 annul('k14x',[1,7],[{'to':'k13','port':'right',**L_('다시 훼손','Desecrate again')}]),   # 17:56 빛의 징조 + 소멸의 오브, 18:06 2티어(30%)도 지움
 done([0,8])]
graph11('mazbro-proj-gloves-v2','Gloves_str_dex','Blacksteel Gauntlets',80,
  'MazBro 투사체 +2 분열 장갑(2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 특출난 검은강철 건틀릿 → 콜르의 사냥 → 완벽한 진화·확장·제왕 → 소멸로 옵션 1개 → 카오스 오브(투사체 +2) → 완벽한 엑잘 + 좌측 찬미 + 상위 찬미(접두 2개) → 고대 갈비뼈 + 우측 강령술 → 아스트리드의 창의성 → 분열(1/3, 빗나가면 새 베이스) → 소멸로 분열 + 옵션 1개 → 카오스 오브(접두 투사체 속도 1티어) → 상위 엑잘 + 우측 찬미(접미 치명타 확률·관통, 빗나가면 우측 결정화 + 군왕의 합금 → 우측 결정화 + 발작의 에센스 → 소멸) → 고대 갈비뼈(접두) → 공개(투사체 피해, 빛의 징조로 다시). 퀄리티 30%·룬벼림·신성한 오브·룬 교체는 비용에서 뺌.',
  PT,P2,{'high':K('영상: 상위 엑잘 반복과 공개 모두 1티어','Video: T1 in the exalt loop and on the reveal'),'bal':K('상위 엑잘 반복과 공개를 1~2티어까지','The exalt loop and the reveal accept T1–2')},tags,nodes,
  [{'id':'L1','nodes':['k12','ka','kb','kc'],'kr':'접미 치명타 확률·관통','en':'Crit or pierce suffix',
    # 다중 루프를 상자 하나로(사용자 확정 2026-11-12 17:06, 정책 11장) — 영상 노트 4A 순서, 시각은 timeline.md 13번 묶음 표
    'fold':True,'goal':K('접미 치명타 확률·관통 1티어','T1 crit chance or pierce suffix'),
    'goalBy':{'high':K('접미 치명타 확률·관통 1티어','T1 crit chance or pierce suffix'),'bal':K('접미 치명타 확률·관통 1~2티어','T1–2 crit chance or pierce suffix')},
    'steps':[{**K('상위 엑잘 + 우측 찬미로 접미 치명타 확률·관통','Greater Exalt + Dextral Exaltation for a crit or pierce suffix'),'node':'k12'},
             {**K('1번째 빗나감 — 우측 결정화 + 군왕의 합금으로 룬 수호(접두)','1st miss: Dextral Crystallisation + Sovereign Alloy for runic ward (prefix)'),'node':'ka'},
             {**K('2번째 빗나감 — 우측 결정화 + 발작의 에센스로 치명타 피해','2nd miss: Dextral Crystallisation + Essence of Hysteria for crit damage'),'node':'kb'},
             {**K('3번째 빗나감 — 빗나간 접미가 지워질 때까지 소멸의 오브 한 개씩','3rd miss: Annulment one at a time until the missed suffix goes'),'node':'kc'}],
    'worst':{**K('투사체 속도가 지워지면 카오스 단계부터','Projectile speed gone: back to the Chaos step'),'to':'kz'},
    'item':G3},{'id':'L2','nodes':['k13','k14','k14x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'pspd1'},{'tag':'pdmg1' if v=='high' else 'pdmg2','des':True},{'tag':'ward'},{'tag':'proj','fr':True},{'tag':'ss1' if v=='high' else 'ss2'},{'tag':'hyst'}]),
  {'quality':30,'sockets':2},{'all':ALL+[{'has':'pdmg'},{'has':'proj'}]},('high','bal'),xsub=["Kolr's Hunt"],xroll=True)
_gp=f"{H}/mazbro-proj-gloves-v2.json"; _g=json.load(open(_gp))
for _n in _g['nodes']:
    if _n.get('group')=='main': _n['pos']=[_n['pos'][0], _n['pos'][1]+12.4]
_g['basePrice']={'Divine_Orb':12}
_PJI=[{'s':'s','kr':'모든 투사체 스킬 레벨 +2 (콜르)','en':'+2 projectile skills (Kolr)','m':'n','tags':['proj']}]
_JK=lambda s: {'s':s,'kr':'잡옵','en':'Junk','m':'j'}
_prep=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'pk','start':{'rar':'normal','mods':[],'quality':30},'label':K('특출난 검은강철 건틀릿 구입 (노멀)','Buy exceptional Blacksteel Gauntlets (normal)'),'item':[]},
 {'id':'hq','kind':'side','group':'prep','pos':[1,0.5],'attach':['h1','pk'],'cur':'Vaal_Armourers_Infuser','goal':K('퀄리티 20% → 30%, 선택·비용 미포함','Quality 20% → 30%, optional, not costed'),'label':K('퀄리티','Quality')},
 {'id':'pk','kind':'act','group':'prep','pos':[0,1],'act':'rune','goal':K('콜르의 사냥 장착, 영구','Socket Kolr’s Hunt, permanent'),'showText':[K('콜르 옵션이 붙을 수 있음','Kolr lines can roll')],'label':K('룬','Rune'),'rune':K('콜르의 사냥','Kolr’s Hunt'),'edges':[{'to':'p1'}],'item':[]},   # 4:22 화면 툴팁 '장갑: 명사수 옵션 가능'
 {'id':'p1','kind':'act','group':'prep','pos':[0,2],'act':'transmute','cur':'Perfect_Orb_of_Transmutation','goal':K('매직','Magic'),'label':K('진화','Transmute'),'edges':[{'to':'p2'}],'item':[_JK('p')]},   # 4:42 화면: 투사체 피해 40% 접두
 {'id':'p2','kind':'act','group':'prep','pos':[0,3],'act':'augment','cur':'Perfect_Orb_of_Augmentation','goal':K('매직 두번째 옵션','Second magic line'),'label':K('확장','Augment'),'edges':[{'to':'p3'}],'item':[_JK('p'),_JK('s')]},   # 4:56 화면: 덱스터리티 +32
 {'id':'p3','kind':'act','group':'prep','pos':[0,4],'act':'regal','cur':'Perfect_Regal_Orb','goal':K('레어','Rare'),'label':K('제왕','Regal'),'edges':[{'to':'p3x'}],'item':[_JK('p'),_JK('s'),_JK('x')]},   # 5:02 화면: 방어도·회피 접두 추가
 {'id':'p3x','kind':'cleanup','group':'prep','pos':[0,5],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('옵션 1개만 남기기','Keep one line'),'edges':[{'to':'p4'}],'item':[_JK('s')]},   # 5:12 화면: 덱스터리티만 남음
 {'id':'p4','kind':'act','group':'prep','pos':[0,6],'act':'chaos','cur':'Chaos_Orb','goal':K('모든 투사체 스킬 레벨 +2','+2 to all projectile skills'),'label':K('카오스','Chaos'),'show':['proj'],'edges':[{'if':{'has':'proj'},'to':'p5','res':'ok'},{'to':'p4','res':'fail'}],'item':_PJI},   # 6:34 화면
 {'id':'p5','kind':'act','group':'prep','pos':[0,7],'act':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'goal':K('접두 2개','Two prefixes'),'showText':[K('랜덤 옵션 2개','Two random lines')],'label':K('엑잘','Exalt'),'edges':[{'to':'p6'}],'item':_PJI+[_JK('p'),_JK('p')]},   # 7:01 징조 소모 메시지, 7:51 완벽한 엑잘티드 오브
 {'id':'p6','kind':'act','group':'prep','pos':[0,8],'act':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Dextral_Necromancy'],'goal':K('네번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),'showText':[K('훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],'label':K('훼손','Desecrate'),'edges':[{'to':'pA'}],'item':_PJI+[_JK('p'),_JK('p'),{'s':'s','kr':'훼손 옵션 (미공개)','en':'Desecrated (unrevealed)','m':'n'}]},   # 7:04 화면 미공개 훼손, 7:22~7:32 자막 '접미에만'·'고대 갈비뼈'
 {'id':'pA','kind':'act','group':'prep','pos':[0,9],'act':'rune','goal':K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),'showText':[K('제작 옵션 하나 더','One more crafted modifier')],'label':K('룬','Rune'),'rune':K('아스트리드의 창의성','Astrid’s Creativity'),'edges':[{'to':'p7'}],'item':_PJI+[_JK('p'),_JK('p'),{'s':'s','kr':'훼손 옵션 (미공개)','en':'Desecrated (unrevealed)','m':'n'}]},   # 8:06 장갑 4 장착(분열 8:48 전), 7:16 장갑 2 툴팁에도 '제작 옵션 1개 추가'
 {'id':'p7','kind':'act','group':'prep','pos':[0,10],'act':'fracture','cur':'Fracturing_Orb','goal':K('분열 (셋 중 하나)','Fracture (one of three)'),'showText':[K('투사체 +2가 분열되면 성공','Success when +2 projectile fractures')],'label':K('분열','Fracture'),'edges':[{'if':{'fractured':'proj'},'to':'p8','res':'ok','label':K('투사체 +2 분열','+2 projectile fractured')},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another line fractured')}],'item':[dict(_PJI[0],m='f')]},   # 7:20 실패(투사체 피해 분열), 8:48 성공
 {'id':'xj','kind':'exit','group':'prep','pos':[1,10],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),'note':K('투사체 +2가 아닌 옵션이 분열되면 이 장갑은 다른 용도로 두고 새 베이스로 처음부터','Another line fractured: set this one aside and start on a new base')},
 {'id':'p8','kind':'cleanup','group':'prep','pos':[0,11],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':[dict(_PJI[0],m='f'),_JK('p')]}]   # 12:15~12:27 화면
_g['nodes']=_prep+[n for n in _g['nodes'] if n['id']!='h1']
_g['start']='h1'
json.dump(_g,open(_gp,'w'),ensure_ascii=False,indent=1)
