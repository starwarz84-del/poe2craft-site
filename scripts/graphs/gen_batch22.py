# Batch 22 (사용자 2026-11-11: "이제부터는 플로우차트 작성 후 > 플로우차트 기반으로 일반 레시피 작성, 쉬운 것부터 플로우차트로 다 바꿔줘")
# 시한 0.5.5 영상 7개(2026-11-11 등록분)를 쉬운 것부터: 목걸이 → 차율라 장갑 → 투구 → 마법봉 → 공격 플랫 반지 → 차율라 반지 → 투사체 장갑.
# 어려움(3) → 밸런스(영상) + 에센셜(결과 그대로·더 싼 목표), 전문가(4) → 하이엔드(영상) + 밸런스(1~2티어) — 정책 30.
# 등급 레시피는 이 그래프를 따라 scripts/recipes_v5_zz-batchz22-v2.py가 만듦(같은 단계 id).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch8.py').read(); exec(_src[:_src.index('# ---------- 1. 라그나')])
C=os.path.join(H,'../../site/data/c')
def itg(s,cls,gi,tags,m='n',ti=0,suffix=None):
    t=json.load(open(f'{C}/{cls}.json'))['groups'][gi]['t'][ti]
    kr,en=t[4].replace('\n',' / '),t[5].replace('\n',' / ')
    if suffix: kr+=f' ({suffix[0]})'; en+=f' ({suffix[1]})'
    return it(s,kr,en,tags,m)
def g22(id,*a,xsub=None,xroll=False,basePrice=None,**k):
    graph8(id,*a,**k); g=json.load(open(f'{H}/{id}.json'))
    if xsub: g['xsub']=xsub
    if xroll: g['xroll']=True
    if basePrice: g['basePrice']=basePrice
    json.dump(g,open(f'{H}/{id}.json','w'),ensure_ascii=False,indent=1)
RUNE22=lambda id,pos,nxt,item: act(id,'main',pos,'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':nxt}],item,rune=K('아스트리드의 창의성','Astrid’s Creativity'))
AST=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
FAIL=lambda to,**k: dict({'to':to,'res':'fail'},**k)
OK=lambda to,**k: dict({'to':to,'res':'ok'},**k)
REV22=lambda id,pos,want,show,ok,retry,item,omens=('Omen_of_Abyssal_Echoes',): act(id,'main',pos,'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
    [{'if':{'added':want},'to':ok,'res':'ok'},{'if':{'param':{'v':1}},'to':retry,'res':'fail'},{'to':ok,'res':'fail'}],item,want=want,show=show,omens=list(omens))
VBE=('bal','ess'); VHB=('high','bal')

# ---------- 1. 시한 차율라 목걸이 (2vyq26ZFgOk) ----------
# 영상 재확인 2026-11-11(사용자 지적: 베이스·에센스 옵션이 틀림): 베이스 = 부재 목걸이(접두·접미 2개, 아이템 레벨 80),
# 정신력 분열에 실패한 매물 = 에너지 보호막 최대치 2티어 + 정신력 1티어 / 민첩 1티어 분열 + 미공개 훼손 접미(약 15 div, 3:08).
# 완벽한 무한의 에센스 = 접미 '힘·민첩·지능 (7—10)% 증가'(힘 +25—27은 상위 무한의 에센스) — 접미가 꽉 차 미공개 훼손 줄이 지워지고 힘 %가 들어감(3:20).
# → 우측 강령술 + 군주의 징조 + 보존된 빗장뼈: 접미가 꽉 차 힘 %가 지워지고 울라만 훼손(3:35) → 공개(모든 스킬 레벨 +1, 심연의 메아리).
# 빗나가면 완벽한 무한의 에센스로 훼손 옵션을 지우고(분열 민첩 말고 지울 접미가 그것뿐) 다시 — 빛의 징조 없음(4:03).
c='Amulets'; P={'bal':{'sT':1,'v':1},'ess':{'sT':2,'v':2}}
tags={'spirit':{'gi':28,'tmax':'$sT'},'es':{'gi':13,'tmax':2},'dex':{'gi':1,'tmax':1},'strp':{'gi':75},'skill':{'gi':56}}
SP=itg('p',c,28,['spirit']); ES=itg('p',c,13,['es'],ti=1); DX=itg('s',c,1,['dex'],'f'); STP=itg('s',c,75,['strp'],'c',suffix=('완벽한 무한의 에센스','Perfect Essence of the Infinite')); SK=itg('s',c,56,['skill'],'d')
I0=[ES,SP,DX,UN('s')]; I1=[ES,SP,DX,STP]; I2=[ES,SP,DX,UN('s')]; I3=[ES,SP,DX,SK]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'es'},{'tag':'spirit'},{'tag':'dex','fr':True},{'unrev':'s'}]},K('정신력 분열에 실패한 부재 목걸이 구입 (약 15 div)','Buy a failed Spirit-fracture Absent Amulet (about 15 div)'),I0),
 mark([0,0.6],'a2',I0),
 act('a2','main',[0,1],'essence','Perfect_Essence_of_the_Infinite',K('접미 두번째 옵션 바꾸기','Swap the second suffix'),[st('s','힘 (7—10)% 증가 (제작 옵션)','(7—10)% increased Strength (crafted)')],K('에센스','Essence'),[{'to':'a3'}],I1,ess='strp'),
 act('a3','main',[0,2],'desecrate','Preserved_Collarbone',K('접미 두번째 옵션(울라만 훼손)','Second suffix (Ulaman desecration)'),[st('s','울라만 훼손 옵션(미공개)','Ulaman desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'a4'}],I2,omens=['Omen_of_Dextral_Necromancy','Omen_of_the_Sovereign']),
 act('a4','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'skill'},'to':'ok','res':'ok'},{'if':{'param':{'v':1}},'to':'a2','res':'fail','port':'right'},{'to':'ok','res':'fail'}],I3,want='skill',show=['skill'],omens=['Omen_of_Abyssal_Echoes']),
 done([0,4])]
g22('sihan-chayula-amulet-v2',c,'Absent Amulet',80,
  '시한 차율라 목걸이(2vyq26ZFgOk, 2026-11-11 영상 재확인) — 정신력 분열에 실패한 부재 목걸이(에너지 보호막 2티어 + 정신력 1티어 / 민첩 분열 + 미공개 훼손) 구입 → 완벽한 무한의 에센스(힘 % — 훼손 줄 자리) → 우측 강령술 + 군주의 징조 + 보존된 빗장뼈(힘 % 자리) → 공개(모든 스킬 레벨 +1). 밸런스 = 영상(빗나가면 에센스로 훼손 줄을 지우고 다시, 빛의 징조 없음), 에센셜 = 정신력 1~2티어 매물, 공개 결과 그대로.',
  {'sT':{'kr':'정신력','en':'Spirit','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,
  {'bal':K('영상: 모든 스킬 레벨 +1이 나올 때까지','Video: until +1 to all skills shows'),'ess':K('더 싼 매물, 공개 결과 그대로','Cheaper listing, keep the reveal')},
  tags,nodes,[{'id':'L1','nodes':['a2','a3','a4'],'kr':'울라만 공개','en':'Ulaman reveal'}],
  FIN(VBE,lambda v:[{'tag':'es'},{'tag':'spirit','tmax':1 if v=='bal' else 2},{'tag':'dex','fr':True},{'tag':'skill','des':True} if v=='bal' else {'side':'s','random':True}]),
  {'quality':20,'sockets':0},{'all':[{'has':'spirit'},{'full':'s'}]},VBE,basePrice=15)

# ---------- 2. 시한 차율라 장갑 (Sf-2cvWhQY0) ----------
# 고정된 싸개 + 카틀라의 순흑, 중독 강도 30% 분열 + 잡옵 → 카오스 오브(저주 활성화 속도 30%) → 상위 + 좌측 찬미 + 완벽한 엑잘(접두 2개) → 상위 + 우측 찬미 + 완벽한 엑잘(접미 2개), 결과 그대로.
# 카틀라의 순흑 옵션 가중치는 공개되지 않아 일반 티어 평균으로 추정(xroll).
c='Gloves_dex_int'; P={'bal':{'v':1},'ess':{'v':2}}
tags={'pois':{'gi':88,'tmax':1},'curse':{'gi':99,'tmax':1},'fast':{'gi':90},'ail':{'gi':89},'with':{'gi':95},'cmag':{'gi':96},
      'pgood':{'anyOf':['fast','ail']},'sgood':{'anyOf':['with','cmag']}}
PO=itg('p',c,88,['pois'],'f'); CU=itg('s',c,99,['curse']); FA=itg('p',c,90,['fast']); WI=itg('s',c,95,['with'])
KAT=it('r','카틀라의 순흑','Katla’s Gloom',None,'r')
I0=[KAT,PO,J('s')]; I1=[KAT,PO,CU]; I2=I1+[FA,R1('p')]; I3=I2+[WI,R1('s')]
EX=lambda v: 'Perfect_Exalted_Orb'
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pois','fr':True},{'junk':'s'}]},K('카틀라의 순흑 장착, 중독 강도 30% 분열 + 잡옵 1개','Katla’s Gloom socketed: fractured 30% poison magnitude + one junk line'),I0),
 mark([0,0.6],'g2',I0),
 act('g2','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'curse'},'to':'g3','res':'ok'},{'to':'g2','res':'fail'}],I1,show=['curse']),
 act('g3','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefixes'),[st('p','랜덤 옵션 2개 — 상태 이상 피해 가속·상태 이상 강도면 좋음','Two random lines — faster ailments or ailment magnitude are good')],K('엑잘','Exalt'),[{'to':'g4'}],I2,
     omens=['Omen_of_Greater_Exaltation','Omen_of_Sinistral_Exaltation'],over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('g4','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),[st('s','랜덤 옵션 2개 — 위축·저주 강도면 좋음','Two random lines — withered or curse magnitude are good')],K('엑잘','Exalt'),[{'to':'ok'}],I3,
     omens=['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation'],over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,4])]
g22('sihan-chayula-gloves-v2',c,'Secured Wraps',82,
  '시한 차율라 장갑(Sf-2cvWhQY0) — 카틀라의 순흑 + 중독 강도 분열 → 카오스 오브(저주 활성화 속도 30%) → 상위 + 좌측 찬미 엑잘(접두 2개) → 상위 + 우측 찬미 엑잘(접미 2개), 결과 그대로. 밸런스 = 영상(완벽한 엑잘티드 오브), 에센셜 = 상위 엑잘티드 오브. 카틀라 옵션 가중치는 추정.',
  {'v':{'kr':'엑잘','en':'Exalt','values':TV({'1':('완벽한 엑잘티드 오브','Perfect Exalted Orb'),'2':('상위 엑잘티드 오브','Greater Exalted Orb')})}},P,
  {'bal':K('영상: 완벽한 엑잘티드 오브','Video: Perfect Exalted Orbs'),'ess':K('상위 엑잘티드 오브','Greater Exalted Orbs')},
  tags,nodes,[],
  FIN(VBE,lambda v:[{'tag':'pois','fr':True},{'tag':'fast','tmax':1 if v=='bal' else 2},{'side':'p','random':True},{'tag':'curse'},{'tag':'with','tmax':1 if v=='bal' else 2},{'side':'s','random':True}]),   # 정책 32
  {'quality':20,'sockets':2},{'all':[{'has':'pois'},{'has':'curse'},{'full':'p'},{'full':'s'}]},VBE,xsub=["Katla's Gloom"],xroll=True)

# ---------- 3. 시한 차율라 투구 (z_r1uAYIusk) ----------
# 웃는 가면, 회피·에너지 보호막 % 분열 + 잡옵 → 카오스 오브(튕겨내기 평점) → 좌측 찬미 + 완벽한 엑잘(회피·에너지 보호막 / 생명력 / 복합, 빗나가면 소멸의 오브)
# → 좌측 강령술 + 고대 갈비뼈 → 공개(남은 방어 접두, 빛의 징조로 다시) → 상위 찬미 + 완벽한 엑잘(접미 2개 결과 그대로). 치명타 확률(자금 여유)은 레시피의 선택 단계.
c='Helmets_dex_int'; P={'bal':{'dT':2,'pT':3,'v':1},'ess':{'dT':3,'pT':3,'v':2}}
tags={'pct':{'gi':9,'tmax':1},'defl':{'gi':21,'tmax':'$dT'},'flat':{'gi':8,'tmax':'$pT'},'life':{'gi':6,'tmax':'$pT'},'hyb':{'gi':10,'tmax':'$pT'},
      'pre':{'anyOf':['flat','life','hyb']}}
PC=itg('p',c,9,['pct'],'f'); DF=itg('s',c,21,['defl']); FL=itg('p',c,8,['flat']); HY=itg('p',c,10,['hyb'],'d')
I0=[PC,J('s')]; I1=[PC,DF]; I2=I1+[FL]; I3=I2+[UN('p')]; I4=I2+[HY]; I5=I4+[R1('s'),R1('s')]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pct','fr':True},{'junk':'s'}]},K('웃는 가면(아이템 레벨 82), 회피·에너지 보호막 % 1티어 분열 + 잡옵 1개','Grinning Mask (item level 82): fractured T1 evasion/ES % + one junk line'),I0),
 mark([0,0.6],'h2',I0),
 act('h2','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'defl'},'to':'h4','res':'ok'},{'to':'h2','res':'fail'}],I1,show=['defl']),
 act('h4','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'pre'},'to':'h5','res':'ok'},{'if':{'param':{'v':1}},'to':'h4x','res':'fail'},{'to':'h5','res':'fail'}],I2,show=['flat','life','hyb'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('h4x',[1,2],[{'if':{'has':'defl'},'to':'h4','port':'right','res':'ok'},{'to':'h2','res':'fail'}],omens=(),target=K('빗나간 접두 지우기 (튕겨내기가 지워지면 카오스부터)','Remove the missed prefix (deflection lost → back to Chaos)')),
 act('h5','main',[0,3],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'h6'}],I3,omens=['Omen_of_Sinistral_Necromancy']),
 REV22('h6',[0,4],'pre',['flat','life','hyb'],'h7','h6x',I4),
 annul('h6x',[1,4],[{'to':'h5','port':'right'}]),
 act('h7','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'ok'}],I5,omens=['Omen_of_Greater_Exaltation']),
 done([0,6])]
g22('sihan-chayula-helmet-v2',c,'Grinning Mask',82,
  '시한 차율라 투구(z_r1uAYIusk) — 회피·에너지 보호막 % 분열 → 카오스 오브(튕겨내기 평점) → 좌측 찬미 + 완벽한 엑잘(방어 접두) → 좌측 강령술 + 고대 갈비뼈 → 공개 → 상위 찬미 + 완벽한 엑잘(접미 2개 결과 그대로). 밸런스 = 영상(튕겨내기 1~2티어, 접두 1~3티어, 빗나가면 다시), 에센셜 = 튕겨내기 1~3티어, 접두·공개 결과 그대로.',
  {'dT':{'kr':'튕겨내기 평점','en':'Deflection','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'pT':{'kr':'방어 접두','en':'Defence prefixes','values':TV({'3':('1~3티어','T1–3')})},
   'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,
  {'bal':K('영상: 방어 접두 3개 + 튕겨내기','Video: three defence prefixes + deflection'),'ess':K('접두·공개 결과 그대로','Keep the prefix and reveal results')},
  tags,nodes,[{'id':'L1','nodes':['h5','h6','h6x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(VBE,lambda v:[{'tag':'pct','fr':True},{'tag':'flat','tmax':3},{'tag':'hyb','tmax':3,'des':True} if v=='bal' else {'side':'p','random':True},{'tag':'defl','tmax':2 if v=='bal' else 3},{'side':'s','random':True},{'side':'s','random':True}]),
  {'quality':20,'sockets':1},{'all':[{'has':'pct'},{'has':'defl'},{'full':'p'},{'full':'s'}]},VBE)

# ---------- 4. 시한 차율라 마법봉 (rSs4fumlHo4) ----------
# 카오스 피해 분열 + 잡옵(특출난, 소켓 2) → 카오스 오브(주문 치명타 명중 확률) → 우측 찬미 + 완벽한 엑잘(지능·마나 재생·시전 속도, 빗나가면 소멸의 오브)
# → 좌측 찬미 + 엑잘(잡옵) → 좌측 결정화 + 완벽한 마술의 에센스(주문 +3) → 아스트리드의 창의성 → 보존된 턱뼈(미공개 훼손) → 좌측 결정화 + 천공의 합금(훼손 옵션을 지우고 마나 + 주문 +1)
# → 군주의 징조 + 보존된 턱뼈 → 공개(추가 물리 피해 획득 — 울라만 접두 2개라 확정).
c='Wands'; P={'bal':{'cT':2,'v':1},'ess':{'cT':3,'v':2}}
tags={'chaos':{'gi':8,'tmax':2},'scrit':{'gi':20,'tmax':'$cT'},'int':{'gi':0,'tmax':2},'mreg':{'gi':16,'tmax':2},'cast':{'gi':19,'tmax':2},'suf':{'anyOf':['int','mreg','cast']},
      'sp3':{'gi':50},'cel':{'gi':59},'ula':{'gi':43}}
CH=itg('p',c,8,['chaos'],'f'); SC=itg('s',c,20,['scrit']); IN=itg('s',c,0,['int']); S3=itg('s',c,50,['sp3'],'c',suffix=('완벽한 마술의 에센스','Perfect Essence of Sorcery'))
CE=itg('p',c,59,['cel'],'c',suffix=('천공의 합금','Celestial Alloy')); UL=itg('p',c,43,['ula'],'d')
I0=[CH,J('s')]; I1=[CH,SC]; I2=I1+[IN]; I3=I2+[J('p')]; I4=I2+[S3]; I5=I4+[AST]; I6=I5+[UN('p')]; I7=I5+[CE]; I8=I7+[UN('p')]; I9=I7+[UL]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'chaos','fr':True},{'junk':'s'}]},K('특출난 마법봉(룬 소켓 2), 카오스 피해 분열 + 잡옵 1개','Exceptional wand (two sockets): fractured chaos damage + one junk line'),I0),
 mark([0,0.6],'w2',I0),
 act('w2','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'scrit'},'to':'w3','res':'ok'},{'to':'w2','res':'fail'}],I1,show=['scrit']),
 act('w3','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'suf'},'to':'w4','res':'ok'},{'if':{'param':{'v':1}},'to':'w3x','res':'fail'},{'to':'w4','res':'fail'}],I2,show=['int','mreg','cast'],omens=['Omen_of_Dextral_Exaltation']),
 annul('w3x',[1,2],[{'if':{'has':'scrit'},'to':'w3','port':'right','res':'ok'},{'to':'w2','res':'fail'}],omens=(),target=K('빗나간 접미 지우기 (주문 치명타가 지워지면 카오스부터)','Remove the missed suffix (spell crit lost → back to Chaos)')),
 act('w4','main',[0,3],'exalt','Exalted_Orb',K('에센스가 지울 접두','The prefix for the essence to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'w5'}],I3,omens=['Omen_of_Sinistral_Exaltation']),
 act('w5','main',[0,4],'essence','Perfect_Essence_of_Sorcery',K('접두 잡옵을 지우고 접미 주문 +3','Swap the junk prefix for +3 spell skills'),[st('s','모든 주문 스킬 레벨 +3 (제작 옵션)','+3 to all spell skills (crafted)')],K('에센스','Essence'),[{'to':'w6'}],I4,ess='sp3',omens=['Omen_of_Sinistral_Crystallisation']),
 RUNE22('w6',[0,5],'w7',I5),
 act('w7','main',[0,6],'desecrate','Preserved_Jawbone',K('합금이 지울 접두(훼손)','A desecrated prefix for the alloy to remove'),[st('p','훼손 옵션(미공개) — 공개하지 않음','Desecrated (unrevealed) — leave it hidden')],K('훼손','Desecrate'),[{'to':'w8'}],I6),
 act('w8','main',[0,7],'essence','Celestial_Alloy',K('미공개 훼손을 지우고 천공의 합금','Swap the hidden desecration for the Celestial Alloy'),[st('p','마나 최대치 + 모든 주문 스킬 레벨 +1 (제작 옵션)','Maximum mana + +1 to all spell skills (crafted)')],K('합금','Alloy'),[{'to':'w9'}],I7,ess='cel',omens=['Omen_of_Sinistral_Crystallisation']),
 act('w9','main',[0,8],'desecrate','Preserved_Jawbone',K('접두 세번째 옵션(울라만 훼손)','Third prefix (Ulaman desecration)'),[st('p','울라만 훼손 옵션(미공개)','Ulaman desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'w10'}],I8,omens=['Omen_of_the_Sovereign']),
 act('w10','main',[0,9],'reveal',None,K('훼손 옵션 확인 (울라만 접두 2개가 모두 나옴)','Reveal (both Ulaman prefixes show)'),[st('p','피해의 (21—25)%를 추가 물리 피해로 획득','Gain (21—25)% of Damage as Extra Physical Damage')],K('공개','Reveal'),[{'to':'ok'}],I9,want='ula',omens=['Omen_of_Abyssal_Echoes']),
 done([0,10])]
g22('sihan-chayula-wand-v2',c,'Primordial Wand',82,
  '시한 차율라 마법봉(rSs4fumlHo4) — 카오스 피해 분열 → 카오스 오브(주문 치명타) → 우측 찬미 + 완벽한 엑잘(지능 등) → 좌측 찬미 잡옵 + 좌측 결정화 + 완벽한 마술의 에센스 → 아스트리드 → 보존된 턱뼈 미공개 훼손 → 좌측 결정화 + 천공의 합금 → 군주의 징조 + 보존된 턱뼈 → 공개(울라만 확정). 밸런스 = 영상(주문 치명타 1~2티어, 접미 빗나가면 다시), 에센셜 = 주문 치명타 1~3티어, 접미 결과 그대로.',
  {'cT':{'kr':'주문 치명타 명중 확률','en':'Spell crit chance','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,
  {'bal':K('영상: 주문 치명타 1~2티어 + 지능 등','Video: T1–2 spell crit + intelligence or similar'),'ess':K('주문 치명타 1~3티어, 접미 결과 그대로','T1–3 spell crit, keep the second suffix')},
  tags,nodes,[],
  FIN(VBE,lambda v:[{'tag':'chaos','fr':True},{'tag':'cel','ess':True},{'tag':'ula','des':True},{'tag':'scrit','tmax':2 if v=='bal' else 3},{'tag':'int'} if v=='bal' else {'side':'s','random':True},{'tag':'sp3','ess':True}]),
  {'quality':20,'sockets':2},{'all':[{'has':'chaos'},{'has':'scrit'},{'has':'sp3'},{'has':'cel'},{'has':'ula'}]},VBE)

# ---------- 5. 시한 공격 플랫 3줄 반지 (bpXgZGw4WQo) ----------
# 무보석 반지, 공격 추가 피해 1티어 분열 + 잡옵(매물 약 75 div) → 균열의 에센스 → 강탈자 기폭제 → 카오스 오브(다른 원소 플랫 — 최대 퀄리티 옵션이 바뀜, 약 100번)
# → 우측 찬미 + 엑잘(잡옵) → 우측 결정화 + 재빠른 합금(공격 속도) → 상위 + 우측 찬미 + 완벽한 엑잘(접미 2개, 결과 그대로) → 고대 빗장뼈 → 공개(원소 플랫, 빛의 징조로 다시).
c='Rings'; P={'bal':{'fT':2,'v':1},'ess':{'fT':3,'v':2}}
tags={'phys':{'gi':13,'tmax':1},'fire':{'gi':15,'tmax':'$fT'},'cold':{'gi':17,'tmax':'$fT'},'lgt':{'gi':19,'tmax':'$fT'},'flat':{'anyOf':['fire','cold','lgt']},
      'maxq':{'gi':71},'as':{'gi':73}}
PH=itg('p',c,13,['phys'],'f'); MQ=itg('p',c,71,['maxq'],'c',suffix=('균열의 에센스','Essence of the Breach')); CO=itg('p',c,17,['cold']); LG=itg('p',c,19,['lgt'],'d')
AS=itg('s',c,73,['as'],'c',suffix=('재빠른 합금','Swift Alloy'))
I0=[PH,J('s')]; I1=[PH,MQ]; I2=[PH,CO]; I3=I2+[J('s')]; I4=I2+[AS]; I5=I4+[R1('s'),R1('s')]; I6=I5+[UN('p')]; I7=I5+[LG]
nodes=[base('f2',{'rar':'rare','mods':[{'tag':'phys','fr':True},{'junk':'s'}]},K('무보석 반지(아이템 레벨 75+), 공격 추가 피해 1티어 분열 + 잡옵 1개 (약 75 div)','Unset Ring (item level 75+): fractured T1 attack flat + one junk line (about 75 div)'),I0),
 act('f2','prep',[0,1],'essence','Essence_of_the_Breach',K('최대 퀄리티 +20%','+20% maximum quality'),[st('p','장신구 최대 퀄리티 +20% (제작 옵션)','+20% to maximum quality (crafted)')],K('에센스','Essence'),[{'to':'f3'}],I1,ess='maxq'),
 act('f3','prep',[0,2],'quality','Reaver_Catalyst',K('공격 퀄리티 40%','40% attack quality'),None,K('퀄리티','Quality'),[{'to':'ms'}],I1,count=20),
 mark([0,2.5],'f4',I1),
 act('f4','main',[0,3],'chaos','Chaos_Orb',K('접두 두번째 옵션 (최대 퀄리티 옵션이 바뀜)','Second prefix (replaces the max-quality line)'),None,K('카오스','Chaos'),[{'if':{'has':'flat'},'to':'f5','res':'ok'},{'to':'f4','res':'fail'}],I2,show=['fire','cold','lgt']),
 act('f5','main',[0,4],'exalt','Exalted_Orb',K('합금이 지울 접미','The suffix for the alloy to remove'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'f6'}],I3,omens=['Omen_of_Dextral_Exaltation']),
 act('f6','main',[0,5],'essence','Swift_Alloy',K('접미 잡옵을 지우고 공격 속도','Swap the junk suffix for attack speed'),[st('s','공격 속도 (7—9)% 증가 (제작 옵션)','(7—9)% increased Attack Speed (crafted)')],K('합금','Alloy'),[{'to':'f7'}],I4,ess='as',omens=['Omen_of_Dextral_Crystallisation']),
 act('f7','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'f8'}],I5,omens=['Omen_of_Greater_Exaltation','Omen_of_Dextral_Exaltation']),
 act('f8','main',[0,7],'desecrate','Ancient_Collarbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f9'}],I6),
 REV22('f9',[0,8],'flat',['fire','cold','lgt'],'ok','f9x',I7),
 annul('f9x',[1,8],[{'to':'f8','port':'right'}]),
 done([0,9])]
g22('sihan-attack-flat-ring-v2',c,'Unset Ring',75,
  '시한 공격 플랫 3줄 반지(bpXgZGw4WQo) — 플랫 1티어 분열 매물 → 균열의 에센스 → 강탈자 기폭제 → 카오스 오브(다른 원소 플랫, 최대 퀄리티 옵션이 바뀜) → 우측 찬미 잡옵 + 우측 결정화 + 재빠른 합금 → 상위·우측 찬미 + 완벽한 엑잘(접미 2개) → 고대 빗장뼈 → 공개(원소 플랫). 밸런스 = 영상(플랫 1~2티어, 공개 빗나가면 빛의 징조로 다시), 에센셜 = 플랫 1~3티어, 공개 결과 그대로.',
  {'fT':{'kr':'원소 공격 추가 피해','en':'Elemental attack flats','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,
  {'bal':K('영상: 플랫 3개 + 공격 속도','Video: three flats + attack speed'),'ess':K('플랫 1~3티어, 공개 결과 그대로','T1–3 flats, keep the reveal')},
  tags,nodes,[{'id':'L1','nodes':['f8','f9','f9x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(VBE,lambda v:[{'tag':'phys','fr':True},{'tag':'cold','tmax':2 if v=='bal' else 3},{'tag':'lgt','tmax':2,'des':True} if v=='bal' else {'side':'p','random':True},{'tag':'as','ess':True},{'side':'s','random':True},{'side':'s','random':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'phys'},{'has':'flat'},{'has':'as'},{'full':'p'},{'full':'s'}]},VBE,basePrice=75)

# ---------- 6. 시한 차율라 반지 (GgD_vxKgNsw) ----------
# 균열 반지, 잔류물 거리 분열(카오스로 안 나오는 옵션) + 잡옵 → 균열의 에센스 → 차율라의 기폭제 60% → 카오스 오브(모든 원소 저항 — 최대 퀄리티 옵션이 바뀜)
# → 좌측 찬미 + 완벽한 엑잘(카오스 피해, 빗나가면 소멸의 오브) → 좌측 강령술 + 군왕의 징조 + 보존된 빗장뼈 → 공개(잔류물 효과, 빛의 징조로 다시) → 완벽한 엑잘(마지막 옵션 결과 그대로).
c='Rings'; P={'high':{'rT':1,'cT':1},'bal':{'rT':2,'cT':2}}
tags={'far':{'gi':106},'res':{'gi':7,'tmax':'$rT'},'chaos':{'gi':33,'tmax':'$cT'},'eff':{'gi':37},'maxq':{'gi':71}}
FR=itg('s',c,106,['far'],'f'); MQ=itg('p',c,71,['maxq'],'c',suffix=('균열의 에센스','Essence of the Breach')); RS=itg('s',c,7,['res']); CHD=itg('p',c,33,['chaos']); EF=itg('p',c,37,['eff'],'d')
I0=[FR,J('s')]; I1=[MQ,FR]; I2=[FR,RS]; I3=[CHD]+I2; I4=I3+[UN('p')]; I5=I3+[EF]; I6=I5+[R1('s')]
nodes=[base('r2',{'rar':'rare','mods':[{'tag':'far','fr':True},{'junk':'s'}]},K('균열 반지, 잔류물 거리 분열 + 잡옵 1개','Breach Ring: fractured remnant pickup range + one junk line'),I0),
 act('r2','prep',[0,1],'essence','Essence_of_the_Breach',K('최대 퀄리티 +20%','+20% maximum quality'),[st('p','장신구 최대 퀄리티 +20% (제작 옵션)','+20% to maximum quality (crafted)')],K('에센스','Essence'),[{'to':'r3'}],I1,ess='maxq'),
 act('r3','prep',[0,2],'quality','Chayulas_Catalyst',K('카오스 퀄리티 60%','60% chaos quality'),None,K('퀄리티','Quality'),[{'to':'ms'}],I1,count=40),
 mark([0,2.5],'r4',I1),
 act('r4','main',[0,3],'chaos','Chaos_Orb',K('접미 두번째 옵션 (최대 퀄리티 옵션이 바뀜)','Second suffix (replaces the max-quality line)'),None,K('카오스','Chaos'),[{'if':{'has':'res'},'to':'r5','res':'ok'},{'to':'r4','res':'fail'}],I2,show=['res']),
 act('r5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 첫번째 옵션','First prefix'),None,K('엑잘','Exalt'),[{'if':{'has':'chaos'},'to':'r6','res':'ok'},{'to':'r5x','res':'fail'}],I3,show=['chaos'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('r5x',[1,4],[{'if':{'has':'res'},'to':'r5','port':'right','res':'ok'},{'to':'r4','res':'fail'}],omens=(),target=K('빗나간 접두 지우기 (저항이 지워지면 카오스부터)','Remove the missed prefix (resistance lost → back to Chaos)')),
 act('r6','main',[0,5],'desecrate','Preserved_Collarbone',K('접두 두번째 옵션(아마나무 훼손)','Second prefix (Amanamu desecration)'),[st('p','아마나무 훼손 옵션(미공개)','Amanamu desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'r7'}],I4,omens=['Omen_of_Sinistral_Necromancy','Omen_of_the_Liege']),
 act('r7','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'eff'},'to':'r8','res':'ok'},{'to':'r7x','res':'fail'}],I5,want='eff',show=['eff'],omens=['Omen_of_Abyssal_Echoes']),
 annul('r7x',[1,6],[{'to':'r6','port':'right'}]),
 act('r8','main',[0,7],'exalt','Perfect_Exalted_Orb',K('마지막 옵션','Last line'),[st(None,'랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'ok'}],I6),
 done([0,8])]
g22('sihan-chayula-ring-v2',c,'Breach Ring',81,
  '시한 차율라 반지(GgD_vxKgNsw) — 잔류물 거리 분열 → 균열의 에센스 → 차율라의 기폭제 60% → 카오스 오브(모든 원소 저항) → 좌측 찬미 + 완벽한 엑잘(카오스 피해, 빗나가면 소멸의 오브) → 좌측 강령술 + 군왕의 징조 + 보존된 빗장뼈 → 공개(잔류물 효과) → 완벽한 엑잘. 하이엔드 = 저항·카오스 피해 1티어(영상 완성품), 밸런스 = 1~2티어(영상: 저항 12% 이상이면 충분).',
  {'rT':{'kr':'모든 원소 저항','en':'All resistances','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'cT':{'kr':'카오스 피해','en':'Chaos damage','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},P,
  {'high':K('영상 완성품: 1티어','Video item: tier 1'),'bal':K('영상 기준: 1~2티어','Video bar: T1–2')},
  tags,nodes,[{'id':'L1','nodes':['r6','r7','r7x'],'kr':'아마나무 공개','en':'Amanamu reveal'}],
  FIN(VHB,lambda v:[{'tag':'chaos','tmax':1 if v=='high' else 2},{'tag':'eff','des':True},{'side':'p','random':True},{'tag':'far','fr':True},{'tag':'res','tmax':1 if v=='high' else 2},{'side':'s','random':True}]),
  {'quality':60,'sockets':0},{'all':[{'has':'far'},{'has':'res'},{'has':'chaos'},{'has':'eff'}]},VHB)

# ---------- 7. 시한 하이엔드 투사체 장갑 (DH4jiORLg10) ----------
# 거대한 미트 + 콜르의 사냥, 투사체 +2 분열 + 잡옵 → 카오스 오브(투사체 추가 발사) → 좌측 찬미 + 엑잘(잡옵) → 좌측 결정화 + 발작의 에센스(치명타 피해 보너스) → 아스트리드의 창의성
# → 좌측 찬미 + 완벽한 엑잘(물리 추가·투사체 피해·투사체 속도). 첫 접두가 빗나가면 징조 없는 소멸의 오브(지워진 게 접미면 그 단계부터),
# 두 번째가 빗나가면 좌측 결정화 + 심연의 에센스(징표) → 보존된 갈비뼈 → 빛의 징조 + 소멸의 오브 → 다시. 마지막 접두 = 고대 갈비뼈 공개(빛의 징조로 다시).
c='Gloves_str'; P={'high':{'pT':1,'aT':1},'bal':{'pT':2,'aT':2}}
tags={'lvl':{'gi':78},'add':{'gi':72,'tmax':'$aT'},'pdmg':{'gi':67,'tmax':'$pT'},'pspd':{'gi':69,'tmax':'$pT'},'phys':{'gi':13,'tmax':'$pT'},'pre':{'anyOf':['phys','pdmg','pspd']},
      'cdb':{'gi':54},'mk':{'gi':56}}
LV=itg('s',c,78,['lvl'],'f'); AD=itg('s',c,72,['add']); CD=itg('s',c,54,['cdb'],'c',suffix=('발작의 에센스','Essence of Hysteria'))
PHY=itg('p',c,13,['phys']); PS=itg('p',c,69,['pspd']); PD=itg('p',c,67,['pdmg'],'d'); MK=it('p','심연의 군주의 징표','Mark of the Abyssal Lord',['mk'],'c')
KOL=it('r','콜르의 사냥','Kolr’s Hunt',None,'r')
I0=[KOL,LV,J('p')]; I1=[KOL,LV,AD]; I2=I1+[J('p')]; I3=I1+[CD]; I4=I3+[AST]; I5=I4+[PHY]; I6=I5+[PS]; I7=I6+[UN('p')]; I8=I6+[PD]
G1={'all':[{'has':'add'},{'has':'cdb'}]}   # suffixes done
def RT(first):   # after an annulment: a lost suffix → clear back to the fracture and rebuild (cheap — the point of fracturing +2 projectiles)
    return [{'if':{'all':[{'has':'add'},{'has':'cdb'}]},'to':first,'port':'right','res':'ok'},{'to':'pc','res':'fail'}]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'lvl','fr':True},{'junk':'p'}]},K('거대한 미트(룬 소켓 2), 콜르의 사냥 장착 상태로 투사체 +2 분열 + 잡옵 1개','Massive Mitts (two sockets) with Kolr’s Hunt: fractured +2 projectile skills + one junk line'),I0),
 mark([0,0.6],'p2',I0),
 act('p2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'add'},'to':'p3','res':'ok'},{'to':'p2','res':'fail'}],I1,show=['add']),
 act('p3','main',[0,2],'exalt','Exalted_Orb',K('에센스가 지울 접두','The prefix for the essence to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'p4'}],I2,omens=['Omen_of_Sinistral_Exaltation']),
 act('p4','main',[0,3],'essence','Essence_of_Hysteria',K('접두 잡옵을 지우고 치명타 피해 보너스','Swap the junk prefix for critical damage bonus'),[st('s','치명타 피해 보너스 (25—29)% 증가 (제작 옵션)','(25—29)% increased Critical Damage Bonus (crafted)')],K('에센스','Essence'),[{'to':'p5'}],I3,ess='cdb',omens=['Omen_of_Sinistral_Crystallisation']),
 RUNE22('p5',[0,4],'p6',I4),
 act('p6','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 첫번째 옵션','First prefix'),None,K('엑잘','Exalt'),[{'if':{'has':'pre'},'to':'p7','res':'ok'},{'to':'p6x','res':'fail'}],I5,show=['phys','pdmg','pspd'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('p6x',[1,5],RT('p6'),omens=(),target=K('빗나간 접두 지우기','Remove the missed prefix')),
 {'id':'pc','kind':'cleanup','group':'main','pos':[2,5],'keep':['lvl'],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('분열 + 옵션 1개만 남기기','Leave the fracture and one line'),'edges':[{'to':'p2','res':'fail'}]},
 act('p7','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'pre','min':3}},'to':'ok','res':'ok'},{'if':{'all':[{'count':{'tag':'pre','min':2}},{'not':{'full':'p'}}]},'to':'p8','res':'ok'},{'to':'p7m','res':'fail'}],I6,show=['phys','pdmg','pspd'],omens=['Omen_of_Sinistral_Exaltation']),
 act('p7m','main',[1,6],'essence','Essence_of_the_Abyss',K('접두 하나를 지우고 징표','A prefix goes for the Mark'),[st('p','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),[{'to':'p7b'}],I6,ess='mk',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 act('p7b','main',[1,7],'desecrate','Preserved_Rib',K('징표 훼손','Desecrate the Mark'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p7l'}],I6,fromMark=True),
 annul('p7l',[1,8],[{'if':{'all':[{'count':{'tag':'pre','min':2}},{'has':'add'},{'has':'cdb'}]},'to':'p8','res':'ok'},{'if':{'all':[{'has':'pre'},{'has':'add'},{'has':'cdb'}]},'to':'p7','port':'right','res':'ok'},{'if':{'all':[{'has':'add'},{'has':'cdb'}]},'to':'p6','res':'fail'},{'to':'pc','res':'fail'}]),
 act('p8','main',[0,7],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p9'}],I7,omens=['Omen_of_Sinistral_Necromancy']),
 act('p9','main',[0,8],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'pre'},'to':'ok','res':'ok'},{'to':'p9x','res':'fail'}],I8,want='pre',show=['phys','pdmg','pspd'],omens=['Omen_of_Abyssal_Echoes']),
 annul('p9x',[2,8],[{'to':'p8','port':'right'}]),
 done([0,9])]
g22('sihan-proj-gloves-v2',c,'Massive Mitts',80,
  '시한 하이엔드 투사체 장갑(DH4jiORLg10) — 콜르의 사냥 + 투사체 +2 분열 → 카오스 오브(추가 발사) → 좌측 찬미 잡옵 + 좌측 결정화 + 발작의 에센스 → 아스트리드 → 좌측 찬미 + 완벽한 엑잘 접두 2개(첫째 빗나가면 소멸의 오브, 둘째 빗나가면 심연의 에센스 징표 → 보존된 갈비뼈 → 빛의 징조) → 고대 갈비뼈 공개. 하이엔드 = 1티어(영상), 밸런스 = 1~2티어(영상: 2티어는 금방). 콜르 옵션 가중치는 추정.',
  {'pT':{'kr':'접두 3개','en':'Three prefixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'aT':{'kr':'투사체 추가 발사','en':'Additional projectile','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},P,
  {'high':K('영상: 접두 1티어 3개','Video: three tier 1 prefixes'),'bal':K('접두 1~2티어','T1–2 prefixes')},
  tags,nodes,[{'id':'L1','nodes':['p7m','p7b','p7l'],'kr':'접두 하나만 지우기','en':'Remove one prefix'},{'id':'L2','nodes':['p8','p9','p9x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(VHB,lambda v:[{'tag':'phys','tmax':1 if v=='high' else 2},{'tag':'pspd','tmax':1 if v=='high' else 2},{'tag':'pdmg','tmax':1 if v=='high' else 2,'des':True},{'tag':'lvl','fr':True},{'tag':'add','tmax':1 if v=='high' else 2},{'tag':'cdb','ess':True}]),
  {'quality':20,'sockets':2},{'all':[{'has':'lvl'},{'has':'add'},{'has':'cdb'},{'count':{'tag':'pre','min':3}}]},VHB,xsub=["Kolr's Hunt"],xroll=True)
