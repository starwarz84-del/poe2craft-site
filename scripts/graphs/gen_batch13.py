# Batch 13 (사용자 2026-11-10: 전문가부터는 2개씩) — 전문가(4) → High-end (video) + Balance.
#   noble-timelost-sapphire-v2, mazbro-proj-gloves-v2
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch12.py').read(); exec(_src[:_src.index('# ---------- 1. Master T')])
_s11=open(f'{H}/gen_batch11.py').read(); exec(_s11[_s11.index('def graph11'):_s11.index('def WHIT')])

# ---------- 1. 노블이 5옵션 오래된 사파이어 ----------
# 원본: 주문 치명타 확률 분열 + 잡옵 → 카오스 오브(주문 치명타 피해) → 엑잘(접두) → 고대 위력적인 액체 경멸 → 우측 찬미 + 엑잘(치명타 피해, 빗나가면 소멸의 오브)
# → 좌측 말소의 징조 + 카오스 오브(경멸 옵션) → 엑잘(접두) → 고대 위력적인 액체 우울 → 보존된 두개골(접두가 꽉 차 접두 하나를 지우고 붙음) → 공개(최대 마나, 실패는 카오스 오브로 바꾸고 다시)
# 액체 경멸 규칙(사용자 확정 2026-11-10: 먼저 지우고 붙음)으로 접두 2개를 채운 뒤 경멸(성공 2/3). 기폭제 퀄리티는 뺌.
FRS=it('s','주문 치명타 명중 확률 (분열)','Spell crit chance (fractured)',['cc'])
tags={'cc':{'gi':50},'scd':{'gi':16},'cd':{'gi':15},'contS':{'gi':84,'slot':{'s':1}},'contP':{'gi':85,'slot':{'p':1}},'rad':{'gi':82},'mana':{'gi':69}}
SCD=it('s','주문 치명타 피해 보너스','Spell crit damage bonus',['scd']); CD=it('s','치명타 피해 보너스','Crit damage bonus',['cd']); MN=it('p','최대 마나','Maximum mana',['mana'])
RDs=it('p','범위 아주 큼','Very large radius',['rad'])
I0=[FRS,J('p')]; I1=[FRS,SCD]; I2=[FRS,SCD,J('p'),J('p')]; I3=[FRS,SCD,J('p'),CS2]; I4=I3+[CD]; I5=[FRS,SCD,CD,J('p'),J('p')]; I6=[FRS,SCD,CD,J('p'),RDs]
I7=[FRS,SCD,CD,J('p'),UN('p')]; I8=[FRS,SCD,CD,MN,RDs]
def contempt_s(id,pos,ok,fail,item,keep):
    return LIQ(id,pos,'Ancient_Potent_Liquid_Contempt','contS',K('고대 위력적인 액체 경멸 (한 옵션을 지우고 붙음)','Ancient Potent Liquid Contempt (takes a line, then lands)'),
        [st('p','+1 접미 허용 (접두가 지워지면 성공, 접미가 지워지면 실패)','+1 suffix allowed (a prefix goes: success; a suffix goes: miss)')],
        [{'if':{'all':[{'has':'contS'},{'has':keep}]},'to':ok,'res':'ok'},{'to':fail,'res':'fail','port':'right'}],item,alt='contP')
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'cc','fr':True},{'junk':'p'}]},K('주문 치명타 확률 분열 + 잡옵 1개 오래된 사파이어','Time-Lost Sapphire: fractured spell crit chance + one junk line'),I0),
 mark([0,0.6],'n2',I0),
 act('n2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'scd'},'to':'n3','res':'ok'},{'to':'n2','res':'fail'}],I1,show=['scd']),
 act('n3','main',[0,2],'exalt','Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 1개씩 (접미가 꽉 차 접두로)','One random line each (suffixes are full)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'n4'},{'to':'n3','hide':True}],I2),
 contempt_s('n4',[0,3],'n5','n4x',I3,'scd'), resetx('n4x',[1,3],'n2'),
 act('n5','main',[0,4],'exalt','Exalted_Orb',K('접미 세번째 옵션 (주문 치명타 피해가 지워졌으면 그것도)','Third suffix (and spell crit damage if it went)'),None,K('엑잘','Exalt'),[{'if':{'all':[{'has':'cd'},{'has':'scd'}]},'to':'n6','res':'ok'},{'if':{'full':'s'},'to':'n5x','res':'fail','port':'right'},{'to':'n5','res':'fail'}],I4,show=['cd','scd'],omens=['Omen_of_Dextral_Exaltation']),
 annul('n5x',[1,4],[{'if':{'not':{'has':'contS'}},'to':'n4x','port':'right'},{'if':{'full':'s'},'to':'n5x'},{'to':'n5','port':'bottom'}],omens=(),
       target=K('빗나간 접미 지우기 (경멸 옵션이 지워지면 처음부터)','Remove the missed suffix (losing the contempt line: start over)')),
 erase('n6',[0,5],'n7',I5),
 act('n7','main',[0,6],'exalt','Exalted_Orb',K('접두 채우기','Fill the prefixes'),[st('p','랜덤 옵션 (접미가 한도를 넘어 접두로만)','Random lines (suffixes are over the limit)')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'n9'},{'to':'n7','hide':True}],I5),
 LIQ('n9',[0,7],'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 (접두 하나가 지워짐)','Ancient Potent Liquid Melancholy (one prefix goes)'),[st('p','범위 아주 큼','Very large radius')],
     [{'if':{'all':[{'has':'mana'},{'has':'rad'}]},'to':'ok','res':'ok'},{'to':'n10'}],I6),
 act('n10','main',[0,8],'desecrate','Preserved_Cranium',K('접두 훼손 (접두가 꽉 차 하나를 지우고 붙음)','Prefix desecration (prefixes are full: one goes)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'n11'}],I7,omens=['Omen_of_Sinistral_Necromancy']),
 act('n11','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'all':[{'added':'mana'},{'has':'rad'}]},'to':'ok','res':'ok'},{'if':{'added':'mana'},'to':'n9','res':'ok','port':'right'},{'to':'n11x','res':'fail','port':'right'}],I8,want='mana',show=['mana'],omens=['Omen_of_Abyssal_Echoes'],
     over=[{'param':{'v':2},'set':{'edges':[{'if':{'has':'rad'},'to':'ok','res':'ok'},{'to':'n9k','res':'fail','port':'right'}]}}]),
 act('n11x','main',[1,9],'chaos','Chaos_Orb',K('훼손 옵션 바꾸기 (접미가 한도를 넘어 접두만 바뀜)','Replace the desecrated line (prefixes only)'),None,K('카오스','Chaos'),
     [{'if':{'has':'rad'},'to':'n10','port':'right'},{'to':'n9','port':'right'}],I6),
 LIQ('n9k',[1,9.8],'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 다시 (결과 그대로)','Ancient Potent Liquid Melancholy again (keep it)'),[st('p','범위 아주 큼','Very large radius')],[{'to':'ok'}],I6),
 done([0,10.6])]
graph10('noble-timelost-sapphire-v2','Time-Lost_Sapphire','Time-Lost Sapphire',79,
  '노블이 5옵션 오래된 사파이어(원본 레시피 기록) — 주문 치명타 확률 분열 + 잡옵 → 카오스 오브(주문 치명타 피해) → 엑잘 2번(접두) → 고대 위력적인 액체 경멸(실패 = 분열 + 옵션 1개) → 우측 찬미 + 엑잘(치명타 피해, 빗나가면 소멸의 오브) → 좌측 말소의 징조 + 카오스 오브(경멸 옵션) → 엑잘 → 고대 위력적인 액체 우울 → 보존된 두개골 → 공개(최대 마나, 하이엔드 = 카오스 오브로 바꾸고 다시).',
  ROUTE,PH,{'high':K('영상: 최대 마나가 나올 때까지 카오스 오브로 바꾸고 다시','Video: Chaos the line away and retry until maximum mana'),'bal':K('공개 결과 그대로, 나머지는 영상대로','Keep the reveal, the rest as in the video')},tags,nodes,
  [{'id':'L1','nodes':['n9','n10','n11','n11x'],'kr':'최대 마나','en':'Maximum mana'}],
  FIN(('high','bal'),lambda v:[{'tag':'mana','tmax':1} if v=='high' else {'side':'p','random':True},{'tag':'rad','tmax':1},{'tag':'cc','tmax':1,'fr':True},{'tag':'scd','tmax':1},{'tag':'cd','tmax':1}]),
  {'quality':0,'sockets':0},{'all':[{'has':'scd'},{'has':'cd'},{'has':'rad'}]},('high','bal'),cap={'p':2,'s':2})

# ---------- 2. MazBro 투사체 +2 분열 장갑 ----------
# 원본: 콜르의 사냥 장착 + 모든 투사체 +2 분열 + 잡옵 (퀄리티 30%, 특출난 검은강철 건틀릿) → 아스트리드의 창의성 → 카오스 오브(콜르 옵션 1티어 하나: 투사체 속도·피해 / 치명타 확률·관통)
# → 반대쪽 면을 상위 엑잘 + 면 찬미로. 빗나가면 그 면 결정화의 징조 + 군왕의 합금(룬 수호) → 다시, 또 빗나가면 결정화 + 발작의 에센스(치명타 피해) → 다시
# → 제작 옵션이 남았으면 잡옵을 하나 붙여 결정화 + 합금/에센스 → 남은 접두를 고대 갈비뼈로 훼손 → 공개(투사체 피해·속도 1티어, 빛의 징조로 다시).
# 세 번째로도 빗나가면 영상은 소멸의 오브 — 여기선 그 면 소멸의 징조로 빗나간 옵션 쪽만(좋은 옵션·합금을 지우지 않게). 시전 속도 룬 교체·신성한 오브는 뺌(정책 23).
P2={'high':{'v':1},'bal':{'v':2}}
tags={'proj':{'gi':81},'pspd':{'gi':72,'tmax':1},'pdmg':{'gi':70,'tmax':1},'crit':{'gi':73,'tmax':1},'pierce':{'gi':74},
      'ps':{'anyOf':['pspd','pdmg'],'label':K('투사체 속도·피해 1티어','T1 projectile speed or damage')},'ss':{'anyOf':['crit','pierce'],'label':K('치명타 확률 1티어·관통','T1 crit chance or pierce')},
      'ward':{'gi':69},'hyst':{'gi':57},'gp':{'anyOf':['pspd','pdmg','ward'],'label':K('좋은 접두','Good prefix')},'gs':{'anyOf':['crit','pierce','hyst'],'label':K('좋은 접미','Good suffix')}}
PJ=it('s','모든 투사체 스킬 레벨 +2 (분열, 콜르)','+2 projectile skills (fractured, Kolr)',['proj']); PS=it('p','투사체 속도·피해 1티어','T1 projectile speed or damage',['ps']); SS=it('s','치명타 확률 1티어·관통','T1 crit chance or pierce',['ss'])
WD=it('p','룬 수호 (군왕의 합금)','Runic ward (Sovereign Alloy)',['ward']); HY=it('s','치명타 피해 (발작의 에센스)','Crit damage (Essence of Hysteria)',['hyst'])
G0=[PJ,J('p')]; G1=[PJ,PS]; G2=[PJ,PS,SS]; G3=[PJ,PS,WD,SS,HY]; G4=G3[:1]+[PS,WD,UN('p')]+G3[3:]; G5=[PJ,PS,WD,PS,SS,HY]
ALL4={'all':[{'has':'ps'},{'has':'ss'},{'has':'ward'},{'has':'hyst'}]}
def route(vis=None):   # every step re-checks the item: what is still missing decides the next step; only the edges in vis are drawn
    missS={'not':{'sideAll':{'side':'s','tag':'gs'}}}; missP={'not':{'sideAll':{'side':'p','tag':'gp'}}}
    E=[{'if':{'all':[ALL4,{'count':{'tag':'ps','min':2}}]},'to':'ok'},{'if':{'all':[ALL4,{'full':'p'}]},'to':'apx'},{'if':ALL4,'to':'k15'},
       {'if':{'all':[{'not':{'has':'ps'}},{'not':{'has':'ss'}}]},'to':'kz'},
       {'if':{'all':[{'not':{'has':'ss'}},missS,{'not':{'has':'ward'}}]},'to':'csA'},
       {'if':{'all':[{'not':{'has':'ss'}},missS,{'not':{'has':'hyst'}}]},'to':'csH'},
       {'if':{'all':[{'not':{'has':'ss'}},missS]},'to':'asx'},
       {'if':{'not':{'has':'ss'}},'to':'xs'},
       {'if':{'all':[{'not':{'has':'ps'}},missP,{'not':{'has':'ward'}}]},'to':'cpA'},
       {'if':{'all':[{'not':{'has':'ps'}},missP,{'not':{'has':'hyst'}}]},'to':'cpH'},
       {'if':{'all':[{'not':{'has':'ps'}},missP]},'to':'apx'},
       {'if':{'not':{'has':'ps'}},'to':'xp'},
       {'if':{'all':[{'not':{'has':'ward'}},{'any':[missP,{'full':'p'}]}]},'to':'ja'},
       {'if':{'not':{'has':'ward'}},'to':'jp'},
       {'if':{'any':[missS,{'full':'s'}]},'to':'jh'},
       {'to':'js'}]
    vis=vis or {}; out=[]; shown=set()
    for e in E:
        e=dict(e)
        if e['to'] in vis and e['to'] not in shown: shown.add(e['to']); v=vis[e['to']]; e.update(v if isinstance(v,dict) else {'res':v})
        else: e['hide']=True
        out.append(e)
    return out
def ex(id,pos,omen,show,item,goal,vis):
    return act(id,'main',pos,'exalt','Greater_Exalted_Orb',goal,None,K('엑잘','Exalt'),route(vis),item,show=show,omens=[omen])
def cr(id,pos,cur,ess,omen,goal,shw,item,lbl,vis):
    return act(id,'main',pos,'essence',cur,goal,shw,lbl,route(vis),item,ess=ess,omens=[omen])
F={'res':'fail','port':'right'}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'proj','fr':True},{'junk':'p'}],'quality':30},K('콜르의 사냥 장착, 모든 투사체 +2 분열 + 잡옵 1개 (퀄리티 30%, 특출난 베이스)','Kolr’s Hunt socketed: fractured +2 projectile skills + one junk line (30% quality, Exceptional)'),G0),
 mark([0,0.6],'k8',G0),
 RUNE('k8',[0,1],'k9',G0),
 act('k9','main',[0,2],'chaos','Chaos_Orb',K('콜르 옵션 1티어 하나','One T1 Kolr line'),None,K('카오스','Chaos'),[{'if':{'has':'ps'},'to':'xs','res':'ok'},{'if':{'has':'ss'},'to':'xp','res':'ok'},{'to':'k9','res':'fail'}],G1,show=['pspd','pdmg','crit','pierce']),
 ex('xs',[0,3],'Omen_of_Dextral_Exaltation',['crit','pierce'],G2,K('접미: 치명타 확률 1티어·관통 (접두가 먼저 떴을 때)','Suffix: T1 crit chance or pierce (prefix came first)'),{'jp':'ok','csA':F,'csH':F,'asx':F}),
 cr('csA',[1,3],'Sovereign_Alloy','ward','Omen_of_Dextral_Crystallisation',K('빗나간 접미를 지우고 룬 수호','The missed suffix goes for runic ward'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],G3,K('합금','Alloy'),{'xs':{'port':'right'}}),
 cr('csH',[1,4],'Essence_of_Hysteria','hyst','Omen_of_Dextral_Crystallisation',K('빗나간 접미를 지우고 치명타 피해','The missed suffix goes for crit damage'),[st('s','치명타 피해 (제작 옵션)','Crit damage (crafted)')],G3,K('에센스','Essence'),{'xs':{'port':'right'}}),
 act('asx','main',[1,5],'annul','Orb_of_Annulment',K('빗나간 접미 지우기','Remove the missed suffix'),None,K('소멸','Annul'),route({'xs':{'port':'right'}}),G2,omens=['Omen_of_Dextral_Annulment']),
 ex('xp',[0,6],'Omen_of_Sinistral_Exaltation',['pspd','pdmg'],G2,K('접두: 투사체 속도·피해 1티어 (접미가 먼저 떴을 때)','Prefix: T1 projectile speed or damage (suffix came first)'),{'jp':'ok','cpA':F,'cpH':F,'apx':F}),
 cr('cpA',[1,6],'Sovereign_Alloy','ward','Omen_of_Sinistral_Crystallisation',K('빗나간 접두를 지우고 룬 수호','The missed prefix goes for runic ward'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],G3,K('합금','Alloy'),{'xp':{'port':'right'}}),
 cr('cpH',[1,7],'Essence_of_Hysteria','hyst','Omen_of_Sinistral_Crystallisation',K('빗나간 접두를 지우고 치명타 피해','The missed prefix goes for crit damage'),[st('s','치명타 피해 (제작 옵션)','Crit damage (crafted)')],G3,K('에센스','Essence'),{'xp':{'port':'right'}}),
 act('apx','main',[1,8],'annul','Orb_of_Annulment',K('빗나간 접두 지우기','Remove the missed prefix'),None,K('소멸','Annul'),route({'xp':{'port':'right'}}),G2,omens=['Omen_of_Sinistral_Annulment']),
 act('jp','main',[0,9],'exalt','Exalted_Orb',K('합금이 바꿀 접두 하나 (룬 수호가 아직 없으면)','A prefix for the alloy to replace (if runic ward is still missing)'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),route({'ja':{}}),G2,omens=['Omen_of_Sinistral_Exaltation']),
 cr('ja',[0,10],'Sovereign_Alloy','ward','Omen_of_Sinistral_Crystallisation',K('접두 하나를 지우고 룬 수호 (좋은 접두가 지워지면 4번)','A prefix goes for runic ward (losing the good prefix: back to 4)'),[st('p','룬 수호 (제작 옵션)','Runic ward (crafted)')],G3,K('합금','Alloy'),{'js':'ok','xp':F}),
 act('js','main',[0,11],'exalt','Exalted_Orb',K('에센스가 바꿀 접미 하나 (치명타 피해가 아직 없으면)','A suffix for the essence to replace (if crit damage is still missing)'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),route({'jh':{}}),G2,omens=['Omen_of_Dextral_Exaltation']),
 cr('jh',[0,12],'Essence_of_Hysteria','hyst','Omen_of_Dextral_Crystallisation',K('접미 하나를 지우고 치명타 피해 (좋은 접미가 지워지면 3번)','A suffix goes for crit damage (losing the good suffix: back to 3)'),[st('s','치명타 피해 (제작 옵션)','Crit damage (crafted)')],G3,K('에센스','Essence'),{'k15':'ok','xs':F}),
 resetx('kz',[1,2],'k9'),
 act('k15','main',[0,13],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'k16'}],G4,omens=['Omen_of_Sinistral_Necromancy']),
 act('k16','main',[0,14],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'all':[ALL4,{'count':{'tag':'ps','min':2}}]},'to':'ok','res':'ok'},{'if':{'all':[{'param':{'v':1}},{'unrev':False},{'not':{'added':'ps'}}]},'to':'k16x','res':'fail','port':'right'},{'if':{'all':[{'param':{'v':2}},ALL4]},'to':'ok','res':'ok','hide':True}]+[dict(e,hide=True) for e in route()[1:]],G5,want='ps',show=['pspd','pdmg'],omens=['Omen_of_Abyssal_Echoes'],
     over=[{'param':{'v':2},'set':{'edges':[{'if':ALL4,'to':'ok','res':'ok'}]+[dict(e,hide=True) for e in route()[1:]]}}]),
 annul('k16x',[1,14],[dict(e,hide=True) if e['to']!='k15' else dict(e,port='right') for e in route()]),
 done([0,15])]
graph11('mazbro-proj-gloves-v2','Gloves_str_dex','Blacksteel Gauntlets',82,
  'MazBro 투사체 +2 분열 장갑(원본 레시피 기록) — 콜르의 사냥 + 투사체 +2 분열 + 잡옵(퀄리티 30%) → 아스트리드의 창의성 → 카오스 오브(콜르 1티어 하나) → 반대쪽 면 상위 엑잘 + 면 찬미(빗나가면 결정화 + 군왕의 합금 → 결정화 + 발작의 에센스로 빗나간 옵션을 제작 옵션으로 바꿈) → 남은 제작 옵션 → 고대 갈비뼈 → 공개(투사체 속도·피해 1티어, 하이엔드 = 빛의 징조로 다시). 룬 교체·신성한 오브는 뺌.',
  ROUTE,P2,{'high':K('영상: 공개는 빛의 징조로 다시','Video: Light retries on the reveal'),'bal':K('공개 결과 그대로, 나머지는 영상대로','Keep the reveal, the rest as in the video')},tags,nodes,
  [{'id':'L1','nodes':['k15','k16','k16x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'side':'p','label':K('투사체 속도·피해 1티어','T1 projectile speed or damage')},{'side':'p','label':K('투사체 속도·피해 1티어','T1 projectile speed or damage')} if v=='high' else {'side':'p','random':True},{'tag':'ward','tmax':1},{'tag':'proj','tmax':1,'fr':True},{'side':'s','label':K('치명타 확률 1티어·관통','T1 crit chance or pierce')},{'tag':'hyst','tmax':1}]),
  {'quality':30,'sockets':2},{'all':[{'has':'ps'},{'has':'ss'},{'has':'ward'},{'has':'hyst'}]},('high','bal'),xsub=["Kolr's Hunt"],xroll=True)
