# POE2 크래프팅 사이트 — 작업 인계 문서

이 문서는 새 세션에서 작업을 그대로 이어가기 위한 안내서예요. 새 세션은 **이 파일을 먼저 끝까지 읽고** 시작해요.

## 사용자와 일하는 방식

- 사용자(Atom1q84)는 개발자가 아니에요. **항상 한국어로** 답해요.
- 복사해서 쓸 내용은 코드 블록에 넣고, 블록 안 줄 앞에 공백을 두지 않아요.
- 유튜브 영상을 분석할 때는 소리를 꺼요.
- 사용자가 고친 정책은 아래 "레시피 정책"에 바로 반영해서 다음 세션도 따르게 해요.

## 무엇을 만드는가

Path of Exile 2 아이템 제작 사이트. 탭 4개짜리 한 화면이에요.

| 탭 | 원본 파일 | 게시 파일 | 하는 일 |
|---|---|---|---|
| 에뮬레이터 | `site/emulator.html` | `pub/emulator.html` | 화폐를 직접 써 보는 제작 시뮬레이터 |
| 옵션 빌더 | `site/index.html` | `pub/builder.html` | 원하는 옵션 조합 만들기 |
| 레시피 | `site/recipes.html` | `pub/recipes.html` | 유튜브 영상 기반 제작 레시피, 단계별 확률(가중치 계산) |
| 발굴 | `site/reverse.html` | `pub/discover.html` | 아이템 텍스트 → 옵션 분석 → 레시피 초안 → 검산 → 레시피 탭에 올리기 |

- 껍데기: `site/app.html` (탭 = iframe, `SRC` 맵, 언어 전환, 다운로드 중계, 발굴 → 레시피 초안 전달 `poe2-draft` 메시지)
- **게시 주소(Claude 아티팩트)**: https://claude.ai/artifact/Me2XFis1VHa9dchhbv66x1
- 도메인: 사용자가 `poe2` + `.com`으로 정함(후보 poe2craft.com 등). 구매·호스팅은 아직.

## 폴더

```
scripts/        데이터·레시피 빌드 (python)
  build_recipes.py      레시피 정의 → site/data/recipes.json (recipes_batch2.py, recipes_batch3.py 를 exec)
  build_tips.py         제작 꿀팁 → site/data/tips.json
  build_site_data.py 등 원천 데이터(raw/) → site/data/{index,crafting}.json, site/data/c/*.json(클래스별)
i18n/build.py   site/*.html → site/pub/*.html (영문 번역 런타임 주입, 문서 head 추가)
site/data/      index.json(클래스·베이스 목록), crafting.json(화폐·징조·에센스·기폭제), c/<클래스>.json(옵션 그룹·가중치·룬),
                recipes.json, tips.json, samples.json(등록 레시피 완성템 텍스트 = 발굴 탭 테스트용)
tools/test/     Playwright 검사 스크립트 + serve.sh(테스트 서버)
tools/q.py      클래스 파일 조회: cd site/data/c && python3 ../../../tools/q.py Amulets -b | <정규식>
raw/, out/      원천 수집 데이터(poe2db, RePoE)
private/        (저장소에 안 올림) Forge of Exiles 스크랩 — 게시 금지 테스트 데이터
```

**경로 주의**: 스크립트들이 `/home/claude/poe2data` 절대경로를 써요. 저장소는 반드시 그 위치에 클론해요.

## 빌드 · 테스트 · 게시

```
cd /home/claude/poe2data/scripts && python3 build_recipes.py && python3 build_tips.py && python3 ../i18n/build.py
```

테스트 (테스트 서버 → 스크립트 → 서버 종료):

```
cd /home/claude/poe2data && bash tools/test/serve.sh start
cd tools/test && node audit.js && node ver.js && node eng.js
node build_samples.js      # 레시피를 바꿨으면 samples.json 재생성
cd /home/claude/poe2data && bash tools/test/serve.sh stop
```

- `audit.js` 레시피 정책 점검 · `omen.js` 불필요한 면 징조 · `unk.js` 가중치 모름 표시
- `ver.js` 발굴 초안 17개 검산(오류 0이어야 함) · `eng.js` 초안을 레시피 엔진으로 계산(경고·확률)
- `cmp2.js` 초안 vs 원본 단계 비교 → cmp2.txt · `one.js <레시피id>` 초안 하나 자세히

게시: Artifact 도구 publish, `file_path=/home/claude/poe2data/site/app.html`, `root=/home/claude/poe2data/site`, `url=`위 주소,
`files`에 바뀐 것만: `{"recipes.html":"pub/recipes.html","discover.html":"pub/discover.html","emulator.html":"pub/emulator.html","builder.html":"pub/builder.html","data/recipes.json":"data/recipes.json","data/tips.json":"data/tips.json","data/samples.json":"data/samples.json"}`.
capabilities는 생략(기존 `{downloads:true}` 유지). 새 세션에서 처음 게시하기 전엔 Artifact `read`로 해당 파일을 먼저 읽어야 해요.

## 엔진 요약 (site/recipes.html `analyse`)

- 레시피: `cls, base(베이스 인덱스), ilvl, start{rar, mods[{gi,tmax,fr}|{junk:'p'|'s'}], quality}, cap, sockets, exceptional{sockets}, nodes[]`
- 노드: `do`(base·transmute·augment·regal·exalt·chaos·essence·desecrate·reveal·remove·quality·manual·divine·fracture·socket·note),
  `cur, omens, target, fail{goto, via}, after.keepOnly, expect, extra, knownP, unknownW, ts, note{kr,en}`
- target: `gi | anyOf | all, tmax, replace, removeGi, junk, unrev, reveal{}, side, bone, lord, setQuality, quality, chance, slots, dropGi, imp, anoint, sanctify, vals, rune, runeSwap, removeJunk`
- 확률은 가중치 데이터로 계산(AI가 정하지 않음). 가중치 모름: `가중치 미확인`(x그룹·평탄 가중치 클래스), `가중치 미정`(가중치 1짜리 단독 그룹, 예: 목걸이·반지 시전 속도), 촉진 찬미 + 퀄리티 대상은 `촉진 효과로 확률 상승 (수치 비공개)`.
- 그룹 `s`: n 일반 · d 훼손 전용 · e 에센스 전용 · x 증강물 전용(룬·영혼 핵, sub=이름) 또는 별세계(sub=Otherworldly) · c 타락 · u 희생

## 레시피 정책 (사용자 확정)

1. 제목 "베이스 | 특징". 상단 소개글(r.note) 없음. 기본 상식은 단계에 쓰지 않음. 아이템과 무관한 팁은 제작 꿀팁으로.
2. 시작 상태 = 실제로 사는 베이스. 잡옵이 필요하면 단계(엑잘 등)로 만듦. **분열템은 분열템을 시작점으로**.
3. 분열 뒤엔 보통 분열 + 한 줄 남기고 카오스. 도박이 맞으면 "대박 → 제작 종료".
4. 매직 단계는 완벽한 진화·확장·제왕(최소 레벨 70/70/50) 기준 확률.
5. 면 표시: 징조 없으면 "접두·접미 무관", 한쪽만 남으면 "(남은 자리)", 반대쪽이 꽉 차면 면 징조 제거.
6. 목표 티어는 현실적으로(비싼 작업은 1~2티어). 단일 원소 저항은 액체로 바꿀 수 있어 원소 무관.
7. 완성 카드: 퀄리티 반영(Q표시), 베이스 능력치(방어·무기 피해·DPS, 범위), 룬·영혼 핵, 고유 옵션, 성유·축성, 특출난 베이스 표시.
8. 한글 이름은 게임 데이터(crafting.json kr) 그대로. 예: 발작의 에센스, 정확도(명중 아님), 쇳소리 기폭제 = 시전, **콜르의 사냥**.
9. **퀄리티 상한**: 장신구 기폭제 = 기본 20% + 베이스 고정 옵션(균열 반지 20%, 제련된 균열 반지 25%) + 균열의 에센스(최대 퀄리티 +20%).
   그 위는 바알 촉진시키는 주입기로 최대 +10%(타락 위험). 이론상 최대 75%. 장신구 외 20% 초과는 바알 방어구 장인/대장장이의 주입기.
10. 룬 소켓: 필요한 룬(증강물 전용 옵션의 룬, 제작 옵션 2줄용 아스트리드의 창의성, 접미 4줄용 세를의 승리) 수가 기본 소켓보다 많으면 **특출난 베이스**.
11. 제작 옵션(완벽한 에센스·합금)은 1줄까지, 2줄째는 아스트리드의 창의성 필요. 일반/상위 에센스는 제작 옵션이 아님.

## 발굴(역산) 규칙 — site/reverse.html `makeDraft` / `verifyDraft`

순서: 분석 → 초안 → **검산**(초안을 처음부터 다시 따라가며 규칙·완성 상태 확인) → 사용자가 "레시피 탭에 올리기".

초안 순서:
1. 분열 줄이 있으면 "분열 + 잡옵 3줄" 베이스(분열은 4줄 이상에만 가능). 20% 초과 퀄리티(장신구 외)는 바알 주입기. 증강물 룬은 굴리기 전에 장착.
2. 분열 베이스: 나머지가 잡옵이라 카오스로 원하는 줄 중 하나(anyOf, 가중치 아는 줄 우선).
3. 에센스가 쓸 잡옵만 남기고 나머지 잡옵은 면 소멸로 제거.
4. 장신구 퀄리티: 균열의 에센스(좌측 결정화) → 기폭제 상한까지 → 필요하면 주입기. 마지막에 절사 + 상위 카오스로 최대 퀄리티 줄 제거.
5. 남은 무작위 줄: 면 징조 엑잘로 그 면의 원하는 줄 중 아무거나(anyOf). 실패 시 면 소멸.
6. 확정 줄(완벽한 에센스·합금)은 마지막: 버릴 줄 + 결정화 + 에센스. 두 번째 전엔 아스트리드의 창의성.
7. 훼손: 일반·증강물 풀의 레벨 40+ 목표는 고대 뼈, 심연의 메아리, 실패 시 빛의 징조 + 소멸. 군주 징조는 무기·장신구만. 훼손으로만 나오는 증강물 줄은 에센스 뒤에 아스트리드와 교체해 장착.

검산 항목: 오브 사용 조건, 자리, 면 징조 낭비, 결정화·소멸·카오스가 좋은 줄을 지울 위험, 제작 옵션 수, 룬 수 ≤ 소켓, 뼈·군주 징조 적합성, 퀄리티 상한, 분열 4줄, 완성 상태 = 붙여 넣은 아이템, 가중치 모름.

## 외부 참고

- **POE2_HTC** (poe2htc.com, github Dboire9/POE2_HTC, AGPL-3.0): 목표 → 경로·기대 비용(MDP). 코드 복사 금지(AGPL), 방법론·검증용으로만.
  웹에서 "I have an item" → 아이템 붙여넣기 → 룬 체크 → Full plan to a target. 장갑 검증 결과: 카오스 → 소멸 → 완벽한 에센스(좌측 결정화) → 상위 엑잘 → 고대 뼈 + 메아리, 최소 1,894 카오스(계산 미완료 하한).
- pyoe2-craftpath (MIT, Rust/Python): 상태 트리 경로 탐색, Craft of Exile 가중치.
- 유튜브 자막·화면 수집: 내장 브라우저(사용자 컴퓨터)로 영상 재생, 음소거·광고 건너뛰기 후 timedtext(json3) 수집. pot 토큰이 영상마다 달라서 실제 재생이 필요.

## 남은 일

- [ ] 3단계: 생성 레시피를 공유 저장소(아티팩트 db)에 등록 + 레시피 탭 "새 레시피" 알림
- [ ] 2단계: 유튜브 링크 → 레시피 (나중에 텔레그램 봇 형태로)
- [ ] 초안: 엑잘마다 기폭제 바꾸기 + 촉진하는 찬미(카스터 목걸이 원본 방식)
- [ ] 초안: 실패 시 갈림길(소멸 vs 결정화)을 POE2_HTC식 "다음 최선 수"로 개선, 소멸 재시도 위험 비용 반영
- [ ] 브리치 반지 원본의 결정화 방향(접미 합금에 좌측 결정화) 의도 확인
- [ ] 원본 레시피 이름 "콜러의 사냥" → "콜르의 사냥" 정리
- [ ] 구매 시 잡옵이 붙은 레시피 7개 정리 여부(사용자 결정 대기)
- [ ] craftofexile에서 모르는 가중치 채우기, 완성 카드 기능을 에뮬레이터·빌더에도 적용
- [ ] 도메인 구매 후 호스팅
