# 플로우차트 영상 대조 점검표

사용자 확정(2026-11-11 21:34): 등록된 모든 아이템 레시피를 영상과 대조해 고침. 서비스는 결국 이 솔루션이 얼마나 믿을 만하게 돌아가는지가 중요함. 두 세션(A = Opus, B = Fable)이 겹치지 않게 이 표로 나눠요.

규칙

- 시작하기 전에 `git pull` → 그 줄의 상태를 '진행 중'과 세션 이름으로 바꿔 바로 커밋·푸시해요. 남이 '진행 중'인 줄은 건드리지 않아요.
- 끝나면 '완료' + 날짜 + 한 줄 결과(바꾼 곳, 시뮬 비용 전·후). 자세한 기록은 `docs/recipe-notes.md`.
- 점검 순서: 영상(자막 + 화면) → 플로우차트 단계마다 영상 시점 확인 → 영상에 없는 단계·비싼 징조 반복 정리(더 싼 길은 시뮬로 확인 뒤 고침, 정책 0장 3번) → 들어오는 선·숨긴 선 → 등급(비싼 반복 구간에서 티어 낮추기) → 시뮬 → 레시피 화면 확인.
- 검사 도구: `python3 tools/test/fcaudit.py`(전수), `python3 tools/test/fc_noinput.py`(들어오는 선).

| 플로우차트 | 영상 | 등급 비용(div, 점검 전) | 검사 문제 | 상태 | 세션 | 메모 |
|---|---|---|---|---|---|---|
| mirror-bow-video-v2 | J0LF3MRssh0 | high 9,035 | 6 | 진행 중 | A(Opus) |  |
| banzino-mirror-staff-v2 | vT482uJFESs | high 7,754, bal 4,686 | 5 | 진행 중 | A(Opus) |  |
| xeno-phys-crossbow-v2 | 1TP4aGqxU7Q | high 7,227 | 7 | 진행 중 | A(Opus) |  |
| barricade-quarterstaff-v2 | B4yShuKydt0 | high 4,068, bal 387 | 2 | 진행 중 | A(Opus) |  |
| mazbro-bis-chest-v2 | LUB59xlkNtk | high 3,023, bal 960 | 15 | 대기 |  |  |
| sihan-highend-helmet-v2 | CTrIbhQVU8U | high 2,616, bal 180 | 1 | 대기 |  |  |
| noble-visceral-quiver-v2 | 2PUEwoePtRs | high 2,240, bal 110 | 3 | 대기 |  |  |
| diztoh-iceshot-bow-v2 | 29vO0mMUoME | high 1,999, bal 1,058 | 5 | 완료 | B(Fable) | 영상에 없는 단계 되돌림 |
| breach-ring-video-v2 | RiJixgqBnBY | high 1,956, bal 934 | 4 | 대기 |  |  |
| sihan-proj-gloves-v2 | DH4jiORLg10 | high 1,659, bal 327 | 2 | 대기 |  |  |
| sl-blacksteel-gauntlets-v2 | J7J8Jo7ibvE | high 1,649, bal 140 | 4 | 대기 |  |  |
| sl-flamewave-ring-v2 | UAF91gEFRkM | high 1,423, bal 371 | 2 | 대기 |  |  |
| absent-amulet-spell6-v2 | Yi1u0LhJztI | high 1,330, bal 756 | 10 | 대기 |  |  |
| sl-flamewave-staff-v2 | 6EzSVUItzsg | high 1,296, bal 178 | 3 | 대기 |  |  |
| mazbro-caster-amulet-v2 | 4PazhuHwdL8 | high 1,154, bal 428 | 5 | 대기 |  |  |
| sihan-highend-boots-v2 | dlrD21AcCUE | high 1,147, bal 650, ess 314 | 2 | 대기 |  |  |
| grasping-mail-spell1-v2 | y5Ch3AJpl5c | high 1,140, bal 613 | 11 | 대기 |  |  |
| sl-proj7-gloves-v2 | XMYJh3CnXuY | high 1,104, bal 785 | 7 | 완료 | B(Fable) | 영상 대조 |
| saveq-absent-amulet-v2 | S4sflKbsA8A | high 935, bal 797, ess 729 | 4 | 대기 |  |  |
| unstoppable-vile-robe-v2 | swF5mwXmZ0k | high 739, bal 689 | 4 | 완료 11-11 | A(Opus) | 영상 5:45~24:15 대조. 접미는 엑잘+소멸(비싼 징조는 마지막 한 옵션만), 접두 막기·결정화+심연. 하이엔드 739→809, 밸런스(1티어 + 마지막 접미 랜덤) 689→163 |
| helmet-armour-sl-v2 | p0fChSu91uI | high 723, bal 718, ess 75 | 5 | 대기 |  |  |
| diztoh-endgame-quarterstaff-v2 | YfGJyBrObxI | high 712, bal 36 | 3 | 대기 |  |  |
| unstoppable-slipstrike-vest-v2 | swF5mwXmZ0k | high 651, bal 176 | 1 | 완료 11-11 | A(Opus) | 영상 40:45~46:30 대조. 첫 카오스 추가, 반복은 상위 카오스, 접두 결정화+심연. 하이엔드 870→651, 밸런스 540→176 |
| breach-ring-phys-v2 |  | bal 535, ess 89 | 2 | 대기 |  |  |
| diztoh-crit-helmet-v2 | QuW8BOSpPpo | high 512, bal 340, ess 278 | 1 | 대기 |  |  |
| mazbro-sceptre-v2 | UwzsARlgaFM | high 504 | 10 | 대기 |  |  |
| sihan-chayula-ring-v2 | GgD_vxKgNsw | high 478, bal 144 | 0 | 대기 |  |  |
| mastert-timelost-emerald-v2 | GNNkhSENp6Q | high 469, bal 88 | 1 | 대기 |  |  |
| noble-timelost-sapphire-v2 | zEV8kWwveYQ | high 468, bal 418 | 3 | 대기 |  |  |
| tankjung-kitava-shield-v2 | gQa51XOS98s | bal 359, ess 48 | 2 | 대기 |  |  |
| absent-amulet-video-v2 | jr6-YLMJsC8 | high 356, bal 223 | 8 | 대기 |  |  |
| gold-amulet-6line-v2 | cb36jD9pqsw | high 354, bal 345 | 20 | 대기 |  |  |
| saveq-focus-v2 | R43FVay8_XI | high 343, bal 208 | 5 | 대기 |  |  |
| mazbro-spell5-amulet-v2 | kULlZJBSec4 | high 222, bal 201 | 0 | 대기 |  |  |
| diztoh-rarity-ring-v2 | GDLDxn6yxEs | high 149, bal 20, ess 15 | 1 | 대기 |  |  |
| bigdaddy-lightning-wand-v2 | 글: mobalytics.gg/poe-2/profile/bigdaddygami | bal 146, ess 98 | 2 | 대기 |  |  |
| ragna-spell4-amulet-v2 | Tzpdm8M-Pkk | bal 118, ess 27 | 0 | 대기 |  |  |
| mazbro-proj-gloves-v2 | BIxlixCKPO0 | high 112, bal 66 | 40 | 대기 |  |  |
| fubgun-proj-amulet-v2 | 글: mobalytics.gg/poe-2/builds/ice-shot-dead | bal 110, ess 97 | 3 | 대기 |  |  |
| diztoh-5mod-emerald-v2 | s70CV_nvjXg | bal 108, ess 30 | 0 | 대기 |  |  |
| diztoh-vile-robe-v2 | n97yEuKSWyM | bal 105, ess 51 | 0 | 대기 |  |  |
| sl-5mod-jewel-v2 | VKMT7tuSIYk | bal 104, ess 57 | 0 | 대기 |  |  |
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
