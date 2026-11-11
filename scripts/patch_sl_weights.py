"""SL 게임연구소 실험(카오스 오브 10,000회) 결과로 주얼 옵션 가중치를 채움.
raw/sl_lab/<표>.tsv(옵션 문구 · 나온 횟수) → site/data/c/<주얼>.json 티어 가중치(=나온 횟수, 상대값). 그룹에 wsrc:'sl' 표시.
콜르의 사냥 장갑 표는 증강물(x) 옵션 추정 가중치(1000/500)라 Gloves_*.json의 x 그룹에 넣음.
build_site_data.py 끝에서 자동 실행. 단독: python3 scripts/patch_sl_weights.py"""
import json, re, os
R = '/home/claude/poe2data'
C = f'{R}/site/data/c'
def norm(s):
    s = s.split('\n')[0].replace('—', '-').replace('–', '-')
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'^반경내(소형|주요)패시브스킬이', '', s)
    return re.sub(r'도부여$', '', s)
JEWELS = {'sapphire': 'Sapphire', 'emerald': 'Emerald', 'ruby': 'Ruby',
          'timelost-sapphire': 'Time-Lost_Sapphire', 'timelost-emerald': 'Time-Lost_Emerald', 'timelost-ruby': 'Time-Lost_Ruby'}

def rows(name):
    out = []
    for l in open(f'{R}/raw/sl_lab/{name}.tsv', encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        c = l.rstrip('\n').split('\t'); out.append((c[0], c[-2], int(c[-1])))
    return out

def patch(cls, rs, secs, report):
    p = f'{C}/{cls}.json'; d = json.load(open(p, encoding='utf-8')); hit = 0; miss = []
    idx = {}
    for gi, g in enumerate(d['groups']):
        if g.get('s') not in secs: continue
        for ti, t in enumerate(g['t']): idx.setdefault((g['g'], norm(t[4])), []).append((gi, ti))
    for side, txt, w in rs:
        k = (side, norm(txt)); m = idx.get(k)
        if not m:   # 반경 줄('반경이 중형으로 …')은 면 표시가 다를 수 있어 면 없이 한 번 더
            m = [v for (s, t), vs in idx.items() if t == k[1] for v in vs]
        if not m: miss.append(f'{side} {txt}'); continue
        for gi, ti in m:
            g = d['groups'][gi]; g['t'][ti][1] = w; g['wsrc'] = 'sl'; hit += 1
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    report.append(f'{cls}: {hit} tiers' + (f', 못 찾음 {len(miss)}: ' + ' / '.join(miss) if miss else ''))

if __name__ == '__main__' or True:
    rep = []
    for f, cls in JEWELS.items():
        if os.path.exists(f'{C}/{cls}.json'): patch(cls, rows(f), ('n',), rep)
    kolr = rows('kolr-gloves')
    for f in os.listdir(C):
        if f.startswith('Gloves'): patch(f[:-5], kolr, ('x',), rep)
    print('patch_sl_weights:', *rep, sep='\n  ')
