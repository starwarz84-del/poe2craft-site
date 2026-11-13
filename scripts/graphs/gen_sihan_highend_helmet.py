# P4 2026-11-13: 시한 하이엔드 투구(CTrIbhQVU8U, 27:22) 플로우차트 전용 생성기 — gen_batch8.py 3번 구간을 옮김(gen_batch8.py 끝에서 자동 호출)
# 근거: scratchpad review/W8-sihan-helmet/timeline.md, frames/ (영상 0:00~27:22 화면 대조, W8 2026-11-12)
# 실행: cd scripts/graphs && python3 gen_sihan_highend_helmet.py [출력 폴더]  → sihan-highend-helmet-v2.json
import os, sys
_H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{_H}/gen_batch8.py').read(); exec(_src[:_src.index('\n# ---------- 1. 라그나')])
H=sys.argv[1] if len(sys.argv)>1 else _H   # graph8가 H/<id>.json에 씀
# ---------- 3. 시한 하이엔드 투구 (CTrIbhQVU8U) ----------
# 2026-11-12 W8 영상 전체 재대조(자막 0:00~27:22 + 화면 캡처, 근거 scratchpad review/W8-sihan-helmet/timeline.md) + 새 플로우차트 기준(정책 11장 맨 위):
#   영상 성공 회차 흐름 한 줄. 베이스 준비(화면): 10:40 특출난 제국의 대헬름 흰 베이스 3개 → 11:20 완벽한 진화(창고 III 118 → 115) → 11:40 완벽한 확장(창고 III 51 → 21, 인벤 30개)
#   → 12:15 완벽한 제왕(창고 III 19 → 16) → 12:32 보존된 갈비뼈(18/20)로 네 번째 옵션 미공개 훼손 → 12:40~13:10 신성한 오브로 수치 최대(선택, 비용 미포함)
#   → 13:30~13:50 분열 1/3(투구 셋 중 셋째 '키메라의 돔'에서 생명력 최대치 +174 분열) → 14:02 소멸로 분열 + 옵션 1개.
#   접미(성공 회차 16:40~17:50): 카오스 오브(창고 343 → 322, 일반)로 치명타 확률 26% 2티어(17:01) → 완벽한 엑잘 + 우측 찬미 + 상위 찬미(17:34 번개 저항 3티어·모든 소환수 +2)
#   → 소멸의 오브(17:38 소환수 지워짐) → 상위 찬미 끄고 완벽한 엑잘 + 우측 찬미(17:48 방어도 원소 적용 38% 1티어) → 18:35 공허 유동체(보라색 아이콘·결과로 판단)로 번개 저항 → 카오스 저항 21%.
#   접두(18:52~25:30): 완벽한 엑잘(방어도 80% 2티어 빗나감) → 좌측 결정화 + 심연의 에센스(19:08 징표) → 완벽한 엑잘(19:18 방어도 +213 1티어) → 고대 갈비뼈(20:20 징표 자리 훼손)
#   → 공개 + 심연의 메아리(22:06 방어도 84% 2티어) → 빛의 징조 + 소멸의 오브(23:56) → 고대 갈비뼈(24:02) → 공개 반복 → 25:26 방어도 92% 1티어.
#   영상 첫 회차(14:20~16:40: 카오스 방어도 원소 적용 1티어 → 엑잘 화염·냉기 → 상위 카오스 → 치명타가 지워져 처음부터)는 꿀팁 후보.
#   등급(난이도 4, 정책 10장): 하이엔드 = 영상(방어도 원소 적용·방어도 최대치·방어도 % 1티어, 저항 1~3티어), 밸런스 = 그 반복을 1~2티어, 마지막 접미(저항)는 랜덤 옵션이라 유동체 건너뜀.
P={'high':{'aT':1,'eT':1,'g':1},'bal':{'aT':2,'eT':2,'g':0}}
L_=lambda kr,en: {'label':K(kr,en)}
F_={'res':'fail'}
tags={'life':{'gi':6,'tmax':1},'crit':{'gi':16,'tmax':2},
      'ele':{'gi':20,'tmax':'$eT'},'ele1':{'gi':20,'tmax':1},'ele2':{'gi':20,'tmax':2},
      'fire':{'gi':2,'tmax':3},'cold':{'gi':3,'tmax':3},'lres':{'gi':4,'tmax':3},'chaos3':{'gi':5,'tmax':3},'chaos2':{'gi':5,'tmax':2},
      'res':{'anyOf':['fire','cold','lres','chaos2'],'label':K('원소·카오스 저항 1~3티어','T1–3 elemental or chaos resistance')},
      'flat':{'gi':8,'tmax':'$aT'},'flat1':{'gi':8,'tmax':1},'flat2':{'gi':8,'tmax':2},
      'pct':{'gi':9,'tmax':'$aT'},'pct1':{'gi':9,'tmax':1},'pct2':{'gi':9,'tmax':2},'mark':{'gi':47},
      # 새 정책 A(사용자 확정 11-13 14:17, 정책 11장 '아무거나' 예외): 영상 1:30~2:00 접두 분열 자리 = 생명력·방어도 최대치·방어도 % 1티어 중 아무거나.
      # 성공 조건(진화·분열)은 셋 중 하나, 상자·칸·카드는 성공 회차(생명력 분열, 13:12). 분열된 옵션이 생명력이 아니면 남은 두 접두를 엑잘·훼손 공개로 채움(판정만, 화면은 성공 회차 순서).
      'pre1':{'anyOf':['life','flat1','pct1'],'shown':'life','label':K('생명력 최대치·방어도 최대치·방어도 % 증가 1티어','T1 maximum life, flat armour or % increased armour')},
      'pq1':{'anyOf':['life','flat'],'shown':'flat','label':K('남은 생명력 최대치·방어도 최대치','The remaining maximum life or flat armour')},
      'pq':{'anyOf':['life','flat','pct'],'shown':'pct','label':K('남은 생명력 최대치·방어도 최대치·방어도 % 증가','The remaining maximum life, flat armour or % increased armour')}}
conds={'sOK':{'all':[{'has':'crit'},{'has':'ele'},{'any':[{'param':{'g':0}},{'has':'res'}]},{'full':'s'}]}}
LI0=it('p','생명력 최대치 1티어','T1 maximum life',['life'])
LI=it('p','생명력 최대치 1티어','T1 maximum life',['life'],'f')   # 분열 표시는 m='f'(금색)
CR=it('s','치명타 확률 1~2티어','T1–2 critical hit chance',['crit'])
EL=it('s','방어도 원소 피해 적용 1티어','T1 armour also applies to elemental damage',['ele'])
RS=it('s','원소 저항 1~3티어 (유동체로 카오스 저항)','T1–3 elemental resistance (Flux turns it into chaos)',['res'])
CH=it('s','카오스 저항','Chaos resistance',['chaos2'])   # 공허 유동체: 원소 1~3티어 → 카오스 1~2티어(POE2DB Mod Equivalencies)
AF=it('p','방어도 최대치 1티어','T1 flat armour',['flat'])
MK=it('p','심연 군주의 징표','Mark of the Abyssal Lord',['mark'])
AP=it('p','방어도 % 증가 1티어 (훼손)','T1 % increased armour (desecrated)',['pct'],'d')
_JK=lambda s: {'s':s,'kr':'잡옵','en':'Junk','m':'j'}
nodes=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'p1','start':{'rar':'normal','mods':[]},'label':K('특출난 제국의 대헬름 구입 (노멀, 아이템 레벨 82, 증강 홈 2)','Buy an exceptional Imperial Greathelm (normal, item level 82, 2 augment sockets)'),'item':[]},   # 9:30~10:40 저항 1티어 = 아이템 레벨 82, 거래소 '증강 가능한 홈 2·타락 아니요'
 act('p1','prep',[0,1],'transmute','Perfect_Orb_of_Transmutation',K('접두 생명력 최대치 1티어','T1 maximum life prefix'),None,K('진화','Transmute'),
     [{'if':{'has':'pre1'},'to':'p2','res':'ok'},{'to':'p1x',**F_,**L_('다른 옵션 — 소멸','Another line: annul')}],[LI0],show=['life']),   # 11:20~11:32 화면: 생명력 +159 1티어, 11:35 '접두 아니면 지워 주시고'
 {'id':'p1x','kind':'act','group':'prep','pos':[1,1],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('빗나간 옵션 지우고 다시 진화','Clear the miss, transmute again'),'edges':[{'to':'p1',**L_('다시 진화','Transmute again')}]},
 act('p2','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('매직 두 번째 옵션','Second magic line'),[st(None,'랜덤 옵션 1개','One random line')],K('확장','Augment'),[{'to':'p3'}],[LI0,_JK('s')]),   # 11:40 완벽한 확장의 오브 30개
 act('p3','prep',[0,3],'regal','Perfect_Regal_Orb',K('레어','Rare'),[st(None,'랜덤 옵션 1개','One random line')],K('제왕','Regal'),[{'to':'p4'}],[LI0,_JK('p'),_JK('s')]),   # 12:15~12:30
 act('p4','prep',[0,4],'desecrate','Preserved_Rib',K('네 번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),[st(None,'훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],K('훼손','Desecrate'),[{'to':'p5'}],[LI0,_JK('p'),_JK('s'),UN('s')]),   # 12:32 보존된 갈비뼈 18/20, 12:44 미공개 훼손
 {'id':'hd','kind':'side','group':'prep','pos':[1,4.5],'attach':['p4','p5'],'cur':'Divine_Orb','goal':K('생명력 수치 최대, 선택·비용 미포함','Max the life roll, optional, not costed'),'label':K('신성','Divine')},   # 12:40~13:10 생명력 153 → 174
 act('p5','prep',[0,5],'fracture','Fracturing_Orb',K('분열 (셋 중 하나)','Fracture (one of three)'),[st(None,'생명력 최대치가 분열되면 성공','Success when maximum life fractures')],K('분열','Fracture'),
     [{'if':{'fractured':'pre1'},'to':'p6','res':'ok',**L_('생명력 분열','Life fractured')},{'to':'xj','res':'fail','dash':True,**L_('다른 옵션 분열','Another line fractured')}],[LI,_JK('p'),_JK('s'),UN('s')]),   # 13:30~13:50 셋째 투구 성공
 {'id':'xj','kind':'exit','group':'prep','pos':[1,5],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),'note':K('생명력·방어도 최대치·방어도 % 증가가 아닌 옵션이 분열되면 이 투구는 다른 용도로 두고 새 베이스로 처음부터(어려움 이상, 정책 10장 ⑧)','Another line fractured: set this one aside and start on a new base')},   # 14:00 실패한 투구 2개 버림
 {'id':'p6','kind':'cleanup','group':'prep','pos':[0,6],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':[LI,_JK('p')]},   # 14:05 화면: 생명력 174 분열 + 방어도 40%·생명력 43
 mark([0,7],'s1',[LI,_JK('p')]),
 act('s1','main',[0,8],'chaos','Chaos_Orb',K('접미 치명타 확률 1~2티어','T1–2 critical hit chance suffix'),None,K('카오스','Chaos'),
     [{'if':{'has':'crit'},'to':'k1','res':'ok'},{'to':'s1','res':'fail'}],[LI,CR],show=['crit'],skipIf={'has':'crit'},skipTo='k1',skipHide=True),   # 17:01 성공 회차 치명타 26%(2티어), 창고 카오스 343 → 322(14:22·14:46)
 {'id':'kz','kind':'cleanup','group':'main','pos':[1,8],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep the fracture + one line'),'edges':[{'to':'s1',**L_('다시 카오스','Chaos again')}]},   # 16:30~16:40 '날아갔죠 — 다시 소멸해서 한 줄 남기고 다시 돌려'
 act('k1','main',[0,9],'exalt','Perfect_Exalted_Orb',K('접미 두 번째·세 번째 옵션','Second and third suffixes'),None,K('엑잘','Exalt'),
     [{'if':{'ref':'sOK'},'to':'fx','res':'ok',**L_('목표 접미 성공','Target suffixes hit')},{'to':'k2',**F_,**L_('빗나간 접미 — 소멸','Missed suffix: annul')}],[LI,CR,EL,RS],show=['ele','res'],omens=['Omen_of_Dextral_Exaltation','Omen_of_Greater_Exaltation'],over=[{'param':{'g':0},'set':{'item':[LI,CR,EL,R1('s')],'show':['ele']}}]),   # 17:34 완벽한 엑잘 + 우측 찬미 + 상위 찬미(인벤 20 → 19, 징조 3 → 2, 10 → 9 — 14:48·15:03)
 act('k2','main',[1,9],'annul','Orb_of_Annulment',K('빗나간 접미 지우기 (한 개)','Remove a missed suffix (one)'),None,K('소멸','Annul'),
     [{'if':{'removed':'crit'},'to':'kz',**F_,**L_('치명타 확률이 지워짐 — 카오스부터','Crit chance gone: back to Chaos')},{'to':'k3',**L_('빈 접미에 엑잘','Exalt into the empty suffix')}],[LI,CR,EL]),   # 17:38 소멸 → 모든 소환수 +2 지워짐
 act('k3','main',[1,10],'exalt','Perfect_Exalted_Orb',K('빈 접미 하나','The empty suffix'),None,K('엑잘','Exalt'),
     [{'if':{'ref':'sOK'},'to':'fx','res':'ok'},{'to':'k2',**F_,**L_('또 빗나감 — 소멸','Missed again: annul')}],[LI,CR,EL,RS],show=['ele','res'],omens=['Omen_of_Dextral_Exaltation'],over=[{'param':{'g':0},'set':{'item':[LI,CR,EL,R1('s')],'show':['ele']}}]),   # 17:44 상위 찬미 끔(7/10), 17:48 방어도 원소 적용 38% 1티어(인벤 엑잘 17 → 16, 우측 찬미 10 → 9)
 act('fx','main',[0,10],'flux','Void_Flux',K('원소 저항 → 카오스 저항','Elemental resistance → chaos resistance'),None,K('유동체','Flux'),[{'to':'q1'}],[LI,CR,EL,CH],
     skipIf={'param':{'g':0}},skipTo='q1',skipHide=True,skipNote=K('밸런스는 세 번째 접미가 랜덤 옵션이라 건너뜀','Balance skips it: the third suffix is random')),   # 18:20~18:38 번개 저항 35%(3티어) → 카오스 저항 21%
 act('q1','main',[0,11],'exalt','Perfect_Exalted_Orb',K('접두 방어도 최대치','Flat armour prefix'),None,K('엑잘','Exalt'),
     [{'if':{'added':'pq1'},'to':'q4','res':'ok',**L_('방어도 최대치 성공','Flat armour hit')},{'to':'q2',**F_,**L_('1번째 빗나감 — 심연의 에센스','1st miss: Essence of the Abyss')}],[LI,AF,CR,EL,CH],show=['flat']),   # 18:52 완벽한 엑잘(16/20) → 18:58 방어도 80% 2티어 빗나감
 act('q2','main',[1,11],'essence','Essence_of_the_Abyss',K('빗나간 접두를 징표로','The missed prefix becomes the mark'),[st('p','심연 군주의 징표','Mark of the Abyssal Lord')],K('에센스','Essence'),[{'to':'q3',**L_('다시 엑잘','Exalt again')}],[LI,MK,CR,EL,CH],ess='mark',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),   # 19:02 좌측 결정화 툴팁, 19:08 징표
 act('q3','main',[1,12],'exalt','Perfect_Exalted_Orb',K('접두 방어도 최대치 다시','Flat armour prefix again'),None,K('엑잘','Exalt'),
     [{'if':{'added':'pq1'},'to':'q4','res':'ok'},{'to':'q3x',**F_,**L_('2번째 빗나감 — 징표 훼손','2nd miss: desecrate the mark')}],[LI,AF,MK,CR,EL,CH],show=['flat']),   # 19:14 완벽한 엑잘(15/20) → 19:18 방어도 +213 1티어
 act('q3x','main',[2,12],'desecrate','Preserved_Rib',K('징표를 훼손 옵션으로','The mark becomes a desecrated line'),[st('p','훼손 옵션 (미공개)','Desecrated (unrevealed)')],K('훼손','Desecrate'),[{'to':'q3y'}],[LI,UN('p'),CR,EL,CH],fromMark=True),   # 19:30·21:20 설명만(성공 회차에는 없음)
 {'id':'q3y','kind':'act','group':'main','pos':[2,13],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('훼손 옵션 지우고 남은 빗나간 접두를 다시 징표로','Clear the desecration, mark the missed prefix again'),'target':K('훼손 옵션 제거','Remove the desecrated modifier'),'edges':[{'to':'q2',**L_('다시 심연의 에센스','Essence of the Abyss again')}]},   # 19:40~20:00 설명
 act('q4','main',[0,12],'desecrate','Ancient_Rib',K('접두 세 번째 옵션(훼손) — 징표 자리','Third prefix (desecrated) — on the mark'),[st('p','훼손 옵션 (미공개, 한 티어 높게)','Desecrated (unrevealed, one tier higher)')],K('훼손','Desecrate'),[{'to':'q5'}],[LI,AF,UN('p'),CR,EL,CH],
     fromMark=True,skipIf={'not':{'has':'mark'}},skipTo='q6',skipHide=True,skipNote=K('징표가 없으면 다음 고대 갈비뼈로 빈자리에','No mark: the next Ancient Rib goes to the empty slot')),   # 20:18 고대 갈비뼈(12/20), 20:26 징표 자리 훼손
 act('q5','main',[0,13],'reveal',None,K('접두 방어도 % 증가','% increased armour prefix'),None,K('공개','Reveal'),
     [{'if':{'added':'pq'},'to':'ok','res':'ok'},{'to':'q5x',**F_,**L_('빗나감 — 빛의 징조','Miss: Omen of Light')}],[LI,AF,AP,CR,EL,CH],want='pq',show=['pct'],omens=['Omen_of_Abyssal_Echoes']),   # 22:04 메아리 소모, 22:06 방어도 84% 2티어 · 25:18 메아리 소모, 25:26 방어도 92% 1티어
 {'id':'q5x','kind':'act','group':'main','pos':[1,13],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('훼손 옵션 제거','Remove the desecrated modifier'),'edges':[{'to':'q6',**L_('다시 훼손','Desecrate again')}]},   # 23:56 소멸의 오브(15/20) + 빛의 징조
 act('q6','main',[1,12.4],'desecrate','Ancient_Rib',K('접두 세 번째 옵션(훼손) 다시','Third prefix (desecrated) again'),[st('p','훼손 옵션 (미공개)','Desecrated (unrevealed)')],K('훼손','Desecrate'),[{'to':'q5',**L_('다시 공개','Reveal again')}],[LI,AF,UN('p'),CR,EL,CH]),   # 24:02 고대 갈비뼈(11/20)
 done([0,14])]
graph8('sihan-highend-helmet-v2','Helmets_str','Imperial Greathelm',82,
  '시한 하이엔드 투구(2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 특출난 제국의 대헬름 → 완벽한 진화(생명력 1티어 — 새 정책 11-13: 생명력·방어도 최대치·방어도 % 1티어 중 아무거나 성공, 화면은 성공 회차 생명력)·확장·제왕 → 보존된 갈비뼈 → 분열(1/3, 빗나가면 새 베이스) → 소멸로 분열 + 옵션 1개 → 카오스 오브(치명타 확률 1~2티어) → 완벽한 엑잘 + 우측 찬미 + 상위 찬미(접미 둘, 빗나가면 소멸 → 완벽한 엑잘 + 우측 찬미) → 공허 유동체(저항 → 카오스 저항) → 완벽한 엑잘(방어도 최대치, 빗나가면 좌측 결정화 + 심연의 에센스로 징표 → 완벽한 엑잘) → 고대 갈비뼈(징표 자리) → 공개 + 심연의 메아리(방어도 %, 빗나가면 빛의 징조 + 소멸 → 고대 갈비뼈). 신성한 오브는 비용에서 뺌.',
  {'aT':{'kr':'방어도 접두','en':'Armour prefixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'eT':{'kr':'방어도 원소 피해 적용','en':'Armour to elemental','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'g':{'kr':'세 번째 접미','en':'Third suffix','values':TV({'1':('저항 1~3티어 + 유동체','T1–3 resistance + Flux'),'0':('랜덤 옵션','Random line')})}},P,
  {'high':K('영상: 방어도 원소 적용·방어도 두 옵션 1티어, 저항 1~3티어','Video: T1 armour-to-elemental and both armour lines, T1–3 resistance'),'bal':K('반복 구간 1~2티어, 세 번째 접미는 랜덤 옵션','Loops accept T1–2, the third suffix random')},
  tags,nodes,
  [{'id':'L1','nodes':['k1','k2','k3'],'kr':'접미 방어도 원소 적용·저항','en':'Armour-to-elemental and resistance suffixes',
    'fold':True,'goal':K('접미 방어도 원소 피해 적용 1티어 + 원소 저항 1~3티어','T1 armour-to-elemental + T1–3 elemental resistance suffixes'),
    'goalBy':{'high':K('접미 방어도 원소 피해 적용 1티어 + 원소 저항 1~3티어','T1 armour-to-elemental + T1–3 elemental resistance suffixes'),'bal':K('접미 방어도 원소 피해 적용 1~2티어 + 랜덤 옵션','T1–2 armour-to-elemental suffix + a random line')},
    'steps':[{**K('완벽한 엑잘 + 우측 찬미 + 상위 찬미로 접미 두 개','Perfect Exalt + Dextral + Greater Exaltation for two suffixes'),'node':'k1'},
             {**K('빗나간 접미가 있으면 소멸의 오브 한 개','A missed suffix: one Orb of Annulment'),'node':'k2'},
             {**K('빈 접미에 완벽한 엑잘 + 우측 찬미, 또 빗나가면 2번부터','Perfect Exalt + Dextral Exaltation into the empty suffix, another miss: from step 2'),'node':'k3'}],
    'worst':{**K('치명타 확률이 지워지면 분열 + 옵션 1개로 정리하고 카오스 단계부터','Crit chance gone: back to the fracture + one line, then the Chaos step'),'to':'kz'},
    'item':[LI,CR,EL,RS]},
   {'id':'L2','nodes':['q1','q2','q3','q3x','q3y'],'kr':'접두 방어도 최대치','en':'Flat armour prefix',
    'fold':True,'goal':K('접두 방어도 최대치 1티어','T1 flat armour prefix'),
    'goalBy':{'high':K('접두 방어도 최대치 1티어','T1 flat armour prefix'),'bal':K('접두 방어도 최대치 1~2티어','T1–2 flat armour prefix')},
    'steps':[{**K('완벽한 엑잘로 접두 방어도 최대치','Perfect Exalt for flat armour'),'node':'q1'},
             {**K('1번째 빗나감 — 좌측 결정화 + 심연의 에센스로 빗나간 접두를 징표로','1st miss: Sinistral Crystallisation + Essence of the Abyss turn the miss into the mark'),'node':'q2'},
             {**K('완벽한 엑잘 다시','Perfect Exalt again'),'node':'q3'},
             {**K('2번째 빗나감 — 보존된 갈비뼈로 징표 훼손','2nd miss: Preserved Rib on the mark'),'node':'q3x'},
             {**K('빛의 징조 + 소멸의 오브로 훼손 옵션 제거 → 2번부터','Omen of Light + Annulment clear it, then from step 2'),'node':'q3y'}],
    'item':[LI,AF,MK,CR,EL,CH]},
   {'id':'L3','nodes':['q6','q5','q5x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'life','fr':True},{'tag':'flat1' if v=='high' else 'flat2'},{'tag':'pct1' if v=='high' else 'pct2','des':True},{'tag':'crit'},{'tag':'ele1' if v=='high' else 'ele2'},{'tag':'chaos2'} if v=='high' else {'side':'s','random':True}]),
  {'quality':0,'sockets':2},{'all':[{'has':'life'},{'has':'crit'},{'has':'ele'},{'has':'flat'},{'has':'pct'},{'any':[{'param':{'g':0}},{'has':'chaos2'}]},{'full':'p'},{'full':'s'}]},('high','bal'),conds=conds)
print('wrote', f'{H}/sihan-highend-helmet-v2.json')
