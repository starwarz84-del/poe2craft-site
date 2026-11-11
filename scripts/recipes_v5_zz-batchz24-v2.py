# ---- 2026-11-11 batch 24: 균열 반지 물리 (플로우차트 scripts/graphs/gen_batch24.py와 같은 단계 id, 정책 30·31) ----
# 원본 breach-ring-phys(recipes_batch4.py, 사이트 운영자 제작 방식)의 꼬인 순서를 그래프대로 고침: 최대 퀄리티를 지운 새 옵션이 접미로 가면
# 접미 잡옵을 절사·말소 + 상위 카오스 오브로 접두로 옮긴 뒤 접두를 채우고 좌측 결정화 + 재빠른 합금.
def _brp(t):
    r=_cp.deepcopy(_orig('breach-ring-phys')); bal = t=='bal'
    r['id']='breach-ring-phys-v2-'+t; r['tierGroup']='breach-ring-phys-v2'; r['tier']=t; r['tierLabel']=_TL[t]; r.pop('note',None)
    if 'breach-ring-phys' in DIFFSET: r['difficulty']=DIFFSET['breach-ring-phys']
    ELE=[{'gi':15,'tmax':3},{'gi':17,'tmax':3},{'gi':19,'tmax':3}]
    LIGHT={'cur':'Orb_of_Annulment','omens':['Omen_of_Light']}
    r['phases']=[{'id':'base','kr':'베이스','en':'Base'},{'id':'suf','kr':'접미','en':'Suffixes'},{'id':'pre','kr':'접두','en':'Prefixes'}]
    N=[{'id':'b1','phase':'base','do':'base','cost':'base','note':K('공격 시 물리 피해 1티어 분열 + 잡옵 1개.','Fractured tier 1 physical attack damage + one junk line.')},
       {'id':'b2','phase':'suf','do':'chaos','cur':'Chaos_Orb','target':{'gi':7,'tmax':1},'fail':{'goto':'self'}},
       {'id':'b3','phase':'suf','do':'exalt','cur':'Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'}},
       {'id':'b4','phase':'suf','do':'essence','cur':'Essence_of_the_Breach','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':71}},
       {'id':'b5','phase':'suf','do':'quality','cur':'Xophs_Catalyst','target':{'quality':60}},
       {'id':'b6','phase':'suf','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Catalysing_Exaltation','Omen_of_Dextral_Exaltation'],'target':{'gi':4,'tmax':2 if bal else 3},
        **({'fail':{'goto':'b5','via':{'cur':'Orb_of_Annulment','omens':['Omen_of_Dextral_Annulment']},'lost':'b1'}} if bal else {'br':KEEP})},
       {'id':'b7','phase':'suf','do':'quality','cur':'Reaver_Catalyst','target':{'quality':60}},
       {'id':'b8','phase':'pre','do':'chaos','cur':'Chaos_Orb','omens':['Omen_of_Whittling'],'target':{'removeGi':71,'junk':'p'},
        'br':K('새 옵션이 접미로 가면 → 다음 단계로 접미 자리 비우기','The new line lands on the suffixes → free a suffix slot next')},
       {'id':'b8s','phase':'pre','do':'chaos','cur':'Greater_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Dextral_Erasure'],'optional':True,
        'label':K('접미 자리 비우기 (새 옵션이 접미로 갔을 때)','Free a suffix slot (when the new line went to the suffixes)'),'target':{'junk':'p','chance':0.5},'knownP':True,'fail':{'goto':'self'}},
       {'id':'b9a','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'junk':'p'}},
       {'id':'b9','phase':'pre','do':'essence','cur':'Swift_Alloy','omens':['Omen_of_Sinistral_Crystallisation'],'target':{'gi':73},
        'br':K('남은 접두가 공격 시 원소 피해면 → 바로 훼손' if bal else '남은 접두가 무엇이든 빈자리에 훼손','The remaining prefix is elemental → desecrate next' if bal else 'Whatever prefix is left, desecrate the open slot')}]
    if bal:
        N+=[{'id':'e1','phase':'pre','do':'exalt','cur':'Perfect_Exalted_Orb','omens':['Omen_of_Sinistral_Exaltation'],'target':{'anyOf':ELE},'label':K('남은 접두가 잡옵이면','When the remaining prefix is junk')},
            {'id':'e2','phase':'pre','do':'chaos','cur':'Perfect_Chaos_Orb','omens':['Omen_of_Whittling','Omen_of_Sinistral_Erasure'],'fallbackFor':'e1','target':{'anyOf':ELE,'replace':'p'},'fail':{'goto':'self'}}]
    N+=[{'id':'d1','phase':'pre','do':'desecrate','cur':'Ancient_Collarbone','omens':['Omen_of_Sinistral_Necromancy'],'target':{'unrev':'p'}},
        {'id':'d2','phase':'pre','do':'reveal','omens':['Omen_of_Abyssal_Echoes'],'target':{'reveal':{'anyOf':[dict(x,tmax=3 if bal else 4) for x in ELE]},'side':'p','bone':'Ancient_Collarbone'},
         **({'fail':{'goto':'d1','via':LIGHT}} if bal else {'br':KEEP})}]
    r['nodes']=N; R.append(r)
for _t in ('bal','ess'): _brp(_t)
