from itertools import product, combinations

from dlprintopt.enums import PrintType, PrintParameter, StatusParameter
from dlprintopt.model import Wyrmprint, PrintComp

prints_r5: dict[str, Wyrmprint] = {
    "POISON_30": Wyrmprint(
        name="POISON_30", type=PrintType.R5,
        effect_param=PrintParameter.PUNISHER_POISON, effect_rate=0.3
    ),
    "BK_30": Wyrmprint(
        name="BK_30", type=PrintType.R5,
        effect_param=PrintParameter.PUNISHER_BK, effect_rate=0.3
    ),
    "SD_40": Wyrmprint(
        name="SD_40", type=PrintType.R5,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4
    ),
}

prints_r4: dict[str, Wyrmprint] = {
    "POISON_25": Wyrmprint(
        name="POISON_25", type=PrintType.R4,
        effect_param=PrintParameter.PUNISHER_POISON, effect_rate=0.25
    ),
    "BK_25": Wyrmprint(
        name="BK_25", type=PrintType.R5,
        effect_param=PrintParameter.PUNISHER_BK, effect_rate=0.25
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
    "ENMITY": Wyrmprint(
        name="ENMITY", type=PrintType.SINDOM,
        effect_param=PrintParameter.ENMITY, effect_rate=0.6,
    ),
}

additional_base: dict[StatusParameter, float] = {
    StatusParameter.ATK_PASSIVE: 0.7,
    StatusParameter.PUNISHER: 0.3
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

        most_effective = max(comps, key=lambda comp: comp.get_prints_effectiveness(additional_base))
        most_effective.report_effectiveness(additional_base)
        print()


def check_partial_count():
    counts: list[tuple[int, int, int]] = [
        (2, 0, 2),
        (1, 1, 2)
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

        most_effective = max(comps, key=lambda comp: comp.get_prints_effectiveness(additional_base))
        most_effective.report_effectiveness(additional_base)
        print()


def check_full():
    r5_count = 2
    r4_count = 0
    sindom_count = 2

    r5_combinations = combinations(prints_r5.values(), r5_count)
    r4_combinations = combinations(prints_r4.values(), r4_count)
    sindom_combinations = combinations(prints_sindom.values(), sindom_count)

    comps = [
        PrintComp(prints=r5_picked + r4_picked + sindom_picked)
        for r5_picked, r4_picked, sindom_picked in product(r5_combinations, r4_combinations, sindom_combinations)
    ]

    for comp in sorted(comps, key=lambda comp: comp.get_prints_effectiveness(additional_base), reverse=True):
        comp.report_effectiveness(additional_base)
        print()


if __name__ == '__main__':
    check_partial_count()
