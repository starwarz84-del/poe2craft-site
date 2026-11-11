#!/usr/bin/env bash
# 에뮬레이터·속성부여 제작 규칙 점검(2026-11-11): 내부 함수를 연 사본을 만들어 서버 8801에서 실제 코드로 굴려 봄.
# 결과 줄 앞 XX = 규칙 위반. 사용: bash tools/test/rules/run.sh
set -e
R=$(cd "$(dirname "$0")/../../.." && pwd)/site; T=${T:-/tmp/poe2rules}; mkdir -p $T; cd $T
ln -sfn $R/data data; ln -sfn $R/img img
python3 - "$R" <<'P'
import sys; R=sys.argv[1]
e=open(R+'/emulator.html').read().replace("boot().catch(err=>","window.__E={S,apply,check,pool,essTiersFor,essWhy,newItem,loadClass,socketRune,grp,genOf,rareCap,magicCap,craftedCount,craftedLimit,startReveal,chooseReveal,revealOptions,runesList,runeAt,maxSockets,qmax,render,renderShelves,manualWhy,isDes,isMark,base:()=>base()};\nboot().catch(err=>",1)
open('emu.html','w').write('<meta charset="utf-8">\n'+e)
b=open(R+'/index.html').read().replace("loadIndex().catch(err=>","window.__B={S,reason,assignAffix,assignRune,loadClass,selectBase,maxOf,craftedCount,craftedLimit,runesList,sockets,render,maxQuality,setCorr,toggleAffix};\nloadIndex().catch(err=>",1)
open('bld.html','w').write('<meta charset="utf-8">\n'+b)
P
python3 -m http.server 8801 >/dev/null 2>&1 & PID=$!; sleep 1
D=$(dirname "$0"); cd "$R/../tools/test/rules"
node emu_rules.js; node runes_builder.js
kill $PID
