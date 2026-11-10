# Batch 10 (사용자 2026-11-10: 남은 레시피를 쉬운 것부터) — 어려움(3) → Balance (video) + Essential (results kept).
#   sl-5mod-jewel-v2, vodnarg-timelost-emerald-v2, lilbotq-boots-v2, mazbro-caster-ring-v2
# Sim addition: augment / Otherworldly lines join the reveal pool for the socketed rune (graph.xsub) or an Altered bone, weighted like desecrated-only lines (estimate).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch9.py').read(); exec(_src[:_src.index('# ---------- 1. LilBotQ')])
RUNE=lambda id,pos,nxt,item: act(id,'main',pos,'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':nxt}],item)
ROUTE={'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}}
PV={'bal':{'v':1},'ess':{'v':2}}
def graph10(*a, cap=None, xsub=None, **k):
    graph8(*a, **k); g=json.load(open(f'{H}/{a[0]}.json'))
    if cap: g['cap']=cap
    if xsub: g['xsub']=xsub
    json.dump(g,open(f'{H}/{a[0]}.json','w'),ensure_ascii=False,indent=1)
def REVEAL(id,pos,want,show,ok,retry,item,omens=('Omen_of_Abyssal_Echoes',)):
    return act(id,'main',pos,'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
        [{'if':{'added':want},'to':ok,'res':'ok'},{'if':{'param':{'v':1}},'to':retry,'res':'fail'},{'to':ok,'res':'fail'}],item,want=want,show=show,omens=list(omens))

# ---------- 1. SL 5옵션 사파이어 (VKMT7tuSIYk) ----------
# 원본: 상태 이상 가속 분열 + 잡옵 → 카오스 오브(접두) → 좌측 찬미 + 엑잘(다른 접두, 빗나가면 소멸의 오브) → 엑잘(접미 잡옵) → 위력적인 액체 경멸(+1 접두 허용)
# → 보존된 두개골(세번째 접두) → 공개 → 우측 소멸의 징조(경멸 옵션 제거) → 엑잘(접미 잡옵) → 위력적인 액체 흉포함(접두 효과).
PRE=[29,1,49,4,53]
tags={'ail':{'gi':24},**{f'p{g}':{'gi':g} for g in PRE},'pre':{'anyOf':[f'p{g}' for g in PRE],'label':K('점화·상태 이상·주문·카오스·위축','Ignite, ailment, spell, chaos or wither')},
      'contP':{'gi':104,'slot':{'p':1}},'contS':{'gi':103,'slot':{'s':1}},'fer':{'gi':102}}
AI=it('s','상태 이상 가속 (분열)','Faster ailments (fractured)',['ail']); PR=lambda: it('p','원하는 접두','Wanted prefix',['pre']); CP=it('s','+1 접두 허용','+1 prefix allowed',['contP']); FP=it('s','접두 효과 증가','Increased effect of prefixes',['fer'])
I0=[AI,J('p')]; I1=[AI,PR()]; I2=I1+[PR()]; I3=I2+[J('s')]; I4=[AI,PR(),PR(),CP]; I5=I4+[UN('p')]; I6=[AI,PR(),PR(),PR(),CP]; I7=I6[:4]; I8=I7+[J('s')]; I9=I7+[FP]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'ail','fr':True},{'junk':'p'}]},K('상태 이상 가속 분열 + 잡옵 1개 사파이어','Sapphire: fractured faster ailments + one junk line'),I0),
 mark([0,0.6],'s2',I0),
 act('s2','main',[0,1],'chaos','Chaos_Orb',K('접두 첫번째 옵션','First prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pre'},'to':'s3','res':'ok'},{'to':'s2','res':'fail'}],I1,show=[f'p{g}' for g in PRE]),
 act('s3','main',[0,2],'exalt','Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'pre','min':2}},'to':'s4','res':'ok'},{'to':'s3x','res':'fail'}],I2,show=[f'p{g}' for g in PRE],omens=['Omen_of_Sinistral_Exaltation']),
 cleanup('s3x',[1,2],['pre'],[{'lost':'pre','to':'s2','port':'right'},{'to':'s3','port':'bottom'}],K('빗나간 접두 지우기','Remove the missed prefix')),
 act('s4','main',[0,3],'exalt','Exalted_Orb',K('접미 두번째 옵션','Second suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'s5'}],I3),
 LIQ('s5',[0,4],'Potent_Liquid_Contempt','contP',K('위력적인 액체 경멸 (50%로 +1 접두 허용)','Potent Liquid Contempt (50%: +1 prefix allowed)'),[st('s','+1 접두 허용 (아니면 +1 접미 허용 → 접두가 지워짐)','+1 prefix allowed (else +1 suffix allowed takes a prefix)')],
     [{'if':{'has':'contP'},'to':'s6','res':'ok'},{'to':'s5x','res':'fail'}],I4,alt='contS'),
 cleanup('s5x',[1,4],[],[{'to':'s2','port':'right'}],K('분열 + 옵션 1개로 되돌리기','Back to the fracture + one line'),maxJunk=1),
 act('s6','main',[0,5],'desecrate','Preserved_Cranium',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'s7'}],I5),
 REVEAL('s7',[0,6],'pre',[f'p{g}' for g in PRE],'s8','s7x',I6),
 LIGHTX('s7x',[1,6],'s6'),
 act('s8','main',[0,7],'annul','Orb_of_Annulment',K('+1 접두 허용 옵션 제거','Remove the +1 prefix line'),None,K('소멸','Annul'),[{'to':'s9'}],I7,omens=['Omen_of_Dextral_Annulment']),
 act('s9','main',[0,8],'exalt','Exalted_Orb',K('흉포함이 지울 접미','The suffix for Ferocity to remove'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'s11'}],I8),
 LIQ('s11',[0,9],'Potent_Liquid_Ferocity','fer',K('위력적인 액체 흉포함 (접미 잡옵이 지워짐)','Potent Liquid Ferocity (the junk suffix goes)'),[st('s','접두 효과 증가','Increased effect of prefixes')],[{'to':'ok'}],I9),
 done([0,10])]
graph10('sl-5mod-jewel-v2','Sapphire','Sapphire',81,
  'SL 5옵션 사파이어(원본 레시피 기록) — 상태 이상 가속 분열 + 잡옵 → 카오스 오브(접두) → 좌측 찬미 + 엑잘(다른 접두, 빗나가면 소멸의 오브) → 엑잘(접미) → 위력적인 액체 경멸(+1 접두 허용, 아니면 분열 + 옵션 1개로 되돌림) → 보존된 두개골 → 공개(밸런스 = 빛의 징조로 다시) → 우측 소멸의 징조 → 엑잘 → 위력적인 액체 흉포함. 신성한 오브·차율라의 기폭제는 마무리라 뺌.',
  ROUTE,PV,{'bal':K('영상: 공개가 빗나가면 빛의 징조로 다시','Video: Light on a missed reveal'),'ess':K('공개 결과 그대로','Keep the reveal')},tags,nodes,
  [{'id':'L1','nodes':['s6','s7','s7x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('bal','ess'),lambda v:[{'side':'p','label':K('원하는 접두','Wanted prefix')},{'side':'p','label':K('원하는 접두','Wanted prefix')},{'side':'p','label':K('원하는 접두','Wanted prefix')} if v=='bal' else {'side':'p','random':True},{'tag':'ail','tmax':1,'fr':True},{'tag':'fer','tmax':1}]),
  {'quality':20,'sockets':0},{'all':[{'count':{'tag':'pre','min':2}},{'has':'fer'}]},('bal','ess'),cap={'p':2,'s':2})

# ---------- 2. Vodnarg 오래된 에메랄드 (3tFs16SXkD8) ----------
# 원본: 원하는 접미 옵션 2개 + 접두 옵션 2개 구입 → 고대 위력적인 액체 경멸(+1 접미 허용 50%) → 우측 강령술 + 보존된 두개골 → 공개 → 좌측 말소의 징조 + 카오스 오브(경멸 옵션 지우기)
# → 카오스 오브(좋은 접두) → 고대 위력적인 액체 우울(범위 아주 큼, 접두 하나가 지워짐 1/2).
SUFA=[11,65]; REV=[8,64,9]; GP=[54,66,55,10]
tags={**{f's{g}':{'gi':g} for g in SUFA+REV},'suf':{'anyOf':[f's{g}' for g in SUFA],'label':K('핵심 패시브 접미','Notable suffix')},'rev':{'anyOf':[f's{g}' for g in REV],'label':K('핵심 패시브 접미','Notable suffix')},
      **{f'p{g}':{'gi':g} for g in GP},'pre':{'anyOf':[f'p{g}' for g in GP],'label':K('반경 패시브 접두','Radius passive prefix')},
      'contS':{'gi':101,'slot':{'s':1}},'contP':{'gi':102,'slot':{'p':1}},'rad':{'gi':99}}
SU=lambda: it('s','핵심 패시브 접미','Notable suffix',['suf']); CS2=it('p','+1 접미 허용','+1 suffix allowed',['contS']); RV=it('s','공개 접미','Revealed suffix',['rev']); GPI=it('p','반경 패시브 접두','Radius passive prefix',['pre']); RD=it('p','범위 아주 큼','Very large radius',['rad'])
I0=[SU(),SU(),J('p'),J('p')]; I1=[SU(),SU(),J('p'),CS2]; I2=I1+[UN('s')]; I3=[SU(),SU(),RV,J('p'),CS2]; I4=[SU(),SU(),RV,J('p'),J('p')]; I5=[SU(),SU(),RV,GPI,J('p')]; I6=[SU(),SU(),RV,GPI,RD]
nodes=[base('ms',{'rar':'rare','mods':['s11','s65',{'junk':'p'},{'junk':'p'}]},K('원하는 접미 옵션 2개 + 접두 옵션 2개 희귀 오래된 에메랄드 구입','Buy a rare Time-Lost Emerald: two wanted suffixes + two prefixes'),I0),
 mark([0,0.6],'v2',I0),
 LIQ('v2',[0,1],'Ancient_Potent_Liquid_Contempt','contS',K('고대 위력적인 액체 경멸 (50%로 +1 접미 허용)','Ancient Potent Liquid Contempt (50%: +1 suffix allowed)'),[st('p','+1 접미 허용 (아니면 접미가 지워져 새 주얼)','+1 suffix allowed (else a suffix goes: new jewel)')],
     [{'if':{'has':'contS'},'to':'v3','res':'ok'},{'to':'h1','res':'fail','port':'right'}],I1,alt='contP'),
 act('v3','main',[0,2],'desecrate','Preserved_Cranium',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'v4'}],I2,omens=['Omen_of_Dextral_Necromancy']),
 REVEAL('v4',[0,3],'rev',[f's{g}' for g in REV],'v5','v4x',I3),
 LIGHTX('v4x',[1,3],'v3'),
 act('v5','main',[0,4],'chaos','Chaos_Orb',K('+1 접미 허용 옵션 지우기 (접두만 바뀜)','Reroll the +1 suffix line away (prefixes only)'),None,K('카오스','Chaos'),[{'if':{'has':'contS'},'to':'v5','res':'fail'},{'to':'v6','res':'ok'}],I4,omens=['Omen_of_Sinistral_Erasure']),
 act('v6','main',[0,5],'chaos','Chaos_Orb',K('좋은 접두 (접미가 한도를 넘어 접두만 바뀜)','A good prefix (only prefixes change)'),None,K('카오스','Chaos'),
     [{'if':{'has':'pre'},'to':'v7','res':'ok'},{'to':'v6','res':'fail'}],I5,show=[f'p{g}' for g in GP],
     over=[{'param':{'v':2},'set':{'edges':[{'to':'v7'}],'goal':K('접두 한 번 다시 (결과 그대로)','One prefix reroll (keep it)')}}]),
 LIQ('v7',[0,6],'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 (접두 하나가 지워짐)','Ancient Potent Liquid Melancholy (one prefix goes)'),[st('p','범위 아주 큼','Very large radius')],
     [{'if':{'param':{'v':2}},'to':'ok','res':'ok'},{'if':{'has':'pre'},'to':'ok','res':'ok'},{'to':'v6','res':'fail','port':'right'}],I6),
 done([0,7])]
graph10('vodnarg-timelost-emerald-v2','Time-Lost_Emerald','Time-Lost Emerald',80,
  'Vodnarg 오래된 에메랄드(원본 레시피 기록) — 원하는 접미 옵션 2개 + 접두 옵션 2개 구입 → 고대 위력적인 액체 경멸(+1 접미 허용, 아니면 새 주얼) → 우측 강령술 + 보존된 두개골 → 공개(밸런스 = 빛의 징조로 다시) → 좌측 말소의 징조 + 카오스 오브(경멸 옵션 지우기) → 카오스 오브(좋은 접두, 밸런스) → 고대 위력적인 액체 우울. 오래된',
  ROUTE,PV,{'bal':K('영상: 빛의 징조로 다시 공개, 좋은 접두까지 카오스 오브','Video: Light retries, Chaos until a good prefix'),'ess':K('공개 결과 그대로, 접두 카오스 한 번','Keep the reveal, one prefix Chaos')},tags,nodes,
  [{'id':'L1','nodes':['v3','v4','v4x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['v6','v7'],'kr':'우울','en':'Melancholy'}],
  FIN(('bal','ess'),lambda v:[{'side':'p','label':K('반경 패시브 접두','Radius passive prefix')} if v=='bal' else {'side':'p','random':True},{'tag':'rad','tmax':1},{'side':'s','label':K('핵심 패시브 접미','Notable suffix')},{'side':'s','label':K('핵심 패시브 접미','Notable suffix')},{'side':'s','label':K('핵심 패시브 접미','Notable suffix')} if v=='bal' else {'side':'s','random':True}]),
  {'quality':0,'sockets':0},{'all':[{'count':{'tag':'suf','min':2}},{'has':'rad'}]},('bal','ess'),cap={'p':2,'s':2})

# ---------- 3. LilBotQ 고급 장화 (S-7YHuq3-P4) ----------
# 원본: 우트레드의 성좌 장착 + 이동 속도·둔화 감소 분열 + 번개 저항 + 희귀도(상위 풍요의 에센스) + 미공개 훼손 접두(퀄리티 26%) → 아스트리드 → 좌측 결정화 + 신비한 합금(정신력, 미공개 훼손이 지워짐)
# → 완벽한 엑잘(방어도·생명력 접두, 빗나가면 좌측 말소의 징조 + 카오스 오브) → 고대 갈비뼈 → 공개(우트레드 구르기 거리, 빛의 징조로 다시).
tags={'ms':{'gi':55},'lres':{'gi':3,'tmax':1},'rar':{'gi':44},'spirit':{'gi':51},'flat':{'gi':7,'tmax':1},'pct':{'gi':8,'tmax':2},'life':{'gi':5,'tmax':2},
      'pre':{'anyOf':['flat','pct','life'],'label':K('방어도·생명력 접두','Armour or life prefix')},'dodge':{'gi':57,'tmax':2}}
MS=it('p','이동 속도·둔화 감소 (분열, 우트레드)','Movement speed + slow reduction (fractured, Uhtred)',['ms']); LR=it('s','번개 저항 1티어','T1 lightning resistance',['lres']); RA=it('s','희귀도 (제작 옵션)','Rarity (crafted)',['rar'])
SP=it('s','정신력 (합금)','Spirit (alloy)',['spirit']); PRE2=it('p','방어도·생명력 접두','Armour or life prefix',['pre']); DG=it('p','구르기 거리 (우트레드)','Dodge roll distance (Uhtred)',['dodge'])
I0=[MS,UN('p'),LR,RA]; I1=[MS,LR,RA,SP]; I2=[MS,PRE2,LR,RA,SP]; I3=[MS,PRE2,UN('p'),LR,RA,SP]; I4=[MS,PRE2,DG,LR,RA,SP]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'ms','fr':True},'lres',{'tag':'rar','ess':True},{'unrev':'p','bone':'Ancient_Rib'}]},K('우트레드의 성좌 장착, 이동 속도 분열 + 번개 저항 + 희귀도 + 미공개 훼손 (퀄리티 26%, 특출난 베이스)','Uhtred socketed: fractured movement speed + lightning res + rarity + unrevealed desecration (26% quality, exceptional)'),I0),
 mark([0,0.6],'h2',I0),
 RUNE('h2',[0,1],'h3',I0),
 act('h3','main',[0,2],'essence','Mystic_Alloy',K('미공개 훼손 접두를 지우고 접미 정신력','Swap the unrevealed prefix for Spirit'),[st('s','정신력 (제작 옵션)','Spirit (crafted)')],K('합금','Alloy'),[{'to':'h4'}],I1,ess='spirit',omens=['Omen_of_Sinistral_Crystallisation']),
 act('h4','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'pre'},'to':'h5','res':'ok'},{'if':{'param':{'v':1}},'to':'h4b','res':'fail'},{'to':'h5','res':'fail'}],I2,show=['flat','pct','life']),
 act('h4b','main',[1,3],'chaos','Chaos_Orb',K('접두 다시','Reroll the prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pre'},'to':'h5','res':'ok'},{'to':'h4b','res':'fail'}],I2,show=['flat','pct','life'],omens=['Omen_of_Sinistral_Erasure']),
 act('h5','main',[0,4],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'h6'}],I3),
 REVEAL('h6',[0,5],'dodge',['dodge'],'ok','h6x',I4),
 LIGHTX('h6x',[1,5],'h5'),
 done([0,6])]
nodes[0]['group']='prep'
graph10('lilbotq-boots-v2','Boots_str','Tasalian Greaves',82,
  'LilBotQ 고급 장화(원본 레시피 기록) — 우트레드의 성좌 장착 + 이동 속도 분열 + 번개 저항 + 희귀도 + 미공개 훼손 → 아스트리드 → 좌측 결정화 + 신비한 합금(정신력) → 완벽한 엑잘(방어도·생명력, 밸런스는 빗나가면 좌측 말소의 징조 + 카오스 오브) → 고대 갈비뼈 → 공개(우트레드 구르기 거리, 밸런스 = 빛의 징조로 다시). 우트레드 옵션은 공개 가중치가 없어 훼손 전용 옵션과 같은 기준으로 추정.',
  ROUTE,PV,{'bal':K('영상: 접두 말소 반복, 구르기 거리까지 빛의 징조','Video: Erasure for the prefix, Light until dodge roll'),'ess':K('엑잘·공개 결과 그대로','Keep the exalt and the reveal')},tags,nodes,
  [{'id':'L1','nodes':['h5','h6','h6x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('bal','ess'),lambda v:[{'tag':'ms','tmax':1,'fr':True},{'side':'p','label':K('방어도·생명력 접두','Armour or life prefix')} if v=='bal' else {'side':'p','random':True},{'tag':'dodge','tmax':2} if v=='bal' else {'side':'p','random':True},{'tag':'lres','tmax':1},{'tag':'rar','tmax':1},{'tag':'spirit','tmax':1}]),
  {'quality':26,'sockets':3},{'all':[{'has':'ms'},{'has':'spirit'},{'full':'p'},{'full':'s'}]},('bal','ess'),xsub=["Uhtred's Sidereus"])

# ---------- 4. MazBro 캐스터 반지 (o3Fh1DJmxBA) ----------
# 원본: 시전 속도 1티어 분열 + 잡옵 → 좌측 결정화 + 균열의 에센스 → 신경 기폭제 40% (+ 주입기 1회 41%) → 카오스 오브(마나 재생·희귀도·모든 원소 저항 1티어, 최대 퀄리티가 바뀜)
# → 좌측 찬미 + 엑잘 → 좌측 결정화 + 정신의 에센스(마나 %) → 좌측 찬미 + 상위 엑잘(마나 최대치 1티어) → 우측 찬미 + 엑잘(접미)
# → 마나 1티어면 뒤바뀐 빗장뼈 → 공개(받는 피해를 마나로, 이계 옵션), 아니면 고대 빗장뼈 → 공개(마나 1티어). 순서는 정신의 에센스가 마나 옵션을 지우지 않게 바꿈(영상은 마나 엑잘 먼저).
tags={'cast':{'gi':34,'tmax':1},'maxQ':{'gi':71},'regen':{'gi':21,'tmax':1},'rar':{'gi':27,'tmax':1},'res':{'gi':7,'tmax':1},'good':{'anyOf':['regen','rar','res'],'label':K('마나 재생·희귀도·모든 원소 저항 1티어','T1 mana regen, rarity or all res')},
      'pmana':{'gi':67},'mana':{'gi':10,'tmax':1},'manaAny':{'gi':10},'mom':{'gi':87}}
CA=it('s','시전 속도 1티어 (분열)','T1 cast speed (fractured)',['cast']); MQ=it('p','최대 퀄리티 +20% (제작 옵션)','+20% maximum quality (crafted)',['maxQ']); GD=it('s','마나 재생·희귀도·저항','Mana regen, rarity or res',['good'])
PM=it('p','마나 최대치 % (제작 옵션)','% maximum mana (crafted)',['pmana']); MA=it('p','마나 최대치 1티어','T1 maximum mana',['mana']); MO=it('p','받는 피해를 마나로 (이계)','Damage taken from mana (Otherworldly)',['mom'])
I0=[CA,J('p')]; I1=[CA,MQ]; I2=[CA,GD]; I3=I2+[J('p')]; I4=I2+[PM]; I5=I4+[MA]; I6=I5+[J('s')]; I7=I6+[UN('p')]; I8=[CA,GD,J('s'),PM,MA,MO]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'cast','fr':True},{'junk':'p'}]},K('시전 속도 1티어 분열 + 잡옵 1개 기억 반지','Mnemonic Ring: fractured T1 cast speed + one junk line'),I0),
 mark([0,0.6],'r5',I0),
 act('r5','main',[0,1],'essence','Essence_of_the_Breach',K('접두 잡옵을 최대 퀄리티로','Swap the junk prefix for maximum quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% maximum quality (crafted)')],K('에센스','Essence'),[{'to':'r6'}],I1,ess='maxQ',omens=['Omen_of_Sinistral_Crystallisation']),
 act('r6','main',[0,2],'quality','Neural_Catalyst',K('마나 퀄리티 40%','Mana quality 40%'),[st(None,'신경 기폭제 40개 (+ 바알 촉진시키는 주입기 1회로 41%)','40 Neural Catalysts (+ one infuser for 41%)')],K('퀄리티','Quality'),[{'to':'r8'}],I1,count=40),
 act('r8','main',[0,3],'chaos','Chaos_Orb',K('최대 퀄리티 옵션을 좋은 접미로','Replace maximum quality with a good suffix'),None,K('카오스','Chaos'),[{'if':{'has':'good'},'to':'r10','res':'ok'},{'to':'r8','res':'fail'}],I2,show=['regen','rar','res']),
 act('r10','main',[0,4],'exalt','Exalted_Orb',K('에센스가 지울 접두','The prefix for the essence to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'r10b'}],I3,omens=['Omen_of_Sinistral_Exaltation']),
 act('r10b','main',[0,5],'essence','Essence_of_the_Mind',K('접두 잡옵을 마나 %로','Swap the junk prefix for % mana'),[st('p','마나 최대치 % (제작 옵션)','% maximum mana (crafted)')],K('에센스','Essence'),[{'to':'r9'}],I4,ess='pmana',omens=['Omen_of_Sinistral_Crystallisation']),
 act('r9','main',[0,6],'exalt','Greater_Exalted_Orb',K('접두 두번째 옵션 (마나 최대치 1티어)','Second prefix (T1 maximum mana)'),None,K('엑잘','Exalt'),[{'if':{'has':'mana'},'to':'r11','res':'ok'},{'to':'r11','res':'fail'}],I5,show=['mana'],omens=['Omen_of_Sinistral_Exaltation']),
 act('r11','main',[0,7],'exalt','Exalted_Orb',K('남은 접미','The last suffix'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'if':{'has':'manaAny'},'to':'r12','res':'ok'},{'to':'r12b','res':'fail'}],I6,omens=['Omen_of_Dextral_Exaltation']),
 act('r12','main',[0,8],'desecrate','Altered_Collarbone',K('접두 세번째 옵션(훼손, 이계)','Third prefix (desecrated, Otherworldly)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'r13'}],I7),
 REVEAL('r13',[0,9],'mom',['mom'],'ok','r13x',I8),
 LIGHTX('r13x',[1,9],'r12'),
 act('r12b','main',[2,8],'desecrate','Ancient_Collarbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'r13b'}],I7),
 REVEAL('r13b',[2,9],'mana',['mana'],'ok','r13bx',I8),
 LIGHTX('r13bx',[3,9],'r12b'),
 done([0,10])]
graph10('mazbro-caster-ring-v2','Rings','Mnemonic Ring',82,
  'MazBro 캐스터 반지(원본 레시피 기록) — 시전 속도 분열 + 잡옵 → 좌측 결정화 + 균열의 에센스 → 신경 기폭제 → 카오스 오브(마나 재생·희귀도·모든 원소 저항 1티어) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 정신의 에센스 → 좌측 찬미 + 상위 엑잘(마나 1티어) → 우측 찬미 + 엑잘 → 마나 최대치가 붙었으면 뒤바뀐 빗장뼈(받는 피해를 마나로), 아니면 고대 빗장뼈(마나 1티어). 밸런스 = 빛의 징조로 다시. 이계 옵션은 공개 가중치가 없어 추정. 신성한 오브·주입기는 뺌.',
  ROUTE,PV,{'bal':K('영상: 빛의 징조로 다시 공개','Video: Light retries on the reveal'),'ess':K('공개 결과 그대로','Keep the reveal')},tags,nodes,
  [{'id':'L1','nodes':['r12','r13','r13x'],'kr':'이계 공개','en':'Otherworldly reveal'},{'id':'L2','nodes':['r12b','r13b','r13bx'],'kr':'마나 공개','en':'Mana reveal'}],
  FIN(('bal','ess'),lambda v:[{'tag':'pmana','tmax':1},{'tag':'mana','tmax':1},{'side':'p','label':K('받는 피해를 마나로 또는 마나 1티어','Damage from mana or T1 mana')} if v=='bal' else {'side':'p','random':True},{'tag':'cast','tmax':1,'fr':True},{'side':'s','label':K('마나 재생·희귀도·모든 원소 저항 1티어','T1 mana regen, rarity or all res')},{'side':'s','random':True}]),
  {'quality':41,'sockets':0},{'all':[{'has':'cast'},{'has':'pmana'},{'has':'good'},{'full':'p'},{'full':'s'}]},('bal','ess'))
print('wrote 4 graphs (batch 10)')
