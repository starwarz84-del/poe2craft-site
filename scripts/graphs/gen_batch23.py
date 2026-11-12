# Batch 23 (사용자 2026-11-11: "EasyBabi·SL 게임연구소 최근 제작 영상 추가" — 등록 안 된 제작 영상만, 정책 31 플로우차트 먼저)
#   easybabi-spiny-talisman-v2 (fabBIuR6yhw, 아스트리드의 창의성 무도 무기), sl-blacksteel-gauntlets-v2 (J7J8Jo7ibvE 슬라이드, 딜용 장갑)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch22.py').read(); exec(_src[:_src.index('# ---------- 1. 시한')])

# ---------- 1. EasyBabi 가시투성이 부적 (fabBIuR6yhw, 0.5) ----------
# 영상 요약(4:43): 치명타 확률 매직 베이스 구입(82레벨) → 숙련공의 오브로 소켓 + 아스트리드의 창의성 → 상위 가속의 에센스(공격 속도)
# → 좌측 결정화 + 완벽한 전투의 에센스(모든 공격 스킬 +3, 접두 잡옵 자리) → 접두 훼손(정확도로 막기 — 완벽한 엑잘에 잘 떠서) + 심연의 메아리
# → 상위 찬미 + 완벽한 엑잘(접두 2개, 마음에 안 들고 가장 낮으면 절사의 징조 + 카오스 오브 반복) → 빛의 징조 + 소멸의 오브로 정확도 지우고 훼손 + 메아리 반복.
# 완성품(0:31): 공격 스킬의 원소 피해 T2 · 냉기 피해 추가 T2 · 번개 피해 추가 T5 / 치명타 확률 T1 · 공격 속도 23% · 공격 스킬 +3.
c='Talismans'; P={'high':{'pT':2,'v':1},'bal':{'pT':3,'v':2}}
tags={'crit':{'gi':18,'tmax':1},'as':{'gi':47},'battle':{'gi':56},'acc':{'gi':17},
      'eatk':{'gi':23,'tmax':'$pT'},'cold':{'gi':5,'tmax':'$pT'},'light':{'gi':7,'tmax':'$pT'},'fire':{'gi':4,'tmax':'$pT'},
      'pgood':{'anyOf':['eatk','cold','light','fire']},'keep':{'anyOf':['eatk','cold','light','fire','crit','as','battle']}}
WS={'whittleSafe':{'tag':'keep','keepDes':True}}
CRT=itg('s',c,18,['crit']); ASE=itg('s',c,47,['as'],'c',suffix=('상위 가속의 에센스','Greater Essence of Haste')); BAT=itg('s',c,56,['battle'],'c',suffix=('완벽한 전투의 에센스','Perfect Essence of Battle'))
ACC=itg('p',c,17,['acc'],'d'); EA=itg('p',c,23,['eatk'],ti=1); CO=itg('p',c,5,['cold'],ti=1); LI=itg('p',c,7,['light'],ti=4)
I0=[CRT,J('p')]; I1=[AST]+I0; I2=[AST,CRT,J('p'),ASE]; I3=[AST,CRT,ASE,BAT]; I4=I3+[UN('p')]; I5=I3+[ACC]; I6=I5+[EA,CO]; I7=I3+[EA,CO]; I8=I7+[UN('p')]; I9=I7+[LI]
nodes=[base('ms',{'rar':'magic','mods':[{'tag':'crit'},{'junk':'p'}]},K('치명타 확률 1티어 매직 가시투성이 부적 구입 (아이템 레벨 82)','Buy a magic Spiny Talisman with T1 crit chance (item level 82)'),I0),
 mark([0,0.6],'t1',I0),
 RUNE22('t1',[0,1],'t2',I1),
 act('t2','main',[0,2],'essence','Greater_Essence_of_Haste',K('희귀 전환 + 접미 두번째 옵션','To rare + second suffix'),[st('s','공격 속도 (23—25)% 증가 (제작 옵션)','(23—25)% increased Attack Speed (crafted)')],K('에센스','Essence'),[{'to':'t3'}],I2,ess='as'),
 act('t3','main',[0,3],'essence','Perfect_Essence_of_Battle',K('접미 세번째 옵션','Third suffix'),[st('s','모든 공격 스킬 레벨 +3 (제작 옵션)','+3 to Level of all Attack Skills (crafted)')],K('에센스','Essence'),[{'to':'t4'}],I3,ess='battle',omens=['Omen_of_Sinistral_Crystallisation']),
 act('t4','main',[0,4],'desecrate','Ancient_Jawbone',K('접두 첫번째 옵션(막기 훼손)','First prefix (blocker desecration)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'t5'}],I4),
 act('t5','main',[0,5],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'acc'},'to':'t6','res':'ok'},{'if':{'param':{'v':1}},'to':'t5x','res':'fail'},{'to':'t6','res':'fail'}],I5,want='acc',show=['acc'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('t5x',[1,5],'t4'),
 act('t6','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefixes'),[st('p','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pgood','min':2}},'to':'t7','res':'ok'},{'if':{'all':[{'param':{'v':1}},WS]},'to':'t6b','res':'fail'},{'to':'t7','res':'fail'}],I6,show=['eatk','cold','light','fire'],omens=['Omen_of_Greater_Exaltation']),
 act('t6b','main',[1,6],'chaos','Chaos_Orb',K('가장 낮은 접두를 원소 피해로','The lowest prefix into elemental damage'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'pgood','min':2}},'to':'t7','res':'ok'},{'if':{'sideLt':{'side':'p','n':3}},'to':'t6','res':'fail','hide':True},{'if':WS,'to':'t6b','res':'fail'},{'to':'t7','res':'fail'}],I6,show=['eatk','cold','light','fire'],omens=['Omen_of_Whittling']),
 annul('t7',[0,7],[{'to':'t8'}]),
 act('t8','main',[0,8],'desecrate','Ancient_Jawbone',K('접두 첫번째 옵션(훼손)','First prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'t9'}],I8),
 act('t9','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'pgood'},'to':'ok','res':'ok'},{'if':{'param':{'v':1}},'to':'t9x','res':'fail'},{'to':'ok','res':'fail'}],I9,want='pgood',show=['eatk','cold','light','fire'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('t9x',[1,9],'t8'),
 done([0,10])]
g22('easybabi-spiny-talisman-v2',c,'Spiny Talisman',82,
  'EasyBabi 가시투성이 부적(fabBIuR6yhw, 0.5 아스트리드의 창의성) — 치명타 확률 1티어 매직 구입 → 아스트리드의 창의성 → 상위 가속의 에센스(공격 속도) → 좌측 결정화 + 완벽한 전투의 에센스(공격 스킬 +3) → 고대 턱뼈로 정확도 막기 → 상위 찬미 + 완벽한 엑잘(접두 2개, 하이엔드는 절사 카오스) → 빛의 징조 + 소멸의 오브 → 고대 턱뼈 → 공개(원소 피해 접두). 하이엔드 = 영상(원소 피해 1~2티어), 밸런스 = 1~3티어, 엑잘·공개 결과 그대로.',
  {'pT':{'kr':'원소 피해 접두','en':'Elemental prefixes','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'v':{'kr':'진행','en':'Route','values':TV({'1':('영상 (다시 도전)','Video (retry)'),'2':('결과 그대로','As it comes')})}},P,
  {'high':K('영상: 정확도 막기·절사 카오스·공개를 원하는 옵션까지','Video: accuracy blocker, whittling chaos and reveals until they land'),'bal':K('엑잘·공개 결과 그대로','Keep the exalts and the reveal')},
  tags,nodes,[{'id':'L1','nodes':['t7','t8','t9','t9x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(VHB,lambda v:[{'tag':'eatk','tmax':v=='high' and 2 or 3},{'tag':'cold','tmax':v=='high' and 2 or 3},{'side':'p','label':K('원소 피해 접두 (훼손)','Elemental prefix (desecrated)')} if v=='high' else {'side':'p','random':True},{'tag':'crit'},{'tag':'as'},{'tag':'battle'}]),
  {'quality':20,'sockets':2},{'all':[{'has':'crit'},{'has':'as'},{'has':'battle'},{'full':'p'}]},VHB)

# ---------- 2. SL 딜용 장갑 — 룬벼림 검은강철 건틀릿 (J7J8Jo7ibvE 4:20~6:10 슬라이드) ----------
# 슬라이드 순서: 검은강철 건틀릿 82+ 홈 2개 → 바알 방어구 장인의 주입기 25%+ → 카틀라의 순흑 → 완벽한 진화·확장 + 소멸 반복(1티어 2개) → 완벽한 제왕 → 보존된 갈비뼈 + 분열의 오브(1티어 분열)
# — 여기까지는 베이스 준비(정책 2: 시작 = 분열 + 잡옵 1개) → 카오스 오브(접두 1개) → 좌측 찬미 + 완벽한 엑잘(실패 = 소멸의 오브) → (분열이 접두라) 상위 찬미 + 완벽한 엑잘(접미, 실패 = 우측 소멸의 징조 2개)
# → 절사 + 우측 말소 + 완벽한 카오스(접미 1티어) → 고대 갈비뼈로 접미 마저 → 룬벼림. 완성품: 상태 이상 강도 32%(분열)·점화 50%·피해 가속 20% / 저주 29%·화염 저항 44%·위축 26%.
# 카틀라의 순흑 옵션 가중치는 공개되지 않아 일반 티어 평균으로 추정(xroll).
# 2026-11-12 슬라이드 다시 확인(6:12, 메인 세션 — 자막엔 제작 설명 없음): 단계 일치. 슬라이드에 없는 심연의 메아리는 뺌, 빗나간 공개를 지우는 빛의 징조는 내부 결정.
#   '소멸도 실패 시 7로'는 분열 + 옵션 1개 상태로 돌아가는 것과 같아 카오스 단계로 이음. 등급 C17: 밸런스 = 1~2티어, 마지막 접두(엑잘)·마지막 접미(훼손)는 랜덤 옵션.
#   밸런스는 상위 엑잘·상위 카오스(최소 레벨 35)로 — 카틀라 옵션 2티어가 레벨 45라 완벽한 오브(50)로는 2티어가 안 나옴.
c='Gloves_str_dex'; P={'high':{'pT':1,'sT':1,'v':1},'bal':{'pT':2,'sT':2,'v':2}}
tags={'am':{'gi':85,'tmax':1},'ig':{'gi':82,'tmax':'$pT'},'fa':{'gi':86,'tmax':'$pT'},'cu':{'gi':92,'tmax':'$sT'},'wi':{'gi':91,'tmax':'$sT'},'fr':{'gi':2,'tmax':'$sT'},
      'p2':{'anyOf':['ig','fa']},'sg':{'anyOf':['cu','wi','fr']}}
SL3=K('저주 강도·위축 강도·화염 저항 1~2티어','T1–2 curse magnitude, wither magnitude or fire resistance')
KT=it('r','카틀라의 순흑','Katla’s Gloom',None,'r')
AM=itg('p',c,85,['am'],'f'); IG=itg('p',c,82,['ig']); FA=itg('p',c,86,['fa']); CU=itg('s',c,92,['cu']); WI=itg('s',c,91,['wi']); FR=itg('s',c,2,['fr'],'d',ti=0)
G0=[KT,AM,J('s')]; G1=[KT,AM,IG]; G2=G1+[FA]; G3=G2+[CU,R1('s')]; G4=G2+[CU,WI]; G5=G4+[UN('s')]; G6=G4+[FR]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'am','fr':True},{'junk':'s'}],'quality':25},K('카틀라의 순흑 장착, 상태 이상 강도 1티어 분열 + 잡옵 1개 (퀄리티 25%, 특출난 베이스)','Katla’s Gloom socketed: fractured T1 ailment magnitude + one junk line (25% quality, Exceptional)'),G0),
 mark([0,0.6],'k1',G0),
 act('k1','main',[0,1],'chaos','Chaos_Orb',K('접두 두번째 옵션','Second prefix'),None,K('카오스','Chaos'),[{'if':{'has':'p2'},'to':'k2','res':'ok'},{'to':'k1','res':'fail'}],G1,show=['ig','fa']),
 act('k2','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'p2','min':2}},'to':'k3','res':'ok'},{'if':{'param':{'v':1}},'to':'k2x','res':'fail'},{'to':'k3','res':'fail'}],G2,show=['ig','fa'],omens=['Omen_of_Sinistral_Exaltation'],over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 annul('k2x',[1,2],[{'if':{'has':'p2'},'to':'k2','res':'ok','port':'right'},{'to':'k1','res':'fail','port':'right'}],omens=(),target=K('빗나간 접두 지우기','Remove the missed prefix')),
 act('k3','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접미 첫번째·두번째 옵션','First and second suffixes'),[st('s','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'if':{'has':'sg'},'to':'k4','res':'ok'},{'to':'k3x','res':'fail'}],G3,show=['cu','wi','fr'],omens=['Omen_of_Greater_Exaltation'],over=[{'param':{'v':2},'set':{'cur':'Greater_Exalted_Orb'}}]),
 annul('k3x',[1,3],[{'if':{'sideLt':{'side':'s','n':1}},'to':'k3','res':'ok','port':'right'},{'to':'k3x','res':'fail','hide':True}],omens=('Omen_of_Dextral_Annulment',),target=K('접미 지우기','Remove the suffixes')),
 act('k4','main',[0,4],'chaos','Perfect_Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'sg','min':2}},'to':'k5','res':'ok'},{'to':'k4','res':'fail'}],G4,show=['cu','wi','fr'],trim={'side':'s','keep':'sg'},over=[{'param':{'v':2},'set':{'cur':'Greater_Chaos_Orb'}}]),
 act('k5','main',[0,5],'desecrate','Ancient_Rib',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'k6'}],G5),
 act('k6','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'sg'},'to':'ok','res':'ok'},{'if':{'param':{'v':1}},'to':'k6x','res':'fail'},{'to':'ok','res':'fail'}],G6,want='sg',show=['fr','cu','wi']),
 LIGHTX('k6x',[1,6],'k5'),
 done([0,7])]
g22('sl-blacksteel-gauntlets-v2',c,'Blacksteel Gauntlets',82,
  'SL 딜용 장갑(J7J8Jo7ibvE 슬라이드) — 카틀라의 순흑 · 상태 이상 강도 1티어 분열 + 잡옵(퀄리티 25%) → 카오스 오브(점화 강도·피해 가속) → 좌측 찬미 + 완벽한 엑잘(실패 = 소멸의 오브) → 상위 찬미 + 완벽한 엑잘(접미, 실패 = 우측 소멸의 징조) → 절사 + 우측 말소 + 완벽한 카오스 오브 → 고대 갈비뼈 → 공개(화염 저항·저주·위축). 하이엔드 = 영상(1티어), 밸런스 = 1~2티어, 접두 엑잘·접미 카오스 한 번·공개 결과 그대로. 카틀라 옵션 가중치는 추정.',
  {'pT':{'kr':'접두','en':'Prefixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'sT':{'kr':'접미','en':'Suffixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'v':{'kr':'마지막 접두·접미','en':'Last prefix and suffix','values':TV({'1':('목표 옵션까지 반복','Repeat until a wanted line'),'2':('랜덤 옵션','Random line')})}},P,
  {'high':K('영상: 1티어까지','Video: tier 1 lines'),'bal':K('1~2티어, 마지막 접두·접미는 랜덤 옵션','T1–2, the last prefix and suffix random')},
  tags,nodes,[{'id':'L1','nodes':['k5','k6','k6x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(VHB,lambda v:[{'tag':'am','fr':True},{'tag':'ig','tmax':1},{'tag':'fa','tmax':1},{'tag':'cu','tmax':1},{'tag':'wi','tmax':1},{'tag':'fr','tmax':1,'des':True}] if v=='high' else
      [{'tag':'am','fr':True},{'side':'p','label':K('점화 강도·피해 가속 1~2티어','T1–2 ignite magnitude or ailment acceleration')},{'side':'p','random':True},{'side':'s','label':SL3},{'side':'s','label':SL3},{'side':'s','random':True}]),
  {'quality':25,'sockets':2},{'all':[{'has':'am'},{'full':'p'},{'full':'s'}]},VHB,xsub=["Katla's Gloom"],xroll=True)
print('wrote batch 23')

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_easybabi_spiny_talisman.py'): _sp.run([_sy.executable, f'{H}/gen_easybabi_spiny_talisman.py'], check=True)   # 2026-11-13: 새 기준 전용 생성기가 덮어씀
