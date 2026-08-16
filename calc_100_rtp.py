# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
# Total outcomes per line: 5^4 = 625
# 4-match: 1 outcome
# 3-match: 8 outcomes (4 for [0..2], 4 for [1..3])

# Target: Sum(m4 + 8 * m3) = 625 exactly (RTP = 100.00%)

options = [
    {
        "title": "옵션 1 (균형 상향형 - 모든 심볼의 배당을 골고루 소폭 상향)",
        "payouts": {
            "🎰 메가 잭팟": (22, 100),  # 100 + 8*22 = 276
            "👑 왕관": (13, 50),        # 50 + 8*13 = 154
            "💎 보석": (9, 32),         # 32 + 8*9  = 104
            "🔔 황금종": (5, 16),       # 16 + 8*5  = 56
            "🍒 체리": (3, 11),         # 11 + 8*3  = 35
        }
    },
    {
        "title": "옵션 2 (잭팟 대박형 - 4개 일치 잭팟 배당을 대폭 강화)",
        "payouts": {
            "🎰 메가 잭팟": (20, 125),  # 125 + 8*20 = 285
            "👑 왕관": (12, 60),        # 60 + 8*12  = 156
            "💎 보석": (8, 35),         # 35 + 8*8   = 99
            "🔔 황금종": (5, 20),       # 20 + 8*5   = 60
            "🍒 체리": (2.5, 5),        # 5 + 8*2.5  = 25
        }
    },
    {
        "title": "옵션 3 (정수 배당 최적화형 - 소수점 없이 깔끔한 자연수 배당)",
        "payouts": {
            "🎰 메가 잭팟": (22, 105),  # 105 + 8*22 = 281
            "👑 왕관": (12, 55),        # 55 + 8*12  = 151
            "💎 보석": (8, 35),         # 35 + 8*8   = 99
            "🔔 황금종": (5, 18),       # 18 + 8*5   = 58
            "🍒 체리": (3, 12),         # 12 + 8*3   = 36
        }
    }
]

for opt in options:
    print(f"=== {opt['title']} ===")
    total_numerator = 0
    for sym, (m3, m4) in opt['payouts'].items():
        contrib = m4 + 8 * m3
        total_numerator += contrib
        print(f"  {sym}: 3개 일치 {m3}배 | 4개 일치 {m4}배 => 기댓값 기여도 {contrib}/625")
    rtp = (total_numerator / 625) * 100
    print(f"  => 총 분자 합: {total_numerator}/625 | 기대 환수율(RTP): {rtp:.2f}%\n")
