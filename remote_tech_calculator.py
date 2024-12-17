import math

# WIP, mostly for my own testing

Gm = 10 ** 9
Mm = 10 ** 6
Km = 10 ** 3

# Your input:

YOUR_OMNI_ANTENNA_POWERS = [
    # 0.5 * Mm, # DP-10
    # 0.5 * Mm, # You can add multiple antennas =)
    1.5 * Mm, # CO-15 Communotron 16-S
]
CURRENT_DSN_LEVEL = 2

# Stock game defaults, I'd recommend using them:
TRACKING_STATION_POWERS = [
    2 * Gm,
    50 * Gm,
    250 * Gm,
]
# Defaults for Remote tech: 
# TRACKING_STATION_POWERS = [
#     4 * Mm,
#     30 * Mm,
#     75 * Mm,
# ]

OMNI_COMBINE_COEF = 0.5

# ------------------------------------------

dsn_power = TRACKING_STATION_POWERS[CURRENT_DSN_LEVEL - 1]

print(f"Tracking station power: {dsn_power / Mm} Mm")

omni_power = sum(YOUR_OMNI_ANTENNA_POWERS) * OMNI_COMBINE_COEF + max(YOUR_OMNI_ANTENNA_POWERS) * (1 - OMNI_COMBINE_COEF)

print(f"Omni power: {omni_power / Mm} Mm")

max_range = min(min(min(dsn_power, omni_power) + math.sqrt(omni_power * dsn_power), dsn_power * 100), omni_power * 100)

print(f"Max omni-range: {max_range / Mm} Mm")
