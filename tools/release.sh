#!/usr/bin/env bash
# 빌드 → 검사 → 점수 → 배포 폴더까지 한 번에 (2026-11-11). 순서를 빼먹어 생기는 실수를 막으려고 만듦.
#   bash tools/release.sh            빌드 + 빠른 검사 + 크래프팅 점수 + 배포 폴더 + 배포 폴더 검수
#   bash tools/release.sh --full     위 + 제작 옵션 한도 점검(c1check, 약 2분) + 리버스 점수(_revscore, 약 15분)
# 끝에 '문제 n'이 0이 아니면 커밋하지 말고 위 출력에서 '!!' 줄을 봄. 커밋·푸시는 하지 않음.
set -u
ROOT=/home/claude/poe2data; [ -e "$ROOT" ] || ln -s "$(cd "$(dirname "$0")/.." && pwd)" "$ROOT"
cd "$ROOT"; FULL=0; [ "${1:-}" = "--full" ] && FULL=1; BAD=0
step(){ echo; echo "== $1"; }
fail(){ echo "!! $1"; BAD=$((BAD+1)); }

step "1. 데이터·레시피 빌드"
( cd scripts && python3 build_prices.py >/dev/null && python3 build_tips.py >/dev/null && python3 build_recipes.py | tail -1 && python3 build_special.py >/dev/null && python3 graphs/patch_astrid.py ) || fail "빌드 실패"
python3 i18n/build.py | tail -1 || fail "i18n 빌드 실패"

step "2. 검사 (테스트 서버)"
bash tools/test/serve.sh stop >/dev/null 2>&1; bash tools/test/serve.sh start >/dev/null || fail "테스트 서버 시작 실패"
( cd tools/test
  node build_samples.js >/dev/null 2>&1 || echo "!! build_samples"
  node build_board.js   >/dev/null 2>&1 || echo "!! build_board"
  n=$(node ver.js 2>&1 | grep -c "오류"); [ "$n" = 0 ] && echo "리버스 검산 오류 0" || echo "!! 리버스 검산 오류 $n"
  node share.js 2>&1 | grep -c "^FAIL" | sed 's/^0$/공유 검사 통과/; t; s/^/!! 공유 검사 실패 /'
  node _gradesame.js 2>&1 | tail -1
  # 리버스 빠른 점검: 분열·매직 구입·주얼·장신구 6개로 초안 → 검산 → 시뮬 (2026-11-11: 분열 아이템 초안이 통째로 깨진 것을 ver.js가 못 잡았음)
  r=$(NOSAVE=1 node _revscore.js diztoh-vile-robe-v2-bal farmer-budget-armour-v2-ess sihan-chayula-amulet-v2-bal mazbro-sceptre-v2 zenm-timelost-sapphire-v2-ess breach-ring-video-v2-bal 2>&1 | tail -1); echo "리버스 6개: $r"
  echo "$r" | grep -q "검산 오류 0 · 시뮬 문제 0" || echo "!! 리버스 빠른 점검 실패"
  node _score.js >/dev/null && node skipcheck.js > skipcheck.txt; tail -1 skipcheck.txt
) | tee /tmp/poe2-release.log; BAD=$((BAD + $(grep -c '^!!' /tmp/poe2-release.log)))
python3 tools/test/essence_tier.py | tail -1
python3 tools/test/essence_tier.py | tail -1 | grep -q " 0 problem" || fail "에센스 등급 오류"
if [ $FULL = 1 ]; then
  step "2-1. 제작 옵션 한도 점검"; node tools/sim/c1check.js | tail -1; node tools/sim/c1check.js >/dev/null; python3 -c "import json,sys; sys.exit(1 if json.load(open('tools/sim/c1check.json')) else 0)" || fail "제작 옵션 한도 위반"
  step "2-2. 리버스 점수 (오래 걸림)"; ( cd tools/test && node _revscore.js | tail -1 ) && python3 tools/test/revscore_md.py >/dev/null
fi

step "3. 크래프팅 점수"
python3 scripts/score_recipes.py | head -1 | tee /tmp/poe2-score.log
grep -q "<70: 0" /tmp/poe2-score.log || fail "70점 미만 레시피 있음 — docs/recipe-notes.md 점수표 확인"
bash tools/test/serve.sh stop >/dev/null 2>&1

step "4. 배포 폴더"
python3 scripts/build_web.py | tail -1 || fail "배포 폴더 빌드 실패"
( cd web && python3 -m http.server 8790 >/dev/null 2>&1 & echo $! > /tmp/poe2-web.pid ); sleep 1
( cd tools/test && node _web.js 2>&1 | tail -1 ) | tee /tmp/poe2-web.log
kill "$(cat /tmp/poe2-web.pid)" 2>/dev/null
grep -q "ERRORS 0" /tmp/poe2-web.log || fail "배포 폴더 검수 오류"

echo; echo "문제 $BAD"; [ $BAD = 0 ]
