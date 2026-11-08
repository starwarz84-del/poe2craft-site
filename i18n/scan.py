import re, json, sys
HAN = re.compile(r'[가-힣]')
def scan(js):
    """yield (start,end,kind,text) for string literals; templates yield static chunks"""
    i=0; n=len(js); out=[]; prev=''
    stack=[]  # template nesting: when inside ${ } of a template we track brace depth
    def is_regex_ctx(p):
        return p=='' or p in '(,=:[!&|?{};+-*%<>~^' or p=='\n'
    while i<n:
        c=js[i]
        if c=='/' and i+1<n and js[i+1]=='/':
            j=js.find('\n',i); i=n if j<0 else j; continue
        if c=='/' and i+1<n and js[i+1]=='*':
            j=js.find('*/',i+2); i=j+2; continue
        if c=='/' and is_regex_ctx(prev):
            j=i+1; cls=False
            while j<n:
                d=js[j]
                if d=='\\': j+=2; continue
                if d=='[': cls=True
                elif d==']': cls=False
                elif d=='/' and not cls: break
                elif d=='\n': break
                j+=1
            j+=1
            while j<n and js[j].isalpha(): j+=1
            i=j; prev='x'; continue
        if c in '\'"':
            j=i+1
            while js[j]!=c:
                if js[j]=='\\': j+=1
                j+=1
            out.append((i,j+1,'q',js[i+1:j],i)); i=j+1; prev='x'; continue
        if c=='`':
            # parse template, record static chunks
            j=i+1; chunk_start=j; tstart=i
            while True:
                d=js[j]
                if d=='\\': j+=2; continue
                if d=='`':
                    out.append((chunk_start,j,'t',js[chunk_start:j],tstart)); j+=1; break
                if d=='$' and js[j+1]=='{':
                    out.append((chunk_start,j,'t',js[chunk_start:j],tstart))
                    # find matching } by recursive scan of expression
                    k=j+2; depth=1
                    sub_start=k
                    # recursive: scan expression region using same function on substring until depth 0
                    while depth>0:
                        e=js[k]
                        if e in '\'"':
                            m=k+1
                            while js[m]!=e:
                                if js[m]=='\\': m+=1
                                m+=1
                            k=m+1; continue
                        if e=='`':
                            # nested template: find its end via recursion
                            sub=scan_template_end(js,k)
                            k=sub; continue
                        if e=='{': depth+=1
                        elif e=='}': depth-=1
                        k+=1
                    # recurse into expression for literals
                    for (a,b,kk,tt,ts) in scan(js[sub_start:k-1]):
                        out.append((a+sub_start,b+sub_start,kk,tt,ts+sub_start))
                    j=k; chunk_start=j; continue
                j+=1
            i=j; prev='x'; continue
        if not c.isspace(): prev=c if not (c.isalnum() or c in '_$.') else 'x'
        if c in ')]': prev='x'
        i+=1
    return out
def scan_template_end(js,k):
    j=k+1
    while True:
        d=js[j]
        if d=='\\': j+=2; continue
        if d=='`': return j+1
        if d=='$' and js[j+1]=='{':
            depth=1; m=j+2
            while depth>0:
                e=js[m]
                if e in '\'"':
                    q=m+1
                    while js[q]!=e:
                        if js[q]=='\\': q+=1
                        q+=1
                    m=q+1; continue
                if e=='`': m=scan_template_end(js,m); continue
                if e=='{': depth+=1
                elif e=='}': depth-=1
                m+=1
            j=m; continue
        j+=1
