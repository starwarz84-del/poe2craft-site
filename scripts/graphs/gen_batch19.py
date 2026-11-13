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
 act('c1','main',[0,1],'chaos','Chaos_Orb',K('접미 두 번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'suf'},'to':'s1','res':'ok'},{'to':'c1','res':'fail'}],M1,show=['csd','cs']),
 act('s1','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 세 번째 옵션','Third suffix'),None,K('엑잘','Exalt'),RGM({'p0':'ok','w1':F}),M2,show=['csd','cs'],omens=['Omen_of_Dextral_Exaltation']),
 act('w1','main',[1,2],'chaos','Perfect_Chaos_Orb',K('접미 세 번째 옵션','Third suffix'),None,K('카오스','Chaos'),RGM({'p0':'ok','s1':{'res':'fail'}}),M2,show=['csd','cs'],trim={'side':'s','keep':'keepS'}),
 act('p0','main',[0,3],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','잡옵','Junk')],K('엑잘','Exalt'),RGM({'p1':{}}),M3,omens=['Omen_of_Sinistral_Exaltation']),
 act('p1','main',[0,4],'essence','Essence_of_Delirium',K('잡옵을 지우고 무작위 주요 패시브 스킬 할당','The junk goes for Allocates a random Notable Passive Skill'),[st('p','무작위 주요 패시브 스킬 할당 (제작 옵션)','Allocates a random Notable Passive Skill (crafted)')],K('에센스','Essence'),
     ROUTE_([{'if':{'not':{'has':'rw'}},'to':'p2'}],{'p2':{}})+RGM({}),M4,ess='nt',omens=['Omen_of_Sinistral_Crystallisation']),
 act('p2','main',[0,5],'exalt','Exalted_Orb',K('접두 잡옵','A junk prefix'),[st('p','잡옵','Junk')],K('엑잘','Exalt'),
     ROUTE_([{'if':{'not':{'has':'rw'}},'to':'r1'}],{'r1':{}})+RGM({}),M5,omens=['Omen_of_Sinistral_Exaltation']),
 act('r1','main',[0,6],'rune',None,K('아스트리드의 창의성 장착','Socket Astrid’s Creativity'),[st(None,'제작 옵션 하나 더','One more crafted modifier')],K('룬','Rune'),[{'to':'p3'}],M6,rune=K('아스트리드의 창의성','Astrid’s Creativity')),
 act('p3','main',[0,7],'essence','Runic_Alloy',K('잡옵을 지우고 룬 수호 (24—30)% 증가','The junk goes for (24—30)% increased Runic Ward'),[st('p','룬 수호 (24—30)% 증가 (제작 옵션)','(24—30)% increased Runic Ward (crafted)')],K('합금','Alloy'),RGM({'d1':'ok','p1':F}),M7,ess='rw',omens=['Omen_of_Sinistral_Crystallisation']),
 act('d1','main',[0,8],'desecrate','Ancient_Rib',K('접두 세 번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RGM({'rv':{}}),M8,omens=['Omen_of_Sinistral_Necromancy']),
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
import subprocess, sys as _sys; subprocess.run([_sys.executable, f'{H}/gen_grasping_mail_spell1.py'], check=True)   # 2026-11-13: 이 아이템은 gen_grasping_mail_spell1.py가 만듦 — 위 결과를 새 생성기로 덮어씀

# ---------- 2. MazBro BiS 갑옷 (LUB59xlkNtk) ----------
# 2026-11-13 D1: 전용 생성기 gen_mazbro_bis_chest.py로 옮김(하이엔드·밸런스)
subprocess.run([_sys.executable, f'{H}/gen_mazbro_bis_chest.py'], check=True)
