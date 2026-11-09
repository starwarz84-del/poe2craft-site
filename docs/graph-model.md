# 분기형 레시피(그래프) 모델 — 1차 시험 (2026-11-09)

지금 레시피(`nodes[]`)는 단계를 한 줄로 놓고 단계마다 기대값을 곱해요. 갈래가 여럿인 흐름(타협, 결과에 따라 다른 단계로 가기, 지워진 줄에 따라 되돌아가는 곳이 다름)은 정확히 못 세요.
그래프 레시피는 **노드 = 행동, 간선 = 결과 조건 → 다음 노드**로 적고, 확률은 적지 않아요. 시뮬레이터가 아이템 상태를 실제로 굴려서(가중치 데이터) 어느 간선으로 갈지 정해요.

- 시범: `scripts/graphs/diztoh-crit-helmet-v2.json` (사용자 확정 흐름, 웃는 가면 치명타 투구)
- 시뮬레이터: `site/sim.js` (node·브라우저 공용) · 실행: `node tools/sim/run.js <id> [횟수=20000]` → `site/data/sim/<id>.json`
- 화면: 레시피 탭 상세의 "플로우차트" 버튼(레시피에 `sim:1`이 있을 때만, `build_recipes.py`가 sim 파일이 있으면 붙임)

## 파일 구조

```
{
 id, recipe(레시피 id), cls, base(영문 베이스 이름), ilvl,
 basePrice: {커런시 id: 개수}            // 베이스 1개 값(예: 카오스 오브 8개)
 params:  {이름: {kr, en, values:{값:{kr,en}}}}   // 전략 옵션(아래)
 strategies: [{id, params:{...}, hidden?}]       // 미리 계산할 조합. hidden = 화면 토글엔 안 나오고 비교용
 tags:    {이름: {fam, side?, sec?, tmax?} | {anyOf:[태그…]}}   // 옵션 이름표. fam = 클래스 파일 그룹 f(여럿이면 '+'로)
 conds:   {이름: 조건}                              // 자주 쓰는 조건 묶음, {ref:'이름'}으로 씀
 require: 조건                                     // 완성 상태 검사(시뮬레이션 결과 reqOk = 이 조건을 만족한 비율, 1이어야 함)
 groups:  [{id, kr, en, cols:[처음, 끝]}]           // 그림의 묶음(베이스 준비 / 본 제작)
 start:   노드 id
 nodes:   [노드…]
}
```

`tmax`는 `"$bTier"`처럼 전략 옵션을 가리킬 수 있어요(예: B 목표 1티어 / 1~2티어).

## 노드 종류

| kind | 뜻 | 필드 |
|---|---|---|
| `base` | 새 베이스 구입(노멀, 옵션 없음). 베이스 수를 셈 | `next` |
| `act` | 커런시 한 번 사용 | `act`(transmute·augment·regal·exalt·chaos·annul·desecrate·reveal·divine·fracture), `cur`, `omens[]`, `curIf:[{if, cur}]`(상태에 따라 오브 바꾸기, 예: 치명타 1티어면 완벽한 엑잘티드 오브), `trim:{side, keep}`(정책 23④ 절사/말소 자동 선택), `want`(공개 때 고를 태그), `skipIf`+`skipTo`, `edges` |
| `cleanup` | 징조 없는 소멸의 오브를 반복해 `keep` 태그 밖의 줄을 `maxJunk`개 이하로 줄임. `keep` 줄이 지워지면 그 자리에서 멈춤 | `keep[]`, `maxJunk`, `edges:[{lost:태그, to}, {to}]` |
| `choice` | **정책 노드**: 전략 옵션 값으로 갈래를 고름(타협 / 추가 과정, 정리 방법 등) | `param`, `options:{값: 노드 id}`, `edgeLabels` |
| `assume` | 계산상 가정(1차 시험: 접미 분열 = 같은 비용 가정 → 분열 줄을 바꿔 본 흐름으로) | `swapFracture`, `next` |
| `done` | 완성 | — |

재시작은 따로 종류를 두지 않고 `base` 노드로 가는 간선이에요(예: 잡옵 분열 → 베이스부터).

## 간선 조건 (행동 직후 상태로 판단, 위에서부터 처음 맞는 것)

- `{has:태그}` 아이템에 있음 · `{added:태그}` 이번에 붙음 · `{removed:태그}` 이번에 지워짐 · `{fractured:태그}` 이번에 분열됨
- `{full:'p'|'s'}` 그 면이 꽉 참 · `{sideAll:{side, tag}}` 그 면의 분열 아닌 줄이 모두 태그에 맞음
- `{all:[…]}`, `{any:[…]}`, `{not:…}`, `{ref:'conds 이름'}`, `{param:{이름:값}}`
- 조건 없는 간선 = 나머지 전부

확률은 그래프에 적지 않아요. 같은 상태 규칙(아래)으로 굴린 결과가 간선을 고르고, 간선별 통과 횟수가 결과 파일 `edges`에 남아요.

## 시뮬레이터 규칙 (`site/sim.js`)

에뮬레이터(`site/emulator.html`)와 같은 규칙, 확률 모델은 레시피 엔진(`recipes.html analyse`)과 같은 가정이에요.

- 추가: 자리 남은 면의 일반 그룹(같은 계열 제외), 가중치 비례. 상위·완벽 오브는 최소 레벨(crafting.json `min`), 단 그 계열의 최고 티어는 항상 후보
- 매직 = 면당 1줄, 희귀 = 3줄(베이스 `pd`/`sd` 반영). 면 징조(찬미·대관식·말소·소멸·강령술)는 그 면만
- 소멸의 오브: 분열 아닌 줄(미공개 훼손 포함) 중 무작위 1개. 빛의 징조 = 훼손 줄만
- 카오스 오브: 지우고 아무 면에 추가(말소의 징조는 **지우는 면만** 정함 — 새 줄은 자리 남은 어느 면이든). 절사의 징조 = 요구 레벨이 가장 낮은 줄(동률 무작위), 말소와 같이 쓰면 그 면에서 가장 낮은 줄
- 뼈: 빈 면으로, 꽉 찬 면이면 그 면 줄 하나를 지우고 들어감. 공개 = 그룹 3개(훼손 전용 1000, 일반 = 티어 가중치 합, 뼈 최소 레벨) 중 고름, 심연의 메아리 = 못 찾으면 한 번 다시 뽑기
- 분열: 공개된 분열 아닌 줄 중 무작위
- 비용: `site/data/prices.json`(엑잘티드 오브 단위 → 디바인), 베이스는 `basePrice`

## 결과 파일 (`site/data/sim/<id>.json`)

`{id, recipe, runs, generated, graph:{그리기용 노드·간선·묶음·옵션}, strategies:[{id, params, hidden, res}], engine}`

`res` = 완성 1개 기준: `mean`·`median`·`p10`·`p90`(div), `bases`, `use`(커런시별 평균), `nodes:{id:{reach(완성품 중 거친 비율), visits(평균 방문), use, div}}`, `edges:{"a>b": 평균 통과}`, `reqOk`(완성 조건 만족 비율).
`engine` = 같은 레시피를 지금 엔진으로 계산한 값(`node tools/sim/engine.js <id> > tools/sim/engine/<id>.json`, 테스트 서버 필요): `total`(확정까지 + 준비 + 베이스), `totalAll`(선택 단계 포함).

## 기존 레시피 형식 → 간선 자동 변환 규칙 (2차에서 구현)

| 기존 | 그래프 |
|---|---|
| 노드 순서 | 성공 간선 = 다음 노드(`fallbackFor`·`onLost`·`branch:miss`·`retryFor`·`optional` 노드는 건너뛰고 다음 주 경로 노드) |
| `target` | 성공 조건: `gi/anyOf` → `{added:태그}`(chaos·exalt·reveal) 또는 `{has:태그}`(이미 있으면 건너뜀 = `skipIf`). `junk` 목표 = 조건 없음 |
| `fail.goto:'self'` | 실패 간선 → 자기 자신 |
| `fail.goto:'<id>'` | 실패 간선 → 그 노드 |
| `fail.goto:'restart'` | 실패 간선 → `base` 노드 |
| `fail.via` | 실패 간선 사이에 `act` 노드 하나(via의 cur·omens) → 그다음 goto |
| `fail.lost:'<id>'` | via 노드 뒤 간선 두 개: `{removed:그 단계 태그}` → `<id>`, 나머지 → goto. 소멸이면 `cleanup`(keep = 지금까지 만든 줄)로 |
| `fallbackFor:'<id>'` | `<id>`의 실패 간선 → 이 노드(이 노드 성공 → `<id>`의 성공 다음) |
| `optional` + `compromise` | `<id>` 실패 간선 → `choice`(param = 노드 id, 값 settle → 다음 주 경로 노드, extra → 선택 노드) |
| `branch:{of, when:'ok'|'miss'}` | `of` 노드의 성공/실패 간선이 각 갈래 첫 노드로 |
| `retryFor:'<id>'` | 공개 실패 간선 → 다시 시도 블록 첫 노드, 블록 끝 → `<id>` |
| `onLost:'<id>'` | `<id>`의 `{removed:태그}` 간선 → 이 노드 |
| `after.keepOnly` | 다음에 `cleanup` 노드(keep = 남길 줄, maxJunk = junk1이면 1) |
| `extra` | 그 노드 `act`의 추가 사용(시뮬레이터 `extra` 필드, 2차) |
| `phase` | `group`(그림 묶음). 위치 `pos`는 자동 배치(층 = 주 경로 순서, 옆 칸 = 실패 노드) |

변환은 "레시피가 쓴 그대로"만 옮기고, 확률은 다시 시뮬레이터가 정해요. 지금 엔진 값과 차이가 크면(아래 1차 결과처럼) 엔진 쪽 가정(되돌아가기 곱셈, 잃는 비율)을 다시 봐요.

## 1차 시험 결과 (치명타 투구, 20,000회)

`tools/sim/run.js` 출력과 `site/data/sim/diztoh-crit-helmet-v2.json` 참고. 요약은 CLAUDE.md "남은 일".
