import json,sys,re
cls=sys.argv[1]; pats=sys.argv[2:]
d=json.load(open(cls+'.json'))
if pats and pats[0]=='-b':
    for i,b in enumerate(d['bases']): print(i,b['en'],b['kr'],b.get('lv'),b.get('imp',[[]])[0][:2],b.get('sock'))
    sys.exit()
for gi,g in enumerate(d['groups']):
    t=g['t'][0][5]
    if any(re.search(p,t,re.I) for p in pats): print(gi,g['s'],g['g'],[(x[0],x[1]) for x in g['t'][:3]],len(g['t']),t.replace('\n',' / ')[:80])
