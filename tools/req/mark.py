#!/usr/bin/env python3
"""분석 요청 처리 결과 기록 → site/data/reqdone.json (배포되면 Worker가 상태로 보여 줌).
python3 tools/req/mark.py <요청 id> done <레시피 id(그룹 id)>
python3 tools/req/mark.py <요청 id> fail "<이유, 화면에 그대로 나옴 — 짧은 명사형>"
"""
import json, sys, datetime, pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'site/data/reqdone.json'
if len(sys.argv) < 4 or sys.argv[2] not in ('done', 'fail'):
    sys.exit(__doc__)
rid, st, val = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.loads(P.read_text() or '{}') if P.exists() else {}
e = {'st': st, 'at': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M')}
if st == 'done': e['recipe'] = val
else: e['why'] = val[:120]
d[rid] = e
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(rid, e)
