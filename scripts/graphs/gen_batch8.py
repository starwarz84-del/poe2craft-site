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
 act('g5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션 (시전 속도 1차 도전)','Second suffix (first try at cast speed)'),[st('s','랜덤 옵션 1개 — 시전 속도면 좋음','One random line — cast speed is good')],K('엑잘','Exalt'),[{'to':'g5b'}],I3,omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation']),
 act('g5b','main',[0,5],'quality','Skittering_Catalyst',K('속도 퀄리티 다시 40%','Speed quality back to 40%'),[st(None,'달리는 기폭제 40개 (촉진으로 0%가 됨)','40 Skittering Catalysts (Catalysing used it up)')],K('퀄리티','Quality'),[{'to':'g6'}],I3,count=40),
 act('g6','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'cast'},'to':'g7','res':'ok'},{'if':{'param':{'cT':2}},'to':'g6x','res':'fail'},{'to':'g7','res':'fail'}],I4,show=['cast'],omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation']),
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
# 원본: 번개 피해 추가 1티어 분열 + 잡옵 → 카오스 오브(공격 치명타 확률·치명타 피해·투사체 스킬 +1) → 우측 찬미 + 완벽한 엑잘(다른 하나, 빗나가면 소멸의 오브)
# → 우측 강령술 + 보존된 턱뼈 → 완벽한 엑잘 2번(투사체 속도·활 피해 1티어, 빗나가면 좌측 소멸의 징조 + 소멸의 오브) → 공개(남은 하나, 빛의 징조로 다시).
P={'high':{'cT':1,'dT':2,'pT':1},'bal':{'cT':2,'dT':3,'pT':2}}
tags={'light':{'gi':8,'tmax':1},'critA':{'gi':14,'tmax':'$cT'},'critD':{'gi':15,'tmax':'$dT'},'proj':{'gi':9},
      'suf':{'anyOf':['critA','critD','proj'],'label':K('공격 치명타 확률·치명타 피해·투사체 스킬 +1','Attack crit chance, crit damage or +1 projectile skills')},
      'pspd':{'gi':18,'tmax':'$pT'},'bow':{'gi':19,'tmax':'$pT'},'pre':{'anyOf':['pspd','bow'],'label':K('투사체 속도·활 스킬 피해','Projectile speed or bow damage')}}
LF=it('p','번개 피해 추가 (분열)','Flat lightning (fractured)',['light']); SU=lambda: it('s','치명타·투사체 접미','Crit or projectile suffix',['suf']); PR=lambda: it('p','투사체 속도·활 피해','Projectile speed or bow damage',['pre'])
I0=[LF,J('s')]; I1=[LF,SU()]; I2=I1+[SU()]; I3=I2+[UN('s')]; I4=[LF,PR()]+I3[1:]; I5=[LF,PR(),PR()]+I3[1:]; I6=[LF,PR(),PR(),SU(),SU(),SU()]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'light','fr':True},{'junk':'s'}]},K('번개 피해 추가 1티어 분열 + 잡옵 1개','Fractured T1 flat lightning + one junk line'),I0),
 mark([0,0.6],'q2',I0),
 act('q2','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix option'),None,K('카오스','Chaos'),[{'if':{'has':'suf'},'to':'q3','res':'ok'},{'to':'q2','res':'fail'}],I1,show=['critA','critD','proj']),
 act('q3','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix option'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'suf','min':2}},'to':'q4','res':'ok'},{'to':'q3x','res':'fail'}],I2,show=['critA','critD','proj'],omens=['Omen_of_Dextral_Exaltation']),
 cleanup('q3x',[1,2],['suf'],[{'lost':'suf','to':'q2','port':'right'},{'to':'q3','port':'bottom'}],K('빗나간 접미 지우기 (첫번째 접미는 유지)','Remove the missed suffix (keep the first)')),
 act('q4','main',[0,3],'desecrate','Preserved_Jawbone',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'q5'}],I3,omens=['Omen_of_Dextral_Necromancy']),
 act('q5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'pre'},'to':'q6','res':'ok'},{'if':{'param':{'pT':1}},'to':'q5x','res':'fail'},{'to':'q6','res':'fail'}],I4,show=['pspd','bow']),
 cleanup('q5x',[1,4],['pre'],[{'to':'q5','port':'bottom'}],K('빗나간 접두 지우기','Remove the missed prefix'),side='p'),
 act('q6','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre','min':2}},'to':'q7','res':'ok'},{'if':{'param':{'pT':1}},'to':'q6x','res':'fail'},{'to':'q7','res':'fail'}],I5,show=['pspd','bow']),
 cleanup('q6x',[1,5],['pre'],[{'lost':'pre','to':'q5','port':'right'},{'to':'q6','port':'bottom'}],K('빗나간 접두 지우기 (앞의 접두는 유지)','Remove the missed prefix (keep the first)'),side='p'),
 act('q7','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'suf'},'to':'ok','res':'ok'},{'to':'q7x','res':'fail'}],I6,want='suf',show=['critA','critD','proj'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('q7x',[1,6],'q7d'),
 act('q7d','main',[1,6.6],'desecrate','Preserved_Jawbone',K('다시 훼손','Desecrate again'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'q7','port':'right'}],I5),
 done([0,7])]
graph8('noble-visceral-quiver-v2','Quivers','Visceral Quiver',82,
  '노블이 본능적인 화살통(원본 레시피 기록, 0.4 영상을 0.5.5 방식으로 응용) — 번개 피해 추가 분열 + 잡옵 → 카오스 오브(치명타·투사체 접미) → 우측 찬미 + 완벽한 엑잘(다른 하나, 빗나가면 소멸의 오브) → 우측 강령술 + 보존된 턱뼈 → 완벽한 엑잘 2번(투사체 속도·활 피해) → 공개(남은 접미, 빛의 징조로 다시). 하이엔드 = 영상(접두 1티어, 빗나가면 좌측 소멸의 징조), 밸런스 = 1~2티어 목표, 접두 엑잘은 결과 그대로.',
  {'cT':{'kr':'공격 치명타 확률','en':'Attack crit chance','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'dT':{'kr':'치명타 피해','en':'Crit damage','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})},'pT':{'kr':'접두 (투사체 속도·활 피해)','en':'Prefixes','values':TV({'1':('1티어 (좌측 소멸의 징조로 다시)','T1 (Sinistral Annulment retry)'),'2':('결과 그대로','As they come')})}},P,
  {'high':K('영상: 1티어까지 좌측 소멸의 징조로 다시','Video: Sinistral Annulment until T1'),'bal':K('1~2티어 목표, 접두는 결과 그대로','T1–2 targets, prefixes as they come')},
  tags,nodes,[{'id':'L1','nodes':['q7','q7x','q7d'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'light','tmax':1,'fr':True}]+([{'tag':'pspd','tmax':1},{'tag':'bow','tmax':1}] if v=='high' else [{'side':'p','label':K('투사체 속도·활 피해 (나오는 대로)','Projectile speed or bow damage (as it comes)')},{'side':'p','random':True}])+[{'tag':'critA','tmax':P[v]['cT']},{'tag':'critD','tmax':P[v]['dT']},{'tag':'proj','tmax':1}]),
  {'quality':20,'sockets':0},{'all':[{'has':'light'},{'count':{'tag':'suf','min':3}},{'full':'p'}]},('high','bal'))

# ---------- 3. 시한 하이엔드 투구 (CTrIbhQVU8U) ----------
# 원본: 생명력 최대치 1티어 분열 + 잡옵 → 카오스 오브(방어도 원소 적용 1티어·치명타 확률 1~2티어) → 우측 찬미 + 상위 찬미 + 완벽한 엑잘(다른 하나, 빗나가면 소멸의 오브)
# → 상위 카오스 오브(남은 잡옵을 저항으로) → 완벽한 엑잘(방어도 1티어) → 맞으면 고대 갈비뼈 → 공개(다른 방어도, 빛의 징조로 다시) / 빗나가면 좌측 결정화 + 심연의 에센스(징표) → 완벽한 엑잘 → 징표에 고대 갈비뼈 → 공개.
P={'high':{'aT':1,'rT':3},'bal':{'aT':2,'rT':4}}
tags={'life':{'gi':6,'tmax':1},'ele':{'gi':20,'tmax':1},'crit':{'gi':16,'tmax':2},'sGood':{'anyOf':['ele','crit'],'label':K('방어도 원소 적용·치명타 확률','Armour to elemental or crit chance')},
      'fire':{'gi':2,'tmax':'$rT'},'cold':{'gi':3,'tmax':'$rT'},'lres':{'gi':4,'tmax':'$rT'},'chaos':{'gi':5,'tmax':2},'res':{'anyOf':['fire','cold','lres','chaos'],'label':K('저항','Resistance')},
      'flat':{'gi':8,'tmax':'$aT'},'pct':{'gi':9,'tmax':'$aT'},'arm':{'anyOf':['flat','pct'],'label':K('방어도 최대치·%','Flat or % armour')},'mark':{'gi':47}}
LI=it('p','생명력 최대치 1티어 (분열)','T1 maximum life (fractured)',['life']); SG=lambda: it('s','방어도 원소 적용·치명타 확률','Armour to elemental or crit chance',['sGood'])
RS=it('s','저항','Resistance',['res']); AR=lambda: it('p','방어도 최대치·%','Flat or % armour',['arm']); MK=it('p','심연 군주의 징표','Mark of the Abyssal Lord',['mark'])
I0=[LI,J('s')]; I1=[LI,SG()]; I2=I1+[SG(),J('s')]; I3=[LI,SG(),SG(),RS]; I4=[LI,AR(),SG(),SG(),RS]; I5=I4[:2]+[UN('p')]+I4[2:]; I6=[LI,AR(),AR(),SG(),SG(),RS]
I7=[LI,J('p'),SG(),SG(),RS]; I8=[LI,MK,SG(),SG(),RS]; I9=[LI,MK,AR(),SG(),SG(),RS]; I10=[LI,UN('p'),AR(),SG(),SG(),RS]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'life','fr':True},{'junk':'s'}]},K('생명력 최대치 1티어 분열 + 잡옵 1개 (특출난 베이스, 소켓 2)','Fractured T1 maximum life + one junk line (exceptional, 2 sockets)'),I0),
 mark([0,0.6],'s1',I0),
 act('s1','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix option'),None,K('카오스','Chaos'),[{'if':{'has':'sGood'},'to':'s2','res':'ok'},{'to':'s1','res':'fail'}],I1,show=['ele','crit']),
 act('s2','main',[0,2],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix option'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'sGood','min':2}},'to':'s3','res':'ok'},{'to':'s2x','res':'fail'}],I2,show=['ele','crit'],omens=['Omen_of_Dextral_Exaltation','Omen_of_Greater_Exaltation'],
     over=[{'param':{'aT':2},'set':{'cur':'Greater_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation']}}]),
 cleanup('s2x',[1,2],['sGood'],[{'lost':'sGood','to':'s1','port':'right'},{'to':'s2','port':'bottom'}],K('빗나간 접미 지우기 (첫번째 접미는 유지)','Remove the missed suffix (keep the first)')),
 act('s3','main',[0,3],'chaos','Greater_Chaos_Orb',K('남은 접미 잡옵을 저항으로','The junk suffix into a resistance'),None,K('카오스','Chaos'),
     [{'if':{'all':[{'count':{'tag':'sGood','min':2}},{'has':'res'},{'sideLt':{'side':'p','n':2}}]},'to':'p1','res':'ok'},{'if':{'count':{'tag':'sGood','min':2}},'to':'s3','res':'fail'},{'to':'s2x','res':'fail'}],I3,show=['fire','cold','lres','chaos'],
     over=[{'param':{'aT':2},'set':{'act':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Dextral_Exaltation'],'goal':K('접미 세번째 옵션 (저항이면 좋음, 결과 그대로)','Third suffix (a resistance is good, keep it)'),'edges':[{'to':'p1'}]}}],
     ),
 act('p1','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접두 두번째 옵션','Second prefix'),None,K('엑잘','Exalt'),
     [{'if':{'added':'arm'},'to':'p2','res':'ok'},{'if':{'param':{'aT':1}},'to':'m1','res':'fail'},{'to':'p2','res':'fail'}],I4,show=['flat','pct']),
 act('p2','main',[0,5],'desecrate','Ancient_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'p3'}],I5),
 act('p3','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'arm'},'to':'ok','res':'ok'},{'to':'p3x','res':'fail'}],I6,want='arm',show=['flat','pct'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('p3x',[1,6],'p2'),
 act('m1','main',[2,4],'essence','Essence_of_the_Abyss',K('빗나간 접두를 징표로','The missed prefix into the Abyssal mark'),[st('p','심연 군주의 징표','Mark of the Abyssal Lord')],K('에센스','Essence'),[{'to':'m2'}],I8,ess='mark',mark=True,omens=['Omen_of_Sinistral_Crystallisation']),
 act('m2','main',[2,5],'exalt','Perfect_Exalted_Orb',K('접두 다시','The prefix again'),None,K('엑잘','Exalt'),[{'if':{'added':'arm'},'to':'m3','res':'ok'},{'to':'m2x','res':'fail'}],I9,show=['flat','pct']),
 act('m2x','main',[3,5],'desecrate','Preserved_Rib',K('징표를 훼손해 지울 준비','Desecrate the mark to clear it'),[st('p','징표 → 훼손 옵션(미공개), 빛의 징조 + 소멸의 오브로 제거','Mark → unrevealed, then Light + Annulment')],K('훼손','Desecrate'),[{'to':'m2y'}],I7,fromMark=True),
 annul('m2y',[3,5.6],[{'to':'m1','port':'right'}]),
 act('m3','main',[2,6],'desecrate','Ancient_Rib',K('징표에 훼손','Desecrate the mark'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'m4'}],I10,fromMark=True),
 act('m4','main',[2,7],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),[{'if':{'added':'arm'},'to':'ok','res':'ok'},{'to':'m4x','res':'fail'}],I6,want='arm',show=['flat','pct'],omens=['Omen_of_Abyssal_Echoes']),
 annul('m4x',[3,7],[{'to':'m4d','port':'right'}]),
 act('m4d','main',[3,7.6],'desecrate','Ancient_Rib',K('다시 훼손','Desecrate again'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'m4','port':'right'}],I10),
 done([0,8])]
graph8('sihan-highend-helmet-v2','Helmets_str','Imperial Greathelm',82,
  '시한 하이엔드 투구(원본 레시피 기록) — 생명력 1티어 분열 + 잡옵 → 카오스 오브(방어도 원소 적용·치명타 확률) → 우측 찬미 + 상위 찬미 + 완벽한 엑잘(다른 하나, 빗나가면 소멸의 오브) → 상위 카오스 오브(남은 잡옵을 저항으로) → 완벽한 엑잘(방어도) → 맞으면 고대 갈비뼈 훼손·공개, 빗나가면 좌측 결정화 + 심연의 에센스(징표) → 완벽한 엑잘 → 징표에 고대 갈비뼈 → 공개. 하이엔드 = 영상, 밸런스 = 상위 찬미 없이 상위 엑잘로 접미 하나씩(치명타 2티어 레벨 44도 후보)·저항은 엑잘 결과 그대로, 방어도 1~2티어, 접두 엑잘 빗나감은 그대로 두고 훼손 공개.',
  {'aT':{'kr':'방어도 접두','en':'Armour prefixes','values':TV({'1':('1티어 (징표로 다시)','T1 (Abyssal mark retry)'),'2':('1~2티어','T1–2')})},'rT':{'kr':'저항','en':'Resistance','values':TV({'3':('1~3티어 (상위 카오스)','T1–3 (Greater Chaos)'),'4':('엑잘 결과 그대로','Exalt, as it comes')})}},P,
  {'high':K('영상: 상위 찬미·상위 카오스·심연 징표','Video: Greater Exaltation, Greater Chaos, Abyssal mark'),'bal':K('접미 하나씩, 저항은 결과 그대로, 방어도 1~2티어','One suffix at a time, resistance as it comes, T1–2 armour')},
  tags,nodes,[{'id':'L1','nodes':['p2','p3','p3x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L2','nodes':['m1','m2','m2x','m2y'],'kr':'심연 징표','en':'Abyssal mark'}],
  FIN(('high','bal'),lambda v:[{'tag':'life','tmax':1,'fr':True},{'tag':'flat','tmax':P[v]['aT']},{'tag':'pct','tmax':P[v]['aT']},{'tag':'ele','tmax':1},{'tag':'crit','tmax':2},{'side':'s','label':K('저항 1~3티어','T1–3 resistance')} if v=='high' else {'side':'s','random':True}]),
  {'quality':20,'sockets':2},{'all':[{'has':'life'},{'count':{'tag':'sGood','min':2}},{'has':'arm'},{'full':'p'},{'full':'s'}]},('high','bal'))

# ---------- 4. Barricade 험악한 육척봉 (B4yShuKydt0) ----------
# 원본: 퀄리티 30%, 치명타 확률 5% 분열 + 잡옵 → 카오스 오브(근접 스킬 +5) → 우측 강령술 + 보존된 턱뼈 → 공개(공격 속도·치명타 피해 1티어, 빛의 징조로 다시)
# → 상위 찬미 + 완벽한 엑잘(접두 옵션 2개) → 절사의 징조 + 완벽한 카오스 오브로 원소 피해 접두 옵션 2개 → 완벽한 엑잘(세번째, 빗나가면 절사 카오스).
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
     [{'if':{'count':{'tag':'ele','min':2}},'to':'p4','res':'ok'},{'if':{'all':[{'param':{'eT':2}},{'count':{'tag':'ele','min':1}}]},'to':'p4','res':'ok'},{'to':'p2','res':'fail'}],I5,trim={'side':'p','keep':'keep'},
     over=[{'param':{'eT':2},'set':{'cur':'Greater_Chaos_Orb'}}]),
 act('p4','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'ele','min':3}},'to':'ok','res':'ok'},{'if':{'param':{'eT':1}},'to':'p5','res':'fail'},{'to':'ok','res':'fail'}],I6,show=['fire','cold','lflat']),
 act('p5','main',[0,7],'chaos','Perfect_Chaos_Orb',K('버릴 옵션을 원소 피해로','The junk line into elemental damage'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'ele','min':3}},'to':'ok','res':'ok'},{'to':'p5','res':'fail'}],I6,show=['fire','cold','lflat'],trim={'side':'p','keep':'keep'}),
 done([0,8])]
graph8('barricade-quarterstaff-v2','Quarterstaves','Sinister Quarterstaff',81,
  'Barricade 험악한 육척봉(원본 레시피 기록) — 치명타 확률 5% 분열 + 잡옵(퀄리티 30%) → 카오스 오브(근접 스킬 +5) → 우측 강령술 + 보존된 턱뼈 → 공개(공격 속도·치명타 피해, 빛의 징조로 다시) → 상위 찬미 + 완벽한 엑잘 → 절사의 징조 + 완벽한 카오스 오브로 원소 피해 접두 옵션 2개 → 완벽한 엑잘(세번째, 하이엔드는 빗나가면 절사 카오스 — 가장 낮은 옵션이 버릴 옵션일 때만). 하이엔드 = 영상(1티어), 밸런스 = 1~2티어 원소 피해 접두 옵션 1개까지 절사 + 상위 카오스 오브, 나머지 접두는 결과 그대로.',
  {'rT':{'kr':'공격 속도·치명타 피해','en':'Attack speed or crit damage','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'eT':{'kr':'원소 피해 접두','en':'Elemental prefixes','values':TV({'1':('1티어 옵션 3개 (완벽한 카오스)','Three T1 lines (Perfect Chaos)'),'2':('1~2티어 옵션 1개 이상 (상위 카오스)','At least one T1–2 line (Greater Chaos)')})}},P,
  {'high':K('영상: 원소 피해 1티어 옵션 3개','Video: three T1 elemental prefixes'),'bal':K('1~2티어 옵션 2개, 세번째는 결과 그대로','Two T1–2 lines, the third as it comes')},
  tags,nodes,[{'id':'L1','nodes':['q3','q4','q4x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'side':'p','label':K('원소 피해 접두','Elemental damage prefix')}]+([{'side':'p','label':K('원소 피해 접두','Elemental damage prefix')},{'side':'p','label':K('원소 피해 접두','Elemental damage prefix')}] if v=='high' else [{'side':'p','random':True},{'side':'p','random':True}])+[{'tag':'crit','tmax':1,'fr':True},{'tag':'melee','tmax':1},{'side':'s','label':K('공격 속도·치명타 피해','Attack speed or crit damage')}]),
  {'quality':30,'sockets':3},{'all':[{'has':'melee'},{'has':'rev'},{'has':'ele'},{'full':'p'}]},('high','bal'))

# ---------- 5. Diztoh 엔드게임 육척봉 (YfGJyBrObxI) ----------
# 원본: 근접 스킬 +5 분열 + 잡옵(퀄리티 20%) → 상위 카오스 오브(물리 피해 추가·물리 %·복합) → 좌측 찬미 + 완벽한 엑잘(다른 물리 %, 빗나가면 좌측 소멸의 징조)
# → 좌측 찬미 + 완벽한 엑잘(복합·화염 추가, 빗나가면 절사 + 좌측 말소 + 완벽한 카오스) → 완벽한 엑잘(접미, 빗나가면 우측 말소 + 카오스) → 우측 강령술 + 고대 턱뼈 → 공개(치명타, 빗나가면 우측 소멸의 징조).
P={'high':{'xT':2,'sT':2},'bal':{'xT':3,'sT':3}}
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
     [{'if':{'count':{'tag':'pre','min':2}},'to':'s4','res':'ok'},{'if':{'param':{'xT':2}},'to':'s3x','res':'fail'},{'to':'s4','res':'fail'}],I2,show=['ppct','hyb'],omens=['Omen_of_Sinistral_Exaltation']),
 cleanup('s3x',[1,2],['pre'],[{'lost':'pre','to':'s2','port':'right'},{'to':'s3','port':'bottom'}],K('빗나간 접두 지우기 (첫번째 접두는 유지)','Remove the missed prefix (keep the first)'),side='p'),
 act('s4','main',[0,3],'exalt','Perfect_Exalted_Orb',K('접두 세번째 옵션','Third prefix'),None,K('엑잘','Exalt'),
     [{'if':{'count':{'tag':'pre','min':3}},'to':'s5','res':'ok'},{'if':{'all':[{'param':{'xT':2}},{'whittleSafe':{'tag':'keepP','side':'p'}}]},'to':'s4b','res':'fail'},{'to':'s5','res':'fail'}],I3,show=['hyb','fire'],omens=['Omen_of_Sinistral_Exaltation'],
     over=[{'param':{'xT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('s4b','main',[1,3],'chaos','Perfect_Chaos_Orb',K('가장 낮은 접두를 다시 (버릴 옵션일 때만)','Reroll the lowest prefix (only while it is junk)'),None,K('카오스','Chaos'),
     [{'if':{'count':{'tag':'pre','min':3}},'to':'s5','res':'ok'},{'if':{'whittleSafe':{'tag':'keepP','side':'p'}},'to':'s4b','res':'fail'},{'to':'s5','res':'fail'}],I3,show=['hyb','fire'],omens=['Omen_of_Whittling','Omen_of_Sinistral_Erasure']),
 act('s5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),
     [{'if':{'has':'suf'},'to':'s6','res':'ok'},{'if':{'param':{'xT':2}},'to':'s5b','res':'fail'},{'to':'s6','res':'fail'}],I4,show=['as','crit','cdmg'],
     over=[{'param':{'xT':3},'set':{'cur':'Greater_Exalted_Orb'}}]),
 act('s5b','main',[1,4],'chaos','Chaos_Orb',K('접미를 다시','Reroll a suffix'),None,K('카오스','Chaos'),[{'if':{'has':'suf'},'to':'s6','res':'ok'},{'to':'s5b','res':'fail'}],I4,show=['as','crit','cdmg'],omens=['Omen_of_Dextral_Erasure']),
 act('s6','main',[0,5],'desecrate','Ancient_Jawbone',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'s7'}],I5,omens=['Omen_of_Dextral_Necromancy']),
 act('s7','main',[0,6],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'cr'},'to':'ok','res':'ok'},{'to':'s7y','res':'fail'}],I6,want='cr',show=['crit','cdmg'],omens=['Omen_of_Abyssal_Echoes']),
 LIGHTX('s7y',[1,6],'s6'),
 done([0,7])]
graph8('diztoh-endgame-quarterstaff-v2','Quarterstaves','Sinister Quarterstaff',82,
  'Diztoh 엔드게임 육척봉(원본 레시피 기록) — 근접 스킬 +5 분열 + 잡옵 → 상위 카오스 오브(물리 접두) → 좌측 찬미 + 완벽한 엑잘(물리 %·복합, 하이엔드는 빗나가면 좌측 소멸의 징조) → 좌측 찬미 + 완벽한 엑잘(복합·화염 추가, 하이엔드는 빗나가면 절사 + 좌측 말소 + 완벽한 카오스) → 완벽한 엑잘(접미, 하이엔드는 빗나가면 우측 말소 + 카오스) → 우측 강령술 + 고대 턱뼈 → 공개(치명타, 빗나가면 빛의 징조 — 영상의 우측 소멸의 징조는 접미 좋은 옵션도 지울 수 있어 바꿈). 밸런스 = 물리 % 1~3티어, 상위 엑잘, 빗나가도 그대로.',
  {'xT':{'kr':'물리 %·복합','en':'% physical / hybrid','values':TV({'2':('1~2티어 (다시 도전)','T1–2 (retry)'),'3':('1~3티어 (결과 그대로)','T1–3 (as it comes)')})},'sT':{'kr':'치명타 확률·피해','en':'Crit chance / damage','values':TV({'2':('1~2티어','T1–2'),'3':('1~3티어','T1–3')})}},P,
  {'high':K('영상: 빗나가면 소멸·말소 징조로 다시','Video: Annulment/Erasure omens on misses'),'bal':K('상위 엑잘, 빗나가도 그대로, 공개는 빛의 징조로','Greater Exalts, misses stay, Light on the reveal')},
  tags,nodes,[{'id':'L1','nodes':['s6','s7','s7y'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('high','bal'),lambda v:[{'tag':'ppct','tmax':P[v]['xT']},{'tag':'hyb','tmax':P[v]['xT']},{'side':'p','label':K('물리·화염 피해 추가','Flat physical or fire')} if v=='high' else {'side':'p','random':True},{'tag':'melee','tmax':1,'fr':True},{'side':'s','label':K('공격 속도·치명타','Attack speed or crit')} if v=='high' else {'side':'s','random':True},{'side':'s','label':K('치명타 확률·피해','Crit chance or damage')}]),
  {'quality':20,'sockets':2},{'all':[{'has':'melee'},{'has':'p1'},{'has':'cr'},{'full':'p'},{'full':'s'}]},('high','bal'))
print('wrote 5 graphs (batch 8)')
