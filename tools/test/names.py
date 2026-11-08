# 커런시·징조·뼈 이름이 게임 공식 한글(crafting.json kr)과 다른 곳을 찾음: python3 tools/test/names.py
import json,re,collections
C=json.load(open('site/data/crafting.json')); off=set()
for k in C:
    for x in C[k]:
        if x.get('kr'): off.add(x['kr'])
SUF=r'(?:징조|오브|에센스|기폭제|빗장뼈|뼈|주입기|합금|촉매)'
pat=re.compile(r'(?:\$\{[^}]*\}\s?)?[가-힣]+(?:\s[가-힣]+){0,3}\s?'+SUF)
STRIP=re.compile(r'^(?:으로|로|와|과|및|후|그|이|첫|다음|한|두|세|각|더|약|또는|이후|아니면|먼저|또|같은|그냥|이제|쓴|쓰는|돌린|남은|나머지|다른|새|싼|비싼|대신|일반|모든|한번|매번)\s')
def bad(w):
    w=w.strip()
    if w.startswith('${'): return w
    while True:
        w2=STRIP.sub('',w)
        if w2==w: break
        w=w2
    if any(w.endswith(o) or o.endswith(w) and len(w)>3 for o in off): return None
    return w
hits=collections.Counter()
def scan(name,text):
    for m in pat.finditer(text):
        b=bad(m.group(0))
        if b: hits[(name,b)]+=1
src=open('site/reverse.html').read(); scan('reverse.html',src)
scan('recipes.html',open('site/recipes.html').read())
def walk(name,x):
    if isinstance(x,dict):
        for k,v in x.items():
            if k=='kr' and isinstance(v,str): scan(name,v)
            else: walk(name,v)
    elif isinstance(x,list):
        for v in x: walk(name,v)
walk('recipes.json',json.load(open('site/data/recipes.json')))
walk('tips.json',json.load(open('site/data/tips.json')))
for (f,w),n in sorted(hits.items()): print(f'{f}\t{n}\t{w}')
