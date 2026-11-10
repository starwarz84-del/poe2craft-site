# 사용자 확정 2026-11-10: 화면 문구의 '줄'(옵션 세는 말)을 '옵션'으로. Korean-only rewrite; verbs (줄이다·줄여·해 줄) are left alone.
# usage: python3 tools/opt_word.py <files...>   (prints a sample of changes; --dry to only show)
import re, sys
H='[가-힣]'
VOW={'이':'가','을':'를','은':'는','과':'와','으로':'로'}
NUMK={'한':'하나','두':'두 개','세':'세 개','네':'네 개','다섯':'다섯 개'}
AUX=set('해어아여워와줘쳐켜려혀춰겨져셔봐내')
KEEPW=('이름',)   # 아이템 이름 줄 = a text line, not a modifier
PART=r'(?:처럼|보다|에만|에서|마다|이라도|뿐이라|뿐이고|뿐이면|뿐인|만으로|으로|이나|까지|부터|이|을|은|과|에|만|뿐|로|도|의|씩)?'
def vowel_part(p):
    for k,v in VOW.items():
        if p.startswith(k): return v+p[len(k):]
    return p
def fix(s):
    if 'youtube' in s or 'src(' in s or 'youtu.be' in s: return s   # video titles stay as published
    s = re.sub(r'(\$\{[^}]+\})줄', r'옵션 \1개', s)
    # N줄 → 옵션 N개 (잡옵 N개, 옵션 N개)
    def num(m):
        pre, n, p = m.group(1) or '', m.group(2), m.group(3)
        w = pre.strip()
        if w == '잡옵': out = f'잡옵 {n}개'
        elif w.endswith('옵션'): out = f'{pre}{n}개'
        else: out = f'{pre}옵션 {n}개'
        return out + vowel_part(p)
    s = re.sub(r'(?<![가-힣+ ])(\d+)줄(?= (?!이하|이상|중|모두|전부)%s)' % H, lambda m: m.group(1)+'옵션', s)   # 5줄 주얼 → 5옵션 주얼
    s = re.sub(r'((?:%s+ )?)(\d+)줄(%s(?!%s))' % (H, PART, H), num, s)
    s = re.sub(r'((?:%s+ )?)(\d+)줄(?=%s)' % (H, H), lambda m: num(type('M',(object,),{'group':lambda self,i,m=m:(m.group(1),m.group(2),'')[i-1] if i else m.group(0)})()), s)
    # 한/두/세 줄
    def kn(m):
        p = m.group(2); w = NUMK[m.group(1)]
        return '옵션 ' + w + vowel_part(p)
    s = re.sub(r'(?<!%s)(한|두|세|네|다섯) 줄(%s)(?!%s)' % (H, PART, H), kn, s)
    # 버릴 줄일 때 / 좋은 줄이면 (copula after a modifier) — not 비용을 줄일 (verb after an object)
    s = re.sub(r'(%s+) 줄(일|이면|인|이라|이고)(?!%s)' % (H, H), lambda m: m.group(0) if m.group(1)[-1] in '을를' else m.group(1)+' 옵션'+m.group(2), s)
    # standalone 줄 (noun)
    def word(m):
        prev = m.group(1)
        if prev and prev[-1] in AUX: return m.group(0)
        if m.string[max(0,m.start()-3):m.start()+1].strip().endswith(KEEPW): return m.group(0)
        return (prev or '') + m.group(2) + '옵션' + m.group(3)
    s = re.sub(r'(%s?)( ?)줄(%s)(?!%s)' % (H, PART, H), lambda m: m.group(0) if (m.group(1) and not m.group(2)) else word(m), s)
    return s
if __name__=='__main__':
    dry = '--dry' in sys.argv
    for f in [a for a in sys.argv[1:] if a!='--dry']:
        t=open(f,encoding='utf-8').read(); u='\n'.join(fix(x) for x in t.split('\n'))
        if t!=u:
            a=t.splitlines(); b=u.splitlines(); shown=0
            for x,y in zip(a,b):
                if x!=y and shown<2: print(f'{f}:\n  - {x.strip()[:160]}\n  + {y.strip()[:160]}'); shown+=1
            if not dry: open(f,'w',encoding='utf-8').write(u)
