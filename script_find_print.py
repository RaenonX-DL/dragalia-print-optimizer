from itertools import product, combinations

from dlprintopt.enums import PrintType, PrintParameter, StatusParameter, DamageType
from dlprintopt.model import Wyrmprint, PrintComp

prints_r5: dict[str, Wyrmprint] = {
    "ATK_20": Wyrmprint(
        name="ATK_20", type=PrintType.R5,
        effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2
    ),
    "SD_40": Wyrmprint(
        name="SD_40", type=PrintType.R5,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4
    ),
    "CRT_10": Wyrmprint(
        name="CRT_10", type=PrintType.R5,
        effect_param=PrintParameter.CRT_RATE, effect_rate=0.1
    ),
    "CDMG_22": Wyrmprint(
        name="CDMG_22", type=PrintType.R5,
        effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.22
    ),
    "PUN_BURN": Wyrmprint(
        name="PUN_BURN", type=PrintType.R5,
        effect_param=PrintParameter.PUNISHER_BURN, effect_rate=0.3
    ),
    "PUN_SCORCH": Wyrmprint(
        name="PUN_SCORCH", type=PrintType.R5,
        effect_param=PrintParameter.PUNISHER_SCORCHREND, effect_rate=0.25
    ),
    "DDMG": Wyrmprint(
        name="DDMG", type=PrintType.R5,
        effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18
    ),
}

prints_r4: dict[str, Wyrmprint] = {
    "SD_20": Wyrmprint(
        name="SD_20", type=PrintType.R4,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2
    ),
    "SD_20_2": Wyrmprint(
        name="SD_20_2", type=PrintType.R4,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2
    ),
    "CRT": Wyrmprint(
        name="CRT", type=PrintType.R4,
        effect_param=PrintParameter.CRT_RATE, effect_rate=0.12
    ),
    "CDMG": Wyrmprint(
        name="CDMG", type=PrintType.R4,
        effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15
    ),
    "DDMG": Wyrmprint(
        name="DDMG", type=PrintType.R4,
        effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.14
    ),
}

prints_sindom: dict[str, Wyrmprint] = {
    "SINDOM_SD_20": Wyrmprint(
        name="SINDOM_SD_20", type=PrintType.SINDOM,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2,
    ),
    "SINDOM_SD_20_2": Wyrmprint(
        name="SINDOM_SD_20_2", type=PrintType.SINDOM,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2,
    ),
}

additional_base: dict[StatusParameter, float] = {
    StatusParameter.ATK_PASSIVE: 0.9,
    StatusParameter.CRT_RATE: 0.02,
    StatusParameter.PUNISHER: 0.1
}

damage_distribution: dict[DamageType, float] = {
    DamageType.SKILL: 0.5,
    DamageType.FS: 0,
    DamageType.DRAGON: 0.5,
}


def check_all_count():
    for r5_count, r4_count, sindom_count in product([1, 2, 3], [1, 2], [1, 2]):
        print(f"--- R5 x {r5_count} / R4 x {r4_count} / Sindom x {sindom_count} ---")
        r5_combinations = combinations(prints_r5.values(), r5_count)
        r4_combinations = combinations(prints_r4.values(), r4_count)
        sindom_combinations = combinations(prints_sindom.values(), sindom_count)

        comps = [
            PrintComp(prints=r5_picked + r4_picked + sindom_picked)
            for r5_picked, r4_picked, sindom_picked in product(r5_combinations, r4_combinations, sindom_combinations)
        ]

        most_effective = max(
            comps,
            key=lambda comp: comp.get_prints_effectiveness(additional_base, damage_distribution)
        )
        most_effective.report_effectiveness(additional_base, damage_distribution)
        print()


def check_partial_count():
    counts: list[tuple[int, int, int]] = [
        (3, 2, 2),
    ]

    for r5_count, r4_count, sindom_count in counts:
        print(f"--- R5 x {r5_count} / R4 x {r4_count} / Sindom x {sindom_count} ---")
        r5_combinations = combinations(prints_r5.values(), r5_count)
        r4_combinations = combinations(prints_r4.values(), r4_count)
        sindom_combinations = combinations(prints_sindom.values(), sindom_count)

        comps = [
            PrintComp(prints=r5_picked + r4_picked + sindom_picked)
            for r5_picked, r4_picked, sindom_picked in product(r5_combinations, r4_combinations, sindom_combinations)
        ]

        most_effective = max(
            comps,
            key=lambda comp: comp.get_prints_effectiveness(additional_base, damage_distribution)
        )
        most_effective.report_effectiveness(additional_base, damage_distribution)
        print()


def check_full():
    r5_count = 3
    r4_count = 2
    sindom_count = 2

    r5_combinations = combinations(prints_r5.values(), r5_count)
    r4_combinations = combinations(prints_r4.values(), r4_count)
    sindom_combinations = combinations(prints_sindom.values(), sindom_count)

    comps = [
        PrintComp(prints=r5_picked + r4_picked + sindom_picked)
        for r5_picked, r4_picked, sindom_picked in product(r5_combinations, r4_combinations, sindom_combinations)
    ]

    for comp in sorted(
            comps,
            key=lambda comp: comp.get_prints_effectiveness(additional_base, damage_distribution),
            reverse=True
    ):
        comp.report_effectiveness(additional_base, damage_distribution)
        print()


if __name__ == '__main__':
    # PrintComp(prints=[
    #     prints_r5["ATK_20"],
    #     prints_r5["SD_40"],
    #     prints_r5["DDMG"],
    #     prints_r4["SD_20"],
    #     prints_r4["SD_20_2"],
    #     prints_sindom["SINDOM_SD_20"],
    #     prints_sindom["SINDOM_SD_20_2"]
    # ]).get_prints_effectiveness(additional_base, damage_distribution)
    check_partial_count()
