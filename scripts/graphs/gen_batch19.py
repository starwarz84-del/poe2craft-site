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
# 영상: 요술사 외투 정신력 1티어 분열 + 잡옵 → 메드베드의 보살핌(영혼 핵) → 카오스 오브(정신력 % 또는 마나 %) → 좌측 찬미 + 엑잘(남은 하나, 빗나가면 소멸의 오브 50/50 — 영상 뒷부분: 완벽한 엑잘 권장)
# → 접미: 첫 엑잘 → 잡옵이면 우측 결정화 + 심연의 에센스(징표) → 보존된 갈비뼈로 징표 훼손 → 공개(가중치 높은 잡옵으로 자리 막기 — 받는 피해를 마나로·정신력 효율이 뜨면 그대로)
#   → 상위 찬미 + 완벽한 엑잘(복합 저항) → 잡옵이 가장 낮으면 절사의 징조 + 완벽한 카오스 오브, 아니면 우측 소멸의 징조 + 소멸의 오브(1/3) — 막기 훼손이 지워지면 심연의 에센스부터
# → 빛의 징조 + 소멸의 오브로 막기 제거 → 고대 갈비뼈(우측 강령술) → 받는 피해를 마나로 또는 정신력 점유 효율 공개(빛의 징조로 다시). 신성한 오브 · 축복받은 자의 징조 · 유동체는 뺌(정책 23).
# 하이엔드 = 영상(메드베드 복합 저항 2개), 밸런스 = 영상 중간 "여기서 끝내도 됨": 복합 저항 1개 + 일반 원소 저항 1티어.
tags={'spirit':{'gi':15,'tmax':1},'isp':{'gi':53},'ima':{'gi':52},'hf':{'gi':56},'hc':{'gi':57},'hl':{'gi':58},'rf':{'gi':2,'tmax':1},'rc':{'gi':3,'tmax':1},'rl':{'gi':4,'tmax':1},
      'mbl':{'gi':26},'sre':{'gi':23},'mkS':{'gi':None},
      'pre':{'anyOf':['isp','ima']},'hyb':{'anyOf':['hf','hc','hl']},'nres':{'anyOf':['rf','rc','rl']},'fin':{'anyOf':['mbl','sre']},
      'sgood':{'anyOf':['hyb','nres']},'keepS':{'anyOf':['hyb','nres','fin']},'keepW':{'anyOf':['pre','hyb','nres','fin']}}
_cd=json.load(open(f'{H}/../../site/data/c/Body_Armours_str_int.json'))
tags['mkS']={'gi':next(i for i,g in enumerate(_cd['groups']) if g['s']=='e' and g['g']=='s' and 'Abyssal' in ' '.join(x[5] for x in g['t']))}
V1={'param':{'pT':1}}; V2={'param':{'pT':2}}
DONE={'any':[{'all':[V1,{'count':{'tag':'hyb','min':2}}]},{'all':[V2,{'has':'hyb'},{'count':{'tag':'sgood','min':2}}]}]}
SJ=JK('s','sgood')
def RM(vis):   # every step re-checks the item
    two={'count':{'tag':'pre','min':2}}
    return ROUTE_([{'if':{'not':{'has':'pre'}},'to':'c1'},{'if':{'all':[{'not':two},{'sideLt':{'side':'p','n':3}}]},'to':'e1'},{'if':{'not':two},'to':'e1x'},
       {'if':{'all':[{'has':'fin'},DONE]},'to':'ok'},{'if':{'all':[{'unrevSide':'s'},DONE]},'to':'f3'},{'if':{'unrevSide':'s'},'to':'b3'},
       {'if':{'has':'mkS'},'to':'b2'},{'if':{'all':[DONE,{'des':True}]},'to':'f1'},
       {'if':{'all':[DONE,SJ,{'whittleSafe':{'tag':'keepW','keepDes':True}}]},'to':'w1'},{'if':{'all':[DONE,SJ]},'to':'da'},{'if':DONE,'to':'f2'},
       {'if':{'all':[{'des':False},SJ]},'to':'mA'},{'if':{'all':[{'des':False},{'sideLt':{'side':'s','n':1}}]},'to':'s0'},{'if':{'des':False},'to':'b2n'},
       {'if':{'sideLt':{'side':'s','n':3}},'to':'s1'},{'if':{'whittleSafe':{'tag':'keepW','keepDes':True}},'to':'w1'},{'to':'da'}],vis)
SPR=it('p','정신력 +(57—61) (분열)','+(57—61) to Spirit (fractured)',['spirit']); MD=it('r','메드베드의 보살핌','Medved’s Tending',None,'r')
ISP=it('p','정신력 (1—20)% 증가','(1—20)% increased Spirit',['isp']); IMA=it('p','마나 최대치 (1—20)% 증가','(1—20)% increased maximum Mana',['ima'])
HC=it('s','냉기 및 카오스 저항 +(3—31)%','+(3—31)% to Cold and Chaos Resistances',['hc']); HL=it('s','번개 및 카오스 저항 +(3—31)%','+(3—31)% to Lightning and Chaos Resistances',['hl'])
MKS=it('s','심연의 군주의 징표','Mark of the Abyssal Lord',['mkS'],'c'); BLK=it('s','초당 생명력 재생 (훼손, 자리 막기)','Life Regeneration per second (desecrated, blocker)',None,'d')
SRE=it('s','스킬의 정신력 점유 효율 (6—12)% 증가','(6—12)% increased Spirit Reservation Efficiency of Skills',['sre'],'d')
B0=[SPR,J('s')]; B1=B0+[MD]; B2=[SPR,ISP,MD]; B3=[SPR,ISP,IMA,MD]; B4=B3[:3]+[J('s'),MD]; B5=B3[:3]+[MKS,MD]; B6=B3[:3]+[UN('s'),MD]; B7=B3[:3]+[BLK,MD]
B8=B3[:3]+[HC,J('s'),BLK,MD]; B9=B3[:3]+[HC,HL,BLK,MD]; B10=B3[:3]+[HC,HL,MD]; B11=B3[:3]+[HC,HL,UN('s'),MD]; B12=B3[:3]+[HC,HL,SRE,MD]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},{'junk':'s'}]},K('정신력 1티어 분열 + 잡옵 1개','Fractured T1 Spirit + one junk line'),B0),
 mark([0,0.6],'r1',B0),
 act('r1','main',[0,1],'rune',None,K('메드베드의 보살핌 장착','Socket Medved’s Tending'),[st(None,'영혼 핵 옵션','Soul core modifiers')],K('영혼 핵','Soul core'),[{'to':'c1'}],B1,rune=K('메드베드의 보살핌','Medved’s Tending')),
 act('c1','main',[0,2],'chaos','Chaos_Orb',K('접두 두번째 옵션','Second prefix'),None,K('카오스','Chaos'),[{'if':{'has':'pre'},'to':'e1','res':'ok'},{'to':'c1','res':'fail'}],B2,show=['isp','ima']),
 act('e1','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),RM({'s0':'ok','e1x':F}),B3,show=['isp','ima'],omens=['Omen_of_Sinistral_Exaltation']),
 annul('e1x',[1,3],RM({'e1':{'res':'ok','port':'right'},'c1':{'res':'fail'}}),omens=(),target=K('접두 잡옵 지우기','Remove the junk prefix')),
 act('s0','main',[0,4],'exalt','Greater_Exalted_Orb',K('접미 첫번째 옵션','First suffix'),None,K('엑잘','Exalt'),RM({'mA':F,'b2n':'ok'}),B4,show=['hf','hc','hl']),
 act('mA','main',[1,4],'essence','Essence_of_the_Abyss',K('접미 옵션을 지우고 심연의 군주의 징표','A suffix goes for the Mark of the Abyssal Lord'),[st('s','심연의 군주의 징표','Mark of the Abyssal Lord')],K('심연','Abyss'),RM({'b2':{}}),B5,ess='mkS',mark=True,omens=['Omen_of_Dextral_Crystallisation']),
 act('b2','main',[1,5],'desecrate','Preserved_Rib',K('접미 징표 훼손','Desecrate the suffix Mark'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RM({'b3':{}}),B6,fromMark=True),
 act('b2n','main',[2,5],'desecrate','Preserved_Rib',K('접미 빈자리 훼손','Desecrate the open suffix'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RM({'b3':{}}),B6,omens=['Omen_of_Dextral_Necromancy']),
 act('b3','main',[1,6],'reveal',None,K('자리 막기 옵션 확인','Reveal the blocker'),None,K('공개','Reveal'),RM({'s1':{}}),B7,want='fin',show=['fin'],omens=['Omen_of_Abyssal_Echoes']),
 act('s1','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접미 복합 저항 옵션','Suffix hybrid resistances'),None,K('엑잘','Exalt'),RM({'f1':'ok','w1':F,'da':F}),B8,show=['hf','hc','hl','rf','rc','rl'],omens=['Omen_of_Greater_Exaltation'],
     showIf=[{'param':{'pT':1},'show':['hf','hc','hl']}]),
 act('w1','main',[1,7],'chaos','Perfect_Chaos_Orb',K('가장 낮은 잡옵을 다시','Reroll the lowest junk line'),None,K('카오스','Chaos'),RM({'f1':'ok','s1':{'res':'fail'}}),B8,show=['hf','hc','hl'],omens=['Omen_of_Whittling']),
 annul('da',[2,7],RM({'s1':{'res':'ok'},'mA':{'res':'fail'}}),omens=('Omen_of_Dextral_Annulment',),target=K('접미 잡옵 지우기','Remove the junk suffix')),
 annul('f1',[0,8],RM({'f2':{}}),target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),
 act('f2','main',[0,9],'desecrate','Ancient_Rib',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),RM({'f3':{}}),B11,omens=['Omen_of_Dextral_Necromancy']),
 act('f3','main',[0,10],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'fin'},'to':'ok','res':'ok'},{'to':'f3x',**F}],B12,want='fin',show=['mbl','sre'],omens=['Omen_of_Abyssal_Echoes']),
 annul('f3x',[1,10],RM({'f2':{'port':'right'}})),
 done([0,11])]
graph11('mazbro-bis-chest-v2','Body_Armours_str_int','Conjurer Mantle',82,
  'MazBro BiS 갑옷(LUB59xlkNtk) — 정신력 1티어 분열 + 잡옵 → 메드베드의 보살핌 → 카오스 오브(정신력 % 또는 마나 %) → 좌측 찬미 + 완벽한 엑잘(빗나가면 소멸의 오브) → 접미 첫 엑잘 → 우측 결정화 + 심연의 에센스 → 보존된 갈비뼈로 징표 훼손 → 자리 막기 공개 → 상위 찬미 + 완벽한 엑잘(복합 저항) → 절사의 징조 + 완벽한 카오스 오브 또는 우측 소멸의 징조 + 소멸의 오브 → 빛의 징조로 막기 제거 → 고대 갈비뼈 → 받는 피해를 마나로·정신력 점유 효율 공개. 하이엔드 = 영상(복합 저항 2개), 밸런스 = 복합 저항 1개 + 원소 저항 1티어(영상 중간 판단). 메드베드 옵션 가중치는 추정.',
  {'pT':{'kr':'접미 저항','en':'Suffix resistances','values':TV({'1':('복합 저항 2개','Two hybrids'),'2':('복합 저항 + 원소 저항 1티어','Hybrid + T1 resistance')})}},PT,
  {'high':K('영상: 메드베드 복합 저항 2개','Video: two Medved hybrid resistances'),'bal':K('복합 저항 1개 + 원소 저항 1티어','One hybrid + a T1 resistance')},tags,nodes,
  [{'id':'L1','nodes':['f2','f3','f3x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['mA','b2','b3'],'kr':'자리 막기','en':'Block'}],
  FIN(('high','bal'),lambda v:[{'tag':'spirit','fr':True},{'tag':'isp'},{'tag':'ima'},{'tag':'hc'},{'tag':'hl'} if v=='high' else {'tag':'rf'},{'tag':'sre','des':True}]),
  {'quality':20,'sockets':2},{'all':[DONE,{'count':{'tag':'pre','min':2}},{'has':'fin'}]},('high','bal'),xsub=["Medved's Tending"],xroll=True)
