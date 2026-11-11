# 영상·제작글 분석 요청 처리 (2026-11-11)

> 지금은 닫아 둠(사용자 확정 2026-11-11 20:50). 화면 '준비 중'(`site/reverse.html` `REQ_OPEN=false`), 예약 작업 꺼짐. Worker API는 그대로 살아 있어 다시 열 때 스위치만 바꾸면 돼요.

리버스 크래프팅 ① 탭에서 받은 주소를 레시피로 바꾸는 흐름이에요. 예약 작업(하루 3번)이 이 문서대로 처리해요.

## 구조

- 받기: `site/reverse.html` ① 탭 → `POST /api/req` {url, memo, code}. 서버 = `worker/index.js`(Cloudflare Worker, 정적 파일 `web/`도 같이 서빙), 저장 = KV `REQ`(첫 배포 때 자동 생성).
- 접근 코드: 로그인 전 테스트 기간 전용. 코드 자체는 저장소에 없고 해시만 `worker/index.js` `CODE_HASHES`에 있음. 코드마다 하루 3회(한국 날짜). 코드 추가 = 해시 한 줄 추가.
- 같은 영상(유튜브 영상 id)·같은 글 주소: 이미 레시피가 있으면 `exists`(그 레시피로 안내), 대기 중이면 같은 요청을 돌려줌.
- 상태: `GET /api/req?ids=a,b` — 대기 중 / 완료(레시피 링크) / 실패(이유). 요청한 기기의 localStorage `poe2r:reqs`에 id가 남음.
- 대기열: `GET /api/queue` — 처리 결과가 없는 요청(오래된 순). 결과는 저장소 `site/data/reqdone.json`이 배포되면 반영(Worker가 정적 파일을 읽음). 그래서 처리 쪽엔 서버 비밀 값이 필요 없어요.
- POE 계정 로그인: GGG 개발자 문서에 신규 앱 신청을 지금 받지 않는다고 적혀 있음(2026-11-11 확인). 열리면 접근 코드 대신 로그인으로 바꿈.

## 예약 작업이 하는 일 (한 번에 최대 3건)

1. 저장소 최신으로(`git pull --rebase`), `CLAUDE.md`를 끝까지 읽음. 경로 링크: `[ -e /home/claude/poe2data ] || ln -s <저장소> /home/claude/poe2data`.
2. 대기열 받기: 사이트는 robots 차단이라 WebFetch가 안 됨 → 내장 브라우저로 `https://poe2craft.xyz/api/queue`를 열어 본문 JSON을 읽음. 비어 있으면 끝.
3. 요청마다:
   - 유튜브: 내장 브라우저로 영상을 열고 **바로 음소거**, 광고 건너뛰기, 자막(timedtext json3) 수집 + 필요한 장면 화면 확인(CLAUDE.md '외부 참고'). 제작글: WebFetch로 본문.
   - 제작 영상·글이 아니거나(빌드 소개만, 유니크 타락, 부패의 징조, 재조합기 등) 단계가 빠져 레시피가 안 되면 → `python3 tools/req/mark.py <id> fail "<짧은 이유>"`(예: '제작 과정 없음', '부패의 징조 제작이라 제외', '자막·화면으로 단계 확인 불가').
   - 레시피가 되면 정책 31 순서: 기록 `tools/notes/<id>.md` → 그래프 `scripts/graphs/gen_batch<n>.py` → `node tools/sim/run.js` → 등급 레시피 `recipes_v5_<원본>.py` + `recipes_v5_zz-batchz<n>-v2.py`(작성자 = 영상·글 작성자, `source.url` = 요청 주소) → `notes_short.py`·`base_prices.py` → 빌드·테스트(CLAUDE.md '빌드 · 테스트') → `docs/recipe-notes.md` 점수·기록 → `python3 tools/req/mark.py <id> done <그룹 id>`.
4. 빌드(`python3 i18n/build.py` → `python3 scripts/build_web.py`), `node tools/test/_web.js` 오류 0 확인, 커밋·푸시(병합 뒤 배포 폴더 다시 빌드). 푸시하면 배포 → 요청한 사람 화면에 완료/실패가 보임.
5. 내장 브라우저를 쓸 수 없으면(컴퓨터 꺼짐) 유튜브 요청은 건드리지 않고 다음 차례로 미룸. 제작글은 그대로 처리.

## 점검

- 로컬: `npx wrangler dev --local --port 8795`(저장소 루트, 빌드 뒤) → `curl -XPOST localhost:8795/api/req -d '{"url":"…","code":"…"}'`, 화면은 `/discover.html` ① 탭.
- 아티팩트판(app.html)은 서버가 없어 '서버 연결 불가 · poe2craft.xyz에서 사용'이 나옴.
