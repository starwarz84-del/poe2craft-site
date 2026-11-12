#!/usr/bin/env bash
# Test server: copies the built pages into $T with debug hooks exposed, links the data folder, serves on :8779.
# Usage: bash tools/test/serve.sh start|stop     (run the build first: see CLAUDE.md)
set -e
ROOT=/home/claude/poe2data; T=${T:-/tmp/poe2test}
if [ "$1" = stop ]; then kill "$(cat $T/.pid)" 2>/dev/null || true; exit 0; fi
mkdir -p $T && cd $T
ln -sfn $ROOT/site/data data
ln -sfn $ROOT/site/img img   # 카드 머리 모서리 그림(img/tt) 등 — 실제 사이트와 같게(2026-11-12)
(echo '<meta charset="utf-8">'; cat $ROOT/site/app.html) > app.html
for f in recipes discover emulator builder bases; do cp $ROOT/site/pub/$f.html .; done
cp $ROOT/site/sim.js $ROOT/site/graphify.js .
# expose engine internals to the Playwright scripts
sed -i "s/if(location.search.includes('debug')) window.__rec/window.__rec/; s/window.__rec = Object.assign(S, {renderBoard:()=>renderBoard()\(, [^}]*\)\?});/window.__rec = Object.assign(S, {renderBoard:()=>renderBoard()\1, analyse, prepRecipe});/" recipes.html
# 검사 스크립트는 모든 레시피를 엔진으로 계산하니 클래스 파일을 처음에 다 받음(실제 사이트는 목록 요약만, ?lite 로 실제와 같게)
sed -i "s/S.recipes.filter(r=>!S.board\[r.id\])/S.recipes.filter(r=>!S.board[r.id] || !location.search.includes('lite'))/" recipes.html
grep -q "includes('lite')" recipes.html || { echo 'serve.sh: lite sed failed'; exit 1; }
python3 -m http.server 8779 >/dev/null 2>&1 & echo $! > .pid
sleep 1; echo "serving $T on http://localhost:8779"
