# P5 2026-11-13: 탱정 키타바 방패(gQa51XOS98s, 방패 부분 12:48~22:24) 플로우차트 전용 생성기 — gen_batch7.py 5번 구간을 옮기고 새 정책(11-13 14:17) 반영
# 근거: scratchpad review/W5-kitava-shield/timeline.md(슬라이드 전 구간), review/A1/plan.md
# 실행: cd scripts/graphs && python3 gen_tankjung_kitava_shield.py → tankjung-kitava-shield-v2.json (gen_batch7.py 끝에서 자동 호출, 그 파일의 이 아이템 구간을 대신함)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch7.py').read(); exec(_src[:_src.index('\n# ---------- 1.')])

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
#   새 정책(11-13 14:17, A·F, 사용자 결정: 슬라이드에 나온 대로): 11-12 확정 옵션(분열 = 받는 물리 피해 감소) 대신 슬라이드 규칙 그대로 —
#     STEP 04(15:22) 첫 목표 '접미 4종 중 1개'(받는 물리 피해 8% 감소·화염·냉기·번개 저항 최대치 +3%, 1티어) → STEP 06(16:18) 냉기·번개면 맹렬한 유동체로 화염(물리 피해 감소·화염이면 그대로)
#     → STEP 09 분열 = 물리 피해 감소 또는 화염 저항 최대치 → STEP 10(17:24) 카오스 '목표 4종 같음'(이미 붙은 계열 빼고 아무거나)
#     → STEP 11(17:54) 세 번째 '물리 피해 감소가 없으면 물리 피해 감소, 있으면 저항 최대치'. 공개 뒤 맹렬한 유동체(11-12 사용자 결정, STEP 11 완성 문구 '화염 저항 최대치 총 +6%')는 유지.
#     화면(왼쪽 칸·상자·완성 카드)은 슬라이드 완성 문구(분열 물리 피해 감소, 카오스 화염, 공개 냉기 → 유동체 화염)로 보임(shown). 실제 제작 장면이 없는 영상이라 '성공 회차'는 슬라이드 완성 문구.
#   등급(난이도 4 = 하이엔드·밸런스, 사용자 확정 2026-11-12): 분열 준비·카오스 오브는 싼 단계라 두 등급 모두 1티어(C15).
#   반복 구간 = 훼손 공개(빛의 징조)·절사 카오스. 하이엔드 = 영상(1티어), 밸런스 = 저항 최대치 공개 1~2티어·방어도 3종 1~2티어(정책 11장 15:02 '유효 옵션은 반드시, 티어만 타협').
#   절사 안전 조건(옛 whittleSafe)은 뺌: 방패 접두는 모두 레벨 75 이하, 접미는 물리 피해 감소 1티어 77·저항 최대치 75 이상이라 절사가 접미를 칠 일이 없음(이전 시뮬에서도 0회).
P={'high':{'mT':1,'aT':1},'bal':{'mT':2,'aT':2}}
tags={'pdr1':{'gi':13,'tmax':1},'mf1':{'gi':14,'tmax':1},'mc1':{'gi':15,'tmax':1},'ml1':{'gi':16,'tmax':1},
      'mf2':{'gi':14,'tmax':2},'mc2':{'gi':15,'tmax':2},'ml2':{'gi':16,'tmax':2},
      'mfT':{'gi':14,'tmax':'$mT'},'mc':{'gi':15,'tmax':'$mT'},'ml':{'gi':16,'tmax':'$mT'},'mcl':{'anyOf':['mc','ml'],'label':K('냉기·번개 저항 최대치 +3%','+3% maximum cold or lightning resistance')},
      'flat':{'gi':6,'tmax':'$aT'},'pct':{'gi':7,'tmax':'$aT'},'hyb':{'gi':8,'tmax':'$aT'},'arm':{'anyOf':['flat','pct','hyb'],'label':K('방어도 최대치·%·복합','Flat, % or hybrid armour')},
      # 새 정책(11-13): 슬라이드 STEP 04·10·11의 '접미 4종' 묶음
      'g4M':{'anyOf':['pdr1','mf1','mc1','ml1'],'shown':'pdr1','label':K('받는 물리 피해 감소·화염·냉기·번개 저항 최대치 1티어','T1 physical damage reduction or maximum fire, cold or lightning resistance')},   # 매직 단계(STEP 04·05)
      'g4':{'anyOf':['pdr1','mf1','mc1','ml1'],'shown':'mf1','label':K('받는 물리 피해 감소·화염·냉기·번개 저항 최대치 1티어','T1 physical damage reduction or maximum fire, cold or lightning resistance')},
      'g2':{'anyOf':['pdr1','mf1'],'shown':'pdr1','label':K('받는 물리 피해 감소·화염 저항 최대치 1티어','T1 physical damage reduction or maximum fire resistance')},
      'g4R':{'anyOf':['pdr1','mfT','mc','ml'],'shown':'mc','label':K('받는 물리 피해 감소·저항 최대치','Physical damage reduction or maximum resistance')},
      # 완성 카드(공개 뒤 맹렬한 유동체로 냉기·번개가 모두 화염이 됨): 분열 = g2, 나머지 두 줄 = 받는 물리 피해 감소·화염 저항 최대치
      'c2':{'anyOf':['pdr1','mf1'],'shown':'mf1','label':K('받는 물리 피해 감소·화염 저항 최대치 1티어','T1 physical damage reduction or maximum fire resistance')},
      'c3':{'anyOf':['pdr1','mfT'],'shown':'mfT','label':K('받는 물리 피해 감소·화염 저항 최대치','Physical damage reduction or maximum fire resistance')},
      'flat1':{'gi':6,'tmax':1},'pct1':{'gi':7,'tmax':1},'hyb1':{'gi':8,'tmax':1},'flat2':{'gi':6,'tmax':2},'pct2':{'gi':7,'tmax':2},'hyb2':{'gi':8,'tmax':2},
}
ARMDONE={'count':{'tag':'arm','min':3}}
SUFDONE={'all':[{'has':'pdr1'},{'count':{'tag':'g4R','min':3}}]}   # STEP 11: 물리 피해 감소 + 저항 최대치 2개(공개는 $mT)
SUF=lambda m='n',t='g4M': it('s','받는 물리 피해 8% 추가 감소 1티어','T1 8% physical damage reduction',[t],m)
X=lambda: it('x','잡옵','Junk',None,'j')
PD=SUF('f','g2'); MR=it('s','화염 저항 최대치 +3% 1티어','T1 +3% maximum fire resistance',['g4'])
MRD=it('s','냉기 저항 최대치 +3% (훼손)','+3% maximum cold resistance (desecrated)',['g4R'],'d')
MFD=it('s','화염 저항 최대치 +3% (훼손)','+3% maximum fire resistance (desecrated)',['c3'],'d')
I1=[PD,MR]; I2=I1+[UN('s')]; I3=I1+[MRD]; I3F=I1+[MFD]; I4=[J('p'),J('p')]+I3F; I5=[J('p')]+I4
I6=[it('p','방어도 최대치','Flat armour',['flat']),it('p','방어도 %','% armour',['pct']),it('p','방어도 %·기절 한계치 복합','Armour % and stun threshold',['hyb'])]+I3F
OKM={'if':{'has':'g4M'},'to':'fl','res':'ok','label':K('접미 4종 중 하나','One of the four suffixes')}
G2OK={'any':[{'has':'pdr1'},{'has':'mf1'}]}
b0=base('m1',None,K('특출난 타호아의 거대 방패 구입 (소켓 2개, 아이템 레벨 81)','Buy an exceptional Tawhoan Tower Shield (two sockets, item level 81)'),[]); b0['id']='b0'; b0.pop('start',None)   # 14:30 STEP 02
nodes=[b0,
 {'id':'hq','kind':'side','group':'prep','pos':[1,0.5],'attach':['b0','m1'],'cur':'Vaal_Armourers_Infuser','goal':K('퀄리티 30%, 선택·비용 미포함','30% quality, optional, not costed'),'label':K('퀄리티','Quality')},   # 14:58 STEP 03
 act('m1','prep',[0,1],'transmute','Perfect_Orb_of_Transmutation',K('매직 첫 옵션','First magic option'),None,K('진화','Transmute'),   # 15:52 STEP 05 '최초 1회'
     [OKM,{'if':{'full':'s'},'to':'m2x','label':K('다른 접미','Another suffix')},{'to':'m2','label':K('접두','A prefix')}],[SUF()],show=['g4M']),
 act('m2','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('매직 접미 옵션','Magic suffix option'),None,K('확장','Augment'),
     [OKM,{'if':{'not':{'full':'s'}},'to':'m2','res':'fail','label':K('접두','A prefix')},{'to':'m2x','res':'fail','label':K('다른 접미','Another suffix')}],[J('p'),SUF()],show=['g4M']),
 {'id':'m2x','kind':'act','group':'prep','pos':[1,2],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),
  'target':K('빗나간 접미 지우기','Remove the missed suffix'),'edges':[{'if':{'full':'s'},'to':'m2x','label':K('접미가 남음','Suffix still there')},{'to':'m2','label':K('접미가 지워짐','Suffix removed')}]},
 act('fl','prep',[0,2.8],'flux','Blazing_Flux',K('냉기·번개 저항 최대치를 화염으로','Cold or lightning maximum resistance into fire'),[st('s','화염 저항 최대치 +3%','+3% maximum fire resistance')],K('유동체','Flux'),[{'to':'r1'}],[J('p'),SUF()],
     skipIf=G2OK,skipTo='r1',skipNote=K('받는 물리 피해 감소·화염이면 건너뜀','Skip on physical damage reduction or fire')),   # 16:18 STEP 06 분열 전 접미 변환
 act('r1','prep',[0,3.8],'augment','Perfect_Orb_of_Augmentation',K('매직 접두 옵션','Magic prefix option'),[st('p','랜덤 옵션 1개','One random option')],K('확장','Augment'),[{'to':'r2'}],[J('p'),SUF()],skipIf={'full':'p'},skipTo='r2',skipNote=K('옵션 2개면 건너뜀','Skip with two options')),   # 16:46 STEP 07
 act('r2','prep',[0,4.8],'regal','Perfect_Regal_Orb',K('레어 전환','To rare'),[st(None,'옵션 3개','Three options')],K('제왕','Regal'),[{'to':'f1'}],[J('p'),SUF(),X()]),
 act('f1','prep',[0,5.8],'desecrate','Preserved_Rib',K('분열 확률을 높이기 위해 훼손','Desecrate to raise the fracture odds'),[st(None,'훼손 옵션 1개 (미공개)','One desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f2'}],[J('p'),SUF(),X(),UN('x')]),   # 16:46 STEP 07·17:12 STEP 08
 act('f2','prep',[0,6.8],'fracture','Fracturing_Orb',K('분열','Fracture'),[st(None,'받는 물리 피해 감소·화염 저항 최대치가 분열되면 성공','Success when physical damage reduction or maximum fire resistance fractures')],K('분열','Fracture'),   # 17:16 STEP 09
     [{'if':{'fractured':'g2'},'to':'f4','res':'ok'},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another option fractured')}],[J('p'),PD,X(),UN('x')],pAll=True),
 {'id':'xj','kind':'exit','group':'prep','pos':[1,6.8],'simTo':'b0','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another option fractured — new base')},
 dict(cleanup('f4',[0,7.8],[],[{'to':'ms','label':K('분열 + 옵션 1개','Fracture + one option')}],K('분열 + 옵션 1개만 남기기','Keep only the fracture + one option')),group='prep',maxJunk=1,item=[PD,X()]),   # 17:26 STEP 10 '소멸의 오브 ×2'
 mark([0,8.4],'t2',[PD,X()]),
 act('t2','main',[0,9],'chaos','Chaos_Orb',K('접미 두 번째 옵션','Second suffix option'),None,K('카오스','Chaos'),   # 17:26 STEP 10
     [{'if':{'count':{'tag':'g4','min':2}},'to':'t3','res':'ok'},{'to':'t2','res':'fail'}],I1,show=['g4'],skipIf={'count':{'tag':'g4','min':2}},skipTo='t3',skipHide=True),
 act('t3','main',[0,10],'desecrate','Ancient_Rib',K('접미 세 번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'t4'}],I2,omens=['Omen_of_Dextral_Necromancy']),   # 17:56 STEP 11 ①②
 act('t4','main',[0,11],'reveal',None,K('접미 세 번째 옵션 공개','Reveal the third suffix'),None,K('공개','Reveal'),   # 17:56 STEP 11 ③④
     [{'if':SUFDONE,'to':'tf','res':'ok'},{'to':'t4x','res':'fail'}],I3,want='g4R',show=['g4R'],omens=['Omen_of_Abyssal_Echoes']),
 annul('t4x',[1,11],[{'to':'t3','label':K('다시 훼손','Desecrate again')}]),   # 17:56 STEP 11 NO: 빛의 징조 → 소멸의 오브 → ①부터
 act('tf','main',[0,12],'flux','Blazing_Flux',K('냉기·번개 저항 최대치를 화염으로','Cold or lightning maximum resistance into fire'),[st('s','화염 저항 최대치 +3% 두 줄 (하나 훼손)','Two +3% maximum fire resistance lines (one desecrated)')],K('유동체','Flux'),[{'to':'t5'}],I3F),   # 영상에 없음(내부 결정, 사용자 결정 2026-11-12)
 act('t5','main',[0,13],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 2개','Two random options')],K('엑잘','Exalt'),[{'to':'t6'}],I4,omens=['Omen_of_Greater_Exaltation']),   # 19:06 STEP 12 ①②
 act('t6','main',[0,14],'exalt','Perfect_Exalted_Orb',K('접두 세 번째 옵션','Third prefix'),[st('p','랜덤 옵션 1개','One random option')],K('엑잘','Exalt'),   # 19:06 STEP 12 ③
     [{'to':'t7'}],I5),
 act('t7','main',[0,15.6],'chaos','Perfect_Chaos_Orb',K('가장 낮은 옵션을 방어도로','The lowest option into armour'),[st('p','방어도 최대치·%·복합 1티어','T1 flat, % and hybrid armour')],K('카오스','Chaos'),   # 19:10~21:26 STEP 13
     [{'if':ARMDONE,'to':'ok','res':'ok'},{'to':'t7','res':'fail'}],I6,omens=['Omen_of_Whittling'],skipIf=ARMDONE,skipTo='ok',skipHide=True,
     over=[{'param':{'aT':2},'set':{'showText':[st('p','방어도 최대치·%·복합 1~2티어','T1–2 flat, % and hybrid armour')]}}]),
 done([0,16.6])]
graph('tankjung-kitava-shield-v2','Shields_str','Tawhoan Tower Shield',81,
  '탱정 키타바 방패(gQa51XOS98s, 2026-11-12 W5 영상 전체 재대조, 새 플로우차트 기준) — 특출난 타호아의 거대 방패 → 완벽한 진화 → 완벽한 확장 + 소멸의 오브로 접미 4종(받는 물리 피해 감소·화염·냉기·번개 저항 최대치) 중 하나 → 냉기·번개면 맹렬한 유동체(화염) → 완벽한 확장·완벽한 제왕 + 보존된 갈비뼈(미공개) → 분열(물리 피해 감소·화염 저항 최대치, 실패면 새 베이스) → 소멸 2번 + 카오스 오브(접미 4종 중 남은 것) → 우측 강령술 + 고대 갈비뼈 → 공개(물리 피해 감소가 없으면 물리 피해 감소, 있으면 저항 최대치, 심연의 메아리, 빗나가면 빛의 징조 + 소멸) → 맹렬한 유동체(화염 저항 최대치 두 줄, 슬라이드 완성 문구) → 상위 찬미 + 완벽한 엑잘 → 완벽한 엑잘 → 절사의 징조 + 완벽한 카오스 오브로 방어도 최대치·%·복합. 하이엔드 = 영상(모두 1티어), 밸런스 = 저항 최대치 공개·방어도 3종 1~2티어. 퀄리티 30%·철 룬은 비용에서 뺌.',
  {'mT':{'kr':'훼손 저항 최대치','en':'Desecrated maximum resistance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'aT':{'kr':'방어도 접두 (절사)','en':'Armour prefixes (Whittling)','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})}},dict(P,ess=P['bal']),
  {'high':K('영상: 모두 1티어','Video: all T1'),'bal':K('저항 최대치 공개·방어도 3종 1~2티어','T1–2 revealed maximum resistance and armour'),'ess':None},
  tags,nodes,
  [{'id':'L0','nodes':['m2','m2x'],'kr':'매직 접미 찾기','en':'Magic suffix hunt',
    # 다중 루프를 상자 하나로(사용자 확정 2026-11-12 17:06, 정책 11장) — STEP 05 순서도(15:52~16:18)
    'fold':True,'goal':K('매직 접미 4종(받는 물리 피해 감소·화염·냉기·번개 저항 최대치) 중 하나 1티어','One of the four T1 suffixes (physical damage reduction, maximum fire, cold or lightning resistance) on a magic item'),
    'steps':[{**K('완벽한 확장의 오브로 접미','Perfect Orb of Augmentation for a suffix'),'node':'m2'},
             {**K('빗나간 접미 — 접미가 지워질 때까지 소멸의 오브','Missed suffix: Annulment until the suffix is gone'),'node':'m2x'}],
    'item':[J('p'),SUF()]},
   {'id':'L1','nodes':['t3','t4','t4x'],'kr':'훼손 공개','en':'Desecrated reveal'},{'id':'L2','nodes':['t7'],'kr':'절사','en':'Whittling'}],
  [{'id':'high','kr':'하이엔드 옵션','en':'High-end','lines':[{'tag':'flat1'},{'tag':'pct1'},{'tag':'hyb1'},{'tag':'g2','fr':True},{'tag':'c2'},{'tag':'c3','tmax':1,'des':True}]},
   {'id':'bal','kr':'밸런스 옵션','en':'Balance','lines':[{'tag':'flat2'},{'tag':'pct2'},{'tag':'hyb2'},{'tag':'g2','fr':True},{'tag':'c2'},{'tag':'c3','tmax':2,'des':True}]}],
  {'sockets':2},{'all':[{'has':'pdr1'},{'count':{'tag':'mfT','min':2}},{'has':'flat'},{'has':'pct'},{'has':'hyb'},{'full':'p'},{'full':'s'}]})
_p=f'{H}/tankjung-kitava-shield-v2.json'; _g=json.load(open(_p))   # 등급: 난이도 4 → 하이엔드·밸런스(사용자 확정 2026-11-12)
_D={'high':K('영상: 모두 1티어','Video: all T1'),'bal':K('저항 최대치 공개·방어도 3종 1~2티어','T1–2 revealed maximum resistance and armour')}
_g['groups']=[{'id':'prep','kr':'베이스템 완성','en':'Finished base','cols':[0,1]},{'id':'main','kr':'옵션 추가 작업','en':'Adding modifiers','cols':[0,1]}]
_g['start']='b0'
_g['strategies']=[{'id':v,'params':P[v]} for v in ('high','bal')]
_g['versions']=[{'id':v,'kr':kr,'en':en,'params':P[v],'desc':_D[v]} for v,kr,en in (('bal','밸런스','Balance'),('high','하이엔드','High-end'))]
json.dump(_g,open(_p,'w'),ensure_ascii=False,indent=1)

