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
| mirror-bow-video-v2 | J0LF3MRssh0 | high 9,035 | 6 | 완료 11-11 | A2(서브) | 영상 15:00~16:00대로 물리 피해 % 1티어를 시작에서 빼고 첫 카오스 단계(약 387 div, 영상 예상 카오스 4,000개)로. 공격 원소 피해 타협 길은 숨김. 하이엔드 9,035→9,677(첫 카오스 비용이 들어간 값). 11-11 23시 메인 세션이 자막 전체(0:00~35:20) 다시 확인: 단계 일치, 막기는 영상이 말한 정상 루트(정확도) — 기록 tools/notes/banzino-J0LF3MRssh0.md |
| banzino-mirror-staff-v2 | vT482uJFESs | high 7,754, bal 4,686 | 5 | 완료 11-11 | A2(서브) | 접미 두·세번째는 영상대로 절사의 징조만(말소 빼기). 마지막 접두 pT는 말소 포함 절사 유지(치명타 1티어 레벨 76이라 절사만으로는 끝나지 않음). 하이엔드 7,754→5,415, 밸런스 4,686→3,325. 11-11 23시 메인 세션이 자막 전체(0:00~9:46) 다시 확인: 마지막 접두 '절사'(9:20)는 치명타 1티어(76)가 지워지지 않게 말소를 같이 씀 |
| xeno-phys-crossbow-v2 | 1TP4aGqxU7Q | high 7,227 | 7 | 완료 11-11 | A(Opus) | 자막 없음 → 화면 직접 확인(4:45~9:55, 기록 tools/notes/xeno-1TP4aGqxU7Q.md). 그래프가 영상과 맞아 그대로(순서만 사용자 확정 11-09). 7,227 그대로. 영상에 없는 더 싼 투사체 길(우측 소멸 + 상위 찬미 엑잘, 약 5,840)은 사용자 확인 대기 |
| barricade-quarterstaff-v2 | B4yShuKydt0 | high 4,068, bal 387 | 2 | 완료 11-11 | A(Opus) | 자막 전체 확인. 81 동률 잡옵만 영상대로 좌측 소멸 1/3 → 엑잘. 근접 +5 과정은 영상에 없어 추정. 2,617 / 346(4,068은 옛 시뮬값, 원래 그래프도 지금 2,636) |
| mazbro-bis-chest-v2 | LUB59xlkNtk | high 3,023, bal 960 | 15 | 대조만 끝남 | B(Fable) | 영상 기록 tools/notes/mazbro-LUB59xlkNtk.md. 접두 엑잘·절사 카오스를 상위로 바꾸면 조금 쌈(시뮬 확인) — 아직 안 고침 |
| sihan-highend-helmet-v2 | CTrIbhQVU8U | high 2,616, bal 180 | 1 | 완료 11-12 | A(Opus) | 자막 전체(0:00~27:20) 대조, 단계 일치. 기록 tools/notes/sihan-CTrIbhQVU8U.md. 징표 훼손 한 티어 높게(시뮬 규칙 추가). 2,642/181 → 2,613/202 |
| noble-visceral-quiver-v2 | 2PUEwoePtRs | high 2,240, bal 110 | 3 | 완료 11-12 | A(Opus) | 자막 없음 → 화면 자막 0:00~11:47 전체(기록 tools/notes/noble-2PUEwoePtRs.md). 영상대로 다시 만듦: 남은 접미 훼손을 먼저 공개해 가장 높은 레벨 옵션으로 자리 막기 → 접두 엑잘 → 절사 카오스(막기가 가장 낮으면 빛의 징조로 다시 훼손) → 막기 지우고 보존된 턱뼈로 투사체. 2,240/110 → 1,416/110 |
| diztoh-iceshot-bow-v2 | 29vO0mMUoME | high 1,999, bal 1,058 | 5 | 완료 11-12 | A(Opus) | 자막 전체 + 화면 9:25 대조(기록 tools/notes/diztoh-29vO0mMUoME.md). 단계 일치. 접두 단계에서 접미 잡옵이 쌓여 제작 옵션 한도를 넘던 것을 고침(훼손 전에 접미 비우기, 매 단계 아이템 다시 보기). 1,999/1,058 → 4,091/1,321(치명타 확률 1티어 / 1~2티어) |
| breach-ring-video-v2 | RiJixgqBnBY | high 1,956, bal 934 | 4 | 완료 11-12 | A(Opus) | 자막 전체(0:00~31:50) 대조, 권장 순서와 일치(기록 tools/notes/sl-breach-RiJixgqBnBY.md). 1,956/934 → 1,956/651(밸런스 마지막 훼손 접두 랜덤) |
| sihan-proj-gloves-v2 | DH4jiORLg10 | high 1,659, bal 327 | 2 | 완료 11-12 | A(Opus) | 자막 전체(0:00~27:40) 대조(기록 tools/notes/sihan-DH4jiORLg10.md). 접두 엑잘의 좌측 찬미 뺌(접미가 이미 3개), 두 번째 접두 실패 = 심연 징표를 둔 채 엑잘 → 징표에 고대 갈비뼈(영상 추천). 1,659/327 → 1,619/282 |
| sl-blacksteel-gauntlets-v2 | J7J8Jo7ibvE | high 1,649, bal 140 | 4 | 완료 11-12 | A(Opus) | 자막엔 제작 설명 없음 → 6:12 슬라이드 직접 확대 확인(14단계 일치). 슬라이드에 없는 메아리 뺌. 1,649/140 → 1,794/874(밸런스 두번째 접미도 1~2티어까지 반복, 상위 오브) |
| sl-flamewave-ring-v2 | UAF91gEFRkM | high 1,423, bal 371 | 2 | 완료 11-12 | A(Opus) | 자막 전체(0:00~11:20) 대조, 단계·커런시 일치로 바꾸지 않음(기록 tools/notes/sl-UAF91gEFRkM.md). 1,423/371 그대로 |
| absent-amulet-spell6-v2 | Yi1u0LhJztI | high 1,330, bal 756 | 10 | 완료 11-12 | A(Opus) | 자막 전체(0:00~42:38) + 화면 27:00~34:00(기록 tools/notes/banzino-Yi1u0LhJztI.md). 균열의 에센스에 좌측 결정화 추가, 접미 훼손을 막기로 먼저 공개, 엑잘 빗나감 = 빛의 징조 + 심연 징표 → 고대 빗장뼈 공개(영상 29:30~31:20), 시전 속도는 고대 빗장뼈. 마나가 엑잘·징표 중 어디서 붙었는지는 화면으로 확인 못 함. 1,330/756 → 2,515/216 |
| sl-flamewave-staff-v2 | 6EzSVUItzsg | high 1,296, bal 178 | 3 | 완료 11-12 | A(Opus) | 자막 전체(0:00~15:13) 대조, 단계 일치(기록 tools/notes/sl-6EzSVUItzsg.md). 1,296/178 → 1,296/40(밸런스 마지막 접두·접미 랜덤) |
| mazbro-caster-amulet-v2 | 4PazhuHwdL8 | high 1,154, bal 428 | 5 | 완료 11-12 | A(Opus) | 자동 번역 자막 전체(0:00~39:40) 대조, 영상 가이드 1~11단계와 일치(기록 tools/notes/mazbro-4PazhuHwdL8.md). 1,154/428 → 1,154/410 |
| sihan-highend-boots-v2 | dlrD21AcCUE | high 1,147, bal 650, ess 314 | 2 | 완료 11-12 | A(Opus) | 자막 전체(0:00~17:50) 대조(기록 tools/notes/sihan-dlrD21AcCUE.md). 접두를 영상 순서로 다시 만듦: 징표를 둔 채 엑잘 → 징표에 고대 갈비뼈. 1,143/656/314 → 1,119/265(에센셜 뺌) |
| grasping-mail-spell1-v2 | y5Ch3AJpl5c | high 1,140, bal 613 | 11 | 완료 11-12 | A(Opus) | 자막 전체 + 화면 10:00~12:00(기록 tools/notes/banzino-y5Ch3AJpl5c.md). 할당 → 접두 추가 → 룬 합금 50:50 → 훼손 주문 피해가 그래프와 같음, 접미 과정은 영상이 건너뜀(가정 유지). 분열 베이스 카오스 약 22만 개를 비용에 포함(사용자 확정 11-12). 1,140/613 → 25,619/24,496 |
| sl-proj7-gloves-v2 | XMYJh3CnXuY | high 1,104, bal 785 | 7 | 완료 11-11 | B(Fable) | 자막 전체 대조. 합금 실패 뒤 길을 보이는 선 + 규칙에 맞게(우측 소멸의 징조로 접미 비우기). 1,104·785 |
| saveq-absent-amulet-v2 | S4sflKbsA8A | high 935, bal 797, ess 729 | 4 | 완료 11-12 | A(Opus) | 자동 번역 자막 전체(기록 tools/notes/saveq-S4sflKbsA8A.md), 단계 일치. 935/797/729 → 935/797/688 |
| unstoppable-vile-robe-v2 | swF5mwXmZ0k | high 739, bal 689 | 4 | 완료 11-11 | A(Opus) | 영상 5:45~24:15 대조. 접미는 엑잘+소멸(비싼 징조는 마지막 한 옵션만), 접두 막기·결정화+심연. 하이엔드 739→809, 밸런스(1티어 + 마지막 접미 랜덤) 689→163 |
| helmet-armour-sl-v2 | p0fChSu91uI | high 723, bal 718, ess 75 | 5 | 완료 11-12 | A(Opus) | 자막 전체(0:00~11:10) 대조, 단계 일치(기록 tools/notes/sl-p0fChSu91uI.md). 723/718/75 → 723/83/60(밸런스·에센셜 마지막 접두·접미 랜덤) |
| diztoh-endgame-quarterstaff-v2 | YfGJyBrObxI | high 712, bal 36 | 3 | 완료 11-12 | A(Opus) | 자동 번역 자막 전체(0:00~17:40) 대조, 단계 일치(기록 tools/notes/diztoh-YfGJyBrObxI.md). 공개 빗나감은 영상의 우측 소멸 대신 빛의 징조(지금 시세가 더 쌈). 712/36 → 1,043/577(등급 1티어 / 1~2티어) |
| unstoppable-slipstrike-vest-v2 | swF5mwXmZ0k | high 651, bal 176 | 1 | 완료 11-11 | A(Opus) | 영상 40:45~46:30 대조. 첫 카오스 추가, 반복은 상위 카오스, 접두 결정화+심연. 하이엔드 870→651, 밸런스 540→176 |
| breach-ring-phys-v2 |  | bal 535, ess 89 | 2 | 대기 |  |  |
| diztoh-crit-helmet-v2 | QuW8BOSpPpo | high 512, bal 340, ess 278 | 1 | 완료 11-12 | A(Opus) | 자막 전체 대조, 단계 일치(기록 tools/notes/diztoh-QuW8BOSpPpo.md). 등급 C17 적용. 512/340/278 → 1,287/278/219 |  |
| mazbro-sceptre-v2 | UwzsARlgaFM | high 504 | 10 | 완료 11-11(그림만 확인 안 됨) | B(Fable) | 단계 대조는 함. 화면 캡처가 오른쪽이 잘린 채였음 — 선은 다시 볼 것 |
| sihan-chayula-ring-v2 | GgD_vxKgNsw | high 478, bal 144 | 0 | 완료 11-12 | A(Opus) | 자막 전체 + 화면 2:30~3:45 대조(기록 tools/notes/sihan-GgD_vxKgNsw.md). 카오스는 저항 또는 카오스 피해, 완벽한 엑잘에서 좌측 찬미 뺌(영상에서 접미에도 붙음). 478/144 → 356/130 |
| mastert-timelost-emerald-v2 | GNNkhSENp6Q | high 469, bal 88 | 1 | 완료 11-12 | A(Opus) | 자막 0:00~24:00 대조(기록 tools/notes/mastert-GNNkhSENp6Q.md). 경멸 전 엑잘 2번 → 영상대로 1번, 경멸 옵션을 지운 뒤 엑잘 1번 추가. 469/88 → 459/78 |
| noble-timelost-sapphire-v2 | zEV8kWwveYQ | high 468, bal 418 | 3 | 완료 11-12 | A(Opus) | 자막 전체 대조, 단계 일치(기록 tools/notes/noble-zEV8kWwveYQ.md). 경멸 전 엑잘 2번은 사용자 확정이라 그대로. 변경 없음 |
| tankjung-kitava-shield-v2 | gQa51XOS98s | bal 359, ess 48 | 2 | 완료 11-12 | A(Opus) | 자막 12:00~21:30 대조, 단계 일치(기록 tools/notes/tankjung-gQa51XOS98s.md). 첫 절사 전 확인 추가(에센셜 완성 조건 99% → 100%). 영상(1티어)은 하이엔드로: 358/125/58, 난이도 3 → 4(사용자 확정) |
| absent-amulet-video-v2 | jr6-YLMJsC8 | high 356, bal 223 | 8 | 완료 11-12 | A(Opus) | 자막 전체 대조, 단계·분기 일치(기록 tools/notes/sl-jr6-YLMJsC8.md). 등급 C17도 이미 맞음. 변경 없음 |
| gold-amulet-6line-v2 | cb36jD9pqsw | high 354, bal 345 | 20 | 삭제 11-11 | B(Fable) | 사용자 요청으로 내림(22:21). 플로우차트 옵션이 영상이 만든 목걸이와 달랐음. 다시 올리려면 영상 전체 기준으로 새로 만들고 build_recipes.py REMOVED·build_tips.py·gen_batch11.py의 막아 둔 줄을 지움 |
| saveq-focus-v2 | R43FVay8_XI | high 343, bal 208 | 5 | 완료 11-12 | A(Opus) | 자막 전체 대조, 첫 번째 집중구 단계 일치(기록 tools/notes/saveq-R43FVay8_XI.md). 하이엔드 에너지 보호막 접두도 1티어(C17). 343/208 → 504/208 |
| mazbro-spell5-amulet-v2 | kULlZJBSec4 | high 222, bal 201 | 0 | 완료 11-12 | A(Opus) | 자막 전체 대조, 단계 일치(기록 tools/notes/mazbro-kULlZJBSec4.md). 하이엔드 공개 목표 1티어(C17). 222/201 → 233/201 |
| diztoh-rarity-ring-v2 | GDLDxn6yxEs | high 149, bal 20, ess 15 | 1 | 완료 11-12 | A(Opus) | 자막 전체 대조, 단계 일치(기록 tools/notes/diztoh-GDLDxn6yxEs.md). C17: 에센셜은 공개 나오는 대로(영상과 같음). 149/24/3 |
| bigdaddy-lightning-wand-v2 | 글: mobalytics.gg/poe-2/profile/bigdaddygami | bal 146, ess 98 | 2 | 완료 11-12 | A(Opus) | 글 다시 확인(6/22판), 가성비 길 단계 일치(기록 tools/notes/web-bigdaddy-wand.md). 완성품 임의 문구를 태그로. 비용 그대로 |
| ragna-spell4-amulet-v2 | Tzpdm8M-Pkk | bal 118, ess 27 | 0 | 완료 11-12 | A(Opus) | 자막 전체(3:34) 대조, 단계 일치(기록 tools/notes/ragna-Tzpdm8M-Pkk.md). C17도 맞음. 변경 없음 |
| mazbro-proj-gloves-v2 | BIxlixCKPO0 | high 112, bal 66 | 40 | 진행 중 | A(Opus) |  |
| fubgun-proj-amulet-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 110, ess 97 | 3 | 진행 중 | A(Opus) |  |
| diztoh-5mod-emerald-v2 | s70CV_nvjXg | bal 108, ess 30 | 0 | 진행 중 | A(Opus) |  |
| diztoh-vile-robe-v2 | n97yEuKSWyM | bal 105, ess 51 | 0 | 진행 중 | A(Opus) |  |
| sl-5mod-jewel-v2 | VKMT7tuSIYk | bal 104, ess 57 | 0 | 진행 중 | A(Opus) |  |
| sihan-chayula-wand-v2 | rSs4fumlHo4 | bal 98, ess 26 | 0 | 대기 |  |  |
| sihan-attack-flat-ring-v2 | bpXgZGw4WQo | bal 97, ess 23 | 1 | 대기 |  |  |
| diztoh-5mod-sapphire-v2 | -YZm55-QuoQ | bal 95, ess 43 | 0 | 대기 |  |  |
| easybabi-spiny-talisman-v2 | fabBIuR6yhw | high 94, bal 13 | 1 | 대기 |  |  |
| vodnarg-timelost-emerald-v2 | 3tFs16SXkD8 | bal 94, ess 70 | 0 | 대기 |  |  |
| lilbotq-boots-v2 | S-7YHuq3-P4 | bal 92, ess 5 | 2 | 대기 |  |  |
| mazbro-caster-ring-v2 | o3Fh1DJmxBA | bal 86, ess 16 | 1 | 대기 |  |  |
| lilbotq-emerald-v2 | Hcb_HcWDUOA | bal 84 | 0 | 대기 |  |  |
| diztoh-as-spear-v2 | cTjgn7NnHR8 | bal 81, ess 60 | 2 | 대기 |  |  |
| saveq-alloy-focus-v2 | uCbyTF-LJ5I | bal 80, ess 1 | 0 | 대기 |  |  |
| chiba-timelost-emerald-v2 | O6Rp7JIxhrs | high 78, bal 65 | 0 | 대기 |  |  |
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
| absent-amulet-spell6-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 = 주문 +3까지, 마지막 접두·접미 랜덤 — 756 → 216 |
| absent-amulet-video-v2 | bal·high | high 접두 1티어, bal 1~2티어 + 강화 에센스 마무리 | 완료 11-12 | A(Opus) | 변경 없음 |
| banzino-mirror-staff-v2 | bal·high | - | 완료 11-12 | A(Opus) 하이엔드만 레시피(극한). 플로우차트 밸런스: 시전 속도·훼손 접두 1~2티어, 마지막 접두·접미 랜덤 — 3,325 → 664 |
| barricade-quarterstaff-v2 | bal·high | - | 완료 11-12 | A(Opus) 밸런스 원소 피해 접두 2개 1~2티어(전엔 1개), 세번째 랜덤 — 346 → 619. 하이엔드 2,617 그대로 |
| belton-plus8-wand-v2 | ess·bal | ess 주문 피해 1~5티어; ess 마나 재생 1~3티어; bal 주문 피해 1~3티어; bal 마나 재생 1티어 | 대기 |  |  |
| bigdaddy-lightning-wand-v2 | ess·bal | bal 마지막 접두 1~2티어(빛), ess 1~4티어·공개 그대로 | 완료 11-12 | A(Opus) | 이미 맞음 |
| breach-ring-phys-v2 | ess·bal | ess 화염 저항 1~3티어; bal 공격 시 원소 피해 1~3티어 | 대기 |  |  |
| breach-ring-video-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 접미 1~2티어, 마지막 훼손 접두 랜덤(메아리 없음) — 934 → 651 |
| chiba-timelost-emerald-v2 | bal·high | - | 대기 |  |  |
| diztoh-5mod-emerald-v2 | ess·bal | - | 대기 |  |  |
| diztoh-5mod-sapphire-v2 | ess·bal | - | 대기 |  |  |
| diztoh-as-spear-v2 | ess·bal | - | 대기 |  |  |
| diztoh-budget-crossbow-v2 | ess·bal | ess 물리 피해 % 1~3티어; ess 원소 피해 추가 1~5티어; bal 원소 피해 추가 1~3티어 | 대기 |  |  |
| diztoh-budget-mace-v2 | ess·bal | - | 대기 |  |  |
| diztoh-crit-helmet-v2 | budget·settle·best | best 1티어 + 마지막 접미 도박, settle 1~2티어, budget 최대치 1~4티어·공개 한 번 | 완료 11-12 | A(Opus) | 1,287/278/219 |
| diztoh-endgame-quarterstaff-v2 | bal·high | high 1티어, bal 1~2티어 + 마지막 접두·접미 랜덤 | 완료 11-12 | A(Opus) | 1,043/577 |
| diztoh-es-helmet-v2 | ess·bal | ess 접두 희귀도 1~2티어; bal 에너지 보호막 % 1~3티어; bal 접두 희귀도 1티어 | 대기 |  |  |
| diztoh-iceshot-bow-v2 | bal·high | 물리 피해 추가 모두 1티어, high 1티어 + 마지막 접미 도박, bal 1~2티어 | 완료 11-12 | A(Opus) | 4,091/1,321 |
| diztoh-onehand-mace-v2 | ess·bal | ess 치명타 확률 1~3티어 | 대기 |  |  |
| diztoh-rarity-ring-v2 | ess·bal·high | high 1티어, bal 1~2티어, ess 1~4티어·공개 나오는 대로 | 완료 11-12 | A(Opus) | 149/24/3 |
| diztoh-socket-gloves-v2 | ess·bal | - | 대기 |  |  |
| diztoh-talisman-v2 | ess·bal | ess 화염 피해 추가 1~5티어; bal 화염 피해 추가 1~3티어 | 대기 |  |  |
| diztoh-vile-robe-v2 | ess·bal | ess 정신력 (분열) 1~6티어; ess 에너지 보호막 최대치 1~2티어; ess 에너지 보호막 % 1~3티어; bal 정신력 (분열) 1~4티어; bal 에너지 보호막 최대치 1티어 | 대기 |  |  |
| easybabi-spiny-talisman-v2 | bal·high | bal 원소 피해 접두 1~3티어; high 원소 피해 접두 1~2티어 | 대기 |  |  |
| farmer-budget-armour-v2 | ess·bal·high | ess 에너지 보호막 최대치 1~3티어 | 대기 |  |  |
| farmer-starter-staff-v2 | ess·bal·high | ess 추가 화염 피해 1~2티어 | 대기 |  |  |
| fubgun-crit-bow-v2 | ess·bal | - | 대기 |  |  |
| fubgun-es-helmet-v2 | ess·bal | - | 대기 |  |  |
| fubgun-phys-bow-v2 | ess·bal | - | 대기 |  |  |
| fubgun-proj-amulet-v2 | ess·bal | - | 대기 |  |  |
| fubgun-quiver-v2 | ess·bal | ess 물리 피해 추가 1~2티어; bal 물리 피해 추가 1티어 | 대기 |  |  |
| grasping-mail-spell1-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 접미 하나 1~2티어, 마지막 접두·접미 랜덤 — 613 → 24,496(분열 베이스 카오스 22만 개 포함) |
| helmet-armour-sl-v2 | ess·bal·high | high 1티어, bal 1~2티어, ess 1~4티어(빛의 징조 없음), bal·ess 마지막 접두·접미 랜덤 | 완료 11-12 | A(Opus) | 723/83/60 |
| icesly-budget-wand-v2 | ess·bal | ess 번개 주문 레벨 1~2티어; ess 번개·주문 피해 1~5티어; bal 번개 주문 레벨 1티어; bal 번개·주문 피해 1~3티어 | 대기 |  |  |
| lilbotq-armour-shield-v2 | ess·bal | ess 방어도 % 1~2티어; ess 방어도 % + 기절 한계치 1~3티어; bal 방어도 % 1티어; bal 방어도 % + 기절 한계치 1티어 | 대기 |  |  |
| lilbotq-boots-v2 | ess·bal | - | 대기 |  |  |
| lilbotq-budget-boots-v2 | ess·bal | ess 이동 속도 1~2티어; ess 냉기 저항 1~3티어; bal 이동 속도 1티어; bal 냉기 저항 1티어 | 대기 |  |  |
| lilbotq-emerald-v2 | bal | - | 대기 |  |  |
| mastert-timelost-emerald-v2 | bal·high | 주얼이라 티어 없음, high 이동 속도 공개 반복 · bal 결과 그대로 | 완료 11-12 | A(Opus) | 459/78 |
| mazbro-bis-chest-v2 | bal·high | - | 대기 |  |  |
| mazbro-caster-amulet-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 시전 속도·마나 1~2티어, 마지막 접두·접미 랜덤 — 428 → 410 |
| mazbro-caster-ring-v2 | ess·bal | ess 옵션 티어 1~3티어 | 대기 |  |  |
| mazbro-proj-gloves-v2 | bal·high | - | 대기 |  |  |
| mazbro-sceptre-v2 | high | - | 대기 |  |  |
| mazbro-spell5-amulet-v2 | bal·high | high 공개 1티어, bal 마지막 접미 랜덤 | 완료 11-12 | A(Opus) | 233/201 |
| mirror-bow-video-v2 | high | - | 완료 11-12 | A(Opus) 하이엔드만(극한), 바꿀 것 없음 |
| noble-timelost-sapphire-v2 | bal·high | 주얼이라 티어 없음 | 완료 11-12 | A(Opus) | 변경 없음 |
| noble-visceral-quiver-v2 | bal·high | bal 치명타 피해 1~3티어; high 치명타 피해 1~2티어 | 완료 11-12 | A(Opus) | 하이엔드 모두 1티어(영상 '치피 1티'), 밸런스 1~2티어·마지막 접두·접미 랜덤 — 110 → 110 |
| ragna-ashot-bow-v2 | ess·bal | ess 물리 피해 % 1~3티어; bal 물리 피해 % 1티어 | 대기 |  |  |
| ragna-spell4-amulet-v2 | ess·bal | bal 1~2티어(영상), ess 결과 그대로·빛 없음 | 완료 11-12 | A(Opus) | 이미 맞음 |
| sane-resist-belt-v2 | ess·bal | ess 생명력 1~3티어; ess 번개 저항 1~3티어; bal 생명력 1티어 | 대기 |  |  |
| saveq-absent-amulet-v2 | ess·bal·high | - | 완료 11-12 | A(Opus) | 에센셜 빛의 징조 없이 공개 한 번(랜덤 옵션) — 729 → 688 |
| saveq-alloy-focus-v2 | ess·bal | ess 공개 목표 1~3티어; bal 공개 목표 1티어 | 대기 |  |  |
| saveq-focus-v2 | bal·high | 에너지 보호막·주문 치명타 high 1티어, bal 1~2티어 | 완료 11-12 | A(Opus) | 504/208 |
| seek-cyclone-boots-v2 | ess·bal | - | 대기 |  |  |
| sihan-attack-flat-ring-v2 | ess·bal | ess 원소 공격 추가 피해 1~3티어 | 대기 |  |  |
| sihan-chayula-amulet-v2 | ess·bal | ess 정신력 1~2티어; bal 정신력 1티어 | 대기 |  |  |
| sihan-chayula-gloves-v2 | ess·bal | - | 대기 |  |  |
| sihan-chayula-helmet-v2 | ess·bal | ess 튕겨내기 평점 1~3티어; ess 방어 접두 1~3티어; bal 방어 접두 1~3티어 | 대기 |  |  |
| sihan-chayula-ring-v2 | bal·high | high 1티어, bal 1~2티어, 마지막 두 옵션은 원하는 옵션이 없어 둘 다 랜덤 | 완료 11-12 | A(Opus) | 356/130 |
| sihan-chayula-sceptre-v2 | ess·bal | ess 접근 효과 범위 1~2티어; ess 정신력 % + 마나 1~6티어; bal 접근 효과 범위 1티어; bal 정신력 % + 마나 1~4티어 | 대기 |  |  |
| sihan-chayula-wand-v2 | ess·bal | ess 주문 치명타 명중 확률 1~3티어 | 대기 |  |  |
| sihan-highend-boots-v2 | ess·bal·high | ess 저항 목표 1~2티어; ess 훼손 접두 목표 1~3티어 | 완료 11-12 | A(Opus) | 밸런스 접두 1~2티어, 마지막 접두·접미 랜덤. 에센셜은 밸런스와 같아(265/266) 뺌 — 난이도 4로 올려 하이엔드·밸런스 레시피 둘 다(사용자 확정 11-12) |
| sihan-highend-helmet-v2 | bal·high | high 저항 1~3티어 (상위 카오스) | 완료 11-12 | A(Opus) | 밸런스 방어도 1~2티어, 마지막 접미(저항) 랜덤 — 181 → 202 |
| sihan-proj-gloves-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 1~2티어, 마지막 훼손 접두 랜덤 — 327 → 282 |
| sl-5mod-jewel-v2 | ess·bal | - | 대기 |  |  |
| sl-blacksteel-gauntlets-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 두번째 접미도 1~2티어 반복(상위 카오스), 마지막 접두·접미 랜덤 — 140 → 874 |
| sl-flamewave-ring-v2 | bal·high | - | 완료 11-12 | A(Opus) | 이미 기준대로(저항 1~2티어, 마지막 접미 랜덤, 훼손 핵심 옵션은 반복) — 371 그대로 |
| sl-flamewave-staff-v2 | bal·high | - | 완료 11-12 | A(Opus) | 밸런스 접두 반복 1~2티어, 마지막 접두·접미 랜덤 — 178 → 40 |
| sl-proj7-gloves-v2 | bal·high | - | 대기 |  |  |
| tankjung-kitava-shield-v2 | ess·bal·high | high 1티어(영상), bal 1~2티어, ess 최대 저항 1~3티어·방어도 1~4티어 | 완료 11-12 | A(Opus) | 358/125/58, 난이도 4로 올림(사용자 11-12) → high·bal 표시 |
| unstoppable-slipstrike-vest-v2 | bal·high | bal 굴절 1~4티어; high 굴절 1~3티어 | 완료 11-12 | A(Opus) 하이엔드 굴절 1~3 → 1티어(651 → 1,368), 밸런스 1~2티어 + 마지막 접미 랜덤(176 → 74) |
| unstoppable-vile-robe-v2 | bal·high | bal 접두 에너지 보호막·정신력 1티어; bal 저항 1티어 | 완료 11-12 | A(Opus) 밸런스 접두(엑잘·훼손 반복) 1 → 1~2티어(163 → 99), 저항은 싼 반복이라 1티어 유지 |
| vodnarg-timelost-emerald-v2 | ess·bal | - | 대기 |  |  |
| xeno-phys-crossbow-v2 | high | - | 완료 11-12 | A(Opus) 하이엔드만(극한), 바꿀 것 없음 |
| zenm-timelost-sapphire-v2 | ess·bal | - | 대기 |  |  |
