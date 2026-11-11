"""Assemble the poe2craft.xyz deploy folder (web/) from the built site.

Run after the normal build (build_recipes.py ... i18n/build.py):
    python3 scripts/build_web.py

web/ is what the host serves (Cloudflare Pages output directory = web, no build command).
- index.html  = site/shell.html (trade-style banner + tab bar)
- tool pages  = site/pub/*.html with site/theme.css injected (colors/fonts only)
- about.html, favicon.svg, sim.js, graphify.js, lib/, data/ copied as they are
"""
import os, shutil, re, base64, hashlib, glob

# 데이터 파일 안의 그림(data URI, 클래스 파일·crafting.json 크기의 85~90%)은 파일로 빼고 주소만 남김 — 화면에 보이는 그림만 받고 탭끼리 캐시를 같이 씀 (2026-11-11)
URI = re.compile(r'data:image/(webp|png|jpe?g|gif);base64,([A-Za-z0-9+/=]+)')
def split_images(web):
    out = os.path.join(web, 'img', 'd'); os.makedirs(out, exist_ok=True); n = saved = 0
    for f in glob.glob(os.path.join(web, 'data', '**', '*.json'), recursive=True):
        s = open(f, encoding='utf-8').read()
        if 'data:image/' not in s: continue
        def rep(m):
            nonlocal n
            buf = base64.b64decode(m.group(2)); name = hashlib.sha1(buf).hexdigest()[:12] + '.' + m.group(1).replace('jpeg', 'jpg')
            path = os.path.join(out, name)
            if not os.path.exists(path): open(path, 'wb').write(buf); n += 1
            return 'img/d/' + name
        t = URI.sub(rep, s); saved += len(s) - len(t)
        open(f, 'w', encoding='utf-8').write(t)
    print('images split out of data:', n, 'files,', saved // 1024, 'KB smaller JSON')

# 한글 글꼴(SUIT 610KB)은 사이트 파일에 실제로 나오는 글자 + 기본 문장 부호만 남김 — 배포마다 다시 만들어 새 레시피 글자도 들어감, 붙여 넣은 아이템 글처럼 없는 글자는 맑은 고딕으로 보임
def subset_font(web):
    from fontTools import subset
    chars = set(chr(c) for c in range(0x20, 0x7f)) | set('·…—–‘’“”•→←↑↓↺✓✕★☆♥①②③④⑤⑥⑦⑧⑨⑩％～')
    for f in glob.glob(os.path.join(web, '**', '*'), recursive=True):
        if f.endswith(('.json', '.html', '.js')):
            chars |= set(open(f, encoding='utf-8', errors='ignore').read())
    keep = sorted(c for c in chars if ord(c) >= 0x20 and not (0xd800 <= ord(c) < 0xe000))
    src = os.path.join(web, 'fonts', 'SUIT-Variable.woff2'); before = os.path.getsize(src)
    opt = subset.Options(); opt.flavor = 'woff2'; opt.layout_features = ['*']; opt.name_IDs = ['*']; opt.notdef_outline = True
    font = subset.load_font(src, opt); sub = subset.Subsetter(opt); sub.populate(text=''.join(keep)); sub.subset(font)
    subset.save_font(font, src, opt)
    print('SUIT font subset:', before // 1024, '->', os.path.getsize(src) // 1024, 'KB,', len(keep), 'chars')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
WEB = os.path.join(ROOT, 'web')
DOMAIN = 'poe2craft.xyz'
# Test phase (user decision 2026-11-10): keep the site out of search engines. Set True when it goes public.
INDEX = False
NOINDEX_META = '<meta name="robots" content="noindex, nofollow">\n'
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap">\n'
THEME = '<link rel="stylesheet" href="theme.css">\n'
# 페이지 스크립트가 시작할 때 바로 받는 데이터는 HTML을 읽는 동안 미리 받기 시작
PRELOAD = {'recipes.html': ['recipes', 'board', 'crafting', 'index', 'tips', 'prices', 'budget', 'trade'], 'emulator.html': ['crafting', 'index'], 'builder.html': ['index'], 'bases.html': ['special'], 'discover.html': ['samples']}

def main():
    if os.path.isdir(WEB):
        shutil.rmtree(WEB)
    os.makedirs(WEB)
    for f in ['favicon.svg', 'theme.css', 'sim.js', 'graphify.js']:
        shutil.copy(os.path.join(SITE, f), os.path.join(WEB, f))
    for src, dst in [('shell.html', 'index.html'), ('about.html', 'about.html')]:
        s = open(os.path.join(SITE, src), encoding='utf-8').read()
        if not INDEX:
            s = s.replace('<meta charset="utf-8">\n', '<meta charset="utf-8">\n' + NOINDEX_META, 1)
        open(os.path.join(WEB, dst), 'w', encoding='utf-8').write(s)
    for d in ['data', 'lib', 'img', 'fonts']:
        shutil.copytree(os.path.join(SITE, d), os.path.join(WEB, d))
    split_images(WEB)
    for f in sorted(os.listdir(os.path.join(SITE, 'pub'))):
        if not f.endswith('.html'):
            continue
        s = open(os.path.join(SITE, 'pub', f), encoding='utf-8').read()
        # 구글 글꼴(본문·제목은 theme.css가 SUIT·Fontin으로 덮어씀)은 화면을 막는 외부 파일이라 뺌 — 숫자용 고정폭은 기기 글꼴로
        s = re.sub(r'<link rel="(?:preconnect|stylesheet)" href="https://fonts\.(?:googleapis|gstatic)\.com[^>]*>\n?', '', s)
        # theme goes right after the document head the i18n build added; its :root:root rules win over the page's own tokens
        i = s.find('</style>')
        head = THEME + ('' if INDEX else NOINDEX_META)
        head += ''.join('<link rel="preload" href="data/%s.json" as="fetch" crossorigin="anonymous">\n' % d for d in PRELOAD.get(f, []))
        s = s[:i + 8] + '\n' + head + s[i + 8:] if i >= 0 else head + s
        open(os.path.join(WEB, f), 'w', encoding='utf-8').write(s)
    subset_font(WEB)
    # 줄인 글꼴은 배포마다 내용이 바뀌는데 한 달 캐시라, 예전 글꼴을 가진 방문자에게 새 레시피 글자가 기기 글꼴로 보였음 → 내용 해시를 파일 이름에 넣음(2026-11-11)
    fp = os.path.join(WEB, 'fonts', 'SUIT-Variable.woff2'); fh = hashlib.md5(open(fp, 'rb').read()).hexdigest()[:10]; fn = 'SUIT-Variable.%s.woff2' % fh
    os.rename(fp, os.path.join(WEB, 'fonts', fn))
    for f in glob.glob(os.path.join(WEB, '*.html')) + glob.glob(os.path.join(WEB, '*.css')):
        t = open(f, encoding='utf-8').read()
        if 'SUIT-Variable.woff2' in t:
            open(f, 'w', encoding='utf-8').write(t.replace('SUIT-Variable.woff2', fn))
    open(os.path.join(WEB, 'CNAME'), 'w').write(DOMAIN + '\n')
    if INDEX:
        open(os.path.join(WEB, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: https://%s/sitemap.xml\n' % DOMAIN)
        open(os.path.join(WEB, 'sitemap.xml'), 'w').write(
            '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            '<url><loc>https://%s/</loc></url>\n</urlset>\n' % DOMAIN)
    else:
        open(os.path.join(WEB, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
    # cache: pages always fresh, big data files cached for an hour; while testing, every response says noindex
    noindex = '' if INDEX else '/*\n  X-Robots-Tag: noindex, nofollow\n'
    open(os.path.join(WEB, '_headers'), 'w').write(noindex +
        '/*.html\n  Cache-Control: no-cache\n/\n  Cache-Control: no-cache\n'
        # 데이터는 5분만(배포 직후 새 화면이 옛 데이터를 한 시간 쓰던 것 방지), 이름에 내용 해시가 든 파일은 1년
        '/data/*\n  Cache-Control: public, max-age=300\n/data/bimg/*\n  Cache-Control: public, max-age=31536000, immutable\n'
        '/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n/img/*\n  Cache-Control: public, max-age=604800\n/img/d/*\n  Cache-Control: public, max-age=31536000, immutable\n')
    n = sum(len(fs) for _, _, fs in os.walk(WEB))
    print('web/ built:', n, 'files')

if __name__ == '__main__':
    main()
