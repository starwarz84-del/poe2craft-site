"""대조표에서 '우리 값이 1 이하(모름)이고 CoE 같은 레벨 티어에 값이 있는' 가중치만 뽑아 패치 파일로 저장.
사용: python3 -I tools/coe/make_patch.py <compare 결과 json> raw/coe_weights_patch.json"""
import json, sys, datetime
cmp = json.load(open(sys.argv[1])); patch = {'source': 'Craft of Exile (craftofexile.com, poec_data.json)', 'made': datetime.date.today().isoformat(),
  'rule': '우리(poedb) 가중치가 1 이하인 티어에, 같은 아이템 레벨 티어의 CoE 가중치가 1보다 클 때만 채움', 'fills': {}}
n = 0
for cls, L in cmp.items():
    for x in L:
        coe = {l: w for l, w in x['coe']}
        f = [[ti, l, coe[l]] for ti, (l, w) in enumerate(x['ours']) if w <= 1 and coe.get(l, 0) > 1]
        if f: patch['fills'].setdefault(cls, {})[str(x['gi'])] = f; n += len(f)
json.dump(patch, open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
print('tiers filled:', n, 'groups:', sum(len(v) for v in patch['fills'].values()))
