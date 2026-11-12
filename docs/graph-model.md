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

## 그리기용 필드 (2026-11-09 2차 화면)

- 노드: `item`(그 단계 뒤 아이템 줄 `[{s:'p'|'s'|'x', kr, en, m:'n'|'f'|'u'|'d'|'j'}]` — 첫 열(주 경로) 노드만 왼쪽 아이템 칸에 표시, 앞 단계와 다르면 새 줄 강조·지워진 줄 취소선), `ask`(결과 판단 마름모 글, 간선 2개 이상이면 노드 아래 자동 마름모), `skipNote`(건너뛰는 조건을 상자 안 한 줄로) / `skipLabel`(건너뛰는 곳이 다음 주 경로 노드가 아니면 점선 간선 이름), `variant`(done: `best`·`settle` 등 마감 종류 색), `note`(별첨·마감 설명)
- 그래프: `loops:[{id, nodes:[첫 노드 = 반복 머리, …], kr, en}]`(반복 구간 — 머리 상자에 구간 총 소모·평균 바퀴 수, 소속 상자는 보라 줄), loops `fold:true` + `goal{kr,en}`·`steps:[{kr,en,node}]`·`worst{kr,en,to}`·`item`(2026-11-12: 다중 루프를 상자 하나로 그림 — 소속 노드·간선은 시뮬에 그대로, 그림만 접힘. 상자 안에 목표·순서·단계별 평균 개수, 밖으로는 성공 선과 최악의 경우 선만), `versions:[{id, kr, en, params, desc}]`(가성비·타협·Best 같은 버전 → 전략 옵션 묶음)
- 화면: 위→아래, 묶음(groups) = 영역(① 베이스 작업 ② 옵션 추가 작업), 모양 = 시작(알약)·작업(상자)·결과 판단(마름모)·분기(노란 마름모, `choice`)·마감(알약, `done`)·별첨(접힌 모서리, `assume`). 선 = 꺾은선(모서리 둥글게), 되돌아감 보라 점선, 베이스부터 빨강. 배치는 `pos` 열·행을 쓰고 크기·간격·선 경로는 화면이 계산(recipes.html `fcLayout`·`fcRoute`·`fcLabels`).
- 방향(사용자 확정 2026-11-09): **플로우차트를 먼저 만들고, 유저가 버전(가성비·타협·Best)을 고르면 그 경로를 지금의 레시피 단계 화면처럼 보여 주는 구조**로 감.

## 노드 종류

| kind | 뜻 | 필드 |
|---|---|---|
| `base` | 새 베이스 구입(노멀, 옵션 없음). 베이스 수를 셈 | `next` |
| `act` | 커런시 한 번 사용 | `act`(transmute·augment·regal·exalt·chaos·annul·desecrate·reveal·divine·fracture·flux), `cur`, `omens[]`, `curIf:[{if, cur}]`(상태에 따라 오브 바꾸기, 예: 치명타 1티어면 완벽한 엑잘티드 오브), `trim:{side, keep}`(정책 23④ 절사/말소 자동 선택), `want`(공개 때 고를 태그), `skipIf`+`skipTo`, `edges` |
| `cleanup` | 징조 없는 소멸의 오브를 반복해 `keep` 태그 밖의 줄을 `maxJunk`개 이하로 줄임. `keep` 줄이 지워지면 그 자리에서 멈춤 | `keep[]`, `maxJunk`, `edges:[{lost:태그, to}, {to}]` |
| `choice` | **정책 노드**: 전략 옵션 값으로 갈래를 고름(타협 / 추가 과정, 정리 방법 등) | `param`, `options:{값: 노드 id}`, `edgeLabels` |
| `assume` | 계산상 가정(1차 시험: 접미 분열 = 같은 비용 가정 → 분열 줄을 바꿔 본 흐름으로) | `swapFracture`, `next` |
| `done` | 완성 | — |

재시작은 따로 종류를 두지 않고 `base` 노드로 가는 간선이에요(예: 잡옵 분열 → 베이스부터).

## 간선 조건 (행동 직후 상태로 판단, 위에서부터 처음 맞는 것)

- `{has:태그}` 아이템에 있음 · `{added:태그}` 이번에 붙음 · `{removed:태그}` 이번에 지워짐 · `{fractured:태그}` 이번에 분열됨
- `{full:'p'|'s'}` 그쪽이 꽉 참 · `{sideAll:{side, tag}}` 그쪽의 분열 아닌 줄이 모두 태그에 맞음
- `{all:[…]}`, `{any:[…]}`, `{not:…}`, `{ref:'conds 이름'}`, `{param:{이름:값}}`
- 조건 없는 간선 = 나머지 전부

확률은 그래프에 적지 않아요. 같은 상태 규칙(아래)으로 굴린 결과가 간선을 고르고, 간선별 통과 횟수가 결과 파일 `edges`에 남아요.

## 시뮬레이터 규칙 (`site/sim.js`)

에뮬레이터(`site/emulator.html`)와 같은 규칙, 확률 모델은 레시피 엔진(`recipes.html analyse`)과 같은 가정이에요.

- 추가: 자리 남은 쪽(접두·접미)의 일반 그룹(같은 계열 제외), 가중치 비례. 상위·완벽 오브는 최소 레벨(crafting.json `min`), 단 그 계열의 최고 티어는 항상 후보
- 매직 = 접두·접미당 1줄, 희귀 = 3줄(베이스 `pd`/`sd` 반영). 좌측·우측 징조(찬미·대관식·말소·소멸·강령술)는 그쪽만
- 소멸의 오브: 분열 아닌 줄(미공개 훼손 포함) 중 무작위 1개. 빛의 징조 = 훼손 줄만
- 카오스 오브: 지우고 아무 쪽에 추가(말소의 징조는 **지우는 쪽만** 정함 — 새 줄은 자리 남은 어느 쪽이든). 절사의 징조 = 요구 레벨이 가장 낮은 줄(동률 무작위), 말소와 같이 쓰면 그쪽에서 가장 낮은 줄
- 뼈: 빈 면으로, 꽉 찬 쪽이면 그쪽 줄 하나를 지우고 들어감. 공개 = 그룹 3개(훼손 전용 1000, 일반 = 티어 가중치 합, 뼈 최소 레벨) 중 고름, 심연의 메아리 = 못 찾으면 한 번 다시 뽑기
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

## 2026-11-10 추가 (시한 장화 2차)

- 조건: `count:{tag,min}`(그 태그 줄 수), `allMods:tag`(미공개 말고 모든 줄이 그 태그), `sideLt:{side,n}`(그쪽 줄 수 < n).
- `act:'essence'` + `omens`에 결정화의 징조: 레어면 그쪽 줄 하나를 먼저 지우고 에센스 줄을 붙임. `mark:true`면 그 줄이 심연 군주의 징표.
- `act:'desecrate'` + `fromMark:true`: 징표를 미공개 훼손 줄로 바꿈(뼈 최소 레벨 적용).
- 간선 `hide:true` + `res:'ok'`도 그 단계 성공 확률 계산에 들어감(화면엔 안 그림).
- 간선 `port`(bottom/right)·`enter`(top/left)·`lane`(같은 lane 이름끼리는 겹침 허용). 메인 열(pos[0]=0) 상자는 위로만 들어감(`enter` 없을 때).

## 2026-11-11 추가 (리버스 크래프팅 플로우차트)

- `site/graphify.js` `fromDraft(초안, 클래스 파일, {craft, grades})` → 그래프, `view` → 화면용 그림 데이터, `check` → 등급별 시뮬·문제 목록. 브라우저(리버스 화면)와 node 공용.
- 조건 `rune:'이름 일부'`(2026-11-12): 이번 진행에서 그 룬을 이미 장착함(룬 상자 `act:'rune'`의 `rune.en`·`rune.kr`에서 대소문자 무시하고 찾음, 그래프 `astrid:true`면 아스트리드는 처음부터 장착). 룬 상자에 `skipIf:{rune:'Astrid'}` + `skipTo`로 되돌아올 때 다시 지나지 않게.
- `act:'flux'`(2026-11-12): `cur`가 맹렬한(`Blazing_Flux`)·오싹한(`Chilling_Flux`)·치직대는(`Crackling_Flux`)·공허(`Void_Flux`) 유동체면 아이템의 그 원소 저항 옵션을 같은 수치 범위의 목표 원소 저항 옵션으로 바꿈(원소 → 카오스는 POE2DB 대응표, 원소 3티어 → 카오스 2티어 등 — game-rules.md)(저항·저항 최대치·훼손 복합 저항의 원소 부분, 분열·미공개 옵션은 그대로, 훼손·에센스 표시는 유지, 같은 계열 두 개 공존 가능). 시뮬 `site/sim.js` `fluxTarget`, 엔진 `recipes.html` `do:'flux'`(같은 규칙). 예전처럼 `act:'divine'` + 유동체 `cur`로 두면 변환 없이 사용량만 셈. 완성품 카드에 같은 태그를 두 줄 적으면 `fincheck.js`는 그 태그가 두 개 있어야 통과
- 루프 `itemBy:{high,bal,ess}`(2026-11-12): 접힌 루프 상자의 왼쪽 아이템 칸을 등급(버전 id)마다 따로(`goalBy`처럼). 없으면 `item`. 등급에서 늘 건너뛰는 상자(시뮬 지나간 횟수 = 건너뛴 횟수, 사용량 없음, `skipTo` 있음)는 그 등급 플로우차트에서 빠지고 들어오는 선은 `skipTo`로 이어짐, 레시피 단계에서도 빠짐(`graph2recipe` `Walk.skipall`)
- 조건 `famBlock:태그`: 원하는 옵션의 계열을 다른 옵션(티어가 안 맞는 같은 그룹 포함)이 이미 차지해 그 단계로는 절대 못 붙음.
- 그래프 `maxSteps`: 한 번 진행에서 이 단계 수를 넘으면 `runaway`(기본 200만, 리버스 검사는 30만).
- sim.js 에센스: 에센스 옵션이 들어갈 쪽이 꽉 차 있으면 결정화의 징조가 반대쪽이어도 그쪽 옵션이 지워짐(발굴 규칙 6). 공개할 옵션이 하나도 없으면 아무것도 안 붙음(멈춤 방지).

## 2026-11-13 공용 수정 (S1)

- 룬 상자 `swapAstrid:true`: 아스트리드의 창의성을 빼고 그 룬(시뮬·엔진·완성 카드 `fcRunes`). `count:n`(같은 룬 n개) 또는 `fill:true`(빈 소켓 모두 그 룬) — 'Limited to 1' 룬에는 쓰지 않음(`tools/test/runerules.py`). graph2recipe가 `target.swapAstrid`·`runeCount`·`runeFill`로 옮김.
- graph2recipe: 옛 단계 레시피의 갈래 글(`br`)과 마지막 '선택'(optional) 단계 글은 붙이지 않음 — 갈래는 플로우차트 선에서 읽음. 꿀팁 번호(`tips`)·영상 시각만 이어받고, notes_short `TIPREF`는 플로우차트 상자 id로도 붙음(build_recipes).
- graph2recipe: `act:'flux'` 상자는 확률 1(확정). `trim` 상자의 징조 = 시뮬이 실제로 쓴 절사·말소 징조(많이 쓴 순서), 경우가 둘 이상이면 경우별 줄(`fcs.rows`: 잡옵이 가장 낮음 / 접두·접미에서만 가장 낮음 / 남길 옵션이 더 낮음)과 그때 확률. 공개 상자 쪽 = 공개된 줄 → 바로 앞 훼손 상자의 쪽 → 고르는 옵션의 쪽(접힌 상자는 아이템 칸이 없음). 퀄리티 상자에 `q`가 없으면 상자 글의 'n%' → `count` → 20.
- 상자·단계의 '1회 시도': 선 구조로는 되돌아올 수 있어도 그 버전 시뮬에서 빗나감이 돌아오지 않으면(시도 × 확률 ÷ 도달 < 0.9) 1/확률 대신 실제 사용량을 보여 줌.
- 완성 카드 퀄리티는 그래프 `finalItem.quality`가 먼저(엔진 값은 촉진 징조로 0이 되거나 기본 20일 수 있음).
- `tools/sim/engine.js`: 플로우차트에서 읽은 레시피(fcRead)는 화면 계산이 시뮬 값을 그대로 쓰므로, 엔진 비교값은 시뮬 값(fcRead·fcs)을 빼고 엔진 규칙으로 따로 계산(`mode:'engine'`, '빗나가면 다시' 선은 같은 단계 반복). 계산이 막히면 예전처럼 시뮬 값(`mode:'fcRead(...)'`). 예전 값은 지난번 시뮬과 같아서 비교가 되지 않았음(시한 차유라 반지 '엔진 197' = 옛 시뮬). 엔진은 되돌아가기를 구간 전체 곱으로 세서 그래프 레시피에선 시뮬보다 크게 나오는 경우가 많음 — 차이 자체보다 방향(어느 단계가 큰지)만 참고.
- 선택 상자(`kind:'side'`): graph2recipe가 레시피에 '선택' 단계(`optional`, 붙는 상자 `attach[0]` 다음, `attach`가 완성이면 끝)로 넣음 — 비용 합계는 시뮬 값이라 들어가지 않고, 아이템 상태는 앞 단계 그대로. `tiers:['high']`처럼 버전 id를 적으면 그 버전 플로우차트·레시피에만 나옴. 붙는 상자가 그 버전에서 빠지면 선 없이 그림(예전엔 TypeError로 버전 버튼이 멈춤).
- 완성 카드 훼손 색: 그래프에 `des`를 적지 않은 줄은 시뮬 훼손 비율(`desStat`)이 99.9% 이상일 때만 초록. 81%처럼 다른 경로(먼저 뜬 일반 옵션)가 있으면 일반 색. 바뀐 카드: 시한 셉터 밸런스·에센셜, 노블 화살통 하이엔드, MazBro 시전자 반지 밸런스·에센셜, 시한 투구 에센셜, 균열 물리 반지 밸런스.
