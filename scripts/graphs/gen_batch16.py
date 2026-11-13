# Batch 16 (사용자 2026-11-10: 나머지도 순차적으로) — 전문가(4) → High-end (video) + Balance. Videos rechecked 2026-11-10 (transcripts).
#   absent-amulet-video-v2 (SL jr6-YLMJsC8), sl-flamewave-ring-v2 (SL UAF91gEFRkM)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch15.py').read(); exec(_src[:_src.index('# ---------- 1. MazBro')])
F={'res':'fail','port':'right'}
PT={'high':{'v':1,'pT':1},'bal':{'v':2,'pT':2}}

# ---------- 1. SL 부재 목걸이 심연의 에센스 (jr6-YLMJsC8) ----------
# 영상: 정신력 50 분열 + 잡옵 → 카오스 오브(모든 주문 +3, 약 1,700개) → 좌측 찬미 + 엑잘(접두 잡옵) → 좌측 결정화 + 균열의 에센스 → 쇳소리 기폭제 40%
# → 검은 피의 징조 + 보존된 빗장뼈(접미) → 심연의 메아리 공개(모든 스킬의 퀄리티, 안 나와도 빛의 징조는 아직) → 절사의 징조 + 완벽한 카오스 오브(최대 퀄리티를 지우며 접두)
# → 접두가 좋으면 빛의 징조 + 검은 피 빗장뼈 반복. 둘 다 아니면 빛의 징조로 훼손 제거 → 좌측 결정화 + 심연의 에센스(잡옵 접두를 지우고 징표, 접두·접미 반반)
#   징표가 접두 = 보존된 빗장뼈 + 빛의 징조로 지우고 좌측 찬미 + 완벽한 엑잘 / 접미 = 완벽한 엑잘(접두) → 징표 접미를 검은 피 빗장뼈로 훼손 → 공개.
# 공개는 됐는데 접두가 잡옵: 하이엔드 = 절사 돌리기(영상 "죽어도 그 옵션"), 밸런스 = 좌측 결정화 + 완벽한 강화의 에센스(영상의 가성비 마무리).
GP=[('esf',13),('esp',16),('sd',31),('lf',9)]
tags={'spirit':{'gi':28,'tmax':1},'spell':{'gi':17,'tmax':1},'mq':{'gi':81},'enh':{'gi':74},'markP':{'gi':79},'markS':{'gi':80},'kq':{'gi':46},
      **{n:{'gi':g,'tmax':'$pT'} for n,g in GP},'gp':{'anyOf':[n for n,_ in GP]},'keepT':{'anyOf':['spell','kq']},'mark':{'anyOf':['markP','markS']}}
SP=it('p','정신력 +50 (분열)','+50 Spirit (fractured)',['spirit']); SL=it('s','모든 주문 스킬 레벨 +3','+3 to Level of all Spell Skills',['spell'])
MQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% to Maximum Quality (Essence of the Breach)',['mq'],'c')
KQ=it('s','모든 스킬의 퀄리티 +(3—5)%','+(3—5)% to Quality of all Skills',['kq'],'d')
ES=it('p','에너지 보호막 최대치 (45—50)% 증가','(45—50)% increased maximum Energy Shield',['esp'])
EN=it('p','일반 방어도, 회피, 에너지 보호막 (20—30)% 증가 (완벽한 강화의 에센스)','(20—30)% increased Global Defences (Perfect Essence of Enhancement)',['enh'],'c')
MK=lambda s: it(s,'심연의 군주의 징표','Mark of the Abyssal Lord',['markP' if s=='p' else 'markS'],'c')
GPS=[n for n,_ in GP]
def R(vis):
    kq={'has':'kq'}; gp={'has':'gp'}
    return ROUTE_([{'if':{'has':'mq'},'to':'w1'},{'if':{'unrevSide':'p'},'to':'pL'},{'if':{'unrevSide':'s'},'to':'dR2'},
       {'if':{'all':[{'des':True},{'not':kq}]},'to':'pL'},{'if':{'all':[kq,gp]},'to':'ok'},
       {'if':{'all':[kq,{'param':{'v':1}}]},'to':'tP'},{'if':kq,'to':'eE'},
       {'if':{'all':[gp,{'has':'markS'}]},'to':'dM'},{'if':gp,'to':'dS'},{'if':{'has':'markP'},'to':'pB'},
       {'if':{'all':[{'sideLt':{'side':'p','n':2}},{'has':'markS'}]},'to':'pY'},{'if':{'sideLt':{'side':'p','n':2}},'to':'pX'},
       {'if':{'has':'markS'},'to':'dM'},{'to':'pA'}],vis)
DES=lambda id,pos,lbl,item,**k: act(id,'main',pos,'desecrate','Preserved_Collarbone',lbl,[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'dR2'}],item,omens=['Omen_of_the_Blackblooded'],**k)
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'s'}]},K('정신력 +50 분열 + 잡옵 1개 (부재 목걸이)','Fractured +50 Spirit + one junk line (Absent Amulet)'),[SP,J('s')]),
 mark([0,0.6],'k1',[SP,J('s')]),
 act('k1','main',[0,1],'chaos','Chaos_Orb',K('접미 첫 번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'spell'},'to':'q1','res':'ok'},{'to':'k1','res':'fail'}],[SP,SL],show=['spell']),
 act('q1','main',[0,2],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'q2'}],[SP,J('p'),SL],omens=['Omen_of_Sinistral_Exaltation']),
 act('q2','main',[0,3],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티','The junk goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% to Maximum Quality (crafted)')],K('에센스','Essence'),[{'to':'q3'}],[SP,MQ,SL],ess='mq',omens=['Omen_of_Sinistral_Crystallisation']),
 act('q3','main',[0,4],'quality','Sibilant_Catalyst',K('시전 퀄리티 40%','Caster quality 40%'),[st(None,'쇳소리 기폭제 40개','40 Sibilant Catalysts')],K('퀄리티','Quality'),[{'to':'d1'}],[SP,MQ,SL],count=40),
 act('d1','main',[0,5],'desecrate','Preserved_Collarbone',K('접미 두 번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'dR'}],[SP,MQ,SL,UN('s')],omens=['Omen_of_the_Blackblooded']),
 act('dR','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'kq'},'to':'w1','res':'ok'},{'to':'w1','res':'fail'}],[SP,MQ,SL,KQ],want='kq',show=['kq'],omens=['Omen_of_Abyssal_Echoes']),
 act('w1','main',[0,7],'chaos','Perfect_Chaos_Orb',K('최대 퀄리티를 지우고 접두 두 번째 옵션','Max quality out, second prefix'),None,K('카오스','Chaos'),R({'ok':'ok','pL':F,'tP':F,'eE':F}),[SP,ES,SL,KQ],show=GPS,omens=['Omen_of_Whittling']),
 act('pA','main',[0,8],'essence','Essence_of_the_Abyss',K('잡옵을 지우고 심연의 군주의 징표','The junk goes for the Mark of the Abyssal Lord'),[st(None,'심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),R({'pY':'ok','pB':F}),[SP,SL,MK('s')],ess='markS',alt='markP',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 act('pB','main',[1,8],'desecrate','Preserved_Collarbone',K('접두 징표 훼손','Desecrate the prefix Mark'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),R({'pL':{}}),[SP,UN('p'),SL],fromMark=True),
 annul('pL',[2,8],R({'pX':{'port':'bottom'},'pA':{},'dS':{}})),
 act('pX','main',[0,9],'exalt','Perfect_Exalted_Orb',K('접두 두 번째 옵션','Second prefix'),None,K('엑잘','Exalt'),R({'dS':'ok','pA':F}),[SP,ES,SL],show=GPS,omens=['Omen_of_Sinistral_Exaltation']),
 act('pY','main',[1,9],'exalt','Perfect_Exalted_Orb',K('접두 두 번째 옵션','Second prefix'),None,K('엑잘','Exalt'),R({'dM':{}}),[SP,ES,SL,MK('s')],show=GPS),
 DES('dS',[0,10],K('접미 두 번째 옵션(훼손)','Second suffix (desecrated)'),[SP,ES,SL,UN('s')]),
 DES('dM',[1,10],K('접미 징표 훼손','Desecrate the suffix Mark'),[SP,ES,SL,UN('s')],fromMark=True),
 act('dR2','main',[0,11],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),R({'ok':'ok','tP':F,'eE':F,'pL':F}),[SP,ES,SL,KQ],want='kq',show=['kq'],omens=['Omen_of_Abyssal_Echoes']),
 act('tP','main',[0,12],'chaos','Perfect_Chaos_Orb',K('접두 두 번째 옵션','Second prefix'),None,K('카오스','Chaos'),[{'if':{'has':'gp'},'to':'ok','res':'ok'},{'to':'tP','res':'fail'}],[SP,ES,SL,KQ],show=GPS,trim={'side':'p','keep':'keepT'}),
 act('eE','main',[1,12],'essence','Perfect_Essence_of_Enhancement',K('잡옵을 지우고 제작 옵션','The junk goes for the crafted modifier'),[st('p','일반 방어도, 회피, 에너지 보호막 (20—30)% 증가 (제작 옵션)','(20—30)% increased Global Defences (crafted)')],K('에센스','Essence'),[{'to':'ok'}],[SP,EN,SL,KQ],ess='enh',omens=['Omen_of_Sinistral_Crystallisation']),
 done([0,13])]
graph11('absent-amulet-video-v2','Amulets','Absent Amulet',82,
  'SL 부재 목걸이(jr6-YLMJsC8) — 정신력 50 분열 + 잡옵 → 카오스 오브(주문 +3) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 균열의 에센스 → 쇳소리 기폭제 40% → 검은 피 + 보존된 빗장뼈 → 공개 → 절사 + 완벽한 카오스 오브 → (좋은 접두면) 빛의 징조 + 검은 피 빗장뼈 반복 / (둘 다 아니면) 빛의 징조 → 좌측 결정화 + 심연의 에센스(징표) → 접두 엑잘 → 징표 훼손 → 공개. 하이엔드 = 영상(접두 1티어, 공개 뒤 잡옵 접두는 절사 돌리기), 밸런스 = 접두 1~2티어, 공개 뒤 잡옵 접두는 완벽한 강화의 에센스.',
  {**ROUTE,'pT':{'kr':'접두 두 번째 옵션','en':'Second prefix','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,{'high':K('영상: 접두 1티어, 모든 스킬의 퀄리티가 먼저 뜨면 접두는 절사 돌리기','Video: T1 prefix; with skill quality first, Whittling for the prefix'),
            'bal':K('접두 1~2티어, 모든 스킬의 퀄리티가 먼저 뜨면 완벽한 강화의 에센스로 마무리','T1–2 prefix; with skill quality first, finish with Perfect Essence of Enhancement')},tags,nodes,[],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','tmax':1,'fr':True},{'tag':'esp','tmax':1} if v=='high' else {'tag':'esp','tmax':2},{'tag':'spell','tmax':1},{'tag':'kq','des':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'spell'},{'has':'kq'},{'any':[{'has':'gp'},{'has':'enh'}]}]},('high','bal'))

# ---------- 2. SL 검은 화염파 반지 (UAF91gEFRkM) ----------
# 영상: 모든 원소 저항 16% 분열 반지(82레벨) → 균열의 에센스 → 차율라의 기폭제 40% → 카오스 오브(최대 퀄리티 옵션을 접두 카오스 피해·희귀도 1티어로)
# → 좌측 찬미 + 완벽한 엑잘(나머지 하나, 빗나가면 소멸의 오브 — 생명력 1티어도 좋음) → 좌측 강령술 + 뒤바뀐 빗장뼈 → 메아리 공개(주문이 피해의 %를 카오스 피해로 획득, 빛의 징조로 다시, 영상 세 번째)
# → 상위 찬미 + 완벽한 엑잘(접미 저항 1티어, 빗나가면 우측 소멸의 징조 + 소멸의 오브 → 완벽한 엑잘) → 절사 + 완벽한 카오스 오브로 마지막 접미(영상은 비용 때문에 멈춤).
# 하이엔드 = 영상(저항 1티어 + 마지막 접미 희귀도 1티어), 밸런스 = 저항 1~2티어(영상: 2티어도 괜찮음), 마지막 접미는 나오는 대로.
RS=[('fr',4),('co',5),('li',6),('ch',8)]
tags={'ar':{'gi':7,'tmax':1},'mq':{'gi':71},'cd':{'gi':33,'tmax':1},'rp':{'gi':28,'tmax':1},'lf':{'gi':9,'tmax':1},'oc':{'gi':86},
      **{n:{'gi':g,'tmax':'$pT'} for n,g in RS},'res':{'anyOf':[n for n,_ in RS]},'rs':{'gi':27,'tmax':1},
      'gpre':{'anyOf':['cd','rp']},'gpreB':{'anyOf':['cd','rp','lf']},'keepS':{'anyOf':['ar','res','cd','rp','oc']}}
AR=it('s','모든 원소 저항 +(15—16)% (분열)','+(15—16)% to all Elemental Resistances (fractured)',['ar'])
RQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% to Maximum Quality (Essence of the Breach)',['mq'],'c')
CD=it('p','카오스 피해 (27—30)% 증가','(27—30)% increased Chaos Damage',['cd']); RP=it('p','발견하는 아이템 희귀도 (16—19)% 증가','(16—19)% increased Rarity of Items found',['rp'])
OC=it('p','주문이 피해의 (8—12)%를 카오스 피해로 획득','Spells Gain (8—12)% of Damage as extra Chaos Damage',['oc'],'d')
CR=it('s','카오스 저항 +(24—27)%','+(24—27)% to Chaos Resistance',['ch']); RR=it('s','발견하는 아이템 희귀도 (15—18)% 증가','(15—18)% increased Rarity of Items found',['rs'])
PB=['cd','rp']; SHR=[n for n,_ in RS]
G1=[AR,J('p')]; G2=[RQ,AR]; G3=[RP,AR]; G4=[CD,RP,AR]; G5=G4[:2]+[UN('p'),AR]; G6=[CD,RP,OC,AR]; G7=G6+[CR,J('s')]; G8=G6+[CR,RR]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'ar','fr':True},{'junk':'p'}]},K('모든 원소 저항 1티어 분열 + 잡옵 1개 (황금 반지, 아이템 레벨 82)','Fractured T1 all elemental resistances + one junk line (Gold Ring, item level 82)'),G1),
 mark([0,0.6],'q1',G1),
 act('q1','main',[0,1],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티','The junk goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% to Maximum Quality (crafted)')],K('에센스','Essence'),[{'to':'q2'}],G2,ess='mq'),
 act('q2','main',[0,2],'quality','Chayulas_Catalyst',K('카오스 퀄리티 40%','Chaos quality 40%'),[st(None,'차율라의 기폭제 40개','40 Chayula’s Catalysts')],K('퀄리티','Quality'),[{'to':'p1'}],G2,count=40),
 act('p1','main',[0,3],'chaos','Chaos_Orb',K('최대 퀄리티를 접두 첫 번째 옵션으로','Max quality into the first prefix'),None,K('카오스','Chaos'),[{'if':{'has':'gpre'},'to':'p2','res':'ok'},{'to':'p1','res':'fail'}],G3,show=PB),
 act('p2','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 두 번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'gpre','min':2}},'to':'p3','res':'ok'},{'if':{'all':[{'param':{'v':2}},{'has':'gpre'},{'has':'lf'}]},'to':'p3','res':'ok','hide':True},{'to':'p2x','res':'fail','port':'right'}],G4,show=PB,omens=['Omen_of_Sinistral_Exaltation']),
 annul('p2x',[1,4],[{'if':{'has':'gpre'},'to':'p2','res':'ok','port':'right'},{'to':'p1','res':'fail'}],omens=(),target=K('접두 하나 지우기','Remove one prefix')),
 act('p3','main',[0,5],'desecrate','Altered_Collarbone',K('접두 세 번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p4'}],G5,omens=['Omen_of_Sinistral_Necromancy']),
 act('p4','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'oc'},'to':'s1','res':'ok'},{'to':'p4x',**F}],G6,want='oc',show=['oc'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('p4x',[1,6],'p3'),
 act('s1','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접미 두 번째·세 번째 옵션','Second and third suffixes'),None,K('엑잘','Exalt'),[{'if':{'all':[{'has':'res'},{'param':{'v':2}}]},'to':'ok','res':'ok'},{'if':{'has':'res'},'to':'s3','res':'ok'},{'to':'s2','res':'fail','port':'right'}],G7,show=SHR,omens=['Omen_of_Greater_Exaltation']),
 annul('s2',[1,7],[{'to':'s2b','port':'bottom'}],omens=('Omen_of_Dextral_Annulment',),target=K('접미 옵션 하나 지우기','Remove one suffix')),
 act('s2b','main',[1,8],'exalt','Perfect_Exalted_Orb',K('접미 세 번째 옵션','Third suffix'),None,K('엑잘','Exalt'),[{'if':{'all':[{'has':'res'},{'param':{'v':2}}]},'to':'ok','res':'ok'},{'if':{'has':'res'},'to':'s3','res':'ok'},{'to':'s2','res':'fail','port':'right'}],G7,show=SHR),
 act('s3','main',[0,9],'chaos','Perfect_Chaos_Orb',K('접미 세 번째 옵션','Third suffix'),None,K('카오스','Chaos'),[{'if':{'has':'rs'},'to':'ok','res':'ok'},{'to':'s3','res':'fail'}],G8,show=['rs'],trim={'side':'s','keep':'keepS'}),
 done([0,10])]
graph11('sl-flamewave-ring-v2','Rings','Gold Ring',82,
  'SL 검은 화염파 반지(UAF91gEFRkM) — 모든 원소 저항 분열 반지 → 균열의 에센스 → 차율라의 기폭제 40% → 카오스 오브(접두 카오스 피해·희귀도 1티어) → 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브) → 좌측 강령술 + 뒤바뀐 빗장뼈 → 공개(주문이 피해의 %를 카오스 피해로 획득, 빛의 징조로 다시) → 상위 찬미 + 완벽한 엑잘(저항, 빗나가면 우측 소멸의 징조 + 소멸의 오브 → 완벽한 엑잘) → 절사 + 완벽한 카오스 오브(희귀도). 하이엔드 = 영상, 밸런스 = 저항 1~2티어·접두에 생명력 1티어도 받음·마지막 접미는 나오는 대로.',
  {**ROUTE,'pT':{'kr':'접미 저항','en':'Suffix resistance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,{'high':K('영상: 저항 1티어 + 마지막 접미 희귀도 1티어','Video: T1 resistance + T1 rarity last suffix'),
            'bal':K('저항 1~2티어, 접두 생명력 1티어도 받음, 마지막 접미는 나오는 대로','T1–2 resistance, T1 life is a fine prefix, last suffix as it comes')},tags,nodes,
  [{'id':'L1','nodes':['p3','p4','p4x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['s2','s2b'],'kr':'접미 저항','en':'Suffix resistance'}],
  FIN(('high','bal'),lambda v:[{'tag':'cd','tmax':1},{'tag':'rp','tmax':1},{'tag':'oc','des':True},{'tag':'ar','tmax':1,'fr':True},
      {'tag':'ch','tmax':1 if v=='high' else 2},{'tag':'rs','tmax':1} if v=='high' else {'side':'s','random':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'oc'},{'has':'res'},{'has':'gpreB'}]},('high','bal'))

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_absent_amulet_video.py'): _sp.run([_sy.executable, f'{H}/gen_absent_amulet_video.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_sl_flamewave_ring.py'): _sp.run([_sy.executable, f'{H}/gen_sl_flamewave_ring.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 덮어씀
