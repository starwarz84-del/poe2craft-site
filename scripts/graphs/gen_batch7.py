# Flowcharts for five more recipes converted 2026-11-10 (사용자: "다른 5개 진행, 최종 확인은 나중에 한번에").
# 어려움 이하 → Balance + Essential (정책 30). Balance = the original recipe (video record), Essential = cheaper bases / looser targets / results kept, no expensive omens.
#   sihan-chayula-sceptre-v2, diztoh-budget-crossbow-v2, diztoh-onehand-mace-v2, saveq-alloy-focus-v2, tankjung-kitava-shield-v2
import os
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch5.py').read(); exec(_src[:_src.index('# ---------- 1.')])
def cleanup(id,pos,keep,edges,target,side=None):
    d={'id':id,'kind':'cleanup','group':'main','pos':pos,'keep':keep,'maxJunk':0,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':target,'edges':edges}
    if side: d['side']=side
    return d
RUNE=lambda id,pos,nxt,item,kr='아스트리드의 창의성 장착',en='Socket Astrid’s Creativity',grp='main',**kw: act(id,grp,pos,'rune',None,K(kr,en),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':nxt}],item,**kw)
REV=lambda kr,en,tag: it('s' if tag else 'p',kr,en,[tag] if tag else None)

# ---------- 1. 시한 차율라 셉터 (-F7pV0Y7BMA) ----------
# 원본: 정신력 % 분열 + 잡옵 → 아스트리드 → 카오스 오브로 접근 효과 범위 1티어 → 좌측 찬미 + 상위 엑잘 → 좌측 결정화 + 수호의 합금 → 좌측 찬미 + 상위 엑잘
# → 좌측 결정화 + 완벽한 명령의 에센스(오라) → 엑잘 2번(접두) → 좌측 강령술 + 보존된 턱뼈(접두가 꽉 차 잡옵 하나를 지우고 들어감) → 공개(정신력 % + 마나 1~4티어).
P={'bal':{'sT':2,'aT':1,'hT':4},'ess':{'sT':4,'aT':2,'hT':6}}
tags={'spirit':{'gi':19,'tmax':'$sT'},'hyb':{'gi':20,'tmax':'$hT'},'hybAny':{'gi':20},'aoe':{'gi':21,'tmax':'$aT'},'ward':{'gi':31},'aura':{'gi':29}}
SPI=it('p','정신력 % (분열)','% Spirit (fractured)',['spirit']); AO=it('s','접근 효과 범위','Presence area of effect',['aoe'])
WA=it('s','룬 수호 (제작 옵션)','Runic Ward (crafted)',['ward']); AU=it('s','오라 크기 (제작 옵션)','Aura magnitudes (crafted)',['aura'])
I0=[SPI,J('p')]; I1=[SPI,AO]; I2=I1+[J('p')]; I3=I1+[WA]; I4=I3+[J('p')]; I5=I3+[AU]; I6=I5+[J('p'),J('p')]; I7=I5+[J('p'),UN('p')]; I8=I5+[J('p'),it('p','정신력 % + 마나','% Spirit + mana',['hyb'])]
nodes=[base('s2',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'p'}]},K('정신력 % 분열 + 잡옵 1개 (퀄리티 20%)','Fractured % Spirit + one junk line (20% quality)'),I0),
 RUNE('s2',[0,1],'ms',I0,grp='prep'),
 mark([0,1.5],'s3',I0),
 act('s3','main',[0,2],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix option'),None,K('카오스','Chaos'),[{'if':{'has':'aoe'},'to':'s4','res':'ok'},{'to':'s3','res':'fail'}],I1,show=['aoe']),
 act('s4','main',[0,3],'exalt','Greater_Exalted_Orb',K('합금이 지울 접두','The prefix for the alloy to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'s5'}],I2,omens=['Omen_of_Sinistral_Exaltation']),
 act('s5','main',[0,4],'essence','Protective_Alloy',K('접두 잡옵을 지우고 접미 수호의 합금','Swap the junk prefix for the Protective Alloy suffix'),[st('s','룬 수호 (제작 옵션)','Runic Ward (crafted)')],K('합금','Alloy'),[{'to':'s6'}],I3,ess='ward',omens=['Omen_of_Sinistral_Crystallisation']),
 act('s6','main',[0,5],'exalt','Greater_Exalted_Orb',K('에센스가 지울 접두','The prefix for the essence to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'s7'}],I4,omens=['Omen_of_Sinistral_Exaltation']),
 act('s7','main',[0,6],'essence','Perfect_Essence_of_Command',K('접두 잡옵을 지우고 접미 오라 크기','Swap the junk prefix for the aura suffix'),[st('s','오라 크기 (제작 옵션)','Aura magnitudes (crafted)')],K('에센스','Essence'),[{'to':'p1'}],I5,ess='aura',omens=['Omen_of_Sinistral_Crystallisation']),
 act('p1','main',[0,7],'exalt','Exalted_Orb',K('접두 두번째 옵션','Second prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'p2'}],I5+[J('p')]),
 act('p2','main',[0,7.5],'exalt','Exalted_Orb',K('접두 세번째 옵션','Third prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'p3'}],I6),
 act('p3','main',[0,8],'desecrate','Preserved_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개) — 접두가 꽉 차 잡옵 하나가 지워짐','Desecrated (unrevealed) — a junk prefix makes way')],K('훼손','Desecrate'),[{'to':'p4'}],I7,omens=['Omen_of_Sinistral_Necromancy']),
 act('p4','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'has':'hyb'},'to':'ok','res':'ok'},{'if':{'all':[{'param':{'sT':2}},{'not':{'has':'hybAny'}}]},'to':'p4x','res':'fail'},{'to':'ok','res':'fail'}],I8,want='hyb',show=['hyb'],omens=['Omen_of_Abyssal_Echoes']),
 annul('p4x',[1,9],[{'to':'p4d','port':'right'}]),
 act('p4d','main',[1,9.6],'desecrate','Preserved_Jawbone',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p4','port':'right'}],I7,omens=['Omen_of_Sinistral_Necromancy']),
 done([0,10])]
graph('sihan-chayula-sceptre-v2','Sceptres','Stoic Sceptre',82,
  '시한 차율라 셉터(원본 레시피 기록) — 정신력 % 분열 + 잡옵 → 아스트리드의 창의성 → 카오스 오브(접근 효과 범위 1티어) → 좌측 찬미 + 상위 엑잘 → 좌측 결정화 + 수호의 합금 → 좌측 찬미 + 상위 엑잘 → 좌측 결정화 + 완벽한 명령의 에센스 → 엑잘 2번 → 좌측 강령술 + 보존된 턱뼈 → 공개(정신력 % + 마나). 밸런스 = 영상(1~4티어, 빛의 징조로 다시), 에센셜 = 정신력 1~4티어 분열·접근 효과 1~2티어, 공개는 결과 그대로.',
  {'sT':{'kr':'정신력 % (분열)','en':'% Spirit (fractured)','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})},'aT':{'kr':'접근 효과 범위','en':'Presence area','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'hT':{'kr':'정신력 % + 마나','en':'% Spirit + mana','values':TV({'4':('1~4티어','T1–4'),'6':('1~6티어','T1–6')})}},P,
  {'bal':K('영상 목표, 공개가 빗나가면 빛의 징조로 다시','Video targets; Light on a missed reveal'),'ess':K('더 싼 분열 베이스, 공개 결과 그대로','Cheaper fractured base, keep the reveal')},
  tags,nodes,[{'id':'L1','nodes':['p4','p4x','p4d'],'kr':'훼손 공개','en':'Reveal'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'spirit','tmax':a},{'tag':'hyb','tmax':h},{'side':'p','random':True},{'tag':'aoe','tmax':b},{'tag':'ward','tmax':1},{'tag':'aura','tmax':1}]} for v,kr,en,a,b,h in (('bal','밸런스 옵션','Balance',2,1,4),('ess','에센셜 옵션','Essential',4,2,6))],
  {'quality':20,'sockets':1},{'all':[{'has':'spirit'},{'has':'aoe'},{'has':'ward'},{'has':'aura'},{'full':'p'}]})

# ---------- 2. Diztoh 가성비 석궁 (vk3pLFUov8U) ----------
# 원본: 노멀 → 완벽한 진화(물리 % 1~2티어, 빗나가면 소멸의 오브) → 완벽한 확장(접미) → 상위 마모의 에센스(물리 추가) → 아스트리드 → 우측 결정화 + 완벽한 전투의 에센스(공격 스킬 +3)
# → 우측 강령술 + 군왕의 징조 + 보존된 턱뼈 → 공개(수류탄 2회 발동, 아마나무 접미 2개라 100%) → 상위 찬미 + 완벽한 엑잘(접두·접미 옵션 1개씩) → (선택) 절사의 징조 + 완벽한 카오스 오브로 접두.
P={'bal':{'pT':2,'eT':3},'ess':{'pT':3,'eT':5}}
tags={'ppct':{'gi':8,'tmax':'$pT'},'flatE':{'gi':39},'battle':{'gi':53},'gren':{'gi':30},
      'hyb':{'gi':9,'tmax':3},'fire':{'gi':4,'tmax':4},'cold':{'gi':5,'tmax':4},'light':{'gi':7,'tmax':4},'eatk':{'gi':23,'tmax':2},
      'pre':{'anyOf':['hyb','fire','cold','light','eatk'],'label':K('복합 물리·원소 피해 추가','Hybrid physical or flat elemental')},
      'keep':{'anyOf':['ppct','flatE','battle','gren','pre']}}
PP=it('p','물리 피해 % 증가','% physical damage',['ppct']); FE=it('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)',['flatE'])
BA=it('s','모든 공격 스킬 레벨 +3 (제작 옵션)','+3 attack skills (crafted)',['battle']); GR=it('s','수류탄 2회 발동 (아마나무)','Grenade double activation (Amanamu)',['gren'])
I0=[]; I1=[PP]; I2=I1+[J('s')]; I3=I2+[FE]; I4=[PP,FE,BA]; I5=I4+[UN('s')]; I6=I4+[GR]; I7=I6+[it('p','랜덤 옵션 1개','One random line',None,'j'),J('s')]; I8=I6+[it('p','복합 물리·원소 피해 추가','Hybrid physical or flat elemental',['pre']),J('s')]
nodes=[base('c3',{'rar':'magic','mods':['ppct']},K('물리 피해 % 매직 석궁 구입 (특출난 베이스, 룬 소켓 3)','Buy a magic exceptional crossbow with % physical (3 rune sockets)'),I1),
 act('c3','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('접미 옵션 1개','One suffix'),[st('s','랜덤 옵션 1개','One random line')],K('확장','Augment'),[{'to':'c4'}],I2),
 act('c4','prep',[0,3],'essence','Greater_Essence_of_Abrasion',K('레어로 업그레이드 + 접두 물리 피해 추가','Upgrade to rare + flat physical prefix'),[st('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)')],K('에센스','Essence'),[{'to':'c5'}],I3,ess='flatE'),
 RUNE('c5',[0,4],'c6',I3,grp='prep'),
 act('c6','prep',[0,5],'essence','Perfect_Essence_of_Battle',K('접미 잡옵을 지우고 공격 스킬 +3','Swap the junk suffix for +3 attack skills'),[st('s','모든 공격 스킬 레벨 +3 (제작 옵션)','+3 attack skills (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I4,ess='battle',omens=['Omen_of_Dextral_Crystallisation']),
 mark([0,5.5],'c7',I4),
 act('c7','main',[0,6],'desecrate','Preserved_Jawbone',K('접미 두번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','아마나무 훼손 옵션(미공개)','Amanamu desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'c8'}],I5,omens=['Omen_of_Dextral_Necromancy','Omen_of_the_Liege']),
 act('c8','main',[0,7],'reveal',None,K('훼손 옵션 확인 (아마나무 2개 전부 나옴)','Reveal (both Amanamu lines show)'),[st('s','수류탄 2회 발동','Grenade double activation')],K('공개','Reveal'),[{'to':'c9'}],I6,want='gren',omens=['Omen_of_Abyssal_Echoes']),
 act('c9','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접두·접미 옵션 1개씩','One prefix and one suffix'),[st(None,'랜덤 옵션 2개 — 복합 물리·원소 피해 추가면 좋음','Two random lines — hybrid physical or flat elemental is good')],K('엑잘','Exalt'),
     [{'if':{'has':'pre'},'to':'ok'},{'if':{'all':[{'param':{'pT':2}},{'whittleSafe':'keep'}]},'to':'c11'},{'to':'ok'}],I7,omens=['Omen_of_Greater_Exaltation'],over=[{'param':{'pT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('c11','main',[0,9],'chaos','Perfect_Chaos_Orb',K('가장 낮은 옵션을 접두로 (버릴 옵션일 때만)','Replace the lowest line (only while it is junk)'),None,K('카오스','Chaos'),
     [{'if':{'has':'pre'},'to':'ok','res':'ok'},{'if':{'whittleSafe':'keep'},'to':'c11','res':'fail'},{'to':'ok','res':'fail'}],I8,show=['pre'],omens=['Omen_of_Whittling']),
 done([0,10])]
graph('diztoh-budget-crossbow-v2','Crossbows','Siege Crossbow',82,
  'Diztoh 가성비 석궁(원본 레시피 기록) — 물리 % 매직 베이스 구입(정책 18 — 영상의 완벽한 진화의 오브 반복은 시뮬상 약 86 div) → 완벽한 확장의 오브(접미) → 상위 마모의 에센스 → 아스트리드 → 우측 결정화 + 완벽한 전투의 에센스 → 우측 강령술 + 군왕의 징조 + 보존된 턱뼈 → 공개(아마나무 접미 2개라 수류탄 2회 발동 확정) → 상위 찬미 + 완벽한 엑잘. 밸런스는 접두가 빗나가면 절사의 징조 + 완벽한 카오스 오브(가장 낮은 옵션이 버릴 옵션일 때만, 영상 선택 단계), 에센셜 = 물리 % 1~3티어 베이스, 상위 엑잘, 결과 그대로.',
  {'pT':{'kr':'물리 피해 %','en':'% physical','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'eT':{'kr':'원소 피해 추가','en':'Flat elemental','values':TV({'3':('1~3티어','T1–3'),'5':('1~5티어','T1–5')})}},P,
  {'bal':K('영상 + 절사로 접두 맞추기','Video + Whittling for the prefix'),'ess':K('더 넓은 목표, 결과 그대로','Looser targets, keep whatever comes')},
  tags,nodes,[],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'ppct','tmax':a},{'tag':'flatE','tmax':1},{'side':'p','label':K('복합 물리·원소 피해 추가','Hybrid physical or flat elemental')},{'tag':'battle','tmax':1},{'tag':'gren','tmax':1},{'side':'s','random':True}]} for v,kr,en,a in (('bal','밸런스 옵션','Balance',2),('ess','에센셜 옵션','Essential',3))],
  {'quality':20,'sockets':3},{'all':[{'has':'ppct'},{'has':'gren'},{'full':'p'},{'full':'s'}]})

# ---------- 3. Diztoh 한손 둔기 (WDEkEIQFgT4) ----------
# 원본: 노멀(퀄리티 20%) → 완벽한 진화(치명타 확률 1~2티어, 소멸의 오브로 다시) → 완벽한 확장(접두) → 상위 가속의 에센스(공격 속도) → 아스트리드 → 좌측 결정화 + 완벽한 전투의 에센스(공격 스킬 +2)
# → 완벽한 엑잘(물리 접두, 빗나가면 좌측 말소의 징조 + 상위 카오스) → 검은 피의 징조 + 보존된 턱뼈 → 완벽한 엑잘(피해 추가) → 공개(쿠르갈 물리 %, 쿠르갈 접두 3개라 100%) → (빗나간 피해 추가는 절사 + 상위 카오스).
P={'bal':{'cT':2,'xT':2},'ess':{'cT':3,'xT':4}}
tags={'crit':{'gi':17,'tmax':'$cT'},'as':{'gi':44},'atk':{'gi':54},'kpct':{'gi':25},
      'hyb':{'gi':8,'tmax':2},'ppct':{'gi':7,'tmax':3},'pflat':{'gi':2,'tmax':'$xT'},'fire':{'gi':3,'tmax':'$xT'},'cold':{'gi':4,'tmax':'$xT'},'light':{'gi':6,'tmax':'$xT'},
      'phys':{'anyOf':['hyb','ppct','pflat'],'label':K('물리 피해 접두','Physical damage prefix')},'good':{'anyOf':['hyb','ppct','pflat','fire','cold','light'],'label':K('물리·원소 피해 접두','Physical or elemental prefix')},'kAny':{'anyOf':[{'gi':25},{'gi':26},{'gi':27}]},'flat':{'anyOf':['pflat','fire','cold','light'],'label':K('물리·원소 피해 추가','Flat physical or elemental')},
      'keep':{'anyOf':['crit','as','atk','kAny','good']}}
CR=it('s','치명타 확률','Critical hit chance',['crit']); AS=it('s','공격 속도 (제작 옵션)','Attack speed (crafted)',['as']); AT=it('s','모든 공격 스킬 레벨 +2 (제작 옵션)','+2 attack skills (crafted)',['atk'])
PH=it('p','물리 피해 접두','Physical damage prefix',['phys']); FL2=it('p','물리·원소 피해 추가','Flat physical or elemental',['flat']); KP=it('p','쿠르갈 물리 % (공격 속도 감소)','Kurgal % physical (reduced attack speed)',['kpct'])
I0=[]; I1=[CR]; I2=I1+[J('p')]; I3=I2+[AS]; I4=[CR,AS,AT]; I5=I4+[PH]; I6=I5+[UN('p')]; I7=I6+[FL2]; I8=I5+[FL2,KP]
nodes=[base('m3',{'rar':'magic','mods':['crit']},K('치명타 확률 매직 둔기 구입 (특출난 베이스, 퀄리티 20%)','Buy a magic exceptional mace with crit chance (20% quality)'),I1),
 act('m3','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('접두 옵션 1개','One prefix'),[st('p','랜덤 옵션 1개','One random line')],K('확장','Augment'),[{'to':'m4'}],I2),
 act('m4','prep',[0,3],'essence','Greater_Essence_of_Haste',K('레어로 업그레이드 + 접미 공격 속도','Upgrade to rare + attack speed suffix'),[st('s','공격 속도 (제작 옵션)','Attack speed (crafted)')],K('에센스','Essence'),[{'to':'m5'}],I3,ess='as'),
 RUNE('m5',[0,4],'m6',I3,grp='prep'),
 act('m6','prep',[0,5],'essence','Perfect_Essence_of_Battle',K('접두 잡옵을 지우고 공격 스킬 +2','Swap the junk prefix for +2 attack skills'),[st('s','모든 공격 스킬 레벨 +2 (제작 옵션)','+2 attack skills (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I4,ess='atk',omens=['Omen_of_Sinistral_Crystallisation']),
 mark([0,5.5],'m7',I4),
 act('m7','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 첫번째 옵션','First prefix option'),[st('p','물리 피해 접두 (안 나와도 그대로 — 공개 뒤 절사로)','Physical prefix (a miss stays — Whittling after the reveal)')],K('엑잘','Exalt'),[{'to':'m8'}],I5,
     over=[{'param':{'cT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('m8','main',[0,7],'desecrate','Preserved_Jawbone',K('접두 두번째 옵션(훼손)','Second prefix (desecrated)'),[st('p','쿠르갈 훼손 옵션(미공개)','Kurgal desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'m9'}],I6,omens=['Omen_of_the_Blackblooded']),
 act('m9','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix option'),[st('p','물리·원소 피해 추가 (안 나오면 공개 뒤 절사)','Flat physical or elemental (a miss: Whittling after the reveal)')],K('엑잘','Exalt'),[{'to':'m10'}],I7,
     over=[{'param':{'cT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('m10','main',[0,9],'reveal',None,K('훼손 옵션 확인 (쿠르갈 3개 전부 나옴)','Reveal (all three Kurgal lines show)'),[st('p','물리 % (공격 속도 감소)','% physical (reduced attack speed)')],K('공개','Reveal'),
     [{'if':{'any':[{'count':{'tag':'good','min':2}},{'param':{'cT':3}}]},'to':'ok'},{'if':{'whittleSafe':'keep'},'to':'m11'},{'to':'ok'}],I8,want='kpct'),
 act('m11','main',[0,10],'chaos','Greater_Chaos_Orb',K('가장 낮은 옵션을 피해 추가로 (버릴 옵션일 때만)','Replace the lowest line (only while it is junk)'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'good','min':2}},'to':'ok','res':'ok'},{'if':{'whittleSafe':'keep'},'to':'m11','res':'fail'},{'to':'ok','res':'fail'}],I8,show=['good'],omens=['Omen_of_Whittling']),
 done([0,11])]
graph('diztoh-onehand-mace-v2','One_Hand_Maces','Marauding Mace',82,
  'Diztoh 한손 둔기(원본 레시피 기록) — 치명타 확률 매직 베이스 구입(정책 18 — 영상의 완벽한 진화 반복은 시뮬상 약 55 div) → 완벽한 확장 → 상위 가속의 에센스 → 아스트리드 → 좌측 결정화 + 완벽한 전투의 에센스 → 완벽한 엑잘(물리 접두, 결과 그대로 — 영상의 좌측 말소의 징조(약 20 div) 반복은 시뮬상 평균 470 div라 뺌) → 검은 피의 징조 + 보존된 턱뼈 → 완벽한 엑잘(피해 추가) → 공개(쿠르갈 접두 3개 — 물리 %가 이미 있으면 같은 계열이라 다른 쿠르갈 옵션) → 밸런스는 물리·원소 피해 접두가 옵션 2개가 될 때까지 절사의 징조 + 상위 카오스(가장 낮은 옵션이 버릴 옵션일 때만). 에센셜 = 치명타 1~3티어 베이스, 상위 엑잘, 결과 그대로.',
  {'cT':{'kr':'치명타 확률','en':'Crit chance','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'xT':{'kr':'피해 추가','en':'Flat damage','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('영상: 빗나가면 말소·절사로 다시','Video: Erasure/Whittling on misses'),'ess':K('목표 넓힘, 결과 그대로','Looser targets, keep whatever comes')},
  tags,nodes,[],
  [{'id':v,'kr':kr,'en':en,'lines':[{'side':'p','label':K('물리·원소 피해 접두','Physical or elemental prefix')},{'side':'p','label':K('쿠르갈 접두 (물리 %가 없으면 물리 % + 공격 속도 감소)','Kurgal prefix (% physical with reduced AS when free)')},{'side':'p','label':K('물리·원소 피해 접두','Physical or elemental prefix')},{'tag':'crit','tmax':a},{'tag':'as','tmax':1},{'tag':'atk','tmax':1}]} for v,kr,en,a in (('bal','밸런스 옵션','Balance',2),('ess','에센셜 옵션','Essential',3))],
  {'quality':20,'sockets':2},{'all':[{'has':'crit'},{'full':'p'},{'full':'s'}]})

# ---------- 4. SaVeQ 합금 집중구 (uCbyTF-LJ5I) ----------
# 원본: 모든 주문 +2 분열 + 주문 피해 1티어 + 주문 치명타(상위 추구의 에센스) + 미공개 훼손 접두 → 공개(에너지 보호막·마나 1티어, 실패는 빛의 징조 + 고대 갈비뼈)
# → 좌측 찬미 + 완벽한 엑잘(합금이 지울 접두) → 아스트리드 → 좌측 결정화 + 초월의 합금(접두 3개 중 하나 삭제) → 완벽한 엑잘(빈 접두, 빗나가면 좌측 소멸의 징조).
P={'bal':{'rT':1,'gT':2},'ess':{'rT':3,'gT':4}}
tags={'lvl':{'gi':16},'spell':{'gi':10,'tmax':1},'critE':{'gi':47},'alloy':{'gi':59},
      'esp':{'gi':7,'tmax':'$rT'},'hyb':{'gi':8,'tmax':'$rT'},'mana':{'gi':5,'tmax':'$rT'},'rev':{'anyOf':['esp','hyb','mana'],'label':K('에너지 보호막 %·복합·마나','% ES, hybrid or mana')},
      'esp2':{'gi':7,'tmax':'$gT'},'hyb2':{'gi':8,'tmax':'$gT'},'esf2':{'gi':6,'tmax':3},'mana2':{'gi':5,'tmax':'$gT'},'spell2':{'gi':10,'tmax':2},
      'gp':{'anyOf':['esp2','hyb2','esf2','mana2','spell2'],'label':K('주문 피해·에너지 보호막·마나','Spell damage, ES or mana')}}
LV=it('s','모든 주문 스킬 레벨 +2 (분열)','+2 all spell skills (fractured)',['lvl']); SPL=it('p','주문 피해 1티어','T1 spell damage',['spell']); CE=it('s','주문 치명타 (제작 옵션)','Spell crit (crafted)',['critE'])
RV=it('p','에너지 보호막 %·복합·마나','% ES, hybrid or mana',['rev']); AL=it('s','초월의 합금 (제작 옵션)','Transcendent Alloy (crafted)',['alloy'])
I0=[LV,SPL,CE,UN('p')]; I1=[LV,SPL,CE,RV]; I2=I1+[J('p')]; I3=[LV,SPL,CE,RV,AL]; I4=I3+[it('p','주문 피해·에너지 보호막·마나','Spell damage, ES or mana',['gp'])]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'lvl','fr':True},'spell',{'tag':'critE','ess':True},{'unrev':'p','bone':'Ancient_Rib'}]},K('모든 주문 +2 분열 집중구 준비','Focus with fractured +2 spells'),I0),
 mark([0,0.6],'v2',I0),
 act('v2','main',[0,1],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'rev'},'to':'v4','res':'ok'},{'if':{'param':{'rT':1}},'to':'v2x','res':'fail'},{'to':'v4','res':'fail'}],I1,want='rev',show=['rev'],omens=['Omen_of_Abyssal_Echoes']),
 annul('v2x',[1,1],[{'to':'v2d','port':'right'}]),
 act('v2d','main',[1,1.6],'desecrate','Ancient_Rib',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'v2','port':'right'}],I0,omens=['Omen_of_Sinistral_Necromancy']),
 act('v4','main',[0,2],'exalt','Perfect_Exalted_Orb',K('합금이 지울 접두','The prefix for the alloy to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'v5'}],I2,omens=['Omen_of_Sinistral_Exaltation'],over=[{'param':{'rT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('v5','main',[0,3],'essence','Transcendent_Alloy',K('아스트리드의 창의성 장착 후 초월의 합금','Socket Astrid’s Creativity, then the Transcendent Alloy'),[st('s','초월의 합금 (접두 3개 중 하나가 지워짐)','Transcendent Alloy (one of the three prefixes goes)')],K('합금','Alloy'),[{'to':'v6'}],I3,ess='alloy',omens=['Omen_of_Sinistral_Crystallisation']),
 act('v6','main',[0,4],'exalt','Perfect_Exalted_Orb',K('빈 접두 채우기','Fill the free prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'gp','min':3}},'to':'ok','res':'ok'},{'if':{'all':[{'param':{'rT':1}},{'full':'p'}]},'to':'v6x','res':'fail'},{'if':{'not':{'full':'p'}},'to':'v6','res':'ok'},{'to':'ok','res':'fail'}],I4,show=['gp'],
     over=[{'param':{'rT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 cleanup('v6x',[1,4],['gp','rev'],[{'lost':'gp','to':'v6x'},{'lost':'rev','to':'v6x'},{'to':'v6','port':'right'}],K('빗나간 접두 제거','Remove the missed prefix'),side='p'),
 done([0,5])]
nodes[0]['group']='prep'
graph('saveq-alloy-focus-v2','Foci','Tasalian Focus',81,
  'SaVeQ 합금 집중구(원본 레시피 기록) — 모든 주문 +2 분열 + 주문 피해 1티어 + 주문 치명타(상위 추구의 에센스) + 미공개 훼손 접두 준비 → 공개(에너지 보호막 %·복합·마나 1티어, 밸런스는 빛의 징조 + 고대 갈비뼈로 다시) → 좌측 찬미 + 완벽한 엑잘 → 아스트리드 + 좌측 결정화 + 초월의 합금(접두 3개 중 하나 삭제) → 완벽한 엑잘로 빈 접두(밸런스는 빗나가면 좌측 소멸의 징조). 에센셜 = 목표 넓힘, 상위 엑잘, 결과 그대로.',
  {'rT':{'kr':'공개 목표','en':'Reveal target','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})},'gT':{'kr':'마지막 접두','en':'Last prefix','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('영상: 1티어까지 빛의 징조, 빗나간 엑잘은 좌측 소멸의 징조','Video: Light until T1, Sinistral Annulment on a miss'),'ess':K('목표 넓힘, 결과 그대로','Looser targets, keep whatever comes')},
  tags,nodes,[{'id':'L1','nodes':['v2','v2x','v2d'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['v6','v6x'],'kr':'빈 접두','en':'Free prefix'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'side':'p','label':K(f'주문 피해·에너지 보호막·마나 1~{t}티어',f'Spell damage, ES or mana T1–{t}')},{'side':'p','label':K(f'주문 피해·에너지 보호막·마나 1~{t}티어',f'Spell damage, ES or mana T1–{t}')},{'side':'p','label':K(f'주문 피해·에너지 보호막·마나 1~{t}티어',f'Spell damage, ES or mana T1–{t}')},{'tag':'lvl','tmax':1},{'tag':'critE','tmax':1},{'tag':'alloy','tmax':1}]} for v,kr,en,t in (('bal','밸런스 옵션','Balance',2),('ess','에센셜 옵션','Essential',4))],
  {'quality':20,'sockets':1},{'all':[{'has':'lvl'},{'has':'alloy'},{'full':'p'},{'full':'s'}]})

# ---------- 5. 탱정 키타바 방패 (gQa51XOS98s, 방패 부분 12:48~22:24) ----------
# 2026-11-12 W5 영상 전체 재대조(새 플로우차트 기준, 정책 11장 맨 위). 근거: scratchpad review/W5-kitava-shield/timeline.md·frames/.
#   화면 = 슬라이드뿐(실제 제작 장면 없음). 0:00~47:36 전 구간 2초 간격 화면 변화 검사 + 슬라이드마다 캡처, 자동 자막(영어 번역판) 전부.
#   방패 슬라이드 STEP 01~14(12:48~22:24): 02 베이스(14:30, 특출난 타호아의 거대 방패 2소켓, 아이템 레벨 정확히 81) · 03 퀄리티 선택(14:58)
#   · 04~05 접미 4종 중 하나, 방법 B(15:24~16:18) · 06 냉기·번개면 맹렬한 유동체(16:20) · 07 확장·제왕 → 보존된 갈비뼈(16:46)
#   · 08 미공개 33.3%(17:12) · 09 분열, 실패면 새 베이스(17:16) · 10 소멸 ×2 → 카오스 반복(17:26) · 11 우측 강령술 + 고대 갈비뼈 + 메아리 → 공개, 빛의 징조 + 소멸(17:56)
#   · 12 상위 찬미 + 완벽한 엑잘 → 완벽한 엑잘(19:06) · 13 절사 + 완벽한 카오스로 방어도 1티어 3종(19:10~21:26) · 14 철 룬·퀄리티(21:28, 제작 무관이라 뺌 — 정책 9).
#   영상 흐름 한 줄(2026-11-12 사용자 지적 20:56 반영 — 슬라이드가 보여 주는 옵션을 확정 옵션으로):
#     분열 = 받는 물리 피해 8% 추가 감소(STEP 04 16:05 파란 테두리 첫 칸, STEP 06 16:30 왼쪽 '받는 물리 피해 감소 8% → 그대로 분열', STEP 11 완성 문구 첫 옵션)
#     카오스 = 화염 저항 최대치 +3%(STEP 11 완성 문구 '물리 피해 감소 8% + 화염 저항 최대치 총 +6%')
#     공개 = 저항 최대치 +3%(STEP 11 '물리 피해 감소 8%가 이미 있다면 → 저항 최대치 +3%'). 화염 저항 최대치는 같은 계열이라 두 번 못 붙고(카오스로 이미 붙음),
#       방패 데이터에 화염 저항 최대치 훼손 전용 옵션도 없어 공개로는 냉기·번개 저항 최대치 +3%(둘 다 성공).
#     유동체(내부 결정, 사용자 결정 2026-11-12): 공개 뒤 맹렬한 유동체로 냉기·번개 → 화염 = 화염 저항 최대치 +3% 두 줄(하나 훼손) = 슬라이드 '총 +6%'.
#       영상(슬라이드 STEP 06 16:18)은 분열 전에만 유동체를 씀 — 이 상자는 영상에 없음. 근거: STEP 11 완성 문구 + 사용자 제공 거래소 실물(화염 저항 최대치 +3% 두 줄 공존).
#   다른 조합(냉기·번개 → 맹렬한 유동체로 화염 분열, 저항 최대치 분열 뒤 물리 피해 감소 공개 등)은 꿀팁 후보로만 — STEP 06 유동체 상자는 이 줄에 없음.
#   등급(난이도 4 = 하이엔드·밸런스, 사용자 확정 2026-11-12): 분열 준비·카오스 오브는 싼 단계라 두 등급 모두 1티어(C15).
#   반복 구간 = 훼손 공개(빛의 징조)·절사 카오스. 하이엔드 = 영상(1티어), 밸런스 = 저항 최대치 공개 1~2티어·방어도 3종 1~2티어(정책 11장 15:02 '유효 옵션은 반드시, 티어만 타협').
#   절사 안전 조건(옛 whittleSafe)은 뺌: 방패 접두는 모두 레벨 75 이하, 접미는 물리 피해 감소 1티어 77·저항 최대치 75 이상이라 절사가 접미를 칠 일이 없음(이전 시뮬에서도 0회).
P={'high':{'mT':1,'aT':1},'bal':{'mT':2,'aT':2}}
tags={'pdr1':{'gi':13,'tmax':1},'mf1':{'gi':14,'tmax':1},'mc1':{'gi':15,'tmax':1},'ml1':{'gi':16,'tmax':1},
      'mf2':{'gi':14,'tmax':2},'mc2':{'gi':15,'tmax':2},'ml2':{'gi':16,'tmax':2},
      'mfT':{'gi':14,'tmax':'$mT'},'mc':{'gi':15,'tmax':'$mT'},'ml':{'gi':16,'tmax':'$mT'},'mcl':{'anyOf':['mc','ml'],'label':K('냉기·번개 저항 최대치 +3%','+3% maximum cold or lightning resistance')},
      'flat':{'gi':6,'tmax':'$aT'},'pct':{'gi':7,'tmax':'$aT'},'hyb':{'gi':8,'tmax':'$aT'},'arm':{'anyOf':['flat','pct','hyb'],'label':K('방어도 최대치·%·복합','Flat, % or hybrid armour')},
      'flat1':{'gi':6,'tmax':1},'pct1':{'gi':7,'tmax':1},'hyb1':{'gi':8,'tmax':1},'flat2':{'gi':6,'tmax':2},'pct2':{'gi':7,'tmax':2},'hyb2':{'gi':8,'tmax':2},
}
ARMDONE={'count':{'tag':'arm','min':3}}
SUFDONE={'all':[{'has':'pdr1'},{'has':'mf1'},{'has':'mcl'}]}
SUF=lambda m='n': it('s','받는 물리 피해 8% 추가 감소 1티어','T1 8% physical damage reduction',['pdr1'],m)
X=lambda: it('x','잡옵','Junk',None,'j')
PD=SUF('f'); MR=it('s','화염 저항 최대치 +3% 1티어','T1 +3% maximum fire resistance',['mf1'])
MRD=it('s','냉기·번개 저항 최대치 +3% (훼손)','+3% maximum cold or lightning resistance (desecrated)',['mcl'],'d')
MFD=it('s','화염 저항 최대치 +3% (훼손)','+3% maximum fire resistance (desecrated)',['mfT'],'d')
I1=[PD,MR]; I2=I1+[UN('s')]; I3=I1+[MRD]; I3F=I1+[MFD]; I4=[J('p'),J('p')]+I3F; I5=[J('p')]+I4
I6=[it('p','방어도 최대치','Flat armour',['flat']),it('p','방어도 %','% armour',['pct']),it('p','방어도 %·기절 한계치 복합','Armour % and stun threshold',['hyb'])]+I3F
OKM={'if':{'has':'pdr1'},'to':'r1','res':'ok','label':K('받는 물리 피해 감소','Physical damage reduction')}
b0=base('m1',None,K('특출난 타호아의 거대 방패 구입 (소켓 2개, 아이템 레벨 81)','Buy an exceptional Tawhoan Tower Shield (two sockets, item level 81)'),[]); b0['id']='b0'; b0.pop('start',None)   # 14:30 STEP 02
nodes=[b0,
 {'id':'hq','kind':'side','group':'prep','pos':[1,0.5],'attach':['b0','m1'],'cur':'Vaal_Armourers_Infuser','goal':K('퀄리티 30%, 선택·비용 미포함','30% quality, optional, not costed'),'label':K('퀄리티','Quality')},   # 14:58 STEP 03
 act('m1','prep',[0,1],'transmute','Perfect_Orb_of_Transmutation',K('매직 첫 옵션','First magic option'),None,K('진화','Transmute'),   # 15:52 STEP 05 '최초 1회'
     [OKM,{'if':{'full':'s'},'to':'m2x','label':K('다른 접미','Another suffix')},{'to':'m2','label':K('접두','A prefix')}],[SUF()],show=['pdr1']),
 act('m2','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('매직 접미 옵션','Magic suffix option'),None,K('확장','Augment'),
     [OKM,{'if':{'not':{'full':'s'}},'to':'m2','res':'fail','label':K('접두','A prefix')},{'to':'m2x','res':'fail','label':K('다른 접미','Another suffix')}],[J('p'),SUF()],show=['pdr1']),
 {'id':'m2x','kind':'act','group':'prep','pos':[1,2],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('빗나간 접미 지우기','Remove the missed suffix'),'edges':[{'if':{'full':'s'},'to':'m2x','label':K('접미가 남음','Suffix still there')},{'to':'m2','label':K('접미가 지워짐','Suffix removed')}]},
 act('r1','prep',[0,3],'augment','Perfect_Orb_of_Augmentation',K('매직 접두 옵션','Magic prefix option'),[st('p','랜덤 옵션 1개','One random option')],K('확장','Augment'),[{'to':'r2'}],[J('p'),SUF()],skipIf={'full':'p'},skipTo='r2',skipNote=K('옵션 2개면 건너뜀','Skip with two options')),   # 16:46 STEP 07
 act('r2','prep',[0,4],'regal','Perfect_Regal_Orb',K('레어 전환','To rare'),[st(None,'옵션 3개','Three options')],K('제왕','Regal'),[{'to':'f1'}],[J('p'),SUF(),X()]),
 act('f1','prep',[0,5],'desecrate','Preserved_Rib',K('분열 확률을 높이기 위해 훼손','Desecrate to raise the fracture odds'),[st(None,'훼손 옵션 1개 (미공개)','One desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f2'}],[J('p'),SUF(),X(),UN('x')]),   # 16:46 STEP 07·17:12 STEP 08
 act('f2','prep',[0,6],'fracture','Fracturing_Orb',K('분열','Fracture'),[st(None,'받는 물리 피해 감소가 분열되면 성공','Success when physical damage reduction fractures')],K('분열','Fracture'),   # 17:16 STEP 09
     [{'if':{'fractured':'pdr1'},'to':'f4','res':'ok'},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another option fractured')}],[J('p'),PD,X(),UN('x')],pAll=True),
 {'id':'xj','kind':'exit','group':'prep','pos':[1,6],'simTo':'b0','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another option fractured — new base')},
 dict(cleanup('f4',[0,7],[],[{'to':'ms','label':K('분열 + 옵션 1개','Fracture + one option')}],K('분열 + 옵션 1개만 남기기','Keep only the fracture + one option')),group='prep',maxJunk=1,item=[PD,X()]),   # 17:26 STEP 10 '소멸의 오브 ×2'
 mark([0,7.6],'t2',[PD,X()]),
 act('t2','main',[0,9],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix option'),None,K('카오스','Chaos'),   # 17:26 STEP 10
     [{'if':{'has':'mf1'},'to':'t3','res':'ok'},{'to':'t2','res':'fail'}],I1,show=['mf1'],skipIf={'has':'mf1'},skipTo='t3',skipHide=True),
 act('t3','main',[0,10],'desecrate','Ancient_Rib',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'t4'}],I2,omens=['Omen_of_Dextral_Necromancy']),   # 17:56 STEP 11 ①②
 act('t4','main',[0,11],'reveal',None,K('접미 세번째 옵션 공개','Reveal the third suffix'),None,K('공개','Reveal'),   # 17:56 STEP 11 ③④
     [{'if':SUFDONE,'to':'tf','res':'ok'},{'to':'t4x','res':'fail'}],I3,want='mcl',show=['mc','ml'],omens=['Omen_of_Abyssal_Echoes']),
 annul('t4x',[1,11],[{'to':'t3','label':K('다시 훼손','Desecrate again')}]),   # 17:56 STEP 11 NO: 빛의 징조 → 소멸의 오브 → ①부터
 act('tf','main',[0,12],'flux','Blazing_Flux',K('냉기·번개 저항 최대치를 화염으로','Cold or lightning maximum resistance into fire'),[st('s','화염 저항 최대치 +3% 두 줄 (하나 훼손)','Two +3% maximum fire resistance lines (one desecrated)')],K('유동체','Flux'),[{'to':'t5'}],I3F),   # 영상에 없음(내부 결정, 사용자 결정 2026-11-12)
 act('t5','main',[0,13],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 2개','Two random options')],K('엑잘','Exalt'),[{'to':'t6'}],I4,omens=['Omen_of_Greater_Exaltation']),   # 19:06 STEP 12 ①②
 act('t6','main',[0,14],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),[st('p','랜덤 옵션 1개','One random option')],K('엑잘','Exalt'),   # 19:06 STEP 12 ③
     [{'to':'t7'}],I5),
 act('t7','main',[0,15.6],'chaos','Perfect_Chaos_Orb',K('가장 낮은 옵션을 방어도로','The lowest option into armour'),[st('p','방어도 최대치·%·복합 1티어','T1 flat, % and hybrid armour')],K('카오스','Chaos'),   # 19:10~21:26 STEP 13
     [{'if':ARMDONE,'to':'ok','res':'ok'},{'to':'t7','res':'fail'}],I6,omens=['Omen_of_Whittling'],skipIf=ARMDONE,skipTo='ok',skipHide=True,
     over=[{'param':{'aT':2},'set':{'showText':[st('p','방어도 최대치·%·복합 1~2티어','T1–2 flat, % and hybrid armour')]}}]),
 done([0,16.6])]
graph('tankjung-kitava-shield-v2','Shields_str','Tawhoan Tower Shield',81,
  '탱정 키타바 방패(gQa51XOS98s, 2026-11-12 W5 영상 전체 재대조, 새 플로우차트 기준) — 특출난 타호아의 거대 방패 → 완벽한 진화 → 완벽한 확장 + 소멸의 오브로 받는 물리 피해 감소 → 완벽한 확장·완벽한 제왕 + 보존된 갈비뼈(미공개) → 분열(실패면 새 베이스) → 소멸 2번 + 카오스 오브(화염 저항 최대치) → 우측 강령술 + 고대 갈비뼈 → 공개(냉기·번개 저항 최대치, 심연의 메아리, 빗나가면 빛의 징조 + 소멸) → 맹렬한 유동체(화염 저항 최대치 두 줄, 영상에 없음) → 상위 찬미 + 완벽한 엑잘 → 완벽한 엑잘 → 절사의 징조 + 완벽한 카오스 오브로 방어도 최대치·%·복합. 하이엔드 = 영상(모두 1티어), 밸런스 = 저항 최대치 공개·방어도 3종 1~2티어. 퀄리티 30%·철 룬은 비용에서 뺌.',
  {'mT':{'kr':'훼손 저항 최대치','en':'Desecrated maximum resistance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'aT':{'kr':'방어도 접두 (절사)','en':'Armour prefixes (Whittling)','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},dict(P,ess=P['bal']),
  {'high':K('영상: 모두 1티어','Video: all T1'),'bal':K('저항 최대치 공개·방어도 3종 1~2티어','T1–2 revealed maximum resistance and armour'),'ess':None},
  tags,nodes,
  [{'id':'L0','nodes':['m2','m2x'],'kr':'매직 접미 찾기','en':'Magic suffix hunt',
    # 다중 루프를 상자 하나로(사용자 확정 2026-11-12 17:06, 정책 11장) — STEP 05 순서도(15:52~16:18)
    'fold':True,'goal':K('매직 접미 받는 물리 피해 8% 추가 감소 1티어','T1 8% physical damage reduction suffix on a magic item'),
    'steps':[{**K('완벽한 확장의 오브로 접미','Perfect Orb of Augmentation for a suffix'),'node':'m2'},
             {**K('빗나간 접미 — 접미가 지워질 때까지 소멸의 오브','Missed suffix: Annulment until the suffix is gone'),'node':'m2x'}],
    'item':[J('p'),SUF()]},
   {'id':'L1','nodes':['t3','t4','t4x'],'kr':'훼손 공개','en':'Desecrated reveal'},{'id':'L2','nodes':['t7'],'kr':'절사','en':'Whittling'}],
  [{'id':'high','kr':'하이엔드 옵션','en':'High-end','lines':[{'tag':'flat1'},{'tag':'pct1'},{'tag':'hyb1'},{'tag':'pdr1','fr':True},{'tag':'mf1'},{'tag':'mf1','des':True}]},
   {'id':'bal','kr':'밸런스 옵션','en':'Balance','lines':[{'tag':'flat2'},{'tag':'pct2'},{'tag':'hyb2'},{'tag':'pdr1','fr':True},{'tag':'mf1'},{'tag':'mf2','des':True}]}],
  {'sockets':2},{'all':[{'has':'pdr1'},{'count':{'tag':'mfT','min':2}},{'has':'mf1'},{'has':'flat'},{'has':'pct'},{'has':'hyb'},{'full':'p'},{'full':'s'}]})
_p=f'{H}/tankjung-kitava-shield-v2.json'; _g=json.load(open(_p))   # 등급: 난이도 4 → 하이엔드·밸런스(사용자 확정 2026-11-12)
_D={'high':K('영상: 모두 1티어','Video: all T1'),'bal':K('저항 최대치 공개·방어도 3종 1~2티어','T1–2 revealed maximum resistance and armour')}
_g['groups']=[{'id':'prep','kr':'베이스템 완성','en':'Finished base','cols':[0,1]},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers','cols':[0,1]}]
_g['start']='b0'
_g['strategies']=[{'id':v,'params':P[v]} for v in ('high','bal')]
_g['versions']=[{'id':v,'kr':kr,'en':en,'params':P[v],'desc':_D[v]} for v,kr,en in (('bal','밸런스','Balance'),('high','하이엔드','High-end'))]
json.dump(_g,open(_p,'w'),ensure_ascii=False,indent=1)

print('wrote 5 graphs (batch 7)')

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_diztoh_onehand_mace.py'): _sp.run([_sy.executable, f'{H}/gen_diztoh_onehand_mace.py'], check=True)   # 2026-11-13 G3: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_sihan_chayula_sceptre.py'): _sp.run([_sy.executable, f'{H}/gen_sihan_chayula_sceptre.py'], check=True)   # 2026-11-13 G7: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_saveq_alloy_focus.py'): _sp.run([_sy.executable, f'{H}/gen_saveq_alloy_focus.py'], check=True)   # 2026-11-13 G9: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_diztoh_budget_crossbow.py'): _sp.run([_sy.executable, f'{H}/gen_diztoh_budget_crossbow.py'], check=True)   # 2026-11-13 G14: 새 기준 전용 생성기가 덮어씀
