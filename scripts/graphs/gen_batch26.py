# Batch 26 (사용자 2026-11-11: "재조합기가 없는 아이템은 레시피 작성해서 올리도록") — 웹 글 기반 0.5/0.5.5 제작법 6개
#   fubgun-quiver-v2 · fubgun-phys-bow-v2 · fubgun-crit-bow-v2 · fubgun-proj-amulet-v2 · fubgun-es-helmet-v2
#     (Fubgun 0.5.5 잔상 사격 데드아이 빌드 글의 Crafting Guide, mobalytics.gg/poe-2/builds/ice-shot-deadeye)
#   bigdaddy-lightning-wand-v2 (BigDaddyGaming 0.5 마법봉 글, mobalytics.gg/poe-2/profile/bigdaddygaming/guides/0-5-7-wand-crafting-guide)
# 글이라 영상보다 단계 설명이 짧음 → 빈 곳(베이스 이름, 공개 실패 처리)은 tools/notes/web-*.md에 가정으로 적음.
# 등급(정책 30·32): 쉬움·보통·어려움 → 밸런스(공개를 빛의 징조로 다시) + 에센셜(공개 결과 그대로).
import os, json
H=os.path.dirname(os.path.abspath(__file__))
_src=open(f'{H}/gen_batch22.py').read(); exec(_src[:_src.index('# ---------- 1. 시한')])
VB=VBE  # ('bal','ess')
def REVL(id,pos,want,show,ok,retry,item,omens=('Omen_of_Abyssal_Echoes',)):
    """공개: 밸런스(L=1)는 빗나가면 빛의 징조로 다시, 에센셜은 결과 그대로."""
    return act(id,'main',pos,'reveal',None,K('훼손 옵션 확인','Reveal the desecrated modifier'),None,K('공개','Reveal'),
      [{'if':{'added':want},'to':ok,'res':'ok'},{'if':{'param':{'L':1}},'to':retry,'res':'fail'},{'to':ok,'res':'fail','hide':True}],item,want=want,show=show,omens=list(omens))
RND=lambda s,n=1: it(s,f'랜덤 옵션 {n}개' if n>1 else '랜덤 옵션 1개',f'{n} random lines' if n>1 else 'One random line',None,'j')
LV=TV({'1':('빛의 징조로 다시','Retry with Omen of Light'),'0':('결과 그대로','Keep whatever comes')})

# ---------- 1. Fubgun 가성비 화살통 ----------
c='Quivers'
P={'bal':{'fT':1,'L':1,'gT':2},'ess':{'fT':2,'L':0,'gT':4}}
tags={'flat':{'gi':2,'tmax':'$fT'},'proj':{'gi':9},
      'gp':{'anyOf':[{'gi':4},{'gi':6},{'gi':8},{'gi':19}]},
      'gs':{'anyOf':[{'gi':14,'tmax':'$gT'},{'gi':12,'tmax':'$gT'},{'gi':24},{'gi':25}]}}
FL=itg('p',c,2,['flat']); PJ=itg('s',c,9,['proj'])
I0=[FL,PJ]; I1=I0+[it('p','공격에 화염·냉기·번개 피해 추가 또는 활 스킬 피해','Flat fire, cold or lightning, or bow skill damage',['gp'])]
I2=I1+[UN('s')]; I3=I1+[it('s','공격 치명타 확률 / 공격 속도 / 투사체 치명타 확률 / 투사체 2개 추가 발사','Attack crit / attack speed / projectile crit / two extra projectiles',['gs'])]
I4=I3+[RND('p'),RND('s')]
nodes=[base('q2',{'rar':'magic','mods':['flat','proj']},K('물리 피해 추가 + 투사체 스킬 레벨 +1 매직 화살통 구입','Buy a magic quiver with flat physical + projectile skills +1'),I0),
 act('q2','prep',[0,1],'regal','Perfect_Regal_Orb',K('레어로 업그레이드 + 접두 두번째 옵션','Upgrade to rare + second prefix'),[st('p','공격 원소 피해 추가 또는 활 스킬 피해 — 결과 그대로','Flat elemental or bow damage — keep whatever comes')],K('제왕','Regal'),[{'to':'ms'}],I1,omens=['Omen_of_Sinistral_Coronation'],show=['gp']),
 mark([0,1.5],'q3',I1),
 act('q3','main',[0,2],'desecrate','Preserved_Jawbone',K('접미 두번째 옵션(훼손)','Second suffix (desecrated)'),[st('s','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'q4'}],I2,omens=['Omen_of_Dextral_Necromancy']),
 REVL('q4',[0,3],'gs',['gs'],'q5','q4x',I3),
 annul('q4x',[1,3],[{'to':'q3','port':'right'}]),
 act('q5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('남은 접두·접미 1개씩','The last prefix and suffix'),[st(None,'랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I4,omens=['Omen_of_Greater_Exaltation'],
     over=[{'param':{'L':0},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,5])]
g22('fubgun-quiver-v2',c,'Visceral Quiver',75,
  'Fubgun 가성비 화살통(0.5.5 빌드 글) — 물리 피해 추가 + 투사체 +1 매직 구입 → 완벽한 제왕의 오브(좌측 대관식의 징조로 접두) → 우측 강령술 + 보존된 턱뼈 → 공개(치명타·공격 속도) → 상위 찬미 + 엑잘로 남은 2자리. 글은 제왕 결과가 접미면 더 좋다고 하지만 그러면 접미가 차서 턱뼈가 좋은 접미를 지울 수 있어 접두로 고정(가정). 베이스 이름은 글에 없어 본능적인 화살통으로 가정.',
  {'fT':{'kr':'물리 피해 추가','en':'Flat physical','values':TV({'1':('1티어','T1'),'2':('1~2티어','T1–2')})},'L':{'kr':'훼손 공개','en':'Desecration reveal','values':LV},
   'gT':{'kr':'치명타·공격 속도','en':'Crit / attack speed','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('물리 피해 추가 1티어 구입, 공개는 빛의 징조로 다시','Buy T1 flat physical; retry the reveal with Omen of Light'),'ess':K('물리 피해 추가 1~2티어 구입, 공개 결과 그대로','Buy T1–2 flat physical; keep the reveal')},
  tags,nodes,LIGHT_LOOP(['q3','q4','q4x'],'접미 두번째 옵션(훼손)','Second suffix (desecrated)'),
  FIN(VB,lambda v:[{'tag':'flat','tmax':1 if v=='bal' else 2},{'side':'p','label':K('공격 원소 피해 추가 또는 활 스킬 피해','Flat elemental or bow damage')},{'side':'p','random':True},{'tag':'proj'},{'side':'s','label':K('치명타 확률 / 공격 속도' if v=='bal' else '공개 결과 그대로','Crit / attack speed' if v=='bal' else 'Reveal as it comes')},{'side':'s','random':True}]),
  {'quality':20,'sockets':0},{'all':[{'has':'flat'},{'has':'proj'},{'full':'p'},{'full':'s'}]},VB)

# ---------- 2. Fubgun 가성비 물리 활 (비치명타) ----------
c='Bows'
P={'bal':{'aT':2,'L':1,'eT':3},'ess':{'aT':4,'L':0,'eT':5}}
tags={'pp':{'gi':7,'tmax':'$aT'},'flat':{'gi':39},'ele':{'anyOf':[{'gi':3,'tmax':'$eT'},{'gi':4,'tmax':'$eT'},{'gi':6,'tmax':'$eT'}]}}
PP=itg('p',c,7,['pp']); FA=itg('p',c,39,['flat'],'c',suffix=('제작 옵션','crafted'))
I0=[PP,J('s')]; I1=I0+[FA]; I2=I1+[UN('p')]
I3=I1+[it('p','화염·냉기·번개 피해 추가','Flat fire, cold or lightning',['ele'])]; I4=I3+[RND('s',2)]
nodes=[base('b2',{'rar':'magic','mods':['pp',{'junk':'s'}]},K('물리 피해 % 매직 활 구입 (접미 아무 옵션)','Buy a magic bow with % physical (any suffix)'),I0),
 act('b2','prep',[0,1],'essence','Greater_Essence_of_Abrasion',K('레어로 업그레이드 + 접두 물리 피해 추가','Upgrade to rare + flat physical prefix'),[st('p','물리 피해 추가 (제작 옵션)','Flat physical (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='flat'),
 mark([0,1.5],'b3',I1),
 act('b3','main',[0,2],'desecrate','Preserved_Jawbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'b4'}],I2,omens=['Omen_of_Sinistral_Necromancy']),
 REVL('b4',[0,3],'ele',['ele'],'b5','b4x',I3),
 annul('b4x',[1,3],[{'to':'b3','port':'right'}]),
 act('b5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),[st('s','랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I4,omens=['Omen_of_Greater_Exaltation'],
     over=[{'param':{'L':0},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,5])]
g22('fubgun-phys-bow-v2',c,'Warmonger Bow',75,
  'Fubgun 가성비 물리 활(0.5.5 빌드 글, 비치명타) — 물리 피해 % 매직(확장까지) 구입 → 상위 마모의 에센스 → 좌측 강령술 + 보존된 턱뼈 → 공개(원소 피해 추가, 냉기가 가장 좋음) → 상위 찬미 + 엑잘로 접미 2개. 아이템 레벨 75라 물리 피해 % 1티어(82)·원소 피해 추가 1티어(81)는 안 나옴 — 화면 티어는 이 레벨에서 나오는 것 기준.',
  {'aT':{'kr':'물리 피해 %','en':'% physical','values':TV({'2':('2티어','T2'),'4':('2~4티어','T2–4')})},'L':{'kr':'훼손 공개','en':'Desecration reveal','values':LV},
   'eT':{'kr':'원소 피해 추가','en':'Flat elemental','values':TV({'3':('2~3티어','T2–3'),'5':('2~5티어','T2–5')})}},P,
  {'bal':K('물리 피해 % 2티어 구입, 원소 피해 추가 2~3티어까지 빛의 징조로 다시','Buy T2 % physical; retry with Light until T2–3 flat elemental'),'ess':K('물리 피해 % 2~4티어 구입, 공개 결과 그대로','Buy T2–4 % physical; keep the reveal')},
  tags,nodes,LIGHT_LOOP(['b3','b4','b4x'],'접두 세번째 옵션(훼손)','Third prefix (desecrated)'),
  FIN(VB,lambda v:[{'tag':'pp','tmax':2 if v=='bal' else 4},{'tag':'flat','tmax':1},{'side':'p','label':K('화염·냉기·번개 피해 추가' if v=='bal' else '공개 결과 그대로','Flat elemental' if v=='bal' else 'Reveal as it comes')},{'side':'s','random':True},{'side':'s','random':True},{'side':'s','random':True}]),
  {'quality':20,'sockets':2},{'all':[{'has':'pp'},{'has':'flat'},{'full':'p'},{'full':'s'}]},VB)

# ---------- 3. Fubgun 가성비 치명타 활 ----------
P={'bal':{'aT':2,'L':1,'fT':2},'ess':{'aT':4,'L':0,'fT':4}}
tags={'pp':{'gi':7,'tmax':'$aT'},'crit':{'gi':49},'fl':{'anyOf':[{'gi':2,'tmax':'$fT'},{'gi':3,'tmax':'$fT'},{'gi':4,'tmax':'$fT'},{'gi':6,'tmax':'$fT'}]}}
CR=itg('s',c,49,['crit'],'c',suffix=('제작 옵션','crafted'))
I0=[PP,J('s')]; I1=I0+[CR]; I2=I1+[UN('p')]
I3=I1+[it('p','물리 피해 추가 또는 원소 피해 추가','Flat physical or flat elemental',['fl'])]; I4=I3+[RND('p'),RND('s')]
nodes=[base('b2',{'rar':'magic','mods':['pp',{'junk':'s'}]},K('물리 피해 % 매직 활 구입 (접미 아무 옵션)','Buy a magic bow with % physical (any suffix)'),I0),
 act('b2','prep',[0,1],'essence','Greater_Essence_of_Seeking',K('레어로 업그레이드 + 접미 치명타 확률','Upgrade to rare + crit chance suffix'),[st('s','치명타 확률 (제작 옵션)','Crit chance (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='crit'),
 mark([0,1.5],'b3',I1),
 act('b3','main',[0,2],'desecrate','Preserved_Jawbone',K('접두 두번째 옵션(훼손)','Second prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'b4'}],I2,omens=['Omen_of_Sinistral_Necromancy']),
 REVL('b4',[0,3],'fl',['fl'],'b5','b4x',I3),
 annul('b4x',[1,3],[{'to':'b3','port':'right'}]),
 act('b5','main',[0,4],'exalt','Perfect_Exalted_Orb',K('남은 접두·접미 1개씩','The last prefix and suffix'),[st(None,'랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I4,omens=['Omen_of_Greater_Exaltation'],
     over=[{'param':{'L':0},'set':{'cur':'Greater_Exalted_Orb'}}]),
 done([0,5])]
g22('fubgun-crit-bow-v2',c,'Warmonger Bow',75,
  'Fubgun 가성비 치명타 활(0.5.5 빌드 글) — 물리 피해 % 매직(확장까지) 구입 → 상위 추구의 에센스(치명타 확률) → 좌측 강령술 + 보존된 턱뼈 → 공개(물리 피해 추가가 가장 좋고 원소 피해 추가도 됨) → 상위 찬미 + 엑잘로 남은 2자리.',
  {'aT':{'kr':'물리 피해 %','en':'% physical','values':TV({'2':('2티어','T2'),'4':('2~4티어','T2–4')})},'L':{'kr':'훼손 공개','en':'Desecration reveal','values':LV},
   'fT':{'kr':'피해 추가','en':'Flat damage','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('물리 피해 % 2티어 구입, 피해 추가 1~2티어까지 빛의 징조로 다시','Buy T2 % physical; retry with Light until T1–2 flat damage'),'ess':K('물리 피해 % 2~4티어 구입, 공개 결과 그대로','Buy T2–4 % physical; keep the reveal')},
  tags,nodes,LIGHT_LOOP(['b3','b4','b4x'],'접두 두번째 옵션(훼손)','Second prefix (desecrated)'),
  FIN(VB,lambda v:[{'tag':'pp','tmax':2 if v=='bal' else 4},{'side':'p','label':K('물리 피해 추가 또는 원소 피해 추가' if v=='bal' else '공개 결과 그대로','Flat physical or elemental' if v=='bal' else 'Reveal as it comes')},{'side':'p','random':True},{'tag':'crit','tmax':1},{'side':'s','random':True},{'side':'s','random':True}]),
  {'quality':20,'sockets':2},{'all':[{'has':'pp'},{'has':'crit'},{'full':'p'},{'full':'s'}]},VB)

# ---------- 4. BigDaddyGaming 번개 +5 결투 마법봉 (가성비 길) ----------
c='Wands'
P={'bal':{'L':1,'pT':2},'ess':{'L':0,'pT':4}}
tags={'l5':{'gi':13,'tmax':1},'crit':{'gi':20,'tmax':1},'trans':{'gi':60},'blk':{'gi':1},
      'gp':{'anyOf':[{'gi':3,'tmax':'$pT'},{'gi':7,'tmax':'$pT'},{'gi':4,'tmax':'$pT'},{'gi':28,'tmax':'$pT'}],'label':K('주문 피해·번개 피해·주문 피해 + 마나·번개 피해 추가 획득','Spell, lightning, spell + mana or extra lightning damage')}}
# 2026-11-12 글 다시 확인(내장 브라우저, 6/22 수정판, 메인 세션): 가성비 길(+6) 단계 일치. 등급 C17: 밸런스 마지막 접두 1~2티어(빛의 징조로 다시), 에센셜 1~4티어·공개 나오는 대로. 완성품 줄의 임의 문구를 태그로.
L5=itg('s',c,13,['l5'],'f'); CR=itg('s',c,20,['crit']); TR=itg('s',c,60,['trans'],'c',suffix=('제작 옵션','crafted'))
MA=it('p','마나 최대치 (훼손, 자리 막기)','Max mana (desecrated, slot blocker)',['blk'],'d')
GP=it('p','주문 피해 / 번개 피해 / 주문 피해·마나 복합 / 번개 피해 추가 획득','Spell, lightning, hybrid spell/mana or extra lightning damage',['gp'])
I0=[L5,J('s')]; I1=[L5,CR]; I2=I1+[J('p')]; I3=[L5,CR,TR]; I4=I3+[UN('p')]; I5=I3+[MA]
I6=I5+[GP,RND('p')]; I7=[x for x in I6 if x is not MA]; I8=I7+[UN('p')]; I9=I7+[GP]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'l5','fr':True},{'junk':'s'}]},K('모든 번개 주문 스킬 레벨 +5 분열 결투 마법봉 (잡옵 1개)','Dueling Wand with fractured +5 lightning spells (one junk line)'),I0),
 mark([0,0.6],'w1',I0),
 act('w1','main',[0,1],'chaos','Chaos_Orb',K('접미 두번째 옵션','Second suffix'),None,K('카오스','Chaos'),[{'if':{'has':'crit'},'to':'w2','res':'ok'},{'to':'w1','res':'fail'}],I1,show=['crit']),
 act('w2','main',[0,2],'exalt','Exalted_Orb',K('접두에 잡옵 1개','A junk prefix'),[st('p','잡옵 (아무 옵션)','Junk (any line)')],K('엑잘','Exalt'),[{'to':'w3'}],I2,omens=['Omen_of_Sinistral_Exaltation']),
 act('w3','main',[0,3],'essence','Transcendent_Alloy',K('접두 잡옵을 지우고 접미 세번째 옵션','Remove the junk prefix, third suffix'),[st('s','초월의 합금 옵션 (제작 옵션)','Transcendent Alloy line (crafted)')],K('합금','Alloy'),[{'to':'w4'}],I3,ess='trans',omens=['Omen_of_Sinistral_Crystallisation']),
 act('w4','main',[0,4],'desecrate','Preserved_Jawbone',K('접두 자리 막기(훼손)','Block a prefix slot (desecrate)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'w5'}],I4),
 REVL('w5',[0,5],'blk',['blk'],'w6','w5x',I5),
 annul('w5x',[1,5],[{'to':'w4','port':'right'}]),
 act('w6','main',[0,6],'exalt','Perfect_Exalted_Orb',K('접두 두번째·세번째 옵션','Second and third prefixes'),[st('p','랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'w7'}],I6,omens=['Omen_of_Greater_Exaltation'],
     over=[{'param':{'L':0},'set':{'cur':'Greater_Exalted_Orb'}}]),
 annul('w7',[0,7],[{'to':'w8'}],target=K('자리 막기 훼손 옵션 제거','Remove the blocking desecrated line')),
 act('w8','main',[0,8],'desecrate','Preserved_Jawbone',K('접두 마지막 옵션(훼손)','Last prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'w9'}],I8),
 REVL('w9',[0,9],'gp',['gp'],'ok','w9x',I9),
 annul('w9x',[1,9],[{'to':'w8','port':'right'}]),
 done([0,10])]
g22('bigdaddy-lightning-wand-v2',c,'Dueling Wand',81,
  'BigDaddyGaming 번개 +5 마법봉(0.5 글, 가성비 길) — 번개 주문 +5 분열 → 카오스 오브로 주문 치명타(분열 외 유일한 옵션) → 좌측 찬미 + 엑잘(접두 잡옵) → 좌측 결정화 + 초월의 합금 → 보존된 턱뼈 + 공개로 마나 최대치를 접두 자리 막기 → 상위 찬미 + 엑잘(접두 2개, 마나가 막혀 피해 옵션이 잘 뜸) → 빛의 징조 + 소멸의 오브로 막기 제거 → 보존된 턱뼈 → 마지막 접두 공개. 글의 비싼 길(+7, 아스트리드 + 천공의 합금)은 꿀팁으로만.',
  {'L':{'kr':'훼손 공개','en':'Desecration reveals','values':LV},'pT':{'kr':'마지막 접두','en':'Last prefix','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('마나 막기·마지막 접두 모두 빛의 징조로 다시, 엑잘은 완벽한 엑잘티드 오브','Retry both reveals with Light; perfect exalts'),'ess':K('공개 결과 그대로, 엑잘은 상위 엑잘티드 오브','Keep both reveals; greater exalts')},
  tags,nodes,[{'id':'L1','nodes':['w4','w5','w5x'],'kr':'접두 자리 막기','en':'Prefix blocker'},{'id':'L2','nodes':['w8','w9','w9x'],'kr':'접두 마지막 옵션(훼손)','en':'Last prefix (desecrated)'}],
  FIN(VB,lambda v:[{'tag':'gp'} if v=='bal' else {'side':'p','random':True},{'side':'p','random':True},{'side':'p','random':True},{'tag':'l5','fr':True},{'tag':'crit','tmax':1},{'tag':'trans','tmax':1}]),
  {'quality':20,'sockets':1},{'all':[{'has':'l5'},{'has':'crit'},{'has':'trans'},{'full':'p'}]},VB)

# ---------- 5. Fubgun 투사체 +3 목걸이 ----------
c='Amulets'
P={'bal':{'L':1,'pT':2},'ess':{'L':0,'pT':4}}
tags={'pj':{'gi':20,'tmax':1},'sp':{'gi':28,'tmax':2},'enh':{'gi':74},'catR':{'anyOf':[{'gi':4},{'gi':7}]},
      'gs':{'anyOf':[{'gi':4},{'gi':5},{'gi':6},{'gi':7},{'gi':8},{'gi':24},{'gi':26}],'label':K('저항·치명타·희귀도','Resistance, crit or rarity')},
      'gp':{'anyOf':[{'gi':9,'tmax':'$pT'},{'gi':13,'tmax':'$pT'},{'gi':16,'tmax':'$pT'}],'label':K('생명력·에너지 보호막','Life or energy shield')}}
PJ=itg('s',c,20,['pj'],'f'); SP=itg('p',c,28,['sp']); EN=itg('p',c,74,['enh'],'c',suffix=('제작 옵션','crafted'))
GS=lambda: it('s','저항 (치명타·희귀도도 됨)','A resistance (crit or rarity also fine)',['gs'])
I0=[PJ,J('p')]; I1=[PJ,SP]; I2=I1+[J('s')]; I3=I1+[EN]; I4=I3+[GS()]; I5=I4+[GS()]; I6=I5+[UN('p')]
I7=I5+[it('p','생명력 최대치 / 에너지 보호막 최대치 / 에너지 보호막 증가','Max life / max energy shield / % energy shield',['gp'])]
nodes=[base('ms',{'rar':'rare','mods':[{'tag':'pj','fr':True},{'junk':'p'}]},K('모든 투사체 스킬 레벨 +3 분열 황금 목걸이 (잡옵 1개)','Gold Amulet with fractured +3 projectile skills (one junk line)'),I0),
 mark([0,0.6],'a1',I0),
 act('a1','main',[0,1],'chaos','Chaos_Orb',K('접두 첫번째 옵션','First prefix'),None,K('카오스','Chaos'),[{'if':{'has':'sp'},'to':'a2','res':'ok'},{'to':'a1','res':'fail'}],I1,show=['sp']),
 act('a2','main',[0,2],'exalt','Exalted_Orb',K('접미에 잡옵 1개','A junk suffix'),[st('s','잡옵 (아무 옵션)','Junk (any line)')],K('엑잘','Exalt'),[{'to':'a3'}],I2,omens=['Omen_of_Dextral_Exaltation']),
 act('a3','main',[0,3],'essence','Perfect_Essence_of_Enhancement',K('접미 잡옵을 지우고 접두 두번째 옵션','Remove the junk suffix, second prefix'),[st('p','방어도·회피·에너지 보호막 증가 (제작 옵션)','% armour, evasion and energy shield (crafted)')],K('에센스','Essence'),[{'to':'a4'}],I3,ess='enh',omens=['Omen_of_Dextral_Crystallisation']),
 act('a4','main',[0,4],'quality','Xophs_Catalyst',K('화염 퀄리티 20%','Fire quality 20%'),None,K('퀄리티','Quality'),[{'to':'a5'}],I3,count=20),
 act('a5','main',[0,5],'exalt','Perfect_Exalted_Orb',K('접미 두번째 옵션','Second suffix'),None,K('엑잘','Exalt'),[{'if':{'added':'gs'},'to':'a6','res':'ok'},{'to':'a5x','res':'fail','port':'right'}],I4,show=['gs'],omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],cat='catR'),
 annul('a5x',[1,5],[{'to':'a4','port':'right'}],omens=('Omen_of_Dextral_Annulment',),target=K('빗나간 접미 지우기','Remove the missed suffix')),
 act('a6','main',[0,6],'quality','Xophs_Catalyst',K('화염 퀄리티 20%','Fire quality 20%'),None,K('퀄리티','Quality'),[{'to':'a7'}],I4,count=20),
 act('a7','main',[0,7],'exalt','Perfect_Exalted_Orb',K('접미 세번째 옵션','Third suffix'),None,K('엑잘','Exalt'),[{'if':{'added':'gs'},'to':'a8','res':'ok'},{'to':'a7x','res':'fail','port':'right'}],I5,show=['gs'],omens=['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],cat='catR'),
 annul('a7x',[1,7],[{'if':{'count':{'tag':'gs','min':1}},'to':'a6','port':'right'},{'to':'a4','res':'fail','lost':'gs','hide':True}],omens=('Omen_of_Dextral_Annulment',),target=K('빗나간 접미 지우기','Remove the missed suffix')),
 act('a8','main',[0,8],'desecrate','Preserved_Collarbone',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'a9'}],I6),
 REVL('a9',[0,9],'gp',['gp'],'ok','a9x',I7),
 annul('a9x',[1,9],[{'to':'a8','port':'right'}]),
 done([0,10])]
g22('fubgun-proj-amulet-v2',c,'Gold Amulet',82,
  'Fubgun 투사체 +3 목걸이(0.5.5 빌드 글) — 투사체 +3 분열 + 잡옵 → 카오스 오브로 정신력 1~2티어 → 우측 찬미 + 엑잘(접미 잡옵) → 우측 결정화 + 완벽한 강화의 에센스 → 조프의 기폭제 20% + 촉진 + 우측 찬미 + 완벽한 엑잘로 저항 2개(치명타·희귀도도 받음, 빗나가면 우측 소멸의 징조 + 소멸의 오브) → 보존된 빗장뼈 → 공개(생명력·에너지 보호막). 글의 빗나감 처리(빗장뼈로 덮고 빛의 징조)는 접미에 빈자리가 있으면 안 먹어서 우측 소멸의 징조로 바꿈. 촉진 효과는 퀄리티 %만큼 미는 추정값.',
  {'L':{'kr':'훼손 공개','en':'Desecration reveal','values':LV},'pT':{'kr':'마지막 접두','en':'Last prefix','values':TV({'2':('1~2티어','T1–2'),'4':('1~4티어','T1–4')})}},P,
  {'bal':K('마지막 접두를 1~2티어까지 빛의 징조로 다시','Retry the last prefix with Light until T1–2'),'ess':K('마지막 접두는 공개 결과 그대로','Keep the last reveal')},
  tags,nodes,[{'id':'L1','nodes':['a4','a5','a5x'],'kr':'접미 두번째 옵션','en':'Second suffix'},{'id':'L2','nodes':['a8','a9','a9x'],'kr':'접두 세번째 옵션(훼손)','en':'Third prefix (desecrated)'}],
  FIN(VB,lambda v:[{'tag':'sp','tmax':2},{'tag':'enh','tmax':1},{'tag':'gp'} if v=='bal' else {'side':'p','random':True},{'tag':'pj','fr':True},{'tag':'gs'},{'tag':'gs'}]),
  {'quality':20,'sockets':0},{'all':[{'has':'pj'},{'has':'sp'},{'has':'enh'},{'count':{'tag':'gs','min':2}},{'full':'p'}]},VB)

# ---------- 6. Fubgun 가성비 에너지 보호막 투구 ----------
c='Helmets_int'
P={'bal':{'L':1,'hT':2},'ess':{'L':0,'hT':6}}
tags={'esf':{'gi':7,'tmax':1},'enh':{'gi':34},'hyb':{'anyOf':[{'gi':9,'tmax':'$hT'},{'gi':10,'tmax':'$hT'}]}}
EF=itg('p',c,7,['esf']); EH=itg('p',c,34,['enh'],'c',suffix=('제작 옵션','crafted'))
I0=[EF,J('s')]; I1=I0+[EH]; I2=I1+[UN('p')]
I3=I1+[it('p','에너지 보호막 증가 + 생명력·마나 복합','Hybrid % energy shield + life or mana',['hyb'])]; I4=I3+[RND('s',2)]
nodes=[base('e2',{'rar':'magic','mods':['esf',{'junk':'s'}]},K('에너지 보호막 최대치 1티어 매직 투구 구입 (접미 아무 옵션)','Buy a magic helmet with T1 flat energy shield (any suffix)'),I0),
 act('e2','prep',[0,1],'essence','Greater_Essence_of_Enhancement',K('레어로 업그레이드 + 접두 두번째 옵션','Upgrade to rare + second prefix'),[st('p','방어도·회피·에너지 보호막 증가 (제작 옵션)','% armour, evasion and energy shield (crafted)')],K('에센스','Essence'),[{'to':'ms'}],I1,ess='enh'),
 mark([0,1.5],'e3',I1),
 act('e3','main',[0,2],'desecrate','Preserved_Rib',K('접두 세번째 옵션(훼손)','Third prefix (desecrated)'),[st('p','훼손 옵션(미공개)','Desecrated modifier (unrevealed)')],K('훼손','Desecrate'),[{'to':'e4'}],I2,omens=['Omen_of_Sinistral_Necromancy']),
 REVL('e4',[0,3],'hyb',['hyb'],'e5','e4x',I3,omens=()),
 annul('e4x',[1,3],[{'to':'e3','port':'right'}]),
 act('e5','main',[0,4],'exalt','Greater_Exalted_Orb',K('접미 두번째·세번째 옵션','Second and third suffixes'),[st('s','랜덤 옵션 2개 — 결과 그대로','Two random lines — keep whatever comes')],K('엑잘','Exalt'),[{'to':'ok'}],I4,omens=['Omen_of_Greater_Exaltation']),
 done([0,5])]
g22('fubgun-es-helmet-v2',c,'Kamasan Tiara',78,
  'Fubgun 가성비 에너지 보호막 투구(0.5.5 빌드 글) — 에너지 보호막 최대치 1티어 매직 구입 → 상위 강화의 에센스 → 좌측 강령술 + 보존된 갈비뼈 → 공개(에너지 보호막 % 복합이면 아무 티어나) → 상위 찬미 + 상위 엑잘로 접미 2개. 베이스 이름은 글에 없어 카마사의 티아라로 가정. 마지막 바알 주입기(타락)는 정책 33으로 뺌.',
  {'L':{'kr':'훼손 공개','en':'Desecration reveal','values':LV},'hT':{'kr':'에너지 보호막 복합','en':'Hybrid % energy shield','values':TV({'2':('1~2티어','T1–2'),'6':('아무 티어','Any tier')})}},P,
  {'bal':K('복합 옵션 1~2티어까지 빛의 징조로 다시','Retry with Light until a T1–2 hybrid'),'ess':K('공개 결과 그대로 (글: 복합이면 아무 티어나)','Keep the reveal (the guide takes any hybrid)')},
  tags,nodes,LIGHT_LOOP(['e3','e4','e4x'],'접두 세번째 옵션(훼손)','Third prefix (desecrated)'),
  FIN(VB,lambda v:[{'tag':'esf','tmax':1},{'tag':'enh','tmax':1},{'side':'p','label':K('에너지 보호막 % 복합' if v=='bal' else '공개 결과 그대로','Hybrid % energy shield' if v=='bal' else 'Reveal as it comes')},{'side':'s','random':True},{'side':'s','random':True},{'side':'s','random':True}]),
  {'quality':20,'sockets':1},{'all':[{'has':'esf'},{'has':'enh'},{'full':'p'},{'full':'s'}]},VB)

import os as _os, subprocess as _sp, sys as _sy
if _os.path.exists(f'{H}/gen_bigdaddy_lightning_wand.py'): _sp.run([_sy.executable, f'{H}/gen_bigdaddy_lightning_wand.py'], check=True)   # 2026-11-13 G7: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_fubgun_proj_amulet.py'): _sp.run([_sy.executable, f'{H}/gen_fubgun_proj_amulet.py'], check=True)   # 2026-11-13 G5: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_fubgun_quiver.py'): _sp.run([_sy.executable, f'{H}/gen_fubgun_quiver.py'], check=True)   # 2026-11-13 G10: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_fubgun_es_helmet.py'): _sp.run([_sy.executable, f'{H}/gen_fubgun_es_helmet.py'], check=True)   # 2026-11-13 G11: 새 기준 전용 생성기가 덮어씀
if _os.path.exists(f'{H}/gen_fubgun_phys_bow.py'): _sp.run([_sy.executable, f'{H}/gen_fubgun_phys_bow.py'], check=True)   # 2026-11-13 G10: 새 기준 전용 생성기가 덮어씀
