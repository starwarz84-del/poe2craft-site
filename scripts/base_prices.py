# Base price per recipe (Divine Orbs), policy 22 (user, 2026-11-09 15:19): the price of the base the recipe starts from (the "base" step).
# A value said in the video goes here; None = not known yet (the Recipes tab then prices the base at 0 unless the viewer types one,
# and the price tier leaves it out). For a fractured start this is the fractured base, not the prep (the prep has its own cost).
# build_recipes.py copies it to recipe.basePrice.
BASEPRICE = {
  'mazbro-caster-amulet-v2': 5, 'mazbro-caster-amulet-v2-bal': 5,   # 영상 2:30: 정신력 50 태양 목걸이 약 5 div
  'noble-timelost-sapphire-v2': 1, 'noble-timelost-sapphire-v2-bal': 1,   # 영상 1:38 매직 1 div
  'mirror-bow-video': None,
  'mirror-bow-video-v2': 35,   # 영상 7:30: 퀄리티 30% 전쟁광 활 30~40 div(사용자 확정 11-13: 특출난 그대로, 35 div)
  'absent-amulet-video': None,
  'breach-ring-video': None,
  'helmet-armour-sl': None,
  'gold-amulet-6line': None,
  'grasping-mail-spell1': None,
  'absent-amulet-spell6': None,
  'mazbro-caster-ring': None,
  'mazbro-caster-ring-v2-bal': 2, 'mazbro-caster-ring-v2-ess': 2,   # 2026-11-13 G2: 영상 4:00 '보통 2 div 이하' 시전 속도 기억 반지(분열 전 베이스, 분열 실패로 평균 3개)
  'mazbro-caster-amulet': None,
  'mazbro-bis-chest': None,
  'mazbro-bis-chest-v2': 0.11,   # 영상 2:30·2:50: 노멀 요술사 외투 약 카오스 오브 1개(40.4 ex ÷ 363 ≈ 0.11 div)
  'mazbro-proj-gloves': None,
  'mazbro-proj-gloves-v2': 12, 'mazbro-proj-gloves-v2-bal': 12,   # 영상 2:50 화면 노트 '24 Gloves x 12 Divs' — 특출난 검은강철 건틀릿 장당 12디바인(플로우차트는 노멀 베이스부터 준비)
  'diztoh-twister-spear': None,
  'diztoh-iceshot-bow': None,
  'diztoh-budget-mace': None,
  'diztoh-crit-helmet-v2': 0.9,   # 사용자 흐름: 특출난 웃는 가면 약 8 카오스 오브(카오스 40.4 ex × 8 ÷ 363 ≈ 0.9 div)
  'diztoh-crit-helmet-v2-bal': 0.9,
  'diztoh-crit-helmet-v2-ess': 0.9,
  'diztoh-5mod-sapphire': None,
  'ragna-spell4-amulet': None,
  'breach-ring-phys': None,
  'ragna-ashot-bow': None,
  'barricade-quarterstaff': None,
  'belton-plus8-wand': None,
  'belton-plus8-wand-v2-bal': 61, 'belton-plus8-wand-v2-ess': 61,   # 2026-11-13 G7: 영상 0:30 '61 디바인에 샀다' — 모든 주문 +4 매직 결투 마법봉(아이템 레벨 82, 퀄리티 21%)
  'chiba-timelost-emerald': None,
  'chiba-timelost-emerald-v2': 14,   # 영상 4:05: 공격 치명타 확률 + 옵션 2개 레어 14 div
  'diztoh-5mod-emerald': None,
  'diztoh-as-spear': None,
  'diztoh-budget-2h-mace': None,
  'diztoh-budget-crossbow': None,
  'diztoh-endgame-quarterstaff': None,
  'diztoh-es-helmet': None,
  'diztoh-onehand-mace': 3,   # 영상: 퀄리티 20% 노멀 베이스 3디바인
  'diztoh-rarity-ring': 1,
  'diztoh-rarity-ring-v2': None, 'diztoh-rarity-ring-v2-bal': 1, 'diztoh-rarity-ring-v2-ess': 1,   # 영상: 매직 황금 반지 1디바인 안팎(하이엔드 1티어·1티어 매직은 시세 모름)
  'diztoh-socket-gloves': None,
  'diztoh-talisman': None,
  'diztoh-vile-robe': None,
  'farmer-budget-armour': None,
  'farmer-starter-staff': None,
  'farmer-budget-armour-v2': None,
  'ragna-ashot-bow-v2-bal': None, 'ragna-ashot-bow-v2-ess': 10,   # 2026-11-13 G13: 영상 1:30 자막 '8딥, 10딥, 15딥 정도'(물리 % 매직 활 거래소 가격, 화면 1:40 매물은 5티어 절멸자 활 8 div) — 가운데 10 div
  'sane-resist-belt-v2-bal': None, 'sane-resist-belt-v2-ess': None,
  'diztoh-budget-mace-v2-bal': None, 'diztoh-budget-mace-v2-ess': None,
  'lilbotq-budget-boots-v2-bal': None, 'lilbotq-budget-boots-v2-ess': None,
  'icesly-budget-wand-v2-bal': 13, 'icesly-budget-wand-v2-ess': 13,   # 2026-11-13 G12: 영상 1:18 거래소 번개 +5 매직 결투 마법봉(아이템 레벨 81) 13 div, 1:42에 그 마법봉
  'farmer-starter-staff-v2': 0.11, 'farmer-starter-staff-v2-bal': 0.11, 'farmer-starter-staff-v2-ess': 0.11,   # 사용자 2026-11-10 거래소: 번개 주문 +6 매직 지팡이 카오스 오브 1개(≈0.11 div)
  'icesly-budget-wand': None,
  'lilbotq-armour-shield': None,
  'lilbotq-budget-boots': None,
  'lilbotq-boots': None,
  'lilbotq-emerald': None,
  'lilbotq-emerald-v2-bal': 2.5,   # 2026-11-13 G9: 영상 15:00 '하나에 2~3 div' 좋은 접미 2개 에메랄드
  'mastert-timelost-emerald': None,
  'mastert-timelost-emerald-v2': 94, 'mastert-timelost-emerald-v2-bal': 94,   # 영상 매물 93~95 div(공격 치명타 확률 분열 오래된 에메랄드)
  'mazbro-sceptre': None,
  'mazbro-spell5-amulet': None,
  'noble-timelost-sapphire': None,
  'noble-visceral-quiver': None,
  'sane-resist-belt': None,
  'saveq-absent-amulet': None,
  'saveq-absent-amulet-v2': None, 'saveq-absent-amulet-v2-bal': None, 'saveq-absent-amulet-v2-ess': None,
  'saveq-alloy-focus': None,
  'saveq-alloy-focus-v2-bal': 3.5, 'saveq-alloy-focus-v2-ess': 3.5,   # 2026-11-13 G9: 영상 2:20 '4 div 또는 3 div' 에너지 보호막 최대치 3티어 + 모든 주문 +2 매직 집중구
  'saveq-focus': None,
  'unstoppable-vile-robe-v2': 17.5, 'unstoppable-vile-robe-v2-bal': 17.5,   # 영상 1:30·2:30: 아이템 레벨 82 3소켓 끔찍한 로브 15~20 div
  'saveq-focus-v2': 6, 'saveq-focus-v2-bal': 6,   # 영상 6:00: 특출난 타살리안 집중구(아이템 레벨 79+, 2소켓) 5~7 div, 매물 약 6
  'seek-cyclone-boots': None,
  'sihan-chayula-sceptre': None,
  'sihan-highend-boots': None,
  'sihan-highend-boots-v2': None, 'sihan-highend-boots-v2-bal': None, 'sihan-highend-boots-v2-ess': None,
  'sihan-highend-helmet': None,
  'sihan-chayula-amulet': 15,       # 영상 3:08 — 정신력 분열 실패 부재 목걸이 매물 15 div
  'sihan-chayula-amulet-v2-bal': 15, 'sihan-chayula-amulet-v2-ess': 15,
  'sihan-attack-flat-ring-v2-bal': 75, 'sihan-attack-flat-ring-v2-ess': 75,
  'sihan-attack-flat-ring': 75,     # 영상 9:23 — 1티어 플랫 분열 매물 75 div 구입
  'sl-5mod-jewel': None,
  'sl-5mod-jewel-v2-bal': 5, 'sl-5mod-jewel-v2-ess': 5,   # 영상 3:40 자막 — 상태 이상 가속 7% 사파이어 매물 5 div부터
  'sl-flamewave-ring': None,
  'sl-flamewave-staff': None,
  'sl-proj7-gloves': None,
  'tankjung-kitava-shield': None,
  'vodnarg-timelost-emerald': None,
  'vodnarg-timelost-emerald-v2-bal': 3, 'vodnarg-timelost-emerald-v2-ess': 3,   # 영상 4:50 자막 — 접미 2개 주얼 베이스 약 3 div
  'xeno-phys-crossbow': None,
  'zenm-timelost-sapphire': None,
}
