from itertools import product, combinations

from dlprintopt.enums import PrintType, PrintParameter, StatusParameter, DamageType, Affinity, DamageOnStatus
from dlprintopt.model import CalcParams, Wyrmprint, PrintComp, Effect

prints_r5: dict[str, Wyrmprint] = {
    "ATK_20": Wyrmprint(
        name="ATK_20", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2)]
    ),
    "SD_40": Wyrmprint(
        name="SD_40", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4)]
    ),
    "CRT_12_R5": Wyrmprint(
        name="CRT_12", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.12)],
        affinity_type=Affinity.ATK,
    ),
    "CDMG_22": Wyrmprint(
        name="CDMG_22", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.22)]
    ),
    "PUN_30": Wyrmprint(
        name="PUN_30", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.PUNISHER_POISON, effect_rate=0.3)]
    ),
    "PUN_25": Wyrmprint(
        name="PUN_25", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.PUNISHER_SHADOWBLIGHT, effect_rate=0.25)]
    ),
    "DDMG_18": Wyrmprint(
        name="DDMG_18", type=PrintType.R5,
        effects=[Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18)]
    ),
}

prints_r4: dict[str, Wyrmprint] = {
    "SD_20": Wyrmprint(
        name="SD_20", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)],
        affinity_type=Affinity.ATK,
    ),
    "SD_20_2": Wyrmprint(
        name="SD_20_2", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)]
    ),
    "CRT_12": Wyrmprint(
        name="CRT_12", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.12)],
        affinity_type=Affinity.ATK,
    ),
    "CDMG_15": Wyrmprint(
        name="CDMG_15", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15)]
    ),
    "DDMG_14": Wyrmprint(
        name="DDMG_14", type=PrintType.R4,
        effects=[Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.14)]
    ),
}

prints_sindom: dict[str, Wyrmprint] = {
    "SINDOM_SD_20": Wyrmprint(
        name="SINDOM_SD_20", type=PrintType.SINDOM,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)],
    ),
    "SINDOM_SD_20_2": Wyrmprint(
        name="SINDOM_SD_20_2", type=PrintType.SINDOM,
        effects=[Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.2)],
    ),
    "SINDOM_CRT_4": Wyrmprint(
        name="SINDOM_CRT_4", type=PrintType.SINDOM,
        effects=[Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.04)],
    ),
    "SINDOM_BOON": Wyrmprint(
        name="SINDOM_BOON", type=PrintType.SINDOM,
        effects=[Effect(enables_affinity=Affinity.ATK)]
    ),
    "SINDOM_BOON_TRG": Wyrmprint(
        name="SINDOM_BOON_TRG", type=PrintType.SINDOM,
        effects=[],
        affinity_type=Affinity.ATK
    ),
}

prints_kaleido: dict[str, Wyrmprint] = {
    "KLD_SD_ATK": Wyrmprint(
        name="KLD_SD_ATK", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.SKILL_DMG, effect_rate=0.4),
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
        ],
    ),
    "KLD_ATK_CDMG": Wyrmprint(
        name="KLD_ATK_CDMG", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KLD_CRT_CDMG": Wyrmprint(
        name="KLD_CRT_CDMG", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.15),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    # "KLD_CRT_ATK": Wyrmprint(
    #     name="KLD_CRT_ATK", type=PrintType.KALEIDO,
    #     effects=[
    #         Effect(effect_param=PrintParameter.CRT_RATE, effect_rate=0.15),
    #         Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
    #     ],
    # ),
    "KLD_DDMG_CDMG": Wyrmprint(
        name="KLD_DDMG_CDMG", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18),
            Effect(effect_param=PrintParameter.CRT_DAMAGE, effect_rate=0.15),
        ],
    ),
    "KLD_DDMG_ATK": Wyrmprint(
        name="KLD_DDMG_ATK", type=PrintType.KALEIDO,
        effects=[
            Effect(effect_param=PrintParameter.DRAGON_DAMAGE, effect_rate=0.18),
            Effect(effect_param=PrintParameter.ATK_PASSIVE_PRINT, effect_rate=0.2),
        ],
    ),
}

additional_base: dict[StatusParameter, float] = {
    StatusParameter.ATK_PASSIVE: 1.2 + 0.1,
    StatusParameter.SKILL_DMG: 0.4,
    StatusParameter.CRT_RATE: 0.02
}

damage_distribution: dict[DamageType, float] = {
    DamageType.NORMAL: 0.394127,
    DamageType.SKILL: 0.227061 + 0.191722,  # S1 + S2
    DamageType.FS: 0,
    DamageType.DRAGON: 0.1209,
    DamageType.DRAGON_SKILL: 0.06619,
}

damage_status_distribution: dict[DamageOnStatus, float] = {
    DamageOnStatus.PRE_OD: 0,
    DamageOnStatus.OD: 0.5,
    DamageOnStatus.BK: 0.5
}

params: CalcParams = CalcParams(
    additional_base=additional_base,
    damage_distribution=damage_distribution,
    damage_status_distribution=damage_status_distribution,
)


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
        most_effective.report_effectiveness(params)
        print()


def check_partial_count():
    # R5 / R4 / KLD / SINDOM
    counts: list[tuple[int, int, int, int]] = [
        (3, 2, 1, 2),
        (2, 2, 1, 2),
        (3, 1, 1, 2),
    ]

    for r5_count, r4_count, kld_count, sindom_count in counts:
        print(f"--- R5 x {r5_count} / R4 x {r4_count} / KLD x {kld_count} / Sindom x {sindom_count} ---")
        r5_combinations = combinations(prints_r5.values(), r5_count)
        r4_combinations = combinations(prints_r4.values(), r4_count)
        kaleido_combinations = combinations(prints_kaleido.values(), kld_count)
        sindom_combinations = combinations(prints_sindom.values(), sindom_count)

        comps = [
            PrintComp(prints=r5_picked + r4_picked + kaleido_picked + sindom_picked)
            for r5_picked, r4_picked, kaleido_picked, sindom_picked
            in product(r5_combinations, r4_combinations, kaleido_combinations, sindom_combinations)
        ]

        most_effective = max(
            comps,
            key=lambda comp: comp.get_prints_effectiveness(params)
        )
        most_effective.report_effectiveness(params)
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
            key=lambda comp: comp.get_prints_effectiveness(params),
            reverse=True
    ):
        comp.report_effectiveness(params)
        print()


if __name__ == '__main__':
    check_partial_count()
