# 인계 문서: 제작 정책 정리 → 크래프팅·리버스 크래프팅 점수 올리기

작성 2026-11-11. 새 세션이 이 파일 하나로 일을 시작할 수 있게 썼어요. 사용자(Atom1q84)는 개발자가 아니고, 답은 **항상 한국어**로 해요.

## 1. 저장소와 준비

- 저장소: `https://github.com/starwarz84-del/poe2craft-site` (브랜치 `main`, 푸시하면 Cloudflare Workers가 poe2craft.xyz에 자동 배포)
- Claude 아티팩트판: `https://claude.ai/artifact/Me2XFis1VHa9dchhbv66x1` (게시 방법은 CLAUDE.md "빌드 · 테스트 · 게시")
- 클론 뒤 먼저 링크를 만들어요. 스크립트들이 `/home/claude/poe2data` 절대경로를 써요.

```
[ -e /home/claude/poe2data ] || ln -s /home/claude/poe2craft-site /home/claude/poe2data
```

- Playwright는 세션에 이미 있어요(재설치 금지). `build_web.py`는 `pip install brotli --break-system-packages`가 필요할 수 있어요.
- 푸시 전 `git pull --rebase`. `web/fonts/SUIT-Variable.woff2`가 충돌하면 `git checkout --ours` 뒤 `python3 scripts/build_web.py`로 다시 만들어요(다른 세션도 같은 저장소를 고쳐요).

## 2. 읽는 순서

1. `CLAUDE.md` — 작업 인계 문서 전체. 정책 원문이 여기 있어요(약 350줄).
2. `docs/writing-style.md` — 답·화면 문구·꿀팁·문서 글쓰기 기준.
3. `docs/game-rules.md` — 게임 규칙과 근거(데이터·영상·사용자 확정·추정 구분).
4. `docs/graph-model.md` — 플로우차트(그래프) 데이터 모델과 시뮬레이터.
5. `docs/crafting-knowhow.md` — 상황 → 방법 표 K1~K30, 비싼 징조 시세.
6. `docs/recipe-notes.md` — 작업 기록, 낮은 점수 분석, 리버스 연습 기록, 자동 점수표.

## 3. 이번 일의 목표

사용자 요청(2026-11-11): 지금까지 쌓인 제작 정책을 한 번 싹 정리해서, 크래프팅 레시피와 리버스 크래프팅이 더 높은 점수를 받게 하는 것.

정책은 CLAUDE.md 안에 날짜순으로 덧붙여져 있어서 같은 주제가 여러 곳에 흩어져 있어요. 예를 들어 절사·말소는 정책 13·14·19·23④·발굴 규칙 5·8에, 제작 옵션(에센스·합금·심연)은 정책 11·17과 발굴 규칙 6에, 등급은 정책 25·30·32에 나뉘어 있어요. 배치마다 붙인 긴 기록(9차~27차)도 정책과 섞여 있어요.

### 해 줄 일

1. **정책 정리본 `docs/policies.md`** — 주제별로 묶어요(베이스·시작 상태 / 매직·레어 전환 / 카오스·엑잘 / 실패 정리와 비싼 징조 / 제작 옵션 / 훼손·공개·뼈·군주 징조 / 퀄리티·장신구 촉진 / 주얼·액체 / 룬·소켓 / 등급·난이도·가격 / 플로우차트 작성·그리기 / 화면 용어·문구 / 리버스 전용 규칙). 각 규칙에 원래 정책 번호와 확정 날짜를 남겨요. 서로 부딪치는 규칙은 지우지 말고 "충돌" 목록으로 따로 모아 사용자에게 물어요.
2. **CLAUDE.md 다이어트** — 배치별 긴 기록(플로우차트 표 칸의 9차~27차 등)은 `docs/recipe-notes.md` 작업 기록으로 옮기고, CLAUDE.md에는 정책 정리본 링크와 꼭 필요한 작업 방법만 남겨요. 옮기기 전에 사용자에게 구조를 한 번 보여 주고 확인받아요.
3. **크래프팅 점수 올리기** — 점수표의 감점 이유별로 고쳐요(아래 4장).
4. **리버스 크래프팅 점수 올리기** — 정리한 정책을 `site/reverse.html` `makeDraft`·`site/graphify.js`에 맞춰 반영해요(아래 5장).

정책 자체를 바꾸는 판단(예: 영상 방식 대신 더 싼 방식)은 사용자 확정 사항이라 혼자 정하지 말고 근거(시뮬 비용 비교)와 함께 물어요.

## 4. 크래프팅 점수

점수 기준은 `scripts/score_recipes.py` 맨 위에 있어요(100점).

| 항목 | 배점 | 내용 |
|---|---|---|
| A 완성 조건 | 20 | 플로우차트 시뮬 완성품이 완성 조건을 만족한 비율(`reqOk`) |
| B 가중치 | 15 | 가중치를 모르는 단계 하나마다 −5 |
| C 실패 처리 | 15 | 확률 단계인데 실패 처리가 없는 단계 하나마다 −5 |
| D 비용 일치 | 15 | 레시피 엔진 비용 ÷ 시뮬 평균이 1.5배 안이면 15, 2.5배 10, 4배 5 |
| E 등급 차이 | 10 | 같은 그룹 다른 등급과 비용이 5% 넘게 달라야 함(정책 32) |
| F 근거 | 10 | 영상·글 주소 |
| G 과정 | 15 | skipcheck 문제 하나마다 −5 |

지금 상태(2026-11-11): 레시피 136개, 평균 94.1점, 70점 미만 0개. 감점이 많은 순서는 D 45개, B 22개, E 4개, C 4개, F 2개예요.

D가 가장 많아요. 원인은 대부분 레시피 엔진(`site/recipes.html` `analyse`, 기대값 계산)과 시뮬(`site/sim.js`, 실제 굴림)이 같은 일을 다르게 세는 데 있어요. 알려진 차이:
- 엔진은 좋은 옵션을 잃었을 때 앞 구간 전체를 시도 수 × 손실 비율로 다시 곱해서 크게 셈(치명타 투구 A 구간 1,690 vs 시뮬 985).
- 엔진은 촉진하는 찬미의 징조 엑잘을 p=1로 봄(시뮬은 기폭제 퀄리티 % 확률, 사용자 경험값).
- 엔진 anyOf 하나가 여러 저항을 한 번에 세는 경우(Unstoppable 갑옷).

먼저 할 일은 엔진과 시뮬 중 어느 쪽 모델을 기준으로 맞출지 사용자와 정하는 것이에요. 지금 화면의 플로우차트 비용은 시뮬 값이고, 레시피 탭 비용은 엔진 값이에요.

점수 다시 매기기(테스트 서버 필요):

```
cd /home/claude/poe2data && bash tools/test/serve.sh start
node tools/test/_score.js
node tools/test/skipcheck.js > tools/test/skipcheck.txt
python3 scripts/score_recipes.py
```

## 5. 리버스 크래프팅 점수

리버스 = 붙여 넣은 아이템 → 옵션 분석 → 필수/유효/잡옵 지정 → 초안(`makeDraft`) → 플로우차트(`graphify.js` `fromDraft`) → 시뮬 검사 → 등급 레시피 묶음 → 미리보기 → 크래프팅 목록에 올리기.

점수 = 같은 완성품의 등록 레시피 비용 대비 초안 비용 배수(1.5배 안 = 좋음, 5배 넘음 = 낮음). 연습 스크립트 `tools/test/_rev3.js`(등록 레시피 122개의 완성품으로 초안을 만들어 비교).

지금 상태: 중앙값 3.85배(콜르 가중치 반영 뒤 4.24배), 1.5배 안 33개, 5배 넘음 53개, 검산 오류 0.

가장 큰 원인은 엑잘 실패 정리를 좌측·우측 소멸의 징조(약 10~20 div) 반복으로 하는 초안이에요. 5배 넘는 53개 중 18개가 여기서 비용 대부분이 나와요. 등록 레시피는 같은 자리를 ① 반대쪽이 비어 있을 때 먼저 만들어 징조 없는 소멸의 오브로 지우거나 ② 결과 그대로 받거나 ③ 결정화 + 심연의 에센스(약 0.1 div)로 정리해요. `docs/recipe-notes.md` "리버스 연습 기록"에 다음 할 일이 적혀 있어요: 엑잘 실패 정리를 가장 싼 방법 순(징조 없는 소멸의 오브 → 결정화 + 심연의 에센스 → 좌측·우측 소멸의 징조)으로 고르고, 그 순서가 되도록 작업 순서를 바꾸기. 노하우 표의 "리버스 적용" 칸(자동·선택·제안)도 정리 대상이에요.

## 6. 꼭 지킬 것

- 레시피를 만들거나 고치면 플로우차트 먼저(정책 31), 그다음 같은 단계 id로 등급 레시피. 그래프에 없는 단계는 레시피에도 넣지 않아요.
- 레시피·리버스를 고치면 `docs/recipe-notes.md` 작업 기록 한 줄 + 점수 다시 매기기, 70점 미만은 원인 분석 뒤 고치기.
- 커런시·징조·뼈·옵션 이름은 게임 데이터(crafting.json kr) 공식 이름 그대로, 줄이지 않기.
- 용어: 제작 과정의 버릴 옵션 = '잡옵', 완성품의 나오는 대로 옵션 = '랜덤 옵션'. 옵션을 세는 말은 '옵션'('줄' 아님).
- 훼손 옵션은 아이템당 하나. 완성품 카드의 훼손 표시는 시뮬 과정 기준(`res.desStat`).
- 타락·축성은 깊게 다루지 않음(정책 33).
- 레딧처럼 막힌 사이트는 우회하지 않음.
- 사이트 화면 문구는 명사형·짧게, '~요' 금지(예외: 전문가 이상 비용 안내는 '~습니다').
- 다른 세션이 같은 저장소와 아티팩트를 고쳐요. 커밋 전 `git pull --rebase`, 아티팩트 게시는 바뀐 파일만.

## 7. 주요 파일

| 무엇 | 파일 |
|---|---|
| 레시피 정의 | `scripts/recipes_v5_*.py`(원본), `scripts/recipes_v5_zz-batchz<n>-v2.py`(등급), `scripts/recipes_v5_zzz-grade-tiers.py`(등급 티어 넓히기) |
| 플로우차트 생성 | `scripts/graphs/gen_batch<n>.py` → `scripts/graphs/<id>.json` |
| 시뮬 | `site/sim.js`, `tools/sim/run.js <id> [20000]` → `site/data/sim/<id>.json`, 디버그 `tools/sim/dbg.js` |
| 엔진(기대값) | `site/recipes.html` `analyse`, 비교 `tools/sim/engine.js` |
| 리버스 | `site/reverse.html`(`makeDraft`·`verifyDraft`·`bestDraft`), `site/graphify.js` |
| 빌드 | `scripts/build_recipes.py`(REPLACES·FRSTART), `scripts/notes_short.py`(짧은 설명·꿀팁 연결), `scripts/build_tips.py`, `i18n/build.py`, `scripts/build_web.py` |
| 점검 | `tools/test/audit.js`·`ver.js`·`eng.js`·`skipcheck.js`·`_score.js`·`_rev3.js`·`_fclines.js`, `tools/test/style_lint.py` |
