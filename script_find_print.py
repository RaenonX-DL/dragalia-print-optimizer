from itertools import product, combinations

from dlprintopt.enums import Affinity, PrintType, PrintParameter, StatusParameter
from dlprintopt.model import Wyrmprint, PrintComp

prints_r5: dict[str, Wyrmprint] = {
    "FS_50": Wyrmprint(
        name="FS_50", type=PrintType.R5,
        effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=0.5,
        affinity_type=Affinity.FS
    ),
    "SD_40": Wyrmprint(
        name="SD_40", type=PrintType.R5,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4
    ),
    "ATK_20": Wyrmprint(
        name="ATK_20", type=PrintType.R5,
        effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2,
        affinity_type=Affinity.FS
    )
}

prints_r4: dict[str, Wyrmprint] = {
    "FS_40": Wyrmprint(
        name="FS_40", type=PrintType.R4,
        effect_param=PrintParameter.FS_DMG_PRINT, effect_rate=0.4,
        affinity_type=Affinity.FS
    ),
    "ATK_10": Wyrmprint(
        name="ATK_10", type=PrintType.R4,
        effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.1,
        affinity_type=Affinity.ATK
    ),
    "SD_20": Wyrmprint(
        name="SD_20", type=PrintType.R4,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2,
        affinity_type=Affinity.ATK,
    ),
    "CRT_12": Wyrmprint(
        name="CRT_12", type=PrintType.R4,
        effect_param=PrintParameter.CRT_RATE, effect_rate=0.12
    ),
    "CDMG_17": Wyrmprint(
        name="CDMG_17", type=PrintType.R4,
        effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.17,
        affinity_type=Affinity.ATK
    )
}

prints_sindom: dict[str, Wyrmprint] = {
    "SINDOM_ATK": Wyrmprint(
        name="SINDOM_ATK", type=PrintType.SINDOM,
        enables_affinity=Affinity.ATK,
    ),
    "SINDOM_FS": Wyrmprint(
        name="SINDOM_FS", type=PrintType.SINDOM,
        enables_affinity=Affinity.FS,
    ),
    "SINDOM_SD_20": Wyrmprint(
        name="SINDOM_SD_20", type=PrintType.SINDOM,
        effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2,
    ),
}


def main():
    additional_base: dict[StatusParameter, float] = {
        StatusParameter.ATK_PASSIVE: 0.7
    }

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


if __name__ == '__main__':
    main()
