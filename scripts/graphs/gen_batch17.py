# Batch 17 (사용자 2026-11-10: 다음 작업) — 전문가(4) → High-end (video) + Balance. Videos rechecked 2026-11-10 (transcripts).
#   breach-ring-video-v2 (SL RiJixgqBnBY), saveq-focus-v2 (SaVeQ R43FVay8_XI)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch16.py').read(); exec(_src[:_src.index('# ---------- 1. SL 부재')])

# ---------- 1. SL 원소 3플랫 재련된 균열 반지 (RiJixgqBnBY) ----------
# 2026-11-12 W9 영상 전체 재대조(자막 0:00~31:50 + 화면 캡처, 근거 scratchpad review/W9-breach-ring/timeline.md) + 새 플로우차트 기준(정책 11장 맨 위, 확정 옵션 11-12 20:56).
#   준비 구역 = 영상 가이드 슬라이드 1~3(1:40~2:55)과 영상이 '원래 이렇게 하라'고 다시 말한 순서(26:30 '분열부터 하고 퀄작, 70%까지만').
#     성공 회차(두 번째 반지 묶음)의 실제 순서는 퀄리티 75% 먼저 → 분열이었지만 영상이 따라 하지 말라고 해서 가이드 순서로 둠(내부 결정, 보고).
#     23:40~25:40 성공 회차 화면: 옵션 1개 상태에서 카오스로 원소 플랫 1티어(25:17) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘(25:05 자막) → 보존된 빗장뼈(25:35 툴팁 미공개 훼손)
#     → 분열 1/3, 4개 중 1개 성공(26:25 태풍 장악 = 화염 플랫 1티어 분열, 아이템 레벨 80) → 소멸로 분열 + 옵션 1개(26:43 화염 + 민첩).
#   본 제작 = 성공 회차(27:00~28:25 화면) + 녹화가 끊긴 뒤 자막(28:30~29:40)과 비용 화면(31:00: 좌측 소멸 59, 완벽한 엑잘 70, 소멸 98, 고대 빗장뼈 17, 메아리 17, 빛 16).
#     카오스 → 모든 원소 저항(27:48) → 우측 찬미 + 완벽한 엑잘 6번째에 희귀도(28:10, 빗나가면 소멸 후 다시 — 슬라이드 5) → 좌측 찬미 + 엑잘티드 오브(28:17 툴팁)로 접두 잡옵
#     → 좌측 결정화 + 재빠른 합금(28:21·28:24) → 완벽한 엑잘 1번 + 빗나가면 좌측 소멸의 징조 + 소멸의 오브 반복(번개 플랫 1티어, 29:00 자막) → 고대 빗장뼈 + 메아리(냉기 플랫 1티어, 빛의 징조로 다시).
#   확정 옵션: 분열 = 화염 플랫, 엑잘 = 번개 플랫, 훼손 = 냉기 플랫(30:05 완성품 툴팁), 접미 = 저항 → 희귀도(27:48 → 28:10). 다른 순서는 꿀팁 후보.
#   빼는 것: 75% 퀄리티 작업(영상이 따라 하지 말라고 함, 가이드 최소 66%), 디바인·축성·타락(선택).
# 등급(난이도 4): 하이엔드 = 영상(모두 1티어), 밸런스 = 반복으로 찾는 원소 플랫·접미를 1~2티어(4:00 '2티어로 타협하시는 것도 좋습니다'). 공개 반복은 두 등급 모두 빛의 징조.
tags={'ff1':{'gi':15,'tmax':1},'lf':{'gi':19,'tmax':'$pT'},'cf':{'gi':17,'tmax':'$pT'},'mq':{'gi':71},'ar':{'gi':7,'tmax':'$sT'},'rs':{'gi':27,'tmax':'$sT'},'as':{'gi':73}}
FF=it('p','공격 시 화염 피해 (25—29)~(37—45) 추가','Adds (25—29) to (37—45) Fire damage to Attacks',['ff1'],'f')
FFn=it('p','공격 시 화염 피해 (25—29)~(37—45) 추가','Adds (25—29) to (37—45) Fire damage to Attacks',['ff1'])
LF=it('p','공격 시 번개 피해 (1—4)~(60—71) 추가','Adds (1—4) to (60—71) Lightning damage to Attacks',['lf'])
CF=it('p','공격 시 냉기 피해 (21—24)~(32—37) 추가','Adds (21—24) to (32—37) Cold damage to Attacks',['cf'],'d')
MQ=it('p','최대 퀄리티 +20% (균열의 에센스)','+20% to Maximum Quality (Essence of the Breach)',['mq'],'c')
AR=it('s','모든 원소 저항 +(15—16)%','+(15—16)% to all Elemental Resistances',['ar'])
RS=it('s','발견하는 아이템 희귀도 (15—18)% 증가','(15—18)% increased Rarity of Items found',['rs'])
AS=it('s','공격 속도 (7—9)% 증가 (재빠른 합금)','(7—9)% increased Attack Speed (Swift Alloy)',['as'],'c')
UNs=it('s','훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')
L_=lambda kr,en: {'label':K(kr,en)}
def PREP(d): d['group']='prep'; return d
P0=[FFn]; P1=[FFn,J('p'),J('p')]; P2=P1+[UNs]
B0=[FF,J('s')]; B1=[FF,MQ]; B2=[FF,AR]; B3=[FF,AR,RS]; B4=[FF,J('p'),AR,RS]; B5=[FF,AR,RS,AS]; B6=[FF,LF,AR,RS,AS]; B7=B6+[UN('p')]; B8=[FF,LF,CF,AR,RS,AS]
nodes=[{'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'pz','start':{'rar':'rare','mods':[{'junk':'p'},{'junk':'s'},{'junk':'p'},{'junk':'s'}]},
        'label':K('제련된 균열 반지 구입 (레어, 아이템 레벨 80)','Buy a Refined Breach Ring (rare, item level 80)'),'item':[J('p'),J('s')]},   # 5:35 9개 구입, 1:00 '레어로만 떨어짐', 26:25 아이템 레벨 80
 dict(PREP(cleanup('pz',[0,1],[],[{'to':'pc'}],K('옵션 1개만 남기기','Keep one line'),maxJunk=1)),item=[J('s')]),   # 25:17 화면: 옵션 1개 상태(지우는 장면은 확인 못 함)
 act('pc','prep',[0,2],'chaos','Chaos_Orb',K('접두 화염 플랫 1티어','T1 fire flat prefix'),None,K('카오스','Chaos'),
     [{'if':{'has':'ff1'},'to':'pe','res':'ok'},{'to':'pc','res':'fail'}],P0,show=['ff1']),   # 2:10 슬라이드 2 '카오스 오브 돌려서 띄우고 분열', 24:55 화면 카오스 1,500개
 act('pe','prep',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 2개','Two prefixes'),[st(None,'랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'to':'pb'}],P1,
     omens=['Omen_of_Sinistral_Exaltation','Omen_of_Greater_Exaltation']),   # 25:05 자막 '좌측 찬미, 상위 찬미 켜고 완액', 31:00 비용 화면 좌측 찬미 5·상위 찬미 4
 act('pb','prep',[0,4],'desecrate','Preserved_Collarbone',K('네 번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),[st(None,'훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],K('훼손','Desecrate'),[{'to':'pf'}],P2),   # 25:35 화면 미공개 훼손, 31:00 보존된 빗장뼈 4개
 act('pf','prep',[0,5],'fracture','Fracturing_Orb',K('분열 (셋 중 하나)','Fracture (one of three)'),[st(None,'화염 플랫이 분열되면 성공','Success when the fire flat fractures')],K('분열','Fracture'),
     [{'if':{'fractured':'ff1'},'to':'p8','res':'ok',**L_('화염 플랫 분열','Fire flat fractured')},{'to':'xj','res':'fail','dash':True,**L_('다른 옵션 분열','Another line fractured')}],[FF]),   # 22:45 첫 반지 실패(물리 분열), 26:25 성공
 {'id':'xj','kind':'exit','group':'prep','pos':[1,5],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),
  'note':K('화염 플랫이 아닌 옵션이 분열되면 이 반지는 따로 두고 새 베이스로 처음부터','Another line fractured: set this ring aside and start on a new base')},   # 23:00 '팔고 새로 만들어야겠네'
 dict(PREP(cleanup('p8',[0,6],[],[{'to':'q1'}],K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),maxJunk=1)),item=B0),   # 26:43 화면 화염 + 민첩
 act('q1','prep',[0,7],'essence','Essence_of_the_Breach',K('잡옵을 지우고 최대 퀄리티','The junk goes for max quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% to Maximum Quality (crafted)')],K('에센스','Essence'),[{'to':'q2'}],B1,ess='mq'),   # 2:30 슬라이드 3, 7:35 화면
 act('q2','prep',[0,8],'quality','Reaver_Catalyst',K('공격 퀄리티 65%','Attack quality 65%'),[st(None,'강탈자 기폭제 52개','52 Reaver Catalysts')],K('퀄리티','Quality'),[{'to':'q3'}],B1,count=52,q=65),   # 7:30 자막·31:00 화면 9개에 465~466개
 act('q3','prep',[0,9],'quality','Vaal_Catalysing_Infuser',K('퀄리티 66% 이상','Quality 66%+'),[st(None,'바알 촉진시키는 주입기 1개, 65%에서 첫 1개는 타락 없음','One Vaal Catalysing Infuser, the first at 65% never corrupts')],K('퀄리티','Quality'),[{'to':'ms'}],B1,count=1,q=66),   # 2:30 슬라이드 3 '최소 66%', 7:50 화면 66%
 mark([0,10.6],'s1',B1),
 act('s1','main',[0,11.6],'chaos','Chaos_Orb',K('최대 퀄리티를 지우고 접미 모든 원소 저항','Max quality out, all elemental resistances suffix'),None,K('카오스','Chaos'),
     [{'if':{'has':'ar'},'to':'s2','res':'ok'},{'to':'s1','res':'fail'}],B2,show=['ar']),   # 3:16 슬라이드 4(저항), 27:48 화면
 act('s2','main',[0,12.6],'exalt','Perfect_Exalted_Orb',K('접미 희귀도','Rarity suffix'),None,K('엑잘','Exalt'),
     [{'if':{'all':[{'has':'ar'},{'has':'rs'}]},'to':'p0','res':'ok'},{'to':'s2x','res':'fail'}],B3,show=['rs'],omens=['Omen_of_Dextral_Exaltation']),   # 3:23 슬라이드 5, 28:10 6번째 성공
 annul('s2x',[1,12.6],[{'if':{'has':'ar'},'to':'s2','res':'ok',**L_('저항이 남음','Resistances stay')},{'to':'s1','res':'fail',**L_('저항이 지워짐 — 카오스부터','Resistances gone: back to Chaos')}],
     omens=(),target=K('접미 옵션 하나 지우기','Remove one suffix')),   # 슬라이드 5 '실패 시 소멸 바르고 뜰 때까지 4~5 반복', 27:20 자막 '지우고 다시 카오스'
 act('p0','main',[0,13.6],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'p0b'}],B4,omens=['Omen_of_Sinistral_Exaltation']),   # 28:17 엑잘티드 오브 툴팁, 28:19 마나 최대치(접두)
 act('p0b','main',[0,14.6],'essence','Swift_Alloy',K('접두 잡옵을 지우고 공격 속도','The junk prefix goes, attack speed comes'),[st('s','공격 속도 (7—9)% 증가 (제작 옵션)','(7—9)% increased Attack Speed (crafted)')],K('합금','Alloy'),[{'to':'p1'}],B5,ess='as',omens=['Omen_of_Sinistral_Crystallisation']),   # 28:21 좌측 결정화 툴팁, 28:24 공격 속도
 act('p1','main',[0,15.6],'exalt','Perfect_Exalted_Orb',K('접두 번개 플랫','Lightning flat prefix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'lf'},'to':'d1','res':'ok'},{'to':'p1x','res':'fail'}],B6,show=['lf']),   # 3:46 슬라이드 7 '완벽한 엑잘 1번만, 상위 찬미 없이', 29:00 자막
 annul('p1x',[1,15.6],[{'to':'p1',**L_('빗나감','Miss')}],omens=('Omen_of_Sinistral_Annulment',),target=K('접두 잡옵 지우기','Remove the junk prefix')),   # 4:10 슬라이드 8, 31:00 좌측 소멸의 징조 59개
 act('d1','main',[0,16.6],'desecrate','Ancient_Collarbone',K('접두 세 번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'d2'}],B7),   # 4:22 슬라이드 10 '고대 빗장뼈', 29:35 고대 빗장뼈 툴팁
 act('d2','main',[0,17.6],'reveal',None,K('접두 냉기 플랫','Cold flat prefix'),None,K('공개','Reveal'),
     [{'if':{'added':'cf'},'to':'ok','res':'ok'},{'to':'d2x','res':'fail'}],B8,want='cf',show=['cf'],omens=['Omen_of_Abyssal_Echoes']),   # 29:25 자막 '메아리 켰는데도 17개', 30:05 완성품
 annul('d2x',[1,17.6],[{'to':'d1',**L_('다시 훼손','Desecrate again')}]),   # 31:00 빛의 징조 16개
 done([0,18.6])]
graph11('breach-ring-video-v2','Rings','Refined Breach Ring',80,
  'SL 원소 3플랫 재련된 균열 반지(2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 제련된 균열 반지 → 소멸로 옵션 1개 → 카오스 오브(화염 플랫 1티어) → 좌측 찬미 + 상위 찬미 + 완벽한 엑잘 → 보존된 빗장뼈 → 분열(1/3, 빗나가면 새 베이스) → 소멸로 분열 + 옵션 1개 → 균열의 에센스 → 강탈자 기폭제 65% → 바알 촉진시키는 주입기 1개 → 카오스 오브(모든 원소 저항) → 우측 찬미 + 완벽한 엑잘(희귀도, 빗나가면 소멸의 오브) → 좌측 찬미 + 엑잘 → 좌측 결정화 + 재빠른 합금 → 완벽한 엑잘(번개 플랫, 빗나가면 좌측 소멸의 징조 + 소멸의 오브) → 고대 빗장뼈 → 공개 + 심연의 메아리(냉기 플랫, 빛의 징조로 다시). 75% 퀄리티·디바인·축성·타락은 뺌.',
  {'pT':{'kr':'원소 플랫','en':'Elemental flats','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'sT':{'kr':'접미 저항·희귀도','en':'Resistance and rarity suffixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},
  {'high':{'pT':1,'sT':1},'bal':{'pT':2,'sT':2}},
  {'high':K('영상: 원소 플랫·접미 모두 1티어','Video: every flat and suffix T1'),'bal':K('반복으로 찾는 원소 플랫·접미 1~2티어','T1–2 on the looped flats and suffixes')},tags,nodes,
  [{'id':'L0','nodes':['s2','s2x'],'kr':'접미 희귀도','en':'Rarity suffix'},{'id':'L1','nodes':['p1','p1x'],'kr':'접두 번개 플랫','en':'Lightning flat prefix'},{'id':'L2','nodes':['d1','d2','d2x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'ff1','tmax':1,'fr':True},{'tag':'lf','tmax':1 if v=='high' else 2},{'tag':'cf','tmax':1 if v=='high' else 2,'des':True},
                               {'tag':'ar','tmax':1 if v=='high' else 2},{'tag':'rs','tmax':1 if v=='high' else 2},{'tag':'as','ess':True}]),
  {'quality':66,'sockets':0},{'all':[{'has':'ff1'},{'has':'lf'},{'has':'cf'},{'has':'ar'},{'has':'rs'},{'has':'as'}]},('high','bal'))
_gp=f"{H}/breach-ring-video-v2.json"; _g=json.load(open(_gp)); _g['basePrice']={'Divine_Orb':50}; json.dump(_g,open(_gp,'w'),ensure_ascii=False,indent=1)   # 31:00 비용 화면 '제련된 균열 반지 9개 : 450딥'

# ---------- 2. SaVeQ 집중구 (R43FVay8_XI) ----------
# 영상(첫 번째 집중구): 퀄리티 22% · 상위 마술의 에센스 주문 피해 분열 · 에너지 보호막 1티어 · 모든 주문 스킬 +2 · 접두 잡옵(훼손 공개 "아무거나")
# → 아스트리드의 창의성 장착 → 좌측 결정화 + 초월의 합금(시전 속도, 50/50으로 에너지 보호막 또는 잡옵이 지워짐) → 고대 갈비뼈로 접미 훼손(공개는 접두를 끝낸 뒤)
# → 완벽한 엑잘(에너지 보호막 1티어 기대, 혼합 에너지 보호막이 뜸) → 절사로 접두 → 에너지 보호막 2티어로 타협("완벽을 노리지 말 것")
# → 심연의 메아리 + 빛의 징조로 주문 치명타 명중 확률 1티어(2티어도 고민, 영상은 1티어까지). 완벽한 철 룬은 취향(정책 23).
# 하이엔드 = 영상(주문 치명타 1티어), 밸런스 = 주문 치명타 1~2티어.
# 2026-11-12 영상 전체 대조(자동 번역 자막 0:00~37:30, 메인 세션): 첫 번째 집중구 단계 일치(19:00 접두 훼손 + 분열 → 20:00 아스트리드 → 21:00 좌측 결정화 + 초월의 합금 → 21:40 접미 고대 훼손 → 22:40 완벽한 엑잘(혼합 에너지 보호막) → 23:00 절사 카오스 → 2티어 타협 → 24:00 메아리 + 빛의 징조로 주문 치명타 1티어(26:00)).
#   등급 C17: 세 번째 접두(에너지 보호막)도 하이엔드 1티어(영상은 2티어 타협), 밸런스 1~2티어.
tags={'sp':{'gi':43},'esp':{'gi':7,'tmax':1},'esf':{'gi':6,'tmax':'$pT'},'esh':{'gi':8,'tmax':'$pT'},'lvl':{'gi':16},'cs':{'gi':59},'cr':{'gi':19,'tmax':'$pT'},
      'ges':{'anyOf':['esp','esf','esh'],'label':K('에너지 보호막 접두','Energy shield prefix')},'keepF':{'anyOf':['ges','lvl','cs']}}
SPF=it('p','주문 피해 (75—89)% 증가 (분열)','(75—89)% increased Spell Damage (fractured)',['sp'],'c')
ESP=it('p','에너지 보호막 (92—100)% 증가','(92—100)% increased Energy Shield',['esp']); ESF=it('p','에너지 보호막 최대치 +(81—90)','+(81—90) to maximum Energy Shield',['esf'])
LV=it('s','모든 주문 스킬 레벨 +2','+2 to Level of all Spell Skills',['lvl']); CSA=it('s','시전 속도 (26—31)% 증가 (초월의 합금)','(26—31)% increased Cast Speed (Transcendent Alloy)',['cs'],'c')
CRT=it('s','주문 치명타 명중 확률 (54—59)% 증가','(54—59)% increased Critical Hit Chance for Spells',['cr'],'d')
RNA=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
GES=['esp','esf','esh']
def RF(vis):
    two={'count':{'tag':'ges','min':2}}
    return ROUTE_([{'if':{'all':[{'des':True},{'not':{'has':'cr'}}]},'to':'rvx'},
       {'if':{'all':[{'not':{'has':'cr'}},{'not':{'unrev':True}},{'sideLt':{'side':'s','n':3}}]},'to':'d1'},
       {'if':{'all':[{'not':two},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},{'if':{'not':two},'to':'w1'},{'if':{'unrevSide':'s'},'to':'rv'},{'to':'ok'}],vis)
RV=lambda vis: ROUTE_([{'if':{'not':{'count':{'tag':'ges','min':2}}},'to':'e1'},{'if':{'has':'cr'},'to':'ok'},{'to':'rvx'}],vis)
F0=[SPF,ESP,J('p'),LV]; F1=F0+[RNA]; F2=[SPF,ESP,LV,CSA,RNA]; F3=F2+[UN('s')]; F4=[SPF,ESP,ESF,LV,CSA,UN('s'),RNA]; F5=[SPF,ESP,ESF,LV,CSA,CRT,RNA]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'sp','fr':True,'ess':True},{'tag':'esp'},{'junk':'p'},{'tag':'lvl'}]},K('주문 피해 분열 + 에너지 보호막 1티어 + 모든 주문 스킬 +2 + 잡옵 1개 (퀄리티 22%, 특출난 베이스)','Fractured spell damage + T1 energy shield + all spell skills +2 + one junk line (22% quality, exceptional)'),F0),
 mark([0,0.6],'r1',F0),
 RUNE('r1',[0,1],'a1',F1),
 act('a1','main',[0,2],'essence','Transcendent_Alloy',K('잡옵을 지우고 시전 속도 (26—31)% 증가','The junk goes for (26—31)% increased Cast Speed'),[st('s','시전 속도 (26—31)% 증가 (제작 옵션)','(26—31)% increased Cast Speed (crafted)')],K('합금','Alloy'),RF({'d1':'ok','e1':F}),F2,ess='cs',omens=['Omen_of_Sinistral_Crystallisation']),
 act('d1','main',[0,3],'desecrate','Ancient_Rib',K('접미 세 번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RF({'e1':{}}),F3,omens=['Omen_of_Dextral_Necromancy']),
 act('e1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 세 번째 옵션','Third prefix'),None,K('엑잘','Exalt'),RF({'rv':'ok','w1':F}),F4,show=GES),
 act('w1','main',[1,4],'chaos','Perfect_Chaos_Orb',K('접두 세 번째 옵션','Third prefix'),None,K('카오스','Chaos'),RF({'rv':'ok'}),F4,show=GES,trim={'side':'p','keep':'keepF'}),
 act('rv','main',[0,5],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RV({'ok':'ok','rvx':F}),F5,want='cr',show=['cr'],omens=['Omen_of_Abyssal_Echoes']),
 annul('rvx',[1,5],[{'to':'d1','port':'right'}]),
 done([0,6])]
nodes[0]['start']['runes']=[]
graph11('saveq-focus-v2','Foci','Tasalian Focus',80,
  'SaVeQ 집중구(R43FVay8_XI) — 주문 피해 분열 + 에너지 보호막 1티어 + 모든 주문 스킬 +2 + 잡옵 → 아스트리드의 창의성 → 좌측 결정화 + 초월의 합금 → 고대 갈비뼈(접미 훼손) → 완벽한 엑잘(접두) → 절사로 에너지 보호막 → 공개(빛의 징조로 다시). 하이엔드 = 에너지 보호막·주문 치명타 1티어, 밸런스 = 1~2티어(영상 에너지 보호막 타협).',
  {**ROUTE,'pT':{'kr':'에너지 보호막·주문 치명타','en':'Energy shield and spell crit','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},PT,
  {'high':K('에너지 보호막·주문 치명타 명중 확률 1티어','T1 energy shield and spell crit chance'),'bal':K('에너지 보호막·주문 치명타 명중 확률 1~2티어 (영상은 에너지 보호막 2티어 타협)','T1–2 energy shield and spell crit chance (the video settles for T2 energy shield)')},tags,nodes,
  [{'id':'L1','nodes':['d1','rv','rvx'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'sp','fr':True,'ess':True},{'tag':'esp','tmax':1},{'tag':'ges'},{'tag':'lvl'},{'tag':'cs','ess':True},{'tag':'cr','tmax':1 if v=='high' else 2,'des':True}]),
  {'quality':22,'sockets':2},{'all':[{'has':'cr'},{'has':'cs'},{'count':{'tag':'ges','min':2}}]},('high','bal'))

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_saveq_focus.py'): _sp.run([_sy.executable, f'{H}/gen_saveq_focus.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_breach_ring_video.py'): _sp.run([_sy.executable, f'{H}/gen_breach_ring_video.py'], check=True)   # 2026-11-13 P5: 새 정책 전용 생성기가 덮어씀
