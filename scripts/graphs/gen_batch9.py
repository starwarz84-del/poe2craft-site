# Flowcharts for the remaining recipes, easiest first (사용자 2026-11-10: "플로우차트로 작성되지 않은 리스트를 쉬운 것부터 차례대로").
# Batch 9 = the four 보통(2) jewels → Balance + Essential (정책 30). Jewel modifiers all weigh the same (사용자 확정 2026-11-10), so the flat weights are real.
#   lilbotq-emerald-v2, zenm-timelost-sapphire-v2, diztoh-5mod-emerald-v2, diztoh-5mod-sapphire-v2
# Sim additions: graph cap (jewels 2/2), liquid lines through act 'essence' + liquid:true (not crafted), `alt` = the other 50/50 result,
# tag `slot` (+1 suffix / prefix allowed), and Chaos on an over-limit item only rerolls the other side (Diztoh: "카오스 오브가 접두만 바꿈").
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch8.py').read(); exec(_src[:_src.index('# ---------- 1. 라그나')])
def graph9(*a, **k):
    graph8(*a, **{x:y for x,y in k.items() if x!='cap'})
    g=json.load(open(f'{H}/{a[0]}.json')); g['cap']=k.get('cap',{'p':2,'s':2}); json.dump(g,open(f'{H}/{a[0]}.json','w'),ensure_ascii=False,indent=1)
def LIQ(id,pos,cur,tag,goal,shw,edges,item,**kw): return act(id,'main',pos,'essence',cur,goal,shw,K('액체','Liquid'),edges,item,ess=tag,liquid=True,**kw)
CS=it('p','+1 접미 허용','+1 suffix allowed',['contS']); FE=it('p','접미 효과 증가','Increased effect of suffixes',['fer'])
KEEP_E={'bal':K('영상: 빛의 징조로 다시 공개, 좌측 소멸의 징조로 경멸 옵션 제거, 카오스 오브로 좋은 접두 → 액체 흉포함','Video: Light retries, Sinistral Annulment for the contempt line, Chaos for a good prefix, then Ferocity'),
        'ess':K('공개 결과 그대로, 경멸 옵션은 두고 액체 흉포함 한 번','Keep the reveal, leave the contempt line, Ferocity once')}

def jewel5(gid, cls, bse, ilvl, note, start, startLbl, I0, pre_nodes, sufTags, revTag, revShow, preTag, preShow, extra_tags, sufLines, preLine, contGi, fer, failRoute=None, necro=False):
    """Shared 5-mod jewel flow: [suffix steps] → prefixes full → Potent Liquid Contempt (+1 suffix 50/50) → Preserved Cranium → reveal
       → (Balance) Sinistral Annulment until the contempt line goes → Exalt → Chaos for a good prefix → Ferocity."""
    P={'bal':{'v':1},'ess':{'v':2}}
    tags=dict(extra_tags); tags.update({'contS':{'gi':contGi[0],'slot':{'s':1}},'contP':{'gi':contGi[1],'slot':{'p':1}},'fer':{'gi':fer}})
    SUF=[it('s',kr,en,[t]) for t,kr,en in sufLines]
    I4=SUF+[J('p'),CS]; I5=I4+[UN('s')]; I6=SUF+[it('s','공개 접미','Revealed suffix',[revTag]),J('p'),CS]; I7=I6[:-1]
    I8=I7+[J('p')]; I9=I6[:len(SUF)+1]+[it('p','좋은 접두','Good prefix',[preTag]),J('p')]; I10=I6[:len(SUF)+1]+[it('p','좋은 접두','Good prefix',[preTag]),FE]
    nodes=[base('ms',start,startLbl,I0), mark([0,0.6],pre_nodes[0]['id'] if pre_nodes else 'c1',I0)]+pre_nodes+[
     LIQ('c1',[0,3],'Potent_Liquid_Contempt','contS',K('위력적인 액체 경멸 (50%로 +1 접미 허용)','Potent Liquid Contempt (50%: +1 suffix allowed)'),[st('p','+1 접미 허용 (아니면 +1 접두 허용 → 접미가 지워짐)','+1 suffix allowed (else +1 prefix allowed takes a suffix)')],
         [{'if':{'has':'contS'},'to':'c2','res':'ok'}]+([{'if':{'has':failRoute[1]},'to':'c1x','res':'fail'}] if failRoute and failRoute[0]=='keep' else [{'to':'c1x','res':'fail'}] if failRoute else [])+[{'to':'h1','res':'fail','port':'right'}],I4,alt='contP'),
     # 사용자 확정 2026-11-10 + 영상: a failed contempt → plain Orb of Annulment (prefixes are still junk) until +1 prefix allowed goes, then that suffix step again;
     # Diztoh sapphire video: annul everything down and chaos for the suffix again
     *([annul('c1x',[1,3],[{'if':{'not':{'has':failRoute[1]}},'to':failRoute[2],'port':'right'},{'if':{'has':'contP'},'to':'c1x'},{'to':failRoute[3],'port':'right'}],omens=(),target=K('+1 접두 허용 옵션 지우기 (접두는 잡옵뿐 — 공격 치명타 피해가 지워지면 새 베이스)','Remove +1 prefix allowed (prefixes are junk — losing crit damage means a new base)'))] if failRoute and failRoute[0]=='keep' else
       [cleanup('c1x',[1,3],[],[{'to':failRoute[2],'port':'right'}],K('소멸의 오브로 모두 지우고 접미부터 다시 (영상)','Annul everything and chaos for the suffix again (video)'))] if failRoute else []),
     act('c2','main',[0,4],'desecrate','Preserved_Cranium',K('접미 세번째 옵션(훼손)','Third suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'c3'}],I5,**({'omens':['Omen_of_Dextral_Necromancy']} if necro else {})),
     act('c3','main',[0,5],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
         [{'if':{'added':revTag},'to':'c4','res':'ok'},{'if':{'param':{'v':1}},'to':'c3x','res':'fail'},{'to':'c4','res':'fail'}],I6,want=revTag,show=revShow,omens=['Omen_of_Abyssal_Echoes'],
         over=[{'param':{'v':2},'set':{'edges':[{'if':{'added':revTag},'to':'f1','res':'ok'},{'to':'f1','res':'fail'}]}}]),
     LIGHTX('c3x',[1,5],'c2'),
     act('c4','main',[0,6],'annul','Orb_of_Annulment',K('+1 접미 허용 옵션 제거 (접두 옵션 2개 중 하나)','Remove the +1 suffix line (one of the two prefixes)'),None,K('소멸','Annul'),
         [{'if':{'has':'contS'},'to':'c4e','res':'fail'},{'to':'c5','res':'ok'}],I7,omens=['Omen_of_Sinistral_Annulment']),
     # LilBotQ: a missed Sinistral Annulment leaves +1 suffix allowed as the only prefix → Sinistral Erasure + Chaos Orb takes it
     act('c4e','main',[1,6],'chaos','Chaos_Orb',K('남은 +1 접미 허용 옵션 바꾸기','Reroll the remaining +1 suffix line'),[st('p','랜덤 옵션 1개 (접두가 그 옵션뿐이라 확정)','One random line (it is the only prefix, so it is sure)')],K('카오스','Chaos'),[{'to':'c5','port':'right'}],I8,omens=['Omen_of_Sinistral_Erasure']),
     act('c5','main',[0,7],'exalt','Exalted_Orb',K('접두 두번째 옵션','Second prefix'),[st('p','랜덤 옵션 1개 (접미가 한도를 넘어 접두로만)','One random line (suffixes are over the limit)')],K('엑잘','Exalt'),[{'to':'c6'}],I8),
     act('c6','main',[0,8],'chaos','Chaos_Orb',K('좋은 접두 (접미가 한도를 넘어 접두만 바뀜)','A good prefix (only prefixes change)'),None,K('카오스','Chaos'),
         [{'if':{'has':preTag},'to':'f1','res':'ok'},{'to':'c6','res':'fail'}],I9,show=preShow),
     LIQ('f1',[0,9],'Potent_Liquid_Ferocity','fer',K('위력적인 액체 흉포함 (접두 하나가 지워짐)','Potent Liquid Ferocity (one prefix goes)'),[st('p','접미 효과 증가','Increased effect of suffixes')],
         [{'if':{'param':{'v':2}},'to':'ok','res':'ok'},{'if':{'has':preTag},'to':'ok','res':'ok'},{'to':'c6','res':'fail','port':'right'}],I10),
     done([0,10])]
    return P,tags,nodes,[{'id':'L1','nodes':['c2','c3','c3x'],'kr':'훼손 공개','en':'Reveal'},{'id':'L3','nodes':['c6','f1'],'kr':'흉포함','en':'Ferocity'}]

# ---------- 1. LilBotQ 에메랄드 (Hcb_HcWDUOA) ----------
tg={'critD':{'gi':5},'ms':{'gi':45},'critA':{'gi':4},'as':{'gi':7},'rev':{'anyOf':['critA','as'],'label':K('공격 치명타 확률·공격 속도','Attack crit chance or attack speed')},'atk':{'gi':6}}
I0=[it('s','공격 치명타 피해 보너스','Attack crit damage bonus',['critD']),it('s','이동 속도','Movement speed',['ms']),J('p'),J('p')]
P,tags,nodes,loops=jewel5('lilbotq-emerald-v2','Emerald','Emerald',82,'',{'rar':'rare','mods':['critD','ms',{'junk':'p'},{'junk':'p'}]},K('공격 치명타 피해 + 이동 속도 접미, 접두 옵션 2개 희귀 에메랄드 구입','Buy a rare Emerald: attack crit damage + movement speed, two prefixes'),I0,
   [],None,'rev',['critA','as'],'atk',['atk'],tg,[('critD','공격 치명타 피해 보너스','Attack crit damage bonus'),('ms','이동 속도','Movement speed')],None,(119,120),117,necro=True)
# Essential = the video's budget route (Hcb_HcWDUOA 3:35~): a cheap jewel with three good lines (two prefixes + one suffix) and one junk suffix,
# then Concentrated Liquid Fear (crafted attack crit damage, a suffix: one of the two suffixes goes, 50/50). A miss = buy another cheap jewel.
tags.update({'critX':{'gi':113},'pg':{'gi':6}})
nodes[0]['over']=[{'param':{'v':2},'set':{'start':{'rar':'rare','mods':['as',{'junk':'s'},'pg',{'junk':'p'}]},'next':'b1',
    'label':K('좋은 접두 2개 + 공격 속도 + 잡옵 접미 희귀 에메랄드 구입 (약 1 카오스)','Buy a cheap rare Emerald: two good prefixes + attack speed + a junk suffix (about 1 Chaos)'),
    'item':[it('p','좋은 접두','Good prefix',['pg']),it('p','좋은 접두','Good prefix'),it('s','공격 속도','Attack speed',['as']),J('s')]}}]
nodes.insert(2, LIQ('b1',[0,1.5],'Concentrated_Liquid_Fear','critX',K('농축된 액체 두려움 (접미 2개 중 하나가 지워짐)','Concentrated Liquid Fear (one of the two suffixes goes)'),[st('s','공격 치명타 피해 보너스 (제작 옵션)','Attack crit damage bonus (crafted)')],
    [{'if':{'all':[{'has':'as'},{'has':'critX'}]},'to':'ok','res':'ok'},{'to':'h1','res':'fail','port':'right'}],[it('p','좋은 접두','Good prefix',['pg']),it('p','좋은 접두','Good prefix'),it('s','공격 속도','Attack speed',['as']),it('s','공격 치명타 피해 보너스 (제작)','Attack crit damage bonus (crafted)',['critX'])]))
graph9('lilbotq-emerald-v2','Emerald','Emerald',82,
  'LilBotQ 에메랄드(원본 레시피 기록) — 공격 치명타 피해 + 이동 속도 접미 + 접두 옵션 2개 구입 → 위력적인 액체 경멸(+1 접미 허용 50%, 아니면 새 주얼) → 보존된 두개골 → 공개(공격 치명타 확률·공격 속도) → 좌측 소멸의 징조로 경멸 옵션 제거 → 엑잘 → 카오스 오브(공격 피해 접두) → 위력적인 액체 흉포함.',
  {'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,{'bal':KEEP_E['bal'],'ess':K('영상의 가성비 방법: 좋은 옵션 3개 주얼 + 농축된 액체 두려움 (4옵션)','The video’s budget route: a three-good-line jewel + Concentrated Liquid Fear (four lines)')},tags,nodes,loops,
  FIN(('bal','ess'),lambda v:[{'tag':'atk','tmax':1},{'tag':'fer','tmax':1},{'tag':'critD','tmax':1},{'tag':'ms','tmax':1},{'side':'s','label':K('공격 치명타 확률·공격 속도','Attack crit chance or attack speed')}] if v=='bal' else [{'side':'p','label':K('좋은 접두','Good prefix')},{'side':'p','label':K('좋은 접두','Good prefix')},{'tag':'as','tmax':1},{'tag':'critX','tmax':1}]),
  {'quality':0,'sockets':0},{'any':[{'all':[{'has':'critD'},{'has':'ms'},{'has':'fer'}]},{'all':[{'has':'as'},{'has':'critX'}]}]},('bal','ess'))

# ---------- 2. Diztoh 5옵션 에메랄드 (s70CV_nvjXg) ----------
tg={'critD':{'gi':5},'qas':{'gi':55},'as':{'gi':7},'asAny':{'anyOf':['qas','as'],'label':K('공격 속도 (육척봉 포함)','Attack speed (or with quarterstaves)')},'atk':{'gi':6},'qd':{'gi':53},'pre':{'anyOf':['atk','qd'],'label':K('공격 피해·육척봉 피해','Attack or quarterstaff damage')}}
I0=[it('s','공격 치명타 피해 보너스','Attack crit damage bonus',['critD']),J('p')]
pre=[act('e2','main',[0,1],'exalt','Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),[{'if':{'has':'asAny'},'to':'e3','res':'ok'},{'to':'e2x','res':'fail'}],I0+[it('s','공격 속도','Attack speed',['asAny'])],show=['qas','as'],omens=['Omen_of_Dextral_Exaltation']),
     cleanup('e2x',[1,1],['critD','asAny'],[{'lost':'critD','to':'h1','port':'right'},{'to':'e2','port':'bottom'}],K('빗나간 접미 지우기','Remove the missed suffix')),
     act('e3','main',[0,2],'exalt','Exalted_Orb',K('접두 두번째 옵션','Second prefix'),[st('p','랜덤 옵션 1개','One random line')],K('엑잘','Exalt'),[{'if':{'full':'p'},'to':'c1'},{'to':'e3','hide':True}],I0+[it('s','공격 속도','Attack speed',['asAny']),J('p')])]
P,tags,nodes,loops=jewel5('diztoh-5mod-emerald-v2','Emerald','Emerald',80,'',{'rar':'rare','mods':['critD',{'junk':'p'}]},K('공격 치명타 피해 접미 + 잡옵 1개 희귀 에메랄드','Rare Emerald: attack crit damage suffix + one junk line'),I0,
   pre,None,'asAny',['qas','as'],'pre',['atk','qd'],tg,[('critD','공격 치명타 피해 보너스','Attack crit damage bonus'),('asAny','공격 속도','Attack speed')],None,(119,120),117,failRoute=('keep','critD','h1','e2'))
graph9('diztoh-5mod-emerald-v2','Emerald','Emerald',80,
  'Diztoh 5옵션 에메랄드(원본 레시피 기록) — 공격 치명타 피해 + 잡옵 → 우측 찬미 + 엑잘(공격 속도, 빗나가면 소멸의 오브) → 엑잘(접두) → 위력적인 액체 경멸 → 보존된 두개골 → 공개(공격 속도) → 좌측 소멸의 징조로 경멸 옵션 제거 → 엑잘 → 카오스 오브(공격·육척봉 피해) → 위력적인 액체 흉포함. 제련된 강탈자 기폭제(퀄리티)는 마무리라 시뮬에서 뺌.',
  {'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,KEEP_E,tags,nodes,loops,
  FIN(('bal','ess'),lambda v:([{'side':'p','label':K('공격·육척봉 피해','Attack or quarterstaff damage')},{'tag':'fer','tmax':1}] if v=='bal' else [{'side':'p','label':K('+1 접미 허용 또는 랜덤','+1 suffix allowed or random')},{'tag':'fer','tmax':1}])+[{'tag':'critD','tmax':1},{'side':'s','label':K('공격 속도','Attack speed')},{'side':'s','label':K('공격 속도','Attack speed')} if v=='bal' else {'side':'s','random':True}]),
  {'quality':20,'sockets':0},{'all':[{'has':'critD'},{'has':'asAny'},{'has':'fer'}]},('bal','ess'))

# ---------- 3. Diztoh 5옵션 사파이어 (-YZm55-QuoQ) ----------
tg={'scrit':{'gi':48},'crit':{'gi':10},'cdmg':{'gi':11},'critAny':{'anyOf':['scrit','crit','cdmg'],'label':K('치명타 접미','Crit suffix')},'cast':{'gi':3},'rev':{'anyOf':['cast','cdmg','scrit'],'label':K('시전 속도·치명타','Cast speed or crit')},
    'cold':{'gi':6},'spell':{'gi':49},'ele':{'gi':20},'pre':{'anyOf':['cold','spell','ele'],'label':K('냉기·주문·원소 피해','Cold, spell or elemental damage')}}
I0=[J('s')]; C1=it('s','치명타 접미','Crit suffix',['critAny'])
pre=[act('j1','main',[0,1],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'critAny'},'to':'j2','res':'ok'},{'to':'j1','res':'fail'}],[C1],show=['scrit','crit','cdmg']),
     act('j2','main',[0,1.5],'exalt','Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),[{'if':{'count':{'tag':'critAny','min':2}},'to':'j3','res':'ok'},{'to':'j2x','res':'fail'}],[C1,C1],show=['scrit','crit','cdmg'],omens=['Omen_of_Dextral_Exaltation']),
     cleanup('j2x',[1,1.5],['critAny'],[{'lost':'critAny','to':'j1','port':'right'},{'to':'j2','port':'bottom'}],K('빗나간 접미 지우기','Remove the missed suffix')),
     act('j3','main',[0,2],'exalt','Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 2개 (엑잘티드 오브 2개)','Two random lines (two Exalted Orbs)')],K('엑잘','Exalt'),[{'to':'c1'}],[C1,C1,J('p'),J('p')],omens=['Omen_of_Greater_Exaltation'])]
P,tags,nodes,loops=jewel5('diztoh-5mod-sapphire-v2','Sapphire','Sapphire',82,'',{'rar':'rare','mods':[{'junk':'s'}]},K('희귀 사파이어 (소멸의 오브로 옵션 1개만 남김)','Rare Sapphire (annulled down to one line)'),I0,
   pre,None,'rev',['cast','cdmg','scrit'],'pre',['cold','spell','ele'],tg,[('critAny','치명타 접미','Crit suffix'),('critAny','치명타 접미','Crit suffix')],None,(103,104),101,failRoute=('all',None,'j1'))
for n in nodes:
    if n['id']=='c5': n['cur']='Greater_Exalted_Orb'
graph9('diztoh-5mod-sapphire-v2','Sapphire','Sapphire',82,
  'Diztoh 5옵션 사파이어(원본 레시피 기록) — 카오스 오브(치명타 접미) → 우측 찬미 + 엑잘(다른 치명타, 빗나가면 소멸의 오브) → 접두 옵션 2개(영상은 엑잘 2개, 그림은 상위 찬미로 표시) → 위력적인 액체 경멸 → 보존된 두개골 → 공개(시전 속도) → 좌측 소멸의 징조로 경멸 옵션 제거 → 상위 엑잘 → 카오스 오브(냉기·주문·원소 피해) → 위력적인 액체 흉포함.',
  {'v':{'kr':'진행','en':'Route','values':TV({'1':('영상','Video'),'2':('결과 그대로','As it comes')})}},P,KEEP_E,tags,nodes,loops,
  FIN(('bal','ess'),lambda v:([{'side':'p','label':K('냉기·주문·원소 피해','Cold, spell or elemental damage')},{'tag':'fer','tmax':1}] if v=='bal' else [{'side':'p','label':K('+1 접미 허용 또는 랜덤','+1 suffix allowed or random')},{'tag':'fer','tmax':1}])+[{'side':'s','label':K('치명타 접미','Crit suffix')},{'side':'s','label':K('치명타 접미','Crit suffix')},{'side':'s','label':K('시전 속도·치명타','Cast speed or crit')} if v=='bal' else {'side':'s','random':True}]),
  {'quality':20,'sockets':0},{'all':[{'count':{'tag':'critAny','min':2}},{'has':'fer'}]},('bal','ess'))

# ---------- 4. Zen_M 오래된 사파이어 (IKC9DquM7GM) ----------
# 원본: 옵션 1개 매직 오래된 사파이어 → 제왕의 오브 → 소멸의 오브로 옵션 1개만 → 카오스 오브(치명타 계열 핵심 패시브 접미) → 우측 강령술 + 보존된 두개골 → 공개(다른 하나) → 엑잘 2번(접두) → 고대 위력적인 액체 우울(접두 하나를 지우고 범위 아주 큼).
P={'bal':{'v':1},'ess':{'v':2}}
NOT=[16,15,50,14,40,41]
tags={**{f'n{g}':{'gi':g} for g in NOT},'note':{'anyOf':[f'n{g}' for g in NOT],'label':K('치명타 계열 핵심 패시브','Crit notable line')},'rad':{'gi':82}}
NL=it('s','치명타 계열 핵심 패시브','Crit notable line',['note']); RD=it('p','범위 아주 큼','Very large radius',['rad'])
I0=[J('s')]; I1=[J('s'),J('p')]; I2=[J('s')]; I3=[NL]; I4=[NL,UN('s')]; I5=[NL,NL]; I6=I5+[J('p'),J('p')]; I7=I5+[J('p'),RD]
nodes=[base('z2',{'rar':'magic','mods':[{'junk':'s'}]},K('옵션 1개 매직 오래된 사파이어 (아이템 레벨 41)','Magic Time-Lost Sapphire with one line (item level 41)'),I0),
 act('z2','prep',[0,1],'regal','Regal_Orb',K('레어로','To rare'),[st(None,'랜덤 옵션 1개','One random line')],K('제왕','Regal'),[{'to':'z2x'}],I1),
 dict(cleanup('z2x',[0,2],[],[{'to':'ms'}],K('옵션 1개만 남기기','Keep one line'),maxJunk=1),group='prep'),
 mark([0,2.6],'z3',I2),
 act('z3','main',[0,3],'chaos','Chaos_Orb',K('접미 첫번째 옵션','First suffix'),None,K('카오스','Chaos'),[{'if':{'has':'note'},'to':'z4','res':'ok'},{'to':'z3','res':'fail'}],I3,show=[f'n{g}' for g in NOT]),
 act('z4','main',[0,4],'desecrate','Preserved_Cranium',K('접미 두번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'z5'}],I4,omens=['Omen_of_Dextral_Necromancy']),
 act('z5','main',[0,5],'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
     [{'if':{'added':'note'},'to':'z6','res':'ok'},{'if':{'param':{'v':1}},'to':'z5x','res':'fail'},{'to':'z6','res':'fail'}],I5,want='note',show=[f'n{g}' for g in NOT],omens=['Omen_of_Abyssal_Echoes']),
 annul('z5x',[1,5],[{'if':{'has':'note'},'to':'z4','port':'right'},{'to':'z3','port':'right'}],omens=(),target=K('징조 없는 소멸의 오브 (1/2로 훼손 옵션, 좋은 접미가 지워지면 카오스 오브부터)','Plain Orb of Annulment (1/2 the desecrated line; the good suffix gone: Chaos again)')),   # Zen_M 영상 6:17: 빛의 징조 없이 그냥 소멸의 오브
 act('z6','main',[0,6],'exalt','Exalted_Orb',K('접두 옵션 2개','Two prefixes'),[st('p','랜덤 옵션 2개 (엑잘티드 오브 2개)','Two random lines (two Exalted Orbs)')],K('엑잘','Exalt'),[{'to':'z7'}],I6,omens=['Omen_of_Greater_Exaltation']),
 LIQ('z7',[0,7],'Ancient_Potent_Liquid_Melancholy','rad',K('고대 위력적인 액체 우울 (접두 하나가 지워짐)','Ancient Potent Liquid Melancholy (one prefix goes)'),[st('p','범위 아주 큼','Very large radius')],[{'to':'ok'}],I7),
 done([0,8])]
graph9('zenm-timelost-sapphire-v2','Time-Lost_Sapphire','Time-Lost Sapphire',41,
  'Zen_M 오래된 사파이어(원본 레시피 기록) — 옵션 1개 매직 → 제왕의 오브 → 소멸의 오브로 옵션 1개만 → 카오스 오브(치명타 계열 핵심 패시브) → 우측 강령술 + 보존된 두개골 → 공개(밸런스 = 빗나가면 징조 없는 소멸의 오브 — 1/2로 좋은 접미가 지워지면 카오스 오브부터, 영상) → 엑잘 2번 → 고대 위력적인 액체 우울. 오래된',
  {'v':{'kr':'진행','en':'Route','values':TV({'1':('영상 (소멸의 오브로 다시)','Video (Annulment retry)'),'2':('공개 결과 그대로','Keep the reveal')})}},P,
  {'bal':K('영상: 공개가 빗나가면 징조 없는 소멸의 오브(1/2)','Video: a plain Annulment on a missed reveal (1/2)'),'ess':K('공개 결과 그대로','Keep the reveal')},tags,nodes,[{'id':'L1','nodes':['z4','z5','z5x'],'kr':'훼손 공개','en':'Reveal'}],
  FIN(('bal','ess'),lambda v:[{'side':'p','random':True},{'tag':'rad','tmax':1},{'side':'s','label':K('치명타 계열 핵심 패시브','Crit notable line')},{'side':'s','label':K('치명타 계열 핵심 패시브','Crit notable line')} if v=='bal' else {'side':'s','random':True}]),
  {'quality':0,'sockets':0},{'all':[{'has':'note'},{'has':'rad'}]},('bal','ess'))
print('wrote 4 graphs (batch 9)')
