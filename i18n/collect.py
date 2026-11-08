import re,json,sys
exec(open('/home/claude/poe2data/i18n/scan.py').read())
HAN=re.compile(r'[가-힣]')
PIECE=re.compile(r'[^<>"=${}`]+')
def isL(js,ts):
    k=ts-1
    while k>=0 and js[k] in ' \n\t': k-=1
    return k>=1 and js[k]=='(' and js[k-1]=='L' and (k<2 or not (js[k-2].isalnum() or js[k-2]=='_'))
def line_of(js,a):
    b=js.rfind('\n',0,a)+1; e=js.find('\n',a); return js[b:e]
def items(js):
    res=[]
    for (a,b,k,t,ts) in scan(js):
        if not HAN.search(t): continue
        if isL(js,ts): continue
        ln=line_of(js,a)
        if re.search(r'\bRN = |CATKR|const GLY',ln): continue
        if k=='q': res.append((a,b,'q',t))
        else:
            for m in PIECE.finditer(t):
                p=m.group(0)
                if not HAN.search(p): continue
                lead=len(p)-len(p.lstrip()); trail=len(p)-len(p.rstrip())
                core=p.strip()
                res.append((a+m.start()+lead, a+m.end()-trail, 't', core))
    return res
if __name__=='__main__':
    allt={}
    for f in ['emulator.html','index.html']:
        s=open('/home/claude/poe2data/site/'+f).read()
        i=s.rindex('<script>')+8; js=s[i:s.rindex('</script>')]
        for it in items(js): allt.setdefault(it[3],[]).append(f[0])
    json.dump(sorted(allt),open('/home/claude/poe2data/i18n/keys.json','w'),ensure_ascii=False,indent=0)
    print(len(allt))
