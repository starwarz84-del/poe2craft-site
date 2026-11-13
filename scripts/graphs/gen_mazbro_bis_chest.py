# D1 2026-11-13: MazBro BiS 갑옷(LUB59xlkNtk) 전용 플로우차트 생성기 — gen_batch19.py 2번 구간을 옮겨 옴(그 파일 끝에서 이 파일을 부름)
# 근거: scratchpad review/W7-bis-chest/timeline.md, frames/
# 실행: cd scripts/graphs && python3 gen_mazbro_bis_chest.py → mazbro-bis-chest-v2.json
# 밸런스 새로 만듦(사용자 확정 2026-11-13 15:42 ①: 난이도 표 4 전문가 → 하이엔드·밸런스). 영상 21:00 '여기서 끝내도 됨'(복합 저항 1개 + 냉기 저항 1티어)대로
#   접미 반복을 복합 저항 하나 + 화염·냉기·번개 저항 1~2티어(C17 밸런스 1~2티어)에서 끝냄. 마지막 훼손 공개는 영상에서 빛의 징조로 다시 해서(27:05~27:28) 밸런스도 다시(C17-3).
#   자리 막기(훼손)는 완성 판정에 넣지 않음: 막기를 뺀 접미 옵션이 모두 복합 저항·원소 저항 1~2티어일 때만 끝(빛의 징조로 막기를 지우면 남는 옵션).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch19.py').read(); exec(_src[:_src.index('# ---------- 1. 반지깎는노인')])

# ---------- 2. MazBro BiS 갑옷 (LUB59xlkNtk) ----------
# 2026-11-12 W7 영상 전체 재대조(자막 0:00~34:33 + 화면 캡처 94장, 근거 scratchpad review/W7-bis-chest/timeline.md) + 새 플로우차트 기준(정책 11장 맨 위):
#   영상 흐름 한 줄. 성공 회차 = 첫 번째 흉갑(12:40~29:42, 완성 툴팁 29:42). 두 번째 흉갑(30:30~33:30)과 유동체·신성한 오브는 꿀팁 후보.
# 베이스 준비(3:23 노트 Step 1 + 3:36~4:45 시연, 흉갑 분열 순간은 영상에 없음): 요술사 외투(노트 '1 Chaos') → 완벽한 진화 → 확장·소멸로 정신력 1티어
#   → (신성한 오브로 최대 수치 — 선택·비용 미포함) → 제왕 → 보존된 갈비뼈로 훼손(4:20 자막) → 분열(1/3) → 소멸로 분열 + 옵션 1개(5:10~5:27 화면)
# 본 제작: 메드베드의 보살핌(5:40 화면) → 카오스 오브로 정신력 %(6:28 화면, 일반 카오스 오브) → 좌측 찬미 + 상위 엑잘티드 오브로 마나 %(6:38 상위 47 → 46, 7:00 자막
#   '접두는 카오스 후 상위 엑잘'), 빗나가면 소멸의 오브(50/50, 정신력 %가 지워지면 카오스부터) → 8:10 접두 완성
#   → 접미 첫 상위 엑잘(12:46 생명력 재생 잡옵) → 우측 결정화 + 심연의 에센스(13:04 징표) → 보존된 갈비뼈(징표 훼손) → 공개 + 메아리(13:43 생명력 재생 = 자리 막기)
#   → [접힌 상자] 상위 찬미 + 완벽한 엑잘(2개) / 절사의 징조 + 완벽한 카오스 오브 / 우측 소멸의 징조 + 소멸의 오브, 막기가 지워지면 심연의 에센스 단계부터
#     (성공 회차 23:47 이중 엑잘 화염·카오스 → 24:36~24:44 절사 2번으로 냉기·카오스, 막기는 화염 저항 1티어)
#   → 빛의 징조 + 소멸의 오브로 막기 제거(26:40) → 고대 갈비뼈(26:30 자막) → 공개 + 메아리로 정신력 점유 효율(27:30 화면, 빗나가면 빛의 징조로 다시)
# 신성한 오브(28:00)·축복받은 자의 징조(29:20)·유동체(32:00)는 수치 올리기라 뺌(14장).
# 등급: 난이도 5(극한) → 하이엔드만(10장). 복합 저항은 티어가 하나뿐이라 티어 타협 자리가 없음.
# 내부 결정: 반복의 완성 조건은 영상대로 복합 저항 셋 중 둘(17:00·19:30 번개·카오스도 받아들임). 상자 글·왼쪽 칸·카드는 성공 회차의 두 옵션(화염·카오스, 냉기·카오스, 24:44)으로 적음(확정 옵션 규칙, 활과 같은 방식).
#   두 옵션만 받는 시뮬(시험 1500회)은 평균 약 6,900 div, 셋 중 둘은 약 3,300 div. 접두 카오스·엑잘도 같은 방식(정신력 %·마나 % 중 먼저 나온 쪽).
P1={'high':{'g':1,'pT':1},'bal':{'g':0,'pT':2}}
tags={'spirit':{'gi':15,'tmax':1},'isp':{'gi':53},'ima':{'gi':52},'pre':{'anyOf':['isp','ima'],'label':K('메드베드 접두 % 옵션','Medved % prefix')},'hf':{'gi':56},'hc':{'gi':57},'sre':{'gi':23},
      'mkS':{'gi':47},
      'b14':{'gi':14},
      'hl':{'gi':58},'good':{'anyOf':['hf','hc','hl'],'shownBy':{'bal':'hl'},'label':K('원소 및 카오스 복합 저항','Elemental and chaos hybrid resistances')},
      'keepW':{'anyOf':['isp','ima','hf','hc','hl'],'label':K('남길 옵션','Lines to keep')},
      # 밸런스(영상 21:00): 복합 저항 하나 + 화염·냉기·번개 저항 1~2티어
      'rf':{'gi':2,'tmax':'$pT'},'rc':{'gi':3,'tmax':'$pT'},'rl':{'gi':4,'tmax':'$pT'},
      'eres':{'anyOf':['rf','rc','rl'],'shownBy':{'bal':'rc'},'label':K('화염·냉기·번개 저항 1~2티어','T1–2 fire, cold or lightning resistance')},
      'keepB':{'anyOf':['good','eres'],'shownBy':{'bal':['hl','rc']},'label':K('복합 저항·화염·냉기·번개 저항 1~2티어','Hybrid resistance or T1–2 fire, cold or lightning resistance')},   # 밸런스 카드 두 줄(한 묶음이라 꿀팁 한 줄 — R-D1 5), 성공 회차 21:06 번개 및 카오스 + 냉기 저항 1티어. 두 번째 줄: 복합 저항 둘로 끝나는 회차도 있음(fincheck)
      'keepBW':{'anyOf':['isp','ima','good','eres'],'label':K('남길 옵션','Lines to keep')}}
DONE2={'count':{'tag':'good','min':2}}
DONEB={'all':[{'has':'good'},{'count':{'tag':'keepB','min':2}},{'not':{'junk':{'side':'s','tag':'keepB'}}},{'any':[{'full':'s'},{'des':False}]}]}   # 막기를 뺀 접미가 모두 복합·원소 저항(막기가 원소 저항이어도 세지 않음)
DONE={'any':[{'all':[{'param':{'g':1}},DONE2]},{'all':[{'param':{'g':0}},DONEB]}]}   # 영상은 복합 저항 셋 중 둘이면 됨(17:00·19:30 번개·카오스도 '원하는 것') — 카드·상자 글은 성공 회차의 두 옵션
L_=lambda kr,en: {'label':K(kr,en)}
F={'res':'fail'}
def RM(vis):   # 접미 반복(접힌 상자)과 공개 뒤: 아이템 상태로 다음 상자
    out=ROUTE_([{'if':{'all':[DONE,{'des':True}]},'to':'f1'},
       {'if':{'all':[DONE,{'sideLt':{'side':'s','n':3}}]},'to':'f2'},
       {'if':DONE,'to':'da'},
       {'if':{'all':[{'not':{'des':True}},{'not':{'unrevSide':'s'}},{'not':{'junk':{'side':'s','tag':'good'}}}]},'to':'b2n'},   # 잡옵이 없으면 심연의 에센스·징표 훼손을 건너뛰고 빈자리 훼손(행동은 같음, 레시피 글 정리 R-D1)
       {'if':{'all':[{'not':{'des':True}},{'not':{'unrevSide':'s'}}]},'to':'mA'},
       {'if':{'sideLt':{'side':'s','n':3}},'to':'s1'},
       {'if':{'all':[{'param':{'g':1}},{'has':'good'},{'whittleSafe':{'tag':'keepW','keepDes':True}}]},'to':'w1'},
       {'if':{'all':[{'param':{'g':0}},{'has':'keepB'},{'whittleSafe':{'tag':'keepBW','keepDes':True}}]},'to':'w1'},
       {'to':'da'}],vis)
    for e in out:   # 등급별로 둘인 절사 선: 숨긴 쪽도 성공·실패 표시를 같이(밸런스 레시피 글이 '성공 … → 절사'로 읽히던 것, R-D1)
        v=vis.get(e['to'])
        if e.get('hide') and v is not None and 'res' not in e: e.update({k:x for k,x in (v if isinstance(v,dict) else {'res':v}).items() if k!='label'})
    return out
SPR=it('p','정신력 +(57—61) (분열)','+(57—61) to Spirit (fractured)',['spirit'],'f'); MD=it('r','메드베드의 보살핌','Medved’s Tending',None,'r')
ISP=it('p','정신력 (1—20)% 증가','(1—20)% increased Spirit',['isp']); IMA=it('p','마나 최대치 (1—20)% 증가','(1—20)% increased maximum Mana',['ima'])
HF=it('s','화염 및 카오스 저항 +(3—31)%','+(3—31)% to Fire and Chaos Resistances',['hf']); HC=it('s','냉기 및 카오스 저항 +(3—31)%','+(3—31)% to Cold and Chaos Resistances',['hc'])
HL=it('s','번개 및 카오스 저항 +(3—31)%','+(3—31)% to Lightning and Chaos Resistances',['hl'])   # 밸런스 성공 회차(영상 21:06)
MKS=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mkS'],'c')
LRB=it('s','초당 생명력 재생 (훼손, 자리 막기)','Life Regeneration per second (desecrated, blocker)',None,'d')
FRB=it('s','화염 저항 (훼손, 자리 막기)','Fire Resistance (desecrated, blocker)',None,'d')
RCB=it('s','냉기 저항 +(36—45)%','+(36—45)% to Cold Resistance',['rc'])   # 밸런스 접힌 상자 왼쪽 칸: 영상 21:00 냉기 저항 1티어(1~2티어 범위)
SRE=it('s','스킬의 정신력 점유 효율 (6—12)% 증가','(6—12)% increased Spirit Reservation Efficiency of Skills',['sre'],'d')
B0=[SPR,J('s')]; B1=B0+[MD]; B2=[SPR,ISP,MD]; B3=[SPR,ISP,IMA,MD]; B4=B3[:3]+[J('s'),MD]; B5=B3[:3]+[MKS,MD]; B6=B3[:3]+[UN('s'),MD]; B7=B3[:3]+[LRB,MD]
BL=B3[:3]+[HF,HC,FRB,MD]; BLb=B3[:3]+[HL,RCB,FRB,MD]; B10b=B3[:3]+[HL,RCB,UN('s'),MD]; B11b=B3[:3]+[HL,RCB,SRE,MD]; B9=B3[:3]+[HF,HC,MD]; B10=B3[:3]+[HF,HC,UN('s'),MD]; B11=B3[:3]+[HF,HC,SRE,MD]
nodes=[
 mark([0,0.6],'r1',B0),
 act('r1','main',[0,1],'rune',None,K('메드베드의 보살핌 장착','Socket Medved’s Tending'),[st(None,'영혼 핵 옵션이 붙을 수 있음','Soul core lines can roll')],K('룬','Rune'),[{'to':'c1'}],B1,rune=K('메드베드의 보살핌','Medved’s Tending')),   # 5:40 화면 '제거·교체 불가' 확인 창
 act('c1','main',[0,2],'chaos','Chaos_Orb',K('접두 정신력 % 증가','Prefix % increased Spirit'),None,K('카오스','Chaos'),[{'if':{'has':'pre'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],B2,show=['isp']),   # 영상은 둘 중 먼저 나온 쪽(6:28 정신력, 6:50 마나) — 상자 글은 6:28 정신력   # 6:28 화면 정신력 11%
 act('e1','main',[0,3],'exalt','Greater_Exalted_Orb',K('접두 마나 최대치 % 증가','Prefix % increased maximum Mana'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre','min':2}},'to':'s0','res':'ok'},{'to':'e1x',**F,**L_('빗나감 — 소멸','Miss: annul')}],B3,show=['ima'],omens=['Omen_of_Sinistral_Exaltation']),   # 6:38 상위 엑잘(47 → 46), 7:00 자막
 annul('e1x',[1,3],[{'if':{'not':{'has':'pre'}},'to':'c1',**F,**L_('정신력 %가 지워짐 — 카오스부터','% Spirit gone: back to Chaos')},{'to':'e1','res':'ok',**L_('다시 엑잘','Exalt again')}],
       omens=(),target=K('빗나간 접두 지우기 — 확률 반반','Remove the missed prefix — a 50/50')),   # 6:44 '50/50'
 act('s0','main',[0,4],'exalt','Greater_Exalted_Orb',K('접미 첫 번째 옵션','First suffix'),[st('s','잡옵 (초당 생명력 재생)','Junk (life regeneration per second)')],K('엑잘','Exalt'),[{'to':'mA'}],B4),   # 12:46 화면 생명력 재생 2티어
 act('mA','main',[0,5],'essence','Essence_of_the_Abyss',K('접미 잡옵을 지우고 심연의 군주의 징표','The junk suffix goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('에센스','Essence'),[{'to':'b2'}],B5,
     ess='mkS',mark=True,omens=['Omen_of_Dextral_Crystallisation'],skipIf={'not':{'junk':{'side':'s','tag':'good'}}},skipTo='b2n',skipHide=True,skipNote=K('첫 접미가 복합 저항이면 징표 없이 빈자리 훼손','First suffix is a hybrid: no Mark, desecrate the open slot')),   # 13:04 화면 징표, 12:58 우측 결정화 툴팁
 act('b2','main',[0,6],'desecrate','Preserved_Rib',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),
     [{'if':{'not':{'unrevSide':'s'}},'to':'b2n',**L_('징표 없음 — 빈자리에 훼손','No Mark: desecrate the open slot')},{'to':'b3'}],B6,
     fromMark=True,skipIf={'not':{'has':'mkS'}},skipTo='b2n',skipHide=True),   # 징표가 없으면 건너뜀 — 그 통과 수가 b2 → b2n 선에 붙음   # 10:30 자막 '보존된 갈비뼈', 13:36 가방 II 뼈
 act('b2n','main',[2,6],'desecrate','Preserved_Rib',K('접미 빈자리 훼손','Desecrate the open suffix'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'b3'}],B6,omens=['Omen_of_Dextral_Necromancy']),   # 30:58~31:04 두 번째 흉갑 '막기 먼저 훼손'(접미 빈자리), 첫 흉갑 성공 회차에는 없음
 act('b3','main',[0,7],'reveal',None,K('자리 막기 옵션 확인','Reveal the blocker'),[st('s','초당 생명력 재생','Life Regeneration per second')],K('공개','Reveal'),RM({'s1':{}}),B7,want='b14',missPick='lvl',omens=['Omen_of_Abyssal_Echoes']),   # 생명력 재생이 없으면 가장 높은 레벨 옵션(16:04 편집 자막 '높은 레벨로 막기')   # 13:38~13:43 화면 공개 2번(메아리), 생명력 재생 선택
 act('s1','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접미 화염·카오스 저항 + 냉기·카오스 저항','Suffix fire and chaos + cold and chaos resistances'),None,K('엑잘','Exalt'),RM({'f1':'ok','w1':F,'da':F}),BL,show=['hf','hc'],omens=['Omen_of_Greater_Exaltation'],over=[{'param':{'g':0},'set':{'show':['hl','rc'],'item':BLb}}],
     goalBy={'bal':K('접미 번개·카오스 저항 + 냉기 저항 1~2티어 — 복합 저항 하나와 원소 저항','Suffix lightning and chaos resistance + T1–2 cold resistance: one hybrid and an elemental resistance')}),   # 14:30·23:47 상위 찬미 + 완벽한 엑잘
 act('w1','main',[1,8],'chaos','Perfect_Chaos_Orb',K('가장 낮은 잡옵을 다시','Reroll the lowest junk line'),None,K('카오스','Chaos'),RM({'f1':'ok','s1':F}),BL,show=['hf','hc'],omens=['Omen_of_Whittling'],over=[{'param':{'g':0},'set':{'show':['rc'],'item':BLb}}]),   # 18:10·24:36~24:42 절사
 annul('da',[2,8],RM({'s1':{'res':'ok'},'mA':F}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 지우기','Remove a junk suffix')),   # 15:00 빛의 징조를 끄고 우측 소멸
 annul('f1',[0,9],[{'if':DONE,'to':'f2'},{'if':{'junk':{'side':'s','tag':'good'}},'to':'mA','hide':True},{'to':'b2n','hide':True}],target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),   # 막기 자리에 복합 저항이 붙어 있었으면(시뮬 드묾) 막기부터 다시   # 26:40 빛의 징조로 화염 저항 제거
 act('f2','main',[0,10],'desecrate','Ancient_Rib',K('접미 세 번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f3'}],B10,over=[{'param':{'g':0},'set':{'item':B10b}}]),   # 26:30 자막 '고대 갈비뼈 14개'
 act('f3','main',[0,11],'reveal',None,K('접미 정신력 점유 효율','Suffix Spirit Reservation Efficiency'),None,K('공개','Reveal'),[{'if':{'added':'sre'},'to':'ok','res':'ok'},{'to':'f3x',**F}],B11,want='sre',show=['sre'],omens=['Omen_of_Abyssal_Echoes'],over=[{'param':{'g':0},'set':{'item':B11b}}]),   # 27:30 화면 6% 선택
 annul('f3x',[1,11],[{'to':'f2',**L_('다시 훼손','Desecrate again')}]),   # 27:05~27:28 빛의 징조 + 소멸 반복
 done([0,12])]
graph11('mazbro-bis-chest-v2','Body_Armours_str_int','Conjurer Mantle',82,
  'MazBro BiS 갑옷(LUB59xlkNtk, 2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 요술사 외투 → 완벽한 진화·확장·소멸로 정신력 1티어 → 제왕 → 보존된 갈비뼈 → 분열(1/3) → 소멸로 분열 + 옵션 1개 → 메드베드의 보살핌 → 카오스 오브(정신력 %) → 좌측 찬미 + 상위 엑잘(마나 %, 빗나가면 소멸의 오브) → 상위 엑잘(접미 잡옵) → 우측 결정화 + 심연의 에센스 → 보존된 갈비뼈 → 공개(자리 막기) → 상위 찬미 + 완벽한 엑잘·절사 + 완벽한 카오스·우측 소멸 반복(화염·카오스 + 냉기·카오스) → 빛의 징조로 막기 제거 → 고대 갈비뼈 → 정신력 점유 효율 공개. 메드베드 옵션 가중치는 추정. 신성한 오브·축복받은 자의 징조·유동체는 뺌.',
  {'pT':{'kr':'원소 저항','en':'Elemental resistance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'g':{'kr':'복합 저항','en':'Hybrid resistances','values':TV({'1':('2개','Two'),'0':('1개 + 원소 저항','One + elemental')})}},P1,
  {'high':K('영상: 복합 저항 2개 + 정신력 점유 효율','Video: two hybrid resistances + Spirit reservation efficiency'),
   'bal':K('영상 21:00 \'여기서 끝내도 됨\': 복합 저항 1개 + 원소 저항 1~2티어 + 정신력 점유 효율','Video 21:00 “you can stop here”: one hybrid + T1–2 elemental resistance + Spirit reservation efficiency')},tags,nodes,
  [{'id':'L1','nodes':['s1','w1','da'],'kr':'접미 복합 저항','en':'Hybrid resistance suffixes',
    'fold':True,'goal':K('접미 화염·카오스 저항 + 냉기·카오스 저항','Fire and chaos + cold and chaos resistance suffixes'),
    'goalBy':{'bal':K('접미 번개·카오스 저항 + 냉기 저항 1~2티어 — 복합 저항 하나와 원소 저항','Lightning and chaos resistance + T1–2 cold resistance: one hybrid and an elemental resistance')},
    'itemBy':{'bal':BLb},
    'steps':[{**K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 2개','Omen of Greater Exaltation + Perfect Exalted Orb for two suffixes'),'node':'s1'},
             {**K('복합 저항이 있고 가장 낮은 옵션이 잡옵이면 절사의 징조 + 완벽한 카오스 오브','A hybrid on and the lowest line is junk: Omen of Whittling + Perfect Chaos Orb'),'node':'w1'},
             {**K('아니면 우측 소멸의 징조 + 소멸의 오브로 접미 잡옵 지우기','Otherwise Omen of Dextral Annulment + Orb of Annulment on a junk suffix'),'node':'da'}],
    'worst':{**K('자리 막기 훼손이 지워지면 심연의 에센스 단계부터','Blocker gone: back to the Essence of the Abyss step'),'to':'mA'},
    'item':BL},
   {'id':'L2','nodes':['f2','f3','f3x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','fr':True},{'tag':'isp'},{'tag':'ima'},*([{'tag':'hf'},{'tag':'hc'}] if v=='high' else [{'tag':'keepB'},{'tag':'keepB'}]),{'tag':'sre','des':True}]),
  {'sockets':2},{'all':[DONE,{'has':'isp'},{'has':'ima'},{'has':'sre'}]},('high','bal'),xsub=["Medved's Tending"],xroll=True)
_gp=f"{H}/mazbro-bis-chest-v2.json"; _g=json.load(open(_gp))
for _n in _g['nodes']:
    if _n.get('group')=='main': _n['pos']=[_n['pos'][0], _n['pos'][1]+8.4]
_g['basePrice']={'Chaos_Orb':1}   # 2:50 노트 'Conjurer Mantle Cloak … 1 Chaos'
_SP=lambda m='n': {'s':'p','kr':'정신력 +(57—61)'+(' (분열)' if m=='f' else ''),'en':'+(57—61) to Spirit'+(' (fractured)' if m=='f' else ''),'m':m,'tags':['spirit']}
_JK=lambda s: {'s':s,'kr':'잡옵','en':'Junk','m':'j'}
_prep=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'p1','start':{'rar':'normal','mods':[]},'label':K('요술사 외투 구입 (노멀)','Buy a Conjurer Mantle (normal)'),'item':[]},   # 2:30 화면·2:50 노트
 {'id':'p1','kind':'act','group':'prep','pos':[0,1],'act':'transmute','cur':'Perfect_Orb_of_Transmutation','goal':K('매직','Magic'),'label':K('진화','Transmute'),'edges':[{'to':'p2'}],'item':[_JK('s')]},   # 3:35 자막, 3:56 화면 III 묶음
 {'id':'p2','kind':'act','group':'prep','pos':[0,2],'act':'augment','cur':'Perfect_Orb_of_Augmentation','goal':K('접두 정신력 1티어','T1 Spirit prefix'),'label':K('확장','Augment'),'show':['spirit'],
  'edges':[{'if':{'has':'spirit'},'to':'p3','res':'ok'},{'to':'p2x','res':'fail','label':K('빗나감 — 소멸','Miss: annul')}],'item':[_SP(),_JK('s')]},   # 3:23 노트 Step 1, 3:40~4:00 시연
 {'id':'p2x','kind':'act','group':'prep','pos':[1,2],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('옵션 1개 지우기','Remove one line'),'edges':[{'to':'p2','label':K('다시 확장','Augment again')}]},
 {'id':'hd','kind':'side','group':'prep','pos':[1,3],'attach':['p2','p3'],'cur':'Divine_Orb','goal':K('정신력 최대 수치, 선택·비용 미포함','Max-roll Spirit, optional, not costed'),'label':K('신성','Divine')},   # 3:23 노트 'Divine Orb it to max roll'
 {'id':'p3','kind':'act','group':'prep','pos':[0,3],'act':'regal','cur':'Perfect_Regal_Orb','goal':K('레어','Rare'),'label':K('제왕','Regal'),'edges':[{'to':'p4'}],'item':[_SP(),_JK('s'),_JK('x')]},   # 3:23 노트 'Regal orb', 4:30 화면 옵션 3개
 {'id':'p4','kind':'act','group':'prep','pos':[0,4],'act':'desecrate','cur':'Preserved_Rib','goal':K('네 번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),'showText':[K('훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],'label':K('훼손','Desecrate'),'edges':[{'to':'p5'}],
  'item':[_SP(),_JK('s'),_JK('x'),{'s':'s','kr':'훼손 옵션 (미공개)','en':'Desecrated (unrevealed)','m':'n'}]},   # 4:20 자막 '보존된 갈비뼈', 4:30 화면 미공개 훼손
 {'id':'p5','kind':'act','group':'prep','pos':[0,5],'act':'fracture','cur':'Fracturing_Orb','goal':K('분열 (셋 중 하나)','Fracture (one of three)'),'showText':[K('정신력이 분열되면 성공','Success when Spirit fractures')],'label':K('분열','Fracture'),
  'edges':[{'if':{'fractured':'spirit'},'to':'p6','res':'ok','label':K('정신력 분열','Spirit fractured')},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another line fractured')}],'item':[_SP('f')]},   # 3:23 노트, 4:40 반지 시연(흉갑 분열 장면은 없음)
 {'id':'xj','kind':'exit','group':'prep','pos':[1,5],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),'note':K('정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터','Another line fractured: start again on a new base')},
 {'id':'p6','kind':'cleanup','group':'prep','pos':[0,6],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':[_SP('f'),_JK('s')]}]   # 5:10~5:27 화면
_g['nodes']=_prep+[n for n in _g['nodes'] if n['id']!='h1']
_g['start']='h1'
json.dump(_g,open(_gp,'w'),ensure_ascii=False,indent=1)
