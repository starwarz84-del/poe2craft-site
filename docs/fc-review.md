# 플로우차트 영상 대조 점검표

사용자 확정(2026-11-11 21:34): 등록된 모든 아이템 레시피를 영상과 대조해 고침. 서비스는 결국 이 솔루션이 얼마나 믿을 만하게 돌아가는지가 중요함. 두 세션(A = Opus, B = Fable)이 겹치지 않게 이 표로 나눠요.

규칙

- 시작하기 전에 `git pull` → 그 줄의 상태를 '진행 중'과 세션 이름으로 바꿔 바로 커밋·푸시해요. 남이 '진행 중'인 줄은 건드리지 않아요.
- 끝나면 '완료' + 날짜 + 한 줄 결과(바꾼 곳, 시뮬 비용 전·후). 자세한 기록은 `docs/recipe-notes.md`.
- 점검 순서: 영상(자막 + 화면) → 플로우차트 단계마다 영상 시점 확인 → 영상에 없는 단계 정리(영상대로가 원칙, 더 싼 길은 기록만 — 정책 0장 3번, 11-12) → 들어오는 선·숨긴 선 → 등급(정책 10장 C17: 반복 목표 티어 1 / 1~2 / 1~4, 마지막 옵션 잡옵 도박은 하이엔드만, 에센셜은 빛의 징조 없음, 같으면 높은 등급만) → 시뮬 → 레시피 화면 확인.
- 검사 도구: `python3 tools/test/fcaudit.py`(전수), `python3 tools/test/fc_noinput.py`(들어오는 선).
- 알림(A, 11-12): `site/sim.js`가 바뀜 — 징표를 훼손한 공개는 한 티어 높게, 선 번호별 통과 수(`edgesI`), 공개 빗나감에 가장 높은 레벨 옵션 고르기(`missPick:'lvl'`), 조건 `desSide`. B가 맡은 mazbro-bis-chest-v2·diztoh-iceshot-bow-v2 시뮬은 다시 돌려야 새 규칙이 반영됨. `recipes.html` 준비 구간 계산이 플로우차트 합계를 같이 쓰던 문제도 고침(엔진 비교값이 두 배로 나오던 것).

| 플로우차트 | 영상 | 등급 비용(div, 점검 전) | 검사 문제 | 상태 | 세션 | 메모 |
|---|---|---|---|---|---|---|
| mirror-bow-video-v2 | J0LF3MRssh0 | high 13,791 | 6 | 완료 11-13(새 기준) · 검수 90점 | W15-거울활(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W15): 영상 전체 재대조(성공 회차 = 독사의 비), 전용 생성기 gen_mirror_bow_video.py. 준비 구역(매직 접힘·제왕·턱뼈·분열 1/3) 추가, 자리 막기 = 공격 스킬의 원소 피해(옛 정확도 틀림) 접힌 상자, 세 번째 접두 = 물리 피해 + 정확도·물리 피해 추가 중 먼저 뜬 것(남은 쪽은 마지막 훼손 공개, 사용자 결정 11-13), 베이스 특출난 그대로 35 div(사용자 확정). 9,677(준비 미포함) → 13,791 |
| banzino-mirror-staff-v2 | vT482uJFESs | high 7,754, bal 4,686 | 5 | 제외 11-13(사용자 결정) | W18-거울지팡이(Opus 5.5) · 검수 마스터 | W18 재작성 뒤 사용자 결정: 가중치 문제(전도성 지팡이 베이스별 옵션 제한이 데이터에 없어 카오스·절사 확률이 실제보다 낮음)로 사이트에서 뺌(build_recipes.py EXCLUDED). 재작성 결과 7,842 div·생성기 gen_banzino_mirror_staff.py는 남김 |
| xeno-phys-crossbow-v2 | 1TP4aGqxU7Q | high 10,845 | 7 | 완료 11-13(새 기준) · 검수 90점 | W17-석궁(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W17): 자막 없는 영상 전체 화면 대조, 전용 생성기 gen_xeno_crossbow.py. 준비 구역(상위 진화·완벽한 확장 → 제왕 → 보존된 턱뼈 → 분열 1/3) 추가, 자리 막기 = 정확도·공격 원소 피해 1티어 중 먼저 뜬 것(사용자 결정 11-13), 공격 속도 뒤 물리 피해 추가 공개(사용자 확정 11-09) 유지, 신성한 오브·히네코라·룬 뺌, 퀄리티 20%(숫돌)는 비용 밖. 7,227(준비 미포함) → 10,845. 11번 주변(w1·w1p·wc)과 12번 접미(s2·w2·s3·w3)를 접힌 상자로(사용자 지적 11-13 04:04), 11 → 9 되돌림은 상자 단계 ③ 글로만 |
| barricade-quarterstaff-v2 | B4yShuKydt0 | high 6,095, bal 960 | 2 | 완료 11-13(새 기준) · 검수 88점 | W21(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W21): 영상 전체 화면 재대조, 전용 생성기 gen_barricade_quarterstaff.py. 준비 구역(7 div 베이스·숫돌·주입기 8개 30%·진화·제왕·소멸·카오스 치명타·엑잘 2번·턱뼈·분열 1/3) 펼침, 세번째 접두 L2 접음(완벽한 엑잘 → 절사 카오스 → 좌측 소멸), 접두는 원소 피해 넷 중 먼저 뜬 것, 절사가 훼손 공격 속도를 지키게(옛 그래프 버그). 2,617/619 → 6,095/960(준비·베이스 3개 포함, 하이엔드 절사 카오스 210개). 레시피 탭에 옛 recipes_v5 글(p2 분기·히네코라 선택)이 이어짐(공용) |
| mazbro-bis-chest-v2 | LUB59xlkNtk | high 2,859 | 21 | 완료 11-12(검수 90점) | W7-흉갑(Opus 5.5) · 검수 마스터 | 새 기준 재작성: 성공 회차(첫 흉갑) 한 줄, 분열 준비 구역(노트대로, 흉갑 분열 장면은 영상에 없음), 접미 반복(상위 찬미 엑잘 → 절사 + 완벽한 카오스 → 우측 소멸) 접음, 자리 막기 = 생명력 재생 훼손. 난이도 5라 하이엔드만(밸런스 삭제, 21:00 '끝내도 됨'은 꿀팁 후보). 완성 조건은 영상대로 복합 저항 셋 중 둘이라 카드(화염·카오스 + 냉기·카오스)는 완성품의 66%만 그대로. 베이스 0.11 div(카오스 오브 1개). 시뮬 5000회 2,859(중앙 2,400), reqOk 1 |
| sihan-highend-helmet-v2 | CTrIbhQVU8U | high 479, bal 259 | 0 | 완료 11-12(새 기준) · 검수 92점 | W8-시한투구(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W8): 영상 27:22 전체, 캡처 98장. 성공 회차(셋째 투구, 접미 16:40~17:58, 유동체 18:35, 접두 18:52~25:26), 완성품 25:45 툴팁과 카드 일치. 확정 옵션: 분열 생명력, 카오스 치명타, 접미 방어도 원소 적용, 접두 방어도 최대치, 공개 방어도 %. 다중 루프 2곳 접음, 공허 유동체로 번개 → 카오스 저항. 밸런스 세번째 접미 랜덤. 첫 회차(치명타가 지워짐)는 꿀팁. 2,613/202 → 471/260 |
| noble-visceral-quiver-v2 | 2PUEwoePtRs | high 1,803, bal 307 | 3 | 완료 11-13(새 기준) · 검수 88점 | W20(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W20): 자막 없는 영상 전체 화면 대조(0.4 영상), 전용 생성기 gen_noble_visceral_quiver.py. 준비 구역(진화·확장 + 소멸 → 제왕 + 턱뼈 → 분열 1/3), 접미 치명타 L1·접두 마지막 L2 접음, 첫 공개는 막기(0.5 모든 투사체 +1은 레벨 5라 마지막 공개 — 0.4의 +2 훼손 옵션은 0.5에 없음). 신성한 오브 비용 제외. 1,416/110 → 1,803/307. 첫 접미를 영상 계획(치확·치피·투사체 중 하나)으로 넓힐지 사용자 확인 대기 |
| diztoh-iceshot-bow-v2 | 29vO0mMUoME | high 3,719 | 0 | 완료 11-12(새 기준) · 검수 94점 | W3-활(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W3): 영상 22:21 전체, 캡처 97장. 옛 메모 바로잡음(1:21 분열 장면 있음, 절사 오브 = 상위 카오스 재확인). 베이스 하나로 끝까지 간 회차 그대로, 원소 피해 추가·빛 없이 다시 공개 루프 접음. 첫 훼손 고대 턱뼈·다시 훼손 보존된 턱뼈(인벤토리 아이콘·개수 6:41~14:40). 하이엔드만(난이도 5), 마지막 접미 랜덤(정책 10장 예외, 사용자 확정). 뼈 이름 툴팁은 확인 못 함. 5,638 → 3,719 |
| breach-ring-video-v2 | RiJixgqBnBY | high 3,912, bal 1,912 | 0 | 완료 11-12(새 기준) · 검수 92점 | W9-균열반지(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W9): 영상 31:50 전체, 캡처 63장. 성공 회차 = 두 번째 반지(분열 26:25, 완성 29:05 툴팁과 카드 일치). 28:25~29:40은 녹화 정전으로 화면 없음(자막·비용 화면·완성 툴팁으로 판단). 확정 옵션: 분열 화염 플랫, 카오스 모든 원소 저항, 엑잘 번개, 훼손 냉기. 준비 = 분열 먼저 → 퀄리티 66%(가이드, 사용자 확정). 밸런스 유효 옵션 필수. 1,956/651 → 3,912/1,912(베이스·분열 비용 포함, 확정 옵션) |
| sihan-proj-gloves-v2 | DH4jiORLg10 | high 1,257, bal 443 | 2 | 완료 11-12(새 기준) · 검수 90점 | W10-시한장갑(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W10): 성공 회차 한 줄, 첫 접두·접두 루프·공개는 물리 피해 추가·투사체 피해·투사체 속도 중 먼저 뜬 것(사용자 확정 11-12), 카드는 성공 회차 순서. 시뮬 5000회 1,257(중앙 958)·443(중앙 371), reqOk 1. 레시피 글 12·15번에는 '먼저 뜬 것' 줄이 아직 안 나옴(graph2recipe showText 미반영) |
| sl-blacksteel-gauntlets-v2 | J7J8Jo7ibvE | high 2,823 | 4 | 완료 11-13(새 기준) · 검수 88점 | W13-검은강철(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W13): 슬라이드(6:10~6:22)만 있는 영상. 6:08 완성품 툴팁에서 분열은 접미 저주 강도(옛 그래프의 상태 이상 강도 분열은 틀림) → 슬라이드 10번 갈래로 다시 짬. 하이엔드만(극한), 매직 루프(저주 강도 1티어 + 카틀라 접두 1티어) 접음, 접두·접미는 같은 1티어 묶음이라 먼저 뜬 것(K39). 베이스 12 div는 MazBro 장갑 값 빌림. 비용의 78%는 13번 절사 카오스(평균 114번) |
| sl-flamewave-ring-v2 | UAF91gEFRkM | high 1,449, bal 390 | 2 | 완료 11-13(새 기준) · 검수 88점 | W30(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W30): 영상 전체 화면 대조, 전용 생성기 gen_sl_flamewave_ring.py. 분열 준비 구역 추가, 접미 반복을 우측 소멸 2번 + 상위 찬미로 고침(옛 그래프는 하나씩), 절사 카오스 징조는 화면대로 우측 말소(슬라이드 좌측은 오기). 하이엔드 마지막 접미 = 희귀도 T1 반복(슬라이드 목표, 잡옵만 바뀌어 안전), 밸런스 랜덤. 1,423/371 → 1,449/390 |
| absent-amulet-spell6-v2 | Yi1u0LhJztI | high 830 | 10 | 완료 11-13(새 기준) · 검수 90점 | W12-부재목걸이(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W12): 하이엔드만, 준비 구역(제왕 → 균열 에센스 → 기폭제·주입기 49% → 카오스 정신력 1티어 → 접미 찬미 엑잘·결정화 균열 에센스 → 빗장뼈 → 분열 1/3) 포함. 히네코라 없이(사용자 결정 11-13: 영상대로면 10,349 div), 실패하면 새 베이스. 퀄리티 50% 주입기 타락 위험은 비용에 없음. 마나 최대치 루프 접음. 베이스 가격 미정. 사용자 결정(11-13 02:24): 퀄리티 50%(기폭제 40개·주입기 10개)와 축성을 빼고 전문가(4)로 — 제목 주문 +3, 1,014 → 830 |
| sl-flamewave-staff-v2 | 6EzSVUItzsg | high 1,620, bal 382 | 3 | 완료 11-13(새 기준) · 검수 88점 | W26(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W26): 영상 전체 화면 대조, 전용 생성기 gen_sl_flamewave_staff.py. 준비 구역(매직 +7 확장·소멸 → 제왕 → 보존된 턱뼈 → 분열 1/3) 추가, 성공 회차 옵션(화염 피해·추가 냉기·추가 화염 1티어, 접두는 먼저 뜬 것), 하이엔드 = 스루드의 완력 → 상위 찬미 엑잘 → 절사 카오스(화염 속성 부여 규모) → 초월의 합금(지우면 절사 다시, 영상에 없음), 밸런스 = 9:13 가성비 마무리. 알두르의 배신·유동체·퀄리티·바알 오브 뺌. 1,296/39.7 → 1,620/382(준비 약 330 포함). 합금 도박 구간 552 div — 선택 단계로 뺄지 사용자 확인 대기 |
| mazbro-caster-amulet-v2 | 4PazhuHwdL8 | high 1,689, bal 589 | 5 | 완료 11-13(새 기준) · 검수 88점 | W27(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W27): 영상 전체 화면 대조, 전용 생성기 gen_mazbro_caster_amulet.py. 준비(정신력 50 구입 5 div·빗장뼈·분열 1/3) 추가, 카오스 스팸·접미 두 자리·접두 촉진 엑잘 접힌 상자 3개, 기폭제 촉진 대상을 게임 태그대로. 1,154/410 → 1,689/589. 세 번째 접미 목표(메모 = 시전 속도·치명타, 영상 성공 회차는 마나 재생·희귀도)와 밸런스 공개 결과 그대로(C17-3 충돌)는 사용자 확인 대기. 카드 퀄리티 +20% 표시(실제 40%) 공용 문제 |
| sihan-highend-boots-v2 | dlrD21AcCUE | high 192, bal 139 | 2 | 완료 11-13(새 기준) · 검수 88점 | W19(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W19): 영상 전체 재대조(성공 회차 기적의 발걸음), 전용 생성기 gen_sihan_highend_boots.py. 분열 준비(진화·확장 → 제왕 → 갈비뼈 → 분열 1/3), 접미 L2(우측 찬미 엑잘 + 공허 유동체 + 소멸, 힘·원소 저항 중 먼저 뜬 것), 접두 L4(엑잘 → 결정화 + 심연 징표), 훼손 L5 접음. 옛 퀄리티·다른 유효 옵션 분열 상자 뺌. 1,119/265 → 192/139. 남은 것: 레시피 탭 p1에 옛 recipes_v5 분기 줄이 이어짐, 유동체 단계가 확률(6.8%)로 표시(공용) |
| grasping-mail-spell1-v2 | y5Ch3AJpl5c | high 35,199 | 11 | 완료 11-13(새 기준) · 검수 90점 | W11-사슬옷(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W11): 하이엔드만, 베이스 = 모든 주문 +1 분열(카오스 22만 개 + 히네코라 4개 — 마스터가 히네코라를 베이스 가격에 다시 넣음, 영상 8:38·19차 노트), 접미 반복 접음(절사 10:12), 아스트리드 → 접두 잡옵 하나만 남기기(영상은 육신의 에센스 반복, 시뮬은 좌측 소멸로 대체 약 37 div) → 섬망 → 군왕의 합금(POE2DB: 룬 수호는 군왕의 합금) → 고대 갈비뼈 → 주문 피해 1티어. 베이스 제외 제작 약 1,170 div |
| sl-proj7-gloves-v2 | XMYJh3CnXuY | high 2,362 | 7 | 완료 11-13(새 기준) · 검수 88점 | W14-SL장갑(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W14): 영상 전체 화면 대조, 전용 생성기 gen_sl_proj7_gloves.py. 준비 구역(콜르 → 완벽한 진화·확장 + 소멸 → 제왕 → 보존된 갈비뼈 → 분열 1/3) 펼침, 콜르 옵션 xroll 누락 수정. 접두 3개 접은 상자(세 번째 = 공격 시 피해 추가·에너지 보호막·마나 최대치 중 먼저 뜬 것, 사용자 결정 11-13), 접미 치명타 + 합금 접은 상자, 관통 1티어 훼손. 세를은 분열 뒤 장착(시뮬 매직 한계). 1,104 → 2,362(준비 포함), 베이스 가격 미정. 접은 상자 11의 사용량 띠가 왼쪽 칸과 겹침(공용 화면) |
| saveq-absent-amulet-v2 | S4sflKbsA8A | high 935, bal 797, ess 729 | 4 | 재확인 필요 | A(Opus) | 자동 번역 자막 전체(기록 tools/notes/saveq-S4sflKbsA8A.md), 단계 일치. 935/797/729 → 935/797/688 |
| unstoppable-vile-robe-v2 | swF5mwXmZ0k | high 739, bal 689 | 4 | 진행 중(새 기준 재작성) | W34(Opus 5.5) · 검수 마스터 | 영상 5:45~24:15 대조. 접미는 엑잘+소멸(비싼 징조는 마지막 한 옵션만), 접두 막기·결정화+심연. 하이엔드 739→809, 밸런스(1티어 + 마지막 접미 랜덤) 689→163 |
| helmet-armour-sl-v2 | p0fChSu91uI | high 723, bal 718, ess 75 | 5 | 재확인 필요 | A(Opus) | 자막 전체(0:00~11:10) 대조, 단계 일치(기록 tools/notes/sl-p0fChSu91uI.md). 723/718/75 → 723/83/60(밸런스·에센셜 마지막 접두·접미 랜덤) |
| diztoh-endgame-quarterstaff-v2 | YfGJyBrObxI | high 2,887, bal 948 | 3 | 완료 11-13(새 기준) · 검수 88점 | W22(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W22): 영상 전체 화면 대조로 성공 회차를 새로 씀(옛 노트와 크게 다름), 전용 생성기 gen_diztoh_endgame_quarterstaff.py. 상위 카오스 → 상위 엑잘 + 좌측 찬미(소멸) → 완벽한 엑잘·절사 카오스 → 우측 말소 + 상위 카오스 → 훼손 공개 접음. 사용자 결정(11-13): 접미 빈자리에 훼손, 공개 빗나감은 항상 빛의 징조(영상 방식이면 36,103 div). 세 번째 접두는 두 등급 모두 랜덤 옵션(10장 예외). 1,043/577 → 2,887/948 |
| unstoppable-slipstrike-vest-v2 | swF5mwXmZ0k | high 651, bal 176 | 1 | 진행 중(새 기준 재작성) | W34(Opus 5.5) · 검수 마스터 | 영상 40:45~46:30 대조. 첫 카오스 추가, 반복은 상위 카오스, 접두 결정화+심연. 하이엔드 870→651, 밸런스 540→176 |
| breach-ring-phys-v2 |  | bal 535, ess 89 | 2 | 대기 |  |  |
| diztoh-crit-helmet-v2 | QuW8BOSpPpo | high 3,852, bal 1,132 | 1 | 완료 11-13(새 기준) · 검수 90점 | W6-투구(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W6): 성공 회차(7:23~12:03) 한 줄, 접두 반복 8번 접음. 말소 카오스의 새 옵션이 접미로 가면 희귀도·카오스 저항 3티어 이상은 남기고 원소 저항 3티어 이상은 공허 유동체로 카오스 저항(사용자 결정 11-13, 영상은 9:17 소멸) — 4,436 → 3,852. 마지막 접미는 배포판처럼 11번 완벽한 엑잘(희귀도·화염·카오스 저항 1티어) + 11.A 가장 낮은 레벨일 때만 절사·우측 말소, 카드는 랜덤 옵션(사용자 확정 11-13: 영상도 마지막은 받아들임). 생성기 scripts/graphs/gen_diztoh_crit_helmet.py |
| mazbro-sceptre-v2 | UwzsARlgaFM | high 757 | 10 | 완료 11-13(새 기준) · 검수 88점 | W16-셉터(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W16): 영상 전체 재대조, 전용 생성기 gen_mazbro_sceptre.py. 준비 구역(진화·확장 + 소멸 → 제왕 → 좌측 강령술 턱뼈 → 분열 1/3) 펼침, 사용자 결정(11-13 영상 계획대로 넓게): 정신력 증가·정신력과 마나 1티어 중 먼저 뜬 것, 접미는 마나 재생·시전 속도·존재 범위·치명타 확률·치명타 피해 1티어 중 둘 + 합금(접힌 상자). 501(준비 미포함) → 1,876(좁게) → 757. 신성한 오브·식각기·유동체·쥬얼러 오브 뺌 |
| sihan-chayula-ring-v2 | GgD_vxKgNsw | high 478, bal 144 | 0 | 진행 중(새 기준 재작성) | W32(Opus 5.5) · 검수 마스터 | 자막 전체 + 화면 2:30~3:45 대조(기록 tools/notes/sihan-GgD_vxKgNsw.md). 카오스는 저항 또는 카오스 피해, 완벽한 엑잘에서 좌측 찬미 뺌(영상에서 접미에도 붙음). 478/144 → 356/130 |
| mastert-timelost-emerald-v2 | GNNkhSENp6Q | high 460(+베이스 94), bal 91(+94) | 1 | 완료 11-13(새 기준) · 검수 90점 | W23(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W23): 영상 전체 화면 대조(성공 회차 Sol Curio), 전용 생성기 gen_mastert_timelost_emerald.py. 접두 = 상태 이상·감전의 강도 먼저 뜬 것(18:00 계획), 하이엔드 공개 = 이동 속도, 밸런스 = 영상 11:00의 좋은 접미 다섯 중 하나 + 빛의 징조(C17-3). 신성한 오브 마무리 뺌, 베이스 94 div(영상 매물), 아이템 레벨 80(화면) |
| noble-timelost-sapphire-v2 | zEV8kWwveYQ | high 592, bal 564 | 3 | 완료 11-13(새 기준) · 검수 88점 | W25(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W25): 영상 전체 화면 재대조, 전용 생성기 gen_noble_timelost_sapphire.py. 준비 구역(매직 1 div → 제왕·엑잘 → 분열 1/4 → 소멸), 경멸·치명타 피해(L1)·반경·최대 마나(L2) 접음, 두개골에 좌측 강령술(시뮬 쪽 고정). 퀄리티 기폭제 20개(약 194 div) 뺌. 경멸 전 엑잘을 영상대로 1번(11-10 사용자 확정은 2번 — 시뮬 차이 없음, 사용자 확인 대기). 468/418 → 592/564 |
| tankjung-kitava-shield-v2 | gQa51XOS98s | high 572, bal 392 | 0 | 완료 11-12(새 기준) · 검수 93점 · 21:46 배포 | W5-방패(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W5): 슬라이드 영상 전 구간(2초 간격 훑기 1,428프레임, 캡처 98장). 실제 게임 장면 없음 → 오브 등급·뼈·징조는 슬라이드 글로만 확인. 흐름 = 슬라이드 STEP 02~13 한 줄, 매직 접미 루프 접음, 물리 피해 감소 공개 갈래를 공개 상자 하나로, 절사는 완벽한 카오스(자막 20:00). 밸런스 = 방어도 3종 1~2티어(유효 옵션 필수). 아이템 레벨 81 이유는 확인 못 함. 524/165 → 523/352. 공용 문제(진화 상자 평균 10개, 무관한 자동 꿀팁 #77, 왼쪽 칸 겹침)는 W2 수정 중 · 4차(사용자 지적 20:56): 확정 옵션 — 분열 받는 물리 피해 8%, 카오스 화염 저항 최대치, 훼손 공개(냉기·번개) 뒤 맹렬한 유동체로 화염 두 줄(슬라이드 완성 문구·사용자 제공 거래소 아이템). 523/352 → 572/392 |
| absent-amulet-video-v2 | jr6-YLMJsC8 | high 356, bal 223 | 8 | 진행 중(새 기준 재작성) | W29(Opus 5.5) · 검수 마스터 | 자막 전체 대조, 단계·분기 일치(기록 tools/notes/sl-jr6-YLMJsC8.md). 등급 C17도 이미 맞음. 변경 없음 |
| gold-amulet-6line-v2 | cb36jD9pqsw | high 354, bal 345 | 20 | 삭제 11-11 | B(Fable) | 사용자 요청으로 내림(22:21). 플로우차트 옵션이 영상이 만든 목걸이와 달랐음. 다시 올리려면 영상 전체 기준으로 새로 만들고 build_recipes.py REMOVED·build_tips.py·gen_batch11.py의 막아 둔 줄을 지움 |
| saveq-focus-v2 | R43FVay8_XI | high 343, bal 208 | 5 | 진행 중(새 기준 재작성) | W31(Opus 5.5) · 검수 마스터 | 자막 전체 대조, 첫 번째 집중구 단계 일치(기록 tools/notes/saveq-R43FVay8_XI.md). 하이엔드 에너지 보호막 접두도 1티어(C17). 343/208 → 504/208 |
| mazbro-spell5-amulet-v2 | kULlZJBSec4 | high 222, bal 201 | 0 | 진행 중(새 기준 재작성) | W28(Opus 5.5) · 검수 마스터 | 자막 전체 대조, 단계 일치(기록 tools/notes/mazbro-kULlZJBSec4.md). 하이엔드 공개 목표 1티어(C17). 222/201 → 233/201 |
| diztoh-rarity-ring-v2 | GDLDxn6yxEs | high 149, bal 20, ess 15 | 1 | 재확인 필요 | A(Opus) | 자막 전체 대조, 단계 일치(기록 tools/notes/diztoh-GDLDxn6yxEs.md). C17: 에센셜은 공개 나오는 대로(영상과 같음). 149/24/3 |
| bigdaddy-lightning-wand-v2 | 글: mobalytics.gg/poe-2/profile/bigdaddygami | bal 146, ess 98 | 2 | 재확인 필요 | A(Opus) | 글 다시 확인(6/22판), 가성비 길 단계 일치(기록 tools/notes/web-bigdaddy-wand.md). 완성품 임의 문구를 태그로. 비용 그대로 |
| ragna-spell4-amulet-v2 | Tzpdm8M-Pkk | bal 118, ess 27 | 0 | 재확인 필요 | A(Opus) | 자막 전체(3:34) 대조, 단계 일치(기록 tools/notes/ragna-Tzpdm8M-Pkk.md). C17도 맞음. 변경 없음 |
| mazbro-proj-gloves-v2 | BIxlixCKPO0 | high 677, bal 364 | 0 | 완료 11-12(새 기준) · 검수 96점(13번 묶음 접힌 상자·11.A 아래 출구 17:40, 14번 제작 옵션 붙이기(발작·합금) 접힌 상자 추가 20:00 — 사용자 지적 19:12) | W1-장갑(Opus 5.5) · 검수 마스터 | 새 기준 재작성: 영상 전 구간 캡처 80장·단계표(scratchpad W1-mazbro-gloves). 흐름 한 줄 — 영상 성공 회차대로 카오스 = 투사체 속도 1티어(15:56), 마지막 공개 = 투사체 피해(18:24, 사용자 확정 11-12). 아스트리드 분열 전(8:06), 룬 가격은 시뮬 비용 미포함. 388/265 → 672/357 |
| fubgun-proj-amulet-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 110, ess 97 | 3 | 재확인 필요 | A(Opus) | 글 목걸이 부분 다시 대조, 일치(기록 tools/notes/web-fubgun-iceshot.md). 완성품 줄을 DB 태그로. 값 그대로 |
| diztoh-5mod-emerald-v2 | s70CV_nvjXg | bal 108, ess 30 | 0 | 재확인 필요 | A(Opus) | 자막 전체(31:47) 대조, 단계 일치(기록 tools/notes/diztoh-s70CV_nvjXg.md). 완성품 줄을 DB 태그로. 값 그대로 |
| diztoh-vile-robe-v2 | n97yEuKSWyM | bal 152, ess 49 | 0 | 완료 11-12(새 기준) · 검수 94점 | W4-로브(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W4): 영상 전체 캡처 82장·단계표. 로브 한 개를 처음부터 완성까지 진행한 회차 그대로. 준비 구역에 소멸(2:23·3:18), 아스트리드는 영상대로 갈비뼈(4:55) 뒤 6:10, 8번 접미 원소 저항 다중 루프 접음(우측 소멸 → 절사 + 상위 카오스 → 빈 접미 엑잘), 7 → 8 확정 선. 원소 저항 2~3티어(아이템 레벨 81이라 1티어 불가). 확인 못 함: 베이스 가격, 3:19~3:28 상위 카오스 II 아이콘(구입·툴팁·자막으로 판단), 10:04~10:27 갈비뼈 순간(편집). 152/49 → 152/49 |
| sl-5mod-jewel-v2 | VKMT7tuSIYk | bal 104, ess 57 | 0 | 재확인 필요 | A(Opus) | 자막 전체(13:10) 대조, 단계 일치(기록 tools/notes/sl-VKMT7tuSIYk.md). 완성품 줄을 DB 태그로. 값 그대로 |
| sihan-chayula-wand-v2 | rSs4fumlHo4 | bal 98, ess 26 | 0 | 대기 |  |  |
| sihan-attack-flat-ring-v2 | bpXgZGw4WQo | bal 97, ess 23 | 1 | 대기 |  |  |
| diztoh-5mod-sapphire-v2 | -YZm55-QuoQ | bal 95, ess 43 | 0 | 대기 |  |  |
| easybabi-spiny-talisman-v2 | fabBIuR6yhw | high 94, bal 13 | 1 | 진행 중(새 기준 재작성) | W33(Opus 5.5) · 검수 마스터 |  |
| vodnarg-timelost-emerald-v2 | 3tFs16SXkD8 | bal 94, ess 70 | 0 | 대기 |  |  |
| lilbotq-boots-v2 | S-7YHuq3-P4 | bal 92, ess 5 | 2 | 대기 |  |  |
| mazbro-caster-ring-v2 | o3Fh1DJmxBA | bal 86, ess 16 | 1 | 대기 |  |  |
| lilbotq-emerald-v2 | Hcb_HcWDUOA | bal 84 | 0 | 대기 |  |  |
| diztoh-as-spear-v2 | cTjgn7NnHR8 | bal 81, ess 60 | 2 | 대기 |  |  |
| saveq-alloy-focus-v2 | uCbyTF-LJ5I | bal 80, ess 1 | 0 | 대기 |  |  |
| chiba-timelost-emerald-v2 | O6Rp7JIxhrs | high 160, bal 157 | 0 | 완료 11-13(새 기준) · 검수 90점 | W24(Opus 5.5) · 검수 마스터 | 새 기준 재작성(W24): 영상 전체 화면 대조, 전용 생성기 gen_chiba_timelost_emerald.py, 노트 tools/notes/chiba-O6Rp7JIxhrs.md. 준비 구역(공격 치명타 + 옵션 2개 레어 14 div → 보존된 두개골 → 분열 1/3, 실패 새 베이스 → 소멸) 추가. 밸런스 = 마지막 접두 랜덤 + 공개는 빛의 징조로 다시(C17-3). 77.9/64.8(베이스·준비 없음) → 160/157. 밸런스가 2%만 싸서 뺄지 사용자 확인 대기 |
| fubgun-crit-bow-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 62, ess ? | 3 | 대기 |  |  |
| seek-cyclone-boots-v2 | cj9o8_LuFQs | bal 53, ess 14 | 2 | 대기 |  |  |
| belton-plus8-wand-v2 | j0FeuX0NZQI | bal 38, ess 12 | 0 | 대기 |  |  |
| sihan-chayula-sceptre-v2 | -F7pV0Y7BMA | bal 36, ess 13 | 0 | 대기 |  |  |
| diztoh-onehand-mace-v2 | WDEkEIQFgT4 | bal 33, ess ? | 0 | 대기 |  |  |
| sihan-chayula-helmet-v2 | z_r1uAYIusk | bal 31, ess 15 | 0 | 대기 |  |  |
| fubgun-phys-bow-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 28, ess ? | 3 | 대기 |  |  |
| lilbotq-armour-shield-v2 | 4YOSSAa53UU | bal 27, ess 7 | 0 | 대기 |  |  |
| sihan-chayula-gloves-v2 | Sf-2cvWhQY0 | bal 27, ess 23 | 1 | 대기 |  |  |
| diztoh-budget-mace-v2 | ITbefGq6V18 | bal 23, ess 1 | 0 | 대기 |  |  |
| diztoh-budget-crossbow-v2 | vk3pLFUov8U | bal 22, ess 1 | 0 | 대기 |  |  |
| fubgun-es-helmet-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 18, ess ? | 3 | 대기 |  |  |
| farmer-budget-armour-v2 | UWrIgHklsPg | high 17, bal 6, ess ? | 0 | 대기 |  |  |
| icesly-budget-wand-v2 | gtxAqZfCxxI | bal 15, ess 11 | 0 | 대기 |  |  |
| zenm-timelost-sapphire-v2 | IKC9DquM7GM | bal 13, ess 9 | 0 | 대기 |  |  |
| fubgun-quiver-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 10, ess ? | 3 | 대기 |  |  |
| lilbotq-budget-boots-v2 | S-7YHuq3-P4 | bal 10, ess 6 | 0 | 대기 |  |  |
| farmer-starter-staff-v2 | ITBexsgq2NI | high 8, bal 4, ess 2 | 0 | 대기 |  |  |
| diztoh-socket-gloves-v2 | CI7zQO_Ml_s | bal 5, ess 1 | 1 | 대기 |  |  |
| diztoh-talisman-v2 | p6HIFmJ9mRU | bal 5, ess ? | 0 | 대기 |  |  |
| diztoh-es-helmet-v2 | yegMdBTuEtY | bal 2, ess ? | 0 | 대기 |  |  |
| sane-resist-belt-v2 | Zop328DR50Q | bal 1, ess 1 | 0 | 대기 |  |  |
| ragna-ashot-bow-v2 | m0eHw6nq24Q | bal ?, ess ? | 0 | 대기 |  |  |
| sihan-chayula-amulet-v2 | 2vyq26ZFgOk | bal ?, ess ? | 0 | 대기 |  |  |

## 등급 기준 C17 점검 (사용자 확정 2026-11-12 00:09)

기준(policies.md 10장): 비싼 반복으로 찾는 옵션은 하이엔드 1티어 · 밸런스 1~2티어 · 에센셜 1~4티어, 접두어·접미어 마지막 옵션이 잡옵이면 하이엔드만 바꾸는 도박(밸런스·에센셜은 랜덤 옵션), 훼손 공개 빗나감에 빛의 징조는 하이엔드·밸런스만(빛 없이 다시 할 수 있으면 에센셜도 반복), 다 적용해도 같으면 높은 등급만 남김. 싸게 한 번에 붙이는 옵션(분열 뒤 카오스, 매직 단계)은 모든 등급 1티어, 티어 수가 적은 옵션은 있는 만큼만.
시작 전 그 줄을 '진행 중 + 세션'으로 바꿔 푸시. 영상 대조 표의 같은 아이템을 맡은 세션이 같이 해도 됨.

| 플로우차트 | 등급 | 기준과 다른 티어 범위(자동 검사) | 상태 | 세션 | 메모 |
|---|---|---|---|---|---|
| absent-amulet-spell6-v2 | bal·high | - | 재확인 필요 | 진행 중(새 기준 재작성) | W12-부재목걸이(Opus 5.5) · 검수 마스터
| absent-amulet-video-v2 | bal·high | high 접두 1티어, bal 1~2티어 + 강화 에센스 마무리 | 재확인 필요 | A(Opus) | 변경 없음 |
| banzino-mirror-staff-v2 | bal·high | - | 재확인 필요 | A(Opus) 하이엔드만 레시피(극한). 플로우차트 밸런스: 시전 속도·훼손 접두 1~2티어, 마지막 접두·접미 랜덤 — 3,325 → 664 |
| barricade-quarterstaff-v2 | bal·high | - | 재확인 필요 | A(Opus) 밸런스 원소 피해 접두 2개 1~2티어(전엔 1개), 세번째 랜덤 — 346 → 619. 하이엔드 2,617 그대로 |
| belton-plus8-wand-v2 | ess·bal | ess 주문 피해 1~5티어; ess 마나 재생 1~3티어; bal 주문 피해 1~3티어; bal 마나 재생 1티어 | 대기 |  |  |
| bigdaddy-lightning-wand-v2 | ess·bal | bal 마지막 접두 1~2티어(빛), ess 1~4티어·공개 그대로 | 재확인 필요 | A(Opus) | 이미 맞음 |
| breach-ring-phys-v2 | ess·bal | ess 화염 저항 1~3티어; bal 공격 시 원소 피해 1~3티어 | 대기 |  |  |
| breach-ring-video-v2 | bal·high | - | 재확인 필요 | A(Opus) | 밸런스 접미 1~2티어, 마지막 훼손 접두 랜덤(메아리 없음) — 934 → 651 |
| chiba-timelost-emerald-v2 | bal·high | - | 대기 |  |  |
| diztoh-5mod-emerald-v2 | ess·bal | - | 재확인 필요 | A(Opus) | 주얼 티어 하나라 맞음 |
| diztoh-5mod-sapphire-v2 | ess·bal | - | 대기 |  |  |
| diztoh-as-spear-v2 | ess·bal | - | 대기 |  |  |
| diztoh-budget-crossbow-v2 | ess·bal | ess 물리 피해 % 1~3티어; ess 원소 피해 추가 1~5티어; bal 원소 피해 추가 1~3티어 | 대기 |  |  |
| diztoh-budget-mace-v2 | ess·bal | - | 대기 |  |  |
| diztoh-crit-helmet-v2 | budget·settle·best | best 1티어 + 마지막 접미 도박, settle 1~2티어, budget 최대치 1~4티어·공개 한 번 | 완료 11-12 · 검수 95점 | A(Opus) | 1,287/278/219 |
| diztoh-endgame-quarterstaff-v2 | bal·high | high 1티어, bal 1~2티어 + 마지막 접두·접미 랜덤 | 재확인 필요 | A(Opus) | 1,043/577 |
| diztoh-es-helmet-v2 | ess·bal | ess 접두 희귀도 1~2티어; bal 에너지 보호막 % 1~3티어; bal 접두 희귀도 1티어 | 대기 |  |  |
| diztoh-iceshot-bow-v2 | bal·high | 물리 피해 추가 모두 1티어, high 1티어 + 마지막 접미 도박, bal 1~2티어 | 완료 11-12 · 검수 90점 | A(Opus) | 4,091/1,321 |
| diztoh-onehand-mace-v2 | ess·bal | ess 치명타 확률 1~3티어 | 대기 |  |  |
| diztoh-rarity-ring-v2 | ess·bal·high | high 1티어, bal 1~2티어, ess 1~4티어·공개 나오는 대로 | 재확인 필요 | A(Opus) | 149/24/3 |
| diztoh-socket-gloves-v2 | ess·bal | - | 대기 |  |  |
| diztoh-talisman-v2 | ess·bal | ess 화염 피해 추가 1~5티어; bal 화염 피해 추가 1~3티어 | 대기 |  |  |
| diztoh-vile-robe-v2 | ess·bal | ess 정신력 (분열) 1~6티어; ess 에너지 보호막 최대치 1~2티어; ess 에너지 보호막 % 1~3티어; bal 정신력 (분열) 1~4티어; bal 에너지 보호막 최대치 1티어 | 완료 11-12 · 검수 97점 | A(Opus) | 반복 목표: 밸런스 최대치 1 → 1~2, 에센셜 최대치·% 1~4(정신력은 구입 베이스라 그대로) |
| easybabi-spiny-talisman-v2 | bal·high | bal 원소 피해 접두 1~3티어; high 원소 피해 접두 1~2티어 | 대기 |  |  |
| farmer-budget-armour-v2 | ess·bal·high | ess 에너지 보호막 최대치 1~3티어 | 대기 |  |  |
| farmer-starter-staff-v2 | ess·bal·high | ess 추가 화염 피해 1~2티어 | 대기 |  |  |
| fubgun-crit-bow-v2 | ess·bal | - | 대기 |  |  |
| fubgun-es-helmet-v2 | ess·bal | - | 대기 |  |  |
| fubgun-phys-bow-v2 | ess·bal | - | 대기 |  |  |
| fubgun-proj-amulet-v2 | ess·bal | - | 재확인 필요 | A(Opus) | 이미 맞음(밸런스 빛 1~2티어, 에센셜 결과 그대로) |
| fubgun-quiver-v2 | ess·bal | ess 물리 피해 추가 1~2티어; bal 물리 피해 추가 1티어 | 대기 |  |  |
| grasping-mail-spell1-v2 | bal·high | - | 재확인 필요 | 진행 중(새 기준 재작성) | W11-사슬옷(Opus 5.5) · 검수 마스터
| helmet-armour-sl-v2 | ess·bal·high | high 1티어, bal 1~2티어, ess 1~4티어(빛의 징조 없음), bal·ess 마지막 접두·접미 랜덤 | 재확인 필요 | A(Opus) | 723/83/60 |
| icesly-budget-wand-v2 | ess·bal | ess 번개 주문 레벨 1~2티어; ess 번개·주문 피해 1~5티어; bal 번개 주문 레벨 1티어; bal 번개·주문 피해 1~3티어 | 대기 |  |  |
| lilbotq-armour-shield-v2 | ess·bal | ess 방어도 % 1~2티어; ess 방어도 % + 기절 한계치 1~3티어; bal 방어도 % 1티어; bal 방어도 % + 기절 한계치 1티어 | 대기 |  |  |
| lilbotq-boots-v2 | ess·bal | - | 대기 |  |  |
| lilbotq-budget-boots-v2 | ess·bal | ess 이동 속도 1~2티어; ess 냉기 저항 1~3티어; bal 이동 속도 1티어; bal 냉기 저항 1티어 | 대기 |  |  |
| lilbotq-emerald-v2 | bal | - | 대기 |  |  |
| mastert-timelost-emerald-v2 | bal·high | 주얼이라 티어 없음, high 이동 속도 공개 반복 · bal 결과 그대로 | 재확인 필요 | A(Opus) | 459/78 |
| mazbro-bis-chest-v2 | high | 난이도 5 → 하이엔드만 | 완료 11-12 | W7 | 3,023 → 2,859 |
| mazbro-caster-amulet-v2 | bal·high | - | 재확인 필요 | A(Opus) | 밸런스 시전 속도·마나 1~2티어, 마지막 접두·접미 랜덤 — 428 → 410 |
| mazbro-caster-ring-v2 | ess·bal | ess 옵션 티어 1~3티어 | 대기 |  |  |
| mazbro-proj-gloves-v2 | bal·high | - | 완료 11-12 · 검수 95점 | A(Opus) | 이미 맞음(하이엔드 1티어 훼손, 밸런스 마지막 접두 랜덤) |
| mazbro-sceptre-v2 | high | - | 대기 |  |  |
| mazbro-spell5-amulet-v2 | bal·high | high 공개 1티어, bal 마지막 접미 랜덤 | 재확인 필요 | A(Opus) | 233/201 |
| mirror-bow-video-v2 | high | - | 재확인 필요 | A(Opus) 하이엔드만(극한), 바꿀 것 없음 |
| noble-timelost-sapphire-v2 | bal·high | 주얼이라 티어 없음 | 재확인 필요 | A(Opus) | 변경 없음 |
| noble-visceral-quiver-v2 | bal·high | bal 치명타 피해 1~3티어; high 치명타 피해 1~2티어 | 재확인 필요 | A(Opus) | 하이엔드 모두 1티어(영상 '치피 1티'), 밸런스 1~2티어·마지막 접두·접미 랜덤 — 110 → 110 |
| ragna-ashot-bow-v2 | ess·bal | ess 물리 피해 % 1~3티어; bal 물리 피해 % 1티어 | 대기 |  |  |
| ragna-spell4-amulet-v2 | ess·bal | bal 1~2티어(영상), ess 결과 그대로·빛 없음 | 재확인 필요 | A(Opus) | 이미 맞음 |
| sane-resist-belt-v2 | ess·bal | ess 생명력 1~3티어; ess 번개 저항 1~3티어; bal 생명력 1티어 | 대기 |  |  |
| saveq-absent-amulet-v2 | ess·bal·high | - | 재확인 필요 | A(Opus) | 에센셜 빛의 징조 없이 공개 한 번(랜덤 옵션) — 729 → 688 |
| saveq-alloy-focus-v2 | ess·bal | ess 공개 목표 1~3티어; bal 공개 목표 1티어 | 대기 |  |  |
| saveq-focus-v2 | bal·high | 에너지 보호막·주문 치명타 high 1티어, bal 1~2티어 | 재확인 필요 | A(Opus) | 504/208 |
| seek-cyclone-boots-v2 | ess·bal | - | 대기 |  |  |
| sihan-attack-flat-ring-v2 | ess·bal | ess 원소 공격 추가 피해 1~3티어 | 대기 |  |  |
| sihan-chayula-amulet-v2 | ess·bal | ess 정신력 1~2티어; bal 정신력 1티어 | 대기 |  |  |
| sihan-chayula-gloves-v2 | ess·bal | - | 대기 |  |  |
| sihan-chayula-helmet-v2 | ess·bal | ess 튕겨내기 평점 1~3티어; ess 방어 접두 1~3티어; bal 방어 접두 1~3티어 | 대기 |  |  |
| sihan-chayula-ring-v2 | bal·high | high 1티어, bal 1~2티어, 마지막 두 옵션은 원하는 옵션이 없어 둘 다 랜덤 | 재확인 필요 | A(Opus) | 356/130 |
| sihan-chayula-sceptre-v2 | ess·bal | ess 접근 효과 범위 1~2티어; ess 정신력 % + 마나 1~6티어; bal 접근 효과 범위 1티어; bal 정신력 % + 마나 1~4티어 | 대기 |  |  |
| sihan-chayula-wand-v2 | ess·bal | ess 주문 치명타 명중 확률 1~3티어 | 대기 |  |  |
| sihan-highend-boots-v2 | ess·bal·high | ess 저항 목표 1~2티어; ess 훼손 접두 목표 1~3티어 | 재확인 필요 | A(Opus) | 밸런스 접두 1~2티어, 마지막 접두·접미 랜덤. 에센셜은 밸런스와 같아(265/266) 뺌 — 난이도 4로 올려 하이엔드·밸런스 레시피 둘 다(사용자 확정 11-12) |
| sihan-highend-helmet-v2 | bal·high | high 저항 1~3티어 (상위 카오스) | 재확인 필요 | A(Opus) | 밸런스 방어도 1~2티어, 마지막 접미(저항) 랜덤 — 181 → 202 |
| sihan-proj-gloves-v2 | bal·high | - | 재확인 필요 | A(Opus) | 밸런스 1~2티어, 마지막 훼손 접두 랜덤 — 327 → 282 |
| sl-5mod-jewel-v2 | ess·bal | - | 재확인 필요 | A(Opus) | 주얼 티어 하나라 맞음 |
| sl-blacksteel-gauntlets-v2 | bal·high | - | 재확인 필요 | 진행 중(새 기준 재작성) | W13-검은강철(Opus 5.5) · 검수 마스터
| sl-flamewave-ring-v2 | bal·high | - | 재확인 필요 | A(Opus) | 이미 기준대로(저항 1~2티어, 마지막 접미 랜덤, 훼손 핵심 옵션은 반복) — 371 그대로 |
| sl-flamewave-staff-v2 | bal·high | - | 재확인 필요 | A(Opus) | 밸런스 접두 반복 1~2티어, 마지막 접두·접미 랜덤 — 178 → 40 |
| sl-proj7-gloves-v2 | bal·high | - | 대기 |  |  |
| tankjung-kitava-shield-v2 | ess·bal·high | high 1티어(영상), bal 1~2티어, ess 최대 저항 1~3티어·방어도 1~4티어 | 완료 11-12 · 검수 94점 | A(Opus) | 358/125/58, 난이도 4로 올림(사용자 11-12) → high·bal 표시 |
| unstoppable-slipstrike-vest-v2 | bal·high | bal 굴절 1~4티어; high 굴절 1~3티어 | 재확인 필요 | A(Opus) 하이엔드 굴절 1~3 → 1티어(651 → 1,368), 밸런스 1~2티어 + 마지막 접미 랜덤(176 → 74) |
| unstoppable-vile-robe-v2 | bal·high | bal 접두 에너지 보호막·정신력 1티어; bal 저항 1티어 | 재확인 필요 | A(Opus) 밸런스 접두(엑잘·훼손 반복) 1 → 1~2티어(163 → 99), 저항은 싼 반복이라 1티어 유지 |
| vodnarg-timelost-emerald-v2 | ess·bal | - | 대기 |  |  |
| xeno-phys-crossbow-v2 | high | - | 재확인 필요 | A(Opus) 하이엔드만(극한), 바꿀 것 없음 |
| zenm-timelost-sapphire-v2 | ess·bal | - | 대기 |  |  |

> 2026-11-12 12:45 A(Opus): 11-12에 '완료'로 표시한 A(Opus) 줄은 자막·단계 이름만 맞추고 완성 화면(플로우차트·완성품 카드)을 보지 않은 채 표시한 것이라 모두 '재확인 필요'로 되돌림(사용자 지적). 다시 할 때는 한 개씩: 영상 자막 + 화면 전체 확인 → 고침 → 플로우차트·완성품 카드 스크린샷을 사용자에게 보인 뒤 완료.
