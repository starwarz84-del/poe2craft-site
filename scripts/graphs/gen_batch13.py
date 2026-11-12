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

# ---------- 2. MazBro 투사체 +2 분열 장갑 ----------
# 원본: 콜르의 사냥 장착 + 모든 투사체 +2 분열 + 잡옵 (퀄리티 30%, 특출난 검은강철 건틀릿) → 아스트리드의 창의성 → 카오스 오브(콜르 옵션 1티어 하나: 투사체 속도·피해 / 치명타 확률·관통)
# → 반대쪽을 상위 엑잘 + 좌측·우측 찬미로. 빗나가면 그쪽 결정화의 징조(좌측·우측) + 군왕의 합금(룬 수호) → 다시, 또 빗나가면 결정화 + 발작의 에센스(치명타 피해) → 다시
# → 제작 옵션이 남았으면 잡옵을 하나 붙여 결정화 + 합금/에센스 → 남은 접두를 고대 갈비뼈로 훼손 → 공개(투사체 피해·속도 1티어, 빛의 징조로 다시).
# 2026-11-12 영상 전체 대조(하위 작업, 자막 + 화면 프레임 — 증거 scratchpad evidence/mazbro-proj-gloves-v2/timeline.md):
#   9:35 화면 단계 노트 4A '합금 다음 발작', 4B '군왕의 합금만(발작은 합금을 대체)' → 접두 쪽 발작의 에센스 없음. 17:35 '접두만 비어 징조 필요 없음' → 고대 갈비뼈 징조 없음.
#   12:57 치명타 16%(낮은 티어)·15:40 관통 25%(2티어)를 버림 → 영상 목표는 1티어(관통 tmax 1 추가). 투사체 +2는 +1(2티어)과 다른 티어 → proj tmax 1.
#   등급(정책 10장 C17): 하이엔드 = 영상(반복 구간 1티어), 밸런스 = 상위 엑잘·결정화·소멸 반복과 빛의 징조 공개를 1~2티어로. 분열 뒤 카오스 오브는 싼 반복이라 두 등급 모두 1티어(C15).
# 영상 재확인(2026-11-10): 세 번째로도 빗나가면 징조 없는 소멸의 오브로 하나씩(좋은 옵션이 지워지면 카오스 오브부터). 시전 속도 룬 교체·룬 모루(룬벼림)·신성한 오브는 뺌(정책 23).
P2={'high':{'t':1},'bal':{'t':2}}
PT={'t':{'kr':'반복 목표','en':'Loop target','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}}
tags={'proj':{'gi':81,'tmax':1},
      'pspd':{'gi':72,'tmax':'$t'},'pdmg':{'gi':70,'tmax':'$t'},'crit':{'gi':73,'tmax':'$t'},'pierce':{'gi':74,'tmax':'$t'},
      'pspd1':{'gi':72,'tmax':1},'pdmg1':{'gi':70,'tmax':1},'crit1':{'gi':73,'tmax':1},'pierce1':{'gi':74,'tmax':1},
      'pspd2':{'gi':72,'tmax':2},'pdmg2':{'gi':70,'tmax':2},'crit2':{'gi':73,'tmax':2},'pierce2':{'gi':74,'tmax':2},
      'ps':{'anyOf':['pspd','pdmg'],'label':K('투사체 속도·피해','Projectile speed or damage')},'ss':{'anyOf':['crit','pierce'],'label':K('치명타 확률·관통','Crit chance or pierce')},
      'ps1':{'anyOf':['pspd1','pdmg1'],'label':K('투사체 속도·피해 1티어','T1 projectile speed or damage')},'ss1':{'anyOf':['crit1','pierce1'],'label':K('치명타 확률·관통 1티어','T1 crit chance or pierce')},
      'ps2':{'anyOf':['pspd2','pdmg2'],'label':K('투사체 속도·피해 1~2티어','T1–2 projectile speed or damage')},'ss2':{'anyOf':['crit2','pierce2'],'label':K('치명타 확률·관통 1~2티어','T1–2 crit chance or pierce')},
      'ward':{'gi':69},'hyst':{'gi':57},'gp':{'anyOf':['pspd','pdmg','ward'],'label':K('좋은 접두','Good prefix')},'gs':{'anyOf':['crit','pierce','hyst'],'label':K('좋은 접미','Good suffix')}}
PJ=it('s','모든 투사체 스킬 레벨 +2 (콜르)','+2 projectile skills (Kolr)',['proj'],'f'); PS=it('p','투사체 속도·피해','Projectile speed or damage',['ps']); SS=it('s','치명타 확률·관통','Crit chance or pierce',['ss'])   # PJ 글은 베이스 준비 _PJI와 같아야 왼쪽 칸이 같은 옵션으로 봄
WD=it('p','룬 수호 (군왕의 합금)','Runic ward (Sovereign Alloy)',['ward']); HY=it('s','치명타 피해 (발작의 에센스)','Crit damage (Essence of Hysteria)',['hyst'])
G0=[PJ,J('p')]; G1=[PJ,PS]; G2=[PJ,PS,SS]; G3=[PJ,PS,WD,SS,HY]; G4=G3[:1]+[PS,WD,UN('p')]+G3[3:]; G5=[PJ,PS,WD,PS,SS,HY]
ALL4={'all':[{'has':'ps'},{'has':'ss'},{'has':'ward'},{'has':'hyst'}]}
def route(vis=None, okHidden=()):   # every step re-checks the item: what is still missing decides the next step; only the edges in vis are drawn
    # vis / okHidden use edge keys: the target id, or apx_all / csH_h for the second edge to that target (2026-11-12: vis used to style the first edge with that target,
    # so xp→apx painted the success case 'all four + full prefixes' red). okHidden: hidden edges that still count as success in the step's probability.
    missS={'not':{'sideAll':{'side':'s','tag':'gs'}}}; missP={'not':{'sideAll':{'side':'p','tag':'gp'}}}
    E=[{'if':{'all':[ALL4,{'count':{'tag':'ps','min':2}}]},'to':'ok'},{'if':{'all':[ALL4,{'full':'p'}]},'to':'apx','key':'apx_all'},{'if':ALL4,'to':'k15'},
       {'if':{'all':[{'not':{'has':'ps'}},{'not':{'has':'ss'}}]},'to':'kz'},
       {'if':{'all':[{'not':{'has':'ss'}},missS,{'not':{'has':'ward'}}]},'to':'csA'},
       {'if':{'all':[{'not':{'has':'ss'}},missS,{'not':{'has':'hyst'}}]},'to':'csH'},
       {'if':{'all':[{'not':{'has':'ss'}},missS]},'to':'asx'},
       {'if':{'not':{'has':'ss'}},'to':'xs'},
       {'if':{'all':[{'not':{'has':'ps'}},missP,{'not':{'has':'ward'}}]},'to':'cpA'},
       {'if':{'all':[{'not':{'has':'ps'}},missP]},'to':'apx'},
       {'if':{'not':{'has':'ps'}},'to':'xp'},
       {'if':{'all':[{'not':{'has':'hyst'}},missS]},'to':'csH','key':'csH_h'},
       {'if':{'all':[{'not':{'has':'hyst'}},{'any':[missP,{'full':'p'}]}]},'to':'jh'},
       {'if':{'not':{'has':'hyst'}},'to':'js'},
       {'if':{'all':[{'not':{'has':'ward'}},{'any':[missP,{'full':'p'}]}]},'to':'ja'},
       {'to':'jp'}]
    vis=vis or {}; out=[]
    failTo={e['to'] for e in E if e.get('key',e['to']) in vis and (vis[e.get('key',e['to'])] if isinstance(vis[e.get('key',e['to'])],str) else vis[e.get('key',e['to'])].get('res'))=='fail'}
    for e in E:
        e=dict(e); k=e.pop('key',e['to'])
        if k in vis: v=vis[k]; e.update(v if isinstance(v,dict) else {'res':v})
        else:
            e['hide']=True
            if k in okHidden and e['to'] not in failTo: e['res']='ok'   # 화면 확률은 간선 통과 수를 도착 상자별로 세므로, 실패 상자와 같은 도착은 성공으로 못 셈
        out.append(e)
    return out
OKH=('ok','apx_all','k15','csH_h','js','jh','jp','ja')   # after a hit the item goes on to one of these
def ex(id,pos,omen,show,item,goal,vis):
    return act(id,'main',pos,'exalt','Greater_Exalted_Orb',goal,None,K('엑잘','Exalt'),route(vis,OKH),item,show=show,omens=[omen])
def cr(id,pos,cur,ess,omen,goal,shw,item,lbl,vis,okh=()):
    return act(id,'main',pos,'essence',cur,goal,shw,lbl,route(vis,okh),item,ess=ess,omens=[omen])
F={'res':'fail','port':'right'}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'proj','fr':True},{'junk':'p'}],'quality':30},K('콜르의 사냥 장착, 모든 투사체 +2 분열 + 잡옵 1개 (퀄리티 30%, 특출난 베이스)','Kolr’s Hunt socketed: fractured +2 projectile skills + one junk line (30% quality, Exceptional)'),G0),
 mark([0,0.6],'k8',G0),
 RUNE('k8',[0,1],'k9',G0),
 act('k9','main',[0,2],'chaos','Chaos_Orb',K('콜르 옵션 1티어 하나','One T1 Kolr line'),None,K('카오스','Chaos'),[{'if':{'has':'ps1'},'to':'xs','res':'ok'},{'if':{'has':'ss1'},'to':'xp','res':'ok'},{'to':'k9','res':'fail'}],G1,show=['pspd1','pdmg1','crit1','pierce1']),   # 분열 뒤 카오스 오브 = 싼 반복이라 두 등급 모두 1티어(C15)
 ex('xs',[0,3],'Omen_of_Dextral_Exaltation',['crit','pierce'],G2,K('접미: 치명타 확률·관통','Suffix: crit chance or pierce'),{'js':'ok','csA':F,'csH':F,'asx':F}),
 cr('csA',[1,3],'Sovereign_Alloy','ward','Omen_of_Dextral_Crystallisation',K('빗나간 접미를 지우고 룬 수호','The missed suffix goes for runic ward'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],[PJ,PS,WD],K('합금','Alloy'),{'xs':{'port':'right'}}),
 cr('csH',[1,4],'Essence_of_Hysteria','hyst','Omen_of_Dextral_Crystallisation',K('빗나간 접미를 지우고 치명타 피해','The missed suffix goes for crit damage'),[st('s','치명타 피해 (제작 옵션)','Crit damage (crafted)')],[PJ,PS,HY],K('에센스','Essence'),{'xs':{'port':'right'}}),
 act('asx','main',[1,5],'annul','Orb_of_Annulment',K('빗나간 접미 지우기','Remove the missed suffix'),None,K('소멸','Annul'),route({'xs':{'port':'right'},'kz':{'port':'right'}}),G2),
 ex('xp',[0,6],'Omen_of_Sinistral_Exaltation',['pspd','pdmg'],G2,K('접두: 투사체 속도·피해','Prefix: projectile speed or damage'),{'js':'ok','cpA':F,'apx':F}),
 cr('cpA',[1,6],'Sovereign_Alloy','ward','Omen_of_Sinistral_Crystallisation',K('빗나간 접두를 지우고 룬 수호','The missed prefix goes for runic ward'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],[PJ,WD,SS],K('합금','Alloy'),{'xp':{'port':'right'}}),
 act('apx','main',[1,7],'annul','Orb_of_Annulment',K('빗나간 접두 지우기','Remove the missed prefix'),None,K('소멸','Annul'),route({'xp':{'port':'right'},'kz':{'port':'right'}}),G2),
 act('js','main',[0,9],'exalt','Exalted_Orb',K('에센스가 바꿀 접두 하나','A prefix for the essence to replace'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),route({'jh':{}}),[PJ,PS,J('p'),SS],omens=['Omen_of_Sinistral_Exaltation']),
 cr('jh',[0,10],'Essence_of_Hysteria','hyst','Omen_of_Sinistral_Crystallisation',K('접두 하나를 지우고 치명타 피해','A prefix goes for crit damage'),[st('s','치명타 피해 (제작 옵션)','Crit damage (crafted)')],[PJ,PS,SS,HY],K('에센스','Essence'),{'jp':'ok','ja':'ok','k15':'ok','cpA':F,'apx':F},OKH),   # 다음으로 가는 길이 여러 개라 투사체가 남으면 모두 성공으로 셈
 act('jp','main',[0,11],'exalt','Exalted_Orb',K('합금이 바꿀 접두 하나','A prefix for the alloy to replace'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),route({'ja':{}}),[PJ,PS,J('p'),SS,HY],omens=['Omen_of_Sinistral_Exaltation']),
 cr('ja',[0,12],'Sovereign_Alloy','ward','Omen_of_Sinistral_Crystallisation',K('접두 하나를 지우고 룬 수호','A prefix goes for runic ward'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],G3,K('합금','Alloy'),{'k15':'ok','apx':F,'cpA':F},OKH),
 resetx('kz',[1,2],'k9'),
 act('k15','main',[0,13],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'k16'}],G4),   # 영상 17:35: 접두에만 빈자리라 징조 없음
 act('k16','main',[0,14],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'all':[ALL4,{'count':{'tag':'ps','min':2}}]},'to':'ok','res':'ok'},{'if':{'all':[{'unrev':False},{'not':{'added':'ps'}}]},'to':'k16x','res':'fail','port':'right'}]+[dict(e,hide=True) for e in route()[1:]],G5,want='ps',show=['pspd','pdmg'],omens=['Omen_of_Abyssal_Echoes']),
 annul('k16x',[1,14],[dict(e,hide=True) if e['to']!='k15' else dict(e,port='right',hide=False) for e in route()]),   # 빛의 징조 + 소멸의 오브: 두 등급 모두(C17 3번), 밸런스는 1~2티어까지
 done([0,15])]
graph11('mazbro-proj-gloves-v2','Gloves_str_dex','Blacksteel Gauntlets',82,
  'MazBro 투사체 +2 분열 장갑(원본 레시피 기록, 2026-11-12 영상 전체 대조) — 특출난 검은강철 건틀릿 + 콜르의 사냥 → 완벽한 진화·확장·제왕 → 옵션 1개까지 소멸 → 카오스 오브(투사체 +2) → 완벽한 엑잘 + 좌측 찬미 + 상위 찬미(접두 2개) → 고대 갈비뼈 + 우측 강령술 → 분열(1/3, 빗나가면 새 베이스) → 분열 + 옵션 1개 → 아스트리드의 창의성 → 카오스 오브(콜르 1티어 하나) → 반대쪽 상위 엑잘 + 좌측·우측 찬미(빗나가면 결정화 + 군왕의 합금 → 결정화 + 발작의 에센스, 그래도 빗나가면 소멸) → 남은 제작 옵션 → 고대 갈비뼈 → 공개(투사체 피해·속도, 빛의 징조로 다시). 퀄리티 30%·룬벼림·룬 교체·신성한 오브는 비용에서 뺌.',
  PT,P2,{'high':K('영상: 반복 구간과 공개 모두 1티어','Video: T1 in every loop and on the reveal'),'bal':K('상위 엑잘 반복과 공개를 1~2티어까지','Exalt loops and the reveal accept T1–2')},tags,nodes,
  [{'id':'L1','nodes':['k15','k16','k16x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'ps1' if v=='high' else 'ps2'},{'tag':'ps1' if v=='high' else 'ps2','des':True},{'tag':'ward','tmax':1},{'tag':'proj','tmax':1,'fr':True},{'tag':'ss1' if v=='high' else 'ss2'},{'tag':'hyst','tmax':1}]),
  {'quality':30,'sockets':2},{'all':[{'has':'ps'},{'has':'ss'},{'has':'ward'},{'has':'hyst'}]},('high','bal'),xsub=["Kolr's Hunt"],xroll=True)
# 베이스 준비(2026-11-12 영상 전체 대조, 프레임 근거는 timeline.md):
# 2:05 특출난 검은강철 건틀릿(화면 노트 '24 Gloves x 12 Divs' → 장당 12디바인, basePrice) → 퀄리티 20% → 3:00~4:05 바알 방어구 장인의 주입기로 30%(선택, 비용 미포함 — 노트 '65 * 2.7 = 175 Divs', 자막 '10번에 1번꼴', '300~400디바인')
# → 4:22 콜르의 사냥 장착 → 4:36 완벽한 진화·확장 → 5:06 완벽한 제왕 → 5:32 소멸의 오브로 옵션 1개까지 → 6:32 카오스 오브로 투사체 +2(옵션 1개 상태)
# → 6:58 '좌측 찬미·상위 찬미의 징조 소모' 메시지로 접두 2개(7:45 자막 '접두에 완벽한 엑잘') → 7:04·7:32 '우측 강령술의 징조 소모' + 7:13 고대 갈비뼈 → 분열 1/3(훼손은 분열 안 됨)
# → 영상은 장갑 4개째(8:58)에 성공, 빗나간 장갑은 새 베이스 → 12:30 소멸의 오브로 분열 + 옵션 1개.
# 내부 결정: 영상의 '분열 전에 좋은 옵션 2개 이상'(5:15 권장)은 실제 장갑 1~3에서 지키지 않아 뺌. 4번째 장갑의 아스트리드 + 결정화 + 발작·합금(8:00~8:40)은 분열이 빗나갈 때를 위한 보험이고 12:30에 모두 지우므로 뺌.
_gp=f"{H}/mazbro-proj-gloves-v2.json"; _g=json.load(open(_gp))
for _n in _g['nodes']:
    if _n.get('group')=='main': _n['pos']=[_n['pos'][0], _n['pos'][1]+10.4]
_g['basePrice']={'Divine_Orb':12}
_PJI=[{'s':'s','kr':'모든 투사체 스킬 레벨 +2 (콜르)','en':'+2 projectile skills (Kolr)','m':'n','tags':['proj']}]
_JK=lambda s: {'s':s,'kr':'잡옵','en':'Junk','m':'j'}
_prep=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'p1','start':{'rar':'normal','mods':[],'quality':30},'label':K('특출난 검은강철 건틀릿 구입 (노멀)','Buy exceptional Blacksteel Gauntlets (normal)'),'item':[]},
 {'id':'hq','kind':'side','group':'prep','pos':[1,0.5],'attach':['h1','p1'],'cur':'Vaal_Armourers_Infuser','goal':K('퀄리티 20% → 30%, 선택·비용 미포함','Quality 20% → 30%, optional, not costed'),'label':K('퀄리티','Quality')},
 {'id':'hk','kind':'side','group':'prep','pos':[1,1.5],'attach':['p1','p2'],'goal':K('콜르의 사냥 장착, 영구','Socket Kolr’s Hunt, permanent'),'label':K('룬','Rune')},
 {'id':'p1','kind':'act','group':'prep','pos':[0,1],'act':'transmute','cur':'Perfect_Orb_of_Transmutation','goal':K('매직','Magic'),'label':K('진화','Transmute'),'edges':[{'to':'p2'}],'item':[]},
 {'id':'p2','kind':'act','group':'prep','pos':[0,2],'act':'augment','cur':'Perfect_Orb_of_Augmentation','goal':K('매직 두번째 옵션','Second magic line'),'label':K('확장','Augment'),'edges':[{'to':'p3'}],'item':[]},
 {'id':'p3','kind':'act','group':'prep','pos':[0,3],'act':'regal','cur':'Perfect_Regal_Orb','goal':K('레어','Rare'),'label':K('제왕','Regal'),'edges':[{'to':'p3x'}],'item':[]},
 {'id':'p3x','kind':'cleanup','group':'prep','pos':[0,4],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('옵션 1개만 남기기','Keep one line'),'edges':[{'to':'p4'}],'item':[_JK('x')]},
 {'id':'p4','kind':'act','group':'prep','pos':[0,5],'act':'chaos','cur':'Chaos_Orb','goal':K('모든 투사체 스킬 레벨 +2','+2 to all projectile skills'),'label':K('카오스','Chaos'),'show':['proj'],'edges':[{'if':{'has':'proj'},'to':'p5','res':'ok'},{'to':'p4','res':'fail'}],'item':_PJI},
 {'id':'p5','kind':'act','group':'prep','pos':[0,6],'act':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation'],'goal':K('접두 2개','Two prefixes'),'showText':[K('랜덤 옵션 2개','Two random lines')],'label':K('엑잘','Exalt'),'edges':[{'to':'p6'}],'item':_PJI+[_JK('p'),_JK('p')]},
 {'id':'p6','kind':'act','group':'prep','pos':[0,7],'act':'desecrate','cur':'Ancient_Rib','omens':['Omen_of_Dextral_Necromancy'],'goal':K('네번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),'showText':[K('훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],'label':K('훼손','Desecrate'),'edges':[{'to':'p7'}],'item':_PJI+[_JK('p'),_JK('p'),{'s':'s','kr':'훼손 옵션 (미공개)','en':'Desecrated (unrevealed)','m':'n'}]},
 {'id':'p7','kind':'act','group':'prep','pos':[0,8],'act':'fracture','cur':'Fracturing_Orb','goal':K('분열 (셋 중 하나)','Fracture (one of three)'),'showText':[K('투사체 +2가 분열되면 성공','Success when +2 projectile fractures')],'label':K('분열','Fracture'),'edges':[{'if':{'fractured':'proj'},'to':'p8','res':'ok','label':K('투사체 +2 분열','+2 projectile fractured')},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another line fractured')}],'item':[dict(_PJI[0],m='f')]},
 {'id':'xj','kind':'exit','group':'prep','pos':[1,8],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),'note':K('투사체 +2가 아닌 옵션이 분열되면 이 장갑은 다른 용도로 두고 새 베이스로 처음부터','Another line fractured: set this one aside and start on a new base')},
 {'id':'p8','kind':'cleanup','group':'prep','pos':[0,9],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':[dict(_PJI[0],m='f'),_JK('p')]}]
_g['nodes']=_prep+[n for n in _g['nodes'] if n['id']!='h1']
_g['start']='h1'
json.dump(_g,open(_gp,'w'),ensure_ascii=False,indent=1)
