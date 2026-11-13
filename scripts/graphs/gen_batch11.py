# Batch 11 (사용자 2026-11-10: 남은 레시피를 쉬운 것부터) — 어려움(3) → Balance (video) + Essential (results kept).
#   diztoh-as-spear-v2 (also replaces the duplicate diztoh-twister-spear: same video), diztoh-socket-gloves-v2, seek-cyclone-boots-v2
# Sim addition: graph.xroll — the socketed rune's lines also roll on exalts / chaos (each tier at the average normal tier weight, estimate).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch10.py').read(); exec(_src[:_src.index('# ---------- 1. SL')])
def graph11(*a, xroll=False, **k):
    if a[0] in ('gold-amulet-6line-v2',): return   # 내린 플로우차트(2026-11-11, build_recipes.py REMOVED)
    graph10(*a, **k)
    if xroll:
        g=json.load(open(f'{H}/{a[0]}.json')); g['xroll']=True; json.dump(g,open(f'{H}/{a[0]}.json','w'),ensure_ascii=False,indent=1)
def WHIT(id,pos,keep,want,okto,item,show,cur='Chaos_Orb'):
    return act(id,'main',pos,'chaos',cur,K('가장 낮은 옵션을 다시 (버릴 옵션일 때만)','Reroll the lowest line (only while it is junk)'),None,K('카오스','Chaos'),
        [{'if':{'has':want},'to':okto,'res':'ok'},{'if':{'whittleSafe':keep},'to':id,'res':'fail'},{'to':okto,'res':'fail'}],item,show=show,omens=['Omen_of_Whittling'])

# ---------- 1. Diztoh 트위스터 공격 속도 창 (cTjgn7NnHR8) ----------
# 원본: 투사체 +4 분열 + 잡옵(아스트리드의 창의성 장착) → 카오스 오브(공격 속도 1~3티어) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 군왕의 합금(장착 증강 효과)
# → 엑잘 → 좌측 결정화 + 천공의 합금(정확도 + 공격 속도) → 스루드의 완력으로 교체 → 고대 턱뼈 → 공개(명시 속도 옵션 강화, 빛의 징조로 다시)
# → 완벽한 엑잘(물리 접두, 빗나가면 절사의 징조 + 카오스 오브).
P={'bal':{'v':1},'ess':{'v':2}}
tags={'proj':{'gi':11,'tmax':1},'as':{'gi':17,'tmax':3},'sov':{'gi':63},'cel':{'gi':64},'thrud':{'gi':74},
      'ppct':{'gi':8,'tmax':2},'hyb':{'gi':9,'tmax':2},'flat':{'gi':3,'tmax':2},'phys':{'anyOf':['ppct','hyb','flat'],'label':K('물리 피해 접두','Physical damage prefix')},
      'keep':{'anyOf':['proj','as','sov','cel','thrud','phys']}}
PJ=it('s','투사체 스킬 +4 (분열)','+4 projectile skills (fractured)',['proj']); AS=it('s','공격 속도','Attack speed',['as']); SV=it('s','장착 증강 효과 (군왕의 합금)','Socketed augment effect (Sovereign Alloy)',['sov'])
CE=it('p','정확도 + 공격 속도 (천공의 합금)','Accuracy + attack speed (Celestial Alloy)',['cel']); TH=it('p','명시 속도 옵션 강화 (스루드의 완력)','Explicit speed magnitudes (Thrud’s Might)',['thrud']); PH=it('p','물리 피해 접두','Physical damage prefix',['phys'])
I0=[PJ,J('p')]; I1=[PJ,AS]; I2=I1+[J('p')]; I3=I1+[SV]; I4=I3+[J('p')]; I5=I3+[CE]; I6=I5+[UN('p')]; I7=I5+[TH]; I8=I7+[PH]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'proj','fr':True},{'junk':'p'}]},K('투사체 스킬 +4 분열 + 잡옵 1개 (아스트리드의 창의성 장착)','Fractured +4 projectile skills + one junk line (Astrid’s Creativity socketed)'),I0),
 mark([0,0.6],'a2',I0),
 act('a2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'as'},'to':'a3','res':'ok'},{'to':'a2','res':'fail'}],I1,show=['as']),
 act('a3','main',[0,2],'exalt','Exalted_Orb',K('합금이 지울 접두','The prefix for the alloy to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'a4'}],I2,omens=['Omen_of_Sinistral_Exaltation']),
 act('a4','main',[0,3],'essence','Sovereign_Alloy',K('접두 잡옵을 지우고 장착 증강 효과','Swap the junk prefix for socketed augment effect'),[st('s','장착 증강 효과 (제작 옵션)','Socketed augment effect (crafted)')],K('합금','Alloy'),[{'to':'a5'}],I3,ess='sov',omens=['Omen_of_Sinistral_Crystallisation']),
 act('a5','main',[0,4],'exalt','Exalted_Orb',K('합금이 지울 접두','The prefix for the alloy to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'a6'}],I4),
 act('a6','main',[0,5],'essence','Celestial_Alloy',K('접두 잡옵을 정확도 + 공격 속도로','Swap the junk prefix for accuracy + attack speed'),[st('p','정확도 + 공격 속도 (제작 옵션)','Accuracy + attack speed (crafted)')],K('합금','Alloy'),[{'to':'a8'}],I5,ess='cel',omens=['Omen_of_Sinistral_Crystallisation']),
 act('a8','main',[0,6],'desecrate','Ancient_Jawbone',K('스루드의 완력으로 교체 후 접두 훼손','Swap to Thrud’s Might, then desecrate a prefix'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'a9'}],I6),
 act('a9','main',[0,7],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'thrud'},'to':'a10','res':'ok'},{'to':'a9x','res':'fail'}],I7,want='thrud',show=['thrud'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('a9x',[1,7],'a8'),
 act('a10','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'phys'},'to':'ok','res':'ok'},{'if':{'all':[{'param':{'v':1}},{'whittleSafe':'keep'}]},'to':'a11','res':'fail'},{'to':'ok','res':'fail'}],I8,show=['ppct','hyb','flat'],
     over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 WHIT('a11',[1,8],'keep','phys','ok',I8,['ppct','hyb','flat']),
 done([0,9])]
graph11('diztoh-as-spear-v2','Spears','Akoyan Spear',82,
  'Diztoh 트위스터 공격 속도 창(원본 레시피 기록, 같은 영상의 두 레시피를 하나로) — 투사체 +4 분열 + 잡옵(아스트리드의 창의성) → 카오스 오브(공격 속도) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 군왕의 합금 → 엑잘 → 좌측 결정화 + 천공의 합금 → 스루드의 완력 교체 → 고대 턱뼈 → 공개(명시 속도 옵션 강화, 빛의 징조로 다시) → 완벽한 엑잘(물리 접두, 밸런스는 빗나가면 절사의 징조 + 카오스 오브 — 가장 낮은 옵션이 버릴 옵션일 때만). 스루드 옵션은 공개 가중치가 없어 추정. 에센셜 = 상위 엑잘 결과 그대로.',
  ROUTE,PV,{'bal':K('영상: 물리 접두까지 절사의 징조','Video: Whittling until a physical prefix'),'ess':K('상위 엑잘 결과 그대로','Greater Exalt, keep it')},tags,nodes,
  [{'id':'L1','nodes':['a8','a9','a9x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('bal','ess'),lambda v:[{'tag':'cel','tmax':1},{'tag':'thrud','tmax':1},{'side':'p','label':K('물리 피해 접두','Physical damage prefix')} if v=='bal' else {'side':'p','random':True},{'tag':'proj','tmax':1,'fr':True},{'tag':'as','tmax':3},{'tag':'sov','tmax':1}]),
  {'quality':20,'sockets':2},{'all':[{'has':'proj'},{'has':'as'},{'has':'thrud'},{'full':'p'}]},('bal','ess'),xsub=["Thrud's Might"])

# ---------- 2. Diztoh 소켓 효과 장갑 (CI7zQO_Ml_s) ----------
# 원본: 콜르의 사냥 장착 + 투사체 +2 분열 + 에너지 보호막 최대치 + 희귀도(상위 풍요의 에센스) + 미공개 훼손 접두 → 아스트리드 → 좌측 결정화 + 경악의 에센스(장착 증강 효과 60%, 접두 둘 중 하나가 지워짐)
# → 훼손이 지워졌으면 고대 갈비뼈 → 공개(에너지 보호막 %·투사체 피해·속도) → 완벽한 엑잘(남은 접두, 빗나가면 좌측 소멸의 징조) / 에너지 보호막이 지워졌으면 완벽한 엑잘 2번 → 남은 훼손 공개.
tags={'proj2':{'gi':82},'esf':{'gi':8,'tmax':2},'rar':{'gi':57},'sock':{'gi':59},'esp':{'gi':9},'pdmg':{'gi':71},'pspd':{'gi':73},
      'pre':{'anyOf':['esp','pdmg','pspd'],'label':K('에너지 보호막 %·투사체 피해·투사체 속도','% ES, projectile damage or speed')},'pre4':{'anyOf':['esf','esp','pdmg','pspd'],'label':K('에너지 보호막·투사체 접두','ES or projectile prefix')}}
P2=it('s','투사체 스킬 +2 (분열, 콜르)','+2 projectile skills (fractured, Kolr)',['proj2']); EF=it('p','에너지 보호막 최대치','Flat energy shield',['esf']); RA=it('s','희귀도 (제작 옵션)','Rarity (crafted)',['rar'])
SO=it('s','장착 증강 효과 60% (에센스)','60% socketed augment effect (essence)',['sock']); PRx=lambda: it('p','에너지 보호막·투사체 접두','ES or projectile prefix',['pre4'])
I0=[EF,UN('p'),P2,RA]; I1=[EF,P2,RA,SO]; I2=I1[:1]+[UN('p')]+I1[1:]; I3=[EF,PRx(),P2,RA,SO]; I4=[EF,PRx(),PRx(),P2,RA,SO]; Im=[UN('p'),P2,RA,SO]; Im2=[UN('p'),PRx(),PRx(),P2,RA,SO]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'proj2','fr':True},'esf',{'tag':'rar','ess':True},{'unrev':'p','bone':'Ancient_Rib'}]},K('콜르의 사냥 장착, 투사체 +2 분열 + 에너지 보호막 + 희귀도 + 미공개 훼손 (특출난 베이스)','Kolr’s Hunt socketed: fractured +2 projectile + flat ES + rarity + unrevealed desecration (exceptional)'),I0),
 mark([0,0.6],'d7',I0),
 RUNE('d7',[0,1],'d8',I0),
 act('d8','main',[0,2],'essence','Essence_of_Horror',K('접두 하나를 지우고 장착 증강 효과 60%','A prefix goes for 60% socketed augment effect'),[st('s','장착 증강 효과 60% (제작 옵션)','60% socketed augment effect (crafted)')],K('에센스','Essence'),
     [{'if':{'unrev':False},'to':'d9','res':'ok'},{'to':'dm1','res':'fail'}],I1,ess='sock',omens=['Omen_of_Sinistral_Crystallisation']),
 act('d9','main',[0,3],'desecrate','Ancient_Rib',K('접두 두번째 옵션(훼손)','Second prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d10'}],I2),
 REVEAL('d10',[0,4],'pre',['esp','pdmg','pspd'],'d11','d10x',I3),
 LIGHTX('d10x',[1,4],'d9'),
 act('d11','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre4','min':3}},'to':'ok','res':'ok'},{'to':'ok','res':'fail'}],I4,show=['esp','pdmg','pspd'],
     over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('dm1','main',[2,3],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개 (에너지 보호막이 지워졌을 때)','Two prefixes (when the ES line went)'),[st('p','에너지 보호막·투사체 접두 (결과 그대로)','ES or projectile prefixes (as they come)')],K('엑잘','Exalt'),[{'to':'dm3'}],Im2,omens=['Omen_of_Greater_Exaltation'],
     over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 REVEAL('dm3',[2,4],'pre',['esp','pdmg','pspd'],'ok','dm3x',I4),
 LIGHTX('dm3x',[3,4],'dm3d'),
 act('dm3d','main',[3,4.6],'desecrate','Ancient_Rib',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'dm3','port':'right'}],Im2),
 done([0,6])]
graph11('diztoh-socket-gloves-v2','Gloves_int','Sirenscale Gloves',81,
  'Diztoh 소켓 효과 장갑(원본 레시피 기록) — 콜르의 사냥 장착 + 투사체 +2 분열 + 에너지 보호막 + 희귀도 + 미공개 훼손 → 아스트리드 → 좌측 결정화 + 경악의 에센스(접두 둘 중 하나가 지워짐) → 훼손이 지워졌으면 고대 갈비뼈 → 공개 → 완벽한 엑잘(결과 그대로 — 영상의 좌측 소멸의 징조 반복은 시뮬상 평균 약 650 div라 뺌), 에너지 보호막이 지워졌으면 엑잘 옵션 2개 → 남은 훼손 공개(빛의 징조로 다시). 콜르 옵션(투사체 피해·속도)은 가중치가 없어 추정. 그림은 엑잘 옵션 2개를 상위 찬미로 표시(영상은 엑잘 2번).',
  ROUTE,PV,{'bal':K('영상: 공개는 빛의 징조로 다시, 마지막 접두는 완벽한 엑잘 결과 그대로','Video: Light on the reveal, last prefix Perfect Exalt kept'),'ess':K('상위 엑잘 결과 그대로','Greater Exalt, kept')},tags,nodes,
  [{'id':'L1','nodes':['d9','d10','d10x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['dm3','dm3x','dm3d'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('bal','ess'),lambda v:[{'side':'p','label':K('에너지 보호막·투사체 접두','ES or projectile prefix')},{'side':'p','label':K('에너지 보호막·투사체 접두','ES or projectile prefix')},{'side':'p','label':K('에너지 보호막·투사체 접두','ES or projectile prefix')} if v=='bal' else {'side':'p','random':True},{'tag':'proj2','tmax':1,'fr':True},{'tag':'rar','tmax':1},{'tag':'sock','tmax':1}]),
  {'quality':20,'sockets':3},{'all':[{'has':'proj2'},{'has':'sock'},{'full':'p'}]},('bal','ess'),xsub=["Kolr's Hunt"],xroll=True)

# ---------- 3. 시크 돌개바람 장화 (cj9o8_LuFQs) ----------
# 원본: 방어도 원소 적용 분열 + 잡옵 → 우트레드의 성좌 → 카오스 오브(충전 미소모, 우트레드) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘(접두 옵션 2개) → 좌측 결정화 + 신비한 합금(정신력)
# → (가성비 마무리 가능) 세를의 승리(접미 +1) → 우측 강령술 + 보존된 갈비뼈 → 공개(지속시간·저항) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘(방어도·생명력 접두, 빗나가면 좌측 소멸의 징조).
RES=[2,3,4]
tags={'ele':{'gi':20,'tmax':1},'chg':{'gi':60,'tmax':2},'spirit':{'gi':53},'dur':{'gi':55,'tmax':2},**{f'r{g}':{'gi':g,'tmax':2} for g in RES},
      'rev':{'anyOf':['dur']+[f'r{g}' for g in RES],'label':K('지속시간·저항','Duration or resistance')},
      'aes':{'gi':9,'tmax':2},'flat':{'gi':8,'tmax':1},'life':{'gi':6,'tmax':2},'pre':{'anyOf':['aes','flat','life'],'label':K('방어도·에너지 보호막·생명력 접두','Armour/ES or life prefix')}}
EL=it('s','방어도 원소 적용 (분열)','Armour applies to elemental (fractured)',['ele']); CH=it('s','충전 미소모 (우트레드)','Charges not removed (Uhtred)',['chg']); SP=it('s','정신력 (합금)','Spirit (alloy)',['spirit'])
RV=it('s','지속시간·저항','Duration or resistance',['rev']); PRE=lambda: it('p','방어도·생명력 접두','Armour or life prefix',['pre'])
I0=[EL,J('p')]; I1=[EL,CH]; I2=I1+[J('p'),J('p')]; I3=I1+[SP,J('p')]; I4=I3+[UN('s')]; I5=I3+[RV]; I6=[EL,CH,SP,RV,J('p'),PRE(),PRE()]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'ele','fr':True},{'junk':'p'}]},K('방어도 원소 적용 분열 + 잡옵 1개 (특출난 베이스, 우트레드의 성좌 장착)','Fractured armour applies to elemental + one junk line (exceptional, Uhtred socketed)'),I0),
 mark([0,0.6],'k3',I0),
 act('k3','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'chg'},'to':'k4','res':'ok'},{'to':'k3','res':'fail'}],I1,show=['chg']),
 act('k4','main',[0,2],'exalt','Perfect_Exalted_Orb',K('합금이 지울 접두 옵션 2개','Two prefixes for the alloy to remove from'),[st('p','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'k5'}],I2,omens=['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation']),
 act('k5','main',[0,3],'essence','Mystic_Alloy',K('접두 하나를 지우고 정신력','A prefix goes for Spirit'),[st('s','정신력 (제작 옵션)','Spirit (crafted)')],K('합금','Alloy'),[{'if':{'param':{'v':2}},'to':'k10'},{'to':'k7'}],I3,ess='spirit',omens=['Omen_of_Sinistral_Crystallisation']),
 act('k7','main',[0,4],'rune',None,K('세를의 승리 장착 (접미 +1)','Socket Serle’s Triumph (+1 suffix)'),[st(None,'접미 옵션 4개','Four suffixes')],K('룬','Rune'),[{'to':'k8'}],I3,slots={'s':1}),
 act('k8','main',[0,5],'desecrate','Preserved_Rib',K('접미 네번째 옵션(훼손)','Fourth suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'k9'}],I4,omens=['Omen_of_Dextral_Necromancy']),
 act('k9','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'rev'},'to':'k10','res':'ok'},{'to':'k9x','res':'fail'}],I5,want='rev',show=['dur']+[f'r{g}' for g in RES],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('k9x',[1,6],'k8'),
 act('k10','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개','Two prefixes'),None,K('엑잘','Exalt'),
     [{'if':{'has':'pre'},'to':'ok','res':'ok'},{'if':{'param':{'v':1}},'to':'k10x','res':'fail'},{'to':'ok','res':'fail'}],I6,show=['aes','flat','life'],omens=['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation']),
 cleanup('k10x',[1,7],[],[{'to':'k10','port':'right'}],K('빗나간 접두 옵션 2개 지우기','Remove the two missed prefixes'),side='p',maxJunk=1),
 done([0,8])]
graph11('seek-cyclone-boots-v2','Boots_str_int','Faithful Leggings',81,
  '시크 돌개바람 장화(원본 레시피 기록) — 방어도 원소 적용 분열 + 잡옵(우트레드의 성좌) → 카오스 오브(충전 미소모) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘 → 좌측 결정화 + 신비한 합금 → 세를의 승리 → 우측 강령술 + 보존된 갈비뼈 → 공개(지속시간·저항, 빛의 징조로 다시) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘(방어도·생명력, 밸런스는 빗나가면 좌측 소멸의 징조). 에센셜 = 영상의 가성비 마무리(세를의 승리·훼손 없이 접두 엑잘 결과 그대로). 우트레드 옵션은 가중치가 없어 추정.',
  ROUTE,PV,{'bal':K('영상: 세를의 승리 + 훼손 공개 + 접두 다시','Video: Serle’s Triumph, reveal, prefix retries'),'ess':K('영상의 가성비 마무리','The video’s budget finish')},tags,nodes,
  [{'id':'L1','nodes':['k8','k9','k9x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['k10','k10x'],'kr':'접두','en':'Prefixes'}],
  FIN(('bal','ess'),lambda v:[{'side':'p','random':True},{'side':'p','label':K('방어도·생명력 접두','Armour or life prefix')},{'side':'p','random':True},{'tag':'ele','tmax':1,'fr':True},{'tag':'chg','tmax':2},{'tag':'spirit','tmax':1}]+([{'side':'s','label':K('지속시간·저항','Duration or resistance')}] if v=='bal' else [])),
  {'quality':20,'sockets':3},{'all':[{'has':'ele'},{'has':'chg'},{'has':'spirit'},{'full':'p'}]},('bal','ess'),xsub=["Uhtred's Sidereus"],xroll=True)
print('wrote 3 graphs (batch 11)')

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_seek_cyclone_boots.py'): _sp.run([_sy.executable, f'{H}/gen_seek_cyclone_boots.py'], check=True)   # 2026-11-13 G4: 새 기준 전용 생성기가 덮어씀

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_diztoh_socket_gloves.py'): _sp.run([_sy.executable, f'{H}/gen_diztoh_socket_gloves.py'], check=True)   # 2026-11-13 G3: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_diztoh_as_spear.py'): _sp.run([_sy.executable, f'{H}/gen_diztoh_as_spear.py'], check=True)   # 2026-11-13 G3: 새 기준 전용 생성기가 덮어씀
