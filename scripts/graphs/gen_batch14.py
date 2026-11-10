# Batch 14 (사용자 2026-11-10: 전문가부터는 2개씩, 영상 확인 후 바로잡기) — 전문가(4) → High-end (video) + Balance.
#   sl-flamewave-staff-v2 (6EzSVUItzsg), mazbro-caster-amulet-v2 (4PazhuHwdL8)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch12.py').read(); exec(_src[:_src.index('# ---------- 1. Master T')])
_s11=open(f'{H}/gen_batch11.py').read(); exec(_s11[_s11.index('def graph11'):_s11.index('def WHIT')])
P2={'high':{'v':1},'bal':{'v':2}}
def setg(id, **kv):
    g=json.load(open(f'{H}/{id}.json')); g.update(kv); json.dump(g,open(f'{H}/{id}.json','w'),ensure_ascii=False,indent=1)
V1={'param':{'v':1}}; V2={'param':{'v':2}}

# ---------- 1. SL 화염파 지팡이 (6EzSVUItzsg) ----------
# 영상: 화염 주문 +7 분열 + 잡옵 → 카오스 오브(피해 % 증가 1티어, 원소 무관 — 알두르의 배신) → 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브, 첫 옵션이 지워지면 카오스부터)
# → 좌측 강령술 + 고대 턱뼈 → 공개(빛의 징조로 다시). 가성비 마무리 = 엑잘 접미 2개 + 초월의 합금.
# 하이엔드 = 스루드의 완력 → 상위 찬미 + 완벽한 엑잘(잡옵 2개) → 절사의 징조 + 완벽한 카오스 오브(비고정 화염 속성 부여 규모 — 가중치 비공개, 영상 경험상 절사 20~30번)
# → 초월의 합금(접미 하나가 지워짐, 화염 규모가 지워지면 절사 카오스 다시). 알두르의 배신·아산드라 룬·영혼 핵·바알 오브는 취향이라 뺌(정책 23).
tags={'fire7':{'gi':12},'pd':{'anyOf':[{'gi':3,'tmax':1},{'gi':5,'tmax':1},{'gi':6,'tmax':1},{'gi':7,'tmax':1},{'gi':8,'tmax':1}],'label':K('피해 % 증가 1티어','T1 % increased damage')},
      'px':{'anyOf':[{'gi':32,'tmax':1},{'gi':33,'tmax':1},{'gi':34,'tmax':1}],'label':K('피해의 %를 추가 피해로 1티어','T1 damage as extra')},
      'pre':{'anyOf':['pd','px'],'label':K('피해 접두 1티어','T1 damage prefix')},
      'fm':{'gi':68},'alloy':{'gi':65},'keep':{'anyOf':['fm','alloy']}}
F7=it('s','모든 화염 주문 스킬 레벨 +7 (분열)','+7 fire spell skills (fractured)',['fire7'])
PD=it('p','피해 % 증가 1티어','T1 % increased damage',['pd']); PR=lambda: it('p','피해 접두 1티어','T1 damage prefix',['pre'])
FM=it('s','비고정 화염 속성 부여 규모 (스루드의 완력)','Explicit fire magnitudes (Thrud’s Might)',['fm']); AL=it('s','시전 속도 + 추가 냉기 (초월의 합금)','Cast speed + extra cold (Transcendent Alloy)',['alloy'])
S0=[F7,J('p')]; S1=[F7,PD]; S2=[F7,PD,PR()]; S3=[F7,PD,PR(),UN('p')]; S4=[F7,PD,PR(),PR()]
S5=S4+[J('s'),J('s')]; S6=S4+[FM,J('s')]; S7=S4+[FM,AL]; B1=S4+[J('s'),J('s')]; B2=S4+[J('s'),AL]
F={'res':'fail','port':'right'}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'fire7','fr':True},{'junk':'p'}]},K('모든 화염 주문 +7 분열 + 잡옵 1개','Fractured +7 fire spell skills + one junk line'),S0),
 mark([0,0.6],'p1',S0),
 act('p1','main',[0,1],'chaos','Chaos_Orb',K('피해 % 증가 1티어 (원소 무관)','T1 % increased damage (any element)'),None,K('카오스','Chaos'),[{'if':{'has':'pd'},'to':'p2','res':'ok'},{'to':'p1','res':'fail'}],S1,show=['pd']),
 act('p2','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'pre','min':2}},'to':'p3','res':'ok'},{'to':'p2x',**F}],S2,show=['pd','px'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('p2x',[1,2],[{'if':{'has':'pre'},'to':'p2','res':'ok','port':'right'},{'to':'p1','res':'fail'}],omens=(),target=K('빗나간 접두 지우기','Remove the missed prefix')),
 act('p3','main',[0,3],'desecrate','Ancient_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p4'}],S3,omens=['Omen_of_Sinistral_Necromancy']),
 act('p4','main',[0,4],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'all':[{'added':'pre'},V1]},'to':'r2','res':'ok'},{'if':V1,'to':'p4x',**F},{'if':{'added':'pre'},'to':'b1','res':'ok'},{'to':'b1','res':'fail'}],S4,want='pre',show=['pd','px'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('p4x',[1,4],'p3'),
 # 하이엔드
 act('r2','main',[0,5],'rune',None,K('스루드의 완력 장착','Socket Thrud’s Might'),[st(None,'파괴 속성 부여 가능','Can roll Destruction modifiers')],K('룬','Rune'),[{'to':'s1'}],S4),
 act('s1','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접미 잡옵 2개','Two junk suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'if':{'has':'fm'},'to':'s3','hide':True},{'to':'s2'}],S5,omens=['Omen_of_Greater_Exaltation']),
 act('s2','main',[0,7],'chaos','Perfect_Chaos_Orb',K('접미 : 비고정 화염 속성 부여 규모','Suffix: explicit fire magnitudes'),None,K('카오스','Chaos'),[{'if':{'has':'fm'},'to':'s3','res':'ok'},{'to':'s2','res':'fail'}],S6,show=['fm'],trim={'side':'s','keep':'keep'}),
 act('s3','main',[0,8],'essence','Transcendent_Alloy',K('접미 : 시전 속도 + 추가 냉기 (접미 하나가 지워짐)','Suffix: cast speed + extra cold (a suffix goes)'),[st('s','초월의 합금 (제작 옵션)','Transcendent Alloy (crafted)')],K('합금','Alloy'),
     [{'if':{'all':[{'has':'fm'},{'has':'alloy'}]},'to':'ok','res':'ok'},{'to':'s3m',**F}],S7,ess='alloy'),
 act('s3m','main',[1,8],'chaos','Perfect_Chaos_Orb',K('접미 : 비고정 화염 속성 부여 규모','Suffix: explicit fire magnitudes'),None,K('카오스','Chaos'),
     [{'if':{'all':[{'has':'fm'},{'has':'alloy'}]},'to':'ok','res':'ok'},{'if':{'has':'fm'},'to':'s3','res':'ok','port':'right'},{'to':'s3m','res':'fail'}],S7,show=['fm'],trim={'side':'s','keep':'keep'}),
 # 밸런스 (영상의 가성비 마무리)
 act('b1','main',[2,5],'exalt','Exalted_Orb',K('접미 잡옵 2개','Two junk suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'b2'}],B1,omens=['Omen_of_Greater_Exaltation']),
 act('b2','main',[2,6],'essence','Transcendent_Alloy',K('접미 : 시전 속도 + 추가 냉기 (접미 하나가 지워짐)','Suffix: cast speed + extra cold (a suffix goes)'),[st('s','초월의 합금 (제작 옵션)','Transcendent Alloy (crafted)')],K('합금','Alloy'),[{'to':'ok'}],B2,ess='alloy'),
 done([0,9])]
graph11('sl-flamewave-staff-v2','Staves','Chiming Staff',81,
  'SL 화염파 지팡이(6EzSVUItzsg) — 화염 주문 +7 분열 + 잡옵 → 카오스 오브(피해 % 증가 1티어) → 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브) → 좌측 강령술 + 고대 턱뼈 → 공개(빛의 징조로 다시). 하이엔드 = 스루드의 완력 → 상위 찬미 + 완벽한 엑잘 → 절사 + 완벽한 카오스 오브(화염 규모, 가중치 비공개: 영상 경험 절사 20~30번으로 맞춤) → 초월의 합금. 밸런스 = 영상의 가성비 마무리(엑잘 접미 2개 + 초월의 합금, 공개 결과 그대로).',
  ROUTE,P2,{'high':K('영상: 스루드의 완력으로 화염 규모, 공개는 빛의 징조로 다시','Video: Thrud’s Might fire magnitudes, Light retries the reveal'),'bal':K('영상의 가성비 마무리: 엑잘 접미 2개 + 초월의 합금, 공개 결과 그대로','Video budget finish: two exalted suffixes + Transcendent Alloy, reveal kept')},tags,nodes,
  [{'id':'L1','nodes':['p3','p4','p4x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'side':'p','label':K('피해 % 증가 1티어','T1 % increased damage')},{'side':'p','label':K('피해 접두 1티어','T1 damage prefix')},{'side':'p','label':K('피해 접두 1티어','T1 damage prefix')} if v=='high' else {'side':'p','random':True},
      {'tag':'fire7','tmax':1,'fr':True},{'tag':'fm'} if v=='high' else {'side':'s','random':True},{'tag':'alloy'}]),
  {'quality':20,'sockets':3},{'all':[{'has':'pd'},{'has':'alloy'}]},('high','bal'),xsub=["Thrud's Might"],xroll=True)

# ---------- 2. MazBro 캐스터 목걸이 (4PazhuHwdL8) ----------
# 영상: 정신력 50 분열 + 잡옵 → 카오스 오브(모든 주문 +3) → 좌측 찬미 + 상위 엑잘 2번(접두 잡옵) → 좌측 결정화 + 균열의 에센스(최대 퀄리티)
# → 우측 강령술 + 보존된 빗장뼈 → 공개(생명력 재생·능력치·저항으로 자리 막기, 빛의 징조로 다시) → 달리는 기폭제 40% → 촉진 + 우측 찬미 + 완벽한 엑잘(시전 속도·치명타·치명타 피해, 빗나가면 소멸의 오브)
# → 좌측 소멸의 징조 + 소멸의 오브(최대 퀄리티가 지워지면 좌측 결정화 + 균열의 에센스) → 신경 기폭제 40% → 촉진 + 완벽한 엑잘(마나 % · 마나 · 주문 피해)
# → 쇳소리 기폭제 → 절사의 징조 + 완벽한 카오스 오브(최대 퀄리티를 지우며 접두, 필요하면 좌측 말소의 징조) → 빛의 징조 + 소멸의 오브(막아 둔 옵션) → 검은 피의 징조 + 고대 빗장뼈 → 공개(모든 스킬 퀄리티, 빛의 징조로 다시).
# 빗나간 접미는 우측 소멸의 징조(영상 두 번째 목걸이: 주문 +3을 지킬 확률을 올림). 신성한 오브·축복받은 자의 징조는 뺌(정책 23).
tags={'spirit':{'gi':28},'spell':{'gi':17},'mq':{'gi':81},
      'blk':{'anyOf':[{'gi':21},{'gi':0},{'gi':1},{'gi':2},{'gi':3},{'gi':4},{'gi':5},{'gi':6},{'gi':7}],'label':K('생명력 재생·능력치·저항','Life regen, attribute or resistance')},
      'gs':{'anyOf':[{'gi':32,'tmax':1},{'gi':24,'tmax':1},{'gi':25,'tmax':1}],'label':K('시전 속도·치명타 1티어','T1 cast speed or crit')},
      'gp':{'anyOf':[{'gi':12,'tmax':1},{'gi':11,'tmax':1},{'gi':31,'tmax':1}],'label':K('마나·주문 피해 1티어','T1 mana or spell damage')},
      'kq':{'gi':46},'keep':{'anyOf':['gp']}}
SP=it('p','정신력 +50 (분열)','+50 Spirit (fractured)',['spirit']); SL=it('s','모든 주문 스킬 레벨 +3','+3 spell skills',['spell']); MQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% max quality (Essence of the Breach)',['mq'])
BK=it('s','생명력 재생·능력치·저항 (자리 막기)','Life regen, attribute or resistance (blocker)',['blk']); GS=it('s','시전 속도·치명타 1티어','T1 cast speed or crit',['gs'])
GP=lambda: it('p','마나·주문 피해 1티어','T1 mana or spell damage',['gp']); KQ=it('s','모든 스킬의 퀄리티 (쿠르갈)','Quality of all skills (Kurgal)',['kq'])
A0=[SP,J('s')]; A1=[SP,SL]; A2=[SP,J('p'),J('p'),SL]; A3=[SP,J('p'),MQ,SL]; A4=A3+[UN('s')]; A5=A3+[BK]; A6=A5+[GS]; A7=[SP,MQ,SL,BK,GS]; A8=[SP,GP(),MQ,SL,BK,GS]
A9=[SP,GP(),GP(),SL,BK,GS]; A10=[SP,GP(),GP(),SL,GS]; A11=A10+[UN('s')]; A12=A10+[KQ]
def R7(vis):   # after a missed suffix exalt (video: a plain Annulment) every step re-checks the item; only the edges in vis are drawn
    E=[{'if':{'not':{'has':'spell'}},'to':'a1r'},{'if':{'not':{'has':'mq'}},'to':'a7e'},{'if':{'full':'s'},'to':'a7x'},
       {'if':{'all':[{'des':False},{'sideLt':{'side':'s','n':2}}]},'to':'a4'},{'if':{'des':False},'to':'a7x'},{'to':'a6'}]
    out=[]
    for e in E:
        e=dict(e); v=vis.get(e['to'])
        if v is not None and not any(o['to']==e['to'] and not o.get('hide') for o in out): e.update(v if isinstance(v,dict) else {'res':v})
        else: e['hide']=True
        out.append(e)
    return out
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'s'}]},K('정신력 +50 분열 + 잡옵 1개','Fractured +50 Spirit + one junk line'),A0),
 mark([0,0.6],'a1',A0),
 act('a1','main',[0,1],'chaos','Chaos_Orb',K('접미 : 모든 주문 스킬 레벨 +3','Suffix: +3 spell skills'),None,K('카오스','Chaos'),[{'if':{'has':'spell'},'to':'a2','res':'ok'},{'to':'a1','res':'fail'}],A1,show=['spell']),
 act('a2','main',[0,2],'exalt','Greater_Exalted_Orb',K('접두 잡옵 2개','Two junk prefixes'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'if':{'sideLt':{'side':'p','n':3}},'to':'a2'},{'to':'a3'}],A2,omens=['Omen_of_Sinistral_Exaltation']),
 act('a3','main',[0,3],'essence','Essence_of_the_Breach',K('접두 하나를 지우고 최대 퀄리티','A prefix goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% max quality (crafted)')],K('에센스','Essence'),[{'to':'a4'}],A3,ess='mq',omens=['Omen_of_Sinistral_Crystallisation']),
 act('a4','main',[0,4],'desecrate','Preserved_Collarbone',K('접미 두번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'a5'}],A4,omens=['Omen_of_Dextral_Necromancy']),
 act('a5','main',[0,5],'reveal',None,K('훼손 옵션 확인 (자리 막기)','Reveal the desecrated modifier (blocker)'),None,K('공개','Reveal'),[{'if':{'added':'blk'},'to':'a6','res':'ok'},{'to':'a5x',**F}],A5,want='blk',show=['blk'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('a5x',[1,5],'a4'),
 act('a6','main',[0,6],'quality','Skittering_Catalyst',K('속도 퀄리티 40%','Speed quality 40%'),None,K('퀄리티','Quality'),[{'to':'a7'}],A5,count=40),
 act('a7','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접미 : 시전 속도·치명타 1티어','Suffix: T1 cast speed or crit'),None,K('엑잘','Exalt'),[{'if':{'all':[{'added':'gs'},{'sideLt':{'side':'p','n':3}}]},'to':'a9','res':'ok','hide':True},{'if':{'added':'gs'},'to':'a8','res':'ok'},{'to':'a7x',**F}],A6,show=['gs'],omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation']),
 annul('a7x',[1,7],R7({'a6':{'res':'ok','port':'right'},'a1r':'fail'}),omens=(),target=K('빗나간 접미 지우기','Remove the missed suffix')),
 act('a7e','main',[2,6],'essence','Essence_of_the_Breach',K('접두 하나를 지우고 최대 퀄리티','A prefix goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% max quality (crafted)')],K('에센스','Essence'),R7({'a6':{'res':'ok'}}),A5,ess='mq',omens=['Omen_of_Sinistral_Crystallisation']),
 resetx('a1r',[2,7],'a1'),
 annul('a8',[0,8],[{'if':{'has':'mq'},'to':'a9','res':'ok'},{'to':'a8e',**F}],omens=('Omen_of_Sinistral_Annulment',),target=K('잡옵 접두 지우기','Remove the junk prefix')),
 act('a8e','main',[1,8],'essence','Essence_of_the_Breach',K('접두 하나를 지우고 최대 퀄리티','A prefix goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% max quality (crafted)')],K('에센스','Essence'),[{'to':'a9','port':'bottom'}],A7,ess='mq',omens=['Omen_of_Sinistral_Crystallisation']),
 act('a9','main',[0,9],'quality','Neural_Catalyst',K('마나 퀄리티 40%','Mana quality 40%'),None,K('퀄리티','Quality'),[{'to':'a10'}],A7,count=40),
 act('a10','main',[0,10],'exalt','Perfect_Exalted_Orb',K('접두 : 마나·주문 피해 1티어','Prefix: T1 mana or spell damage'),None,K('엑잘','Exalt'),[{'if':{'added':'gp'},'to':'a11','res':'ok'},{'to':'a8',**F}],A8,show=['gp'],omens=['Omen_of_Catalysing_Exaltation']),
 act('a11','main',[0,11],'quality','Sibilant_Catalyst',K('시전 퀄리티 40%','Caster quality 40%'),None,K('퀄리티','Quality'),[{'to':'a12'}],A8,count=40),
 act('a12','main',[0,12],'chaos','Perfect_Chaos_Orb',K('최대 퀄리티를 지우며 접두 : 마나·주문 피해 1티어','Max quality out, prefix: T1 mana or spell damage'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'gp','min':2}},'to':'a13','res':'ok'},{'if':V2,'to':'a13','res':'fail','hide':True},{'to':'a12','res':'fail'}],A9,show=['gp'],trim={'side':'p','keep':'keep'}),
 annul('a13',[0,13],[{'to':'a14'}]),
 act('a14','main',[0,14],'desecrate','Ancient_Collarbone',K('접미 세번째 옵션(훼손, 쿠르갈)','Third suffix (desecrated, Kurgal)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'a15'}],A11,omens=['Omen_of_the_Blackblooded']),
 act('a15','main',[0,15],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'kq'},'to':'ok','res':'ok'},{'if':V1,'to':'a15x',**F},{'to':'ok','res':'fail'}],A12,want='kq',show=['kq'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('a15x',[1,15],'a14'),
 done([0,16])]
graph11('mazbro-caster-amulet-v2','Amulets','Solar Amulet',82,
  'MazBro 캐스터 목걸이(4PazhuHwdL8) — 정신력 50 분열 + 잡옵 → 카오스 오브(주문 +3) → 좌측 찬미 + 상위 엑잘 2번 → 좌측 결정화 + 균열의 에센스 → 우측 강령술 + 보존된 빗장뼈 → 공개(자리 막기) → 달리는 기폭제 + 촉진 + 우측 찬미 + 완벽한 엑잘(시전 속도·치명타, 빗나가면 우측 소멸의 징조) → 좌측 소멸의 징조(최대 퀄리티가 지워지면 균열의 에센스 다시) → 신경 기폭제 + 촉진 + 완벽한 엑잘(마나·주문 피해) → 쇳소리 기폭제 → 절사 + 완벽한 카오스 오브 → 빛의 징조 + 소멸의 오브 → 검은 피 + 고대 빗장뼈 → 공개(모든 스킬 퀄리티). 하이엔드 = 영상(절사 카오스로 좋은 접두 2개, 쿠르갈 공개는 빛의 징조로 다시), 밸런스 = 절사 카오스 한 번·공개 결과 그대로. 촉진하는 찬미의 징조 효과는 시뮬에 없음.',
  ROUTE,P2,{'high':K('영상: 절사 카오스로 좋은 접두 2개, 쿠르갈 공개는 빛의 징조로 다시','Video: Whittling chaos for two good prefixes, Light retries the Kurgal reveal'),
            'bal':K('절사 카오스 한 번(결과 그대로), 공개 결과 그대로','One Whittling chaos, reveal kept')},tags,nodes,
  [{'id':'L1','nodes':['a6','a7','a7x'],'kr':'접미 엑잘','en':'Suffix exalt'},{'id':'L2','nodes':['a8','a8e','a9','a10'],'kr':'접두 엑잘','en':'Prefix exalt'},{'id':'L3','nodes':['a14','a15','a15x'],'kr':'쿠르갈 공개','en':'Kurgal reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','tmax':1,'fr':True},{'side':'p','label':K('마나·주문 피해 1티어','T1 mana or spell damage')},{'side':'p','label':K('마나·주문 피해 1티어','T1 mana or spell damage')} if v=='high' else {'side':'p','random':True},
      {'tag':'spell','tmax':1},{'side':'s','label':K('시전 속도·치명타 1티어','T1 cast speed or crit')},{'tag':'kq'} if v=='high' else {'side':'s','random':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'spell'},{'has':'gs'},{'has':'gp'}]},('high','bal'))
