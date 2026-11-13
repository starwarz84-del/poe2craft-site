# Flowcharts for five more recipes converted 2026-11-10 (사용자: "이대로 5개 더" — 영상 기록을 다시 보고, 비싼 징조는 꼭 필요할 때만).
# All are 어려움 이하 → Balance + Essential (정책 30). Balance = the video, Essential = cheaper bases / looser targets / results kept.
#   diztoh-es-helmet-v2, belton-plus8-wand-v2, lilbotq-armour-shield-v2, diztoh-vile-robe-v2, diztoh-talisman-v2
import os
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch5.py').read(); exec(_src[:_src.index('# ---------- 1.')])   # shared helpers (it, act, annul, base, mark, done, graph …)
def cleanup(id,pos,keep,edges,target,side=None):
    d={'id':id,'kind':'cleanup','group':'main','pos':pos,'keep':keep,'maxJunk':0,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':target,'edges':edges}
    if side: d['side']=side
    return d
L2=lambda kr,en,tag: it('p',kr,en,[tag])

# ---------- 1. Diztoh 에너지 보호막 투구 (yegMdBTuEtY, 자막 확인) ----------
# 영상: 매직(에너지 보호막 최대치 1티어 + 희귀도) → 상위 무한의 에센스(지능) → 좌측 강령술 + 고대 갈비뼈 → 분열(에너지 보호막 최대치)
# → 우측 찬미 + 상위 엑잘(접미 채우기) → 상위 엑잘(접두: 희귀도 또는 에너지 보호막 %) → 공개(심연의 메아리) → 희귀도 1티어. 실패 처리는 영상에 없음.
P={'bal':{'pT':3,'rT':1},'ess':{'pT':4,'rT':2}}
tags={'esf':{'gi':7,'tmax':1},'esp':{'gi':8,'tmax':'$pT'},'rarP':{'gi':17,'tmax':'$rT'},'rarS':{'gi':16,'tmax':1},'int':{'gi':38},
      'pre':{'anyOf':['esp','rarP'],'label':K('에너지 보호막 % 또는 희귀도','% energy shield or rarity')}}
ESF=it('p','에너지 보호막 최대치 (분열)','Flat energy shield (fractured)',['esf']); RS=it('s','아이템 희귀도','Item rarity',['rarS']); IN=it('s','지능 (제작 옵션)','Intelligence (crafted)',['int'])
PRE=lambda: it('p','에너지 보호막 % 또는 희귀도','% energy shield or rarity',['pre'])
I0=[ESF,UN('p'),RS,IN]; I1=I0+[J('s')]; I2=I1+[PRE()]; I3=[ESF,RS,IN,J('s'),PRE(),PRE()]
GOOD2={'count':{'tag':'pre','min':2}}
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'esf','fr':True},{'unrev':'p','bone':'Ancient_Rib'},'rarS',{'tag':'int','ess':True}]},K('에너지 보호막 최대치 분열 티아라 준비','Fractured flat energy shield tiara'),I0),
 mark([0,0.6],'e2',I0),
 act('e2','main',[0,1],'exalt','Greater_Exalted_Orb',K('접미 세 번째 옵션','Third suffix option'),[st('s','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'e3'}],I1,omens=['Omen_of_Dextral_Exaltation']),
 act('e3','main',[0,2],'exalt','Greater_Exalted_Orb',K('접두 두 번째 옵션','Second prefix option'),[st('p','에너지 보호막 % 또는 희귀도 (안 나와도 그대로)','% energy shield or rarity (keep whatever comes)')],K('엑잘','Exalt'),[{'to':'e4'}],I2),
 act('e4','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':GOOD2,'to':'ok','res':'ok'},{'if':{'all':[{'param':{'rT':1}},{'not':{'added':'pre'}},{'count':{'tag':'pre','min':1}}]},'to':'e4x','res':'fail'},{'to':'ok','res':'fail'}],I3,want='pre',show=['pre'],omens=['Omen_of_Abyssal_Echoes']),
 annul('e4x',[1,3],[{'to':'e4d','port':'right'}]),
 act('e4d','main',[1,3.6],'desecrate','Ancient_Rib',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'e4','port':'right'}],I2,omens=['Omen_of_Sinistral_Necromancy']),
 done([0,4])]
nodes[0]['group']='prep'
graph('diztoh-es-helmet-v2','Helmets_int','Kamasan Tiara',81,
  'Diztoh 에너지 보호막 투구(영상 자막 확인 2026-11-10) — 에너지 보호막 최대치 1티어 분열 + 미공개 훼손 접두(고대 갈비뼈) + 희귀도 + 지능(상위 무한의 에센스) 준비 → 우측 찬미 + 상위 엑잘(접미) → 상위 엑잘(접두, 결과 그대로) → 공개(심연의 메아리). 소멸의 오브 반복 없음. 빛의 징조는 밸런스에서 좋은 접두 옵션 2개를 완성할 수 있을 때만. 밸런스 = 영상(에너지 보호막 % 1~3티어·희귀도 1티어), 에센셜 = 1~4티어·1~2티어, 결과 그대로.',
  {'pT':{'kr':'에너지 보호막 %','en':'% energy shield','values':TV({'3':('1~3티어','T1–3'),'4':('1~4티어','T1–4')})},'rT':{'kr':'접두 희귀도','en':'Prefix rarity','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},P,
  {'bal':K('영상 목표, 남은 훼손이 빗나가면 빛의 징조로 다시','Video targets; Light on a missed reveal'),'ess':K('목표 넓힘, 결과 그대로','Looser targets, keep whatever comes')},
  tags,nodes,[{'id':'L1','nodes':['e4','e4x','e4d'],'kr':'훼손 공개','en':'Reveal'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'esf','tmax':1},{'side':'p','label':K(f'에너지 보호막 % 또는 희귀도 1~{t}티어',f'% energy shield or rarity T1–{t}')},{'side':'p','label':K(f'에너지 보호막 % 또는 희귀도 1~{t}티어',f'% energy shield or rarity T1–{t}')},{'tag':'rarS','tmax':1},{'tag':'int','tmax':1},{'side':'s','random':True}]} for v,kr,en,t in (('bal','밸런스 옵션','Balance',3),('ess','에센셜 옵션','Essential',4))],
  {'quality':20,'sockets':2},{'all':[{'has':'esf'},{'full':'p'},{'full':'s'}]})

# ---------- 2. Belton +8 완드 (j0FeuX0NZQI, 자막 확인) ----------
# 영상: 모든 주문 +4 레어 구입 → 접두·접미 작업 후 분열(초월의 합금이 분열됨) → 천공의 합금 → 군왕의 징조 훼손 공개(원소 피해 = 화염·냉기·번개 % 막기)
# → 좌측 찬미 + 완벽한 엑잘(추가 피해·주문 피해) → 빛의 징조로 막기 옵션 삭제 → 우측 강령술 + 고대 턱뼈(접미) → 완벽한 엑잘(카오스 피해 3티어로 타협).
P={'bal':{'xT':2,'yT':3,'sT':1,'cT':2},'ess':{'xT':4,'yT':5,'sT':3,'cT':4}}
tags={'l4':{'gi':10,'tmax':1},'trans':{'gi':60},'cel':{'gi':59},'ele':{'gi':30},
      'xF':{'gi':26,'tmax':'$xT'},'xC':{'gi':27,'tmax':'$xT'},'xL':{'gi':28,'tmax':'$xT'},'spell':{'gi':3,'tmax':'$yT'},'hyb':{'gi':4,'tmax':1},
      'pre':{'anyOf':['xF','xC','xL','spell','hyb'],'label':K('추가 피해 획득·주문 피해','Extra damage or spell damage')},
      'regen':{'gi':16,'tmax':'$sT'},'scrit':{'gi':20,'tmax':'$cT'},'cdmg':{'gi':21,'tmax':'$cT'},
      'suf':{'anyOf':['regen','scrit','cdmg'],'label':K('마나 재생·주문 치명타·주문 치명타 피해','Mana regen, spell crit or spell crit damage')}}
L4=it('s','모든 주문 스킬 레벨 +4','+4 all spell skills',['l4']); TR=it('s','초월의 합금 (분열)','Transcendent Alloy (fractured)',['trans']); CE=it('p','천공의 합금 (제작 옵션)','Celestial Alloy (crafted)',['cel'])
EL=it('p','원소 피해 증가 (아마나무, 막기)','Elemental damage (Amanamu, blocker)',['ele']); PR=lambda: it('p','추가 피해 획득·주문 피해','Extra damage or spell damage',['pre'])
I0=[L4,TR,CE,UN('p')]; I1=[L4,TR,CE,EL]; I2=I1+[PR()]; I3=[L4,TR,CE,PR()]; I4=I3+[UN('s')]; I5=I3+[it('s','마나 재생·주문 치명타·주문 치명타 피해','Mana regen or spell crit',['suf'])]; I6=I5+[it('p','랜덤 옵션 1개','One random line',None,'j')]
BAL={'param':{'sT':1}}
nodes=[base('ms',{'rar':'rare','mods':['l4',{'tag':'trans','fr':True,'ess':True},{'tag':'cel','ess':True},{'unrev':'p','bone':'Preserved_Jawbone','lord':'amanamu'}]},K('모든 주문 +4 · 초월의 합금 분열 완드 준비','+4 all spells wand with fractured Transcendent Alloy'),I0),
 mark([0,0.6],'b2',I0),
 act('b2','main',[0,1],'reveal',None,K('훼손 옵션 확인 (아마나무 3개 전부 나옴)','Reveal (all three Amanamu lines show)'),[st('p','원소 피해 증가 — 화염·냉기·번개 %를 막음','Elemental damage — blocks fire, cold and lightning %')],K('공개','Reveal'),[{'to':'b3'}],I1,want='ele',omens=['Omen_of_Abyssal_Echoes']),
 act('b3','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 세 번째 옵션','Third prefix option'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre','min':1}},'to':'b4','res':'ok'},{'if':BAL,'to':'b3x','res':'fail'},{'to':'b4','res':'fail'}],I2,show=['pre'],omens=['Omen_of_Sinistral_Exaltation']),
 cleanup('b3x',[1,2],['cel','ele','pre'],[{'lost':'cel','to':'b3c','port':'right'},{'lost':'ele','to':'b3','port':'right'},{'to':'b3','port':'right'}],K('빗나간 접두 제거 (천공의 합금이 지워지면 다시)','Remove the missed prefix (Celestial Alloy gone: craft it again)'),side='p'),
 act('b3c','main',[2,2],'essence','Celestial_Alloy',K('천공의 합금 다시','Celestial Alloy again'),[st('p','천공의 합금 (제작 옵션)','Celestial Alloy (crafted)')],K('합금','Alloy'),[{'to':'b3','port':'right'}],I1,ess='cel',omens=['Omen_of_Sinistral_Crystallisation']),
 annul('b4',[0,3],[{'to':'b5'}],target=K('원소 피해(막기 옵션) 제거','Remove the elemental damage blocker')),
 act('b5','main',[0,4],'desecrate','Ancient_Jawbone',K('접미 세 번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'b6'}],I4,omens=['Omen_of_Dextral_Necromancy']),
 act('b6','main',[0,5],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'suf'},'to':'b7','res':'ok'},{'if':BAL,'to':'b6x','res':'fail'},{'to':'b7','res':'fail'}],I5,want='suf',show=['suf'],omens=['Omen_of_Abyssal_Echoes']),
 annul('b6x',[1,5],[{'to':'b6d','port':'right'}]),
 act('b6d','main',[1,5.6],'desecrate','Ancient_Jawbone',K('다시 훼손','Desecrate again'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'b6','port':'right'}],I4,omens=['Omen_of_Dextral_Necromancy']),
 act('b7','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 마지막 옵션','Last prefix option'),[st('p','추가 피해 획득·주문 피해 (안 나와도 그대로 — 영상: 카오스 피해 3티어)','Extra or spell damage (keep whatever comes — chaos damage T3 in the video)')],K('엑잘','Exalt'),[{'to':'ok'}],I6,
     over=[{'param':{'sT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,7])]
nodes[0]['group']='prep'
graph('belton-plus8-wand-v2','Wands','Dueling Wand',82,
  'Belton +8 완드(영상 자막 확인 2026-11-10) — 모든 주문 +4 · 초월의 합금 분열 · 천공의 합금 · 군왕의 징조 미공개 훼손 준비 → 공개(원소 피해 = 막기, 아마나무 3개 전부) → 좌측 찬미 + 완벽한 엑잘(추가 피해·주문 피해) → 빛의 징조 + 소멸의 오브로 막기 옵션 삭제 → 우측 강령술 + 고대 턱뼈 → 공개 → 마지막 접두 엑잘(결과 그대로). 밸런스 = 영상(빗나간 엑잘은 좌측 소멸의 징조로 다시, 공개 실패는 빛의 징조), 에센셜 = 목표 넓힘·결과 그대로·마지막 엑잘은 상위 엑잘티드 오브.',
  {'xT':{'kr':'추가 피해 획득','en':'Extra damage','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})},'yT':{'kr':'주문 피해','en':'Spell damage','values':TV({'3':('1~3티어','T1–3'),'5':('1~5티어','T1–5')})},
   'sT':{'kr':'마나 재생','en':'Mana regen','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})},'cT':{'kr':'주문 치명타','en':'Spell crit','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('영상 목표, 빗나가면 다시','Video targets, redo misses'),'ess':K('목표 넓힘, 결과 그대로','Looser targets, keep whatever comes')},
  tags,nodes,[{'id':'L1','nodes':['b3','b3x'],'kr':'접두 엑잘','en':'Prefix exalt'},{'id':'L2','nodes':['b6','b6x','b6d'],'kr':'접미 훼손 공개','en':'Suffix reveal'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'cel','tmax':1},{'side':'p','label':K(f'추가 피해 획득 1~{x}티어·주문 피해 1~{y}티어',f'Extra damage T1–{x} or spell damage T1–{y}')},{'side':'p','random':True},{'tag':'l4','tmax':1},{'tag':'trans','tmax':1},{'side':'s','label':K(f'마나 재생 1~{r}티어·주문 치명타 1~{c}티어'.replace('1~1티어','1티어'),f'Mana regen T1–{r} or spell crit T1–{c}')}]} for v,kr,en,x,y,r,c in (('bal','밸런스 옵션','Balance',2,3,1,2),('ess','에센셜 옵션','Essential',4,5,3,4))],
  {'quality':20,'sockets':2},{'all':[{'has':'cel'},{'has':'l4'},{'full':'p'},{'full':'s'}]})

# ---------- 3. LilBotQ 방어도 2000 방패 (4YOSSAa53UU, 자막 확인) ----------
# 영상: 분열(방어도 1티어) 뒤 소멸의 오브로 옵션 1개만 남김 → 카오스 오브로 방어도 % 1티어(복합 아님, 약 51개) → 좌측 강령술 + 고대 갈비뼈 + 심연의 메아리
# → 복합(방어도 % + 기절 한계치) 1티어. 자기 템이면 빛의 징조 반복(1회 약 8 div), 팔 템이면 나온 티어로 타협 → 상위 찬미 + 완벽한 엑잘, 완벽한 엑잘(접미 아무거나).
P={'bal':{'pT':1,'hT':1},'ess':{'pT':2,'hT':3}}
tags={'flat':{'gi':6,'tmax':1},'pct':{'gi':7,'tmax':'$pT'},'hyb':{'gi':8,'tmax':'$hT'}}
FL=it('p','방어도 (분열)','Flat armour (fractured)',['flat']); PC=it('p','방어도 % 증가','% armour',['pct']); HY=it('p','방어도 % + 기절 한계치','% armour + stun threshold',['hyb'])
I0=[FL,J('s')]; I1=[FL,PC]; I2=I1+[UN('p')]; I3=I1+[HY]; I4=I3+[J('s'),J('s')]; I5=I4+[J('s')]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'flat','fr':True},{'junk':'s'}]},K('방어도 1티어 분열 + 잡옵 1개 (퀄리티 28%)','Fractured T1 flat armour + one junk line (28% quality)'),I0),
 mark([0,0.6],'l2',I0),
 act('l2','main',[0,1],'chaos','Chaos_Orb',K('접두 두 번째 옵션','Second prefix option'),None,K('카오스','Chaos'),[{'if':{'has':'pct'},'to':'l3','res':'ok'},{'to':'l2','res':'fail'}],I1,show=['pct']),
 act('l3','main',[0,2],'desecrate','Ancient_Rib',K('접두 세 번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'l4'}],I2,omens=['Omen_of_Sinistral_Necromancy']),
 act('l4','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'hyb'},'to':'l7','res':'ok'},{'if':{'param':{'hT':1}},'to':'l4x','res':'fail'},{'to':'l7','res':'fail'}],I3,want='hyb',show=['hyb'],omens=['Omen_of_Abyssal_Echoes']),
 annul('l4x',[1,3],[{'to':'l4d','port':'right'}]),
 act('l4d','main',[1,3.6],'desecrate','Ancient_Rib',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'l4','port':'right'}],I2,omens=['Omen_of_Sinistral_Necromancy']),
 act('l7','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 옵션 2개','Two suffixes'),[st('s','랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'l8'}],I4,omens=['Omen_of_Greater_Exaltation'],
     over=[{'param':{'hT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('l8','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 세 번째 옵션','Third suffix'),[st('s','랜덤 옵션 1개 — 결과 그대로','One random line — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I5,
     over=[{'param':{'hT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,6])]
nodes[0]['group']='prep'
graph('lilbotq-armour-shield-v2','Shields_str','Tawhoan Tower Shield',81,
  'LilBotQ 방어도 2000 방패(영상 자막 확인 2026-11-10) — 방어도 1티어 분열 + 잡옵 1개(퀄리티 28%) → 카오스 오브로 방어도 % → 좌측 강령술 + 고대 갈비뼈 → 공개(방어도 % + 기절 한계치, 심연의 메아리) → 접미 옵션 3개 아무거나. 밸런스 = 영상(자기 템: 1티어까지 빛의 징조), 에센셜 = 팔 템 방식(방어도 % 1~2티어, 복합 1~3티어, 공개는 결과 그대로, 접미는 상위 엑잘티드 오브).',
  {'pT':{'kr':'방어도 %','en':'% armour','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'hT':{'kr':'방어도 % + 기절 한계치','en':'% armour + stun threshold','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})}},P,
  {'bal':K('1티어까지 빛의 징조로 다시 (영상)','Light until T1 (as the video)'),'ess':K('나온 티어로 타협 (판매용)','Settle for the tier you get (to sell)')},
  tags,nodes,[{'id':'L1','nodes':['l4','l4x','l4d'],'kr':'훼손 공개','en':'Reveal'}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'flat','tmax':1},{'tag':'pct','tmax':a},{'tag':'hyb','tmax':b},{'side':'s','random':True},{'side':'s','random':True},{'side':'s','random':True}]} for v,kr,en,a,b in (('bal','밸런스 옵션','Balance',1,1),('ess','에센셜 옵션','Essential',2,3))],
  {'quality':28,'sockets':2},{'all':[{'has':'flat'},{'has':'pct'},{'full':'p'},{'full':'s'}]})

# ---------- 4. Diztoh 정신력 로브 (n97yEuKSWyM) ----------
# 2026-11-12 W4 영상 전체 재대조(자막 0:00~20:33 + 화면 캡처, 근거 scratchpad review/W4-vile-robe/timeline.md) + 새 플로우차트 기준(정책 11장 맨 위):
#   영상은 한 번에 끝까지 간 회차 하나(성공 회차). 분기는 그 회차에서 나온 대로 한 줄로.
# 준비(화면): 0:02·2:05 시작 = 정신력 +50 4티어(분열 색) + 에너지 보호막 최대치 +52 + 에너지 보호막 98% 2티어, 접미 없음, 아이템 레벨 81, 퀄리티 20%
#   → 2:23 소멸의 오브(최대치 52 제거) → 3:00~3:17 좌측 찬미 + 상위 엑잘로 최대치를 노리다 그만둠(가시 피해·복합 옵션 → 소멸) → 3:18 소멸의 오브로 98% 제거, 정신력 + 가시 피해.
# 본 제작(화면): 3:19~3:28 상위 카오스 오브 반복(지능·재충전·최대치 6티어·중독 지속시간 거쳐 3:28 최대치 +95 1티어, 2:45 상위 카오스 오브 15개 구입)
#   → 3:35~4:22 좌측 찬미 + 상위 엑잘(복합·생명력·5티어 65%는 소멸의 오브로 지움) → 4:22 101% 1티어 → 4:55 보존된 갈비뼈(접미 훼손) → 6:10 아스트리드의 창의성 장착
#   → 8:56 공개(심연의 메아리로 한 번 다시) 빗나감(에너지 보호막 재충전) → 9:34 우측 결정화 + 완벽한 추구의 에센스 → 9:58 우측 결정화 + 심연의 에센스(징표)
#   → 10:27 보존된 갈비뼈로 징표 훼손(쓰는 장면은 화면에 없음, 결과만) → 10:31 공개: 정신력 점유 효율 8% → 11:30 상위 찬미 + 완벽한 엑잘(접미 2개, 저항 없음)
#   → 12:29 우측 소멸의 징조 + 소멸의 오브(30% 능력치 요구 제거) → 13:20·13:52 절사의 징조 + 상위 카오스 오브 2번(중독 → 능력치 요구 25% → 냉기 저항 35% 3티어)
#   → 14:24 완벽한 엑잘 1개 구입 → 14:36 접미 세 번째(능력치 요구 35% 감소 1티어) → 15:30~16:50 신성한 오브, 17:00 룬·여우 우상, 19:40 치직대는 유동체(마무리, 비용 제외).
P={'bal':{'sT':4,'fT':2,'eT':2,'g':1},'ess':{'sT':4,'fT':4,'eT':4,'g':0}}
# 밸런스 원소 저항 '2~3티어' = 아이템 레벨 81이라 1티어(레벨 82)가 붙지 않아, 붙을 수 있는 위 두 티어를 C17의 1~2티어로 봄(마스터 확정 2026-11-12, 영상 결과 냉기 3티어)
tags={'spirit':{'gi':14,'tmax':'$sT'},'esf':{'gi':6,'tmax':'$fT'},'esp':{'gi':7,'tmax':'$eT'},'res':{'gi':21},'seek':{'gi':43},'mark':{'gi':45},
      'fire':{'gi':1,'tmax':3},'cold':{'gi':2,'tmax':3},'light':{'gi':3,'tmax':3},'anyres':{'anyOf':['fire','cold','light'], 'shown': 'cold','label':K('원소 저항 2~3티어','Elemental resistance T2–3')},'keepR':{'anyOf':['spirit','esf','esp','res']}}
SP=it('p','정신력 (분열)','Spirit (fractured)',['spirit'],'f'); EF=it('p','에너지 보호막 최대치','Flat energy shield',['esf']); EP=it('p','에너지 보호막 % 증가','% energy shield',['esp'])
RE=it('s','스킬의 정신력 점유 효율 (아마나무)','Spirit reservation efficiency (Amanamu)',['res'],'d'); AR=it('s','원소 저항','Elemental resistance',['anyres'])
IP=[SP,J('p'),J('p')]; I0=[SP,J('p')]; I1=[SP,EF]; I2=I1+[EP]; I3=I2+[UN('s')]; I4=I2+[RE]; I5=I4+[J('s'),J('s')]; I6=I4+[AR]; I8=I6+[J('s')]
IA=I2+[it('s','추구의 에센스 옵션 (제작 옵션)','Essence of Seeking line (crafted)',['seek'])]; IB=I2+[it('s','심연 군주의 징표','Mark of the Abyssal Lord',['mark'])]
nodes=[base('p1',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'p'},{'junk':'p'}],'quality':20},K('정신력 분열 특출난 끔찍한 로브 구입','Buy an exceptional Vile Robe with fractured Spirit'),IP),
 {**cleanup('p1',[0,1],[],[{'to':'ms'}],K('정신력 분열 + 옵션 1개만 남기기','Keep the fractured Spirit + one line')),'group':'prep','maxJunk':1,'item':I0},   # 2:23 최대치 52 제거, 3:18 98% 제거(화면)
 mark([0,1.6],'v2',I0),
 act('v2','main',[0,2],'chaos','Greater_Chaos_Orb',K('접두 에너지 보호막 최대치','Flat energy shield prefix'),None,K('카오스','Chaos'),[{'if':{'added':'esf'},'to':'v3','res':'ok'},{'to':'v2','res':'fail'}],I1,show=['esf']),   # 3:19~3:28
 act('v3','main',[0,3],'exalt','Greater_Exalted_Orb',K('접두 에너지 보호막 % 증가','% energy shield prefix'),None,K('엑잘','Exalt'),[{'if':{'added':'esp'},'to':'v5','res':'ok'},{'to':'v3x','res':'fail','label':K('빗나감 — 소멸','Miss: annul')}],I2,show=['esp'],omens=['Omen_of_Sinistral_Exaltation']),   # 3:35~4:22
 cleanup('v3x',[1,3],['spirit','esf'],[{'lost':'esf','to':'v2','label':K('최대치가 지워짐 — 카오스부터','Flat ES gone: back to Chaos')},{'to':'v3','label':K('다시 엑잘','Exalt again')}],K('빗나간 접두 제거, 접미가 비어 있어 접두만 지워짐','Remove the missed prefix; no suffixes yet, so a prefix goes')),   # 4:20
 act('v5','main',[0,4],'desecrate','Preserved_Rib',K('접미 첫 번째 옵션(훼손)','First suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated (unrevealed)')],K('훼손','Desecrate'),[{'to':'v4'}],I3),   # 4:55 보존된 갈비뼈 툴팁, 5:09 미공개
 act('v4','main',[0,5],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':'v6'}],I3,rune=K('아스트리드의 창의성','Astrid’s Creativity'),skipIf={'rune':'Astrid'},skipTo='v6',skipHide=True,skipNote=K('이미 장착돼 있으면 건너뜀','Skipped when already socketed')),   # 6:04 툴팁, 6:10 '제작 옵션 1개 추가' — 영상대로 갈비뼈 뒤(마스터 검수 2026-11-12)
 act('v6','main',[0,6],'reveal',None,K('접미 스킬의 정신력 점유 효율','Spirit reservation efficiency suffix'),None,K('공개','Reveal'),[{'if':{'added':'res'},'to':'v7','res':'ok'},{'to':'v6a','res':'fail','label':K('빗나감 — 빛의 징조 없이 다시','Miss: reroll without Omen of Light')}],I4,want='res',show=['res'],omens=['Omen_of_Abyssal_Echoes']),   # 8:56 빗나감, 10:31 성공
 act('v6a','main',[1,6],'essence','Perfect_Essence_of_Seeking',K('빗나간 훼손 옵션을 추구의 에센스 옵션으로','Swap the missed desecration for the Seeking line'),[st('s','추구의 에센스 옵션 (유일한 접미가 지워짐)','Essence of Seeking line (the only suffix goes)')],K('에센스','Essence'),[{'to':'v6b'}],IA,ess='seek',omens=['Omen_of_Dextral_Crystallisation']),   # 9:34
 act('v6b','main',[1,7],'essence','Essence_of_the_Abyss',K('심연 군주의 징표로 바꿈','Turn it into the Abyssal Lord’s Mark'),[st('s','심연 군주의 징표','Mark of the Abyssal Lord')],K('에센스','Essence'),[{'to':'v6c'}],IB,ess='mark',mark=True,omens=['Omen_of_Dextral_Crystallisation']),   # 9:58
 act('v6c','main',[1,8],'desecrate','Preserved_Rib',K('징표 훼손','Desecrate the Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'v6','label':K('다시 공개','Reveal again')}],I3,fromMark=True),   # 10:27 결과(쓰는 장면은 편집으로 없음)
 act('v7','main',[0,9],'exalt','Perfect_Exalted_Orb',K('접미 옵션 2개','Two suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),
     [{'to':'v8a'}],I5,omens=['Omen_of_Greater_Exaltation'],over=[{'param':{'g':0},'set':{'cur':'Greater_Exalted_Orb','edges':[{'to':'ok'}]}}]),   # 11:30 저항 없음(30%·50%)
 {**annul('v8a',[0,10],[{'if':{'removed':'res'},'to':'v8x','res':'fail'},{'to':'v8','res':'ok'}],omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 하나 제거','Remove one junk suffix')),'skipIf':{'has':'anyres'},'skipTo':'ok','skipHide':True,'skipNote':K('원소 저항이 이미 있으면 건너뜀','Skipped when a resistance is already there')},   # 12:29
 act('v8','main',[0,10.5],'chaos','Greater_Chaos_Orb',K('가장 낮은 옵션을 원소 저항으로','The lowest line into an elemental resistance'),None,K('카오스','Chaos'),
     [{'if':{'has':'anyres'},'to':'v8b','res':'ok'},{'if':{'whittleSafe':'keepR'},'to':'v8','res':'fail','label':K('가장 낮은 옵션이 잡옵이면 반복','Repeat while the lowest line is junk')},{'to':'v8c','res':'fail','label':K('가장 낮은 옵션이 남길 옵션','The lowest line is one to keep')}],I6,show=['anyres'],omens=['Omen_of_Whittling'],
     skipIf={'not':{'whittleSafe':'keepR'}},skipTo='v8c',skipNote=K('가장 낮은 옵션이 남길 옵션이면 건너뜀','Skipped when the lowest line is one to keep'),skipLabel=K('가장 낮은 옵션이 남길 옵션','The lowest line is one to keep')),   # 13:20·13:52 채팅 '절사의 징조 소모'
 act('v8c','main',[1,10.5],'exalt','Perfect_Exalted_Orb',K('빈 접미에 원소 저항','An elemental resistance in the open suffix'),None,K('엑잘','Exalt'),[{'if':{'has':'anyres'},'to':'ok','res':'ok'},{'to':'v8a','res':'fail'}],I6,show=['anyres']),   # 영상에 없음(내부 결정)
 {**cleanup('v8x',[1,10],[],[{'to':'v5','label':K('훼손부터 다시','Desecrate again')}],K('남은 접미 잡옵 제거','Remove the remaining junk suffixes'),side='s'),'omens':['Omen_of_Dextral_Annulment']},   # 영상에 없음(최악의 경우)
 act('v8b','main',[0,11],'exalt','Perfect_Exalted_Orb',K('접미 세 번째 옵션','Third suffix'),[st('s','랜덤 옵션','Random modifier')],K('엑잘','Exalt'),[{'to':'ok'}],I8),   # 14:24 구입, 14:36
 done([0,12])]
graph('diztoh-vile-robe-v2','Body_Armours_int','Vile Robe',81,
  'Diztoh 정신력 로브(2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 정신력 분열 베이스를 소멸의 오브로 분열 + 옵션 1개 → 상위 카오스 오브로 에너지 보호막 최대치 → 좌측 찬미의 징조 + 상위 엑잘티드 오브로 단일 에너지 보호막 %, 빗나가면 소멸의 오브 → 아스트리드의 창의성 → 보존된 갈비뼈 → 공개(스킬의 정신력 점유 효율), 빗나가면 우측 결정화 + 완벽한 추구의 에센스 → 우측 결정화 + 심연의 에센스(징표) → 보존된 갈비뼈 → 상위 찬미 + 완벽한 엑잘(접미 2개) → 우측 소멸의 징조 + 소멸의 오브 → 절사의 징조 + 상위 카오스 오브로 원소 저항 → 완벽한 엑잘(접미 세 번째). 신성한 오브·룬·여우 우상·유동체는 비용에서 뺌.',
  {'sT':{'kr':'정신력 (분열)','en':'Spirit (fractured)','values':TV({'4':('1~4티어','T1–4')})},'fT':{'kr':'에너지 보호막 최대치','en':'Flat energy shield','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})},'eT':{'kr':'에너지 보호막 %','en':'% energy shield','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})},'g':{'kr':'원소 저항','en':'Resistance','values':TV({'1':('절사의 징조로 맞춤','Whittling'),'0':('결과 그대로','As it comes')})}},P,
  {'bal':K('에너지 보호막 옵션 2개 1~2티어 + 원소 저항(우측 소멸·절사의 징조, 영상)','Two T1–2 energy shield lines + a resistance (Dextral Annulment and Whittling, as the video)'),'ess':K('에너지 보호막 1~4티어, 상위 엑잘, 저항은 결과 그대로','T1–4 energy shield, Greater Exalts, resistances as they come')},
  tags,nodes,[{'id':'L0','nodes':['v3','v3x'],'kr':'접두 에너지 보호막 % 옵션','en':'% energy shield prefix'},{'id':'L1','nodes':['v6','v6a','v6b','v6c'],'kr':'정신력 점유 효율 공개','en':'Reservation efficiency reveal'},
   {'id':'L2','nodes':['v8a','v8','v8c'],'kr':'접미 원소 저항','en':'Resistance suffix',
    # 다중 루프를 상자 하나로(정책 11장, 2026-11-12 17:06) — 영상 12:29 우측 소멸 → 13:20·13:52 절사 2번, 3번 단계는 영상에 없음(내부 결정)
    'fold':True,'goal':K('접미 원소 저항 2~3티어','T2–3 elemental resistance suffix'),
    'steps':[{**K('우측 소멸의 징조 + 소멸의 오브로 접미 하나 제거','Dextral Annulment + Orb of Annulment removes one suffix'),'node':'v8a'},
             {**K('절사의 징조 + 상위 카오스 오브로 가장 낮은 잡옵을 원소 저항으로, 저항이 나올 때까지','Whittling + Greater Chaos turns the lowest junk line into a resistance, until one comes'),'node':'v8'},
             {**K('가장 낮은 옵션이 남길 옵션이면 완벽한 엑잘티드 오브로 빈 접미에 원소 저항, 빗나가면 처음부터','When a kept line is lowest: Perfect Exalt the open suffix for a resistance, a miss starts over'),'node':'v8c'}],
    'worst':{**K('스킬의 정신력 점유 효율이 지워지면 접미 잡옵을 지우고 훼손부터','Reservation efficiency gone: clear the junk suffixes and desecrate again'),'to':'v8x'},
    'item':I6}],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'spirit','tmax':4,'fr':True},{'tag':'esf','tmax':b},{'tag':'esp','tmax':c},{'tag':'res','tmax':1,'des':True}]+([{'tag':'anyres'},{'side':'s','random':True}] if v=='bal' else [{'side':'s','random':True},{'side':'s','random':True}])} for v,kr,en,b,c in (('bal','밸런스 옵션','Balance',2,2),('ess','에센셜 옵션','Essential',4,4))],
  {'quality':20,'sockets':3},{'all':[{'has':'spirit'},{'has':'esf'},{'has':'esp'},{'has':'res'},{'full':'s'},{'any':[{'has':'anyres'},{'param':{'g':0}}]}]})

# ---------- 5. Diztoh +5 부적 (p6HIFmJ9mRU) ----------
# 원본 레시피(영상 기록): 근접 +5 + 화염 피해 추가 매직 구입 → 상위 추구의 에센스(치명타) → 우측 강령술 + 군왕의 징조 + 보존된 턱뼈 → 공개(공격 속도, 아마나무 3개 전부)
# → 상위 찬미 + 완벽한 엑잘(접두 옵션 2개, 결과 그대로) → 세를의 승리(접미 +1) → 완벽한 엑잘(영상: 정확도 + 빛 반경으로 타협). 좌측·우측 소멸의 징조 재도전은 안 넣음.
P={'bal':{'fT':3},'ess':{'fT':5}}
tags={'melee':{'gi':10,'tmax':1},'fire':{'gi':4,'tmax':'$fT'},'crit':{'gi':51},'as':{'gi':32},'cdmg':{'gi':19,'tmax':2},
      'phys':{'gi':3,'tmax':3},'cold':{'gi':5,'tmax':3},'light':{'gi':7,'tmax':3},'ppct':{'gi':8,'tmax':4},'hyb':{'gi':9,'tmax':3},'eatk':{'gi':23,'tmax':2},
      'pre':{'anyOf':['phys','cold','light','ppct','hyb','eatk'],'label':K('물리·원소 피해 접두','Physical or elemental damage prefix')}}
ME=it('s','모든 근접 스킬 레벨 +5','+5 melee skills',['melee']); FI=it('p','화염 피해 추가','Flat fire damage',['fire']); CR=it('s','치명타 확률 (제작 옵션)','Critical hit chance (crafted)',['crit'])
AS=it('s','공격 속도 + 반려수 공격 속도 (아마나무)','Attack speed + companion attack speed (Amanamu)',['as'])
I0=[ME,FI]; I1=I0+[CR]; I2=I1+[UN('s')]; I3=I1+[AS]; I4=I3+[it('p','물리·원소 피해 접두 (옵션 2개)','Physical or elemental damage (two lines)',['pre'])]; I5=I4+[it('s','랜덤 옵션 1개 (치명타 피해면 좋음)','One random line (crit damage is good)',None,'j')]
EXO=[{'param':{'fT':5},'set':{'cur':'Greater_Exalted_Orb'}}]
nodes=[base('t2',{'rar':'magic','mods':['melee','fire']},K('근접 +5 + 화염 피해 추가 매직 부적 구입','Buy a magic talisman with +5 melee + flat fire'),I0),
 act('t2','prep',[0,1],'essence','Greater_Essence_of_Seeking',K('레어로 업그레이드 + 접미 치명타 확률','Upgrade to rare + crit chance suffix'),[st('s','치명타 확률 (제작 옵션)','Critical hit chance (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='crit'),
 mark([0,1.5],'t3',I1),
 act('t3','main',[0,2],'desecrate','Preserved_Jawbone',K('접미 세 번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','아마나무 훼손 옵션(미공개)','Amanamu desecration (unrevealed)')],K('훼손','Desecrate'),[{'to':'t4'}],I2,omens=['Omen_of_Dextral_Necromancy','Omen_of_the_Liege']),
 act('t4','main',[0,3],'reveal',None,K('훼손 옵션 확인 (아마나무 3개 전부 나옴)','Reveal (all three Amanamu lines show)'),[st('s','공격 속도 + 반려수 공격 속도','Attack speed + companion attack speed')],K('공개','Reveal'),[{'to':'t5'}],I3,want='as'),
 act('t5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','물리·원소 피해 접두 (안 나와도 그대로)','Physical or elemental damage (keep whatever comes)')],K('엑잘','Exalt'),[{'to':'t8'}],I4,omens=['Omen_of_Greater_Exaltation'],over=EXO),
 act('t8','main',[0,5],'rune',None,K('세를의 승리 장착 (접미 +1)','Socket Serle’s Triumph (one more suffix)'),[st('s','접미 자리 +1','One more suffix slot')],K('룬','Rune'),[{'to':'t9'}],I4,slots={'s':1},rune=K('세를의 승리',"Serle's Triumph")),
 act('t9','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접미 네 번째 옵션','Fourth suffix'),[st('s','치명타 피해 보너스 1~2티어 (안 나와도 그대로 — 영상: 정확도 + 빛 반경)','Crit damage bonus T1–2 (keep whatever comes — accuracy + light radius in the video)')],K('엑잘','Exalt'),[{'to':'ok'}],I5,over=EXO),
 done([0,7])]
graph('diztoh-talisman-v2','Talismans','Maji Talisman',81,
  'Diztoh +5 부적(원본 레시피 기록) — 근접 +5 + 화염 피해 추가 매직 구입 → 상위 추구의 에센스(치명타) → 우측 강령술 + 군왕의 징조 + 보존된 턱뼈 → 공개(아마나무 접미 3개 전부 → 공격 속도 확정) → 상위 찬미 + 완벽한 엑잘(접두 옵션 2개, 결과 그대로) → 세를의 승리 → 완벽한 엑잘(접미 4번째, 결과 그대로). 소멸의 징조 재도전은 뺌(영상도 타협). 에센셜 = 화염 피해 1~5티어 베이스, 엑잘은 상위 엑잘티드 오브.',
  {'fT':{'kr':'화염 피해 추가','en':'Flat fire damage','values':TV({'3':('1~3티어','T1–3'),'5':('1~5티어','T1–5')})}},P,
  {'bal':K('영상 그대로 (완벽한 엑잘티드 오브)','As the video (Perfect Exalts)'),'ess':K('더 싼 베이스, 상위 엑잘티드 오브','Cheaper base, Greater Exalts')},
  tags,nodes,[],
  [{'id':v,'kr':kr,'en':en,'lines':[{'tag':'fire','tmax':a},{'side':'p','label':K('물리·원소 피해 접두','Physical or elemental damage')},{'side':'p','label':K('물리·원소 피해 접두','Physical or elemental damage')},{'tag':'melee','tmax':1},{'tag':'crit','tmax':1},{'tag':'as','tmax':1},{'side':'s','random':True}]} for v,kr,en,a in (('bal','밸런스 옵션','Balance',3),('ess','에센셜 옵션','Essential',5))],
  {'quality':20,'sockets':0},{'all':[{'has':'as'},{'full':'p'},{'full':'s'}]})
print('wrote 5 graphs (batch 6)')

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_belton_plus8_wand.py'): _sp.run([_sy.executable, f'{H}/gen_belton_plus8_wand.py'], check=True)   # 2026-11-13 G7: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_diztoh_es_helmet.py'): _sp.run([_sy.executable, f'{H}/gen_diztoh_es_helmet.py'], check=True)   # 2026-11-13 G11: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_lilbotq_armour_shield.py'): _sp.run([_sy.executable, f'{H}/gen_lilbotq_armour_shield.py'], check=True)   # 2026-11-13 G9: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_diztoh_talisman.py'): _sp.run([_sy.executable, f'{H}/gen_diztoh_talisman.py'], check=True)   # 2026-11-13 G11: 새 기준 전용 생성기가 덮어씀
