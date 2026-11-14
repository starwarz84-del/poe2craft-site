#!/usr/bin/env bash
# 빌드 → 검사 → 점수 → 배포 폴더까지 한 번에 (2026-11-11). 순서를 빼먹어 생기는 실수를 막으려고 만듦.
#   bash tools/release.sh            빠른 모드(작업 중·커밋 전): 빌드 + 검사 + 크래프팅 점수 + 배포 폴더 + 배포 폴더 검수.
#                                    리버스 점검은 리버스 파일(REV_FILES)이 origin/main 대비 또는 마지막 통과 이후 바뀌었을 때만, 그것도 가볍게
#                                    (_revparse·ver = 부위마다 대표 하나, _revscore = 3개, _revtpl 4개). 안 바뀌었으면 '건너뜀(리버스 변경 없음)'.
#   bash tools/release.sh --full     배포 전: 빠른 시뮬(quick:true)을 --final로 다시 돌림 + 리버스 점검 전부(_revparse 240회·ver 전부·_revtpl)
#                                    + 제작 옵션 한도(c1check) + 리버스 전체 점수(_revscore 전부, revscore.json 저장).
#   REV=1 bash tools/release.sh      리버스 파일이 안 바뀌어도 가벼운 리버스 점검을 돌림.
# 끝에 '문제 n'이 0이 아니면 커밋하지 말고 위 출력에서 '!!' 줄을 봄. 커밋·푸시는 하지 않음.
# RT 2026-11-14(사용자: 테스팅 구간 줄이기): 빠른·전체 모드 분리, 걸린 시간 출력.
set -u
ROOT=/home/claude/poe2data; [ -e "$ROOT" ] || ln -s "$(cd "$(dirname "$0")/.." && pwd)" "$ROOT"
# 동시에 두 번 돌면 테스트 서버(8779)를 서로 껐다 켜서 결과가 깨짐(RT 11-14: 작업자 둘이 같은 때 돌린 사고) → 앞 것이 끝날 때까지 기다림
exec 8>/tmp/poe2-release.lock; flock -n 8 || { echo "다른 release.sh가 돌고 있어 끝날 때까지 기다림"; flock 8; }
cd "$ROOT"; FULL=0; [ "${1:-}" = "--full" ] && FULL=1; BAD=0; T0=$(date +%s); TS=$T0
STEPN=0; step(){ local now; now=$(date +%s); [ $STEPN -gt 0 ] && echo "   ($((now-TS))초)"; STEPN=$((STEPN+1)); TS=$now; echo; echo "== $1"; }
fail(){ echo "!! $1"; BAD=$((BAD+1)); }
export FAST=1   # 점검 스크립트가 초안 '최소 10초' 계산 시간을 뺌(화면 동작은 그대로)

# 리버스 파일이 바뀌었나: origin/main 대비(커밋·수정·새 파일) 그리고 마지막으로 리버스 점검을 통과한 때의 내용(해시, 저장소 밖 파일)과 비교
REV_FILES="site/reverse.html site/graphify.js site/fcread.js site/sim.js tools/test/_regcard.js"
REV_LIST(){ echo $REV_FILES; ls tools/test/_rev*.js; }
REV_STAMP=/home/claude/.poe2-release-rev
REV_HASH=$(cat $(REV_LIST) 2>/dev/null | sha1sum | cut -c1-40)
REV_DIFF=$( { git diff --name-only origin/main -- $(REV_LIST); git ls-files --others --exclude-standard -- 'tools/test/_rev*.js'; } 2>/dev/null | sort -u | tr '\n' ' ')
if [ $FULL = 1 ]; then REVMODE=full
elif [ -n "${REV:-}" ]; then REVMODE=light
elif [ -z "$REV_DIFF" ]; then REVMODE=skip; REVWHY="origin/main과 같음"
elif [ "$(cat $REV_STAMP 2>/dev/null)" = "$REV_HASH" ]; then REVMODE=skip; REVWHY="마지막 통과 이후 같음"
else REVMODE=light; fi
echo "리버스 점검: $REVMODE${REV_DIFF:+ (바뀐 파일: $REV_DIFF)}"
# 부위(클래스)마다 대표 완성품 하나 — 등급 이름이 붙은 id(-bal·-ess)를 먼저 골라 앞부분 일치로 형제까지 잡히지 않게
REV_REPS=$(python3 - <<'PY'
import json
R=json.load(open('site/data/recipes.json')); R=R.get('recipes',R); S={s['id'] for s in json.load(open('site/data/samples.json'))['samples']}
pick={}
for r in R:
  if r['id'] not in S: continue
  c=r['cls']; sib=any(x!=r['id'] and x.startswith(r['id']) for x in S)
  if c not in pick or (pick[c][1] and not sib): pick[c]=(r['id'], sib)
print(' '.join(v[0] for v in pick.values()))
PY
)

if [ $FULL = 1 ]; then
  step "0. 빠른 시뮬 결과를 최종 횟수로 (run.js quick:true → --final)"
  node tools/sim/quickcheck.js --rerun | tail -3 || fail "빠른 시뮬 결과가 남음 — node tools/sim/quickcheck.js"
fi

step "1. 데이터·레시피 빌드"
( cd scripts && python3 build_prices.py >/dev/null && python3 build_tips.py >/dev/null && python3 graphs/patch_runes.py >/dev/null && python3 build_recipes.py | tail -1 && python3 build_special.py >/dev/null && python3 graphs/patch_astrid.py && python3 build_revtpl.py | head -1 ) || fail "빌드 실패"
python3 tools/knowhow_index.py >/dev/null || fail "노하우 분류 빠짐 (tools/knowhow_index.py CLS에 추가)"
python3 i18n/build.py | tail -1 || fail "i18n 빌드 실패"

step "2. 검사 (테스트 서버)"
bash tools/test/serve.sh stop >/dev/null 2>&1; bash tools/test/serve.sh start >/dev/null 8>&- || fail "테스트 서버 시작 실패"
( cd tools/test
  node build_samples.js >/dev/null 2>&1 || echo "!! build_samples"
  node build_board.js   >/dev/null 2>&1 || echo "!! build_board"
  node share.js 2>&1 | grep -c "^FAIL" | sed 's/^0$/공유 검사 통과/; t; s/^/!! 공유 검사 실패 /'
  node _gradesame.js 2>&1 | tail -1
  if [ $REVMODE = skip ]; then echo "리버스 점검 건너뜀(리버스 변경 없음 — $REVWHY)"
  else
    if [ $REVMODE = full ]; then ONLY=""; else ONLY="$REV_REPS"; fi
    n=$(node ver.js $ONLY 2>&1 | grep -c "오류"); [ "$n" = 0 ] && echo "리버스 검산 오류 0" || echo "!! 리버스 검산 오류 $n"
    # 리버스 분석 정확도(W1 2026-11-13): 레시피 완성품 × 고급·일반 복사 → 인식 못 한 줄 0, 쪽·분열·훼손 표시 수 일치, 같은 옵션 두 줄, 검산 오류 0 (빠른 모드 = 부위마다 하나)
    r=$(node _revparse.js $ONLY 2>&1 | tail -1); echo "$r"; echo "$r" | grep -q "문제 0" || echo "!! 리버스 분석 점검 실패 — node tools/test/_revparse.js"
    # 리버스 빠른 점검: 초안 → 검산 → 시뮬 (2026-11-11: 분열 아이템 초안이 통째로 깨진 것을 ver.js가 못 잡았음). 빠른 모드 = 분열 방패(하이엔드)·분열 희귀 셉터 구입(밸런스)·분열 장화(에센셜), --full은 2-2 전체 점수가 대신함
    if [ $REVMODE = light ]; then
      r=$(NOSAVE=1 node _revscore.js tankjung-kitava-shield-v2 sihan-chayula-sceptre-v2-bal lilbotq-boots-v2-ess 2>&1 | tail -1); echo "리버스 3개: $r"
      echo "$r" | grep -q "검산 오류 0" || echo "!! 리버스 빠른 점검 실패(검산 오류)"
    fi
    # 리버스 등록 틀(W9 2026-11-14): 등록 완성품 → 자기 그래프가 틀로 잡히고 비용이 등록 시뮬 ±5%
    r=$(N=500 node _revtpl.js icesly-budget-wand-v2-bal diztoh-rarity-ring-v2-bal lilbotq-emerald-v2-bal seek-cyclone-boots-v2-ess 2>&1 | tail -1); echo "$r"; echo "$r" | grep -q "문제 0" || echo "!! 리버스 틀 점검 실패 — node tools/test/_revtpl.js"
  fi
  node _score.js >/dev/null && node skipcheck.js > skipcheck.txt; tail -1 skipcheck.txt
) | tee /tmp/poe2-release.log; BAD=$((BAD + $(grep -c '^!!' /tmp/poe2-release.log)))
node tools/test/_fcparity.js | tail -1 | tee /tmp/poe2-fcparity.log; grep -q "차이 0" /tmp/poe2-fcparity.log || fail "graph2recipe.py ≠ site/fcread.js — node tools/test/_fcparity.js (파이썬을 고쳤으면 fcread.js도 같이)"
node tools/test/_revgrades.js | tail -1 | tee /tmp/poe2-revgrades.log; grep -q "문제 0" /tmp/poe2-revgrades.log || fail "난이도 표 JS(graphify diffOf) ≠ _difftable.py — node tools/test/_revgrades.js"   # W5 2026-11-13
python3 tools/test/fc_noinput.py | tail -1
python3 tools/test/fc_noinput.py | tail -1 | grep -q " 0$" || fail "들어오는 선 없는 상자 있음 — python3 tools/test/fc_noinput.py"
python3 tools/test/essence_tier.py | tail -1
python3 tools/test/runerules.py | tail -1
python3 tools/test/runerules.py | tail -1 | grep -q " 0$" || fail "룬 규칙 위반 — python3 tools/test/runerules.py"
python3 tools/test/essence_tier.py | tail -1 | grep -q " 0 problem" || fail "에센스 등급 오류"
if [ $FULL = 1 ]; then
  step "2-1. 제작 옵션 한도 점검"; node tools/sim/c1check.js | tail -1;   # 한 번만(RT 11-14: 같은 점검을 두 번 돌려 약 5분)
  python3 -c "import json,sys; sys.exit(1 if json.load(open('tools/sim/c1check.json')) else 0)" || fail "제작 옵션 한도 위반"
  step "2-2. 리버스 전체 점수 (revscore.json)"; r=$(cd tools/test && node _revscore.js 2>&1 | tail -1); echo "$r"; python3 tools/test/revscore_md.py >/dev/null
  echo "$r" | grep -q "검산 오류 0" || fail "리버스 전체 점수에 검산 오류 — tools/test/revscore.json"
fi

QS=$(node tools/sim/quickcheck.js | tail -1); echo "$QS"; echo "$QS" | grep -q " 0개" || fail "빠른 횟수로 돌린 시뮬 결과가 있음(커밋 금지) — node tools/sim/quickcheck.js --rerun 또는 run.js <id> --final"

step "2-3. 플로우차트 전수 검사 (tools/test/fcaudit.txt)"
python3 tools/test/fcaudit.py

step "3. 크래프팅 점수"
python3 scripts/score_recipes.py | head -1 | tee /tmp/poe2-score.log
python3 tools/test/fclabel.py -q   # 정책 12장: 고르는 줄의 DB 옵션 연결(아직 정리 중이라 알림만)
grep -q "<70: 0" /tmp/poe2-score.log || fail "70점 미만 레시피 있음 — docs/recipe-notes.md 점수표 확인"
bash tools/test/serve.sh stop >/dev/null 2>&1

step "4. 배포 폴더"
python3 scripts/build_web.py | tail -1 || fail "배포 폴더 빌드 실패"
( cd web && exec python3 -m http.server 8790 >/dev/null 2>&1 ) 9>&- 8>&- & echo $! > /tmp/poe2-web.pid; sleep 1   # exec: 기록한 번호 = 서버 자신, 9>&-: 빌드 잠금을 물려받지 않음(2026-11-12 서버가 남아 잠금을 쥔 사고)
( cd tools/test && node _web.js 2>&1 | tail -1 ) | tee /tmp/poe2-web.log
kill "$(cat /tmp/poe2-web.pid)" 2>/dev/null
grep -q "ERRORS 0" /tmp/poe2-web.log || fail "배포 폴더 검수 오류"

step "끝"
# 리버스 점검이 통과했으면 지금 리버스 파일 내용을 기록 → 다음 빠른 모드는 안 바뀌었으면 건너뜀
if [ $REVMODE != skip ] && ! grep -q '^!! 리버스' /tmp/poe2-release.log; then echo "$REV_HASH" > $REV_STAMP; fi
echo "문제 $BAD · 걸린 시간 $(( ($(date +%s)-T0)/60 ))분 $(( ($(date +%s)-T0)%60 ))초 (모드: $([ $FULL = 1 ] && echo 전체 || echo 빠름), 리버스: $REVMODE)"; [ $BAD = 0 ]
