# Batch 19 (사용자 2026-11-10: 다음 2개) — 극한(5) → High-end (video) + Balance. Videos rechecked 2026-11-10 (transcripts).
#   grasping-mail-spell1-v2 (반지깎는노인 y5Ch3AJpl5c), mazbro-bis-chest-v2 (MazBro LUB59xlkNtk)
# Sim additions: condition junk:{side, tag} (a plain junk line: not fractured / desecrated, outside the tag), whittleSafe keepDes (a revealed desecrated line counts as kept).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch18.py').read(); exec(_src[:_src.index('# ---------- 1. SL 투사체')])
PT={'high':{'pT':1},'bal':{'pT':2}}
PG={'high':{'pT':1,'g':1},'bal':{'pT':2,'g':0}}
JK=lambda s,t: {'junk':{'side':s,'tag':t}}

# ---------- 1. 반지깎는노인 탐욕스러운 사슬옷 (y5Ch3AJpl5c) ----------
# 영상: 룬 아버지의 탐욕스러운 사슬옷(퀄리티 30% · 기폭제 퀄리티 30%) · 카오스 오브 약 22만 개로 모든 주문 스킬 +1 → 히네코라의 머리카락 4개로 확인하고 분열 (= 베이스)
# → 접미: 주문 치명타 피해 보너스 · 시전 속도 (영상은 방법을 안 보여 줌 — 카오스 오브 → 우측 찬미 + 완벽한 엑잘 → 빗나가면 절사로 가정)
# → 접두: 좌측 결정화 + 섬망의 에센스(주요 패시브 할당, 영상은 지배) → 접두 잡옵 → 아스트리드의 창의성 → 좌측 결정화 + 룬 합금(룬 수호 %, 1/2 — 영상은 한 번에)
# → 남은 접두 훼손(고대 갈비뼈) → 주문 피해 공개(빛의 징조로 다시). 기원의 나무 옵션은 가중치가 없어 일반 티어 평균으로 추정(xroll).
# 2026-11-12 영상 전체 대조(자막 0:00~12:40 + 화면 10:00~12:00, 메인 세션): 접미 두 옵션을 만드는 과정은 영상이 건너뜀(7:00 '2 hours later'), 11:00 '할당을 붙이고 접두 한 자리 추가 → 50:50으로 룬 합금'과 마지막 훼손 주문 피해는 그래프와 같음.
#   등급 C17: 밸런스 = 접미 하나 1~2티어, 마지막 접두(훼손)·접미는 랜덤 옵션.
tags={'spell':{'gi':140},'csd':{'gi':138,'tmax':'$pT'},'cs':{'gi':126,'tmax':'$pT'},'sd':{'gi':134,'tmax':'$pT'},'nt':{'gi':51},'rw':{'gi':57},
      'suf':{'anyOf':['csd','cs']},'keepS':{'anyOf':['csd','cs','spell']},'keepP':{'anyOf':['nt','rw','sd']}}
SPL=it('s','모든 주문 스킬 레벨 +1 (분열)','+1 to Level of all Spell Skills (fractured)',['spell'])
CSD=it('s','주문 치명타 피해 보너스 (26—29)% 증가','(26—29)% increased Critical Spell Damage Bonus',['csd']); CS=it('s','시전 속도 (22—24)% 증가','(22—24)% increased Cast Speed',['cs'])
NT=it('p','무작위 주요 패시브 스킬 할당 (섬망의 에센스)','Allocates a random Notable Passive Skill (Essence of Delirium)',['nt'],'c')
RW=it('p','룬 수호 (24—30)% 증가 (룬 합금)','(24—30)% increased Runic Ward (Runic Alloy)',['rw'],'c')
SD=it('p','주문 피해 (35—39)% 증가','(35—39)% increased Spell Damage',['sd'],'d'); AS=it('r','아스트리드의 창의성','Astrid’s Creativity',None,'r')
def RGM(vis):   # every step re-checks the item
    two={'any':[{'count':{'tag':'suf','min':2}},{'all':[{'param':{'g':0}},{'has':'suf'},{'full':'s'}]}]}
    return ROUTE_([{'if':{'all':[{'param':{'g':0}},two,{'has':'nt'},{'has':'rw'},{'full':'p'},{'not':{'unrev':True}}]},'to':'ok'},{'if':{'all':[{'not':two},{'not':{'has':'suf'}}]},'to':'c1'},
       {'if':{'all':[{'not':two},{'sideLt':{'side':'s','n':3}}]},'to':'s1'},{'if':{'not':two},'to':'w1'},
       {'if':{'unrevSide':'p'},'to':'rv'},{'if':{'all':[{'has':'nt'},{'has':'rw'},{'has':'sd'}]},'to':'ok'},
       {'if':{'des':True},'to':'rvx'},
       {'if':{'all':[{'not':{'has':'nt'}},JK('p','keepP')]},'to':'p1'},{'if':{'not':{'has':'nt'}},'to':'p0'},
       {'if':{'all':[{'not':{'has':'rw'}},JK('p','keepP')]},'to':'p3'},{'if':{'not':{'has':'rw'}},'to':'p2'},
       {'to':'d1'}],vis)
M0=[J('p'),SPL]; M1=[SPL,CSD]; M2=[SPL,CSD,CS]; M3=[J('p'),SPL,CSD,CS]; M4=[NT,SPL,CSD,CS]; M5=[NT,J('p'),SPL,CSD,CS]; M6=M5+[AS]
M7=[NT,RW,SPL,CSD,CS,AS]; M8=[NT,RW,UN('p'),SPL,CSD,CS,AS]; M9=[NT,RW,SD,SPL,CSD,CS,AS]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spell','fr':True},{'junk':'p'}]},K('모든 주문 스킬 레벨 +1 분열 + 잡옵 1개 (퀄리티 30% · 기폭제 퀄리티 30%)','Fractured +1 to all spell skills + one junk line (30% quality, 30% catalyst quality)'),M0),
 mark([0,0.6],'c1',M0),
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'suf'},'to':'s1','res':'ok'},{'to':'c1','res':'fail'}],M1,show=['csd','cs']),
 act('s1','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),RGM({'p0':'ok','w1':F}),M2,show=['csd','cs'],omens=['Omen_of_Dextral_Exaltation']),
 act('w1','main',[1,2],'chaos','Perfect_Chaos_Orb',K('접미 세번째 옵션','Third suffix'),None,K('카오스','Chaos'),RGM({'p0':'ok','s1':{'res':'fail'}}),M2,show=['csd','cs'],trim={'side':'s','keep':'keepS'}),
 act('p0','main',[0,3],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','잡옵','Junk')],K('엑잘','Exalt'),RGM({'p1':{}}),M3,omens=['Omen_of_Sinistral_Exaltation']),
 act('p1','main',[0,4],'essence','Essence_of_Delirium',K('잡옵을 지우고 무작위 주요 패시브 스킬 할당','The junk goes for Allocates a random Notable Passive Skill'),[st('p','무작위 주요 패시브 스킬 할당 (제작 옵션)','Allocates a random Notable Passive Skill (crafted)')],K('에센스','Essence'),
     ROUTE_([{'if':{'not':{'has':'rw'}},'to':'p2'}],{'p2':{}})+RGM({}),M4,ess='nt',omens=['Omen_of_Sinistral_Crystallisation']),
 act('p2','main',[0,5],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','잡옵','Junk')],K('엑잘','Exalt'),
     ROUTE_([{'if':{'not':{'has':'rw'}},'to':'r1'}],{'r1':{}})+RGM({}),M5,omens=['Omen_of_Sinistral_Exaltation']),
 act('r1','main',[0,6],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':'p3'}],M6,rune=K('아스트리드의 창의성','Astrid’s Creativity')),
 act('p3','main',[0,7],'essence','Runic_Alloy',K('잡옵을 지우고 룬 수호 (24—30)% 증가','The junk goes for (24—30)% increased Runic Ward'),[st('p','룬 수호 (24—30)% 증가 (제작 옵션)','(24—30)% increased Runic Ward (crafted)')],K('합금','Alloy'),RGM({'d1':'ok','p1':F}),M7,ess='rw',omens=['Omen_of_Sinistral_Crystallisation']),
 act('d1','main',[0,8],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RGM({'rv':{}}),M8,omens=['Omen_of_Sinistral_Necromancy']),
 act('rv','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),RGM({'ok':'ok','rvx':F}),M9,want='sd',show=['sd'],omens=['Omen_of_Abyssal_Echoes']),
 annul('rvx',[1,9],RGM({'d1':{'port':'right'}})),
 done([0,10])]
nodes[0]['start']['quality']=30
GEN=['Genesis Tree Caster','Genesis Tree Minion']
graph11('grasping-mail-spell1-v2','Grasping_Mail_ring',"Runefather's Grasping Mail",82,
  '반지깎는노인 탐욕스러운 사슬옷(y5Ch3AJpl5c) — 모든 주문 스킬 +1 분열 + 잡옵(카오스 오브 약 22만 개 + 히네코라의 머리카락 4개, 베이스) → 접미 주문 치명타 피해 보너스 · 시전 속도(영상은 방법 생략: 카오스 오브 → 우측 찬미 + 완벽한 엑잘 → 절사로 가정) → 좌측 결정화 + 섬망의 에센스(주요 패시브 할당) → 접두 잡옵 → 아스트리드의 창의성 → 좌측 결정화 + 룬 합금(1/2) → 고대 갈비뼈 → 주문 피해 공개(빛의 징조로 다시). 기원의 나무 옵션 가중치는 추정.',
  {'pT':{'kr':'목표 티어','en':'Target tier','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'g':{'kr':'마지막 접두·접미','en':'Last prefix and suffix','values':TV({'1':('목표 옵션까지 반복','Repeat until the wanted line'),'0':('랜덤 옵션','Random line')})}},PG,
  {'high':K('영상: 주문 치명타 피해 · 시전 속도 · 주문 피해 1티어','Video: T1 spell crit damage, cast speed and spell damage'),'bal':K('접미 하나 1~2티어, 마지막 접두(훼손)·접미는 랜덤 옵션','One suffix T1–2, the last prefix (desecrated) and suffix random')},tags,nodes,
  [{'id':'L1','nodes':['d1','rv','rvx'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'nt','ess':True},{'tag':'rw','ess':True},{'tag':'sd','tmax':1,'des':True},{'tag':'spell','fr':True},{'tag':'csd','tmax':1},{'tag':'cs','tmax':1}] if v=='high' else
      [{'tag':'nt','ess':True},{'tag':'rw','ess':True},{'side':'p','random':True},{'tag':'spell','fr':True},{'side':'s','label':K('주문 치명타 피해·시전 속도 1~2티어','T1–2 spell crit damage or cast speed')},{'side':'s','random':True}]),
  {'quality':30,'sockets':2},{'all':[{'has':'nt'},{'has':'rw'},{'any':[{'all':[{'count':{'tag':'suf','min':2}},{'has':'sd'}]},{'all':[{'param':{'g':0}},{'has':'suf'},{'full':'s'},{'full':'p'}]}]}]},('high','bal'),xsub=GEN,xroll=True)
_g=json.load(open(f'{H}/grasping-mail-spell1-v2.json')); _g['basePrice']={'Chaos_Orb':220000}; json.dump(_g,open(f'{H}/grasping-mail-spell1-v2.json','w'),ensure_ascii=False,indent=1)   # 분열 베이스 = 영상의 카오스 약 22만 개(사용자 확정 2026-11-12: 비싸게 보여도 포함)

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
#   두 옵션만 받는 시뮬(시험 1500회)은 평균 약 6,900 div, 셋 중 둘은 약 3,300 div.
P1={'high':{}}
tags={'spirit':{'gi':15,'tmax':1},'isp':{'gi':53},'ima':{'gi':52},'hf':{'gi':56},'hc':{'gi':57},'sre':{'gi':23},
      'mkS':{'gi':47},
      **{f'b{g}':{'gi':g} for g in (0,1,2,3,4,5,11,12,14,16,17,18,19,20,21,22,24,25,27,28,29,30,31,54,55)},
      'blk':{'anyOf':[f'b{g}' for g in (0,1,2,3,4,5,11,12,14,16,17,18,19,20,21,22,24,25,27,28,29,30,31,54,55)],'label':K('자리 막기 옵션','Blocker line')},   # 공개에서 고를 막기 옵션 = 목표 복합 저항·마지막 훼손 옵션 밖의 접미(공개 풀에 메드베드 옵션도 있음)
      'hl':{'gi':58},'good':{'anyOf':['hf','hc','hl'],'label':K('원소 및 카오스 복합 저항','Elemental and chaos hybrid resistances')},
      'keepW':{'anyOf':['isp','ima','hf','hc','hl'],'label':K('남길 옵션','Lines to keep')}}
DONE={'count':{'tag':'good','min':2}}   # 영상은 복합 저항 셋 중 둘이면 됨(17:00·19:30 번개·카오스도 '원하는 것') — 카드·상자 글은 성공 회차의 두 옵션
L_=lambda kr,en: {'label':K(kr,en)}
F={'res':'fail'}
def RM(vis):   # 접미 반복(접힌 상자)과 공개 뒤: 아이템 상태로 다음 상자
    return ROUTE_([{'if':{'all':[DONE,{'des':True}]},'to':'f1'},
       {'if':{'all':[DONE,{'sideLt':{'side':'s','n':3}}]},'to':'f2'},
       {'if':DONE,'to':'da'},
       {'if':{'all':[{'not':{'des':True}},{'not':{'unrevSide':'s'}}]},'to':'mA'},
       {'if':{'sideLt':{'side':'s','n':3}},'to':'s1'},
       {'if':{'all':[{'has':'good'},{'whittleSafe':{'tag':'keepW','keepDes':True}}]},'to':'w1'},
       {'to':'da'}],vis)
SPR=it('p','정신력 +(57—61) (분열)','+(57—61) to Spirit (fractured)',['spirit'],'f'); MD=it('r','메드베드의 보살핌','Medved’s Tending',None,'r')
ISP=it('p','정신력 (1—20)% 증가','(1—20)% increased Spirit',['isp']); IMA=it('p','마나 최대치 (1—20)% 증가','(1—20)% increased maximum Mana',['ima'])
HF=it('s','화염 및 카오스 저항 +(3—31)%','+(3—31)% to Fire and Chaos Resistances',['hf']); HC=it('s','냉기 및 카오스 저항 +(3—31)%','+(3—31)% to Cold and Chaos Resistances',['hc'])
MKS=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mkS'],'c')
LRB=it('s','초당 생명력 재생 (훼손, 자리 막기)','Life Regeneration per second (desecrated, blocker)',None,'d')
FRB=it('s','화염 저항 (훼손, 자리 막기)','Fire Resistance (desecrated, blocker)',None,'d')
SRE=it('s','스킬의 정신력 점유 효율 (6—12)% 증가','(6—12)% increased Spirit Reservation Efficiency of Skills',['sre'],'d')
B0=[SPR,J('s')]; B1=B0+[MD]; B2=[SPR,ISP,MD]; B3=[SPR,ISP,IMA,MD]; B4=B3[:3]+[J('s'),MD]; B5=B3[:3]+[MKS,MD]; B6=B3[:3]+[UN('s'),MD]; B7=B3[:3]+[LRB,MD]
BL=B3[:3]+[HF,HC,FRB,MD]; B9=B3[:3]+[HF,HC,MD]; B10=B3[:3]+[HF,HC,UN('s'),MD]; B11=B3[:3]+[HF,HC,SRE,MD]
nodes=[
 mark([0,0.6],'r1',B0),
 act('r1','main',[0,1],'rune',None,K('메드베드의 보살핌 장착','Socket Medved’s Tending'),[st(None,'영혼 핵 옵션이 붙을 수 있음','Soul core lines can roll')],K('룬','Rune'),[{'to':'c1'}],B1,rune=K('메드베드의 보살핌','Medved’s Tending')),   # 5:40 화면 '제거·교체 불가' 확인 창
 act('c1','main',[0,2],'chaos','Chaos_Orb',K('접두 정신력 % 증가','Prefix % increased Spirit'),None,K('카오스','Chaos'),[{'if':{'has':'isp'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],B2,show=['isp']),   # 6:28 화면 정신력 11%
 act('e1','main',[0,3],'exalt','Greater_Exalted_Orb',K('접두 마나 최대치 % 증가','Prefix % increased maximum Mana'),None,K('엑잘','Exalt'),
     [{'if':{'has':'ima'},'to':'s0','res':'ok'},{'to':'e1x',**F,**L_('빗나감 — 소멸','Miss: annul')}],B3,show=['ima'],omens=['Omen_of_Sinistral_Exaltation']),   # 6:38 상위 엑잘(47 → 46), 7:00 자막
 annul('e1x',[1,3],[{'if':{'not':{'has':'isp'}},'to':'c1',**F,**L_('정신력 %가 지워짐 — 카오스부터','% Spirit gone: back to Chaos')},{'to':'e1','res':'ok',**L_('다시 엑잘','Exalt again')}],
       omens=(),target=K('반반 — 빗나간 접두가 지워지길','50/50: hoping the missed prefix goes')),   # 6:44 '50/50'
 act('s0','main',[0,4],'exalt','Greater_Exalted_Orb',K('접미 첫번째 옵션','First suffix'),[st('s','잡옵 (초당 생명력 재생)','Junk (life regeneration per second)')],K('엑잘','Exalt'),[{'to':'mA'}],B4),   # 12:46 화면 생명력 재생 2티어
 act('mA','main',[0,5],'essence','Essence_of_the_Abyss',K('접미 잡옵을 지우고 심연의 군주의 징표','The junk suffix goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('에센스','Essence'),[{'to':'b2'}],B5,
     ess='mkS',mark=True,omens=['Omen_of_Dextral_Crystallisation'],skipIf={'not':{'junk':{'side':'s','tag':'good'}}},skipTo='b2',skipHide=True),   # 13:04 화면 징표, 12:58 우측 결정화 툴팁
 act('b2','main',[0,6],'desecrate','Preserved_Rib',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),
     [{'if':{'not':{'unrevSide':'s'}},'to':'b2n',**L_('징표 없음 — 빈자리에 훼손','No Mark: desecrate the open slot')},{'to':'b3'}],B6,
     fromMark=True,skipIf={'not':{'has':'mkS'}},skipTo='b2n',skipHide=True),   # 징표가 없으면 건너뜀 — 그 통과 수가 b2 → b2n 선에 붙음   # 10:30 자막 '보존된 갈비뼈', 13:36 가방 II 뼈
 act('b2n','main',[1,6],'desecrate','Preserved_Rib',K('접미 빈자리 훼손','Desecrate the open suffix'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'b3'}],B6,omens=['Omen_of_Dextral_Necromancy']),   # 30:58~31:04 두 번째 흉갑 '막기 먼저 훼손'(접미 빈자리), 첫 흉갑 성공 회차에는 없음
 act('b3','main',[0,7],'reveal',None,K('자리 막기 옵션 확인','Reveal the blocker'),[st('s','초당 생명력 재생','Life Regeneration per second')],K('공개','Reveal'),RM({'s1':{}}),B7,want='blk',omens=['Omen_of_Abyssal_Echoes']),   # 13:38~13:43 화면 공개 2번(메아리), 생명력 재생 선택
 act('s1','main',[0,8],'exalt','Perfect_Exalted_Orb',K('접미 화염·카오스 저항 + 냉기·카오스 저항','Suffix fire and chaos + cold and chaos resistances'),None,K('엑잘','Exalt'),RM({'f1':'ok','w1':F,'da':F}),BL,show=['hf','hc'],omens=['Omen_of_Greater_Exaltation']),   # 14:30·23:47 상위 찬미 + 완벽한 엑잘
 act('w1','main',[1,8],'chaos','Perfect_Chaos_Orb',K('가장 낮은 잡옵을 다시','Reroll the lowest junk line'),None,K('카오스','Chaos'),RM({'f1':'ok','s1':F}),BL,show=['hf','hc'],omens=['Omen_of_Whittling']),   # 18:10·24:36~24:42 절사
 annul('da',[2,8],RM({'s1':{'res':'ok'},'mA':F}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 지우기','Remove a junk suffix')),   # 15:00 빛의 징조를 끄고 우측 소멸
 annul('f1',[0,9],[{'to':'f2'}],target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),   # 26:40 빛의 징조로 화염 저항 제거
 act('f2','main',[0,10],'desecrate','Ancient_Rib',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'f3'}],B10),   # 26:30 자막 '고대 갈비뼈 14개'
 act('f3','main',[0,11],'reveal',None,K('접미 정신력 점유 효율','Suffix Spirit Reservation Efficiency'),None,K('공개','Reveal'),[{'if':{'added':'sre'},'to':'ok','res':'ok'},{'to':'f3x',**F}],B11,want='sre',show=['sre'],omens=['Omen_of_Abyssal_Echoes']),   # 27:30 화면 6% 선택
 annul('f3x',[1,11],[{'to':'f2',**L_('다시 훼손','Desecrate again')}]),   # 27:05~27:28 빛의 징조 + 소멸 반복
 done([0,12])]
graph11('mazbro-bis-chest-v2','Body_Armours_str_int','Conjurer Mantle',82,
  'MazBro BiS 갑옷(LUB59xlkNtk, 2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 요술사 외투 → 완벽한 진화·확장·소멸로 정신력 1티어 → 제왕 → 보존된 갈비뼈 → 분열(1/3) → 소멸로 분열 + 옵션 1개 → 메드베드의 보살핌 → 카오스 오브(정신력 %) → 좌측 찬미 + 상위 엑잘(마나 %, 빗나가면 소멸의 오브) → 상위 엑잘(접미 잡옵) → 우측 결정화 + 심연의 에센스 → 보존된 갈비뼈 → 공개(자리 막기) → 상위 찬미 + 완벽한 엑잘·절사 + 완벽한 카오스·우측 소멸 반복(화염·카오스 + 냉기·카오스) → 빛의 징조로 막기 제거 → 고대 갈비뼈 → 정신력 점유 효율 공개. 메드베드 옵션 가중치는 추정. 신성한 오브·축복받은 자의 징조·유동체는 뺌.',
  {},P1,{'high':K('영상: 복합 저항 2개 + 정신력 점유 효율','Video: two hybrid resistances + Spirit reservation efficiency')},tags,nodes,
  [{'id':'L1','nodes':['s1','w1','da'],'kr':'접미 복합 저항','en':'Hybrid resistance suffixes',
    'fold':True,'goal':K('접미 화염·카오스 저항 + 냉기·카오스 저항','Fire and chaos + cold and chaos resistance suffixes'),
    'steps':[{**K('상위 찬미의 징조 + 완벽한 엑잘티드 오브로 접미 2개','Omen of Greater Exaltation + Perfect Exalted Orb for two suffixes'),'node':'s1'},
             {**K('복합 저항이 있고 가장 낮은 옵션이 잡옵이면 절사의 징조 + 완벽한 카오스 오브','A hybrid on and the lowest line is junk: Omen of Whittling + Perfect Chaos Orb'),'node':'w1'},
             {**K('아니면 우측 소멸의 징조 + 소멸의 오브로 접미 잡옵 지우기','Otherwise Omen of Dextral Annulment + Orb of Annulment on a junk suffix'),'node':'da'}],
    'worst':{**K('자리 막기 훼손이 지워지면 심연의 에센스 단계부터','Blocker gone: back to the Essence of the Abyss step'),'to':'mA'},
    'item':BL},
   {'id':'L2','nodes':['f2','f3','f3x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high',),lambda v:[{'tag':'spirit','fr':True},{'tag':'isp'},{'tag':'ima'},{'tag':'hf'},{'tag':'hc'},{'tag':'sre','des':True}]),
  {'sockets':2},{'all':[DONE,{'has':'isp'},{'has':'ima'},{'has':'sre'}]},('high',),xsub=["Medved's Tending"],xroll=True)
_gp=f"{H}/mazbro-bis-chest-v2.json"; _g=json.load(open(_gp))
for _n in _g['nodes']:
    if _n.get('group')=='main': _n['pos']=[_n['pos'][0], _n['pos'][1]+8.4]
_g['basePrice']={'Chaos_Orb':1}   # 2:50 노트 'Conjurer Mantle Cloak … 1 Chaos'
_SP=lambda m='n': {'s':'p','kr':'정신력 +(57—61)','en':'+(57—61) to Spirit','m':m,'tags':['spirit']}
_JK=lambda s: {'s':s,'kr':'잡옵','en':'Junk','m':'j'}
_prep=[
 {'id':'h1','kind':'base','group':'prep','pos':[0,0],'next':'p1','start':{'rar':'normal','mods':[]},'label':K('요술사 외투 구입 (노멀)','Buy a Conjurer Mantle (normal)'),'item':[]},   # 2:30 화면·2:50 노트
 {'id':'p1','kind':'act','group':'prep','pos':[0,1],'act':'transmute','cur':'Perfect_Orb_of_Transmutation','goal':K('매직','Magic'),'label':K('진화','Transmute'),'edges':[{'to':'p2'}],'item':[_JK('s')]},   # 3:35 자막, 3:56 화면 III 묶음
 {'id':'p2','kind':'act','group':'prep','pos':[0,2],'act':'augment','cur':'Perfect_Orb_of_Augmentation','goal':K('접두 정신력 1티어','T1 Spirit prefix'),'label':K('확장','Augment'),'show':['spirit'],
  'edges':[{'if':{'has':'spirit'},'to':'p3','res':'ok'},{'to':'p2x','res':'fail','label':K('빗나감 — 소멸','Miss: annul')}],'item':[_SP(),_JK('s')]},   # 3:23 노트 Step 1, 3:40~4:00 시연
 {'id':'p2x','kind':'act','group':'prep','pos':[1,2],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('옵션 1개 지우기','Remove one line'),'edges':[{'to':'p2','label':K('다시 확장','Augment again')}]},
 {'id':'hd','kind':'side','group':'prep','pos':[1,3],'attach':['p2','p3'],'cur':'Divine_Orb','goal':K('정신력 최대 수치, 선택·비용 미포함','Max-roll Spirit, optional, not costed'),'label':K('신성','Divine')},   # 3:23 노트 'Divine Orb it to max roll'
 {'id':'p3','kind':'act','group':'prep','pos':[0,3],'act':'regal','cur':'Perfect_Regal_Orb','goal':K('레어','Rare'),'label':K('제왕','Regal'),'edges':[{'to':'p4'}],'item':[_SP(),_JK('s'),_JK('x')]},   # 3:23 노트 'Regal orb', 4:30 화면 옵션 3개
 {'id':'p4','kind':'act','group':'prep','pos':[0,4],'act':'desecrate','cur':'Preserved_Rib','goal':K('네번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),'showText':[K('훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],'label':K('훼손','Desecrate'),'edges':[{'to':'p5'}],
  'item':[_SP(),_JK('s'),_JK('x'),{'s':'s','kr':'훼손 옵션 (미공개)','en':'Desecrated (unrevealed)','m':'n'}]},   # 4:20 자막 '보존된 갈비뼈', 4:30 화면 미공개 훼손
 {'id':'p5','kind':'act','group':'prep','pos':[0,5],'act':'fracture','cur':'Fracturing_Orb','goal':K('분열 (셋 중 하나)','Fracture (one of three)'),'showText':[K('정신력이 분열되면 성공','Success when Spirit fractures')],'label':K('분열','Fracture'),
  'edges':[{'if':{'fractured':'spirit'},'to':'p6','res':'ok','label':K('정신력 분열','Spirit fractured')},{'to':'xj','res':'fail','dash':True,'label':K('다른 옵션 분열','Another line fractured')}],'item':[_SP('f')]},   # 3:23 노트, 4:40 반지 시연(흉갑 분열 장면은 없음)
 {'id':'xj','kind':'exit','group':'prep','pos':[1,5],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),'note':K('정신력이 아닌 옵션이 분열되면 새 베이스로 처음부터','Another line fractured: start again on a new base')},
 {'id':'p6','kind':'cleanup','group':'prep','pos':[0,6],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':[_SP('f'),_JK('s')]}]   # 5:10~5:27 화면
_g['nodes']=_prep+[n for n in _g['nodes'] if n['id']!='h1']
_g['start']='h1'
json.dump(_g,open(_gp,'w'),ensure_ascii=False,indent=1)
