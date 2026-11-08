#!/usr/bin/env bash
# Test server: copies the built pages into $T with debug hooks exposed, links the data folder, serves on :8779.
# Usage: bash tools/test/serve.sh start|stop     (run the build first: see CLAUDE.md)
set -e
ROOT=/home/claude/poe2data; T=${T:-/tmp/poe2test}
if [ "$1" = stop ]; then kill "$(cat $T/.pid)" 2>/dev/null || true; exit 0; fi
mkdir -p $T && cd $T
ln -sfn $ROOT/site/data data
(echo '<meta charset="utf-8">'; cat $ROOT/site/app.html) > app.html
for f in recipes discover emulator builder; do cp $ROOT/site/pub/$f.html .; done
# expose engine internals to the Playwright scripts
sed -i "s/if(location.search.includes('debug')) window.__rec/window.__rec/; s/window.__rec = Object.assign(S, {renderBoard:()=>renderBoard()});/window.__rec = Object.assign(S, {renderBoard:()=>renderBoard(), analyse});/" recipes.html
python3 -m http.server 8779 >/dev/null 2>&1 & echo $! > .pid
sleep 1; echo "serving $T on http://localhost:8779"
