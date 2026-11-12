# Flowcharts for five more recipes converted 2026-11-10 (사용자: "다음 레시피들 적용하자"). Final video check later (사용자: 최종 확인은 나중에 한번에).
#   어려움 이하 → Balance + Essential, 전문가 이상 → High-end + Balance (정책 30).
#   ragna-spell4-amulet-v2 (bal/ess), noble-visceral-quiver-v2, sihan-highend-helmet-v2, barricade-quarterstaff-v2, diztoh-endgame-quarterstaff-v2 (high/bal)
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch5.py').read(); exec(_src[:_src.index('# ---------- 1.')])
def cleanup(id,pos,keep,edges,target,side=None,maxJunk=0):
    d={'id':id,'kind':'cleanup','group':'main','pos':pos,'keep':keep,'maxJunk':maxJunk,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':target,'edges':edges}
    if side: d['side']=side
    return d
VNAME={'high':('하이엔드','High-end'),'bal':('밸런스','Balance'),'ess':('에센셜','Essential')}
def graph8(id,cls,bse,ilvl,note,params,P,desc,tags,nodes,loops,finals,finalItem,require,vers,conds=None):
    g={'id':id,'recipe':id,'cls':cls,'base':bse,'ilvl':ilvl,'note':note,'params':params,
       'strategies':[{'id':v,'params':P[v]} for v in vers],
       'versions':[{'id':v,'kr':VNAME[v][0],'en':VNAME[v][1],'params':P[v],'desc':desc[v]} for v in reversed(vers)],
       'tags':tags,'require':require,'groups':GRP,'start':'h1','loops':loops,'finals':finals,'finalItem':finalItem,'nodes':nodes}
    if conds: g['conds']=conds
    json.dump(g,open(f'{H}/{id}.json','w'),ensure_ascii=False,indent=1)
def FIN(vers, fn): return [dict({'id':v,'kr':VNAME[v][0]+' 옵션','en':VNAME[v][1]},lines=fn(v)) for v in vers]
LIGHTX=lambda id,pos,to: annul(id,pos,[{'to':to,'port':'right'}])
R1=lambda s: it(s,'랜덤 옵션 1개','One random line',None,'j')

# ---------- 1. 라그나 주문 +4 목걸이 (Tzpdm8M-Pkk) ----------
# 원본: 정신력 +50 분열 + 모든 주문 +3 → 좌측 찬미 + 엑잘 → 좌측 결정화 + 균열의 에센스(최대 퀄리티) → 달리는 기폭제 40% → 촉진 + 우측 찬미 + 완벽한 엑잘(시전 속도 노림)
# → 달리는 기폭제 다시 → 촉진 + 우측 찬미 + 완벽한 엑잘(시전 속도 1~2티어, 빗나가면 우측 소멸의 징조 + 소멸의 오브) → 보존된 빗장뼈 → 쇳소리 기폭제 40% → 공개(주문 피해, 빛의 징조로 다시) → 절사의 징조 + 상위 카오스(최대 퀄리티 옵션).
# 촉진하는 찬미의 징조 효과는 수치 비공개라 시뮬에 넣지 않음(실제 확률은 더 높음).
P={'bal':{'sT':1,'cT':2,'dT':2},'ess':{'sT':3,'cT':3,'dT':4}}
tags={'spirit':{'gi':28,'tmax':'$sT'},'spell':{'gi':17,'tmax':1},'maxQ':{'gi':81},'cast':{'gi':32,'tmax':'$cT'},'sdmg':{'gi':31,'tmax':'$dT'}}
SP=it('p','정신력 +50 (분열)','+50 Spirit (fractured)',['spirit']); SL=it('s','모든 주문 스킬 +3','+3 all spell skills',['spell']); MQ=it('p','최대 퀄리티 +20% (제작 옵션)','+20% maximum quality (crafted)',['maxQ'])
CS=it('s','시전 속도','Cast speed',['cast']); SD=it('p','주문 피해','Spell damage',['sdmg'])
I0=[SP,SL]; I1=I0+[J('p')]; I2=I0+[MQ]; I3=I2+[J('s')]; I4=I2+[J('s'),CS]; I5=I4+[UN('p')]; I6=I4+[SD]; I7=[SP,SD,R1('p'),SL,J('s'),CS]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'spirit','fr':True},'spell']},K('정신력 분열 + 모든 주문 스킬 +3 태양의 목걸이','Solar Amulet with fractured Spirit + all spell skills +3'),I0),
 mark([0,0.6],'g2',I0),
 act('g2','main',[0,1],'exalt','Exalted_Orb',K('에센스가 지울 접두','The prefix for the essence to remove'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'to':'g3'}],I1,omens=['Omen_of_Sinistral_Exaltation']),
 act('g3','main',[0,2],'essence','Essence_of_the_Breach',K('접두 잡옵을 최대 퀄리티로','Swap the junk prefix for maximum quality'),[st('p','최대 퀄리티 +20% (제작 옵션)','+20% maximum quality (crafted)')],K('에센스','Essence'),[{'to':'g4'}],I2,ess='maxQ',omens=['Omen_of_Sinistral_Crystallisation']),
 act('g4','main',[0,3],'quality','Skittering_Catalyst',K('속도 퀄리티 40%','Speed quality 40%'),[st(None,'달리는 기폭제 40개','40 Skittering Catalysts')],K('퀄리티','Quality'),[{'to':'g5'}],I2,count=40),
 act('g5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션 (시전 속도 1차 도전)','Second suffix (first try at cast speed)'),[st('s','랜덤 옵션 1개 — 시전 속도면 좋음','One random line — cast speed is good')],K('엑잘','Exalt'),[{'to':'g5b'}],I3,omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],cat='cast'),
 act('g5b','main',[0,5],'quality','Skittering_Catalyst',K('속도 퀄리티 다시 40%','Speed quality back to 40%'),[st(None,'달리는 기폭제 40개 (촉진으로 0%가 됨)','40 Skittering Catalysts (Catalysing used it up)')],K('퀄리티','Quality'),[{'to':'g6'}],I3,count=40),
 act('g6','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'cast'},'to':'g7','res':'ok'},{'if':{'param':{'cT':2}},'to':'g6x','res':'fail'},{'to':'g7','res':'fail'}],I4,show=['cast'],omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],cat='cast'),
 cleanup('g6x',[1,6],['spell','cast'],[{'lost':'spell','to':'h1','port':'right'},{'to':'g5b','port':'right'}],K('접미 하나 지우기 (주문 +3이 지워지면 새 베이스)','Remove one suffix (losing +3 spells means a new base)'),side='s',maxJunk=1),
 act('g7','main',[0,7],'desecrate','Preserved_Collarbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'g8'}],I5),
 act('g8','main',[0,8],'quality','Sibilant_Catalyst',K('시전 퀄리티 40% (주문 +3 → +4)','Caster quality 40% (+3 spells → +4)'),[st(None,'쇳소리 기폭제 40개','40 Sibilant Catalysts')],K('퀄리티','Quality'),[{'to':'g9'}],I5,count=40),
 act('g9','main',[0,9],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'sdmg'},'to':'g10','res':'ok'},{'if':{'param':{'cT':2}},'to':'g9x','res':'fail'},{'to':'g10','res':'fail'}],I6,want='sdmg',show=['sdmg'],omens=['Omen_of_Abyssal_Echoes']),
 annul('g9x',[1,9],[{'to':'g7','port':'right'}]),
 act('g10','main',[0,10],'chaos','Greater_Chaos_Orb',K('최대 퀄리티 옵션을 다른 접두로','Replace the maximum quality line'),[st('p','랜덤 옵션 1개 (최대 퀄리티가 가장 낮아 그 옵션만 바뀜)','One random line (maximum quality is the lowest, so only it goes)')],K('카오스','Chaos'),[{'to':'ok'}],I7,omens=['Omen_of_Whittling']),
 done([0,11])]
graph8('ragna-spell4-amulet-v2','Amulets','Solar Amulet',81,
  '라그나 주문 +4 목걸이(원본 레시피 기록) — 정신력 분열 + 주문 +3 베이스 → 좌측 찬미 + 엑잘 → 좌측 결정화 + 균열의 에센스 → 달리는 기폭제 → 촉진 + 우측 찬미 + 완벽한 엑잘 2번(시전 속도) → 보존된 빗장뼈 → 쇳소리 기폭제(주문 +4) → 공개(주문 피해) → 절사의 징조 + 상위 카오스(최대 퀄리티 옵션). 밸런스 = 영상(시전 속도 1~2티어까지 우측 소멸의 징조로 다시, 공개는 빛의 징조로 다시), 에센셜 = 정신력 1~3티어 분열, 결과 그대로. 촉진 효과는 시뮬에 없음.',
  {'sT':{'kr':'정신력 (분열)','en':'Spirit (fractured)','values':TV({'1':('1티어','T1'),'3':('1~3티어','T1–3')})},'cT':{'kr':'시전 속도','en':'Cast speed','values':TV({'2':('1~2티어 (다시 도전)','T1–2 (retry)'),'3':('결과 그대로','As it comes')})},'dT':{'kr':'주문 피해','en':'Spell damage','values':TV({'2':('1~2티어','T1–2'),'4':('결과 그대로','As it comes')})}},P,
  {'bal':K('영상: 시전 속도·주문 피해가 나올 때까지 다시','Video: retry until cast speed and spell damage'),'ess':K('더 싼 분열 베이스, 결과 그대로','Cheaper fractured base, keep whatever comes')},
  tags,nodes,[{'id':'L1','nodes':['g5b','g6','g6x'],'kr':'시전 속도','en':'Cast speed'},{'id':'L2','nodes':['g7','g8','g9','g9x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('bal','ess'),lambda v:[{'tag':'spirit','tmax':P[v]['sT'],'fr':True},{'tag':'sdmg','tmax':P[v]['dT']} if v=='bal' else {'side':'p','random':True},{'side':'p','random':True},{'tag':'spell','tmax':1},{'tag':'cast','tmax':2} if v=='bal' else {'side':'s','random':True},{'side':'s','random':True}]),
  {'quality':40,'sockets':0},{'all':[{'has':'spirit'},{'has':'spell'},{'full':'p'},{'full':'s'}]},('bal','ess'))

# ---------- 2. 노블이 본능적인 화살통 (2PUEwoePtRs, 0.4 영상 → 0.5.5 응용) ----------
# 2026-11-12 영상 전체 대조(2PUEwoePtRs 0:00~11:47, 자막 없음·화면 자막으로 확인, 메인 세션) — tools/notes/noble-2PUEwoePtRs.md.
# 영상: 번개 피해 추가 분열(0:35~5:00, 시작 상태로 둠) → 소멸의 오브로 한 자리만 남기고 카오스 오브(접미 치명타 확률·치명타 피해·투사체 중 하나) → 완벽한 엑잘(우측 찬미는 필수 아님, 5:22)
#   → 접미 잡옵이면 소멸의 오브, 잡옵이 지워지면 훼손(5:42) → 남은 접미 한 자리에 훼손(6:35~7:50, 투사체가 안 나오면 '그나마 높은 레벨' 옵션으로 자리 막기 8:00~8:20)
#   → 접두: 투사체 속도(8:20) → 마지막 접두는 절사 카오스. 막기 옵션이 잡옵과 레벨이 같으면(65) 좌측 말소 대신 빛의 징조로 막기를 지우고 다시 훼손(9:00~10:20, 민첩 66)
#   → 막기 옵션을 지우고 보존된 턱뼈로 훼손 → 공개(투사체, 10:50).
# 0.5 데이터: 영상의 '모든 투사체 +2'(훼손, 레벨 41)는 없어서 일반 옵션 '모든 투사체 +1'(레벨 5)을 공개로 찾음. 훼손 전용 옵션은 모두 레벨 65.
# 등급 C17: 하이엔드 = 영상(모두 1티어, 마지막 접두·접미까지 반복), 밸런스 = 1~2티어, 마지막 접두와 마지막 접미(막기 자리)는 랜덤 옵션.
# 내부 결정(영상에서 확인 못 함): 엑잘·카오스는 완벽한 오브, 공개에 메아리 징조 없음, '소멸빵'은 일반 소멸의 오브.
F={'res':'fail','port':'right'}
def ROUTE_(E, vis):
    out=[]
    for e in E:
        e=dict(e); v=vis.get(e['to'])
        if v is not None and not any(o['to']==e['to'] and not o.get('hide') for o in out): e.update(v if isinstance(v,dict) else {'res':v})
        else: e['hide']=True
        out.append(e)
    return out
P={'high':{'cT':1,'dT':1,'pT':1,'g':1},'bal':{'cT':2,'dT':2,'pT':2,'g':0}}
tags={'light':{'gi':8,'tmax':1},'critA':{'gi':14,'tmax':'$cT'},'critD':{'gi':15,'tmax':'$dT'},'proj':{'gi':9},
      'suf':{'anyOf':['critA','critD','proj'],'label':K('공격 치명타 확률·치명타 피해·투사체 스킬 +1','Attack crit chance, crit damage or +1 projectile skills')},
      'pspd':{'gi':18,'tmax':'$pT'},'bow':{'gi':19,'tmax':'$pT'},'pre':{'anyOf':['pspd','bow'],'label':K('투사체 속도·활 스킬 피해','Projectile speed or bow damage')},
      'keep':{'anyOf':['critA','critD','proj','pspd','bow']}}
G1={'param':{'g':1}}; G0={'param':{'g':0}}
S1={'count':{'tag':'suf','min':1}}; S2={'count':{'tag':'suf','min':2}}; S3={'count':{'tag':'suf','min':3}}
PD={'any':[{'all':[G1,{'count':{'tag':'pre','min':2}}]},{'all':[G0,{'has':'pre'},{'full':'p'}]}]}
def RN(vis):   # every step re-checks the item
    return ROUTE_([{'if':{'not':S1},'to':'q2'},
       {'if':{'all':[{'not':S2},{'sideLt':{'side':'s','n':3}},{'not':{'junk':{'side':'s','tag':'suf'}}}]},'to':'q3'},{'if':{'not':S2},'to':'q3x'},
       {'if':{'all':[G1,{'not':S3},{'junk':{'side':'s','tag':'suf'}}]},'to':'q3x'},
       {'if':{'all':[{'not':S3},{'sideLt':{'side':'s','n':3}},{'des':True}]},'to':'q3'},
       {'if':{'all':[{'not':S3},{'sideLt':{'side':'s','n':3}}]},'to':'q4'},
       {'if':{'all':[{'not':PD},{'sideLt':{'side':'p','n':3}}]},'to':'p1'},
       {'if':{'all':[{'not':PD},{'whittleSafe':{'tag':'keep','keepDes':True}}]},'to':'w1'},
       {'if':{'all':[{'not':PD},{'not':S3},{'des':True},{'whittleSafe':{'tag':'keep'}}]},'to':'r1'},
       {'if':{'not':PD},'to':'w1'},
       {'if':{'any':[S3,{'all':[G0,{'full':'s'}]}]},'to':'ok'},
       {'if':{'des':True},'to':'r1'},{'to':'q4'}],vis)
LF=it('p','번개 피해 추가 1티어 (분열)','T1 flat lightning (fractured)',['light']); SU=lambda: it('s','치명타·투사체 접미','Crit or projectile suffix',['suf']); PR=lambda: it('p','투사체 속도·활 피해','Projectile speed or bow damage',['pre'])
SL2=K('공격 치명타 확률·치명타 피해 1~2티어 또는 투사체 +1','T1–2 attack crit chance or crit damage, or +1 projectile skills')
BL=it('s','자리 막기 (공개된 훼손 옵션)','Blocker (revealed desecration)',None,'d')
I0=[LF,J('s')]; I1=[LF,SU()]; I2=I1+[SU()]; I3=I2+[UN('s')]; I4=I2+[BL]; I5=[LF,PR()]+I4[1:]; I6=[LF,PR(),PR()]+I4[1:]; I7=[LF,PR(),PR(),SU(),SU(),UN('s')]; I8=[LF,PR(),PR(),SU(),SU(),SU()]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'light','fr':True},{'junk':'s'}]},K('번개 피해 추가 1티어 분열 + 잡옵 1개','Fractured T1 flat lightning + one junk line'),I0),
 mark([0,0.6],'q2',I0),
 act('q2','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix option'),None,K('카오스','Chaos'),RN({'q3':'ok','q2':F}),I1,show=['critA','critD','proj']),
 act('q3','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix option'),None,K('엑잘','Exalt'),RN({'q4':'ok','q3x':F}),I2,show=['critA','critD','proj']),
 annul('q3x',[1,2],[{'if':{'all':[S1,{'not':S2},{'not':{'junk':{'side':'s','tag':'suf'}}},{'sideLt':{'side':'s','n':3}},{'not':{'des':True}}]},'to':'q4','res':'ok'}]+RN({'q2':{'port':'right'}}),omens=(),target=K('접미 잡옵 지우기 (잡옵이 지워지면 훼손)','Remove the junk suffix (desecrate once it is gone)')),
 act('q4','main',[0,3],'desecrate','Preserved_Jawbone',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'q4r'}],I3,omens=['Omen_of_Dextral_Necromancy']),
 act('q4r','main',[0,4],'reveal',None,K('훼손 옵션 확인 (없으면 가장 높은 레벨로 자리 막기)','Reveal (on a miss, keep the highest-level option as a blocker)'),None,K('공개','Reveal'),RN({'ok':'ok','p1':F}),I4,want='suf',show=['critA','critD','proj'],missPick='lvl'),
 act('p1','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 옵션','Prefix option'),None,K('엑잘','Exalt'),RN({'w1':{'port':'right'},'ok':{}}),I5,show=['pspd','bow']),
 act('w1','main',[1,5],'chaos','Perfect_Chaos_Orb',K('접두 잡옵을 다시','Reroll the junk prefix'),None,K('카오스','Chaos'),RN({'p1':'ok','r1':F}),I6,show=['pspd','bow'],trim={'side':'p','keep':'keep','keepDes':True}),
 annul('r1',[2,4],RN({'q4':{'port':'right'}}),target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecration')),
 done([0,7])]
graph8('noble-visceral-quiver-v2','Quivers','Visceral Quiver',82,
  '노블이 본능적인 화살통(2PUEwoePtRs, 0.4 영상을 0.5 데이터로) — 번개 피해 추가 분열 → 카오스 오브(접미 치명타·투사체 하나) → 완벽한 엑잘(접미 잡옵이면 소멸의 오브, 잡옵이 지워지면 훼손) → 우측 강령술 + 보존된 턱뼈로 남은 접미 훼손(투사체가 아니면 가장 높은 레벨 옵션으로 자리 막기) → 완벽한 엑잘(접두) → 절사 카오스(마지막 접두, 막기 옵션이 잡옵보다 낮으면 빛의 징조로 지우고 다시 훼손) → 막기 옵션을 지우고 다시 훼손 → 공개(투사체). 하이엔드 = 영상(모두 1티어), 밸런스 = 1~2티어, 마지막 접두·접미는 랜덤 옵션.',
  {'cT':{'kr':'공격 치명타 확률','en':'Attack crit chance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'dT':{'kr':'치명타 피해','en':'Crit damage','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'pT':{'kr':'접두 (투사체 속도·활 피해)','en':'Prefixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'g':{'kr':'마지막 접두·접미','en':'Last prefix and suffix','values':TV({'1':('목표 옵션까지 반복','Repeat until the wanted line'),'0':('랜덤 옵션','Random line')})}},P,
  {'high':K('영상: 모두 1티어, 마지막 접두·접미까지 반복','Video: all T1, repeat for the last prefix and suffix'),'bal':K('1~2티어, 마지막 접두·접미는 랜덤 옵션','T1–2, the last prefix and suffix random')},
  tags,nodes,[{'id':'L1','nodes':['q4','q4r','r1'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['p1','w1'],'kr':'접두','en':'Prefixes'}],
  FIN(('high','bal'),lambda v:[{'tag':'light','tmax':1,'fr':True}]+([{'tag':'pspd','tmax':1},{'tag':'bow','tmax':1}] if v=='high' else [{'side':'p','label':K('투사체 속도·활 피해 1~2티어','T1–2 projectile speed or bow damage')},{'side':'p','random':True}])+([{'tag':'critA','tmax':1},{'tag':'critD','tmax':1},{'tag':'proj','des':True}] if v=='high' else [{'side':'s','label':SL2},{'side':'s','label':SL2},{'side':'s','random':True}])),
  {'quality':20,'sockets':0},{'all':[{'has':'light'},{'count':{'tag':'suf','min':2}},{'full':'s'},{'any':[{'all':[G1,{'count':{'tag':'suf','min':3}},{'count':{'tag':'pre','min':2}}]},{'all':[G0,{'has':'pre'},{'full':'p'}]}]}]},('high','bal'))

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
      'pct':{'gi':9,'tmax':'$aT'},'pct1':{'gi':9,'tmax':1},'pct2':{'gi':9,'tmax':2},'mark':{'gi':47}}
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
     [{'if':{'has':'life'},'to':'p2','res':'ok'},{'to':'p1x',**F_,**L_('다른 옵션 — 소멸','Another line: annul')}],[LI0],show=['life']),   # 11:20~11:32 화면: 생명력 +159 1티어, 11:35 '접두 아니면 지워 주시고'
 {'id':'p1x','kind':'act','group':'prep','pos':[1,1],'act':'annul','cur':'Orb_of_Annulment','label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('빗나간 옵션 지우고 다시 진화','Clear the miss, transmute again'),'edges':[{'to':'p1',**L_('다시 진화','Transmute again')}]},
 act('p2','prep',[0,2],'augment','Perfect_Orb_of_Augmentation',K('매직 두번째 옵션','Second magic line'),[st(None,'랜덤 옵션 1개','One random line')],K('확장','Augment'),[{'to':'p3'}],[LI0,_JK('s')]),   # 11:40 완벽한 확장의 오브 30개
 act('p3','prep',[0,3],'regal','Perfect_Regal_Orb',K('레어','Rare'),[st(None,'랜덤 옵션 1개','One random line')],K('제왕','Regal'),[{'to':'p4'}],[LI0,_JK('p'),_JK('s')]),   # 12:15~12:30
 act('p4','prep',[0,4],'desecrate','Preserved_Rib',K('네번째 옵션(훼손) — 분열 조건 옵션 4개','Fourth line (desecrated) — fracture needs four'),[st(None,'훼손 옵션 (미공개, 분열되지 않음)','Desecrated (unrevealed, cannot fracture)')],K('훼손','Desecrate'),[{'to':'p5'}],[LI0,_JK('p'),_JK('s'),UN('s')]),   # 12:32 보존된 갈비뼈 18/20, 12:44 미공개 훼손
 {'id':'hd','kind':'side','group':'prep','pos':[1,4.5],'attach':['p4','p5'],'cur':'Divine_Orb','goal':K('생명력 수치 최대, 선택·비용 미포함','Max the life roll, optional, not costed'),'label':K('신성','Divine')},   # 12:40~13:10 생명력 153 → 174
 act('p5','prep',[0,5],'fracture','Fracturing_Orb',K('분열 (셋 중 하나)','Fracture (one of three)'),[st(None,'생명력 최대치가 분열되면 성공','Success when maximum life fractures')],K('분열','Fracture'),
     [{'if':{'fractured':'life'},'to':'p6','res':'ok',**L_('생명력 분열','Life fractured')},{'to':'xj','res':'fail','dash':True,**L_('다른 옵션 분열','Another line fractured')}],[LI,_JK('p'),_JK('s'),UN('s')]),   # 13:30~13:50 셋째 투구 성공
 {'id':'xj','kind':'exit','group':'prep','pos':[1,5],'simTo':'h1','variant':'fail','label':K('다른 옵션 분열 — 새 베이스','Another line fractured — new base'),'note':K('생명력 최대치가 아닌 옵션이 분열되면 이 투구는 다른 용도로 두고 새 베이스로 처음부터','Another line fractured: set this one aside and start on a new base')},   # 14:00 실패한 투구 2개 버림
 {'id':'p6','kind':'cleanup','group':'prep','pos':[0,6],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep only the fracture + one line'),'edges':[{'to':'ms'}],'item':[LI,_JK('p')]},   # 14:05 화면: 생명력 174 분열 + 방어도 40%·생명력 43
 mark([0,7],'s1',[LI,_JK('p')]),
 act('s1','main',[0,8],'chaos','Chaos_Orb',K('접미 치명타 확률 1~2티어','T1–2 critical hit chance suffix'),None,K('카오스','Chaos'),
     [{'if':{'has':'crit'},'to':'k1','res':'ok'},{'to':'s1','res':'fail'}],[LI,CR],show=['crit'],skipIf={'has':'crit'},skipTo='k1',skipHide=True),   # 17:01 성공 회차 치명타 26%(2티어), 창고 카오스 343 → 322(14:22·14:46)
 {'id':'kz','kind':'cleanup','group':'main','pos':[1,8],'keep':[],'maxJunk':1,'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('분열 + 옵션 1개만 남기기','Keep the fracture + one line'),'edges':[{'to':'s1',**L_('다시 카오스','Chaos again')}]},   # 16:30~16:40 '날아갔죠 — 다시 소멸해서 한 줄 남기고 다시 돌려'
 act('k1','main',[0,9],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),None,K('엑잘','Exalt'),
     [{'if':{'ref':'sOK'},'to':'fx','res':'ok',**L_('목표 접미 성공','Target suffixes hit')},{'to':'k2',**F_,**L_('빗나간 접미 — 소멸','Missed suffix: annul')}],[LI,CR,EL,RS],show=['ele','res'],omens=['Omen_of_Dextral_Exaltation','Omen_of_Greater_Exaltation'],over=[{'param':{'g':0},'set':{'item':[LI,CR,EL,R1('s')],'show':['ele']}}]),   # 17:34 완벽한 엑잘 + 우측 찬미 + 상위 찬미(인벤 20 → 19, 징조 3 → 2, 10 → 9 — 14:48·15:03)
 act('k2','main',[1,9],'annul','Orb_of_Annulment',K('빗나간 접미 지우기 (한 개)','Remove a missed suffix (one)'),None,K('소멸','Annul'),
     [{'if':{'removed':'crit'},'to':'kz',**F_,**L_('치명타 확률이 지워짐 — 카오스부터','Crit chance gone: back to Chaos')},{'to':'k3',**L_('빈 접미에 엑잘','Exalt into the empty suffix')}],[LI,CR,EL]),   # 17:38 소멸 → 모든 소환수 +2 지워짐
 act('k3','main',[1,10],'exalt','Perfect_Exalted_Orb',K('빈 접미 하나','The empty suffix'),None,K('엑잘','Exalt'),
     [{'if':{'ref':'sOK'},'to':'fx','res':'ok'},{'to':'k2',**F_,**L_('또 빗나감 — 소멸','Missed again: annul')}],[LI,CR,EL,RS],show=['ele','res'],omens=['Omen_of_Dextral_Exaltation'],over=[{'param':{'g':0},'set':{'item':[LI,CR,EL,R1('s')],'show':['ele']}}]),   # 17:44 상위 찬미 끔(7/10), 17:48 방어도 원소 적용 38% 1티어(인벤 엑잘 17 → 16, 우측 찬미 10 → 9)
 act('fx','main',[0,10],'flux','Void_Flux',K('원소 저항 → 카오스 저항','Elemental resistance → chaos resistance'),None,K('유동체','Flux'),[{'to':'q1'}],[LI,CR,EL,CH],
     skipIf={'param':{'g':0}},skipTo='q1',skipHide=True,skipNote=K('밸런스는 세번째 접미가 랜덤 옵션이라 건너뜀','Balance skips it: the third suffix is random')),   # 18:20~18:38 번개 저항 35%(3티어) → 카오스 저항 21%
 act('q1','main',[0,11],'exalt','Perfect_Exalted_Orb',K('접두 방어도 최대치','Flat armour prefix'),None,K('엑잘','Exalt'),
     [{'if':{'added':'flat'},'to':'q4','res':'ok',**L_('방어도 최대치 성공','Flat armour hit')},{'to':'q2',**F_,**L_('1번째 빗나감 — 심연의 에센스','1st miss: Essence of the Abyss')}],[LI,AF,CR,EL,CH],show=['flat']),   # 18:52 완벽한 엑잘(16/20) → 18:58 방어도 80% 2티어 빗나감
 act('q2','main',[1,11],'essence','Essence_of_the_Abyss',K('빗나간 접두를 징표로','The missed prefix becomes the mark'),[st('p','심연 군주의 징표','Mark of the Abyssal Lord')],K('에센스','Essence'),[{'to':'q3',**L_('다시 엑잘','Exalt again')}],[LI,MK,CR,EL,CH],ess='mark',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),   # 19:02 좌측 결정화 툴팁, 19:08 징표
 act('q3','main',[1,12],'exalt','Perfect_Exalted_Orb',K('접두 방어도 최대치 다시','Flat armour prefix again'),None,K('엑잘','Exalt'),
     [{'if':{'added':'flat'},'to':'q4','res':'ok'},{'to':'q3x',**F_,**L_('2번째 빗나감 — 징표 훼손','2nd miss: desecrate the mark')}],[LI,AF,MK,CR,EL,CH],show=['flat']),   # 19:14 완벽한 엑잘(15/20) → 19:18 방어도 +213 1티어
 act('q3x','main',[2,12],'desecrate','Preserved_Rib',K('징표를 훼손 옵션으로','The mark becomes a desecrated line'),[st('p','훼손 옵션 (미공개)','Desecrated (unrevealed)')],K('훼손','Desecrate'),[{'to':'q3y'}],[LI,UN('p'),CR,EL,CH],fromMark=True),   # 19:30·21:20 설명만(성공 회차에는 없음)
 {'id':'q3y','kind':'act','group':'main','pos':[2,13],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('훼손 옵션 지우고 남은 빗나간 접두를 다시 징표로','Clear the desecration, mark the missed prefix again'),'target':K('훼손 옵션 제거','Remove the desecrated modifier'),'edges':[{'to':'q2',**L_('다시 심연의 에센스','Essence of the Abyss again')}]},   # 19:40~20:00 설명
 act('q4','main',[0,12],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손) — 징표 자리','Third prefix (desecrated) — on the mark'),[st('p','훼손 옵션 (미공개, 한 티어 높게)','Desecrated (unrevealed, one tier higher)')],K('훼손','Desecrate'),[{'to':'q5'}],[LI,AF,UN('p'),CR,EL,CH],
     fromMark=True,skipIf={'not':{'has':'mark'}},skipTo='q6',skipHide=True,skipNote=K('징표가 없으면 다음 고대 갈비뼈로 빈자리에','No mark: the next Ancient Rib goes to the empty slot')),   # 20:18 고대 갈비뼈(12/20), 20:26 징표 자리 훼손
 act('q5','main',[0,13],'reveal',None,K('접두 방어도 % 증가','% increased armour prefix'),None,K('공개','Reveal'),
     [{'if':{'added':'pct'},'to':'ok','res':'ok'},{'to':'q5x',**F_,**L_('빗나감 — 빛의 징조','Miss: Omen of Light')}],[LI,AF,AP,CR,EL,CH],want='pct',show=['pct'],omens=['Omen_of_Abyssal_Echoes']),   # 22:04 메아리 소모, 22:06 방어도 84% 2티어 · 25:18 메아리 소모, 25:26 방어도 92% 1티어
 {'id':'q5x','kind':'act','group':'main','pos':[1,13],'act':'annul','cur':'Orb_of_Annulment','omens':['Omen_of_Light'],'label':K('소멸의 오브 사용','Use an Orb of Annulment'),'goal':K('소멸의 오브 사용','Use an Orb of Annulment'),'target':K('훼손 옵션 제거','Remove the desecrated modifier'),'edges':[{'to':'q6',**L_('다시 훼손','Desecrate again')}]},   # 23:56 소멸의 오브(15/20) + 빛의 징조
 act('q6','main',[1,12.4],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손) 다시','Third prefix (desecrated) again'),[st('p','훼손 옵션 (미공개)','Desecrated (unrevealed)')],K('훼손','Desecrate'),[{'to':'q5',**L_('다시 공개','Reveal again')}],[LI,AF,UN('p'),CR,EL,CH]),   # 24:02 고대 갈비뼈(11/20)
 done([0,14])]
graph8('sihan-highend-helmet-v2','Helmets_str','Imperial Greathelm',82,
  '시한 하이엔드 투구(2026-11-12 영상 전체 재대조, 새 플로우차트 기준) — 특출난 제국의 대헬름 → 완벽한 진화(생명력 1티어)·확장·제왕 → 보존된 갈비뼈 → 분열(1/3, 빗나가면 새 베이스) → 소멸로 분열 + 옵션 1개 → 카오스 오브(치명타 확률 1~2티어) → 완벽한 엑잘 + 우측 찬미 + 상위 찬미(접미 둘, 빗나가면 소멸 → 완벽한 엑잘 + 우측 찬미) → 공허 유동체(저항 → 카오스 저항) → 완벽한 엑잘(방어도 최대치, 빗나가면 좌측 결정화 + 심연의 에센스로 징표 → 완벽한 엑잘) → 고대 갈비뼈(징표 자리) → 공개 + 심연의 메아리(방어도 %, 빗나가면 빛의 징조 + 소멸 → 고대 갈비뼈). 신성한 오브는 비용에서 뺌.',
  {'aT':{'kr':'방어도 접두','en':'Armour prefixes','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'eT':{'kr':'방어도 원소 피해 적용','en':'Armour to elemental','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},
   'g':{'kr':'세번째 접미','en':'Third suffix','values':TV({'1':('저항 1~3티어 + 유동체','T1–3 resistance + Flux'),'0':('랜덤 옵션','Random line')})}},P,
  {'high':K('영상: 방어도 원소 적용·방어도 두 옵션 1티어, 저항 1~3티어','Video: T1 armour-to-elemental and both armour lines, T1–3 resistance'),'bal':K('반복 구간 1~2티어, 세번째 접미는 랜덤 옵션','Loops accept T1–2, the third suffix random')},
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

# ---------- 4. Barricade 험악한 육척봉 (B4yShuKydt0) ----------
# 원본: 퀄리티 30%, 치명타 확률 5% 분열 + 잡옵 → 카오스 오브(근접 스킬 +5) → 우측 강령술 + 보존된 턱뼈 → 공개(공격 속도·치명타 피해 1티어, 빛의 징조로 다시)
# → 상위 찬미 + 완벽한 엑잘(접두 옵션 2개) → 절사의 징조 + 완벽한 카오스 오브로 원소 피해 접두 옵션 2개 → 완벽한 엑잘(세번째, 빗나가면 절사 카오스).
# 2026-11-11 영상 대조(A2, 자막 B4yShuKydt0): 세번째 접두 반복(p5)은 영상대로 절사의 징조 + 완벽한 카오스 오브만(15:02·17:36). 잡옵이 가장 낮은 옵션이 아니면(물리 + 정확도 1티어처럼 레벨 81, 17:46)
#   좌측 말소의 징조 대신 영상의 좌측 소멸의 징조 + 소멸의 오브(1/3로 잡옵, 18:39~19:35) → 완벽한 엑잘(p4)로 다시 — 영상이 말소는 비싸다고 말함(18:50).
P={'high':{'rT':1,'eT':1},'bal':{'rT':2,'eT':2}}
tags={'crit':{'gi':18,'tmax':1},'melee':{'gi':10,'tmax':1},'as':{'gi':16,'tmax':'$rT'},'cdmg':{'gi':19,'tmax':'$rT'},'rev':{'anyOf':['as','cdmg'],'label':K('공격 속도·치명타 피해','Attack speed or crit damage')},
      'eatk':{'gi':23,'tmax':'$eT'},'fire':{'gi':4,'tmax':'$eT'},'cold':{'gi':5,'tmax':'$eT'},'lflat':{'gi':7,'tmax':'$eT'},
      'ele':{'anyOf':['eatk','fire','cold','lflat'],'label':K('원소 피해 접두','Elemental damage prefix')},'keep':{'anyOf':['melee','rev','ele']}}
CR=it('s','치명타 확률 +5% (분열)','+5% crit chance (fractured)',['crit']); ME=it('s','근접 스킬 +5','+5 melee skills',['melee']); RV=it('s','공격 속도·치명타 피해','Attack speed or crit damage',['rev'])
EL=lambda: it('p','원소 피해 접두','Elemental damage prefix',['ele'])
I0=[CR,J('s')]; I1=[CR,ME]; I2=I1+[UN('s')]; I3=I1+[RV]; I4=[J('p'),J('p')]+I3; I5=[EL(),EL()]+I3; I6=[EL(),EL(),EL()]+I3
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'crit','fr':True},{'junk':'s'}]},K('치명타 확률 5% 분열 + 잡옵 1개 (특출난 베이스, 퀄리티 30%)','Fractured 5% crit chance + one junk line (exceptional, 30% quality)'),I0),
 mark([0,0.6],'q2',I0),
 act('q2','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix option'),None,K('카오스','Chaos'),[{'if':{'has':'melee'},'to':'q3','res':'ok'},{'to':'q2','res':'fail'}],I1,show=['melee']),
 act('q3','main',[0,2],'desecrate','Preserved_Jawbone',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'q4'}],I2,omens=['Omen_of_Dextral_Necromancy']),
 act('q4','main',[0,3],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'rev'},'to':'p1','res':'ok'},{'to':'q4x','res':'fail'}],I3,want='rev',show=['as','cdmg'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('q4x',[1,3],'q3'),
 act('p1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 2개','Two random lines')],K('엑잘','Exalt'),[{'if':{'count':{'tag':'ele','min':2}},'to':'p4','res':'ok'},{'to':'p2','res':'fail'}],I4,omens=['Omen_of_Greater_Exaltation']),
 act('p2','main',[0,5],'chaos','Perfect_Chaos_Orb',K('가장 낮은 옵션을 원소 피해로','The lowest line into elemental damage'),[st('p','원소 피해 접두 옵션 2개','Two elemental damage prefixes')],K('카오스','Chaos'),
     [{'if':{'count':{'tag':'ele','min':2}},'to':'p4','res':'ok'},{'to':'p2','res':'fail'}],I5,trim={'side':'p','keep':'keep'},
     over=[{'param':{'eT':2},'set':{'cur':'Greater_Chaos_Orb'}}]),
 act('p4','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'ele','min':3}},'to':'ok','res':'ok'},{'if':{'all':[{'param':{'eT':1}},{'whittleSafe':{'tag':'keep','side':'p'}}]},'to':'p5','res':'fail'},{'if':{'param':{'eT':1}},'to':'p5x','res':'fail'},{'to':'ok','res':'fail'}],I6,show=['fire','cold','lflat']),
 act('p5','main',[0,7],'chaos','Perfect_Chaos_Orb',K('버릴 옵션을 원소 피해로','The junk line into elemental damage'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'ele','min':3}},'to':'ok','res':'ok'},{'if':{'whittleSafe':{'tag':'keep','side':'p'}},'to':'p5','res':'fail'},{'to':'p5x','res':'fail'}],I6,show=['fire','cold','lflat'],trim={'side':'p','keep':'keep'}),
 annul('p5x',[1,7],[{'to':'p4','port':'right'}],omens=('Omen_of_Sinistral_Annulment',),target=K('접두 옵션 하나 지우기','Remove one prefix')),
 done([0,8])]
graph8('barricade-quarterstaff-v2','Quarterstaves','Sinister Quarterstaff',81,
  'Barricade 험악한 육척봉(원본 레시피 기록) — 치명타 확률 5% 분열 + 잡옵(퀄리티 30%) → 카오스 오브(근접 스킬 +5) → 우측 강령술 + 보존된 턱뼈 → 공개(공격 속도·치명타 피해, 빛의 징조로 다시) → 상위 찬미 + 완벽한 엑잘 → 절사의 징조 + 완벽한 카오스 오브로 원소 피해 접두 옵션 2개 → 완벽한 엑잘(세번째, 하이엔드는 빗나가면 절사 카오스 — 가장 낮은 옵션이 버릴 옵션일 때만). 하이엔드 = 영상(1티어), 밸런스 = 원소 피해 접두 2개를 1~2티어까지 절사 + 상위 카오스 오브, 세번째 접두는 랜덤 옵션(2026-11-12 등급 기준 C17).',
  {'rT':{'kr':'공격 속도·치명타 피해','en':'Attack speed or crit damage','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'eT':{'kr':'원소 피해 접두','en':'Elemental prefixes','values':TV({'1':('1티어 옵션 3개 (완벽한 카오스)','Three T1 lines (Perfect Chaos)'),'2':('1~2티어 옵션 2개 (상위 카오스), 세번째는 랜덤','Two T1–2 lines (Greater Chaos), the third random')})}},P,
  {'high':K('영상: 원소 피해 1티어 옵션 3개','Video: three T1 elemental prefixes'),'bal':K('1~2티어 옵션 2개, 세번째는 결과 그대로','Two T1–2 lines, the third as it comes')},
  tags,nodes,[{'id':'L1','nodes':['q3','q4','q4x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:([{'side':'p','label':K('원소 피해 접두 1티어','Elemental damage prefix T1')}]*3 if v=='high' else [{'side':'p','label':K('원소 피해 접두 1~2티어','Elemental damage prefix T1–2')}]*2+[{'side':'p','random':True}])+[{'tag':'crit','tmax':1,'fr':True},{'tag':'melee','tmax':1},{'side':'s','des':True,'label':K('공격 속도·치명타 피해 1티어','Attack speed or crit damage T1') if v=='high' else K('공격 속도·치명타 피해 1~2티어','Attack speed or crit damage T1–2')}]),
  {'quality':30,'sockets':3},{'all':[{'has':'melee'},{'has':'rev'},{'has':'ele'},{'full':'p'}]},('high','bal'))

# ---------- 5. Diztoh 엔드게임 육척봉 (YfGJyBrObxI) ----------
# 원본: 근접 스킬 +5 분열 + 잡옵(퀄리티 20%) → 상위 카오스 오브(물리 피해 추가·물리 %·복합) → 좌측 찬미 + 완벽한 엑잘(다른 물리 %, 빗나가면 좌측 소멸의 징조)
# → 좌측 찬미 + 완벽한 엑잘(복합·화염 추가, 빗나가면 절사 + 좌측 말소 + 완벽한 카오스) → 완벽한 엑잘(접미, 빗나가면 우측 말소 + 카오스) → 우측 강령술 + 고대 턱뼈 → 공개(치명타, 빗나가면 우측 소멸의 징조).
# 2026-11-12 영상 전체 대조(자동 번역 자막 0:00~17:40, 메인 세션): 단계 일치. 영상은 접두 둘을 상위 찬미로 한 번에도 하지만 '하나씩 해도 된다'(6:00)고 해서 하나씩 둠.
#   훼손 공개 빗나감: 영상은 우측 소멸의 징조 50:50(13:00, '빛의 징조보다 싸서'). 지금 시세는 빛의 징조(2,587)가 우측 소멸(3,708)보다 싸고 공격 속도를 잃지 않아 빛의 징조로 둠
#   (시뮬 1,000회: 하이엔드 우측 소멸 8,130 → 빛 1,232).
#   등급 C17: 하이엔드 1티어, 밸런스 1~2티어, 밸런스는 마지막 접두·접미(훼손)를 랜덤 옵션으로. 영상은 2·3티어로 타협했지만 등급 기준을 따름.
P={'high':{'xT':1,'sT':1,'g':1},'bal':{'xT':2,'sT':2,'g':0}}
tags={'melee':{'gi':10,'tmax':1},'pflat':{'gi':3,'tmax':3},'ppct':{'gi':8,'tmax':'$xT'},'hyb':{'gi':9,'tmax':'$xT'},'fire':{'gi':4,'tmax':4},
      'p1':{'anyOf':['pflat','ppct','hyb'],'label':K('물리 피해 접두','Physical damage prefix')},'pp':{'anyOf':['ppct','hyb'],'label':K('물리 % · 복합','% physical or hybrid')},'p3':{'anyOf':['hyb','fire'],'label':K('복합·화염 피해 추가','Hybrid or flat fire')},
      'pre':{'anyOf':['pflat','ppct','hyb','fire'],'label':K('물리·화염 피해 접두','Physical or fire prefix')},
      'as':{'gi':16,'tmax':4},'crit':{'gi':18,'tmax':'$sT'},'cdmg':{'gi':19,'tmax':'$sT'},'suf':{'anyOf':['as','crit','cdmg'],'label':K('공격 속도·치명타','Attack speed or crit')},'cr':{'anyOf':['crit','cdmg'],'label':K('치명타 확률·피해','Crit chance or damage')},
      'keepP':{'anyOf':['melee','pre','suf']}}
ML=it('s','근접 스킬 +5 (분열)','+5 melee skills (fractured)',['melee']); PP=lambda: it('p','물리·화염 피해 접두','Physical or fire prefix',['pre']); SF=lambda: it('s','공격 속도·치명타','Attack speed or crit',['suf'])
I0=[ML,J('s')]; I1=[PP(),ML]; I2=[PP(),PP(),ML]; I3=[PP(),PP(),PP(),ML]; I4=I3+[SF()]; I5=I4+[UN('s')]; I6=[PP(),PP(),PP(),ML,SF(),SF()]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'melee','fr':True},{'junk':'s'}]},K('근접 스킬 +5 분열 + 잡옵 1개 (퀄리티 20%)','Fractured +5 melee skills + one junk line (20% quality)'),I0),
 mark([0,0.6],'s2',I0),
 act('s2','main',[0,1],'chaos','Greater_Chaos_Orb',K('접두 첫번째 옵션','First prefix option'),None,K('카오스','Chaos'),[{'if':{'has':'p1'},'to':'s3','res':'ok'},{'to':'s2','res':'fail'}],I1,show=['pflat','ppct','hyb']),
 act('s3','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre','min':2}},'to':'s4','res':'ok'},{'to':'s3x','res':'fail'}],I2,show=['ppct','hyb'],omens=['Omen_of_Sinistral_Exaltation']),
 cleanup('s3x',[1,2],['pre'],[{'lost':'pre','to':'s2','port':'right'},{'to':'s3','port':'bottom'}],K('빗나간 접두 지우기 (첫번째 접두는 유지)','Remove the missed prefix (keep the first)'),side='p'),
 act('s4','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre','min':3}},'to':'s5','res':'ok'},{'if':{'all':[{'param':{'g':1}},{'whittleSafe':{'tag':'keepP','side':'p'}}]},'to':'s4b','res':'fail'},{'to':'s5','res':'fail'}],I3,show=['hyb','fire'],omens=['Omen_of_Sinistral_Exaltation'],
     over=[{'param':{'g':0},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('s4b','main',[1,3],'chaos','Perfect_Chaos_Orb',K('가장 낮은 접두를 다시 (버릴 옵션일 때만)','Reroll the lowest prefix (only while it is junk)'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'pre','min':3}},'to':'s5','res':'ok'},{'if':{'sideLt':{'side':'p','n':3}},'to':'s4','res':'fail','hide':True},{'if':{'whittleSafe':{'tag':'keepP','side':'p'}},'to':'s4b','res':'fail'},{'to':'s5','res':'fail'}],I3,show=['hyb','fire'],omens=['Omen_of_Whittling','Omen_of_Sinistral_Erasure']),
 act('s5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'suf'},'to':'s6','res':'ok'},{'to':'s5b','res':'fail'}],I4,show=['as','crit','cdmg'],
     over=[{'param':{'g':0},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('s5b','main',[1,4],'chaos','Chaos_Orb',K('접미를 다시','Reroll a suffix'),None,K('카오스','Chaos'),[{'if':{'has':'suf'},'to':'s6','res':'ok'},{'to':'s5b','res':'fail'}],I4,show=['as','crit','cdmg'],omens=['Omen_of_Dextral_Erasure']),
 act('s6','main',[0,5],'desecrate','Ancient_Jawbone',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'s7'}],I5,omens=['Omen_of_Dextral_Necromancy']),
 act('s7','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'cr'},'to':'ok','res':'ok'},{'if':{'param':{'g':0}},'to':'ok','res':'ok'},{'to':'s7y','res':'fail'}],I6,want='cr',show=['crit','cdmg'],omens=['Omen_of_Abyssal_Echoes'],
     over=[{'param':{'g':0},'set':{'omens':[],'goal':K('훼손 옵션 확인 (나오는 대로)','Reveal (keep what comes)')}}]),
 LIGHTX('s7y',[1,6],'s6'),
 done([0,7])]
graph8('diztoh-endgame-quarterstaff-v2','Quarterstaves','Sinister Quarterstaff',82,
  'Diztoh 엔드게임 육척봉(원본 레시피 기록) — 근접 스킬 +5 분열 + 잡옵 → 상위 카오스 오브(물리 접두) → 좌측 찬미 + 완벽한 엑잘(물리 %·복합, 하이엔드는 빗나가면 좌측 소멸의 징조) → 좌측 찬미 + 완벽한 엑잘(복합·화염 추가, 하이엔드는 빗나가면 절사 + 좌측 말소 + 완벽한 카오스) → 완벽한 엑잘(접미, 하이엔드는 빗나가면 우측 말소 + 카오스) → 우측 강령술 + 고대 턱뼈 → 공개(치명타, 빗나가면 빛의 징조 — 영상의 우측 소멸의 징조는 접미 좋은 옵션도 지울 수 있어 바꿈). 밸런스 = 물리 % 1~3티어, 상위 엑잘, 빗나가도 그대로.',
  {'xT':{'kr':'물리 %·복합','en':'% physical / hybrid','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'sT':{'kr':'치명타 확률·피해','en':'Crit chance / damage','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'g':{'kr':'마지막 접두·접미','en':'Last prefix and suffix','values':TV({'1':('목표 옵션까지 반복','Repeat until the wanted line'),'0':('랜덤 옵션','Random line')})}},P,
  {'high':K('1티어까지, 빗나가면 소멸·말소 징조로 다시','To T1, Annulment/Erasure omens on misses'),'bal':K('1~2티어, 상위 엑잘, 마지막 접두·접미는 랜덤 옵션','T1–2, Greater Exalts, the last prefix and suffix random')},
  tags,nodes,[{'id':'L1','nodes':['s6','s7','s7y'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'p1'},{'tag':'pp'},{'tag':'p3'} if v=='high' else {'side':'p','random':True},{'tag':'melee','tmax':1,'fr':True},{'tag':'suf'},{'tag':'cr'} if v=='high' else {'side':'s','random':True}]),
  {'quality':20,'sockets':2},{'all':[{'has':'melee'},{'has':'p1'},{'any':[{'has':'cr'},{'param':{'g':0}}]},{'full':'p'},{'full':'s'}]},('high','bal'))
print('wrote 5 graphs (batch 8)')
