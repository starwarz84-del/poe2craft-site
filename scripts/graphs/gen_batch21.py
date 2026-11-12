# Batch 21 (사용자 2026-11-10: 나머지 2개) — 극한(5) → High-end only.
#   mazbro-sceptre-v2 (MazBro UwzsARlgaFM, 자막 재확인), xeno-phys-crossbow-v2 (XenoARPG 1TP4aGqxU7Q, 자막 없음 — 화면만 본 기존 레시피 기준)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch19.py').read(); exec(_src[:_src.index('# ---------- 1. 반지깎는노인')])
P1={'high':{'pT':1}}
PT1={'pT':{'kr':'목표 티어','en':'Target tier','values':TV({'1':('1티어','T1')})}}

# ---------- 1. MazBro BiS 셉터 (UwzsARlgaFM) ----------
# 영상: 동료(존재 범위 내 아군) 피해 1티어 분열 + 잡옵 → 카오스 오브(마나 최대치 1티어) → 좌측 찬미 + 상위 엑잘(정신력 증가 1티어 또는 정신력·마나 1티어, 빗나가면 소멸의 오브)
# → 아스트리드의 창의성(제작 옵션 2개: 합금 + 징표) → 접미는 완벽한 엑잘 하나씩. 빗나가면 싼 방법부터: 우측 결정화 + 군왕의 합금(장착 증강 효과) /
#   우측 결정화 + 심연의 에센스 → 보존된 턱뼈로 징표 훼손 → 공개(마나 재생·존재 범위·시전 속도 1티어, 아니면 생명력 재생으로 자리 막기) / 우측 소멸의 징조 + 소멸의 오브.
#   마나 1티어(레벨 70)보다 높은 잡옵이 많아 절사의 징조는 못 씀(영상 46:28). 신성한 오브·바알 신비학자의 주입기·유동체·쥬얼러 오브는 뺌(정책 23).
tags={'dmg':{'gi':10,'tmax':1},'mana':{'gi':3,'tmax':1},'sp':{'gi':19,'tmax':1},'hyb':{'gi':20,'tmax':1},'regen':{'gi':13,'tmax':1},'cs':{'gi':15,'tmax':1},
      'aoe':{'gi':21,'tmax':1},'cr':{'gi':16,'tmax':1},'cd':{'gi':17,'tmax':1},'aug':{'gi':34},'mkS':{'gi':28},
      'spi':{'anyOf':['sp','hyb']},'sg':{'anyOf':['regen','cs','aoe','cr','cd']},'keepS':{'anyOf':['regen','cs','aoe','cr','cd','aug']}}
DM=it('p','존재 범위 내 아군이 주는 피해 (105—119)% 증가 (분열)','Allies in your Presence deal (105—119)% increased Damage (fractured)',['dmg'])
MA=it('p','마나 최대치 +(150—164)','+(150—164) to maximum Mana',['mana']); SPI=it('p','정신력 (61—65)% 증가','(61—65)% increased Spirit',['sp'])
AS=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
AUG=it('s','장착 증강 아이템 효과 (20—30)% 증가 (군왕의 합금)','(20—30)% increased effect of Socketed Augment Items (Sovereign Alloy)',['aug'],'c')
RG=it('s','마나 재생 속도 (60—69)% 증가','(60—69)% increased Mana Regeneration Rate',['regen'],'d'); CS=it('s','존재 범위 내 아군의 시전 속도 (17—20)% 증가','Allies in your Presence have (17—20)% increased Cast Speed',['cs'])
MK=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mkS'],'c')
def RS(vis):   # every step re-checks the item
    done={'all':[{'has':'aug'},{'count':{'tag':'sg','min':2}}]}; js=JK('s','keepS')
    return ROUTE_([{'if':{'not':{'has':'mana'}},'to':'c1'},{'if':{'all':[{'not':{'has':'spi'}},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},{'if':{'not':{'has':'spi'}},'to':'e1x'},
       {'if':{'unrevSide':'s'},'to':'b3'},{'if':{'has':'mkS'},'to':'b2'},{'if':done,'to':'ok'},
       {'if':{'all':[{'any':[js,{'full':'s'}]},{'not':{'has':'aug'}}]},'to':'aL'},{'if':{'all':[js,{'des':False}]},'to':'mA'},{'if':js,'to':'da'},
       {'if':{'all':[{'des':True},{'full':'s'}]},'to':'fl'},{'if':{'all':[{'des':False},{'has':'aug'},{'count':{'tag':'sg','min':1}},{'sideLt':{'side':'s','n':3}}]},'to':'b2n'},
       {'to':'s1'}],vis)
M0=[DM,J('s')]; M1=[DM,MA]; M2=[DM,MA,SPI]; M3=M2+[AS]; M4=M3+[J('s')]; M5=M2+[AUG,AS]; M6=M2+[AUG,MK,AS]; M7=M2+[AUG,UN('s'),AS]; M8=M2+[AUG,RG,AS]; M9=M2+[AUG,RG,CS,AS]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'dmg','fr':True},{'junk':'s'}]},K('존재 범위 내 아군이 주는 피해 1티어 분열 + 잡옵 1개','Fractured T1 ally damage + one junk line'),M0),
 mark([0,0.6],'c1',M0),
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접두 두번째 옵션','Second prefix'),None,K('카오스','Chaos'),[{'if':{'has':'mana'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],M1,show=['mana']),
 act('e1','main',[0,2],'exalt','Greater_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),[{'if':{'has':'spi'},'to':'r1','res':'ok'},{'to':'e1x',**F}],M2,show=['sp','hyb'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('e1x',[1,2],RS({'e1':{'res':'ok','port':'right'},'c1':{'res':'fail'}}),omens=(),target=K('접두 잡옵 지우기','Remove the junk prefix')),
 act('r1','main',[0,3],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':'s1'}],M3,rune=K('아스트리드의 창의성','Astrid’s Creativity')),
 act('s1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 옵션','A suffix'),None,K('엑잘','Exalt'),RS({'ok':'ok','aL':F,'mA':F,'da':F}),M4,show=['regen','aoe','cs','cr','cd']),
 act('aL','main',[1,4],'essence','Sovereign_Alloy',K('잡옵을 지우고 장착 증강 아이템 효과 (20—30)% 증가','The junk goes for (20—30)% increased effect of Socketed Augment Items'),[st('s','장착 증강 아이템 효과 (20—30)% 증가 (제작 옵션)','(20—30)% increased effect of Socketed Augment Items (crafted)')],K('합금','Alloy'),RS({'s1':{},'mA':{}}),M5,ess='aug',omens=['Omen_of_Dextral_Crystallisation']),
 act('mA','main',[1,5],'essence','Essence_of_the_Abyss',K('잡옵을 지우고 심연의 군주의 징표','The junk goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),RS({'b2':{}}),M6,ess='mkS',mark=True,omens=['Omen_of_Dextral_Crystallisation']),
 act('b2','main',[1,6],'desecrate','Preserved_Jawbone',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RS({'b3':{}}),M7,fromMark=True),
 act('b2n','main',[2,6],'desecrate','Preserved_Jawbone',K('접미 빈자리 훼손','Desecrate the open suffix'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RS({'b3':{}}),M7),
 act('b3','main',[1,7],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RS({'s1':{},'fl':{'port':'right'}}),M8,want='sg',show=['regen','aoe','cs'],omens=['Omen_of_Abyssal_Echoes']),
 annul('da',[2,4],RS({'s1':{'res':'ok'}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 지우기','Remove the junk suffix')),
 annul('fl',[2,7],RS({'b2n':{}}),target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),
 done([0,8])]
graph11('mazbro-sceptre-v2','Sceptres','Stoic Sceptre',82,
  'MazBro BiS 셉터(UwzsARlgaFM) — 아군 피해 1티어 분열 + 잡옵 → 카오스 오브(마나 최대치 1티어) → 좌측 찬미 + 상위 엑잘(정신력 증가 또는 정신력·마나 1티어, 빗나가면 소멸의 오브) → 아스트리드의 창의성 → 완벽한 엑잘(접미 하나씩). 빗나가면 우측 결정화 + 군왕의 합금 → 우측 결정화 + 심연의 에센스 → 보존된 턱뼈 징표 훼손 → 공개(마나 재생·존재 범위·시전 속도, 아니면 자리 막기) → 우측 소멸의 징조. 마나 1티어(레벨 70) 때문에 절사의 징조는 못 씀.',
  PT1,P1,{'high':K('영상: 접미 1티어 2개 + 장착 증강 효과','Video: two T1 suffixes + socketed augment effect')},tags,nodes,
  [{'id':'L1','nodes':['mA','b2','b3'],'kr':'자리 막기','en':'Block'}],
  FIN(('high',),lambda v:[{'tag':'dmg','fr':True},{'tag':'mana'},{'tag':'sp'},{'tag':'aug','ess':True},{'tag':'regen','des':True},{'tag':'cs'}]),
  {'quality':20,'sockets':2},{'all':[{'has':'mana'},{'has':'spi'},{'has':'aug'},{'count':{'tag':'sg','min':2}}]},('high',))

# ---------- 2. XenoARPG 물리 석궁 (1TP4aGqxU7Q, 자막 없음) ----------
# 화면: 치명타 확률 1티어 분열 + 잡옵 → 카오스 오브(물리 피해 % 1티어) → 고대 턱뼈 + 좌측 강령술(자리 막기 — 영상은 공격 원소 피해 1티어, 사용자 방식은 정확도 1티어)
# → 좌측 찬미 + 완벽한 엑잘(물리 % + 정확도 1티어, 빗나가면 절사 + 완벽한 카오스 오브) → 상위 찬미 + 완벽한 엑잘(투사체 +5·공격 속도 1티어) → 절사 + 완벽한 카오스 오브(남은 것)
# → 빛의 징조로 막기 제거 → 고대 턱뼈 → 물리 피해 추가 1티어 공개(빛의 징조로 다시). 상위 철 룬·신성한 오브는 뺌(정책 23).
tags={'crit':{'gi':18,'tmax':1},'pp':{'gi':8,'tmax':1},'hyb':{'gi':9,'tmax':1},'flat':{'gi':3,'tmax':1},'eatk':{'gi':23,'tmax':1},'acc':{'gi':17,'tmax':1},
      'proj':{'gi':10,'tmax':1},'as':{'gi':16,'tmax':1},'blk':{'anyOf':['eatk','acc']},'p3':{'anyOf':['hyb','flat']},'sg':{'anyOf':['proj','as']},
      'keepP':{'anyOf':['pp','p3']},'keepS':{'anyOf':['proj','as']}}
CRX=it('s','치명타 확률 +(4.41—5)% (분열)','+(4.41—5)% to Critical Hit Chance (fractured)',['crit']); PPX=it('p','물리 피해 (170—179)% 증가','(170—179)% increased Physical Damage',['pp'])
BKX=it('p','정확도 +(551—650) (훼손, 자리 막기)','+(551—650) to Accuracy Rating (desecrated, blocker)',['acc'],'d')
HYX=it('p','물리 피해 (75—79)% 증가 + 정확도 +(175—200)','(75—79)% increased Physical Damage + (175—200) to Accuracy Rating',['hyb'])
FLX=it('p','물리 피해 (37—55)~(63—94) 추가','Adds (37—55) to (63—94) Physical Damage',['flat'],'d')
PJX=it('s','모든 투사체 스킬 레벨 +5','+5 to Level of all Projectile Skills',['proj']); ASX=it('s','공격 속도 (17—19)% 증가','(17—19)% increased Attack Speed',['as'])
def RX(vis):
    fs={'count':{'tag':'sg','min':2}}
    return ROUTE_([{'if':{'not':{'has':'pp'}},'to':'c1'},{'if':JK('p','keepP'),'to':'w1'},{'if':{'all':[fs,{'has':'p3'},{'not':{'des':True}},{'unrevSide':'p'}]},'to':'f3'},{'if':{'unrevSide':'p'},'to':'rv'},
       {'if':{'all':[{'not':{'des':True}},{'not':{'has':'p3'}},{'sideLt':{'side':'p','n':3}}]},'to':'d1'},
       {'if':{'all':[{'not':{'has':'p3'}},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},{'if':{'not':{'has':'p3'}},'to':'w1'},
       {'if':{'all':[{'not':{'has':'proj'}},{'sideLt':{'side':'s','n':3}}]},'to':'s1'},{'if':{'not':{'has':'proj'}},'to':'w2'},
       {'if':{'all':[{'not':{'has':'as'}},{'sideLt':{'side':'s','n':3}}]},'to':'s3'},{'if':{'not':{'has':'as'}},'to':'w3'},
       {'if':{'des':True},'to':'f1'},{'if':{'count':{'tag':'p3','min':2}},'to':'ok'},{'to':'f2'}],vis)
X0=[PPX,CRX,J('s')]; X0b=[PPX,UN('p'),CRX]; X1=[PPX,BKX,CRX]; X2=[PPX,BKX,HYX,CRX]; X3=X2+[PJX,J('s')]; X3b=X2+[PJX]; X4j=X2+[PJX,J('s')]; X4=X2+[PJX,ASX]; X5=[PPX,HYX,UN('p'),CRX,PJX,ASX]; X6=[PPX,HYX,FLX,CRX,PJX,ASX]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'crit','fr':True},{'junk':'s'}]},K('치명타 확률 1티어 분열 + 잡옵 1개','Fractured T1 crit chance + one junk line'),[CRX,J('s')]),
 mark([0,0.6],'c1',[CRX,J('s')]),
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접두 첫번째 옵션','First prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pp'},'to':'d1','res':'ok'},{'to':'c1','res':'fail'}],X0,show=['pp']),
 act('d1','main',[0,2],'desecrate','Ancient_Jawbone',K('접두 두번째 옵션(훼손)','Second prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RX({'rv':{}}),X0b,omens=['Omen_of_Sinistral_Necromancy']),
 act('rv','main',[0,3],'reveal',None,K('자리 막기 옵션 확인','Reveal the blocker'),None,K('공개','Reveal'),[{'if':{'added':'$bw'},'to':'e1','res':'ok'},{'to':'rvx',**F}],X1,want='$bw',show=['acc','eatk'],omens=['Omen_of_Abyssal_Echoes'],showIf=[{'param':{'bw':'acc'},'show':['acc']}]),
 annul('rvx',[1,3],RX({'d1':{'port':'right'}})),
 act('e1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),RX({'s1':'ok','w1':F}),X2,show=['hyb','flat'],omens=['Omen_of_Sinistral_Exaltation']),
 act('w1','main',[1,4],'chaos','Perfect_Chaos_Orb',K('접두 세번째 옵션','Third prefix'),None,K('카오스','Chaos'),RX({'s1':'ok','e1':{'res':'fail'}}),X2,show=['hyb','flat'],trim={'side':'p','keep':'keepP','keepDes':True}),
 act('s1','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),RX({'s3':'ok','w2':F}),X3,show=['proj'],omens=['Omen_of_Greater_Exaltation']),
 act('w2','main',[1,5],'chaos','Perfect_Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),RX({'s3':'ok'}),X3b,show=['proj'],trim={'side':'s','keep':'keepS','keepDes':True}),
 act('s3','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),RX({'f1':'ok','w3':F}),X4j,show=['as']),
 act('w3','main',[1,6],'chaos','Greater_Chaos_Orb',K('접미 세번째 옵션','Third suffix'),None,K('카오스','Chaos'),RX({'f1':'ok'}),X4,show=['as'],trim={'side':'s','keep':'keepS','keepDes':True}),
 annul('f1',[0,7],RX({'f2':{}}),target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),
 act('f2','main',[0,8],'desecrate','Ancient_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f3'}],X5),
 act('f3','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'p3'},'to':'ok','res':'ok'},{'to':'f3x',**F}],X6,want='p3',show=['flat','hyb'],omens=['Omen_of_Abyssal_Echoes']),
 annul('f3x',[1,9],RX({'f2':{'port':'right'}})),
 done([0,10])]
graph11('xeno-phys-crossbow-v2','Crossbows','Desolate Crossbow',82,
  'XenoARPG 물리 석궁(1TP4aGqxU7Q, 자막 없음 — 화면 기준) — 치명타 확률 분열 + 잡옵 → 카오스 오브(물리 피해 % 1티어) → 고대 턱뼈 자리 막기(정확도 1티어, 영상·타협 = 공격 원소 피해 1티어) → 좌측 찬미 + 완벽한 엑잘(물리 % + 정확도, 빗나가면 절사 카오스) → 상위 찬미 + 완벽한 엑잘 → 절사 + 완벽한 카오스 오브(투사체 +5) → 완벽한 엑잘 → 절사 + 상위 카오스 오브(공격 속도 1티어, 레벨 37) → 빛의 징조로 막기 제거 → 고대 턱뼈 → 물리 피해 추가 공개.',
  {**PT1,'bw':{'kr':'자리 막기','en':'Blocker','values':TV({'acc':('정확도 1티어','T1 accuracy'),'blk':('정확도 또는 공격 원소 피해 1티어 (영상·타협)','T1 accuracy or attack elemental (video, settle)')})}},
  {'high':{'pT':1,'bw':'acc'}},{'high':K('정확도 1티어로 자리 막기 → 절사로 확정 제작','Block with T1 accuracy, then whittle safely')},tags,nodes,
  [{'id':'L1','nodes':['f2','f3','f3x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['d1','rv','rvx'],'kr':'자리 막기','en':'Block'}],
  FIN(('high',),lambda v:[{'tag':'pp'},{'tag':'hyb'},{'tag':'flat','des':True},{'tag':'crit','fr':True},{'tag':'proj'},{'tag':'as'}]),
  {'quality':20,'sockets':3},{'all':[{'has':'pp'},{'count':{'tag':'p3','min':2}},{'count':{'tag':'sg','min':2}}]},('high',))
_g=json.load(open(f'{H}/xeno-phys-crossbow-v2.json')); _g['strategies'].append({'id':'high-settle','params':{'pT':1,'bw':'blk'}}); json.dump(_g,open(f'{H}/xeno-phys-crossbow-v2.json','w'),ensure_ascii=False,indent=1)

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_mazbro_sceptre.py'): _sp.run([_sy.executable, f'{H}/gen_mazbro_sceptre.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 이 파일의 결과를 덮어씀

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_xeno_crossbow.py'): _sp.run([_sy.executable, f'{H}/gen_xeno_crossbow.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 이 파일의 결과를 덮어씀
