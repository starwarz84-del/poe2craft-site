"""Assemble the poe2craft.xyz deploy folder (web/) from the built site.

Run after the normal build (build_recipes.py ... i18n/build.py):
    python3 scripts/build_web.py

web/ is what the host serves (Cloudflare Pages output directory = web, no build command).
- index.html  = site/shell.html (trade-style banner + tab bar)
- tool pages  = site/pub/*.html with site/theme.css injected (colors/fonts only)
- about.html, favicon.svg, sim.js, lib/, data/ copied as they are
"""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
WEB = os.path.join(ROOT, 'web')
DOMAIN = 'poe2craft.xyz'
# Test phase (user decision 2026-11-10): keep the site out of search engines. Set True when it goes public.
INDEX = False
NOINDEX_META = '<meta name="robots" content="noindex, nofollow">\n'
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap">\n'
THEME = '<link rel="stylesheet" href="theme.css">\n'

def main():
    if os.path.isdir(WEB):
        shutil.rmtree(WEB)
    os.makedirs(WEB)
    for f in ['favicon.svg', 'theme.css', 'sim.js']:
        shutil.copy(os.path.join(SITE, f), os.path.join(WEB, f))
    for src, dst in [('shell.html', 'index.html'), ('about.html', 'about.html')]:
        s = open(os.path.join(SITE, src), encoding='utf-8').read()
        if not INDEX:
            s = s.replace('<meta charset="utf-8">\n', '<meta charset="utf-8">\n' + NOINDEX_META, 1)
        open(os.path.join(WEB, dst), 'w', encoding='utf-8').write(s)
    for d in ['data', 'lib']:
        shutil.copytree(os.path.join(SITE, d), os.path.join(WEB, d))
    for f in sorted(os.listdir(os.path.join(SITE, 'pub'))):
        if not f.endswith('.html'):
            continue
        s = open(os.path.join(SITE, 'pub', f), encoding='utf-8').read()
        # theme goes right after the document head the i18n build added; its :root:root rules win over the page's own tokens
        i = s.find('</style>')
        head = FONTS + THEME + ('' if INDEX else NOINDEX_META)
        s = s[:i + 8] + '\n' + head + s[i + 8:] if i >= 0 else head + s
        open(os.path.join(WEB, f), 'w', encoding='utf-8').write(s)
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
        '/*.html\n  Cache-Control: no-cache\n/\n  Cache-Control: no-cache\n/data/*\n  Cache-Control: public, max-age=3600\n')
    n = sum(len(fs) for _, _, fs in os.walk(WEB))
    print('web/ built:', n, 'files')

if __name__ == '__main__':
    main()
