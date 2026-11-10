# Batch 15 (사용자 2026-11-10: 두 개 더, 영상 확인 후 바로잡기) — 전문가(4) → High-end (video) + Balance.
#   mazbro-spell5-amulet-v2 (kULlZJBSec4), gold-amulet-6line-v2 (cb36jD9pqsw)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch12.py').read(); exec(_src[:_src.index('# ---------- 1. Master T')])
_s11=open(f'{H}/gen_batch11.py').read(); exec(_s11[_s11.index('def graph11'):_s11.index('def WHIT')])
P2={'high':{'v':1},'bal':{'v':2}}; V1={'param':{'v':1}}
F={'res':'fail','port':'right'}
def ROUTE_(E, vis):   # every step re-checks the item; only the edges in vis are drawn
    out=[]
    for e in E:
        e=dict(e); v=vis.get(e['to'])
        if v is not None and not any(o['to']==e['to'] and not o.get('hide') for o in out): e.update(v if isinstance(v,dict) else {'res':v})
        else: e['hide']=True
        out.append(e)
    return out
def T(gis, tm=None): return {'anyOf':[dict({'gi':g}, **({'tmax':tm} if tm else {})) for g in gis]}

# ---------- 1. MazBro +5 부재 목걸이 (kULlZJBSec4) ----------
# 영상: 부재 목걸이(접두·접미 2개씩) 정신력 50 분열 + 잡옵 → (소멸의 오브로 옵션 1개) → 균열의 에센스(최대 퀄리티) → 쇳소리 기폭제 40%(주문 +3 → +4)
# → 카오스 오브로 모든 주문 +3(약 1/1000, 최대 퀄리티 옵션은 첫 카오스에 바뀌어도 퀄리티는 남음) → 좌측 찬미 + 상위 엑잘(접두) → 좌측 결정화 + 룬 합금(룬 수호)
# → 고대 빗장뼈(남은 접미) → 공개(시전 속도·치명타·모든 원소 저항·희귀도·모든 스킬 퀄리티, 빛의 징조로 다시) → 성유·완벽한 유동체·완벽한 쥬얼러 오브·신성한 오브 → 축성(+5, 약 13%).
# 촉진 + 완벽한 엑잘로 주문 +3·시전 속도를 같이 노리는 방법은 영상에서 20번에 1번 — 뺌. 성유~축성은 제작 옵션이 아니라 그림에서 뺌(레시피 하이엔드에는 남김).
tags={'spirit':{'gi':28,'tmax':1},'spell':{'gi':17,'tmax':1},'mq':{'gi':81},'rw':{'gi':82},
      'kq':{'gi':46},'cs':{'gi':32,'tmax':1},'cr':{'gi':24,'tmax':2},'cd':{'gi':25,'tmax':2},'ar':{'gi':7,'tmax':2},'rs':{'gi':26,'tmax':1},'fin':{'anyOf':['kq','cs','cr','cd','ar','rs']}}
SP=it('p','정신력 +50 (분열)','+50 Spirit (fractured)',['spirit']); SL=it('s','모든 주문 스킬 레벨 +3','+3 spell skills',['spell']); MQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% max quality (Essence of the Breach)',['mq'],'c')
RW=it('p','최대 룬 수호 % (룬 합금)','% max runic ward (Runic Alloy)',['rw'],'c'); FN=it('s','시전 속도','Cast speed',['cs'],'d')
M0=[SP,J('s')]; M1=[SP,MQ]; M2=[SP,SL]; M3=[SP,J('p'),SL]; M4=[SP,RW,SL]; M5=M4+[UN('s')]; M6=M4+[FN]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'s'}]},K('정신력 +50 분열 + 잡옵 1개 (부재 목걸이)','Fractured +50 Spirit + one junk line (Absent Amulet)'),M0),
 mark([0,0.6],'z7',M0),
 act('z7','main',[0,1],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티','The junk goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% max quality (crafted)')],K('에센스','Essence'),[{'to':'z8'}],M1,ess='mq'),
 act('z8','main',[0,2],'quality','Sibilant_Catalyst',K('시전 퀄리티 40%','Caster quality 40%'),[st(None,'쇳소리 기폭제 40개','40 Sibilant Catalysts')],K('퀄리티','Quality'),[{'to':'z9'}],M1,count=40),
 act('z9','main',[0,3],'chaos','Chaos_Orb',K('접미 : 모든 주문 스킬 레벨 +3','Suffix: +3 spell skills'),None,K('카오스','Chaos'),[{'if':{'has':'spell'},'to':'z10','res':'ok'},{'to':'z9','res':'fail'}],M2,show=['spell']),
 act('z10','main',[0,4],'exalt','Greater_Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'z11'}],M3,omens=['Omen_of_Sinistral_Exaltation']),
 act('z11','main',[0,5],'essence','Runic_Alloy',K('잡옵을 지우고 룬 수호','The junk goes for runic ward'),[st('p','최대 룬 수호 % (제작 옵션)','% max runic ward (crafted)')],K('합금','Alloy'),[{'to':'z12'}],M4,ess='rw',omens=['Omen_of_Sinistral_Crystallisation']),
 act('z12','main',[0,6],'desecrate','Ancient_Collarbone',K('접미 두번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'z13'}],M5),
 act('z13','main',[0,7],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'fin'},'to':'ok','res':'ok'},{'if':V1,'to':'z13x',**F},{'to':'ok','res':'fail'}],M6,want='fin',show=['fin'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('z13x',[1,7],'z12'),
 done([0,8])]
graph11('mazbro-spell5-amulet-v2','Amulets','Absent Amulet',81,
  'MazBro +5 부재 목걸이(kULlZJBSec4) — 정신력 50 분열 + 잡옵 → 균열의 에센스 → 쇳소리 기폭제 40% → 카오스 오브(주문 +3) → 좌측 찬미 + 상위 엑잘 → 좌측 결정화 + 룬 합금 → 고대 빗장뼈 → 공개. 하이엔드 = 영상(공개는 빛의 징조로 다시, 이후 성유·유동체·쥬얼러·신성한 오브·축성은 레시피에만), 밸런스 = 공개 결과 그대로·축성 없이 판매.',
  ROUTE,P2,{'high':K('영상: 공개는 빛의 징조로 다시, 그다음 축성(+5 약 13%)','Video: Light retries the reveal, then sanctify (+5 about 13%)'),'bal':K('공개 결과 그대로, 축성 없이','Reveal kept, no sanctify')},tags,nodes,
  [{'id':'L1','nodes':['z12','z13','z13x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','tmax':1,'fr':True},{'tag':'rw','ess':True},{'tag':'spell','tmax':1},{'tag':'cs','tmax':1,'des':True} if v=='high' else {'side':'s','random':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'spell'},{'has':'rw'}]},('high','bal'))

# ---------- 2. SL 6옵션 황금 목걸이 (cb36jD9pqsw) ----------
# 영상: 정신력 50 분열 + 잡옵 → 카오스 오브(주문 +3) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 균열의 에센스 → 기폭제 40% → 절사 + 완벽한 카오스 오브(최대 퀄리티를 날리며 접미 하나, 2티어 이상이면 멈춤.
# 접두로 가면 우측 찬미 + 완벽한 엑잘) → 접두: 좌측 찬미 + 완벽한 엑잘로 채움 → 잡옵 1개면 완벽한 강화의 에센스(1/2), 실패하면 보존된 빗장뼈로 잡옵 노리기(1/2, 빛의 징조로 지움),
# 잡옵 2개·잡옵이 끝까지 남으면 좌측 결정화 + 심연의 에센스(절사보다 쌈) — 징표가 접두면 빗장뼈 + 빛의 징조로 지우고 다시, 접미로 내려가면 마지막 접미 자리 → 고대 빗장뼈 훼손 → 공개.
GN=[('rs',26),('ar',7),('fr',4),('co',5),('li',6),('cs',32),('cr',24),('cd',25),('sd',31),('mp',12),('mf',11),('esf',13),('esp',16),('arp',14),('rp',27)]
tags={'spirit':{'gi':28,'tmax':1},'spell':{'gi':17,'tmax':1},'mq':{'gi':81},'enh':{'gi':74},'markP':{'gi':79},'markS':{'gi':80},
      **{n:{'gi':g,'tmax':2} for n,g in GN},'gs':{'anyOf':[n for n,_ in GN[:8]]},'gpn':{'anyOf':[n for n,_ in GN[8:]]},
      'gp':{'anyOf':['gpn','enh']},'keepS':{'anyOf':['spell','gs']}}
GS=it('s','희귀도','Rarity',['rs']); GP=lambda: it('p','주문 피해','Spell damage',['sd']); GP2=it('p','마나 최대치','Maximum mana',['mf'])
EN=it('p','방어 % (완벽한 강화의 에센스)','% defences (Perfect Essence of Enhancement)',['enh'],'c'); MK=lambda s: it(s,'심연 군주의 징표','Mark of the Abyssal Lord',['markP' if s=='p' else 'markS'],'c')
Q0=[SP,J('s')]; Q1=[SP,SL]; Q2=[SP,J('p'),SL]; Q3=[SP,MQ,SL]; Q4=[SP,SL,GS]; Q5=[SP,GP(),J('p'),SL,GS]; Q6=[SP,GP(),EN,SL,GS]; Q7=[SP,J('p'),SL,GS,MK('s')]; Q8=[SP,GP(),GP2,SL,GS,UN('s')]; Q9=[SP,GP(),GP2,SL,GS,it('s','시전 속도','Cast speed',['cs'],'d')]
def RS(vis):
    return ROUTE_([{'if':{'not':{'has':'spell'}},'to':'k1r'},{'if':{'has':'gs'},'to':'p1'},{'if':{'sideLt':{'side':'s','n':2}},'to':'s2'},{'to':'s1b'}],vis)
def RP(vis):
    full={'full':'p'}; g1={'count':{'tag':'gp','min':1}}; g2={'count':{'tag':'gp','min':2}}; two={'all':[{'sideLt':{'side':'p','n':3}},{'not':{'sideLt':{'side':'p','n':2}}}]}
    return ROUTE_([{'if':{'not':{'has':'spell'}},'to':'k1r'},{'if':{'unrev':True},'to':'pL'},{'if':{'has':'markP'},'to':'pB'},
       {'if':{'all':[g2,{'has':'markS'}]},'to':'dM'},{'if':g2,'to':'d1'},
       {'if':{'all':[two,{'not':g1},{'not':{'has':'markS'}},{'not':{'has':'enh'}}]},'to':'pA'},
       {'if':{'sideLt':{'side':'p','n':3}},'to':'p1'},
       {'if':{'all':[full,g1,{'not':{'has':'enh'}},{'not':{'has':'markS'}}]},'to':'pE'},
       {'if':{'all':[full,g1,{'not':{'has':'enh'}}]},'to':'pM'},
       {'if':{'all':[full,{'has':'enh'}]},'to':'pC'},
       {'if':{'has':'markS'},'to':'pM'},{'to':'pA'}],vis)
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'s'}]},K('정신력 +50 분열 + 잡옵 1개','Fractured +50 Spirit + one junk line'),Q0),
 mark([0,0.6],'k1',Q0),
 act('k1','main',[0,1],'chaos','Chaos_Orb',K('접미 : 모든 주문 스킬 레벨 +3','Suffix: +3 spell skills'),None,K('카오스','Chaos'),[{'if':{'has':'spell'},'to':'q1','res':'ok'},{'to':'k1','res':'fail'}],Q1,show=['spell']),
 resetx('k1r',[2,1],'k1'),
 act('q1','main',[0,2],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'q2'}],Q2,omens=['Omen_of_Sinistral_Exaltation']),
 act('q2','main',[0,3],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티','The junk goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% max quality (crafted)')],K('에센스','Essence'),[{'to':'q3'}],Q3,ess='mq',omens=['Omen_of_Sinistral_Crystallisation']),
 act('q3','main',[0,4],'quality','Sibilant_Catalyst',K('시전 퀄리티 40%','Caster quality 40%'),[st(None,'쇳소리 기폭제 40개','40 Sibilant Catalysts')],K('퀄리티','Quality'),[{'to':'s1'}],Q3,count=40),
 act('s1','main',[0,5],'chaos','Perfect_Chaos_Orb',K('최대 퀄리티를 지우고 접미 두번째 옵션','Max quality out, second suffix'),None,K('카오스','Chaos'),RS({'p1':'ok','s1b':F}),Q4,show=['gs'],omens=['Omen_of_Whittling']),
 act('s1b','main',[1,5],'chaos','Perfect_Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),RS({'p1':{'res':'ok'},'s2':F}),Q4,show=['gs'],trim={'side':'s','keep':'keepS'}),
 act('s2','main',[2,5],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),RS({'p1':{'res':'ok'},'s1b':{'res':'fail'}}),Q4,show=['gs'],omens=['Omen_of_Dextral_Exaltation']),
 act('p1','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefixes'),None,K('엑잘','Exalt'),RP({'d1':'ok','pE':F}),Q5,show=['gpn'],omens=['Omen_of_Sinistral_Exaltation']),
 act('pE','main',[1,6],'essence','Perfect_Essence_of_Enhancement',K('접두 하나를 지우고 방어 %','A prefix goes for % defences'),[st('p','방어 % (제작 옵션)','% defences (crafted)')],K('에센스','Essence'),RP({'d1':'ok','pC':F}),Q6,ess='enh',omens=['Omen_of_Sinistral_Crystallisation']),
 act('pC','main',[2,6],'desecrate','Preserved_Collarbone',K('접두 하나를 훼손으로 (잡옵 노리기)','A prefix into a desecration (hoping for the junk)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RP({'pL':{}}),Q6,omens=['Omen_of_Sinistral_Necromancy']),
 act('pA','main',[1,7],'essence','Essence_of_the_Abyss',K('잡옵을 지우고 심연 군주의 징표','The junk goes for the Abyssal Lord’s Mark'),[st(None,'심연 군주의 징표 (접두·접미 무관)','Mark of the Abyssal Lord (either side)')],K('심연','Abyss'),RP({'p1':{'res':'ok'},'pB':F}),Q7,ess='markS',alt='markP',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 act('pB','main',[2,7],'desecrate','Preserved_Collarbone',K('접두 징표 훼손','Desecrate the prefix Mark'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RP({'pL':{}}),Q7,fromMark=True),
 act('pM','main',[2,8],'desecrate','Preserved_Collarbone',K('접미 징표 훼손 (에센스 자리 비우기)','Desecrate the suffix Mark (free the essence slot)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RP({'pL':{}}),Q7,fromMark=True),
 annul('pL',[1,8],RP({'p1':{'port':'right'}})),
 act('dM','main',[0,9],'desecrate','Ancient_Collarbone',K('접미 세번째 옵션(징표 훼손)','Third suffix (desecrate the Mark)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],Q8,fromMark=True),
 act('d1','main',[0,10],'desecrate','Ancient_Collarbone',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],Q8),
 act('d2','main',[0,11],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'gs'},'to':'ok','res':'ok'},{'if':V1,'to':'d2x',**F},{'to':'ok','res':'fail'}],Q9,want='gs',show=['gs'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('d2x',[1,11],'d1'),
 done([0,12])]
nodes[0]['label']=K('정신력 +50 분열 + 잡옵 1개','Fractured +50 Spirit + one junk line')
graph11('gold-amulet-6line-v2','Amulets','Gold Amulet',82,
  'SL 6옵션 황금 목걸이(cb36jD9pqsw) — 정신력 50 분열 + 잡옵 → 카오스 오브(주문 +3) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 균열의 에센스 → 쇳소리 기폭제 → 절사 + 완벽한 카오스 오브(접미 하나, 접두로 가면 우측 찬미 + 완벽한 엑잘) → 좌측 찬미 + 완벽한 엑잘(접두) → 완벽한 강화의 에센스 / 보존된 빗장뼈 / 심연의 에센스로 잡옵 접두 정리 → 고대 빗장뼈 → 공개. 하이엔드 = 영상(공개는 빛의 징조로 다시), 밸런스 = 공개 결과 그대로.',
  ROUTE,P2,{'high':K('영상: 공개는 빛의 징조로 다시','Video: Light retries the reveal'),'bal':K('공개 결과 그대로, 나머지는 영상대로','Keep the reveal, the rest as in the video')},tags,nodes,
  [{'id':'L1','nodes':['d1','d2','d2x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','tmax':1,'fr':True},{'tag':'sd','tmax':2},{'tag':'mf','tmax':2},
      {'tag':'spell','tmax':1},{'tag':'rs','tmax':2},{'tag':'cs','tmax':2,'des':True} if v=='high' else {'side':'s','random':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'spell'},{'has':'gs'},{'count':{'tag':'gp','min':2}}]},('high','bal'))
