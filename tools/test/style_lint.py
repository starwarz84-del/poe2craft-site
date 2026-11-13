"""글쓰기 기준(docs/writing-style.md) 점검: 꿀팁·레시피 단계 글·화면 문구에서 자주 걸리는 표현을 찾음.
python3 tools/test/style_lint.py [--all]   (--all: 화면 html의 한글 문구까지)"""
import json, re, sys, glob
ROOT = '/home/claude/poe2data'
RULES = [
  ('이중 피동', r'(보여지|되어지|생각되어|만들어지게|불려지|쓰여지)'),
  ('번역투 ~에 있어서', r'에 있어(서)?'),
  ('번역투 ~를 통해', r'[을를]\s?통(해|하여)'),
  ('대명사 그것', r'그것[은이을]'),
  ('상투적 맺음', r'(결론적으로|종합하면|시사하는 바|의미가 크다|라는 점에서)'),
  ('가르치는 말투', r'(주목할 점|기억해야 할|짚어 볼|유의해야 할|명심)'),
  ('과장', r'(혁신적|획기적|압도적|완벽하게|엄청난|최고의)'),
  ('출처 없는 권위', r'(전문가들은|업계에서는|많은 사람들이|흔히들)'),
  ('대구 A가 아니라 B', r'(이|가) 아니라'),
  ('형식 명사 것·점 몰림', r'(것[이은을]?.{0,15}것|점[이은을].{0,15}점[이은을])'),
  ('쉬운 동사', r'(구매하|구입하|기능합|활용하여|진행하여|수행하)'),
  ('띄어쓰기 n 번째', r'(첫|두|세|네|다섯|여섯)번째'),   # '두 번째'(2026-11-13 S3 11번)
  ('영어 섞임', r'(?<![A-Za-z])(tip|div 기준|step|target|option|base)(?![A-Za-z])'),
]
def scan(src, text):
  out=[]
  for name, rx in RULES:
    for m in re.finditer(rx, text):
      out.append((src, name, text[max(0,m.start()-25):m.end()+25].replace('\n',' ')))
  return out
hits=[]
tips=json.load(open(f'{ROOT}/site/data/tips.json')); tips=tips.get('tips',tips)
for i,t in enumerate(tips,1):
  for k in ('title','body'):
    v=(t.get(k) or {}).get('kr','')
    hits+=scan(f'꿀팁 #{i} {k}', v)
R=json.load(open(f'{ROOT}/site/data/recipes.json')); R=R['recipes'] if isinstance(R,dict) else R
seen=set()
for r in R:
  for n in r['nodes']:
    for k in ('br','label','note'):
      v=(n.get(k) or {}).get('kr','') if isinstance(n.get(k),dict) else ''
      if v and (k,v) not in seen: seen.add((k,v)); hits+=scan(f'{r["id"]} {n["id"]} {k}', v)
if '--all' in sys.argv:
  for f in sorted(glob.glob(f'{ROOT}/site/*.html')):
    s=open(f).read()
    for m in re.finditer(r"L\('([^']*[가-힣][^']*)'", s):
      hits+=scan(f.split('/')[-1], m.group(1))
from collections import Counter
c=Counter(h[1] for h in hits)
for h in hits: print(f'[{h[1]}] {h[0]}: …{h[2]}…')
print('\n합계', len(hits), dict(c))
