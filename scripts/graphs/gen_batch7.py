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

# ---------- 5. 탱정 키타바 방패 (gQa51XOS98s, 방패 부분) ----------
# 원본: 받는 물리 피해 감소 분열 + 잡옵 → 카오스 오브로 최대 저항 1티어 → 우측 강령술 + 고대 갈비뼈 → 공개(최대 저항, 빛의 징조로 다시)
# → 상위 찬미 + 완벽한 엑잘(접두 옵션 2개) → 완벽한 엑잘(접두) → 절사의 징조 + 완벽한 카오스 오브로 방어도 1티어 옵션 3개(방어도 1티어 레벨 75가 접두 최고라 절사는 늘 잡옵만 침).
# 2026-11-12 영상 전체 대조(자막 12:00~21:30 방패 부분, 메인 세션): 단계 일치(카오스 → 우측 강령술 + 고대 갈비뼈 + 메아리, 빛의 징조로 다시 → 상위 찬미 + 완벽한 엑잘 → 완벽한 엑잘 → 절사 + 완벽한 카오스). 영상 = 모두 1티어 종결 방패.
#   등급 C17: 하이엔드 = 영상(1티어), 밸런스 = 최대 저항·방어도 1~2티어, 에센셜 = 1~4티어(최대 저항은 3티어까지만 있음).
P={'high':{'mT':1,'aT':1},'bal':{'mT':2,'aT':2},'ess':{'mT':3,'aT':4}}
tags={'pdr':{'gi':13,'tmax':1},'mf':{'gi':14,'tmax':'$mT'},'mc':{'gi':15,'tmax':'$mT'},'ml':{'gi':16,'tmax':'$mT'},'maxres':{'anyOf':['mf','mc','ml'],'label':K('최대 저항 +%','Maximum resistance')},
      'flat':{'gi':6,'tmax':'$aT'},'pct':{'gi':7,'tmax':'$aT'},'hyb':{'gi':8,'tmax':'$aT'},'arm':{'anyOf':['flat','pct','hyb'],'label':K('방어도 접두','Armour prefix')},
      'keep':{'anyOf':['pdr','maxres','arm']}}
PD=it('s','받는 물리 피해 감소 (분열)','Physical damage reduction (fractured)',['pdr']); MR=it('s','최대 저항 +%','Maximum resistance',['maxres']); AR=lambda: it('p','방어도 접두','Armour prefix',['arm'])
I0=[PD,J('s')]; I1=[PD,MR]; I2=I1+[UN('s')]; I3=I1+[MR]; I4=I3+[J('p'),J('p')]; I5=I4+[J('p')]; I6=I3+[AR(),AR(),AR()]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pdr','fr':True},{'junk':'s'}]},K('받는 물리 피해 감소 분열 + 잡옵 1개 (퀄리티 20%)','Fractured physical damage reduction + one junk line (20% quality)'),I0),
 mark([0,0.6],'t2',I0),
 act('t2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix option'),None,K('카오스','Chaos'),[{'if':{'has':'maxres'},'to':'t3','res':'ok'},{'to':'t2','res':'fail'}],I1,show=['maxres']),
 act('t3','main',[0,2],'desecrate','Ancient_Rib',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'t4'}],I2,omens=['Omen_of_Dextral_Necromancy']),
 act('t4','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'maxres'},'to':'t5','res':'ok'},{'to':'t4x','res':'fail'}],I3,want='maxres',show=['maxres'],omens=['Omen_of_Abyssal_Echoes']),
 annul('t4x',[1,3],[{'to':'t3','port':'right'}]),
 act('t5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'t6'}],I4,omens=['Omen_of_Greater_Exaltation']),
 act('t6','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'if':{'count':{'tag':'arm','min':3}},'to':'ok','res':'ok','hide':True},{'if':{'whittleSafe':'keep'},'to':'t7'},{'to':'ok','res':'fail','hide':True}],I5),
 act('t7','main',[0,6],'chaos','Perfect_Chaos_Orb',K('가장 낮은 옵션을 방어도 1티어로','The lowest line into T1 armour'),[st('p','방어도 1티어 (최대치·%·복합) 옵션 3개','Three T1 armour lines (flat, %, hybrid)')],K('카오스','Chaos'),
     [{'if':{'count':{'tag':'arm','min':3}},'to':'ok','res':'ok'},{'if':{'whittleSafe':'keep'},'to':'t7','res':'fail'},{'to':'ok','res':'fail'}],I6,omens=['Omen_of_Whittling']),
 done([0,7])]
nodes[0]['group']='prep'
graph('tankjung-kitava-shield-v2','Shields_str','Tawhoan Tower Shield',81,
  '탱정 키타바 방패(gQa51XOS98s) — 받는 물리 피해 감소 분열 + 잡옵 → 카오스 오브(최대 저항) → 우측 강령술 + 고대 갈비뼈 → 공개(최대 저항, 빛의 징조로 다시) → 상위 찬미 + 완벽한 엑잘 → 완벽한 엑잘 → 절사의 징조 + 완벽한 카오스 오브로 방어도 옵션 3개. 하이엔드 = 영상(모두 1티어), 밸런스 = 1~2티어, 에센셜 = 최대 저항 1~3티어·방어도 1~4티어.',
  {'mT':{'kr':'최대 저항','en':'Maximum resistance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'aT':{'kr':'방어도 접두 3개 (절사)','en':'Three armour prefixes (Whittling)','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'high':K('영상: 최대 저항·방어도 1티어','Video: T1 max res and armour'),'bal':K('최대 저항·방어도 1~2티어','T1–2 max res and armour'),'ess':K('최대 저항 1~3티어, 방어도 1~4티어','T1–3 max res, T1–4 armour')},
  tags,nodes,[{'id':'L1','nodes':['t3','t4','t4x'],'kr':'최대 저항 공개','en':'Max res reveal'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'arm'},{'tag':'arm'},{'tag':'arm'},{'tag':'pdr','tmax':1,'fr':True},{'tag':'maxres'},{'tag':'maxres'}]} for v,kr,en in (('high','하이엔드 옵션','High-end'),('bal','밸런스 옵션','Balance'),('ess','에센셜 옵션','Essential'))],
  {'quality':20,'sockets':2},{'all':[{'has':'pdr'},{'count':{'tag':'maxres','min':2}},{'full':'p'},{'full':'s'}]})
_p=f'{H}/tankjung-kitava-shield-v2.json'; _g=json.load(open(_p))   # 등급 C17: 하이엔드·밸런스·에센셜
_D={'high':K('영상: 최대 저항·방어도 1티어','Video: T1 max res and armour'),'bal':K('최대 저항·방어도 1~2티어','T1–2 max res and armour'),'ess':K('최대 저항 1~3티어, 방어도 1~4티어','T1–3 max res, T1–4 armour')}
_g['strategies']=[{'id':v,'params':P[v]} for v in ('high','bal','ess')]
_g['versions']=[{'id':v,'kr':kr,'en':en,'params':P[v],'desc':_D[v]} for v,kr,en in (('ess','에센셜','Essential'),('bal','밸런스','Balance'),('high','하이엔드','High-end'))]
json.dump(_g,open(_p,'w'),ensure_ascii=False,indent=1)
print('wrote 5 graphs (batch 7)')
