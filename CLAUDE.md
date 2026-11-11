# POE2 크래프팅 사이트 — 작업 인계 문서

이 문서는 새 세션에서 작업을 그대로 이어가기 위한 안내서예요. 새 세션은 **이 파일을 먼저 끝까지 읽고** 시작해요.

## 사용자와 일하는 방식

- 사용자(Atom1q84)는 개발자가 아니에요. **항상 한국어로** 답해요.
- 복사해서 쓸 내용은 코드 블록에 넣고, 블록 안 줄 앞에 공백을 두지 않아요.
- **화면은 최대한 간결하게**(사용자 확정 2026-11-08): 제작 자체가 복잡하니 꼭 필요한 정보만 보여요. 데이터 출처 같은 부가 정보는 화면에 넣지 않고 `docs/game-rules.md`에만 적어요.
- 유튜브 영상을 분석할 때는 소리를 꺼요.
- **글쓰기 기준**(사용자 제공 2026-11-11): 답·화면 문구·꿀팁·문서 모두 `docs/writing-style.md`를 따라요(대구·세 개 맞춤·상투적 맺음·번역투·이중 피동·굵은 글씨와 글머리표 남발 금지, 문장 길이 섞기, 끝에서 다시 요약하지 않기).
- **용어: 잡옵 = 제작 과정, 랜덤 옵션 = 완성품**(사용자 확정 2026-11-11): 단계·플로우차트 상자·왼쪽 옵션 칸처럼 만드는 중인 아이템의 버릴 옵션은 '잡옵', 완성품 카드(개요 완성 카드·마지막 단계 카드·플로우차트 완성품 카드)의 나오는 대로 둔 옵션은 '랜덤 옵션'(`itemTipHTML` `opt.final`).
- **화면 문구에서 옵션을 세는 말은 '줄'이 아니라 '옵션'**(사용자 확정 2026-11-10): "잡옵 1줄" → "잡옵 1개", "랜덤 1줄" → "랜덤 옵션 1개", "좋은 줄" → "좋은 옵션". 영상 제목은 그대로. 일괄 변환 도구 `python3 tools/opt_word.py <파일…>`(동사 '줄이다'·'해 줄'·'아이템 이름 줄'은 건드리지 않음).
- 사용자가 고친 정책은 `docs/policies.md`에 바로 반영해서 다음 세션도 따르게 해요(아래 "제작 정책").
- **레시피 노트 습관**(사용자 확정 2026-11-11): 레시피(플로우차트·등급 레시피·리버스 초안)를 만들거나 고치면 **항상 `docs/recipe-notes.md`를 업데이트** — 점수 다시 매기기(`node tools/test/_score.js` → `node tools/test/skipcheck.js > tools/test/skipcheck.txt` → `python3 scripts/score_recipes.py`, 테스트 서버 필요), 작업 기록 한 줄, **70점 미만이면 이유를 분석하고 해결책을 찾아** 고친 뒤 결과까지 적음. 점수 기준은 `docs/policies.md` 15장(크래프팅 `scripts/score_recipes.py`, 리버스 `tools/test/_revscore.js`).
- **제작 노하우**: `docs/crafting-knowhow.md`(상황 → 방법 표 K1~K15, 시세로 본 비싼 징조, 출처). 새 노하우는 여기에 추가하고 리버스 적용 칸(자동·선택·제안)을 적음.

## 무엇을 만드는가

Path of Exile 2 아이템 제작 사이트. 탭 5개짜리 한 화면이에요.

| 탭 | 원본 파일 | 게시 파일 | 하는 일 |
|---|---|---|---|
| 에뮬레이터 | `site/emulator.html` | `pub/emulator.html` | 화폐를 직접 써 보는 제작 시뮬레이터. "다음 결과 확률" 목록 줄마다 티어 선택(그 티어 이상이 붙을 확률) + "올리기"(그 티어로 아이템에 붙이기, 사용자 확정 2026-11-10). 스크린샷 `tools/test/_shots_tier.js`. **화면 배치**(사용자 확정 2026-11-11: 커런시에서 장비까지 너무 멀어 옮기기 불편): 창 폭 1280px 이상이면 베이스 목록을 왼쪽에 고정(서랍 대신 `DOCK`) → 아이템 → 커런시(최대 640px, 칸 46px)를 아이템 바로 옆에, 그보다 좁으면 예전처럼 서랍 + '베이스 변경'. 스크린샷 `tools/test/_emu.js`. **부위·세부 종류 = 드롭다운 2개**(`.pickrow` `#cats`·`#clss`, 사용자 확정 2026-11-11 — 속성부여도 같음, 속성부여는 옵션 분류·세부 분류도 드롭다운 `#toptabs`·`#subtabs`), 휴대폰(520px 이하)은 커런시 분류 4칸 2줄. **룬 칸**(2026-11-11): 분류 = 룬·알두르 룬·유산·영혼핵·우상·기타(`RCAT`, 그 아이템에 있는 분류만), 전체 보기는 분류별 제목 줄(`.rsec`), 목록은 안쪽 스크롤 없이 전체 높이. 데이터 확인: poe2db 유산 룬 63개 모두 클래스 파일에 있음(부위별), 알두르 4종은 **모든 무기**(사용자 확정 2026-11-11 — 룬 설명이 '무기:'(무도 무기·'마법봉 또는 지팡이'와 구분)이고 '희귀 무기 빈 홈에 장착', Diztoh 활도 알두르의 숨결 사용. poe2db 클래스 페이지엔 시전자 무기에만 있어서 `scripts/patch_aldur_runes.py`가 채움 — build_site_data.py 끝에서 자동 실행) |
| 옵션 빌더 | `site/index.html` | `pub/builder.html` | 원하는 옵션 조합 만들기. 티어 칩 = 고르면 슬롯에 올림, 고른 줄의 오른쪽 숫자 = "Tn 이상" 확률(같은 면 일반 옵션 가중치 기준, `tierShare`), 칩에 마우스를 올리면 그 티어 이상 확률 |
| 레시피 | `site/recipes.html` | `pub/recipes.html` | 유튜브 영상 기반 제작 레시피, 단계별 확률(가중치 계산) |
| 발굴 | `site/reverse.html` | `pub/discover.html` | 아이템 텍스트 → 옵션 분석 → 레시피 초안 → 검산 → 레시피 탭에 올리기 |
| 특수 베이스 | `site/bases.html` | `pub/bases.html` | 특수 베이스 안내(사용자 확정 2026-11-10: 따로 안내 페이지, 모든 특수 베이스). 데이터 `scripts/build_special.py` → `site/data/special.json`(게임 데이터만: 스킬 부여 목걸이·면 개수 바뀌는 장신구·균열 반지·다른 부위처럼 쓰는 베이스·룬벼림/룬숙련 691개, 그 베이스를 쓰는 레시피 링크 → 껍데기 `poe2-goto`). 레시피를 추가하면 build_special.py 다시 실행. 스크린샷 `tools/test/_shots_bases.js` |

- 껍데기: `site/app.html` (탭 = iframe, `SRC` 맵, 언어 전환, 다운로드 중계, 발굴 → 레시피 초안 전달 `poe2-draft` 메시지, 공유 레시피 저장소 중계)
- **공유 레시피(아티팩트 db)**: 문서 `shared/<사용자 id>` = `{recipes:{<s-id>:{recipe, at}}}`. 규칙: 모두 읽기, 각자 자기 문서만 쓰기, 소유자는 전체 정리 가능.
  껍데기가 db를 구독해 레시피 탭에 `poe2-shared`로 넘기고, 레시피 탭은 `poe2-share`/`poe2-unshare`로 등록·취소를 요청해요.
  레시피 탭: 초안 상세의 "공유 레시피로 등록"(id `draft-x` → `s-x`), 내 공유 레시피는 "공유 취소". 남의 새 레시피는 탭 배지 + 오른쪽 아래 알림 + NEW 표시(본 시점은 localStorage `poe2seen`).
  공유 데이터는 남이 쓴 것이라 레시피 탭 `cleanShared`가 `<>"`` 제거·필드 검사·엔진 시험 계산 후에만 표시해요.
  링크로 보는 사람(보기 권한)은 읽기만 가능해서 등록 버튼이 안 보여요. 테스트: `tools/test/share.js`(가짜 db).
- **플로우차트 + 전체 공정 시뮬레이션**(`docs/graph-model.md`): 그래프 레시피 `scripts/graphs/<id>.json`(`gen_batch<n>.py`가 만듦) → `site/sim.js` → `node tools/sim/run.js <id> [20000]` → `site/data/sim/<id>.json` → 레시피 탭 '플로우 차트'. 엔진 비교값 `node tools/sim/engine.js <레시피 id> > tools/sim/engine/<그래프 id>.json`(테스트 서버 필요, run.js 전에). 디버그 `tools/sim/dbg.js`·`reveal_odds.js`·`fincheck.js`·`desstat.js`·`c1check.js`. 그래프를 다시 만들면 `python3 scripts/graphs/patch_astrid.py`. 배치별 작업 기록(1차~27차, 레시피마다 영상과 다르게 정한 점·시뮬 값)은 `docs/recipe-notes.md` "배치 기록".
- **게시 주소(Claude 아티팩트)**: https://claude.ai/artifact/Me2XFis1VHa9dchhbv66x1
- **도메인: https://poe2craft.xyz 운영 중**(2026-11-10 연결 완료: 가비아 구입 → 네임서버 Cloudflare(april·sevki) → Workers `poe2craft`(GitHub main 푸시마다 자동 배포) + 사용자 지정 도메인 poe2craft.xyz·www). 임시 주소 poe2craft.starwarz84.workers.dev.

## 폴더

```
scripts/        데이터·레시피 빌드 (python)
  build_recipes.py      레시피 정의 → site/data/recipes.json (recipes_batch2~4.py, recipes_v5_*.py(영상 하나당 파일 하나)를 exec)
  try_recipe.py         새 레시피 파일 하나만 시험 실행(사이트 데이터는 안 바뀜): python3 try_recipe.py recipes_v5_xxx.py
  build_tips.py         제작 꿀팁 → site/data/tips.json
  build_site_data.py 등 원천 데이터(raw/) → site/data/{index,crafting}.json, site/data/c/*.json(클래스별)
  apply_coe_weights.py  raw/coe_weights_patch.json → c/*.json 가중치 채우기 (**build_site_data.py를 다시 돌렸으면 반드시 뒤에, build_recipes.py 앞에 실행** — 탐욕스러운 사슬옷 클래스가 반지 풀을 복사해 감)
scripts/graphs/ 그래프 레시피(플로우차트) 정의 JSON — docs/graph-model.md
tools/sim/      run.js(그래프 시뮬레이션 → site/data/sim/<id>.json), engine.js(같은 레시피의 엔진 기대값 → tools/sim/engine/<id>.json)
site/sim.js     그래프 시뮬레이터(공용)
tools/coe/      compare.py(Craft of Exile poec_data.json ↔ 우리 데이터 대조), make_patch.py(모르는 가중치만 패치로). CoE 원본 파일은 저장소에 안 넣음
i18n/build.py   site/*.html → site/pub/*.html (영문 번역 런타임 주입, 문서 head 추가)
site/data/      index.json(클래스·베이스 목록), crafting.json(화폐·징조·에센스·기폭제), c/<클래스>.json(옵션 그룹·가중치·룬),
                recipes.json, tips.json, samples.json(등록 레시피 완성템 텍스트 = 발굴 탭 테스트용)
tools/test/     Playwright 검사 스크립트 + serve.sh(테스트 서버)
tools/q.py      클래스 파일 조회: cd site/data/c && python3 ../../../tools/q.py Amulets -b | <정규식>
raw/, out/      원천 수집 데이터(poe2db, RePoE)
private/        (저장소에 안 올림) Forge of Exiles 스크랩 — 게시 금지 테스트 데이터
```

**경로 주의**: 스크립트들이 `/home/claude/poe2data` 절대경로를 써요. 새 세션에서 저장소가 다른 곳(예: `/home/claude/poe2craft-site`)에 클론됐다면 먼저 링크를 만들어요.

```
[ -e /home/claude/poe2data ] || ln -s /home/claude/poe2craft-site /home/claude/poe2data
```

Playwright는 세션에 이미 설치돼 있어요(`require('playwright')`, 재설치 금지).

**게시된 사이트는 샌드박스 iframe**이라 `confirm()`·`alert()`·`prompt()`가 막혀요(누르면 바로 취소). 확인이 필요하면 레시피 탭의 `armed(btn, label)`처럼 "한 번 더 누르기"로 만들어요.

## 빌드 · 테스트 · 게시

**한 번에**(2026-11-11): `bash tools/release.sh` — 빌드 → 검사(리버스 검산·공유·등급 비교·리버스 6개 빠른 점검·건너뛴 과정·에센스 등급) → 크래프팅 점수 → 배포 폴더 → 배포 폴더 검수. 끝의 '문제 0'을 확인하고 커밋. `--full`은 제작 옵션 한도 점검과 리버스 전체 점수(약 15분)까지. 아래는 단계별로 따로 돌릴 때.

`site/*.html`은 한 줄에 문장이 여러 개라 **줄 끝 `//` 주석을 코드 중간에 넣지 않아요**(뒤 코드가 가려짐 — 2026-11-11 사고). `/* */`를 써요.

```
cd /home/claude/poe2data/scripts && python3 build_prices.py && python3 build_tips.py && python3 build_recipes.py && python3 build_special.py && python3 ../i18n/build.py
```

테스트 (테스트 서버 → 스크립트 → 서버 종료):

```
cd /home/claude/poe2data && bash tools/test/serve.sh start
cd tools/test && node audit.js && node ver.js && node eng.js && node share.js
node build_samples.js      # 레시피를 바꿨으면 samples.json 재생성
node build_board.js        # 레시피를 바꿨으면 board.json(목록 카드 요약) + data/bimg/ 재생성 — 빼먹어도 바뀐 레시피만 원래 계산으로 그림
node _shots_sim.js         # 플로우차트 화면 스크린샷 → shots/sim-<id>-*.png (kr·en·full·erase·mobile)
cd /home/claude/poe2data && bash tools/test/serve.sh stop
```

- **크래프팅 첫 로딩**(2026-11-11, 사용자: 처음 들어갈 때 로딩이 심함): 목록 카드는 `data/board.json`(빌드 때 만든 요약: 완성 옵션 줄 kr/en·소모량·난이도·베이스, 레시피 내용 해시 `recHash`가 같을 때만 씀) + `data/bimg/`(베이스 그림 파일)로 그리고, 클래스 파일(`data/c/*.json`, 모두 합쳐 약 17MB)은 레시피를 열 때(카드에 마우스를 올리면 미리) 받음 — recipes.html `A(r)`·`liteA`·`lite`. 사용자가 비용을 바꾼 레시피·초안·공유 레시피는 원래 계산. 테스트 서버(serve.sh)는 검사 스크립트를 위해 클래스 파일을 다 받고, `?lite`를 붙이면 실제 사이트와 같음. 점검 `node tools/test/_boardcheck.js`(요약 카드 = 원래 카드, 목록에서 클래스 파일 0개)·`_boardopen.js`(모든 카드 열기·주소로 열기)·`_loadtime.js`(배포 폴더 첫 로딩: 3.0초 17.9MB → 0.6초 4.1MB). 아티팩트판에 올릴 땐 `data/board.json`·`data/bimg/*`도 `files`에.
- **사이트 전체 로딩**(2026-11-11, 사용자: 홈페이지 전반 로딩 속도 개선): `build_web.py`가 배포 폴더를 만들 때 ① 데이터 파일 안의 그림(data URI — 클래스 파일·crafting.json 크기의 85~90%)을 `img/d/<해시>.webp`로 빼고 주소만 남김(`split_images`, 원본 site/·아티팩트판은 그대로) ② 한글 글꼴 SUIT를 사이트 파일에 실제로 나오는 글자만 남겨 줄임(`subset_font`, 610 → 약 214KB, 배포마다 다시 만듦 — 없는 글자는 맑은 고딕) ③ 도구 페이지의 구글 글꼴 링크를 뺌(화면을 막는 외부 파일, 본문·제목은 theme.css가 이미 덮어씀, 고정폭 숫자는 theme.css `--f-mono` 기기 글꼴) ④ 페이지가 시작하자마자 받는 데이터는 `<link rel=preload>`(`PRELOAD`). 껍데기의 불꽃 로고(134KB)는 극한 레시피를 열 때나 로딩 3초 뒤에 받음. 점검 `node tools/test/_loadall.js [탭…]`(탭별 파일·크기)·`_loadslow.js <포트> [포트2]`(느린 회선 비교)·`_imgcheck.js`(깨진 그림·404·경고, 배포 폴더 서버 8790).
- **영문 넘침 점검**(2026-11-11, 사용자: 번역으로 영역을 벗어나는 곳 수정): `node tools/test/_overflow.js [탭…]`(배포 폴더 서버 8790, 영문 1600·1280·1024·390px에서 글자 넘침·짧은 이름표 줄바꿈·가로 스크롤 → overflow.txt), 긴 스크린샷 `_ovshots.js [탭,…] [폭,…]` → shots/ovs-*, 플로우차트·리버스 분석 결과 `_ovextra.js` → shots/ovx-*. 줄인 Fontin 글꼴엔 ffi 합자 글자가 없어 'affix'가 'a  x'로 보였음 → theme.css·shell.html·about.html `html{font-variant-ligatures:none}`. CSS `content:` 글은 번역이 안 되니 `html[lang="en"]` 규칙을 따로 둠.
- **배포 전 검수**(2026-11-11): `cd web && python3 -m http.server 8790 &` → `node tools/test/_web.js`(배포 폴더 그대로 탭 6개·레시피·플로우차트·영문·모바일, 오류·404·가로 스크롤 → shots/web-*.png), 배포 뒤엔 내장 브라우저로 poe2craft.xyz의 `/data/recipes.json`을 받아 최신 커밋 내용인지 확인(사이트는 robots 차단이라 WebFetch는 안 됨)
- `_rev10e.js <레시피id…>`(2026-11-11 리버스 10개 시험): 등록 레시피 완성품으로 초안 → 레시피 엔진으로 초안·원본 비용(확정 / 추가 포함) 비교, `NEED=<json>`이면 그 그룹만 필수. `_rev10.js`(초안 단계·검산), `_rev10f.js`(티어 범위별 비용, 타협 있음|없음). 찾은 것: 타협이 들어가면 '확정' 비용이 너무 작아 보이고 티어 범위를 넓혀도 비용이 오르기도 함 → 리버스 화면의 티어 범위 비교는 타협 없이(필수 옵션을 모두 맞출 때, `market:1e9`) 계산, 액체 옵션은 '가중치 모름'에서 뺌, 콜르 등 증강물 옵션은 리버스·엔진에서 아직 가중치 모름(시뮬만 SL 추정값 사용)
- `skipcheck.js` 건너뛴 과정 점검(2026-11-11, 사용자: 중간 과정을 건너뛰고 완성한 레시피 찾기): 모든 레시피를 엔진으로 따라가 완성 때 미공개·징표 남음, 목표가 아닌 단계에서 옵션이 생김, 확률 0 단계, 시작 = 완성을 찾음(0이어야 함). 그래프 쪽은 sim 파일 `reqOk`(완성품이 완성 조건을 만족한 비율, 1이어야 함). 찾은 것: 로브 등급 레시피(두 번째 엑잘 전 잡옵 소멸 단계 `v2b` 빠짐), 엔드게임 육척봉 그래프(말소 카오스 새 옵션이 접미로 가면 접두 2개로 완성 → `s4`로 돌아감)
- `style_lint.py [--all]` 글쓰기 기준 점검(꿀팁·단계 글·화면 문구의 번역투·이중 피동·상투적 맺음·대구 등, 2026-11-11). 꿀팁·분기 줄은 설명하는 괄호를 쓰지 않고 문장으로 풀어요(옵션 수치 범위·'(선택)' 표시는 그대로)
- `audit.js` 레시피 정책 점검 · `omen.js` 불필요한 면 징조 · `unk.js` 가중치 모름 표시
- `ver.js` 발굴 초안 17개 검산(오류 0이어야 함) · `eng.js` 초안을 레시피 엔진으로 계산(경고·확률)
- `_cost.js` 레시피·초안 비용(div, 확정/추가 포함, 비싼 징조, 타협 수) · `_cheap.js` 시세로 바뀐 초안 오브 선택 · `_shots_price.js` 시세 화면 스크린샷 → shots/price-*.png
- `cmp2.js` 초안 vs 원본 단계 비교 → cmp2.txt · `one.js <레시피id>` 초안 하나 자세히 · `pair.js <레시피id>` 원본·초안 단계별 확률 나란히

게시(아티팩트판은 리버스 화면이 `sim.js`·`graphify.js`를 읽으니 `files`에 `"sim.js":"sim.js","graphify.js":"graphify.js"`도): Artifact 도구 publish, `file_path=/home/claude/poe2craft-site/site/app.html`, `root=/home/claude/poe2craft-site/site`(**링크 경로 poe2data는 게시가 거부돼요**), `url=`위 주소,
`files`에 바뀐 것만(그래프 시뮬레이션 데이터는 `"data/sim/<id>.json":"data/sim/<id>.json"` 추가, 특수 베이스 탭은 `"bases.html":"pub/bases.html","data/special.json":"data/special.json"`, 지금 `diztoh-crit-helmet-v2`, `helmet-armour-sl-v2`, `sihan-highend-boots-v2`, `diztoh-rarity-ring-v2`, `saveq-absent-amulet-v2`, `farmer-budget-armour-v2`, `farmer-starter-staff-v2`, `ragna-ashot-bow-v2`, `sane-resist-belt-v2`, `diztoh-budget-mace-v2`, `lilbotq-budget-boots-v2`, `icesly-budget-wand-v2`, `diztoh-es-helmet-v2`, `belton-plus8-wand-v2`, `lilbotq-armour-shield-v2`, `diztoh-vile-robe-v2`, `diztoh-talisman-v2`, `sihan-chayula-sceptre-v2`, `diztoh-budget-crossbow-v2`, `diztoh-onehand-mace-v2`, `saveq-alloy-focus-v2`, `tankjung-kitava-shield-v2`, `ragna-spell4-amulet-v2`, `noble-visceral-quiver-v2`, `sihan-highend-helmet-v2`, `barricade-quarterstaff-v2`, `diztoh-endgame-quarterstaff-v2`, `lilbotq-emerald-v2`, `zenm-timelost-sapphire-v2`, `diztoh-5mod-emerald-v2`, `diztoh-5mod-sapphire-v2`, `sl-5mod-jewel-v2`, `vodnarg-timelost-emerald-v2`, `lilbotq-boots-v2`, `mazbro-caster-ring-v2`, `diztoh-as-spear-v2`, `diztoh-socket-gloves-v2`, `seek-cyclone-boots-v2`, `mastert-timelost-emerald-v2`, `chiba-timelost-emerald-v2`, `noble-timelost-sapphire-v2`, `mazbro-proj-gloves-v2`, `sl-flamewave-staff-v2`, `mazbro-caster-amulet-v2`, `mazbro-spell5-amulet-v2`, `gold-amulet-6line-v2`, `absent-amulet-video-v2`, `sl-flamewave-ring-v2`, `breach-ring-video-v2`, `saveq-focus-v2`, `sl-proj7-gloves-v2`, `diztoh-iceshot-bow-v2`, `grasping-mail-spell1-v2`, `mazbro-bis-chest-v2`, `mirror-bow-video-v2`, `absent-amulet-spell6-v2`, `mazbro-sceptre-v2`, `xeno-phys-crossbow-v2`, `fubgun-quiver-v2`, `fubgun-phys-bow-v2`, `fubgun-crit-bow-v2`, `fubgun-proj-amulet-v2`, `fubgun-es-helmet-v2`, `bigdaddy-lightning-wand-v2`, `unstoppable-vile-robe-v2`, `unstoppable-slipstrike-vest-v2`): `{"recipes.html":"pub/recipes.html","discover.html":"pub/discover.html","emulator.html":"pub/emulator.html","builder.html":"pub/builder.html","data/recipes.json":"data/recipes.json","data/tips.json":"data/tips.json","data/samples.json":"data/samples.json","data/prices.json":"data/prices.json","data/budget.json":"data/budget.json","data/crafting.json":"data/crafting.json"}`.
capabilities는 생략(저장된 `{downloads, user, db(rules 2개)}` 유지 — 다시 적을 땐 셋 다 적어야 해요). 새 세션에서 처음 게시하기 전엔 Artifact `read`로 해당 파일을 먼저 읽어야 해요.

## 자체 도메인 poe2craft.xyz

- 운영 주소 https://poe2craft.xyz (Cloudflare Workers `poe2craft`, GitHub main 푸시마다 자동 배포, `wrangler.jsonc`가 `web/`를 서빙). 배포 폴더: 빌드 뒤 `python3 scripts/build_web.py` → `web/`(커밋해요).
- 원본: `site/shell.html`(껍데기) · `site/theme.css` · `site/about.html`. 아티팩트판 `site/app.html`도 같이 유지해요.
- 메뉴: 크래프팅(recipes) / 리버스 크래프팅(discover) / 에뮬레이터 / 속성부여(builder) / 데이터(bases) / 정보(about).
- 화면 문구는 명사형·짧게, '~요' 금지(전문가 이상 비용 안내만 '~습니다'). 영문은 `i18n/en.py` 끝 `EN.update`.
- 글꼴·로고·배너·필터·에뮬레이터·속성부여·리버스 화면·거래소 검색 등 확정된 화면 결정 전체는 `docs/site-ui.md`.

## 로드맵 (사용자 확정 2026-11-10 22:09 — 이 순서대로 진행)

- **테스트 기간**: 사이트는 구글 검색에 올리지 않음(`scripts/build_web.py` `INDEX = False` → robots.txt 전체 차단 + `X-Robots-Tag`·meta noindex, sitemap 없음). 공개할 때 True로 바꿈.
- **로그인 = POE 계정(pathofexile.com OAuth)**(사용자 확정): 공유 레시피·직접 작성 레시피 올리기에 씀. GGG 개발자 앱 신청이 필요해 시간이 걸림 — 아래 1-⑤ 때 같이 진행.

1. **크래프팅 기능 고도화**(지금 레시피 탭)
   ① 크래프팅 화면 레이아웃 정리 ② 플로우차트 고도화 — 어려움 이상 아이템의 95%를 플로우차트로 ③ 플로우차트에서 완성품 카드를 고르면 그 아이템의 크래프팅 순서(단계) 화면으로 이동(2026-11-11 완료: 완성품 카드 클릭·"레시피 보기 →" = 그 등급 레시피 탭, `fcFinalsHTML` `data-rtab`, 전체화면이면 닫고 이동) ④ 아이템 등급(하이엔드·밸런스·에센셜) ⑤ 유저가 직접 크래프팅 레시피를 작성하는 기능
2. **리버스 크래프팅 고도화**(지금 발굴 탭) — 화면에 "완성도 약 60%, 데이터가 쌓일수록 정교해지는 중"이라고 안내
   ① 입력: 유튜브 영상·커뮤니티 제작글 → 리버스 엔지니어링(1~5분) → 크래프트 리스트에 올릴지 결정 → 결과의 아쉬운 점 작성 요청
   ② 입력: 경매장에서 원하는 옵션으로 만든 결과물(아이템 정보) → 같은 흐름
   ③ 옵션 빌더를 리버스 크래프팅 메뉴로 옮김: 아이템 선택 → 원하는 옵션 빌드 → 그 아이템을 리버스 엔지니어링(같은 흐름)
3. **에뮬레이터 고도화** — 더 쉽고 편하게, 계속 손봄
4. **데이터** — POE2 DB·Craft of Exile 2 등 POE2 제작 데이터를 깔끔하게 정리

## 엔진 요약 (site/recipes.html `analyse`)

- 레시피: `cls, base(베이스 인덱스), ilvl, start{rar, mods[{gi,tmax,fr}|{junk:'p'|'s'}], quality, runes[{kr,en}]}, cap, sockets, exceptional{sockets}, nodes[]`
- 노드: `do`(base·transmute·augment·regal·exalt·chaos·essence·desecrate·reveal·remove·quality·manual·divine·fracture·socket·note),
  `cur, omens, target, fail{goto, via}, after.keepOnly, expect, extra, knownP, unknownW, ts, note{kr,en}`
- target: `gi | anyOf | all, tmax, replace, removeGi, junk, unrev, reveal{}, side, bone, lord, setQuality, quality, chance, slots, dropGi, imp, anoint, sanctify, vals, rune, runeSwap, removeJunk`
- **게임 규칙과 근거는 `docs/game-rules.md`**(데이터·설명·사용자·영상·교차·추정·미확인 표시). 규칙을 바꾸면 여기도 같이 고쳐요.
- **Craft of Exile 가중치**(2026-11-08): 2,703개 옵션 대조 → 2,307개 완전 일치. poedb 가중치가 1(모름)인 티어에 같은 레벨 CoE 값이 있으면만 채움(358티어·222그룹, 예: 목걸이 시전 속도 800). 채운 그룹은 `wsrc:'coe'`·`wcoe`(데이터에만 기록, 화면엔 출처 표시 안 함). 둘 다 값이 있는데 다른 12개는 poedb 유지.
- 확률은 가중치 데이터로 계산(AI가 정하지 않음). 훼손 공개: 일반 옵션은 원래 가중치, 훼손 전용 옵션은 공개 가중치가 없어 그룹당 1000 가정 → **"가중치 추정"** 표시(`o.pEst`, 사용자 확정 2026-11-08). 가중치 모름: `가중치 미확인`(x그룹·평탄 가중치 클래스), `가중치 미정`(가중치 1짜리 단독 그룹, 예: 목걸이·반지 시전 속도), 촉진 찬미 + 퀄리티 대상은 기폭제 퀄리티 %를 확률로 씀(추정, 시뮬과 같은 값 — 2026-11-11).
- 그룹 `s`: n 일반 · d 훼손 전용 · e 에센스 전용 · x 증강물 전용(룬·영혼 핵, sub=이름) 또는 별세계(sub=Otherworldly) · c 타락 · u 희생

## 제작 정책

제작 정책은 `docs/policies.md`가 기준이에요(주제별 17장: 베이스·시작 상태, 매직·레어 전환, 카오스·엑잘, 실패 정리와 비싼 징조, 제작 옵션, 훼손, 퀄리티·촉진, 주얼·액체, 룬, 등급·난이도·가격, 플로우차트, 화면 문구, 리버스, 점수 기준, 충돌 기록, 다른 계산기에서 가져온 방법). 레시피·리버스 작업 전에 읽어요.

- 사용자가 정책을 고치면 `docs/policies.md`의 그 장을 고치고 원래 번호·날짜 표기처럼 날짜를 남겨요. 앞 규칙과 부딪치면 16장 표에 한 줄 추가해요.
- 날짜순 원문(정책 1~33, 발굴 규칙 1~8)은 `docs/policies-archive.md`.
- 꼭 기억할 것: 플로우차트 먼저(11장) · 제작 옵션 한도와 아스트리드의 창의성(5장) · 훼손 옵션은 아이템당 하나(6장) · 비용 기준은 시뮬(0장) · 영상 방식을 더 싼 방식으로 바꾸는 판단은 사용자에게 묻기(0장) · 이름은 게임 데이터 그대로(12장).
- 점수: 크래프팅 `python3 scripts/score_recipes.py`, 리버스 `node tools/test/_revscore.js`(15장). 제작 옵션 한도 점검 `node tools/sim/c1check.js`.

## 외부 참고

- **POE2_HTC** (poe2htc.com, github Dboire9/POE2_HTC, AGPL-3.0): 목표 → 경로·기대 비용(MDP). 코드 복사 금지(AGPL), 방법론·검증용으로만.
  웹에서 "I have an item" → 아이템 붙여넣기 → 룬 체크 → Full plan to a target. 장갑 검증 결과: 카오스 → 소멸 → 완벽한 에센스(좌측 결정화) → 상위 엑잘 → 고대 뼈 + 메아리, 최소 1,894 카오스(계산 미완료 하한).
- pyoe2-craftpath (MIT, Rust/Python): 상태 트리 경로 탐색, Craft of Exile 가중치.
- **Maxroll 제작 가이드**(사용자 제공 2026-11-09, `private/maxroll-how-to-craft.txt`, 저장소 밖): 규칙만 우리 말로 `docs/game-rules.md` "Maxroll 가이드로 확인한 규칙"에 정리. 문장·표는 옮기지 않음. 일관된 제작 정책을 세울 때 참고.
- 유튜브 자막·화면 수집: 내장 브라우저(사용자 컴퓨터)로 영상 재생, 음소거·광고 건너뛰기 후 timedtext(json3) 수집. pot 토큰이 영상마다 달라서 실제 재생이 필요. **탭은 `tabs_create` → `navigate`로 열고 열자마자 음소거**(`preview_start`는 기존 탭을 재사용해서 음소거 전에 소리가 난 적 있음, 2026-11-09). 하위 작업 브리프 예: 영상 하나 → recipes_v5 파일 하나, 꿀팁 후보는 보고로만.

## 남은 일

끝난 일의 기록은 `docs/recipe-notes.md` "배치 기록".

- [ ] **우선순위(사용자 확정 2026-11-09 14:44)**: 발굴(역산)은 장기 과제. 당장은 **영상·웹페이지(예: poe2way 가이드)의 제작 데이터를 레시피로 저장해 유저가 찾아볼 수 있게** 하는 것까지. 분기형 그래프는 보기 + 시뮬레이션 위주(편집기·발굴 그래프 생성은 뒤로).
- [ ] **분기형 레시피(그래프) + 전체 공정 시뮬레이션 — 목표 2026-12 초**(사용자 확정 2026-11-09, 참고: Craft of Exile "Simulate entire crafting processes" — 단계 노드 + 결과별 화살표(성공/실패/결과 종류마다 다음 단계), 성공 1회당 커런시·베이스 소모, 단계별 도달 수). 순서: ① 데이터 모델(노드 = 행동, 간선 = 결과 조건 → 다음 노드, 기존 fail/branch/fallbackFor/retryFor를 간선으로 변환) ② 엔진: 상태 기반 몬테카를로 시뮬레이션(가중치 데이터로 실제 굴림, 수만 회) + 기존 기대값 계산과 대조 ③ 레시피 탭 그래프 보기(단계 표 + 노드 그림, 노드마다 도달 수·성공 1회당 소모) ④ 편집기(노드·간선 추가/수정, 에뮬레이터에서 따라하기 연결) ⑤ 기존 레시피 61개 변환·검증 ⑥ 발굴 초안을 그래프로 생성 + 시세(poe2scout) 연동 뒤 경로 비용 비교(MDP)
  - **1차 시험 완료(2026-11-09, 치명타 투구 `diztoh-crit-helmet-v2`)**: 모델 `docs/graph-model.md`, 그래프 `scripts/graphs/diztoh-crit-helmet-v2.json`, 시뮬레이터 `site/sim.js`, 결과 `site/data/sim/…json`, 레시피 탭 "플로우차트". 20,000회, 완성 1개당(준비·베이스 포함, div): 타협 평균 240(중앙 209, 90% 432, 베이스 1.5개) · 말소 반복 309(259/578) · B 최대치 1~2티어 + 타협 207(183/363) · 1~2티어 + 말소 272(233/496) · 접미 분열을 베이스부터로 291(베이스 3.0개) · B 빗나감에 좌측 소멸의 징조 388. 엔진 기대값: 타협 322, 선택 포함 890 — 엔진이 A(카오스 1,690 vs 시뮬 985)를 크게 셈(B 실패 소멸로 치명타를 잃을 때 A 전체를 tries × lose로 다시 곱함)과 말소 반복(엔진 +568 vs 시뮬 +69: 시뮬은 최대치 줄이 지워지면 B로 돌아가고, 새 줄이 접미로 가면 C 다시).
  - 1차에서 정한 해석(사용자 확인 필요): ① 희귀도 두고 3번째 접두가 필수(최대치/복합)면 C를 건너뛰고 D(접두 꽉 참) ② B에서 복합 줄이 떠도 빗나감 처리(사용자 흐름대로) ③ 말소의 징조 + 카오스는 지우는 면만 정하고 새 줄은 아무 면(접미로 가면 C 다시, 접미가 꽉 차면 D에 우측 강령술의 징조) ④ 접미 분열 = 같은 비용 가정 ⑤ 절사 + 좌측 말소 같이 쓰기(에뮬레이터는 아직 절사만 적용).
  - 2차: 기존 61개 자동 변환(규칙은 graph-model.md 표), 노드 자동 배치, 엔진 되돌아가기 곱셈 재검토, 브라우저에서 직접 돌리기(조건 바꿔 보기), 에뮬레이터 따라하기 연결.
- [ ] 2단계: 유튜브 링크 → 레시피 = 텔레그램 봇(설계 확정 2026-11-11, 위 "메뉴 > 영상·글 주소 → 레시피" 참고)
- [ ] **부위별 최소 5개 레시피**(사용자 확정 2026-11-09): 방어구(갑옷·장갑·투구·장화·방패·버클러·집중구), 장신구(목걸이·반지·벨트·화살통), 무기(활·지팡이·완드·석궁·창·육척봉·양손 둔기·셉터·한손 둔기·탈리스만, 0.5에 없는 종류 제외), 주얼은 사파이어·에메랄드·루비 + **오래된 사파이어·에메랄드·루비(Time-Lost)를 따로**, 다이아몬드는 제외. 채운 뒤 발굴로 간극 해소
- [ ] 4차 확인할 점: 화살통·버클러는 0.5 이후 영상 없음, 루비·오래된 루비 영상 아직 없음. 벨트 영상 2개는 유니크 타락(Asterix)·제네시스 트리 도박(Clickachu)이라 레시피 못 만듦(바알 함양 오브(Vaal Cultivation Orb, 옛 표기 "바알 수양 오브")·건축가의 오브 이름은 2026-11-09 POE2DB로 해결(crafting.json `extra`), 따뜻한 선물 데이터 없음). Vodnarg·Diztoh 육척봉 훼손에 불필요한 면 강령술 징조(영상대로, 정책 13 충돌). 탱정 방패는 슬라이드만(아이템 레벨 81 이유 미확인, 맹렬한 유동체 이름은 2026-11-09 해결). Xeno 석궁은 자막 없이 화면만 본 요약판(사용자 확정 2026-11-09: 영상과 달리 공격 속도 절사까지 접미를 다 끝낸 뒤 막기 줄을 지우고 물리 피해 추가를 마지막에 공개 — 물리 피해 추가(레벨 75)가 절사에 노출되지 않음). 액체 줄이 엔진에서 제작 옵션(C)로 표시되는지 확인 필요
- [ ] 3차 확인할 점: 오래된 루비·에메랄드, 루비, 화살통·버클러 영상 아직 없음. 건축가의 오브 이름 해결(2026-11-09). 노블이 두개골·우울 1/2 흐름 단순화(비용 과소). Diztoh 투구 접두 엑잘 실패 처리 추정
- [ ] 2차 확인할 점: SaVeQ 두 번째 포커스(주문 스킬 분열판) 미수록, Barricade 마무리 룬 3종·Belton "+2 룬" 이름 미확인, 유동체 이름 해결(2026-11-09: 공허·맹렬한·오싹한·치직대는·완벽한 유동체), Belton 심연의 에센스로 제작 칸 비우기 요령(징표 = 제작 옵션 규칙과 충돌 가능), 시한 "징표가 훼손 티어를 올린다"(엔진 미반영)
- [ ] 새 레시피 확인할 점: 알두르의 배신은 카드에 룬 옵션 줄로만 표시(2026-11-09), 유동체·여우 우상 이름 해결(2026-11-09: "한기 유동체" → 오싹한 유동체, 여우 우상은 룬 데이터에 있었음, "보석세공사의 오브" → 쥬얼러 오브, 완벽한 유동체·완벽한 쥬얼러 오브 비용을 부재 목걸이 2개·MazBro +5 목걸이에 `extra`로 반영), MazBro 셉터는 영상 순서를 정리한 요약판, SL 반지 슬라이드 8번(좌측 말소) 대신 우측 말소 사용, MazBro 셉터 영상에서 합금이 공개된 훼손 줄을 지운 사례(규칙과 충돌 가능)
- [ ] **역산 전체 점검(2026-11-09, 레시피 61개 → 초안 60개)**: 검산 오류 0. 문제: ① 초안 45개가 원본보다 비싼 커런시를 크게 더 씀 — 엑잘을 한 줄씩(≤T1 1% 미만) 노리고 실패마다 면 소멸의 징조(예: Diztoh 엔드게임 육척봉·석궁 수백 개), 원본은 anyOf·상위 찬미·절사 카오스·말소 카오스 사용 ② 첫 카오스 카오스 수천 개는 정상(정책 16) ③ 확정 줄(에센스·합금)을 그 면 좋은 줄 다음에 둬서 1/2로 지워질 위험(23개 경고, 예: Diztoh 가성비 둔기 — 원본은 먼저) → 정책 17로 해결 ④ ragna-spell4-amulet 초안 완성 상태에 잡옵 2줄 ⑤ grasping-mail-spell1 샘플 없음 ⑥ 주얼·증강물 가중치 미확인(데이터). 비교 스크립트 `tools/test/_cmp3.js` → cmp3.txt
  - 개선(2026-11-09 4차, 정책 19·20): 절사·말소 반복 상위 카오스 오브, 구간 요약, 베이스 준비 접힌 구간, 선택 단계 합계 분리, 에센스 줄 절사 복구, 왼쪽 목록 `do:'note'` 단계 이름(label). 검산 오류 0·경고 26(그대로). 비싼 커런시(카오스 오브 제외) 59,991 → 64,174(완벽한 카오스 오브 3,698 → 0, 상위 카오스 오브 139 → 5,669, 절사의 징조 2,668 → 3,959, 말소의 징조 2,423 → 3,483 — 상위는 레벨 35~49 줄도 후보라 시도 수가 늘어남. 늘어난 초안 16개, 가장 큰 것 Diztoh 엔드게임 육척봉 +812). 모래맹세 샌들 추가 과정: 절사가 카오스 저항(레벨 56)을 바꿀 확률 71%라 목표 도달 2.8%, 선택 포함 시 베이스 ×36(새 베이스 뒤 다시 하는 구간 비용은 아직 안 셈)
  - 개선(2026-11-09 3차, 정책 18): 매직 구입 시작 + 에센스 대체 + 훼손 + 상위 찬미. 검산 오류 0·경고 26·결정화 경고 2(그대로), 비싼 커런시(카오스 오브 제외, cmp3.txt 초안 tot 합) 81,532 → 59,991(늘어난 초안 0개, 가장 줄어든 것 Diztoh 한손 둔기 −15,555). 남은 것: 추가 과정 비용이 "총 소모품"에 같이 들어감, 절사로 에센스 줄이 지워지면 "그 단계부터"가 실제로는 완벽한 에센스(결정화)로 복구하는 게 맞음
  - 개선(2026-11-09 2차): 정책 17(난이도 추정 + 제작 옵션 먼저), 절사 카오스·면 말소 카오스 실패 처리, anyOf 중복 제거, ragna 잡옵 2줄 버그 수정, 노멀 베이스 시작, 확률 단계 실패 처리 검사, 부패의 징조 차단, 룬·타락 단계. 검산 오류 0, 경고 49 → 26(결정화 경고 23 → 2). 비싼 커런시(카오스 오브 제외) 합계 46,359 → 22,508. "원본보다 2배+5 넘게 늘어난 초안" 수는 43 → 44로 그대로 — **주원인은 샘플**: `build_samples.js`가 완성품을 그 줄의 최고 티어로 만들어서 초안 목표(붙여 넣은 티어 이상)가 원본(2~3티어·anyOf)보다 훨씬 어려움. 원본처럼 쓰려면 샘플을 `tmax` 티어로 만들지 결정 필요. 남은 것: 전문가 아이템의 제작 옵션 1/2 도박, 매직 단계 확률이 낮은 1티어 진화(완벽한 진화의 오브 수백~수천 개)
